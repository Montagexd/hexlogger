import threading
from enum import Enum

from .themes import Theme, THEMES
from .styles import STYLES

__all__ = ["LogLevel", "LoggerConfig", "get_config", "settheme", "setstyle", "setlog", "setlevel"]


class LogLevel(Enum):
    TRACE = 0
    DEBUG = 1
    INFO = 2
    SUCCESS = 3
    WARNING = 4
    ERROR = 5
    CRITICAL = 6
    FATAL = 7


class LoggerConfig:
    def __init__(self):
        self.theme = THEMES.get("default", Theme("default", {}))
        self.style = "default"
        self.time_format = "%H:%M:%S"
        self.show_time = True
        self.log_file = None
        self.min_level = LogLevel.TRACE
        self._file_handle = None
        self._lock = threading.Lock()

    def set_theme(self, name):
        if name in THEMES:
            self.theme = THEMES[name]
        else:
            raise ValueError(f"Unknown theme: {name}. Available: {', '.join(THEMES.keys())}")

    def set_style(self, name):
        if name in STYLES:
            self.style = name
        else:
            raise ValueError(f"Unknown style: {name}. Available: {', '.join(STYLES.keys())}")

    def add_theme(self, name, colors):
        try:
            theme = Theme(str(name), colors if isinstance(colors, dict) else {})
            THEMES[str(name)] = theme
            return theme
        except Exception:
            raise ValueError(f"Failed to add theme: {name}")

    def set_log_file(self, path):
        try:
            self.log_file = str(path)
            if self._file_handle:
                try:
                    self._file_handle.close()
                except Exception:
                    pass
            self._file_handle = open(self.log_file, "a", encoding="utf-8")
        except Exception:
            self._file_handle = None
            raise

    def close(self):
        if self._file_handle:
            try:
                self._file_handle.close()
            except Exception:
                pass
            self._file_handle = None

    def __del__(self):
        self.close()


_config = LoggerConfig()


def get_config():
    return _config


def settheme(name):
    _config.set_theme(str(name))


def setstyle(name):
    _config.set_style(str(name))


def setlog(path):
    _config.set_log_file(str(path))


def setlevel(level):
    mapping = {
        "trace": LogLevel.TRACE, "debug": LogLevel.DEBUG,
        "info": LogLevel.INFO, "success": LogLevel.SUCCESS,
        "warning": LogLevel.WARNING, "error": LogLevel.ERROR,
        "critical": LogLevel.CRITICAL, "fatal": LogLevel.FATAL,
    }
    key = str(level).lower().strip()
    if key in mapping:
        _config.min_level = mapping[key]
    else:
        raise ValueError(f"Unknown level: {level}. Available: {', '.join(mapping.keys())}")

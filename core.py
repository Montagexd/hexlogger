from datetime import datetime

from .config import get_config, LogLevel
from .styles import STYLES
from .utils import strip_ansi

__all__ = ["debug", "info", "success", "warn", "warning", "error", "critical", "fatal", "trace"]


def _get_time():
    try:
        return datetime.now().strftime(get_config().time_format)
    except Exception:
        return ""


def _log(level, message, level_enum):
    try:
        cfg = get_config()
        if level_enum.value < cfg.min_level.value:
            return
        t = cfg.theme
        now = _get_time()
        style_fn = STYLES.get(cfg.style, STYLES["default"])
        line = style_fn(now, level, t.get(level), t.get(f"label_{level}"), str(message), t, cfg.show_time)
        with cfg._lock:
            print(line)
            if cfg._file_handle:
                try:
                    cfg._file_handle.write(strip_ansi(line) + "\n")
                    cfg._file_handle.flush()
                except Exception:
                    pass
    except Exception:
        try:
            print(f"[{level.upper()}] {message}")
        except Exception:
            pass


def debug(msg): _log("debug", msg, LogLevel.DEBUG)
def info(msg): _log("info", msg, LogLevel.INFO)
def success(msg): _log("success", msg, LogLevel.SUCCESS)
def warn(msg): _log("warning", msg, LogLevel.WARNING)
def warning(msg): _log("warning", msg, LogLevel.WARNING)
def error(msg): _log("error", msg, LogLevel.ERROR)
def critical(msg): _log("critical", msg, LogLevel.CRITICAL)
def fatal(msg): _log("fatal", msg, LogLevel.FATAL)
def trace(msg): _log("trace", msg, LogLevel.TRACE)

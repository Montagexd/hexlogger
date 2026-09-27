from .colors import Colors, rgb

__all__ = ["Theme", "THEMES", "LEVEL_ICONS"]


class Theme:
    def __init__(self, name, colors):
        self.name = str(name)
        self.colors = colors if isinstance(colors, dict) else {}

    def get(self, key):
        try:
            return self.colors.get(key, Colors.RESET)
        except Exception:
            return Colors.RESET

THEMES = {
    "default": Theme("default", {
        "timestamp": rgb(100, 100, 100), "bracket": rgb(70, 70, 70),
        "dot": rgb(255, 255, 255), "separator": rgb(100, 100, 100),
        "debug": rgb(138, 180, 248), "info": rgb(130, 170, 255),
        "success": rgb(80, 230, 120), "warning": rgb(255, 200, 60),
        "error": rgb(255, 85, 85), "critical": rgb(255, 50, 50),
        "fatal": rgb(200, 0, 0), "trace": rgb(160, 160, 160),
        "divider": rgb(60, 60, 60),
        "label_debug": "DEBUG", "label_info": "INFO",
        "label_success": "SUCCESS", "label_warning": "WARNING",
        "label_error": "ERROR", "label_critical": "CRITICAL",
        "label_fatal": "FATAL", "label_trace": "TRACE",
    }),
    "neon": Theme("neon", {
        "timestamp": rgb(0, 255, 200), "bracket": rgb(0, 200, 150),
        "dot": rgb(0, 255, 255), "separator": rgb(0, 180, 180),
        "debug": rgb(0, 200, 255), "info": rgb(0, 255, 200),
        "success": rgb(0, 255, 100), "warning": rgb(255, 255, 0),
        "error": rgb(255, 50, 80), "critical": rgb(255, 0, 100),
        "fatal": rgb(200, 0, 50), "trace": rgb(100, 200, 200),
        "divider": rgb(0, 100, 100),
        "label_debug": "DEBUG", "label_info": "INFO",
        "label_success": "SUCCESS", "label_warning": "WARNING",
        "label_error": "ERROR", "label_critical": "CRITICAL",
        "label_fatal": "FATAL", "label_trace": "TRACE",
    }),
    "minimal": Theme("minimal", {
        "timestamp": rgb(120, 120, 120), "bracket": rgb(80, 80, 80),
        "dot": rgb(180, 180, 180), "separator": rgb(100, 100, 100),
        "debug": rgb(150, 150, 150), "info": rgb(200, 200, 200),
        "success": rgb(100, 200, 100), "warning": rgb(200, 180, 80),
        "error": rgb(200, 80, 80), "critical": rgb(220, 50, 50),
        "fatal": rgb(180, 0, 0), "trace": rgb(120, 120, 120),
        "divider": rgb(60, 60, 60),
        "label_debug": "DBG", "label_info": "INF",
        "label_success": "OK", "label_warning": "WRN",
        "label_error": "ERR", "label_critical": "CRT",
        "label_fatal": "FTL", "label_trace": "TRC",
    }),
    "hacker": Theme("hacker", {
        "timestamp": rgb(0, 180, 0), "bracket": rgb(0, 120, 0),
        "dot": rgb(0, 255, 0), "separator": rgb(0, 150, 0),
        "debug": rgb(0, 200, 0), "info": rgb(0, 255, 0),
        "success": rgb(50, 255, 50), "warning": rgb(200, 255, 0),
        "error": rgb(255, 100, 0), "critical": rgb(255, 50, 0),
        "fatal": rgb(255, 0, 0), "trace": rgb(0, 150, 0),
        "divider": rgb(0, 80, 0),
        "label_debug": "DEBUG", "label_info": "INFO",
        "label_success": "SUCCESS", "label_warning": "WARNING",
        "label_error": "ERROR", "label_critical": "CRITICAL",
        "label_fatal": "FATAL", "label_trace": "TRACE",
    }),
    "sunset": Theme("sunset", {
        "timestamp": rgb(255, 150, 50), "bracket": rgb(200, 100, 50),
        "dot": rgb(255, 200, 100), "separator": rgb(200, 120, 60),
        "debug": rgb(255, 180, 100), "info": rgb(255, 160, 80),
        "success": rgb(255, 220, 50), "warning": rgb(255, 120, 30),
        "error": rgb(255, 60, 60), "critical": rgb(200, 30, 30),
        "fatal": rgb(150, 0, 0), "trace": rgb(200, 150, 100),
        "divider": rgb(150, 80, 40),
        "label_debug": "DEBUG", "label_info": "INFO",
        "label_success": "SUCCESS", "label_warning": "WARNING",
        "label_error": "ERROR", "label_critical": "CRITICAL",
        "label_fatal": "FATAL", "label_trace": "TRACE",
    }),
    "ocean": Theme("ocean", {
        "timestamp": rgb(0, 150, 200), "bracket": rgb(0, 100, 160),
        "dot": rgb(0, 200, 255), "separator": rgb(0, 130, 180),
        "debug": rgb(100, 180, 255), "info": rgb(0, 200, 255),
        "success": rgb(0, 255, 200), "warning": rgb(255, 220, 80),
        "error": rgb(255, 80, 100), "critical": rgb(255, 40, 80),
        "fatal": rgb(200, 0, 50), "trace": rgb(80, 150, 200),
        "divider": rgb(0, 80, 120),
        "label_debug": "DEBUG", "label_info": "INFO",
        "label_success": "SUCCESS", "label_warning": "WARNING",
        "label_error": "ERROR", "label_critical": "CRITICAL",
        "label_fatal": "FATAL", "label_trace": "TRACE",
    }),
}

LEVEL_ICONS = {
    "debug": "●", "info": "ℹ", "success": "✓", "warning": "⚠",
    "error": "✗", "critical": "☠", "fatal": "💀", "trace": "→",
}

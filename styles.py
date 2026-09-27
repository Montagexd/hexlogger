from .colors import Colors, bgrgb
from .themes import LEVEL_ICONS

__all__ = ["STYLES"]

_TAG_BG = {
    "debug": bgrgb(50, 80, 120), "info": bgrgb(40, 70, 130),
    "success": bgrgb(30, 100, 50), "warning": bgrgb(130, 100, 0),
    "error": bgrgb(130, 30, 30), "critical": bgrgb(150, 20, 20),
    "fatal": bgrgb(120, 0, 0), "trace": bgrgb(60, 60, 60),
}


def _style_default(now, level, level_color, level_label, message, t, show_time):
    R, B = Colors.RESET, Colors.BOLD
    br, ts, dt, sep = t.get("bracket"), t.get("timestamp"), t.get("dot"), t.get("separator")
    if show_time:
        return f"{br}[-({ts}{now}{R}{br})-]{R} {br}[{R} {dt}●{R} {br}]{R} {B}{level_color}{level_label}{R} {sep}»{R}  {level_color}{message}{R}"
    return f"{br}[{R} {dt}●{R} {br}]{R} {B}{level_color}{level_label}{R} {sep}»{R}  {level_color}{message}{R}"


def _style_box(now, level, level_color, level_label, message, t, show_time):
    R, B = Colors.RESET, Colors.BOLD
    br, ts, icon = t.get("bracket"), t.get("timestamp"), LEVEL_ICONS.get(level, "●")
    lbl = str(level_label).ljust(8)
    if show_time:
        return f"{br}┃{R} {ts}{now}{R} {br}│{R} {level_color}{icon}{R} {B}{level_color}{lbl}{R} {br}│{R} {level_color}{message}{R}"
    return f"{br}┃{R} {level_color}{icon}{R} {B}{level_color}{lbl}{R} {br}│{R} {level_color}{message}{R}"


def _style_modern(now, level, level_color, level_label, message, t, show_time):
    R, B, ts, icon = Colors.RESET, Colors.BOLD, t.get("timestamp"), LEVEL_ICONS.get(level, "●")
    if show_time:
        return f"{ts}{now}{R}  {level_color}{icon} {B}{level_label}{R}  {level_color}{message}{R}"
    return f"{level_color}{icon} {B}{level_label}{R}  {level_color}{message}{R}"


def _style_bracket(now, level, level_color, level_label, message, t, show_time):
    R, B, br, ts = Colors.RESET, Colors.BOLD, t.get("bracket"), t.get("timestamp")
    if show_time:
        return f"{br}[{ts}{now}{R}{br}]{R} {br}[{B}{level_color}{level_label}{R}{br}]{R} {level_color}{message}{R}"
    return f"{br}[{B}{level_color}{level_label}{R}{br}]{R} {level_color}{message}{R}"


def _style_arrow(now, level, level_color, level_label, message, t, show_time):
    R, B, ts, sep = Colors.RESET, Colors.BOLD, t.get("timestamp"), t.get("separator")
    if show_time:
        return f"{ts}{now}{R} {sep}▸{R} {B}{level_color}{level_label}{R} {sep}▸{R} {level_color}{message}{R}"
    return f"{sep}▸{R} {B}{level_color}{level_label}{R} {sep}▸{R} {level_color}{message}{R}"


def _style_pipe(now, level, level_color, level_label, message, t, show_time):
    R, B, ts, br = Colors.RESET, Colors.BOLD, t.get("timestamp"), t.get("bracket")
    lbl = str(level_label).ljust(8)
    if show_time:
        return f"{level_color}▌{R} {ts}{now}{R} {br}|{R} {B}{level_color}{lbl}{R} {br}|{R} {level_color}{message}{R}"
    return f"{level_color}▌{R} {B}{level_color}{lbl}{R} {br}|{R} {level_color}{message}{R}"


def _style_tag(now, level, level_color, level_label, message, t, show_time):
    R, B, ts = Colors.RESET, Colors.BOLD, t.get("timestamp")
    bg = _TAG_BG.get(level, "")
    if show_time:
        return f"{ts}{now}{R} {bg}{B} {level_label} {R} {level_color}{message}{R}"
    return f"{bg}{B} {level_label} {R} {level_color}{message}{R}"


def _style_dots(now, level, level_color, level_label, message, t, show_time):
    R, B = Colors.RESET, Colors.BOLD
    ts, sep, icon = t.get("timestamp"), t.get("separator"), LEVEL_ICONS.get(level, "●")
    if show_time:
        return f"{level_color}{icon}{R} {ts}{now}{R} {sep}·{R} {B}{level_color}{level_label}{R} {sep}·{R} {level_color}{message}{R}"
    return f"{level_color}{icon} {B}{level_color}{level_label}{R} {sep}·{R} {level_color}{message}{R}"


def _style_clean(now, level, level_color, level_label, message, t, show_time):
    R, B, ts = Colors.RESET, Colors.BOLD, t.get("timestamp")
    lbl = str(level_label).ljust(8)
    if show_time:
        return f"  {ts}{now}{R}  {B}{level_color}{lbl}{R}  {level_color}{message}{R}"
    return f"  {B}{level_color}{lbl}{R}  {level_color}{message}{R}"


STYLES = {
    "default": _style_default, "box": _style_box, "modern": _style_modern,
    "bracket": _style_bracket, "arrow": _style_arrow, "pipe": _style_pipe,
    "tag": _style_tag, "dots": _style_dots, "clean": _style_clean,
}

__all__ = ["Colors", "rgb", "bgrgb", "hexclr", "bghex"]


class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    STRIKE = "\033[9m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"


def _clamp(v):
    return max(0, min(255, int(v)))

def rgb(r, g, b):
    return f"\033[38;2;{_clamp(r)};{_clamp(g)};{_clamp(b)}m"

def bgrgb(r, g, b):
    return f"\033[48;2;{_clamp(r)};{_clamp(g)};{_clamp(b)}m"

def hexclr(hex_code):
    try:
        hex_code = str(hex_code).lstrip("#")
        if len(hex_code) < 6:
            hex_code = hex_code.ljust(6, "0")
        r, g, b = int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)
        return rgb(r, g, b)
    except Exception:
        return Colors.RESET

def bghex(hex_code):
    try:
        hex_code = str(hex_code).lstrip("#")
        if len(hex_code) < 6:
            hex_code = hex_code.ljust(6, "0")
        r, g, b = int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)
        return bgrgb(r, g, b)
    except Exception:
        return Colors.RESET

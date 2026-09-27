import re
import shutil

from .colors import Colors

__all__ = ["strip_ansi", "clr", "bold", "italic", "uline"]

_ANSI_RE = re.compile(r'\033\[[0-9;]*m')


def strip_ansi(text):
    try:
        return _ANSI_RE.sub('', str(text))
    except Exception:
        return str(text)


def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 120


def wrap_line(text, max_width):
    if len(strip_ansi(text)) <= max_width:
        return [text]
    wrapped = []
    current = ""
    current_len = 0
    i = 0
    while i < len(text):
        if text[i] == '\033' and i + 1 < len(text) and text[i + 1] == '[':
            j = i + 2
            while j < len(text) and text[j] not in 'mGHJK':
                j += 1
            if j < len(text):
                j += 1
            current += text[i:j]
            i = j
        else:
            if current_len >= max_width:
                wrapped.append(current)
                current = ""
                current_len = 0
            current += text[i]
            current_len += 1
            i += 1
    if current:
        wrapped.append(current)
    return wrapped if wrapped else [text]


def wrap_lines(lines, max_width):
    result = []
    for line in lines:
        result.extend(wrap_line(line, max_width))
    return result


def clr(text, color):
    return f"{color}{text}{Colors.RESET}"


def bold(text):
    return f"{Colors.BOLD}{text}{Colors.RESET}"


def italic(text):
    return f"{Colors.ITALIC}{text}{Colors.RESET}"


def uline(text):
    return f"{Colors.UNDERLINE}{text}{Colors.RESET}"

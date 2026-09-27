from .colors import Colors
from .config import get_config
from .utils import strip_ansi, get_terminal_width, wrap_lines

__all__ = ["panel", "table", "box"]

_PANEL_CHARS = {
    "rounded": ("╭", "╮", "╰", "╯", "─", "│"),
    "sharp":   ("┌", "┐", "└", "┘", "─", "│"),
    "double":  ("╔", "╗", "╚", "╝", "═", "║"),
    "heavy":   ("┏", "┓", "┗", "┛", "━", "┃"),
    "ascii":   ("+", "+", "+", "+", "-", "|"),
}

_TABLE_CHARS = {
    "rounded": ("╭", "╮", "╰", "╯", "─", "│", "┬", "┴", "├", "┤", "┼"),
    "sharp":   ("┌", "┐", "└", "┘", "─", "│", "┬", "┴", "├", "┤", "┼"),
    "double":  ("╔", "╗", "╚", "╝", "═", "║", "╦", "╩", "╠", "╣", "╬"),
    "heavy":   ("┏", "┓", "┗", "┛", "━", "┃", "┳", "┻", "┣", "┫", "╋"),
    "ascii":   ("+", "+", "+", "+", "-", "|", "+", "+", "+", "+", "+"),
}

_BOX_CHARS = {
    **_PANEL_CHARS,
    "stars":  ("*", "*", "*", "*", "*", "*"),
    "dashes": ("+", "+", "+", "+", "~", ":"),
}


def panel(content="", title="", width=50, color=None, style="rounded"):
    try:
        cfg = get_config()
        bc = color or cfg.theme.get("info")
        R = Colors.RESET
        tl, tr, bl, br, h, v = _PANEL_CHARS.get(style, _PANEL_CHARS["rounded"])
        content = str(content)
        term_w = get_terminal_width()
        max_inner = max(term_w - 4, 8)
        lines = wrap_lines(content.split("\n"), max_inner)
        max_line_len = max((len(strip_ansi(l)) for l in lines), default=0)
        width = max(width, max_line_len + 4, 8)
        if title:
            title = str(title)
            width = max(width, len(strip_ansi(title)) + 6)
        width = min(width, term_w)
        inner_w = width - 4
        with cfg._lock:
            if title:
                header_pad = max(width - len(strip_ansi(title)) - 5, 1)
                print(f"{bc}{tl}{h} {Colors.BOLD}{title}{R}{bc} {h * header_pad}{tr}{R}")
            else:
                print(f"{bc}{tl}{h * (width - 2)}{tr}{R}")
            for l in lines:
                pad = max(inner_w - len(strip_ansi(l)), 0)
                print(f"{bc}{v}{R} {l}{' ' * pad} {bc}{v}{R}")
            print(f"{bc}{bl}{h * (width - 2)}{br}{R}")
    except Exception:
        print(content)


def table(headers=None, rows=None, color=None, style="rounded"):
    try:
        if not headers:
            return
        headers = [str(h) for h in headers]
        rows = rows or []
        rows = [[str(c) for c in r] for r in rows]
        cfg = get_config()
        bc = color or cfg.theme.get("info")
        hc = cfg.theme.get("success")
        R, B = Colors.RESET, Colors.BOLD
        tl, tr, bl, br, h, v, tm, bm, ml, mr, mm = _TABLE_CHARS.get(style, _TABLE_CHARS["rounded"])
        col_w = [len(strip_ansi(hdr)) for hdr in headers]
        for r in rows:
            for i, c in enumerate(r):
                vl = len(strip_ansi(c))
                if i < len(col_w):
                    col_w[i] = max(col_w[i], vl)
                else:
                    col_w.append(vl)

        def _sep(left, mid, right, fill):
            return f"{bc}{left}{mid.join(fill * (w + 2) for w in col_w)}{right}{R}"

        def _row(cells, c=""):
            padded = []
            for i, cell in enumerate(cells):
                w = col_w[i] if i < len(col_w) else len(strip_ansi(cell))
                pad = max(w - len(strip_ansi(cell)), 0)
                padded.append(f" {c}{cell}{' ' * pad}{R} ")
            return f"{bc}{v}{R}" + f"{bc}{v}{R}".join(padded) + f"{bc}{v}{R}"

        with cfg._lock:
            print(_sep(tl, tm, tr, h))
            print(_row(headers, B + hc))
            print(_sep(ml, mm, mr, h))
            for r in rows:
                print(_row(r))
            print(_sep(bl, bm, br, h))
    except Exception:
        if headers:
            print(" | ".join(str(h) for h in headers))
            for r in (rows or []):
                print(" | ".join(str(c) for c in r))


def box(text="", width=None, style="rounded", color=None, text_clr=None, align="left", padding=1):
    try:
        cfg = get_config()
        bc = color or cfg.theme.get("info")
        tc = text_clr or Colors.RESET
        R = Colors.RESET
        tl, tr, bl, br, h, v = _BOX_CHARS.get(style, _BOX_CHARS["rounded"])
        text = str(text)
        padding = max(0, int(padding))
        term_w = get_terminal_width()
        max_inner = max(term_w - 4, 1)
        lines = wrap_lines(text.split("\n"), max_inner)
        max_line = max((len(strip_ansi(l)) for l in lines), default=0)
        inner_w = (width - 4) if width else max_line + (padding * 2)
        inner_w = max(inner_w, max_line, 1)
        inner_w = min(inner_w, max_inner)
        total_w = inner_w + 4
        with cfg._lock:
            print(f"{bc}{tl}{h * (total_w - 2)}{tr}{R}")
            for l in lines:
                s_len = len(strip_ansi(l))
                space = max(inner_w - s_len, 0)
                if align == "center":
                    lp = space // 2
                    rp = space - lp
                    padded = f"{' ' * lp}{tc}{l}{R}{' ' * rp}"
                elif align == "right":
                    padded = f"{' ' * space}{tc}{l}{R}"
                else:
                    padded = f"{tc}{l}{R}{' ' * space}"
                print(f"{bc}{v}{R} {padded} {bc}{v}{R}")
            print(f"{bc}{bl}{h * (total_w - 2)}{br}{R}")
    except Exception:
        print(text)

from .colors import Colors
from .config import get_config
from .utils import strip_ansi, get_terminal_width, wrap_lines

__all__ = ["divider", "section", "blank", "rule", "banner", "pair"]


def _write(cfg, message):
    if cfg._file_handle:
        try:
            cfg._file_handle.write(strip_ansi(message) + "\n")
            cfg._file_handle.flush()
        except Exception:
            pass


def divider(char="─", length=60, color=None):
    try:
        cfg = get_config()
        c = color or cfg.theme.get("divider")
        length = min(max(1, int(length)), get_terminal_width())
        line = f"{c}{str(char)[0] * length}{Colors.RESET}"
        with cfg._lock:
            print(line)
            _write(cfg, line)
    except Exception:
        print(str(char) * max(1, int(length)))


def section(title="", char="═", length=60):
    try:
        cfg = get_config()
        t = cfg.theme
        title = str(title)
        title_len = len(strip_ansi(title))
        length = min(max(title_len + 4, int(length)), get_terminal_width())
        pad = length - title_len - 2
        left = pad // 2
        right = pad - left
        line = (
            f"{t.get('divider')}{str(char)[0] * left}{Colors.RESET} "
            f"{Colors.BOLD}{t.get('info')}{title}{Colors.RESET} "
            f"{t.get('divider')}{str(char)[0] * right}{Colors.RESET}"
        )
        with cfg._lock:
            print(line)
            _write(cfg, line)
    except Exception:
        print(f"== {title} ==")


def blank(count=1):
    try:
        cfg = get_config()
        with cfg._lock:
            for _ in range(max(1, int(count))):
                print()
    except Exception:
        for _ in range(max(1, int(count))):
            print()


def rule(text="", char="─", length=60):
    if text:
        section(text, char, length)
    else:
        divider(char, length)


def banner(text="", char="═", padding=2):
    try:
        cfg = get_config()
        text = str(text)
        padding = max(0, int(padding))
        term_w = get_terminal_width()
        max_inner = max(term_w - 2, 1)
        lines = wrap_lines(text.split("\n"), max_inner - (padding * 2))
        max_len = max((len(strip_ansi(l)) for l in lines), default=0)
        width = min(max_len + (padding * 2) + 2, term_w)
        t = cfg.theme
        bc, tc, R = t.get("info"), t.get("success"), Colors.RESET
        ch = str(char)[0] if char else "═"
        with cfg._lock:
            print(f"{bc}╔{ch * (width - 2)}╗{R}")
            for l in lines:
                s_len = len(strip_ansi(l))
                space = max(max_len - s_len, 0)
                lp = space // 2
                rp = space - lp
                padded = f"{' ' * lp}{l}{' ' * rp}"
                print(f"{bc}║{R}{' ' * padding}{tc}{padded}{R}{' ' * padding}{bc}║{R}")
            print(f"{bc}╚{ch * (width - 2)}╝{R}")
    except Exception:
        print(text)


def pair(k, v, k_clr=None, v_clr=None):
    try:
        cfg = get_config()
        kc = k_clr or cfg.theme.get("info")
        vc = v_clr or Colors.RESET
        k, v = str(k), str(v)
        with cfg._lock:
            print(f"  {kc}{Colors.BOLD}{k}{Colors.RESET}: {vc}{v}{Colors.RESET}")
            _write(cfg, f"  {k}: {v}")
    except Exception:
        print(f"  {k}: {v}")

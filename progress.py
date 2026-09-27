import sys
import time
import threading

from .colors import Colors
from .config import get_config
from .utils import get_terminal_width

__all__ = ["Progress", "Spinner", "Timer"]


class Progress:
    def __init__(self, total, width=30, label="Progress", fill="█", empty="░", color=None):
        self.total = max(1, int(total))
        self.width = max(5, int(width))
        self.label = str(label)
        self.fill = str(fill)[0] if fill else "█"
        self.empty = str(empty)[0] if empty else "░"
        try:
            self.color = color or get_config().theme.get("success")
        except Exception:
            self.color = ""
        self.current = 0
        self._start = time.time()

    def update(self, n=1):
        self.current = min(self.current + max(0, int(n)), self.total)
        self._render()

    def _render(self):
        try:
            term_w = get_terminal_width()
            pct = self.current / self.total
            stats = f" ({self.current}/{self.total}) [{time.time() - self._start:.1f}s]"
            label_part = f"{self.color}{self.label}{Colors.RESET} │"
            bar_end = f"│ {Colors.BOLD}{pct * 100:5.1f}%{Colors.RESET}{stats}"
            overhead = len(self.label) + 3 + 10 + len(stats)
            bar_w = min(self.width, max(5, term_w - overhead))
            filled = int(bar_w * pct)
            bar = self.fill * filled + self.empty * (bar_w - filled)
            elapsed = time.time() - self._start
            eta = (elapsed / pct - elapsed) if pct > 0 else 0
            line = (
                f"\r{self.color}{self.label}{Colors.RESET} "
                f"│{self.color}{bar}{Colors.RESET}│ "
                f"{Colors.BOLD}{pct * 100:5.1f}%{Colors.RESET} "
                f"({self.current}/{self.total}) "
                f"[{elapsed:.1f}s / ETA {eta:.1f}s]"
            )
            sys.stdout.write(line)
            sys.stdout.flush()
            if self.current >= self.total:
                print()
        except Exception:
            pass


class Spinner:
    _FRAMES = {
        "dots":   ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
        "line":   ["-", "\\", "|", "/"],
        "arrow":  ["←", "↖", "↑", "↗", "→", "↘", "↓", "↙"],
        "bounce": ["⠁", "⠂", "⠄", "⠂"],
        "box":    ["▖", "▘", "▝", "▗"],
        "circle": ["◐", "◓", "◑", "◒"],
    }

    def __init__(self, msg="Loading", style="dots", color=None):
        self.msg = str(msg)
        self.frames = self._FRAMES.get(style, self._FRAMES["dots"])
        try:
            self.color = color or get_config().theme.get("info")
        except Exception:
            self.color = ""
        self._stop_event = threading.Event()
        self._thread = None

    def start(self):
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()
        return self

    def _spin(self):
        i = 0
        while not self._stop_event.is_set():
            try:
                frame = self.frames[i % len(self.frames)]
                sys.stdout.write(f"\r{self.color}{frame}{Colors.RESET} {self.msg}")
                sys.stdout.flush()
            except Exception:
                pass
            i += 1
            self._stop_event.wait(0.08)

    def stop(self, final=""):
        self._stop_event.set()
        if self._thread:
            try:
                self._thread.join(timeout=2)
            except Exception:
                pass
        try:
            sys.stdout.write(f"\r\033[2K\r")
            sys.stdout.flush()
        except Exception:
            pass
        if final:
            try:
                from .core import success
                success(final)
            except Exception:
                print(final)

    def __enter__(self):
        return self.start()

    def __exit__(self, *args):
        self.stop()


class Timer:
    def __init__(self, label="Elapsed"):
        self.label = str(label)
        self._start = None

    def start(self):
        self._start = time.time()
        return self

    def stop(self):
        try:
            if self._start is None:
                return 0.0
            elapsed = time.time() - self._start
            from .core import info
            info(f"{self.label}: {elapsed:.3f}s")
            return elapsed
        except Exception:
            return 0.0

    def __enter__(self):
        return self.start()

    def __exit__(self, *args):
        self.stop()

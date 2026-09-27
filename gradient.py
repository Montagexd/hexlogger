from .colors import Colors, rgb

__all__ = ["gtext", "gprint", "mgtext", "mgprint", "rbtext", "rbprint"]

_RAINBOW = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 127, 255), (75, 0, 130), (148, 0, 211)]


def _interpolate(c1, c2, t):
    t = max(0.0, min(1.0, float(t)))
    return (
        int(c1[0] + (c2[0] - c1[0]) * t),
        int(c1[1] + (c2[1] - c1[1]) * t),
        int(c1[2] + (c2[2] - c1[2]) * t),
    )


def gtext(text, start=(255, 0, 100), end=(100, 0, 255)):
    try:
        text = str(text)
        if not text:
            return ""
        result = []
        length = max(len(text) - 1, 1)
        for i, c in enumerate(text):
            r, g, b = _interpolate(start, end, i / length)
            result.append(f"{rgb(r, g, b)}{c}")
        return "".join(result) + Colors.RESET
    except Exception:
        return str(text)


def gprint(text, start=(255, 0, 100), end=(100, 0, 255)):
    print(gtext(text, start, end))


def mgtext(text, colors=None):
    try:
        text = str(text)
        if not colors or len(colors) < 2 or not text:
            return text
        result = []
        segments = len(colors) - 1
        chars_per_seg = max(len(text) / segments, 1)
        for i, c in enumerate(text):
            seg = min(int(i / chars_per_seg), segments - 1)
            t = (i - seg * chars_per_seg) / chars_per_seg
            r, g, b = _interpolate(colors[seg], colors[seg + 1], t)
            result.append(f"{rgb(r, g, b)}{c}")
        return "".join(result) + Colors.RESET
    except Exception:
        return str(text)


def mgprint(text, colors=None):
    print(mgtext(text, colors))


def rbtext(text):
    return mgtext(text, _RAINBOW)


def rbprint(text):
    print(rbtext(text))

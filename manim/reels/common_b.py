"""Phụ trợ cho batch reel thứ hai của math-enthusiast."""
from common import *
import math


def nf(x, d=2):
    s = "%.*f" % (d, x)
    return s.replace(".", ",") if LANG == "vi" else s


def line(d, size, color, y, max_w=7.8, minscale=0.8):
    parts = tr(d).split("\n")
    ts = [T(p, size, color) for p in parts]
    w = max(t.width for t in ts)
    assert w <= max_w / minscale, "dòng quá dài (sẽ bị thu nhỏ): %r %.2f" % (tr(d), w)
    g = VGroup(*ts).arrange(DOWN, buff=0.14) if len(ts) > 1 else ts[0]
    return fit(g, max_w).move_to([0, y, 0])


def mkaxes(xr, yr, w, h, c, xt=(), yt=(), yfmt=None, xfmt=None):
    """Axes + tick labels. yt: list of (value, label)."""
    ax = Axes(x_range=xr, y_range=yr, x_length=w, y_length=h,
              axis_config={"color": DIM, "stroke_width": 3, "tick_size": 0.06}, tips=False).move_to(c)
    lab = VGroup()
    for v in xt:
        lab.add(T(str(v) if xfmt is None else xfmt(v), 20, DIM).next_to(ax.c2p(v, yr[0]), DOWN, buff=0.12))
    for v, s in yt:
        lab.add(T(s, 20, DIM).next_to(ax.c2p(xr[0], v), LEFT, buff=0.12))
    return ax, lab

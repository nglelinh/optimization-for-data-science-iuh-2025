"""Chung cho reel Manim của math-enthusiast: 1080x1920, nền tối, phụ đề vi/en (REEL_LANG=vi|en), không nhạc."""
import os
from manim import *
import numpy as np

LANG = os.environ.get("REEL_LANG", "vi")
assert LANG in ("vi", "en")

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9      # 1 đơn vị = 120 px
config.frame_height = 16
config.background_color = "#10121a"

SUN = "#ffd166"
SKY = "#4cc9f0"
MINT = "#80ed99"
PINK = "#ff7eb6"
ORANGE = "#ff9f43"
DIM = "#7b8294"
CARD = "#1d2130"
FONT = "DejaVu Sans"
CAP_Y = 6.3          # vùng an toàn: |x| <= 4, -6.5 <= y <= 6.8


def tr(d):
    """d = {'vi': ..., 'en': ...}"""
    return d[LANG]


def T(s, size=34, color=WHITE, **kw):
    return Text(s, font=FONT, font_size=size, color=color, **kw)


def cap(d, size=40, color=WHITE):
    return T(tr(d) if isinstance(d, dict) else d, size, color).move_to([0, CAP_Y, 0])


def swap_cap(scene, old, new, rt=0.45):
    scene.play(ReplacementTransform(old, new), run_time=rt)
    return new


def fit(m, max_w=7.8):
    if m.width > max_w:
        m.scale_to_fit_width(max_w)
    return m

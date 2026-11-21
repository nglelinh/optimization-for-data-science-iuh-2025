"""Long-form optimization reels: shared layout (1080x1920, captions only, VI/EN).
Layout: title y=6.25 | stage chip y=4.95 | stage area y in [-2.4, 4.3] | readout y~-3.2 | caption y~-5.4"""
import os
from common_b import *
import glob, manimpango
if "DejaVu Sans" not in manimpango.list_fonts():  # macOS: register DejaVu from a local matplotlib install
    for _f in ("DejaVuSans.ttf", "DejaVuSansMono.ttf"):
        for _p in glob.glob(os.path.expanduser("~/miniconda3/lib/python3*/site-packages/matplotlib/mpl-data/fonts/ttf/" + _f))[:1]:
            manimpango.register_font(_p)
config.frame_rate = 30
if os.environ.get("FAST"):
    config.pixel_width, config.pixel_height, config.frame_rate = 540, 960, 10
MONO = "DejaVu Sans Mono"
STAGES = {1: {"vi": "1 · Bài toán", "en": "1 · Setup"}, 2: {"vi": "2 · Ý tưởng chính", "en": "2 · Key idea"},
          3: {"vi": "3 · Thuật toán chạy", "en": "3 · The algorithm, step by step"},
          4: {"vi": "4 · Đối chiếu", "en": "4 · Contrast"}, 5: {"vi": "5 · Ghi nhớ", "en": "5 · Takeaway"}}
SC = {1: SKY, 2: SUN, 3: MINT, 4: PINK, 5: ORANGE}


def L(vi, en):
    return {"vi": vi, "en": en}


def nf(x, d=2):
    s = "%.*f" % (d, x)
    if s.startswith("-") and float(s) == 0: s = s[1:]
    s = s.replace("-", "−")
    return s.replace(".", ",") if LANG == "vi" else s


def vec(v, d=2):
    return "(" + ("; " if LANG == "vi" else ", ").join(nf(a, d) for a in v) + ")"


def sci(v, d=1):
    s = "%.*e" % (d, v)
    m, e = s.split("e"); e = int(e)
    m = m.replace(".", ",") if LANG == "vi" else m
    sup = str(e).translate(str.maketrans("-0123456789", "⁻⁰¹²³⁴⁵⁶⁷⁸⁹"))
    return m + "·10" + sup


def wrap(s, size, max_w, font=FONT):
    out = []
    for para in s.split("\n"):
        words = para.split(" "); cur = ""
        for w in words:
            cand = (cur + " " + w).strip()
            if cur and Text(cand, font=font, font_size=size).width > max_w:
                out.append(cur); cur = w
            else:
                cur = cand
        out.append(cur)
    return out


def para(d, size=27, color=WHITE, max_w=7.9, font=FONT, buff=0.13):
    s = tr(d) if isinstance(d, dict) else d
    g = VGroup(*[Text(t, font=font, font_size=size, color=color) for t in wrap(s, size, max_w, font)]).arrange(DOWN, buff=buff)
    return fit(g, max_w)


def rtime(d):
    s = tr(d) if isinstance(d, dict) else d
    return max(1.8, 1.0 + 0.052 * len(s))


class Reel(Scene):
    def setup(self):
        self.capm = None; self.chipm = None; self.rom = None; self.titlem = None

    def title(self, d):
        self.titlem = para(d, 33, WHITE, 8.0).move_to([0, 6.3, 0]); self.add(self.titlem)

    def stage(self, i):
        t = Text(tr(STAGES[i]), font=FONT, font_size=24, color=SC[i])
        box = RoundedRectangle(corner_radius=0.22, width=t.width + 0.6, height=0.52, stroke_color=SC[i], stroke_width=2.5, fill_color=CARD, fill_opacity=1)
        chip = VGroup(box, t.move_to(box)).move_to([0, 5.0, 0])
        if self.chipm is None: self.play(FadeIn(chip, shift=DOWN * 0.15), run_time=0.4)
        else: self.play(ReplacementTransform(self.chipm, chip), run_time=0.4)
        self.chipm = chip

    def say(self, d, color=WHITE, hold=None, size=27, wait=True):
        m = para(d, size, color, 7.9)
        m.move_to([0, -5.35, 0])
        if m.get_top()[1] > -4.35: m.shift(UP * (-4.35 - m.get_top()[1]))
        anims = [FadeIn(m, shift=UP * 0.1)]
        if self.capm is not None: anims.append(FadeOut(self.capm))
        self.play(*anims, run_time=0.35); self.capm = m
        if wait: self.wait(rtime(d) if hold is None else hold)
        return m

    def readout(self, rows, y=-3.25, size=23, color=SKY, rt=0.25):
        """rows: list of str (or (str,color))"""
        ms = []
        for r in rows:
            s, c = (r, color) if isinstance(r, str) else r
            ms.append(Text(s, font=MONO, font_size=size, color=c))
        g = fit(VGroup(*ms).arrange(DOWN, buff=0.1, aligned_edge=LEFT), 8.0).move_to([0, y, 0])
        if self.rom is None: self.play(FadeIn(g), run_time=rt)
        else: self.remove(self.rom); self.add(g)
        self.rom = g
        return g

    def clear_ro(self):
        if self.rom is not None: self.play(FadeOut(self.rom), run_time=0.25); self.rom = None

    def wipe(self, keep=()):
        keep = set(keep) | {self.titlem, self.chipm}
        ms = [m for m in self.mobjects if m not in keep]
        if ms: self.play(*[FadeOut(m) for m in ms], run_time=0.5)
        self.capm = None; self.rom = None

    def takeaway(self, items, tail=3.0):
        self.wipe(); self.stage(5)
        y = 3.6; ms = []
        for i, d in enumerate(items):
            p = para(("• " if True else "") + tr(d), 29, WHITE if i % 2 == 0 else SUN, 7.8)
            p.next_to([0, y, 0], DOWN, buff=0).set_x(0); y = p.get_bottom()[1] - 0.45
            for row in p: row.align_to(p, LEFT)
            self.play(FadeIn(p, shift=UP * 0.15), run_time=0.45); self.wait(rtime(d) * 0.85); ms.append(p)
        self.wait(tail)

    def reading(self, d):
        self.wait(rtime(d))


def box_panel(w, h, c):
    return RoundedRectangle(corner_radius=0.18, width=w, height=h, stroke_color="#2c3350", stroke_width=2, fill_color=CARD, fill_opacity=0.9).move_to(c)


def trail(scene, ax, pts, dot, color, rt=0.6, width=4, ks=None, cb=None, rate=smooth):
    """animate dot along pts (indices ks), drawing segments; returns VGroup path (single scene mobject)."""
    segs = []
    ks = list(range(1, len(pts))) if ks is None else list(ks)
    prev = 0
    for k in ks:
        seg = Line(ax.c2p(*pts[prev]), ax.c2p(*pts[k]), color=color, stroke_width=width)
        r = rt(k) if callable(rt) else rt
        scene.play(Create(seg), dot.animate.move_to(ax.c2p(*pts[k])), run_time=r, rate_func=rate)
        segs.append(seg); prev = k
        if cb: cb(k)
    scene.remove(*segs); g = VGroup(*segs); scene.add(g); scene.bring_to_front(dot)
    return g


def contours(ax, F, levels, box, N=80, color="#2c3350", width=2.5):
    """marching-squares level sets of F(x,y) inside box=(x0,x1,y0,y1)."""
    X0, X1, Y0, Y1 = box
    gx = np.linspace(X0, X1, N + 1); gy = np.linspace(Y0, Y1, N + 1)
    V = np.array([[F(x, y) for y in gy] for x in gx])
    g = VGroup()
    for lv in levels:
        for i in range(N):
            for j in range(N):
                c = [V[i, j] > lv, V[i + 1, j] > lv, V[i + 1, j + 1] > lv, V[i, j + 1] > lv]
                def P(a, b, k, l):
                    t = (lv - V[a, b]) / (V[k, l] - V[a, b]); return (gx[a] + t * (gx[k] - gx[a]), gy[b] + t * (gy[l] - gy[b]))
                e = []
                if c[0] != c[1]: e.append(P(i, j, i + 1, j))
                if c[1] != c[2]: e.append(P(i + 1, j, i + 1, j + 1))
                if c[3] != c[2]: e.append(P(i, j + 1, i + 1, j + 1))
                if c[0] != c[3]: e.append(P(i, j, i, j + 1))
                prs = [(e[0], e[1])] if len(e) == 2 else ([(e[0], e[1]), (e[2], e[3])] if len(e) == 4 else [])
                for a, b in prs:
                    g.add(Line(ax.c2p(*a), ax.c2p(*b), color=color, stroke_width=width))
    return g


def plain_axes(xr, yr, w, h, c, ticks=False):
    return Axes(x_range=xr, y_range=yr, x_length=w, y_length=h, axis_config={"color": DIM, "stroke_width": 2, "include_ticks": ticks}, tips=False).move_to(c)

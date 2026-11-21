from common_b import *
import math

TX = {
    "title": {"vi": "Gradient descent và BFGS\ntrên cùng một hàm", "en": "Gradient descent vs BFGS\non the same function"},
    "gd": {"vi": "Gradient descent", "en": "Gradient descent"},
    "bf": {"vi": "BFGS (không cần Hessian)", "en": "BFGS (no Hessian needed)"},
    "steps": {"vi": "bước", "en": "steps"},
    "end1": {"vi": "BFGS học độ cong từ các gradient đã thấy,\nnên đi thẳng hơn nhiều", "en": "BFGS learns curvature from gradients it has seen,\nso it heads for the minimum much more directly"},
    "gap": {"vi": "Dừng khi f − f* < 10⁻¹⁰", "en": "Stop when f − f* < 10⁻¹⁰"},
}


def F(p):
    a = math.exp(p[0] + 3 * p[1] - 0.1); b = math.exp(p[0] - 3 * p[1] - 0.1); c = math.exp(-p[0] - 0.1)
    return math.log(a + b + c)


def G(p):
    a = math.exp(p[0] + 3 * p[1] - 0.1); b = math.exp(p[0] - 3 * p[1] - 0.1); c = math.exp(-p[0] - 0.1); z = a + b + c
    return np.array([(a + b - c) / z, (3 * a - 3 * b) / z])


def Hs(p):
    a = math.exp(p[0] + 3 * p[1] - 0.1); b = math.exp(p[0] - 3 * p[1] - 0.1); c = math.exp(-p[0] - 0.1); z = a + b + c
    g = G(p)
    return np.array([[(a + b + c) / z - g[0] ** 2, (3 * a - 3 * b) / z - g[0] * g[1]], [(3 * a - 3 * b) / z - g[0] * g[1], 9 * (a + b) / z - g[1] ** 2]])


ps = np.zeros(2)
for _ in range(60):
    ps = ps - np.linalg.solve(Hs(ps), G(ps))
FS = F(ps)
assert abs(ps[0] + 0.5 * math.log(2)) < 1e-9 and abs(ps[1]) < 1e-9


def run(kind, start, maxit=400):
    p = np.array(start, float); pts = [p.copy()]; H = np.eye(2); it = 0
    while it < maxit and F(p) - FS > 1e-10:
        g = G(p); d = -g if kind == "gd" else -H @ g
        t = 1.0; gd = g @ d; k = 0
        while F(p + t * d) > F(p) + 0.1 * t * gd and k < 80:
            t *= 0.7; k += 1
        pn = p + t * d
        if kind == "bfgs":
            s = pn - p; y = G(pn) - g; sy = s @ y
            if sy > 1e-14:
                r = 1 / sy; I = np.eye(2)
                H = (I - r * np.outer(s, y)) @ H @ (I - r * np.outer(y, s)) + r * np.outer(s, s)
        p = pn; pts.append(p.copy()); it += 1
    return pts, it


S0 = (1.6, 1.1)
GDP, NG = run("gd", S0); BFP, NB = run("bfgs", S0)
assert (NG, NB) == (23, 8), (NG, NB)       # khớp với explainer
# marching squares
N = 90; X0, X1, Y0, Y1 = -2.6, 2.4, -2.6, 2.4
gx = np.linspace(X0, X1, N + 1); gy = np.linspace(Y0, Y1, N + 1)
V = np.array([[F((x, y)) for y in gy] for x in gx])


def segs(lv):
    out = []
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
            if len(e) == 2: out.append((e[0], e[1]))
            elif len(e) == 4: out += [(e[0], e[1]), (e[2], e[3])]
    return out


class QN(Scene):
    def construct(self):
        self.add(line(TX["title"], 30, WHITE, 6.2))
        W = 7.2
        c2p = lambda p: np.array([(p[0] - X0) / (X1 - X0) * W - W / 2, (p[1] - Y0) / (Y1 - Y0) * W + 0.2 - W / 2 + 0.4, 0])
        frame = Rectangle(width=W, height=W, stroke_color="#2c3350", stroke_width=2).move_to(c2p([(X0 + X1) / 2, (Y0 + Y1) / 2]))
        self.play(Create(frame), run_time=0.5)
        cont = VGroup()
        for lv in (FS + 0.05, FS + 0.25, FS + 0.7, FS + 1.5, FS + 2.6):
            for a, b in segs(lv):
                cont.add(Line(c2p(a), c2p(b), color="#46507a", stroke_width=2))
        self.play(FadeIn(cont), run_time=0.8)
        s0 = Dot(c2p(S0), radius=0.11, color=PINK); sx = Dot(c2p(ps), radius=0.09, color=WHITE)
        self.play(FadeIn(s0), FadeIn(sx), run_time=0.5)
        l1 = line(TX["gd"], 30, SUN, -4.0); l2 = line(TX["bf"], 30, MINT, -5.0)
        self.play(FadeIn(l1), FadeIn(l2), run_time=0.5)
        gl = VMobject(color=SUN, stroke_width=4); bl = VMobject(color=MINT, stroke_width=4)
        self.add(gl, bl)
        txt_g = T("0", 30, SUN).next_to(l1, RIGHT, buff=0.3); txt_b = T("0", 30, MINT).next_to(l2, RIGHT, buff=0.3)
        self.add(txt_g, txt_b)
        for k in range(1, NG + 1):
            anims = []
            gl_new = VMobject(color=SUN, stroke_width=4).set_points_as_corners([c2p(p) for p in GDP[:k + 1]])
            self.remove(gl); gl = gl_new; self.add(gl)
            if k <= NB:
                bl_new = VMobject(color=MINT, stroke_width=4).set_points_as_corners([c2p(p) for p in BFP[:k + 1]])
                self.remove(bl); bl = bl_new; self.add(bl)
                self.add(Dot(c2p(BFP[k]), radius=0.06, color=MINT))
            self.add(Dot(c2p(GDP[k]), radius=0.06, color=SUN))
            new_g = T(str(k), 30, SUN).next_to(l1, RIGHT, buff=0.3)
            self.remove(txt_g); txt_g = new_g; self.add(txt_g)
            if k <= NB:
                new_b = T(str(k), 30, MINT).next_to(l2, RIGHT, buff=0.3); self.remove(txt_b); txt_b = new_b; self.add(txt_b)
            self.wait(0.28 if k > NB else 0.55)
        res = line({"vi": "%d bước  vs  %d bước" % (NG, NB), "en": "%d steps  vs  %d steps" % (NG, NB)}, 36, WHITE, -5.9)
        self.play(FadeIn(res), run_time=0.5)
        e = line(TX["end1"], 28, WHITE, -6.55) if False else None
        self.wait(3.2)

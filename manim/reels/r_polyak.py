from rl import *
f = lambda x: abs(x[0] - 1) + 2 * abs(x[1] + .5); sg = lambda v: float(np.sign(v))
XS = np.array([1.0, -0.5])
def run(rule, a, n, fe=0.0):
    x = np.array([-2.3, 1.7]); b = f(x); out = [b]; pts = [x.copy()]
    for k in range(n):
        g = np.array([sg(x[0] - 1), 2 * sg(x[1] + .5)], float); gg = g @ g
        if gg:
            s = a if rule == 'c' else a / (k + 1) if rule == 'd' else (f(x) - fe) / gg
            x = x - s * g; b = min(b, f(x))
        out.append(b); pts.append(x.copy())
    return out, pts
N = 60
PB, PP = run('p', .3, N); CB, CP = run('c', .3, N); DB, DP = run('d', .3, N)
HB, _ = run('p', .3, N, 0.3); LB_, _ = run('p', .3, N, -0.3)
assert PB[-1] < 1e-9 and CB[-1] > .1 and DB[-1] > 1 and abs(HB[-1] - 0.3) < 1e-6 and abs(LB_[-1] - 0.3) < 1e-6
KP = next(k for k in range(N + 1) if PB[k] < 1e-6)

class Polyak(Reel):
    def construct(self):
        self.title(L("Bước Polyak: dùng giá trị tối ưu\nđể chọn độ dài bước", "The Polyak step: use the optimal\nvalue to choose the step length"))
        self.stage(1)
        ax = plain_axes([-3, 2.6], [-2.4, 2.4], 7.6, 6.5, [0, 1.15, 0])
        P = lambda p: ax.c2p(p[0], p[1])
        dia = VGroup(*[Polygon(P((1 + c, -.5)), P((1, -.5 + c / 2)), P((1 - c, -.5)), P((1, -.5 - c / 2)), color="#2c3350", stroke_width=2.5) for c in (0.4, 1.0, 1.8, 2.8, 3.9)])
        self.play(Create(dia), run_time=1.2)
        st = Dot(P(XS), radius=0.1, color=MINT); s0 = Dot(P(PP[0]), radius=0.13, color=SUN); self.add(st, s0)
        self.say(L("f(x) = |x₁ − 1| + 2|x₂ + 0,5|: lồi, không trơn, đường mức hình thoi. f* = 0 tại (1; −0,5).",
                   "f(x) = |x₁ − 1| + 2|x₂ + 0.5|: convex, nonsmooth, diamond-shaped level sets. f* = 0 at (1, −0.5)."), hold=5.0)
        self.say(L("Phương pháp gradient dưới x⁺ = x − t·g. Câu hỏi: chọn t thế nào?", "Subgradient method x⁺ = x − t·g. The question: how to choose t?"))
        # key idea
        self.stage(2)
        self.readout(["hằng:      t = 0,3" if LANG == "vi" else "constant:     t = 0.3", "giảm dần:  t = 0,3/(k+1)" if LANG == "vi" else "diminishing:  t = 0.3/(k+1)", ("Polyak:    t = (f(x) − f*)/‖g‖²" if LANG == "vi" else "Polyak:       t = (f(x) − f*)/‖g‖²", SUN)], color=WHITE, size=24)
        self.say(L("Polyak: mô hình tuyến tính f(x) + gᵀ(y − x) chạm mức f* sau đúng một đoạn (f − f*)/‖g‖. Đi đúng đoạn đó.",
                   "Polyak: the linear model f(x) + gᵀ(y − x) reaches the level f* after exactly (f − f*)/‖g‖. Step exactly that far."), hold=5.5)
        self.say(L("Cái giá: phải biết f*. Ở đây ta biết f* = 0.", "The price: you must know f*. Here we do: f* = 0."))
        # algorithm
        self.stage(3)
        def rd(k):
            self.readout(["Polyak   k = %d" % k, "x = %s" % vec(PP[k], 4), ("f(x) = %s" % (sci(f(PP[k])) if f(PP[k]) < 1e-3 else nf(f(PP[k]), 4)), SUN)], color=SUN); self.wait(0.45)
        p1 = trail(self, ax, PP, s0, SUN, rt=0.7, ks=range(1, 9), cb=rd)
        p1b = trail(self, ax, PP[8:KP + 1], s0, SUN, rt=0.25, width=3)
        self.say(L("Mỗi bước nhắm thẳng tới mức f* = 0. Sau %d bước f < 10⁻⁶." % KP, "Each step aims straight at the level f* = 0. After %d steps f < 10⁻⁶." % KP))
        dc = Dot(P(CP[0]), radius=0.12, color=SKY); self.add(dc)
        self.say(L("Bước hằng t = 0,3 (xanh): tới gần rồi nảy qua lại quanh đáy mãi.", "Constant t = 0.3 (blue): gets close, then bounces around the bottom forever."), wait=False)
        p2 = trail(self, ax, CP, dc, SKY, rt=0.18, ks=range(1, 40), rate=linear, width=3)
        dd = Dot(P(DP[0]), radius=0.12, color=PINK); self.add(dd)
        self.say(L("Bước giảm dần 0,3/(k+1) (hồng): an toàn nhưng tổng các bước quá nhỏ, còn rất xa sau 60 bước.",
                   "Diminishing 0.3/(k+1) (pink): safe, but the steps add up too slowly; still far away after 60 steps."), wait=False)
        p3 = trail(self, ax, DP, dd, PINK, rt=0.12, ks=range(1, N + 1), rate=linear, width=3)
        self.wait(1.5)
        rows = [("  k    Polyak     hằng     giảm dần" if LANG == "vi" else "  k    Polyak     const    dimin.", WHITE)]
        for k in (5, 10, 30, 60):
            rows.append(("%3d    %-9s  %-7s  %s" % (k, nf(PB[k], 4), nf(CB[k], 2), nf(DB[k], 2)), WHITE))
        self.readout(rows, size=22)
        self.say(L("f_best sau k bước: Polyak về 0, bước hằng kẹt ở %s, bước giảm dần vẫn còn %s." % (nf(CB[-1], 1), nf(DB[-1], 2)),
                   "f_best after k steps: Polyak reaches 0, constant is stuck at %s, diminishing is still at %s." % (nf(CB[-1], 1), nf(DB[-1], 2))), hold=5.0)
        # contrast
        self.stage(4)
        rows = [("  k    f*=0 (đúng)  đoán 0,3   đoán −0,3" if LANG == "vi" else "  k    true f*=0   guess 0.3   guess −0.3", WHITE)]
        for k in (5, 10, 30, 60):
            rows.append(("%3d    %-11s  %-9s  %s" % (k, nf(PB[k], 4), nf(HB[k], 4), nf(LB_[k], 4)), WHITE))
        self.readout(rows, size=21)
        self.say(L("Nếu đoán sai f* chỉ 0,3, theo cả hai phía, f_best kẹt lại đúng ở mức 0,3 trên tối ưu.",
                   "If the guess of f* is off by just 0.3, in either direction, f_best gets stuck exactly 0.3 above optimal."), hold=5.0)
        self.say(L("Khi không biết f*, người ta dùng ước lượng động: hạ dần mức mục tiêu khi tiến triển chậm lại.",
                   "When f* is unknown, practical versions use a moving target level, lowered as progress stalls."))
        self.takeaway([L("Bước Polyak t = (f(x) − f*)/‖g‖²: không cần dò bước.", "Polyak step t = (f(x) − f*)/‖g‖²: no step-size tuning."),
                       L("Biết f* thì nó thắng xa bước hằng và bước giảm dần.", "Knowing f*, it beats constant and diminishing steps by far."),
                       L("Đoán sai f* một lượng δ thì kẹt cách tối ưu khoảng δ.", "Misjudge f* by δ and it stalls about δ from optimal.")])

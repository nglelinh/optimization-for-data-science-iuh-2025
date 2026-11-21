from rl import *
from o3lib import cd_gd
C9, NC, XO, F9 = cd_gd(.9, 'cd'); G9, NG, _, _ = cd_gd(.9, 'gd'); assert np.allclose(XO, [1, .5])
C99, NC99, _, _ = cd_gd(.99, 'cd'); C5, NC5, _, _ = cd_gd(.5, 'cd')
assert NC5 < NC < NC99
Q = np.array([[1, .9], [.9, 1]]); bb = np.array([1 + .45, .9 + .5])
for k in range(1, 7):
    assert abs(C9[2 * k - 1][0] - (bb[0] - .9 * C9[2 * k - 2][1])) < 1e-12
h = lambda x, y: abs(x - y) + 0.1 * (x + y) ** 2
T = np.linspace(-4, 4, 160001)
assert abs(T[np.argmin([h(t, 1.0) for t in T[::40]]) * 40] - 1.0) < 1e-3 if False else True
ix = T[np.argmin(np.abs(T - 1) + 0.1 * (T + 1) ** 2)]; assert abs(ix - 1) < 1e-3
iy = T[np.argmin(np.abs(1 - T) + 0.1 * (1 + T) ** 2)]; assert abs(iy - 1) < 1e-3
assert h(1, 1) == 0.4 and h(0, 0) == 0 and h(0.9, 0.9) < h(1, 1)

class Cd(Reel):
    def construct(self):
        self.title(L("Coordinate descent:\nmỗi lần một tọa độ", "Coordinate descent:\none coordinate at a time"))
        self.stage(1)
        ax = plain_axes([-2.6, 2.6], [-1.6, 2.6], 7.6, 6.1, [0, 1.15, 0])
        cs = contours(ax, lambda x, y: F9(np.array([x, y])), [F9(XO) + d for d in (0.02, 0.1, 0.3, 0.7, 1.3, 2.2, 3.4)], (-2.6, 2.6, -1.6, 2.6), N=70)
        self.play(Create(cs), run_time=1.2); self.add(Dot(ax.c2p(*XO), radius=0.1, color=MINT))
        self.say(L("f(x) = ½xᵀQx − bᵀx với Q = [[1; 0,9], [0,9; 1]]: hai biến liên kết mạnh, thung lũng nghiêng. x* = (1; 0,5).",
                   "f(x) = ½xᵀQx − bᵀx with Q = [[1, 0.9], [0.9, 1]]: two strongly coupled variables, a tilted valley. x* = (1, 0.5)."), hold=5.5)
        # key idea
        self.stage(2)
        self.readout(["x₁ ← argmin f(·, x₂) = b₁ − 0,9·x₂" if LANG == "vi" else "x₁ ← argmin f(·, x₂) = b₁ − 0.9·x₂", "x₂ ← argmin f(x₁, ·) = b₂ − 0,9·x₁" if LANG == "vi" else "x₂ ← argmin f(x₁, ·) = b₂ − 0.9·x₁"], color=SUN, size=24)
        self.say(L("Cố định mọi tọa độ trừ một, rồi cực tiểu đúng theo tọa độ đó: một bài 1 chiều có công thức. Lần lượt x₁, x₂, x₁, ...",
                   "Freeze all coordinates but one and minimize exactly over it: a 1-D problem with a formula. Then x₁, x₂, x₁, ..."), hold=5.5)
        # algorithm
        self.stage(3)
        d = Dot(ax.c2p(*C9[0]), radius=0.12, color=SUN); self.add(d)
        self.say(L("Bắt đầu từ (−2; 1,5). Mỗi chấm mới là một cực tiểu 1 chiều.", "Start at (−2, 1.5). Every new point is one 1-D minimization."), wait=False)
        def rd(k):
            self.readout(["lượt %d, tọa độ %d" % ((k + 1) // 2, 2 - k % 2) if LANG == "vi" else "sweep %d, coordinate %d" % ((k + 1) // 2, 2 - k % 2), "x = %s" % vec(C9[k], 4), ("f − f* = %s" % sci(max(F9(C9[k]) - F9(XO), 1e-16)), MINT)], color=SUN, size=23)
            self.wait(0.35)
        p1 = trail(self, ax, C9, d, SUN, rt=0.55, ks=range(1, 13), cb=rd)
        self.say(L("Đường đi là bậc thang: ngang, dọc, ngang, ... Mỗi bậc là một cực tiểu chính xác.", "The path is a staircase: across, up, across, ... Each step is an exact minimization."))
        p2 = trail(self, ax, [C9[12]] + C9[13:], d, SUN, rt=0.06, width=3, rate=linear)
        dg = Dot(ax.c2p(*G9[0]), radius=0.12, color=SKY); self.add(dg)
        self.say(L("So với gradient descent bước 1/L (xanh dương):", "Compare with gradient descent, step 1/L (blue):"), wait=False)
        p3 = trail(self, ax, G9, dg, SKY, rt=0.05, width=3, rate=linear, ks=range(1, NG + 1, max(1, NG // 60)))
        self.readout([("coordinate descent: %d lượt (%d bước 1 chiều)" % (NC, 2 * NC) if LANG == "vi" else "coordinate descent: %d sweeps (%d 1-D steps)" % (NC, 2 * NC), SUN), ("gradient descent:   %d bước" % NG if LANG == "vi" else "gradient descent:   %d steps" % NG, SKY)], size=23)
        self.say(L("Tới f − f* < 10⁻¹⁰: %d lượt CD so với %d bước GD. Mỗi bước CD lại rẻ hơn (chỉ một tọa độ)." % (NC, NG),
                   "To reach f − f* < 10⁻¹⁰: %d CD sweeps versus %d GD steps. And each CD step is cheaper (one coordinate)." % (NC, NG)), hold=5.0)
        rows = [("độ liên kết ρ    số lượt CD" if LANG == "vi" else "coupling ρ     CD sweeps", WHITE), ("%8s         %d" % (nf(0.5, 2), NC5), SKY), ("%8s         %d" % (nf(0.9, 2), NC), SUN), ("%8s         %d" % (nf(0.99, 2), NC99), PINK)]
        self.readout(rows, size=23)
        self.say(L("Biến càng liên kết, thung lũng càng hẹp và chéo, bậc thang càng nhỏ: ρ = 0,99 cần %d lượt." % NC99,
                   "The stronger the coupling, the narrower the diagonal valley and the tinier the stairs: ρ = 0.99 needs %d sweeps." % NC99), hold=5.0)
        # contrast
        self.stage(4); self.wipe()
        ax2 = plain_axes([-2, 2], [-2, 2], 6.6, 6.6, [0, 1.2, 0])
        cs2 = contours(ax2, h, [0.1, 0.4, 0.8, 1.3, 2.0, 2.8], (-2, 2, -2, 2), N=80, color="#3a4466")
        self.play(Create(cs2), run_time=1.2); self.add(Dot(ax2.c2p(0, 0), radius=0.1, color=MINT))
        self.say(L("Thất bại: f(x) = |x₁ − x₂| + 0,1(x₁ + x₂)², lồi nhưng không trơn. Cực tiểu f* = 0 tại gốc.",
                   "A failure: f(x) = |x₁ − x₂| + 0.1(x₁ + x₂)², convex but nonsmooth. Minimum f* = 0 at the origin."), hold=5.0)
        dd = Dot(ax2.c2p(1, 1), radius=0.13, color=PINK); self.play(FadeIn(dd, scale=1.4), run_time=0.3)
        for _ in range(2):
            self.play(dd.animate.shift(RIGHT * 0.5), run_time=0.35); self.play(dd.animate.move_to(ax2.c2p(1, 1)), run_time=0.35)
            self.play(dd.animate.shift(UP * 0.5), run_time=0.35); self.play(dd.animate.move_to(ax2.c2p(1, 1)), run_time=0.35)
        self.readout(["x = (1; 1),  f = 0,4" if LANG == "vi" else "x = (1, 1),  f = 0.4", ("argmin theo x₁: %s   theo x₂: %s" % (nf(ix, 3), nf(iy, 3)) if LANG == "vi" else "argmin over x₁: %s   over x₂: %s" % (nf(ix, 3), nf(iy, 3)), PINK)], color=WHITE, size=23)
        self.say(L("Tại (1; 1), đi theo riêng x₁ hay riêng x₂ đều làm f tăng: CD kẹt mãi ở f = 0,4. Nhưng hướng chéo (−1; −1) thì giảm.",
                   "At (1, 1), moving x₁ alone or x₂ alone both increase f: CD is stuck at f = 0.4 forever. Yet the diagonal (−1, −1) goes down."), hold=6.0)
        ar = Arrow(ax2.c2p(1, 1), ax2.c2p(0.35, 0.35), buff=0, color=MINT, stroke_width=6); self.play(GrowArrow(ar), run_time=0.5); self.wait(1.5)
        self.takeaway([L("Mỗi bước cực tiểu đúng theo một tọa độ: rẻ, không cần chọn bước.", "Each step minimizes exactly over one coordinate: cheap, no step size."),
                       L("Bài trơn: hội tụ, nhanh hơn GD ở đây (%d lượt so với %d bước)." % (NC, NG), "Smooth problems: converges, here faster than GD (%d sweeps vs %d steps)." % (NC, NG)),
                       L("Phần không trơn không tách được (như |x₁ − x₂|) có thể làm CD kẹt.", "A nonsmooth part that does not separate (like |x₁ − x₂|) can trap CD.")])

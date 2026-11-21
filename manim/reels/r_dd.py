from rl import *
W = np.array([1, 2, 4.]); A = np.array([3, 2, 1.]); BUD = 4.0
xs = lambda v: A - v / W
NU = 8 / 7; assert abs(xs(NU).sum() - BUD) < 1e-12
cost = lambda x: 0.5 * np.sum(W * (x - A) ** 2)
# central solution by KKT check
assert np.allclose(W * (xs(NU) - A) + NU, 0)
def run(a, n):
    nus = [0.0]
    for _ in range(n): nus.append(nus[-1] + a * (xs(nus[-1]).sum() - BUD))
    return nus
R1 = run(0.25, 16); assert abs(R1[-1] - NU) < 5e-3
SI = (1 / W).sum(); assert abs(SI - 1.75) < 1e-12
R2 = run(1.2, 8); assert abs(R2[-1] - NU) > abs(R2[1] - NU)
R3 = run(1 / SI, 2); assert abs(R3[1] - NU) < 1e-12

class Dec(Reel):
    def construct(self):
        self.title(L("Phân rã đối ngẫu:\nmột mức giá điều phối", "Dual decomposition:\na price coordinates the agents"))
        self.stage(1)
        base = -0.3; sc = 1.15; xpos = [-2.4, 0, 2.4]; cols = [SKY, PINK, ORANGE]
        axl = Line([-3.6, base, 0], [3.6, base, 0], color=DIM, stroke_width=2)
        tgt = VGroup(*[DashedLine([xpos[i] - 0.6, base + A[i] * sc, 0], [xpos[i] + 0.6, base + A[i] * sc, 0], color=cols[i], stroke_width=3) for i in range(3)])
        names = VGroup(*[Text(tr(L("tác tử %d", "agent %d")) % (i + 1), font=FONT, font_size=22, color=cols[i]).move_to([xpos[i], base - 0.35, 0]) for i in range(3)])
        wl = VGroup(*[Text("w = %d, a = %d" % (W[i], A[i]), font=MONO, font_size=19, color=DIM).move_to([xpos[i], base - 0.75, 0]) for i in range(3)])
        self.play(Create(axl), FadeIn(names), FadeIn(wl), Create(tgt), run_time=0.8)
        self.say(L("Ba tác tử, mỗi người muốn xᵢ gần aᵢ (vạch đứt), chi phí ½wᵢ(xᵢ − aᵢ)². Nhưng tổng chỉ được Σxᵢ = 4 (muốn 6).",
                   "Three agents, each wants xᵢ near aᵢ (dashed), cost ½wᵢ(xᵢ − aᵢ)². But the total is capped: Σxᵢ = 4 (they want 6)."), hold=6.0)
        # key idea
        self.stage(2)
        self.readout(["xᵢ(ν) = argmin ½wᵢ(xᵢ − aᵢ)² + ν·xᵢ = aᵢ − ν/wᵢ", "ν ← ν + α·(Σxᵢ(ν) − 4)"], color=SUN, size=22, y=-2.7)
        self.say(L("Đặt một giá ν cho tài nguyên. Mỗi tác tử tự giải bài riêng của mình với giá đó, không cần biết ai khác.",
                   "Put a price ν on the resource. Each agent solves its own problem at that price, knowing nothing about the others."), hold=5.0)
        self.say(L("Điều phối viên chỉ nhìn tổng: dùng quá thì tăng giá, dùng thiếu thì giảm giá. ν chính là nhân tử Lagrange.",
                   "The coordinator only looks at the total: over budget → raise the price, under → lower it. ν is the Lagrange multiplier."), hold=5.0)
        # algorithm
        self.stage(3)
        nu = ValueTracker(0.0)
        bars = always_redraw(lambda: VGroup(*[Rectangle(width=1.0, height=min(max(xs(nu.get_value())[i], 0.01), 3.5) * sc, stroke_width=0, fill_color=cols[i], fill_opacity=0.85).move_to([xpos[i], base + min(max(xs(nu.get_value())[i], 0.01), 3.5) * sc / 2, 0]) for i in range(3)]))
        self.add(bars)
        gauge = always_redraw(lambda: Text("ν = %s    Σx = %s / 4" % (nf(nu.get_value(), 3), nf(xs(nu.get_value()).sum(), 3)), font=MONO, font_size=26, color=WHITE if abs(xs(nu.get_value()).sum() - 4) > 0.01 else MINT).move_to([0, 4.0, 0]))
        self.add(gauge)
        self.say(L("α = 0,25. Bắt đầu với giá 0: mọi người lấy đúng aᵢ, tổng 6 > 4.", "α = 0.25. Start at price 0: everyone takes aᵢ, the total 6 > 4."), wait=False)
        rows = [("  k    ν        x₁      x₂      x₃      Σx", WHITE)]
        for k in range(0, 17):
            self.play(nu.animate.set_value(R1[k]), run_time=0.55 if k < 6 else 0.3)
            x = xs(R1[k]); rows.append(("%3d   %-7s  %-6s  %-6s  %-6s  %s" % (k, nf(R1[k], 3), nf(x[0], 2), nf(x[1], 2), nf(x[2], 2), nf(x.sum(), 3)), SUN))
            if len(rows) > 5: rows = [rows[0]] + rows[-4:]
            self.readout(rows, size=19, y=-2.9); self.wait(0.35 if k < 6 else 0.15)
        self.say(L("Giá hội tụ về ν* = 8/7 ≈ 1,143; tổng đúng bằng 4. Tác tử có wᵢ nhỏ (ít ngại lệch) nhường nhiều nhất.",
                   "The price converges to ν* = 8/7 ≈ 1.143 and the total hits 4. The agent with small wᵢ (least picky) gives up the most."), hold=5.5)
        # contrast
        self.stage(4)
        self.play(nu.animate.set_value(0), run_time=0.5)
        self.say(L("Đối chiếu: bước giá α = 1,2. Mỗi bước, sai lệch giá bị nhân với 1 − α·Σ1/wᵢ = 1 − 1,2·1,75 = −1,1.",
                   "Contrast: price step α = 1.2. Each step multiplies the price error by 1 − α·Σ1/wᵢ = 1 − 1.2·1.75 = −1.1."), hold=5.0)
        rows = [("  k    ν (α = 1,2)    Σx" if LANG == "vi" else "  k    ν (α = 1.2)    Σx", WHITE)]
        for k in range(0, 9):
            self.play(nu.animate.set_value(R2[k]), run_time=0.45)
            rows.append(("%3d   %-12s  %s" % (k, nf(R2[k], 3), nf(xs(R2[k]).sum(), 3)), PINK))
            if len(rows) > 5: rows = [rows[0]] + rows[-4:]
            self.readout(rows, size=21, y=-2.9); self.wait(0.25)
        self.say(L("Giá dao động và phình ra: phân kỳ. Ổn định cần α < 2/1,75 ≈ 1,14; α = 1/1,75 ≈ 0,571 tới ν* chỉ sau 1 bước.",
                   "The price oscillates and grows: divergence. Stability needs α < 2/1.75 ≈ 1.14; α = 1/1.75 ≈ 0.571 hits ν* in one step."), hold=6.0)
        self.play(nu.animate.set_value(R3[1]), run_time=0.8); self.wait(1.0)
        self.takeaway([L("Giá ν tách bài toán lớn thành các bài nhỏ giải độc lập.", "A price ν splits the big problem into small ones solved independently."),
                       L("Điều phối viên tăng/giảm giá theo phần dư Σxᵢ − 4: đi lên đối ngẫu.", "The coordinator moves the price by the excess Σxᵢ − 4: dual ascent."),
                       L("Bước giá quá lớn thì dao động và phân kỳ.", "Too large a price step oscillates and diverges.")])

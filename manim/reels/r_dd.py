from rl import *
# Bài 20-02-01: phân rã đối ngẫu — ba tác tử chia một ngân sách, điều phối bằng một mức giá ν
W = np.array([1, 2, 4.]); A = np.array([3, 2, 1.]); BUD = 4.0
xs = lambda v: A - v / W
NU = 8 / 7; assert abs(xs(NU).sum() - BUD) < 1e-12
cost = lambda x: 0.5 * np.sum(W * (x - A) ** 2)
assert np.allclose(W * (xs(NU) - A) + NU, 0)                       # KKT: wᵢ(xᵢ − aᵢ) + ν = 0
XST = xs(NU); assert np.allclose(XST, [13 / 7, 10 / 7, 5 / 7]) and np.allclose(W * (A - XST), NU)   # chi phí biên bằng nhau
SI = (1 / W).sum(); assert abs(SI - 1.75) < 1e-12
gd = lambda v: cost(xs(v)) + v * (xs(v).sum() - BUD)               # hàm đối ngẫu g(ν) = min_x L(x, ν)
assert all(np.isclose(gd(v), 2 * v - 0.875 * v * v) for v in np.linspace(0, 3, 13))
assert np.isclose(gd(NU), 8 / 7) and np.isclose(cost(XST), 8 / 7)  # khoảng cách đối ngẫu bằng 0
# x(ν) đúng là argmin của bài con: so với lưới
for v in (0.3, NU, 2.0):
    g_ = np.linspace(-3, 5, 80001)
    for i in range(3): assert abs(g_[np.argmin(0.5 * W[i] * (g_ - A[i]) ** 2 + v * g_)] - xs(v)[i]) < 2e-4
def run(a, n):
    nus = [0.0]
    for _ in range(n): nus.append(nus[-1] + a * (xs(nus[-1]).sum() - BUD))
    return nus
R1 = run(0.25, 16); assert abs(R1[-1] - NU) < 5e-3
assert all(gd(R1[k + 1]) >= gd(R1[k]) - 1e-12 for k in range(16))  # đi lên đối ngẫu: g tăng dần
R2 = run(1.2, 8); assert abs(R2[-1] - NU) > abs(R2[1] - NU)
R3 = run(1 / SI, 2); assert abs(R3[1] - NU) < 1e-12
assert np.isclose(1 - 1.2 * SI, -1.1) and np.isclose(1 - 0.25 * SI, 0.5625)
# giá bóng: chi phí tối ưu theo ngân sách c là (6 − c)²/(2·1,75), đạo hàm = −ν*
cstar = lambda c: (6 - c) ** 2 / (2 * SI)
assert np.isclose(cstar(4), 8 / 7) and np.isclose(cstar(5), 2 / 7) and np.isclose((cstar(4 - 1e-6) - cstar(4 + 1e-6)) / 2e-6, NU, atol=1e-6)
VI = LANG == "vi"

class Dec(Reel):
    def construct(self):
        self.title(L("Phân rã đối ngẫu:\nmột mức giá điều phối", "Dual decomposition:\na price coordinates the agents"))
        # ---- stage 1
        self.stage(1)
        base = -0.3; sc = 1.15; xpos = [-2.4, 0, 2.4]; cols = [SKY, PINK, ORANGE]
        axl = Line([-3.6, base, 0], [3.6, base, 0], color=DIM, stroke_width=2)
        tgt = VGroup(*[DashedLine([xpos[i] - 0.6, base + A[i] * sc, 0], [xpos[i] + 0.6, base + A[i] * sc, 0], color=cols[i], stroke_width=3) for i in range(3)])
        names = VGroup(*[Text(tr(L("tác tử %d", "agent %d")) % (i + 1), font=FONT, font_size=22, color=cols[i]).move_to([xpos[i], base - 0.35, 0]) for i in range(3)])
        wl = VGroup(*[Text("w = %d, a = %d" % (W[i], A[i]), font=MONO, font_size=19, color=DIM).move_to([xpos[i], base - 0.75, 0]) for i in range(3)])
        scene1 = VGroup(axl, names, wl, tgt)
        self.play(Create(axl), FadeIn(names), FadeIn(wl), Create(tgt), run_time=0.8)
        self.say(L("Ba tác tử chia nhau một nguồn tài nguyên, ví dụ 4 đơn vị điện. Người thứ i muốn lấy aᵢ (vạch đứt), lệch đi thì chịu chi phí ½wᵢ(xᵢ − aᵢ)².",
                   "Three agents share one resource, say 4 units of power. Agent i wants aᵢ (dashed); deviating costs ½wᵢ(xᵢ − aᵢ)²."), hold=9.5)
        self.readout(["min  Σ ½wᵢ(xᵢ − aᵢ)²   s.t.  x₁ + x₂ + x₃ = 4" if not VI else "min  Σ ½wᵢ(xᵢ − aᵢ)²   với  x₁ + x₂ + x₃ = 4", ("cả ba cộng lại muốn 3 + 2 + 1 = 6 > 4" if VI else "together they want 3 + 2 + 1 = 6 > 4", PINK)], color=WHITE, size=23, y=-2.7)
        self.say(L("Tổng chỉ có 4 mà cả ba muốn 6. Đây đúng dạng của bài 20-02-01: mục tiêu tách theo từng người, chỉ dính nhau ở một ràng buộc tuyến tính.",
                   "Only 4 exist but together they want 6. This is exactly the form in lesson 20-02-01: the objective splits per agent, coupled only by one linear constraint."), hold=10.0)
        # ---- stage 2
        self.stage(2); self.clear_ro(); self.play(FadeOut(scene1), run_time=0.4)
        hub = VGroup(RoundedRectangle(corner_radius=0.15, width=3.4, height=0.7, stroke_color=SUN, stroke_width=3, fill_color=CARD, fill_opacity=1),
                     Text(tr(L("điều phối viên", "coordinator")), font=FONT, font_size=22, color=SUN)).move_to([0, 3.85, 0]); hub[1].move_to(hub[0])
        ags = VGroup(*[VGroup(RoundedRectangle(corner_radius=0.15, width=1.8, height=0.65, stroke_color=cols[i], stroke_width=3, fill_color=CARD, fill_opacity=1),
                              Text(tr(L("tác tử %d", "agent %d")) % (i + 1), font=FONT, font_size=20, color=cols[i])).move_to([xpos[i], 1.85, 0]) for i in range(3)])
        for g_ in ags: g_[1].move_to(g_[0])
        down = VGroup(*[Arrow(hub.get_bottom() + [x0 * 0.3 - 0.15, 0, 0], ags[i].get_top() + [-0.2, 0, 0], buff=0.05, color=SUN, stroke_width=3, max_tip_length_to_length_ratio=0.12) for i, x0 in enumerate(xpos)])
        up = VGroup(*[Arrow(ags[i].get_top() + [0.2, 0, 0], hub.get_bottom() + [x0 * 0.3 + 0.15, 0, 0], buff=0.05, color=cols[i], stroke_width=3, max_tip_length_to_length_ratio=0.12) for i, x0 in enumerate(xpos)])
        lab_d = Text(tr(L("phát giá ν", "broadcast ν")), font=FONT, font_size=19, color=SUN).move_to([-2.6, 3.0, 0])
        lab_u = Text(tr(L("gửi lại xᵢ", "send back xᵢ")), font=FONT, font_size=19, color=WHITE).move_to([2.6, 3.0, 0])
        self.play(FadeIn(hub), FadeIn(ags), run_time=0.5)
        self.readout(["L(x, ν) = Σ [½wᵢ(xᵢ − aᵢ)² + ν·xᵢ] − 4ν", ("∂L/∂xᵢ = wᵢ(xᵢ − aᵢ) + ν = 0", SUN), ("⇒  xᵢ(ν) = aᵢ − ν/wᵢ", SUN)], color=WHITE, size=24, y=-0.3)
        self.say(L("Đặt một giá ν cho mỗi đơn vị tài nguyên. Lagrangian tách thành ba phần riêng, mỗi tác tử tự giải phần của mình: đạo hàm bằng 0 cho xᵢ = aᵢ − ν/wᵢ.",
                   "Put a price ν on each unit of the resource. The Lagrangian splits into three separate parts and each agent solves its own: setting the derivative to 0 gives xᵢ = aᵢ − ν/wᵢ."), hold=11.0)
        self.play(GrowArrow(down[0]), GrowArrow(down[1]), GrowArrow(down[2]), FadeIn(lab_d), run_time=0.6)
        self.play(GrowArrow(up[0]), GrowArrow(up[1]), GrowArrow(up[2]), FadeIn(lab_u), run_time=0.6)
        self.readout(["L(x, ν) = Σ [½wᵢ(xᵢ − aᵢ)² + ν·xᵢ] − 4ν", ("∂L/∂xᵢ = wᵢ(xᵢ − aᵢ) + ν = 0", SUN), ("⇒  xᵢ(ν) = aᵢ − ν/wᵢ", SUN), ("ν ← ν + α·(x₁ + x₂ + x₃ − 4)", MINT)], color=WHITE, size=24, y=-0.3)
        self.say(L("Mỗi vòng có hai bước như hình của bài: phát giá ν cho mọi người, thu về các xᵢ. Dùng quá thì tăng giá, dùng thiếu thì giảm giá. Không ai cần biết hàm chi phí của người khác.",
                   "Each round has two steps, as in the lesson's figure: broadcast ν to everyone, gather the xᵢ. Over budget → raise the price, under → lower it. Nobody needs the others' cost functions."), hold=11.5)
        self.play(FadeOut(VGroup(hub, ags, down, up, lab_d, lab_u)), run_time=0.4); self.clear_ro()
        gx = plain_axes([0, 2.4], [0, 1.4], 6.8, 3.4, [0.2, 1.9, 0])
        gc = gx.plot(lambda v: gd(v), x_range=[0, 2.29], color=SUN, stroke_width=4)
        gl = Text("g(ν) = 2ν − 0,875ν²" if VI else "g(ν) = 2ν − 0.875ν²", font=MONO, font_size=22, color=SUN).next_to(gx.c2p(0.05, 1.38), RIGHT, buff=0)
        nl = Text("ν", font=MONO, font_size=22, color=DIM).next_to(gx.c2p(2.4, 0), DOWN, buff=0.12)
        top = DashedLine(gx.c2p(NU, 0), gx.c2p(NU, gd(NU)), color=MINT, stroke_width=2.5)
        self.play(Create(gx), Create(gc), FadeIn(gl), FadeIn(nl), run_time=1.0)
        self.readout(["g(ν) = min_x L(x, ν)", "g′(ν) = x₁(ν) + x₂(ν) + x₃(ν) − 4", ("ν* = 2/1,75 = 8/7 ≈ 1,143" if VI else "ν* = 2/1.75 = 8/7 ≈ 1.143", MINT)], color=WHITE, size=24, y=-1.2)
        self.play(Create(top), run_time=0.5)
        self.say(L("Thay xᵢ(ν) vào ta được hàm đối ngẫu g(ν) = 2ν − 0,875ν², một parabol lõm. Đạo hàm của nó chính là phần vượt ngân sách, nên cập nhật giá là đi lên theo gradient của g.",
                   "Plugging xᵢ(ν) back gives the dual function g(ν) = 2ν − 0.875ν², a concave parabola. Its derivative is exactly the budget excess, so the price update is gradient ascent on g."), hold=12.0)
        gdots = VGroup(*[Dot(gx.c2p(v, gd(v)), radius=0.07, color=WHITE) for v in R1[:9]])
        self.play(LaggedStart(*[FadeIn(d_) for d_ in gdots], lag_ratio=0.25), run_time=1.6)
        self.say(L("Các chấm trắng: những mức giá mà thuật toán sẽ thử, leo dần lên đỉnh parabol tại ν* = 8/7.",
                   "The white dots: the prices the algorithm will try, climbing toward the top of the parabola at ν* = 8/7."), hold=7.0)
        # ---- stage 3
        self.stage(3); self.clear_ro(); self.play(FadeOut(VGroup(gx, gc, gl, nl, top, gdots)), run_time=0.4)
        self.play(FadeIn(scene1), run_time=0.4)
        nu = ValueTracker(0.0)
        bars = always_redraw(lambda: VGroup(*[Rectangle(width=1.0, height=min(max(xs(nu.get_value())[i], 0.01), 3.5) * sc, stroke_width=0, fill_color=cols[i], fill_opacity=0.85).move_to([xpos[i], base + min(max(xs(nu.get_value())[i], 0.01), 3.5) * sc / 2, 0]) for i in range(3)]))
        self.add(bars)
        gauge = always_redraw(lambda: Text("ν = %s    Σx = %s / 4" % (nf(nu.get_value(), 3), nf(xs(nu.get_value()).sum(), 3)), font=MONO, font_size=26, color=WHITE if abs(xs(nu.get_value()).sum() - 4) > 0.01 else MINT).move_to([0, 4.0, 0]))
        self.add(gauge)
        self.say(L("α = 0,25. Bắt đầu với giá 0: mọi người lấy đúng aᵢ, tổng 6 > 4, nên giá phải tăng.", "α = 0.25. Start at price 0: everyone takes aᵢ, the total 6 > 4, so the price must rise."), wait=False)
        rows = [("  k    ν        x₁      x₂      x₃      Σx", WHITE)]
        for k in range(0, 17):
            self.play(nu.animate.set_value(R1[k]), run_time=0.6 if k < 6 else 0.3)
            x = xs(R1[k]); rows.append(("%3d   %-7s  %-6s  %-6s  %-6s  %s" % (k, nf(R1[k], 3), nf(x[0], 2), nf(x[1], 2), nf(x[2], 2), nf(x.sum(), 3)), SUN))
            if len(rows) > 5: rows = [rows[0]] + rows[-4:]
            self.readout(rows, size=19, y=-2.9); self.wait(0.45 if k < 6 else 0.15)
            if k == 1:
                self.say(L("Vòng 1: Σx = 6, vượt 2, nên ν tăng 0,25 × 2 = 0,5. Mỗi tác tử tự giảm phần của mình theo giá mới.",
                           "Round 1: Σx = 6, over by 2, so ν rises by 0.25 × 2 = 0.5. Each agent cuts its own share at the new price."), wait=False)
        self.say(L("Giá hội tụ về ν* = 8/7 ≈ 1,143, tổng đúng bằng 4. Sai lệch giá giảm mỗi vòng theo hệ số 1 − 0,25·1,75 = 0,5625.",
                   "The price converges to ν* = 8/7 ≈ 1.143 and the total hits 4. The price error shrinks each round by the factor 1 − 0.25·1.75 = 0.5625."), hold=9.0)
        mc = tuple(nf(v, 3) for v in W * (A - XST))
        self.readout([("x* = (13/7; 10/7; 5/7)" if VI else "x* = (13/7, 10/7, 5/7)", MINT), ("   ≈ %s" % vec(XST, 3), MINT),
                      ("chi phí biên wᵢ(aᵢ − xᵢ*):" if VI else "marginal cost wᵢ(aᵢ − xᵢ*):", SUN), (("= %s; %s; %s = ν*" if VI else "= %s, %s, %s = ν*") % mc, SUN),
                      ("chi phí = g(ν*) = 8/7 ≈ %s" % nf(cost(XST), 3) if VI else "cost = g(ν*) = 8/7 ≈ %s" % nf(cost(XST), 3), WHITE), ("khoảng cách đối ngẫu = 0" if VI else "duality gap = 0", WHITE)], size=20, y=-2.85)
        self.say(L("Kiểm tra nghiệm: x* = (1,857; 1,429; 0,714). Chi phí biên của cả ba đều bằng đúng ν* = 1,143: không ai muốn đổi thêm một đơn vị với người khác.",
                   "Check the answer: x* = (1.857, 1.429, 0.714). All three marginal costs equal ν* = 1.143 exactly: nobody wants to trade one more unit with anyone."), hold=11.0)
        self.say(L("Tác tử 3 (w = 4, ngại lệch nhất) chỉ nhường 0,29; tác tử 1 (w = 1) nhường nhiều nhất, 1,14. Tổng chi phí 8/7 đúng bằng g(ν*): đối ngẫu mạnh.",
                   "Agent 3 (w = 4, the pickiest) gives up only 0.29; agent 1 (w = 1) gives up the most, 1.14. The total cost 8/7 equals g(ν*): strong duality."), hold=10.0)
        # ---- stage 4
        self.stage(4)
        self.play(nu.animate.set_value(0), run_time=0.5)
        self.say(L("Đối chiếu: bước giá α = 1,2. Mỗi vòng, sai lệch giá bị nhân với 1 − α·Σ1/wᵢ = 1 − 1,2·1,75 = −1,1.",
                   "Contrast: price step α = 1.2. Each round multiplies the price error by 1 − α·Σ1/wᵢ = 1 − 1.2·1.75 = −1.1."), hold=7.5)
        rows = [("  k    ν (α = 1,2)    Σx" if VI else "  k    ν (α = 1.2)    Σx", WHITE)]
        for k in range(0, 9):
            self.play(nu.animate.set_value(R2[k]), run_time=0.45)
            rows.append(("%3d   %-12s  %s" % (k, nf(R2[k], 3), nf(xs(R2[k]).sum(), 3)), PINK))
            if len(rows) > 5: rows = [rows[0]] + rows[-4:]
            self.readout(rows, size=21, y=-2.9); self.wait(0.25)
        self.say(L("Giá dao động và phình ra: phân kỳ. Ổn định cần α < 2/1,75 ≈ 1,14; còn α = 1/1,75 ≈ 0,571 tới ν* chỉ sau 1 bước.",
                   "The price oscillates and grows: divergence. Stability needs α < 2/1.75 ≈ 1.14; α = 1/1.75 ≈ 0.571 hits ν* in one step."), hold=9.0)
        self.play(nu.animate.set_value(R3[1]), run_time=0.8)
        self.readout([("ngân sách 4:  ν* = %s,  chi phí %s" % (nf(NU, 3), nf(cstar(4), 3)) if VI else "budget 4:  ν* = %s,  cost %s" % (nf(NU, 3), nf(cstar(4), 3)), MINT), ("ngân sách 5:  ν* = %s,  chi phí %s" % (nf(4 / 7, 3), nf(cstar(5), 3)) if VI else "budget 5:  ν* = %s,  cost %s" % (nf(4 / 7, 3), nf(cstar(5), 3)), SKY),
                      ("d(chi phí)/d(ngân sách) = −ν*" if VI else "d(cost)/d(budget) = −ν*", SUN)], size=23, y=-2.9)
        self.say(L("ν* còn là giá bóng: thêm một chút tài nguyên quanh mức 4 thì chi phí giảm khoảng 1,143 cho mỗi đơn vị. Nâng hẳn lên 5 thì giá rơi còn 0,571, chi phí còn 0,286.",
                   "ν* is also the shadow price: a little more resource around 4 lowers the cost by about 1.143 per unit. Raising it all the way to 5 drops the price to 0.571 and the cost to 0.286."), hold=11.0)
        self.takeaway([L("Giá ν tách bài toán lớn thành các bài nhỏ, giải độc lập và song song.", "A price ν splits the big problem into small ones, solved independently and in parallel."),
                       L("Cập nhật giá theo phần dư Σxᵢ − 4 là đi lên gradient của hàm đối ngẫu.", "Updating the price by the excess Σxᵢ − 4 is gradient ascent on the dual function."),
                       L("Tại ν*, chi phí biên của mọi tác tử bằng nhau và bằng ν*.", "At ν*, every agent's marginal cost is the same and equals ν*."),
                       L("Bước giá quá lớn thì dao động và phân kỳ.", "Too large a price step oscillates and diverges.")], tail=4.0)

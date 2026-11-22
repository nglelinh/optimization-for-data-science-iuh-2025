from rl import *
# Bài 12-03: min −Σ log(αᵢ + xᵢ) s.t. x ≥ 0, 1ᵀx = 1. Ví dụ số: α = (0,1; 0,4; 0,8; 1,2)
AL = np.array([0.1, 0.4, 0.8, 1.2]); n = 4
tot = lambda Lv: np.maximum(0, Lv - AL).sum()
lo, hi = 0.0, 3.0
for _ in range(200):
    mid = (lo + hi) / 2; lo, hi = (mid, hi) if tot(mid) < 1 else (lo, mid)
LV = (lo + hi) / 2; XS = np.maximum(0, LV - AL); NU = 1 / LV; LAM = NU - 1 / (AL + XS)
assert abs(LV - 0.75) < 1e-12 and np.allclose(XS, [.65, .35, 0, 0]) and abs(NU - 4 / 3) < 1e-12
assert np.allclose(LAM, [0, 0, 1 / 12, .5]) and (LAM >= -1e-12).all() and np.allclose(LAM * XS, 0) and abs(XS.sum() - 1) < 1e-12
assert np.allclose(-1 / (AL + XS) - LAM + NU, 0)
fobj = lambda x: -np.sum(np.log(AL + x)); FS = fobj(XS)
r = np.random.default_rng(0); Z = r.dirichlet(np.ones(4), 200000); assert (np.array([fobj(z) for z in Z[:20000]]) >= FS - 1e-12).all()
# độ nhạy: ép x₄ = ε, phần còn lại đổ nước như cũ → mục tiêu tăng ≈ λ₄·ε
def wf(total, al):
    lo_, hi_ = 0.0, 5.0
    for _ in range(200):
        m_ = (lo_ + hi_) / 2; lo_, hi_ = (m_, hi_) if np.maximum(0, m_ - al).sum() < total else (lo_, m_)
    return np.maximum(0, (lo_ + hi_) / 2 - al)
EPS = 1e-3; XE = np.r_[wf(1 - EPS, AL[:3]), EPS]; assert abs((fobj(XE) - FS) / EPS - LAM[3]) < 0.01
# đoán sai 1: mọi ràng buộc xᵢ ≥ 0 không hoạt động (λ = 0)
L1 = (1 + AL.sum()) / 4; X1 = L1 - AL; assert abs(L1 - .875) < 1e-12 and X1[3] < 0 and np.allclose(X1, [.775, .475, .075, -.325])
# đoán sai 2: chỉ kênh 1 có công suất
X2 = np.array([1., 0, 0, 0]); NU2 = 1 / (AL[0] + 1); LAM2 = NU2 - 1 / (AL + X2); assert LAM2[1] < 0 and abs(LAM2[1] - (1 / 1.1 - 2.5)) < 1e-12
# đoán sai 3: ba kênh
L3 = (1 + AL[:3].sum()) / 3; X3 = L3 - AL[:3]; assert X3[2] < 0 and abs(L3 - 2.3 / 3) < 1e-12

class KktW(Reel):
    def bars(self, y0=0.2, w=1.3):
        g = VGroup(); xs = [-2.4 + 1.6 * i for i in range(n)]; s = 2.4
        for i in range(n):
            r_ = Rectangle(width=w, height=AL[i] * s, fill_color="#4a5578", fill_opacity=1, stroke_width=0).move_to([xs[i], y0 + AL[i] * s / 2, 0])
            g.add(r_)
        base = Line([-3.4, y0, 0], [3.4, y0, 0], color=DIM, stroke_width=2)
        labs = VGroup(*[Text("α%s = %s" % ("₁₂₃₄"[i], nf(AL[i], 1)), font=MONO, font_size=19, color=DIM).move_to([xs[i], y0 - 0.3, 0]) for i in range(n)])
        return g, base, labs, xs, s

    def construct(self):
        self.title(L("KKT qua ví dụ đổ nước:\nràng buộc nào hoạt động?", "KKT through water-filling:\nwhich constraints are active?"))
        self.stage(1)
        self.readout(["min  −Σ log(αᵢ + xᵢ)", "với  xᵢ ≥ 0,  x₁ + x₂ + x₃ + x₄ = 1" if LANG == "vi" else "s.t. xᵢ ≥ 0,  x₁ + x₂ + x₃ + x₄ = 1"], color=WHITE, size=25, y=3.7)
        self.say(L("Bài 12-03: chia 1 đơn vị công suất cho n kênh để tổng tốc độ Σ log(αᵢ + xᵢ) lớn nhất. αᵢ là mức nhiễu nền của kênh i.",
                   "Lesson 12-03: split 1 unit of power over n channels to maximize the total rate Σ log(αᵢ + xᵢ). αᵢ is the noise floor of channel i."), hold=7.0)
        g, base, labs, xs, s = self.bars(); self.play(Create(base), FadeIn(g), FadeIn(labs), run_time=0.8)
        self.say(L("Ví dụ số: n = 4, α = (0,1; 0,4; 0,8; 1,2). Kênh 1 tốt nhất (nhiễu thấp), kênh 4 tệ nhất.",
                   "A numeric case: n = 4, α = (0.1, 0.4, 0.8, 1.2). Channel 1 is best (low noise), channel 4 is worst."), hold=6.0)
        self.say(L("Nên cho kênh nào bao nhiêu? log tăng nhanh khi gần 0 và chậm dần sau đó, nên kênh nhiễu thấp được lợi nhiều hơn, nhưng dồn hết vào một kênh cũng không tốt.",
                   "How much should each channel get? log grows fast near 0 and slower later, so low-noise channels gain more, but putting everything into one channel is not good either."), hold=7.5)
        self.say(L("Mục tiêu lồi, ràng buộc tuyến tính, và có điểm trong khả thi (xᵢ = 0,25). Vậy KKT vừa cần vừa đủ: giải KKT là giải xong bài toán.",
                   "Convex objective, linear constraints, and a strictly feasible point (xᵢ = 0.25). So KKT is necessary and sufficient: solving KKT solves the problem."), hold=7.5)
        # ---- stage 2
        self.stage(2)
        self.readout([("tính dừng:   −1/(αᵢ + xᵢ) − λᵢ + ν = 0" if LANG == "vi" else "stationarity:  −1/(αᵢ + xᵢ) − λᵢ + ν = 0", WHITE), ("khả thi:     xᵢ ≥ 0,  Σxᵢ = 1" if LANG == "vi" else "primal feas.:  xᵢ ≥ 0,  Σxᵢ = 1", WHITE), ("đối ngẫu:    λᵢ ≥ 0" if LANG == "vi" else "dual feas.:    λᵢ ≥ 0", SUN), ("bù:          λᵢ·xᵢ = 0" if LANG == "vi" else "compl. slack.: λᵢ·xᵢ = 0", MINT)], size=22)
        self.say(L("Nhân tử λᵢ cho ràng buộc xᵢ ≥ 0, ν cho ràng buộc tổng. Bốn nhóm điều kiện KKT như bài 12-01.",
                   "Multiplier λᵢ for xᵢ ≥ 0, ν for the sum constraint. The four groups of KKT conditions, as in lesson 12-01."), hold=6.0)
        self.say(L("Điều kiện bù λᵢ·xᵢ = 0 chia mỗi kênh thành đúng hai trường hợp.", "Complementary slackness λᵢ·xᵢ = 0 splits each channel into exactly two cases."), hold=4.5)
        c1 = VGroup(Text(L("xᵢ > 0 (không hoạt động) ⇒ λᵢ = 0", "xᵢ > 0 (inactive) ⇒ λᵢ = 0")[LANG], font=FONT, font_size=22, color=SKY), Text("⇒ xᵢ = 1/ν − αᵢ", font=FONT, font_size=22, color=SKY)).arrange(DOWN, buff=0.08).move_to([0, -0.85, 0])
        c2 = VGroup(Text(L("xᵢ = 0 (hoạt động) ⇒ λᵢ = ν − 1/αᵢ", "xᵢ = 0 (active) ⇒ λᵢ = ν − 1/αᵢ")[LANG], font=FONT, font_size=22, color=PINK), Text("λᵢ ≥ 0 ⇒ αᵢ ≥ 1/ν", font=FONT, font_size=22, color=PINK)).arrange(DOWN, buff=0.08).move_to([0, -1.85, 0])
        self.play(FadeIn(c1), run_time=0.4)
        self.say(L("Ràng buộc không hoạt động (xᵢ > 0) thì nhân tử bằng 0. Tính dừng cho xᵢ = 1/ν − αᵢ: mực nước 1/ν trừ đáy αᵢ.",
                   "An inactive constraint (xᵢ > 0) has a zero multiplier. Stationarity gives xᵢ = 1/ν − αᵢ: the water level 1/ν minus the floor αᵢ."), hold=7.0)
        self.play(FadeIn(c2), run_time=0.4)
        self.say(L("Ràng buộc hoạt động (xᵢ = 0) thì λᵢ = ν − 1/αᵢ, và dấu λᵢ ≥ 0 đòi αᵢ ≥ 1/ν: đáy cao hơn mực nước.",
                   "An active constraint (xᵢ = 0) has λᵢ = ν − 1/αᵢ, and the sign λᵢ ≥ 0 requires αᵢ ≥ 1/ν: the floor sits above the water level."), hold=7.0)
        self.say(L("Gộp lại: xᵢ = max(0; 1/ν − αᵢ). Chỉ còn tìm mực nước sao cho tổng bằng 1.", "Together: xᵢ = max(0, 1/ν − αᵢ). All that is left is the water level that makes the sum equal 1."), hold=5.5)
        self.play(FadeOut(VGroup(c1, c2)), run_time=0.3)
        # ---- stage 3
        self.stage(3); self.clear_ro()
        y0 = 0.2
        water = VGroup()
        lvl = ValueTracker(0.0)
        def mk_water():
            Lv = lvl.get_value(); gg = VGroup()
            for i in range(n):
                h = max(0.0, Lv - AL[i]) * s
                if h > 1e-4: gg.add(Rectangle(width=1.3, height=h, fill_color=SKY, fill_opacity=0.75, stroke_width=0).move_to([xs[i], y0 + AL[i] * s + h / 2, 0]))
            ln = DashedLine([-3.4, y0 + Lv * s, 0], [3.4, y0 + Lv * s, 0], color=SKY, stroke_width=2.5)
            gg.add(ln); return gg
        wat = always_redraw(mk_water); self.add(wat)
        def ro():
            Lv = lvl.get_value(); self.readout([("mực nước 1/ν = %s" % nf(Lv, 3) if LANG == "vi" else "water level 1/ν = %s" % nf(Lv, 3), SKY), ("tổng nước Σxᵢ = %s" % nf(tot(Lv), 3) if LANG == "vi" else "total water Σxᵢ = %s" % nf(tot(Lv), 3), WHITE)], size=24)
        self.say(L("Đổ nước: nâng mực nước dần lên. Nước chỉ vào kênh có đáy thấp hơn mực nước.", "Pour water: raise the level slowly. Water only fills channels whose floor is below the level."), wait=False)
        for target in (0.4, 0.6, 0.75):
            self.play(lvl.animate.set_value(target), run_time=2.0, rate_func=linear); ro(); self.wait(1.2)
        self.say(L("Dừng ở mực 1/ν = 0,75: tổng nước đúng bằng 1. Nước chưa chạm tới đáy kênh 3 (0,8) và kênh 4 (1,2).",
                   "Stop at level 1/ν = 0.75: the total is exactly 1. The water has not reached the floors of channel 3 (0.8) and channel 4 (1.2)."), hold=7.0)
        self.remove(wat); wat2 = mk_water(); self.add(wat2)
        xl_ = VGroup(*[Text("x%s = %s" % ("₁₂₃₄"[i], nf(XS[i], 2)), font=MONO, font_size=20, color=SKY if XS[i] > 0 else PINK).move_to([xs[i], y0 + max(AL[i], LV) * s + 0.35, 0]) for i in range(n)])
        self.play(FadeIn(xl_), run_time=0.4)
        self.readout([("i   αᵢ    xᵢ     λᵢ     λᵢ·xᵢ", DIM)] + [("%d   %s   %s   %s   %s" % (i + 1, nf(AL[i], 1), nf(XS[i], 2), nf(LAM[i], 3), nf(LAM[i] * XS[i], 1)), SKY if XS[i] > 0 else PINK) for i in range(n)] + [("ν = 1/0,75 = %s" % nf(NU, 3) if LANG == "vi" else "ν = 1/0.75 = %s" % nf(NU, 3), WHITE)], size=21, y=-3.0)
        self.say(L("Nghiệm: x = (0,65; 0,35; 0; 0), ν = 4/3. Kênh 3, 4 có ràng buộc hoạt động, λ₃ = 4/3 − 1/0,8 ≈ 0,083 và λ₄ = 4/3 − 1/1,2 = 0,5.",
                   "Solution: x = (0.65, 0.35, 0, 0), ν = 4/3. Channels 3 and 4 have active constraints, λ₃ = 4/3 − 1/0.8 ≈ 0.083 and λ₄ = 4/3 − 1/1.2 = 0.5."), hold=8.5)
        self.say(L("Kiểm tra đủ bốn điều kiện: x ≥ 0 và tổng 1; mọi λᵢ ≥ 0; λᵢ·xᵢ = 0 ở cả bốn dòng; tính dừng đúng. Vậy đây là nghiệm tối ưu.",
                   "Check all four: x ≥ 0 with sum 1; every λᵢ ≥ 0; λᵢ·xᵢ = 0 on all four rows; stationarity holds. So this is the optimum."), hold=7.5)
        self.say(L("λ₄ lớn hơn λ₃: đáy kênh 4 ở xa mực nước hơn. λᵢ là cái giá: ép một lượng nhỏ ε công suất vào kênh i thì mục tiêu tăng khoảng λᵢ·ε.",
                   "λ₄ is larger than λ₃: channel 4's floor sits farther above the water. λᵢ is a price: forcing a small amount ε of power into channel i raises the objective by about λᵢ·ε."), hold=8.5)
        self.readout([("ép x₄ = ε = 0,001, đổ nước lại phần còn lại:" if LANG == "vi" else "force x₄ = ε = 0.001, re-fill the rest:", WHITE), ("mục tiêu tăng %s ≈ λ₄·ε = %s" % (sci(fobj(XE) - FS, 3), sci(LAM[3] * EPS, 3)) if LANG == "vi" else "objective rises by %s ≈ λ₄·ε = %s" % (sci(fobj(XE) - FS, 3), sci(LAM[3] * EPS, 3)), PINK)], size=22)
        self.say(L("Kiểm tra bằng số: ép 0,001 công suất vào kênh 4 rồi giải lại. Mục tiêu tăng %s, gần đúng λ₄·ε = %s." % (sci(fobj(XE) - FS, 2), sci(LAM[3] * EPS, 2)),
                   "Check numerically: force 0.001 of power into channel 4 and solve again. The objective rises by %s, almost exactly λ₄·ε = %s." % (sci(fobj(XE) - FS, 2), sci(LAM[3] * EPS, 2))), hold=7.0)
        # ---- stage 4
        self.stage(4); self.clear_ro(); self.play(FadeOut(VGroup(wat2, xl_)), run_time=0.3)
        def show(xv, col):
            gg = VGroup()
            for i in range(n):
                h = xv[i] * s
                if abs(h) > 1e-4:
                    yb = y0 + AL[i] * s
                    gg.add(Rectangle(width=1.3, height=abs(h), fill_color=col if h > 0 else PINK, fill_opacity=0.7, stroke_width=0 if h > 0 else 3, stroke_color=PINK).move_to([xs[i], yb + h / 2, 0]))
            return gg
        w1 = show(X1, SKY); self.play(FadeIn(w1), run_time=0.5)
        self.readout([("đoán: λ = 0 cho mọi i (không ràng buộc nào hoạt động)" if LANG == "vi" else "guess: λ = 0 for all i (no constraint active)", WHITE), ("x = %s" % vec(X1, 3), SKY), ("x₄ = %s < 0: vi phạm khả thi gốc" % nf(X1[3], 3) if LANG == "vi" else "x₄ = %s < 0: primal infeasible" % nf(X1[3], 3), PINK)], size=21)
        self.say(L("Đoán sai 1: coi mọi xᵢ ≥ 0 không hoạt động. Khi đó mực nước 0,875 và x₄ = −0,325 < 0. Khối hồng là \"nước âm\": vi phạm khả thi gốc.",
                   "Wrong guess 1: treat every xᵢ ≥ 0 as inactive. Then the level is 0.875 and x₄ = −0.325 < 0. The pink block is \"negative water\": primal infeasible."), hold=8.0)
        self.play(FadeOut(w1), run_time=0.3)
        w3 = show(np.r_[X3, 0], SKY); self.play(FadeIn(w3), run_time=0.5)
        self.readout([("đoán: chỉ kênh 4 hoạt động" if LANG == "vi" else "guess: only channel 4 active", WHITE), ("mực = %s,  x₃ = %s < 0" % (nf(L3, 3), nf(X3[2], 3)) if LANG == "vi" else "level = %s,  x₃ = %s < 0" % (nf(L3, 3), nf(X3[2], 3)), PINK)], size=22)
        self.say(L("Đoán sai 2: chỉ kênh 4 hoạt động. Mực nước %s vẫn thấp hơn đáy kênh 3, nên x₃ = %s < 0. Lại sai." % (nf(L3, 3), nf(X3[2], 3)),
                   "Wrong guess 2: only channel 4 active. The level %s is still below channel 3's floor, so x₃ = %s < 0. Wrong again." % (nf(L3, 3), nf(X3[2], 3))), hold=6.5)
        self.play(FadeOut(w3), run_time=0.3)
        w2 = show(X2, SKY); self.play(FadeIn(w2), run_time=0.5)
        self.readout([("đoán: dồn hết vào kênh 1, x = (1; 0; 0; 0)" if LANG == "vi" else "guess: all power to channel 1, x = (1, 0, 0, 0)", WHITE), ("ν = 1/1,1 = %s" % nf(NU2, 3) if LANG == "vi" else "ν = 1/1.1 = %s" % nf(NU2, 3), WHITE), ("λ₂ = ν − 1/0,4 = %s < 0: sai dấu" % nf(LAM2[1], 3) if LANG == "vi" else "λ₂ = ν − 1/0.4 = %s < 0: wrong sign" % nf(LAM2[1], 3), PINK)], size=21)
        self.say(L("Đoán sai 3: dồn hết vào kênh 1. Khả thi gốc thì ổn, nhưng λ₂ = %s < 0. Nhân tử âm nghĩa là nới ràng buộc ra (cho kênh 2 ít công suất) sẽ tốt hơn." % nf(LAM2[1], 2),
                   "Wrong guess 3: all power to channel 1. Primal feasible, but λ₂ = %s < 0. A negative multiplier means relaxing that constraint (giving channel 2 some power) would do better." % nf(LAM2[1], 2)), hold=8.5)
        self.say(L("Cách đọc chung: xᵢ < 0 thì ràng buộc xᵢ ≥ 0 phải hoạt động (đóng kênh i). λᵢ < 0 thì ràng buộc đó không nên hoạt động (mở kênh i). Sửa đến khi không còn dấu sai.",
                   "The general reading: xᵢ < 0 means the constraint xᵢ ≥ 0 must be active (close channel i). λᵢ < 0 means it should not be active (open channel i). Fix until no sign is wrong."), hold=8.0)
        self.takeaway([L("KKT = tính dừng + khả thi gốc + λ ≥ 0 + bù λᵢ·hᵢ = 0. Bài lồi có Slater: KKT ⇔ tối ưu.", "KKT = stationarity + primal feasibility + λ ≥ 0 + λᵢ·hᵢ = 0. Convex with Slater: KKT ⇔ optimal."),
                       L("Ràng buộc không hoạt động: λᵢ = 0. Ràng buộc hoạt động: λᵢ ≥ 0 có thể dương.", "Inactive constraint: λᵢ = 0. Active constraint: λᵢ ≥ 0, possibly positive."),
                       L("Đổ nước: xᵢ = max(0; 1/ν − αᵢ). Ở đây x = (0,65; 0,35; 0; 0), ν = 4/3.", "Water-filling: xᵢ = max(0, 1/ν − αᵢ). Here x = (0.65, 0.35, 0, 0), ν = 4/3."),
                       L("Đoán sai tập hoạt động sẽ lộ ra: hoặc x < 0, hoặc λ < 0.", "A wrong active set shows itself: either x < 0 or λ < 0.")])

---
layout: post
title: "11-07 Dual của Dual trong Tối Ưu Convex Tổng Quát"
chapter: "11"
order: 8
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter11
redirect_from:
  - /contents/vi/chapter11/11_09_Dual_of_Dual_General_Case/
---

Ở Chương 10, ta đã tận hưởng cảm giác đối xứng hoàn hảo của Quy hoạch tuyến tính: lấy đối ngẫu hai lần luôn quay về chính xác bài toán gốc. Bước sang Chương 11 với các hàm phi tuyến tổng quát, một câu hỏi vừa sâu sắc vừa tinh tế xuất hiện: **trong tối ưu lồi tổng quát, "đối ngẫu của đối ngẫu" có còn là bài toán gốc nữa không?**

Câu trả lời là một kiệt tác của giải tích lồi hiện đại (Định lý Fenchel–Moreau): **CÓ**, miễn là bài toán gốc lồi, các hàm đóng (nửa liên tục dưới) và thỏa điều kiện chuẩn hóa (như Slater)! Còn nếu bài toán gốc *không lồi* thì sao? Khi đó, phép lấy đối ngẫu hai lần không quay về bài toán gốc gồ ghề ban đầu nữa, mà trả về **bản bao lồi đóng chặt nhất nằm dưới bài toán gốc (convex relaxation / biconjugate $$f^{**}$$)**! Khám phá này giải thích lý do vì sao trong tối ưu tổ hợp và học máy không lồi, việc lấy đối ngẫu kép là cách tự động tạo ra bản nới lỏng lồi tốt nhất!

## Kiến thức cần nhớ: Bốn trụ cột của tính đối ngẫu kép tổng quát

- **Định lý Fenchel–Moreau (Liên hợp kép $$f^{**} = f$$):** Nếu $$f$$ là hàm lồi, chính quy (proper) và đóng (lower semicontinuous), thì hàm liên hợp của hàm liên hợp bằng chính nó: $$(f^*)^*(x) = f(x)$$. Nếu $$f$$ không lồi, $$f^{**}$$ là hàm lồi đóng lớn nhất nằm dưới $$f$$ (bao lồi đóng — closed convex envelope).
- **Chuyển bài toán đối ngẫu $$\max_{u \ge 0} g(u)$$ về dạng $$\min$$ để lấy đối ngẫu lần 2:** Viết lại thành $$\min_{u} (-g(u))$$ với ràng buộc $$-u \le 0$$, rồi đưa thêm nhân tử Lagrange mới $$\tilde{x}$$ (chính là biến gốc hồi sinh!) để lập Lagrangian bậc hai.
- **Vai trò của điều kiện Slater trong đối ngẫu kép:** Để không xuất hiện khe hở khi đảo thứ tự $$\min_x \max_u$$ và $$\max_u \min_x$$ (định lý điểm yên ngựa Sion / minimax), điều kiện Slater bảo đảm giá trị tối ưu và tập nghiệm được bảo toàn trọn vẹn khi quay về bài toán gốc.
- **Ý nghĩa cho bài toán không lồi (Convexification):** Khi áp dụng quy trình Primal $$\to$$ Dual $$\to$$ Bi-dual lên một bài toán không lồi, ta tự động nhận được bản nới lỏng lồi chặt nhất của nó (ví dụ nới lỏng chuẩn hạt nhân cho bài toán hạng thấp hay SDP relaxation cho Max-Cut!).

### Giải thích: Kiểm chứng tay $$f^{**}(x) = f(x)$$ cho hàm mũ phi tuyến $$f(x) = e^x$$

Hàm $$f(x) = e^x$$ là hàm lồi, trơn, đóng trên toàn $$\mathbb{R}$$. Hãy tự tay thực hiện phép biến đổi liên hợp Fenchel hai lần liên tiếp!

1. **Lần 1 — Tính hàm liên hợp $$f^*(y) = \sup_{x \in \mathbb{R}} (yx - e^x)$$:**
   - Nếu $$y < 0$$: cho $$x \to -\infty$$ thì $$yx \to +\infty$$ và $$e^x \to 0$$, nên $$f^*(y) = +\infty$$.
   - Nếu $$y = 0$$: $$\sup_x (-e^x) = 0$$ (khi $$x \to -\infty$$).
   - Nếu $$y > 0$$: cho đạo hàm theo $$x$$ bằng $$0$$: $$y - e^x = 0 \implies x = \ln y$$. Thay lại:
     $$f^*(y) = y\ln y - y \quad (\text{hàm entropy âm!}).$$
2. **Lần 2 — Tính hàm liên hợp kép $$f^{**}(x) = \sup_{y > 0} \big(xy - (y\ln y - y)\big)$$:**
   Lấy đạo hàm theo $$y > 0$$ và cho bằng $$0$$:
   $$\frac{d}{dy}\big(xy - y\ln y + y\big) = x - (\ln y + 1) + 1 = x - \ln y = 0 \implies y^* = e^x > 0.$$
   Thay $$y^* = e^x$$ trở lại biểu thức:
   $$f^{**}(x) = x e^x - e^x \ln(e^x) + e^x = x e^x - x e^x + e^x = e^x = f(x)!$$
   Ta quay trở về **đúng từng ký tự của hàm gốc $$e^x$$** — minh họa sống động nhất cho định lý Fenchel–Moreau và tính đối ngẫu kép trong tối ưu lồi!

Trong Chương 10, chúng ta đã chứng minh rằng đối với quy hoạch tuyến tính (LP), đối ngẫu của bài toán đối ngẫu luôn quay trở về đúng bài toán gốc. Bài học này làm rõ câu hỏi mở rộng: tính chất đó có còn đúng trong tối ưu lồi tổng quát hay không và cần thêm những điều kiện nào.

---

## Nhắc lại: Đối ngẫu kép trong quy hoạch tuyến tính

Với cặp bài toán LP:

**Bài toán gốc (Primal):**
$$
\begin{align}
\text{minimize} \quad & c^T x \\
\text{subject to} \quad & Ax \geq b, \\
& x \geq 0
\end{align}
$$

**Bài toán đối ngẫu (Dual):**
$$
\begin{align}
\text{maximize} \quad & b^T y \\
\text{subject to} \quad & A^T y \leq c, \\
& y \geq 0
\end{align}
$$

Ta luôn có **Đối ngẫu của đối ngẫu = Bài toán gốc**. Hãy xem điều gì xảy ra khi mở rộng sang bài toán tối ưu lồi tổng quát.

---

## Bài toán tối ưu lồi tổng quát

Xét bài toán tối ưu lồi tổng quát:

$$
\begin{align}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \leq 0, \; i = 1, \ldots, m, \\
& h_j(x) = 0, \; j = 1, \ldots, p,
\end{align}
$$

trong đó:
- $$f_0, f_1, \ldots, f_m$$ là các hàm lồi,
- $$h_1, \ldots, h_p$$ là các hàm affine,
- $$x \in \mathbb{R}^n$$ là vector biến quyết định.

---

## Xây dựng bài toán đối ngẫu

### Hàm Lagrangian

Hàm Lagrangian được định nghĩa là:

$$
\mathcal{L}(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$

với:
- $$\lambda \in \mathbb{R}^m, \lambda \geq 0$$: vector nhân tử Lagrange cho các ràng buộc bất đẳng thức,
- $$\nu \in \mathbb{R}^p$$: vector nhân tử Lagrange cho các ràng buộc đẳng thức.

### Hàm đối ngẫu

$$
g(\lambda, \nu) = \inf_x \mathcal{L}(x, \lambda, \nu)
$$

### Bài toán đối ngẫu

$$
\begin{align}
\text{maximize} \quad & g(\lambda, \nu) \\
\text{subject to} \quad & \lambda \geq 0
\end{align}
$$

---

## Đối ngẫu của đối ngẫu cho bài toán lồi

Khi lấy đối ngẫu thêm một lần nữa từ bài toán đối ngẫu ở trên, ta có thu lại được bài toán gốc ban đầu hay không?

<div class="textbook-theorem" markdown="1">
**Định lý:** Nếu bài toán thỏa mãn các điều kiện sau:
1. Bài toán gốc là **lồi** (và hàm mục tiêu đóng / nửa liên tục dưới),
2. **Tính đối ngẫu mạnh** thỏa mãn (khoảng cách đối ngẫu bằng 0),
3. Thỏa mãn một **điều kiện chuẩn hóa ràng buộc** (constraint qualification, chẳng hạn điều kiện Slater),
</div>

thì:

$$
\boxed{\text{Dual của Dual} = \text{Primal}}
$$

### Điều kiện Slater

Điều kiện Slater yêu cầu tồn tại một điểm khả thi chặt $$\tilde{x}$$:
- $$f_i(\tilde{x}) < 0$$ với mọi $$i = 1, \ldots, m$$ (không bắt buộc chặt đối với các ràng buộc affine),
- $$h_j(\tilde{x}) = 0$$ với mọi $$j = 1, \ldots, p$$.

**Lưu ý về độ chặt chẽ:** Điều kiện Slater đảm bảo tính đối ngẫu mạnh. Để bài toán đối ngẫu kép (bidual) khôi phục chính xác bài toán gốc, bài toán gốc cần có thêm tính lồi và tính đóng (hàm mục tiêu nửa liên tục dưới). Với các bài toán không lồi, đối ngẫu kép nói chung chỉ cho ra bản lồi hóa (convex relaxation) của bài toán gốc.

---

## So sánh: Quy hoạch tuyến tính và tối ưu lồi tổng quát

| Tính chất | Quy hoạch tuyến tính (LP) | Tối ưu lồi tổng quát |
|-----------|---------------------------|----------------------|
| **Dual của Dual = Primal** | Luôn đúng | Cần thêm điều kiện |
| **Đối ngẫu mạnh** | Đúng nếu ít nhất một bài toán khả thi | Cần điều kiện Slater (hoặc CQ tương đương) |
| **Cấu trúc** | Đối xứng trực tiếp | Đối xứng có điều kiện |
| **Điều kiện ràng buộc (CQ)** | Tự động thỏa mãn (ràng buộc affine) | Cần kiểm tra |

---

## Vì sao LP là trường hợp đặc biệt?

Trong LP, tính chất đối ngẫu kép luôn đúng nhờ bốn đặc điểm sau:

1. **Luôn là bài toán lồi:** Hàm mục tiêu tuyến tính và miền khả thi là đa diện lồi.
2. **Đối ngẫu mạnh không cần điều kiện chặt:** Chỉ cần bài toán gốc hoặc bài toán đối ngẫu khả thi, khoảng cách đối ngẫu bằng 0 khi tồn tại nghiệm tối ưu hữu hạn.
3. **Cấu trúc ma trận đối xứng:** Phép chuyển vị hai lần trả về ma trận ban đầu ($$(A^T)^T = A$$), và việc hoán đổi $$(b, c)$$ hai lần khôi phục đúng vị trí cũ.
4. **Ràng buộc đều là affine:** Điều kiện chuẩn hóa ràng buộc dạng mở rộng tự động được thỏa mãn khi bài toán khả thi.

---

## Ví dụ minh họa

### Ví dụ 1: Quy hoạch bậc hai lồi (Convex QP)

**Bài toán gốc:**
$$
\begin{align}
\text{minimize} \quad & \frac{1}{2}x^T Q x + c^T x \\
\text{subject to} \quad & Ax \leq b
\end{align}
$$

với $$Q \succ 0$$ (xác định dương).

- Hàm mục tiêu lồi chặt và các ràng buộc là affine.
- Khi bài toán khả thi, điều kiện Slater dạng mở rộng được thỏa mãn.
- Do đó **Đối ngẫu của đối ngẫu = Bài toán gốc** ✓.

### Ví dụ 2: Bài toán không lồi

**Bài toán gốc:**
$$
\text{minimize} \quad -x^2 \quad \text{subject to} \quad 0 \leq x \leq 1
$$

- Hàm mục tiêu $$-x^2$$ là hàm lõm (không lồi).
- Nghiệm tối ưu gốc: $$x^* = 1$$, $$p^* = -1$$.
- Với nhân tử $$\lambda_1 \geq 0$$ (cho $$-x \leq 0$$) và $$\lambda_2 \geq 0$$ (cho $$x - 1 \leq 0$$), hàm đối ngẫu là:

$$
g(\lambda_1, \lambda_2) = \inf_{x \in \mathbb{R}} \left( -x^2 - \lambda_1 x + \lambda_2 (x - 1) \right) = -\infty \quad \text{với mọi } \lambda_1, \lambda_2 \geq 0,
$$

vì $$-x^2 \to -\infty$$ khi $$|x| \to \infty$$.

- Giá trị tối ưu đối ngẫu là $$d^* = -\infty < p^* = -1$$. Khoảng cách đối ngẫu bằng vô hạn, đối ngẫu mạnh không xảy ra và đối ngẫu kép không quay về bài toán gốc ✗.

### Ví dụ 3: Bài toán lồi không thỏa điều kiện Slater

**Bài toán gốc:**
$$
\text{minimize} \quad x^2 \quad \text{subject to} \quad x^2 \leq 0
$$

- Hàm mục tiêu và hàm ràng buộc đều lồi, nhưng miền khả thi chỉ gồm đúng một điểm $$x = 0$$ nên không tồn tại điểm khả thi chặt ($$x^2 < 0$$ vô nghiệm).
- Điều kiện Slater **không thỏa mãn** ✗.
- Dù vậy, trong trường hợp cụ thể này ta vẫn có $$p^* = d^* = 0$$ (đối ngẫu mạnh vẫn xảy ra vì điều kiện Slater chỉ là điều kiện đủ, không phải điều kiện cần).

---

## Ứng dụng và ý nghĩa

1. **Phân tích khoảng cách đối ngẫu:** Khi đối ngẫu kép không trùng với bài toán gốc, khoảng cách đối ngẫu thường dương; ta cần kiểm tra lại tính lồi hoặc sử dụng các phương pháp nới lỏng lồi.
2. **Lựa chọn chiến lược giải:** Với LP, có thể giải bài toán gốc hay bài toán đối ngẫu tùy theo kích thước. Với bài toán lồi tổng quát, cần kiểm tra điều kiện đối ngẫu mạnh trước khi chuyển sang giải đối ngẫu. Với bài toán không lồi, bài toán đối ngẫu chỉ bảo đảm cung cấp cận dưới.
3. **Cơ sở lý thuyết:** Tính chất này gắn trực tiếp với điều kiện tối ưu KKT (Chương 12) và thiết kế các thuật toán gốc – đối ngẫu.

---

## Bài tập thực hành

### Bài tập 1: Kiểm tra điều kiện Slater

Kiểm tra điều kiện Slater và xác định xem đối ngẫu kép có trùng với bài toán gốc không đối với các bài toán sau:

a) $$\min x^2 + y^2$$ s.t. $$x + y \geq 2$$

b) $$\min e^x$$ s.t. $$x \geq 0$$

c) $$\min -\log x$$ s.t. $$x \leq 1$$, $$x > 0$$

### Bài tập 2: So sánh LP và QP

Cho hai bài toán:

- **LP:** $$\min c^T x$$ s.t. $$Ax \leq b$$
- **QP:** $$\min \frac{1}{2}x^T Q x$$ s.t. $$Ax \leq b$$ với $$Q \succ 0$$

a) Xây dựng bài toán đối ngẫu của mỗi bài toán.
b) Kiểm tra tính chất đối ngẫu kép.
c) So sánh các điều kiện cần thiết giữa hai bài toán.

### Bài tập 3: Ví dụ không lồi

Xét bài toán:

$$
\min_{x \in \mathbb{R}} x^3 \quad \text{s.t.} \quad x \geq 1
$$

a) Giải bài toán gốc.
b) Xây dựng bài toán đối ngẫu.
c) Chứng minh đối ngẫu kép không quay về bài toán gốc.

---

## Tóm tắt

| Điều kiện | LP | Tối ưu lồi | Không lồi |
|-----------|----|------------|-----------|
| Tính lồi | ✓ (tự động) | ✓ (cần kiểm tra) | ✗ |
| Đối ngẫu mạnh | ✓ (nếu khả thi) | ✓ (cần điều kiện Slater) | ✗ (nói chung) |
| Dual của Dual = Primal | ✓ | ✓ (có điều kiện) | ✗ |

---

## Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L. (2004).** *Convex Optimization.* Cambridge University Press.
   - Chapter 5: Duality (đặc biệt Section 5.2 và 5.3)

2. **Rockafellar, R. T. (1970).** *Convex Analysis.* Princeton University Press.
   - Chapter 31: Duality correspondences

3. **Bertsekas, D. P. (1999).** *Nonlinear Programming* (2nd ed.). Athena Scientific.
   - Chapter 6: Duality and convex analysis

4. **Nesterov, Y. (2018).** *Lectures on Convex Optimization.* Springer.
   - Chapter 3: Duality Theory (Section 3.4)

---

**Kết nối với các chương khác:**
- **Chương 10:** Đối ngẫu kép trong LP (trường hợp đặc biệt).
- **Chương 12:** Điều kiện KKT.
- **Chương 15 và 17:** Phương pháp hàm rào (barrier method) và phương pháp điểm trong gốc – đối ngẫu (primal-dual interior-point methods).

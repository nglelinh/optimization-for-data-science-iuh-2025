---
layout: post
title: 05-06 Quy Hoạch Nón (CP)
chapter: '05'
order: 12
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

Nhìn lại chặng đường từ LP ($$x \ge 0$$), sang SOCP ($$\|u\|_2 \le t$$), rồi đến SDP ($$X \succeq 0$$), bạn có nhận ra cả ba lớp bài toán đồ sộ ấy thực chất chỉ khác nhau ở đúng **một ký hiệu duy nhất** không? Tất cả đều có hàm mục tiêu tuyến tính $$c^T x$$, ràng buộc đẳng thức affine $$Ax = b$$, và một ràng buộc thành viên duy nhất: $$x \in K$$ (hoặc $$Gx + s = h,\; s \in K$$), trong đó $$K$$ là một **nón lồi**!

Đó chính là tầm nhìn thống nhất tuyệt đẹp của **Quy hoạch Nón (Conic Programming - CP)**. Thay vì phải viết hàng chục bộ giải riêng biệt cho từng loại bài toán, các nhà tối ưu hóa hiện đại chỉ cần xây dựng lý thuyết đối ngẫu và thuật toán điểm trong cho *bài toán nón tổng quát* — và lập tức giải được cả LP, QP, SOCP, SDP, thậm chí cả quy hoạch mũ (exponential cone) và quy hoạch lũy thừa (power cone) trong cùng một kiến trúc phần mềm!

## Bản đồ kiến thức nền: Bức tranh thống nhất của Quy hoạch Nón

Ba trụ cột sau cho thấy vì sao Quy hoạch Nón là "ngôn ngữ máy" (assembly language) của tối ưu hóa lồi hiện đại:

- **Từ điển các Nón chuẩn (Standard Cones):**
  - **Nón không âm** $$\mathbb{R}_+^n$$ sinh ra **LP**.
  - **Nón bậc hai** $$\mathcal{Q}^n$$ sinh ra **SOCP** (bao hàm QP và QCQP).
  - **Nón nửa xác định dương** $$\mathbb{S}_+^n$$ sinh ra **SDP**.
  - **Nón mũ** $$K_{\text{exp}} = \operatorname{cl}\{(x,y,z) : y > 0,\; y e^{x/y} \le z\}$$ sinh ra **GP, Hồi quy Logistic và Entropy**!
- **Tích Đề-các của nhiều nón (Mixed Cone Programs):** Trong thực tế, một bài toán duy nhất có thể đồng thời chứa cả biến không âm, ràng buộc chuẩn $$\ell_2$$ và ràng buộc ma trận $$X \succeq 0$$. Khi đó ta chỉ cần đặt $$K = \mathbb{R}_+^{n_1} \times \mathcal{Q}^{n_2} \times \mathbb{S}_+^{n_3}$$ — vẫn là một bài toán Quy hoạch Nón chuẩn!
- **Đối ngẫu Nón & Tự đối ngẫu (Conic Duality):** Bài toán đối ngẫu của CP có cấu trúc đối xứng gần như y hệt bài toán gốc, chỉ thay nón $$K$$ bằng **nón đối ngẫu** $$K^*$$. Nhờ tính đối xứng này, các bộ giải như Clarabel, SCS hay MOSEK giải đồng thời cả bài toán gốc lẫn đối ngẫu và chứng nhận nghiệm tối ưu khi khoảng cách đối ngẫu về $$0$$.

### Khung giải thích (nên đọc chậm): Viết một bài toán hỗn hợp về đúng dạng chuẩn Quy hoạch Nón

Xét bài toán tối ưu 2 biến kết hợp cả ràng buộc tuyến tính lẫn chuẩn Euclidean:
$$\min_{x_1, x_2} \; -x_1 - x_2 \quad \text{thỏa mãn} \quad x_1 \ge 0,\quad x_2 \ge 0,\quad \sqrt{x_1^2 + x_2^2} \le 2.$$

1. **Bước 1 — Đưa vào vector biến phụ $$s$$ thuộc tích nón $$K = \mathbb{R}_+^2 \times \mathcal{Q}^3$$:**
   - Với ràng buộc tuyến tính $$x_1 \ge 0,\; x_2 \ge 0$$: đặt $$s_1 = x_1 \ge 0,\; s_2 = x_2 \ge 0 \implies (s_1, s_2) \in \mathbb{R}_+^2$$.
   - Với ràng buộc chuẩn $$\|(x_1, x_2)\|_2 \le 2$$: đặt $$s_3 = 2,\; s_4 = x_1,\; s_5 = x_2 \implies (s_3, s_4, s_5) \in \mathcal{Q}^3$$ (vì $$\sqrt{s_4^2 + s_5^2} \le s_3$$).
2. **Bước 2 — Gom thành dạng chuẩn CP $$\min c^T x \text{ s.t. } Gx + s = h,\; s \in K$$:**
   $$G = \begin{pmatrix} -1 & 0 \\ 0 & -1 \\ 0 & 0 \\ -1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad h = \begin{pmatrix} 0 \\ 0 \\ 2 \\ 0 \\ 0 \end{pmatrix}, \qquad c = \begin{pmatrix} -1 \\ -1 \end{pmatrix}, \qquad K = \mathbb{R}_+^2 \times \mathcal{Q}^3.$$
3. **Bước 3 — Kiểm chứng nghiệm:** Nghiệm tối ưu là $$x^\star = (\sqrt{2}, \sqrt{2})$$, cho $$f^\star = -2\sqrt{2} \approx -2.828$$. Khi đó $$s^\star = (\sqrt{2}, \sqrt{2}, 2, \sqrt{2}, \sqrt{2})^T$$ nằm gọn trong $$\mathbb{R}_+^2 \times \mathcal{Q}^3$$ (vì $$\sqrt{2+2} = 2$$)! Toàn bộ phần phi tuyến đã được đóng gói sạch sẽ vào hình học của nón $$K$$.

---

Nếu ràng buộc bất đẳng thức thông thường trong một bài toán LP tổng quát được thay bằng một **bất đẳng thức tổng quát theo nón lồi** $$K$$, ta thu được **bài toán quy hoạch nón** (Conic Programming - CP).

### Bài toán Quy hoạch Nón
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Fx + g \preceq_K 0} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&c, x \in \mathbb{R}^{n}, \; A \in \mathbb{R}^{p \times n}, \text{ và } b \in \mathbb{R}^{p}.
>\end{align}$$

* $$F: \mathbb{R}^n \rightarrow Y$$ là một ánh xạ tuyến tính và $$g \in Y$$, với $$Y$$ là một không gian Euclid hữu hạn chiều và $$K \subseteq Y$$ là một nón lồi chính quy.
* LP là trường hợp đặc biệt khi $$K = \mathbb{R}_{+}^m$$, do đó $$\text{LP} \subseteq \text{CP}$$.
* SDP là trường hợp đặc biệt khi $$K = \mathbb{S}_{+}^k$$, do đó $$\text{SDP} \subseteq \text{CP}$$.
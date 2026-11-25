---
layout: post
title: 05-04 Quy Hoạch Nón Bậc Hai (SOCP)
chapter: '05'
order: 10
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

Hãy tưởng tượng một chiếc ốc quế kem dựng thẳng đứng trong không gian 3 chiều: đáy nhọn tại gốc tọa độ $$(0,0,0)$$ và miệng mở dần lên trên theo quy luật $$\sqrt{x_1^2 + x_2^2} \le t$$. Trong tối ưu hóa lồi, hình khối quen thuộc ấy có một cái tên rất trang trọng: **Nón bậc hai (Second-Order Cone / Lorentz Cone)**.

Khi bạn cực tiểu hóa một hàm tuyến tính $$f^T x$$ dưới các ràng buộc nằm trong nón bậc hai $$\|A_i x + b_i\|_2 \le c_i^T x + d_i$$, bạn có **Quy hoạch Nón Bậc hai (SOCP)**. Đừng để vẻ ngoài đơn giản đánh lừa: SOCP đủ sức nuốt trọn LP, QP, QCQP, tối ưu bền vững (robust LP với nhiễu ellipsoid), bài toán vị trí kho bãi Weber (tổng khoảng cách Euclidean), và thiết kế chùm sóng ăng-ten — trong khi các bộ giải điểm trong hiện đại giải SOCP gần như nhanh ngang ngửa LP!

## Kiến thức cần nhớ: Sức mạnh biểu diễn của Nón Bậc Hai

Bốn trụ cột dưới đây giúp bạn làm chủ nghệ thuật nhận diện và chuyển đổi về SOCP:

- **Hình học Nón bậc hai $$\mathcal{Q}_{k+1}$$:** Tập $$\{(u, t) \in \mathbb{R}^k \times \mathbb{R} : \|u\|_2 \le t\}$$ là một nón lồi, đóng, nhọn và **tự đối ngẫu** ($$\mathcal{Q}^* = \mathcal{Q}$$). Tính tự đối ngẫu này là lý do các thuật toán điểm trong nguyên–đối ngẫu giải SOCP cực kỳ hiệu quả.
- **Mẹo chuyển ràng buộc Hyperbolic & Bậc hai sang SOCP:** Đẳng thức đại số vàng $$u^2 \le v \cdot w \iff \left\|\begin{pmatrix} 2u \\ v - w \end{pmatrix}\right\|_2 \le v + w$$ (với $$v, w \ge 0$$) cho phép biến mọi ràng buộc phân thức, căn bậc hai, và mọi ràng buộc bậc hai lồi (QP, QCQP) thành ràng buộc nón bậc hai chuẩn!
- **Bao hàm LP, QP, QCQP:** Đặt $$A_i = 0, b_i = 0$$ thì SOCP thu về LP. Dùng biến phụ $$t$$ đưa hàm mục tiêu bậc hai $$\|Px + q\|_2^2 \le t$$ vào ràng buộc hyperbolic thì mọi QP và QCQP đều trở thành SOCP.
- **Ứng dụng Tối ưu Bền vững (Robust Linear Programming):** Khi hệ số ràng buộc tuyến tính $$a_i$$ có sai số nằm trong ellipsoid $$\{a_i = \bar{a}_i + P_i u : \|u\|_2 \le 1\}$$, điều kiện $$\sup_{\|u\|_2 \le 1} (\bar{a}_i + P_i u)^T x \le b_i$$ tự động biến thành đúng một ràng buộc SOCP: $$\bar{a}_i^T x + \|P_i^T x\|_2 \le b_i$$!

### Giải thích: Chuyển đổi ràng buộc bậc hai sang dạng nón SOCP bằng phép biến đổi đại số

Xét ràng buộc bậc hai 1 biến $$x^2 \le t$$ với $$t \ge 0$$. Làm sao viết nó thành dạng chuẩn $$\|A z + b\|_2 \le c^T z + d$$ (chỉ có chuẩn Euclidean bậc 1 ở vế trái và biểu thức tuyến tính ở vế phải)?

1. **Bước 1 — Dùng hằng đẳng thức $$4t = (t + 1)^2 - (t - 1)^2$$:**
   $$x^2 \le t \iff 4x^2 \le 4t = (t + 1)^2 - (t - 1)^2 \iff (2x)^2 + (t - 1)^2 \le (t + 1)^2.$$
2. **Bước 2 — Lấy căn bậc hai hai vế (vì $$t \ge 0 \implies t + 1 > 0$$):**
   $$\left\| \begin{pmatrix} 2x \\ t - 1 \end{pmatrix} \right\|_2 \le t + 1.$$
3. **Bước 3 — Kiểm tra bằng số cụ thể:**
   - Thử $$x = 2,\; t = 4$$ (thỏa $$2^2 = 4 \le 4$$):
     Vế trái $$= \sqrt{(2\cdot 2)^2 + (4 - 1)^2} = \sqrt{16 + 9} = 5$$; vế phải $$= 4 + 1 = 5$$. Khớp chính xác!
   - Thử $$x = 3,\; t = 4$$ (vi phạm $$9 > 4$$):
     Vế trái $$= \sqrt{6^2 + 3^2} = \sqrt{45} \approx 6.708 > 5$$. Vi phạm đúng như bài toán gốc!
4. **Ý nghĩa:** Nhờ đúng một dòng hằng đẳng thức này, mọi bài toán QP và QCQP đều được "dịch" tự động sang SOCP để đưa vào các bộ giải nón hiện đại như ECOS, Clarabel hay MOSEK.

---

Nếu các ràng buộc bất đẳng thức tuyến tính trong một bài toán LP tổng quát được thay bằng các ràng buộc nón bậc hai (tức là các bất đẳng thức dạng chuẩn $$\ell_2$$ của hàm affine không vượt quá một hàm affine), ta thu được **bài toán quy hoạch nón bậc hai** (Second-Order Cone Programming - SOCP).

### Bài toán Quy hoạch Nón Bậc hai

>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } &&{\| A_i x + b_i \|_2 \leq c_i^T x + d_i, \quad i = 1, \dotsc, m}\\\\
>    & &&{Fx = g},\\\\
>    & \text{where } &&x \in \mathbb{R}^n \text{ là biến tối ưu, } A_i \in \mathbb{R}^{n_i \times n}, \text{ và } F \in \mathbb{R}^{p \times n}.
>\end{align} $$

### Nhắc lại: Nón chuẩn
Một **nón chuẩn** (norm cone) là một nón lồi trong $$\mathbb{R}^{n+1}$$ gồm tất cả các điểm $$(x, t)$$ thỏa mãn $$\| x \| \le t$$ đối với một chuẩn $$\| \cdot \|$$ cho trước:

>$$\left\{(x, t) : \| x \| \le t \right\} \text{, với chuẩn } \| \cdot \|$$

Hình dưới đây minh họa nón chuẩn ứng với chuẩn $$\ell_2$$ ($$\| \cdot \|_2$$), thường gọi là **nón bậc hai** (second-order cone) hay *nón kem* (ice-cream cone).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_04_Norm_Cone.png" alt="[Fig1] Nón Chuẩn [1]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Nón chuẩn [1]</figcaption>
</p>
</figure>

## Chuyển đổi QCQP sang SOCP
Mọi bài toán QCQP lồi đều có thể viết lại dưới dạng một bài toán SOCP, tức là $$QCQP \subseteq SOCP$$. Dưới đây là cách chuyển đổi trực tiếp trong trường hợp các ma trận $$P_i$$ xác định dương ($$P_i \succ 0$$; trường hợp nửa xác định dương tổng quát xử lý tương tự bằng dạng ép đồ thị/nón bậc hai xoay).

### Nhắc lại: Bài toán Quy hoạch Bậc hai có Ràng buộc Bậc hai
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, \quad i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ với } i = 0, \dotsc, m, \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

**Bước 1.** Để tiện biến đổi (nhân đôi hàm mục tiêu và các hàm ràng buộc bất đẳng thức rồi đổi ký hiệu lại hệ số $$r_i$$), ta viết QCQP dưới dạng:
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{x^T P_0 x + 2q_0^T x + r_0} \\\\
>    &\text{subject to } &&{x^T P_i x + 2q_i^T x + r_i \leq 0}, \quad i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } && P_i \in \mathbb{S}_{++}^n \text{ với } i = 0, \dotsc, m, \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align}
>$$

**Bước 2.** Vì $$P_0$$ đối xứng xác định dương, qua phân tích trị riêng $$P_0 = Q_0 \Lambda_0^2 Q_0^T$$ (với $$Q_0$$ trực giao, $$Q_0^{-1} = Q_0^T$$ và $$\Lambda_0$$ là ma trận đường chéo chứa căn bậc hai các giá trị riêng dương), ta có thể hoàn thiện bình phương hàm mục tiêu như sau:

* $$P_0 = Q_0 \Lambda_0 \Lambda_0 Q_0^T$$
* $$I = Q_0 \Lambda_0 \Lambda_0^{-1} Q_0^{-1} = Q_0 \Lambda_0^{-1} \Lambda_0 Q_0^{-1}$$

> $$
> \begin{align}
> {x^T P_0 x + 2q_0^T x + r_0} &= {x^T P_0 x + q_0^T x + x^T q_0 + q_0^T P_0^{-1} q_0 - q_0^T P_0^{-1} q_0 + r_0}\\\\
> &= {x^T Q_0 \Lambda_0 \Lambda_0 Q_0^T x} +
>      {q_0^T Q_0 \Lambda_0^{-1} \Lambda_0 Q_0^T x} + {x^T Q_0 \Lambda_0 \Lambda_0^{-1} Q_0^T q_0} +
>      {q_0^T Q_0 \Lambda_0^{-1} \Lambda_0^{-1} Q_0^T q_0} - q_0^T P_0^{-1} q_0 + r_0\\\\
> &=(\Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0)^T(\Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0) - q_0^T P_0^{-1} q_0 + r_0\\\\
> &=\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2 - q_0^T P_0^{-1} q_0 + r_0.\\\\
> \end{align}
> $$

**Bước 3.** Áp dụng cùng phép hoàn thiện bình phương cho từng ràng buộc bất đẳng thức rồi thay vào bài toán ở Bước 1:

>$$
>\begin{align}
>    &\text{minimize}_{x} &&{\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2 - q_0^T P_0^{-1} q_0 + r_0} \\\\
>    &\text{subject to } &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq q_i^T P_i^{-1} q_i - r_i}, \quad i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$

**Bước 4.** Số hạng $$-q_0^T P_0^{-1} q_0 + r_0$$ trong hàm mục tiêu là hằng số nên có thể bỏ qua:
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2} \\\\
>    &\text{subject to } &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq q_i^T P_i^{-1} q_i - r_i}, \quad i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$

**Bước 5.** Đưa thêm biến vô hướng $$t \ge 0$$ và lấy căn bậc hai hai vế (khi các vế phải không âm, nếu có ràng buộc có vế phải âm thì bài toán vô nghiệm):
>$$
>\begin{align}
>    &\text{minimize}_{x, t} &&{t} \\\\
>    &\text{subject to } &&\lVert{\Lambda_{0} Q_0^T x + \Lambda_0^{-1} Q_0^T q_0} \rVert_2 \leq t\\\\
>    & &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2 \leq \sqrt{q_i^T P_i^{-1} q_i - r_i}}, \quad i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$

Bài toán thu được là một trường hợp đặc biệt của SOCP. Như vậy, ta có quan hệ bao hàm $$QCQP \subseteq SOCP$$.

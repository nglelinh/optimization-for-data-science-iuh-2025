---
layout: post
title: 17-08 Bài Tập Thực Hành - Primal-Dual Interior Point
chapter: '17'
order: 12
owner: GitHub Copilot
lang: vi
categories:
- chapter17
lesson_type: required
redirect_from:
  - /contents/vi/chapter17/17_07_Practical_Exercises_Primal_Dual_Interior_Point/
---

Cách nhanh nhất để thực sự làm chủ phương pháp điểm trong gốc–đối ngẫu là tự tay lắp ráp hệ phương trình đường trung tâm, giải thử hệ Newton trên giấy với bài toán 2 biến, rồi tự viết vài chục dòng mã quan sát ba phần dư $$r_{\text{prim}}, r_{\text{dual}}, \eta$$ rơi tự do về không qua từng vòng lặp. Bộ bài tập thực hành này dẫn bạn đi từ việc giải tay đường trung tâm của LP cho đến phân tích bước Newton và cài đặt thuật toán hoàn chỉnh.

## Bản đồ kiến thức nền: Quy trình 4 bước giải mọi bài tập thực hành PD-IPM

Khi tiếp cận các bài tập tính tay và lập trình bên dưới, hãy luôn đi theo bốn bước kiểm soát chặt chẽ sau để tránh sai dấu:

- **Chuẩn hóa dấu ràng buộc:** Luôn viết rõ ràng ràng buộc bất đẳng thức dưới dạng $$h_i(x) \le 0$$ (ví dụ $$x_i \ge 0 \iff -x_i \le 0$$) hoặc dùng ký hiệu LP chuẩn $$x \ge 0, s \ge 0$$; sai một dấu trừ ở $$\nabla h(x)$$ sẽ làm hỏng toàn bộ hệ KKT.
- **Lập đủ ba khối phần dư:** Viết tường minh $$r_{\text{dual}}$$, $$r_{\text{cent}}$$ và $$r_{\text{prim}}$$ trước khi lấy đạo hàm lập ma trận Jacobi. Kiểm tra kích thước của từng khối ma trận để chắc chắn hệ tuyến tính vuông.
- **Giữ chặt tính điểm trong khi cập nhật:** Trước mỗi phép cập nhật $$(x, u, v) + \theta(\Delta x, \Delta u, \Delta v)$$, luôn kiểm tra tỷ lệ chạm biên $$\theta_{\max}$$ cho cả biến gốc $$h(x) < 0$$ và biến đối ngẫu $$u > 0$$.
- **Kiểm chứng chéo kết quả:** Ở mỗi điểm tính được, kiểm tra lại tích $$x_i s_i \approx \tau$$ và đối chiếu giá trị hàm mục tiêu gốc $$f(x)$$ với giá trị đối ngẫu $$g(u, v)$$ để phát hiện lỗi tính toán ngay lập tức.

### Khung giải thích (nên đọc chậm): Khởi động bằng một phép kiểm tra 1 bước trên bài toán bậc hai có ràng buộc không âm

Trước khi bắt đầu Bài tập 1, hãy thử kiểm tra nhanh một vòng lặp trên bài toán tối ưu 2 biến:

$$\min_{x_1, x_2} \; \frac{1}{2}(x_1 - 2)^2 + \frac{1}{2}(x_2 + 1)^2 \qquad \text{với điều kiện} \qquad x_1 \ge 0, \; x_2 \ge 0.$$

Nghiệm chính xác là $$x^\star = (2, 0)$$, nhân tử $$u^\star = (0, 1)$$ (ràng buộc $$x_2 \ge 0$$ hoạt động, $$x_1 \ge 0$$ không hoạt động). Xét điểm đường trung tâm ứng với $$\tau = 0.25$$:

1. **Hệ KKT bị nhiễu:** Với $$h_1(x) = -x_1, h_2(x) = -x_2$$, ta có:
   $$x_1 - 2 - u_1 = 0, \quad x_2 + 1 - u_2 = 0, \quad x_1 u_1 = 0.25, \quad x_2 u_2 = 0.25.$$
2. **Giải tách từng biến:**
   - Với $$x_1 > 0$$: $$x_1(x_1 - 2) = 0.25 \implies x_1^2 - 2x_1 - 0.25 = 0 \implies x_1(0.25) = 1 + \sqrt{1.25} \approx 2.1180$$, $$u_1(0.25) \approx 0.1180$$.
   - Với $$x_2 > 0$$: $$x_2(x_2 + 1) = 0.25 \implies x_2^2 + x_2 - 0.25 = 0 \implies x_2(0.25) = \frac{-1 + \sqrt{2}}{2} \approx 0.2071$$, $$u_2(0.25) \approx 1.2071$$.
3. **Kiểm tra khoảng cách đối ngẫu:** $$\eta = x_1 u_1 + x_2 u_2 = 0.25 + 0.25 = 0.50 = 2\tau$$. Quan sát thấy khi $$\tau \to 0$$, $$x_1(\tau) \to 2, u_1(\tau) \to 0$$ (không hoạt động) còn $$x_2(\tau) \to 0, u_2(\tau) \to 1$$ (hoạt động) — chính xác hành vi bạn sẽ gặp xuyên suốt các bài tập bên dưới!

---

# Bài Tập Thực Hành - Phương pháp điểm trong gốc-đối ngẫu

Các bài tập được tham khảo từ Wright (1997) và Nesterov & Nemirovskii (1994).

---

## 📝 **Bài tập 1: Đường trung tâm gốc-đối ngẫu cho LP**

Cho bài toán LP:

$$
\begin{align}
\min \quad & x_1 + 2x_2 \\
\text{s.t.} \quad & x_1 + x_2 = 3 \\
& x_1, x_2 \geq 0
\end{align}
$$

**Yêu cầu:**  
a) Viết các điều kiện KKT.  
b) Thiết lập hệ điều kiện KKT bị nhiễu với tham số $$\mu$$.  
c) Tính điểm trên đường trung tâm $$x(\mu)$$ tại $$\mu = 1, 0.1, 0.01$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Các điều kiện KKT:**

$$
\begin{align}
\nabla f + A^T\nu - \lambda &= 0 \quad \text{(tính dừng)} \\
Ax &= b \quad \text{(khả thi gốc)} \\
x &\geq 0, \, \lambda \geq 0 \quad \text{(khả thi gốc và đối ngẫu)} \\
\lambda_i x_i &= 0 \quad \text{(bù chặt)}
\end{align}
$$

Thay dữ liệu bài toán vào, ta có:

$$
\begin{align}
\begin{bmatrix} 1 \\ 2 \end{bmatrix} + \nu \begin{bmatrix} 1 \\ 1 \end{bmatrix} - \begin{bmatrix} \lambda_1 \\ \lambda_2 \end{bmatrix} &= 0 \\
x_1 + x_2 &= 3 \\
\lambda_1 x_1 = \lambda_2 x_2 &= 0
\end{align}
$$

---

**b) Điều kiện KKT bị nhiễu (phương trình đường trung tâm):**

Thay điều kiện bù chặt $$\lambda_i x_i = 0$$ bằng:

$$\lambda_i x_i = \mu \quad \forall i$$

Ta thu được hệ:

$$
\begin{cases}
1 + \nu - \lambda_1 = 0 \\
2 + \nu - \lambda_2 = 0 \\
x_1 + x_2 = 3 \\
\lambda_1 x_1 = \mu \\
\lambda_2 x_2 = \mu
\end{cases}
$$

---

**c) Giải tìm đường trung tâm:**

Từ (1): $$\lambda_1 = 1 + \nu$$  
Từ (2): $$\lambda_2 = 2 + \nu$$  
Từ (4): $$x_1 = \frac{\mu}{1 + \nu}$$  
Từ (5): $$x_2 = \frac{\mu}{2 + \nu}$$

Thay vào phương trình (3):

$$\frac{\mu}{1+\nu} + \frac{\mu}{2+\nu} = 3$$

$$\mu\left(\frac{1}{1+\nu} + \frac{1}{2+\nu}\right) = 3$$

$$\mu \cdot \frac{(2+\nu) + (1+\nu)}{(1+\nu)(2+\nu)} = 3$$

$$\mu \cdot \frac{3 + 2\nu}{(1+\nu)(2+\nu)} = 3$$

$$(1+\nu)(2+\nu) = \mu\left(1 + \frac{2\nu}{3}\right)$$

Giải phương trình bậc hai: $$\nu^2 + 3\nu + 2 = \mu + \frac{2\mu\nu}{3}$$.

**Với $$\mu = 1$$:**

$$\nu^2 + 3\nu + 2 = 1 + \frac{2\nu}{3}$$

$$\nu^2 + \frac{7\nu}{3} + 1 = 0$$

$$\nu = \frac{-7/3 \pm \sqrt{49/9 - 4}}{2} \in \{-0.566, -1.768\}$$

Chỉ nghiệm $$\nu > -1$$ mới đảm bảo $$\lambda_1, \lambda_2 > 0$$, do đó chọn $$\nu \approx -0.566$$, suy ra $$x_1 = \frac{1}{1-0.566} \approx 2.30$$, $$x_2 = \frac{1}{2-0.566} \approx 0.70$$ (kiểm tra: $$x_1 + x_2 = 3$$ ✓).

**Với $$\mu = 0.1$$:** $$\nu \approx -0.9656$$, $$x \approx (2.90, 0.097)$$.

**Với $$\mu = 0.01$$:** $$\nu \approx -0.9967$$, $$x \approx (2.99, 0.010)$$.

**Khi $$\mu \to 0$$:** $$x^* \to (3, 0)$$ (nghiệm tối ưu của bài toán gốc), $$\nu^* \to -1$$.

</details>

---

## 📝 **Bài tập 2: Bước Newton cho hệ gốc-đối ngẫu**

Xét bài toán LP từ Bài tập 1. Tại điểm lặp $$(x, \lambda, \nu)^{(k)}$$, xét hệ Newton:

$$
\begin{bmatrix}
0 & A^T & -I \\
A & 0 & 0 \\
\Lambda & 0 & X
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta \nu \\
\Delta \lambda
\end{bmatrix}
=
-\begin{bmatrix}
r_d \\
r_p \\
r_c
\end{bmatrix}
$$

với $$\Lambda = \text{diag}(\lambda)$$, $$X = \text{diag}(x)$$.

**Yêu cầu:**  
a) Viết các phần dư $$r_d, r_p, r_c$$.  
b) Rút gọn hệ phương trình bằng cách khử $$\Delta\lambda$$.  
c) Tính $$\Delta x$$ tại $$x = (1, 1)$$, $$\lambda = (2, 3)$$, $$\nu = -1$$, $$\mu = 0.5$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Các phần dư:**

$$
\begin{align}
r_d &= \nabla f + A^T\nu - \lambda = \begin{bmatrix} 1 \\ 2 \end{bmatrix} + \nu \begin{bmatrix} 1 \\ 1 \end{bmatrix} - \begin{bmatrix} \lambda_1 \\ \lambda_2 \end{bmatrix} \\
r_p &= Ax - b = x_1 + x_2 - 3 \\
r_c &= \Lambda X e - \mu e = \begin{bmatrix} \lambda_1 x_1 - \mu \\ \lambda_2 x_2 - \mu \end{bmatrix}
\end{align}
$$

---

**b) Khử $$\Delta\lambda$$:**

Từ hàng thứ 3: $$\Lambda \Delta x + X \Delta\lambda = -r_c$$, suy ra:

$$\Delta\lambda = -X^{-1}(\Lambda \Delta x + r_c)$$

Thay vào hàng thứ 1:

$$A^T \Delta\nu - \Delta\lambda = -r_d$$

$$A^T \Delta\nu + X^{-1}(\Lambda \Delta x + r_c) = -r_d$$

$$\Lambda X^{-1} \Delta x + A^T \Delta\nu = -r_d - X^{-1}r_c$$

Kết hợp với hàng thứ 2, ta thu được hệ rút gọn:

$$
\begin{bmatrix}
\Lambda X^{-1} & A^T \\
A & 0
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta \nu
\end{bmatrix}
=
\begin{bmatrix}
-r_d - X^{-1}r_c \\
-r_p
\end{bmatrix}
$$

---

**c) Tính toán bằng số:**

Với $$x = (1, 1)$$, $$\lambda = (2, 3)$$, $$\nu = -1$$, $$\mu = 0.5$$:

$$r_d = \begin{bmatrix} 1-1-2 \\ 2-1-3 \end{bmatrix} = \begin{bmatrix} -2 \\ -2 \end{bmatrix}$$

$$r_p = 1 + 1 - 3 = -1$$

$$r_c = \begin{bmatrix} 2 \cdot 1 - 0.5 \\ 3 \cdot 1 - 0.5 \end{bmatrix} = \begin{bmatrix} 1.5 \\ 2.5 \end{bmatrix}$$

$$\Lambda X^{-1} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$$

$$-r_d - X^{-1}r_c = \begin{bmatrix} 2 \\ 2 \end{bmatrix} - \begin{bmatrix} 1.5 \\ 2.5 \end{bmatrix} = \begin{bmatrix} 0.5 \\ -0.5 \end{bmatrix}$$

Hệ phương trình tuyến tính:

$$
\begin{bmatrix}
2 & 0 & 1 \\
0 & 3 & 1 \\
1 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
\Delta x_1 \\
\Delta x_2 \\
\Delta \nu
\end{bmatrix}
=
\begin{bmatrix}
0.5 \\
-0.5 \\
1
\end{bmatrix}
$$

Giải hệ thu được $$\Delta x = (0.8, 0.2)$$, $$\Delta\nu = -1.1$$ (kiểm tra: $$2(0.8) - 1.1 = 0.5$$, $$3(0.2) - 1.1 = -0.5$$, $$0.8 + 0.2 = 1$$ ✓).

</details>

---

## 📝 **Bài tập 3: Thuật toán Dự báo – Hiệu chỉnh Mehrotra (Predictor-Corrector)**

Thuật toán Mehrotra kết hợp hai bước dự báo (predictor) và hiệu chỉnh (corrector):

**Bước dự báo (Predictor):** $$\mu = 0$$ (hướng affine scaling)  
**Bước hiệu chỉnh (Corrector):** $$\mu = \sigma \cdot \frac{x^T\lambda}{n}$$ với $$\sigma \in (0, 1)$$

**Yêu cầu:**  
a) Giải thích trực giác của hai bước này.  
b) Trình bày cách tính $$\sigma$$ từ bước dự báo.  
c) Áp dụng minh họa cho bài toán LP từ Bài tập 1.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Trực giác:**

**Bước dự báo (affine):** Hướng thẳng về tập nghiệm tối ưu ($$\mu = 0$$), tạo bước tiến mạnh nhằm giảm nhanh khoảng cách đối ngẫu.

**Bước hiệu chỉnh (centering):** Kéo điểm lặp trở lại gần đường trung tâm, giúp duy trì tính khả thi và đảm bảo hội tụ ổn định.

**Tham số $$\sigma$$ thích nghi** dựa trên chất lượng của bước dự báo:
- Nếu bước dự báo giảm mạnh khoảng cách đối ngẫu → chọn $$\sigma$$ nhỏ (tiến mạnh hơn).
- Nếu bước dự báo tiến được ít → chọn $$\sigma$$ lớn (ưu tiên định tâm an toàn hơn).

---

**b) Tính $$\sigma$$:**

Sau bước dự báo affine thu được $$(\tilde{x}, \tilde{\lambda})$$:

$$\tilde{\mu} = \frac{\tilde{x}^T\tilde{\lambda}}{n}$$

$$\sigma = \left(\frac{\tilde{\mu}}{\mu}\right)^3$$

(quy tắc lũy thừa bậc ba mang lại tốc độ hội tụ nhanh trong thực tế).

---

**c) Ví dụ minh họa:**

Điểm hiện tại: $$x = (2, 1)$$, $$\lambda = (1, 2)$$, $$\mu = \frac{2 \cdot 1 + 1 \cdot 2}{2} = 2$$.

**Bước dự báo ($$\mu_{\text{aff}} = 0$$):**

$$\tilde{x} = (2.5, 0.5)$$, $$\tilde{\lambda} = (0.5, 1.5)$$

$$\tilde{\mu} = \frac{2.5 \cdot 0.5 + 0.5 \cdot 1.5}{2} = \frac{2}{2} = 1$$

$$\sigma = \left(\frac{1}{2}\right)^3 = 0.125$$

**Bước hiệu chỉnh:** Mục tiêu mới $$\mu_{\text{new}} = 0.125 \cdot 2 = 0.25$$.

Giá trị $$\sigma$$ nhỏ cho phép giảm mạnh tham số rào cản ở bước này.

</details>

---

## 📝 **Bài tập 4: Khởi tạo không khả thi (Infeasible Start)**

Cho điểm khởi tạo không khả thi $$(x^{(0)}, \lambda^{(0)}, \nu^{(0)})$$ không thỏa mãn ràng buộc đẳng thức $$Ax = b$$.

**Yêu cầu:**  
a) Trình bày cách xử lý phần dư để cho phép điểm khởi tạo không khả thi.  
b) Giải thích cơ chế hội tụ về miền khả thi gốc – đối ngẫu.  
c) Minh họa với bài toán LP và $$x^{(0)} = (1, 1)$$ (không thỏa mãn $$x_1 + x_2 = 3$$).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Xử lý phần dư:**

Cho phép phần dư gốc ban đầu $$r_p = Ax - b \neq 0$$. Hệ phương trình Newton giữ nguyên cấu trúc:

$$
\begin{bmatrix}
0 & A^T & -I \\
A & 0 & 0 \\
\Lambda & 0 & X
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta \nu \\
\Delta \lambda
\end{bmatrix}
=
-\begin{bmatrix}
r_d \\
r_p \\
r_c
\end{bmatrix}
$$

Qua các vòng lặp, chuẩn phần dư $$\|r_p\|$$ giảm dần về $$0$$.

---

**b) Hội tụ:**

Mỗi bước Newton làm giảm đồng thời chuẩn tổng hợp $$\|(r_d, r_p, r_c)\|$$ (và hội tụ bậc hai khi ở gần nghiệm). Trong phương pháp điểm trong gốc-đối ngẫu khởi tạo không khả thi, cả biến gốc $$x$$ và biến đối ngẫu $$(\lambda, \nu)$$ cùng tiến về miền khả thi và nghiệm tối ưu.

---

**c) Ví dụ minh họa:**

Với $$x^{(0)} = (1, 1)$$, ta có $$r_p = 1 + 1 - 3 = -1$$.

Sau một bước Newton đầy đủ ($$\alpha = 1$$), chẳng hạn $$x^{(1)} = (1.5, 1.5)$$, ta có $$r_p = 0$$ (đạt khả thi gốc) vì phương trình hàng 2 đảm bảo $$A\Delta x = -r_p$$. (Nếu dùng độ dài bước $$\alpha < 1$$ thì $$r_p$$ giảm theo hệ số $$1 - \alpha$$.) Sau đó thuật toán tiếp tục như PD-IPM chuẩn.

</details>

---

## 📝 **Bài tập 5: Tính tự tương thích (Self-Concordance) và độ phức tạp đa thức**

Các phương pháp điểm trong đạt độ phức tạp thời gian đa thức nhờ sử dụng hàm chắn tự tương thích (self-concordant barriers).

**Yêu cầu:**  
a) Phát biểu định nghĩa tính tự tương thích.  
b) Chứng minh hàm chắn logarit $$\phi(x) = -\sum \log x_i$$ là hàm tự tương thích.  
c) Giải thích vì sao tính chất này dẫn đến số vòng lặp $$O(\sqrt{n} \log(1/\epsilon))$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tính tự tương thích:**

Hàm lồi khả vi ba lần $$\phi$$ được gọi là tự tương thích nếu với mọi hướng $$h$$:

$$|\phi'''(x)[h, h, h]| \leq 2(\phi''(x)[h, h])^{3/2}$$

**Ý nghĩa:** Đạo hàm bậc ba bị chặn bởi lũy thừa $$3/2$$ của đạo hàm bậc hai, đảm bảo xấp xỉ bậc hai cục bộ của phương pháp Newton có độ ổn định nhất quán trên toàn miền.

---

**b) Chứng minh cho hàm chắn logarit:**

$$\phi(x) = -\sum_{i=1}^n \log x_i$$

$$\phi'(x) = -\sum \frac{1}{x_i} e_i$$

$$\phi''(x) = \sum \frac{1}{x_i^2} e_i e_i^T = \text{diag}(1/x_1^2, \ldots, 1/x_n^2)$$

$$\phi'''(x)[h, h, h] = -\sum \frac{2}{x_i^3} h_i^3$$

Kiểm tra bất đẳng thức:

$$|\phi'''[h,h,h]| = 2\sum \frac{|h_i|^3}{x_i^3} \leq 2\left(\sum \frac{h_i^2}{x_i^2}\right)^{3/2} = 2(\phi''[h,h])^{3/2}$$ ✓

---

**c) Độ phức tạp thời gian đa thức:**

Tính tự tương thích đảm bảo bước Newton có miền hội tụ bậc hai xác định trước và mức giảm hàm mục tiêu ổn định.

**Ý chính:** Tham số chắn của $$\phi(x) = -\sum_{i=1}^n \log x_i$$ trên góc phần tư dương $$\mathbb{R}^n_+$$ là $$\vartheta = n$$. Mỗi vòng lặp cho phép giảm $$\mu$$ theo hệ số $$\left(1 - \frac{1}{\sqrt{\vartheta}}\right)$$ chỉ với $$O(1)$$ bước Newton, nên chỉ cần tổng cộng $$O(\sqrt{\vartheta}\log(1/\epsilon)) = O(\sqrt{n}\log(1/\epsilon))$$ vòng lặp để đưa $$\mu$$ xuống dưới $$\epsilon$$.

Đây là **độ phức tạp đa thức** (so với độ phức tạp hàm mũ trong trường hợp xấu nhất của phương pháp đơn hình).

</details>

---

## 💡 **Tổng kết**

### **Các thành phần chính của PD-IPM:**

| Thành phần | Vai trò |
|-----------|---------|
| **Đường trung tâm (Central path)** | Quỹ đạo trơn dẫn về nghiệm tối ưu |
| **Điều kiện KKT bị nhiễu** | Thay điều kiện bù chặt bằng $$\lambda x = \mu e$$ |
| **Hệ Newton** | Hệ phương trình tuyến tính khối $$3\times 3$$ cập nhật đồng thời biến gốc và đối ngẫu |
| **Dự báo – Hiệu chỉnh (Predictor-Corrector)** | Cân bằng giữa tốc độ giảm khoảng cách đối ngẫu và bước định tâm |
| **Khởi tạo không khả thi (Infeasible start)** | Xử lý trực tiếp điểm khởi tạo chưa thỏa mãn $$Ax = b$$ |

### **Độ phức tạp tính toán:**

- **Mỗi vòng lặp:** $$O(n^3)$$ (phân rã ma trận)
- **Tổng số vòng lặp:** $$O(\sqrt{n} \log(1/\epsilon))$$
- **Tổng thể cho LP:** $$O(n^{3.5} \log(1/\epsilon))$$

---

## 📚 **Tài liệu tham khảo**

1. Wright, S. J. (1997). *Primal-Dual Interior-Point Methods*. SIAM.
2. Nesterov, Y., & Nemirovskii, A. (1994). *Interior-Point Polynomial Algorithms*.
3. Mehrotra, S. (1992). "On the Implementation of a Primal-Dual IPM". *SIAM Journal*.

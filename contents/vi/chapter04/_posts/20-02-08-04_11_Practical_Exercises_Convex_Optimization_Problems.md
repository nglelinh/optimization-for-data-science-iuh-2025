---
layout: post
title: 04-11 Bài Tập Thực Hành - Bài Toán Tối Ưu Convex
chapter: '4'
order: 12
owner: GitHub Copilot
lang: vi
categories:
- chapter04
lesson_type: required
redirect_from:
  - /contents/vi/chapter04/04_10_Practical_Exercises_Convex_Optimization_Problems/
---

Hiểu lý thuyết tối ưu hóa lồi giống như đọc sách dạy bơi trên bờ; chỉ khi tự tay cầm một bài toán thực tế lộn xộn — có giá trị tuyệt đối, có chuẩn, có cực đại lồng nhau, có tham số nhiễu — và biến đổi nó về dạng chuẩn rồi chạy kiểm chứng bằng code, các khái niệm của Chương 04 mới thực sự trở thành kỹ năng của riêng bạn.

Bộ bài tập thực hành này dẫn bạn đi qua năm kỹ năng cốt lõi của một kỹ sư tối ưu hóa: chuyển đổi dạng chuẩn, phân tích điều kiện tối ưu, độ nhạy nghiệm theo tham số ràng buộc, thiết kế nới lỏng cho bài toán khó và mô hình hóa tối ưu bền vững (robust optimization) khi dữ liệu có bất định.

## Kiến thức cần nhớ: Quy trình 4 bước giải bài tập thực hành tối ưu lồi

Khi đối mặt với bất kỳ bài tập mô hình hóa hay chuyển đổi nào trong bộ bài này, hãy đi theo đúng khung bốn bước:

- **Bước 1 — Chuẩn hóa ngôn ngữ (Standard Form Canonicalization):** Đưa mọi cực đại hóa về cực tiểu hóa ($$\max f \iff \min -f$$), chuyển mọi bất đẳng thức $$a \ge b$$ về $$b - a \le 0$$, và tách các hàm không trơn như $$|x_i|$$ hay $$\max_k (a_k^T x + b_k)$$ bằng cách thêm biến phụ (epigraph reformulation).
- **Bước 2 — Kiểm định tính lồi & Ràng buộc tích cực:** Xác định rõ hàm nào lồi, hàm nào affine; tìm điểm cực tiểu không ràng buộc trước để biết ràng buộc nào thực sự phải kích hoạt.
- **Bước 3 — Phân tích độ nhạy & Đối ngẫu (Sensitivity & Perturbation):** Khi vế phải ràng buộc thay đổi một lượng nhỏ $$\Delta b$$, giá trị tối ưu thay đổi xấp xỉ $$-\lambda^\star \Delta b$$ — công cụ cực mạnh để định giá tài nguyên biên.
- **Bước 4 — Xử lý bất định & Phi lồi (Robust & Relaxation):** Với bài toán có tham số nhiễu trong tập bất định (ví dụ hình cầu $$\|u\|_2 \le \rho$$), dùng bất đẳng thức Cauchy-Schwarz để chuyển ràng buộc "với mọi $$u$$" thành dạng đóng lồi (thường là ràng buộc chuẩn $$\ell_2$$).

### Giải thích: Chuyển đổi một bài toán có trị tuyệt đối & bất định về dạng chuẩn lồi

Xét bài toán: tìm $$x \in \mathbb{R}^2$$ cực tiểu hóa $$f(x) = |x_1 - 2| + 2|x_2 + 1|$$ thỏa mãn ràng buộc bền vững
$$(a_0 + u)^T x \le 3 \quad \text{với mọi } u \in \mathbb{R}^2 \text{ thỏa } \|u\|_2 \le 0.5, \quad \text{trong đó } a_0 = (1, 1)^T.$$

1. **Khử trị tuyệt đối bằng biến phụ $$t_1, t_2$$:**
   Đặt $$|x_1 - 2| \le t_1$$ và $$|x_2 + 1| \le t_2$$. Tương đương với 4 bất đẳng thức tuyến tính:
   $$x_1 - 2 \le t_1,\quad -(x_1 - 2) \le t_1,\quad x_2 + 1 \le t_2,\quad -(x_2 + 1) \le t_2.$$
   Hàm mục tiêu trở thành hàm tuyến tính $$t_1 + 2t_2$$!
2. **Chuyển ràng buộc vô hạn "với mọi $$u$$" về dạng đóng lồi:**
   Ràng buộc đúng với mọi $$\|u\|_2 \le 0.5$$ khi và chỉ khi giá trị xấu nhất (lớn nhất) cũng $$\le 3$$:
   $$\max_{\|u\|_2 \le 0.5} (a_0^T x + u^T x) = a_0^T x + 0.5 \|x\|_2 \le 3.$$
   (Dấu bằng đạt được theo Cauchy-Schwarz khi $$u = 0.5 \frac{x}{\|x\|_2}$$.)
3. **Kiểm tra bài toán dạng chuẩn cuối cùng:**
   $$\min_{x, t} \; t_1 + 2t_2 \quad \text{s.t.} \quad \begin{cases} x_1 - t_1 - 2 \le 0,\; -x_1 - t_1 + 2 \le 0 \\ x_2 - t_2 + 1 \le 0,\; -x_2 - t_2 - 1 \le 0 \\ x_1 + x_2 + 0.5\sqrt{x_1^2 + x_2^2} - 3 \le 0 \end{cases}$$
   Mọi hàm đều lồi rõ ràng (thực chất là một bài toán SOCP)! Thử điểm $$x = (2, -1)$$: $$x_1 + x_2 + 0.5\sqrt{4+1} = 1 + 0.5\sqrt{5} \approx 2.118 \le 3$$, nên $$x^\star = (2, -1)$$ khả thi và đạt ngay $$f^\star = 0$$!

---

# Bài Tập Thực Hành - Bài Toán Tối Ưu Hóa Lồi

## 📝 **Bài tập 1: Chuyển đổi về dạng chuẩn**

**Đề bài:** Chuyển đổi các bài toán sau về dạng chuẩn của tối ưu hóa lồi:

a) **Ràng buộc hỗn hợp:**
$$\min_{x \in \mathbb{R}^3} x_1^2 + x_2^2 + x_3^2$$
$$\text{s.t.} \quad x_1 + 2x_2 - x_3 = 5, \quad x_1 - x_2 \geq 3, \quad x_2 \leq 4, \quad x_3 \text{ tự do}$$

b) **Bài toán minimax:**
$$\min_x \max_{i=1,\ldots,m} (a_i^T x + b_i)$$

c) **Bình phương tối thiểu bền vững (robust least squares):**
$$\min_x \max_{\lVert u \rVert_2 \leq 1} \lVert (A + \sum_{i=1}^k u_i B_i)x - b \rVert_2^2$$

**Yêu cầu:**
1. Chuyển bài toán về dạng chuẩn của tối ưu hóa lồi.
2. Xác định rõ biến quyết định, các ràng buộc và hàm mục tiêu.
3. Kiểm tra tính lồi của bài toán sau khi biến đổi.
4. Thảo luận tác động về mặt tính toán.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Bài toán có ràng buộc hỗn hợp**

**Xử lý biến tự do:** tách $$x_3 = x_3^+ - x_3^-$$ với $$x_3^+, x_3^- \geq 0$$.

**Đổi chiều bất đẳng thức:** $$x_1 - x_2 \geq 3 \Rightarrow -x_1 + x_2 \leq -3$$.

**Dạng chuẩn hóa:**
$$\min_{x_1,x_2,x_3^+,x_3^-} x_1^2 + x_2^2 + (x_3^+)^2 + (x_3^-)^2 - 2x_3^+ x_3^-$$
$$\text{s.t.} \quad x_1 + 2x_2 - x_3^+ + x_3^- = 5$$
$$\quad -x_1 + x_2 \leq -3$$
$$\quad x_2 \leq 4$$
$$\quad x_3^+, x_3^- \geq 0 \quad (x_1, x_2 \text{ vẫn tự do vì bài toán gốc không có ràng buộc } x_1, x_2 \geq 0)$$

**Lưu ý:** Vì $$(x_3^+ - x_3^-)^2 = (x_3^+)^2 + (x_3^-)^2 - 2x_3^+ x_3^-$$, hàm mục tiêu vẫn lồi (ma trận Hessian nửa xác định dương). Việc tách biến tự do thực chất chỉ cần thiết cho dạng chuẩn của quy hoạch tuyến tính (LP); đối với bộ giải quy hoạch bậc hai (QP), ta không cần tách biến này.

**Cách tiếp cận trực tiếp:** giữ nguyên $$x_3$$ tự do và giải trực tiếp bài toán QP lồi:
$$\min_{x_1,x_2,x_3} x_1^2 + x_2^2 + x_3^2$$
$$\text{s.t.} \quad x_1 + 2x_2 - x_3 = 5, \quad x_1 - x_2 \geq 3, \quad x_2 \leq 4$$

**Bước 2: Bài toán minimax**

**Biểu diễn trên đồ thị (epigraph):**
$$\min_{x,t} t$$
$$\text{s.t.} \quad a_i^T x + b_i \leq t, \quad i = 1,\ldots,m$$

**Tính lồi:** Hàm mục tiêu tuyến tính và các ràng buộc tuyến tính $$\Rightarrow$$ đây là một bài toán quy hoạch tuyến tính (LP).

**Bước 3: Bình phương tối thiểu bền vững**

**Hàm mục tiêu trường hợp xấu nhất:**
$$\max_{\lVert u \rVert_2 \leq 1} \lVert (A + \sum_{i=1}^k u_i B_i)x - b \rVert_2^2$$

**Viết lại dưới dạng ma trận:** $$\max_{\lVert u \rVert_2 \leq 1} \lVert Ax - b + (\sum_{i=1}^k u_i B_i)x \rVert_2^2$$.

**Đặt** $$q(x) = Ax - b$$ và $$P(x) = [B_1 x \ \cdots \ B_k x]$$ (đều là hàm affine theo $$x$$). Khi đó $$(\sum_i u_i B_i)x = P(x)u$$ và giá trị trường hợp xấu nhất là $$\max_{\lVert u \rVert_2 \leq 1} \lVert q(x) + P(x)u \rVert_2^2$$. Lưu ý rằng biểu thức này **không** bằng $$\lVert q \rVert_2^2 + \lVert \sum_i B_i x \rVert_2^2$$.

**Biểu diễn quy hoạch nửa xác định (bổ đề S, Boyd & Vandenberghe §6.4.2):**
$$\min_{x,t,\lambda} t + \lambda$$
$$\text{s.t.} \quad \begin{bmatrix} I & P(x) & q(x) \\ P(x)^T & \lambda I & 0 \\ q(x)^T & 0 & t \end{bmatrix} \succeq 0$$

**Chặn trên dạng SOCP (đơn giản hơn nhưng chặt hơn về mức bảo thủ):** do $$\lVert P(x)u \rVert_2 \leq \lVert P(x) \rVert_F$$ khi $$\lVert u \rVert_2 \leq 1$$, ta thu được bài toán xấp xỉ:
$$\min_{x} \ \lVert Ax - b \rVert_2 + \lVert P(x) \rVert_F$$

</details>

---

## 📝 **Bài tập 2: Phân tích điều kiện tối ưu**

**Đề bài:** Phân tích các điều kiện tối ưu cho các bài toán sau:

a) **Bài toán bậc hai có ràng buộc:**
$$\min_x \frac{1}{2}x^T Q x + c^T x \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$
với $$Q \succeq 0$$.

b) **Cực đại hóa entropy:**
$$\max_x -\sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad \sum_{i=1}^n x_i = 1, \quad \sum_{i=1}^n a_i x_i = \alpha, \quad x \geq 0$$

c) **Máy vectơ hỗ trợ (Support Vector Machine - SVM):**
$$\min_{w,b,\xi} \frac{1}{2}\lVert w \rVert_2^2 + C\sum_{i=1}^m \xi_i$$
$$\text{s.t.} \quad y_i(w^T x_i + b) \geq 1 - \xi_i, \quad \xi_i \geq 0$$

**Yêu cầu:**
1. Thiết lập các điều kiện KKT.
2. Phân tích điều kiện bù lỏng (complementary slackness).
3. Đặc trưng hóa nghiệm tối ưu.
4. Giải thích ý nghĩa hình học.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Bài toán bậc hai có ràng buộc**

**Hàm Lagrange:**
$$L(x,\lambda,\mu) = \frac{1}{2}x^T Q x + c^T x + \lambda^T(Ax - b) - \mu^T x$$

**Các điều kiện KKT:**
- **Điều kiện dừng:** $$Qx + c + A^T \lambda - \mu = 0$$
- **Tính khả thi gốc:** $$Ax = b, \quad x \geq 0$$
- **Tính khả thi đối ngẫu:** $$\mu \geq 0$$
- **Điều kiện bù lỏng:** $$\mu_i x_i = 0, \quad \forall i$$

**Phân tích:**
- Nếu $$x_i > 0$$ thì $$\mu_i = 0$$.
- Nếu $$x_i = 0$$ thì $$\mu_i \geq 0$$ (chi phí rút gọn).

**Cấu trúc nghiệm:** Các phương pháp tập tích cực (active-set methods) tận dụng cấu trúc thưa này để cập nhật tập các ràng buộc chặt.

**Bước 2: Cực đại hóa entropy**

**Chuyển về bài toán cực tiểu hóa:**
$$\min_x \sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad \sum_{i=1}^n x_i = 1, \quad \sum_{i=1}^n a_i x_i = \alpha, \quad x \geq 0$$

**Hàm Lagrange:**
$$L(x,\lambda_1,\lambda_2,\mu) = \sum_{i=1}^n x_i \log x_i + \lambda_1\left(\sum_{i=1}^n x_i - 1\right) + \lambda_2\left(\sum_{i=1}^n a_i x_i - \alpha\right) - \sum_{i=1}^n \mu_i x_i$$

**Các điều kiện KKT:**
- **Điều kiện dừng:** $$\log x_i + 1 + \lambda_1 + \lambda_2 a_i - \mu_i = 0$$
- **Điều kiện bù lỏng:** $$\mu_i x_i = 0$$

**Nghiệm tối ưu:**
$$x_i^* = e^{-1 - \lambda_1 - \lambda_2 a_i}$$ (luôn dương, suy ra $$\mu_i = 0$$); sau khi chuẩn hóa theo điều kiện $$\sum_i x_i = 1$$:
$$x_i^* = \frac{e^{-\lambda_2 a_i}}{\sum_j e^{-\lambda_2 a_j}}$$

**Dạng họ mũ:** Phân phối có entropy cực đại dưới ràng buộc mô-men luôn thuộc họ phân phối mũ (phân phối Boltzmann/Gibbs).

**Bước 3: Máy vectơ hỗ trợ (SVM)**

**Hàm Lagrange:**
$$L(w,b,\xi,\alpha,\beta) = \frac{1}{2}\lVert w \rVert_2^2 + C\sum_{i=1}^m \xi_i - \sum_{i=1}^m \alpha_i[y_i(w^T x_i + b) - 1 + \xi_i] - \sum_{i=1}^m \beta_i \xi_i$$

**Các điều kiện KKT:**
- **Điều kiện dừng:**
  - $$\nabla_w L = w - \sum_{i=1}^m \alpha_i y_i x_i = 0 \Rightarrow w = \sum_{i=1}^m \alpha_i y_i x_i$$
  - $$\nabla_b L = -\sum_{i=1}^m \alpha_i y_i = 0$$
  - $$\nabla_{\xi_i} L = C - \alpha_i - \beta_i = 0$$

- **Điều kiện bù lỏng:**
  - $$\alpha_i[y_i(w^T x_i + b) - 1 + \xi_i] = 0$$
  - $$\beta_i \xi_i = 0$$

**Phân loại các điểm dữ liệu theo $$\alpha_i$$:**
- $$\alpha_i = 0$$: $$x_i$$ không phải là vectơ hỗ trợ (nằm đúng phía và ngoài biên).
- $$0 < \alpha_i < C$$: $$x_i$$ nằm chính xác trên biên ($$\xi_i = 0$$).
- $$\alpha_i = C$$: $$x_i$$ vi phạm biên hoặc nằm trên biên với $$\xi_i \geq 0$$.

</details>

---

## 📝 **Bài tập 3: Đối ngẫu và phân tích độ nhạy**

**Đề bài:** Xét bài toán quy hoạch tuyến tính:
$$\min_x c^T x \quad \text{s.t.} \quad Ax \leq b, \quad x \geq 0$$

a) Thiết lập bài toán đối ngẫu và phân tích điều kiện đối ngẫu mạnh.
b) Thực hiện phân tích độ nhạy: giá trị tối ưu thay đổi thế nào khi $$b$$ thay đổi?
c) Giải thích ý nghĩa kinh tế của giá bóng (shadow prices).
d) Phân tích quy hoạch tham số với $$b(\theta) = b_0 + \theta d$$.

**Yêu cầu:**
1. Phân tích đầy đủ bài toán đối ngẫu.
2. Tính toán độ nhạy theo vế phải $$b$$.
3. Giải thích ý nghĩa kinh tế.
4. Mô tả quỹ đạo nghiệm theo tham số $$\theta$$.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Thiết lập bài toán đối ngẫu**

**Bài toán gốc (primal):** $$\min_x c^T x \text{ s.t. } Ax \leq b, \; x \geq 0$$

**Hàm Lagrange (đặt miền $$x \geq 0$$):** $$L(x,\lambda) = c^T x + \lambda^T(Ax - b)$$

**Hàm đối ngẫu:** $$g(\lambda) = \inf_{x \geq 0} L(x,\lambda) = \inf_{x \geq 0} (c + A^T \lambda)^T x - \lambda^T b$$

**Điều kiện để hàm đối ngẫu hữu hạn:** $$c + A^T \lambda \geq 0$$.

**Bài toán đối ngẫu:**
$$\max_\lambda -\lambda^T b \quad \text{s.t.} \quad A^T \lambda + c \geq 0, \quad \lambda \geq 0$$

Hoặc viết tương đương bằng cách đặt $$\nu = -\lambda$$:
$$\max_\nu b^T \nu \quad \text{s.t.} \quad A^T \nu \leq c, \quad \nu \leq 0$$

**Bước 2: Điều kiện đối ngẫu mạnh**

**Điều kiện Slater:** Tồn tại $$x > 0$$ sao cho $$Ax < b$$.

**Định lý cơ bản của quy hoạch tuyến tính:** Đối với LP, đối ngẫu mạnh luôn đúng miễn là cả bài toán gốc và bài toán đối ngẫu đều khả thi (không nhất thiết cần điểm khả thi chặt).

**Điều kiện bù lỏng:**
- $$(c + A^T \lambda^*)_j x_j^* = 0, \quad \forall j$$
- $$\lambda_i^* (Ax^* - b)_i = 0, \quad \forall i$$

**Bước 3: Phân tích độ nhạy**

**Hàm giá trị tối ưu:** $$f^*(b) = \min\{c^T x : Ax \leq b, \; x \geq 0\}$$.

**Định lý bao (Envelope theorem):** Tại các điểm mà $$f^*$$ khả vi,
$$\nabla_b f^*(b) = -\lambda^*(b) \leq 0$$
(khi nới rộng vế phải $$b$$, tập khả thi lớn hơn nên giá trị cực tiểu $$f^*(b)$$ giảm hoặc giữ nguyên).

**Ý nghĩa giá bóng (shadow price):** $$\lambda_i^*$$ đo mức giảm cận biên của chi phí tối ưu khi tăng thêm một đơn vị tài nguyên thứ $$i$$.

**Ứng dụng thực tế:**
- Giải cặp bài toán gốc – đối ngẫu.
- Nghiệm đối ngẫu $$\lambda^*$$ cung cấp trực tiếp các hệ số độ nhạy.
- Kết quả có hiệu lực cục bộ trong một lân cận của giá trị $$b$$ hiện tại (khi cơ sở tối ưu chưa thay đổi).

**Bước 4: Quy hoạch tham số**

**Bài toán tham số hóa:** $$\min_x c^T x \text{ s.t. } Ax \leq b_0 + \theta d, \; x \geq 0$$.

**Giá trị tối ưu theo tham số:** $$f^*(\theta) = f^*(b_0 + \theta d)$$.

**Tính chất:** $$f^*(\theta)$$ là hàm lồi và tuyến tính từng khúc theo $$\theta$$.

**Điểm tới hạn (breakpoints):** Xuất hiện tại các giá trị $$\theta$$ nơi cơ sở tối ưu thay đổi.

**Quỹ đạo nghiệm:**
1. Bắt đầu từ nghiệm tối ưu tại $$\theta = 0$$.
2. Tăng $$\theta$$ cho đến khi một biến cơ sở chạm 0 (hoặc tính khả thi thay đổi).
3. Thực hiện phép xoay (pivot) sang cơ sở tối ưu mới.
4. Lặp lại cho đến khi đạt giá trị $$\theta$$ mong muốn.

</details>

---

## 📝 **Bài tập 4: Các kỹ thuật nới lỏng (Relaxation)**

**Đề bài:** Xét bài toán quy hoạch nguyên nhị phân:
$$\min_x c^T x \quad \text{s.t.} \quad Ax \leq b, \quad x_i \in \{0,1\}, \quad i \in I$$

a) **Nới lỏng LP:** nới lỏng điều kiện $$x_i \in [0,1]$$.
b) **Nới lỏng Lagrange:** đưa một tập con các ràng buộc vào hàm mục tiêu.
c) **Nới lỏng SDP:** nâng biến với $$x_i x_j = X_{ij}$$ và $$X \succeq 0$$.
d) **Bao lồi (convex hull):** mô tả $$\text{conv}(\text{tập điểm nguyên khả thi})$$.

**Yêu cầu:**
1. Phát biểu các dạng nới lỏng.
2. Phân tích chất lượng chặn dưới thu được.
3. Trình bày kỹ thuật làm chặt (tightening).
4. So sánh chi phí tính toán.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Nới lỏng LP**

**Bài toán nới lỏng:**
$$\min_x c^T x \quad \text{s.t.} \quad Ax \leq b, \quad 0 \leq x_i \leq 1, \quad i \in I$$

**Tính chất:**
- **Chặn dưới:** $$z_{LP} \leq z_{IP}$$.
- **Độ phức tạp:** giải được trong thời gian đa thức.
- **Độ chặt:** chặn dưới là chặt khi nghiệm tối ưu của bài toán LP có giá trị nguyên.

**Khoảng cách nguyên (integrality gap):** $$\frac{z_{IP}}{z_{LP}}$$ (với giá trị dương).

**Bước 2: Nới lỏng Lagrange**

**Đưa nhóm ràng buộc $$A_2 x \leq b_2$$ vào hàm mục tiêu:**
$$L_D(\lambda) = \min_x \{c^T x + \lambda^T(A_2 x - b_2) : A_1 x \leq b_1, \; x_i \in \{0,1\}\}$$

**Chặn dưới đối ngẫu:** $$\max_{\lambda \geq 0} L_D(\lambda)$$.

**Ưu điểm:**
- **Khả năng phân rã:** bài toán tách thành nhiều bài toán con độc lập nếu $$A_1$$ có cấu trúc đường chéo khối.
- **Chặn chặt hơn:** thường cho chặn dưới chặt hơn hoặc bằng nới lỏng LP.
- **Tối ưu hóa dưới gradient:** bài toán đối ngẫu có thể giải bằng phương pháp dưới gradient (subgradient).

**Bước 3: Nới lỏng SDP**

**Bài toán bậc hai tương ứng:** $$\min \sum_{ij} c_{ij} x_i x_j$$

**Dạng nới lỏng SDP:**
$$\min_{X} \sum_{ij} c_{ij} X_{ij}$$
$$\text{s.t.} \quad \text{các ràng buộc tuyến tính theo } X$$
$$\quad X_{ii} = x_i, \quad X \succeq 0$$

**Ràng buộc hạng 1:** ràng buộc phi lồi $$X = xx^T$$ được nới lỏng thành $$X \succeq 0$$ (hoặc $$\begin{bmatrix} 1 & x^T \\ x & X \end{bmatrix} \succeq 0$$).

**Ứng dụng tiêu biểu:**
- **Bài toán cắt cực đại (Max-Cut):** thuật toán Goemans–Williamson.
- **Bài toán gán bậc hai (QAP):** các phép nới lỏng SDP.

**Bước 4: Đặc trưng hóa bao lồi**

**Đa diện lồi nguyên:** $$P_I = \text{conv}\{x \in \{0,1\}^n : Ax \leq b\}$$.

**Nhận diện các mặt (facets):**
- **Bất đẳng thức hợp lệ (valid inequalities):** $$\alpha^T x \leq \beta$$ đúng với mọi $$x \in P_I$$.
- **Bất đẳng thức tạo mặt (facet-defining):** các bất đẳng thức hợp lệ chặt nhất mô tả biên của $$P_I$$.

**Phương pháp mặt phẳng cắt (cutting plane methods):**
1. Giải bài toán nới lỏng LP.
2. Nếu nghiệm còn chứa thành phần phân số, tìm một bất đẳng thức hợp lệ bị nghiệm này vi phạm.
3. Bổ sung lát cắt (cut) vào bài toán LP và giải lại.
4. Lặp lại cho đến khi thu được nghiệm nguyên.

**Ví dụ:**
- **Bài toán cái túi (Knapsack):** bất đẳng thức phủ (cover inequalities).
- **Bài toán người bán hàng (TSP):** ràng buộc loại bỏ chu trình con (subtour elimination constraints).

</details>

---

## 📝 **Bài tập 5: Tối ưu hóa bền vững (Robust optimization)**

**Đề bài:** Bài toán tối ưu hóa danh mục đầu tư dưới điều kiện bất định:
$$\min_x x^T \Sigma x \quad \text{s.t.} \quad \mu^T x \geq r, \quad \mathbf{1}^T x = 1, \quad x \geq 0$$

với tham số bất định $$(\mu, \Sigma)$$.

a) **Bất định dạng hộp (box uncertainty):** $$\mu_i \in [\underline{\mu}_i, \overline{\mu}_i]$$.
b) **Bất định dạng ellipsoid:** $$\mu \in \{\mu_0 + Pu : \lVert u \rVert_2 \leq 1\}$$.
c) **Mô hình nhân tố (factor model):** $$\mu = \beta f + \epsilon$$ với $$f$$ bất định.
d) **Bền vững theo phân phối (distributionally robust):** $$\mathbb{E}_P[\mu] = \mu_0$$, $$\text{Var}_P[\mu] \preceq \Sigma_0$$.

**Yêu cầu:**
1. Viết lại các bài toán dưới dạng bài toán tối ưu hóa lồi tất định.
2. Phân tích mức độ bảo thủ của từng mô hình.
3. So sánh độ phức tạp tính toán.
4. Nhận xét về cài đặt thực tế.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Bất định dạng hộp**

**Ràng buộc trường hợp xấu nhất:** $$\min_{\mu \in \mathcal{U}} \mu^T x \geq r$$

với $$\mathcal{U} = \{\mu : \underline{\mu}_i \leq \mu_i \leq \overline{\mu}_i\}$$.

**Phân tích trường hợp xấu nhất:**
$$\min_{\mu \in \mathcal{U}} \mu^T x = \sum_{i: x_i \geq 0} \underline{\mu}_i x_i + \sum_{i: x_i < 0} \overline{\mu}_i x_i$$

**Bài toán bền vững tương đương:**
$$\min_x x^T \Sigma x$$
$$\text{s.t.} \quad \sum_{i: x_i \geq 0} \underline{\mu}_i x_i + \sum_{i: x_i < 0} \overline{\mu}_i x_i \geq r$$
$$\quad \mathbf{1}^T x = 1, \quad x \geq 0$$
(với ràng buộc $$x \geq 0$$, điều kiện lợi suất rút gọn thành $$\underline{\mu}^T x \geq r$$).

**Bước 2: Bất định dạng ellipsoid**

**Tập bất định:** $$\mathcal{U} = \{\mu_0 + Pu : \lVert u \rVert_2 \leq 1\}$$.

**Ràng buộc trường hợp xấu nhất:**
$$\min_{\lVert u \rVert_2 \leq 1} (\mu_0 + Pu)^T x = \mu_0^T x - \lVert P^T x \rVert_2 \geq r$$

**Bài toán bền vững tương đương:**
$$\min_x x^T \Sigma x$$
$$\text{s.t.} \quad \mu_0^T x - \lVert P^T x \rVert_2 \geq r$$
$$\quad \mathbf{1}^T x = 1, \quad x \geq 0$$

**Phân loại:** Ràng buộc $$\mu_0^T x - \lVert P^T x \rVert_2 \geq r$$ là ràng buộc nón bậc hai, nên bài toán có thể đưa về dạng SOCP.

**Bước 3: Mô hình nhân tố**

**Mô hình:** $$\mu = \beta f + \epsilon$$ với $$f \in \mathcal{F}$$ và nhiễu $$\epsilon$$.

**Tập bất định:** $$\mathcal{U} = \{\beta f + \epsilon : f \in \mathcal{F}, \; \lVert \epsilon \rVert_2 \leq \sigma\}$$.

**Phân tích trường hợp xấu nhất:**
$$\min_{\mu \in \mathcal{U}} \mu^T x = \min_{f \in \mathcal{F}} (\beta f)^T x - \sigma \lVert x \rVert_2$$

**Trường hợp đa nhân tố:** $$\mu = \sum_{k=1}^K \beta_k f_k + \epsilon$$.

**Bước 4: Bền vững theo phân phối**

**Tập phân phối bất định (ambiguity set):** $$\mathcal{P} = \{P : \mathbb{E}_P[\mu] = \mu_0, \; \text{Cov}_P[\mu] \preceq \Sigma_0\}$$.

**Lưu ý:** Kỳ vọng không mang tính bất định vì $$\mathbb{E}_P[\mu^T x] = \mu_0^T x$$ với mọi $$P \in \mathcal{P}$$. Tính bền vững đến từ ràng buộc xác suất (chance constraint) $$\inf_{P \in \mathcal{P}} \mathbb{P}_P[\mu^T x \geq r] \geq 1 - \epsilon$$; theo bất đẳng thức Cantelli/Chebyshev một phía, ràng buộc này tương đương với:
$$\mu_0^T x - \kappa \sqrt{x^T \Sigma_0 x} \geq r, \qquad \kappa = \sqrt{\frac{1-\epsilon}{\epsilon}}$$

**Bài toán bền vững tương đương:**
$$\min_x x^T \Sigma x$$
$$\text{s.t.} \quad \mu_0^T x - \kappa \sqrt{x^T \Sigma_0 x} \geq r$$
$$\quad \mathbf{1}^T x = 1, \quad x \geq 0$$

**Liên hệ với dạng ellipsoid:** Biểu thức trên tương đương với bất định ellipsoid có $$P P^T = \kappa^2 \Sigma_0$$ (vì $$\lVert P^T x \rVert_2^2 = x^T P P^T x$$).

</details>

---

## 📝 **Bài tập 6: Tối ưu hóa đa mục tiêu**

**Đề bài:** Xét bài toán hai mục tiêu:
$$\min_x (f_1(x), f_2(x)) \quad \text{s.t.} \quad x \in \mathcal{X}$$

với $$f_1, f_2$$ là các hàm lồi và $$\mathcal{X}$$ là tập lồi.

a) **Tính tối ưu Pareto:** đặc trưng hóa các nghiệm tối ưu Pareto.
b) **Các phương pháp vô hướng hóa:** tổng có trọng số, ràng buộc $$\epsilon$$, và vô hướng hóa theo mức đạt được (achievement scalarization).
c) **Xây dựng biên Pareto:** liệt kê có hệ thống các điểm trên biên.
d) **Ứng dụng:** tối ưu hóa danh mục đầu tư và thiết kế kỹ thuật.

**Yêu cầu:**
1. Trình bày đặc trưng lý thuyết.
2. Trình bày các thuật toán tiếp cận.
3. Minh họa bằng ví dụ tính toán.
4. Nêu các lưu ý thực tế.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Đặc trưng hóa tính tối ưu Pareto**

**Định nghĩa:** $$x^* \in \mathcal{X}$$ là nghiệm tối ưu Pareto nếu không tồn tại $$x \in \mathcal{X}$$ sao cho:
- $$f_i(x) \leq f_i(x^*)$$ với mọi $$i$$, và
- $$f_j(x) < f_j(x^*)$$ với ít nhất một chỉ số $$j$$.

**Điều kiện cần (trong trường hợp lồi):** Nếu $$x^*$$ là nghiệm tối ưu Pareto, tồn tại $$\lambda \geq 0$$, $$\lambda \neq 0$$ sao cho $$x^*$$ là nghiệm của bài toán:
$$\min_x \sum_{i=1}^2 \lambda_i f_i(x) \quad \text{s.t.} \quad x \in \mathcal{X}$$

**Điều kiện đủ:** Nếu $$\lambda > 0$$ (các thành phần đều dương chặt) và $$x^*$$ giải bài toán tổng trọng số (hoặc $$\lambda \geq 0, \lambda \neq 0$$ và $$x^*$$ là nghiệm duy nhất), thì $$x^*$$ là nghiệm tối ưu Pareto.

**Bước 2: Các phương pháp vô hướng hóa**

**Phương pháp tổng có trọng số (weighted sum):**
$$\min_x \lambda_1 f_1(x) + \lambda_2 f_2(x) \quad \text{s.t.} \quad x \in \mathcal{X}$$

với $$\lambda_1, \lambda_2 \geq 0$$, $$\lambda_1 + \lambda_2 = 1$$.

**Hạn chế:** Không thể tìm được các điểm nằm trên phần không lồi của biên Pareto (nếu bài toán tổng quát không lồi).

**Phương pháp ràng buộc $$\epsilon$$ ($$\epsilon$$-constraint):**
$$\min_x f_1(x) \quad \text{s.t.} \quad f_2(x) \leq \epsilon, \quad x \in \mathcal{X}$$

**Ưu điểm:** Có thể tìm được toàn bộ biên Pareto kể cả khi biên không lồi.

**Vô hướng hóa theo mức đạt được (achievement scalarization):**
$$\min_{x,t} t \quad \text{s.t.} \quad f_i(x) - z_i^* \leq t, \quad x \in \mathcal{X}$$

với $$z^*$$ là điểm lý tưởng: $$z_i^* = \min_{x \in \mathcal{X}} f_i(x)$$.

**Bước 3: Tính toán biên Pareto**

**Thuật toán 1: Quét tổng có trọng số**
```
For λ₁ = 0 to 1 (step δ):
    λ₂ = 1 - λ₁
    Solve: min λ₁f₁(x) + λ₂f₂(x) s.t. x ∈ X
    Store solution if Pareto optimal
```

**Thuật toán 2: Quét ràng buộc $$\epsilon$$**
```
Compute range [ε_min, ε_max] for f₂
For ε = ε_min to ε_max (step δ):
    Solve: min f₁(x) s.t. f₂(x) ≤ ε, x ∈ X
    Store solution
```

**Thuật toán 3: Giao tuyến biên pháp tuyến (Normal Boundary Intersection)**
- Xây dựng bao lồi của các điểm cực tiểu riêng lẻ.
- Sinh các điểm phân bố đều trên bao lồi đó.
- Giải các bài toán tối ưu hóa có ràng buộc tương ứng để chiếu lên biên Pareto.

**Bước 4: Ví dụ danh mục đầu tư**

**Hai hàm mục tiêu:**
- $$f_1(x) = x^T \Sigma x$$ (rủi ro)
- $$f_2(x) = -\mu^T x$$ (âm lợi suất kỳ vọng)

**Ràng buộc:** $$\mathbf{1}^T x = 1$$, $$x \geq 0$$.

**Biên hiệu quả (efficient frontier):**
$$\min_x x^T \Sigma x \quad \text{s.t.} \quad \mu^T x \geq r, \quad \mathbf{1}^T x = 1, \quad x \geq 0$$

**Họ nghiệm theo tham số:** quét $$r \in [r_{\min}, r_{\max}]$$.

**Biên trung bình – phương sai:** có dạng nhánh hyperbol trong không gian $$(r, \sigma)$$.

</details>

---

## 📝 **Bài tập 7: Tối ưu hóa ngẫu nhiên (Stochastic optimization)**

**Đề bài:** Xét bài toán quy hoạch ngẫu nhiên hai giai đoạn:
$$\min_{x} c^T x + \mathbb{E}_\xi[Q(x, \xi)]$$
$$\text{s.t.} \quad Ax = b, \quad x \geq 0$$

trong đó $$Q(x, \xi) = \min_y \{q^T y : Wy = h - Tx, \; y \geq 0\}$$.

a) **Xấp xỉ trung bình mẫu (Sample Average Approximation - SAA).**
b) **Mô hình hóa theo kịch bản (scenario-based formulation).**
c) **Phân rã Benders (Benders decomposition).**
d) **Thước đo rủi ro:** CVaR và hướng tiếp cận bền vững.

**Yêu cầu:**
1. Xây dựng dạng tương đương tất định.
2. Trình bày thuật toán phân rã.
3. Nêu kết quả hội tụ thống kê.
4. Trình bày mở rộng có xét đến rủi ro.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Xấp xỉ trung bình mẫu (SAA)**

**Bài toán gốc:** $$\min_x \{c^T x + \mathbb{E}_\xi[Q(x, \xi)] : Ax = b, \; x \geq 0\}$$.

**Bài toán xấp xỉ SAA:** $$\min_x \left\{c^T x + \frac{1}{N}\sum_{i=1}^N Q(x, \xi^i) : Ax = b, \; x \geq 0\right\}$$

với $$\xi^1, \ldots, \xi^N$$ là các mẫu độc lập, cùng phân phối (i.i.d.).

**Tính hội tụ:** $$\hat{x}_N \to x^*$$ khi $$N \to \infty$$ (hội tụ hầu chắc chắn).

**Kích thước mẫu:** cần $$N = O(\epsilon^{-2})$$ để đạt nghiệm $$\epsilon$$-tối ưu.

**Bước 2: Mô hình hóa theo kịch bản**

**Bài toán tương đương tất định:**
$$\min_{x,y^1,\ldots,y^N} c^T x + \frac{1}{N}\sum_{i=1}^N q^T y^i$$
$$\text{s.t.} \quad Ax = b, \quad x \geq 0$$
$$\quad W y^i = h^i - T^i x, \quad y^i \geq 0, \quad i = 1,\ldots,N$$

**Quy mô bài toán LP:** kích thước tăng nhanh theo số kịch bản $$N$$ (số biến và số ràng buộc tỷ lệ với $$N$$).

**Cấu trúc khối:** Ma trận ràng buộc có cấu trúc khối góc, thuận lợi cho các thuật toán phân rã.

**Bước 3: Phân rã Benders**

**Bài toán chính (master problem):**
$$\min_{x,\theta} c^T x + \theta$$
$$\text{s.t.} \quad Ax = b, \quad x \geq 0$$
$$\quad \theta \geq \frac{1}{N}\sum_{i=1}^N (\pi^{i,k})^T(h^i - T^i x), \quad k = 1, 2, \ldots \quad \text{(lát cắt tối ưu, với } \pi^{i,k} \text{ là nghiệm đối ngẫu của bài toán con)}$$

**Các bài toán con (subproblems):** với mỗi kịch bản $$i$$,
$$\min_{y^i} q^T y^i \quad \text{s.t.} \quad W y^i = h^i - T^i x, \quad y^i \geq 0$$

**Quy trình thuật toán:**
1. Giải bài toán chính để nhận nghiệm $$x^k$$.
2. Giải các bài toán con theo từng kịch bản để thu được nghiệm đối ngẫu $$\pi^{i,k}$$.
3. Bổ sung các lát cắt Benders vào bài toán chính.
4. Lặp lại cho đến khi hội tụ.

**Bước 4: Thước đo rủi ro**

**Giá trị rủi ro có điều kiện (Conditional Value-at-Risk - CVaR):**
$$\text{CVaR}_\alpha[Z] = \mathbb{E}[Z \mid Z \geq \text{VaR}_\alpha[Z]]$$

**Biểu diễn dưới dạng bài toán tối ưu:**
$$\min_{x,\eta,s} c^T x + \eta + \frac{1}{(1-\alpha)N}\sum_{i=1}^N s_i$$
$$\text{s.t.} \quad Ax = b, \quad x \geq 0$$
$$\quad s_i \geq Q(x, \xi^i) - \eta, \quad s_i \geq 0$$

**Bài toán có ràng buộc rủi ro:**
$$\min_x c^T x \quad \text{s.t.} \quad \text{CVaR}_\alpha[Q(x, \xi)] \leq \gamma$$

**Hướng tiếp cận bền vững theo phân phối:** xét trường hợp xấu nhất trên tập phân phối $$\mathcal{P}$$:
$$\min_x c^T x + \max_{P \in \mathcal{P}} \mathbb{E}_P[Q(x, \xi)]$$

</details>

---

## 📝 **Bài tập 8: Tối ưu hóa nón (Conic optimization)**

**Đề bài:** Phân tích các lớp bài toán tối ưu hóa nón sau:

a) **Quy hoạch nón bậc hai (SOCP):**
$$\min_x c^T x \quad \text{s.t.} \quad \lVert A_i x + b_i \rVert_2 \leq c_i^T x + d_i$$

b) **Quy hoạch nửa xác định (SDP):**
$$\min_X \langle C, X \rangle \quad \text{s.t.} \quad \langle A_i, X \rangle = b_i, \quad X \succeq 0$$

c) **Quy hoạch nón mũ (exponential cone programming):**
$$\min_x c^T x \quad \text{s.t.} \quad (x_i, x_j, x_k) \in \mathcal{K}_{\exp}$$

**Yêu cầu:**
1. Trình bày dạng chuẩn của từng lớp bài toán.
2. Thiết lập bài toán đối ngẫu.
3. Nêu vai trò của thuật toán điểm trong.
4. Liệt kê các ứng dụng và ví dụ mô hình hóa.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Quy hoạch nón bậc hai (SOCP)**

**Dạng chuẩn:**
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b, \quad x \in \mathcal{K}$$

với $$\mathcal{K} = \mathcal{K}_1 \times \cdots \times \mathcal{K}_m$$ và $$\mathcal{K}_i = \{(t, u) : \lVert u \rVert_2 \leq t\}$$.

**Bài toán đối ngẫu:**
$$\max_y b^T y \quad \text{s.t.} \quad A^T y + s = c, \quad s \in \mathcal{K}$$

**Tính tự đối ngẫu:** $$\mathcal{K}_i^* = \mathcal{K}_i$$.

**Ứng dụng:**
- **Tối ưu hóa bền vững:** bất định dạng ellipsoid.
- **Tối ưu hóa danh mục đầu tư:** ràng buộc rủi ro và phương sai.
- **Thiết kế bộ lọc:** các ràng buộc đáp ứng tần số.

**Bước 2: Quy hoạch nửa xác định (SDP)**

**Dạng chuẩn:**
$$\min_X \langle C, X \rangle \quad \text{s.t.} \quad \langle A_i, X \rangle = b_i, \quad X \succeq 0$$

**Dạng vectơ hóa:** $$\min_x c^T x \text{ s.t. } Ax = b, \; x \in \mathcal{S}_+^n$$.

**Bài toán đối ngẫu:**
$$\max_y b^T y \quad \text{s.t.} \quad \sum_{i=1}^m y_i A_i + S = C, \quad S \succeq 0$$

**Đối ngẫu mạnh:** Đúng khi điều kiện Slater được thỏa mãn.

**Ứng dụng:**
- **Tối ưu hóa tổ hợp:** bài toán cắt cực đại (Max-Cut), tô màu đồ thị.
- **Lý thuyết điều khiển:** bất đẳng thức ma trận tuyến tính (LMI).
- **Học máy:** các phương pháp nhân (kernel methods).

**Bước 3: Nón mũ (Exponential cone)**

**Định nghĩa nón mũ:** $$\mathcal{K}_{\exp} = \{(x,y,z) : ye^{x/y} \leq z, \; y > 0\} \cup \{(x,0,z) : x \leq 0, \; z \geq 0\}$$.

**Nón đối ngẫu:** $$\mathcal{K}_{\exp}^* = \{(u,v,w) : u < 0, \; -ue^{v/u} \leq ew, \text{ hoặc } u = 0, \; v \geq 0, \; w \geq 0\}$$.

**Ứng dụng:**
- **Tối ưu hóa entropy:** $$\min \sum x_i \log x_i$$.
- **Quy hoạch hình học:** sau phép đổi biến logarit.
- **Entropy tương đối:** cực tiểu hóa phân kỳ KL.

**Ví dụ mô hình hóa:**

**Entropy:** $$x \log x \leq t \Leftrightarrow (-t, x, 1) \in \mathcal{K}_{\exp}$$ (vì $$x e^{-t/x} \leq 1 \Leftrightarrow t \geq x \log x$$).

**Log-sum-exp:** $$\log(\sum e^{x_i}) \leq t$$ tương đương với một hệ các ràng buộc nón mũ.

**Nón lũy thừa (power cone):** $$x_1^{p_1} \cdots x_k^{p_k} \geq |x_{k+1}|$$ là một loại nón riêng (không phải nón mũ); với số mũ hữu tỉ, có thể biểu diễn lại bằng các ràng buộc nón bậc hai.

</details>

---

## 📝 **Bài tập 9: Thuật toán xấp xỉ**

**Đề bài:** Thiết kế thuật toán xấp xỉ cho các bài toán không lồi sau:

a) **Nới lỏng SDP cho Max-Cut:** thuật toán Goemans–Williamson.
b) **Định vị cơ sở (Facility location):** làm tròn dựa trên LP.
c) **Phủ tập hợp (Set cover):** phân tích thuật toán tham lam.
d) **Bài toán cái túi (Knapsack):** lược đồ xấp xỉ thời gian đa thức đầy đủ (FPTAS) qua quy hoạch động.

**Yêu cầu:**
1. Xây dựng dạng nới lỏng.
2. Thiết kế lược đồ làm tròn (rounding).
3. Phân tích tỉ số xấp xỉ.
4. Nêu các đảm bảo hiệu năng.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Nới lỏng SDP cho bài toán Max-Cut**

**Bài toán gốc:** $$\max_{x \in \{-1,1\}^n} \frac{1}{2}\sum_{(i,j) \in E} w_{ij}(1 - x_i x_j)$$ (mỗi cạnh tính một lần; cạnh bị cắt cho $$1 - x_i x_j = 2$$).

**Dạng tương đương:** $$\min_{x \in \{-1,1\}^n} \sum_{(i,j) \in E} w_{ij} x_i x_j$$.

**Nới lỏng SDP:** đặt $$X = xx^T \Rightarrow X_{ij} = x_i x_j$$ và nới lỏng thành:
$$\max_X \frac{1}{2}\sum_{(i,j) \in E} w_{ij}(1 - X_{ij})$$
$$\text{s.t.} \quad X_{ii} = 1, \quad X \succeq 0$$

**Thuật toán Goemans–Williamson:**
1. Giải bài toán nới lỏng SDP để thu được nghiệm tối ưu $$X^*$$.
2. Phân tích Cholesky: $$X^* = V^T V$$.
3. Chọn siêu phẳng ngẫu nhiên: $$r \sim \mathcal{N}(0, I)$$.
4. Làm tròn: $$x_i = \text{sign}(r^T v_i)$$.

**Tỉ số xấp xỉ:** $$\alpha_{GW} = \min_{0 \leq \theta \leq \pi} \frac{2}{\pi} \cdot \frac{\theta}{1 - \cos \theta} \approx 0.878$$.

**Bước 2: Bài toán định vị cơ sở (Facility location)**

**Bài toán:** $$\min \sum_{i \in F} f_i y_i + \sum_{i \in F, j \in C} c_{ij} x_{ij}$$
$$\text{s.t.} \quad \sum_{i \in F} x_{ij} = 1, \quad x_{ij} \leq y_i, \quad x_{ij}, y_i \in \{0,1\}$$

**Nới lỏng LP:** $$x_{ij}, y_i \in [0,1]$$.

**Thuật toán làm tròn:**
1. Giải bài toán nới lỏng LP.
2. Gom cụm các khách hàng và trong mỗi cụm, mở một cơ sở được chọn với xác suất tỷ lệ với $$x_{ij}^*$$ (nếu chỉ mở từng cơ sở độc lập với xác suất $$y_i^*$$ thì có thể xảy ra trường hợp một số khách hàng không có cơ sở phục vụ).
3. Nối mỗi khách hàng $$j$$ với cơ sở đang mở gần nhất.

**Phân tích:** Làm tròn ngẫu nhiên theo cụm (Chudak–Shmoys) cho chi phí kỳ vọng $$\leq (1 + 2/e) \times$$ giá trị tối ưu LP $$\approx 1.736 \times$$ LP.

**Các đảm bảo tốt hơn:** Thuật toán tham lam khớp đối ngẫu của Jain–Mahdian–Saberi đạt tỉ số $$1.61$$; tỉ số tốt nhất từng biết là khoảng $$1.488$$ (Li, 2011).

**Bước 3: Thuật toán tham lam cho phủ tập hợp (Set cover)**

**Bài toán:** $$\min \sum_{S \in \mathcal{S}} x_S \quad \text{s.t.} \quad \sum_{S: e \in S} x_S \geq 1, \quad x_S \in \{0,1\}$$.

**Thuật toán tham lam:**
```
While uncovered elements exist:
    Pick set S maximizing |S ∩ (uncovered elements)| / cost(S)
    Add S to solution
```

**Phân tích:** Đạt tỉ số xấp xỉ $$H_n$$ với $$H_n = \sum_{i=1}^n \frac{1}{i} \approx \ln n$$.

**Kỹ thuật phân tích dựa trên LP:**
- Phương pháp khớp đối ngẫu (dual fitting).
- Thuật toán gốc – đối ngẫu (primal-dual).

**Bước 4: FPTAS cho bài toán cái túi (Knapsack)**

**Bài toán:** $$\max \sum_{i=1}^n v_i x_i \quad \text{s.t.} \quad \sum_{i=1}^n w_i x_i \leq W, \quad x_i \in \{0,1\}$$.

**Quy hoạch động chuẩn:** thời gian $$O(nW)$$ (giả đa thức).

**Hướng tiếp cận FPTAS:**
1. Co giãn giá trị: $$\tilde{v}_i = \lfloor v_i / K \rfloor$$ với $$K = \epsilon \cdot v_{\max} / n$$.
2. Chạy quy hoạch động trên bài toán đã co giãn với độ phức tạp $$O(n^3 / \epsilon)$$ (tổng giá trị sau co giãn $$\leq n^2/\epsilon$$).
3. Trả về nghiệm thu được.

**Đảm bảo xấp xỉ:** đạt ít nhất $$(1 - \epsilon)$$ lần giá trị tối ưu.

**Ý tưởng chính:** Phép làm tròn giá trị vừa giữ được độ gần tối ưu, vừa thu nhỏ đáng kể không gian trạng thái của quy hoạch động.

</details>

---

## 📝 **Bài tập 10: Ứng dụng trong học máy**

**Đề bài:** Phân tích các bài toán học máy sau dưới góc độ tối ưu hóa lồi:

a) **Hồi quy logistic:** $$\min_w \sum_{i=1}^n \log(1 + e^{-y_i w^T x_i}) + \lambda \lVert w \rVert_2^2$$

b) **Hồi quy vectơ hỗ trợ (SVR):** $$\min_{w,b} \frac{1}{2}\lVert w \rVert_2^2 + C\sum_{i=1}^n \max(0, |y_i - w^T x_i - b| - \epsilon)$$

c) **Hoàn thiện ma trận (Matrix completion):** $$\min_X \lVert X \rVert_* \quad \text{s.t.} \quad X_{ij} = M_{ij}, \; (i,j) \in \Omega$$

d) **Mã hóa thưa (Sparse coding):** $$\min_{D,\alpha} \frac{1}{2}\lVert Y - D\alpha \rVert_F^2 + \lambda \lVert \alpha \rVert_1$$

**Yêu cầu:**
1. Phân tích tính lồi.
2. Thiết lập điều kiện tối ưu.
3. Đề xuất các thuật toán giải.
4. Phân tích tác dụng của thành phần chính quy hóa.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Hồi quy logistic**

**Hàm mục tiêu:** $$f(w) = \sum_{i=1}^n \log(1 + e^{-y_i w^T x_i}) + \lambda \lVert w \rVert_2^2$$.

**Tính lồi:**
- Mỗi số hạng $$\log(1 + e^{-y_i w^T x_i})$$ là hàm lồi (dạng log-sum-exp hợp với hàm affine).
- Thành phần chính quy hóa $$\ell_2$$ là hàm lồi (lồi chặt nếu $$\lambda > 0$$).
- Tổng các hàm lồi là hàm lồi.

**Gradient:** $$\nabla f(w) = -\sum_{i=1}^n \frac{y_i x_i}{1 + e^{y_i w^T x_i}} + 2\lambda w$$.

**Ma trận Hessian:** $$\nabla^2 f(w) = \sum_{i=1}^n \frac{e^{y_i w^T x_i}}{(1 + e^{y_i w^T x_i})^2} x_i x_i^T + 2\lambda I \succ 0$$ (với $$\lambda > 0$$).

**Thuật toán giải:**
- **Phương pháp Newton:** hội tụ nhanh khi số chiều vừa phải.
- **BFGS / L-BFGS:** phương pháp tựa Newton.
- **SGD:** mở rộng tốt cho tập dữ liệu lớn.

**Bước 2: Hồi quy vectơ hỗ trợ (SVR)**

**Viết lại bằng biến phụ:** $$\min_{w,b,\xi,\xi^*} \frac{1}{2}\lVert w \rVert_2^2 + C\sum_{i=1}^n (\xi_i + \xi_i^*)$$
$$\text{s.t.} \quad y_i - w^T x_i - b \leq \epsilon + \xi_i$$
$$\quad w^T x_i + b - y_i \leq \epsilon + \xi_i^*$$
$$\quad \xi_i, \xi_i^* \geq 0$$

**Bài toán đối ngẫu:**
$$\max_{\alpha,\alpha^*} -\frac{1}{2}\sum_{i,j}(\alpha_i - \alpha_i^*)(\alpha_j - \alpha_j^*) x_i^T x_j - \epsilon \sum_i(\alpha_i + \alpha_i^*) + \sum_i y_i(\alpha_i - \alpha_i^*)$$
$$\text{s.t.} \quad \sum_i(\alpha_i - \alpha_i^*) = 0, \quad 0 \leq \alpha_i, \alpha_i^* \leq C$$

**Vectơ hỗ trợ:** các điểm $$x_i$$ có $$\alpha_i > 0$$ hoặc $$\alpha_i^* > 0$$.

**Bước 3: Hoàn thiện ma trận (Matrix completion)**

**Chuẩn hạt nhân (nuclear norm):** $$\lVert X \rVert_* = \sum_{i=1}^{\min(m,n)} \sigma_i(X)$$.

**Tính lồi:** Chuẩn hạt nhân là hàm lồi (tổng các giá trị kỳ dị).

**Biểu diễn dưới dạng SDP:**
$$\min_{X,U,V} \frac{1}{2}(\text{tr}(U) + \text{tr}(V))$$
$$\text{s.t.} \quad \begin{bmatrix} U & X \\ X^T & V \end{bmatrix} \succeq 0, \quad X_{ij} = M_{ij}, \; (i,j) \in \Omega$$

**Thuật toán giải:**
- **Hạ gradient cận kề (proximal gradient):** ngưỡng mềm (soft thresholding) trên các giá trị kỳ dị SVD.
- **ADMM:** phương pháp nhân tử theo hướng luân phiên.
- **Frank–Wolfe:** phương pháp gradient có điều kiện.

**Bước 4: Mã hóa thưa (Sparse coding)**

**Tính song lồi (bi-convex):** Lồi theo $$D$$ khi cố định $$\alpha$$, và lồi theo $$\alpha$$ khi cố định $$D$$ (không lồi đồng thời theo $$(D, \alpha)$$).

**Cập nhật từ điển:** $$\min_D \frac{1}{2}\lVert Y - D\alpha \rVert_F^2$$ (bài toán bình phương tối thiểu).

**Cập nhật mã thưa:** $$\min_\alpha \frac{1}{2}\lVert Y - D\alpha \rVert_F^2 + \lambda \lVert \alpha \rVert_1$$ (bài toán LASSO).

**Cực tiểu hóa luân phiên:**
1. **Bước mã hóa thưa:** giải LASSO cho từng cột của $$\alpha$$.
2. **Bước cập nhật từ điển:** giải bình phương tối thiểu kèm chuẩn hóa các cột của $$D$$.
3. Lặp lại cho đến khi hội tụ.

**Nghiệm LASSO bằng ngưỡng mềm:**
$$\alpha_j^{(k+1)} = \text{soft}(\alpha_j^{(k)} - \eta \nabla_j f, \; \eta \lambda)$$

với $$\text{soft}(x, \tau) = \text{sign}(x) \max(|x| - \tau, 0)$$.

</details>

---

## 💡 Mẹo thực hành

#### **Khi mô hình hóa bài toán tối ưu:**
- **Nhận diện cấu trúc:** xác định bài toán thuộc lớp LP, QP, SOCP, SDP hay GP.
- **Kiểm tra tính lồi:** kiểm tra đồng thời hàm mục tiêu và các ràng buộc.
- **Đưa về dạng chuẩn:** biến đổi để tận dụng hiệu quả các bộ giải chuyên dụng.

#### **Khi phân tích tính tối ưu:**
- **Điều kiện KKT:** xác định mối liên hệ giữa điều kiện cần và điều kiện đủ.
- **Điều kiện bù lỏng:** nhận diện các ràng buộc tích cực tại nghiệm.
- **Phân tích độ nhạy:** đánh giá giá bóng và tác động khi tham số nhiễu động.

#### **Khi thiết kế thuật toán:**
- **Khai thác cấu trúc:** tận dụng tính thưa, tính tách được và khả năng phân rã.
- **Xấp xỉ:** dùng nới lỏng và làm tròn khi bài toán chính xác khó giải.
- **Tính bền vững:** xử lý bất định và nhiễu dữ liệu một cách có hệ thống.

---

## 💡 **Tổng kết**

### **Dạng chuẩn của bài toán tối ưu hóa lồi:**

$$
\begin{align}
\min_{x} \quad & f_0(x) \\
\text{s.t.} \quad & f_i(x) \leq 0, \quad i = 1, \ldots, m \\
& h_i(x) = 0, \quad i = 1, \ldots, p
\end{align}
$$

với $$f_0, \ldots, f_m$$ là các hàm lồi và $$h_i$$ là các hàm affine.

### **Điều kiện tối ưu:**

| Trường hợp | Công thức / Điều kiện | Khi nào đủ cho tối ưu toàn cục |
|------------|-----------------------|-------------------------------|
| **Không ràng buộc** | $$\nabla f(x^*) = 0$$ | $$f$$ lồi và khả vi |
| **Ràng buộc đẳng thức** | $$\nabla f(x^*) + \sum \nu_i^* \nabla h_i(x^*) = 0$$, $$h_i(x^*)=0$$ | $$f$$ lồi khả vi, $$h_i$$ affine |
| **KKT (tổng quát)** | Điều kiện dừng, khả thi gốc/đối ngẫu, bù lỏng | Bài toán lồi khả vi (điều kiện Slater đảm bảo KKT là cần) |
| **Tính chất lồi** | Cực tiểu địa phương = Cực tiểu toàn cục | Bài toán lồi |

### **Đối ngẫu:**

| Khái niệm | Định nghĩa | Ý nghĩa |
|-----------|------------|---------|
| **Hàm Lagrange** | $$L(x, \lambda, \nu) = f_0(x) + \sum \lambda_i f_i(x) + \sum \nu_i h_i(x)$$ | Hàm mục tiêu mở rộng theo ràng buộc |
| **Hàm đối ngẫu** | $$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$ | Chặn dưới của giá trị tối ưu gốc |
| **Bài toán đối ngẫu** | $$\max g(\lambda, \nu)$$ s.t. $$\lambda \geq 0$$ | Tìm chặn dưới tốt nhất |
| **Đối ngẫu yếu** | $$d^* \leq p^*$$ | Luôn đúng với mọi bài toán |
| **Đối ngẫu mạnh** | $$d^* = p^*$$ | Điều kiện Slater $$\Rightarrow$$ khe đối ngẫu bằng 0 |
| **Bù lỏng** | $$\lambda_i^* f_i(x^*) = 0$$ | Liên hệ giữa nhân tử và ràng buộc tích cực |

### **Tối ưu hóa tựa lồi (Quasiconvex Optimization):**

- **Định nghĩa:** $$f$$ là hàm tựa lồi nếu mọi tập mức dưới $$\{x : f(x) \leq \alpha\}$$ đều là tập lồi.
- **Không bảo toàn qua phép cộng:** tổng $$f_1 + f_2$$ của hai hàm tựa lồi nói chung không nhất thiết tựa lồi.
- **Quy hoạch phân thức:** $$\min \frac{f(x)}{g(x)}$$ có thể giải bằng phương pháp chia đôi (bisection) qua một chuỗi bài toán khả thi lồi.

### **Tối ưu hóa vectơ:**

- **Tối ưu Pareto:** không tồn tại $$y$$ khả thi sao cho $$f(y) \preceq_{K} f(x)$$ và $$f(y) \neq f(x)$$.
- **Vô hướng hóa:** $$\min \lambda^T f(x)$$ với $$\lambda \succ_{K^*} 0$$.
- **Phương pháp ràng buộc $$\epsilon$$:** cố định ngưỡng cho $$m-1$$ mục tiêu và tối ưu mục tiêu còn lại.

### **Tối ưu hóa ngẫu nhiên và bền vững:**

| Phương pháp | Công thức | Đặc trưng đánh đổi |
|-------------|-----------|--------------------|
| **Giá trị kỳ vọng** | $$\min \mathbb{E}[f(x, \xi)]$$ | Tối ưu hiệu năng trung bình |
| **Trường hợp xấu nhất** | $$\min \max_{\xi \in \mathcal{U}} f(x, \xi)$$ | Bảo thủ, an toàn trước bất định |
| **Ràng buộc xác suất** | $$\mathbb{P}[f(x, \xi) \leq 0] \geq 1 - \epsilon$$ | Đảm bảo ở mức tin cậy xác suất |
| **Trung bình mẫu (SAA)** | $$\min \frac{1}{N}\sum f(x, \xi_i)$$ | Xấp xỉ khả giải từ dữ liệu mẫu |

### **Các kỹ thuật nới lỏng:**

- **Nới lỏng LP:** $$x \in \{0,1\}^n \to x \in [0,1]^n$$.
- **Nới lỏng SDP:** $$xx^T \to X \succeq 0$$, $$X_{ii} = 1$$.
- **Nới lỏng Lagrange:** đưa các ràng buộc phức tạp vào hàm mục tiêu.
- **Làm tròn ngẫu nhiên:** chuyển nghiệm phân số hoặc nghiệm ma trận về nghiệm nguyên.

---

## 📚 Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 4: Convex Optimization Problems

2. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming*. Athena Scientific.

4. **Shapiro, A., Dentcheva, D., & Ruszczyński, A.** (2009). *Lectures on Stochastic Programming*. SIAM.

5. **Williamson, D. P., & Shmoys, D. B.** (2011). *The Design of Approximation Algorithms*. Cambridge University Press.

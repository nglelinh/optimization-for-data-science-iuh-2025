---
layout: post
title: 01-07 Bài Tập Thực Hành - Giới Thiệu Tối Ưu Hóa
chapter: '1'
order: 8
owner: GitHub Copilot
lang: vi
categories:
- chapter01
lesson_type: required
redirect_from:
  - /contents/vi/chapter01/01_06_Practical_Exercises_Introduction/
---

# Bài tập thực hành - Giới thiệu tối ưu hóa

## 📝 **Bài tập 1: Phân loại bài toán tối ưu hóa cơ bản**

**Đề bài:** (Bài 1.1 từ Boyd & Vandenberghe)
Phân loại các bài toán sau đây vào các lớp: LP (quy hoạch tuyến tính), QP (quy hoạch bậc hai), QCQP (quy hoạch bậc hai có ràng buộc bậc hai), SOCP (quy hoạch nón bậc hai), SDP (quy hoạch nửa xác định) hoặc GP (quy hoạch hình học):

a) $$\min_{x \in \mathbb{R}^n} c^T x \quad \text{s.t.} \quad Ax \leq b$$

b) $$\min_{x \in \mathbb{R}^n} x^T P x + q^T x \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

c) $$\min_{x \in \mathbb{R}^n} \lVert Ax - b \rVert_2 \quad \text{s.t.} \quad \lVert x \rVert_2 \leq 1$$

**Yêu cầu:**
1. Xác định lớp bài toán cho mỗi trường hợp.
2. Giải thích lý do phân loại.
3. Nêu điều kiện để bài toán là bài toán lồi.
4. Đề xuất phương pháp giải phù hợp.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Phân loại**

**a) Quy hoạch tuyến tính (LP)**
- Hàm mục tiêu: tuyến tính ($$c^T x$$).
- Ràng buộc: bất đẳng thức tuyến tính ($$Ax \leq b$$).
- Đây là dạng chuẩn của bài toán LP.

**b) Quy hoạch bậc hai (QP)**
- Hàm mục tiêu: hàm bậc hai ($$x^T P x + q^T x$$).
- Ràng buộc: tuyến tính ($$Ax = b, x \geq 0$$).
- Là bài toán QP lồi khi $$P \succeq 0$$.

**c) Quy hoạch nón bậc hai (SOCP)**
- Hàm mục tiêu: chuẩn Euclid ($$\lVert Ax - b \rVert_2$$).
- Ràng buộc: ràng buộc chuẩn Euclid ($$\lVert x \rVert_2 \leq 1$$).
- Có thể đưa trực tiếp về dạng chuẩn SOCP (bằng cách thêm biến phụ $$t$$ với ràng buộc $$\lVert Ax - b \rVert_2 \leq t$$).

**Bước 2: Điều kiện tính lồi**
- **a)** Luôn lồi (hàm mục tiêu và các ràng buộc đều tuyến tính/affine).
- **b)** Lồi khi $$P \succeq 0$$ (ma trận nửa xác định dương).
- **c)** Luôn lồi (chuẩn Euclid là hàm lồi và hình cầu chuẩn là tập lồi).

**Bước 3: Phương pháp giải**
- **a)** Thuật toán đơn hình (Simplex), phương pháp điểm trong.
- **b)** Phương pháp tập hoạt động (Active-set), phương pháp điểm trong.
- **c)** Phương pháp điểm trong cho SOCP.

</details>

---

## 📝 **Bài tập 2: Bình phương tối thiểu và các biến thể**

**Đề bài:** (Bài 1.2 từ Boyd & Vandenberghe)
Xét các bài toán bình phương tối thiểu sau:

a) **Bình phương tối thiểu thông thường (OLS):** $$\min_x \lVert Ax - b \rVert_2^2$$

b) **Bình phương tối thiểu có trọng số (WLS):** $$\min_x (Ax - b)^T W (Ax - b)$$ với $$W \succ 0$$

c) **Bình phương tối thiểu có điều chuẩn (Ridge):** $$\min_x \lVert Ax - b \rVert_2^2 + \lambda \lVert x \rVert_2^2$$

d) **Bình phương tối thiểu bền vững (Robust LS):** $$\min_x \sum_{i=1}^m \phi((Ax - b)_i)$$ với $$\phi(u) = \begin{cases} u^2 & |u| \leq M \\ 2M|u| - M^2 & |u| > M \end{cases}$$

**Yêu cầu:**
1. Tìm nghiệm giải tích (dạng đóng) cho các trường hợp a, b, c.
2. Chứng minh tính lồi của cả bốn bài toán.
3. Phân tích ý nghĩa hình học của thành phần điều chuẩn.
4. So sánh độ bền vững (robustness) trước điểm ngoại lai của các phương pháp.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Nghiệm giải tích**

**a) Bình phương tối thiểu thông thường:**
$$x^* = (A^T A)^{-1} A^T b$$ (khi $$A^T A$$ khả nghịch).

**b) Bình phương tối thiểu có trọng số:**
$$x^* = (A^T W A)^{-1} A^T W b$$ (khi $$A^T W A$$ khả nghịch).

**c) Bình phương tối thiểu có điều chuẩn (Hồi quy Ridge):**
$$x^* = (A^T A + \lambda I)^{-1} A^T b$$ (luôn khả nghịch với mọi $$\lambda > 0$$).

**d) Bình phương tối thiểu bền vững:**
Không có công thức nghiệm dạng đóng, cần giải bằng các phương pháp số lặp.

**Bước 2: Chứng minh tính lồi**

- **a–c)** Đều là hàm bậc hai có ma trận Hessian nửa xác định dương: $$2A^TA \succeq 0$$, $$2A^TWA \succeq 0$$ và $$2(A^TA + \lambda I) \succ 0$$ (với $$\lambda > 0$$).
- **d)** Hàm phạt Huber $$\phi(u)$$ là hàm lồi (hàm bậc hai từng khúc có đạo hàm liên tục và không giảm), nên tổng hợp tuyến tính của chúng cũng là hàm lồi.

**Bước 3: Ý nghĩa hình học của điều chuẩn**
- **Điều chuẩn $$L_2$$:** kéo nghiệm về gần gốc tọa độ, hạn chế quá khớp (overfitting).
- **Tham số $$\lambda$$:** kiểm soát sự đánh đổi giữa độ chệch (bias) và phương sai (variance).
- Về mặt thống kê Bayes, bài toán tương đương ước lượng hậu nghiệm cực đại (MAP) với phân phối tiên nghiệm chuẩn $$x \sim \mathcal{N}(0, \sigma^2/\lambda I)$$.

**Bước 4: So sánh độ bền vững**
- **OLS:** nhạy cảm mạnh với điểm ngoại lai do sai số bị bình phương.
- **WLS:** có thể giảm ảnh hưởng của điểm ngoại lai nếu chọn ma trận trọng số $$W$$ phù hợp.
- **Ridge:** giảm quá khớp và cải thiện khả năng tổng quát hóa, nhưng vẫn dùng mất mát bình phương.
- **Robust LS:** hàm mất mát Huber tăng tuyến tính khi $$|u| > M$$ nên giảm đáng kể độ nhạy với ngoại lai.

</details>

---

## 📝 **Bài tập 3: Quy hoạch tuyến tính ở dạng chuẩn**

**Đề bài:** (Bài 1.3 từ Boyd & Vandenberghe)
Đưa các bài toán sau về dạng chuẩn của quy hoạch tuyến tính (LP):

a) $$\min_{x,y} 2x + 3y \quad \text{s.t.} \quad x + 2y \geq 5, \quad x - y = 2, \quad x \geq 0, \quad y \text{ free}$$

b) $$\max_x c^T x \quad \text{s.t.} \quad Ax \leq b, \quad x \geq 0$$

c) $$\min_x \lVert c^T x - d \rVert_\infty \quad \text{s.t.} \quad Ax \leq b$$

**Yêu cầu:**
1. Biến đổi về dạng $$\min c^T z \text{ s.t. } Az = b, z \geq 0$$.
2. Xác định rõ ma trận $$A$$ và các vector $$b, c$$ mới.
3. Giải thích các phép biến đổi đã sử dụng.
4. Kiểm tra tính tương đương giữa bài toán gốc và bài toán sau biến đổi.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Biến đổi bài toán a)**

- **Xử lý biến tự do:** đặt $$y = y^+ - y^-$$ với $$y^+, y^- \geq 0$$.
- **Xử lý bất đẳng thức:** thêm biến bù (surplus) $$s \geq 0$$ để chuyển $$x + 2y \geq 5 \Rightarrow x + 2y - s = 5$$.

**Dạng chuẩn:**
$$\min_{x,y^+,y^-,s} 2x + 3y^+ - 3y^- \quad \text{s.t.} \quad \begin{bmatrix} 1 & 2 & -2 & -1 \\ 1 & -1 & 1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y^+ \\ y^- \\ s \end{bmatrix} = \begin{bmatrix} 5 \\ 2 \end{bmatrix}$$

với $$x, y^+, y^-, s \geq 0$$.

**Bước 2: Biến đổi bài toán b)**

- **Chuyển cực đại thành cực tiểu:** $$\max c^T x = -\min (-c^T x)$$.
- **Chuyển bất đẳng thức thành đẳng thức:** thêm vector biến bù (slack) $$s \geq 0$$ sao cho $$Ax \leq b \Rightarrow Ax + s = b$$.

**Dạng chuẩn:**
$$\min_{x,s} (-c^T x + 0^T s) \quad \text{s.t.} \quad [A \quad I] \begin{bmatrix} x \\ s \end{bmatrix} = b, \quad x,s \geq 0$$

**Bước 3: Biến đổi bài toán c)**

- **Loại bỏ chuẩn $$\ell_\infty$$:** đưa vào biến phụ $$t$$ sao cho $$\min t \text{ s.t. } -t \leq c^T x - d \leq t$$.

**Dạng chuẩn:**
$$\min_{x,t,s_1,s_2,s_3} t \quad \text{s.t.} \quad \begin{bmatrix} A & 0 & I & 0 & 0 \\ c^T & -1 & 0 & 1 & 0 \\ -c^T & -1 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ t \\ s_1 \\ s_2 \\ s_3 \end{bmatrix} = \begin{bmatrix} b \\ d \\ -d \end{bmatrix}, \quad t, s_1, s_2, s_3 \geq 0$$

Hai hàng cuối biểu diễn lần lượt $$c^T x - d \leq t$$ và $$-(c^T x - d) \leq t$$, mỗi hàng dùng một biến bù riêng. Do $$x$$ là biến tự do, ta thay tiếp $$x = x^+ - x^-$$ với $$x^+, x^- \geq 0$$ để đảm bảo mọi biến đều không âm.

</details>

---

## 📝 **Bài tập 4: Ứng dụng quy hoạch bậc hai**

**Đề bài:** (Bài 1.4 từ Boyd & Vandenberghe)
Xét bài toán tối ưu hóa danh mục đầu tư:

$$\min_x \frac{1}{2} x^T \Sigma x \quad \text{s.t.} \quad \mu^T x \geq r, \quad \mathbf{1}^T x = 1, \quad x \geq 0$$

trong đó $$\Sigma \succ 0$$ là ma trận hiệp phương sai, $$\mu$$ là vector lợi suất kỳ vọng và $$r$$ là mức lợi suất mục tiêu.

**Yêu cầu:**
1. Chứng minh đây là bài toán QP lồi.
2. Viết hệ điều kiện KKT.
3. Phân tích trường hợp bỏ ràng buộc $$x \geq 0$$.
4. Tìm đường biên hiệu quả (efficient frontier).
5. Cài đặt lời giải số.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Chứng minh tính lồi**
- Hàm mục tiêu: $$f(x) = \frac{1}{2} x^T \Sigma x$$ có Hessian $$\nabla^2 f = \Sigma \succ 0$$ nên là hàm lồi chặt.
- Các ràng buộc đều là bất đẳng thức và đẳng thức tuyến tính.
- $$\Rightarrow$$ Đây là bài toán QP lồi.

**Bước 2: Điều kiện KKT**
Hàm Lagrange (dùng $$\eta$$ làm nhân tử cho $$x \geq 0$$ để tránh trùng ký hiệu với $$\mu$$):
$$L(x,\lambda,\nu,\eta) = \frac{1}{2} x^T \Sigma x - \lambda(\mu^T x - r) + \nu(\mathbf{1}^T x - 1) - \eta^T x$$

Hệ điều kiện KKT:
- Điều kiện dừng (Stationarity): $$\Sigma x - \lambda \mu + \nu \mathbf{1} - \eta = 0$$.
- Tính khả thi gốc (Primal feasibility): $$\mu^T x \geq r, \mathbf{1}^T x = 1, x \geq 0$$.
- Tính khả thi đối ngẫu (Dual feasibility): $$\lambda \geq 0, \eta \geq 0$$.
- Điều kiện bù lỏng (Complementary slackness): $$\lambda(\mu^T x - r) = 0, \eta_i x_i = 0$$.

**Bước 3: Trường hợp bỏ ràng buộc $$x \geq 0$$ (giả sử ràng buộc lợi suất chặt, $$\mu^T x = r$$)**
Từ điều kiện dừng ta có:
$$x^* = \Sigma^{-1}(\lambda^* \mu - \nu^* \mathbf{1})$$

Thay vào hai ràng buộc đẳng thức:
- $$\mathbf{1}^T x^* = 1 \Rightarrow \mathbf{1}^T \Sigma^{-1}(\lambda^* \mu - \nu^* \mathbf{1}) = 1$$
- $$\mu^T x^* = r \Rightarrow \mu^T \Sigma^{-1}(\lambda^* \mu - \nu^* \mathbf{1}) = r$$

Thu được hệ phương trình tuyến tính 2 ẩn:
$$\begin{bmatrix} A & B \\ B & C \end{bmatrix} \begin{bmatrix} \lambda^* \\ -\nu^* \end{bmatrix} = \begin{bmatrix} r \\ 1 \end{bmatrix}$$

với $$A = \mu^T \Sigma^{-1} \mu, B = \mu^T \Sigma^{-1} \mathbf{1}, C = \mathbf{1}^T \Sigma^{-1} \mathbf{1}$$.

**Bước 4: Đường biên hiệu quả**
Phương sai rủi ro nhỏ nhất theo mức lợi suất mục tiêu $$r$$ là:
$$\sigma^2(r) = x^{*T} \Sigma x^* = \frac{Cr^2 - 2Br + A}{AC - B^2}$$

Đây là một nhánh hyperbol trong mặt phẳng $$(r, \sigma)$$.

</details>

---

## 📝 **Bài tập 5: Quy hoạch hình học (Geometric Programming)**

**Đề bài:** (Bài 1.5 từ Boyd & Vandenberghe)
Xét bài toán thiết kế mạch điện:

$$\min_{x,y,z} \frac{1}{xyz} \quad \text{s.t.} \quad \frac{x}{y} + \frac{y}{z} \leq 1, \quad z \leq 1, \quad x,y,z > 0$$

*(Ràng buộc $$z \leq 1$$ là cần thiết: nếu bỏ ràng buộc này, khi nhân $$(x, y, z)$$ với hệ số $$s > 0$$ thì ràng buộc thứ nhất không đổi nhưng $$\frac{1}{xyz} \to 0$$ khi $$s \to \infty$$, khiến bài toán không có nghiệm tối ưu.)*

**Yêu cầu:**
1. Chứng minh đây là một bài toán quy hoạch hình học (GP).
2. Chuyển bài toán về dạng lồi bằng phép đổi biến logarit.
3. Giải bài toán lồi thu được.
4. Diễn giải nghiệm trong bối cảnh thiết kế mạch.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Kiểm tra dạng quy hoạch hình học**
- Hàm mục tiêu: $$f_0(x,y,z) = x^{-1} y^{-1} z^{-1}$$ (đơn thức — monomial).
- Các ràng buộc: $$g_1(x,y,z) = x^1 y^{-1} z^0 + x^0 y^1 z^{-1}$$ (đa thức dương — posynomial) và $$g_2(x,y,z) = z$$ (đơn thức).
- Miền biến: $$x,y,z > 0$$.

$$\Rightarrow$$ Đây là bài toán GP ở dạng chuẩn.

**Bước 2: Phép đổi biến logarit**
Đặt $$u = \log x, v = \log y, w = \log z$$:

$$\min_{u,v,w} -u - v - w \quad \text{s.t.} \quad \log(e^{u-v} + e^{v-w}) \leq 0, \quad w \leq 0$$

Tương đương:
$$\min_{u,v,w} -u - v - w \quad \text{s.t.} \quad e^{u-v} + e^{v-w} \leq 1, \quad w \leq 0$$

**Bước 3: Xác nhận tính lồi**
Hàm mục tiêu là tuyến tính, $$\log(e^{u-v} + e^{v-w})$$ là hàm log-sum-exp của các hàm affine (nên lồi), còn $$w \leq 0$$ là ràng buộc tuyến tính.

Vậy bài toán sau đổi biến là bài toán tối ưu hóa lồi.

**Bước 4: Nghiệm tối ưu**
Có thể giải tổng quát bằng phương pháp điểm trong hoặc các bộ giải GP chuyên dụng. Ở bài toán nhỏ này ta giải trực tiếp được:
- Nghiệm trong biến gốc liên hệ qua $$x^* = e^{u^*}, y^* = e^{v^*}, z^* = e^{w^*}$$.
- Cả hai ràng buộc đều chặt tại nghiệm tối ưu. Với $$z = 1$$, bài toán trở thành $$\max xy$$ s.t. $$x \leq y(1 - y)$$, tức $$\max_y y^2(1-y)$$, đạt cực đại tại $$y = 2/3$$.
- Nghiệm tối ưu: $$x^* = 2/9$$, $$y^* = 2/3$$, $$z^* = 1$$; kiểm tra $$\frac{x^*}{y^*} + \frac{y^*}{z^*} = \frac{1}{3} + \frac{2}{3} = 1$$ ✓; giá trị tối ưu $$\frac{1}{x^*y^*z^*} = \frac{27}{4}$$.

</details>

---

## 📝 **Bài tập 6: Cơ bản về quy hoạch nửa xác định (SDP)**

**Đề bài:** (Bài 1.6 từ Boyd & Vandenberghe)
Xét bài toán:

$$\min_X \text{tr}(CX) \quad \text{s.t.} \quad \text{tr}(A_i X) = b_i, \quad i = 1,\ldots,m, \quad X \succeq 0$$

**Yêu cầu:**
1. Chứng minh đây là bài toán tối ưu hóa lồi.
2. Xây dựng bài toán đối ngẫu.
3. Phân tích điều kiện đối ngẫu mạnh (strong duality).
4. Nêu ví dụ cụ thể: nới lỏng SDP cho bài toán cắt cực đại (Maximum Cut).

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Chứng minh tính lồi**
- Hàm mục tiêu: $$\text{tr}(CX)$$ là hàm tuyến tính theo ma trận $$X$$.
- Các ràng buộc đẳng thức: $$\text{tr}(A_i X) = b_i$$ là các ràng buộc tuyến tính.
- Ràng buộc nón: $$X \succeq 0$$ xác định nón các ma trận đối xứng nửa xác định dương, vốn là một tập lồi.

$$\Rightarrow$$ Đây là bài toán quy hoạch nửa xác định (SDP) lồi.

**Bước 2: Bài toán đối ngẫu**
Hàm Lagrange: $$L(X,y,Z) = \text{tr}(CX) + \sum_{i=1}^m y_i (b_i - \text{tr}(A_i X)) - \text{tr}(ZX)$$

Hàm đối ngẫu: $$g(y,Z) = \inf_X L(X,y,Z)$$

Để hàm đối ngẫu hữu hạn, hệ số của $$X$$ phải bằng không: $$C - \sum_{i=1}^m y_i A_i - Z = 0$$.

**Bài toán đối ngẫu:**
$$\max_{y,Z} \sum_{i=1}^m b_i y_i \quad \text{s.t.} \quad \sum_{i=1}^m y_i A_i + Z = C, \quad Z \succeq 0$$

**Bước 3: Đối ngẫu mạnh**
Đối ngẫu mạnh xảy ra khi điều kiện Slater được thỏa mãn (bài toán gốc khả thi chặt):
$$\exists X \succ 0 \text{ s.t. } \text{tr}(A_i X) = b_i, \forall i$$

**Bước 4: Ví dụ nới lỏng cho bài toán cắt cực đại (Max-Cut)**
Cho đồ thị $$G = (V,E)$$ với trọng số cạnh $$w_{ij}$$:

$$\max_x \sum_{(i,j) \in E} w_{ij} \frac{1 - x_i x_j}{2} \quad \text{s.t.} \quad x_i \in \{-1,1\}$$

**Nới lỏng SDP:**
$$\max_X \sum_{(i,j) \in E} w_{ij} \frac{1 - X_{ij}}{2} \quad \text{s.t.} \quad X_{ii} = 1, \quad X \succeq 0$$

</details>

---

## 📝 **Bài tập 7: Giới thiệu tối ưu hóa bền vững (Robust Optimization)**

**Đề bài:** (Bài 1.7 từ Boyd & Vandenberghe)
Xét bài toán quy hoạch tuyến tính bền vững:

$$\min_x c^T x \quad \text{s.t.} \quad a_i^T x \leq b_i \quad \forall a_i \in \mathcal{U}_i, \quad i = 1,\ldots,m$$

với hai dạng tập bất định (uncertainty sets):
a) Dạng hình hộp (Box): $$\mathcal{U}_i = \{a_i^{nom} + u : \lVert u \rVert_\infty \leq \rho_i\}$$
b) Dạng ellipsoid: $$\mathcal{U}_i = \{a_i^{nom} + P_i u : \lVert u \rVert_2 \leq 1\}$$

**Yêu cầu:**
1. Biến đổi thành các bài toán tối ưu hóa lồi tất định tương đương.
2. So sánh độ phức tạp tính toán.
3. Phân tích mức độ bảo thủ của từng dạng tập bất định.
4. Cài đặt và so sánh nghiệm thu được.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Tập bất định dạng hình hộp**
$$\max_{a_i \in \mathcal{U}_i} a_i^T x = (a_i^{nom})^T x + \rho_i \lVert x \rVert_1$$

**Bài toán tất định tương đương:**
$$\min_x c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \rho_i \lVert x \rVert_1 \leq b_i$$

**Đưa về dạng LP:**
$$\min_{x,t_i} c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \rho_i \sum_j t_{ij} \leq b_i, \quad -t_{ij} \leq x_j \leq t_{ij}$$

**Bước 2: Tập bất định dạng ellipsoid**
$$\max_{a_i \in \mathcal{U}_i} a_i^T x = (a_i^{nom})^T x + \lVert P_i^T x \rVert_2$$

**Bài toán tất định tương đương:**
$$\min_x c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \lVert P_i^T x \rVert_2 \leq b_i$$

Đây là một bài toán quy hoạch nón bậc hai (SOCP).

**Bước 3: So sánh độ phức tạp**
- **Hình hộp:** bài toán LP với $$O(mn)$$ biến và ràng buộc (khi đặt riêng $$t_{ij}$$).
- **Ellipsoid:** bài toán SOCP với $$n + m$$ biến (hoặc $$n$$ biến trực tiếp) và $$m$$ ràng buộc nón bậc hai.
- **Danh nghĩa (Nominal):** bài toán LP với $$n$$ biến và $$m$$ ràng buộc.

**Bước 4: Phân tích mức độ bảo thủ**
- **Hình hộp:** bảo thủ nhất (xét trường hợp xấu nhất đồng thời trên mọi tọa độ).
- **Ellipsoid:** bảo thủ ở mức trung bình (giới hạn tổng độ lệch theo chuẩn Euclid).
- **Danh nghĩa:** ít bảo thủ nhất (bỏ qua tính bất định).

"Chi phí của tính bền vững" (price of robustness) thường được đo bằng: $$\frac{\text{Giá trị tối ưu bền vững}}{\text{Giá trị tối ưu danh nghĩa}} - 1$$.

</details>

---

## 📝 **Bài tập 8: Kiểm tra tính lồi**

**Đề bài:** (Bài 1.8 từ Boyd & Vandenberghe)
Xác định tính lồi của các hàm số sau:

a) $$f(x) = x \log x$$ trên $$\mathbb{R}_{++}$$
b) $$f(x) = -\log(\det X)$$ trên $$\mathbb{S}_{++}^n$$
c) $$f(x) = \lVert x \rVert_p$$ với $$p \geq 1$$
d) $$f(X) = \lambda_{\max}(X)$$ trên $$\mathbb{S}^n$$

**Yêu cầu:**
1. Chứng minh hoặc phản chứng tính lồi của từng hàm.
2. Áp dụng điều kiện bậc hai khi phù hợp.
3. Kiểm chứng bằng định nghĩa hoặc các quy tắc bảo toàn tính lồi.
4. Xác định miền xác định lồi của mỗi hàm.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: $$f(x) = x \log x$$**
- **Miền xác định:** $$\mathbb{R}_{++}$$ (tập lồi).
- **Đạo hàm bậc hai:** $$f''(x) = \frac{1}{x} > 0$$ với mọi $$x > 0$$.
- $$\Rightarrow$$ Hàm lồi chặt trên $$\mathbb{R}_{++}$$.

**Bước 2: $$f(X) = -\log(\det X)$$**
- **Miền xác định:** $$\mathbb{S}_{++}^n$$ (nón ma trận đối xứng xác định dương, là tập lồi).
- **Hessian:** có thể chứng minh $$\nabla^2 f \succ 0$$.
- Biểu diễn theo giá trị riêng: $$-\log(\det X) = -\log(\prod_i \lambda_i) = -\sum_i \log \lambda_i$$.
- Lưu ý: lập luận tách riêng từng giá trị riêng là chưa đủ (các giá trị riêng nói chung không phải hàm lõm của $$X$$; chỉ $$\lambda_{\min}$$ là hàm lõm). Cách chứng minh chuẩn là hạn chế hàm lên một đường thẳng bất kỳ $$X = Z + tV$$ với $$Z \succ 0$$: ta có $$f(Z + tV) = -\log\det Z - \sum_i \log(1 + t\lambda_i)$$, trong đó $$\lambda_i$$ là các giá trị riêng của $$Z^{-1/2} V Z^{-1/2}$$. Mỗi số hạng $$-\log(1 + t\lambda_i)$$ lồi theo $$t$$, nên $$f$$ lồi.
- **Kết luận:** Hàm lồi trên $$\mathbb{S}_{++}^n$$.

**Bước 3: $$f(x) = \lVert x \rVert_p$$**
- **Miền xác định:** $$\mathbb{R}^n$$ (tập lồi).
- **Với $$p \geq 1$$:** bất đẳng thức tam giác (bất đẳng thức Minkowski) kết hợp với tính thuần nhất dương kéo theo tính lồi.
- **Với $$0 < p < 1$$:** không lồi (bất đẳng thức tam giác bị vi phạm; ví dụ với $$p = 1/2$$, $$\lVert (1,1) \rVert_{1/2} = 4 > \lVert (1,0) \rVert_{1/2} + \lVert (0,1) \rVert_{1/2} = 2$$).

**Bước 4: $$f(X) = \lambda_{\max}(X)$$**
- **Miền xác định:** $$\mathbb{S}^n$$ (tập lồi).
- **Chứng minh tính lồi:** theo biểu diễn thương Rayleigh, $$\lambda_{\max}(X) = \max_{\lVert v \rVert = 1} v^T X v$$.
- Vì mỗi hàm $$X \mapsto v^T X v$$ là hàm tuyến tính theo $$X$$, giá trị lớn nhất theo điểm của một họ hàm tuyến tính là hàm lồi.

</details>

---

## 📝 **Bài tập 9: Mô hình hóa bài toán tối ưu**

**Đề bài:** (Bài 1.9 từ Boyd & Vandenberghe)
Mô hình hóa các bài toán kỹ thuật sau dưới dạng bài toán tối ưu hóa lồi:

a) **Thiết kế mảng ăng-ten:** cực tiểu hóa mức búp phụ (sidelobe level).
b) **Thiết kế bộ lọc:** cực tiểu hóa gợn dải thông (passband ripple) và năng lượng dải chắn (stopband energy).
c) **Thiết kế dàn kết cấu (truss design):** cực tiểu hóa khối lượng với ràng buộc độ cứng.
d) **Khớp dữ liệu:** hồi quy bền vững khi dữ liệu có điểm ngoại lai.

**Yêu cầu:**
1. Xây dựng mô hình toán học cho từng bài toán.
2. Xác định rõ biến quyết định, hàm mục tiêu và các ràng buộc.
3. Kiểm chứng tính lồi của mô hình.
4. Đề xuất hướng giải phù hợp.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Thiết kế mảng ăng-ten**
- **Biến quyết định:** $$w \in \mathbb{C}^n$$ (vector trọng số của các phần tử mảng).
- **Hàm mục tiêu:** cực tiểu hóa biên độ búp phụ lớn nhất:
$$\min_{w,t} t \quad \text{s.t.} \quad |a(\theta)^H w| \leq t, \quad \forall \theta \in \Theta_{sidelobe}$$
trong đó $$a(\theta)$$ là vector lái (steering vector) và $$\Theta_{sidelobe}$$ là miền góc búp phụ.
- **Ràng buộc búp chính:** $$a(\theta_0)^H w = 1$$ (chuẩn hóa độ lợi theo hướng mục tiêu).
- **Tính lồi:** là bài toán SOCP (các ràng buộc mô-đun phức là ràng buộc nón bậc hai).

**Bước 2: Thiết kế bộ lọc**
- **Biến quyết định:** $$h \in \mathbb{R}^n$$ (các hệ số của bộ lọc).
- **Gợn dải thông:** $$|H(\omega) - 1| \leq \delta_p, \quad \omega \in \Omega_p$$
- **Suy hao dải chắn:** $$|H(\omega)| \leq \delta_s, \quad \omega \in \Omega_s$$
trong đó $$H(\omega) = \sum_{k=0}^{n-1} h_k e^{-j\omega k}$$ là đáp ứng tần số.
- **Mô hình lồi:**
$$\min_{h,\delta_p,\delta_s} \alpha \delta_p + \beta \delta_s$$
với các ràng buộc đáp ứng tần số nêu trên.

**Bước 3: Thiết kế dàn kết cấu**
- **Biến quyết định:** $$A \in \mathbb{R}^m$$ (diện tích mặt cắt ngang các thanh dàn).
- **Hàm mục tiêu:** $$\min \sum_{i=1}^m \rho_i l_i A_i$$ (tổng khối lượng).
- **Ràng buộc độ cứng:** $$u^T K(A) u \geq u_{min}^T K_0 u_{min}$$
với $$K(A) = \sum_{i=1}^m A_i K_i$$ là ma trận độ cứng tổng thể.
- **Tính lồi:** hàm mục tiêu tuyến tính và ràng buộc tuyến tính theo $$A$$ (với chuyển vị $$u$$ cố định).

**Bước 4: Hồi quy bền vững**
- **Biến quyết định:** $$\beta \in \mathbb{R}^p$$ (vector hệ số hồi quy).
- **Hàm mất mát Huber:** $$\min_\beta \sum_{i=1}^n \phi(y_i - x_i^T \beta)$$
với $$\phi(u) = \begin{cases} \frac{1}{2}u^2 & |u| \leq M \\ M|u| - \frac{1}{2}M^2 & |u| > M \end{cases}$$
- **Tính lồi:** hàm Huber là hàm lồi, nên bài toán tối ưu là lồi.

</details>

---

## 📝 **Bài tập 10: Nhập môn lý thuyết đối ngẫu**

**Đề bài:** (Bài 1.10 từ Boyd & Vandenberghe)
Cho bài toán quy hoạch tuyến tính (LP):
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Yêu cầu:**
1. Xây dựng bài toán đối ngẫu thông qua hàm Lagrange.
2. Chứng minh định lý đối ngẫu yếu (weak duality).
3. Nêu điều kiện để đối ngẫu mạnh (strong duality) xảy ra.
4. Diễn giải ý nghĩa kinh tế của các biến đối ngẫu.
5. Phát biểu điều kiện bù lỏng (complementary slackness).

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Hàm Lagrange và bài toán đối ngẫu**
$$L(x,\nu,\lambda) = c^T x + \nu^T(Ax - b) - \lambda^T x$$

**Hàm đối ngẫu:**
$$g(\nu,\lambda) = \inf_x L(x,\nu,\lambda) = \inf_x (c + A^T \nu - \lambda)^T x - \nu^T b$$

**Điều kiện để hàm đối ngẫu hữu hạn:** $$c + A^T \nu - \lambda = 0$$, tức $$\lambda = A^T \nu + c$$.

**Bài toán đối ngẫu:**
$$\max_{\nu,\lambda} g(\nu,\lambda) = \max_\nu -\nu^T b \quad \text{s.t.} \quad A^T \nu + c \geq 0$$

Đổi dấu biến $$\nu \leftarrow -\nu$$, ta viết lại ở dạng quen thuộc:
$$\max_\nu b^T \nu \quad \text{s.t.} \quad A^T \nu \leq c$$

**Bước 2: Đối ngẫu yếu**
Với mọi nghiệm khả thi gốc $$x$$ và nghiệm khả thi đối ngẫu $$\nu$$:
$$c^T x \geq b^T \nu$$

**Chứng minh:**
$$c^T x \geq (A^T \nu)^T x = \nu^T Ax = \nu^T b = b^T \nu$$

**Bước 3: Đối ngẫu mạnh**
Với bài toán LP, đối ngẫu mạnh luôn đúng khi cả bài toán gốc và bài toán đối ngẫu đều khả thi (định lý cơ bản của quy hoạch tuyến tính).

**Bước 4: Ý nghĩa kinh tế**
- $$\nu_i$$ là giá ẩn (shadow price) của nguồn lực thứ $$i$$.
- $$\nu_i$$ biểu thị giá trị biên của ràng buộc thứ $$i$$: nếu $$b_i$$ tăng thêm 1 đơn vị (trong phạm vi cơ sở tối ưu không đổi), giá trị tối ưu thay đổi xấp xỉ một lượng $$\nu_i$$.

**Bước 5: Điều kiện bù lỏng (Complementary slackness)**
- Nếu $$x_j^* > 0$$ thì $$(A^T \nu^*)_j = c_j$$ (chi phí giảm bằng 0).
- Nếu $$(A^T \nu^*)_j < c_j$$ thì $$x_j^* = 0$$.

</details>

---

## 💡 Kinh nghiệm thực hành

#### **Khi phân loại bài toán tối ưu hóa:**
- Kiểm tra dạng của hàm mục tiêu (tuyến tính, bậc hai hay tổng quát).
- Xác định loại ràng buộc (tuyến tính, bậc hai hay nón).
- Kiểm tra tính lồi của từng thành phần.

#### **Khi chuyển đổi về dạng chuẩn:**
- Biến tự do: tách thành hiệu hai biến không âm $$x = x^+ - x^-$$.
- Bất đẳng thức: bổ sung biến bù (slack/surplus).
- Bài toán cực đại: đổi dấu hàm mục tiêu để chuyển thành cực tiểu.

#### **Khi xác minh tính lồi:**
- Ưu tiên điều kiện bậc hai khi hàm khả vi hai lần.
- Áp dụng các phép toán bảo toàn tính lồi.
- Quay về định nghĩa trực tiếp khi cần thiết.

---

## 💡 **Tổng kết**

### **Phân loại các lớp bài toán tối ưu**

| Loại | Hàm mục tiêu | Ràng buộc | Ví dụ |
|------|--------------|-----------|-------|
| **LP** | Tuyến tính | Tuyến tính | $$\min c^Tx$$, $$Ax \leq b$$ |
| **QP** | Bậc hai | Tuyến tính | $$\min \frac{1}{2}x^TQx + c^Tx$$ |
| **QCQP** | Bậc hai | Bậc hai | Danh mục đầu tư có ràng buộc rủi ro |
| **SOCP** | Tuyến tính | Chuẩn $$\ell_2$$ | $$\|\|Ax-b\|\|_2 \leq c^Tx$$ |
| **SDP** | Tuyến tính | Ma trận nửa xác định dương | $$\min \text{tr}(CX)$$, $$X \succeq 0$$ |

### **Các biến thể bình phương tối thiểu**

| Phương pháp | Hàm mục tiêu | Đặc điểm |
|-------------|--------------|----------|
| Bình phương tối thiểu (OLS) | $$\|\|Ax-b\|\|_2^2$$ | Có nghiệm dạng đóng |
| Có trọng số (WLS) | $$(Ax-b)^TW(Ax-b)$$ | Gán trọng số khác nhau cho từng quan sát |
| Có điều chuẩn (Ridge) | $$\|\|Ax-b\|\|_2^2 + \lambda\|\|x\|\|_2^2$$ | Giảm quá khớp, ổn định ma trận |
| Bền vững (Robust LS) | $$\sum \phi((Ax-b)_i)$$ | Ít nhạy cảm với điểm ngoại lai |
| LASSO | $$\|\|Ax-b\|\|_2^2 + \lambda\|\|x\|\|_1$$ | Tạo nghiệm thưa (sparse) |

### **Các khái niệm đối ngẫu cốt lõi**

- **Đối ngẫu yếu:** $$d^* \leq p^*$$ (luôn đúng).
- **Đối ngẫu mạnh:** $$d^* = p^*$$ (đúng khi thỏa điều kiện chính quy, ví dụ điều kiện Slater).
- **Giá ẩn (Shadow price):** $$\nu_i^*$$ là giá trị biên của ràng buộc thứ $$i$$.
- **Điều kiện bù lỏng:** $$\lambda_i^* (g_i(x^*)) = 0$$.

---

## 📚 Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 1: Introduction
   - Exercises 1.1–1.15

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization*. Springer.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming*. Athena Scientific.

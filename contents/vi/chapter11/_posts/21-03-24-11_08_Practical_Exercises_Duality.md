---
layout: post
title: 11-8 Bài Tập Thực Hành - Tính Đối Ngẫu Tổng Quát
chapter: '11'
order: 9
owner: GitHub Copilot
lang: vi
categories:
- chapter11
lesson_type: required
---

# Bài Tập Thực Hành - Tính Đối Ngẫu Tổng Quát

## 📝 **Bài tập 1: Quadratic Programming đơn giản**

**Đề bài:** Cho bài toán
$$\min_x \frac{1}{2}x^2 + x \quad \text{s.t.} \quad x \geq 1$$

**Yêu cầu:**
1. Viết lại bài toán ở dạng chuẩn
2. Xây dựng hàm Lagrangian
3. Tính hàm đối ngẫu $$g(u)$$
4. Giải bài toán đối ngẫu
5. So sánh nghiệm primal và dual

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Viết lại bài toán**
$$\min_x \frac{1}{2}x^2 + x \quad \text{s.t.} \quad -x + 1 \leq 0$$

**Bước 2: Hàm Lagrangian**
$$L(x,u) = \frac{1}{2}x^2 + x + u(-x + 1) = \frac{1}{2}x^2 + (1-u)x + u$$

**Bước 3: Tính hàm đối ngẫu**
$$g(u) = \inf_x L(x,u) = \inf_x \left\{\frac{1}{2}x^2 + (1-u)x + u\right\}$$

Đạo hàm theo $$x$$: $$\frac{\partial L}{\partial x} = x + (1-u) = 0$$

Suy ra: $$x^* = u - 1$$

Thay vào: $$g(u) = \frac{1}{2}(u-1)^2 + (1-u)(u-1) + u = -\frac{1}{2}(u-1)^2 + u$$

**Bước 4: Bài toán đối ngẫu**
$$\max_u g(u) = \max_u \left\{-\frac{1}{2}(u-1)^2 + u\right\} \quad \text{s.t.} \quad u \geq 0$$

Đạo hàm: $$g'(u) = -(u-1) + 1 = 2 - u = 0 \Rightarrow u^* = 2$$

**Bước 5: So sánh nghiệm**
- **Dual optimal:** $$u^* = 2$$, $$g^* = g(2) = -\frac{1}{2} + 2 = \frac{3}{2}$$
- **Primal optimal:** $$x^* = u^* - 1 = 1$$, $$f^* = \frac{1}{2} + 1 = \frac{3}{2}$$
- **Strong duality:** $$f^* = g^* = \frac{3}{2}$$ ✓

</details>

---

## 📝 **Bài tập 2: Bài toán với nhiều ràng buộc**

**Đề bài:** 
$$\min_{x,y} x^2 + y^2 \quad \text{s.t.} \quad x + y \geq 2, \quad x \geq 0, \quad y \geq 0$$

**Yêu cầu:**
1. Xây dựng hàm Lagrangian đầy đủ
2. Tính hàm đối ngẫu $$g(u_1, u_2, u_3)$$
3. Tìm điều kiện để $$g(u_1, u_2, u_3) > -\infty$$
4. Giải bài toán đối ngẫu

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Viết lại bài toán**
$$\min_{x,y} x^2 + y^2 \quad \text{s.t.} \quad -x - y + 2 \leq 0, \quad -x \leq 0, \quad -y \leq 0$$

**Bước 2: Hàm Lagrangian**
$$L(x,y,u_1,u_2,u_3) = x^2 + y^2 + u_1(-x - y + 2) + u_2(-x) + u_3(-y)$$
$$= x^2 + y^2 - (u_1 + u_2)x - (u_1 + u_3)y + 2u_1$$

**Bước 3: Tính hàm đối ngẫu**
$$g(u_1,u_2,u_3) = \inf_{x,y} L(x,y,u_1,u_2,u_3)$$

Điều kiện tối ưu:
- $$\frac{\partial L}{\partial x} = 2x - (u_1 + u_2) = 0 \Rightarrow x^* = \frac{u_1 + u_2}{2}$$
- $$\frac{\partial L}{\partial y} = 2y - (u_1 + u_3) = 0 \Rightarrow y^* = \frac{u_1 + u_3}{2}$$

Thay vào:
$$g(u_1,u_2,u_3) = -\frac{(u_1 + u_2)^2}{4} - \frac{(u_1 + u_3)^2}{4} + 2u_1$$

**Bước 4: Điều kiện hữu hạn**
$$g(u_1,u_2,u_3) > -\infty$$ luôn đúng vì là hàm bậc hai.

**Bước 5: Bài toán đối ngẫu**
$$\max_{u_1,u_2,u_3} g(u_1,u_2,u_3) \quad \text{s.t.} \quad u_1,u_2,u_3 \geq 0$$

Sử dụng điều kiện KKT để tìm nghiệm tối ưu.

</details>

---

## 📝 **Bài tập 3: Linear Programming với ràng buộc đẳng thức**

**Đề bài:** (Bài 5.1 từ Boyd & Vandenberghe)
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b$$

**Yêu cầu:**
1. Xây dựng hàm Lagrangian
2. Tính hàm đối ngẫu $$g(\nu)$$
3. Chứng minh strong duality
4. Tìm điều kiện tối ưu

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Hàm Lagrangian**
$$L(x,\nu) = c^T x + \nu^T (Ax - b)$$

**Bước 2: Hàm đối ngẫu**
$$g(\nu) = \inf_x L(x,\nu) = \inf_x \{c^T x + \nu^T Ax\} - \nu^T b$$
$$= \inf_x (c + A^T \nu)^T x - \nu^T b$$

Nếu $$c + A^T \nu \neq 0$$, thì $$g(\nu) = -\infty$$

Nếu $$c + A^T \nu = 0$$, thì $$g(\nu) = -\nu^T b$$

**Bước 3: Bài toán đối ngẫu**
$$\max_\nu \{-\nu^T b\} \quad \text{s.t.} \quad A^T \nu + c = 0$$

Tương đương:
$$\min_\nu \nu^T b \quad \text{s.t.} \quad A^T \nu = -c$$

**Bước 4: Strong duality**
Vì bài toán primal là LP và feasible (giả sử), nên có strong duality.

</details>

---

## 📝 **Bài tập 4: Quadratic Programming với ràng buộc bất đẳng thức**

**Đề bài:** (Bài 5.2 từ Boyd & Vandenberghe)
$$\min_x \frac{1}{2}x^T P x + q^T x + r \quad \text{s.t.} \quad Gx \leq h$$

với $$P \succ 0$$.

**Yêu cầu:**
1. Xây dựng hàm Lagrangian
2. Tính hàm đối ngẫu
3. Tìm điều kiện KKT
4. Giải trường hợp cụ thể

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Hàm Lagrangian**
$$L(x,\lambda) = \frac{1}{2}x^T P x + q^T x + r + \lambda^T (Gx - h)$$

**Bước 2: Tính hàm đối ngẫu**
$$g(\lambda) = \inf_x L(x,\lambda)$$

Điều kiện tối ưu: $$\nabla_x L = Px + q + G^T \lambda = 0$$

Suy ra: $$x^*(\lambda) = -P^{-1}(q + G^T \lambda)$$

Thay vào:
$$g(\lambda) = -\frac{1}{2}(q + G^T \lambda)^T P^{-1} (q + G^T \lambda) + r - \lambda^T h$$

**Bước 3: Bài toán đối ngẫu**
$$\max_\lambda g(\lambda) \quad \text{s.t.} \quad \lambda \geq 0$$

**Bước 4: Điều kiện KKT**
- Stationarity: $$Px^* + q + G^T \lambda^* = 0$$
- Primal feasibility: $$Gx^* \leq h$$
- Dual feasibility: $$\lambda^* \geq 0$$
- Complementary slackness: $$\lambda_i^* (G_i x^* - h_i) = 0$$

</details>

---

## 📝 **Bài tập 5: Norm approximation**

**Đề bài:** (Bài 5.3 từ Boyd & Vandenberghe)
$$\min_x \lVert Ax - b \rVert$$

với norm là $$\ell_1, \ell_2,$$ hoặc $$\ell_\infty$$.

**Yêu cầu:**
1. Reformulate thành bài toán có ràng buộc
2. Xây dựng dual cho mỗi trường hợp
3. So sánh các dual problems

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Trường hợp 1: $$\ell_1$$ norm**
$$\min_{x,t} \mathbf{1}^T t \quad \text{s.t.} \quad -t \leq Ax - b \leq t$$

Dual:
$$\max_{\lambda,\mu} -b^T(\lambda - \mu) \quad \text{s.t.} \quad A^T(\lambda - \mu) = 0, \quad \lambda + \mu = \mathbf{1}, \quad \lambda,\mu \geq 0$$

**Trường hợp 2: $$\ell_2$$ norm**
$$\min_{x,t} t \quad \text{s.t.} \quad \lVert Ax - b \rVert_2 \leq t$$

Dual:
$$\max_{\lambda,\nu} -b^T \nu - \lambda \quad \text{s.t.} \quad A^T \nu = 0, \quad \lVert \nu \rVert_2 \leq \lambda, \quad \lambda \geq 0$$

**Trường hợp 3: $$\ell_\infty$$ norm**
$$\min_{x,t} t \quad \text{s.t.} \quad -t\mathbf{1} \leq Ax - b \leq t\mathbf{1}$$

Dual:
$$\max_{\lambda,\mu} -b^T(\lambda - \mu) \quad \text{s.t.} \quad A^T(\lambda - \mu) = 0, \quad \lVert \lambda - \mu \rVert_1 \leq 1$$

</details>

---

## 📝 **Bài tập 6: Entropy maximization**

**Đề bài:** (Bài 5.4 từ Boyd & Vandenberghe)
$$\max_x \sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Yêu cầu:**
1. Chuyển về bài toán minimization
2. Xây dựng hàm Lagrangian
3. Tính hàm đối ngẫu
4. Tìm nghiệm tối ưu

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Chuyển đổi**
$$\min_x -\sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Bước 2: Hàm Lagrangian**
$$L(x,\nu,\lambda) = -\sum_{i=1}^n x_i \log x_i + \nu^T(Ax - b) - \lambda^T x$$

**Bước 3: Điều kiện tối ưu**
$$\frac{\partial L}{\partial x_i} = -(\log x_i + 1) + (A^T \nu)_i - \lambda_i = 0$$

Suy ra: $$x_i = e^{(A^T \nu)_i - \lambda_i - 1}$$

**Bước 4: Complementary slackness**
Nếu $$x_i > 0$$, thì $$\lambda_i = 0$$, suy ra:
$$x_i = e^{(A^T \nu)_i - 1}$$

**Bước 5: Hàm đối ngẫu**
$$g(\nu,\lambda) = -\sum_{i=1}^n e^{(A^T \nu)_i - \lambda_i - 1} - \nu^T b$$

</details>

---

## 📝 **Bài tập 7: Minimum volume ellipsoid**

**Đề bài:** (Bài 5.5 từ Boyd & Vandenberghe)
Tìm ellipsoid có thể tích nhỏ nhất chứa các điểm $$x_1, \ldots, x_m \in \mathbb{R}^n$$:

$$\min_{A,b} \log \det A^{-1} \quad \text{s.t.} \quad \lVert A x_i + b \rVert_2 \leq 1, \quad i = 1,\ldots,m$$

**Yêu cầu:**
1. Giải thích ý nghĩa hình học
2. Xây dựng hàm Lagrangian
3. Tính điều kiện KKT
4. Phân tích trường hợp 2D

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Ý nghĩa hình học**
Ellipsoid: $$\mathcal{E} = \{A^{-1}(u - b) : \lVert u \rVert_2 \leq 1\}$$
Thể tích: $$\text{vol}(\mathcal{E}) = \frac{\pi^{n/2}}{\Gamma(n/2 + 1)} \det A^{-1}$$

**Bước 2: Hàm Lagrangian**
$$L(A,b,\lambda) = \log \det A^{-1} + \sum_{i=1}^m \lambda_i (\lVert A x_i + b \rVert_2^2 - 1)$$

**Bước 3: Điều kiện KKT**
- $$\frac{\partial L}{\partial b} = 2\sum_{i=1}^m \lambda_i (A x_i + b) = 0$$
- $$\frac{\partial L}{\partial A} = -A^{-T} + 2\sum_{i=1}^m \lambda_i (A x_i + b) x_i^T = 0$$

**Bước 4: Từ điều kiện đầu tiên:**
$$\sum_{i=1}^m \lambda_i (A x_i + b) = 0$$

**Bước 5: Từ điều kiện thứ hai:**
$$A^{-T} = 2\sum_{i=1}^m \lambda_i (A x_i + b) x_i^T$$

</details>

---

## 📝 **Bài tập 8: Chebyshev center**

**Đề bài:** (Bài 5.6 từ Boyd & Vandenberghe)
Tìm tâm và bán kính của hình cầu lớn nhất nằm trong polyhedron:
$$P = \{x : a_i^T x \leq b_i, \quad i = 1,\ldots,m\}$$

$$\max_{x_c,r} r \quad \text{s.t.} \quad a_i^T x_c + r \lVert a_i \rVert_2 \leq b_i, \quad i = 1,\ldots,m$$

**Yêu cầu:**
1. Giải thích ý nghĩa hình học
2. Xây dựng dual problem
3. Phân tích điều kiện strong duality
4. Tính toán cho trường hợp cụ thể

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Ý nghĩa hình học**
Hình cầu $$\{x : \lVert x - x_c \rVert_2 \leq r\}$$ nằm trong $$P$$ khi và chỉ khi:
$$\max_{\lVert u \rVert_2 \leq 1} a_i^T(x_c + ru) \leq b_i$$
$$\Leftrightarrow a_i^T x_c + r \lVert a_i \rVert_2 \leq b_i$$

**Bước 2: Hàm Lagrangian**
$$L(x_c,r,\lambda) = -r + \sum_{i=1}^m \lambda_i (a_i^T x_c + r \lVert a_i \rVert_2 - b_i)$$

**Bước 3: Điều kiện tối ưu**
- $$\frac{\partial L}{\partial x_c} = \sum_{i=1}^m \lambda_i a_i = 0$$
- $$\frac{\partial L}{\partial r} = -1 + \sum_{i=1}^m \lambda_i \lVert a_i \rVert_2 = 0$$

**Bước 4: Hàm đối ngẫu**
Từ điều kiện trên: $$\sum_{i=1}^m \lambda_i \lVert a_i \rVert_2 = 1$$

$$g(\lambda) = -\sum_{i=1}^m \lambda_i b_i$$

**Bước 5: Bài toán đối ngẫu**
$$\min_\lambda \sum_{i=1}^m \lambda_i b_i \quad \text{s.t.} \quad \sum_{i=1}^m \lambda_i a_i = 0, \quad \sum_{i=1}^m \lambda_i \lVert a_i \rVert_2 = 1, \quad \lambda \geq 0$$

</details>

---

## 📝 **Bài tập 9: Geometric programming**

**Đề bài:** (Bài 5.7 từ Boyd & Vandenberghe)
Bài toán geometric programming:
$$\min_x f_0(x) \quad \text{s.t.} \quad f_i(x) \leq 1, \quad i = 1,\ldots,m$$

với $$f_i(x) = \sum_{k=1}^{K_i} c_{ik} x_1^{a_{ik1}} \cdots x_n^{a_{ikn}}$$, $$c_{ik} > 0$$.

**Yêu cầu:**
1. Chuyển về convex form bằng log transformation
2. Xây dựng dual của convex form
3. Phân tích complementary slackness
4. Giải bài toán cụ thể

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Log transformation**
Đặt $$y_j = \log x_j$$, ta có:
$$f_i(x) = \sum_{k=1}^{K_i} c_{ik} e^{a_{ik}^T y}$$

Bài toán trở thành:
$$\min_y \log\left(\sum_{k=1}^{K_0} c_{0k} e^{a_{0k}^T y}\right) \quad \text{s.t.} \quad \log\left(\sum_{k=1}^{K_i} c_{ik} e^{a_{ik}^T y}\right) \leq 0$$

**Bước 2: Hàm Lagrangian**
$$L(y,\lambda) = \log\left(\sum_{k=1}^{K_0} c_{0k} e^{a_{0k}^T y}\right) + \sum_{i=1}^m \lambda_i \log\left(\sum_{k=1}^{K_i} c_{ik} e^{a_{ik}^T y}\right)$$

**Bước 3: Điều kiện tối ưu**
$$\frac{\partial L}{\partial y_j} = \sum_{i=0}^m \lambda_i \frac{\sum_{k=1}^{K_i} c_{ik} a_{ikj} e^{a_{ik}^T y}}{\sum_{k=1}^{K_i} c_{ik} e^{a_{ik}^T y}} = 0$$

với $$\lambda_0 = 1$$.

**Bước 4: Complementary slackness**
Nếu $$\lambda_i > 0$$, thì $$f_i(x^*) = 1$$ (ràng buộc active).

</details>

---

## 📝 **Bài tập 10: Water-filling**

**Đề bài:** (Bài 5.8 từ Boyd & Vandenberghe)
Bài toán phân bổ công suất trong thông tin:
$$\max_x \sum_{i=1}^n \log(\alpha_i + x_i) \quad \text{s.t.} \quad \sum_{i=1}^n x_i \leq P, \quad x_i \geq 0$$

với $$\alpha_i > 0$$, $$P > 0$$.

**Yêu cầu:**
1. Xây dựng điều kiện KKT
2. Tìm nghiệm water-filling
3. Phân tích thuật toán
4. Ứng dụng vào trường hợp cụ thể

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Hàm Lagrangian**
$$L(x,\nu,\lambda) = -\sum_{i=1}^n \log(\alpha_i + x_i) + \nu\left(\sum_{i=1}^n x_i - P\right) - \sum_{i=1}^n \lambda_i x_i$$

**Bước 2: Điều kiện KKT**
- Stationarity: $$-\frac{1}{\alpha_i + x_i} + \nu - \lambda_i = 0$$
- Complementary slackness: $$\lambda_i x_i = 0$$, $$\nu\left(\sum_{i=1}^n x_i - P\right) = 0$$

**Bước 3: Phân tích**
Từ stationarity: $$\frac{1}{\alpha_i + x_i} = \nu - \lambda_i$$

Nếu $$x_i > 0$$, thì $$\lambda_i = 0$$, suy ra:
$$\alpha_i + x_i = \frac{1}{\nu} \Rightarrow x_i = \frac{1}{\nu} - \alpha_i$$

Nếu $$x_i = 0$$, thì $$\lambda_i \geq 0$$, suy ra:
$$\nu \leq \frac{1}{\alpha_i}$$

**Bước 4: Water-filling solution**
$$x_i^* = \max\left\{0, \frac{1}{\nu^*} - \alpha_i\right\}$$

với $$\nu^*$$ được xác định từ:
$$\sum_{i=1}^n \max\left\{0, \frac{1}{\nu^*} - \alpha_i\right\} = P$$

**Bước 5: Thuật toán**
1. Sắp xếp $$\alpha_i$$ theo thứ tự tăng dần
2. Tìm $$\nu^*$$ sao cho constraint được thỏa mãn
3. Tính $$x_i^*$$ theo công thức water-filling

</details>


---

## 📝 **Bài tập 11: Semidefinite programming relaxation**

**Đề bài:** (Bài 5.9 từ Boyd & Vandenberghe)
Cho bài toán QCQP (Quadratically Constrained Quadratic Program):
$$\min_x x^T P_0 x + 2q_0^T x + r_0$$
$$\text{s.t.} \quad x^T P_i x + 2q_i^T x + r_i \leq 0, \quad i = 1,\ldots,m$$

**Yêu cầu:**
1. Xây dựng SDP relaxation
2. Tính dual của SDP relaxation
3. Phân tích điều kiện strong duality
4. So sánh bound với original problem

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: SDP relaxation**
Đặt $$X = xx^T$$, bài toán trở thành:
$$\min_{X,x} \text{tr}(P_0 X) + 2q_0^T x + r_0$$
$$\text{s.t.} \quad \text{tr}(P_i X) + 2q_i^T x + r_i \leq 0, \quad X \succeq 0, \quad X = xx^T$$

Bỏ constraint $$X = xx^T$$:
$$\min_{X,x} \text{tr}(P_0 X) + 2q_0^T x + r_0$$
$$\text{s.t.} \quad \text{tr}(P_i X) + 2q_i^T x + r_i \leq 0, \quad X \succeq 0$$

**Bước 2: Dual của SDP**
$$\max_{\lambda,Z} -\sum_{i=1}^m \lambda_i r_i + r_0$$
$$\text{s.t.} \quad \sum_{i=1}^m \lambda_i P_i - P_0 + Z = 0, \quad \sum_{i=1}^m \lambda_i q_i = q_0, \quad \lambda \geq 0, \quad Z \succeq 0$$

**Bước 3: Strong duality**
SDP có strong duality khi Slater's condition thỏa mãn: tồn tại $$(X,x)$$ với $$X \succ 0$$ và constraints nghiêm ngặt.

</details>

---

## 📝 **Bài tập 12: Robust linear programming**

**Đề bài:** (Bài 5.10 từ Boyd & Vandenberghe)
$$\min_x c^T x \quad \text{s.t.} \quad a_i^T x \leq b_i \quad \forall a_i \in \mathcal{E}_i, \quad i = 1,\ldots,m$$

với $$\mathcal{E}_i = \{a_i^{nom} + u : \lVert u \rVert_2 \leq \rho_i\}$$.

**Yêu cầu:**
1. Reformulate thành deterministic problem
2. Xây dựng dual problem
3. Phân tích worst-case scenarios
4. Tính price of robustness

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Deterministic reformulation**
$$\max_{a_i \in \mathcal{E}_i} a_i^T x = (a_i^{nom})^T x + \rho_i \lVert x \rVert_2$$

Bài toán trở thành:
$$\min_x c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \rho_i \lVert x \rVert_2 \leq b_i$$

**Bước 2: Second-order cone constraints**
$$\min_{x,t_i} c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \rho_i t_i \leq b_i, \quad \lVert x \rVert_2 \leq t_i$$

**Bước 3: Dual problem**
$$\max_{\lambda,\mu_i,v_i} \sum_{i=1}^m \lambda_i b_i$$
$$\text{s.t.} \quad \sum_{i=1}^m \lambda_i a_i^{nom} + \sum_{i=1}^m \mu_i v_i = c, \quad \lVert v_i \rVert_2 \leq \mu_i, \quad \lambda_i \rho_i = \mu_i$$

</details>

---

## 📝 **Bài tập 13: Maximum likelihood estimation**

**Đề bài:** (Bài 5.11 từ Boyd & Vandenberghe)
Cho $$n$$ observations $$y_1, \ldots, y_n$$ từ distribution với density:
$$p(y|\theta) = \exp(\theta^T \phi(y) - g(\theta))$$

**Yêu cầu:**
1. Formulate MLE problem
2. Derive dual problem
3. Phân tích convexity
4. Tìm điều kiện optimality

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: MLE formulation**
$$\max_\theta \sum_{i=1}^n \log p(y_i|\theta) = \max_\theta \sum_{i=1}^n (\theta^T \phi(y_i) - g(\theta))$$

Tương đương:
$$\min_\theta ng(\theta) - \theta^T \sum_{i=1}^n \phi(y_i)$$

**Bước 2: Convexity**
Vì $$g(\theta)$$ là log-partition function nên convex. Do đó bài toán là convex.

**Bước 3: Optimality condition**
$$\nabla g(\theta^*) = \frac{1}{n}\sum_{i=1}^n \phi(y_i)$$

**Bước 4: Dual interpretation**
Dual variables tương ứng với moment constraints trong exponential family.

</details>

---

## 📝 **Bài tập 14: Analytic centering**

**Đề bài:** (Bài 5.12 từ Boyd & Vandenberghe)
$$\min_x -\sum_{i=1}^m \log(b_i - a_i^T x)$$

với $$\{x : a_i^T x < b_i, i = 1,\ldots,m\} \neq \emptyset$$.

**Yêu cầu:**
1. Chứng minh strict convexity
2. Tìm điều kiện optimality
3. Phân tích geometric interpretation
4. Xây dựng Newton method

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Strict convexity**
$$\nabla^2 f(x) = \sum_{i=1}^m \frac{a_i a_i^T}{(b_i - a_i^T x)^2} \succ 0$$

**Bước 2: Optimality condition**
$$\sum_{i=1}^m \frac{a_i}{b_i - a_i^T x^*} = 0$$

**Bước 3: Geometric interpretation**
$$x^*$$ là center của polytope $$\{x : a_i^T x \leq b_i\}$$ theo nghĩa minimize tích các khoảng cách đến boundaries.

**Bước 4: Newton step**
$$\Delta x = -(\nabla^2 f(x))^{-1} \nabla f(x)$$

với backtracking line search để đảm bảo feasibility.

</details>

---

## 📝 **Bài tập 15: Minimum fuel optimal control**

**Đề bài:** (Bài 5.13 từ Boyd & Vandenberghe)
$$\min_{u,x} \sum_{t=0}^{T-1} \lVert u_t \rVert_1$$
$$\text{s.t.} \quad x_{t+1} = Ax_t + Bu_t, \quad x_0 = x^{init}, \quad x_T = x^{final}$$

**Yêu cầu:**
1. Reformulate thành LP
2. Xây dựng dual problem
3. Phân tích bang-bang control
4. Tìm switching times

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: LP formulation**
Đặt $$u_t = u_t^+ - u_t^-$$ với $$u_t^+, u_t^- \geq 0$$:
$$\min \sum_{t=0}^{T-1} \mathbf{1}^T (u_t^+ + u_t^-)$$
$$\text{s.t.} \quad x_{t+1} = Ax_t + B(u_t^+ - u_t^-), \quad x_0 = x^{init}, \quad x_T = x^{final}$$

**Bước 2: Dual variables**
- $$\lambda_t$$: dual cho dynamics constraints
- $$\mu_t^+, \mu_t^-$$: dual cho control bounds

**Bước 3: Bang-bang property**
Optimal control có dạng $$u_t^* \in \{-u^{max}, 0, u^{max}\}$$ cho mỗi component.

**Bước 4: Switching condition**
$$u_t^*$$ switches khi $$B^T \lambda_t$$ đổi dấu.

</details>

---

## 📝 **Bài tập 16: Sparse signal recovery**

**Đề bài:** (Bài 5.14 từ Boyd & Vandenberghe)
$$\min_x \lVert x \rVert_1 \quad \text{s.t.} \quad Ax = b$$

với $$A \in \mathbb{R}^{m \times n}$$, $$m < n$$.

**Yêu cầu:**
1. Reformulate thành LP
2. Derive dual problem
3. Phân tích uniqueness conditions
4. So sánh với $$\ell_0$$ minimization

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: LP formulation**
$$\min_{x,t} \mathbf{1}^T t \quad \text{s.t.} \quad Ax = b, \quad -t \leq x \leq t$$

**Bước 2: Dual problem**
$$\max_{\nu,\lambda,\mu} b^T \nu$$
$$\text{s.t.} \quad A^T \nu + \lambda - \mu = 0, \quad \lambda + \mu = \mathbf{1}, \quad \lambda,\mu \geq 0$$

Tương đương:
$$\max_\nu b^T \nu \quad \text{s.t.} \quad \lVert A^T \nu \rVert_\infty \leq 1$$

**Bước 3: Complementary slackness**
Nếu $$|x_i^*| < t_i^*$$, thì $$(A^T \nu^*)_i = 0$$.
Nếu $$x_i^* = t_i^*$$, thì $$(A^T \nu^*)_i = 1$$.
Nếu $$x_i^* = -t_i^*$$, thì $$(A^T \nu^*)_i = -1$$.

**Bước 4: Uniqueness**
Nghiệm unique khi restricted isometry property (RIP) thỏa mãn.

</details>

---

## 📝 **Bài tập 17: Matrix completion**

**Đề bài:** (Bài 5.15 từ Boyd & Vandenberghe)
$$\min_X \text{tr}(X) \quad \text{s.t.} \quad X_{ij} = M_{ij}, \quad (i,j) \in \Omega, \quad X \succeq 0$$

với $$\Omega$$ là tập các entries đã biết.

**Yêu cầu:**
1. Xây dựng dual problem
2. Phân tích rank minimization connection
3. Tìm điều kiện recoverability
4. Implement alternating minimization

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Dual problem**
$$\max_Y \sum_{(i,j) \in \Omega} M_{ij} Y_{ij}$$
$$\text{s.t.} \quad \mathcal{P}_\Omega(Y) + Z = I, \quad Z \succeq 0$$

với $$\mathcal{P}_\Omega(Y)_{ij} = Y_{ij}$$ nếu $$(i,j) \in \Omega$$, ngược lại $$= 0$$.

**Bước 2: Rank connection**
Nuclear norm $$\lVert X \rVert_* = \text{tr}(X)$$ là convex relaxation của $$\text{rank}(X)$$.

**Bước 3: Complementary slackness**
$$X^* Z^* = 0$$, nghĩa là $$\text{range}(X^*) \perp \text{range}(Z^*)$$.

**Bước 4: Recoverability condition**
Incoherence condition và sufficient sampling trong $$\Omega$$.

</details>

---

## 📝 **Bài tập 18: Total variation denoising**

**Đề bài:** (Bài 5.16 từ Boyd & Vandenberghe)
$$\min_x \frac{1}{2}\lVert x - y \rVert_2^2 + \lambda \sum_{i=1}^{n-1} |x_{i+1} - x_i|$$

**Yêu cầu:**
1. Reformulate thành QP
2. Derive dual problem
3. Phân tích piecewise linear solution
4. Implement ADMM algorithm

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: QP formulation**
Đặt $$z_i = x_{i+1} - x_i$$:
$$\min_{x,z} \frac{1}{2}\lVert x - y \rVert_2^2 + \lambda \lVert z \rVert_1$$
$$\text{s.t.} \quad Dx = z$$

với $$D$$ là difference matrix.

**Bước 2: Dual problem**
$$\max_\nu -\frac{1}{2}\lVert y - D^T \nu \rVert_2^2 + y^T D^T \nu$$
$$\text{s.t.} \quad \lVert \nu \rVert_\infty \leq \lambda$$

**Bước 3: Piecewise linear**
Solution $$x^*$$ là piecewise linear với breakpoints tại các điểm mà $$|\nu_i^*| = \lambda$$.

**Bước 4: ADMM**
Alternating minimization giữa $$x$$ và $$z$$ với augmented Lagrangian.

</details>

---

## 📝 **Bài tập 19: Facility location**

**Đề bài:** (Bài 5.17 từ Boyd & Vandenberghe)
$$\min_{x,y} \sum_{i=1}^m f_i y_i + \sum_{i=1}^m \sum_{j=1}^n c_{ij} x_{ij}$$
$$\text{s.t.} \quad \sum_{j=1}^n x_{ij} \leq M_i y_i, \quad \sum_{i=1}^m x_{ij} = d_j, \quad x_{ij} \geq 0, \quad y_i \in \{0,1\}$$

**Yêu cầu:**
1. LP relaxation analysis
2. Lagrangian dual formulation
3. Subgradient method implementation
4. Branch-and-bound algorithm

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: LP relaxation**
Relax $$y_i \in [0,1]$$:
$$\min_{x,y} \sum_{i=1}^m f_i y_i + \sum_{i=1}^m \sum_{j=1}^n c_{ij} x_{ij}$$
$$\text{s.t.} \quad \sum_{j=1}^n x_{ij} \leq M_i y_i, \quad \sum_{i=1}^m x_{ij} = d_j, \quad x,y \geq 0, \quad y \leq 1$$

**Bước 2: Lagrangian dual**
Dualize demand constraints:
$$L(x,y,\lambda) = \sum_{i=1}^m f_i y_i + \sum_{i,j} c_{ij} x_{ij} + \sum_j \lambda_j (d_j - \sum_i x_{ij})$$

**Bước 3: Dual function**
$$g(\lambda) = \sum_j \lambda_j d_j + \sum_i \min\{0, f_i + \sum_j (c_{ij} - \lambda_j) M_i / M_i\}$$

**Bước 4: Subgradient**
$$\partial g(\lambda) = d - \sum_i x_i^*(\lambda)$$

</details>

---

## 📝 **Bài tập 20: Optimal power flow**

**Đề bài:** (Bài 5.18 từ Boyd & Vandenberghe)
$$\min_p \sum_{i=1}^n C_i(p_i)$$
$$\text{s.t.} \quad \sum_{i=1}^n p_i = \sum_{j=1}^m d_j, \quad |f_k| \leq f_k^{max}, \quad p_i^{min} \leq p_i \leq p_i^{max}$$

với $$f_k$$ là power flow trên line $$k$$.

**Yêu cầu:**
1. DC power flow approximation
2. Lagrangian dual formulation
3. Economic dispatch interpretation
4. Locational marginal pricing

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: DC approximation**
$$f_k = \sum_{i=1}^n H_{ki} p_i$$

với $$H$$ là power transfer distribution factor matrix.

**Bước 2: Reformulated problem**
$$\min_p \sum_{i=1}^n C_i(p_i)$$
$$\text{s.t.} \quad \mathbf{1}^T p = \mathbf{1}^T d, \quad -f^{max} \leq Hp \leq f^{max}, \quad p^{min} \leq p \leq p^{max}$$

**Bước 3: Lagrangian**
$$L(p,\lambda,\mu,\nu) = \sum_i C_i(p_i) + \lambda(\mathbf{1}^T d - \mathbf{1}^T p) + \mu^T(Hp - f^{max}) + \nu^T(-f^{max} - Hp)$$

**Bước 4: Optimality**
$$C_i'(p_i^*) = \lambda^* - (H^T(\mu^* - \nu^*))_i + \text{dual variables cho bounds}$$

$$\lambda^*$$ là system marginal price, $$(H^T(\mu^* - \nu^*))_i$$ là congestion component.

</details>

---

## 📚 Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 5: Duality
   - Exercises 5.1-5.39

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming*. Athena Scientific.

---

## 💡 Mẹo Thực Hành

#### **Khi xây dựng bài toán đối ngẫu:**
- Luôn kiểm tra tính convex của bài toán nguyên thủy
- Xác định rõ các ràng buộc bất đẳng thức và đẳng thức
- Chú ý dấu của dual variables: $$u \geq 0$$ cho bất đẳng thức, $$v$$ free cho đẳng thức

#### **Khi tính hàm đối ngẫu:**
- Sử dụng điều kiện $$\nabla_x L(x,u,v) = 0$$ để tìm $$x^*(u,v)$$
- Thay ngược lại vào Lagrangian để được $$g(u,v)$$
- Kiểm tra điều kiện để $$g(u,v) > -\infty$$

#### **Khi phân tích KKT conditions:**
- Complementary slackness: $$u_i h_i(x^*) = 0$$
- Dual feasibility: $$u \geq 0$$
- Primal feasibility: $$h_i(x^*) \leq 0$$, $$l_j(x^*) = 0$$


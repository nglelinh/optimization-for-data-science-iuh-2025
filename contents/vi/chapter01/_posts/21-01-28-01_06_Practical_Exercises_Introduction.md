---
layout: post
title: 1-6 Bài Tập Thực Hành - Giới Thiệu Tối Ưu Hóa
chapter: '1'
order: 7
owner: GitHub Copilot
lang: vi
categories:
- chapter01
lesson_type: required
---

# Bài Tập Thực Hành - Giới Thiệu Tối Ưu Hóa

## 📝 **Bài tập 1: Phân loại bài toán tối ưu hóa cơ bản**

**Đề bài:** (Bài 1.1 từ Boyd & Vandenberghe)
Phân loại các bài toán sau đây thành: LP (Linear Programming), QP (Quadratic Programming), QCQP (Quadratically Constrained QP), SOCP (Second-Order Cone Programming), SDP (Semidefinite Programming), hay GP (Geometric Programming):

a) $$\min_{x \in \mathbb{R}^n} c^T x \quad \text{s.t.} \quad Ax \leq b$$

b) $$\min_{x \in \mathbb{R}^n} x^T P x + q^T x \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

c) $$\min_{x \in \mathbb{R}^n} \lVert Ax - b \rVert_2 \quad \text{s.t.} \quad \lVert x \rVert_2 \leq 1$$

**Yêu cầu:**
1. Xác định loại bài toán cho mỗi trường hợp
2. Giải thích lý do phân loại
3. Chỉ ra điều kiện để bài toán là convex
4. Đề xuất phương pháp giải phù hợp

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Phân loại**

**a) Quy hoạch tuyến tính (LP)**
- Hàm mục tiêu: tuyến tính ($$c^T x$$)
- Ràng buộc: bất đẳng thức tuyến tính ($$Ax \leq b$$)
- Đây là dạng chuẩn của LP

**b) Quy hoạch bậc hai (QP)**
- Hàm mục tiêu: bậc hai ($$x^T P x + q^T x$$)
- Ràng buộc: tuyến tính ($$Ax = b, x \geq 0$$)
- Lồi khi $$P \succeq 0$$

**c) Quy hoạch nón bậc hai (SOCP)**
- Hàm mục tiêu: chuẩn ($$\lVert Ax - b \rVert_2$$)
- Ràng buộc: ràng buộc chuẩn ($$\lVert x \rVert_2 \leq 1$$)
- Có thể biến đổi thành dạng chuẩn SOCP

**Bước 2: Điều kiện tính lồi**
- **a)** Luôn lồi (hàm tuyến tính)
- **b)** Lồi khi $$P \succeq 0$$ (nửa xác định dương)
- **c)** Luôn lồi (hàm chuẩn và ràng buộc chuẩn)

**Bước 3: Phương pháp giải**
- **a)** Phương pháp đơn hình (Simplex), phương pháp điểm trong
- **b)** Phương pháp tập hoạt động (Active set), phương pháp điểm trong
- **c)** Phương pháp điểm trong cho SOCP

</details>

---

## 📝 **Bài tập 2: Least squares và variants**

**Đề bài:** (Bài 1.2 từ Boyd & Vandenberghe)
Xét các bài toán least squares sau:

a) **Ordinary least squares:** $$\min_x \lVert Ax - b \rVert_2^2$$

b) **Weighted least squares:** $$\min_x (Ax - b)^T W (Ax - b)$$ với $$W \succ 0$$

c) **Regularized least squares:** $$\min_x \lVert Ax - b \rVert_2^2 + \lambda \lVert x \rVert_2^2$$

d) **Robust least squares:** $$\min_x \sum_{i=1}^m \phi((Ax - b)_i)$$ với $$\phi(u) = \begin{cases} u^2 & |u| \leq M \\ 2M|u| - M^2 & |u| > M \end{cases}$$

**Yêu cầu:**
1. Tìm nghiệm analytical cho các trường hợp a, b, c
2. Chứng minh tính convex của tất cả các bài toán
3. Phân tích ý nghĩa geometric của regularization
4. So sánh robustness của các methods

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Nghiệm analytical**

**a) Ordinary least squares:**
$$x^* = (A^T A)^{-1} A^T b$$ (nếu $$A^T A$$ invertible)

**b) Weighted least squares:**
$$x^* = (A^T W A)^{-1} A^T W b$$

**c) Regularized least squares (Ridge regression):**
$$x^* = (A^T A + \lambda I)^{-1} A^T b$$

**d) Robust least squares:**
Không có closed form, cần numerical methods.

**Bước 2: Chứng minh convexity**

**a-c)** Quadratic functions với positive definite Hessian
**d)** $$\phi(u)$$ là convex function (piecewise quadratic với non-decreasing derivative)

**Bước 3: Ý nghĩa hình học**
- **Regularization:** Co lại về gốc tọa độ, ngăn ngừa overfitting
- **$$\lambda$$** kiểm soát sự cân bằng giữa độ chệch và phương sai
- Tương đương với tiên nghiệm Bayesian $$x \sim \mathcal{N}(0, \sigma^2/\lambda I)$$

**Bước 4: So sánh tính bền vững**
- **OLS:** Nhạy cảm với ngoại lai (hàm phạt bậc hai)
- **Có trọng số:** Có thể giảm trọng số cho ngoại lai nếu chọn $$W$$ phù hợp  
- **Có regularization:** Giảm overfitting, cải thiện khả năng tổng quát hóa
- **Bền vững:** Hàm mất mát Huber giảm độ nhạy với ngoại lai

</details>

---

## 📝 **Bài tập 3: Linear programming trong standard form**

**Đề bài:** (Bài 1.3 từ Boyd & Vandenberghe)
Chuyển đổi các bài toán sau về LP standard form:

a) $$\min_{x,y} 2x + 3y \quad \text{s.t.} \quad x + 2y \geq 5, \quad x - y = 2, \quad x \geq 0, \quad y \text{ free}$$

b) $$\max_x c^T x \quad \text{s.t.} \quad Ax \leq b, \quad x \geq 0$$

c) $$\min_x \lVert c^T x - d \rVert_\infty \quad \text{s.t.} \quad Ax \leq b$$

**Yêu cầu:**
1. Chuyển về dạng $$\min c^T z \text{ s.t. } Az = b, z \geq 0$$
2. Xác định ma trận $$A$$, vector $$b, c$$ mới
3. Giải thích các phép biến đổi sử dụng
4. Verify tương đương của bài toán gốc và transformed

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Chuyển đổi bài toán a)**

**Xử lý biến tự do:** $$y = y^+ - y^-$$ với $$y^+, y^- \geq 0$$

**Xử lý bất đẳng thức:** $$x + 2y \geq 5 \Rightarrow x + 2y - s = 5$$ với $$s \geq 0$$

**Dạng chuẩn:**
$$\min_{x,y^+,y^-,s} 2x + 3y^+ - 3y^- \quad \text{s.t.} \quad \begin{bmatrix} 1 & 2 & -2 & -1 \\ 1 & -1 & 1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y^+ \\ y^- \\ s \end{bmatrix} = \begin{bmatrix} 5 \\ 2 \end{bmatrix}$$

với $$x, y^+, y^-, s \geq 0$$.

**Bước 2: Chuyển đổi bài toán b)**

**Chuyển max thành min:** $$\max c^T x = -\min (-c^T x)$$

**Chuyển bất đẳng thức thành đẳng thức:** $$Ax \leq b \Rightarrow Ax + s = b$$ với $$s \geq 0$$

**Dạng chuẩn:**
$$\min_{x,s} (-c^T x + 0^T s) \quad \text{s.t.} \quad [A \quad I] \begin{bmatrix} x \\ s \end{bmatrix} = b, \quad x,s \geq 0$$

**Bước 3: Chuyển đổi bài toán c)**

**Biến đổi chuẩn $$\ell_\infty$$:** $$\min t \text{ s.t. } -t \leq c^T x - d \leq t$$

**Dạng chuẩn:**
$$\min_{x,t,s_1,s_2} t \quad \text{s.t.} \quad \begin{bmatrix} A & 0 & I & 0 \\ c^T & -1 & 0 & I \\ -c^T & -1 & 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ t \\ s_1 \\ s_2 \end{bmatrix} = \begin{bmatrix} b \\ d \\ -d \end{bmatrix}$$

</details>

---

## 📝 **Bài tập 4: Quadratic programming applications**

**Đề bài:** (Bài 1.4 từ Boyd & Vandenberghe)
Xét bài toán portfolio optimization:

$$\min_x \frac{1}{2} x^T \Sigma x \quad \text{s.t.} \quad \mu^T x \geq r, \quad \mathbf{1}^T x = 1, \quad x \geq 0$$

với $$\Sigma \succ 0$$ (covariance matrix), $$\mu$$ (expected returns), $$r$$ (target return).

**Yêu cầu:**
1. Chứng minh đây là convex QP
2. Viết điều kiện KKT
3. Phân tích trường hợp không có constraint $$x \geq 0$$
4. Tìm efficient frontier
5. Implement numerical solution

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Chứng minh convexity**
- Objective: $$f(x) = \frac{1}{2} x^T \Sigma x$$ với $$\nabla^2 f = \Sigma \succ 0$$
- Constraints: tất cả đều linear
- $$\Rightarrow$$ Convex QP

**Bước 2: KKT conditions**
Lagrangian: $$L(x,\lambda,\nu,\mu) = \frac{1}{2} x^T \Sigma x - \lambda(\mu^T x - r) + \nu(\mathbf{1}^T x - 1) - \mu^T x$$

KKT conditions:
- Stationarity: $$\Sigma x - \lambda \mu + \nu \mathbf{1} - \mu = 0$$
- Primal feasibility: $$\mu^T x \geq r, \mathbf{1}^T x = 1, x \geq 0$$
- Dual feasibility: $$\lambda \geq 0, \mu \geq 0$$
- Complementary slackness: $$\lambda(\mu^T x - r) = 0, \mu_i x_i = 0$$

**Bước 3: Trường hợp unconstrained ($$x \geq 0$$)**
$$x^* = \Sigma^{-1}(\lambda^* \mu - \nu^* \mathbf{1})$$

Từ constraints:
- $$\mathbf{1}^T x^* = 1 \Rightarrow \mathbf{1}^T \Sigma^{-1}(\lambda^* \mu - \nu^* \mathbf{1}) = 1$$
- $$\mu^T x^* = r \Rightarrow \mu^T \Sigma^{-1}(\lambda^* \mu - \nu^* \mathbf{1}) = r$$

Giải hệ:
$$\begin{bmatrix} A & B \\ B & C \end{bmatrix} \begin{bmatrix} \lambda^* \\ -\nu^* \end{bmatrix} = \begin{bmatrix} r \\ 1 \end{bmatrix}$$

với $$A = \mu^T \Sigma^{-1} \mu, B = \mu^T \Sigma^{-1} \mathbf{1}, C = \mathbf{1}^T \Sigma^{-1} \mathbf{1}$$

**Bước 4: Biên hiệu quả**
$$\sigma^2(r) = \frac{Ar^2 - 2Br + C}{AC - B^2}$$

Đây là đường hyperbola trong không gian $$(r, \sigma)$$.

</details>

---

## 📝 **Bài tập 5: Geometric programming**

**Đề bài:** (Bài 1.5 từ Boyd & Vandenberghe)
Xét bài toán thiết kế mạch điện:

$$\min_{x,y,z} \frac{1}{xyz} \quad \text{s.t.} \quad \frac{x}{y} + \frac{y}{z} \leq 1, \quad x,y,z > 0$$

**Yêu cầu:**
1. Chứng minh đây là geometric program
2. Chuyển về convex form bằng log transformation
3. Solve bài toán convex
4. Interpret nghiệm trong context thiết kế mạch

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Verify geometric program**
- Objective: $$f_0(x,y,z) = x^{-1} y^{-1} z^{-1}$$ (monomial)
- Constraint: $$g_1(x,y,z) = x^1 y^{-1} z^0 + x^0 y^1 z^{-1}$$ (posynomial)
- Domain: $$x,y,z > 0$$

$$\Rightarrow$$ Đây là GP trong standard form.

**Bước 2: Biến đổi logarit**
Đặt $$u = \log x, v = \log y, w = \log z$$:

$$\min_{u,v,w} -u - v - w \quad \text{s.t.} \quad \log(e^{u-v} + e^{v-w}) \leq 0$$

Tương đương:
$$\min_{u,v,w} -u - v - w \quad \text{s.t.} \quad e^{u-v} + e^{v-w} \leq 1$$

**Bước 3: Công thức lồi**
$$\min_{u,v,w,t} -u - v - w \quad \text{s.t.} \quad e^{u-v} + e^{v-w} \leq t, \quad t \leq 1$$

Đây là bài toán lồi (ràng buộc log-sum-exp).

**Bước 4: Phương pháp giải**
Sử dụng phương pháp điểm trong hoặc các bộ giải GP chuyên dụng.

Nghiệm tối ưu sẽ có dạng:
- $$x^* = e^{u^*}, y^* = e^{v^*}, z^* = e^{w^*}$$
- Ràng buộc thường hoạt động: $$\frac{x^*}{y^*} + \frac{y^*}{z^*} = 1$$

</details>

---

## 📝 **Bài tập 6: Semidefinite programming basics**

**Đề bài:** (Bài 1.6 từ Boyd & Vandenberghe)
Xét bài toán:

$$\min_X \text{tr}(CX) \quad \text{s.t.} \quad \text{tr}(A_i X) = b_i, \quad i = 1,\ldots,m, \quad X \succeq 0$$

**Yêu cầu:**
1. Chứng minh đây là convex optimization problem
2. Viết dual problem
3. Phân tích điều kiện strong duality
4. Ví dụ cụ thể: Maximum cut relaxation

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Chứng minh convexity**
- Objective: $$\text{tr}(CX)$$ linear trong $$X$$
- Constraints: $$\text{tr}(A_i X) = b_i$$ linear
- Constraint: $$X \succeq 0$$ convex (positive semidefinite cone)

$$\Rightarrow$$ Convex SDP

**Bước 2: Dual problem**
Lagrangian: $$L(X,y,Z) = \text{tr}(CX) + \sum_{i=1}^m y_i (b_i - \text{tr}(A_i X)) - \text{tr}(ZX)$$

Dual function: $$g(y,Z) = \inf_X L(X,y,Z)$$

Điều kiện: $$C - \sum_{i=1}^m y_i A_i - Z = 0$$

**Dual problem:**
$$\max_{y,Z} \sum_{i=1}^m b_i y_i \quad \text{s.t.} \quad \sum_{i=1}^m y_i A_i + Z = C, \quad Z \succeq 0$$

**Bước 3: Strong duality**
Strong duality holds nếu Slater condition thỏa mãn:
$$\exists X \succ 0 \text{ s.t. } \text{tr}(A_i X) = b_i, \forall i$$

**Bước 4: Maximum cut example**
Cho graph $$G = (V,E)$$ với weights $$w_{ij}$$:

$$\max_x \sum_{(i,j) \in E} w_{ij} \frac{1 - x_i x_j}{2} \quad \text{s.t.} \quad x_i \in \{-1,1\}$$

**SDP relaxation:**
$$\max_X \sum_{(i,j) \in E} w_{ij} \frac{1 - X_{ij}}{2} \quad \text{s.t.} \quad X_{ii} = 1, \quad X \succeq 0$$

</details>

---

## 📝 **Bài tập 7: Robust optimization introduction**

**Đề bài:** (Bài 1.7 từ Boyd & Vandenberghe)
Xét robust linear program:

$$\min_x c^T x \quad \text{s.t.} \quad a_i^T x \leq b_i \quad \forall a_i \in \mathcal{U}_i, \quad i = 1,\ldots,m$$

với uncertainty sets:
a) Box: $$\mathcal{U}_i = \{a_i^{nom} + u : \lVert u \rVert_\infty \leq \rho_i\}$$
b) Ellipsoidal: $$\mathcal{U}_i = \{a_i^{nom} + P_i u : \lVert u \rVert_2 \leq 1\}$$

**Yêu cầu:**
1. Reformulate thành deterministic convex programs
2. So sánh computational complexity
3. Phân tích conservatism level
4. Implement và compare solutions

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Box uncertainty**
$$\max_{a_i \in \mathcal{U}_i} a_i^T x = (a_i^{nom})^T x + \rho_i \lVert x \rVert_1$$

**Deterministic equivalent:**
$$\min_x c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \rho_i \lVert x \rVert_1 \leq b_i$$

**LP reformulation:**
$$\min_{x,t_i} c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \rho_i \sum_j t_{ij} \leq b_i, \quad -t_{ij} \leq x_j \leq t_{ij}$$

**Bước 2: Ellipsoidal uncertainty**
$$\max_{a_i \in \mathcal{U}_i} a_i^T x = (a_i^{nom})^T x + \lVert P_i^T x \rVert_2$$

**Deterministic equivalent:**
$$\min_x c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \lVert P_i^T x \rVert_2 \leq b_i$$

Đây là Second-Order Cone Program (SOCP).

**Bước 3: So sánh độ phức tạp**
- **Box:** LP với $$O(mn)$$ biến và ràng buộc
- **Ellipsoidal:** SOCP với $$n + m$$ biến và $$m$$ ràng buộc SOC
- **Nominal:** LP với $$n$$ biến và $$m$$ ràng buộc

**Bước 4: Phân tích tính bảo thủ**
- **Box:** Bảo thủ nhất (trường hợp xấu nhất theo mọi hướng)
- **Ellipsoidal:** Bảo thủ vừa phải (bất định theo hướng)
- **Nominal:** Ít bảo thủ nhất (không có bất định)

Giá của tính bền vững = $$\frac{\text{Giá trị tối ưu bền vững}}{\text{Giá trị tối ưu danh nghĩa}} - 1$$

</details>

---

## 📝 **Bài tập 8: Convexity verification**

**Đề bài:** (Bài 1.8 từ Boyd & Vandenberghe)
Xác định tính convex của các functions sau:

a) $$f(x) = x \log x$$ trên $$\mathbb{R}_{++}$$
b) $$f(x) = -\log(\det X)$$ trên $$\mathbb{S}_{++}^n$$
c) $$f(x) = \lVert x \rVert_p$$ với $$p \geq 1$$
d) $$f(X) = \lambda_{\max}(X)$$ trên $$\mathbb{S}^n$$

**Yêu cầu:**
1. Chứng minh/phản chứng tính convex
2. Tính second-order conditions khi applicable
3. Verify bằng definition hoặc composition rules
4. Tìm domain convex của mỗi function

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: $$f(x) = x \log x$$**
**Domain:** $$\mathbb{R}_{++}$$ (convex)

**Second derivative:** $$f''(x) = \frac{1}{x} > 0$$ for $$x > 0$$

$$\Rightarrow$$ Convex trên $$\mathbb{R}_{++}$$

**Bước 2: $$f(X) = -\log(\det X)$$**
**Domain:** $$\mathbb{S}_{++}^n$$ (convex)

**Hessian:** Có thể chứng minh $$\nabla^2 f \succ 0$$

Alternative: $$-\log(\det X) = -\log(\prod_i \lambda_i) = -\sum_i \log \lambda_i$$

Vì $$-\log$$ convex và eigenvalues là concave functions của $$X$$, cần careful analysis.

**Result:** Convex trên $$\mathbb{S}_{++}^n$$

**Bước 3: $$f(x) = \lVert x \rVert_p$$**
**Domain:** $$\mathbb{R}^n$$ (convex)

**For $$p \geq 1$$:** Triangle inequality $$\Rightarrow$$ convex
**For $$0 < p < 1$$:** Not convex (subadditive but not convex)

**Verification:** Minkowski inequality for $$p \geq 1$$

**Bước 4: $$f(X) = \lambda_{\max}(X)$$**
**Domain:** $$\mathbb{S}^n$$ (convex)

**Convexity:** $$\lambda_{\max}(X) = \max_{\lVert v \rVert = 1} v^T X v$$

Maximum của linear functions $$\Rightarrow$$ convex

**Alternative:** Spectral norm property

</details>

---

## 📝 **Bài tập 9: Optimization modeling**

**Đề bài:** (Bài 1.9 từ Boyd & Vandenberghe)
Formulate các bài toán thực tế sau thành convex optimization:

a) **Antenna array design:** Minimize sidelobe level
b) **Filter design:** Minimize passband ripple và stopband energy  
c) **Truss design:** Minimize weight subject to stiffness constraints
d) **Data fitting:** Robust regression với outliers

**Yêu cầu:**
1. Mathematical formulation cho mỗi problem
2. Identify variables, objective, constraints
3. Verify convexity
4. Suggest solution approaches

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Antenna array design**
**Variables:** $$w \in \mathbb{C}^n$$ (array weights)

**Objective:** Minimize maximum sidelobe level
$$\min_{w,t} t \quad \text{s.t.} \quad |a(\theta)^H w| \leq t, \quad \forall \theta \in \Theta_{sidelobe}$$

với $$a(\theta)$$ là steering vector, $$\Theta_{sidelobe}$$ là sidelobe region.

**Main beam constraint:** $$a(\theta_0)^H w = 1$$ (normalization)

**Convex:** SOCP (second-order cone constraints)

**Bước 2: Filter design**
**Variables:** $$h \in \mathbb{R}^n$$ (filter coefficients)

**Passband ripple:** $$|H(\omega) - 1| \leq \delta_p, \quad \omega \in \Omega_p$$
**Stopband attenuation:** $$|H(\omega)| \leq \delta_s, \quad \omega \in \Omega_s$$

với $$H(\omega) = \sum_{k=0}^{n-1} h_k e^{-j\omega k}$$

**Convex formulation:**
$$\min_{h,\delta_p,\delta_s} \alpha \delta_p + \beta \delta_s$$
subject to frequency response constraints.

**Bước 3: Truss design**
**Variables:** $$A \in \mathbb{R}^m$$ (cross-sectional areas)

**Objective:** $$\min \sum_{i=1}^m \rho_i l_i A_i$$ (total weight)

**Stiffness constraint:** $$u^T K(A) u \geq u_{min}^T K_0 u_{min}$$

với $$K(A) = \sum_{i=1}^m A_i K_i$$ (stiffness matrix)

**Convex:** Linear objective, linear constraint trong $$A$$

**Bước 4: Robust regression**
**Variables:** $$\beta \in \mathbb{R}^p$$ (regression coefficients)

**Huber loss:** $$\min_\beta \sum_{i=1}^n \phi(y_i - x_i^T \beta)$$

với $$\phi(u) = \begin{cases} \frac{1}{2}u^2 & |u| \leq M \\ M|u| - \frac{1}{2}M^2 & |u| > M \end{cases}$$

**Convex:** Huber function là convex

</details>

---

## 📝 **Bài tập 10: Duality introduction**

**Đề bài:** (Bài 1.10 từ Boyd & Vandenberghe)
Cho bài toán LP:
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Yêu cầu:**
1. Derive dual problem bằng Lagrangian approach
2. Chứng minh weak duality
3. Tìm điều kiện strong duality
4. Interpret dual variables economically
5. Verify complementary slackness

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Lagrangian và dual**
$$L(x,\nu,\lambda) = c^T x + \nu^T(Ax - b) - \lambda^T x$$

**Dual function:**
$$g(\nu,\lambda) = \inf_x L(x,\nu,\lambda) = \inf_x (c + A^T \nu - \lambda)^T x - \nu^T b$$

**Điều kiện finite:** $$c + A^T \nu - \lambda = 0$$, i.e., $$\lambda = A^T \nu + c$$

**Dual problem:**
$$\max_{\nu,\lambda} g(\nu,\lambda) = \max_\nu -\nu^T b \quad \text{s.t.} \quad A^T \nu + c \geq 0$$

Tương đương:
$$\max_\nu b^T \nu \quad \text{s.t.} \quad A^T \nu \leq c$$

**Bước 2: Weak duality**
Với mọi primal feasible $$x$$ và dual feasible $$\nu$$:
$$c^T x \geq b^T \nu$$

**Proof:** 
$$c^T x \geq (A^T \nu)^T x = \nu^T Ax = \nu^T b = b^T \nu$$

**Bước 3: Strong duality**
Strong duality holds cho LP khi cả primal và dual đều feasible (fundamental theorem of LP).

**Bước 4: Economic interpretation**
- $$\nu_i$$: shadow price của resource $$i$$
- $$\nu_i$$ = marginal value của constraint $$i$$
- Nếu $$b_i$$ tăng 1 unit, optimal value tăng $$\nu_i$$

**Bước 5: Complementary slackness**
- Nếu $$x_j^* > 0$$, thì $$(A^T \nu^*)_j = c_j$$ (reduced cost = 0)
- Nếu $$(A^T \nu^*)_j < c_j$$, thì $$x_j^* = 0$$

</details>

---

## 💡 Mẹo Thực Hành

#### **Khi phân loại bài toán tối ưu hóa:**
- Kiểm tra dạng hàm mục tiêu (tuyến tính, bậc hai, tổng quát)
- Xác định loại ràng buộc (tuyến tính, bậc hai, nón)
- Xác minh tính lồi của từng thành phần

#### **Khi chuyển đổi về dạng chuẩn:**
- Xử lý biến tự do: $$x = x^+ - x^-$$
- Chuyển bất đẳng thức: thêm biến slack
- Chuyển max thành min: đổi dấu hàm mục tiêu

#### **Khi xác minh tính lồi:**
- Sử dụng điều kiện bậc hai khi có thể
- Áp dụng quy tắc kết hợp và các phép toán bảo toàn tính lồi
- Kiểm tra định nghĩa trực tiếp nếu cần

---

## 💡 **Tổng kết**

### **Phân loại Bài toán Tối ưu:**

| Loại | Hàm mục tiêu | Ràng buộc | Ví dụ |
|------|--------------|-----------|-------|
| **LP** | Tuyến tính | Tuyến tính | $$\min c^Tx$$, $$Ax \leq b$$ |
| **QP** | Bậc hai | Tuyến tính | $$\min \frac{1}{2}x^TQx + c^Tx$$ |
| **QCQP** | Bậc hai | Bậc hai | Portfolio với risk constraints |
| **SOCP** | Tuyến tính | Chuẩn $$\ell_2$$ | $$\|\|Ax-b\|\|_2 \leq c^Tx$$ |
| **SDP** | Tuyến tính | Ma trận PSD | $$\min \text{tr}(CX)$$, $$X \succeq 0$$ |

### **Least Squares Variants:**

| Method | Objective | Đặc điểm |
|--------|-----------|----------|
| Ordinary LS | $$\|\|Ax-b\|\|_2^2$$ | Nghiệm closed-form |
| Weighted LS | $$(Ax-b)^TW(Ax-b)$$ | Weights cho observations |
| Regularized LS | $$\|\|Ax-b\|\|_2^2 + \lambda\|\|x\|\|_2^2$$ | Ridge regression |
| Robust LS | $$\sum \phi((Ax-b)_i)$$ | Resistant to outliers |
| LASSO | $$\|\|Ax-b\|\|_2^2 + \lambda\|\|x\|\|_1$$ | Sparse solutions |

### **Duality Concepts:**

- **Weak duality:** $$d^* \leq p^*$$ (luôn đúng)
- **Strong duality:** $$d^* = p^*$$ (cần điều kiện, e.g., Slater)
- **Shadow price:** $$\nu_i^*$$ = marginal value của constraint $$i$$
- **Complementary slackness:** $$\lambda_i^* (g_i(x^*)) = 0$$

---

## 📚 Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 1: Introduction
   - Exercises 1.1-1.15

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization*. Springer.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming*. Athena Scientific.

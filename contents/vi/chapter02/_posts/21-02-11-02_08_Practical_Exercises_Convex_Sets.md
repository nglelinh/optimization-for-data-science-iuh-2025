---
layout: post
title: "2-8 Bài Tập Thực Hành - Tập Convex"
chapter: "2"
order: 9
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter02
lesson_type: required
---

# Bài Tập Thực Hành - Tập Convex

## **Bài tập 1: Verification of convex sets**

**Đề bài:** (Bài 2.1 từ Boyd & Vandenberghe)
Xác định tính convex của các tập hợp sau:

a) $$S_1 = \{x \in \mathbb{R}^n : \lVert x \rVert_2 \leq 1\}$$

b) $$S_2 = \{x \in \mathbb{R}^n : \lVert x \rVert_\infty \leq 1\}$$

c) $$S_3 = \{x \in \mathbb{R}^n : x^T P x \leq 1\}$$ với $$P \succeq 0$$

d) $$S_4 = \{x \in \mathbb{R}^n : \lVert x_i \rVert  \leq a_i, i = 1,\ldots,n\}$$

**Yêu cầu:**
1. Chứng minh tính convex bằng definition
2. Verify bằng operations preserving convexity
3. Visualize trong $$\mathbb{R}^2$$
4. Tìm extreme points của mỗi tập

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Chứng minh bằng definition**

**a) $$\ell_2$$ ball:** $$S_1 = \{x : \lVert x \rVert_2 \leq 1\}$$

Với $$x, y \in S_1$$ và $$\theta \in [0,1]$$:
$$\lVert \theta x + (1-\theta) y \rVert_2 \leq \theta \lVert x \rVert_2 + (1-\theta) \lVert y \rVert_2 \leq \theta \cdot 1 + (1-\theta) \cdot 1 = 1$$

$$\Rightarrow$$ Convex

**b) $$\ell_\infty$$ ball:** $$S_2 = \{x : \max_i |x_i| \leq 1\}$$

$$\max_i |\theta x_i + (1-\theta) y_i| \leq \max_i (\theta |x_i| + (1-\theta) |y_i|) \leq \theta \max_i |x_i| + (1-\theta) \max_i |y_i| \leq 1$$

$$\Rightarrow$$ Convex

**c) Ellipsoid:** $$S_3 = \{x : x^T P x \leq 1\}$$ với $$P \succeq 0$$

$$(\theta x + (1-\theta) y)^T P (\theta x + (1-\theta) y) = \theta^2 x^T P x + 2\theta(1-\theta) x^T P y + (1-\theta)^2 y^T P y$$

Vì $$P \succeq 0$$, quadratic form là convex function, nên sublevel set convex.

**d) Hyperrectangle:** $$S_4 = \prod_{i=1}^n [-a_i, a_i]$$

Cartesian product của convex sets (intervals) là convex.

**Bước 2: Các phép toán bảo toàn tính lồi**
- **a, b:** Tập mức dưới của hàm lồi (chuẩn)
- **c:** Tập mức dưới của dạng toàn phương lồi
- **d:** Tích Descartes của các khoảng lồi

**Bước 3: Điểm cực biên**
- **a:** Biên $$\{x : \lVert x \rVert_2 = 1\}$$ (vô số điểm cực biên)
- **b:** Các đỉnh $$\{\pm e_i : i = 1,\ldots,n\}$$ ($$2n$$ điểm cực biên)
- **c:** Phụ thuộc vào $$P$$; nếu $$P \succ 0$$, ellipse biên
- **d:** Các đỉnh $$\{(\pm a_1, \ldots, \pm a_n)\}$$ ($$2^n$$ điểm cực biên)

</details>

---

## **Bài tập 2: Operations preserving convexity**

**Đề bài:** (Bài 2.2 từ Boyd & Vandenberghe)
Cho các tập convex $$C_1, C_2 \subseteq \mathbb{R}^n$$. Chứng minh hoặc phản chứng tính convex của:

a) **Intersection:** $$C_1 \cap C_2$$

b) **Union:** $$C_1 \cup C_2$$

c) **Minkowski sum:** $$C_1 + C_2 = \{x + y : x \in C_1, y \in C_2\}$$

d) **Cartesian product:** $$C_1 \times C_2$$

e) **Affine transformation:** $$f(C_1) = \{Ax + b : x \in C_1\}$$

**Yêu cầu:**
1. Chứng minh mathematical cho các trường hợp đúng
2. Đưa ra counterexample cho các trường hợp sai
3. Visualize bằng examples cụ thể
4. Generalize cho arbitrary collections

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Giao - LỒI**

**Chứng minh:** Với $$x, y \in C_1 \cap C_2$$ và $$\theta \in [0,1]$$:
- $$x, y \in C_1 \Rightarrow \theta x + (1-\theta) y \in C_1$$ (vì $$C_1$$ lồi)
- $$x, y \in C_2 \Rightarrow \theta x + (1-\theta) y \in C_2$$ (vì $$C_2$$ lồi)
- $$\Rightarrow \theta x + (1-\theta) y \in C_1 \cap C_2$$

**Tổng quát hóa:** $$\bigcap_{i \in I} C_i$$ lồi nếu mỗi $$C_i$$ lồi.

**Bước 2: Hợp - KHÔNG LỒI**

**Phản ví dụ:** $$C_1 = \{(x,0) : x \geq 0\}$$, $$C_2 = \{(0,y) : y \geq 0\}$$

Cả hai đều lồi, nhưng $$C_1 \cup C_2$$ không lồi:
- $$(1,0) \in C_1 \cup C_2$$, $$(0,1) \in C_1 \cup C_2$$
- $$\frac{1}{2}(1,0) + \frac{1}{2}(0,1) = (\frac{1}{2}, \frac{1}{2}) \notin C_1 \cup C_2$$

**Bước 3: Tổng Minkowski - LỒI**

**Chứng minh:** Với $$z_1, z_2 \in C_1 + C_2$$:
- $$z_1 = x_1 + y_1$$, $$z_2 = x_2 + y_2$$ với $$x_i \in C_1, y_i \in C_2$$
- $$\theta z_1 + (1-\theta) z_2 = \theta(x_1 + y_1) + (1-\theta)(x_2 + y_2)$$
- $$= (\theta x_1 + (1-\theta) x_2) + (\theta y_1 + (1-\theta) y_2)$$
- $$\in C_1 + C_2$$ (vì $$C_1, C_2$$ lồi)

**Bước 4: Tích Descartes - LỒI**

**Chứng minh:** $$(x_1, y_1), (x_2, y_2) \in C_1 \times C_2$$:
$$\theta(x_1, y_1) + (1-\theta)(x_2, y_2) = (\theta x_1 + (1-\theta) x_2, \theta y_1 + (1-\theta) y_2) \in C_1 \times C_2$$

**Bước 5: Biến đổi affine - LỒI**

**Chứng minh:** Với $$z_1, z_2 \in f(C_1)$$:
- $$z_i = Ax_i + b$$ với $$x_i \in C_1$$
- $$\theta z_1 + (1-\theta) z_2 = A(\theta x_1 + (1-\theta) x_2) + b \in f(C_1)$$

</details>

---

## **Bài tập 3: Separating hyperplanes**

**Đề bài:** (Bài 2.3 từ Boyd & Vandenberghe)
Cho hai convex sets $$C, D \subset \mathbb{R}^n$$ disjoint ($$C \cap D = \emptyset$$).

a) Chứng minh tồn tại separating hyperplane
b) Tìm separating hyperplane cho:
   - $$C = \{x : \lVert x \rVert_2 \leq 1\}$$, $$D = \{x : \lVert x - (3,0) \rVert_2 \leq 1\}$$
   - $$C = \{x : x_1 + x_2 \leq 1, x_1, x_2 \geq 0\}$$, $$D = \{(2,2)\}$$

**Yêu cầu:**
1. Constructive proof của separating hyperplane theorem
2. Tính toán explicit cho examples
3. Visualize separation
4. Analyze case khi sets touch at boundary

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Separating hyperplane theorem**

**Theorem:** Nếu $$C, D$$ là convex sets disjoint, tồn tại $$a \neq 0$$ và $$b$$ sao cho:
$$a^T x \leq b \leq a^T y, \quad \forall x \in C, y \in D$$

**Constructive proof:**
1. Xét $$S = C - D = \{x - y : x \in C, y \in D\}$$ (convex)
2. $$0 \notin S$$ (vì $$C \cap D = \emptyset$$)
3. Tìm $$s^* \in S$$ closest to origin: $$s^* = \arg\min_{s \in S} \lVert s \rVert_2$$
4. Đặt $$a = s^*$$, $$b = \frac{1}{2} \lVert s^* \rVert_2^2$$

**Bước 2: Example 1 - Two balls**
$$C = \{x : \lVert x \rVert_2 \leq 1\}$$, $$D = \{x : \lVert x - (3,0) \rVert_2 \leq 1\}$$

**Geometric approach:** Centers tại $$(0,0)$$ và $$(3,0)$$, radii = 1.
Separating line vuông góc với line connecting centers.

**Solution:** $$a = (1,0)$$, $$b = 1.5$$
Hyperplane: $$x_1 = 1.5$$

**Verification:**
- $$\max_{x \in C} x_1 = 1 < 1.5$$
- $$\min_{x \in D} x_1 = 2 > 1.5$$

**Bước 3: Example 2 - Simplex và point**
$$C = \{x : x_1 + x_2 \leq 1, x_1, x_2 \geq 0\}$$, $$D = \{(2,2)\}$$

**Approach:** Tìm closest point trong $$C$$ to $$(2,2)$$.

**Optimization problem:**
$$\min_{x \in C} \lVert x - (2,2) \rVert_2^2$$

**KKT conditions:** Closest point là $$(1,0)$$ hoặc $$(0,1)$$.

**Solution:** $$a = (1,1)$$, $$b = 1.5$$
Hyperplane: $$x_1 + x_2 = 1.5$$

</details>

---

## **Bài tập 4: Convex hull computations**

**Đề bài:** (Bài 2.4 từ Boyd & Vandenberghe)
Tính convex hull của các tập hợp sau:

a) $$S_1 = \{(0,0), (1,0), (0,1), (1,1)\}$$ trong $$\mathbb{R}^2$$

b) $$S_2 = \{x \in \mathbb{R}^3 : \lVert x \rVert_2 = 1, x_3 = 0\} \cup \{(0,0,1), (0,0,-1)\}$$

c) $$S_3 = \{(t, t^2) : t \in [-1,1]\}$$ trong $$\mathbb{R}^2$$

**Yêu cầu:**
1. Tính convex hull explicitly
2. Identify extreme points
3. Describe bằng inequalities khi possible
4. Visualize results

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Finite point set**
$$S_1 = \{(0,0), (1,0), (0,1), (1,1)\}$$

**Convex hull:** Unit square $$[0,1] \times [0,1]$$

**Extreme points:** Tất cả 4 points đều là extreme points.

**Inequality description:**
$$\text{conv}(S_1) = \{x : 0 \leq x_1 \leq 1, 0 \leq x_2 \leq 1\}$$

**Bước 2: Circle plus two points**
$$S_2 = \{x \in \mathbb{R}^3 : x_1^2 + x_2^2 = 1, x_3 = 0\} \cup \{(0,0,1), (0,0,-1)\}$$

**Convex hull:** Double cone
$$\text{conv}(S_2) = \{x \in \mathbb{R}^3 : x_1^2 + x_2^2 \leq (1 - |x_3|)^2, |x_3| \leq 1\}$$

**Extreme points:** Circle $$\{x : x_1^2 + x_2^2 = 1, x_3 = 0\}$$

**Bước 3: Parabola segment**
$$S_3 = \{(t, t^2) : t \in [-1,1]\}$$

**Convex hull:** Region below parabola
$$\text{conv}(S_3) = \{(x_1, x_2) : x_2 \geq x_1^2, |x_1| \leq 1\}$$

**Extreme points:** 
- $$(1,1)$$ và $$(-1,1)$$ (endpoints)
- Entire parabolic arc forms boundary

**Alternative description:**
$$\text{conv}(S_3) = \{(x_1, x_2) : x_2 \geq x_1^2, -1 \leq x_1 \leq 1\}$$

</details>

---

## **Bài tập 5: Dual cones**

**Đề bài:** (Bài 2.5 từ Boyd & Vandenberghe)
Tìm dual cone của các cones sau:

a) $$K_1 = \mathbb{R}_+^n = \{x \in \mathbb{R}^n : x_i \geq 0, \forall i\}$$

b) $$K_2 = \{x \in \mathbb{R}^n : \lVert x \rVert_2 \leq x_n\}$$ (second-order cone)

c) $$K_3 = \{x \in \mathbb{R}^n : \sum_{i=1}^{n-1} |x_i| \leq x_n\}$$ ($$\ell_1$$ cone)

d) $$K_4 = \{X \in \mathbb{S}^n : X \succeq 0\}$$ (positive semidefinite cone)

**Yêu cầu:**
1. Tính dual cone $$K^* = \{y : y^T x \geq 0, \forall x \in K\}$$
2. Verify self-duality khi applicable
3. Establish duality relationships
4. Geometric interpretation

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Non-negative orthant**
$$K_1^* = \{y : y^T x \geq 0, \forall x \in \mathbb{R}_+^n\}$$

**Analysis:** $$y^T x = \sum_{i=1}^n y_i x_i \geq 0$$ for all $$x_i \geq 0$$

$$\Rightarrow y_i \geq 0, \forall i$$

**Result:** $$K_1^* = \mathbb{R}_+^n = K_1$$ (self-dual)

**Bước 2: Second-order cone**
$$K_2 = \{x : \lVert (x_1, \ldots, x_{n-1}) \rVert_2 \leq x_n\}$$

**Dual:** $$K_2^* = \{y : y^T x \geq 0, \forall x \in K_2\}$$

**Result:** $$K_2^* = K_2$$ (self-dual)

**Proof sketch:** Sử dụng Cauchy-Schwarz inequality và homogeneity.

**Bước 3: $$\ell_1$$ cone**
$$K_3 = \{x : \sum_{i=1}^{n-1} |x_i| \leq x_n\}$$

**Dual:** $$K_3^* = \{y : \lVert (y_1, \ldots, y_{n-1}) \rVert_\infty \leq y_n\}$$

**Verification:** Sử dụng duality giữa $$\ell_1$$ và $$\ell_\infty$$ norms.

**Bước 4: PSD cone**
$$K_4 = \{X \in \mathbb{S}^n : X \succeq 0\}$$

**Dual:** $$K_4^* = \{Y \in \mathbb{S}^n : \text{tr}(YX) \geq 0, \forall X \succeq 0\}$$

**Result:** $$K_4^* = K_4$$ (self-dual)

**Proof:** $$Y \succeq 0 \Leftrightarrow \text{tr}(YX) \geq 0, \forall X \succeq 0$$

</details>

---

## **Bài tập 6: Projection onto convex sets**

**Đề bài:** (Bài 2.6 từ Boyd & Vandenberghe)
Tính projection của point $$x_0$$ onto convex set $$C$$:

$$\text{proj}_C(x_0) = \arg\min_{x \in C} \lVert x - x_0 \rVert_2$$

a) $$C = \{x : a^T x = b\}$$ (hyperplane)

b) $$C = \{x : a^T x \leq b\}$$ (halfspace)  

c) $$C = \{x : \lVert x \rVert_2 \leq r\}$$ ($$\ell_2$$ ball)

d) $$C = \{x : \lVert x \rVert_\infty \leq r\}$$ ($$\ell_\infty$$ ball)

**Yêu cầu:**
1. Derive closed-form solutions
2. Verify optimality conditions
3. Analyze uniqueness
4. Implement algorithms

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Projection onto hyperplane**
$$C = \{x : a^T x = b\}$$

**Lagrangian:** $$L(x,\lambda) = \frac{1}{2}\lVert x - x_0 \rVert_2^2 + \lambda(a^T x - b)$$

**Optimality:** $$x - x_0 + \lambda a = 0 \Rightarrow x = x_0 - \lambda a$$

**Constraint:** $$a^T(x_0 - \lambda a) = b \Rightarrow \lambda = \frac{a^T x_0 - b}{\lVert a \rVert_2^2}$$

**Solution:** $$\text{proj}_C(x_0) = x_0 - \frac{a^T x_0 - b}{\lVert a \rVert_2^2} a$$

**Bước 2: Projection onto halfspace**
$$C = \{x : a^T x \leq b\}$$

**Case analysis:**
- If $$a^T x_0 \leq b$$: $$\text{proj}_C(x_0) = x_0$$
- If $$a^T x_0 > b$$: project onto boundary hyperplane

**Solution:** 
$$\text{proj}_C(x_0) = \begin{cases} 
x_0 & \text{if } a^T x_0 \leq b \\
x_0 - \frac{a^T x_0 - b}{\lVert a \rVert_2^2} a & \text{if } a^T x_0 > b
\end{cases}$$

**Bước 3: Projection onto $$\ell_2$$ ball**
$$C = \{x : \lVert x \rVert_2 \leq r\}$$

**Case analysis:**
- If $$\lVert x_0 \rVert_2 \leq r$$: $$\text{proj}_C(x_0) = x_0$$
- If $$\lVert x_0 \rVert_2 > r$$: project radially

**Solution:**
$$\text{proj}_C(x_0) = \begin{cases}
x_0 & \text{if } \lVert x_0 \rVert_2 \leq r \\
r \frac{x_0}{\lVert x_0 \rVert_2} & \text{if } \lVert x_0 \rVert_2 > r
\end{cases}$$

**Bước 4: Projection onto $$\ell_\infty$$ ball**
$$C = \{x : \lVert x \rVert_\infty \leq r\}$$

**Component-wise projection:**
$$[\text{proj}_C(x_0)]_i = \begin{cases}
x_{0i} & \text{if } |x_{0i}| \leq r \\
r \cdot \text{sign}(x_{0i}) & \text{if } |x_{0i}| > r
\end{cases}$$

**Equivalently:** $$\text{proj}_C(x_0) = \text{clip}(x_0, -r, r)$$

</details>

---

## **Bài tập 7: Extreme points và vertices**

**Đề bài:** (Bài 2.7 từ Boyd & Vandenberghe)
Cho polytope $$P = \{x : Ax \leq b\}$$ trong $$\mathbb{R}^n$$.

a) Chứng minh $$x$$ là extreme point khi và chỉ khi $$n$$ constraints active tại $$x$$

b) Tìm tất cả extreme points của:
   - $$P_1 = \{x \in \mathbb{R}^2 : x_1 + x_2 \leq 1, x_1 \geq 0, x_2 \geq 0\}$$
   - $$P_2 = \{x \in \mathbb{R}^3 : x_1 + x_2 + x_3 \leq 1, x_i \geq 0\}$$

c) Verify Krein-Milman theorem: $$P = \text{conv}(\text{extreme points})$$

**Yêu cầu:**
1. Rigorous proof của characterization
2. Systematic enumeration của vertices
3. Geometric visualization
4. Computational algorithms

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Characterization theorem**

**Theorem:** $$x \in P$$ là extreme point $$\Leftrightarrow$$ $$n$$ linearly independent constraints active tại $$x$$.

**Proof ($$\Leftarrow$$):** Giả sử $$n$$ constraints active: $$A_I x = b_I$$ với $$A_I$$ full rank.

Nếu $$x = \theta y + (1-\theta) z$$ với $$y, z \in P$$, $$\theta \in (0,1)$$:
- $$A_I y \leq b_I$$ và $$A_I z \leq b_I$$
- $$b_I = A_I x = \theta A_I y + (1-\theta) A_I z \leq b_I$$
- $$\Rightarrow A_I y = A_I z = b_I$$
- Vì $$A_I$$ full rank: $$y = z = x$$

**Proof ($$\Rightarrow$$):** Contrapositive - nếu $$< n$$ constraints active, thì không extreme.

**Bước 2: Example 1 - 2D simplex**
$$P_1 = \{x : x_1 + x_2 \leq 1, x_1 \geq 0, x_2 \geq 0\}$$

**Active constraint combinations:**
- $$\{x_1 = 0, x_2 = 0\}$$: vertex $$(0,0)$$
- $$\{x_1 = 0, x_1 + x_2 = 1\}$$: vertex $$(0,1)$$  
- $$\{x_2 = 0, x_1 + x_2 = 1\}$$: vertex $$(1,0)$$

**Extreme points:** $$\{(0,0), (0,1), (1,0)\}$$

**Bước 3: Example 2 - 3D simplex**
$$P_2 = \{x : x_1 + x_2 + x_3 \leq 1, x_1, x_2, x_3 \geq 0\}$$

**Systematic enumeration:** Choose 3 from 4 constraints.

**Extreme points:**
- $$(0,0,0)$$: $$\{x_1 = 0, x_2 = 0, x_3 = 0\}$$
- $$(1,0,0)$$: $$\{x_2 = 0, x_3 = 0, x_1 + x_2 + x_3 = 1\}$$
- $$(0,1,0)$$: $$\{x_1 = 0, x_3 = 0, x_1 + x_2 + x_3 = 1\}$$
- $$(0,0,1)$$: $$\{x_1 = 0, x_2 = 0, x_1 + x_2 + x_3 = 1\}$$

**Bước 4: Krein-Milman verification**
$$P_1 = \text{conv}\{(0,0), (0,1), (1,0)\}$$
$$P_2 = \text{conv}\{(0,0,0), (1,0,0), (0,1,0), (0,0,1)\}$$

</details>

---

## **Bài tập 8: Generalized inequalities**

**Đề bài:** (Bài 2.8 từ Boyd & Vandenberghe)
Cho proper cone $$K \subseteq \mathbb{R}^n$$ và generalized inequality $$\preceq_K$$.

a) Verify các properties của $$\preceq_K$$:
   - Reflexive: $$x \preceq_K x$$
   - Antisymmetric: $$x \preceq_K y, y \preceq_K x \Rightarrow x = y$$
   - Transitive: $$x \preceq_K y, y \preceq_K z \Rightarrow x \preceq_K z$$

b) Cho $$K = \mathbb{S}_+^n$$, verify:
   - $$A \preceq B \Rightarrow A + C \preceq B + C$$
   - $$A \preceq B, C \succeq 0 \Rightarrow CAC \preceq CBC$$

**Yêu cầu:**
1. Rigorous proofs của properties
2. Counterexamples cho improper cones
3. Applications trong optimization
4. Dual cone relationships

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Properties của generalized inequality**

**Definition:** $$x \preceq_K y \Leftrightarrow y - x \in K$$

**Reflexive:** $$x \preceq_K x \Leftrightarrow x - x = 0 \in K$$
- True vì $$K$$ là cone (chứa 0)

**Antisymmetric:** $$x \preceq_K y, y \preceq_K x$$
- $$\Rightarrow y - x \in K$$ và $$x - y \in K$$
- $$\Rightarrow y - x \in K \cap (-K)$$
- Vì $$K$$ pointed: $$K \cap (-K) = \{0\}$$
- $$\Rightarrow y - x = 0 \Rightarrow x = y$$

**Transitive:** $$x \preceq_K y, y \preceq_K z$$
- $$\Rightarrow y - x \in K, z - y \in K$$
- $$\Rightarrow z - x = (z - y) + (y - x) \in K + K = K$$
- $$\Rightarrow x \preceq_K z$$

**Bước 2: Matrix inequalities**

**Property 1:** $$A \preceq B \Rightarrow A + C \preceq B + C$$

**Proof:** 
- $$A \preceq B \Rightarrow B - A \succeq 0$$
- $$(B + C) - (A + C) = B - A \succeq 0$$
- $$\Rightarrow A + C \preceq B + C$$

**Property 2:** $$A \preceq B, C \succeq 0 \Rightarrow CAC \preceq CBC$$

**Proof:**
- $$B - A \succeq 0$$ và $$C \succeq 0$$
- For any $$x$$: $$x^T(B - A)x \geq 0$$
- Let $$y = Cx$$: $$y^T C^{-1}(B - A)C^{-1} y \geq 0$$
- $$\Rightarrow C^{-1}(B - A)C^{-1} \succeq 0$$
- $$\Rightarrow CBC - CAC \succeq 0$$
- $$\Rightarrow CAC \preceq CBC$$

**Bước 3: Counterexample cho improper cone**

**Non-pointed cone:** $$K = \{x \in \mathbb{R}^2 : x_1 = 0\}$$
- $$K \cap (-K) = K \neq \{0\}$$
- Antisymmetric property fails

**Non-solid cone:** $$K = \mathbb{R}_+ \times \{0\} \subset \mathbb{R}^2$$
- Interior empty
- Strict inequality không well-defined

</details>

---

## **Bài tập 9: Convex combinations và Carathéodory theorem**

**Đề bài:** (Bài 2.9 từ Boyd & Vandenberghe)
a) Chứng minh Carathéodory theorem: Mọi point trong $$\text{conv}(S)$$ có thể biểu diễn bằng convex combination của tối đa $$n+1$$ points từ $$S$$.

b) Apply cho:
   - $$S = \{(1,0), (0,1), (-1,0), (0,-1)\}$$ trong $$\mathbb{R}^2$$
   - $$S = \{e_i : i = 1,\ldots,n\} \cup \{0\}$$ trong $$\mathbb{R}^n$$

c) Construct algorithm để find minimal representation

**Yêu cầu:**
1. Complete proof của Carathéodory theorem
2. Explicit computations cho examples
3. Algorithmic implementation
4. Geometric interpretation

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Carathéodory theorem proof**

**Theorem:** Nếu $$x \in \text{conv}(S)$$, thì $$x$$ có thể viết thành:
$$x = \sum_{i=1}^{n+1} \lambda_i x_i$$
với $$x_i \in S$$, $$\lambda_i \geq 0$$, $$\sum \lambda_i = 1$$.

**Proof:** 
1. Giả sử $$x = \sum_{i=1}^k \lambda_i x_i$$ với $$k > n+1$$
2. Vectors $$\{x_1 - x_k, \ldots, x_{k-1} - x_k\}$$ linearly dependent trong $$\mathbb{R}^n$$
3. Tồn tại $$\mu_i$$ không đồng thời bằng 0: $$\sum_{i=1}^{k-1} \mu_i (x_i - x_k) = 0$$
4. Đặt $$\mu_k = -\sum_{i=1}^{k-1} \mu_i$$, ta có $$\sum_{i=1}^k \mu_i x_i = 0$$
5. $$x = \sum_{i=1}^k (\lambda_i - t\mu_i) x_i$$ for any $$t$$
6. Choose $$t$$ để một coefficient bằng 0, giảm $$k$$

**Bước 2: Example 1 - Square vertices**
$$S = \{(1,0), (0,1), (-1,0), (0,-1)\}$$

**Convex hull:** Diamond/square rotated 45°

**Carathéodory bound:** $$n+1 = 3$$ points sufficient

**Example point:** $$(0,0) = \frac{1}{4}(1,0) + \frac{1}{4}(0,1) + \frac{1}{4}(-1,0) + \frac{1}{4}(0,-1)$$

**Minimal representation:** $$(0,0) = \frac{1}{2}(1,0) + \frac{1}{2}(-1,0)$$ (2 points)

**Bước 3: Example 2 - Standard basis**
$$S = \{e_1, \ldots, e_n, 0\}$$

**Convex hull:** Standard simplex $$\{x : \sum x_i \leq 1, x_i \geq 0\}$$

**Any point:** $$x = \sum_{i=1}^n x_i e_i + (1 - \sum x_i) \cdot 0$$

**Carathéodory:** At most $$n+1$$ points needed (already achieved)

**Bước 4: Minimal representation algorithm**

```
Algorithm: Minimal Convex Combination
Input: Point x, set S
Output: Minimal convex combination

1. Find any representation x = Σ λᵢ xᵢ
2. While |active set| > n+1:
   a. Solve Σ μᵢ xᵢ = 0 with some μᵢ ≠ 0
   b. Find t = max{λᵢ/μᵢ : μᵢ > 0}
   c. Update λᵢ ← λᵢ - t μᵢ
   d. Remove zero coefficients
3. Return minimal representation
```

</details>

---

## **Bài tập 10: Facial structure của convex sets**

**Đề bài:** (Bài 2.10 từ Boyd & Vandenberghe)
Cho convex set $$C$$ và supporting hyperplane $$H = \{x : a^T x = \alpha\}$$ với $$\sup_{x \in C} a^T x = \alpha$$.

a) Chứng minh $$F = C \cap H$$ là face của $$C$$

b) Classify faces của:
   - Unit cube $$[0,1]^n$$
   - Unit simplex $$\{x : \sum x_i \leq 1, x_i \geq 0\}$$
   - $$\ell_2$$ ball $$\{x : \lVert x \rVert_2 \leq 1\}$$

c) Establish face lattice structure

**Yêu cầu:**
1. Rigorous proof của face property
2. Complete enumeration cho examples
3. Dimension analysis
4. Lattice structure visualization

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bước 1: Face characterization**

**Definition:** $$F$$ là face của $$C$$ nếu:
- $$F \subseteq C$$
- $$F$$ convex
- Nếu $$x \in F$$ và $$x = \theta y + (1-\theta) z$$ với $$y, z \in C$$, $$\theta \in (0,1)$$, thì $$y, z \in F$$

**Theorem:** $$F = C \cap H$$ với $$H$$ supporting hyperplane là face.

**Proof:** 
1. $$F \subseteq C$$ (by definition)
2. $$F$$ convex (intersection của convex sets)
3. Nếu $$x \in F$$, $$x = \theta y + (1-\theta) z$$, $$y, z \in C$$:
   - $$\alpha = a^T x = \theta a^T y + (1-\theta) a^T z$$
   - $$a^T y, a^T z \leq \alpha$$ (vì $$y, z \in C$$)
   - $$\Rightarrow a^T y = a^T z = \alpha$$
   - $$\Rightarrow y, z \in F$$

**Bước 2: Unit cube faces**
$$C = [0,1]^n$$

**Face enumeration:**
- **Dimension 0:** $$2^n$$ vertices $$\{0,1\}^n$$
- **Dimension 1:** $$n \cdot 2^{n-1}$$ edges
- **Dimension $$k$$:** Faces obtained by fixing $$n-k$$ coordinates to $$\{0,1\}$$
- **Dimension $$n-1$$:** $$2n$$ facets $$\{x_i = 0\}$$, $$\{x_i = 1\}$$
- **Dimension $$n$$:** $$C$$ itself

**Total faces:** $$3^n$$ (each coordinate can be free, 0, or 1)

**Bước 3: Unit simplex faces**
$$C = \{x : \sum x_i \leq 1, x_i \geq 0\}$$

**Face structure:**
- **Vertices:** $$\{0, e_1, \ldots, e_n\}$$ ($$n+1$$ vertices)
- **Edges:** Connect vertices
- **Facets:** $$\{x_i = 0\}$$ và $$\{\sum x_i = 1\}$$
- **General faces:** Obtained by setting subset of coordinates to 0

**Bước 4: $$\ell_2$$ ball faces**
$$C = \{x : \lVert x \rVert_2 \leq 1\}$$

**Face structure:**
- **Dimension 0:** Origin $$\{0\}$$ (unique vertex)
- **Dimension $$n-1$$:** Boundary sphere $$\{x : \lVert x \rVert_2 = 1\}$$
- **Dimension $$n$$:** $$C$$ itself
- **No other faces:** Smooth boundary

**Lattice structure:** Linear lattice $$\{0\} \subset \partial C \subset C$$

</details>

---

## Mẹo Thực Hành

#### **Khi verify tính convex:**
- Sử dụng definition trực tiếp: $$\theta x + (1-\theta) y \in C$$
- Áp dụng operations preserving convexity
- Kiểm tra sublevel sets của convex functions

#### **Khi tính convex hull:**
- Identify extreme points trước
- Sử dụng Carathéodory theorem để giảm complexity
- Verify bằng supporting hyperplanes

#### **Khi work với dual cones:**
- Nhớ definition: $$K^* = \{y : y^T x \geq 0, \forall x \in K\}$$
- Exploit self-duality của important cones
- Sử dụng trong generalized inequalities

---

## **Tổng kết**

### **Các Tập Convex Quan trọng:**

| Tập | Định nghĩa | Ví dụ |
|-----|------------|-------|
| **Affine set** | $$\{x : Ax = b\}$$ | Không gian con, hyperplane |
| **Convex hull** | $$\text{conv}(S) = \{\sum \theta_i x_i : \sum \theta_i = 1, \theta_i \geq 0\}$$ | Smallest convex set chứa $$S$$ |
| **Cone** | $$\theta x \in C$$ $$\forall x \in C, \theta \geq 0$$ | Nonnegative orthant |
| **Polyhedron** | $$\{x : Ax \leq b, Cx = d\}$$ | Intersection của halfspaces |
| **Ellipsoid** | $$\{x : (x-x_c)^TP^{-1}(x-x_c) \leq 1\}$$ | $$P \succ 0$$ |
| **Norm ball** | $$\{x : \|\|x - x_c\|\| \leq r\}$$ | $$\ell_1, \ell_2, \ell_\infty$$ balls |

### **Operations bảo toàn Convexity:**

| Operation | Ví dụ |
|-----------|-------|
| **Intersection** | $$C_1 \cap C_2$$ convex nếu $$C_1, C_2$$ convex |
| **Affine map** | $$f(C) = \{Ax + b : x \in C\}$$ |
| **Perspective** | $$P(x, t) = x/t$$ |
| **Linear fractional** | $$f(x) = \frac{Ax + b}{c^Tx + d}$$ |

### **Separation & Support:**

- **Separating hyperplane:** Tồn tại $$a$$ sao cho $$a^Tx \leq b$$ $$\forall x \in C_1$$ và $$a^Tx \geq b$$ $$\forall x \in C_2$$
- **Supporting hyperplane:** $$\{x : a^Tx = a^Tx_0\}$$ tại boundary point $$x_0$$
- **Dual cone:** $$K^* = \{y : y^Tx \geq 0, \forall x \in K\}$$
- **Self-dual cones:** $$K^* = K$$ (e.g., nonnegative orthant, PSD cone)

### **Key Theorems:**

- **Carathéodory:** Mọi điểm trong $$\text{conv}(S) \subset \mathbb{R}^n$$ là combination của $$\leq n+1$$ points
- **Radon:** Mọi tập $$n+2$$ points trong $$\mathbb{R}^n$$ có thể partition thành 2 disjoint sets với convex hulls giao nhau
- **Helly:** Nếu $$C_1, \ldots, C_m$$ convex trong $$\mathbb{R}^n$$ ($$m \geq n+1$$), và mọi $$n+1$$ sets có intersection, thì $$\bigcap_{i=1}^m C_i \neq \emptyset$$

---

## Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 2: Convex Sets
   - Exercises 2.1-2.27

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Ziegler, G. M.** (1995). *Lectures on Polytopes*. Springer-Verlag.

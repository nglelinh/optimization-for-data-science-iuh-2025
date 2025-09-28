---
layout: post
title: 3-9 Bài Tập Thực Hành - Hàm Convex
chapter: '3'
order: 10
owner: GitHub Copilot
lang: vi
categories:
- chapter03
lesson_type: required
---

# Bài Tập Thực Hành - Hàm Convex

## 📝 **Bài tập 1: Verification of convex functions**

**Đề bài:** (Bài 3.1 từ Boyd & Vandenberghe)
Xác định tính convex của các hàm sau trên domain tương ứng:

a) $$f(x) = x^2$$ trên $$\mathbb{R}$$

b) $$f(x) = e^{ax}$$ trên $$\mathbb{R}$$

c) $$f(x) = x \log x$$ trên $$\mathbb{R}_{++}$$

d) $$f(x) = -\log x$$ trên $$\mathbb{R}_{++}$$

e) $$f(x) = x^p$$ với $$p \geq 1$$ trên $$\mathbb{R}_+$$

f) $$f(x) = |x|^p$$ với $$p \geq 1$$ trên $$\mathbb{R}$$

**Yêu cầu:**
1. Verify bằng definition của convexity
2. Sử dụng second-order conditions khi applicable
3. Analyze domain restrictions
4. Visualize functions và convexity

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: $$f(x) = x^2$$**

**Second-order condition:** $$f''(x) = 2 > 0$$ $$\forall x \in \mathbb{R}$$

$$\Rightarrow$$ Strictly convex trên $$\mathbb{R}$$

**Definition verification:** 
$$f(\theta x + (1-\theta) y) = (\theta x + (1-\theta) y)^2 = \theta^2 x^2 + 2\theta(1-\theta)xy + (1-\theta)^2 y^2$$

$$\theta f(x) + (1-\theta) f(y) = \theta x^2 + (1-\theta) y^2$$

$$f(\theta x + (1-\theta) y) - [\theta f(x) + (1-\theta) f(y)] = -\theta(1-\theta)(x-y)^2 \leq 0$$

**Bước 2: $$f(x) = e^{ax}$$**

**Second-order condition:** $$f''(x) = a^2 e^{ax} \geq 0$$ $$\forall x$$

$$\Rightarrow$$ Convex trên $$\mathbb{R}$$ (strictly convex nếu $$a \neq 0$$)

**Bước 3: $$f(x) = x \log x$$**

**Domain:** $$\mathbb{R}_{++}$$ ($$x > 0$$)

**First derivative:** $$f'(x) = \log x + 1$$

**Second derivative:** $$f''(x) = \frac{1}{x} > 0$$ for $$x > 0$$

$$\Rightarrow$$ Strictly convex trên $$\mathbb{R}_{++}$$

**Bước 4: $$f(x) = -\log x$$**

**Second derivative:** $$f''(x) = \frac{1}{x^2} > 0$$ for $$x > 0$$

$$\Rightarrow$$ Strictly convex trên $$\mathbb{R}_{++}$$

**Bước 5: $$f(x) = x^p$$ với $$p \geq 1$$**

**Case $$p = 1$$:** $$f(x) = x$$ linear $$\Rightarrow$$ convex

**Case $$p > 1$$:** $$f''(x) = p(p-1)x^{p-2} \geq 0$$ for $$x \geq 0$$

$$\Rightarrow$$ Convex trên $$\mathbb{R}_+$$

**Bước 6: $$f(x) = |x|^p$$ với $$p \geq 1$$**

**Symmetry:** $$f(-x) = f(x)$$, chỉ cần xét $$x \geq 0$$

**For $$x \geq 0$$:** $$f(x) = x^p$$ convex (từ bước 5)

**For $$x < 0$$:** $$f(x) = |x|^p = (-x)^p$$ cũng convex

**Tại $$x = 0$$:** Subdifferential analysis shows convexity

$$\Rightarrow$$ Convex trên $$\mathbb{R}$$

</details>

---

## 📝 **Bài tập 2: Operations preserving convexity**

**Đề bài:** (Bài 3.2 từ Boyd & Vandenberghe)
Cho các hàm convex $$f, g: \mathbb{R}^n \to \mathbb{R}$$. Xác định tính convex của:

a) $$h(x) = \alpha f(x) + \beta g(x)$$ với $$\alpha, \beta \geq 0$$

b) $$h(x) = \max\{f(x), g(x)\}$$

c) $$h(x) = f(Ax + b)$$ với $$A \in \mathbb{R}^{n \times m}$$, $$b \in \mathbb{R}^n$$

d) $$h(x) = \inf_{y \in C} f(x, y)$$ với $$C$$ convex

e) $$h(x) = \int_0^\infty f(x, t) dt$$ (nếu integral tồn tại)

**Yêu cầu:**
1. Chứng minh tính convex cho các operations
2. Đưa ra counterexamples khi không convex
3. Provide concrete examples
4. Discuss conditions for strict convexity

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Non-negative weighted sum - CONVEX**

**Theorem:** Nếu $$f, g$$ convex và $$\alpha, \beta \geq 0$$, thì $$h(x) = \alpha f(x) + \beta g(x)$$ convex.

**Proof:**
$$h(\theta x + (1-\theta) y) = \alpha f(\theta x + (1-\theta) y) + \beta g(\theta x + (1-\theta) y)$$
$$\leq \alpha[\theta f(x) + (1-\theta) f(y)] + \beta[\theta g(x) + (1-\theta) g(y)]$$
$$= \theta[\alpha f(x) + \beta g(x)] + (1-\theta)[\alpha f(y) + \beta g(y)]$$
$$= \theta h(x) + (1-\theta) h(y)$$

**Bước 2: Pointwise maximum - CONVEX**

**Theorem:** $$h(x) = \max\{f(x), g(x)\}$$ convex nếu $$f, g$$ convex.

**Proof:**
$$h(\theta x + (1-\theta) y) = \max\{f(\theta x + (1-\theta) y), g(\theta x + (1-\theta) y)\}$$
$$\leq \max\{\theta f(x) + (1-\theta) f(y), \theta g(x) + (1-\theta) g(y)\}$$
$$\leq \theta \max\{f(x), g(x)\} + (1-\theta) \max\{f(y), g(y)\}$$
$$= \theta h(x) + (1-\theta) h(y)$$

**Generalization:** $$\sup_{t \in T} f_t(x)$$ convex nếu mỗi $$f_t$$ convex.

**Bước 3: Affine composition - CONVEX**

**Theorem:** $$h(x) = f(Ax + b)$$ convex nếu $$f$$ convex.

**Proof:**
$$h(\theta x + (1-\theta) y) = f(A(\theta x + (1-\theta) y) + b)$$
$$= f(\theta(Ax + b) + (1-\theta)(Ay + b))$$
$$\leq \theta f(Ax + b) + (1-\theta) f(Ay + b)$$
$$= \theta h(x) + (1-\theta) h(y)$$

**Bước 4: Partial minimization - CONVEX**

**Theorem:** $$h(x) = \inf_{y \in C} f(x, y)$$ convex trong $$x$$ nếu $$f(x, y)$$ convex trong $$(x, y)$$ và $$C$$ convex.

**Proof:** Với mọi $$y \in C$$:
$$h(\theta x_1 + (1-\theta) x_2) \leq f(\theta x_1 + (1-\theta) x_2, y)$$
$$\leq \theta f(x_1, y) + (1-\theta) f(x_2, y)$$

Taking infimum over $$y$$:
$$h(\theta x_1 + (1-\theta) x_2) \leq \theta h(x_1) + (1-\theta) h(x_2)$$

**Bước 5: Integration - CONVEX**

**Theorem:** $$h(x) = \int_0^\infty f(x, t) dt$$ convex nếu $$f(x, t)$$ convex trong $$x$$ for each $$t$$.

**Proof:** Monotone convergence theorem + convexity preservation under limits.

</details>

---

## 📝 **Bài tập 3: Conjugate functions**

**Đề bài:** (Bài 3.3 từ Boyd & Vandenberghe)
Tính conjugate function $$f^*(y) = \sup_x (y^T x - f(x))$$ cho:

a) $$f(x) = \frac{1}{2}x^T Q x$$ với $$Q \succ 0$$

b) $$f(x) = \lVert x \rVert_2$$

c) $$f(x) = \lVert x \rVert_1$$

d) $$f(x) = \log \sum_{i=1}^n e^{x_i}$$ (log-sum-exp)

e) $$f(x) = \max_{i=1,\ldots,n} x_i$$

**Yêu cầu:**
1. Derive conjugates using optimization
2. Verify conjugacy relationships
3. Analyze domains của conjugates
4. Geometric interpretation

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Quadratic function**
$$f(x) = \frac{1}{2}x^T Q x$$ với $$Q \succ 0$$

**Optimization:** $$\max_x (y^T x - \frac{1}{2}x^T Q x)$$

**First-order condition:** $$y - Qx = 0 \Rightarrow x^* = Q^{-1} y$$

**Conjugate:**
$$f^*(y) = y^T Q^{-1} y - \frac{1}{2}y^T Q^{-1} Q Q^{-1} y = \frac{1}{2}y^T Q^{-1} y$$

**Domain:** $$\mathbb{R}^n$$ (vì $$Q \succ 0$$)

**Bước 2: Euclidean norm**
$$f(x) = \lVert x \rVert_2$$

**Optimization:** $$\max_x (y^T x - \lVert x \rVert_2)$$

**Case analysis:**
- Nếu $$\lVert y \rVert_2 \leq 1$$: supremum achieved tại $$x^* = \frac{y}{\lVert y \rVert_2}$$ với value $$\lVert y \rVert_2$$
- Nếu $$\lVert y \rVert_2 > 1$$: supremum = $$+\infty$$

**Conjugate:**
$$f^*(y) = \begin{cases} 0 & \text{if } \lVert y \rVert_2 \leq 1 \\ +\infty & \text{if } \lVert y \rVert_2 > 1 \end{cases}$$

**Domain:** Unit ball $$\{y : \lVert y \rVert_2 \leq 1\}$$

**Bước 3: $$\ell_1$$ norm**
$$f(x) = \lVert x \rVert_1 = \sum_{i=1}^n |x_i|$$

**Separable optimization:** $$\max_{x_i} (y_i x_i - |x_i|)$$ for each $$i$$

**Component analysis:**
- Nếu $$|y_i| \leq 1$$: maximum = 0 tại $$x_i = 0$$
- Nếu $$|y_i| > 1$$: maximum = $$+\infty$$

**Conjugate:**
$$f^*(y) = \begin{cases} 0 & \text{if } \lVert y \rVert_\infty \leq 1 \\ +\infty & \text{if } \lVert y \rVert_\infty > 1 \end{cases}$$

**Bước 4: Log-sum-exp**
$$f(x) = \log \sum_{i=1}^n e^{x_i}$$

**Optimization:** $$\max_x \left(\sum_{i=1}^n y_i x_i - \log \sum_{i=1}^n e^{x_i}\right)$$

**First-order conditions:** $$y_i = \frac{e^{x_i}}{\sum_j e^{x_j}}$$

**Interpretation:** $$y$$ must be probability vector: $$y \geq 0$$, $$\sum y_i = 1$$

**Conjugate:** $$f^*(y) = \sum_{i=1}^n y_i \log y_i$$ (negative entropy)

**Domain:** Probability simplex $$\{y : y \geq 0, \sum y_i = 1\}$$

**Bước 5: Max function**
$$f(x) = \max_{i=1,\ldots,n} x_i$$

**Dual của $$\ell_\infty$$ norm:** 

**Conjugate:**
$$f^*(y) = \begin{cases} 0 & \text{if } y \geq 0, \sum y_i = 1 \\ +\infty & \text{otherwise} \end{cases}$$

**Domain:** Probability simplex

</details>

---

## 📝 **Bài tập 4: Subdifferentials và optimality**

**Đề bài:** (Bài 3.4 từ Boyd & Vandenberghe)
Tính subdifferential $$\partial f(x) = \{g : f(y) \geq f(x) + g^T(y - x), \forall y\}$$ cho:

a) $$f(x) = |x|$$ tại các điểm khác nhau

b) $$f(x) = \max\{0, x\}$$ (ReLU function)

c) $$f(x) = \lVert x \rVert_1$$

d) $$f(x) = \lVert x \rVert_2$$

**Yêu cầu:**
1. Compute subdifferentials explicitly
2. Verify optimality conditions
3. Analyze non-differentiable points
4. Apply to optimization problems

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Absolute value $$f(x) = |x|$$**

**Case $$x > 0$$:** $$f$$ differentiable, $$\partial f(x) = \{1\}$$

**Case $$x < 0$$:** $$f$$ differentiable, $$\partial f(x) = \{-1\}$$

**Case $$x = 0$$:** Non-differentiable point

**Subdifferential tại $$x = 0$$:**
$$\partial f(0) = \{g : |y| \geq g \cdot y, \forall y\}$$

**Analysis:** Cần $$|g| \leq 1$$

$$\Rightarrow \partial f(0) = [-1, 1]$$

**Bước 2: ReLU function $$f(x) = \max\{0, x\}$$**

**Case $$x > 0$$:** $$f(x) = x$$, $$\partial f(x) = \{1\}$$

**Case $$x < 0$$:** $$f(x) = 0$$, $$\partial f(x) = \{0\}$$

**Case $$x = 0$$:** 
$$\partial f(0) = \{g : \max\{0, y\} \geq g \cdot y, \forall y\}$$

**Analysis:**
- For $$y > 0$$: $$y \geq g \cdot y \Rightarrow g \leq 1$$
- For $$y < 0$$: $$0 \geq g \cdot y \Rightarrow g \geq 0$$

$$\Rightarrow \partial f(0) = [0, 1]$$

**Bước 3: $$\ell_1$$ norm $$f(x) = \lVert x \rVert_1$$**

**Component-wise analysis:** $$f(x) = \sum_{i=1}^n |x_i|$$

**Subdifferential:** $$\partial f(x) = \partial f_1(x_1) \times \cdots \times \partial f_n(x_n)$$

với $$\partial f_i(x_i) = \begin{cases} \{1\} & \text{if } x_i > 0 \\ \{-1\} & \text{if } x_i < 0 \\ [-1, 1] & \text{if } x_i = 0 \end{cases}$$

**Result:** $$\partial f(x) = \{g : g_i = \text{sign}(x_i) \text{ if } x_i \neq 0, |g_i| \leq 1 \text{ if } x_i = 0\}$$

**Bước 4: Euclidean norm $$f(x) = \lVert x \rVert_2$$**

**Case $$x \neq 0$$:** $$\partial f(x) = \left\{\frac{x}{\lVert x \rVert_2}\right\}$$

**Case $$x = 0$$:** 
$$\partial f(0) = \{g : \lVert y \rVert_2 \geq g^T y, \forall y\}$$

**By Cauchy-Schwarz:** $$g^T y \leq \lVert g \rVert_2 \lVert y \rVert_2$$

**Condition:** $$\lVert g \rVert_2 \leq 1$$

$$\Rightarrow \partial f(0) = \{g : \lVert g \rVert_2 \leq 1\}$$ (unit ball)

</details>

---

## 📝 **Bài tập 5: Jensen's inequality và applications**

**Đề bài:** (Bài 3.5 từ Boyd & Vandenberghe)
a) Chứng minh Jensen's inequality: Nếu $$f$$ convex, $$\lambda_i \geq 0$$, $$\sum \lambda_i = 1$$, thì:
$$f\left(\sum_{i=1}^n \lambda_i x_i\right) \leq \sum_{i=1}^n \lambda_i f(x_i)$$

b) Apply Jensen's inequality để chứng minh:
   - Arithmetic-geometric mean: $$\frac{x_1 + \cdots + x_n}{n} \geq \sqrt[n]{x_1 \cdots x_n}$$
   - Hölder's inequality: $$\sum_{i=1}^n |x_i y_i| \leq \left(\sum_{i=1}^n |x_i|^p\right)^{1/p} \left(\sum_{i=1}^n |y_i|^q\right)^{1/q}$$

c) Derive log-sum inequality

**Yêu cầu:**
1. Rigorous proof bằng induction
2. Geometric interpretation
3. Applications trong probability
4. Extensions to continuous case

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Jensen's inequality proof**

**Base case ($$n = 2$$):** Definition của convexity

**Inductive step:** Assume true for $$n-1$$, prove for $$n$$.

Với $$\sum_{i=1}^n \lambda_i = 1$$, đặt $$\mu = \sum_{i=1}^{n-1} \lambda_i < 1$$.

$$f\left(\sum_{i=1}^n \lambda_i x_i\right) = f\left(\mu \cdot \frac{\sum_{i=1}^{n-1} \lambda_i x_i}{\mu} + (1-\mu) x_n\right)$$

**By convexity:**
$$\leq \mu f\left(\frac{\sum_{i=1}^{n-1} \lambda_i x_i}{\mu}\right) + (1-\mu) f(x_n)$$

**By induction hypothesis:**
$$\leq \mu \sum_{i=1}^{n-1} \frac{\lambda_i}{\mu} f(x_i) + \lambda_n f(x_n) = \sum_{i=1}^n \lambda_i f(x_i)$$

**Bước 2: Arithmetic-geometric mean**

**Setup:** $$f(x) = -\log x$$ convex trên $$\mathbb{R}_{++}$$

**Jensen:** $$-\log\left(\frac{x_1 + \cdots + x_n}{n}\right) \leq \frac{1}{n}\sum_{i=1}^n (-\log x_i) = -\frac{1}{n}\log(x_1 \cdots x_n)$$

**Rearranging:** $$\log\left(\frac{x_1 + \cdots + x_n}{n}\right) \geq \log\sqrt[n]{x_1 \cdots x_n}$$

$$\Rightarrow \frac{x_1 + \cdots + x_n}{n} \geq \sqrt[n]{x_1 \cdots x_n}$$

**Bước 3: Hölder's inequality**

**Setup:** Sử dụng conjugate exponents $$\frac{1}{p} + \frac{1}{q} = 1$$

**Key function:** $$f(t) = e^t$$ convex

**Application:** $$|x_i y_i| = |x_i|^{1/p} |x_i|^{1/q} |y_i|^{1/p} |y_i|^{1/q}$$

**Jensen application với weights:**
$$\log|x_i y_i| \leq \frac{1}{p}\log|x_i|^p + \frac{1}{q}\log|y_i|^q$$

**Summing và exponentiating:**
$$\sum |x_i y_i| \leq \left(\sum |x_i|^p\right)^{1/p} \left(\sum |y_i|^q\right)^{1/q}$$

**Bước 4: Log-sum inequality**

**Statement:** $$\sum_{i=1}^n a_i \log \frac{a_i}{b_i} \geq \left(\sum_{i=1}^n a_i\right) \log \frac{\sum_{i=1}^n a_i}{\sum_{i=1}^n b_i}$$

**Proof:** Sử dụng Jensen với $$f(x) = x \log x$$ convex và appropriate weights.

</details>

---

## 📝 **Bài tập 6: Quasiconvex functions**

**Đề bài:** (Bài 3.6 từ Boyd & Vandenberghe)
a) Verify quasiconvexity của:
   - $$f(x) = \frac{x_1}{x_2}$$ trên $$\{x : x_2 > 0\}$$
   - $$f(x) = x_1^2 / x_2$$ trên $$\{x : x_2 > 0\}$$
   - $$f(x) = \log(x_1) - \log(x_2)$$ trên $$\mathbb{R}_{++}^2$$

b) Chứng minh: $$f$$ quasiconvex $$\Leftrightarrow$$ sublevel sets $$\{x : f(x) \leq \alpha\}$$ convex

c) Operations preserving quasiconvexity

**Yêu cầu:**
1. Verify bằng sublevel set analysis
2. Check first-order conditions
3. Analyze monotonic transformations
4. Compare với convexity

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Ratio function $$f(x) = \frac{x_1}{x_2}$$**

**Sublevel sets:** $$S_\alpha = \{x : x_1 \leq \alpha x_2, x_2 > 0\}$$

**Analysis:** $$S_\alpha = \{x : x_1 - \alpha x_2 \leq 0, x_2 > 0\}$$

Intersection của halfspace và halfspace $$\Rightarrow$$ convex

$$\Rightarrow f$$ quasiconvex

**Bước 2: $$f(x) = \frac{x_1^2}{x_2}$$**

**Sublevel sets:** $$S_\alpha = \{x : x_1^2 \leq \alpha x_2, x_2 > 0\}$$

**For $$\alpha \leq 0$$:** $$S_\alpha = \{x : x_1 = 0, x_2 > 0\}$$ (convex)

**For $$\alpha > 0$$:** $$S_\alpha = \{x : x_1^2 \leq \alpha x_2, x_2 > 0\}$$

**Second-order cone:** $$\{x : \lVert x_1 \rVert_2 \leq \sqrt{\alpha x_2}, x_2 > 0\}$$ (convex)

$$\Rightarrow f$$ quasiconvex

**Bước 3: Log ratio $$f(x) = \log x_1 - \log x_2$$**

**Equivalent:** $$f(x) = \log\frac{x_1}{x_2}$$

**Monotonic transformation:** $$\log$$ increasing, $$\frac{x_1}{x_2}$$ quasiconvex

$$\Rightarrow f$$ quasiconvex

**Bước 4: Characterization theorem**

**Theorem:** $$f$$ quasiconvex $$\Leftrightarrow$$ all sublevel sets convex

**Proof ($$\Rightarrow$$):** 
Với $$x, y \in S_\alpha$$, $$f(x), f(y) \leq \alpha$$

By quasiconvexity: $$f(\theta x + (1-\theta) y) \leq \max\{f(x), f(y)\} \leq \alpha$$

$$\Rightarrow \theta x + (1-\theta) y \in S_\alpha$$

**Proof ($$\Leftarrow$$):**
Với $$f(x), f(y) \leq \alpha$$, ta có $$x, y \in S_\alpha$$

Vì $$S_\alpha$$ convex: $$\theta x + (1-\theta) y \in S_\alpha$$

$$\Rightarrow f(\theta x + (1-\theta) y) \leq \alpha = \max\{f(x), f(y)\}$$

**Bước 5: Operations preserving quasiconvexity**

- **Nonnegative weighted maximum:** $$\max\{f_1, f_2\}$$ quasiconvex
- **Composition với increasing function:** $$g \circ f$$ quasiconvex nếu $$g$$ increasing
- **Minimization:** Generally not preserved

</details>

---

## 📝 **Bài tập 7: Log-concave và log-convex functions**

**Đề bài:** (Bài 3.7 từ Boyd & Vandenberghe)
a) Verify log-concavity của:
   - Gaussian density: $$f(x) = e^{-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)}$$
   - Gamma function: $$\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt$$
   - Determinant: $$\det(X)$$ trên $$\mathbb{S}_{++}^n$$

b) Applications trong probability và statistics

c) Relationship với convexity

**Yêu cầu:**
1. Verify bằng second-order conditions
2. Analyze preservation properties
3. Statistical applications
4. Optimization implications

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Gaussian density**

**Function:** $$f(x) = e^{-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)}$$

**Log function:** $$\log f(x) = -\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)$$

**Hessian:** $$\nabla^2 \log f(x) = -\Sigma^{-1} \preceq 0$$

$$\Rightarrow \log f$$ concave $$\Rightarrow f$$ log-concave

**Bước 2: Determinant function**

**Function:** $$f(X) = \det(X)$$ trên $$\mathbb{S}_{++}^n$$

**Log function:** $$\log f(X) = \log \det(X)$$

**Known result:** $$\log \det(X)$$ concave trên $$\mathbb{S}_{++}^n$$

**Proof sketch:** Hessian analysis hoặc operator concavity

$$\Rightarrow \det(X)$$ log-concave

**Bước 3: Preservation properties**

**Products:** Nếu $$f, g$$ log-concave, thì $$fg$$ log-concave

**Proof:** $$\log(fg) = \log f + \log g$$ (sum của concave functions)

**Powers:** Nếu $$f$$ log-concave và $$\alpha \geq 0$$, thì $$f^\alpha$$ log-concave

**Integration:** Log-concavity preserved under integration

**Bước 4: Statistical applications**

**Maximum likelihood:** Log-concave likelihoods $$\Rightarrow$$ concave log-likelihood

**Unimodality:** Log-concave densities are unimodal

**Concentration:** Log-concave measures satisfy concentration inequalities

**Bước 5: Optimization implications**

**Geometric programming:** Log-convex functions trong GP

**Barrier methods:** $$-\log \det(X)$$ barrier cho PSD cone

**Exponential families:** Natural parameters và log-partition functions

</details>

---

## 📝 **Bài tập 8: Perspective và epigraph**

**Đề bài:** (Bài 3.8 từ Boyd & Vandenberghe)
a) Cho convex function $$f: \mathbb{R}^n \to \mathbb{R}$$. Chứng minh perspective function:
$$g(x, t) = t f(x/t)$$ với $$t > 0$$
là convex trên $$\mathbb{R}^n \times \mathbb{R}_{++}$$

b) Applications:
   - $$f(x) = \lVert x \rVert_2 \Rightarrow g(x,t) = \lVert x \rVert_2$$
   - $$f(x) = x^2 \Rightarrow g(x,t) = x^2/t$$
   - $$f(x) = e^x \Rightarrow g(x,t) = t e^{x/t}$$

c) Epigraph characterization của convexity

**Yêu cầu:**
1. Rigorous proof của perspective convexity
2. Geometric interpretation
3. Second-order cone connections
4. Epigraph analysis

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Perspective function convexity**

**Theorem:** Nếu $$f$$ convex, thì $$g(x,t) = tf(x/t)$$ convex trên $$\text{dom}(g) = \{(x,t) : x/t \in \text{dom}(f), t > 0\}$$

**Proof:** Với $$(x_1, t_1), (x_2, t_2) \in \text{dom}(g)$$ và $$\theta \in [0,1]$$:

$$g(\theta(x_1, t_1) + (1-\theta)(x_2, t_2)) = g(\theta x_1 + (1-\theta) x_2, \theta t_1 + (1-\theta) t_2)$$

$$= (\theta t_1 + (1-\theta) t_2) f\left(\frac{\theta x_1 + (1-\theta) x_2}{\theta t_1 + (1-\theta) t_2}\right)$$

**Key observation:** 
$$\frac{\theta x_1 + (1-\theta) x_2}{\theta t_1 + (1-\theta) t_2} = \frac{\theta t_1}{\theta t_1 + (1-\theta) t_2} \cdot \frac{x_1}{t_1} + \frac{(1-\theta) t_2}{\theta t_1 + (1-\theta) t_2} \cdot \frac{x_2}{t_2}$$

**Convex combination với weights:** $$\frac{\theta t_1}{\theta t_1 + (1-\theta) t_2} + \frac{(1-\theta) t_2}{\theta t_1 + (1-\theta) t_2} = 1$$

**By convexity của $$f$$:**
$$f\left(\frac{\theta x_1 + (1-\theta) x_2}{\theta t_1 + (1-\theta) t_2}\right) \leq \frac{\theta t_1}{\theta t_1 + (1-\theta) t_2} f(x_1/t_1) + \frac{(1-\theta) t_2}{\theta t_1 + (1-\theta) t_2} f(x_2/t_2)$$

**Multiplying by $$\theta t_1 + (1-\theta) t_2$$:**
$$g(\theta(x_1, t_1) + (1-\theta)(x_2, t_2)) \leq \theta t_1 f(x_1/t_1) + (1-\theta) t_2 f(x_2/t_2) = \theta g(x_1, t_1) + (1-\theta) g(x_2, t_2)$$

**Bước 2: Applications**

**Example 1:** $$f(x) = \lVert x \rVert_2$$
$$g(x,t) = t \lVert x/t \rVert_2 = \lVert x \rVert_2$$

**Geometric interpretation:** Norm function invariant under perspective

**Example 2:** $$f(x) = x^2$$
$$g(x,t) = t(x/t)^2 = x^2/t$$

**Second-order cone:** $$\{(x,t) : x^2/t \leq s, t > 0\} = \{(x,t,s) : \lVert (x,s-t) \rVert_2 \leq s+t\}$$

**Example 3:** $$f(x) = e^x$$
$$g(x,t) = te^{x/t}$$

**Exponential cone:** Important trong conic optimization

**Bước 3: Epigraph characterization**

**Theorem:** $$f$$ convex $$\Leftrightarrow$$ $$\text{epi}(f) = \{(x,t) : f(x) \leq t\}$$ convex

**Proof ($$\Rightarrow$$):** 
Với $$(x_1, t_1), (x_2, t_2) \in \text{epi}(f)$$:
$$f(\theta x_1 + (1-\theta) x_2) \leq \theta f(x_1) + (1-\theta) f(x_2) \leq \theta t_1 + (1-\theta) t_2$$

$$\Rightarrow (\theta x_1 + (1-\theta) x_2, \theta t_1 + (1-\theta) t_2) \in \text{epi}(f)$$

**Proof ($$\Leftarrow$$):**
Với $$f(x_1) \leq t_1, f(x_2) \leq t_2$$, choose $$t_1 = f(x_1), t_2 = f(x_2)$$

Convexity của epigraph $$\Rightarrow$$ convexity của $$f$$

</details>

---

## 📝 **Bài tập 9: Matrix functions và convexity**

**Đề bài:** (Bài 3.9 từ Boyd & Vandenberghe)
Analyze convexity của các matrix functions:

a) $$f(X) = \text{tr}(X)$$ trên $$\mathbb{S}^n$$

b) $$f(X) = \text{tr}(X^2)$$ trên $$\mathbb{S}^n$$

c) $$f(X) = \lambda_{\max}(X)$$ trên $$\mathbb{S}^n$$

d) $$f(X) = \det(X)$$ trên $$\mathbb{S}_{++}^n$$

e) $$f(X) = -\log \det(X)$$ trên $$\mathbb{S}_{++}^n$$

**Yêu cầu:**
1. Verify convexity/concavity
2. Compute subdifferentials
3. Applications trong SDP
4. Optimization algorithms

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Trace function $$f(X) = \text{tr}(X)$$**

**Linearity:** $$\text{tr}(\theta X + (1-\theta) Y) = \theta \text{tr}(X) + (1-\theta) \text{tr}(Y)$$

$$\Rightarrow$$ Both convex và concave (affine)

**Subdifferential:** $$\partial f(X) = \{I\}$$

**Bước 2: Trace of square $$f(X) = \text{tr}(X^2)$$**

**Expansion:** $$\text{tr}(X^2) = \sum_{i,j} X_{ij}^2$$

**Convexity:** Sum của convex functions ($$x^2$$)

**Subdifferential:** $$\partial f(X) = \{2X\}$$

**Bước 3: Maximum eigenvalue $$f(X) = \lambda_{\max}(X)$$**

**Variational characterization:** $$\lambda_{\max}(X) = \max_{\lVert v \rVert_2 = 1} v^T X v$$

**Convexity:** Maximum của linear functions $$v^T X v$$

**Subdifferential:** $$\partial f(X) = \text{conv}\{vv^T : v \text{ eigenvector of } \lambda_{\max}(X), \lVert v \rVert_2 = 1\}$$

**Bước 4: Determinant $$f(X) = \det(X)$$**

**Log-concavity:** $$\log \det(X)$$ concave $$\Rightarrow \det(X)$$ log-concave

**Not convex:** $$\det$$ neither convex nor concave trên $$\mathbb{S}_{++}^n$$

**Geometric mean:** $$\det(X)^{1/n} = (\prod \lambda_i)^{1/n}$$ concave

**Bước 5: Negative log-determinant $$f(X) = -\log \det(X)$$**

**Convexity:** $$-\log \det(X)$$ strictly convex trên $$\mathbb{S}_{++}^n$$

**Subdifferential:** $$\partial f(X) = \{-X^{-1}\}$$

**Barrier function:** Used trong interior-point methods cho SDP

**Hessian:** $$\nabla^2 f(X)[H, H] = \text{tr}(X^{-1} H X^{-1} H) > 0$$ for $$H \neq 0$$

**Applications:**
- **SDP barrier:** $$-\log \det(X)$$ barrier cho $$X \succ 0$$
- **Maximum likelihood:** Covariance estimation
- **Optimal design:** D-optimal experimental design

</details>

---

## 📝 **Bài tập 10: Convex optimization applications**

**Đề bài:** (Bài 3.10 từ Boyd & Vandenberghe)
Formulate các bài toán sau sử dụng convex functions:

a) **Robust regression:** Minimize sum of Huber losses
b) **Entropy maximization:** Subject to moment constraints
c) **Geometric mean maximization:** $$\max \prod_{i=1}^n x_i^{1/n}$$ subject to constraints
d) **Relative entropy minimization:** $$\min \sum_{i=1}^n x_i \log(x_i/y_i)$$

**Yêu cầu:**
1. Identify convex formulations
2. Analyze optimality conditions
3. Suggest solution algorithms
4. Discuss practical applications

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Robust regression**

**Problem:** $$\min_\beta \sum_{i=1}^n \phi(y_i - x_i^T \beta)$$

với Huber loss: $$\phi(u) = \begin{cases} \frac{1}{2}u^2 & |u| \leq M \\ M|u| - \frac{1}{2}M^2 & |u| > M \end{cases}$$

**Convexity:** $$\phi$$ convex (piecewise quadratic với non-decreasing derivative)

**Reformulation:** 
$$\min_{\beta,r,s} \frac{1}{2}\sum_{i=1}^n r_i^2 + M\sum_{i=1}^n s_i$$
$$\text{s.t.} \quad |y_i - x_i^T \beta| \leq r_i + s_i, \quad 0 \leq r_i \leq M, \quad s_i \geq 0$$

**Bước 2: Entropy maximization**

**Problem:** $$\max_x -\sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad \sum_{i=1}^n a_{ij} x_i = b_j, \quad x_i \geq 0$$

**Convex formulation:** $$\min_x \sum_{i=1}^n x_i \log x_i$$

**Optimality conditions:** 
$$\log x_i + 1 + \sum_{j=1}^m \lambda_j a_{ij} = 0$$
$$\Rightarrow x_i^* = e^{-1 - \sum_j \lambda_j a_{ij}}$$

**Maximum entropy distribution:** Exponential family form

**Bước 3: Geometric mean maximization**

**Problem:** $$\max_{x \geq 0} \prod_{i=1}^n x_i^{1/n} \quad \text{s.t.} \quad Ax \leq b$$

**Log transformation:** $$\max_x \frac{1}{n}\sum_{i=1}^n \log x_i$$

**Convex formulation:** $$\min_x -\sum_{i=1}^n \log x_i \quad \text{s.t.} \quad Ax \leq b, \quad x > 0$$

**Barrier method:** Natural fit với log barriers

**Applications:** Optimal design, Nash bargaining

**Bước 4: Relative entropy minimization**

**Problem:** $$\min_x \sum_{i=1}^n x_i \log \frac{x_i}{y_i} \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Convexity:** KL divergence convex trong first argument

**Optimality conditions:**
$$\log \frac{x_i}{y_i} + 1 + (A^T \lambda)_i + \mu_i = 0$$

**Solution form:** $$x_i^* = y_i e^{-(A^T \lambda^*)_i - 1}$$

**Applications:**
- **Information theory:** Channel capacity
- **Statistics:** Maximum likelihood với prior
- **Machine learning:** Regularized optimization

</details>

---

## 💡 Mẹo Thực Hành

#### **Khi verify convexity:**
- **Second-order conditions:** $$f''(x) \geq 0$$ hoặc $$\nabla^2 f \succeq 0$$
- **Definition:** Check $$f(\theta x + (1-\theta) y) \leq \theta f(x) + (1-\theta) f(y)$$
- **Composition rules:** Sử dụng operations preserving convexity

#### **Khi tính conjugate functions:**
- **Optimization approach:** $$f^*(y) = \sup_x (y^T x - f(x))$$
- **First-order conditions:** $$y \in \partial f(x^*)$$
- **Geometric interpretation:** Supporting hyperplanes

#### **Khi work với subdifferentials:**
- **Differentiable case:** $$\partial f(x) = \{\nabla f(x)\}$$
- **Non-differentiable:** Use definition hoặc calculus rules
- **Optimality:** $$0 \in \partial f(x^*)$$

---

## 📚 Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 3: Convex Functions
   - Exercises 3.1-3.54

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Hiriart-Urruty, J.-B., & Lemaréchal, C.** (1993). *Convex Analysis and Minimization Algorithms*. Springer.

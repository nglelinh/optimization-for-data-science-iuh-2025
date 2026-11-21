---
layout: post
title: '3-9 Practical Exercises - Convex Functions'
chapter: '3'
order: 10
owner: GitHub Copilot
lang: en
categories:
- chapter03
lesson_type: required
---

# Practical Exercises - Convex Functions

## 📝 **Exercise 1: Verifying convex functions**

**Problem:** (Exercise 3.1 from Boyd & Vandenberghe)
Determine whether the following functions are convex on their domains:

a) $$f(x) = x^2$$ on $$\mathbb{R}$$

b) $$f(x) = e^{ax}$$ on $$\mathbb{R}$$

c) $$f(x) = x \log x$$ on $$\mathbb{R}_{++}$$

d) $$f(x) = -\log x$$ on $$\mathbb{R}_{++}$$

e) $$f(x) = x^p$$ with $$p \geq 1$$ on $$\mathbb{R}_+$$

f) $$f(x) = |x|^p$$ with $$p \geq 1$$ on $$\mathbb{R}$$

**Task:**
1. Verify using the definition of convexity
2. Use second-order conditions where applicable
3. Analyze domain restrictions
4. Visualize the functions and their convexity

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: $$f(x) = x^2$$**

**Second-order condition:** $$f''(x) = 2 > 0$$ $$\forall x \in \mathbb{R}$$

$$\Rightarrow$$ Strictly convex on $$\mathbb{R}$$

**Verification from the definition:**
$$f(\theta x + (1-\theta) y) = (\theta x + (1-\theta) y)^2 = \theta^2 x^2 + 2\theta(1-\theta)xy + (1-\theta)^2 y^2$$

$$\theta f(x) + (1-\theta) f(y) = \theta x^2 + (1-\theta) y^2$$

$$f(\theta x + (1-\theta) y) - [\theta f(x) + (1-\theta) f(y)] = -\theta(1-\theta)(x-y)^2 \leq 0$$

**Step 2: $$f(x) = e^{ax}$$**

**Second-order condition:** $$f''(x) = a^2 e^{ax} \geq 0$$ $$\forall x$$

$$\Rightarrow$$ Convex on $$\mathbb{R}$$ (strictly convex if $$a \neq 0$$)

**Step 3: $$f(x) = x \log x$$**

**Domain:** $$\mathbb{R}_{++}$$ ($$x > 0$$)

**First derivative:** $$f'(x) = \log x + 1$$

**Second derivative:** $$f''(x) = \frac{1}{x} > 0$$ for $$x > 0$$

$$\Rightarrow$$ Strictly convex on $$\mathbb{R}_{++}$$

**Step 4: $$f(x) = -\log x$$**

**Second derivative:** $$f''(x) = \frac{1}{x^2} > 0$$ for $$x > 0$$

$$\Rightarrow$$ Strictly convex on $$\mathbb{R}_{++}$$

**Step 5: $$f(x) = x^p$$ with $$p \geq 1$$**

**Case $$p = 1$$:** $$f(x) = x$$ is linear $$\Rightarrow$$ convex

**Case $$p > 1$$:** $$f''(x) = p(p-1)x^{p-2} \geq 0$$ for $$x \geq 0$$

$$\Rightarrow$$ Convex on $$\mathbb{R}_+$$

**Step 6: $$f(x) = |x|^p$$ with $$p \geq 1$$**

**Symmetry:** $$f(-x) = f(x)$$, so it suffices to look at $$x \geq 0$$

**For $$x \geq 0$$:** $$f(x) = x^p$$ is convex (from step 5)

**Note:** being convex on each half-line is not enough to conclude convexity on $$\mathbb{R}$$. The correct argument: $$f(x) = g(|x|)$$ where $$g(t) = t^p$$ is convex and **non-decreasing** on $$\mathbb{R}_+$$, and $$|x|$$ is convex.

**Composition rule:** a non-decreasing convex function of a convex function is convex, so $$|x|^p$$ is convex.

$$\Rightarrow$$ Convex on $$\mathbb{R}$$

</details>

---

## 📝 **Exercise 2: Operations preserving convexity**

**Problem:** (Exercise 3.2 from Boyd & Vandenberghe)
Let $$f, g: \mathbb{R}^n \to \mathbb{R}$$ be convex. Determine whether the following are convex:

a) $$h(x) = \alpha f(x) + \beta g(x)$$ with $$\alpha, \beta \geq 0$$

b) $$h(x) = \max\{f(x), g(x)\}$$

c) $$h(x) = f(Ax + b)$$ with $$A \in \mathbb{R}^{n \times m}$$, $$b \in \mathbb{R}^n$$

d) $$h(x) = \inf_{y \in C} f(x, y)$$ with $$C$$ convex

e) $$h(x) = \int_0^\infty f(x, t) dt$$ (if the integral exists)

**Task:**
1. Prove convexity for the operations
2. Give counterexamples when not convex
3. Provide concrete examples
4. Discuss conditions for strict convexity

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Non-negative weighted sum - CONVEX**

**Theorem:** If $$f, g$$ are convex and $$\alpha, \beta \geq 0$$, then $$h(x) = \alpha f(x) + \beta g(x)$$ is convex.

**Proof:**
$$h(\theta x + (1-\theta) y) = \alpha f(\theta x + (1-\theta) y) + \beta g(\theta x + (1-\theta) y)$$
$$\leq \alpha[\theta f(x) + (1-\theta) f(y)] + \beta[\theta g(x) + (1-\theta) g(y)]$$
$$= \theta[\alpha f(x) + \beta g(x)] + (1-\theta)[\alpha f(y) + \beta g(y)]$$
$$= \theta h(x) + (1-\theta) h(y)$$

**Step 2: Pointwise maximum - CONVEX**

**Theorem:** $$h(x) = \max\{f(x), g(x)\}$$ is convex if $$f, g$$ are convex.

**Proof:**
$$h(\theta x + (1-\theta) y) = \max\{f(\theta x + (1-\theta) y), g(\theta x + (1-\theta) y)\}$$
$$\leq \max\{\theta f(x) + (1-\theta) f(y), \theta g(x) + (1-\theta) g(y)\}$$
$$\leq \theta \max\{f(x), g(x)\} + (1-\theta) \max\{f(y), g(y)\}$$
$$= \theta h(x) + (1-\theta) h(y)$$

**Generalization:** $$\sup_{t \in T} f_t(x)$$ is convex if every $$f_t$$ is convex.

**Step 3: Affine composition - CONVEX**

**Theorem:** $$h(x) = f(Ax + b)$$ is convex if $$f$$ is convex.

**Proof:**
$$h(\theta x + (1-\theta) y) = f(A(\theta x + (1-\theta) y) + b)$$
$$= f(\theta(Ax + b) + (1-\theta)(Ay + b))$$
$$\leq \theta f(Ax + b) + (1-\theta) f(Ay + b)$$
$$= \theta h(x) + (1-\theta) h(y)$$

**Step 4: Partial minimization - CONVEX**

**Theorem:** $$h(x) = \inf_{y \in C} f(x, y)$$ is convex in $$x$$ if $$f(x, y)$$ is jointly convex in $$(x, y)$$ and $$C$$ is convex.

**Proof:** Given $$\epsilon > 0$$, choose $$y_1, y_2 \in C$$ with $$f(x_k, y_k) \leq h(x_k) + \epsilon$$ ($$k = 1, 2$$). Since $$C$$ is convex, $$\bar{y} = \theta y_1 + (1-\theta) y_2 \in C$$, so:
$$h(\theta x_1 + (1-\theta) x_2) \leq f(\theta x_1 + (1-\theta) x_2, \bar{y})$$
$$\leq \theta f(x_1, y_1) + (1-\theta) f(x_2, y_2) \leq \theta h(x_1) + (1-\theta) h(x_2) + \epsilon$$
Letting $$\epsilon \to 0$$:
$$h(\theta x_1 + (1-\theta) x_2) \leq \theta h(x_1) + (1-\theta) h(x_2)$$
(Note: one must use two different points $$y_1, y_2$$ and **joint** convexity in $$(x, y)$$; using the same $$y$$ for both does not prove it.)

**Step 5: Integration - CONVEX**

**Theorem:** $$h(x) = \int_0^\infty f(x, t) dt$$ is convex if $$f(x, t)$$ is convex in $$x$$ for each $$t$$.

**Proof:** For each $$t$$: $$f(\theta x + (1-\theta) y, t) \leq \theta f(x, t) + (1-\theta) f(y, t)$$. Integrating both sides in $$t$$ (integration preserves inequalities and is linear) gives $$h(\theta x + (1-\theta) y) \leq \theta h(x) + (1-\theta) h(y)$$.

</details>

---

## 📝 **Exercise 3: Conjugate functions**

**Problem:** (Exercise 3.3 from Boyd & Vandenberghe)
Compute the conjugate function $$f^*(y) = \sup_x (y^T x - f(x))$$ for:

a) $$f(x) = \frac{1}{2}x^T Q x$$ with $$Q \succ 0$$

b) $$f(x) = \lVert x \rVert_2$$

c) $$f(x) = \lVert x \rVert_1$$

d) $$f(x) = \log \sum_{i=1}^n e^{x_i}$$ (log-sum-exp)

e) $$f(x) = \max_{i=1,\ldots,n} x_i$$

**Task:**
1. Derive conjugates using optimization
2. Verify conjugacy relationships
3. Analyze the domains of the conjugates
4. Geometric interpretation

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Quadratic function**
$$f(x) = \frac{1}{2}x^T Q x$$ with $$Q \succ 0$$

**Optimization:** $$\max_x (y^T x - \frac{1}{2}x^T Q x)$$

**First-order condition:** $$y - Qx = 0 \Rightarrow x^* = Q^{-1} y$$

**Conjugate:**
$$f^*(y) = y^T Q^{-1} y - \frac{1}{2}y^T Q^{-1} Q Q^{-1} y = \frac{1}{2}y^T Q^{-1} y$$

**Domain:** $$\mathbb{R}^n$$ (since $$Q \succ 0$$)

**Step 2: Euclidean norm**
$$f(x) = \lVert x \rVert_2$$

**Optimization:** $$\max_x (y^T x - \lVert x \rVert_2)$$

**Case analysis:**
- If $$\lVert y \rVert_2 \leq 1$$: by Cauchy-Schwarz, $$y^T x - \lVert x \rVert_2 \leq (\lVert y \rVert_2 - 1)\lVert x \rVert_2 \leq 0$$, so the supremum is $$0$$, attained at $$x = 0$$
- If $$\lVert y \rVert_2 > 1$$: the supremum is $$+\infty$$

**Conjugate:**
$$f^*(y) = \begin{cases} 0 & \text{if } \lVert y \rVert_2 \leq 1 \\ +\infty & \text{if } \lVert y \rVert_2 > 1 \end{cases}$$

**Domain:** Unit ball $$\{y : \lVert y \rVert_2 \leq 1\}$$

**Step 3: $$\ell_1$$ norm**
$$f(x) = \lVert x \rVert_1 = \sum_{i=1}^n |x_i|$$

**Separable optimization:** $$\max_{x_i} (y_i x_i - |x_i|)$$ for each $$i$$

**Component analysis:**
- If $$|y_i| \leq 1$$: the maximum is 0, at $$x_i = 0$$
- If $$|y_i| > 1$$: the maximum is $$+\infty$$

**Conjugate:**
$$f^*(y) = \begin{cases} 0 & \text{if } \lVert y \rVert_\infty \leq 1 \\ +\infty & \text{if } \lVert y \rVert_\infty > 1 \end{cases}$$

**Step 4: Log-sum-exp**
$$f(x) = \log \sum_{i=1}^n e^{x_i}$$

**Optimization:** $$\max_x \left(\sum_{i=1}^n y_i x_i - \log \sum_{i=1}^n e^{x_i}\right)$$

**First-order condition:** $$y_i = \frac{e^{x_i}}{\sum_j e^{x_j}}$$

**Interpretation:** $$y$$ must be probability vector: $$y \geq 0$$, $$\sum y_i = 1$$

**Conjugate:** $$f^*(y) = \sum_{i=1}^n y_i \log y_i$$ (negative entropy)

**Domain:** Probability simplex $$\{y : y \geq 0, \sum y_i = 1\}$$

**Step 5: Max function**
$$f(x) = \max_{i=1,\ldots,n} x_i$$

**Related to the dual of the $$\ell_\infty$$ norm:**

**Conjugate:**
$$f^*(y) = \begin{cases} 0 & \text{if } y \geq 0, \sum y_i = 1 \\ +\infty & \text{otherwise} \end{cases}$$

**Domain:** Probability simplex

</details>

---

## 📝 **Exercise 4: Subdifferentials and optimality**

**Problem:** (Exercise 3.4 from Boyd & Vandenberghe)
Compute the subdifferential $$\partial f(x) = \{g : f(y) \geq f(x) + g^T(y - x), \forall y\}$$ for:

a) $$f(x) = |x|$$ at different points

b) $$f(x) = \max\{0, x\}$$ (ReLU function)

c) $$f(x) = \lVert x \rVert_1$$

d) $$f(x) = \lVert x \rVert_2$$

**Task:**
1. Compute subdifferentials explicitly
2. Verify optimality conditions
3. Analyze non-differentiable points
4. Apply to optimization problems

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Absolute value $$f(x) = |x|$$**

**Case $$x > 0$$:** $$f$$ differentiable, $$\partial f(x) = \{1\}$$

**Case $$x < 0$$:** $$f$$ differentiable, $$\partial f(x) = \{-1\}$$

**Case $$x = 0$$:** Non-differentiable point

**Subdifferential at $$x = 0$$:**
$$\partial f(0) = \{g : |y| \geq g \cdot y, \forall y\}$$

**Analysis:** We need $$|g| \leq 1$$

$$\Rightarrow \partial f(0) = [-1, 1]$$

**Step 2: ReLU function $$f(x) = \max\{0, x\}$$**

**Case $$x > 0$$:** $$f(x) = x$$, $$\partial f(x) = \{1\}$$

**Case $$x < 0$$:** $$f(x) = 0$$, $$\partial f(x) = \{0\}$$

**Case $$x = 0$$:** 
$$\partial f(0) = \{g : \max\{0, y\} \geq g \cdot y, \forall y\}$$

**Analysis:**
- For $$y > 0$$: $$y \geq g \cdot y \Rightarrow g \leq 1$$
- For $$y < 0$$: $$0 \geq g \cdot y \Rightarrow g \geq 0$$

$$\Rightarrow \partial f(0) = [0, 1]$$

**Step 3: $$\ell_1$$ norm $$f(x) = \lVert x \rVert_1$$**

**Component-wise analysis:** $$f(x) = \sum_{i=1}^n |x_i|$$

**Subdifferential:** $$\partial f(x) = \partial f_1(x_1) \times \cdots \times \partial f_n(x_n)$$

where $$\partial f_i(x_i) = \begin{cases} \{1\} & \text{if } x_i > 0 \\ \{-1\} & \text{if } x_i < 0 \\ [-1, 1] & \text{if } x_i = 0 \end{cases}$$

**Result:** $$\partial f(x) = \{g : g_i = \text{sign}(x_i) \text{ if } x_i \neq 0, |g_i| \leq 1 \text{ if } x_i = 0\}$$

**Step 4: Euclidean norm $$f(x) = \lVert x \rVert_2$$**

**Case $$x \neq 0$$:** $$\partial f(x) = \left\{\frac{x}{\lVert x \rVert_2}\right\}$$

**Case $$x = 0$$:** 
$$\partial f(0) = \{g : \lVert y \rVert_2 \geq g^T y, \forall y\}$$

**By Cauchy-Schwarz:** $$g^T y \leq \lVert g \rVert_2 \lVert y \rVert_2$$

**Condition:** $$\lVert g \rVert_2 \leq 1$$

$$\Rightarrow \partial f(0) = \{g : \lVert g \rVert_2 \leq 1\}$$ (unit ball)

</details>

---

## 📝 **Exercise 5: Jensen's inequality and applications**

**Problem:** (Exercise 3.5 from Boyd & Vandenberghe)
a) Prove Jensen's inequality: if $$f$$ is convex, $$\lambda_i \geq 0$$, $$\sum \lambda_i = 1$$, then:
$$f\left(\sum_{i=1}^n \lambda_i x_i\right) \leq \sum_{i=1}^n \lambda_i f(x_i)$$

b) Use Jensen's inequality to prove:
   - Arithmetic-geometric mean: $$\frac{x_1 + \cdots + x_n}{n} \geq \sqrt[n]{x_1 \cdots x_n}$$
   - Hölder's inequality: $$\sum_{i=1}^n |x_i y_i| \leq \left(\sum_{i=1}^n |x_i|^p\right)^{1/p} \left(\sum_{i=1}^n |y_i|^q\right)^{1/q}$$

c) Derive log-sum inequality

**Task:**
1. A rigorous proof by induction
2. Geometric interpretation
3. Applications in probability
4. Extensions to continuous case

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Proof of Jensen's inequality**

**Base case ($$n = 2$$):** The definition of convexity

**Inductive step:** Assume it holds for $$n-1$$; prove it for $$n$$.

With $$\sum_{i=1}^n \lambda_i = 1$$, let $$\mu = \sum_{i=1}^{n-1} \lambda_i < 1$$.

$$f\left(\sum_{i=1}^n \lambda_i x_i\right) = f\left(\mu \cdot \frac{\sum_{i=1}^{n-1} \lambda_i x_i}{\mu} + (1-\mu) x_n\right)$$

**By convexity:**
$$\leq \mu f\left(\frac{\sum_{i=1}^{n-1} \lambda_i x_i}{\mu}\right) + (1-\mu) f(x_n)$$

**By induction hypothesis:**
$$\leq \mu \sum_{i=1}^{n-1} \frac{\lambda_i}{\mu} f(x_i) + \lambda_n f(x_n) = \sum_{i=1}^n \lambda_i f(x_i)$$

**Step 2: Arithmetic-geometric mean**

**Setup:** $$f(x) = -\log x$$ is convex on $$\mathbb{R}_{++}$$

**Jensen:** $$-\log\left(\frac{x_1 + \cdots + x_n}{n}\right) \leq \frac{1}{n}\sum_{i=1}^n (-\log x_i) = -\frac{1}{n}\log(x_1 \cdots x_n)$$

**Rearranging:** $$\log\left(\frac{x_1 + \cdots + x_n}{n}\right) \geq \log\sqrt[n]{x_1 \cdots x_n}$$

$$\Rightarrow \frac{x_1 + \cdots + x_n}{n} \geq \sqrt[n]{x_1 \cdots x_n}$$

**Step 3: Hölder's inequality**

**Setup:** Use conjugate exponents $$\frac{1}{p} + \frac{1}{q} = 1$$

**Key function:** $$f(t) = e^t$$ convex

**Young's inequality:** for $$a, b > 0$$, Jensen for the convex function $$e^t$$ with weights $$\frac{1}{p}, \frac{1}{q}$$:
$$ab = e^{\frac{1}{p}\log a^p + \frac{1}{q}\log b^q} \leq \frac{1}{p}a^p + \frac{1}{q}b^q$$
**Normalize and sum:** let $$a_i = \frac{|x_i|}{\lVert x \rVert_p}$$, $$b_i = \frac{|y_i|}{\lVert y \rVert_q}$$; then $$\sum_i a_i b_i \leq \frac{1}{p}\sum_i a_i^p + \frac{1}{q}\sum_i b_i^q = \frac{1}{p} + \frac{1}{q} = 1$$, that is:
$$\sum |x_i y_i| \leq \left(\sum |x_i|^p\right)^{1/p} \left(\sum |y_i|^q\right)^{1/q}$$

**Step 4: Log-sum inequality**

**Statement:** $$\sum_{i=1}^n a_i \log \frac{a_i}{b_i} \geq \left(\sum_{i=1}^n a_i\right) \log \frac{\sum_{i=1}^n a_i}{\sum_{i=1}^n b_i}$$

**Proof:** Use Jensen with the convex function $$f(x) = x \log x$$ and appropriate weights.

</details>

---

## 📝 **Exercise 6: Quasiconvex functions**

**Problem:** (Exercise 3.6 from Boyd & Vandenberghe)
a) Verify quasiconvexity of:
   - $$f(x) = \frac{x_1}{x_2}$$ on $$\{x : x_2 > 0\}$$
   - $$f(x) = x_1^2 / x_2$$ on $$\{x : x_2 > 0\}$$
   - $$f(x) = \log(x_1) - \log(x_2)$$ on $$\mathbb{R}_{++}^2$$

b) Prove: $$f$$ is quasiconvex $$\Leftrightarrow$$ its sublevel sets $$\{x : f(x) \leq \alpha\}$$ are convex

c) Operations preserving quasiconvexity

**Task:**
1. Verify using sublevel-set analysis
2. Check first-order conditions
3. Analyze monotonic transformations
4. Compare with convexity

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Ratio function $$f(x) = \frac{x_1}{x_2}$$**

**Sublevel sets:** $$S_\alpha = \{x : x_1 \leq \alpha x_2, x_2 > 0\}$$

**Analysis:** $$S_\alpha = \{x : x_1 - \alpha x_2 \leq 0, x_2 > 0\}$$

Intersection of a halfspace and an (open) halfspace $$\Rightarrow$$ convex

$$\Rightarrow f$$ quasiconvex

**Step 2: $$f(x) = \frac{x_1^2}{x_2}$$**

**Sublevel sets:** $$S_\alpha = \{x : x_1^2 \leq \alpha x_2, x_2 > 0\}$$

**For $$\alpha \leq 0$$:** $$S_\alpha = \{x : x_1 = 0, x_2 > 0\}$$ (convex)

**For $$\alpha > 0$$:** $$S_\alpha = \{x : x_1^2 \leq \alpha x_2, x_2 > 0\}$$

**Second-order cone:** $$\{x : \lVert x_1 \rVert_2 \leq \sqrt{\alpha x_2}, x_2 > 0\}$$ (convex)

$$\Rightarrow f$$ quasiconvex

**Step 3: Log ratio $$f(x) = \log x_1 - \log x_2$$**

**Equivalent:** $$f(x) = \log\frac{x_1}{x_2}$$

**Monotonic transformation:** $$\log$$ increasing, $$\frac{x_1}{x_2}$$ quasiconvex

$$\Rightarrow f$$ quasiconvex

**Step 4: Characterization theorem**

**Theorem:** $$f$$ quasiconvex $$\Leftrightarrow$$ all sublevel sets convex

**Proof ($$\Rightarrow$$):** 
For $$x, y \in S_\alpha$$, $$f(x), f(y) \leq \alpha$$

By quasiconvexity: $$f(\theta x + (1-\theta) y) \leq \max\{f(x), f(y)\} \leq \alpha$$

$$\Rightarrow \theta x + (1-\theta) y \in S_\alpha$$

**Proof ($$\Leftarrow$$):**
If $$f(x), f(y) \leq \alpha$$, then $$x, y \in S_\alpha$$

Since $$S_\alpha$$ is convex: $$\theta x + (1-\theta) y \in S_\alpha$$

$$\Rightarrow f(\theta x + (1-\theta) y) \leq \alpha = \max\{f(x), f(y)\}$$

**Step 5: Operations preserving quasiconvexity**

- **Nonnegative weighted maximum:** $$\max\{f_1, f_2\}$$ quasiconvex
- **Composition with an increasing function:** $$g \circ f$$ is quasiconvex if $$g$$ is increasing
- **Minimization:** Generally not preserved

</details>

---

## 📝 **Exercise 7: Log-concave and log-convex functions**

**Problem:** (Exercise 3.7 from Boyd & Vandenberghe)
a) Verify log-concavity of:
   - Gaussian density: $$f(x) = e^{-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)}$$
   - Gamma function: $$\Gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt$$ (note: $$\Gamma$$ is actually **log-convex**, not log-concave, on $$x > 0$$: each function $$x \mapsto t^{x-1}e^{-t} = e^{(x-1)\log t - t}$$ is log-affine, and an integral of log-convex functions is log-convex)
   - Determinant: $$\det(X)$$ on $$\mathbb{S}_{++}^n$$

b) Applications in probability and statistics

c) Relationship with convexity

**Task:**
1. Verify using second-order conditions
2. Analyze preservation properties
3. Statistical applications
4. Optimization implications

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Gaussian density**

**Function:** $$f(x) = e^{-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)}$$

**Log function:** $$\log f(x) = -\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)$$

**Hessian:** $$\nabla^2 \log f(x) = -\Sigma^{-1} \preceq 0$$

$$\Rightarrow \log f$$ concave $$\Rightarrow f$$ log-concave

**Step 2: Determinant function**

**Function:** $$f(X) = \det(X)$$ on $$\mathbb{S}_{++}^n$$

**Log function:** $$\log f(X) = \log \det(X)$$

**Known result:** $$\log \det(X)$$ is concave on $$\mathbb{S}_{++}^n$$

**Proof sketch:** Hessian analysis or operator concavity

$$\Rightarrow \det(X)$$ log-concave

**Step 3: Preservation properties**

**Products:** If $$f, g$$ are log-concave, then $$fg$$ is log-concave

**Proof:** $$\log(fg) = \log f + \log g$$ (a sum of concave functions)

**Powers:** If $$f$$ is log-concave and $$\alpha \geq 0$$, then $$f^\alpha$$ is log-concave

**Integration:** Log-concavity preserved under integration

**Step 4: Statistical applications**

**Maximum likelihood:** Log-concave likelihoods $$\Rightarrow$$ concave log-likelihood

**Unimodality:** Log-concave densities are unimodal

**Concentration:** Log-concave measures satisfy concentration inequalities

**Step 5: Optimization implications**

**Geometric programming:** Log-convex functions in GP

**Barrier methods:** $$-\log \det(X)$$ as a barrier for the PSD cone

**Exponential families:** Natural parameters and log-partition functions

</details>

---

## 📝 **Exercise 8: Perspective and epigraph**

**Problem:** (Exercise 3.8 from Boyd & Vandenberghe)
a) Let $$f: \mathbb{R}^n \to \mathbb{R}$$ be convex. Prove that the perspective function:
$$g(x, t) = t f(x/t)$$ with $$t > 0$$
is convex on $$\mathbb{R}^n \times \mathbb{R}_{++}$$

b) Applications:
   - $$f(x) = \lVert x \rVert_2 \Rightarrow g(x,t) = \lVert x \rVert_2$$
   - $$f(x) = x^2 \Rightarrow g(x,t) = x^2/t$$
   - $$f(x) = e^x \Rightarrow g(x,t) = t e^{x/t}$$

c) The epigraph characterization of convexity

**Task:**
1. A rigorous proof of convexity of the perspective
2. Geometric interpretation
3. Second-order cone connections
4. Epigraph analysis

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Convexity of the perspective function**

**Theorem:** If $$f$$ is convex, then $$g(x,t) = tf(x/t)$$ is convex on $$\text{dom}(g) = \{(x,t) : x/t \in \text{dom}(f), t > 0\}$$

**Proof:** For $$(x_1, t_1), (x_2, t_2) \in \text{dom}(g)$$ and $$\theta \in [0,1]$$:

$$g(\theta(x_1, t_1) + (1-\theta)(x_2, t_2)) = g(\theta x_1 + (1-\theta) x_2, \theta t_1 + (1-\theta) t_2)$$

$$= (\theta t_1 + (1-\theta) t_2) f\left(\frac{\theta x_1 + (1-\theta) x_2}{\theta t_1 + (1-\theta) t_2}\right)$$

**Key observation:** 
$$\frac{\theta x_1 + (1-\theta) x_2}{\theta t_1 + (1-\theta) t_2} = \frac{\theta t_1}{\theta t_1 + (1-\theta) t_2} \cdot \frac{x_1}{t_1} + \frac{(1-\theta) t_2}{\theta t_1 + (1-\theta) t_2} \cdot \frac{x_2}{t_2}$$

**Convex combination with weights:** $$\frac{\theta t_1}{\theta t_1 + (1-\theta) t_2} + \frac{(1-\theta) t_2}{\theta t_1 + (1-\theta) t_2} = 1$$

**By convexity of $$f$$:**
$$f\left(\frac{\theta x_1 + (1-\theta) x_2}{\theta t_1 + (1-\theta) t_2}\right) \leq \frac{\theta t_1}{\theta t_1 + (1-\theta) t_2} f(x_1/t_1) + \frac{(1-\theta) t_2}{\theta t_1 + (1-\theta) t_2} f(x_2/t_2)$$

**Multiplying by $$\theta t_1 + (1-\theta) t_2$$:**
$$g(\theta(x_1, t_1) + (1-\theta)(x_2, t_2)) \leq \theta t_1 f(x_1/t_1) + (1-\theta) t_2 f(x_2/t_2) = \theta g(x_1, t_1) + (1-\theta) g(x_2, t_2)$$

**Step 2: Applications**

**Example 1:** $$f(x) = \lVert x \rVert_2$$
$$g(x,t) = t \lVert x/t \rVert_2 = \lVert x \rVert_2$$

**Geometric interpretation:** Norm function invariant under perspective

**Example 2:** $$f(x) = x^2$$
$$g(x,t) = t(x/t)^2 = x^2/t$$

**Second-order cone:** $$\{(x,t,s) : x^2/t \leq s, t > 0\} = \{(x,t,s) : \lVert (2x,\ s-t) \rVert_2 \leq s+t,\ t > 0\}$$ (since $$(2x)^2 + (s-t)^2 \leq (s+t)^2 \Leftrightarrow x^2 \leq st$$)

**Example 3:** $$f(x) = e^x$$
$$g(x,t) = te^{x/t}$$

**Exponential cone:** Important in conic optimization

**Step 3: Epigraph characterization**

**Theorem:** $$f$$ convex $$\Leftrightarrow$$ $$\text{epi}(f) = \{(x,t) : f(x) \leq t\}$$ convex

**Proof ($$\Rightarrow$$):** 
For $$(x_1, t_1), (x_2, t_2) \in \text{epi}(f)$$:
$$f(\theta x_1 + (1-\theta) x_2) \leq \theta f(x_1) + (1-\theta) f(x_2) \leq \theta t_1 + (1-\theta) t_2$$

$$\Rightarrow (\theta x_1 + (1-\theta) x_2, \theta t_1 + (1-\theta) t_2) \in \text{epi}(f)$$

**Proof ($$\Leftarrow$$):**
For $$f(x_1) \leq t_1, f(x_2) \leq t_2$$, choose $$t_1 = f(x_1), t_2 = f(x_2)$$

Convexity of the epigraph $$\Rightarrow$$ convexity of $$f$$

</details>

---

## 📝 **Exercise 9: Matrix functions and convexity**

**Problem:** (Exercise 3.9 from Boyd & Vandenberghe)
Analyze the convexity of the following matrix functions:

a) $$f(X) = \text{tr}(X)$$ on $$\mathbb{S}^n$$

b) $$f(X) = \text{tr}(X^2)$$ on $$\mathbb{S}^n$$

c) $$f(X) = \lambda_{\max}(X)$$ on $$\mathbb{S}^n$$

d) $$f(X) = \det(X)$$ on $$\mathbb{S}_{++}^n$$

e) $$f(X) = -\log \det(X)$$ on $$\mathbb{S}_{++}^n$$

**Task:**
1. Verify convexity/concavity
2. Compute subdifferentials
3. Applications in SDP
4. Optimization algorithms

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Trace function $$f(X) = \text{tr}(X)$$**

**Linearity:** $$\text{tr}(\theta X + (1-\theta) Y) = \theta \text{tr}(X) + (1-\theta) \text{tr}(Y)$$

$$\Rightarrow$$ Both convex and concave (affine)

**Subdifferential:** $$\partial f(X) = \{I\}$$

**Step 2: Trace of the square $$f(X) = \text{tr}(X^2)$$**

**Expansion:** $$\text{tr}(X^2) = \sum_{i,j} X_{ij}^2$$

**Convexity:** A sum of convex functions ($$x^2$$)

**Subdifferential:** $$\partial f(X) = \{2X\}$$

**Step 3: Maximum eigenvalue $$f(X) = \lambda_{\max}(X)$$**

**Variational characterization:** $$\lambda_{\max}(X) = \max_{\lVert v \rVert_2 = 1} v^T X v$$

**Convexity:** A maximum of linear functions $$v^T X v$$

**Subdifferential:** $$\partial f(X) = \text{conv}\{vv^T : v \text{ eigenvector of } \lambda_{\max}(X), \lVert v \rVert_2 = 1\}$$

**Step 4: Determinant $$f(X) = \det(X)$$**

**Log-concavity:** $$\log \det(X)$$ concave $$\Rightarrow \det(X)$$ log-concave

**Not convex:** $$\det$$ is neither convex nor concave on $$\mathbb{S}_{++}^n$$ (for $$n \geq 2$$)

**Geometric mean:** $$\det(X)^{1/n} = (\prod \lambda_i)^{1/n}$$ concave

**Step 5: Negative log-determinant $$f(X) = -\log \det(X)$$**

**Convexity:** $$-\log \det(X)$$ is strictly convex on $$\mathbb{S}_{++}^n$$

**Subdifferential:** $$\partial f(X) = \{-X^{-1}\}$$

**Barrier function:** Used in interior-point methods for SDP

**Hessian:** $$\nabla^2 f(X)[H, H] = \text{tr}(X^{-1} H X^{-1} H) > 0$$ for $$H \neq 0$$

**Applications:**
- **SDP barrier:** $$-\log \det(X)$$ as a barrier for $$X \succ 0$$
- **Maximum likelihood:** Covariance estimation
- **Optimal design:** D-optimal experimental design

</details>

---

## 📝 **Exercise 10: Convex optimization applications**

**Problem:** (Exercise 3.10 from Boyd & Vandenberghe)
Formulate the following problems using convex functions:

a) **Robust regression:** Minimize sum of Huber losses
b) **Entropy maximization:** Subject to moment constraints
c) **Geometric mean maximization:** $$\max \prod_{i=1}^n x_i^{1/n}$$ subject to constraints
d) **Relative entropy minimization:** $$\min \sum_{i=1}^n x_i \log(x_i/y_i)$$

**Task:**
1. Identify convex formulations
2. Analyze optimality conditions
3. Suggest solution algorithms
4. Discuss practical applications

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Robust regression**

**Problem:** $$\min_\beta \sum_{i=1}^n \phi(y_i - x_i^T \beta)$$

where the Huber loss is $$\phi(u) = \begin{cases} \frac{1}{2}u^2 & |u| \leq M \\ M|u| - \frac{1}{2}M^2 & |u| > M \end{cases}$$

**Convexity:** $$\phi$$ is convex (piecewise quadratic with a non-decreasing derivative)

**Reformulation:** 
$$\min_{\beta,r,s} \frac{1}{2}\sum_{i=1}^n r_i^2 + M\sum_{i=1}^n s_i$$
$$\text{s.t.} \quad |y_i - x_i^T \beta| \leq r_i + s_i, \quad 0 \leq r_i \leq M, \quad s_i \geq 0$$

**Step 2: Entropy maximization**

**Problem:** $$\max_x -\sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad \sum_{i=1}^n a_{ij} x_i = b_j, \quad x_i \geq 0$$

**Convex formulation:** $$\min_x \sum_{i=1}^n x_i \log x_i$$

**Optimality conditions:** 
$$\log x_i + 1 + \sum_{j=1}^m \lambda_j a_{ij} = 0$$
$$\Rightarrow x_i^* = e^{-1 - \sum_j \lambda_j a_{ij}}$$

**Maximum entropy distribution:** Exponential family form

**Step 3: Geometric mean maximization**

**Problem:** $$\max_{x \geq 0} \prod_{i=1}^n x_i^{1/n} \quad \text{s.t.} \quad Ax \leq b$$

**Log transformation:** $$\max_x \frac{1}{n}\sum_{i=1}^n \log x_i$$

**Convex formulation:** $$\min_x -\sum_{i=1}^n \log x_i \quad \text{s.t.} \quad Ax \leq b, \quad x > 0$$

**Barrier method:** A natural fit for log barriers

**Applications:** Optimal design, Nash bargaining

**Step 4: Relative entropy minimization**

**Problem:** $$\min_x \sum_{i=1}^n x_i \log \frac{x_i}{y_i} \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Convexity:** The KL divergence is convex in its first argument

**Optimality conditions:**
$$\log \frac{x_i}{y_i} + 1 + (A^T \lambda)_i - \mu_i = 0$$ (with $$\mu \geq 0$$ the multiplier for $$x \geq 0$$; since the solution has $$x_i > 0$$, $$\mu_i = 0$$)

**Solution form:** $$x_i^* = y_i e^{-(A^T \lambda^*)_i - 1}$$

**Applications:**
- **Information theory:** Channel capacity
- **Statistics:** Maximum likelihood with a prior
- **Machine learning:** Regularized optimization

</details>

---

## 💡 Practical Tips

#### **When verifying convexity:**
- **Second-order condition:** $$f''(x) \geq 0$$ or $$\nabla^2 f \succeq 0$$
- **Definition:** Check $$f(\theta x + (1-\theta) y) \leq \theta f(x) + (1-\theta) f(y)$$
- **Composition rules:** Use operations that preserve convexity

#### **When computing conjugate functions:**
- **Optimization approach:** $$f^*(y) = \sup_x (y^T x - f(x))$$
- **First-order condition:** $$y \in \partial f(x^*)$$
- **Geometric interpretation:** Supporting hyperplanes

#### **When working with subdifferentials:**
- **Differentiable case:** $$\partial f(x) = \{\nabla f(x)\}$$
- **Non-differentiable:** Use the definition or calculus rules
- **Optimality:** $$0 \in \partial f(x^*)$$

---

## 💡 **Summary**

### **Definition and Tests of Convexity:**

| Method | Condition | When to use |
|--------|-----------|--------------|
| **Definition** | $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$ | Direct proofs |
| **First-order** | $$f(y) \geq f(x) + \nabla f(x)^T(y-x)$$ | Differentiable functions |
| **Second-order** | $$\nabla^2 f(x) \succeq 0$$ | Twice differentiable |
| **Epigraph** | $$\text{epi}(f)$$ convex | Geometric view |

### **Convexity-preserving Operations:**

| Operation | Result |
|-----------|---------|
| **Nonnegative weighted sum** | $$\sum \alpha_i f_i$$ with $$\alpha_i \geq 0$$ |
| **Composition with affine** | $$f(Ax + b)$$ |
| **Pointwise maximum** | $$f(x) = \max\{f_1(x), \ldots, f_m(x)\}$$ |
| **Pointwise supremum** | $$g(x) = \sup_{y \in \mathcal{A}} f(x, y)$$ |
| **Composition rules** | $$h \circ g$$ (requires $$h$$ increasing convex, $$g$$ convex) |
| **Minimization** | $$g(x) = \inf_y f(x, y)$$ if $$f$$ is convex in $$(x,y)$$ |
| **Perspective** | $$g(x, t) = tf(x/t)$$ |

### **Examples of Convex Functions:**

| Function | Domain | Convex? |
|----------|--------|---------|
| **Exponential** | $$e^{ax}$$ | $$\mathbb{R}$$ | ✓ |
| **Powers** | $$x^a$$ | $$\mathbb{R}_{++}$$ | ✓ ($$a \geq 1$$ or $$a \leq 0$$) |
| **Logarithm** | $$-\log x$$ | $$\mathbb{R}_{++}$$ | ✓ |
| **Norms** | $$\|\|x\|\|_p$$ | $$\mathbb{R}^n$$ | ✓ |
| **Max** | $$\max\{x_1, \ldots, x_n\}$$ | $$\mathbb{R}^n$$ | ✓ |
| **Quadratic** | $$x^TQx$$ | $$\mathbb{R}^n$$ | ✓ (if $$Q \succeq 0$$) |
| **Log-sum-exp** | $$\log(\sum e^{x_i})$$ | $$\mathbb{R}^n$$ | ✓ |

### **Conjugate Functions:**

- **Definition:** $$f^*(y) = \sup_x (y^Tx - f(x))$$
- **Fenchel inequality:** $$f(x) + f^*(y) \geq x^Ty$$
- **Conjugate of the conjugate:** $$f^{**} = f$$ (if $$f$$ is closed and convex)
- **Examples:**
  - $$(x^2/2)^* = y^2/2$$
  - $$(\|\|x\|\|)^* = I_{\|\|y\|\|^* \leq 1}$$ (indicator dual norm ball)
  - $$(-\log x)^* = -\log(-y) - 1$$

### **Subdifferential:**

- **Definition:** $$g \in \partial f(x)$$ if $$f(y) \geq f(x) + g^T(y-x)$$ $$\forall y$$
- **Optimality:** $$x^*$$ optimal $$\Leftrightarrow$$ $$0 \in \partial f(x^*)$$
- **Calculus rules:**
  - $$\partial(\alpha f) = \alpha \partial f$$
  - $$\partial(f_1 + f_2) = \partial f_1 + \partial f_2$$
  - $$\partial \max\{f_1, f_2\} = \text{conv}\{\partial f_i : f_i(x) = f(x)\}$$

---

## 📚 References

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 3: Convex Functions
   - Exercises 3.1-3.54

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Hiriart-Urruty, J.-B., & Lemaréchal, C.** (1993). *Convex Analysis and Minimization Algorithms*. Springer.

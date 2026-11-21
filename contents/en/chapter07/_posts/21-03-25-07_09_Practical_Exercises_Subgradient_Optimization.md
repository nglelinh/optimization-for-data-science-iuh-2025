---
layout: post
title: '07-9 Practical Exercises - Subgradient Optimization'
chapter: '07'
order: 10
owner: GitHub Copilot
lang: en
categories:
- chapter07
lesson_type: required
---

# Practical Exercises - Subgradient Optimization

The exercises are adapted from Boyd & Vandenberghe (2004) and Shor (1985).

---

## 📝 **Part I: Computing Subgradients**

### **Exercise 1: Subgradients of Non-differentiable Functions**

Compute the subgradients of the following functions at the given points:

**a)** $$f(x) = |x|$$ at $$x = 0$$

**b)** $$f(x) = \max\{x_1, x_2\}$$ at $$x = (1, 1)^T$$

**c)** $$f(x) = \|x\|_1$$ at $$x = (0, 0)^T$$

**d)** $$f(x) = \max\{x_1 + x_2, 2x_1 - x_2\}$$ at $$x = (1, 0)^T$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) $$f(x) = |x|$$ at $$x = 0$$:**

**Definition:** $$g \in \partial f(0)$$ if

$$f(y) \geq f(0) + g(y - 0)$$ $$\forall y$$

$$|y| \geq 0 + gy \quad \forall y$$

- For $$y > 0$$: $$y \geq gy$$ → $$g \leq 1$$
- For $$y < 0$$: $$-y \geq gy$$ → $$g \geq -1$$

$$\partial f(0) = [-1, 1]$$

**Geometric interpretation:** the set of all slopes of the supporting lines at $$x = 0$$.

---

**b) $$f(x) = \max\{x_1, x_2\}$$ at $$x = (1, 1)$$:**

$$f(1, 1) = 1$$ (both are active)

**Active set:** $$I = \{1, 2\}$$

$$\partial f(x) = \text{conv}\{\nabla f_i(x) : i \in I\}$$

$$= \text{conv}\{(1, 0), (0, 1)\}$$

$$= \{(\lambda, 1-\lambda) : 0 \leq \lambda \leq 1\}$$

**Geometry:** the line segment joining $$(1, 0)$$ and $$(0, 1)$$.

---

**c) $$f(x) = \|x\|_1 = |x_1| + |x_2|$$ at $$x = (0, 0)$$:**

$$\partial f(0) = \partial |x_1| \times \partial |x_2|$$

$$= [-1, 1] \times [-1, 1]$$

$$= \{(g_1, g_2) : |g_1| \leq 1, |g_2| \leq 1\}$$

**Geometry:** the square $$[-1, 1]^2$$.

---

**d) $$f(x) = \max\{x_1 + x_2, 2x_1 - x_2\}$$ at $$x = (1, 0)$$:**

$$f_1(1, 0) = 1 + 0 = 1$$

$$f_2(1, 0) = 2 - 0 = 2$$

$$\Rightarrow f(1, 0) = 2$$ (only $$f_2$$ is active)

$$\nabla f_2 = (2, -1)$$

$$\partial f(1, 0) = \{(2, -1)\}$$ (a singleton because only one function is active)

</details>

---

## 📝 **Part II: The Subgradient Method**

### **Exercise 2: Convergence Analysis**

Cho $$f(x) = |x - 2| + |x + 1|$$.

**Tasks:**  
a) Find $$x^*$$ (the minimizer)  
b) With step size $$\alpha_k = \frac{1}{\sqrt{k}}$$, iterate from $$x^{(0)} = 5$$  
c) Compute $$x^{(1)}, x^{(2)}, x^{(3)}$$  
d) Estimate the convergence rate

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Find $$x^*$$:**

$$f(x) = |x - 2| + |x + 1|$$

**Case analysis:**
- $$x < -1$$: $$f(x) = -(x-2) - (x+1) = -2x + 1$$ (decreasing)
- $$-1 \leq x \leq 2$$: $$f(x) = -(x-2) + (x+1) = 3$$ (constant!)
- $$x > 2$$: $$f(x) = (x-2) + (x+1) = 2x - 1$$ (increasing)

$$f^* = 3$$, $$x^* \in [-1, 2]$$

---

**b) Subgradient method:**

$$x^{(k+1)} = x^{(k)} - \alpha_k g^{(k)}$$

with $$g^{(k)} \in \partial f(x^{(k)})$$.

---

**c) Iterations:**

$$x^{(0)} = 5 > 2$$

$$\partial f(5) = \{\text{sign}(5-2)\} + \{\text{sign}(5+1)\} = \{1\} + \{1\} = \{2\}$$

$$g^{(0)} = 2$$

$$\alpha_0 = \frac{1}{\sqrt{1}} = 1$$

$$x^{(1)} = 5 - 1 \cdot 2 = 3$$

---

$$x^{(1)} = 3 > 2$$

$$g^{(1)} = 2$$

$$\alpha_1 = \frac{1}{\sqrt{2}} \approx 0.707$$

$$x^{(2)} = 3 - 0.707 \cdot 2 = 1.586$$

---

$$x^{(2)} = 1.586 \in [-1, 2]$$ (optimal region!)

$$\partial f(1.586) = \{\text{sign}(1.586 - 2) + \text{sign}(1.586 + 1)\} = \{-1 + 1\} = \{0\}$$ (on $$(-1, 2)$$, $$f$$ is constant, hence differentiable with gradient 0)

$$g^{(2)} = 0 \Rightarrow x^{(3)} = x^{(2)} = 1.586$$ (already converged to the optimal set)

---

**d) Convergence rate:**

With $$\alpha_k = \frac{1}{\sqrt{k}}$$:

$$f(x_{\text{best}}^{(k)}) - f^* \leq \frac{R^2 + G^2 \sum_{i=1}^k \alpha_i^2}{2\sum_{i=1}^k \alpha_i}$$

$$\sum_{i=1}^k \frac{1}{\sqrt{i}} \approx 2\sqrt{k}$$

$$\sum_{i=1}^k \frac{1}{i} \approx \log k$$

$$\Rightarrow O\left(\frac{\log k}{\sqrt{k}}\right) = O\left(\frac{1}{\sqrt{k}}\right)$$

**Sublinear convergence** (slower than gradient descent!)

</details>

---

## 📝 **Part III: Step Size Rules**

### **Exercise 3: Comparing Step Size Strategies**

Cho $$f(x) = \max\{x_1, x_2, -x_1 - x_2 + 1\}$$.

**Tasks:**  
a) Find $$x^*$$ graphically  
b) Compare 3 step size rules:
   - Constant: $$\alpha_k = 0.1$$
   - Diminishing: $$\alpha_k = \frac{1}{k}$$
   - Square summable: $$\alpha_k = \frac{1}{k^{0.6}}$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Graphical solution:**

$$f(x) = \max\{x_1, x_2, 1 - x_1 - x_2\}$$

**Intersection points:**
- $$x_1 = x_2$$: Line $$x_1 = x_2$$
- $$x_1 = 1 - x_1 - x_2$$: $$2x_1 + x_2 = 1$$
- $$x_2 = 1 - x_1 - x_2$$: $$x_1 + 2x_2 = 1$$

Solve the system $$x_1 = x_2$$ and $$2x_1 + x_2 = 1$$:

$$3x_1 = 1 \Rightarrow x_1 = \frac{1}{3}$$

$$x^* = \left(\frac{1}{3}, \frac{1}{3}\right)$$, $$f^* = \frac{1}{3}$$

---

**b) Step size comparison:**

**From $$x^{(0)} = (1, 1)$$:**

$$f_1 = 1$$, $$f_2 = 1$$, $$f_3 = -1$$ → the max is $$f_1, f_2$$ (tie)

$$\partial f(1, 1) = \text{conv}\{(1, 0), (0, 1)\}$$

Choose $$g = (0.5, 0.5)$$ (the midpoint)

---

**Constant $$\alpha_k = 0.1$$:**

$$x^{(1)} = (1, 1) - 0.1(0.5, 0.5) = (0.95, 0.95)$$

$$x^{(2)} = (0.90, 0.90)$$

$$x^{(3)} = (0.85, 0.85)$$

...

**Converges to a neighborhood of $$x^*$$ (radius $$O(\alpha)$$), but does not reach it exactly.**

---

**Diminishing $$\alpha_k = \frac{1}{k}$$:**

$$x^{(1)} = (1, 1) - 1 \cdot (0.5, 0.5) = (0.5, 0.5)$$

$$x^{(2)} = (0.5, 0.5) - 0.5 \cdot (0.5, 0.5) = (0.25, 0.25)$$ (with $$g^{(1)} = (0.5, 0.5)$$)

At $$(0.25, 0.25)$$: $$f_3 = 0.5$$ is the largest, $$g^{(2)} = (-1, -1)$$, so $$x^{(3)} = (0.25, 0.25) + \frac{1}{3}(1, 1) \approx (0.583, 0.583)$$ (the iterates oscillate around $$x^*$$ with decreasing amplitude).

...

**Converges to $$x^*$$, but very slowly (bound $$O(1/\log k)$$ since $$\sum_{i \le k} 1/i \approx \log k$$).**

---

**Square summable $$\alpha_k = \frac{1}{k^{0.6}}$$:**

$$\sum \alpha_k = \sum \frac{1}{k^{0.6}} = \infty$$ ✓

$$\sum \alpha_k^2 = \sum \frac{1}{k^{1.2}} < \infty$$ ✓

**Converges to $$x^*$$ with bound $$O(1/k^{0.4})$$ (since $$\sum_{i \le k} \alpha_i \sim k^{0.4}$$), faster than $$\alpha_k = 1/k$$ but still sublinear.**

</details>

---

## 📝 **Part IV: Polyak Step Size**

### **Exercise 4: Polyak's Step Size for $$\ell_1$$ Minimization**

$$\min_{x} \|x\|_1 \quad \text{s.t.} \quad Ax = b$$

with $$A = [1, 2, 3]$$, $$b = 6$$.

**Tasks:**  
a) Write the Lagrangian  
b) Find the dual function  
c) Maximize the dual by subgradient method with Polyak step size

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Lagrangian:**

$$L(x, \nu) = \|x\|_1 + \nu^T(Ax - b)$$

$$= \sum_i (|x_i| + \nu a_i x_i) - \nu b$$

---

**b) Dual function:**

$$g(\nu) = \inf_x L(x, \nu)$$

$$= \inf_x \sum_i (|x_i| + \nu a_i x_i) - \nu b$$

Minimize over each $$x_i$$ independently:

$$\inf_{x_i} (|x_i| + \nu a_i x_i) = \begin{cases}
0 & \text{if } |\nu a_i| \leq 1 \\
-\infty & \text{otherwise}
\end{cases}$$

$$g(\nu) = \begin{cases}
-\nu b & \text{if } |\nu a_i| \leq 1 \, \forall i \\
-\infty & \text{otherwise}
\end{cases}$$

With $$A = [1, 2, 3]$$:

$$|\nu| \leq 1, \quad |2\nu| \leq 1, \quad |3\nu| \leq 1$$

$$\Rightarrow |\nu| \leq \frac{1}{3}$$

$$g(\nu) = -6\nu$$ for $$|\nu| \leq \frac{1}{3}$$

---

**c) Dual maximization:**

$$\max_{\nu} \quad -6\nu \quad \text{s.t.} \quad -\frac{1}{3} \leq \nu \leq \frac{1}{3}$$

**Obvious:** $$\nu^* = -\frac{1}{3}$$, $$g^* = 2$$

**Subgradient of $$g(\nu) = -6\nu$$:** $$s = -6$$ (since we maximize the concave function $$g$$, we use subgradient ascent).

**Polyak step size** (knowing $$g^* = 2$$):

$$\alpha_k = \frac{g^* - g(\nu^{(k)})}{\|s^{(k)}\|^2}, \qquad \nu^{(k+1)} = \Pi_{[-1/3,\,1/3]}\left(\nu^{(k)} + \alpha_k s^{(k)}\right)$$

From $$\nu^{(0)} = 0$$: $$g(0) = 0$$

$$\alpha_0 = \frac{2 - 0}{36} = \frac{1}{18}$$

$$\nu^{(1)} = 0 + \frac{1}{18} \cdot (-6) = -\frac{1}{3}$$ ✓ (inside the domain)

**Converged in 1 step!** ($$g(-1/3) = 2 = g^*$$, and the primal solution is $$x^* = (0, 0, 2)$$ with $$\|x^*\|_1 = 2$$.)

</details>

---

## 📝 **Part V: Projected Subgradient**

### **Exercise 5: Projected Subgradient for Constrained Optimization**

$$\min_{x} \|x - c\|_1 \quad \text{s.t.} \quad \|x\|_2 \leq R$$

with $$c = (2, 3)^T$$, $$R = 2$$.

**Tasks:**  
a) Write the projected subgradient update  
b) Iterate from $$x^{(0)} = (0, 0)$$  
c) Find the exact solution

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Projected subgradient:**

$$x^{(k+1)} = \Pi_C\left(x^{(k)} - \alpha_k g^{(k)}\right)$$

with $$C = \{x : \|x\|_2 \leq R\}$$, $$g^{(k)} \in \partial f(x^{(k)})$$.

**Projection onto $$\ell_2$$ ball:**

$$\Pi_C(y) = \begin{cases}
y & \text{if } \|y\| \leq R \\
R \frac{y}{\|y\|} & \text{if } \|y\| > R
\end{cases}$$

---

**b) Iterations:**

$$x^{(0)} = (0, 0)$$

$$\partial f(0, 0) = \partial \|(0, 0) - (2, 3)\|_1 = \partial(|{-2}| + |{-3}|)$$

Subgradient: $$g = \text{sign}(x - c) = (-1, -1)$$

Choose $$\alpha_0 = 1$$:

$$\tilde{x}^{(1)} = (0, 0) - 1 \cdot (-1, -1) = (1, 1)$$

$$\|\tilde{x}^{(1)}\| = \sqrt{2} < 2$$ → no projection needed

$$x^{(1)} = (1, 1)$$

---

$$g^{(1)} = \text{sign}((1, 1) - (2, 3)) = (-1, -1)$$

$$\tilde{x}^{(2)} = (1, 1) + (1, 1) = (2, 2)$$

$$\|\tilde{x}^{(2)}\| = 2\sqrt{2} > 2$$ → project!

$$x^{(2)} = 2 \cdot \frac{(2, 2)}{2\sqrt{2}} = \frac{2}{\sqrt{2}}(1, 1) = (\sqrt{2}, \sqrt{2})$$

---

**c) Exact solution:**

Minimize $$\|x - c\|_1$$ over $$\|x\| \leq 2$$.

**Unconstrained optimum:** $$x = c = (2, 3)$$

$$\|c\| = \sqrt{13} > 2$$ → infeasible!

**Constrained optimum:** since $$c$$ lies outside the ball, the solution lies on the boundary $$\|x\|_2 = 2$$. (Note: projecting $$c$$ onto the ball is optimal only for the $$\ell_2$$ distance, not for $$\ell_1$$.) On the boundary with $$x_1 < 2$$, $$x_2 < 3$$:

$$f(x) = (2 - x_1) + (3 - x_2) = 5 - (x_1 + x_2)$$

so the problem becomes $$\max\; x_1 + x_2$$ on the circle $$x_1^2 + x_2^2 = 4$$, attained at $$x_1 = x_2 = \sqrt{2}$$:

$$x^* = (\sqrt{2}, \sqrt{2}) \approx (1.414, 1.414)$$

**Objective:** $$f(x^*) = 5 - 2\sqrt{2} \approx 2.172$$ (the projected point $$\frac{2}{\sqrt{13}}(2,3)$$ gives $$2.227$$, which is worse). This is exactly the point reached by projected subgradient at $$x^{(2)}$$.

</details>

---

## 💡 **Summary**

### **Subgradient Method Properties:**

| Aspect | Gradient Descent | Subgradient Method |
|--------|------------------|-------------------|
| **Applicability** | Smooth $$f$$ | Non-smooth $$f$$ |
| **Convergence** | Linear ($$O(\rho^k)$$) | Sublinear ($$O(1/\sqrt{k})$$) |
| **Step size** | Fixed or line search | Diminishing or Polyak |
| **Descent** | Always decreases | May increase! |
| **Usage** | Well-behaved $$f$$ | $$\ell_1$$, max, constraints |

### **Step Size Rules:**

1. **Constant $$\alpha$$:** Converges to neighborhood
2. **Diminishing $$\frac{1}{k}$$:** Converges exactly but very slowly (bound $$O(1/\log k)$$)
3. **Square summable $$\frac{1}{k^{0.6}}$$:** Converges exactly with bound $$O(1/k^{0.4})$$, faster than $$\frac{1}{k}$$
4. **Polyak:** Fast if $$f^*$$ known

### **When to use the subgradient method:**
- Non-differentiable $$f$$ ($$\ell_1$$, max)
- Simple per-iteration cost needed
- Willing to accept slow convergence
- Constraints via projection

---

## 📚 **References**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Section 3.1.

2. **Shor, N. Z.** (1985). *Minimization Methods for Non-Differentiable Functions*. Springer.

3. **Polyak, B. T.** (1987). *Introduction to Optimization*. Optimization Software.


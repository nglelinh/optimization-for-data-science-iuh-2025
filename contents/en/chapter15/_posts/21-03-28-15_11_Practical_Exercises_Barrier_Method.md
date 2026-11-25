---
layout: post
title: '15-11 Practical Exercises - Barrier Method'
chapter: '15'
order: 17
owner: GitHub Copilot
lang: en
categories:
- chapter15
lesson_type: required
redirect_from:
  - /contents/en/chapter15/15_10_Practical_Exercises_Barrier_Method/
---

Working through barrier-method exercises by hand builds deep intuition for what modern solvers like Clarabel do inside every iteration: computing exact barrier gradients and Hessians, deriving closed-form central paths on small LPs and QPs, verifying the $$m/t$$ duality gap, and formulating Phase I feasibility problems. Keep this four-pillar playbook handy as you solve the exercises below.

## Background Knowledge Map: Exercise-Solving Playbook for Chapter 15

- **Pillar 1 — Sign Hygiene in $$\phi(x)$$:** Always rewrite every inequality in the canonical form $$h_i(x) \le 0$$ first (so $$-h_i(x) > 0$$ inside the logarithm!). For example, $$x \ge a$$ becomes $$h(x) = a - x \le 0$$, giving $$-\log(x - a)$$.
- **Pillar 2 — Computing Central Paths Analytically:** Set $$t\nabla f(x) + \nabla\phi(x) = 0$$, clear denominators to obtain a polynomial equation, and select the unique root lying strictly inside the feasible domain $$h_i(x) < 0$$.
- **Pillar 3 — Dual Variable & Gap Verification:** After finding $$x^*(t)$$, always compute $$u_i(t) = -\frac{1}{t h_i(x^*(t))}$$ and check both stationarity and $$f(x^*(t)) - f^\star \le \frac{m}{t}$$ as a built-in algebraic error detector.
- **Pillar 4 — Newton Step Inside the Barrier:** Remember to include **both** $$t\nabla^2 f(x)$$ and $$\nabla^2 \phi(x)$$ in the Hessian of the centering problem, and never let a trial step jump outside $$h_i(x + tv) < 0$$ during backtracking.

### Step-by-Step Worked Example (Read Slowly): One Full Centering Newton Step on a Barrier Problem

Minimize $$f(x) = 2x$$ subject to $$x \ge 1$$ ($$h_1(x) = 1 - x \le 0$$) using the barrier problem $$\Phi_t(x) = 2tx - \log(x - 1)$$ at $$t = 1$$, starting from the strictly feasible point $$x^{(0)} = 2$$.

1. **Compute exact central-path target (for reference):**
   $$\Phi_1'(x) = 2 - \frac{1}{x - 1} = 0 \implies x^*(1) = 1.5.$$
2. **Compute gradient and Hessian of $$\Phi_1(x)$$ at $$x^{(0)} = 2$$:**
   - $$\Phi_1'(2) = 2 - \frac{1}{2 - 1} = 1$$.
   - $$\Phi_1''(2) = \frac{1}{(2 - 1)^2} = 1$$.
3. **Compute the pure Newton step:**
   $$\Delta x_{\text{nt}} = -\frac{\Phi_1'(2)}{\Phi_1''(2)} = -\frac{1}{1} = -1 \implies x^{(0)} + \Delta x_{\text{nt}} = 2 - 1 = 1!$$
4. **Domain-safety catch!** Notice $$x = 1$$ lands right on the boundary where $$\log(x - 1) = -\infty$$! Backtracking immediately halves $$t_{\text{step}} = 0.5$$:
   $$x^{(1)} = 2 + 0.5(-1) = 1.5 = x^*(1)!$$
   This tiny example illustrates *both* why domain-checking in backtracking is mandatory and how rapidly Newton centers once inside the domain.

# Practical Exercises - The Barrier Method

The exercises are adapted from Boyd & Vandenberghe (2004), Nocedal & Wright (2006), and Nesterov (2004).

---

## 📝 **Part I: The Log-Barrier Function**

### **Exercise 1: Computing the Log-Barrier (Boyd & Vandenberghe, Ex. 11.1)**

Consider the problem:

$$
\begin{align}
\min_{x} \quad & f(x) \\
\text{s.t.} \quad & h_i(x) \leq 0, \quad i = 1, \ldots, m
\end{align}
$$

Log-barrier function:

$$
\phi(x) = -\sum_{i=1}^m \log(-h_i(x))
$$

**Tasks:**  
a) Compute $$\nabla \phi(x)$$ and $$\nabla^2 \phi(x)$$  
b) Let $$f(x) = x^2$$, $$h_1(x) = x - 1$$, $$h_2(x) = -x - 1$$ (i.e. $$-1 \leq x \leq 1$$). Compute $$\phi(x)$$, $$\nabla \phi(x)$$, $$\nabla^2 \phi(x)$$  
c) Evaluate the quantities above at $$x = 0$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Gradient and Hessian of $$\phi(x)$$:**

**Gradient:**

$$
\nabla \phi(x) = -\sum_{i=1}^m \frac{1}{-h_i(x)} \nabla h_i(x) = \sum_{i=1}^m \frac{\nabla h_i(x)}{-h_i(x)}
$$

**Hessian:**

$$
\nabla^2 \phi(x) = \sum_{i=1}^m \left( \frac{\nabla^2 h_i(x)}{-h_i(x)} + \frac{\nabla h_i(x) \nabla h_i(x)^T}{h_i(x)^2} \right)
$$

---

**b) A concrete example:**

$$
f(x) = x^2, \quad h_1(x) = x - 1, \quad h_2(x) = -x - 1
$$

**Barrier function:**

$$
\phi(x) = -\log(-(x-1)) - \log(-(-x-1)) = -\log(1-x) - \log(1+x)
$$

**Gradient:**

$$
\nabla h_1(x) = 1, \quad \nabla h_2(x) = -1
$$

$$
\nabla \phi(x) = \frac{1}{1-x} + \frac{-1}{1+x} = \frac{1+x-(1-x)}{(1-x)(1+x)} = \frac{2x}{1-x^2}
$$

**Hessian:**

$$
\nabla^2 h_1(x) = 0, \quad \nabla^2 h_2(x) = 0
$$

$$
\nabla^2 \phi(x) = \frac{1}{(1-x)^2} + \frac{1}{(1+x)^2}
$$

$$
= \frac{(1+x)^2 + (1-x)^2}{(1-x^2)^2} = \frac{2(1+x^2)}{(1-x^2)^2}
$$

---

**c) At $$x = 0$$:**

$$
\phi(0) = -\log(1) - \log(1) = 0
$$

$$
\nabla \phi(0) = \frac{0}{1} = 0
$$

$$
\nabla^2 \phi(0) = \frac{2 \cdot 1}{1} = 2
$$

**Explanation:** At the center of the feasible region ($$x=0$$), the barrier function attains its minimum and the gradient is 0.

</details>

---

### **Exercise 2: Central Path (Boyd & Vandenberghe, Ex. 11.2)**

Continuing Exercise 1, consider the barrier problem:

$$
\min_x \quad t f(x) + \phi(x) = t x^2 - \log(1-x) - \log(1+x)
$$

**Tasks:**  
a) Find the first-order condition (FOC)  
b) Solve the FOC to find $$x^*(t)$$ (a central path point)  
c) Compute $$x^*(1)$$, $$x^*(10)$$, $$x^*(100)$$  
d) What is $$x^*(t)$$ as $$t \to \infty$$?

<details>
<summary><strong>💡 Solution</strong></summary>

**a) FOC:**

$$
\frac{d}{dx}\left( t x^2 - \log(1-x) - \log(1+x) \right) = 0
$$

$$
2tx + \frac{1}{1-x} - \frac{1}{1+x} = 0
$$

$$
2tx + \frac{2x}{1-x^2} = 0
$$

$$
x\left( 2t + \frac{2}{1-x^2} \right) = 0
$$

**Two cases:**
1. $$x = 0$$ (always a solution, by symmetry)
2. $$2t + \frac{2}{1-x^2} = 0$$ (no real solution since the left-hand side is > 0)

**Conclusion:** $$x^*(t) = 0$$ for all $$t > 0$$.

---

**b) Explanation:**

Since $$f(x) = x^2$$ is symmetric about $$x=0$$ and the feasible region $$(-1, 1)$$ is also symmetric, the central path is $$x^*(t) = 0$$ for every $$t$$.

---

**c) Values:**

$$
x^*(1) = 0, \quad x^*(10) = 0, \quad x^*(100) = 0
$$

---

**d) Limit:**

$$
\lim_{t \to \infty} x^*(t) = 0
$$

This is exactly the solution of the original problem: $$\min_{-1 \leq x \leq 1} x^2 = 0$$ at $$x = 0$$.

**Note:** This is a special case. Normally, the central path moves as $$t$$ increases.

</details>

---

## 📝 **Part II: Central Path Analysis**

### **Exercise 3: Central Path for an LP (Nocedal & Wright, Ex. 14.1)**

Consider the LP:

$$
\begin{align}
\min_{x} \quad & c^T x \\
\text{s.t.} \quad & Ax = b \\
& x \geq 0
\end{align}
$$

With $$c = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$$, $$A = \begin{bmatrix} 1 & 1 \end{bmatrix}$$, $$b = 1$$.

**Tasks:**  
a) Write the barrier problem  
b) Find the central path $$x^*(t)$$  
c) Compute $$\lim_{t \to \infty} x^*(t)$$  
d) Compare with the primal-dual solution

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Barrier problem:**

$$
\min_x \quad t c^T x - \sum_{i=1}^2 \log x_i \quad \text{s.t.} \quad x_1 + x_2 = 1
$$

$$
= \min_x \quad -t(x_1 + x_2) - \log x_1 - \log x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1
$$

---

**b) Find the central path:**

**Lagrangian:**

$$
L(x, \nu) = -t(x_1 + x_2) - \log x_1 - \log x_2 - \nu(x_1 + x_2 - 1)
$$

**FOC:**

$$
\frac{\partial L}{\partial x_1} = -t - \frac{1}{x_1} - \nu = 0 \Rightarrow \frac{1}{x_1} = -t - \nu
$$

$$
\frac{\partial L}{\partial x_2} = -t - \frac{1}{x_2} - \nu = 0 \Rightarrow \frac{1}{x_2} = -t - \nu
$$

From the two equations → $$x_1 = x_2$$.

From $$x_1 + x_2 = 1$$: $$x_1 = x_2 = 0.5$$.

**Central path:**

$$
x^*(t) = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix} \quad \forall t > 0
$$

**Dual variable:**

$$
\frac{1}{0.5} = -t - \nu \Rightarrow \nu = -t - 2
$$

---

**c) Limit:**

$$
\lim_{t \to \infty} x^*(t) = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}
$$

**Check against the original problem:**

$$
\min -x_1 - x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1, \quad x \geq 0
$$

Optimal value: $$-1$$ at any $$x$$ satisfying $$x_1 + x_2 = 1$$, $$x \geq 0$$.

Optimal set: the line segment from $$(0,1)$$ to $$(1,0)$$.

The central path converges to the **analytic center** of the optimal set ($$x_1 = x_2 = 0.5$$).

---

**d) Primal-dual comparison:**

**Dual problem:**

$$
\max_{\nu} \quad \nu \quad \text{s.t.} \quad \begin{bmatrix} \nu \\ \nu \end{bmatrix} \leq \begin{bmatrix} -1 \\ -1 \end{bmatrix}
$$

$$\nu \leq -1$$ → $$\nu^* = -1$$.

**Duality gap:**

$$
\text{gap}(t) = c^T x^*(t) - b^T y(t)
$$

The dual feasible point obtained from the central path: $$\lambda_i(t) = \frac{1}{t x_i^*(t)} = \frac{2}{t}$$ and $$y(t) = \frac{\nu(t)}{t} = -1 - \frac{2}{t} \leq -1$$ (feasible for the dual). The dual value is $$b^Ty(t) = -1 - \frac{2}{t}$$, hence

$$
\text{gap}(t) = -1 - \left(-1 - \frac{2}{t}\right) = \frac{2}{t} = \frac{m}{t}
$$

The gap is **nonzero** for every finite $$t$$ and $$\to 0$$ as $$t \to \infty$$ (exactly the formula $$m/t$$ with $$m = 2$$).

**Note:** The formula $$\text{gap} = m/t$$ always holds on the central path; the gap is 0 only when compared with the optimal dual value $$\nu^* = -1$$, i.e. in the limit $$t \to \infty$$.

</details>

---

## 📝 **Part III: Perturbed KKT Conditions**

### **Exercise 4: KKT Conditions with the Barrier (Boyd & Vandenberghe, Ex. 11.4)**

Consider the barrier problem:

$$
\min_x \quad t f(x) + \phi(x)
$$

**Tasks:**  
a) Write the KKT conditions for the barrier problem  
b) Prove: if $$x^*(t)$$ satisfies the KKT conditions of the barrier problem, then there exists $$\lambda^*(t)$$ such that:

$$
\begin{align}
\nabla f(x^*(t)) + \sum_i \lambda_i^*(t) \nabla h_i(x^*(t)) &= 0 \\
\lambda_i^*(t) &= -\frac{1}{t h_i(x^*(t))} \\
h_i(x^*(t)) &< 0
\end{align}
$$

c) Compute $$\lambda_i^*(t) h_i(x^*(t))$$  
d) What happens as $$t \to \infty$$?

<details>
<summary><strong>💡 Solution</strong></summary>

**a) KKT for the barrier problem:**

$$
\min_x \quad t f(x) + \phi(x) = t f(x) - \sum_i \log(-h_i(x))
$$

**FOC:**

$$
t \nabla f(x) + \nabla \phi(x) = 0
$$

$$
t \nabla f(x) + \sum_i \frac{\nabla h_i(x)}{-h_i(x)} = 0
$$

---

**b) Proof of the perturbed KKT conditions:**

Define:

$$
\lambda_i^*(t) := -\frac{1}{t h_i(x^*(t))}
$$

Substitute into the FOC:

$$
t \nabla f(x^*) + \sum_i \frac{\nabla h_i(x^*)}{-h_i(x^*)} = 0
$$

$$
\nabla f(x^*) + \sum_i \frac{1}{-t h_i(x^*)} \nabla h_i(x^*) = 0
$$

$$
\nabla f(x^*) + \sum_i \left(-\frac{1}{t h_i(x^*)}\right) \nabla h_i(x^*) = 0
$$

$$
\nabla f(x^*) + \sum_i \lambda_i^*(t) \nabla h_i(x^*) = 0
$$

✓ This is exactly the stationarity condition of KKT!

**Feasibility:**

Since $$x^*$$ is strictly feasible for the barrier problem: $$h_i(x^*) < 0$$ ✓

**Dual feasibility:**

$$
\lambda_i^* = -\frac{1}{t h_i(x^*)} > 0 \quad \text{(since } h_i(x^*) < 0 \text{)}
$$

✓

---

**c) Complementary slackness (perturbed):**

$$
\lambda_i^*(t) h_i(x^*(t)) = -\frac{1}{t h_i(x^*)} \cdot h_i(x^*) = -\frac{1}{t}
$$

**Not zero!** This is **perturbed complementary slackness**.

---

**d) As $$t \to \infty$$:**

$$
\lambda_i^*(t) h_i(x^*(t)) = -\frac{1}{t} \to 0
$$

**Perturbed KKT conditions** → **exact KKT conditions**.

$$x^*(t) \to x^*$$, $$\lambda^*(t) \to \lambda^*$$ (the true optimal solution).

**Duality gap:**

$$
\text{gap}(t) = f(x^*(t)) - g(\lambda^*(t), \nu^*(t)) = \frac{m}{t}
$$

where $$m$$ = the number of inequality constraints.

</details>

---

## 📝 **Part IV: Convergence Analysis**

### **Exercise 5: Duality Gap and Convergence (Boyd & Vandenberghe, Theorem 11.2)**

Consider the barrier method with parameter $$t^{(k)} = \mu^k t^{(0)}$$, $$\mu > 1$$.

**Tasks:**  
a) Prove that the duality gap after $$k$$ iterations is $$\text{gap}^{(k)} = \frac{m}{t^{(k)}}$$  
b) How many outer iterations are needed to reach $$\text{gap} < \epsilon$$?  
c) For $$m = 100$$, $$\mu = 10$$, $$\epsilon = 10^{-6}$$, compute the number of iterations  
d) Total number of Newton iterations (assume each outer iteration needs $$\approx 10$$ Newton steps)

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Duality gap:**

At iteration $$k$$, the central path point $$x^*(t^{(k)})$$ satisfies the perturbed KKT conditions:

$$
\lambda_i^*(t^{(k)}) h_i(x^*(t^{(k)})) = -\frac{1}{t^{(k)}}
$$

**Duality gap:**

$$
\eta(t^{(k)}) = f(x^*(t^{(k)})) - g(\lambda^*(t^{(k)}), \nu^*(t^{(k)}))
$$

By barrier method theory (Boyd & Vandenberghe, Theorem 11.2):

$$
\eta(t) = \frac{m}{t}
$$

where $$m$$ = the number of inequality constraints.

---

**b) Required number of iterations:**

Condition: $$\frac{m}{t^{(k)}} < \epsilon$$

$$
t^{(k)} > \frac{m}{\epsilon}
$$

With $$t^{(k)} = \mu^k t^{(0)}$$:

$$
\mu^k t^{(0)} > \frac{m}{\epsilon}
$$

$$
k > \frac{\log(m/(\epsilon t^{(0)}))}{\log \mu}
$$

If we start with $$t^{(0)} = 1$$:

$$
k > \frac{\log(m/\epsilon)}{\log \mu}
$$

---

**c) Numerical computation:**

$$
k > \frac{\log(100/10^{-6})}{\log 10} = \frac{\log(10^8)}{\log 10} = 8
$$

**Number of outer iterations:** $$k > 8$$, so we need $$k = 9$$ (for $$k = 8$$ the gap is $$m/\mu^8 = 10^{-6} = \epsilon$$, which is not strictly smaller than $$\epsilon$$)

---

**d) Total Newton iterations:**

Assume each outer iteration needs $$\approx 10$$ Newton steps:

$$
\text{Total Newton iters} \approx 9 \times 10 = 90
$$

**Analysis:**
- Barrier method with fixed $$\mu$$: $$O(\log(m/\epsilon))$$ outer iterations
- With $$\mu = 1 + 1/\sqrt{m}$$ (short-step): $$O(\sqrt{m}\log(m/\epsilon))$$ outer iterations, each needing only $$O(1)$$ Newton steps
- Total Newton steps (in theory): $$O(\sqrt{m} \log(m/\epsilon))$$

For this problem ($$\mu = 10$$ is large): few outer iterations, but possibly more Newton steps per iteration.

</details>

---

## 📝 **Part V: Feasibility and Phase I**

### **Exercise 6: Phase I Method (Nocedal & Wright, Ex. 14.3)**

Find a strictly feasible point for:

$$
\begin{align}
& x_1 + x_2 \leq 1 \\
& x_1 - x_2 \leq 0.5 \\
& -x_1 \leq 0 \\
& -x_2 \leq 0
\end{align}
$$

**Tasks:**  
a) Write the Phase I problem:

$$
\min_{x, s} \quad s \quad \text{s.t.} \quad h_i(x) \leq s, \quad i=1,\ldots,m
$$

b) Solve the Phase I problem with the barrier method  
c) If the solution has $$s^* < 0$$, choose a strictly feasible point

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Phase I problem:**

$$
\begin{align}
\min_{x_1, x_2, s} \quad & s \\
\text{s.t.} \quad & x_1 + x_2 - 1 \leq s \\
& x_1 - x_2 - 0.5 \leq s \\
& -x_1 \leq s \\
& -x_2 \leq s
\end{align}
$$

**Equivalently:**

$$
\min_{x, s} \quad s \quad \text{s.t.} \quad h_i(x) - s \leq 0
$$

---

**b) Solving via the analytic center:**

**Barrier problem:**

$$
\min_{x, s} \quad t \cdot s - \sum_i \log(-(h_i(x) - s))
$$

For large $$t$$, the solution is close to:

$$
\min_s \quad s \quad \text{s.t.} \quad h_i(x) \leq s
$$

that is, $$s^* = \max_i h_i(x)$$.

**Solution:** The Phase I problem is an LP in 3 variables $$(x_1, x_2, s)$$. At the optimum, the three constraints $$h_1, h_3, h_4$$ are all active:

$$x_1 + x_2 - 1 = -x_1 = -x_2 = s \;\Rightarrow\; x_1 = x_2 = -s,\quad -2s - 1 = s \;\Rightarrow\; s = -\tfrac{1}{3}$$

**Solution:** $$x^* = \left(\tfrac{1}{3}, \tfrac{1}{3}\right)$$, $$s^* = -\tfrac{1}{3}$$.

**Check:**

$$
\begin{align}
h_1 &= \tfrac{1}{3} + \tfrac{1}{3} - 1 = -\tfrac{1}{3} \\
h_2 &= \tfrac{1}{3} - \tfrac{1}{3} - 0.5 = -0.5 \\
h_3 &= -\tfrac{1}{3} \\
h_4 &= -\tfrac{1}{3}
\end{align}
$$

$$s = \max_i h_i = -\tfrac{1}{3}$$. (The point $$x = (0.25, 0.25)$$ is also feasible with $$s = -0.25$$, but it is not optimal for Phase I since $$-0.25 > -\tfrac{1}{3}$$.)

---

**c) Strictly feasible point:**

Since $$s^* = -\tfrac{1}{3} < 0$$, the problem is **feasible** and $$x = (\tfrac{1}{3}, \tfrac{1}{3})$$ satisfies all four inequalities **strictly** ($$h_i = -\tfrac{1}{3}, -0.5, -\tfrac{1}{3}, -\tfrac{1}{3} < 0$$).

In practice any point with $$s < 0$$ (for example $$x = (0.25, 0.25)$$ with $$s = -0.25$$) is enough as a starting point for the barrier method.

</details>

---

## 📝 **Part VI: A Comprehensive Problem**

### **Exercise 7: Portfolio Optimization with the Barrier Method (Boyd & Vandenberghe, Ex. 11.10)**

$$
\begin{align}
\min_x \quad & x^T \Sigma x \\
\text{s.t.} \quad & \mu^T x \geq r_{\min} \\
& \mathbf{1}^T x = 1 \\
& x \geq 0
\end{align}
$$

With $$\Sigma = \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{bmatrix}$$, $$\mu = \begin{bmatrix} 0.10 \\ 0.15 \end{bmatrix}$$, $$r_{\min} = 0.12$$.

**Tasks:**  
a) Write the barrier problem  
b) Compute the central path at $$t = 1, 10, 100$$  
c) Analyze the convergence

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Barrier problem:**

Rewrite:

$$
\begin{align}
\min_x \quad & x^T \Sigma x \\
\text{s.t.} \quad & -\mu^T x + r_{\min} \leq 0 \quad \text{(inequality 1)} \\
& \mathbf{1}^T x = 1 \quad \text{(equality)} \\
& -x_i \leq 0, \quad i=1,2 \quad \text{(inequalities 2, 3)}
\end{align}
$$

**Barrier function:**

$$
\phi(x) = -\log(-(-\mu^T x + r_{\min})) - \sum_{i=1}^2 \log x_i
$$

$$
= -\log(\mu^T x - r_{\min}) - \log x_1 - \log x_2
$$

**Barrier problem:**

$$
\min_x \quad t \cdot x^T \Sigma x - \log(\mu^T x - r_{\min}) - \log x_1 - \log x_2
$$

s.t. $$\mathbf{1}^T x = 1$$

---

**b) Central path (numerical):**

**Lagrangian:**

$$
L = t x^T \Sigma x - \log(\mu^T x - r_{\min}) - \sum_i \log x_i - \nu(x_1 + x_2 - 1)
$$

**FOC:**

$$
2t \Sigma x - \frac{\mu}{\mu^T x - r_{\min}} - \begin{bmatrix} 1/x_1 \\ 1/x_2 \end{bmatrix} - \nu \mathbf{1} = 0
$$

$$
x_1 + x_2 = 1
$$

**Solving the system (a numerical solver is needed):**

For the given data, approximate solutions:

**$$t = 1$$:**

$$x^*(1) \approx (0.247, 0.753)$$

(for small $$t$$ the barrier term dominates, so the solution is near the analytic center of the feasible region)

**$$t = 10$$:**

$$x^*(10) \approx (0.282, 0.718)$$

**$$t = 100$$:**

$$x^*(100) \approx (0.448, 0.552)$$ (and $$x^*(1000) \approx (0.571, 0.429)$$)

Converging to the optimal solution: $$x^* = (0.6, 0.4)$$ (the return constraint is active: $$0.10(0.6)+0.15(0.4)=0.12$$; $$x^T\Sigma x = 0.0336$$).

---

**c) Convergence analysis:**

**Duality gap:**

$$m = 3$$ inequality constraints

$$
\text{gap}(t) = \frac{3}{t}
$$

- $$t = 1$$: gap = 3
- $$t = 10$$: gap = 0.3
- $$t = 100$$: gap = 0.03

For a gap $$< 10^{-6}$$ we need $$t > 3 \times 10^6$$.

With $$\mu = 10$$:

$$
k > \frac{\log(3 \times 10^6)}{\log 10} \approx 6.5 \Rightarrow k = 7 \text{ iterations}
$$

</details>

---

## 💡 **Summary and Strategy**

### **Log-Barrier Function:**
- $$\phi(x) = -\sum_i \log(-h_i(x))$$
- $$\nabla \phi(x) = \sum_i \frac{\nabla h_i(x)}{-h_i(x)}$$
- $$\phi(x) \to \infty$$ as $$x$$ approaches the boundary

### **Central Path:**
- $$x^*(t)$$ = the solution of $$\min t f(x) + \phi(x)$$
- As $$t \to \infty$$: $$x^*(t) \to x^*$$ (the optimal solution)
- Central path characterization: perturbed KKT

### **Perturbed KKT:**
- $$\nabla f(x^*) + \sum_i \lambda_i^* \nabla h_i(x^*) = 0$$
- $$\lambda_i^* = -\frac{1}{t h_i(x^*)}$$
- $$\lambda_i^* h_i(x^*) = -\frac{1}{t} \to 0$$ as $$t \to \infty$$

### **Convergence:**
- Duality gap: $$\eta(t) = \frac{m}{t}$$
- Outer iterations: $$O(\log(m/\epsilon) / \log \mu)$$
- With $$\mu = 10$$: $$\approx \log_{10}(m/\epsilon)$$ iterations
- Each iteration: solve the barrier problem with Newton's method

### **Phase I Method:**
- Find a strictly feasible point
- $$\min_{x,s} s$$ s.t. $$h_i(x) \leq s$$
- If $$s^* < 0$$: feasible, choose $$x^*$$

---

## 📚 **References**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 11.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization* (2nd ed.). Springer. Chapter 14, 19.

3. **Nesterov, Y.** (2004). *Introductory Lectures on Convex Optimization*. Springer. Chapter 4.

4. **Wright, S. J.** (1997). *Primal-Dual Interior-Point Methods*. SIAM.

5. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM. Chapter 4.


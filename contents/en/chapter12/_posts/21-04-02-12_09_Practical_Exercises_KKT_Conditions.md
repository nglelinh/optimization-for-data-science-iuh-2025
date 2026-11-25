---
layout: post
title: '12-09 Practical Exercises - KKT Conditions'
chapter: '12'
order: 10
owner: GitHub Copilot
lang: en
categories:
- chapter12
lesson_type: required
redirect_from:
  - /contents/en/chapter12/12_08_Practical_Exercises_KKT_Conditions/
---

Solving KKT systems by hand is a rite of passage in graduate optimization: it teaches you how to perform systematic active-set case analysis, spot symmetry before grinding algebra, and interpret Lagrange multipliers as physical forces or financial risk prices. The practical exercises below—adapted from Boyd & Vandenberghe, Nocedal & Wright, and Bertsekas—take you from basic 2D quadratic programs through Markowitz portfolio optimization and Support Vector Machines.

## Background Knowledge Map: Systematic Workflow for Solving KKT Exercises

- **Pillar 1 — Standardize All Inequalities First:** Rewrite every inequality constraint as $$h_i(x) \le 0$$ before writing $$L(x, u, v)$$ so that dual feasibility is uniformly $$u_i \ge 0$$.
- **Pillar 2 — Active-Set Case Splitting via Complementary Slackness:** With $$m$$ inequalities, complementary slackness splits the search into $$2^m$$ active-set combinations (for each $$i$$, either $$u_i = 0$$ or $$h_i(x) = 0$$). Always test the **unconstrained / all-inactive** case first—if the unconstrained minimizer is primal feasible, you are done immediately!
- **Pillar 3 — Eliminating Primal Variables Using Stationarity:** For convex quadratics (like Markowitz portfolios or ridge regression), stationarity expresses $$x$$ linearly in terms of $$(u, v)$$; substituting into active constraints solves for the multipliers in closed form.
- **Pillar 4 — Checking Convexity & Slater Before Concluding:** Once you find a KKT point $$(x^\star, u^\star, v^\star)$$, verify convexity of $$f$$ and $$h_i$$ (and affinity of $$l_j$$) to conclude *global* optimality immediately; for nonconvex problems, compare objective values across all KKT candidates!

### Step-by-Step Worked Example (Read Slowly): Active-Set KKT Case Analysis on a 2-Constraint QP

Minimize $$f(x_1, x_2) = (x_1 - 3)^2 + (x_2 - 2)^2$$ subject to $$h_1(x) = x_1 + x_2 - 3 \le 0$$ and $$h_2(x) = -x_2 \le 0$$.

1. **Write stationarity:**
   $$2(x_1 - 3) + u_1 = 0, \qquad 2(x_2 - 2) + u_1 - u_2 = 0, \qquad u_1, u_2 \ge 0.$$
2. **Case 1 — Neither constraint active ($$u_1 = u_2 = 0$$):** Gives $$(3, 2)$$, which violates $$h_1(3, 2) = 3 + 2 - 3 = 2 > 0$$. Reject!
3. **Case 2 — Only $$h_1$$ active ($$x_1 + x_2 = 3,\; u_2 = 0$$):**
   - Stationarity: $$x_1 = 3 - u_1/2$$ and $$x_2 = 2 - u_1/2$$.
   - Plug into $$x_1 + x_2 = 3$$: $$(3 - u_1/2) + (2 - u_1/2) = 3 \implies 5 - u_1 = 3 \implies u_1^\star = 2 \ge 0$$!
   - Recover primal point: $$x_1^\star = 3 - 1 = 2$$, $$x_2^\star = 2 - 1 = 1$$.
   - Check remaining feasibility: $$h_2(2, 1) = -1 < 0$$ (strictly feasible, matching $$u_2^\star = 0$$!).
4. **Stop immediately!** Because the problem is convex and Case 2 satisfies all four KKT conditions, $$(x_1^\star, x_2^\star) = (2, 1)$$ with $$(u_1^\star, u_2^\star) = (2, 0)$$ is the **unique global optimum**—no need to test Cases 3 or 4!

# Practical Exercises - KKT Conditions (Karush-Kuhn-Tucker)

The exercises are adapted from Boyd & Vandenberghe (2004), Nocedal & Wright (2006), and Bertsekas (1999).

---

## 📝 **Part I: Verifying the KKT Conditions**

### **Exercise 1: A Basic Problem (Boyd & Vandenberghe, Ex. 5.1)**

Consider the problem:

$$
\begin{align}
\min_{x} \quad & x_1^2 + x_2^2 \\
\text{s.t.} \quad & x_1 + x_2 = 1 \\
& x_1 \geq 0
\end{align}
$$

Check the two candidate solutions:
1. $$x^{(1)} = (0.5, 0.5)$$, $$\nu = 1$$, $$\lambda = 0$$
2. $$x^{(2)} = (0, 1)$$, $$\nu = 2$$, $$\lambda = 2$$

**Tasks:** Write the KKT conditions, check each condition, and determine the optimal solution.

<details>
<summary><strong>💡 Solution</strong></summary>

**Lagrangian:** $$L(x,\nu,\lambda) = x_1^2 + x_2^2 - \nu(x_1+x_2-1) + \lambda(-x_1)$$ (the inequality constraint is written as $$g(x)=-x_1 \leq 0$$)

**The four KKT conditions:**

1. **Stationarity:** $$2x_1 - \nu - \lambda = 0$$, $$2x_2 - \nu = 0$$
2. **Primal Feasibility:** $$x_1 + x_2 = 1$$, $$x_1 \geq 0$$
3. **Dual Feasibility:** $$\lambda \geq 0$$
4. **Complementary Slackness:** $$\lambda \cdot (-x_1) = 0$$

**Check $$x^{(1)} = (0.5,0.5)$$, $$\nu=1$$, $$\lambda=0$$:**
- Stationarity: $$2(0.5)-1-0=0$$ ✓, $$2(0.5)-1=0$$ ✓
- Primal Feasibility: $$0.5+0.5=1$$ ✓, $$0.5 \geq 0$$ ✓
- Dual Feasibility: $$0 \geq 0$$ ✓
- Comp. Slackness: $$0 \cdot (-0.5)=0$$ ✓

**Satisfied!** Value: $$f^{(1)} = 0.5$$

**Check $$x^{(2)} = (0,1)$$, $$\nu=2$$, $$\lambda=2$$:**
- Stationarity: $$0-2-2=-4 \neq 0$$ ✗ (second component: $$2-2=0$$ ✓)
- Primal Feasibility: $$0+1=1$$ ✓, $$0 \geq 0$$ ✓
- Dual Feasibility: $$2 \geq 0$$ ✓
- Comp. Slackness: $$2 \cdot 0=0$$ ✓

**Not satisfied!** In fact, at $$x^{(2)}$$ we need $$\nu=2x_2=2$$ and $$\lambda = 2x_1-\nu = -2 < 0$$: no valid multiplier exists, so $$(0,1)$$ is not a KKT point. (The value $$f^{(2)} = 1 > f^{(1)}$$ is consistent with this.)

**Conclusion:** Only $$x^* = (0.5,0.5)$$ is a KKT point.

**Explanation:** The problem is convex, so KKT is sufficient for global optimality; hence $$x^* = (0.5,0.5)$$ is the unique optimal solution.

</details>

---

### **Exercise 2: A Simple QP (Nocedal & Wright, Ex. 12.1)**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2}(x_1^2 + x_2^2) \\
\text{s.t.} \quad & x_1 + x_2 = 1 \\
& x_1, x_2 \geq 0
\end{align}
$$

**Tasks:** Solve with the active set method.

<details>
<summary><strong>💡 Solution</strong></summary>

**3 active-set cases** (with $$L = \frac{1}{2}\|x\|^2 - \nu(x_1+x_2-1) - \lambda_1x_1 - \lambda_2x_2$$, stationarity: $$x_i = \nu + \lambda_i$$):

**Case 1:** no constraint $$\geq 0$$ is active ($$\lambda_1=\lambda_2=0$$)

From stationarity: $$x_1=\nu$$, $$x_2=\nu$$  
From $$x_1+x_2=1$$: $$2\nu=1 \Rightarrow \nu=0.5$$

→ $$x=(0.5, 0.5)$$, $$f=0.25$$, feasible ✓

**TH2:** $$x_1=0$$ active

$$x_2=1$$, stationarity for $$x_2$$: $$\nu=1$$  
Stationarity for $$x_1$$: $$\lambda_1 = x_1 - \nu = -1 < 0$$ ✗

→ $$x=(0,1)$$ is feasible but **violates dual feasibility**, so it is not a KKT point ($$f=0.5$$)

**TH3:** $$x_2=0$$ active

→ similarly, $$\lambda_2 = -1 < 0$$ ✗, so $$x=(1,0)$$ ($$f=0.5$$) is not a KKT point

**Optimal solution:** $$x^*=(0.5,0.5)$$ with $$f^*=0.25$$

</details>

---

## 📝 **Part II: Portfolio Optimization Application**

### **Exercise 3: Markowitz Mean-Variance**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2} x^T \Sigma x \\
\text{s.t.} \quad & \mu^T x \geq r_{\min} \\
& \mathbf{1}^T x = 1 \\
& x \geq 0
\end{align}
$$

With $$n=3$$:

$$
\Sigma = \begin{bmatrix} 0.04 & 0.01 & 0 \\ 0.01 & 0.09 & 0.02 \\ 0 & 0.02 & 0.16 \end{bmatrix}, \quad
\mu = \begin{bmatrix} 0.10 \\ 0.15 \\ 0.08 \end{bmatrix}, \quad
r_{\min} = 0.12
$$

**Tasks:** Try the assumption $$x_3=0$$ (invest only in assets 1 and 2): find $$x_1, x_2$$ and the dual variables, then check the KKT conditions.

<details>
<summary><strong>💡 Solution</strong></summary>

**Assume:** $$x_3=0$$ ($$\nu_{2,3} > 0$$), $$x_1,x_2>0$$, return constraint active ($$\lambda>0$$)

**Constraints:**
$$
\begin{cases}
x_1 + x_2 = 1 \\
0.10x_1 + 0.15x_2 = 0.12
\end{cases}
$$

From equation 2: $$0.10x_1 + 0.15x_2 = 0.12$$  
Substitute $$x_1 = 1-x_2$$:

$$
0.10(1-x_2) + 0.15x_2 = 0.12 \\
0.10 + 0.05x_2 = 0.12 \\
x_2 = 0.4
$$

→ $$x_1 = 0.6$$

**Solution:** $$x^* = (0.6, 0.4, 0)^T$$

**Check the dual variables from stationarity** (with $$L = \frac{1}{2}x^T\Sigma x - \lambda(\mu^Tx - r_{\min}) - \nu_1(\mathbf{1}^Tx-1) - \nu_2^Tx$$, so $$\Sigma x = \lambda\mu + \nu_1\mathbf{1} + \nu_2$$):

$$\Sigma x^* = \begin{bmatrix} 0.028 \\ 0.042 \\ 0.008 \end{bmatrix}$$

With $$\nu_{2,1}=\nu_{2,2}=0$$:

$$
\begin{cases}
0.028 = 0.10\lambda + \nu_1 \\
0.042 = 0.15\lambda + \nu_1
\end{cases}
$$

Subtract: $$0.014 = 0.05\lambda \Rightarrow \lambda = 0.28$$  
→ $$\nu_1 = 0.028 - 0.028 = 0$$

From equation 3:
$$\nu_{2,3} = 0.008 - 0.08(0.28) - 0 = -0.0144 < 0$$ ✗

**Conclusion:** Dual feasibility ($$\nu_2 \geq 0$$) is violated, so the assumption $$x_3=0$$ is **wrong**: asset 3 (weakly correlated with asset 1) should still receive a small investment thanks to the diversification effect.

**Re-solving with all 3 assets active** ($$x_i>0$$, return constraint active): solving $$\Sigma x = \lambda\mu + \nu_1\mathbf{1}$$, $$\mu^Tx=0.12$$, $$\mathbf{1}^Tx=1$$ gives

$$x^* \approx (0.522,\ 0.422,\ 0.056)^T, \quad \lambda^* \approx 0.385, \quad \nu_1^* \approx -0.0134$$

Check component 3: $$(\Sigma x^*)_3 \approx 0.0174 = 0.08(0.385) - 0.0134$$ ✓. The variance $$\frac{1}{2}x^{*T}\Sigma x^* \approx 0.0164$$ ($$\sigma \approx 0.181$$) is lower than $$0.0168$$ ($$\sigma \approx 0.183$$) for $$(0.6, 0.4, 0)$$.

**Meaning:**
- $$\lambda^*\approx 0.385$$: shadow price of the return constraint (raising $$r_{\min}$$ by $$0.001$$ → $$\frac{1}{2}x^T\Sigma x$$ increases by about $$0.000385$$)
- $$x_3^* \approx 0.056 > 0$$: asset 3 has a low return but helps reduce risk through diversification

</details>

---

## 📝 **Part III: Support Vector Machines**

### **Exercise 4: Hard-Margin SVM (Boyd & Vandenberghe, Ex. 8.6)**

**Data:**
- Class +1: $$(1,2)$$, $$(2,3)$$, $$(3,3)$$
- Class -1: $$(1,1)$$, $$(2,1)$$, $$(3,2)$$

**Primal:**

$$
\begin{align}
\min_{w,b} \quad & \frac{1}{2}\|w\|^2 \\
\text{s.t.} \quad & y_i(w^Tx_i + b) \geq 1, \quad i=1,\ldots,6
\end{align}
$$

**Dual:**

$$
\begin{align}
\max_{\alpha} \quad & \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i\alpha_j y_iy_j x_i^Tx_j \\
\text{s.t.} \quad & \sum_i \alpha_i y_i = 0 \\
& \alpha_i \geq 0
\end{align}
$$

**Tasks:** Determine the support vectors and the hyperplane.

<details>
<summary><strong>💡 Solution</strong></summary>

**Geometric observation:** The two classes are linearly separable. The support vectors are the points lying on the margin boundaries.

**Solution (computed with a QP solver, then verified with KKT):**
- Support vectors: $$x_1=(1,2)$$ (class +1), $$x_3=(3,3)$$ (class +1), $$x_6=(3,2)$$ (class -1)
- $$\alpha_1^* = 0.5$$, $$\alpha_3^* = 2$$, $$\alpha_6^* = 2.5$$
- All other $$\alpha$$'s = 0

Check: $$\sum_i \alpha_i y_i = 0.5 + 2 - 2.5 = 0$$ ✓

**Compute $$w^*$$:**

$$
w^* = \sum_i \alpha_i^* y_i x_i = 0.5(1,2) + 2(3,3) - 2.5(3,2)
$$

$$
= (0.5,1.0) + (6,6) - (7.5,5) = (-1, 2)
$$

**Compute $$b^*$$ from SV $$x_1$$:**

$$y_1(w^{*T}x_1 + b^*) = 1$$

$$1 \cdot ((-1)(1) + (2)(2) + b^*) = 1$$

$$3 + b^* = 1 \Rightarrow b^* = -2$$

**Decision boundary:** $$-x_1 + 2x_2 - 2 = 0$$, i.e. $$x_2 = \frac{x_1+2}{2}$$

**Margin check:** $$y_i(w^{*T}x_i+b^*) = 1, 2, 1, 1, 2, 1$$ for the 6 points (all $$\geq 1$$, equal to 1 at the SVs) ✓. Margin width: $$\frac{2}{\|w^*\|} = \frac{2}{\sqrt{5}} \approx 0.894$$.

</details>

---

## 📝 **Part IV: Water-Filling Algorithm**

### **Exercise 5: Power Allocation (Boyd & Vandenberghe, Ex. 5.7)**

$$
\begin{align}
\max_{p} \quad & \sum_{i=1}^n \log(1 + p_i/\sigma_i^2) \\
\text{s.t.} \quad & \sum_i p_i \leq P_{\text{total}} \\
& p_i \geq 0
\end{align}
$$

With $$n=4$$, $$\sigma^2=(1,2,3,4)$$, $$P_{\text{total}}=10$$.

**Tasks:** Derive the water-filling formula and compute the solution.

<details>
<summary><strong>💡 Solution</strong></summary>

**KKT conditions (converted to a minimization):**

Lagrangian: $$L = -\sum \log(1+p_i/\sigma_i^2) + \lambda(\sum p_i - P) - \sum \mu_i p_i$$

Stationarity: $$\frac{\partial L}{\partial p_i} = -\frac{1}{\sigma_i^2 + p_i} + \lambda - \mu_i = 0$$

**Analysis:**

- If $$p_i > 0$$: $$\mu_i=0 \Rightarrow \frac{1}{\sigma_i^2+p_i}=\lambda \Rightarrow p_i = \frac{1}{\lambda}-\sigma_i^2$$
- If $$p_i = 0$$: $$\mu_i \geq 0 \Rightarrow \sigma_i^2 \geq \frac{1}{\lambda}$$

**Water-filling formula:**

$$
\boxed{p_i^* = \max\left(0, \frac{1}{\lambda^*} - \sigma_i^2\right)}
$$

where $$\lambda^*$$ is such that $$\sum p_i^* = P_{\text{total}}$$.

---

**Computing the solution:**

Assume all channels are active:

$$
\sum_{i=1}^4 \left(\frac{1}{\lambda}-\sigma_i^2\right) = 10
$$

$$
\frac{4}{\lambda} - (1+2+3+4) = 10
$$

$$
\frac{4}{\lambda} = 20 \Rightarrow \lambda = 0.2
$$

**Water level:** $$\frac{1}{\lambda} = 5$$

**Power:**
- $$p_1 = 5-1 = 4$$ ✓
- $$p_2 = 5-2 = 3$$ ✓
- $$p_3 = 5-3 = 2$$ ✓
- $$p_4 = 5-4 = 1$$ ✓

**Total:** $$4+3+2+1=10$$ ✓

**Solution:** $$p^* = (4,3,2,1)$$

**Water Level interpretation:**

```
Water level = 5
|     |     |     |
|  4  |  3  |  2  |  1  |  ← Power
+-----+-----+-----+-----+
|  1  |  2  |  3  |  4  |  ← Noise floor
+-----+-----+-----+-----+
  p₁    p₂    p₃    p₄
```

Good channels (low noise) receive more power!

**Capacity:** 

$$C = \sum \log_2(1+p_i^*/\sigma_i^2) \approx 4.70 \text{ bits/s/Hz}$$

</details>

---

## 📝 **Part V: Advanced Exercises**

### **Exercise 6: Constrained Least Squares (Bertsekas, Ex. 3.2.2)**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2}\|Ax-b\|^2 \\
\text{s.t.} \quad & Cx = d \\
& x \geq 0
\end{align}
$$

With:

$$
A = \begin{bmatrix} 1&1\\1&-1\\2&0 \end{bmatrix}, \quad
b = \begin{bmatrix} 2\\0\\3 \end{bmatrix}, \quad
C = [1\ 1], \quad
d = 2
$$

**Tasks:** Solve using KKT.

<details>
<summary><strong>💡 Solution</strong></summary>

$$\nabla f(x) = A^TAx - A^Tb$$

$$
A^TA = \begin{bmatrix} 6&0\\0&2 \end{bmatrix}, \quad
A^Tb = \begin{bmatrix} 8\\2 \end{bmatrix}
$$

**KKT system (without $$x \geq 0$$):**

$$
\begin{bmatrix} 6&0&-1\\0&2&-1\\1&1&0 \end{bmatrix}
\begin{bmatrix} x_1\\x_2\\\nu \end{bmatrix} =
\begin{bmatrix} 8\\2\\2 \end{bmatrix}
$$

Solve:
- From (3): $$x_1+x_2=2$$
- From (1), (2): $$x_1=\frac{8+\nu}{6}$$, $$x_2=\frac{2+\nu}{2}$$; substituting into (3): $$14+4\nu=12 \Rightarrow \nu=-0.5$$
- $$x_1=1.25$$, $$x_2=0.75$$

**Check $$x \geq 0$$:** $$x_1=1.25>0$$, $$x_2=0.75>0$$ ✓

**Check $$\lambda$$:**

$$\lambda = A^TAx - A^Tb - C^T\nu = \begin{bmatrix} 7.5-8+0.5\\1.5-2+0.5 \end{bmatrix} = \begin{bmatrix} 0\\0 \end{bmatrix} \geq 0$$ ✓

**Solution:** $$x^*=(1.25, 0.75)^T$$, $$Ax^*-b=(0,0.5,-0.5)^T$$, $$f^*=\frac{1}{2}(0.25+0.25)=0.25$$

</details>

---

### **Exercise 7: Penalty Method (Nocedal & Wright, Ex. 17.1)**

$$
\begin{align}
\min_{x} \quad & x_1 + x_2 \\
\text{s.t.} \quad & x_1^2 + x_2^2 = 1
\end{align}
$$

**Penalty:** $$\min \phi(x;\mu) = x_1+x_2 + \frac{\mu}{2}(x_1^2+x_2^2-1)^2$$

**Tasks:** Solve with KKT, compute the penalty solution for $$\mu=1,10,100$$, and analyze the convergence.

<details>
<summary><strong>💡 Solution</strong></summary>

**Solving with KKT:**

Lagrangian: $$L = x_1+x_2 - \nu(x_1^2+x_2^2-1)$$

Stationarity: $$1-2\nu x_1=0$$, $$1-2\nu x_2=0$$ → $$x_1=x_2=\frac{1}{2\nu}$$

Feasibility: $$\frac{1}{4\nu^2}+\frac{1}{4\nu^2}=1 \Rightarrow \nu = \pm\frac{1}{\sqrt{2}}$$

**Two KKT points:**
1. $$x=(1/\sqrt{2}, 1/\sqrt{2})$$, $$f=\sqrt{2}$$
2. $$x=(-1/\sqrt{2}, -1/\sqrt{2})$$, $$f=-\sqrt{2}$$

**Optimal (min):** $$x^* = (-1/\sqrt{2}, -1/\sqrt{2})$$

---

**Penalty method:**

FOC: $$1 + 2\mu x_i(x_1^2+x_2^2-1)=0$$

With $$x_1=x_2=x$$: $$1 + 2\mu x(2x^2-1)=0$$, i.e. $$4\mu x^3 - 2\mu x + 1=0$$

**Numerical solution** (take the negative real root of the cubic, which has the smallest $$\phi$$; for large $$\mu$$ the cubic also has a positive root corresponding to a local minimum near the KKT maximizer, with larger $$\phi$$):
- $$\mu=1$$: $$x \approx -0.885$$ ($$x_1^2+x_2^2-1 \approx 0.57$$, a fairly large constraint violation)
- $$\mu=10$$: $$x \approx -0.731$$ ($$x_1^2+x_2^2-1 \approx 0.07$$)
- $$\mu=100$$: $$x \approx -0.710$$ ($$x_1^2+x_2^2-1 \approx 0.007$$) $$\to -1/\sqrt{2} \approx -0.7071$$

**Convergence:** As $$\mu \to \infty$$, the penalty solution converges to the KKT solution (from **outside** the feasible set, since $$x_1^2+x_2^2>1$$)!

**Relation:** $$\nu \approx -\mu(x_1^2+x_2^2-1)$$ (with the convention $$L = f - \nu h$$; e.g. $$\mu=100$$: $$\nu \approx -100 \cdot 0.007 \approx -0.7 \approx -1/\sqrt{2}$$ ✓)

</details>

---

## 💡 **Strategy Summary**

### **Verifying KKT:**
- Check the **4 conditions** separately
- KKT is **necessary** for a local optimum (under a CQ) and **sufficient** for a global optimum (convex problems)

### **Solving with KKT:**
- **Active set strategy:** try the active-set cases
- Solve the KKT system from stationarity + active constraints
- Check feasibility and compare objectives

### **Complementary Slackness:**
- $$\lambda_i > 0 \Rightarrow$$ constraint $$i$$ is active
- **Shadow price:** $$\lambda_i^*$$ = marginal value of constraint $$i$$

### **Convex problems:**
- KKT sufficient → a KKT point is globally optimal
- Strong duality: $$f^*=g^*$$

---

## 📚 **References**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 5.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization* (2nd ed.). Springer. Chapters 12, 16-17.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming* (2nd ed.). Athena Scientific. Chapter 3.

4. **Luenberger, D. G., & Ye, Y.** (2008). *Linear and Nonlinear Programming* (3rd ed.). Springer. Chapter 10.

5. **Bazaraa, M. S., Sherali, H. D., & Shetty, C. M.** (2006). *Nonlinear Programming: Theory and Algorithms* (3rd ed.). Wiley.


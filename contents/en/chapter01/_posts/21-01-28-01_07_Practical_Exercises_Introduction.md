---
layout: post
title: '01-07 Practical Exercises - Introduction to Optimization'
chapter: '1'
order: 8
owner: GitHub Copilot
lang: en
categories:
- chapter01
lesson_type: required
redirect_from:
  - /contents/en/chapter01/01_06_Practical_Exercises_Introduction/
---

# Practical Exercises - Introduction to Optimization

## 📝 **Exercise 1: Classifying basic optimization problems**

**Problem:** (Exercise 1.1 from Boyd & Vandenberghe)
Classify the following problems as LP (Linear Programming), QP (Quadratic Programming), QCQP (Quadratically Constrained QP), SOCP (Second-Order Cone Programming), SDP (Semidefinite Programming), or GP (Geometric Programming):

a) $$\min_{x \in \mathbb{R}^n} c^T x \quad \text{s.t.} \quad Ax \leq b$$

b) $$\min_{x \in \mathbb{R}^n} x^T P x + q^T x \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

c) $$\min_{x \in \mathbb{R}^n} \lVert Ax - b \rVert_2 \quad \text{s.t.} \quad \lVert x \rVert_2 \leq 1$$

**Task:**
1. Identify the problem class for each case
2. Explain the reason for the classification
3. State the conditions under which the problem is convex
4. Suggest a suitable solution method

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Classification**

**a) Linear programming (LP)**
- Objective: linear ($$c^T x$$)
- Constraints: linear inequalities ($$Ax \leq b$$)
- This is the standard form of an LP

**b) Quadratic programming (QP)**
- Objective: quadratic ($$x^T P x + q^T x$$)
- Constraints: linear ($$Ax = b, x \geq 0$$)
- Convex when $$P \succeq 0$$

**c) Second-order cone programming (SOCP)**
- Objective: a norm ($$\lVert Ax - b \rVert_2$$)
- Constraint: a norm constraint ($$\lVert x \rVert_2 \leq 1$$)
- Can be rewritten in standard SOCP form

**Step 2: Convexity conditions**
- **a)** Always convex (linear functions)
- **b)** Convex when $$P \succeq 0$$ (positive semidefinite)
- **c)** Always convex (norm objective and norm constraint)

**Step 3: Solution methods**
- **a)** The Simplex method, interior-point methods
- **b)** Active-set methods, interior-point methods
- **c)** Interior-point methods for SOCP

</details>

---

## 📝 **Exercise 2: Least squares and variants**

**Problem:** (Exercise 1.2 from Boyd & Vandenberghe)
Consider the following least squares problems:

a) **Ordinary least squares:** $$\min_x \lVert Ax - b \rVert_2^2$$

b) **Weighted least squares:** $$\min_x (Ax - b)^T W (Ax - b)$$ with $$W \succ 0$$

c) **Regularized least squares:** $$\min_x \lVert Ax - b \rVert_2^2 + \lambda \lVert x \rVert_2^2$$

d) **Robust least squares:** $$\min_x \sum_{i=1}^m \phi((Ax - b)_i)$$ with $$\phi(u) = \begin{cases} u^2 & |u| \leq M \\ 2M|u| - M^2 & |u| > M \end{cases}$$

**Task:**
1. Find the analytical solution for cases a, b, c
2. Prove that all of the problems are convex
3. Analyze the geometric meaning of regularization
4. Compare the robustness of the methods

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Analytical solutions**

**a) Ordinary least squares:**
$$x^* = (A^T A)^{-1} A^T b$$ (if $$A^T A$$ is invertible)

**b) Weighted least squares:**
$$x^* = (A^T W A)^{-1} A^T W b$$

**c) Regularized least squares (Ridge regression):**
$$x^* = (A^T A + \lambda I)^{-1} A^T b$$

**d) Robust least squares:**
No closed form; numerical methods are needed.

**Step 2: Proving convexity**

**a-c)** Quadratic functions with positive semidefinite Hessians: $$2A^TA \succeq 0$$, $$2A^TWA \succeq 0$$, $$2(A^TA + \lambda I) \succ 0$$ (for $$\lambda > 0$$)
**d)** $$\phi(u)$$ is a convex function (piecewise quadratic with a non-decreasing derivative)

**Step 3: Geometric meaning**
- **Regularization:** Shrinks toward the origin, preventing overfitting
- **$$\lambda$$** controls the bias-variance trade-off
- Equivalent to a Bayesian prior $$x \sim \mathcal{N}(0, \sigma^2/\lambda I)$$

**Step 4: Comparing robustness**
- **OLS:** Sensitive to outliers (quadratic penalty)
- **Weighted:** Can down-weight outliers if $$W$$ is chosen well
- **Regularized:** Reduces overfitting, improves generalization
- **Robust:** The Huber loss reduces sensitivity to outliers

</details>

---

## 📝 **Exercise 3: Linear programming in standard form**

**Problem:** (Exercise 1.3 from Boyd & Vandenberghe)
Convert the following problems to LP standard form:

a) $$\min_{x,y} 2x + 3y \quad \text{s.t.} \quad x + 2y \geq 5, \quad x - y = 2, \quad x \geq 0, \quad y \text{ free}$$

b) $$\max_x c^T x \quad \text{s.t.} \quad Ax \leq b, \quad x \geq 0$$

c) $$\min_x \lVert c^T x - d \rVert_\infty \quad \text{s.t.} \quad Ax \leq b$$

**Task:**
1. Convert to the form $$\min c^T z \text{ s.t. } Az = b, z \geq 0$$
2. Identify the new matrix $$A$$ and vectors $$b, c$$
3. Explain the transformations used
4. Verify that the original and transformed problems are equivalent

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Converting problem a)**

**Free variable:** $$y = y^+ - y^-$$ with $$y^+, y^- \geq 0$$

**Inequality:** $$x + 2y \geq 5 \Rightarrow x + 2y - s = 5$$ with $$s \geq 0$$

**Standard form:**
$$\min_{x,y^+,y^-,s} 2x + 3y^+ - 3y^- \quad \text{s.t.} \quad \begin{bmatrix} 1 & 2 & -2 & -1 \\ 1 & -1 & 1 & 0 \end{bmatrix} \begin{bmatrix} x \\ y^+ \\ y^- \\ s \end{bmatrix} = \begin{bmatrix} 5 \\ 2 \end{bmatrix}$$

with $$x, y^+, y^-, s \geq 0$$.

**Step 2: Converting problem b)**

**Max to min:** $$\max c^T x = -\min (-c^T x)$$

**Inequality to equality:** $$Ax \leq b \Rightarrow Ax + s = b$$ with $$s \geq 0$$

**Standard form:**
$$\min_{x,s} (-c^T x + 0^T s) \quad \text{s.t.} \quad [A \quad I] \begin{bmatrix} x \\ s \end{bmatrix} = b, \quad x,s \geq 0$$

**Step 3: Converting problem c)**

**Rewriting the $$\ell_\infty$$ norm:** $$\min t \text{ s.t. } -t \leq c^T x - d \leq t$$

**Standard form:**
$$\min_{x,t,s_1,s_2,s_3} t \quad \text{s.t.} \quad \begin{bmatrix} A & 0 & I & 0 & 0 \\ c^T & -1 & 0 & 1 & 0 \\ -c^T & -1 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} x \\ t \\ s_1 \\ s_2 \\ s_3 \end{bmatrix} = \begin{bmatrix} b \\ d \\ -d \end{bmatrix}, \quad t, s_1, s_2, s_3 \geq 0$$

The last two rows are $$c^T x - d \leq t$$ and $$-(c^T x - d) \leq t$$; each needs its own slack variable. Since $$x$$ is free, also substitute $$x = x^+ - x^-$$ with $$x^+, x^- \geq 0$$ to reach the exact form $$z \geq 0$$.

</details>

---

## 📝 **Exercise 4: Quadratic programming applications**

**Problem:** (Exercise 1.4 from Boyd & Vandenberghe)
Consider the portfolio optimization problem:

$$\min_x \frac{1}{2} x^T \Sigma x \quad \text{s.t.} \quad \mu^T x \geq r, \quad \mathbf{1}^T x = 1, \quad x \geq 0$$

with $$\Sigma \succ 0$$ (covariance matrix), $$\mu$$ (expected returns), $$r$$ (target return).

**Task:**
1. Prove that this is a convex QP
2. Write the KKT conditions
3. Analyze the case without the constraint $$x \geq 0$$
4. Find the efficient frontier
5. Implement numerical solution

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Proving convexity**
- Objective: $$f(x) = \frac{1}{2} x^T \Sigma x$$ with $$\nabla^2 f = \Sigma \succ 0$$
- Constraints: all linear
- $$\Rightarrow$$ Convex QP

**Step 2: KKT conditions**
Lagrangian (using $$\eta$$ for the multiplier of $$x \geq 0$$ to avoid a clash with $$\mu$$): $$L(x,\lambda,\nu,\eta) = \frac{1}{2} x^T \Sigma x - \lambda(\mu^T x - r) + \nu(\mathbf{1}^T x - 1) - \eta^T x$$

KKT conditions:
- Stationarity: $$\Sigma x - \lambda \mu + \nu \mathbf{1} - \eta = 0$$
- Primal feasibility: $$\mu^T x \geq r, \mathbf{1}^T x = 1, x \geq 0$$
- Dual feasibility: $$\lambda \geq 0, \eta \geq 0$$
- Complementary slackness: $$\lambda(\mu^T x - r) = 0, \eta_i x_i = 0$$

**Step 3: Dropping the constraint $$x \geq 0$$ (assuming the return constraint is active, $$\mu^T x = r$$)**
$$x^* = \Sigma^{-1}(\lambda^* \mu - \nu^* \mathbf{1})$$

From the constraints:
- $$\mathbf{1}^T x^* = 1 \Rightarrow \mathbf{1}^T \Sigma^{-1}(\lambda^* \mu - \nu^* \mathbf{1}) = 1$$
- $$\mu^T x^* = r \Rightarrow \mu^T \Sigma^{-1}(\lambda^* \mu - \nu^* \mathbf{1}) = r$$

Solve the system:
$$\begin{bmatrix} A & B \\ B & C \end{bmatrix} \begin{bmatrix} \lambda^* \\ -\nu^* \end{bmatrix} = \begin{bmatrix} r \\ 1 \end{bmatrix}$$

with $$A = \mu^T \Sigma^{-1} \mu, B = \mu^T \Sigma^{-1} \mathbf{1}, C = \mathbf{1}^T \Sigma^{-1} \mathbf{1}$$

**Step 4: The efficient frontier**
$$\sigma^2(r) = x^{*T} \Sigma x^* = \frac{Cr^2 - 2Br + A}{AC - B^2}$$

This is a hyperbola in the $$(r, \sigma)$$ plane.

</details>

---

## 📝 **Exercise 5: Geometric programming**

**Problem:** (Exercise 1.5 from Boyd & Vandenberghe)
Consider the circuit design problem:

$$\min_{x,y,z} \frac{1}{xyz} \quad \text{s.t.} \quad \frac{x}{y} + \frac{y}{z} \leq 1, \quad z \leq 1, \quad x,y,z > 0$$

*(The constraint $$z \leq 1$$ is needed: without it, scaling $$(x, y, z)$$ by $$s > 0$$ leaves the first constraint unchanged but drives $$\frac{1}{xyz} \to 0$$ as $$s \to \infty$$, so the problem has no optimal solution.)*

**Task:**
1. Show that this is a geometric program
2. Convert it to convex form with a log transformation
3. Solve the convex problem
4. Interpret the solution in the circuit-design context

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Verify that it is a geometric program**
- Objective: $$f_0(x,y,z) = x^{-1} y^{-1} z^{-1}$$ (monomial)
- Constraint: $$g_1(x,y,z) = x^1 y^{-1} z^0 + x^0 y^1 z^{-1}$$ (posynomial), $$g_2(x,y,z) = z$$ (monomial)
- Domain: $$x,y,z > 0$$

$$\Rightarrow$$ This is a GP in standard form.

**Step 2: Log transformation**
Let $$u = \log x, v = \log y, w = \log z$$:

$$\min_{u,v,w} -u - v - w \quad \text{s.t.} \quad \log(e^{u-v} + e^{v-w}) \leq 0, \quad w \leq 0$$

Equivalently:
$$\min_{u,v,w} -u - v - w \quad \text{s.t.} \quad e^{u-v} + e^{v-w} \leq 1, \quad w \leq 0$$

**Step 3: Convex formulation**
The objective is linear, $$\log(e^{u-v} + e^{v-w})$$ is log-sum-exp of affine functions (convex), and $$w \leq 0$$ is linear.

This is a convex problem (log-sum-exp constraint).

**Step 4: Solution method**
Use an interior-point method or a dedicated GP solver.

The optimal solution:
- $$x^* = e^{u^*}, y^* = e^{v^*}, z^* = e^{w^*}$$
- Both constraints are active. With $$z = 1$$, the problem becomes $$\max xy$$ s.t. $$x \leq y(1 - y)$$, i.e. $$\max_y y^2(1-y)$$, attained at $$y = 2/3$$.
- Solution: $$x^* = 2/9$$, $$y^* = 2/3$$, $$z^* = 1$$; check $$\frac{x^*}{y^*} + \frac{y^*}{z^*} = \frac{1}{3} + \frac{2}{3} = 1$$ ✓; optimal value $$\frac{1}{x^*y^*z^*} = \frac{27}{4}$$.

</details>

---

## 📝 **Exercise 6: Semidefinite programming basics**

**Problem:** (Exercise 1.6 from Boyd & Vandenberghe)
Consider the problem:

$$\min_X \text{tr}(CX) \quad \text{s.t.} \quad \text{tr}(A_i X) = b_i, \quad i = 1,\ldots,m, \quad X \succeq 0$$

**Task:**
1. Prove that this is a convex optimization problem
2. Write the dual problem
3. Analyze the conditions for strong duality
4. Concrete example: the Maximum Cut relaxation

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Proving convexity**
- Objective: $$\text{tr}(CX)$$ is linear in $$X$$
- Constraints: $$\text{tr}(A_i X) = b_i$$ linear
- Constraint: $$X \succeq 0$$ convex (positive semidefinite cone)

$$\Rightarrow$$ Convex SDP

**Step 2: Dual problem**
Lagrangian: $$L(X,y,Z) = \text{tr}(CX) + \sum_{i=1}^m y_i (b_i - \text{tr}(A_i X)) - \text{tr}(ZX)$$

Dual function: $$g(y,Z) = \inf_X L(X,y,Z)$$

Condition: $$C - \sum_{i=1}^m y_i A_i - Z = 0$$

**Dual problem:**
$$\max_{y,Z} \sum_{i=1}^m b_i y_i \quad \text{s.t.} \quad \sum_{i=1}^m y_i A_i + Z = C, \quad Z \succeq 0$$

**Step 3: Strong duality**
Strong duality holds if Slater's condition is satisfied:
$$\exists X \succ 0 \text{ s.t. } \text{tr}(A_i X) = b_i, \forall i$$

**Step 4: Maximum cut example**
Given a graph $$G = (V,E)$$ with weights $$w_{ij}$$:

$$\max_x \sum_{(i,j) \in E} w_{ij} \frac{1 - x_i x_j}{2} \quad \text{s.t.} \quad x_i \in \{-1,1\}$$

**SDP relaxation:**
$$\max_X \sum_{(i,j) \in E} w_{ij} \frac{1 - X_{ij}}{2} \quad \text{s.t.} \quad X_{ii} = 1, \quad X \succeq 0$$

</details>

---

## 📝 **Exercise 7: Introduction to robust optimization**

**Problem:** (Exercise 1.7 from Boyd & Vandenberghe)
Consider the robust linear program:

$$\min_x c^T x \quad \text{s.t.} \quad a_i^T x \leq b_i \quad \forall a_i \in \mathcal{U}_i, \quad i = 1,\ldots,m$$

with uncertainty sets:
a) Box: $$\mathcal{U}_i = \{a_i^{nom} + u : \lVert u \rVert_\infty \leq \rho_i\}$$
b) Ellipsoidal: $$\mathcal{U}_i = \{a_i^{nom} + P_i u : \lVert u \rVert_2 \leq 1\}$$

**Task:**
1. Reformulate as deterministic convex programs
2. Compare the computational complexity
3. Analyze the level of conservatism
4. Implement and compare the solutions

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Box uncertainty**
$$\max_{a_i \in \mathcal{U}_i} a_i^T x = (a_i^{nom})^T x + \rho_i \lVert x \rVert_1$$

**Deterministic equivalent:**
$$\min_x c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \rho_i \lVert x \rVert_1 \leq b_i$$

**LP reformulation:**
$$\min_{x,t_i} c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \rho_i \sum_j t_{ij} \leq b_i, \quad -t_{ij} \leq x_j \leq t_{ij}$$

**Step 2: Ellipsoidal uncertainty**
$$\max_{a_i \in \mathcal{U}_i} a_i^T x = (a_i^{nom})^T x + \lVert P_i^T x \rVert_2$$

**Deterministic equivalent:**
$$\min_x c^T x \quad \text{s.t.} \quad (a_i^{nom})^T x + \lVert P_i^T x \rVert_2 \leq b_i$$

This is a Second-Order Cone Program (SOCP).

**Step 3: Comparing complexity**
- **Box:** LP with $$O(mn)$$ variables and constraints
- **Ellipsoidal:** SOCP with $$n + m$$ variables and $$m$$ SOC constraints
- **Nominal:** LP with $$n$$ variables and $$m$$ constraints

**Step 4: Analyzing conservatism**
- **Box:** Most conservative (worst case in every direction)
- **Ellipsoidal:** Moderately conservative (direction-dependent uncertainty)
- **Nominal:** Least conservative (no uncertainty)

Price of robustness = $$\frac{\text{Robust optimal value}}{\text{Nominal optimal value}} - 1$$

</details>

---

## 📝 **Exercise 8: Convexity verification**

**Problem:** (Exercise 1.8 from Boyd & Vandenberghe)
Determine whether the following functions are convex:

a) $$f(x) = x \log x$$ on $$\mathbb{R}_{++}$$
b) $$f(x) = -\log(\det X)$$ on $$\mathbb{S}_{++}^n$$
c) $$f(x) = \lVert x \rVert_p$$ with $$p \geq 1$$
d) $$f(X) = \lambda_{\max}(X)$$ on $$\mathbb{S}^n$$

**Task:**
1. Prove or disprove convexity
2. Compute second-order conditions where applicable
3. Verify using the definition or composition rules
4. Find the convex domain of each function

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: $$f(x) = x \log x$$**
**Domain:** $$\mathbb{R}_{++}$$ (convex)

**Second derivative:** $$f''(x) = \frac{1}{x} > 0$$ for $$x > 0$$

$$\Rightarrow$$ Convex on $$\mathbb{R}_{++}$$

**Step 2: $$f(X) = -\log(\det X)$$**
**Domain:** $$\mathbb{S}_{++}^n$$ (convex)

**Hessian:** One can show that $$\nabla^2 f \succ 0$$

Alternative: $$-\log(\det X) = -\log(\prod_i \lambda_i) = -\sum_i \log \lambda_i$$

Arguing eigenvalue by eigenvalue is not enough (eigenvalues are not concave functions of $$X$$; only $$\lambda_{\min}$$ is). The standard argument: take $$X = Z + tV$$ with $$Z \succ 0$$; then $$f(Z + tV) = -\log\det Z - \sum_i \log(1 + t\lambda_i)$$, where $$\lambda_i$$ are the eigenvalues of $$Z^{-1/2} V Z^{-1/2}$$. Each term $$-\log(1 + t\lambda_i)$$ is convex in $$t$$, so $$f$$ is convex.

**Result:** Convex on $$\mathbb{S}_{++}^n$$

**Step 3: $$f(x) = \lVert x \rVert_p$$**
**Domain:** $$\mathbb{R}^n$$ (convex)

**For $$p \geq 1$$:** Triangle inequality $$\Rightarrow$$ convex
**For $$0 < p < 1$$:** Not convex (the triangle inequality fails: for $$p = 1/2$$, $$\lVert (1,1) \rVert_{1/2} = 4 > \lVert (1,0) \rVert_{1/2} + \lVert (0,1) \rVert_{1/2} = 2$$)

**Verification:** Minkowski inequality for $$p \geq 1$$

**Step 4: $$f(X) = \lambda_{\max}(X)$$**
**Domain:** $$\mathbb{S}^n$$ (convex)

**Convexity:** $$\lambda_{\max}(X) = \max_{\lVert v \rVert = 1} v^T X v$$

A maximum of linear functions $$\Rightarrow$$ convex

**Alternative:** Spectral norm property

</details>

---

## 📝 **Exercise 9: Optimization modeling**

**Problem:** (Exercise 1.9 from Boyd & Vandenberghe)
Formulate the following real-world problems as convex optimization problems:

a) **Antenna array design:** Minimize sidelobe level
b) **Filter design:** Minimize passband ripple and stopband energy
c) **Truss design:** Minimize weight subject to stiffness constraints
d) **Data fitting:** Robust regression with outliers

**Task:**
1. Mathematical formulation of each problem
2. Identify variables, objective, constraints
3. Verify convexity
4. Suggest solution approaches

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Antenna array design**
**Variables:** $$w \in \mathbb{C}^n$$ (array weights)

**Objective:** Minimize maximum sidelobe level
$$\min_{w,t} t \quad \text{s.t.} \quad |a(\theta)^H w| \leq t, \quad \forall \theta \in \Theta_{sidelobe}$$

where $$a(\theta)$$ is the steering vector and $$\Theta_{sidelobe}$$ is the sidelobe region.

**Main beam constraint:** $$a(\theta_0)^H w = 1$$ (normalization)

**Convex:** SOCP (second-order cone constraints)

**Step 2: Filter design**
**Variables:** $$h \in \mathbb{R}^n$$ (filter coefficients)

**Passband ripple:** $$|H(\omega) - 1| \leq \delta_p, \quad \omega \in \Omega_p$$
**Stopband attenuation:** $$|H(\omega)| \leq \delta_s, \quad \omega \in \Omega_s$$

where $$H(\omega) = \sum_{k=0}^{n-1} h_k e^{-j\omega k}$$

**Convex formulation:**
$$\min_{h,\delta_p,\delta_s} \alpha \delta_p + \beta \delta_s$$
subject to frequency response constraints.

**Step 3: Truss design**
**Variables:** $$A \in \mathbb{R}^m$$ (cross-sectional areas)

**Objective:** $$\min \sum_{i=1}^m \rho_i l_i A_i$$ (total weight)

**Stiffness constraint:** $$u^T K(A) u \geq u_{min}^T K_0 u_{min}$$

where $$K(A) = \sum_{i=1}^m A_i K_i$$ (stiffness matrix)

**Convex:** Linear objective, constraint linear in $$A$$

**Step 4: Robust regression**
**Variables:** $$\beta \in \mathbb{R}^p$$ (regression coefficients)

**Huber loss:** $$\min_\beta \sum_{i=1}^n \phi(y_i - x_i^T \beta)$$

where $$\phi(u) = \begin{cases} \frac{1}{2}u^2 & |u| \leq M \\ M|u| - \frac{1}{2}M^2 & |u| > M \end{cases}$$

**Convex:** The Huber function is convex

</details>

---

## 📝 **Exercise 10: Introduction to duality**

**Problem:** (Exercise 1.10 from Boyd & Vandenberghe)
Consider the LP:
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$

**Task:**
1. Derive the dual problem using the Lagrangian approach
2. Prove weak duality
3. Find conditions for strong duality
4. Interpret dual variables economically
5. Verify complementary slackness

<details>
<summary><strong>💡 Detailed solution</strong></summary>

**Step 1: Lagrangian and dual**
$$L(x,\nu,\lambda) = c^T x + \nu^T(Ax - b) - \lambda^T x$$

**Dual function:**
$$g(\nu,\lambda) = \inf_x L(x,\nu,\lambda) = \inf_x (c + A^T \nu - \lambda)^T x - \nu^T b$$

**Finiteness condition:** $$c + A^T \nu - \lambda = 0$$, i.e., $$\lambda = A^T \nu + c$$

**Dual problem:**
$$\max_{\nu,\lambda} g(\nu,\lambda) = \max_\nu -\nu^T b \quad \text{s.t.} \quad A^T \nu + c \geq 0$$

Equivalently:
$$\max_\nu b^T \nu \quad \text{s.t.} \quad A^T \nu \leq c$$

**Step 2: Weak duality**
For every primal feasible $$x$$ and dual feasible $$\nu$$:
$$c^T x \geq b^T \nu$$

**Proof:** 
$$c^T x \geq (A^T \nu)^T x = \nu^T Ax = \nu^T b = b^T \nu$$

**Step 3: Strong duality**
Strong duality holds for LP whenever both the primal and the dual are feasible (fundamental theorem of LP).

**Step 4: Economic interpretation**
- $$\nu_i$$: shadow price of resource $$i$$
- $$\nu_i$$ = marginal value of constraint $$i$$
- If $$b_i$$ increases by 1 unit, the optimal value increases by $$\nu_i$$

**Step 5: Complementary slackness**
- If $$x_j^* > 0$$, then $$(A^T \nu^*)_j = c_j$$ (reduced cost = 0)
- If $$(A^T \nu^*)_j < c_j$$, then $$x_j^* = 0$$

</details>

---

## 💡 Practical Tips

#### **When classifying optimization problems:**
- Check the form of the objective (linear, quadratic, general)
- Identify the constraint types (linear, quadratic, conic)
- Verify the convexity of each component

#### **When converting to standard form:**
- Free variables: $$x = x^+ - x^-$$
- Inequalities: add slack variables
- Max to min: flip the sign of the objective

#### **When verifying convexity:**
- Use the second-order condition when possible
- Apply composition rules and convexity-preserving operations
- Check the definition directly if needed

---

## 💡 **Summary**

### **Classes of Optimization Problems:**

| Class | Objective | Constraints | Example |
|------|--------------|-----------|-------|
| **LP** | Linear | Linear | $$\min c^Tx$$, $$Ax \leq b$$ |
| **QP** | Quadratic | Linear | $$\min \frac{1}{2}x^TQx + c^Tx$$ |
| **QCQP** | Quadratic | Quadratic | Portfolio with risk constraints |
| **SOCP** | Linear | $$\ell_2$$ norm | $$\|\|Ax-b\|\|_2 \leq c^Tx$$ |
| **SDP** | Linear | PSD matrix | $$\min \text{tr}(CX)$$, $$X \succeq 0$$ |

### **Least Squares Variants:**

| Method | Objective | Characteristics |
|--------|-----------|----------|
| Ordinary LS | $$\|\|Ax-b\|\|_2^2$$ | Closed-form solution |
| Weighted LS | $$(Ax-b)^TW(Ax-b)$$ | Weights for observations |
| Regularized LS | $$\|\|Ax-b\|\|_2^2 + \lambda\|\|x\|\|_2^2$$ | Ridge regression |
| Robust LS | $$\sum \phi((Ax-b)_i)$$ | Resistant to outliers |
| LASSO | $$\|\|Ax-b\|\|_2^2 + \lambda\|\|x\|\|_1$$ | Sparse solutions |

### **Duality Concepts:**

- **Weak duality:** $$d^* \leq p^*$$ (always holds)
- **Strong duality:** $$d^* = p^*$$ (requires conditions, e.g., Slater)
- **Shadow price:** $$\nu_i^*$$ = marginal value of constraint $$i$$
- **Complementary slackness:** $$\lambda_i^* (g_i(x^*)) = 0$$

---

## 📚 References

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 1: Introduction
   - Exercises 1.1-1.15

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization*. Springer.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming*. Athena Scientific.

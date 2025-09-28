---
layout: post
title: 4-10 Bài Tập Thực Hành - Bài Toán Tối Ưu Convex
chapter: '4'
order: 11
owner: GitHub Copilot
lang: vi
categories:
- chapter04
lesson_type: required
---

# Bài Tập Thực Hành - Bài Toán Tối Ưu Convex

## 📝 **Bài tập 1: Standard form transformations**

**Đề bài:** Chuyển đổi các bài toán sau về standard forms:

a) **Mixed constraints:**
$$\min_{x \in \mathbb{R}^3} x_1^2 + x_2^2 + x_3^2$$
$$\text{s.t.} \quad x_1 + 2x_2 - x_3 = 5, \quad x_1 - x_2 \geq 3, \quad x_2 \leq 4, \quad x_3 \text{ free}$$

b) **Minimax problem:**
$$\min_x \max_{i=1,\ldots,m} (a_i^T x + b_i)$$

c) **Robust least squares:**
$$\min_x \max_{\lVert u \rVert_2 \leq 1} \lVert (A + \sum_{i=1}^k u_i B_i)x - b \rVert_2^2$$

**Yêu cầu:**
1. Transform về convex optimization standard form
2. Identify variables, constraints, và objective
3. Verify convexity của transformed problem
4. Discuss computational implications

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Mixed constraints problem**

**Handle free variable:** $$x_3 = x_3^+ - x_3^-$$ với $$x_3^+, x_3^- \geq 0$$

**Handle inequality:** $$x_1 - x_2 \geq 3 \Rightarrow -x_1 + x_2 \leq -3$$

**Standard form:**
$$\min_{x_1,x_2,x_3^+,x_3^-} x_1^2 + x_2^2 + (x_3^+)^2 + (x_3^-)^2 + 2x_3^+ x_3^-$$
$$\text{s.t.} \quad x_1 + 2x_2 - x_3^+ + x_3^- = 5$$
$$\quad -x_1 + x_2 \leq -3$$
$$\quad x_2 \leq 4$$
$$\quad x_1, x_2, x_3^+, x_3^- \geq 0$$

**Note:** Cross term $$2x_3^+ x_3^-$$ makes objective non-separable but still convex.

**Alternative approach:** Keep $$x_3$$ free, handle directly:
$$\min_{x_1,x_2,x_3} x_1^2 + x_2^2 + x_3^2$$
$$\text{s.t.} \quad x_1 + 2x_2 - x_3 = 5, \quad x_1 - x_2 \geq 3, \quad x_2 \leq 4, \quad x_1 \geq 0$$

**Bước 2: Minimax problem**

**Epigraph formulation:**
$$\min_{x,t} t$$
$$\text{s.t.} \quad a_i^T x + b_i \leq t, \quad i = 1,\ldots,m$$

**Convexity:** Linear objective, linear constraints $$\Rightarrow$$ LP

**Bước 3: Robust least squares**

**Worst-case reformulation:**
$$\max_{\lVert u \rVert_2 \leq 1} \lVert (A + \sum_{i=1}^k u_i B_i)x - b \rVert_2^2$$

**Matrix form:** $$\max_{\lVert u \rVert_2 \leq 1} \lVert Ax - b + (\sum_{i=1}^k u_i B_i)x \rVert_2^2$$

**Let $$y = (\sum_{i=1}^k u_i B_i)x$$:** Need $$\lVert y \rVert_2 \leq \lVert \sum_{i=1}^k B_i x \rVert_2$$

**Semidefinite reformulation:**
$$\min_{x,t} t$$
$$\text{s.t.} \quad \lVert Ax - b \rVert_2^2 + \lVert \sum_{i=1}^k B_i x \rVert_2^2 \leq t$$

**SOCP form:**
$$\min_{x,t} t$$
$$\text{s.t.} \quad \begin{bmatrix} t - \lVert Ax - b \rVert_2^2 \\ \sum_{i=1}^k B_i x \end{bmatrix} \in \mathcal{K}_{SOCP}$$

</details>

---

## 📝 **Bài tập 2: Optimality conditions analysis**

**Đề bài:** Analyze optimality conditions cho các bài toán:

a) **Constrained quadratic:**
$$\min_x \frac{1}{2}x^T Q x + c^T x \quad \text{s.t.} \quad Ax = b, \quad x \geq 0$$
với $$Q \succeq 0$$

b) **Entropy maximization:**
$$\max_x \sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad \sum_{i=1}^n x_i = 1, \quad \sum_{i=1}^n a_i x_i = \alpha, \quad x \geq 0$$

c) **Support vector machine:**
$$\min_{w,b,\xi} \frac{1}{2}\lVert w \rVert_2^2 + C\sum_{i=1}^m \xi_i$$
$$\text{s.t.} \quad y_i(w^T x_i + b) \geq 1 - \xi_i, \quad \xi_i \geq 0$$

**Yêu cầu:**
1. Derive KKT conditions
2. Analyze complementary slackness
3. Characterize optimal solutions
4. Discuss geometric interpretation

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Constrained quadratic**

**Lagrangian:**
$$L(x,\lambda,\mu) = \frac{1}{2}x^T Q x + c^T x + \lambda^T(Ax - b) - \mu^T x$$

**KKT conditions:**
- **Stationarity:** $$Qx + c + A^T \lambda - \mu = 0$$
- **Primal feasibility:** $$Ax = b, x \geq 0$$
- **Dual feasibility:** $$\mu \geq 0$$
- **Complementary slackness:** $$\mu_i x_i = 0, \forall i$$

**Analysis:**
- Nếu $$x_i > 0$$: $$\mu_i = 0$$
- Nếu $$x_i = 0$$: $$\mu_i \geq 0$$ (reduced cost)

**Solution structure:** Active set methods exploit sparsity pattern.

**Bước 2: Entropy maximization**

**Convert to minimization:**
$$\min_x -\sum_{i=1}^n x_i \log x_i \quad \text{s.t.} \quad \sum_{i=1}^n x_i = 1, \sum_{i=1}^n a_i x_i = \alpha, x \geq 0$$

**Lagrangian:**
$$L(x,\lambda_1,\lambda_2,\mu) = -\sum_{i=1}^n x_i \log x_i + \lambda_1(\sum x_i - 1) + \lambda_2(\sum a_i x_i - \alpha) - \sum \mu_i x_i$$

**KKT conditions:**
- **Stationarity:** $$-\log x_i - 1 + \lambda_1 + \lambda_2 a_i - \mu_i = 0$$
- **Complementary slackness:** $$\mu_i x_i = 0$$

**Optimal solution:**
$$x_i^* = e^{\lambda_1 + \lambda_2 a_i - 1}$$ (if $$x_i > 0$$)

**Exponential family form:** Maximum entropy distribution với moment constraints.

**Bước 3: Support vector machine**

**Lagrangian:**
$$L(w,b,\xi,\alpha,\beta) = \frac{1}{2}\lVert w \rVert_2^2 + C\sum \xi_i - \sum \alpha_i[y_i(w^T x_i + b) - 1 + \xi_i] - \sum \beta_i \xi_i$$

**KKT conditions:**
- **Stationarity:**
  - $$\nabla_w L = w - \sum \alpha_i y_i x_i = 0 \Rightarrow w = \sum \alpha_i y_i x_i$$
  - $$\nabla_b L = -\sum \alpha_i y_i = 0$$
  - $$\nabla_{\xi_i} L = C - \alpha_i - \beta_i = 0$$

- **Complementary slackness:**
  - $$\alpha_i[y_i(w^T x_i + b) - 1 + \xi_i] = 0$$
  - $$\beta_i \xi_i = 0$$

**Support vector characterization:**
- $$\alpha_i = 0$$: $$x_i$$ not support vector
- $$0 < \alpha_i < C$$: $$x_i$$ on margin ($$\xi_i = 0$$)
- $$\alpha_i = C$$: $$x_i$$ violates margin ($$\xi_i > 0$$)

</details>

---

## 📝 **Bài tập 3: Duality và sensitivity analysis**

**Đề bài:** Cho linear program:
$$\min_x c^T x \quad \text{s.t.} \quad Ax \leq b, \quad x \geq 0$$

a) Derive dual problem và analyze strong duality conditions
b) Perform sensitivity analysis: How does optimal value change với $$b$$?
c) Shadow prices interpretation
d) Parametric programming: $$b(\theta) = b_0 + \theta d$$

**Yêu cầu:**
1. Complete duality analysis
2. Sensitivity computations
3. Economic interpretation
4. Parametric solution paths

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Dual derivation**

**Primal:** $$\min_x c^T x \text{ s.t. } Ax \leq b, x \geq 0$$

**Lagrangian:** $$L(x,\lambda) = c^T x + \lambda^T(Ax - b)$$

**Dual function:** $$g(\lambda) = \inf_x L(x,\lambda) = \inf_x (c + A^T \lambda)^T x - \lambda^T b$$

**Condition for finiteness:** $$c + A^T \lambda \geq 0$$

**Dual problem:**
$$\max_\lambda -\lambda^T b \quad \text{s.t.} \quad A^T \lambda \leq c, \quad \lambda \geq 0$$

Equivalently:
$$\max_\lambda b^T \lambda \quad \text{s.t.} \quad A^T \lambda \leq c, \quad \lambda \geq 0$$

**Bước 2: Strong duality conditions**

**Slater's condition:** $$\exists x > 0 \text{ s.t. } Ax < b$$

**Fundamental theorem of LP:** Strong duality holds khi cả primal và dual feasible.

**Complementary slackness:**
- $$(A^T \lambda^* - c)_j x_j^* = 0, \forall j$$
- $$\lambda_i^* (Ax^* - b)_i = 0, \forall i$$

**Bước 3: Sensitivity analysis**

**Optimal value function:** $$f^*(b) = \min\{c^T x : Ax \leq b, x \geq 0\}$$

**Envelope theorem:** $$\nabla_b f^*(b) = \lambda^*(b)$$

**Shadow price interpretation:** $$\lambda_i^*$$ = marginal value của resource $$i$$

**Practical computation:**
- Solve primal-dual pair
- $$\lambda^*$$ gives sensitivity coefficients
- Valid trong neighborhood của current $$b$$

**Bước 4: Parametric programming**

**Parameterized problem:** $$\min_x c^T x \text{ s.t. } Ax \leq b_0 + \theta d, x \geq 0$$

**Optimal value:** $$f^*(\theta) = f^*(b_0 + \theta d)$$

**Piecewise linear:** $$f^*(\theta)$$ piecewise linear trong $$\theta$$

**Critical points:** Breakpoints khi optimal basis changes

**Solution path:**
1. Start với optimal solution tại $$\theta = 0$$
2. Increase $$\theta$$ until basis change
3. Pivot to new basis
4. Repeat until desired $$\theta$$

</details>

---

## 📝 **Bài tập 4: Relaxation techniques**

**Đề bài:** Consider integer programming problem:
$$\min_x c^T x \quad \text{s.t.} \quad Ax \leq b, \quad x_i \in \{0,1\}, \quad i \in I$$

a) **LP relaxation:** Relax $$x_i \in [0,1]$$
b) **Lagrangian relaxation:** Dualize subset của constraints
c) **SDP relaxation:** $$x_i x_j = X_{ij}$$ với $$X \succeq 0$$
d) **Convex hull:** Characterize $$\text{conv}(\text{feasible integer points})$$

**Yêu cầu:**
1. Formulate relaxations
2. Analyze bound quality
3. Tightening techniques
4. Computational comparison

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: LP relaxation**

**Relaxed problem:**
$$\min_x c^T x \quad \text{s.t.} \quad Ax \leq b, \quad 0 \leq x_i \leq 1, \quad i \in I$$

**Properties:**
- **Lower bound:** $$z_{LP} \leq z_{IP}$$
- **Polynomial time** solvable
- **Tight khi** optimal LP solution integer

**Integrality gap:** $$\frac{z_{IP}}{z_{LP}}$$

**Bước 2: Lagrangian relaxation**

**Dualize constraints $$A_2 x \leq b_2$$:**
$$L_D(\lambda) = \min_x \{c^T x + \lambda^T(A_2 x - b_2) : A_1 x \leq b_1, x_i \in \{0,1\}\}$$

**Dual bound:** $$\max_{\lambda \geq 0} L_D(\lambda)$$

**Advantages:**
- **Decomposition:** Nếu $$A_1$$ block diagonal
- **Better bounds:** Potentially tighter than LP relaxation
- **Subgradient optimization:** For dual problem

**Bước 3: SDP relaxation**

**Quadratic reformulation:** $$\min \sum_{ij} c_{ij} x_i x_j$$

**SDP relaxation:**
$$\min_{X} \sum_{ij} c_{ij} X_{ij}$$
$$\text{s.t.} \quad \text{linear constraints in } X$$
$$\quad X_{ii} = x_i, \quad X \succeq 0$$

**Rank-1 constraint:** $$X = xx^T$$ (relaxed)

**Applications:**
- **Max-cut:** Goemans-Williamson algorithm
- **Quadratic assignment:** QAP relaxations

**Bước 4: Convex hull characterization**

**Polytope:** $$P_I = \text{conv}\{x \in \{0,1\}^n : Ax \leq b\}$$

**Facet identification:**
- **Valid inequalities:** $$\alpha^T x \leq \beta$$ for all $$x \in P_I$$
- **Facet-defining:** Maximal valid inequalities

**Cutting plane methods:**
1. Solve LP relaxation
2. If fractional, find violated valid inequality
3. Add cut và resolve
4. Repeat until integer solution

**Examples:**
- **Knapsack:** Cover inequalities
- **TSP:** Subtour elimination constraints

</details>

---

## 📝 **Bài tập 5: Robust optimization**

**Đề bài:** Portfolio optimization under uncertainty:
$$\min_x x^T \Sigma x \quad \text{s.t.} \quad \mu^T x \geq r, \quad \mathbf{1}^T x = 1, \quad x \geq 0$$

với uncertain parameters $$(\mu, \Sigma)$$.

a) **Box uncertainty:** $$\mu_i \in [\underline{\mu}_i, \overline{\mu}_i]$$
b) **Ellipsoidal uncertainty:** $$\mu \in \{\mu_0 + Pu : \lVert u \rVert_2 \leq 1\}$$
c) **Factor model:** $$\mu = \beta f + \epsilon$$ với $$f$$ uncertain
d) **Distributionally robust:** $$\mathbb{E}_P[\mu] = \mu_0$$, $$\text{Var}_P[\mu] \preceq \Sigma_0$$

**Yêu cầu:**
1. Reformulate as deterministic convex programs
2. Analyze conservatism levels
3. Compare computational complexity
4. Practical implementation

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Box uncertainty**

**Worst-case constraint:** $$\min_{\mu \in \mathcal{U}} \mu^T x \geq r$$

với $$\mathcal{U} = \{\mu : \underline{\mu}_i \leq \mu_i \leq \overline{\mu}_i\}$$

**Worst-case analysis:**
$$\min_{\mu \in \mathcal{U}} \mu^T x = \sum_{i: x_i \geq 0} \underline{\mu}_i x_i + \sum_{i: x_i < 0} \overline{\mu}_i x_i$$

**Robust formulation:**
$$\min_x x^T \Sigma x$$
$$\text{s.t.} \quad \sum_{i: x_i \geq 0} \underline{\mu}_i x_i + \sum_{i: x_i < 0} \overline{\mu}_i x_i \geq r$$
$$\quad \mathbf{1}^T x = 1, \quad x \geq 0$$

**Bước 2: Ellipsoidal uncertainty**

**Uncertainty set:** $$\mathcal{U} = \{\mu_0 + Pu : \lVert u \rVert_2 \leq 1\}$$

**Worst-case constraint:**
$$\min_{\lVert u \rVert_2 \leq 1} (\mu_0 + Pu)^T x = \mu_0^T x - \lVert P^T x \rVert_2 \geq r$$

**Robust formulation:**
$$\min_x x^T \Sigma x$$
$$\text{s.t.} \quad \mu_0^T x - \lVert P^T x \rVert_2 \geq r$$
$$\quad \mathbf{1}^T x = 1, \quad x \geq 0$$

**SOCP formulation:** Second-order cone constraint

**Bước 3: Factor model**

**Model:** $$\mu = \beta f + \epsilon$$ với $$f \in \mathcal{F}$$, $$\epsilon$$ noise

**Uncertainty set:** $$\mathcal{U} = \{\beta f + \epsilon : f \in \mathcal{F}, \lVert \epsilon \rVert_2 \leq \sigma\}$$

**Worst-case analysis:**
$$\min_{\mu \in \mathcal{U}} \mu^T x = \min_{f \in \mathcal{F}} (\beta f)^T x - \sigma \lVert x \rVert_2$$

**Multi-factor case:** $$\mu = \sum_{k=1}^K \beta_k f_k + \epsilon$$

**Bước 4: Distributionally robust**

**Ambiguity set:** $$\mathcal{P} = \{P : \mathbb{E}_P[\mu] = \mu_0, \text{Cov}_P[\mu] \preceq \Sigma_0\}$$

**Worst-case expectation:**
$$\min_{P \in \mathcal{P}} \mathbb{E}_P[\mu^T x] = \mu_0^T x - \sqrt{x^T \Sigma_0 x}$$

**Robust formulation:**
$$\min_x x^T \Sigma x$$
$$\text{s.t.} \quad \mu_0^T x - \sqrt{x^T \Sigma_0 x} \geq r$$
$$\quad \mathbf{1}^T x = 1, \quad x \geq 0$$

**Connection:** Ellipsoidal uncertainty với $$P^T P = \Sigma_0$$

</details>

---

## 📝 **Bài tập 6: Multi-objective optimization**

**Đề bài:** Consider bi-objective problem:
$$\min_x (f_1(x), f_2(x)) \quad \text{s.t.} \quad x \in \mathcal{X}$$

với $$f_1, f_2$$ convex và $$\mathcal{X}$$ convex.

a) **Pareto efficiency:** Characterize Pareto optimal solutions
b) **Scalarization methods:** Weighted sum, $$\epsilon$$-constraint, achievement
c) **Pareto frontier computation:** Systematic enumeration
d) **Applications:** Portfolio optimization, engineering design

**Yêu cầu:**
1. Theoretical characterization
2. Algorithmic approaches
3. Computational examples
4. Practical considerations

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Pareto efficiency characterization**

**Definition:** $$x^*$$ Pareto optimal nếu không tồn tại $$x \in \mathcal{X}$$ sao cho:
- $$f_i(x) \leq f_i(x^*)$$ for all $$i$$
- $$f_j(x) < f_j(x^*)$$ for some $$j$$

**Necessary condition:** Nếu $$x^*$$ Pareto optimal, tồn tại $$\lambda \geq 0$$, $$\lambda \neq 0$$ sao cho $$x^*$$ solves:
$$\min_x \sum_{i=1}^2 \lambda_i f_i(x) \quad \text{s.t.} \quad x \in \mathcal{X}$$

**Sufficient condition:** Nếu $$\lambda > 0$$ và $$x^*$$ uniquely solves weighted problem, thì $$x^*$$ Pareto optimal.

**Bước 2: Scalarization methods**

**Weighted sum method:**
$$\min_x \lambda_1 f_1(x) + \lambda_2 f_2(x) \quad \text{s.t.} \quad x \in \mathcal{X}$$

với $$\lambda_1, \lambda_2 \geq 0$$, $$\lambda_1 + \lambda_2 = 1$$

**Limitations:** Cannot find non-convex parts của Pareto frontier

**$$\epsilon$$-constraint method:**
$$\min_x f_1(x) \quad \text{s.t.} \quad f_2(x) \leq \epsilon, \quad x \in \mathcal{X}$$

**Advantages:** Can find entire Pareto frontier

**Achievement scalarization:**
$$\min_{x,t} t \quad \text{s.t.} \quad f_i(x) - z_i^* \leq t, \quad x \in \mathcal{X}$$

với $$z^*$$ ideal point: $$z_i^* = \min_x f_i(x)$$

**Bước 3: Pareto frontier computation**

**Algorithm 1: Weighted sum sweep**
```
For λ₁ = 0 to 1 (step δ):
    λ₂ = 1 - λ₁
    Solve: min λ₁f₁(x) + λ₂f₂(x) s.t. x ∈ X
    Store solution if Pareto optimal
```

**Algorithm 2: $$\epsilon$$-constraint sweep**
```
Compute range [ε_min, ε_max] for f₂
For ε = ε_min to ε_max (step δ):
    Solve: min f₁(x) s.t. f₂(x) ≤ ε, x ∈ X
    Store solution
```

**Algorithm 3: Normal boundary intersection**
- Construct convex hull của individual minima
- Generate evenly distributed points
- Solve constrained problems

**Bước 4: Portfolio example**

**Objectives:**
- $$f_1(x) = x^T \Sigma x$$ (risk)
- $$f_2(x) = -\mu^T x$$ (negative return)

**Constraints:** $$\mathbf{1}^T x = 1$$, $$x \geq 0$$

**Efficient frontier:** 
$$\min_x x^T \Sigma x \quad \text{s.t.} \quad \mu^T x \geq r, \quad \mathbf{1}^T x = 1, \quad x \geq 0$$

**Parametric solution:** $$r \in [r_{\min}, r_{\max}]$$

**Mean-variance frontier:** Hyperbola trong $$(r, \sigma)$$ space

</details>

---

## 📝 **Bài tập 7: Stochastic optimization**

**Đề bài:** Two-stage stochastic program:
$$\min_{x} c^T x + \mathbb{E}_\xi[Q(x, \xi)]$$
$$\text{s.t.} \quad Ax = b, \quad x \geq 0$$

với $$Q(x, \xi) = \min_y \{q^T y : Wy = h - Tx, y \geq 0\}$$

a) **Sample average approximation (SAA)**
b) **Scenario-based formulation**
c) **Benders decomposition**
d) **Risk measures:** CVaR, robust optimization

**Yêu cầu:**
1. Deterministic equivalent formulations
2. Decomposition algorithms
3. Statistical analysis
4. Risk-aware extensions

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Sample average approximation**

**True problem:** $$\min_x \{c^T x + \mathbb{E}_\xi[Q(x, \xi)] : Ax = b, x \geq 0\}$$

**SAA approximation:** $$\min_x \{c^T x + \frac{1}{N}\sum_{i=1}^N Q(x, \xi^i) : Ax = b, x \geq 0\}$$

với $$\xi^1, \ldots, \xi^N$$ i.i.d. samples

**Convergence:** $$\hat{x}_N \to x^*$$ as $$N \to \infty$$ (w.p.1)

**Sample size:** $$N = O(\epsilon^{-2})$$ for $$\epsilon$$-optimal solution

**Bước 2: Scenario-based formulation**

**Deterministic equivalent:**
$$\min_{x,y^1,\ldots,y^N} c^T x + \frac{1}{N}\sum_{i=1}^N q^T y^i$$
$$\text{s.t.} \quad Ax = b, \quad x \geq 0$$
$$\quad W y^i = h^i - T^i x, \quad y^i \geq 0, \quad i = 1,\ldots,N$$

**Large-scale LP:** $$(n + Nm)$$ variables, $$(m + Nm)$$ constraints

**Block structure:** Exploitable bằng decomposition

**Bước 3: Benders decomposition**

**Master problem:**
$$\min_{x,\theta} c^T x + \theta$$
$$\text{s.t.} \quad Ax = b, \quad x \geq 0$$
$$\quad \theta \geq \frac{1}{N}\sum_{i=1}^N (q^T y^i + (\pi^i)^T(h^i - T^i x))$$

**Subproblems:** For each scenario $$i$$:
$$\min_{y^i} q^T y^i \quad \text{s.t.} \quad W y^i = h^i - T^i x, \quad y^i \geq 0$$

**Algorithm:**
1. Solve master problem → get $$x^k$$
2. Solve subproblems → get $$\pi^{i,k}$$
3. Add Benders cuts
4. Repeat until convergence

**Bước 4: Risk measures**

**Conditional Value-at-Risk (CVaR):**
$$\text{CVaR}_\alpha[Z] = \mathbb{E}[Z | Z \geq \text{VaR}_\alpha[Z]]$$

**Optimization formulation:**
$$\min_{x,\eta,s} c^T x + \eta + \frac{1}{(1-\alpha)N}\sum_{i=1}^N s_i$$
$$\text{s.t.} \quad Ax = b, \quad x \geq 0$$
$$\quad s_i \geq Q(x, \xi^i) - \eta, \quad s_i \geq 0$$

**Risk-constrained:**
$$\min_x c^T x \quad \text{s.t.} \quad \text{CVaR}_\alpha[Q(x, \xi)] \leq \gamma$$

**Robust approach:** Worst-case over ambiguity set
$$\min_x c^T x + \max_{P \in \mathcal{P}} \mathbb{E}_P[Q(x, \xi)]$$

</details>

---

## 📝 **Bài tập 8: Conic optimization**

**Đề bài:** Analyze conic optimization problems:

a) **Second-order cone programming (SOCP):**
$$\min_x c^T x \quad \text{s.t.} \quad \lVert A_i x + b_i \rVert_2 \leq c_i^T x + d_i$$

b) **Semidefinite programming (SDP):**
$$\min_X \langle C, X \rangle \quad \text{s.t.} \quad \langle A_i, X \rangle = b_i, \quad X \succeq 0$$

c) **Exponential cone programming:**
$$\min_x c^T x \quad \text{s.t.} \quad (x_i, x_j, x_k) \in \mathcal{K}_{\exp}$$

**Yêu cầu:**
1. Standard form representations
2. Duality theory
3. Interior-point algorithms
4. Applications và modeling

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Second-order cone programming**

**Standard form:**
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b, \quad x \in \mathcal{K}$$

với $$\mathcal{K} = \mathcal{K}_1 \times \cdots \times \mathcal{K}_m$$ và $$\mathcal{K}_i = \{(t, u) : \lVert u \rVert_2 \leq t\}$$

**Dual problem:**
$$\max_y b^T y \quad \text{s.t.} \quad A^T y + s = c, \quad s \in \mathcal{K}$$

**Self-dual cone:** $$\mathcal{K}_i^* = \mathcal{K}_i$$

**Applications:**
- **Robust optimization:** Ellipsoidal uncertainty
- **Portfolio optimization:** Risk measures
- **Filter design:** Frequency response constraints

**Bước 2: Semidefinite programming**

**Standard form:**
$$\min_X \langle C, X \rangle \quad \text{s.t.} \quad \langle A_i, X \rangle = b_i, \quad X \succeq 0$$

**Vectorized form:** $$\min_x c^T x \text{ s.t. } Ax = b, x \in \mathcal{S}_+^n$$

**Dual problem:**
$$\max_y b^T y \quad \text{s.t.} \quad \sum_{i=1}^m y_i A_i + S = C, \quad S \succeq 0$$

**Strong duality:** Holds under Slater condition

**Applications:**
- **Combinatorial optimization:** Max-cut, coloring
- **Control theory:** LMI constraints
- **Machine learning:** Kernel methods

**Bước 3: Exponential cone**

**Exponential cone:** $$\mathcal{K}_{\exp} = \{(x,y,z) : ye^{x/y} \leq z, y > 0\} \cup \{(x,0,z) : x \leq 0, z \geq 0\}$$

**Dual cone:** $$\mathcal{K}_{\exp}^* = \{(u,v,w) : u < 0, -ue^{v/u} \leq ew, \text{ or } u = 0, v \geq 0, w \geq 0\}$$

**Applications:**
- **Entropy optimization:** $$\min \sum x_i \log x_i$$
- **Geometric programming:** After log transformation
- **Relative entropy:** KL divergence minimization

**Modeling examples:**

**Entropy:** $$x \log x \leq t \Leftrightarrow (t, x, 1) \in \mathcal{K}_{\exp}^*$$

**Log-sum-exp:** $$\log(\sum e^{x_i}) \leq t \Leftrightarrow$$ system của exponential cone constraints

**Power cone:** $$x_1^{p_1} \cdots x_k^{p_k} \geq |x_{k+1}|$$ reducible to exponential cones

</details>

---

## 📝 **Bài tập 9: Approximation algorithms**

**Đề bài:** Design approximation algorithms cho non-convex problems:

a) **Max-cut SDP relaxation:** Goemans-Williamson algorithm
b) **Facility location:** LP-based rounding
c) **Set cover:** Greedy algorithm analysis
d) **Knapsack:** FPTAS via dynamic programming

**Yêu cầu:**
1. Relaxation formulations
2. Rounding schemes
3. Approximation ratio analysis
4. Performance guarantees

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Max-cut SDP relaxation**

**Original problem:** $$\max_{x \in \{-1,1\}^n} \frac{1}{4}\sum_{(i,j) \in E} w_{ij}(1 - x_i x_j)$$

**Equivalent:** $$\max_{x \in \{-1,1\}^n} \frac{1}{4}\sum_{(i,j) \in E} w_{ij}(1 - x_i x_j)$$

**SDP relaxation:** $$X = xx^T \Rightarrow X_{ij} = x_i x_j$$
$$\max_X \frac{1}{4}\sum_{(i,j) \in E} w_{ij}(1 - X_{ij})$$
$$\text{s.t.} \quad X_{ii} = 1, \quad X \succeq 0$$

**Goemans-Williamson algorithm:**
1. Solve SDP relaxation → optimal $$X^*$$
2. Cholesky decomposition: $$X^* = V^T V$$
3. Random hyperplane: $$r \sim \mathcal{N}(0, I)$$
4. Rounding: $$x_i = \text{sign}(r^T v_i)$$

**Approximation ratio:** $$\alpha_{GW} = \min_{0 \leq \theta \leq \pi} \frac{2}{\pi} \cdot \frac{\theta}{1 - \cos \theta} \approx 0.878$$

**Bước 2: Facility location**

**Problem:** $$\min \sum_{i \in F} f_i y_i + \sum_{i \in F, j \in C} c_{ij} x_{ij}$$
$$\text{s.t.} \quad \sum_{i \in F} x_{ij} = 1, \quad x_{ij} \leq y_i, \quad x_{ij}, y_i \in \{0,1\}$$

**LP relaxation:** $$x_{ij}, y_i \in [0,1]$$

**Rounding algorithm:**
1. Solve LP relaxation
2. Open facility $$i$$ với probability $$y_i^*$$
3. Connect client $$j$$ to closest open facility

**Analysis:** Expected cost $$\leq 2 \times$$ LP optimal

**Improved rounding:** Deterministic 1.61-approximation

**Bước 3: Set cover greedy**

**Problem:** $$\min \sum_{S \in \mathcal{S}} x_S \quad \text{s.t.} \quad \sum_{S: e \in S} x_S \geq 1, \quad x_S \in \{0,1\}$$

**Greedy algorithm:**
```
While uncovered elements exist:
    Pick set S maximizing |S ∩ (uncovered elements)| / cost(S)
    Add S to solution
```

**Analysis:** $$H_n$$-approximation với $$H_n = \sum_{i=1}^n \frac{1}{i} \approx \ln n$$

**LP-based analysis:**
- Dual fitting method
- Primal-dual algorithm

**Bước 4: Knapsack FPTAS**

**Problem:** $$\max \sum_{i=1}^n v_i x_i \quad \text{s.t.} \quad \sum_{i=1}^n w_i x_i \leq W, \quad x_i \in \{0,1\}$$

**Dynamic programming:** $$O(nW)$$ time (pseudo-polynomial)

**FPTAS approach:**
1. Scale profits: $$\tilde{v}_i = \lfloor v_i / K \rfloor$$ với $$K = \epsilon \cdot v_{\max} / n$$
2. DP on scaled instance: $$O(n^2 / \epsilon)$$ time
3. Return solution

**Approximation guarantee:** $$(1 - \epsilon)$$-optimal

**Key insight:** Rounding preserves near-optimality nhưng reduces state space

</details>

---

## 📝 **Bài tập 10: Machine learning applications**

**Đề bài:** Formulate machine learning problems as convex optimization:

a) **Logistic regression:** $$\min_w \sum_{i=1}^n \log(1 + e^{-y_i w^T x_i}) + \lambda \lVert w \rVert_2^2$$

b) **Support vector regression:** $$\min_{w,b} \frac{1}{2}\lVert w \rVert_2^2 + C\sum_{i=1}^n \max(0, |y_i - w^T x_i - b| - \epsilon)$$

c) **Matrix completion:** $$\min_X \lVert X \rVert_* \quad \text{s.t.} \quad X_{ij} = M_{ij}, (i,j) \in \Omega$$

d) **Sparse coding:** $$\min_{D,\alpha} \frac{1}{2}\lVert Y - D\alpha \rVert_F^2 + \lambda \lVert \alpha \rVert_1$$

**Yêu cầu:**
1. Convexity analysis
2. Optimality conditions
3. Algorithmic approaches
4. Regularization effects

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**Bước 1: Logistic regression**

**Objective:** $$f(w) = \sum_{i=1}^n \log(1 + e^{-y_i w^T x_i}) + \lambda \lVert w \rVert_2^2$$

**Convexity:** 
- Log-sum-exp convex
- $$\ell_2$$ regularization convex
- Sum preserves convexity

**Gradient:** $$\nabla f(w) = -\sum_{i=1}^n \frac{y_i x_i}{1 + e^{y_i w^T x_i}} + 2\lambda w$$

**Hessian:** $$\nabla^2 f(w) = \sum_{i=1}^n \frac{e^{y_i w^T x_i}}{(1 + e^{y_i w^T x_i})^2} x_i x_i^T + 2\lambda I \succ 0$$

**Algorithms:**
- **Newton method:** Fast convergence
- **BFGS:** Quasi-Newton
- **SGD:** Scalable to large datasets

**Bước 2: Support vector regression**

**Reformulation:** $$\min_{w,b,\xi,\xi^*} \frac{1}{2}\lVert w \rVert_2^2 + C\sum_{i=1}^n (\xi_i + \xi_i^*)$$
$$\text{s.t.} \quad y_i - w^T x_i - b \leq \epsilon + \xi_i$$
$$\quad w^T x_i + b - y_i \leq \epsilon + \xi_i^*$$
$$\quad \xi_i, \xi_i^* \geq 0$$

**Dual problem:**
$$\max_{\alpha,\alpha^*} -\frac{1}{2}\sum_{i,j}(\alpha_i - \alpha_i^*)(\alpha_j - \alpha_j^*) x_i^T x_j - \epsilon \sum_i(\alpha_i + \alpha_i^*) + \sum_i y_i(\alpha_i - \alpha_i^*)$$
$$\text{s.t.} \quad \sum_i(\alpha_i - \alpha_i^*) = 0, \quad 0 \leq \alpha_i, \alpha_i^* \leq C$$

**Support vectors:** $$x_i$$ với $$\alpha_i > 0$$ hoặc $$\alpha_i^* > 0$$

**Bước 3: Matrix completion**

**Nuclear norm:** $$\lVert X \rVert_* = \sum_{i=1}^{\min(m,n)} \sigma_i(X)$$

**Convexity:** Nuclear norm là convex (spectral function)

**SDP formulation:**
$$\min_{X,U,V} \frac{1}{2}(\text{tr}(U) + \text{tr}(V))$$
$$\text{s.t.} \quad \begin{bmatrix} U & X \\ X^T & V \end{bmatrix} \succeq 0, \quad X_{ij} = M_{ij}$$

**Algorithms:**
- **Proximal gradient:** Soft thresholding của SVD
- **ADMM:** Alternating direction method
- **Frank-Wolfe:** Conditional gradient

**Bước 4: Sparse coding**

**Bi-convex:** Convex trong $$D$$ (fixed $$\alpha$$) và convex trong $$\alpha$$ (fixed $$D$$)

**Dictionary update:** $$\min_D \frac{1}{2}\lVert Y - D\alpha \rVert_F^2$$ (least squares)

**Sparse coding:** $$\min_\alpha \frac{1}{2}\lVert Y - D\alpha \rVert_F^2 + \lambda \lVert \alpha \rVert_1$$ (LASSO)

**Alternating minimization:**
1. **Sparse coding step:** Solve LASSO for each column
2. **Dictionary update:** Least squares với normalization
3. Repeat until convergence

**LASSO solution:** Soft thresholding
$$\alpha_j^{(k+1)} = \text{soft}(\alpha_j^{(k)} - \eta \nabla_j f, \eta \lambda)$$

với $$\text{soft}(x, \tau) = \text{sign}(x) \max(|x| - \tau, 0)$$

</details>

---

## 💡 Mẹo Thực Hành

#### **Khi formulate optimization problems:**
- **Identify structure:** LP, QP, SOCP, SDP, GP
- **Check convexity:** Objective và constraints
- **Standard forms:** Transform để sử dụng efficient solvers

#### **Khi analyze optimality:**
- **KKT conditions:** Necessary và sufficient conditions
- **Complementary slackness:** Active constraints
- **Sensitivity analysis:** Shadow prices và perturbations

#### **Khi design algorithms:**
- **Exploit structure:** Sparsity, separability, decomposition
- **Approximation:** When exact solution intractable
- **Robustness:** Handle uncertainty và noise

---

## 📚 Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 4: Convex Optimization Problems

2. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming*. Athena Scientific.

4. **Shapiro, A., Dentcheva, D., & Ruszczyński, A.** (2009). *Lectures on Stochastic Programming*. SIAM.

5. **Williamson, D. P., & Shmoys, D. B.** (2011). *The Design of Approximation Algorithms*. Cambridge University Press.

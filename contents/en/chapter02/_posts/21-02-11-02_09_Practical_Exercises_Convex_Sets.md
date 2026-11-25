---
layout: post
title: '02-09 Practical Exercises - Convex Sets'
chapter: "2"
order: 19
owner: "GitHub Copilot"
lang: en
categories:
  - chapter02
lesson_type: required
redirect_from:
  - /contents/en/chapter02/02_08_Practical_Exercises_Convex_Sets/
---

Knowing that a set is convex is the first step; *projecting* an infeasible iterate back onto that convex set is the computational core of projected gradient descent and ADMM. These practical exercises move you from proofs to computation—testing convexity, finding separating hyperplanes, computing convex hulls and dual cones, and projecting points onto polyhedra, balls, and simplexes.

## Background Knowledge Map: Computational Skills in These Exercises

- **Algebraic & Computational Verification:** Checking convexity by rewriting sets as intersections, affine preimages, or epigraphs, and validating numerically.
- **Dual Cones & Separation Oracles:** Computing explicit separating hyperplanes and dual cones for polyhedral and norm-cone constraints.
- **Euclidean Projections ($$\Pi_C(y) = \arg\min_{x \in C} \frac{1}{2}\|x - y\|_2^2$$):** Deriving closed-form projections onto hyperplanes, boxes, $$\ell_2$$ balls, $$\mathbb{R}_+^n$$, and the probability simplex $$\Delta_n$$.
- **Extreme Points & Vertices:** Identifying extreme points of polytopes—where linear objectives always attain their optima.

### Step-by-Step Worked Example (Read Slowly): Projecting onto $$\mathbb{R}_+^3$$ and the Probability Simplex $$\Delta_3$$

Project the vector $$y = (3, -2, 1)^T$$ onto two fundamental convex sets:

1. **Projection onto the nonnegative orthant $$\mathbb{R}_+^3$$:** Componentwise clipping $$x_i^* = \max(y_i, 0)$$ immediately gives
   $$\Pi_{\mathbb{R}_+^3}(y) = (3, 0, 1)^T.$$
2. **Projection onto the probability simplex $$\Delta_3 = \{x \ge 0 : x_1 + x_2 + x_3 = 1\}$$:** By KKT conditions, $$\Pi_{\Delta_3}(y)_i = \max(y_i - \nu, 0)$$ where the threshold $$\nu \in \mathbb{R}$$ is chosen so the entries sum to $$1$$.
   - Try $$\nu = 2$$:
     $$\max(3 - 2, 0) = 1, \qquad \max(-2 - 2, 0) = 0, \qquad \max(1 - 2, 0) = 0.$$
   - Sum $$= 1 + 0 + 0 = 1$$! Thus $$x^* = \Pi_{\Delta_3}(y) = (1, 0, 0)^T$$.
3. **Verify the variational optimality condition $$(y - x^*)^T(x - x^*) \le 0 \;\forall x \in \Delta_3$$:**
   With $$y - x^* = (2, -2, 1)^T$$ and $$x_1 - 1 = -(x_2 + x_3)$$ for any $$x \in \Delta_3$$,
   $$(y - x^*)^T(x - x^*) = 2(-x_2 - x_3) - 2x_2 + x_3 = -4x_2 - x_3 \le 0,$$
   certifying $$x^* = (1, 0, 0)^T$$ as the exact Euclidean projection.

# Practical Exercises - Convex Sets

## **Exercise 1: Verification of convex sets**

**Problem:** (Exercise 2.1 from Boyd & Vandenberghe)
Determine whether the following sets are convex:

a) $$S_1 = \{x \in \mathbb{R}^n : \lVert x \rVert_2 \leq 1\}$$

b) $$S_2 = \{x \in \mathbb{R}^n : \lVert x \rVert_\infty \leq 1\}$$

c) $$S_3 = \{x \in \mathbb{R}^n : x^T P x \leq 1\}$$ with $$P \succeq 0$$

d) $$S_4 = \{x \in \mathbb{R}^n : \lVert x_i \rVert  \leq a_i, i = 1,\ldots,n\}$$

**Task:**
1. Prove convexity from the definition
2. Verify using operations that preserve convexity
3. Visualize in $$\mathbb{R}^2$$
4. Find the extreme points of each set

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Proof from the definition**

**a) $$\ell_2$$ ball:** $$S_1 = \{x : \lVert x \rVert_2 \leq 1\}$$

For $$x, y \in S_1$$ and $$\theta \in [0,1]$$:
$$\lVert \theta x + (1-\theta) y \rVert_2 \leq \theta \lVert x \rVert_2 + (1-\theta) \lVert y \rVert_2 \leq \theta \cdot 1 + (1-\theta) \cdot 1 = 1$$

$$\Rightarrow$$ Convex

**b) $$\ell_\infty$$ ball:** $$S_2 = \{x : \max_i |x_i| \leq 1\}$$

$$\max_i |\theta x_i + (1-\theta) y_i| \leq \max_i (\theta |x_i| + (1-\theta) |y_i|) \leq \theta \max_i |x_i| + (1-\theta) \max_i |y_i| \leq 1$$

$$\Rightarrow$$ Convex

**c) Ellipsoid:** $$S_3 = \{x : x^T P x \leq 1\}$$ with $$P \succeq 0$$

$$(\theta x + (1-\theta) y)^T P (\theta x + (1-\theta) y) = \theta^2 x^T P x + 2\theta(1-\theta) x^T P y + (1-\theta)^2 y^T P y$$

Since $$P \succeq 0$$, the quadratic form is a convex function, so its sublevel set is convex.

**d) Hyperrectangle:** $$S_4 = \prod_{i=1}^n [-a_i, a_i]$$

A Cartesian product of convex sets (intervals) is convex.

**Step 2: Operations that preserve convexity**
- **a, b:** Sublevel sets of convex functions (norms)
- **c:** Sublevel set of a convex quadratic form
- **d:** Cartesian product of convex intervals

**Step 3: Extreme points**
- **a:** The boundary $$\{x : \lVert x \rVert_2 = 1\}$$ (infinitely many extreme points)
- **b:** The vertices $$\{(\pm 1, \ldots, \pm 1)\}$$ ($$2^n$$ extreme points; the points $$\pm e_i$$ are the vertices of the $$\ell_1$$ ball, not of the $$\ell_\infty$$ ball)
- **c:** Depends on $$P$$: if $$P \succ 0$$, every point on the boundary $$x^T P x = 1$$ is an extreme point; if $$P$$ is singular, the set contains an entire line and has no extreme points
- **d:** The vertices $$\{(\pm a_1, \ldots, \pm a_n)\}$$ ($$2^n$$ extreme points)

</details>

---

## **Exercise 2: Operations preserving convexity**

**Problem:** (Exercise 2.2 from Boyd & Vandenberghe)
Let $$C_1, C_2 \subseteq \mathbb{R}^n$$ be convex sets. Prove or disprove convexity of:

a) **Intersection:** $$C_1 \cap C_2$$

b) **Union:** $$C_1 \cup C_2$$

c) **Minkowski sum:** $$C_1 + C_2 = \{x + y : x \in C_1, y \in C_2\}$$

d) **Cartesian product:** $$C_1 \times C_2$$

e) **Affine transformation:** $$f(C_1) = \{Ax + b : x \in C_1\}$$

**Task:**
1. Give mathematical proofs for the true cases
2. Give counterexamples for the false cases
3. Visualize with concrete examples
4. Generalize to arbitrary collections

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Intersection - CONVEX**

<div class="textbook-proof" markdown="1">
**Proof:** For $$x, y \in C_1 \cap C_2$$ and $$\theta \in [0,1]$$:
- $$x, y \in C_1 \Rightarrow \theta x + (1-\theta) y \in C_1$$ (since $$C_1$$ is convex)
- $$x, y \in C_2 \Rightarrow \theta x + (1-\theta) y \in C_2$$ (since $$C_2$$ is convex)
- $$\Rightarrow \theta x + (1-\theta) y \in C_1 \cap C_2$$
</div>

**Generalization:** $$\bigcap_{i \in I} C_i$$ is convex if every $$C_i$$ is convex.

**Step 2: Union - NOT CONVEX**

**Counterexample:** $$C_1 = \{(x,0) : x \geq 0\}$$, $$C_2 = \{(0,y) : y \geq 0\}$$

Both are convex, but $$C_1 \cup C_2$$ is not:
- $$(1,0) \in C_1 \cup C_2$$, $$(0,1) \in C_1 \cup C_2$$
- $$\frac{1}{2}(1,0) + \frac{1}{2}(0,1) = (\frac{1}{2}, \frac{1}{2}) \notin C_1 \cup C_2$$

**Step 3: Minkowski sum - CONVEX**

<div class="textbook-proof" markdown="1">
**Proof:** For $$z_1, z_2 \in C_1 + C_2$$:
- $$z_1 = x_1 + y_1$$, $$z_2 = x_2 + y_2$$ with $$x_i \in C_1, y_i \in C_2$$
- $$\theta z_1 + (1-\theta) z_2 = \theta(x_1 + y_1) + (1-\theta)(x_2 + y_2)$$
- $$= (\theta x_1 + (1-\theta) x_2) + (\theta y_1 + (1-\theta) y_2)$$
- $$\in C_1 + C_2$$ (since $$C_1, C_2$$ are convex)
</div>

**Step 4: Cartesian product - CONVEX**

<div class="textbook-proof" markdown="1">
**Proof:** $$(x_1, y_1), (x_2, y_2) \in C_1 \times C_2$$:
$$\theta(x_1, y_1) + (1-\theta)(x_2, y_2) = (\theta x_1 + (1-\theta) x_2, \theta y_1 + (1-\theta) y_2) \in C_1 \times C_2$$
</div>

**Step 5: Affine transformation - CONVEX**

<div class="textbook-proof" markdown="1">
**Proof:** For $$z_1, z_2 \in f(C_1)$$:
- $$z_i = Ax_i + b$$ with $$x_i \in C_1$$
- $$\theta z_1 + (1-\theta) z_2 = A(\theta x_1 + (1-\theta) x_2) + b \in f(C_1)$$
</div>

</details>

---

## **Exercise 3: Separating hyperplanes**

**Problem:** (Exercise 2.3 from Boyd & Vandenberghe)
Let $$C, D \subset \mathbb{R}^n$$ be disjoint convex sets ($$C \cap D = \emptyset$$).

a) Prove that a separating hyperplane exists
b) Find a separating hyperplane for:
   - $$C = \{x : \lVert x \rVert_2 \leq 1\}$$, $$D = \{x : \lVert x - (3,0) \rVert_2 \leq 1\}$$
   - $$C = \{x : x_1 + x_2 \leq 1, x_1, x_2 \geq 0\}$$, $$D = \{(2,2)\}$$

**Task:**
1. A constructive proof of the separating hyperplane theorem
2. Explicit computations for the examples
3. Visualize separation
4. Analyze the case where the sets touch at the boundary

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Separating hyperplane theorem**

<div class="textbook-theorem" markdown="1">
**Theorem:** If $$C, D$$ are disjoint convex sets, there exist $$a \neq 0$$ and $$b$$ such that:
$$a^T x \leq b \leq a^T y, \quad \forall x \in C, y \in D$$
</div>

**Constructive proof:**
1. Consider $$S = C - D = \{x - y : x \in C, y \in D\}$$ (convex)
2. $$0 \notin S$$ (since $$C \cap D = \emptyset$$)
3. Find the point $$s^* \in S$$ closest to the origin: $$s^* = \arg\min_{s \in S} \lVert s \rVert_2$$
4. Write $$s^* = x^* - y^*$$ ($$x^* \in C$$, $$y^* \in D$$; assume $$C, D$$ are closed and one of them is bounded so that $$s^*$$ exists). Set $$a = y^* - x^* = -s^*$$, $$b = \frac{1}{2}(\lVert y^* \rVert_2^2 - \lVert x^* \rVert_2^2)$$ (the perpendicular bisector of the segment $$x^* y^*$$). The optimality condition for $$s^*$$ gives $$s^{*T}(s - s^*) \geq 0$$ for all $$s \in S$$, from which $$a^T x \leq b \leq a^T y$$.

**Step 2: Example 1 - Two balls**
$$C = \{x : \lVert x \rVert_2 \leq 1\}$$, $$D = \{x : \lVert x - (3,0) \rVert_2 \leq 1\}$$

**Geometric approach:** Centers at $$(0,0)$$ and $$(3,0)$$, radii = 1.
The separating line is perpendicular to the line connecting the centers.

**Solution:** $$a = (1,0)$$, $$b = 1.5$$
Hyperplane: $$x_1 = 1.5$$

**Verification:**
- $$\max_{x \in C} x_1 = 1 < 1.5$$
- $$\min_{x \in D} x_1 = 2 > 1.5$$

**Step 3: Example 2 - Simplex and a point**
$$C = \{x : x_1 + x_2 \leq 1, x_1, x_2 \geq 0\}$$, $$D = \{(2,2)\}$$

**Approach:** Find the point in $$C$$ closest to $$(2,2)$$.

**Optimization problem:**
$$\min_{x \in C} \lVert x - (2,2) \rVert_2^2$$

**KKT conditions:** The closest point is $$(1/2, 1/2)$$ (the projection of $$(2,2)$$ onto the edge $$x_1 + x_2 = 1$$), at distance $$\frac{3}{\sqrt{2}}$$.

**Solution:** $$a = (1,1)$$ (in the direction of $$(2,2) - (1/2,1/2)$$), $$b = 1.5$$. Any $$b \in (1, 4)$$ separates; the perpendicular bisector is $$x_1 + x_2 = 2.5$$.
Hyperplane: $$x_1 + x_2 = 1.5$$

</details>

---

## **Exercise 4: Convex hull computations**

**Problem:** (Exercise 2.4 from Boyd & Vandenberghe)
Compute the convex hulls of the following sets:

a) $$S_1 = \{(0,0), (1,0), (0,1), (1,1)\}$$ in $$\mathbb{R}^2$$

b) $$S_2 = \{x \in \mathbb{R}^3 : \lVert x \rVert_2 = 1, x_3 = 0\} \cup \{(0,0,1), (0,0,-1)\}$$

c) $$S_3 = \{(t, t^2) : t \in [-1,1]\}$$ in $$\mathbb{R}^2$$

**Task:**
1. Compute the convex hull explicitly
2. Identify extreme points
3. Describe it by inequalities when possible
4. Visualize results

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Finite point set**
$$S_1 = \{(0,0), (1,0), (0,1), (1,1)\}$$

**Convex hull:** Unit square $$[0,1] \times [0,1]$$

**Extreme points:** All 4 points are extreme points.

**Inequality description:**
$$\text{conv}(S_1) = \{x : 0 \leq x_1 \leq 1, 0 \leq x_2 \leq 1\}$$

**Step 2: Circle plus two points**
$$S_2 = \{x \in \mathbb{R}^3 : x_1^2 + x_2^2 = 1, x_3 = 0\} \cup \{(0,0,1), (0,0,-1)\}$$

**Convex hull:** Double cone
$$\text{conv}(S_2) = \{x \in \mathbb{R}^3 : x_1^2 + x_2^2 \leq (1 - |x_3|)^2, |x_3| \leq 1\}$$

**Extreme points:** Circle $$\{x : x_1^2 + x_2^2 = 1, x_3 = 0\}$$ and the two apexes $$(0,0,\pm 1)$$

**Step 3: Parabola segment**
$$S_3 = \{(t, t^2) : t \in [-1,1]\}$$

**Convex hull:** Region above the parabola and below the chord $$x_2 = 1$$
$$\text{conv}(S_3) = \{(x_1, x_2) : x_1^2 \leq x_2 \leq 1\}$$

**Extreme points:** 
- Every point $$(t, t^2)$$, $$t \in [-1,1]$$, of the parabolic arc (including the two endpoints $$(\pm 1, 1)$$)
- Interior points of the segment $$x_2 = 1$$ are not extreme points

**Alternative description:**
$$\text{conv}(S_3) = \{(x_1, x_2) : x_2 \geq x_1^2,\ x_2 \leq 1\}$$ (the condition $$|x_1| \leq 1$$ follows automatically)

</details>

---

## **Exercise 5: Dual cones**

**Problem:** (Exercise 2.5 from Boyd & Vandenberghe)
Find the dual cones of the following cones:

a) $$K_1 = \mathbb{R}_+^n = \{x \in \mathbb{R}^n : x_i \geq 0, \forall i\}$$

b) $$K_2 = \{x \in \mathbb{R}^n : \lVert (x_1, \ldots, x_{n-1}) \rVert_2 \leq x_n\}$$ (second-order cone)

c) $$K_3 = \{x \in \mathbb{R}^n : \sum_{i=1}^{n-1} |x_i| \leq x_n\}$$ ($$\ell_1$$ cone)

d) $$K_4 = \{X \in \mathbb{S}^n : X \succeq 0\}$$ (positive semidefinite cone)

**Task:**
1. Compute the dual cone $$K^* = \{y : y^T x \geq 0, \forall x \in K\}$$
2. Verify self-duality where applicable
3. Establish duality relationships
4. Geometric interpretation

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Non-negative orthant**
$$K_1^* = \{y : y^T x \geq 0, \forall x \in \mathbb{R}_+^n\}$$

**Analysis:** $$y^T x = \sum_{i=1}^n y_i x_i \geq 0$$ for all $$x_i \geq 0$$

$$\Rightarrow y_i \geq 0, \forall i$$

**Result:** $$K_1^* = \mathbb{R}_+^n = K_1$$ (self-dual)

**Step 2: Second-order cone**
$$K_2 = \{x : \lVert (x_1, \ldots, x_{n-1}) \rVert_2 \leq x_n\}$$

**Dual:** $$K_2^* = \{y : y^T x \geq 0, \forall x \in K_2\}$$

**Result:** $$K_2^* = K_2$$ (self-dual)

**Proof sketch:** Use the Cauchy-Schwarz inequality and homogeneity.

**Step 3: $$\ell_1$$ cone**
$$K_3 = \{x : \sum_{i=1}^{n-1} |x_i| \leq x_n\}$$

**Dual:** $$K_3^* = \{y : \lVert (y_1, \ldots, y_{n-1}) \rVert_\infty \leq y_n\}$$

**Verification:** Use the duality between the $$\ell_1$$ and $$\ell_\infty$$ norms.

**Step 4: PSD cone**
$$K_4 = \{X \in \mathbb{S}^n : X \succeq 0\}$$

**Dual:** $$K_4^* = \{Y \in \mathbb{S}^n : \text{tr}(YX) \geq 0, \forall X \succeq 0\}$$

**Result:** $$K_4^* = K_4$$ (self-dual)

<div class="textbook-proof" markdown="1">
**Proof:** $$Y \succeq 0 \Leftrightarrow \text{tr}(YX) \geq 0, \forall X \succeq 0$$
</div>

</details>

---

## **Exercise 6: Projection onto convex sets**

**Problem:** (Exercise 2.6 from Boyd & Vandenberghe)
Compute the projection of a point $$x_0$$ onto a convex set $$C$$:

$$\text{proj}_C(x_0) = \arg\min_{x \in C} \lVert x - x_0 \rVert_2$$

a) $$C = \{x : a^T x = b\}$$ (hyperplane)

b) $$C = \{x : a^T x \leq b\}$$ (halfspace)  

c) $$C = \{x : \lVert x \rVert_2 \leq r\}$$ ($$\ell_2$$ ball)

d) $$C = \{x : \lVert x \rVert_\infty \leq r\}$$ ($$\ell_\infty$$ ball)

**Task:**
1. Derive closed-form solutions
2. Verify optimality conditions
3. Analyze uniqueness
4. Implement algorithms

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Projection onto a hyperplane**
$$C = \{x : a^T x = b\}$$

**Lagrangian:** $$L(x,\lambda) = \frac{1}{2}\lVert x - x_0 \rVert_2^2 + \lambda(a^T x - b)$$

**Optimality:** $$x - x_0 + \lambda a = 0 \Rightarrow x = x_0 - \lambda a$$

**Constraint:** $$a^T(x_0 - \lambda a) = b \Rightarrow \lambda = \frac{a^T x_0 - b}{\lVert a \rVert_2^2}$$

**Solution:** $$\text{proj}_C(x_0) = x_0 - \frac{a^T x_0 - b}{\lVert a \rVert_2^2} a$$

**Step 2: Projection onto a halfspace**
$$C = \{x : a^T x \leq b\}$$

**Case analysis:**
- If $$a^T x_0 \leq b$$: $$\text{proj}_C(x_0) = x_0$$
- If $$a^T x_0 > b$$: project onto boundary hyperplane

**Solution:** 
$$\text{proj}_C(x_0) = \begin{cases} 
x_0 & \text{if } a^T x_0 \leq b \\
x_0 - \frac{a^T x_0 - b}{\lVert a \rVert_2^2} a & \text{if } a^T x_0 > b
\end{cases}$$

**Step 3: Projection onto the $$\ell_2$$ ball**
$$C = \{x : \lVert x \rVert_2 \leq r\}$$

**Case analysis:**
- If $$\lVert x_0 \rVert_2 \leq r$$: $$\text{proj}_C(x_0) = x_0$$
- If $$\lVert x_0 \rVert_2 > r$$: project radially

**Solution:**
$$\text{proj}_C(x_0) = \begin{cases}
x_0 & \text{if } \lVert x_0 \rVert_2 \leq r \\
r \frac{x_0}{\lVert x_0 \rVert_2} & \text{if } \lVert x_0 \rVert_2 > r
\end{cases}$$

**Step 4: Projection onto the $$\ell_\infty$$ ball**
$$C = \{x : \lVert x \rVert_\infty \leq r\}$$

**Component-wise projection:**
$$[\text{proj}_C(x_0)]_i = \begin{cases}
x_{0i} & \text{if } |x_{0i}| \leq r \\
r \cdot \text{sign}(x_{0i}) & \text{if } |x_{0i}| > r
\end{cases}$$

**Equivalently:** $$\text{proj}_C(x_0) = \text{clip}(x_0, -r, r)$$

</details>

---

## **Exercise 7: Extreme points and vertices**

**Problem:** (Exercise 2.7 from Boyd & Vandenberghe)
Let $$P = \{x : Ax \leq b\}$$ be a polytope in $$\mathbb{R}^n$$.

a) Prove that $$x$$ is an extreme point if and only if $$n$$ linearly independent constraints are active at $$x$$

b) Find all extreme points of:
   - $$P_1 = \{x \in \mathbb{R}^2 : x_1 + x_2 \leq 1, x_1 \geq 0, x_2 \geq 0\}$$
   - $$P_2 = \{x \in \mathbb{R}^3 : x_1 + x_2 + x_3 \leq 1, x_i \geq 0\}$$

c) Verify Krein-Milman theorem: $$P = \text{conv}(\text{extreme points})$$

**Task:**
1. A rigorous proof of the characterization
2. Systematic enumeration of the vertices
3. Geometric visualization
4. Computational algorithms

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Characterization theorem**

<div class="textbook-theorem" markdown="1">
**Theorem:** $$x \in P$$ is an extreme point $$\Leftrightarrow$$ $$n$$ linearly independent constraints are active at $$x$$.
</div>

**Proof ($$\Leftarrow$$):** Suppose $$n$$ constraints are active: $$A_I x = b_I$$ with $$A_I$$ of full rank.

If $$x = \theta y + (1-\theta) z$$ with $$y, z \in P$$, $$\theta \in (0,1)$$:
- $$A_I y \leq b_I$$ and $$A_I z \leq b_I$$
- $$b_I = A_I x = \theta A_I y + (1-\theta) A_I z \leq b_I$$
- $$\Rightarrow A_I y = A_I z = b_I$$
- Since $$A_I$$ has full rank: $$y = z = x$$

<div class="textbook-proof" markdown="1">
**Proof ($$\Rightarrow$$):** Contrapositive - if fewer than $$n$$ independent constraints are active, the point is not extreme.
</div>

**Step 2: Example 1 - 2D simplex**
$$P_1 = \{x : x_1 + x_2 \leq 1, x_1 \geq 0, x_2 \geq 0\}$$

**Active constraint combinations:**
- $$\{x_1 = 0, x_2 = 0\}$$: vertex $$(0,0)$$
- $$\{x_1 = 0, x_1 + x_2 = 1\}$$: vertex $$(0,1)$$  
- $$\{x_2 = 0, x_1 + x_2 = 1\}$$: vertex $$(1,0)$$

**Extreme points:** $$\{(0,0), (0,1), (1,0)\}$$

**Step 3: Example 2 - 3D simplex**
$$P_2 = \{x : x_1 + x_2 + x_3 \leq 1, x_1, x_2, x_3 \geq 0\}$$

**Systematic enumeration:** Choose 3 from 4 constraints.

**Extreme points:**
- $$(0,0,0)$$: $$\{x_1 = 0, x_2 = 0, x_3 = 0\}$$
- $$(1,0,0)$$: $$\{x_2 = 0, x_3 = 0, x_1 + x_2 + x_3 = 1\}$$
- $$(0,1,0)$$: $$\{x_1 = 0, x_3 = 0, x_1 + x_2 + x_3 = 1\}$$
- $$(0,0,1)$$: $$\{x_1 = 0, x_2 = 0, x_1 + x_2 + x_3 = 1\}$$

**Step 4: Krein-Milman verification**
$$P_1 = \text{conv}\{(0,0), (0,1), (1,0)\}$$
$$P_2 = \text{conv}\{(0,0,0), (1,0,0), (0,1,0), (0,0,1)\}$$

</details>

---

## **Exercise 8: Generalized inequalities**

**Problem:** (Exercise 2.8 from Boyd & Vandenberghe)
Let $$K \subseteq \mathbb{R}^n$$ be a proper cone with generalized inequality $$\preceq_K$$.

a) Verify the properties of $$\preceq_K$$:
   - Reflexive: $$x \preceq_K x$$
   - Antisymmetric: $$x \preceq_K y, y \preceq_K x \Rightarrow x = y$$
   - Transitive: $$x \preceq_K y, y \preceq_K z \Rightarrow x \preceq_K z$$

b) For $$K = \mathbb{S}_+^n$$, verify:
   - $$A \preceq B \Rightarrow A + C \preceq B + C$$
   - $$A \preceq B, C \succeq 0 \Rightarrow CAC \preceq CBC$$

**Task:**
1. Rigorous proofs of the properties
2. Counterexamples for improper cones
3. Applications in optimization
4. Dual cone relationships

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Properties of the generalized inequality**

<div class="textbook-definition" markdown="1">
**Definition:** $$x \preceq_K y \Leftrightarrow y - x \in K$$
</div>

**Reflexive:** $$x \preceq_K x \Leftrightarrow x - x = 0 \in K$$
- True because $$K$$ is a cone (contains 0)

**Antisymmetric:** $$x \preceq_K y, y \preceq_K x$$
- $$\Rightarrow y - x \in K$$ and $$x - y \in K$$
- $$\Rightarrow y - x \in K \cap (-K)$$
- Since $$K$$ is pointed: $$K \cap (-K) = \{0\}$$
- $$\Rightarrow y - x = 0 \Rightarrow x = y$$

**Transitive:** $$x \preceq_K y, y \preceq_K z$$
- $$\Rightarrow y - x \in K, z - y \in K$$
- $$\Rightarrow z - x = (z - y) + (y - x) \in K + K = K$$
- $$\Rightarrow x \preceq_K z$$

**Step 2: Matrix inequalities**

**Property 1:** $$A \preceq B \Rightarrow A + C \preceq B + C$$

<div class="textbook-proof" markdown="1">
**Proof:** 
- $$A \preceq B \Rightarrow B - A \succeq 0$$
- $$(B + C) - (A + C) = B - A \succeq 0$$
- $$\Rightarrow A + C \preceq B + C$$
</div>

**Property 2:** $$A \preceq B, C \succeq 0 \Rightarrow CAC \preceq CBC$$

<div class="textbook-proof" markdown="1">
**Proof:**
- $$B - A \succeq 0$$ and $$C \succeq 0$$
- For any $$x$$ (with $$C$$ symmetric): $$x^T(CBC - CAC)x = (Cx)^T(B - A)(Cx) \geq 0$$
- $$\Rightarrow CBC - CAC \succeq 0$$ (no invertibility of $$C$$ needed; in fact $$C$$ only needs to be symmetric)
- $$\Rightarrow CAC \preceq CBC$$
</div>

**Step 3: Counterexample for an improper cone**

**Non-pointed cone:** $$K = \{x \in \mathbb{R}^2 : x_1 = 0\}$$
- $$K \cap (-K) = K \neq \{0\}$$
- Antisymmetric property fails

**Non-solid cone:** $$K = \mathbb{R}_+ \times \{0\} \subset \mathbb{R}^2$$
- Interior empty
- Strict inequality is not well defined

</details>

---

## **Exercise 9: Convex combinations and Carathéodory's theorem**

**Problem:** (Exercise 2.9 from Boyd & Vandenberghe)
a) Prove Carathéodory's theorem: every point in $$\text{conv}(S)$$ can be written as a convex combination of at most $$n+1$$ points of $$S$$.

b) Apply it to:
   - $$S = \{(1,0), (0,1), (-1,0), (0,-1)\}$$ in $$\mathbb{R}^2$$
   - $$S = \{e_i : i = 1,\ldots,n\} \cup \{0\}$$ in $$\mathbb{R}^n$$

c) Construct an algorithm to find a minimal representation

**Task:**
1. A complete proof of Carathéodory's theorem
2. Explicit computations for the examples
3. Algorithmic implementation
4. Geometric interpretation

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Proof of Carathéodory's theorem**

<div class="textbook-theorem" markdown="1">
**Theorem:** If $$x \in \text{conv}(S)$$, then $$x$$ can be written as:
$$x = \sum_{i=1}^{n+1} \lambda_i x_i$$
with $$x_i \in S$$, $$\lambda_i \geq 0$$, $$\sum \lambda_i = 1$$.
</div>

<div class="textbook-proof" markdown="1">
**Proof:** 
1. Suppose $$x = \sum_{i=1}^k \lambda_i x_i$$ with $$k > n+1$$
2. The vectors $$\{x_1 - x_k, \ldots, x_{k-1} - x_k\}$$ are linearly dependent in $$\mathbb{R}^n$$
3. There exist $$\mu_i$$, not all zero, with $$\sum_{i=1}^{k-1} \mu_i (x_i - x_k) = 0$$
4. Setting $$\mu_k = -\sum_{i=1}^{k-1} \mu_i$$, we get $$\sum_{i=1}^k \mu_i x_i = 0$$
5. $$x = \sum_{i=1}^k (\lambda_i - t\mu_i) x_i$$ for any $$t$$
6. Choose $$t = \min\{\lambda_i/\mu_i : \mu_i > 0\}$$: all coefficients stay $$\geq 0$$, they still sum to 1 (since $$\sum \mu_i = 0$$), and at least one coefficient becomes 0, so $$k$$ decreases
</div>

**Step 2: Example 1 - Square vertices**
$$S = \{(1,0), (0,1), (-1,0), (0,-1)\}$$

**Convex hull:** Diamond/square rotated 45°

**Carathéodory bound:** $$n+1 = 3$$ points suffice

**Example point:** $$(0,0) = \frac{1}{4}(1,0) + \frac{1}{4}(0,1) + \frac{1}{4}(-1,0) + \frac{1}{4}(0,-1)$$

**Minimal representation:** $$(0,0) = \frac{1}{2}(1,0) + \frac{1}{2}(-1,0)$$ (2 points)

**Step 3: Example 2 - Standard basis**
$$S = \{e_1, \ldots, e_n, 0\}$$

**Convex hull:** Standard simplex $$\{x : \sum x_i \leq 1, x_i \geq 0\}$$

**Any point:** $$x = \sum_{i=1}^n x_i e_i + (1 - \sum x_i) \cdot 0$$

**Carathéodory:** At most $$n+1$$ points are needed (already achieved)

**Step 4: Minimal representation algorithm**

```
Algorithm: Minimal Convex Combination
Input: Point x, set S
Output: Minimal convex combination

1. Find any representation x = Σ λᵢ xᵢ
2. While |active set| > n+1:
   a. Solve Σ μᵢ xᵢ = 0, Σ μᵢ = 0 with some μᵢ ≠ 0
b. Find t = min{λᵢ/μᵢ : μᵢ > 0}
   c. Update λᵢ ← λᵢ - t μᵢ
   d. Remove zero coefficients
3. Return minimal representation
```

</details>

---

## **Exercise 10: Facial structure of convex sets**

**Problem:** (Exercise 2.10 from Boyd & Vandenberghe)
Let $$C$$ be a convex set and $$H = \{x : a^T x = \alpha\}$$ a supporting hyperplane with $$\sup_{x \in C} a^T x = \alpha$$.

a) Prove that $$F = C \cap H$$ is a face of $$C$$

b) Classify the faces of:
   - Unit cube $$[0,1]^n$$
   - Unit simplex $$\{x : \sum x_i \leq 1, x_i \geq 0\}$$
   - $$\ell_2$$ ball $$\{x : \lVert x \rVert_2 \leq 1\}$$

c) Establish face lattice structure

**Task:**
1. A rigorous proof of the face property
2. Complete enumeration for the examples
3. Dimension analysis
4. Lattice structure visualization

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Step 1: Face characterization**

<div class="textbook-definition" markdown="1">
**Definition:** $$F$$ is a face of $$C$$ if:
- $$F \subseteq C$$
- $$F$$ convex
- If $$x \in F$$ and $$x = \theta y + (1-\theta) z$$ with $$y, z \in C$$, $$\theta \in (0,1)$$, then $$y, z \in F$$
</div>

<div class="textbook-theorem" markdown="1">
**Theorem:** $$F = C \cap H$$ with $$H$$ a supporting hyperplane is a face.
</div>

<div class="textbook-proof" markdown="1">
**Proof:** 
1. $$F \subseteq C$$ (by definition)
2. $$F$$ is convex (intersection of convex sets)
3. If $$x \in F$$, $$x = \theta y + (1-\theta) z$$, $$y, z \in C$$:
   - $$\alpha = a^T x = \theta a^T y + (1-\theta) a^T z$$
   - $$a^T y, a^T z \leq \alpha$$ (since $$y, z \in C$$)
   - $$\Rightarrow a^T y = a^T z = \alpha$$
   - $$\Rightarrow y, z \in F$$
</div>

**Step 2: Faces of the unit cube**
$$C = [0,1]^n$$

**Face enumeration:**
- **Dimension 0:** $$2^n$$ vertices $$\{0,1\}^n$$
- **Dimension 1:** $$n \cdot 2^{n-1}$$ edges
- **Dimension $$k$$:** Faces obtained by fixing $$n-k$$ coordinates to $$\{0,1\}$$
- **Dimension $$n-1$$:** $$2n$$ facets $$\{x_i = 0\}$$, $$\{x_i = 1\}$$
- **Dimension $$n$$:** $$C$$ itself

**Total faces:** $$3^n$$ (each coordinate can be free, 0, or 1)

**Step 3: Faces of the unit simplex**
$$C = \{x : \sum x_i \leq 1, x_i \geq 0\}$$

**Face structure:**
- **Vertices:** $$\{0, e_1, \ldots, e_n\}$$ ($$n+1$$ vertices)
- **Edges:** Connect vertices
- **Facets:** $$\{x_i = 0\}$$ and $$\{\sum x_i = 1\}$$
- **General faces:** Obtained by setting subset of coordinates to 0

**Step 4: Faces of the $$\ell_2$$ ball**
$$C = \{x : \lVert x \rVert_2 \leq 1\}$$

**Face structure:**
- **Dimension 0:** Every boundary point $$\{x\}$$ with $$\lVert x \rVert_2 = 1$$ (infinitely many extreme points); the origin is **not** a face
- **Dimension $$n$$:** $$C$$ itself (plus the empty face)
- **No other faces:** The ball is strictly convex, so every supporting hyperplane touches it at exactly one point; the sphere itself is not convex, hence not a face

**Lattice structure:** $$\emptyset \subset \{x\} \subset C$$ for each $$x$$ on the sphere (no chain of length greater than 3)

</details>

---

## Practical Tips

#### **When verifying convexity:**
- Use the definition directly: $$\theta x + (1-\theta) y \in C$$
- Apply operations that preserve convexity
- Check sublevel sets of convex functions

#### **When computing convex hulls:**
- Identify the extreme points first
- Use Carathéodory's theorem to reduce complexity
- Verify with supporting hyperplanes

#### **When working with dual cones:**
- Remember the definition: $$K^* = \{y : y^T x \geq 0, \forall x \in K\}$$
- Exploit the self-duality of important cones
- Use them in generalized inequalities

---

## **Summary**

### **Important Convex Sets:**

| Set | Definition | Example |
|-----|------------|-------|
| **Affine set** | $$\{x : Ax = b\}$$ | Subspace, hyperplane |
| **Convex hull** | $$\text{conv}(S) = \{\sum \theta_i x_i : \sum \theta_i = 1, \theta_i \geq 0\}$$ | Smallest convex set containing $$S$$ |
| **Cone** | $$\theta x \in C$$ $$\forall x \in C, \theta \geq 0$$ | Nonnegative orthant |
| **Polyhedron** | $$\{x : Ax \leq b, Cx = d\}$$ | Intersection of halfspaces |
| **Ellipsoid** | $$\{x : (x-x_c)^TP^{-1}(x-x_c) \leq 1\}$$ | $$P \succ 0$$ |
| **Norm ball** | $$\{x : \|\|x - x_c\|\| \leq r\}$$ | $$\ell_1, \ell_2, \ell_\infty$$ balls |

### **Operations Preserving Convexity:**

| Operation | Example |
|-----------|-------|
| **Intersection** | $$C_1 \cap C_2$$ is convex if $$C_1, C_2$$ are convex |
| **Affine map** | $$f(C) = \{Ax + b : x \in C\}$$ |
| **Perspective** | $$P(x, t) = x/t$$ |
| **Linear fractional** | $$f(x) = \frac{Ax + b}{c^Tx + d}$$ |

### **Separation & Support:**

- **Separating hyperplane:** There exists $$a$$ such that $$a^Tx \leq b$$ $$\forall x \in C_1$$ and $$a^Tx \geq b$$ $$\forall x \in C_2$$
- **Supporting hyperplane:** $$\{x : a^Tx = a^Tx_0\}$$ at a boundary point $$x_0$$
- **Dual cone:** $$K^* = \{y : y^Tx \geq 0, \forall x \in K\}$$
- **Self-dual cones:** $$K^* = K$$ (e.g., nonnegative orthant, PSD cone)

### **Key Theorems:**

- **Carathéodory:** Every point of $$\text{conv}(S) \subset \mathbb{R}^n$$ is a combination of $$\leq n+1$$ points
- **Radon:** Any $$n+2$$ points in $$\mathbb{R}^n$$ can be partitioned into 2 disjoint sets whose convex hulls intersect
- **Helly:** If $$C_1, \ldots, C_m$$ are convex in $$\mathbb{R}^n$$ ($$m \geq n+1$$) and every $$n+1$$ of them intersect, then $$\bigcap_{i=1}^m C_i \neq \emptyset$$

---

## References

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
   - Chapter 2: Convex Sets
   - Exercises 2.1-2.27

2. **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press.

3. **Ziegler, G. M.** (1995). *Lectures on Polytopes*. Springer-Verlag.

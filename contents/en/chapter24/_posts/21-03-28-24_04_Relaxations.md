---
layout: post
title: 24-04 Relaxations
chapter: '24'
order: '5'
owner: YoungJae Choung
categories:
- chapter24
lang: en
---

A relaxation is an intentional, mathematically disciplined lie: we replace an intractable discrete problem with an easier continuous one whose optimal value is *guaranteed* to sit below (for minimization) the true integer optimum. Not all relaxations are created equal, however. A sloppy relaxation gives a weak lower bound and forces millions of branch-and-bound nodes, whereas a tight **convex relaxation** or **Lagrangian relaxation** can close 90% of the integrality gap at the very root node.

## Background Knowledge Map: Convex and Lagrangian Relaxations

- **Formal Definition of a Relaxation:** A problem $$\min_{x \in \tilde{S}} \tilde{f}(x)$$ is a valid relaxation of $$\min_{x \in S} f(x)$$ if (i) $$S \subseteq \tilde{S}$$ and (ii) $$\tilde{f}(x) \le f(x)$$ for all $$x \in S$$. Together these guarantee $$\tilde{f}^\star \le f^\star$$.
- **Convex (LP/SDP) Relaxations:** Dropping integrality $$x \in \{0, 1\}^n \to x \in [0, 1]^n$$ produces the canonical LP relaxation; replacing rank-1 binary matrices $$xx^\top$$ with positive semidefinite matrices $$X \succeq 0$$ produces tighter SDP relaxations (such as Goemans–Williamson for Max-Cut).
- **Lagrangian Relaxation:** Instead of dropping integrality, dualize a set of "complicating" constraints $$Ax \le b$$ into the objective via multipliers $$\lambda \ge 0$$: $$g(\lambda) = \min_{x \in X} \{c^\top x + \lambda^\top(Ax - b)\}$$, then maximize the concave dual function $$g(\lambda)$$.
- **Why Lagrangian Relaxation Can Beat LP Relaxation:** By Geoffrion’s theorem, if the remaining integer subproblem $$X$$ does *not* have the integrality property (i.e., $$\operatorname{conv}(X)$$ is strictly smaller than its LP relaxation), the Lagrangian dual $$\max_{\lambda \ge 0} g(\lambda)$$ equals the LP optimum over $$\operatorname{conv}(X) \cap \{Ax \le b\}$$—strictly tighter than the ordinary LP relaxation!

### Step-by-Step Worked Example (Read Slowly): Computing a Lagrangian Relaxation Lower Bound

Consider the integer program $$\min_{x_1, x_2 \in \{0, 1\}} -3 x_1 - 4 x_2$$ subject to the complicating constraint $$2 x_1 + 3 x_2 \le 4$$. (By inspection, we cannot pick both $$x_1 = x_2 = 1$$ since $$5 > 4$$, so the true IP optimum is $$(0, 1)$$ with value $$-4$$.)

1. **Form the Lagrangian dualizing $$2 x_1 + 3 x_2 - 4 \le 0$$ with $$\lambda \ge 0$$:**
   $$g(\lambda) = \min_{x_1, x_2 \in \{0, 1\}} \bigl[(-3 + 2\lambda) x_1 + (-4 + 3\lambda) x_2 - 4\lambda\bigr].$$
2. **Evaluate $$g(\lambda)$$ in closed form:** Because $$x_1, x_2 \in \{0, 1\}$$ decouple completely, we set $$x_i = 1$$ iff its coefficient is negative:
   $$g(\lambda) = \min(0,\ 2\lambda - 3) + \min(0,\ 3\lambda - 4) - 4\lambda.$$
3. **Test key multiplier values:**
   - At $$\lambda = 0$$: $$g(0) = (-3) + (-4) - 0 = -7$$ (weak bound).
   - At $$\lambda = 4/3$$: $$g(4/3) = \min(0, -1/3) + 0 - 16/3 = -17/3 \approx -5.667$$.
   - At $$\lambda = 3/2$$: $$g(3/2) = 0 + 0 - 6 = -6$$.
   - Check $$\lambda = 4/3$$ vs. the LP relaxation: in the LP relaxation, $$x_1 = 1, x_2 = 2/3$$ gives $$-3(1) - 4(2/3) = -17/3 \approx -5.667$$!
   Here $$X = \{0, 1\}^2$$ has the integrality property, so the best Lagrangian dual bound $$\max_{\lambda \ge 0} g(\lambda) = -17/3$$ matches the LP relaxation exactly—and always certifies $$f^\star = -4 \ge -5.667$$.

For relaxation, specific conditions must be satisfied, and Convex relaxation and Lagrangian relaxation methods can be utilized. Let's examine the detailed content.

## Conditions for Relaxations

If a general optimization problem is defined as follows:

>$$\min_{x \in X} f(x)$$

The relaxation of this problem is defined as follows when represented as an arbitrary optimization problem:

>$$
>\begin{align}
>&\min_{x \in Y} \: g(x)\\\\
>&\text{such that}\\\\
>&\text{① } X \subset Y \quad \text{ and}\\\\
>&\text{② } g(x) \leq f(x) \text{ for all } x \in X
>\end{align}
>$$

If the objective functions $$f(x)$$ and $$g(x)$$ are different, both conditions must be satisfied, and if they are the same, only condition ① needs to be satisfied. By these two conditions, the optimal value of the relaxation becomes a lower bound of the optimal value of the original problem.

## Convex relaxations

When the given problem is as follows:

>$$
>\begin{align}
>&\min_{x} &&f(x) \\\\
>&\text{subject to } && x \in C \\\\
>&&&x_j \in \mathbb{Z}, \quad j \in J \\\\
>\end{align}
>$$
>
>$$
>\begin{align}
>\text{where } f \text{ is convex, } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n
>\quad \text{and} \quad J \subseteq \{1, \dotsc, n\}
>\end{align}
>$$

The convex relaxation can be expressed as follows:

>$$
>\begin{align}
>&\min_{x} && f(x) \\\\
>&\text{subject to } && x \in C \\\\
>\end{align}
>$$
>
>$$
>\begin{align}
>\text{where } f \text{ is convex, } f: \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n
>\end{align}
>$$

## Lagrangian relaxations

When $$X$$ includes both convex and integer constraints, we can define the problem as follows:

>$$
>\begin{align}
>&\min_{x} &&f(x) \\\\
>&\text{subject to } &&Ax \leq b \\\\
>&&& x_{j} \in \mathbb{Z}, \quad x \in X
>\end{align}
>$$

In this case, by adding constraints to the objective and performing Lagrangian relaxation for some $$u \geq 0$$, we get:

>$$
>\begin{align}
>L(u) = &\min_{x} &&f(x) + u^{\top}(Ax-b) \\\\
>&\text{subject to } &&x \in X
>\end{align}
>$$

Through the Lagrangian form, the constraint set is expanded, and since feasible $$x$$ satisfies $$Ax \leq b$$, we always have $$f(x) + u^{\top}(Ax - b) \leq f(x)$$ for $$u \geq 0$$. Therefore, $$L(u)$$ is a lower bound for any $$u \geq 0$$, and the best lower bound can be obtained by solving the dual problem $$\max_{u \geq 0} L(u)$$. Remember that since $$L(u)$$ is the point-wise minimum of convex functions, it becomes a concave optimization problem.

Applying Lagrangian relaxation to the previously mentioned Facility location problem, it transforms into a problem of solving the following equation for unconstrained $$v$$:

>$$
>\begin{align}
>L(u) = &\min_{x} && \sum_{j = 1}^{n} f_{j}y_{j} + \sum_{i = 1}^{m}\sum_{j = 1}^{n}(c_{ij} - v_{i})x_{ij} + \sum_{i = 1}^{m} v_{i} \\\\
>&\text{subject to } && x_{ij} \leq y_{j} \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n \\\\
>&&& x_{ij}, y_{j} \in \{0, 1\} \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n
>\end{align}
>$$

For each $$v$$, the Lagrange relaxation $$L(v)$$ can be easily solved:

>$$
>x_{ij}(v) =\begin{cases}
>1 & \text{if } c_{ij} - v_{i} < 0 \text{ and } \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
>0 & \text{otherwise}
>\end{cases}
>$$
>
>$$
>y_{j}(v) =\begin{cases}
>1 & \text{if } \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
>0 & \text{otherwise}
>\end{cases}
>$$

From this lower bound $$L(v)$$, we can also derive heuristic primal solutions. Also, using the subdifferential of $$-L(v)$$ makes computation easier. Using the subgradient method, we can solve the problem by transforming $$\max_{v} L(v)$$ to $$\min_{v} -L(v)$$.
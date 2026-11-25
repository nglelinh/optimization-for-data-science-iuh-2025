---
layout: post
title: 11 Duality in General Programs
chapter: '11'
order: 1
owner: Wontak Ryu
categories:
- chapter11
lang: en
lesson_type: required
---

In Chapter 10, linear programming duality gave us a remarkable mirror world: every LP has a dual LP whose feasible solutions certify lower bounds, and strong duality closes the gap completely. What happens when the objective and constraints are no longer linear—when they are quadratic, logarithmic, semidefinite, or even **nonconvex**? Chapter 11 lifts duality to *completely general* optimization problems using the **Lagrangian** $$L(x, u, v)$$, revealing a deep surprise: even when the original primal problem is wildly nonconvex, its Lagrange dual problem is **always concave (convex to maximize)**!

## Background Knowledge Map: Lifting Duality Beyond Linear Programs

- **Pillar 1 — The Universal Lagrangian $$L(x, u, v)$$:** Attaching nonnegative prices $$u_i \ge 0$$ to inequalities $$h_i(x) \le 0$$ and free prices $$v_j \in \mathbb{R}$$ to equalities $$l_j(x) = 0$$ transforms *any* constrained problem—convex or nonconvex—into a parameterized unconstrained objective.
- **Pillar 2 — Concavity of the Dual Function $$g(u, v)$$:** Because $$g(u, v) = \inf_x L(x, u, v)$$ is the pointwise infimum of a family of affine functions of $$(u, v)$$, $$g$$ is *always concave*, regardless of how complicated or nonconvex $$f, h_i, l_j$$ are.
- **Pillar 3 — Weak Duality Always, Strong Duality Under Slater's Condition:** Weak duality ($$g^\star \le f^\star$$) holds universally with zero convexity assumptions. Strong duality ($$g^\star = f^\star$$) requires convexity plus a regularity condition—most famously **Slater's condition** (existence of a strictly feasible interior point).
- **Pillar 4 — Duality Gap as a Real-Time Stopping Criterion:** For any primal-feasible $$x$$ and dual-feasible $$(u, v)$$, $$f(x) - f^\star \le f(x) - g(u, v)$$, giving interior-point and primal–dual solvers an exact, provable certificate of suboptimality without ever knowing $$f^\star$$.

### Step-by-Step Worked Example (Read Slowly): From General LP Duality to Nonlinear Quadratic Duality

Contrast how the Lagrangian works on an LP vs. a nonlinear quadratic problem: minimize $$f(x) = x^2$$ subject to $$x \ge 2$$ (i.e., $$h(x) = 2 - x \le 0$$).

1. **Form the Lagrangian with multiplier $$u \ge 0$$:**
   $$L(x, u) = x^2 + u(2 - x) = x^2 - ux + 2u.$$
2. **Minimize $$L(x, u)$$ over unconstrained $$x \in \mathbb{R}$$:**
   Unlike an LP (where $$\inf_x L$$ was $$-\infty$$ unless a linear constraint held), here $$L(x, u)$$ is a strictly convex parabola in $$x$$! Setting $$\frac{\partial L}{\partial x} = 2x - u = 0$$ gives $$x(u) = \frac{u}{2}$$.
3. **Substitute $$x(u) = u/2$$ to obtain the smooth concave dual function:**
   $$g(u) = \left(\frac{u}{2}\right)^2 - u\left(\frac{u}{2}\right) + 2u = -\frac{u^2}{4} + 2u.$$
4. **Maximize $$g(u)$$ over $$u \ge 0$$:** Setting $$g'(u) = -\frac{u}{2} + 2 = 0$$ gives $$u^\star = 4 \ge 0$$, yielding $$g^\star = -\frac{16}{4} + 8 = 4 = 2^2 = f^\star$$! Strong duality holds because the problem is convex and $$x = 3$$ strictly satisfies $$2 - 3 = -1 < 0$$ (Slater's condition).

### Review: duality in linear program

Given $$c \in \mathbb{R}^n$$, $$A \in \mathbb{R}^{m \times n}$$, $$b \in \mathbb{R}^m$$, $$G \in \mathbb{R}^{r \times n}$$, $$h \in \mathbb{R}^r$$, 

#### Primal LP: 
>
$$
\begin{alignat}{1}
\min_{x} & \quad c^T x   \\\\ 
  s.t.   & \quad Ax = b  \\\\
         & \quad Gx \leq h 
\end{alignat}
$$


#### Dual LP: 
>
$$
\begin{alignat}{1}
\max_{u,b} & \quad -b^T u - h^T v   \\\\
         s.t. & \quad - A^T u - G^T v = c  \\\\
             & \quad v \geq 0 
\end{alignat}
$$

### Explanation 1: 

For all $$u$$ and $$v \geq 0$$, and for any primal feasible $$x$$, the following holds. 
>
$$
\begin{equation}
u^T (Ax-b) + v^T(Gx-h) \leq 0
\end{equation}
$$

That is,

>
$$
\begin{equation}
(-A^Tu - G^Tv)^T x \geq -b^Tu - h^T v
\end{equation}
$$

By this relationship, if $$c=-A^Tu - G^Tv$$, we obtain a lower bound on the primal optimum. 


### Explanation 2: 

For all $$u$$ and $$v \geq 0$$, and for any primal feasible $$x$$,

>
$$
\begin{equation}
c^T x \geq c^T x + u^T (Ax-b) + v^T (Gx -h) := L(x,u,v)
\end{equation}
$$

Thus, if $$C$$ is the primal feasible set and $$f^*$$ is the primal optimum, then 

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

In other words, $$g(u,v)$$ is a lower bound on $$f^*$$. 

>
$$
g(u,v) =
\begin{cases}
-b^T u - h^T v & \text{if $c=-A^Tu - G^T v$} \\\\
-\infty            & \text{otherwise} 
\end{cases}
$$

The second explanation yields the same dual as the first, but it is completely general and applies to arbitrary optimization problems (including nonconvex ones).

## Modern applications (2022–2026)

An optional companion lesson uses the same Lagrangian dual as a training signal or certificate in DRO, AC-OPF networks (DC3 / OPF-DNN), Fairlearn reductions, and kernel SVMs. See [11-08 Modern applications of Lagrangian duality]({% multilang_post_url contents/chapter11/2026-09-16-11_08_modern_applications %}).

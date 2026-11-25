---
layout: post
title: 01-02 Convex optimization problem
chapter: '01'
order: 3
owner: Kyeongmin Woo
categories:
- chapter01
lang: en
lesson_type: required
---

Most nonlinear optimization problems are treacherous: a solver can stop at a point that looks flat and locally optimal, yet a far better solution hides over the next ridge. Convex optimization eliminates that anxiety completely. When the objective and inequality constraints are convex and all equality constraints are affine, the geometry of the problem guarantees that *local optimality implies global optimality*.

## Key ideas: What Makes an Optimization Problem Convex

- **Convex Feasible Set:** Requires that for any two feasible solutions $$x, y$$, the entire line segment $$\theta x + (1 - \theta)y$$ ($$0 \le \theta \le 1$$) remains feasible—no holes, disconnected islands, or inward dents.
- **Convex Objective & Inequality Constraints:** Both $$f_0(x)$$ and every $$f_i(x) \le 0$$ must satisfy Jensen's inequality $$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$$.
- **Affine Equality Constraints Only:** Equality constraints must be linear/affine ($$a_j^T x = b_j$$), because a nonlinear equality like $$x_1^2 + x_2^2 = 1$$ (a hollow circle) is nonconvex even though $$x_1^2 + x_2^2$$ is convex!
- **Global Optimality Theorem:** If $$x^*$$ is locally optimal for a convex problem, any strictly better point $$y$$ would pull the line segment toward $$x^*$$ strictly downhill inside the neighborhood of $$x^*$$—a contradiction.

### Worked example: Verifying Convexity and Solving Analytically

Consider:
$$\min_{x_1, x_2} \; f_0(x_1, x_2) = x_1^2 + 2x_2^2 \quad \text{s.t.} \quad x_1^2 + x_2^2 \le 10, \quad x_1 + x_2 = 3.$$

1. **Check the three convexity requirements:**
   - Objective $$f_0$$: Hessian $$\nabla^2 f_0 = \text{diag}(2, 4) \succ 0 \implies$$ strictly convex.
   - Inequality $$f_1(x) = x_1^2 + x_2^2 - 10 \le 0$$: Hessian $$\text{diag}(2, 2) \succ 0 \implies$$ convex.
   - Equality $$h_1(x) = x_1 + x_2 - 3 = 0$$: affine!
   Hence this is a **strictly convex optimization problem** with a unique global minimizer.
2. **Eliminate the affine equality constraint:** Substitute $$x_2 = 3 - x_1$$ into $$f_0$$:
   $$\phi(x_1) = x_1^2 + 2(3 - x_1)^2 = 3x_1^2 - 12x_1 + 18.$$
3. **Minimize $$\phi(x_1)$$ and check the inequality:**
   $$\phi'(x_1) = 6x_1 - 12 = 0 \implies x_1^* = 2, \quad x_2^* = 3 - 2 = 1.$$
   Verify the inequality: $$(2)^2 + (1)^2 = 5 \le 10$$ (strictly satisfied!). Thus $$x^* = (2, 1)^T$$ is the unique global optimum with $$p^* = 2^2 + 2(1)^2 = 6$$.

A convex optimization problem is a type of optimization problem.

>$$\begin{align*} 
>&\min_{x\in D}\ &&f(x) \\
>&\text{subject to} && g_i(x) \le 0,\ i = 1, ..., m \\
>&&& h_j(x) = 0,\ j = 1,\ ..., r
>\end{align*}$$

**Convex Optimization Problem in standard form [3]**

Here, the objective function $$f$$ and the inequality constraint functions $$g_i$$ are convex, and the equality constraint functions $$h_j$$ are affine. An affine function is a linear function plus a constant:
>$$h_j,\ j = 1, ..., r$$ are affine: $$h_j(x) = a_{j}^T x + b_{j},\ j=1, ..., r$$

What does it mean for a function to be convex? To understand this, we first need to understand convex sets.

## Convex sets
A line segment connecting two points $$x_1$$ and $$x_2$$ is defined as:

>$$x = \theta x_1 + (1 - \theta) x_2$$ with $$0 \le \theta \le 1$$

Given a set, if the line segment between any two points $$x_1$$ and $$x_2$$ in the set is also contained in the set, we call it a convex set. In other words, a set $$C$$ is convex if:

>$$x_1, x_2 \in C$$, $$0 \le \theta \le 1$$  $$\Rightarrow$$ $$\theta x_1 + (1-\theta)x_2 \in C$$

For example, in the figure below, only the leftmost shape is a convex set.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/Convex_set.png" alt="Convex Set" width="70%">
  <figcaption style="text-align: center;">[Fig1] left: a convex set, mid & right: non-convex sets [2]</figcaption>
</p>
</figure>

## Convex functions
A convex function is defined as follows:

>$$f: \mathbb{R}^n \rightarrow \mathbb{R} $$ is convex if $$ dom(f) $$ is a convex set and,
>
>$$f(\theta x + (1 - \theta)y) \le \theta f(x) + (1-\theta)f(y) $$ for all $$ x, y \in dom(f),\ 0 \le \theta \le 1$$

Geometrically, this means that for any two points $$(x, f(x))$$ and $$(y, f(y))$$ on the graph of $$f$$, the line segment connecting them lies above the graph between $$x$$ and $$y$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/Convex_function.png" alt="Convex Function" width="70%">
  <figcaption style="text-align: center;">[Fig2] Convex Function [2]</figcaption>
</p>
</figure>

## Relation between a convex set and a convex function
There is a close relationship between convex functions and convex sets:
> A function $$f$$ is convex if and only if its epigraph is a convex set.

What is an epigraph? 'Epi' means 'above', so the epigraph of $$f$$ is the set of points above the graph of $$f$$. Formally, the epigraph is defined as:

>$$
\eqalign{
& \text{epigraph of } f: \mathbb{R}^n \rightarrow \mathbb{R}\\
& \text{epi } f = \{(x, t) \in \mathbb{R}^{n+1} \mid x \in \text{ dom } f, f(x) \le t\}
}
$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/epigraph.png" alt="Epigraph" width="70%">
  <figcaption style="text-align: center;">[Fig3] Epigraph [2]</figcaption>
</p>
</figure>

If $$f$$ is a convex function, then $$\text{epi } f$$ is always a convex set, and vice versa. This is a key property connecting the definitions of convex functions and convex sets.

## Convex and concave functions

A function $$f$$ is concave if $$-f$$ is convex. Equivalently, $$f$$ is concave if:

>$$f(\theta x + (1 - \theta)y) \ge \theta f(x) + (1-\theta)f(y) $$ for all $$ x, y \in dom(f),\ 0 \le \theta \le 1$$

Geometrically, this means that the line segment connecting any two points on the graph lies below the graph of the function. A concave function "curves downward" while a convex function "curves upward".

What about concave functions? Why do we emphasize convex functions so much, and seemingly "ignore" concave ones?
- We "don't care" about concave functions separately because they're just the mirror image of convex ones. Always reformulate maximization of concave $$f$$ as minimization of convex $$-f$$.


## Nice property of convex optimization problems
A local minimum of a convex function is always a global minimum. For convex optimization problems, solutions are generally easier to find than for non-convex problems, because convex functions have the following property:
> If $$f$$ is convex and $$x$$ is a locally optimal point (i.e., a local minimum), then $$x$$ is also a globally optimal point.

Let's prove this by contradiction:

>**Proof by contradiction:**
>
>Suppose for a convex function $$f$$, $$x$$ is a locally optimal point but not a globally optimal point. Let $$y$$ be a feasible global optimal point, so for any positive $$\rho$$, $$\|y - x\|_2 > \rho$$ and $$f(y) < f(x)$$. (Because $$x$$ is locally optimal, if $$\|x - y\|_2 \le \rho$$ then $$f(x) \le f(y)$$, which contradicts $$y$$ being globally optimal.)
>Now, for $$\theta=\frac{\rho}{2\|y-x\|_2}$$, let $$z = \theta y + (1 - \theta) x = x + \theta( y - x)$$. Then:
>
>1. $$z$$ is a convex combination of two feasible points $$x, y$$, so it is also feasible.
>
>2. $$\|z - x\|_2 = \theta \|y - x\|_2 = \frac{\rho}{2} < \rho$$.
>
>3. $$f(z) \le \theta f(y) + (1 - \theta) f(x) < \theta f(x) + (1 - \theta) f(x) = f(x)$$
>
>Points 2 and 3 contradict the assumption that $$x$$ is a locally optimal point, so by contradiction, any locally optimal point $$x$$ is also globally optimal.

## Convex combination

A convex combination of $$x_1, ..., x_k$$ is defined as:

> $$x = \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k$$ with $$\theta_1 + \cdots + \theta_k = 1, \theta_i \ge 0$$

If $$D$$ is a convex set and $$x_1, x_2, ..., x_k \in D$$, then $$x \in D$$ as well.


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


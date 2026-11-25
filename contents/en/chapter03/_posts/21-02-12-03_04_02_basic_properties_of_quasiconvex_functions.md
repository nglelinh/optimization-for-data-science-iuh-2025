---
layout: post
title: 03-04-02 Basic properties of quasiconvex functions
chapter: '03'
order: 10
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

With ordinary convex functions, blending two points always stays below the *average* of their heights; with quasiconvex functions, blending two points only stays below the *higher* of their two heights. That subtle relaxation—Modified Jensen's inequality—explains why quasiconvex functions can have S-shaped inflections and flat shelves while still forbidding multiple separated valleys.

## Key ideas: Structural Properties of Quasiconvex Functions

- **Modified Jensen's Inequality:** $$f$$ is quasiconvex iff $$f(\theta x + (1-\theta)y) \le \max\{f(x), f(y)\}$$ for all $$x, y \in \text{dom}\,f$$ and $$\theta \in [0, 1]$$.
- **1D Characterization:** A function on $$\mathbb{R}$$ is quasiconvex iff it is nondecreasing, nonincreasing, or nonincreasing up to some threshold $$c$$ and nondecreasing after $$c$$.
- **Quasiconvexity vs. Local Minima:** Warning! Unlike convex functions, a *local* minimum of a quasiconvex function on a flat plateau is NOT guaranteed to be a global minimum unless the function is *strictly* quasiconvex.
- **Sum Failure:** Unlike convex functions, the sum of two quasiconvex functions is generally **not** quasiconvex—you must use maxima or monotone compositions instead.

### Worked example: Modified Jensen Succeeds Where Ordinary Jensen Fails

Test $$f(x) = x^3$$ (monotone increasing on $$\mathbb{R}$$, hence quasiconvex) at $$x = -2$$, $$y = 1$$, and $$\theta = 0.5$$.

1. **Evaluate endpoints and midpoint:**
   $$f(-2) = -8, \qquad f(1) = 1, \qquad m = 0.5(-2) + 0.5(1) = -0.5 \implies f(-0.5) = -0.125.$$
2. **Test Modified Jensen's inequality:**
   $$f(-0.5) = -0.125 \le \max\{f(-2), f(1)\} = \max\{-8, 1\} = 1 \quad \checkmark$$
3. **Contrast with ordinary Jensen's inequality:**
   $$0.5 f(-2) + 0.5 f(1) = 0.5(-8) + 0.5(1) = -3.5.$$
   Since $$f(-0.5) = -0.125 > -3.5$$, ordinary Jensen fails ($$x^3$$ is concave on $$x < 0$$), cleanly illustrating why quasiconvexity is strictly broader than convexity.

This section covers the basic properties of quasiconvex functions, including their relationship to convex functions and their behavior under various operations.

## Modified Jensen's inequality
Quasiconvex functions can be defined through Jensen's inequality as follows:
>$$f(\theta x + (1 - \theta)y) \leq \max\{f(x), f(y)\}$$ for all $$x, y \in \text{dom}f, 0 \leq \theta \leq 1$$

The figure below shows that if function $$f$$ is quasiconvex, then the value of $$f$$ along the line segment between two points does not exceed the maximum of $$f$$ at the endpoints.
<br><br>

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.10_quasiconvex_function_on_R_4uChnEm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1]</figcaption>
</p>
</figure>
**quasiconvex function on $$\mathbb{R}$$. The values of $$f$$ between $$x$$ and $$y$$ are less than $$\max\{f(x), f(y)\}$$.**

<br>

## Quasiconvex function on $$\mathbb{R}$$
A continuous function $$f : \mathbb{R} \mapsto \mathbb{R}$$ is quasiconvex if and only if it satisfies at least one of the following conditions:

• $$f$$ is nondecreasing
• $$f$$ is nonincreasing  
• There exists a point $$c \in \text{dom} f$$ such that $$f$$ is nonincreasing on $$\{t \in \text{dom}f \mid t \leq c\}$$ and nondecreasing on $$\{t \in \text{dom}f \mid t \geq c\}$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.11_quasiconvex_function_on_R_2_PPQpNiU.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2]</figcaption>
</p>
</figure>
**quasiconvex function on $$\mathbb{R}$$. It is nonincreasing for $$t \leq c$$ where $$t \in \text{dom} f$$, and nondecreasing for $$t \geq c$$ where $$t \in \text{dom} f$$.**

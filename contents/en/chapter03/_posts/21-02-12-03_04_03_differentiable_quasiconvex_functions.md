---
layout: post
title: 03-04-03 Differentiable quasiconvex functions
chapter: '03'
order: 11
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

This section discusses the properties and characterizations of differentiable quasiconvex functions.

## First-order conditions
Let $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ be a differentiable function. If $$\text{dom}f$$ is convex and the following condition is satisfied, then $$f$$ is quasiconvex.
>$$f$$ is quasiconvex $$\iff$$ $$f(y) \leq f(x) \Rightarrow \nabla f(x)^T(y-x) \leq 0$$ for all $$x, y \in \text{dom}f$$

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/3.12_Three_level_curves_OV6vtPq.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1]</figcaption>
</p>
</figure>
**Three level curves of a quasiconvex function $$f$$. $$\nabla f(x)$$ is the normal vector that defines the supporting hyperplane of the sublevel set $$\{z \mid f(z) \leq f(x)\}$$ at $$x$$.**


The first-order condition for quasiconvexity appears similar to the first-order characterization of convexity (see [03-01-03]({% multilang_post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %})), but there are important differences. For example, if $$f$$ is convex and $$\nabla f(x) = 0$$, then $$x$$ is a global minimizer of $$f$$, but this does not always hold for quasiconvex functions.

<br>
## Second-order conditions

When $$f$$ is twice differentiable, second-order conditions apply. If $$f$$ is quasiconvex, then for all $$x \in \text{dom}f$$ and all $$y \in \mathbb{R}^n$$, the following holds:
>$$f$$ is quasiconvex, $$y^T \nabla f(x) = 0 \Longrightarrow y^T \nabla^2 f(x)y \geq 0$$ for all $$x \in \text{dom} f$$, all $$y \in \mathbb{R}^n$$ <br>

For quasiconvex functions on $$\mathbb{R}$$:

>$$f$$ is quasiconvex, $$f'(x) = 0 \Rightarrow f''(x) \geq 0$$

That is, if there exists any point with zero slope, the second derivative value is non-negative. Returning to $$\mathbb{R}^n$$, the second-order condition also satisfies the following properties:

1) When $$\nabla f(x) = 0$$, we must always have $$\nabla^2f(x) \succeq 0$$.
2) If $$\nabla f(x) \neq 0$$, then $$y^T \nabla f(x) = 0 \Rightarrow y^T \nabla^2 f(x)y \geq 0$$, where $$\nabla^2 f(x)$$ acts as the Hessian matrix and is positive semidefinite on the $$(n-1)$$-dimensional subspace $$\nabla f(x)^\perp$$.

(The $$(n-1)$$-dimensional subspace $$\nabla f(x)^\perp$$ means the $$(n-1)$$-dimensional subspace orthogonal to $$\nabla f(x)$$. It is $$(n-1)$$-dimensional because $$\nabla f(x)$$ is the gradient of an $$n$$-dimensional function $$f$$, reducing the dimension by one.)

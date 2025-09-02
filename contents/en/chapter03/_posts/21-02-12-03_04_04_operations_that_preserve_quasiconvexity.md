---
layout: post
title: 03-04-04 Operations that preserve quasiconvexity
chapter: '03'
order: 12
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

This section discusses operations that preserve the quasiconvexity of functions.

## Nonnegative weighted maximum

When $$f$$ is a quasiconvex function, the nonnegative weighted maximum $$f$$ is quasiconvex.
>$$f = \max\{w_1f_1, ... ,w_mf_m\}$$ with $$w_i \geq 0$$ is quasiconvex

This concept can be extended as follows:
>$$f(x) = \sup_{y \in C}(w(y)g(x,y))$$ with $$w(y) \geq 0$$, 
>where $$g(x,y)$$ is quasiconvex in $$x$$ for each $$y$$.

<br>

## Composition

If $$g : \mathbb{R}^n \mapsto \mathbb{R}$$ is quasiconvex and $$h : \mathbb{R} \mapsto \mathbb{R}$$ is nondecreasing, then the composition $$f$$ satisfies quasiconvexity.
> $$f = h \circ g$$ is quasiconvex if $$h$$ is nondecreasing and $$g$$ is quasiconvex.
 
Composing a quasiconvex function with affine or linear-fractional transformations results in a quasiconvex function.
If $$f$$ is quasiconvex, then $$g(x) = f(Ax + b)$$ is also quasiconvex, and $$\tilde{g}(x) = f((Ax + b)/(c^Tx + d))$$ is also quasiconvex on the set $$\{x \mid c^Tx + d > 0, (Ax + b)/(c^Tx + d) \in \text{dom}f\}$$.

<br>

## Minimization

If $$f(x, y)$$ satisfies quasiconvexity and $$C$$ is a convex set, then the following condition holds:
> $$g(x) = \inf_{y \in C} f(x,y)$$ is quasiconvex if $$f$$ is quasiconvex in $$(x,y)$$ and $$C$$ is a convex set.

<br>

## Representation via family of convex functions

The sublevel sets of a quasiconvex function $$f$$ can be represented by inequalities of convex functions. A family of convex functions is $$\phi_t : \mathbb{R}^n \mapsto \mathbb{R}$$ for $$t \in \mathbb{R}$$, defined as follows:
>$$f(x) \leq t \Longleftrightarrow \phi_t(x) \leq 0$$

That is, the $$t$$-sublevel set of quasiconvex function $$f(x)$$ becomes the 0-sublevel set of convex function $$\phi_t$$. Here, $$t$$ represents the index of convex function $$\phi$$. For all $$x \in \mathbb{R}^n$$, the following is satisfied:
>$$\phi_t(x) \leq 0 \Rightarrow \phi_s(x) \leq 0 \text{ for } s \geq t$$


---
layout: post
title: 07-02 Sub-differentials
chapter: '07'
order: 3
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---


The subdifferential $$\partial f(x)$$ of a convex function $$f$$ at a point $$x$$ is the set of all subgradients at $$x$$:

>
\begin{equation}
\partial f(x) = \{g \in \mathbb{R}^n | \text{g is a subgradient of f at x} \}
\end{equation}

The subdifferential has the following properties:

- $$\partial f(x)$$ is always a closed convex set, whether $$f$$ is convex or not.
- If $$f$$ is convex, $$\partial f(x)$$ always contains at least one element; if $$f$$ is not convex, it may be empty.
- If $$f$$ is differentiable and convex at $$x$$, then $$\partial f(x) = \{\nabla f(x)\}$$.
- If $$\partial f(x) = \{g\}$$, then $$f$$ is differentiable at $$x$$ and $$\nabla f(x) = g$$.


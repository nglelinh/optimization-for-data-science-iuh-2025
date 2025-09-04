---
layout: post
title: 06-03-02 Convex function quadratic upper bound
chapter: '06'
order: 9
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
lesson_type: required
---

## Quadratic Upper Bound
If $$f$$ is convex and $$\nabla f$$ is Lipschitz continuous, then $$f$$ has the following quadratic upper bound (where $$L$$ is the Lipschitz constant):

> $$ \begin{align}
f(y) & \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2 \quad \forall x, y
\end{align} $$

Also, for any convex function $$g$$, the function $$f$$ has a quadratic upper bound:

> $$ \begin{align}
g(x) & = \frac{L}{2} \| x \|^2_2 - f(x) \quad \text{is convex for all } x \text{ with } dom(g) = dom(f)
\end{align} $$

## Proof

### Monotone Operator
If $$f$$ is convex, then $$\nabla f(x)$$ is a monotone operator:

> $$(\nabla f(y) - \nabla f(x))^T (y-x) \ge 0$$

Reference: In vector space $$X$$, operator $$T : X \to X^*$$ is monotone if:
> $$(Tu - Tv, u-v) \ge 0$$, $$\forall u, v \in X$$

### Lipschitz Continuity
$$\nabla f$$ is Lipschitz continuous with constant $$L$$:
>$$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2 $$ for any $$x, y$$

### Proof that $$g$$ is convex
Let $$g(x) = \frac{L}{2} \| x \|^2_2 - f(x)$$. Using the Cauchy-Schwarz inequality, we can show:
> $$ \begin{align}
(\nabla f(x) - \nabla f(y))^T (x-y) & \le \| \nabla f(x) - \nabla f(y) \| \| x - y \| \le L \| x - y \|^2
\end{align} $$

Since $$\nabla g(x) = Lx - \nabla f(x)$$, substituting into the above gives the desired result.
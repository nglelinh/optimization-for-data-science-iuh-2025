---
layout: post
title: 08-01 Subgradient Method
chapter: "08"
order: 2
owner: "Kyeongmin Woo"
---

Assume the domain of the function is $${R}^n$$ and there is a convex function $$f$$ that may not be differentiable everywhere.

The subgradient method is defined by replacing the gradient in gradient descent with a subgradient. ($$\nabla f(x^{(k-1)}) \to g(x^{(k-1)})$$)

>$$ x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}, \quad k = 1, 2, 3, . . . $$

Here, $$g^{(k-1)} \in \partial f(x^{(k-1)})$$, i.e., $$g^{(k-1)}$$ is a subgradient of $$f$$ at $$x^{(k-1)}$$.

## Subgradient method (not subgradient "descent")

Unlike gradient descent, the subgradient method does not always guarantee descent at each step (hence the name is not subgradient "descent"). Therefore, when using the subgradient method, it is important to track the best result at each iteration.

>$$f(x_{best}^{(k)}) = \min_{i=0,...k} f(x^{(i)})$$ 

$$f(x^{(k)}_{best})$$ denotes the minimum value of the function $$f$$ obtained over $$k$$ iterations of the subgradient method.

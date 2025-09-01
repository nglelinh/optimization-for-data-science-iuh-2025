---
layout: post
title: 06-02-03 Exact line search
chapter: '06'
order: 6
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

Another way to adapt the step size in gradient descent is **exact line search**.

#### What is Exact Line Search?
In exact line search, we move in the direction of the negative gradient and choose the best possible step size.

For the following expression, if $$s > 0$$, the next step $$x - s \nabla f(x)$$ moves away from the current position. By varying $$s$$, we find the step size $$t$$ that minimizes $$f$$:

> $$t = \arg\min_{s \ge 0} f(x - s \nabla f(x))$$

Exact line search is efficient for single-variable minimization problems, but for multivariable problems, searching exhaustively for the optimal step size is often impractical. In practice, backtracking is more efficient and commonly used.
---
layout: post
title: 08-01-04 Convergence rate
chapter: "08"
order: 6
owner: "Kyeongmin Woo"
---

The convergence rate describes how the number of iterations required to reach an $$\epsilon$$-suboptimal point depends on $$\epsilon$$, using [Big-O notation](https://en.wikipedia.org/wiki/Big_O_notation). For example, if $$\epsilon = 10^{-2}$$ and the convergence rate is $$O(1/\epsilon)$$, then about $$1/10^{-2}=10^2$$ iterations are needed.

Let’s use [08-01-02 Basic inequality]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) to derive the convergence rate for the subgradient method with fixed step sizes.

>$$Recall:$$
>\begin{align}
> f^{k}_{best} - f^{*} \quad \le \quad \frac{R^{2}}{2kt} + \frac{G^{2}t}{2}
\end{align}

Suppose $$\epsilon$$ satisfies $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ and $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$ (where $$\epsilon$$ is the suboptimality gap, $$G$$ is the Lipschitz constant, and $$R$$ is the distance between the starting point and the optimal point). Then $$ \frac{R^{2}}{2kt} + \frac{G^{2}t}{2} \le \epsilon$$. If $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$, then $$t \le \frac{\epsilon}{G^{2}}$$, and $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ leads to $$\frac{R^2G^2}{\epsilon^2} \le k$$. This means the number of iterations required is at least $$\frac{R^2G^2}{\epsilon^2}$$ to achieve $$f^{k}_{best} - f^{*} \le \epsilon$$.

The convergence rate of this algorithm is $$O(1/\epsilon^2)$$, which means it requires significantly more iterations than the gradient descent method, which has a rate of $$O(1/\epsilon)$$.
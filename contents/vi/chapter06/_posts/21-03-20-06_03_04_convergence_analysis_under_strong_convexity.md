---
layout: post
title: 06-03-04 Convergence analysis under strong convexity
chapter: '06'
order: 11
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

If $$f$$ satisfies the following condition, it is strongly convex (assuming $$f$$ is twice differentiable and $$m > 0$$):
> $$ \begin{align}
f(y) \ge f(x) + \nabla f(x)^T(y-x) + \frac{m}{2} \| y-x \|_2^2, \quad \forall x, y
\end{align} $$

Here, $$f$$ has a quadratic lower bound, and the constant $$m$$ is determined by the minimum eigenvalue of the Hessian of $$f$$.

For any convex function $$g$$, $$f$$ is strongly convex if:
> $$ \begin{align}
g(x) = f(x) - \frac{m}{2} \| x \|_2^2 \quad \text{is convex for all } x \text{ and } m > 0
\end{align} $$

## Convergence Theorem
Given Lipschitz continuity and strong convexity, the following theorem holds (where $$L$$ is the Lipschitz constant and $$m$$ is the strong convexity constant):

**Gradient descent** with fixed step size ($$t \le 2/(m + L)$$) or backtracking line search satisfies:
> $$ \begin{align}
f(x^{(k)}) - f^* \le c^k \frac{L}{2} \| x^{(0)} - x^* \|_2^2, \quad c = (1 - \frac{m}{L}), \quad 0 < c < 1
\end{align} $$

## Proof
If $$\nabla f$$ is Lipschitz continuous and $$f$$ is strongly convex, then $$f$$ has a quadratic upper bound (see [06-03-02]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})).

For gradient descent $$x^+ = x - t \nabla f(x)$$, the optimal $$t$$ is $$1/L$$, yielding:
> $$ \begin{align}
f(x^+) \le f(x) -  \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Subtracting $$f(x^*)$$ from both sides:
> $$ \begin{align}
f(x^+) - f(x^*) \le f(x) - f(x^*) -  \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Since Gradient Descent satisfies the condition:
> $$ \begin{align}
f(x) - f(x^*) \le \frac{1}{2m} \| \nabla f(x) \|_2^2
\end{align} $$

We can substitute to get:
> $$ \begin{align}
f(x^+) - f(x^*) & \le f(x) - f(x^*) -  \frac{m}{L} ( f(x) - f(x^*) ) \\
& =  (1 -  \frac{m}{L} ) ( f(x) - f(x^*) ) \\
& = c  ( f(x) - f(x^*) ) \\
\end{align} $$

Iterating this process gives:
> $$ \begin{align}
f(x^{(k)}) - f(x^*) \le c^k ( f(x^{(0)}) - f(x^*) ) \\
\end{align} $$

From the Taylor expansion of the function with $$y = x^{(0)}$$ and $$x = x^*$$:
> $$ \begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \lVert y - x \rVert^2_2  \space \space \forall x, y
\end{align} $$

And since the function is convex, we have:
> $$ \begin{align}
f(x^{(0)}) & \le f(x^{*}) + \nabla f(x^{*})^T (x^{(0)}- x^{*} ) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\\\
& =  f(x^{*}) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\\\
\end{align} $$

Rearranging gives:
> $$ \begin{align}
f(x^{(0)}) - f(x^{*}) & \le \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\\\
\end{align} $$

Substituting this into the previous inequality results in:
> $$ \begin{align}
f(x^{(k)}) - f(x^{*}) & \le c^k \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2  \\\
\end{align} $$

This proves the Convergence Theorem for Gradient Descent under Strong Convexity.

## Linear convergence
When $$f$$ is strongly convex, the convergence rate becomes $$O(c^k)$$, which is exponential.
To achieve $$f(x^{(k)}) - f^{*} \le \epsilon$$, it requires $$O(\log(1/\epsilon)$$ iterations.
(Without strong convexity, it would require $$O(1/\epsilon)$$ iterations.)

The convergence rate $$O(c^k)$$ appears linear on a semi-log plot, as shown below.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06.03_01_01_Line_Convergence.png" alt="Line_Convergence" width="60%" height="60%">
  <figcaption style="text-align: center;">[Fig 1] Linear convergence [1]</figcaption>
</p>
</figure>

Here, the constant $$c$$ in $$O(c^k)$$ is given by $$1 - \frac{m}{L}$$ and depends on the condition number $$L/m$$. A larger condition number results in slower convergence (where the condition number is the ratio of the largest eigenvalue to the smallest eigenvalue).


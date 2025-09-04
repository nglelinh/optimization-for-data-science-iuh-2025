---
layout: post
title: 06-02-02 Backtracking line search
chapter: '06'
order: 5
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

The basic update rule is:
$$x_{k+1} = x_k - t_k \nabla f(x_k),$$
where $$ x_k $$ is the parameter vector at iteration $$ k $$, $$\nabla f(x_k) $$ is the gradient, and $$ t_k > 0 $$ is the step size (learning rate).

If a fixed step size is used in gradient descent, the convergence speed is always the same, which can be problematic in ill-conditioned regions (where the minimum is missed or progress is slow). To address this, the step size can be adaptively chosen to match the function's curvature. One such method is **backtracking line search**.

### What is Backtracking Line Search?
This method tries a step from the current position, and if the step is too large, it backtracks. The figure below shows how backtracking line search determines the step size.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Backtracking_Line_Search.png" alt="backtrackinglinesearch1" width="100%" height="100%">
  <figcaption style="text-align: center;">[Fig1] Backtracking Line Search [3]</figcaption>
</p>
</figure>

Line search methods dynamically choose $$ t_k $$ to ensure sufficient progress, typically by minimizing $$ f $$ along the search direction $$ d_k = -\nabla f(x_k) $$ (negative gradient for descent).
Exact line search finds $$ t_k = \arg\min_{t > 0} f(x_k + t d_k) $$, but this is computationally expensive for non-quadratic $$ f $$. Inexact line search approximates this efficiently, and backtracking line search is a popular inexact method due to its simplicity and guarantees.

In a convex function $$f$$, the search region is restricted to a line. The lower line is a step from the current position $$x$$ in the descent direction. If $$f$$ is always above the line, it is hard to judge if the step is too large or appropriate. In backtracking line search, the upper line is used, which is a step in the direction of the descent scaled by $$t$$. If $$f(x + t \Delta x)$$ is above the line, the step is too large; if below, the step is appropriate.

If the step is too large, $$t$$ is reduced until $$f$$ falls below the line. The final $$t$$ is in the interval $$0 \le t \le t_0$$.

### Backtracking Line Search Algorithm

Summarized as follows (with $$\Delta x = - \nabla f(x)$$):

1. Initialize parameters ($$0 < \beta < 1$$, $$0 < t \le 1/2$$).
2. For each iteration, set $$t = t_{init}$$ ($$t_{init} = 1$$).
3. While $$f(x - t \nabla f(x)) > f(x) - t t \|\nabla f(x)\|_2^2$$, set $$t = \beta t$$.
4. Update $$x^+ = x - t \nabla f(x)$$.
5. If stopping criterion is not met, repeat from step 2.

Backtracking line search is simple and effective. The parameter $$t$$ determines the direction, and $$\beta$$ determines how much to backtrack. Typically, $$t = 1/2$$ and $$\beta$$ is chosen close to 1.

### Backtracking Line Search Example
With adaptive step size, convergence is much faster than with a fixed step size (e.g., 12 steps vs. 100 steps for the same problem). Including backtracking steps, total convergence is achieved in about 40 steps.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Convergence.png" alt="backtrackinglinesearch1" width="70%" height="70%">
  <figcaption style="text-align: center;">[Fig2] Convergence [3]</figcaption>
</p>
</figure>

### Intuition of Backtracking Line Search
A quadratic approximator for $$f$$ is:
> $$f(y) \approx f(x) + \nabla f(x)^T(y-x) + \frac{1}{2t} \|y - x\|_2^2$$

For $$y = x - t \nabla f(x)$$:
> $$
> \begin{align}
> f(x - t \nabla f(x)) &\approx f(x) - t \|\nabla f(x)\|_2^2 + \frac{1}{2}t \|\nabla f(x)\|_2^2
> \end{align}
>$$
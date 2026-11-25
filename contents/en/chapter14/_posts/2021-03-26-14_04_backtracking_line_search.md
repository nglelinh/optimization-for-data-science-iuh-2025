---
layout: post
title: 14-04 Backtracking line search
chapter: '14'
order: 10
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

Pure Newton's method always takes a full step $$t = 1$$—which is brilliant inside the quadratic basin, yet reckless when far from the solution where the local quadratic bowl is a poor match for the true function. **Backtracking line search** gives Newton a smart throttle: always *try* the full unit step $$t = 1$$ first, and only shrink $$t \leftarrow \beta t$$ if the actual function drop falls short of a fraction $$\alpha$$ of the predicted linear decrease.

## Background Knowledge Map: Globalizing Newton with Backtracking

- **Pillar 1 — The Armijo Sufficient-Decrease Test:** Starting at $$t = 1$$, accept $$t$$ once $$f(x + tv) \le f(x) + \alpha t \nabla f(x)^T v = f(x) - \alpha t \lambda(x)^2$$, with typical parameters $$\alpha \in (0.01, 0.3)$$ and $$\beta \in (0.1, 0.8)$$.
- **Pillar 2 — Why Always Start at $$t = 1$$:** Near the optimum, the full Newton step $$t = 1$$ automatically passes the backtracking test (for any $$\alpha < 1/2$$), so damped Newton transitions seamlessly into pure quadratic convergence with zero wasted evaluations.
- **Pillar 3 — Domain Safety for Barriers:** When $$\operatorname{dom}(f) \subsetneq \mathbb{R}^n$$ (as in log-barrier methods), backtracking first shrinks $$t$$ until $$x + tv \in \operatorname{dom}(f)$$ before checking the Armijo inequality.
- **Pillar 4 — Cheap Per-Step Cost:** Each backtracking trial only evaluates the scalar objective $$f(x + tv)$$ (no Hessian or linear solve), costing $$O(n)$$ compared to $$O(n^3)$$ for the Newton direction.

### Step-by-Step Worked Example (Read Slowly): Executing One Damped Newton Step by Hand

Minimize $$f(x) = e^{x} + e^{-2x}$$ starting from $$x = 2$$, with backtracking parameters $$\alpha = 0.25$$ and $$\beta = 0.5$$.

1. **Compute $$f$$, $$f'$$, $$f''$$, and Newton step $$v$$ at $$x = 2$$:**
   - $$f(2) = e^2 + e^{-4} \approx 7.3891 + 0.0183 = 7.4074$$.
   - $$f'(2) = e^2 - 2e^{-4} \approx 7.3891 - 0.0366 = 7.3525$$.
   - $$f''(2) = e^2 + 4e^{-4} \approx 7.3891 + 0.0733 = 7.4624$$.
   - Newton direction: $$v = -\frac{f'(2)}{f''(2)} \approx -\frac{7.3525}{7.4624} = -0.9853$$.
   - Directional derivative: $$f'(2)v = -\lambda(2)^2 \approx -(7.3525)(0.9853) = -7.244$$.
2. **Test $$t = 1$$ (target RHS: $$f(2) + 0.25(1)(-7.244) = 7.4074 - 1.8110 = 5.5964$$):**
   - Candidate point: $$x + v = 2 - 0.9853 = 1.0147$$.
   - Objective value: $$f(1.0147) = e^{1.0147} + e^{-2.0294} \approx 2.7585 + 0.1314 = 2.8899 \le 5.5964$$!
   - Full step $$t = 1$$ is accepted immediately on the first check, slashing $$f$$ from $$7.41$$ to $$2.89$$.
3. **What if we started at $$x = -2$$ instead?** At $$x = -2$$, $$f(-2) \approx 54.73$$, $$v \approx +0.499$$, and $$f(-2 + 0.499) \approx 20.37$$; if a harsh non-quadratic spike caused $$f(x+v) > f(x) + \alpha f'(x)v$$, backtracking would test $$t = 0.5, 0.25, \dots$$ until sufficient decrease holds.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

So far, we have examined pure Newton's method. However, this method does not guarantee convergence, so we use backtracking line search to ensure convergence in the damped Newton's method.

## Damped Newton's method
The pure Newton's method iteratively applies the following update (here $$t=1$$):

>\begin{align}
>x^{+} = x -t(\nabla^{2}f(x))^{-1}\nabla f(x).
>\end{align}

Damped Newton's method uses backtracking line search. If the function value at the updated position is greater than the quadratic approximation, we shrink the step size $$t$$:

>$$\begin{align}
>&\text{with parameters }0<\alpha \leq \frac{1}{2}, 0<\beta<1, \\
>&\text{while } f(x+tv)>f(x)+\alpha t \nabla f(x)^{T}v\\
>&\text{shrink }t=\beta t
>\end{align}$$

Here, $$v=-(\nabla^{2}f(x))^{-1}\nabla f(x)$$ and $$\nabla f(x)^{T}v = -\lambda^{2}(x)$$.

## Example: logistic regression
As an example, for logistic regression with n = 500, p = 100, we compare the convergence rate of gradient descent and Newton's method with backtracking line search.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/2.jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Logistic regression [3]</figcaption>
</p>
</figure>


Newton's method shows a much faster convergence rate than gradient descent. From the next chapter, we will examine this convergence rate.
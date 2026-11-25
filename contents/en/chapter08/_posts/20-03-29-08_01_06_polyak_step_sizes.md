---
layout: post
title: '08-01-06 Polyak step sizes'
chapter: '08'
order: 8
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

Choosing a diminishing step-size schedule often feels like flying blind: make $$t_k$$ too small and you crawl; make it too large and you bounce wildly. In 1969, Boris Polyak asked a deceptively simple question: *what if you already know the optimal value $$f^\star$$?* In feasibility problems, overparameterized machine learning (where interpolation achieves $$f^\star = 0$$), and exact-zero-residual systems, $$f^\star$$ is known a priori—and Polyak showed that projecting onto the linear underestimator $$f(x^{(k)}) + g^{(k)\top}(x - x^{(k)}) = f^\star$$ yields a self-tuning, parameter-free step size that strictly minimizes the distance bound at every single iteration.

## Background Knowledge Map: The Geometry of Polyak's Step Size

- **Pillar 1 — Exact Hyperplane Projection Intuition:** Setting the first-order convex lower bound $$f(x^{(k)}) + g^{(k)\top}(x - x^{(k)})$$ equal to $$f^\star$$ defines a separating hyperplane that separates $$x^{(k)}$$ from the optimal set. Projecting $$x^{(k)}$$ orthogonally onto this hyperplane yields the exact Polyak step $$t_k = \frac{f(x^{(k)}) - f^\star}{\|g^{(k)}\|_2^2}$$.
- **Pillar 2 — Optimal One-Step Distance Reduction:** Minimizing the RHS of the one-step distance inequality $$\|x^{(k+1)} - x^\star\|_2^2 \le \|x^{(k)} - x^\star\|_2^2 - 2t_k(f(x^{(k)}) - f^\star) + t_k^2 \|g^{(k)}\|_2^2$$ with respect to $$t_k$$ recovers Polyak's formula uniquely, shrinking the squared distance by at least $$\frac{(f(x^{(k)}) - f^\star)^2}{\|g^{(k)}\|_2^2}$$ at every step.
- **Pillar 3 — Scale Invariance & Zero Hyperparameter Tuning:** If you rescale the objective by a constant $$c > 0$$ (replacing $$f$$ with $$cf$$), both the numerator $$f - f^\star$$ and denominator $$\|g\|_2^2$$ scale cleanly so $$t_k g^{(k)}$$ is *completely invariant* to objective scaling—no Lipschitz constant $$G$$ or initial radius $$R$$ is ever needed.
- **Pillar 4 — Sensitivity to Misspecified $$f^\star$$:** Polyak's rule assumes $$f^\star$$ is exact. Overestimating $$f^\star$$ stalls progress early; underestimating $$f^\star$$ causes persistent overshooting near the optimum, motivating modern adaptive variants (such as SPS in stochastic deep learning) that estimate or clip $$f^\star$$.

### Step-by-Step Worked Example (Read Slowly): Polyak's Step vs. Fixed Step on a Steep Piecewise Linear Function

Consider $$f(x) = \max\{ 2x - 2,\; -4x - 2,\; 0 \}$$ on $$\mathbb{R}$$, whose optimal value is known to be $$f^\star = 0$$ (achieved on the interval $$x \in [-0.5, 1]$$). Start at $$x^{(0)} = 4$$.

1. **Iteration 1 at $$x^{(0)} = 4$$:**
   - Evaluate the pieces: $$2(4) - 2 = 6$$, $$-4(4) - 2 = -18$$, $$0$$. Thus $$f(4) = 6$$ and the active piece is $$2x - 2$$, so $$g^{(0)} = 2$$.
   - Compute Polyak step size:
     $$t_1 = \frac{f(x^{(0)}) - f^\star}{\|g^{(0)}\|_2^2} = \frac{6 - 0}{2^2} = \frac{6}{4} = 1.5.$$
   - Update:
     $$x^{(1)} = x^{(0)} - t_1 g^{(0)} = 4 - 1.5(2) = 1.0.$$
2. **Check the result:** At $$x^{(1)} = 1.0$$, $$f(1.0) = \max\{0, -6, 0\} = 0 = f^\star$$! Polyak's step hit the exact optimal set in a *single* iteration because the active linear piece intersected $$y = f^\star$$ at $$x = 1$$.
3. **Verify the distance contraction bound:** With $$x^\star = 1$$ (the closest minimizer), $$\|x^{(0)} - x^\star\|^2 = (4 - 1)^2 = 9$$, and Polyak guarantees:
   $$\|x^{(1)} - x^\star\|^2 \le 9 - \frac{(6 - 0)^2}{2^2} = 9 - 9 = 0.$$
   Here the bound is tight to the last decimal place, illustrating why Polyak's rule is the gold standard whenever $$f^\star$$ is known.

**Polyak step sizes** are a way to set the step size when the optimal value is known. If $$f^*$$ is known, Polyak step sizes can be defined as follows.

## Convergence theorem for Polyak step-sizes
>
$$ \begin{align}
t_k = \frac{f^{(k-1)}-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}}, \quad k = 1,2,3...
\end{align} $$

## Proof of convergence theorem for Polyak step-sizes
The proof can be derived from the [basic inequality]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) and the sequence of inequalities used there.

>
$$ \begin{align}
 \Vert x^{(k)}-x^* \Vert_2^{2}  \quad \le \quad  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} \\
\end{align} $$

By differentiating the right-hand side above with respect to $$t_k$$ and setting it to zero, we obtain the Polyak step size that minimizes the right-hand side.
>
$$ \begin{align}
& \frac{\partial}{\partial t_k}  \Vert x^{(k-1)}-x^* \Vert_2^{2}-2t_k (f(x^{(k-1)})-f^*)+t_k^{2} \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & -2(f(x^{(k-1)})-f^*)+2t_k \Vert g^{(k-1)} \Vert_2^{2} = 0 \\
 \Longleftrightarrow & f(x^{(k-1)})-f^* = t_k \Vert g^{(k-1)} \Vert_2^{2} \\
 \Longleftrightarrow & t_k = \frac{f(x^{(k-1)})-f^*}{ \Vert g^{(k-1)} \Vert_2^{2}} \quad \text{(Polyak step size at k)}
\end{align} $$

The convergence rate of the Polyak step size can also be derived from the [basic inequality]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) and the sequence of inequalities used there.

## Convergence rate for Polyak step-sizes

Let’s substitute the Polyak step size $$t_i$$ into the basic inequality derived in the [basic inequality]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}).
>
$$ \begin{align}
& 2\sum_{i=1}^{k}t_i(f(x^{(i)})-f^*) \le R^2 + \sum_{i=1}^kt_i^2 \Vert g^{(i)} \Vert_2^2 \\
 \Longleftrightarrow \quad & 2\sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 + \sum_{i=1}^k\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \\
 \Longleftrightarrow \quad & \sum_{i=1}^{k}\frac{(f(x^{(i)})-f^*)^2}{ \Vert g^{(i)} \Vert_2^2} \le R^2 \\
\end{align} $$

Assuming that the Lipschitz condition $$ \Vert g^{(i)} \Vert_2 \le G$$ always holds, the above inequality can be rearranged as follows:
>
$$ \begin{align}
& \sum_{i=1}^{k}(f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & k ⋅ (f(x^{(i)})-f^*)^2 \le R^2G^2 \\
 \Longleftrightarrow \quad & \sqrt{k} ⋅ (f(x^{(i)})-f^*) \le RG \\
 \Longleftrightarrow \quad & (f(x^{(i)})-f^*) \le \frac{RG}{\sqrt{k}} \\
\end{align} $$

If we let $$\frac{RG}{\sqrt{k}}=\epsilon$$, then $$k=\big(\frac{RG}{\epsilon}\big)^2$$, so the number of trials required to reach a suboptimal point with respect to $$\epsilon$$ is on the order of $$\big(\frac{RG}{\epsilon}\big)^2$$. In other words, the convergence rate is $$O(1/\epsilon^{2})$$, which is the same as other subgradient methods.

### The Polyak step: choosing the step from f* (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/polyak-step_en.mp4"></video>
</div>

A constant step stalls at a floor, a diminishing step creeps, and the Polyak step $$\alpha_k=\dfrac{f(x_k)-f^*}{\|g_k\|_2^2}$$ lands on the minimiser, but it needs $$f^*$$.

### Try it yourself: three step-size rules

<div class="opx-explainer" data-opx="sgm" data-lang="en"></div>

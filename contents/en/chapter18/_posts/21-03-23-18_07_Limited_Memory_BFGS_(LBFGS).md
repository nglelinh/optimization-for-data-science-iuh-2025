---
layout: post
title: 18-07 Limited Memory BFGS (LBFGS)
chapter: '18'
order: '8'
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

Standard BFGS is a triumph—until your problem has $$n = 1{,}000{,}000$$ variables. Storing a dense $$10^6 \times 10^6$$ inverse Hessian $$H_k$$ in double precision would require **8 terabytes of RAM**, crashing before iteration 1 even finishes. **Limited-Memory BFGS (L-BFGS)** solves this memory wall with a breathtakingly simple observation: you never actually *need* the matrix $$H_k$$; you only ever need its action on a single vector, $$H_k \nabla f(x^k)$$. By keeping only the last $$m$$ curvature pairs $$(s_i, y_i)$$ (typically $$m = 5\text{–}20$$), the **two-loop recursion** computes the exact L-BFGS search direction in $$O(mn)$$ time and $$O(mn)$$ memory!

## Key ideas: Breaking the $$O(n^2)$$ Memory Barrier

- **Implicit Operator Representation:** Instead of storing $$H_k \in \mathbb{R}^{n \times n}$$, L-BFGS stores a rolling FIFO buffer of the $$m$$ most recent vector pairs $$\{(s_i, y_i)\}_{i=k-m}^{k-1}$$ and applies the BFGS congruence formula on the fly to a simple diagonal seed $$H_k^0 = \gamma_k I$$.
- **Self-Scaled Initial Seed ($$\gamma_k = \frac{s_{k-1}^T y_{k-1}}{y_{k-1}^T y_{k-1}}$$):** Choosing $$\gamma_k$$ as the Barzilai–Borwein inverse-curvature estimate scales the initial identity matrix to match the local Hessian magnitude, dramatically improving unit-step acceptance.
- **The Two-Loop Recursion ($$4mn$$ FLOPs):** The backward loop peels off projections $$\alpha_i = \rho_i s_i^T q$$ from newest to oldest; the middle step multiplies by $$H_k^0$$; and the forward loop reconstructs $$r = H_k g_k$$ from oldest to newest via $$\beta_i = \rho_i y_i^T r$$.
- **Trade-Off Between $$m$$ and Convergence:** L-BFGS forfeits full-memory superlinear convergence (converging linearly, like preconditioned CG), yet $$m = 10$$ typically captures the dominant Hessian eigenvalues and outperforms first-order methods by orders of magnitude on smooth, ill-conditioned large-scale objectives.

### Worked example: Tracing the Two-Loop Recursion by Hand ($$m = 2$$)

Suppose $$n = 2$$ and our memory buffer holds $$m = 2$$ pairs:
- Older pair $$i = 0$$: $$s_0 = (1, 0)^T, \; y_0 = (2, 0)^T \implies \rho_0 = \frac{1}{y_0^T s_0} = \frac{1}{2}$$.
- Newer pair $$i = 1$$: $$s_1 = (0, 1)^T, \; y_1 = (0, 4)^T \implies \rho_1 = \frac{1}{y_1^T s_1} = \frac{1}{4}$$.
We want to compute $$r = H_2 q$$ for the current gradient $$q = g_2 = (4, 8)^T$$. (Notice the true underlying Hessian here is $$\operatorname{diag}(2, 4)$$, so the exact Newton vector $$Q^{-1} g_2$$ should be $$(2, 2)^T$!)

1. **Backward loop ($$i = 1$$, then $$i = 0$$):**
   - $$i = 1$$: $$\alpha_1 = \rho_1 (s_1^T q) = \frac{1}{4}(8) = 2$$. Update $$q \leftarrow q - \alpha_1 y_1 = \begin{bmatrix}4\\8\end{bmatrix} - 2\begin{bmatrix}0\\4\end{bmatrix} = \begin{bmatrix}4\\0\end{bmatrix}$$.
   - $$i = 0$$: $$\alpha_0 = \rho_0 (s_0^T q) = \frac{1}{2}(4) = 2$$. Update $$q \leftarrow q - \alpha_0 y_0 = \begin{bmatrix}4\\0\end{bmatrix} - 2\begin{bmatrix}2\\0\end{bmatrix} = \begin{bmatrix}0\\0\end{bmatrix}$$.
2. **Initial seed multiplication:**
   $$\gamma_2 = \frac{s_1^T y_1}{y_1^T y_1} = \frac{4}{16} = \frac{1}{4}, \qquad r \leftarrow \gamma_2 q = \frac{1}{4}\begin{bmatrix}0\\0\end{bmatrix} = \begin{bmatrix}0\\0\end{bmatrix}.$$
3. **Forward loop ($$i = 0$$, then $$i = 1$$):**
   - $$i = 0$$: $$\beta_0 = \rho_0 (y_0^T r) = 0$$. Update $$r \leftarrow r + (\alpha_0 - \beta_0) s_0 = \begin{bmatrix}0\\0\end{bmatrix} + (2 - 0)\begin{bmatrix}1\\0\end{bmatrix} = \begin{bmatrix}2\\0\end{bmatrix}$$.
   - $$i = 1$$: $$\beta_1 = \rho_1 (y_1^T r) = \frac{1}{4}(0) = 0$$. Update $$r \leftarrow r + (\alpha_1 - \beta_1) s_1 = \begin{bmatrix}2\\0\end{bmatrix} + (2 - 0)\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}2\\2\end{bmatrix}$$.
4. **Verify:**
   The two-loop recursion returned $$r = (2, 2)^T = Q^{-1} g_2$$ **identically** using only dot products and vector additions—without ever forming a $$2 \times 2$$ matrix!

# Introduction

LBFGS is an example of limited-memory quasi-Newton methods, and is useful when the cost of computing or storing the Hessian matrix is not reasonable. The method estimates (approximates) the Hessian matrix by maintaining only a few $$n$$-dimensional vectors instead of storing a dense $$n \times n$$ Hessian matrix.

The LBFGS algorithm is based on BFGS, as its name suggests. The main idea is to use curvature information from the most recent iterations to estimate the Hessian. On the other hand, curvature information from older iterations is not used, in order to save storage space, as it may be somewhat distant from the behavior shown by the Hessian of the current iteration.

As a side note, limited-memory versions of other quasi-Newton algorithms (e.g., SR1) can also be derived using the same technique [14].

# LBFGS

To explain LBFGS, let us first look at the BFGS method. At each step, BFGS updates $$x$$ as follows:

>$$
>x^+ = x - t H \nabla f, \\\\
>\text{where } t \text{ is the step length and } H \text{ is updated at every iteration by means of the formula, }\\\\
>\text{ }\\\\
>H^+ = \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts}. \\\\
>$$

For $$H$$ as above, $$H^+q, q \in \mathbb{R}^n$$ can be expressed using scalars $$\alpha, \beta \in \mathbb{R}$$ and vectors $$p, s \in \mathbb{R}^n$$.

>$$
>\begin{align}
>H^+q &= \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big)q + \frac{ss^Tq}{y^Ts}\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) \underbrace{H \big( q - \frac{s^T q}{y^Ts} y \big)}_{p} + \underbrace{\frac{s^Tq}{y^Ts}}_{\alpha} s\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) p + \alpha s\\\\
> &= p - \underbrace{\frac{y^Tp}{y^Ts}}_{\beta}s + \alpha s \\\\
> &= p + (\alpha - \beta) s, \\\\
>& \text{where } \alpha = \frac{s^Tq}{y^Ts}, q^+ = q - \alpha y, p = Hq^+, \beta = \frac{y^Tp}{y^Ts}.
>\end{align} \\\\
>$$

When $$H$$ is obtained through $$k$$ BFGS updates, $$Hq = -H\nabla f(x)$$ can be computed in $$O(kn)$$ operations (see the algorithm below). To use memory efficiently, we only use curvature information from the $$m$$ most recent iterations (for $$k \ge m$$).

# Algorithm

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/algorithm_quasi-newton.png" alt="[Fig1] The algorithm of LBFGS [3]" width="90%">
  <figcaption style="text-align: center;">[Fig1] The algorithm of LBFGS [3]</figcaption>
</p>
</figure>

Usually, the inverse Hessian approximation $$H_k$$ is dense, and when there are many variables the computation becomes very heavy. LBFGS obtains $$H_k \nabla f_k$$ through sums and products of successive vectors, which resolves the computational problem of $$H_k$$.

In the computation, the initial Hessian approximation $$H^{0, k}$$ is usually (and has been verified to be very effective) the identity matrix multiplied by a constant ($$H^{0, k} = \gamma_k I$$), so the computation is not too large ([14], Section 7.2).

>$$
>H^{0, k} = \gamma_k I, \\\\
>\text{where } \: \gamma_k = \frac{s^T_{k-1}y_{k-1}}{y^T_{k-1}y_{k-1}}.
>$$

* **Note:** $$H^{0, k}$$ changes at every iteration.

### L-BFGS in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/l-bfgs_en.mp4"></video>
</div>

Why BFGS needs n² memory, m pairs (s, y) and H₀ = γI, the two-loop recursion by hand in 2D, then step counts on logistic regression.

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

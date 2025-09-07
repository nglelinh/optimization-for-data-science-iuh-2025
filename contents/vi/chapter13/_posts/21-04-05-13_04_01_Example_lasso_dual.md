---
layout: post
title: 13-04-01 Example lasso dual
chapter: '13'
order: 6
owner: Wontak Ryu
categories:
- chapter13
lang: en
---

Let’s look at the lasso problem for $$y \in \mathbb{R}^n, X \in \mathbb{R}^{n\times p}$$:

> $$ \min_\beta \frac{1}{2} \| y-X\beta \|^2_2 + \lambda\| \beta \|_1$$
> 
> $$f(\beta) = \frac{1}{2} \| y - X\beta \|^2_2 +  \lambda\| \beta \|_1$$
> 
> $$L(\beta) = f(\beta)$$
> 
>  $$ \min_\beta L(\beta) = f^{\star}$$

The dual function of the above is constant (= $$f^*$$). Therefore, we can transform the primal problem as follows:

> $$ \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 \text{ subject to } z = X\beta$$

The dual function of the transformed problem is:
> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda) \\
> \end{align}$$
> 

#### [Proof]
> $$\begin{align}
> g(u) &= \min_{\beta,z} \frac{1}{2} \| y-z \|^2_2 + \lambda \| \beta \|_1 + u^T(z-X\beta) \\
> &= \underbrace{ \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)}_{(1)} + \underbrace{\left( \min_\beta  \lambda \| \beta \|_1 + u^TX\beta \right)}_{(2)} \\
> \end{align}$$
> 
> $$ z^{\star} = y - u$$
> 
> $$\begin{align}
> (1) \cdots \left( \min_z \frac{1}{2} \| y - z \|^2_2 + u^Tz \right)
> &= \frac{1}{2} \| u \|^2_2 + u^T(y - u) \\
> &= -\frac{1}{2} \| y - u \|^2_2 + \frac{1}{2} \| y \|^2_2 \\
> \end{align}$$
> $$\begin{align}
> (2) \cdots \left( \min_\beta  \lambda \| \beta \|_1 + u^TX\beta \right) 
> &= - \lambda \max_\beta \frac{u^Tx}{\lambda} \beta - \| \beta \|_2 \\
> &= - \lambda \left( \| \frac{u^Tx}{\lambda} \|_\infty \leq 1 \right) \\
> &= - \lambda \left( \| u^Tx \|_\infty \leq \lambda \right) \\
> \end{align}$$
> \therefore g(u) = -\frac{1}{2} \| y - u \|^2_2 + \frac{1}{2} \| y \|^2_2 + - \lambda \left( \| u^Tx \|_\infty \leq \lambda \right)
> = \frac{1}{2} \| y \|^2_2 - \frac{1}{2} \| y-u \|^2_2 - I_{\{ v : \| v \|_\infty \leq 1 \}}(X^Tu/\lambda)

Therefore, the lasso dual problem is:

> $$ \max_u \frac{1}{2} ( \| y \|^2_2 - \| y-u \|^2_2 ) \text{ subject to } \| X^Tu \|_\infty \leq \lambda$$

This is equivalent to:

> $$ \min_u \| y-u \|^2_2 \text{ subject to } \| X^Tu \|_\infty \leq \lambda$$

### [Check]
Slater’s condition is satisfied, so strong duality holds.
> $$ \text{strong duality } \implies (\beta^{\star}, z^{\star})$$
> 
> $$ \text{ must minimize  } L( \beta, z, u^{\star} ) \text{ over } -u, \beta, z$$

### [note]
The optimal value in the previous problem is not the optimal lasso objective value.
However, the dual solution $$u$$ and the lasso solution $$\beta$$ satisfy $$X\beta = y-u$$.

This is satisfied by the KKT stationarity condition $$z$$ (i.e., $$z-y + \beta = 0$$).

Therefore, lasso satisfies the dual residual.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter13/Conjugate_LassoDual_Example.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2] Lasso Dual [1]</figcaption>
</p>
</figure>
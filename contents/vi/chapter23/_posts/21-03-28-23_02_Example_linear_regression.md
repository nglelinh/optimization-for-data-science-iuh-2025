---
layout: post
title: '23-02 Example: linear regression'
chapter: '23'
order: 3
owner: Jinwoo Park
categories:
- chapter23
lang: vi
---

Let's define the linear regression problem as follows.

> $$\min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2,$$
> $$\text{given } y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^{n \times p} \text{ with columns } X_1, \dots, X_p.$$

When $$\beta_j,\: j \neq i$$ are fixed values, let's find $$\beta_i$$ that minimizes the given objective function.
($$-i$$ means the remaining terms excluding $$i$$. - In the case of $$X$$, the remaining columns excluding the $$i$$-th column.)

$$\begin{align}
0 &= \nabla_i f(\beta)\\\\
&= X_i^T (X\beta - y)\\\\
&= X_i^T (X_i \beta_i + X_{-i} \beta_{-i} - y)\\\\
\Rightarrow\\\\
&\beta_i = \frac{X_i^T (y - X_{-i} \beta_{-i})}{X_i^T X_i}
\end{align}$$

Through coordinate descent, we iterate and update $$\beta_i$$ for $$i=1,2,\dots,p,1,2,\dots$$.

## Experiment: Convergence speed comparison - GD vs AGD vs CD

The graph below shows the convergence speeds of coordinate descent, gradient descent, and accelerated gradient descent for a linear regression problem with $$n=100, p=20$$. (The k on the horizontal axis represents one step (GD, AGD) or one cycle (CD).)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/gd_vs_agd_vs_cd.png" alt="[Fig1] GD vs AGD vs CD [3]">
  <figcaption style="text-align: center;">[Fig1] GD vs AGD vs CD [3]</figcaption>
</p>
</figure>
<br/>

According to the above results, coordinate descent shows significantly better convergence speed than AGD, which is optimal among first-order methods. Why can this phenomenon occur? To conclude, coordinate descent can achieve performance that far surpasses AGD because it utilizes more information than first-order methods. This is because coordinate descent uses the latest information updated in the previous step at each step within one cycle. (That is, CD is not a first-order method.)

### Q. Then, is it fair to compare one cycle of CD with one step of GD in the above experiment?

**A. Yes.** The CD update formula introduced earlier can be modified to have a time complexity of $$O(n)$$ per step. Then, the time complexity of one cycle for CD becomes $$O(np)$$, which has the same time complexity as one step of GD.

* **Gradient descent update:** $$\beta \leftarrow \beta + tX^T(y-X\beta)$$, the time complexity of the $$X\beta$$ operation becomes $$O(np)$$ flops.

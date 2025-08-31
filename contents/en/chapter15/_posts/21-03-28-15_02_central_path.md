---
layout: post
title: 15-02 Central path
chapter: "15"
order: 6
owner: "Minjoo Lee"
---

If we denote the solution to the following barrier problem ($$t > 0$$) as $$x^*(t)$$, then the **central path** is the set $$\{x^*(t) | t > 0 \}$$.

>$$\begin{align}
> &\min_{x} \ &&  tf(x) + \phi(x) \\
> &\text{subject to } \ && Ax = b \\
> \end{align}$$

Given suitable conditions, the **central path** set forms a smooth path in $$\mathbb{R}^n$$, and as $$t \to \infty$$, $$x^*(t) \to x^*$$, where $$x^*$$ is the solution to the original problem.

The **central path** is a set of solutions obtained by gradually redefining the problem for new values of $$t$$, moving from the interior toward the boundary when it is difficult to find the optimal solution at the boundary directly.

## Example: central path for an LP
Let's find the central path for the following LP problem.
>$$\begin{align*}
>&\min_{x} \ && c^Tx \\
>&\text{subject to } \ && a_i^Tx \le b_i^T, i = 1, \cdots , 6 \\
>\end{align*}$$

In the following figure, the dotted line represents the logarithmic barrier function $$\phi$$. <br>

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_central_path_02.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Central path [1]</figcaption>
</p>
</figure>

You can see that as $$t \to \infty$$, the central path converges to the optimal $$x^*$$. At this point, the hyperplane $$c^Tx = c^Tx(t)$$ is the tangent to the level curve of $$\phi$$ passing through $$c^Tx(t)$$.

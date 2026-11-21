---
layout: post
title: 20-02-01 Dual Decomposition with Equality Constraint
chapter: '20'
order: 5
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Consider the following problem.
>$$\begin{equation}
>\min_x \sum_{i=1}^B f_i(x_i) \quad \text{ subject to } \quad Ax = b
>\end{equation}$$

Suppose the variable $$x$$ is split into $$B$$ blocks, $$x = (x_1,\dots,x_B) \in \mathbb{R}^n, \text{ where } x_i \in \mathbb{R}^{n_i}$$, and the matrix $$A$$ is likewise split into $$B$$ column blocks, $$A = [A_1, \dots, A_B], \text{ where } A_i \in \mathbb{R}^{m \times n_i}$$. Then, for a fixed $$u$$, the minimization over $$x$$ separates into $$B$$ independent problems:
> $$
> \begin{alignat}{1}
> & \quad x^+ \in \arg\min_x \sum_{i=1}^B f_i(x_i) + u^T Ax  \\
> \Longleftrightarrow & \quad x_i^+ \in \arg\min_{x_i} f_i(x_i) + u^T A_ix_i, \quad i=1,\dots, B
> \end{alignat}
> $$

### Dual decomposition algorithm:

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right)
> \end{alignat}
> $$

The two steps above can be read as follows.
* The first equation is the **broadcast** step: the current $$u$$ is sent to each of the $$B$$ processors, and each processor finds its own optimal $$x_i$$ in parallel.
* The second equation is the **gather** step: $$A_i x_i$$ is collected from each processor and the global dual variable $$u$$ is updated.

The two steps are repeated for $$k=1,2,3,\dots$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter20/decomposition.png" alt="[Fig 1] Broadcast and Gather" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Broadcast and Gather</figcaption>
</p>
</figure>

### Dual decomposition in 18 seconds

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/dual-decomposition_en.mp4"></video>
</div>

Each agent solves its own small problem given a price $$\nu$$, and dual ascent raises or lowers $$\nu$$ according to the constraint violation $$\sum_i x_i-c$$.

### Try it yourself: set the price

<div class="opx-explainer" data-opx="dd" data-lang="en"></div>

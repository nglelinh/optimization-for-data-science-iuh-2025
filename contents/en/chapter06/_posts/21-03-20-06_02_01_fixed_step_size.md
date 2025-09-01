---
layout: post
title: 06-02-01 Fixed step size
chapter: '06'
order: 4
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

The simplest way to choose the step size in gradient descent is to use a fixed value for all iterations: $$t_k = t$$ for $$k = 1, 2, 3, ...$$. However, the convergence and behavior depend heavily on the choice of $$t$$.

For example, in the figure below, gradient descent is applied to $$f(x) = (10 x_1^2 + x_2^2) / 2$$ with different step sizes:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_02_01_gradientdescent4.png" alt="gradientdescent4" width="100%" height="100%">
  <figcaption style="text-align: center;">[Fig 1] Step size scenarios [3]</figcaption>
</p>
</figure>

* In case A, the step size $$t$$ is too large, causing divergence after 8 steps. The minimum cannot be reached.
* In case B, the step size $$t$$ is too small, so convergence is very slow and the minimum is not reached even after 100 steps.
* In case C, the step size is "appropriate," and convergence is achieved in about 40 steps. (How to find this "appropriate" value is discussed later in this chapter.)

---
layout: post
title: '08-02-04 Batch vs Stochastic Methods'
chapter: '08'
order: 15
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

The convergence properties of batch and stochastic methods are as follows:

Generally, the stochastic method quickly approaches the optimal point in the early stages, but may not converge as well near the optimal point. In contrast, the batch method converges more slowly but approaches the optimal point more accurately.

The figure below compares the convergence of batch and stochastic methods for [logistic regression](https://en.wikipedia.org/wiki/Logistic_regression) (without regularization):

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_02_stochastic_vs_batch.png" alt="stochastic_vs_batch" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Fig 3] Batch vs Stochastic Gradient Descent [2]</figcaption>
</figure>

When each $$f_i$$ is smooth, the leftover jitter of the stochastic curve near the optimum is exactly the noise floor that [26-05 SVRG and SAGA]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %}) removes — without paying a full-batch gradient at every step.

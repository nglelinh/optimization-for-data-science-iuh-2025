---
layout: post
title: '08-02-03 Convergence Rate of Stochastic Method'
chapter: '08'
order: 14
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

There are differences in the convergence rates between cyclic and randomized methods.

The [convergence rate]({% multilang_post_url contents/chapter08/20-03-29-08_01_04_convergence_rate %}) of the batch subgradient method is $$O(G_{batch}^{2}/\epsilon^{2})$$, where $$G_{batch}$$ is the Lipschitz constant of $$\sum f_i$$.

- **Cyclic method**: The iteration complexity of the cyclic method is $$O(m^{3}G^{2}/\epsilon^{2})$$. If one cycle of the cyclic stochastic subgradient method is considered equivalent to one batch subgradient method, then each cycle requires $$O(m^{2}G^{2}/\epsilon^{2})$$ iterations. ($$G$$ is the Lipschitz constant of a single function $$f_i$$)

- **Randomized method**: The iteration complexity of the randomized method is $$O(m^{2}G^{2}/\epsilon^{2})$$. That is, the randomized method requires $$O(mG^{2}/\epsilon^2)$$ iterations, which is $$m$$ times faster than the batch and cyclic methods with $$O(m^2G^2/\epsilon^2)$$. In terms of Big-O notation, if $$m$$ is large, the randomized method has a faster convergence rate.

Although the Big-O bounds for randomized and cyclic methods differ by a factor of $$m$$, note that the cyclic method's Big-O bound is worst-case, while the randomized method's is average-case. In practice, the difference may not be as large as the Big-O notation suggests.

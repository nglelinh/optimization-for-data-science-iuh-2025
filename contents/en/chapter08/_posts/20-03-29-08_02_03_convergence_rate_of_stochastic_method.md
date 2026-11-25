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

A subtle and famous surprise awaits anyone who compares cyclic versus randomized stochastic subgradient methods in terms of $$m$$ (the number of data points): while both share the same $$O(1/\varepsilon^2)$$ dependence on accuracy $$\varepsilon$$, the randomized method saves a full factor of $$m$$ in worst-case complexity over the cyclic method! That extra factor of $$m$$ is not a mere proof artifact—adversarial data orderings genuinely slow cyclic updates down by a factor of $$m$$, whereas random shuffling cancels out correlated errors by the law of large numbers.

## Key ideas: Complexity Scaling in $$m$$, $$G$$, and $$\varepsilon$$

- **Pillar 1 — Batch Subgradient Benchmark:** Using $$G_{\text{batch}} \le mG$$, the batch method takes $$O(G_{\text{batch}}^2 / \varepsilon^2) \le O(m^2 G^2 / \varepsilon^2)$$ batch iterations. Because each batch iteration evaluates all $$m$$ components, total component evaluations scale as $$O(m^3 G^2 / \varepsilon^2)$$ in the worst case.
- **Pillar 2 — Cyclic Method Complexity ($$O(m^3 G^2 / \varepsilon^2)$$ updates):** An adversarial ordering (e.g., putting all $$+1$$ subgradients first and all $$-1$$ subgradients last) creates $$O(m)$$ coherent drift within each cycle. Counting individual steps gives $$O(m^3 G^2 / \varepsilon^2)$$, or $$O(m^2 G^2 / \varepsilon^2)$$ full cycles—matching the worst-case batch evaluation count.
- **Pillar 3 — Randomized Method Complexity ($$O(m^2 G^2 / \varepsilon^2)$$ updates):** Because independent random draws have zero cross-term covariance, the expected squared norm of the step noise does not accumulate coherently across $$m$$ steps, saving a full factor of $$m$$ in component evaluations (equivalent to $$O(m G^2 / \varepsilon^2)$$ passes over the data).
- **Pillar 4 — Normalized Average Objective ($$\frac{1}{m}\sum f_i$$):** Dividing the objective by $$m$$ rescales $$\varepsilon \mapsto m\varepsilon$$, turning the randomized complexity into $$O(G^2 / \varepsilon^2)$$ component evaluations—completely *independent of the dataset size $$m$$*!

### Worked example: Why Adversarial Ordering Hurts Cyclic Updates

Consider $$f(x) = \sum_{i=1}^{2k} f_i(x)$$ with $$m = 2k$$ terms where the first $$k$$ terms are $$f_i(x) = +x$$ and the last $$k$$ terms are $$f_i(x) = -x$$ (so $$f(x) \equiv 0$$ and every $$x$$ is optimal, with $$G = 1$$). Start at $$x^{(0)} = 0$$ with step size $$t$$.

1. **Cyclic ordering (all $$+x$$ first, then all $$-x$$):**
   - After the first $$k = m/2$$ steps, every subgradient is $$+1$$, so $$x^{(k)} = 0 - k t = -\frac{m}{2} t$$.
   - The peak displacement from $$x^{(0)}$$ is $$\left|x^{(k)} - x^{(0)}\right| = \frac{m}{2} t$$, and the squared displacement scales as $$\Theta(m^2 t^2)$$.
   - Over the remaining $$k$$ steps, all subgradients are $$-1$$, returning to $$x^{(2k)} = 0$$, but the huge intermediate drift $$\Theta(m t)$$ injects $$\Theta(m^2 G^2 t)$$ bias whenever $$f_i$$ is nonlinear.
2. **Randomized ordering ($$i_j$$ uniform in $$\{1, \dots, 2k\}$$):**
   - Each step adds $$\pm t$$ independently with probability $$1/2$$ (a 1D symmetric random walk).
   - After $$k = m/2$$ steps, the expected squared displacement is only $$\mathbb{E}[(x^{(k)} - x^{(0)})^2] = k t^2 = \frac{m}{2} t^2$$—smaller by a full factor of $$m/2$$!
   - Typical drift is $$O(\sqrt{m}\, t)$$ instead of $$O(m\, t)$$, directly illustrating where the $$m\times$$ speedup of randomized stochastic subgradient comes from.

There are differences in the convergence rates between cyclic and randomized methods.

The [convergence rate]({% multilang_post_url contents/chapter08/20-03-29-08_01_04_convergence_rate %}) of the batch subgradient method is $$O(G_{batch}^{2}/\epsilon^{2})$$, where $$G_{batch}$$ is the Lipschitz constant of $$\sum f_i$$.

- **Cyclic method**: The iteration complexity of the cyclic method is $$O(m^{3}G^{2}/\epsilon^{2})$$. If one cycle of the cyclic stochastic subgradient method is considered equivalent to one batch subgradient method, then each cycle requires $$O(m^{2}G^{2}/\epsilon^{2})$$ iterations. ($$G$$ is the Lipschitz constant of a single function $$f_i$$)

- **Randomized method**: The iteration complexity of the randomized method is $$O(m^{2}G^{2}/\epsilon^{2})$$. That is, the randomized method requires $$O(mG^{2}/\epsilon^2)$$ iterations, which is $$m$$ times faster than the batch and cyclic methods with $$O(m^2G^2/\epsilon^2)$$. In terms of Big-O notation, if $$m$$ is large, the randomized method has a faster convergence rate.

Although the Big-O bounds for randomized and cyclic methods differ by a factor of $$m$$, note that the cyclic method's Big-O bound is worst-case, while the randomized method's is average-case. In practice, the difference may not be as large as the Big-O notation suggests.

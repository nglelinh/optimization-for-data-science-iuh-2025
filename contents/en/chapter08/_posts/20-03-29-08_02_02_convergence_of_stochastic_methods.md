---
layout: post
title: '08-02-02 Convergence of Stochastic Methods'
chapter: '08'
order: 13
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

Does a noisy, one-sample-at-a-time subgradient loop actually converge to the true minimizer of the full sum, or does the constant tug-of-war between conflicting data points trap it forever? Remarkably, the exact same qualitative dichotomy from deterministic subgradient optimization reappears—only with a sharper dependence on the number of terms $$m$$ and an extra factor of $$5$$ in the fixed-step error neighborhood. This lesson states the core convergence theorems for both cyclic and randomized stochastic subgradient methods.

## Key ideas: Convergence Guarantees Under Sampling Noise

- **Pillar 1 — Componentwise $$G$$-Lipschitz Continuity:** Assuming each individual term $$f_i$$ is $$G$$-Lipschitz ($$\|g_i\|_2 \le G$$) implies the full sum $$f = \sum_{i=1}^m f_i$$ is at most $$mG$$-Lipschitz. The factor $$m^2 G^2$$ in the error floor directly reflects the worst-case disagreement among $$m$$ components.
- **Pillar 2 — Fixed-Step Error Floor ($$5 m^2 G^2 t / 2$$):** With constant step size $$t$$, both cyclic and randomized methods satisfy $$\lim_{k \to \infty} f(x_{\text{best}}^{(k)}) \le f^\star + \frac{5 m^2 G^2 t}{2}$$ (in expectation for the randomized variant). The larger constant compared to batch ($$G_{\text{batch}}^2 t / 2$$) accounts for drift *within* a cycle of $$m$$ updates.
- **Pillar 3 — Exact Asymptotic Convergence via Diminishing Steps:** Under the Robbins–Monro conditions $$\sum t_k = \infty$$ and $$\sum t_k^2 < \infty$$, the intra-cycle drift and stochastic variance both vanish asymptotically, guaranteeing $$f(x_{\text{best}}^{(k)}) \to f^\star$$ (with probability 1 / in expectation for randomized selection).
- **Pillar 4 — Expectation vs. Deterministic Guarantees:** Cyclic methods yield deterministic bounds across full epochs, whereas randomized methods bound $$\mathbb{E}[f(x_{\text{best}}^{(k)})]$$ (and converge almost surely by supermartingale convergence).

### Worked example: Quantifying the Fixed-Step Noise Floor as $$m$$ Grows

Suppose $$f(x) = \sum_{i=1}^m f_i(x)$$ where each $$f_i$$ has Lipschitz constant $$G = 1$$, and we compare $$m = 10$$ vs. $$m = 100$$ components using a fixed step size $$t$$.

1. **Evaluate the guaranteed error floor for $$m = 10$$ and $$t = 10^{-3}$$:**
   $$\frac{5 m^2 G^2 t}{2} = \frac{5 \cdot 10^2 \cdot 1^2 \cdot 10^{-3}}{2} = \frac{500 \cdot 10^{-3}}{2} = 0.25.$$
2. **Evaluate the same step size $$t = 10^{-3}$$ when $$m = 100$$:**
   $$\frac{5 m^2 G^2 t}{2} = \frac{5 \cdot 100^2 \cdot 1^2 \cdot 10^{-3}}{2} = \frac{50{,}000 \cdot 10^{-3}}{2} = 25.0.$$
   Because the unnormalized sum $$f = \sum_{i=1}^m f_i$$ grows linearly with $$m$$ and its squared Lipschitz constant grows like $$m^2$$, keeping $$t$$ fixed inflates the error floor by $$100\times$$!
3. **Rescale $$t$$ to keep the per-sample average error $$\frac{1}{m}(f - f^\star) \le 0.025$$:**
   We need $$\frac{5 m G^2 t}{2} \le 0.025 \implies t \le \frac{0.05}{5 m G^2} = \frac{0.01}{m}$$.
   - For $$m = 10$$: $$t \le 10^{-3}$$.
   - For $$m = 100$$: $$t \le 10^{-4}$$.
   This hand calculation explains a universal rule of thumb in practice: when optimizing an unnormalized sum of $$m$$ losses, the step size must scale inversely with $$m$$ (or equivalently, optimize the average $$\frac{1}{m}\sum f_i$$).

Assume each function $$f_i, i = 1,...,m$$ is convex and Lipschitz continuous with constant G.

For the stochastic subgradient method, the following properties hold for fixed and diminishing step sizes:

- **Fixed step sizes** for $$t_k = t$$, $$k = 1, 2, 3, ...$$

>$$\text{For cyclic and randomized methods with fixed step sizes, the following holds:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) \le f^{*} + 5m^{2}G^{2}t/2
\end{align}
$$

Here, $$mG$$ is the Lipschitz constant of $$\sum_{i=1}^{m} f_i$$.

- **Diminishing step sizes**

>$$\text{For cyclic and randomized methods with diminishing step sizes, the following holds:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) = f^{*}
\end{align}
$$


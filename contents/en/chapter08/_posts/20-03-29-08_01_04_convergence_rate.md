---
layout: post
title: '08-01-04 Convergence rate'
chapter: '08'
order: 6
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

Knowing that an algorithm eventually converges is reassuring in theory, but in engineering practice the decisive question is: *how many iterations will it take to get within $$\varepsilon = 10^{-3}$$ of the optimum?* In smooth gradient descent, cutting $$\varepsilon$$ by a factor of $$10$$ costs $$10\times$$ more iterations ($$O(1/\varepsilon)$$); in the subgradient method, cutting $$\varepsilon$$ by a factor of $$10$$ costs $$100\times$$ more iterations ($$O(1/\varepsilon^2)$$). This lesson derives that famous quadratic penalty directly from the basic inequality and shows why it is not a flaw in our proof, but a fundamental speed limit of nonsmooth geometry.

## Background Knowledge Map: Deriving the $$O(1/\varepsilon^2)$$ Complexity Barrier

- **Pillar 1 — Optimizing the Fixed Step Size for a Known Horizon $$k$$:** Minimizing $$B(t) = \frac{R^2}{2kt} + \frac{G^2 t}{2}$$ over $$t > 0$$ by setting $$B'(t) = 0$$ yields the optimal horizon-dependent step $$t^\star = \frac{R}{G\sqrt{k}}$$ and the tightest upper bound $$f_{\text{best}}^{(k)} - f^\star \le \frac{RG}{\sqrt{k}}$$.
- **Pillar 2 — Translating Error Bound to Iteration Complexity:** Setting $$\frac{RG}{\sqrt{k}} \le \varepsilon$$ and solving for $$k$$ gives $$k \ge \frac{R^2 G^2}{\varepsilon^2}$$. Every extra decimal digit of accuracy multiplies the iteration budget by $$100$$.
- **Pillar 3 — Horizon-Free $$1/\sqrt{k}$$ Schedules:** When the total number of iterations $$k$$ is unknown in advance, choosing $$t_i = \frac{R}{G\sqrt{i}}$$ (which is *not* square-summable, yet $$\sum_{i=1}^k 1/i \approx \ln k$$ while $$\sum_{i=1}^k 1/\sqrt{i} \approx 2\sqrt{k}$$) still achieves $$O\!\left(\frac{\ln k}{\sqrt{k}}\right)$$, far faster than $$t_i = 1/i$$ which gives only $$O(1/\ln k)$$.
- **Pillar 4 — Information-Theoretic Lower Bound (Nesterov / Nemirovski–Yudin):** For high-dimensional nonsmooth convex functions ($$n \ge k$$), *no* first-order black-box method using only subgradients can beat $$\Omega(RG/\sqrt{k})$$ in the worst case—so to go faster, one must exploit extra problem structure.

### Step-by-Step Worked Example (Read Slowly): Optimizing $$t$$ and Counting Iterations for $$\varepsilon = 0.01$$

Suppose $$R = 5$$ and $$G = 2$$, and we want to guarantee $$f_{\text{best}}^{(k)} - f^\star \le \varepsilon$$.

1. **Derive the optimal constant step size for a fixed budget $$k$$:**
   $$\frac{d}{dt}\left(\frac{R^2}{2kt} + \frac{G^2 t}{2}\right) = -\frac{R^2}{2kt^2} + \frac{G^2}{2} = 0 \implies t^\star = \frac{R}{G\sqrt{k}} = \frac{5}{2\sqrt{k}}.$$
2. **Substitute $$t^\star$$ back into the bound:**
   $$f_{\text{best}}^{(k)} - f^\star \le \frac{R^2}{2k \cdot \frac{R}{G\sqrt{k}}} + \frac{G^2}{2} \cdot \frac{R}{G\sqrt{k}} = \frac{RG}{2\sqrt{k}} + \frac{RG}{2\sqrt{k}} = \frac{RG}{\sqrt{k}} = \frac{10}{\sqrt{k}}.$$
3. **Compute iterations needed for $$\varepsilon = 0.1$$ vs. $$\varepsilon = 0.01$$:**
   - For $$\varepsilon = 0.1$$: $$\frac{10}{\sqrt{k}} \le 0.1 \implies \sqrt{k} \ge 100 \implies k = 10{,}000$$ iterations, with $$t^\star = \frac{5}{2 \cdot 100} = 0.025$$.
   - For $$\varepsilon = 0.01$$: $$\frac{10}{\sqrt{k}} \le 0.01 \implies \sqrt{k} \ge 1000 \implies k = 1{,}000{,}000$$ iterations, with $$t^\star = \frac{5}{2 \cdot 1000} = 0.0025$$.
4. **Contrast with smooth gradient descent ($$O(1/\varepsilon)$$):** Improving accuracy $$10\times$$ (from $$0.1$$ to $$0.01$$) multiplied the subgradient budget by $$100\times$$ (from $$10^4$$ to $$10^6$$), explaining why subgradient methods excel at low-to-medium precision and struggle at high precision.

The convergence rate describes how the number of iterations required to reach an $$\epsilon$$-suboptimal point depends on $$\epsilon$$, using [Big-O notation](https://en.wikipedia.org/wiki/Big_O_notation). For example, if $$\epsilon = 10^{-2}$$ and the convergence rate is $$O(1/\epsilon)$$, then about $$1/10^{-2}=10^2$$ iterations are needed.

Let’s use [08-01-02 Basic inequality]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) to derive the convergence rate for the subgradient method with fixed step sizes.

>$$Recall:$$
>\begin{align}
> f^{k}_{best} - f^{*} \quad \le \quad \frac{R^{2}}{2kt} + \frac{G^{2}t}{2}
\end{align}

Suppose $$\epsilon$$ satisfies $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ and $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$ (where $$\epsilon$$ is the suboptimality gap, $$G$$ is the Lipschitz constant, and $$R$$ is the distance between the starting point and the optimal point). Then $$ \frac{R^{2}}{2kt} + \frac{G^{2}t}{2} \le \epsilon$$. If $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$, then $$t \le \frac{\epsilon}{G^{2}}$$, and $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ leads to $$\frac{R^2G^2}{\epsilon^2} \le k$$. This means the number of iterations required is at least $$\frac{R^2G^2}{\epsilon^2}$$ to achieve $$f^{k}_{best} - f^{*} \le \epsilon$$.

The convergence rate of this algorithm is $$O(1/\epsilon^2)$$, which means it requires significantly more iterations than the gradient descent method, which has a rate of $$O(1/\epsilon)$$.
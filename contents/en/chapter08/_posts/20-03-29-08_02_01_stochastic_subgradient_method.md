---
layout: post
title: '08-02-01 Stochastic Subgradient Method'
chapter: '08'
order: 12
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

Replacing a full dataset sweep with a single data point turns every iteration into a quick, noisy tug in one component's direction. To analyze and implement this cleanly, we distinguish two classic index-selection rules: the **cyclic** (incremental) method, which marches through $$i = 1, 2, \dots, m$$ in fixed order, and the **randomized** method, which draws $$i_k$$ uniformly at random at every step. This lesson formalizes both updates side by side and prepares the ground for comparing their convergence guarantees.

## Key ideas: Cyclic vs. Randomized Incremental Updates

- **Pillar 1 — Additive Subdifferential Decomposition:** For convex functions $$f_1, \dots, f_m$$ on $$\mathbb{R}^n$$, $$\partial\left(\sum_{i=1}^m f_i\right)(x) = \sum_{i=1}^m \partial f_i(x)$$. A batch step evaluates all $$m$$ components at the *same* point $$x^{(k-1)}$$, whereas incremental methods update $$x$$ after *every* single component.
- **Pillar 2 — Cyclic (Incremental) Subgradient Rule:** Choosing $$i_k = ((k - 1) \bmod m) + 1$$ guarantees that every component $$f_i$$ is visited exactly once per pass (epoch) of $$m$$ steps, making it natural for sequential disk reads, though vulnerable to poorly ordered data.
- **Pillar 3 — Randomized Subgradient Rule:** Drawing $$i_k \sim \operatorname{Uniform}\{1, \dots, m\}$$ independently at each step breaks worst-case data orderings and makes $$m g_{i_k}^{(k-1)}$$ an unbiased estimator of a full subgradient, simplifying expectation-based convergence proofs.
- **Pillar 4 — Epoch-Level Interpretation:** One full pass of $$m$$ stochastic steps performs roughly the same arithmetic work as $$1$$ batch subgradient step, so fair comparisons always measure progress per *epoch* (effective data passes) rather than per raw update.

### Worked example: One Full Cyclic Epoch on a 3-Term Absolute-Deviation Problem

Minimize $$f(x) = |x - 1| + |x - 2| + |x - 6|$$ (the median minimizer is $$x^\star = 2$$, with $$f^\star = 1 + 0 + 4 = 5$$). Start at $$x^{(0)} = 0$$ with fixed step size $$t = 0.5$$ and cyclic order $$i = 1, 2, 3$$.

1. **Step 1 ($$f_1(x) = |x - 1|$$ at $$x^{(0)} = 0$$):**
   - Since $$0 < 1$$, $$g_1(0) = -1$$.
   - $$x^{(1)} = 0 - 0.5(-1) = 0.5$$.
2. **Step 2 ($$f_2(x) = |x - 2|$$ at $$x^{(1)} = 0.5$$):**
   - Since $$0.5 < 2$$, $$g_2(0.5) = -1$$.
   - $$x^{(2)} = 0.5 - 0.5(-1) = 1.0$$.
3. **Step 3 ($$f_3(x) = |x - 6|$$ at $$x^{(2)} = 1.0$$):**
   - Since $$1.0 < 6$$, $$g_3(1.0) = -1$$.
   - $$x^{(3)} = 1.0 - 0.5(-1) = 1.5$$.
4. **Compare after 1 epoch (3 component evaluations):**
   - Cyclic incremental moved from $$x^{(0)} = 0$$ ($$f(0) = 9$$) to $$x^{(3)} = 1.5$$ ($$f(1.5) = 0.5 + 0.5 + 4.5 = 5.5$$), cutting the suboptimality gap from $$4.0$$ down to $$0.5$$!
   - A batch step from $$x^{(0)} = 0$$ with $$t = 0.5$$ uses $$g(0) = -1 - 1 - 1 = -3$$, landing at $$x^{(1)}_{\text{batch}} = 0 - 0.5(-3) = 1.5$$—identical here because all three components had the same sign, whereas once $$x$$ crosses $$1$$, the incremental method immediately feels the sign flip on $$f_1$$ mid-epoch.

Let’s consider the problem of minimizing the sum of functions as follows:

>$$
\begin{equation}
\min_x \sum_{i=1}^m f_i(x)
\end{equation}
$$

If we apply the subgradient method to this problem, we need to compute the subgradient for each function $$f_i$$ and sum them. (This is similar to the method introduced in [stochastic gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %})).

In summary, the stochastic subgradient method takes the following form:

>$$
\begin{align}
x^{(k)} = x^{(k-1)} - t_k \cdot g_{i_k}^{(k-1)}, \quad k = 1, 2, 3, . . . 
\end{align}
$$

Here, $$i_k \in \{1,...,m\}$$ is the index chosen at the $$k$$-th iteration. As will be discussed in the next section on the convergence rate of the stochastic subgradient method, the choice of cyclic or random method affects the result. $$g_{i}^{(k-1)} \in \partial f_{i}(x^{k-1})$$, and this update direction is different from the usual [subgradient method]({% multilang_post_url contents/chapter08/20-03-29-08_01_subgradient_method %}) (also called batch subgradient method or full batch subgradient method), where $$\sum_{i=1}^{m} g_i^{(k-1)}$$ is used.

If each $$f_i, i = 1,...,m$$ is differentiable, this algorithm becomes stochastic gradient descent. (The stochastic subgradient method is a more general form)
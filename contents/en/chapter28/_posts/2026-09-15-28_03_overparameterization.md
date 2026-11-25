---
layout: post
title: 28-03 Overparameterization
chapter: '28'
order: 4
owner: Nguyen Le Linh
categories:
- chapter28
lang: en
lesson_type: required
---

Classical statistics taught a golden rule: never let the number of parameters $$d$$ exceed the number of training examples $$n$$, or your model will memorize noise and collapse on test data. Modern deep learning routinely violates that rule by factors of $$100\times$$—and somehow becomes *easier* to optimize and *better* at generalizing! Overparameterization ($$d \gg n$$) fundamentally transforms the loss landscape: instead of isolated local valleys, the zero-loss set becomes a vast $$(d - n)$$-dimensional manifold, and gradient descent implicitly picks out the **minimum-norm** interpolating solution.

## Key ideas: Geometry and Implicit Bias of Overparameterized Models

- **Interpolation Manifold ($$d > n$$):** In an underdetermined linear system $$Xw = y$$ ($$X \in \mathbb{R}^{n \times d}$$ full row rank, $$d > n$$), there are infinitely many exact global minimizers forming an affine subspace of dimension $$d - n$$, all achieving $$F(w) = 0$$.
- **Implicit Bias of Gradient Descent:** Even with zero explicit $$\ell_2$$ regularization, running gradient descent from $$w_0 = 0$$ keeps every iterate strictly inside $$\operatorname{row}(X) = \operatorname{span}(X^\top)$$. Because the *unique* interpolator inside $$\operatorname{row}(X)$$ is the minimum-$$\ell_2$$-norm solution $$w_{\text{min}} = X^\top(XX^\top)^{-1} y$$, GD automatically acts as a hidden regularizer!
- **Lazy Training / Neural Tangent Kernel (NTK) Regime:** In ultra-wide neural networks, each weight moves only $$O(1/\sqrt{\text{width}})$$ from initialization, so the network stays well-approximated by its first-order Taylor expansion in $$w$$—turning nonconvex training into convex kernel regression!
- **Feature Learning vs. Lazy Regime:** Practical deep networks operate beyond the pure NTK limit, moving weights far enough to learn task-adaptive representations while still retaining the landscape smoothness granted by overparameterization.

### Worked example: Watching GD Find the Minimum-Norm Interpolator

Consider an overparameterized 1-example, 2-parameter linear model ($$n = 1, d = 2$$): $$X = \begin{pmatrix} 1 & 2 \end{pmatrix}$$, $$y = 5$$, minimizing $$F(w) = \frac{1}{2}(w_1 + 2 w_2 - 5)^2$$.

1. **Describe the infinite manifold of zero-loss solutions:** Every point on the line $$w_1 + 2 w_2 = 5$$ achieves $$F(w) = 0$$ (e.g., $$(5, 0)$$, $$(1, 2)$$, $$(-5, 5)$$, all have zero training loss!).
2. **Trace Gradient Descent starting from $$w^{(0)} = (0, 0)^\top$$:**
   - At any $$w$$, the gradient is $$\nabla F(w) = (w_1 + 2 w_2 - 5)\begin{pmatrix} 1 \\ 2 \end{pmatrix}$$.
   - Notice every single gradient is a scalar multiple of $$(1, 2)^\top$$! Therefore, for *every* step $$k$$, $$w^{(k)} = \alpha_k (1, 2)^\top$$.
3. **Find the exact GD limit:** Imposing $$w_1 + 2 w_2 = 5$$ on $$w = \alpha (1, 2)^\top$$ gives
   $$\alpha + 2(2\alpha) = 5 \implies 5\alpha = 5 \implies \alpha = 1 \implies w^{\text{GD}} = (1, 2)^\top.$$
4. **Verify minimum Euclidean norm:**
   - $$\|w^{\text{GD}}\|_2^2 = 1^2 + 2^2 = 5$$.
   - Compare with other zero-loss interpolators: $$\|(5, 0)\|_2^2 = 25$$, $$\|(3, 1)\|_2^2 = 10$$, $$\|(-5, 5)\|_2^2 = 50$$.
   Without ever adding $$\lambda \|w\|_2^2$$ to the loss, GD from $$w^{(0)} = 0$$ **automatically** converged to the unique minimum-norm interpolator $$(1, 2)^\top$$!

A model is **overparameterized** when the number of parameters $$d$$ substantially exceeds the number of effective constraints coming from the data (classically $$d \gg n$$ for interpolating $$n$$ scalar labels). Then the equation $$F(w)=0$$ (or “train loss $$\approx 0$$”) can have a **huge set** of solutions. Training is no longer “find the unique minimizer”; it is “which interpolator does the algorithm pick?”

That is the implicit-bias viewpoint: gradient descent on an underdetermined least-squares problem converges to the **min-norm** interpolator in the span of the features; on separable linear classification it maximizes the margin in the limit (Soudry et al., and a large follow-up literature). Deep nets are not linear, but the slogan remains: **the optimizer is part of the inductive bias**.

Overparameterization also changes the *shape* of $$F$$. In many random-feature and wide-net limits the loss becomes *locally* benign: once you are close enough, every critical point that SGD finds interpolates, and saddles become less relevant than **which** interpolating point you land on. This is why “nonconvex ⇒ unusable local minima” is the wrong slogan for modern deep learning, even though the function is still nonconvex.

**Polyak–Łojasiewicz (PL) condition** (pointer, not a full lecture). If

$$
\tfrac12 \|\nabla F(w)\|_2^2 \ge \mu \bigl(F(w)-F^\star\bigr)
$$

for some $$\mu>0$$, then gradient descent enjoys a linear rate *without convexity*. Some overparameterized least-squares and certain wide-net regimes satisfy PL locally. The optional lesson [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}) reuses the Chapter 06 proof on that inequality (Karimi, Nutini, Schmidt, [arXiv:1608.04636](https://arxiv.org/abs/1608.04636)); this page only needs the slogan.

**Exercise.** Fit $$n=20$$ scalar points with a degree-$$50$$ polynomial by (i) the numpy least-squares min-norm solution and (ii) GD from two random starts. Compare test error on a smooth underlying function. Same train loss, different interpolators.

---
layout: post
title: 07 Subgradient
chapter: '07'
order: 1
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---

Smooth curves are comfortable, but the most powerful models in modern data science are full of sharp corners: the kink of $$|x|$$ at zero in Lasso, the hinge of $$\max(0, 1 - z)$$ in SVMs, the bend of $$\mathrm{ReLU}(z) = \max(0, z)$$ in every deep neural network, and the hard walls of constrained sets. Ordinary derivatives shatter at every corner. Chapter 07 introduces the **subgradient**—the exact geometric generalization of the derivative that keeps global optimality alive even when functions have kinks!

## Background Knowledge Map: Navigating Nonsmooth Convex Analysis

1. **Supporting Hyperplanes Replace Tangent Planes**: Where a smooth convex function has one unique tangent hyperplane (defined by $$\nabla f(x)$$), a convex function at a kink admits an entire fan of *supporting hyperplanes* staying globally below its graph: $$f(y) \ge f(x) + g^T(y - x)$$ for all $$y$$. Every such slope vector $$g$$ is a **subgradient**.
2. **The Subdifferential $$\partial f(x)$$**: Collecting all subgradients at $$x$$ forms a closed, convex set $$\partial f(x)$$. At differentiable points, $$\partial f(x) = \{\nabla f(x)\}$$ is a singleton; at kinks, $$\partial f(x)$$ is a convex hull of active slopes (such as $$[-1, 1]$$ for $$|x|$$ at $$0$$).
3. **Subgradient Calculus & Normal Cones**: Rules for scaling, addition, affine composition, and pointwise maxima let you compute $$\partial f(x)$$ algebraically without returning to the definition. Even constraints fit inside this framework: the subdifferential of the set indicator $$I_C(x)$$ is the *normal cone* $$N_C(x)$$.
4. **Universal Optimality ($$0 \in \partial f(x^\star)$$)**: Replacing $$\nabla f(x^\star) = 0$$ with $$0 \in \partial f(x^\star)$$ gives a necessary and sufficient condition for global optimality of *any* convex function—unlocking closed-form soft-thresholding for Lasso, optimality for SVMs, and modern nonsmooth automatic differentiation.

### Step-by-Step Worked Example (Read Slowly): Finding a Minimum at a Non-Differentiable Kink

Minimize the nonsmooth convex function $$f(x) = |x - 2| + \frac{1}{2}x^2$$ over $$x \in \mathbb{R}$$.

1. **Compute the subdifferential $$\partial f(x)$$ everywhere** using the sum rule $$\partial(f_1 + f_2) = \partial f_1 + \partial f_2$$:
   - For $$x > 2$$: $$f'(x) = 1 + x$$ (unique slope).
   - For $$x < 2$$: $$f'(x) = -1 + x$$ (unique slope).
   - At the kink $$x = 2$$: $$\partial |x - 2|\big|_{x=2} = [-1, 1]$$, so $$\partial f(2) = [-1, 1] + 2 = [1, 3]$$.
2. **Test the universal optimality condition $$0 \in \partial f(x^\star)$$**:
   - At $$x = 2$$: $$0 \notin [1, 3]$$, so the minimum is *not* at the kink.
   - For $$x > 2$$: $$1 + x > 3 > 0$$, never zero.
   - For $$x < 2$$: $$-1 + x = 0 \implies x^\star = 1 < 2$$!
3. **Now shift the kink to $$x = 0.5$$**: minimize $$h(x) = |x - 0.5| + \frac{1}{2}x^2$$.
   - At $$x = 0.5$$: $$\partial h(0.5) = [-1, 1] + 0.5 = [-0.5,\; 1.5]$$.
   - Since $$0 \in [-0.5, 1.5]$$, the global minimizer lands **right on the kink** $$x^\star = 0.5$$—something ordinary calculus $$h'(x) = 0$$ could never even express!

In this chapter, we introduce the concept of subgradient and subgradient optimality conditions, which generalize the gradient and first-order optimality conditions discussed previously. We also explore several applications and examples related to these concepts.

## Modern applications (2022–2026)

An optional companion lesson maps the same subdifferential objects onto recent CS / data-science pipelines — ReLU autodiff, glmnet / skglm Lasso paths, and pinball + conformal quantiles — without changing the theory below. See [07-08 Modern applications of the subgradient]({% multilang_post_url contents/chapter07/2026-09-16-07_08_modern_applications %}).

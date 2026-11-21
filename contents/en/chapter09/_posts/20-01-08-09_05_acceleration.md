---
layout: post
title: '09-05 Acceleration'
chapter: '09'
order: 6
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

# Acceleration

Proximal gradient descent on a composite problem $$\min_x g(x)+h(x)$$ already has a clean rate $$O(1/k)$$ when $$\nabla g$$ is Lipschitz (lesson 09-02). **Acceleration** is the extra memory that upgrades that rate to the optimal first-order $$O(1/k^2)$$ on smooth convex $$g$$, without forming a Hessian. This page is the Distill-style *picture* that sits in front of the FISTA algebra. The algorithm and the $$O(1/k^2)$$ proof live in [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %}) and [09-05-02]({% multilang_post_url contents/chapter09/20-01-08-09_05_02_convergence_analysis %}); the stochastic, constant-$$\beta$$ cousin used to train nets is [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %}).

## Why a plain proximal step zig-zags

Write a proximal gradient step as “take a gradient step on the smooth piece, then snap back with $$\operatorname{prox}_{t h}$$.” When $$h=0$$ this is ordinary gradient descent, and the classroom counter-example is again the long valley $$g(x)=\tfrac12 x^\top\operatorname{diag}(1,L)\,x$$. A step small enough not to bounce off the sharp wall crawls down the floor. Momentum — the idea Nesterov introduced for smooth convex problems in 1983, and that Beck–Teboulle (2009) wrapped around a proximal map as **FISTA** — stores the *previous* position and extrapolates before the prox.

The FISTA look-ahead of 09-05-01 is

$$
\begin{align}
v^{(k)} &= x^{(k-1)}+\frac{k-2}{k+1}\bigl(x^{(k-1)}-x^{(k-2)}\bigr),\\
x^{(k)} &= \operatorname{prox}_{t_k h}\bigl(v^{(k)}-t_k\nabla g(v^{(k)})\bigr).
\end{align}
$$

The weight $$(k-2)/(k+1)$$ starts at zero (the first step *is* proximal gradient) and climbs toward $$1$$. That schedule is not a tasteful default; it is the discrete analogue of the continuous-time damping that makes Nesterov’s $$O(1/k^2)$$ proof close. Goh’s Distill essay *[Why Momentum Really Works](https://distill.pub/2017/momentum/)* is the same geometry without the prox: a second-order recurrence whose characteristic roots can be placed on a circle of radius $$(\sqrt{\kappa}-1)/(\sqrt{\kappa}+1)$$, turning a $$1-\Theta(1/\kappa)$$ crawl into a $$1-\Theta(1/\sqrt{\kappa})$$ glide.

## Nesterov versus “PyTorch Nesterov”

Two objects share a name in this course, and they are not interchangeable.

On a *smooth convex* $$g$$ (or a composite $$g+h$$ with convex $$h$$), Nesterov / FISTA uses a **scheduled** momentum weight and evaluates the smooth gradient at the extrapolated point $$v$$. The theorem is $$g(x^{(k)})+h(x^{(k)})-F^\star=O(1/k^2)$$, matching the first-order lower bound of [06-03-06]({% multilang_post_url contents/chapter06/21-03-20-06_03_06_can_we_do_better %}). The ISTA-versus-FISTA Lasso paths in [09-05-03]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}) are the picture you should be able to redraw.

On a *deep net*, `torch.optim.SGD(..., nesterov=True)` is usually a **constant** $$\beta\approx 0.9$$ look-ahead on a nonconvex loss. The filter intuition survives — consistent directions get a longer memory, oscillating directions cancel, look-ahead damps overshoot — but the $$O(1/k^2)$$ certificate does not. Lesson 26-02 is where that distinction is drawn in full, including the heavy-ball characteristic polynomial and a two-line NumPy comparison.

<div class="content-box insight-box">
<strong>One sentence to keep.</strong> FISTA is Nesterov’s look-ahead <em>plus</em> a prox, with a weight that depends on $$k$$. Deep-learning momentum is the same look-ahead with the weight frozen. Use the scheduled theorem on Lasso and logistic regression; use the Distill valley on everything else.
</div>

## When acceleration is the wrong first knob

Acceleration is not free speed. The same inertia that glides down a convex valley can overshoot a nonsmooth kink or a small basin, which is why [09-05-04]({% multilang_post_url contents/chapter09/20-01-08-09_05_04_is_acceleration_always_useful %}) exists and why restarted FISTA is a standard fix. If the smooth piece is cheap and strongly convex, a well-tuned proximal gradient step (or a variance-reduced sibling in [26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %})) can beat an un-restarted accelerated method in wall-clock. Monitor the objective; if you see the famous “Nesterov ripples,” restart or drop $$\beta$$.

**Exercise.** On the valley $$g(x)=\tfrac12 x^\top\operatorname{diag}(1,100)\,x$$ with $$h=0$$, plot ISTA (plain GD), FISTA with the $$(k-2)/(k+1)$$ weight, and constant-$$\beta$$ Nesterov from 26-02. Which schedule first reaches $$\|x\|_2\le 10^{-4}$$, and which one rings around the origin if you forget to restart?

**Question.** The FISTA weight tends to $$1$$. Distill’s optimal heavy-ball $$\beta^\star$$ for a known $$\kappa$$ is strictly less than $$1$$. Why can both be right — and what changes when you do *not* know $$\kappa$$?

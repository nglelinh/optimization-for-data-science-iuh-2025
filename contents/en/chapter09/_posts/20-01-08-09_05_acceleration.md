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

Watch plain gradient descent or ISTA descend an elongated, narrow canyon: even with the optimal step size $$t = 1/L$$, the iterates bounce back and forth across the steep walls while inching agonizingly slowly down the gentle valley floor. In 1983, a 27-year-old Yurii Nesterov published a four-page paper proving that adding a carefully calibrated **momentum extrapolation** step cuts the number of iterations from $$O(1/\varepsilon)$$ to $$O(1/\sqrt{\varepsilon})$$—the mathematically provable speed limit for all first-order methods! This lesson builds the geometric intuition behind Nesterov acceleration before diving into the algebra of FISTA.

## Background Knowledge Map: The Intuition Behind Optimal First-Order Acceleration

- **Pillar 1 — Zig-Zagging in Ill-Conditioned Valleys:** Along steep directions (eigenvalue $$L$$), step size $$1/L$$ stops oscillations; along flat directions (small curvature), $$1/L$$ takes tiny steps, causing $$O(1/k)$$ progress. Momentum cancels out the alternating cross-valley zig-zags while reinforcing consistent motion along the valley floor.
- **Pillar 2 — Look-Ahead Gradient Evaluation (Nesterov vs. Heavy Ball):** Unlike Polyak's classical heavy-ball momentum (which evaluates the gradient at $$x^{(k-1)}$$ and then adds momentum), Nesterov extrapolates *first* to $$v^{(k)} = x^{(k-1)} + \beta_k(x^{(k-1)} - x^{(k-2)})$$ and evaluates the gradient/prox *at the look-ahead point* $$v^{(k)}$$, providing a crucial braking correction that guarantees global $$O(1/k^2)$$ convergence for all convex problems.
- **Pillar 3 — Increasing Momentum Schedule ($$\beta_k \to 1$$):** Unlike constant-momentum SGD in deep learning, Nesterov's convex schedule $$\beta_k = \frac{k-2}{k+1}$$ starts at $$0$$ and asymptotically approaches $$1$$, corresponding in continuous time to the Su–Boyd–Candès second-order ODE $$\ddot{X}(t) + \frac{3}{t}\dot{X}(t) + \nabla f(X(t)) = 0$$ with vanishing friction $$3/t$$.
- **Pillar 4 — Non-Monotonic Ripples & Adaptive Restarts:** Because vanishing friction lets the iterate overshoot the minimum like a lightly damped spring, Nesterov acceleration produces characteristic "ripples" where $$f(x^{(k)})$$ briefly rises—which O'Donoghue and Candès (2015) tamed by resetting momentum whenever the velocity points uphill.

### Step-by-Step Worked Example (Read Slowly): Watching Nesterov Extrapolation Outpace Plain Gradient Descent

Minimize the flat 1D quadratic $$g(x) = \frac{1}{20} x^2$$ (so $$\nabla g(x) = 0.1 x$$, optimal $$x^\star = 0$$), using a conservative step size $$t = 1$$ (as if another coordinate had $$L = 1$$). Start at $$x^{(0)} = x^{(-1)} = 10$$.

1. **Plain Gradient Descent ($$x^{(k)} = x^{(k-1)} - 0.1 x^{(k-1)} = 0.9 x^{(k-1)}$$):**
   - $$k = 1$$: $$x^{(1)} = 9.0$$.
   - $$k = 2$$: $$x^{(2)} = 8.1$$.
   - $$k = 3$$: $$x^{(3)} = 7.29$$ (total distance moved: $$2.71$$).
2. **Nesterov Accelerated Gradient with $$\beta_k = \frac{k-1}{k+2}$$ (indexing $$k=1,2,3$$):**
   - $$k = 1$$ ($$\beta_1 = 0$$): $$v^{(1)} = 10$$, $$x^{(1)} = 10 - 0.1(10) = 9.0$$.
   - $$k = 2$$ ($$\beta_2 = 1/4 = 0.25$$):
     - Extrapolate: $$v^{(2)} = 9.0 + 0.25(9.0 - 10) = 8.75$$.
     - Gradient step at $$v^{(2)}$$: $$x^{(2)} = 8.75 - 0.1(8.75) = 7.875$$ (already ahead of $$8.1$$!).
   - $$k = 3$$ ($$\beta_3 = 2/5 = 0.40$$):
     - Extrapolate: $$v^{(3)} = 7.875 + 0.40(7.875 - 9.0) = 7.425$$.
     - Gradient step at $$v^{(3)}$$: $$x^{(3)} = 7.425 - 0.1(7.425) = 6.6825$$ (total distance moved: $$3.3175$$—already 22% farther after just 3 steps, and the lead widens quadratically with $$k$$!).

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

### ISTA and FISTA in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/ista-fista_en.mp4"></video>
</div>

ISTA and FISTA on lasso: soft thresholding, the (k − 2)/(k + 1) weight, Nesterov ripples, a case where acceleration slows down, and restart.

**Exercise.** On the valley $$g(x)=\tfrac12 x^\top\operatorname{diag}(1,100)\,x$$ with $$h=0$$, plot ISTA (plain GD), FISTA with the $$(k-2)/(k+1)$$ weight, and constant-$$\beta$$ Nesterov from 26-02. Which schedule first reaches $$\|x\|_2\le 10^{-4}$$, and which one rings around the origin if you forget to restart?

**Question.** The FISTA weight tends to $$1$$. Distill’s optimal heavy-ball $$\beta^\star$$ for a known $$\kappa$$ is strictly less than $$1$$. Why can both be right — and what changes when you do *not* know $$\kappa$$?

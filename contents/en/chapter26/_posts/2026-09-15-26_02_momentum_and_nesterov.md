---
layout: post
title: 26-02 Momentum and Nesterov acceleration
chapter: '26'
order: 3
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: required
---


Gradient descent on a badly conditioned quadratic zig-zags: the step that is safe for the sharp eigenvalue is painfully small along the flat one. **Momentum** keeps a velocity that accumulates consistent gradient components and cancels oscillating ones. This lesson is the Distill-style *why*, not a second copy of the FISTA algebra in [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %}) or the in-page animation in [06-06]({% multilang_post_url contents/chapter06/21-03-20-06_06_gradent_descent_with_momentum %}). Read Goh, *[Why Momentum Really Works](https://distill.pub/2017/momentum/)* (Distill, 2017), with the quadratic valley open in another tab; the notes below are the course’s spoken version of that picture.

## The valley that vanilla GD cannot walk

Take the model problem that every first-order method is secretly solving,

$$
F(w)=\tfrac12 w^\top A w,\qquad A=\operatorname{diag}(\lambda_1,\ldots,\lambda_d)\succ 0.
$$

The gradient is $$Aw$$. Gradient descent with step $$\eta$$ is the linear recurrence $$w_{k+1}=(I-\eta A)w_k$$, so each eigen-coordinate evolves independently as $$(1-\eta\lambda_i)^k$$. Stability on the sharpest axis forces $$\eta<2/\lambda_{\max}$$. The flattest axis then contracts only by $$1-\eta\lambda_{\min}\approx 1-2/\kappa$$, where $$\kappa=\lambda_{\max}/\lambda_{\min}$$ is the condition number. That is the zig-zag: you bounce off the walls of a long corridor and crawl down the hallway. Chapter 06 already proved the same $$1-m/L$$ factor under strong convexity; here we *see* it as two time-scales on a quadratic.

Open [gradient_descent_demo.html](https://nglelinh.github.io/interactive_math/optimization/gradient_descent_demo.html) and stretch one axis. The path that looks “wrong” is the optimal first-order method *without memory*.

## Heavy ball: a low-pass filter on the gradient

**Polyak’s heavy ball** (1964) introduces a velocity

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k), \\
w_{k+1} &= w_k - \eta v_{k+1},
\end{align}
$$

with $$\beta\in[0,1)$$. PyTorch’s `SGD(momentum=…)` is this family, up to whether the gradient is scaled before or after mixing (the `(1-β)` convention of 06-06 is an exponentially weighted moving average of the same object). Unrolling gives

$$
v_{k+1}=\sum_{j=0}^{k}\beta^{k-j}\nabla F(w_j),
$$

so a direction that *keeps the same sign* is amplified and a direction that *flips every step* is cancelled. That is exactly a discrete low-pass filter. In the corridor, the wall-normal component oscillates and dies; the hallway component is consistent and becomes a cruise speed.

On the same quadratic the closed recurrence is second-order,

$$
w_{k+1}=(1+\beta)(I-\eta A)w_k-\beta w_{k-1}
$$

(up to the usual affine rewrite). Each eigenmode has a characteristic polynomial $$r^2-(1+\beta)(1-\eta\lambda)r+\beta=0$$. Goh’s optimal tuning for a known $$\kappa$$ is the pair that places both roots on a circle of radius $$(\sqrt{\kappa}-1)/(\sqrt{\kappa}+1)$$:

$$
\eta^\star=\Bigl(\frac{2}{\sqrt{\lambda_{\max}}+\sqrt{\lambda_{\min}}}\Bigr)^2,\qquad
\beta^\star=\Bigl(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\Bigr)^2.
$$

The contraction improves from $$1-\Theta(1/\kappa)$$ to $$1-\Theta(1/\sqrt{\kappa})$$ — the same square-root-of-condition-number miracle that Nesterov’s *optimal* convex rate will claim in the next section. You do not need to memorize the two displayed constants; you do need the slogan: **momentum is a change of the discrete-time damping, not a new gradient**.

A useful physics picture, already hinted in 06-06, is the heavy-ball ODE $$m\ddot w+\gamma\dot w+\nabla F(w)=0$$. Too little friction and you orbit; too much and you crawl. The hyperparameter $$\beta$$ is that friction in discrete time. Deep-learning practice ($$\beta=0.9$$, sometimes $$0.99$$) is a robust default, not Goh’s optimal $$\beta^\star$$ — we almost never know $$\kappa$$ of a ResNet.

## Nesterov: evaluate the gradient where you are about to be

**Nesterov acceleration** keeps the same velocity but evaluates the gradient at a *look-ahead* point

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k-\eta\beta v_k), \\
w_{k+1} &= w_k-\eta v_{k+1}.
\end{align}
$$

Heavy ball adds the gradient at the *current* point to a velocity that already points down the corridor; if that velocity is about to overshoot, you only find out after you have left. Look-ahead asks the slope *one step ahead along the current velocity*, so the correction starts a beat earlier. Distill’s vector diagram is the right slide: two arrows (old velocity, new gradient) versus two arrows (old velocity, gradient at the extrapolated point). The second pair turns sooner at the bottom of the bowl.

On *smooth convex* problems, a carefully scheduled $$\beta_k$$ (classically $$\beta_k=(t_k-1)/t_{k+1}$$ with $$t_{k+1}=(1+\sqrt{1+4t_k^2})/2$$, or the FISTA weight $$(k-2)/(k+1)$$ of [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %})) yields the optimal first-order rate

$$
F(w_T)-F^\star=O\bigl(L\|w_0-w^\star\|_2^2/T^2\bigr).
$$

That is a theorem about a *convex* $$F$$ and a *time-varying* momentum. Deep-learning “Nesterov” (`torch.optim.SGD(..., nesterov=True)`) is usually a *constant* $$\beta$$ look-ahead on a nonconvex loss. Use the proof to understand *why* look-ahead damps; do not quote $$O(1/T^2)$$ for CIFAR accuracy.

<div class="content-box insight-box">
<strong>Theory ≠ practice reminder.</strong> Nesterov’s $$O(1/T^2)$$ needs a scheduled $$\beta_k$$ and a convex smooth $$F$$. Heavy ball’s $$\sqrt{\kappa}$$ tuning needs a quadratic (or a locally quadratic bowl). What transfers to AdamW training is the filter intuition: consistent directions get a longer memory; oscillating directions get cancelled; look-ahead spends that memory a little more carefully.
</div>

## What to implement, and what to watch

The two methods differ by a single gradient argument. On the classroom quadratic $$F(w)=\tfrac12 w^\top\operatorname{diag}(1,100)\,w$$ they already look different:

```python
import numpy as np

A = np.diag([1.0, 100.0])

def gd(w, eta):
    return w - eta * (A @ w)

def heavy_ball(w, v, eta, beta):
    v = beta * v + A @ w
    return w - eta * v, v

def nesterov(w, v, eta, beta):
    look = w - eta * beta * v
    v = beta * v + A @ look
    return w - eta * v, v
```

Start both from the same $$w_0$$, sweep $$\beta\in\{0,0.5,0.8,0.9,0.99\}$$ at a step that is stable for vanilla GD, and plot the two trajectories. The first $$\beta$$ that kills the visible zig-zag is the Distill lesson in one figure; the $$\beta$$ that then *overshoots* the origin is the “too little friction” picture.

Chapter 09’s FISTA is the *proximal* sibling of the same look-ahead (composite $$g+h$$, scheduled weight). Chapter 26’s Adam will later put an exponential moving average on the gradient *and* on its coordinate-wise square — momentum is the first of those two averages. Variance reduction ([26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %})) is a different cure for a different disease: it kills *sampling* noise, not *conditioning* zig-zags.

**Exercise 1.** Implement the three updates above. For $$\eta=2/(\lambda_{\min}+\lambda_{\max})$$ (the optimal GD step) and $$\beta=\beta^\star$$, count iterations to $$\|w\|_2\le 10^{-4}$$. Then break the tuning: keep $$\eta$$ and set $$\beta=0.99$$. Which method oscillates more, and why does look-ahead help?

**Exercise 2.** On the same quadratic, replace $$A$$ by a random SPD matrix with the same eigenvalues ($$A=Q\operatorname{diag}(\lambda)Q^\top$$). Convince yourself that momentum’s benefit is *spectral*, not axis-aligned.

**Question.** Given that SGD often escapes shallow basins more readily than full-batch GD, should you raise or lower $$\beta$$ when you switch from the quadratic valley to a small nonconvex net — and what would Distill’s filter picture predict about a noisy gradient that flips sign every minibatch?

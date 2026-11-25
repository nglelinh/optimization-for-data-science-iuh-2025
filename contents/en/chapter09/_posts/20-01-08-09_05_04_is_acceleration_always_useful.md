---
layout: post
title: '09-05-04 Is acceleration always useful?'
chapter: '09'
order: 10
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

After seeing FISTA slash iteration counts from 20,000 down to 282, it is tempting to bolt Nesterov acceleration onto every optimization problem you ever encounter. Yet seasoned practitioners know a sobering truth: acceleration is a **high-gain amplifier**—it amplifies smooth deterministic curvature beautifully, but it also amplifies gradient noise, inexact proximal errors, and miscalibrated step sizes! Knowing *when* acceleration helps and when plain proximal gradient (or restarted FISTA) wins is what separates textbook theory from production-grade optimization.

## Background Knowledge Map: The Practical Limits of Acceleration

- **Pillar 1 — Nesterov Ripples & Overshoot:** When momentum approaches $$1$$ on a strongly convex or locally curved valley, FISTA overshoots the minimum and oscillates in visible "ripples" where $$f(x^{(k)})$$ temporarily increases. Gradient-scheme restarting (resetting $$t_k = 1$$ whenever $$(y^{(k)} - x^{(k)})^\top(x^{(k)} - x^{(k-1)}) > 0$$) eliminates ripples and often unlocks linear convergence.
- **Pillar 2 — Sensitivity to Stochastic Noise & Inexact Prox:** Accelerated methods accumulate gradient errors with weight $$O(k)$$ instead of averaging them out; in noisy SGD or when $$\operatorname{prox}_{t h}$$ is solved only approximately, plain proximal gradient can actually beat FISTA unless errors decay rapidly.
- **Pillar 3 — Warm Starts & Well-Conditioned Problems:** When solving a Lasso regularization path with warm starts (or when the condition number $$\kappa = L/\mu$$ is small, say $$\kappa \le 5$$), plain proximal gradient already converges in a handful of iterations where $$\beta_k$$ barely has time to ramp up.
- **Pillar 4 — Strong Convexity Mismatch:** Standard FISTA assumes $$\mu = 0$$ (merely convex) and sets $$\beta_k \to 1$$, which is *under-damped* when $$g$$ is $$\mu$$-strongly convex. Using the fixed strong-convexity momentum $$\beta = \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$$ (or adaptive restart) avoids under-damped oscillations.

### Step-by-Step Worked Example (Read Slowly): Seeing Nesterov Overshoot on a Well-Conditioned Quadratic

Consider the perfectly conditioned 1D quadratic $$g(x) = \frac{1}{2} x^2$$ ($$L = 1, \mu = 1, \kappa = 1, x^\star = 0$$) with step size $$t = 0.5$$, starting at $$x^{(0)} = x^{(-1)} = 4$$.

1. **Plain Gradient Descent ($$x^{(k)} = 0.5 x^{(k-1)}$$):**
   - $$x^{(1)} = 2.0$$, $$x^{(2)} = 1.0$$, $$x^{(3)} = 0.5$$, $$x^{(4)} = 0.25$$ (smooth, monotone decay; objective drops $$4\times$$ per step).
2. **Standard FISTA (with $$\beta_2 \approx 0.28, \beta_3 \approx 0.43, \beta_4 \approx 0.53$$):**
   - $$k = 1$$: $$x^{(1)} = 2.0$$.
   - $$k = 2$$: $$y^{(2)} = 2.0 + 0.28(2.0 - 4.0) = 1.44 \implies x^{(2)} = 0.5(1.44) = 0.72$$.
   - $$k = 3$$: $$y^{(3)} = 0.72 + 0.43(0.72 - 2.0) = 0.17 \implies x^{(3)} = 0.5(0.17) = 0.085$$.
   - $$k = 4$$: $$y^{(4)} = 0.085 + 0.53(0.085 - 0.72) = -0.252 \implies x^{(4)} = -0.126$$!
3. **Notice the ripple:** At $$k = 4$$, FISTA *overshot* $$x^\star = 0$$ to $$-0.126$$, and the objective *increased* from $$f(x^{(3)}) = \frac{1}{2}(0.085)^2 = 0.0036$$ to $$f(x^{(4)}) = \frac{1}{2}(-0.126)^2 = 0.0079$$! Applying an **adaptive restart** at $$k = 4$$ (since $$(y^{(4)} - x^{(4)})(x^{(4)} - x^{(3)}) = (-0.126)(-0.211) > 0$$) immediately kills the ripple.

# Is acceleration always useful?

Acceleration methods such as FISTA can achieve faster convergence rates in theory, but in practice, acceleration is not always beneficial.

## When acceleration may not help
- If the problem is well-conditioned (small condition number $$\kappa = L/\mu$$), plain proximal gradient already converges fast, at a linear rate. Acceleration gains little, and the momentum can even make it a bit slower. For example, on a 2D lasso with $$\kappa = 3$$, ISTA needs 14 iterations and FISTA needs 16.
- Acceleration helps most when the problem is ill-conditioned (large $$\kappa$$). There, plain proximal gradient is slow, and FISTA cuts the number of iterations by a large factor. The price is that the objective value can oscillate.
- With a non-smooth $$g$$, or when $$\nabla g$$ has no useful Lipschitz constant, the $$O(1/k^2)$$ guarantee does not apply.
- The "Nesterov ripples" phenomenon makes the objective value non-monotonic: it can go up for some iterations before it goes down again.

## Practical advice
- Use acceleration when the smooth part is ill-conditioned; that is where it pays off most.
- When the problem is well-conditioned, plain proximal gradient is often enough.
- Monitor the objective value. If the ripples are large, use a restart scheme (reset $$t_k = 1$$ when the objective goes up) instead of giving up acceleration.

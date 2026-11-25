---
layout: post
title: 28-02 Escaping saddles and landscape geometry
chapter: '28'
order: 3
owner: Nguyen Le Linh
categories:
- chapter28
lang: en
lesson_type: required
---

Knowing that a strict saddle has a negative-curvature escape direction is reassuring, yet vanilla gradient descent can still linger exponentially long near a saddle if it approaches almost orthogonally to that unstable eigenvector. How do practical algorithms break free cleanly? Remarkably, **a tiny injection of isotropic noise** (Perturbed Gradient Descent, Jin et al. 2017) is enough to kick the iterate out of the thin "stuck region" around any strict saddle and guarantee polynomial-time convergence to an $$\varepsilon$$-second-order stationary point—explaining one reason why SGD’s built-in minibatch noise is a feature, not a bug.

## Key ideas: Mechanisms for Escaping Strict Saddles

- **The Thin Stuck Region:** Near a strict saddle $$w_s$$, only trajectories initialized on the measure-zero stable manifold (spanned by eigenvectors with $$\lambda_i \ge 0$$) converge into $$w_s$$. Gradient descent from a random initialization avoids strict saddles almost surely (Lee et al. 2016), though worst-case escape time can be exponential without perturbations.
- **Perturbed Gradient Descent (PGD):** Whenever $$\|\nabla F(w_k)\|_2$$ becomes small, adding a single tiny uniform ball perturbation $$\xi \sim \text{Unif}(B_r(0))$$ ensures a non-negligible projection onto the negative-curvature eigenvector $$v_{\min}$$, triggering exponential growth $$(1 + \eta |\lambda_{\min}|)^t$$ away from the saddle!
- **Approximate Second-Order Stationarity ($$\varepsilon$$-SOSP):** Because exact global minimization of general nonconvex functions is NP-hard, modern theory targets $$\|\nabla F(w)\|_2 \le \varepsilon$$ and $$\lambda_{\min}(\nabla^2 F(w)) \ge -\sqrt{\rho \varepsilon}$$ (where $$\rho$$ is Hessian Lipschitzness)—achievable in $$\tilde{O}(\varepsilon^{-2})$$ perturbed gradient steps.
- **Negative-Curvature Exploitation (Cubic Newton / Trust Region):** Second-order methods explicitly compute or approximate $$v_{\min}$$ via Hessian-vector products (Lanczos) and step directly along $$v_{\min}$$ to escape saddles in fewer iterations at higher per-step cost.

### Worked example: Exponential Escape Rate From a Strict Saddle

Consider the pure quadratic saddle $$F(x, y) = \frac{1}{2}(4 y^2 - x^2)$$ near the saddle $$(0, 0)$$ (so $$\lambda_y = +4$$, $$\lambda_x = -1$$). Run gradient descent with step size $$\eta = 0.2$$ (safe for $$L = 4$$ since $$0.2 < 2/4$$).

1. **Write the exact GD update:**
   $$\nabla F(x, y) = (-x,\ 4y)^\top \implies x_{k+1} = (1 + \eta) x_k = 1.2\, x_k, \qquad y_{k+1} = (1 - 4\eta) y_k = 0.2\, y_k.$$
2. **Start on the stable manifold $$(x_0, y_0) = (0, 1)$$ (zero noise):**
   - $$x_k = 0$$ forever, while $$y_k = (0.2)^k \to 0$$. Vanilla GD falls straight into the saddle $$(0, 0)$$ and stays trapped forever!
3. **Inject a tiny perturbation $$\xi = (0.01, 0)$$ at $$(0, 0)$$:**
   - Now $$x_0 = 0.01$$, and every GD step amplifies $$x_k$$ geometrically by $$1.2\times$$:
     - $$k = 10$$: $$x_{10} = 0.01 \times (1.2)^{10} \approx 0.0619$$.
     - $$k = 26$$: $$x_{26} = 0.01 \times (1.2)^{26} \approx 1.145$$!
   - Objective drops from $$F(0, 0) = 0$$ to $$F(1.145, 0) = -\frac{1}{2}(1.145)^2 \approx -0.655$$.
   Because growth is exponential ($$1.2^k$$), shrinking the perturbation radius by $$100\times$$ only adds $$\log_{1.2}(100) \approx 25$$ extra steps—showing concretely why Perturbed GD escapes strict saddles in $$O(\log(d/\varepsilon))$$ steps!

How do the algorithms you already know leave a strict saddle?

- **Noise helps.** SGD’s gradient estimator is not exactly $$\nabla F$$. A random perturbation has a component along the negative-curvature direction with high probability. Full-batch GD can sit at a saddle if it arrives with zero component in that direction (the $$(0,0)$$ example of the previous lesson).
- **Perturbed GD.** Adding explicit isotropic noise when $$\|\nabla F\|$$ is small is a theorem-friendly cousin of SGD (Ge, Huang, Jin, Yuan, and later Jin et al. on perturbed gradient descent).
- **Momentum** can overshoot a flat ridge and fall off; it can also oscillate. Do not treat it as a saddle-escape guarantee.
- **Second-order / negative-curvature steps** (Hessian–vector products via Pearlmutter, or Neon-style) explicitly walk downhill along the most negative eigenvector. Rare in production DL; useful as a mental model.

**Sharp vs flat minima.** Around two minimizers with the same $$F$$, the larger Hessian eigenvalues mean a *sharp* bowl: a small parameter perturbation (or a small distribution shift) raises the loss a lot. **SAM** (Foret et al., ICLR 2021) optimizes a local-max envelope to prefer flatter regions; it is optional seminar material, not a required algorithm this term.

Geometry to keep: the loss surface is not a 2-D cartoon with a handful of pits. It is a high-dimensional object with huge **plateaus**, **narrow canyons** (the condition-number story of Chapters 06 and 26), and symmetries (permuting hidden units leaves $$F$$ invariant, so minima come in manifolds). When a demo shows a 3-D surface, ask what was *projected away*.

### Saddle points in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/saddle-escape_en.mp4"></video>
</div>

GD pulled into the saddle of x² − y² + ½y⁴, sitting long with a tiny offset, escaping with noise, and why most critical points are saddles in high dimensions.

**Question.** If SGD noise is what knocks you off saddles, what happens to that mechanism as batch size $$B\to n$$? How might that inform the “large-batch generalization” debate?

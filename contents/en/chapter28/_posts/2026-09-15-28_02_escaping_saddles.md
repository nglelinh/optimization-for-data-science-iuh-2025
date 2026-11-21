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


How do the algorithms you already know leave a strict saddle?

- **Noise helps.** SGD’s gradient estimator is not exactly $$\nabla F$$. A random perturbation has a component along the negative-curvature direction with high probability. Full-batch GD can sit at a saddle if it arrives with zero component in that direction (the $$(0,0)$$ example of the previous lesson).
- **Perturbed GD.** Adding explicit isotropic noise when $$\|\nabla F\|$$ is small is a theorem-friendly cousin of SGD (Ge, Huang, Jin, Yuan, and later Jin et al. on perturbed gradient descent).
- **Momentum** can overshoot a flat ridge and fall off; it can also oscillate. Do not treat it as a saddle-escape guarantee.
- **Second-order / negative-curvature steps** (Hessian–vector products via Pearlmutter, or Neon-style) explicitly walk downhill along the most negative eigenvector. Rare in production DL; useful as a mental model.

**Sharp vs flat minima.** Around two minimizers with the same $$F$$, the larger Hessian eigenvalues mean a *sharp* bowl: a small parameter perturbation (or a small distribution shift) raises the loss a lot. **SAM** (Foret et al., ICLR 2021) optimizes a local-max envelope to prefer flatter regions; it is optional seminar material, not a required algorithm this term.

Geometry to keep: the loss surface is not a 2-D cartoon with a handful of pits. It is a high-dimensional object with huge **plateaus**, **narrow canyons** (the condition-number story of Chapters 06 and 26), and symmetries (permuting hidden units leaves $$F$$ invariant, so minima come in manifolds). When a demo shows a 3-D surface, ask what was *projected away*.

**Question.** If SGD noise is what knocks you off saddles, what happens to that mechanism as batch size $$B\to n$$? How might that inform the “large-batch generalization” debate?

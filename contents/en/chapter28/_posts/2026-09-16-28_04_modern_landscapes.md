---
layout: post
title: 28-04 Modern landscape case studies
chapter: '28'
order: 5
owner: Nguyen Le Linh
categories:
- chapter28
lang: en
lesson_type: optional
---

Textbook nonconvexity paints a bleak picture of disconnected, treacherous local traps. Yet empirical deep learning between 2018 and 2026 uncovered four astonishing geometric phenomena that rewrote our intuition: independently trained minima are connected by zero-barrier valleys (**mode connectivity**), networks can suddenly generalize long after memorizing training data (**grokking**), test error drops a second time past the interpolation threshold (**double descent**), and flatter Hessian basins correlate strongly with robustness (**flat minima & SAM**).

## Key ideas: Four Empirical Phenomena of Deep Loss Landscapes

- **Linear & Nonlinear Mode Connectivity:** Two neural nets trained from independent random seeds can be connected by a low-loss curve (Garipov et al. 2018)—and after aligning hidden-neuron permutation symmetries (Git Re-Basin, Ainsworth et al. 2023), often by a *straight line* with nearly zero loss barrier!
- **Grokking (Delayed Generalization):** On algorithmic tasks (e.g., modular arithmetic), AdamW first drives training loss to zero via memorization while validation accuracy sits at random chance; hundreds of epochs later, weight decay slowly prunes the memorizing circuit in favor of a lower-norm generalizing circuit, causing validation accuracy to jump abruptly to 100%.
- **Double Descent:** Plotting test error against model capacity $$d$$ reveals the classical U-shaped bias–variance curve up to the interpolation peak $$d \approx n$$ (where ill-conditioned matrices amplify label noise), followed by a *second descent* for $$d \gg n$$ as minimum-norm interpolation smooths the fit.
- **Flat Minima & Hessian Sharpness:** A minimum with small top Hessian eigenvalue $$\lambda_{\max}(\nabla^2 F(w^\star))$$ tolerates distribution shifts (small shifts in the loss surface) with far smaller test-loss degradation than a razor-sharp minimum.

### Worked example: Quantifying a Flat vs. Sharp Minimum Under Distribution Shift

Suppose test loss is simply training loss shifted horizontally by a small distribution shift $$\Delta = 0.2$$: $$F_{\text{test}}(w) = F_{\text{train}}(w - 0.2)$$. Compare two zero-loss minima—one **flat** and one **sharp**:
- Flat basin around $$w_A^\star = 0$$: $$F_A(w) = \frac{1}{2}(1)\, w^2$$ (curvature $$\lambda_A = 1$$).
- Sharp basin around $$w_B^\star = 0$$: $$F_B(w) = \frac{1}{2}(100)\, w^2$$ (curvature $$\lambda_B = 100$$).

1. **Evaluate training loss at both minima:**
   $$F_A(0) = 0, \qquad F_B(0) = 0.$$
   On training data, both solutions look **100% identical**!
2. **Evaluate test loss under the $$\Delta = 0.2$$ distribution shift:**
   - Flat minimum: $$F_{A,\text{test}}(0) = \frac{1}{2}(1)(0 - 0.2)^2 = 0.02$$.
   - Sharp minimum: $$F_{B,\text{test}}(0) = \frac{1}{2}(100)(0 - 0.2)^2 = 2.00$$!
3. **Takeaway:** Under the exact same distribution shift, the sharp minimum suffers **100× worse** test degradation—illustrating quantitatively why sharpness-aware optimizers (like SAM) and large-step SGD bias toward flatter basins.

Lessons 28-01 to 28-03 defined critical points, saddles, and overparameterization. This optional note is four *empirical* phenomena that those definitions were meant to unlock. It does not re-prove that high-dimensional saddles dominate, and it does not re-derive the PL inequality.

## 1. Mode connectivity: minima are not islands

Garipov, Izmailov, Podoprikhin, Vetrov, and Wilson (NeurIPS 2018) and Draxler, Veschgini, Salmhofer, and Hamprecht (ICML 2018) showed that two SGD solutions of a deep net can be joined by a low-loss *polygonal* path — often two linear segments — on which the train loss stays almost constant. Frankle, Dziugaite, Roy, and Carbin (ICML 2020) tied the same picture to the lottery-ticket literature. The 2025 refinement (entropic confinement, [arXiv:2512.06297](https://arxiv.org/abs/2512.06297)) is the student-level punchline: the path can be low-*loss* and still high-*curvature* in the middle, so noisy SGD stays in one basin even though a deterministic path to another basin exists. Connectivity is a statement about the *sublevel set*; confinement is a statement about *dynamics*. Chapter 28 needs both.

## 2. Grokking: generalization long after interpolation

Power, Burda, Edwards, Babuschkin, and Misra, *Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets*, [arXiv:2201.02177](https://arxiv.org/abs/2201.02177), 2022, train small transformers on modular arithmetic. Training accuracy hits 100% quickly; *validation* accuracy stays at chance for orders of magnitude more steps, then jumps. The landscape interpretation that belongs in this chapter: interpolation (train loss $$\approx 0$$) is not the end of training. The optimizer keeps moving *inside* the interpolating set, and the implicit bias of Chapter 28-03 eventually picks a generalizing point. Weight decay (AdamW, 26-04) is empirically necessary for grokking on these tasks — another reminder that the optimizer is part of the inductive bias.

## 3. Double descent, now a landscape fact

Belkin, Hsu, Ma, and Mandal, *PNAS* 2019, and Nakkiran, Kaplun, Bansal, Yang, Barak, and Sutskever, ICLR 2020 (preprint 2019, [arXiv:1912.02292](https://arxiv.org/abs/1912.02292)), showed that test error can *rise* at the interpolation threshold and then *fall* again as the model grows. Overparameterization (28-03) is not a pathology; it is the second half of that curve. The 2022–2024 follow-ups (epoch-wise double descent, data-wise double descent) are the same geometry with a different axis. When a student says “more parameters overfit,” the figure to draw is double descent, not a U-curve from 1990s statistics.

## 4. Flat minima and SAM, seen from the Hessian

Foret et al., ICLR 2021 (SAM; details in [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %})) is an *algorithm* that prefers flat regions. Bartlett, Long, and Bousquet, *JMLR* 24(43), 2023, and Shin, Lee, Andriushchenko, and Lee, [arXiv:2311.17539](https://arxiv.org/abs/2311.17539), make it a *landscape* statement: linearly stable SAM minima have a more uniform Hessian spectrum, and the generalization gap between SAM and SGD *widens* as the net becomes more overparameterized. You do not need to implement SAM to use this section. You need to stop saying “a local minimum is a local minimum.” In an interpolating deep net, minima differ by sharpness, and sharpness is a Hessian (or PAC-Bayes) story, not a first-order one.

Open [loss_function_landscapes.html](https://nglelinh.github.io/interactive_math/optimization/loss_function_landscapes.html) and look at a 2-D slice: the same low loss can sit in a ravine or a bowl. That cartoon is the whole of 28-04.

**Exercise.** (i) On a 2-D random-ReLU net, take two SGD solutions and plot the loss along the linear path $$w(t)=(1-t)w_A+t w_B$$. You will usually see a barrier (linear paths are the *wrong* connectors). (ii) Insert a bend $$w_{1/2}= (w_A+w_B)/2 + v$$ and minimize the barrier over a small $$v$$ — a poor person’s mode-connectivity search. (iii) Read Power et al. Figure 1 and write three sentences on why train accuracy is the wrong stopping rule for that plot.

## Sources

- T. Garipov et al., NeurIPS 2018; F. Draxler et al., ICML 2018 — mode connectivity.
- J. Frankle et al., ICML 2020 — connectivity and lottery tickets.
- Entropic confinement, [arXiv:2512.06297](https://arxiv.org/abs/2512.06297), 2025.
- A. Power et al., [arXiv:2201.02177](https://arxiv.org/abs/2201.02177), 2022 — grokking.
- M. Belkin et al., *PNAS* 2019; P. Nakkiran et al., ICLR 2020 — double descent.
- P. Foret et al., ICLR 2021; P. L. Bartlett et al., *JMLR* 24(43), 2023 — SAM / flat minima.
- S. Shin, D. Lee, M. Andriushchenko, N. Lee, [arXiv:2311.17539](https://arxiv.org/abs/2311.17539) — SAM and overparameterization.

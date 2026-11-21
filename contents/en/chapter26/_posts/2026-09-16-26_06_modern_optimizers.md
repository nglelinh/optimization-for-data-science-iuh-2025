---
layout: post
title: 26-06 Modern adaptive optimizers (seminar)
chapter: '26'
order: 7
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: optional
---


Lessons 26-01 to 26-05 are the assessed stack: SGD, Distill-style momentum, AdaGrad → Adam, **AdamW**, and SVRG / SAGA. This optional seminar is the 2021–2026 optimizer zoo at *algorithm* depth — one recurrence each, not a second AdamW lecture. [26-04]({% multilang_post_url contents/chapter26/2026-09-15-26_04_adamw_and_practice %}) already owns decoupled weight decay. The Hessian-preconditioner story of Sophia as a Newton cousin lives in [14-10]({% multilang_post_url contents/chapter14/2026-09-16-14_10_modern_applications %}); here we only need the *update*, so we can place SAM, Sophia, and Muon on the same board as AdamW. None of the three is assessed this term.

The question is: *what did people actually train large models with after AdamW became the default, and what extra geometry does each method buy?*

## AdamW remains the baseline

Loshchilov and Hutter, ICLR 2019, [arXiv:1711.05101](https://arxiv.org/abs/1711.05101), is still the optimizer named in Llama / GPT-style recipes: $$\eta$$ in the $$10^{-4}$$ range, $$\beta=(0.9,0.95)$$ or $$(0.9,0.999)$$, decoupled $$\lambda\approx 0.1$$, warmup then cosine. Every method below is measured *against* that recipe. If you can only remember one algorithm from Chapter 26, remember AdamW.

## SAM: a local max, then a descent

Sharpness-Aware Minimization (Foret, Kleiner, Mobahi, Neyshabur, ICLR 2021, [OpenReview](https://openreview.net/forum?id=6Tm1mposlrM)) replaces the pointwise risk $$F(w)$$ by a *neighbourhood* worst case

$$
\min_w\ \max_{\|\varepsilon\|_2\le\rho} F(w+\varepsilon)
\approx F\bigl(w+\rho\,\nabla F(w)/\|\nabla F(w)\|_2\bigr).
$$

The algorithm is two gradients per step, not a new preconditioner.

1. **Ascent (perturb).** $$g\leftarrow\nabla F(w)$$, then $$\varepsilon\leftarrow\rho\,g/\|g\|_2$$ (or a dual-norm cousin).
2. **Descent (SAM gradient).** Evaluate $$g_{\mathrm{SAM}}\leftarrow\nabla F(w+\varepsilon)$$ and step $$w\leftarrow w-\eta\,g_{\mathrm{SAM}}$$ (or feed $$g_{\mathrm{SAM}}$$ to AdamW / SGD+momentum).

The extra ascent biases the iterate toward **flat** minima: a small ball around $$w$$ still has small loss. Bartlett, Long, and Bousquet, *The Dynamics of Sharpness-Aware Minimization*, *JMLR* 24(43), 2023, show that near a smooth minimum the extra step is a bounce across the sharpest Hessian direction plus a drift that *decreases* $$\|\nabla^2 F\|$$. Shin, Lee, Andriushchenko, and Lee ([arXiv:2311.17539](https://arxiv.org/abs/2311.17539)) find that SAM’s generalization gain *grows* with overparameterization — a bridge to Chapter 28 and to the PL story in [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}). SAM is used in vision and some fine-tunes; full LLM pretraining usually skips the doubled gradient cost. Adaptive-radius variants (ASAM, GSAM) change the ball, not the two-step template.

## Sophia: AdamW with a clipped diagonal Hessian

Liu, Li, Hall, Liang, and Ma, *Sophia*, ICLR 2024, [OpenReview](https://openreview.net/forum?id=3xHDeA8Noi), keep Adam-like first moments but replace the second-moment accumulator by a *clipped* diagonal Hessian estimate. Writing $$m$$ for the EMA of the gradient and $$\hat h$$ for the EMA of a diagonal curvature estimate,

$$
w\leftarrow w-\eta\cdot\operatorname{clip}\bigl(m/(\hat h+\varepsilon),\,\tau\bigr),
$$

with $$\hat h$$ refreshed only every handful of steps (Hutchinson Hessian–vector products, or a Gauss–Newton–Bartlett estimator that draws a label from the model and squares that gradient). The clip is a trust-region: a stale or indefinite diagonal must not explode the step. Treat Sophia as “AdamW whose denominator knows curvature,” not as full Newton — the affine-invariance and Hessian-factorisation discussion belongs in 14-10. The claim is fewer steps than AdamW on language-model pretraining at a modest extra cost per step.

## Muon: orthogonalize the hidden-layer update

Jordan, Jin, Boza, Cesista, Newhouse, and Bernstein, *Muon*, 2024, [kellerjordan.github.io/posts/muon](https://kellerjordan.github.io/posts/muon/), take Nesterov momentum on each *matrix* parameter $$W\in\mathbb{R}^{m\times n}$$ and replace the update by its nearest orthogonal matrix, computed by a few Newton–Schulz iterations (no SVD in the inner loop):

$$
\begin{align}
B &\leftarrow \beta B+\nabla_W F,\\
O &\leftarrow \operatorname{NewtonSchulz}(B)\approx\arg\min_{Q^\top Q=I}\|Q-B\|_F,\\
W &\leftarrow W-\eta\,O.
\end{align}
$$

Embeddings, heads, and vectors stay on AdamW — a 2-D hidden weight wants an orthogonal step (a rotation of features, roughly constant spectral norm); a token-embedding table does not. NanoGPT speedrunning (late 2024) made Muon the default in that community. Jingyuan Liu et al., *Muon is Scalable for LLM Training*, [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025, add weight decay and a per-parameter scale, train a 3B/16B MoE (Moonlight) on 5.7T tokens, and report about $$2\times$$ compute efficiency versus AdamW on a scaling-law plot. Shah et al., [arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025, push the Pareto frontier on the compute–time tradeoff up to 4B parameters. This is the first serious *matrix-aware* challenger to diagonal AdamW.

Newton–Schulz itself is a cheap polynomial iteration on $$X^\top X$$ that drives singular values toward $$1$$. You do not need the coefficients for this course; you need the slogan: **Muon preconditions by polar factor, AdamW preconditions by per-coordinate RMS**.

## Schedule-free AdamW (pointer)

Defazio and colleagues (2024) propose a *schedule-free* AdamW that replaces a decreasing $$\eta_t$$ by an implicit Polyak–Ruppert average. Useful as a seminar paper; not a second set of homework knobs. The Chapter 06 optional note [06-08]({% multilang_post_url contents/chapter06/2026-09-16-06_08_Applications_Recent %}) already placed that paper next to Lion and the edge of stability.

| Method | Extra work / memory | Geometry it adds | Typical home (2026) | Assessed? |
|--------|---------------------|------------------|---------------------|-----------|
| AdamW | two EMAs | per-coordinate RMS | default LLM / vision | yes (26-04) |
| SAM | $$2\times$$ gradient | flat-minima (inner max) | vision, some fine-tunes | no |
| Sophia | cheap diagonal Hessian + clip | curvature-aware denominator | LM pretraining experiments | no |
| Muon | Newton–Schulz on hidden matrices | polar / orthogonal update | NanoGPT, some LLM pretrains | no |

**Exercise (survey, not a bake-off).** Read the Muon blog’s “use AdamW on embeddings and the head” paragraph and write four sentences: (i) why a 2-D hidden weight wants an orthogonal update, (ii) why the embedding table does not, (iii) how this differs from AdamW’s *per-coordinate* $$1/\sqrt{\hat v}$$, and (iv) why SAM’s inner max is a *landscape* statement (Ch.28) rather than a preconditioner. No training run required.

**Question.** Which of the three methods still makes sense if you are only allowed *one* gradient per step — and which Chapter 26 object (momentum, diagonal second moment, or variance reduction) is it closest to?

## Sources

- I. Loshchilov and F. Hutter, ICLR 2019 — AdamW.
- P. Foret, A. Kleiner, H. Mobahi, B. Neyshabur, ICLR 2021 — SAM.
- P. L. Bartlett et al., *JMLR* 24(43), 2023 — SAM dynamics.
- H. Liu et al., ICLR 2024 — Sophia (update here; Newton reading in 14-10).
- K. Jordan et al., 2024 — Muon.
- Jingyuan Liu et al., [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025 — Muon at LLM scale.
- I. Shah et al., [arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025 — Muon pretraining efficiency.

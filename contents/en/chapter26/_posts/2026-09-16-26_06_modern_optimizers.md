---
layout: post
title: 26-06 Modern adaptive optimizers (survey)
chapter: '26'
order: 7
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: optional
---


Lessons 26-01 to 26-05 are the assessed stack: SGD, momentum, AdaGrad → Adam, **AdamW**, and a variance-reduction pointer. This optional survey is the 2023–2026 optimizer zoo at *one-paragraph-each* depth. Do not treat it as a second AdamW lecture; [26-04]({% multilang_post_url contents/chapter26/2026-09-15-26_04_adamw_and_practice %}) already owns decoupled weight decay. The question here is: *what did people actually train large models with after AdamW became the default?*

## AdamW remains the baseline

Loshchilov and Hutter, ICLR 2019, [arXiv:1711.05101](https://arxiv.org/abs/1711.05101), is still the optimizer named in Llama / GPT-style recipes: $$\eta$$ in the $$10^{-4}$$ range, $$\beta=(0.9,0.95)$$ or $$(0.9,0.999)$$, decoupled $$\lambda\approx 0.1$$, warmup then cosine. Every method below is measured *against* that recipe. If you can only remember one algorithm from Chapter 26, remember AdamW.

## SAM: optimize a local max, not a point

Sharpness-Aware Minimization (Foret, Kleiner, Mobahi, Neyshabur, ICLR 2021, [OpenReview](https://openreview.net/forum?id=6Tm1mposlrM)) replaces $$F(w)$$ by a *neighborhood* worst case

$$
\min_w\ \max_{\|\varepsilon\|_2\le\rho} F(w+\varepsilon)\ \approx\ F\bigl(w+\rho\,\nabla F(w)/\|\nabla F(w)\|_2\bigr).
$$

One extra gradient (ascent to $$w+\varepsilon$$, then descent at that point) biases SGD toward **flat** minima. Bartlett, Long, and Bousquet, *The Dynamics of Sharpness-Aware Minimization*, *JMLR* 24(43), 2023, [jmlr.org/papers/v24/23-043.html](https://www.jmlr.org/papers/v24/23-043.html), show that the extra step is, near a smooth minimum, a bounce across the sharpest Hessian direction plus a drift that *decreases* $$\|\nabla^2 F\|$$. Shin, Lee, Andriushchenko, and Lee ([arXiv:2311.17539](https://arxiv.org/abs/2311.17539), 2023/2024) find that SAM’s generalization gain *grows* with overparameterization — a bridge to Chapter 28. SAM is used in vision and some fine-tunes; full LLM pretraining usually skips the doubled gradient cost.

## Sophia: a cheap diagonal Hessian

Liu, Li, et al., *Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training*, ICLR 2024, [OpenReview](https://openreview.net/forum?id=3xHDeA8Noi), keep Adam-like moments but replace the second-moment accumulator by a *clipped* diagonal Hessian estimate (Hutchinson or a cheap Gauss–Newton). The claim is fewer steps than AdamW on language-model pretraining at a modest extra cost per step. Treat Sophia as “AdamW with a curvature-aware denominator,” not as full Newton.

## Muon: orthogonalize the hidden-layer update

Jordan, Jin, Boza, Jiacheng, Cesista, Newhouse, and Bernstein, *Muon: An optimizer for hidden layers in neural networks*, 2024, [kellerjordan.github.io/posts/muon](https://kellerjordan.github.io/posts/muon/), take Nesterov momentum on each *matrix* parameter and replace the update by its nearest orthogonal matrix (Newton–Schulz iteration — no SVD in the inner loop). Embeddings, heads, and vectors stay on AdamW. NanoGPT speedrunning (late 2024) made Muon the default in that community. Jingyuan Liu et al., *Muon is Scalable for LLM Training*, [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025, add weight decay and a per-parameter scale, train a 3B/16B MoE (Moonlight) on 5.7T tokens, and report about $$2\times$$ compute efficiency versus AdamW on a scaling-law plot. Shah et al., *Practical Efficiency of Muon for Pretraining*, [arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025, push the Pareto frontier on the compute–time tradeoff up to 4B parameters. This is the first serious *matrix-aware* challenger to diagonal AdamW; it is **not** assessed this term.

## Schedule-free AdamW (pointer)

Defazio and colleagues (2024) propose a *schedule-free* AdamW that replaces a decreasing $$\eta_t$$ by an implicit Polyak–Ruppert average. Useful as a seminar paper; not a second set of homework knobs.

| Method | Extra work / memory | Typical home (2026) | Assessed? |
|--------|---------------------|---------------------|-----------|
| AdamW | two EMAs | default LLM / vision | yes (26-04) |
| SAM | $$2\times$$ gradient | flat-minima vision, some fine-tunes | no |
| Sophia | cheap diagonal Hessian | LM pretraining experiments | no |
| Muon | Newton–Schulz on hidden matrices | NanoGPT, some LLM pretrains | no |

**Exercise (survey, not a bake-off).** Read the Muon blog’s “use AdamW on embeddings and the head” paragraph and write four sentences: (i) why a 2-D hidden weight wants an orthogonal update, (ii) why the embedding table does not, (iii) how this differs from AdamW’s *per-coordinate* $$1/\sqrt{\hat v}$$, and (iv) why SAM’s inner max is a *landscape* statement (Ch.28) rather than a preconditioner. No training run required.

## Sources

- I. Loshchilov and F. Hutter, ICLR 2019 — AdamW.
- P. Foret, A. Kleiner, H. Mobahi, B. Neyshabur, ICLR 2021 — SAM.
- P. L. Bartlett et al., *JMLR* 24(43), 2023 — SAM dynamics.
- H. Liu et al., ICLR 2024 — Sophia.
- K. Jordan et al., 2024 — Muon.
- Jingyuan Liu et al., [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025 — Muon at LLM scale.
- I. Shah et al., [arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025 — Muon pretraining efficiency.

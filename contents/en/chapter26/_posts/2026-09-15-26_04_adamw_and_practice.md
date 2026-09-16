---
layout: post
title: 26-04 AdamW and training practice
chapter: '26'
order: 5
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: required
---


L2 regularization adds $$\frac{\lambda}{2}\|w\|_2^2$$ to the loss, so the gradient gains $$\lambda w$$. Under **Adam**, that term is immediately rescaled by $$1/(\sqrt{\hat v}+\varepsilon)$$. Coordinates with large second moments feel *less* decay than coordinates with small ones. The regularizer you thought you wrote is not the regularizer the optimizer applies.

**AdamW** (Loshchilov & Hutter, ICLR 2019, [arXiv:1711.05101](https://arxiv.org/abs/1711.05101)) **decouples** the decay:

$$
w_{k+1} = w_k - \eta \Bigl( \hat m \oslash (\sqrt{\hat v}+\varepsilon) + \lambda w_k \Bigr).
$$

Weight decay is now a true pull toward the origin in parameter space, independent of the adaptive scale. In PyTorch this is `torch.optim.AdamW`, not “Adam plus `weight_decay` on the old Adam” (the latter still couples on some versions — read the docs for the year you are coding).

## Practice knobs that are really optimization

- **Learning-rate schedules.** Warmup then cosine / linear decay is a time-varying $$\eta_k$$. Theory for convex SGD already wants decreasing steps; deep learning rediscovered it as “training recipes.”
- **Gradient clipping.** Replacing $$g$$ by $$g\cdot \min(1, \tau/\|g\|)$$ is a trust-region on the stochastic step — crude, and essential for RNNs and transformers.
- **Batch size vs $$\eta$$**. Linear scaling rules (Goyal et al.) treat a larger batch as a smaller-noise estimator that can bear a larger $$\eta$$, up to a breakdown regime.
- **Coupled vs decoupled decay.** If you report a “weight decay $$\lambda$$” in a paper, say whether it was AdamW-style.

Further reading (not core): SAM (Foret et al., ICLR 2021) asks for *flat* minima via a local max; Muon and Sophia are 2023–2025 optimizer-zoo case studies. The optional survey [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %}) is the one-page map; they are not assessed this term.

**Exercise.** Train a tiny MLP on a 2-D two-moons set with Adam and AdamW at the same $$\lambda$$. Plot $$\|w\|_2$$ over epochs. You should see different parameter-norm trajectories even when training loss looks similar.

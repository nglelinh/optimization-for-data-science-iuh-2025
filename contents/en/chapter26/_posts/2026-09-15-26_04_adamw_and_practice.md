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

For three years after Adam’s publication, practitioners noticed a puzzling empirical mystery: Adam trained faster than SGD+momentum on computer vision benchmarks, yet generalized noticeably worse—even with carefully tuned $$\ell_2$$ regularization. In 2017–2019, Ilya Loshchilov and Frank Hutter uncovered the culprit: inside Adam, $$\ell_2$$ regularization and weight decay are **not** equivalent! Adding $$\lambda w$$ inside the gradient gets divided by $$\sqrt{\hat{v}_t}$$, accidentally weakening regularization on weights with large historical gradients. Pulling weight decay *outside* the adaptive denominator gave birth to **AdamW**, the default optimizer of modern transformers.

## Key ideas: Decoupled Weight Decay and Optimization Practice Knobs

- **Why $$\ell_2$$ Regularization $$\ne$$ Weight Decay Under Adam:** In vanilla SGD, adding $$\frac{\lambda}{2}\|w\|_2^2$$ yields $$w_{t+1} = (1 - \eta \lambda) w_t - \eta g_t$$—identical to multiplicative weight decay. In Adam, adding $$\lambda w_t$$ to $$g_t$$ scales the decay by $$1 / (\sqrt{\hat{v}_t} + \varepsilon)$$, coupling regularization strength to gradient variance.
- **AdamW (Decoupled Weight Decay):** Updates $$w_{t+1} = (1 - \eta_t \lambda) w_t - \eta_t \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \varepsilon}$$, restoring uniform multiplicative decay across all weights regardless of their gradient history (and typically excluding biases and LayerNorm gains).
- **Warmup + Cosine Annealing:** Early in deep training, Adam’s second-moment estimate $$\hat{v}_t$$ has high variance and curvature is sharp; linear learning-rate warmup prevents early divergence, while cosine decay smoothly shrinks the stochastic noise ball at the end of training.
- **Gradient Clipping & Mixed Precision:** Global norm clipping ($$\text{clip}(\|g\|_2 \le c)$$) caps rare outlier-batch spikes in nonconvex landscapes without changing step direction, making deep transformer runs stable under FP16/BF16 arithmetic.

### Worked example: Adam+L2 vs. AdamW on Two Weights with Different Gradient Scales

Suppose two weights both sit at $$w_1 = w_2 = 1.0$$, with weight decay $$\lambda = 0.1$$, learning rate $$\eta = 0.1$$, and steady historical gradients $$g_1 = 0.01$$ (small-gradient coordinate) and $$g_2 = 10.0$$ (large-gradient coordinate), so $$\sqrt{\hat{v}_1} \approx 0.01$$ and $$\sqrt{\hat{v}_2} \approx 10.0$$.

1. **Under Adam with coupled $$\ell_2$$ regularization ($$\tilde{g}_i = g_i + \lambda w_i$$):**
   - Regularization shrinkage on $$w_1$$: $$\eta \frac{\lambda w_1}{\sqrt{\hat{v}_1}} = 0.1 \cdot \frac{0.1}{0.01} = 1.0$$ (crushes $$w_1$$ by **100%** in one step!).
   - Regularization shrinkage on $$w_2$$: $$\eta \frac{\lambda w_2}{\sqrt{\hat{v}_2}} = 0.1 \cdot \frac{0.1}{10.0} = 0.001$$ (shrinks $$w_2$$ by just **0.1%**!).
   The two weights receive **1000× different** effective decay rates!
2. **Under AdamW (decoupled weight decay):**
   - Regularization shrinkage on $$w_1$$: $$\eta \lambda w_1 = (0.1)(0.1)(1.0) = 0.01$$ (**1%** decay).
   - Regularization shrinkage on $$w_2$$: $$\eta \lambda w_2 = (0.1)(0.1)(1.0) = 0.01$$ (**1%** decay).
3. **Takeaway:** AdamW applies the exact intended $$1\%$$ multiplicative shrinkage uniformly across both coordinates, cleanly separating scale-invariant gradient steps from weight regularization.

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

Further reading (not core): SAM (Foret et al., ICLR 2021) asks for *flat* minima via a local max; Muon and Sophia are 2023–2025 optimizer-zoo case studies. The optional seminar [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %}) writes each update on the board (without repeating the Sophia-as-Newton reading in 14-10); they are not assessed this term.

**Exercise.** Train a tiny MLP on a 2-D two-moons set with Adam and AdamW at the same $$\lambda$$. Plot $$\|w\|_2$$ over epochs. You should see different parameter-norm trajectories even when training loss looks similar.

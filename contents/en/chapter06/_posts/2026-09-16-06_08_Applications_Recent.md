---
layout: post
title: 06-08 Applications and recent developments
chapter: '06'
order: 18
owner: Nguyen Le Linh
categories:
- chapter06
lang: en
lesson_type: optional
---

Chapter 06 developed gradient descent with a Lipschitz gradient, step-size rules, and the faster rate under strong convexity. That theory is still the right first picture — and it is *not* the whole picture of how people train networks in 2022–2026. This lesson adds three empirical and algorithmic developments you should be able to cite: the edge-of-stability regime for full-batch GD, a sign-based momentum method discovered by program search (Lion), and schedule-free averaging that removes the need to know $$T$$ in advance. Adaptive methods (AdamW) live in [Chapter 26]({{ site.baseurl }}/contents/en/chapter26/); we only mention them when a paper uses them as a baseline.

## Edge of stability: when the textbook step-size bound fails

If $$\nabla f$$ is $$L$$-Lipschitz, the standard descent lemma says that a *fixed* step $$t<2/L$$ makes $$f$$ decrease monotonically. Cohen, Kaur, Li, Kolter, and Talwalkar (*Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability*, [ICLR 2021](https://openreview.net/forum?id=jh-rTtvkGeM); [arXiv:2103.00065](https://arxiv.org/abs/2103.00065)) measured full-batch GD on modern nets and found a different regime: the largest Hessian eigenvalue $$\lambda_{\max}$$ *rises* until it hovers just above $$2/t$$, and the training loss oscillates on short windows while still trending down. That is incompatible with a global $$L$$ that you treat as fixed.

Arora, Li, and Panigrahi (*Understanding Gradient Descent on the Edge of Stability in Deep Learning*, [ICML 2022](https://proceedings.mlr.press/v162/arora22a.html)) gave a mechanism: after entering the edge-of-stability phase, iterates can follow a deterministic flow on a manifold of (near) minimal loss that *decreases* sharpness $$\lambda_{\max}(\nabla^2 L)$$. They prove the phenomenon for normalized GD and for GD on $$\sqrt{L-L^\star}$$ under regularity assumptions.

For this chapter, keep both statements in your head. The descent lemma is not wrong; the hypothesis “$$L$$ is constant along the path” is. When your homework assumes a quadratic upper bound (06-03-01), you are in the pre-edge regime. When a deep-learning paper says the run is “at the edge of stability,” they mean $$\lambda_{\max}\approx 2/t$$ and you should not expect monotone decrease.

## Lion: momentum with a sign

Chen, Liang, Huang, Real, Wang, Pham, Dong, Luong, Hsieh, Lu, Le, and colleagues (*Symbolic Discovery of Optimization Algorithms*, [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9a39b4925e35cf447ccba8757137d84f-Abstract-Conference.html); [arXiv:2302.06675](https://arxiv.org/abs/2302.06675); code in [google/automl/lion](https://github.com/google/automl/tree/master/lion)) searched a space of optimizer programs and found **Lion** (EvoLved Sign Momentum). The update keeps a single momentum buffer $$m$$ and steps in the *sign* of a blend of $$m$$ and the current gradient:

$$
\begin{align}
u_t &= \beta_1 m_{t-1} + (1-\beta_1) g_t,\\
\theta_t &= \theta_{t-1} - \eta\,\mathrm{sign}(u_t),\\
m_t &= \beta_2 m_{t-1} + (1-\beta_2) g_t.
\end{align}
$$

There is no second-moment preconditioner, so memory is closer to SGD-with-momentum than to Adam. The authors report ImageNet gains on ViT, compute savings on JFT and on diffusion training, and competitive language-model runs; they also document settings where the gain is small. Default practice is a *smaller* $$\eta$$ than AdamW, because $$\|\mathrm{sign}(u)\|_{\infty}=1$$ makes each coordinate step full size.

Chapter 06 already introduced momentum (06-06). Lion is that idea with a coordinate-wise sign — a non-Euclidean twist you can view as normalized steepest descent in the $$\ell_\infty$$ geometry. It is *not* a replacement for the convergence proofs in 06-03; those proofs assume smooth Euclidean steps.

## Schedule-free SGD and AdamW

Classical theory often wants a decreasing step size that depends on the horizon $$T$$ (or on a budget you announce in advance). Practitioners instead pick a cosine schedule that also depends on $$T$$. Defazio, Yang, Khaled, Mishchenko, Mehta, and Cutkosky (*The Road Less Scheduled*, [NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/136b9a13861308c8948cd308ccd02658-Abstract-Conference.html); [arXiv:2405.15682](https://arxiv.org/abs/2405.15682); [facebookresearch/schedule_free](https://github.com/facebookresearch/schedule_free)) interpolate an iterate-averaged sequence with a momentum-like base sequence so that *no* decreasing schedule is required. Schedule-Free AdamW was the core of their winning entry in the 2024 MLCommons AlgoPerf self-tuning track. Empirically the method tracks the Pareto frontier of “loss versus training time” that you would otherwise get by launching many cosine runs of different lengths.

The link to this chapter is Polyak–Ruppert averaging and momentum, not a new descent lemma. If you understand why averaging can replace a decaying step (the same intuition as 06-05’s noisy SGD), you can read the paper’s interpolation as a *practical* averaging scheme that finally matches tuned schedules.

## What to do in this course versus later

For homework and the midterm, use the Lipschitz and strong-convexity rates as written in 06-03. For a training log of a deep net, plot loss *and*, if you can afford it, a power-iteration estimate of $$\lambda_{\max}$$; expect edge-of-stability oscillations under full-batch GD. For a large stochastic run, start from AdamW or Schedule-Free AdamW (Chapter 26) and treat Lion as an alternative momentum baseline, not as the new default proof.

## Sources

1. J. M. Cohen, S. Kaur, Y. Li, J. Z. Kolter, and A. Talwalkar, “Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability,” ICLR 2021. [OpenReview](https://openreview.net/forum?id=jh-rTtvkGeM) · [arXiv:2103.00065](https://arxiv.org/abs/2103.00065)
2. S. Arora, Z. Li, and A. Panigrahi, “Understanding Gradient Descent on the Edge of Stability in Deep Learning,” ICML 2022. [PMLR](https://proceedings.mlr.press/v162/arora22a.html)
3. X. Chen et al., “Symbolic Discovery of Optimization Algorithms,” NeurIPS 2023. [abstract](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9a39b4925e35cf447ccba8757137d84f-Abstract-Conference.html) · [arXiv:2302.06675](https://arxiv.org/abs/2302.06675)
4. A. Defazio, X. Yang, A. Khaled, K. Mishchenko, H. Mehta, and A. Cutkosky, “The Road Less Scheduled,” NeurIPS 2024. [abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/136b9a13861308c8948cd308ccd02658-Abstract-Conference.html) · [arXiv:2405.15682](https://arxiv.org/abs/2405.15682)

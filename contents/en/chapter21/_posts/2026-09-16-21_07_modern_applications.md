---
layout: post
title: 21-08 Modern applications of ADMM
chapter: '21'
order: 9
owner: Nguyen Le Linh
categories:
- chapter21
lang: en
lesson_type: optional
---


The earlier lessons in this chapter treat ADMM as a *structured convex* splitting method: two (or more) easy proximal pieces, a dual ascent, and residuals you can monitor. That story did not retire in 2011. Between 2022 and 2026 the same consensus / augmented-Lagrangian pattern shows up in federated deep learning, computational imaging with learned denoisers, and online power-system dispatch. This optional note is a map of those deployments, not a second derivation of scaled ADMM.

Recall the consensus form from [21-05]({% multilang_post_url contents/chapter21/21-03-29-21_05_Consensus_ADMM %}):

$$
\min_{x_1,\ldots,x_B,z}\ \sum_{i=1}^B f_i(x_i)\qquad\text{subject to}\qquad x_i=z.
$$

Each client (or each imaging block, or each electrical area) owns a private $$f_i$$; the server only averages and updates duals. Everything below is a specialization of that template.

## 1. FedADMM: consensus learning when clients are heterogeneous

**Federated learning** (Chapter 29) usually averages *weights* after several local SGD steps (FedAvg). That is *not* ADMM: there is no dual residual, and local drift is intentional. A 2022–2023 line of work puts the dual back.

Gong, Li, and Freris ([arXiv:2204.03529](https://arxiv.org/abs/2204.03529), 2022) introduce **FedADMM**. Each client $$i$$ approximately minimizes its augmented Lagrangian (a few local SGD steps are allowed — an *inexact* $$x$$-update), the server averages the primals, and dual variables $$w_i$$ accumulate the disagreement $$x_i-z$$. Communication per round matches FedAvg, but the duals adapt to **statistical heterogeneity** without a hand-tuned proximal penalty. The same paper reports up to 87% fewer rounds than FedAvg/FedProx on CIFAR-10 / Fashion-MNIST under non-IID splits.

Zhou and Li, *Federated Learning via Inexact ADMM*, IEEE TPAMI 45(8):9699–9708, 2023, [doi:10.1109/TPAMI.2023.3243080](https://doi.org/10.1109/TPAMI.2023.3243080), give a companion theory: inexact local solves, partial participation, and a nonconvex objective. The message for this course is precise. If you can write a consensus program and you care about residuals, ADMM is still the right language. If the model is a deep net and the scarce resource is *rounds*, FedADMM is the 2020s dialect of [21-05]({% multilang_post_url contents/chapter21/21-03-29-21_05_Consensus_ADMM %}) — not a replacement for FedAvg, and not “just SGD with a Lagrange multiplier.”

A 2025–2026 medical follow-up (ADMM-enhanced FL on PIMA diabetes and chest X-rays) treats FedADMM as one more federated optimizer next to SCAFFOLD and FedDyn. That is an *application*, not a new algorithm: hospitals cannot pool images, and a primal-dual residual is a useful health check.

## 2. Plug-and-play ADMM in computational imaging

Image restoration is a textbook composite problem

$$
\min_x\ \tfrac12\|Ax-b\|_2^2 + g(x),
$$

where $$A$$ is blur / undersampling and $$g$$ is a regularizer. Classical ADMM uses $$\mathrm{prox}_g$$. **Plug-and-play (PnP) ADMM** replaces that prox by an off-the-shelf denoiser $$D_{\sigma}$$ — BM3D yesterday, a CNN today — and keeps the data-fidelity $$x$$-update.

Chan, Wang, and Elgendy, *IEEE Trans. Computational Imaging* 3:84–98, 2017 (online 2016), [doi:10.1109/TCI.2016.2629286](https://doi.org/10.1109/TCI.2016.2629286), proved fixed-point convergence for *bounded* denoisers under a continuation scheme, with super-resolution and single-photon imaging as the running examples. The 2022–2023 wave made the denoiser a deep network. Zhang, Li, Zuo, Zhang, Van Gool, and Timofte, *Plug-and-Play Image Restoration with Deep Denoiser Prior*, IEEE TPAMI 44(10):6360–6376, 2022, [doi:10.1109/TPAMI.2021.3088914](https://doi.org/10.1109/TPAMI.2021.3088914), drop a single trained DRUNet into many inverse problems. Hurault, Chambolle, Leclaire, and Papadakis ([arXiv:2210.10605](https://arxiv.org/abs/2210.10605), 2023) linearize the ADMM $$x$$-step so that a non-uniform blur operator never needs an inner CG solve. Shoushtari, Liu, Schniter, and Kamilov ([arXiv:2311.18810](https://arxiv.org/abs/2311.18810), 2023) explain why PnP-ADMM often converges even for *expansive* CNN denoisers if one interprets $$D_{\sigma}$$ as an MMSE estimator (hence a prox of a possibly nonconvex $$g$$).

The data-science takeaway: ADMM is a *modular interface*. One block is physics ($$A$$, Poisson likelihood); the other is a learned prior. You do not retrain a network for every camera. That is why computational-imaging groups still teach ADMM after everyone else moved to Adam.

## 3. Distributed optimal power flow

Optimal power flow (OPF) is a nonconvex QCQP on a grid: voltages, generation, and line limits. Areas refuse to share full network data, and renewables make the problem *online*. Consensus ADMM splits the grid at boundary buses: each area solves a local OPF, duals on the shared voltages enforce Kirchhoff agreement.

Wang, Pu, Huang, Yu, Shi, and Wang, *Online ADMM for Distributed Optimal Power Flow via Lagrangian Duality*, *Energies* 15(24):9525, 2022, [doi:10.3390/en15249525](https://doi.org/10.3390/en15249525), run consensus ADMM on the *dual* OPF so that only boundary multipliers move, and they do it *online* as distributed energy resources fluctuate. IEEE 30-bus experiments compare static versus dynamic OPF: the online ADMM iterate tracks renewable ramps without the violent generator chatter of a fully re-solved offline OPF. This is Boyd’s consensus template with a power-systems $$f_i$$, and it is a useful reminder that “distributed optimization” in 2026 is not only GPU all-reduce.

## What to keep, what to send to Chapter 29

| Application | What is split | What is averaged | Certificate |
|-------------|---------------|------------------|-------------|
| FedADMM | local training loss | primal $$z$$ and duals | residuals (and a nonconvex rate) |
| PnP imaging | data fidelity vs denoiser | the image / dual | fixed-point of a denoiser-prox |
| Distributed OPF | electrical areas | boundary voltages / multipliers | power-balance residual |
| FedAvg (Ch.29) | local ERM | **weights** after $$E$$ steps | none |

**Exercise.** Take the scaled consensus updates from 21-05 and write a 3-client FedADMM *sketch* (no training required): each client takes one gradient step on $$\frac12\|x_i-x_i^{\mathrm{data}}\|_2^2+\frac{\rho}{2}\|x_i-z+u_i\|_2^2$$, then average. Plot $$\|x_i-z\|$$ versus a FedAvg-style average-without-duals run. The dual run should pull the three $$x_i$$ together; the dual-free run should leave a gap equal to the data offset.

## Sources

- S. Boyd et al., *Foundations and Trends in ML* 3(1):1–122, 2011 — consensus ADMM.
- Y. Gong, Y. Li, N. M. Freris, [arXiv:2204.03529](https://arxiv.org/abs/2204.03529), 2022 — FedADMM.
- S. Zhou and G. Y. Li, *IEEE TPAMI* 45(8):9699–9708, 2023 — inexact ADMM for FL.
- S. H. Chan, X. Wang, O. A. Elgendy, *IEEE TCI* 3:84–98, 2017 — PnP-ADMM convergence.
- K. Zhang et al., *IEEE TPAMI* 44(10):6360–6376, 2022 — deep PnP denoisers.
- S. Hurault et al., [arXiv:2210.10605](https://arxiv.org/abs/2210.10605), 2023 — linearized PnP-ADMM.
- S. Shoushtari et al., [arXiv:2311.18810](https://arxiv.org/abs/2311.18810), 2023 — nonconvex PnP-ADMM.
- S. Wang, L. Pu, X. Huang, Y. Yu, Y. Shi, H. Wang, *Energies* 15(24):9525, 2022 — online distributed OPF.

---
layout: post
title: 21-09 Modern applications of ADMM
chapter: '21'
order: 10
owner: Nguyen Le Linh
categories:
- chapter21
lang: en
lesson_type: optional
---

Why does an algorithm formalized in the 1970s keep resurfacing in 2022–2026 top conferences across machine learning, computational imaging, and energy systems? Because **consensus ADMM** solves a universal systems bottleneck: decoupling *private local physics or data* (each client's GPU, each imaging forward model, each regional power grid) from *global coordination* through a lightweight dual price vector $$w_i$$. This companion note highlights how modern implementations adapt ADMM for non-IID federated rounds, neural-denoiser imaging, and real-time online power dispatch.

## Background Knowledge Map: Engineering Patterns in Modern ADMM Deployments

- **Communication-Efficient Federated Consensus (Gong et al., 2022):** FedADMM transmits the exact same payload per round as FedAvg (one model vector), yet cuts communication rounds dramatically on non-IID CIFAR-10 / Fashion-MNIST by using dual variables to correct local objective mismatch.
- **Inexact Primal Updates Without Breaking Convergence:** Modern deployments replace exact $$\arg\min_{x_i}$$ with a few steps of SGD, CG, or L-BFGS—preserving convergence as long as subproblem errors are summable or satisfy an adaptive relative-error check.
- **Operator-Splitting with Learned Priors (PnP / RED):** Viewing ADMM through monotone operator theory explains why replacing $$\operatorname{prox}_{g/\rho}$$ with a bounded-Lipschitz neural denoiser still converges to a stable fixed point balancing measurement fidelity and learned priors.
- **Online & Time-Varying Consensus (Smart Grids):** In online power dispatch, load demand $$y_t$$ changes every few seconds; warm-starting ADMM's primal and dual variables $$(x_i^t, z^t, w_i^t)$$ from the previous time slot tracks the moving optimum with just 1–5 iterations per second.

### Step-by-Step Worked Example (Read Slowly): Warm-Starting Online Consensus ADMM in Power Dispatch

Two regional power areas balance a time-varying total load by minimizing $$f_1(x_1) + f_2(x_2)$$ subject to a tie-line consensus variable $$z$$. Suppose at time $$t$$ the grid has converged to $$x_1^\star(t) = x_2^\star(t) = z^\star(t) = 10\text{ MW}$$ with dual prices $$w_1^\star(t) = -2, \; w_2^\star(t) = +2$$ (for $$\rho = 1$$, reflecting Area 1's cheaper cost $$f_1(x_1) = \frac{1}{2}(x_1 - 12)^2$$ and Area 2's cost $$f_2(x_2) = \frac{1}{2}(x_2 - 8)^2$$).

1. **A sudden load shift occurs at time $$t + 1$$:**
   Area 1's target shifts slightly to $$f_1^{\text{new}}(x_1) = \frac{1}{2}(x_1 - 13)^2$$ (new exact global optimum: $$z^\star(t+1) = 10.5\text{ MW}$$).
2. **Compare Cold-Start ($$z^0 = 0, w^0 = 0$$) vs. Warm-Start ($$z^0 = 10, w_1^0 = -2, w_2^0 = +2$$) after 1 ADMM step:**
   - **Cold-start:** $$x_1^1 = \frac{13 + 0}{2} = 6.5$$, $$x_2^1 = \frac{8 + 0}{2} = 4.0 \implies z^1 = 5.25\text{ MW}$$ (error **$$5.25\text{ MW}$$**!).
   - **Warm-start:**
     $$x_1^1 = \frac{13 + (10 - (-2))}{2} = 12.5, \qquad x_2^1 = \frac{8 + (10 - 2)}{2} = 8.0 \implies z^1 = \frac{12.5 + 8.0}{2} = 10.25\text{ MW}$$ (error only **$$0.25\text{ MW}$$**!).
3. **Takeaway:**
   Warm-starting both primal *and* dual variables reduced the tracking error by **21×** in a single iteration—showing why dual memory makes online ADMM ideal for real-time control!

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

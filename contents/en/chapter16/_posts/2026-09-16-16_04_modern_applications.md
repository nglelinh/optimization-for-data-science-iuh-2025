---
layout: post
title: 16-04 Modern applications of duality (2022–2026)
chapter: '16'
order: 5
owner: Nguyen Le Linh
categories:
- chapter16
lang: en
lesson_type: optional
---

When you read papers from 2022–2026 on aligning large language models with human feedback (InstructGPT / RLHF), training safe robots (OmniSafe), or computing single-cell trajectories with optimal transport, you might not expect to see Chapter 16's Lagrangians and Fenchel conjugates on page 2. Yet every one of those breakthroughs relies on the same three dual moves: turning a regularizer's conjugate into a **Fenchel–Young training loss**, pricing a KL divergence constraint with a **Lagrange multiplier**, and solving **entropic optimal transport** via its unconstrained Fenchel dual!

## Key ideas: Duality as a 2022–2026 ML Design Pattern

- **Pillar 1 — Fenchel–Young Losses:** For any convex regularizer $$\Omega$$, the Fenchel–Young gap $$L_\Omega(\theta; y) = \Omega^*(\theta) + \Omega(y) - \theta^T y \ge 0$$ is automatically a convex, nonnegative loss that equals $$0$$ iff $$y = \nabla\Omega^*(\theta)$$.
- **Pillar 2 — RLHF & DPO as Constrained Lagrangian Duality:** Maximizing expected reward subject to $$\mathrm{KL}(\pi \| \pi_{\mathrm{SFT}}) \le \varepsilon$$ produces the exact Lagrangian $$\mathbb{E}[r(x,y)] - \beta\,\mathrm{KL}(\pi \| \pi_{\mathrm{SFT}})$$, where $$\beta \ge 0$$ is the dual price of drifting from the reference model.
- **Pillar 3 — Primal–Dual Safe RL (CMDPs):** Algorithms like PPO-Lagrangian run primal policy steps alternating with dual-ascent updates $$\lambda_{k+1} = [\lambda_k + \eta(J_C(\pi_k) - d)]_+$$ to enforce safety budgets.
- **Pillar 4 — Sinkhorn Potentials as Fenchel Duals:** Entropic optimal transport dualizes the marginal constraints into an unconstrained concave maximization over dual potentials $$(f, g)$$, enabling GPU-parallel Sinkhorn iterations.

### Worked example: Deriving Cross-Entropy as a Fenchel–Young Loss

Let $$\Omega(p) = \sum_{i=1}^K p_i \log p_i + I_{\Delta_K}(p)$$ be the negative entropy on the probability simplex $$\Delta_K$$.

1. **Compute the conjugate $$\Omega^*(\theta) = \max_{p \in \Delta_K} \left(\theta^T p - \sum_{i=1}^K p_i \log p_i\right)$$:**
   - Introducing Lagrange multiplier $$\nu$$ for $$\sum_i p_i = 1$$ gives $$\theta_i - \log p_i - 1 - \nu = 0 \implies p_i^\star = \frac{e^{\theta_i}}{\sum_j e^{\theta_j}} = \operatorname{softmax}(\theta)_i$$.
   - Substituting $$p^\star$$ back into $$\theta^T p - \sum p_i \log p_i$$ yields the log-sum-exp function:
     $$\Omega^*(\theta) = \log\left(\sum_{j=1}^K e^{\theta_j}\right).$$
2. **Evaluate the Fenchel–Young loss for a one-hot label $$y = e_c$$ (where $$\Omega(e_c) = 0$$):**
   $$L_\Omega(\theta; e_c) = \Omega^*(\theta) + \Omega(e_c) - \theta^T e_c = \log\left(\sum_{j=1}^K e^{\theta_j}\right) - \theta_c = -\log\big(\operatorname{softmax}(\theta)_c\big).$$
3. **Numerical check for $$K = 2$$, logits $$\theta = (1, 0)^T$$, true class $$c = 1$$:**
   - $$\Omega^*(\theta) = \log(e^1 + e^0) = \log(3.7183) \approx 1.3133$$.
   - $$L_\Omega(\theta; e_1) = 1.3133 + 0 - 1 = 0.3133 = -\log(0.7311)$$—exact cross-entropy loss, born directly from Fenchel duality!

Chapter 16 revisits Lagrangian duality, KKT, and Fenchel conjugates so that the primal-dual interior-point method of Chapter 17 has somewhere to stand. The same three objects — a Lagrangian, a dual variable that prices a constraint, and a Fenchel conjugate that swaps a loss for a regulariser — are how 2022–2026 machine learning *writes objectives*, not only how it proves them. The four applications below keep the math of this chapter visible: you should be able to name the primal, the constraint, and the dual variable in each story.

## Fenchel–Young losses: conjugates as training objectives

Blondel, Martins, and Niculae (JMLR 2020) define a **Fenchel–Young loss** from a regularised prediction function. If $$\Omega$$ is a convex regulariser on the simplex (or a structured set) and $$\Omega^\star$$ is its conjugate, the loss

$$
L_\Omega(\theta; y) = \Omega^\star(\theta) + \Omega(y) - \theta^\top y
$$

is exactly the Fenchel–Young gap from [16-03]({% multilang_post_url contents/chapter16/21-03-31-16_03_fenchel_duality %}). Cross-entropy is the special case $$\Omega = \text{negentropy}$$; sparse and structured losses appear by changing $$\Omega$$. The construction is older than 2022, but it became a *design pattern* in the years that followed. Blondel, Llinares-López, Dadashi, Hussenot, and Geist (NeurIPS 2022) lift it to energy networks by replacing the bilinear pairing with a general coupling (a generalised conjugate, including the $$C$$-transform of optimal transport). In 2025, sharpened Fenchel–Young losses are used for inverse unbalanced OT and inverse JKO gradient flows — including cell-population dynamics in single-cell genomics (arXiv:2505.07124).

The classroom move is to take a loss you already know, write it as $$\Omega^\star(\theta)-\theta^\top y+\Omega(y)$$, and read the dual variable as a *prediction* rather than as a Lagrange multiplier. Duality is no longer only a certificate; it is the loss.

## RLHF: a KL constraint and its Lagrange multiplier

Ouyang et al. (NeurIPS 2022), *Training language models to follow instructions with human feedback* (InstructGPT), fine-tune a supervised model with PPO against a reward model, plus a **per-token KL penalty** that keeps the policy near the SFT reference. The standard RLHF objective is the Lagrangian of

$$
\max_\pi\ \mathbb{E}_{x\sim\mathcal{D},\, y\sim\pi(\cdot\mid x)}\bigl[r_\theta(x,y)\bigr]
\quad\text{subject to}\quad
\mathbb{E}\bigl[\mathrm{KL}(\pi(\cdot\mid x)\,\|\,\pi_{\mathrm{SFT}}(\cdot\mid x))\bigr] \le \varepsilon.
$$

The coefficient on the KL term is the dual variable of a divergence constraint. Increasing it is a dual ascent step: you raise the price of leaving the reference until the constraint is tolerable. Later alignment recipes (DPO and its cousins) rewrite the *same* Lagrangian so that the optimal policy has a closed form and the dual coefficient becomes a temperature; the duality is still there, just solved analytically.

This is the Chapter 16 story that students have already used as chatbots: strong duality is not claimed for a nonconvex policy class, but the *modelling* — constrain first, price the constraint, read the multiplier as a knob — is Lagrangian duality in production.

## Safe RL: primal–dual loops you can run

Constrained MDPs ask for a policy that maximises return subject to an expected-cost budget. PPO-Lagrangian and TRPO-Lagrangian (OpenAI Safety Gym, Ray et al. 2019) update the policy by PPO/TRPO and the multiplier by dual ascent on the cost residual — the textbook primal-dual method on a stochastic, nonconvex saddle. CPO (Achiam et al., 2017) linearises the constraint and solves a small QP; IPO (Chapter 15) uses a barrier instead of a multiplier. OmniSafe (Ji et al., JMLR 2024) and Safety Gymnasium (Ji et al., NeurIPS 2023) package these algorithms so that a 2024–2026 project can *compare* barrier, primal-dual, and trust-region duals on the same robots.

Paternain, Chamon, Calvo-Fullana, and Ribeiro (and the 2022 line of primal-dual SafeRL) give the convex-analytic backbone: the dual function of a CMDP is a concave program in the multiplier, and a small duality gap controls constraint violation. That is [16-01]({% multilang_post_url contents/chapter16/21-03-31-16_01_lagrangian_duality_revisited %}) with an expectation inside every inner product.

## Optimal transport as a Fenchel dual

Entropic optimal transport,

$$
\min_{\pi\in\Pi(\mu,\nu)}\ \langle C,\pi\rangle + \varepsilon\,\mathrm{KL}(\pi\,\|\,\mu\otimes\nu),
$$

has a Fenchel dual that is an unconstrained concave maximisation over two potentials — the Sinkhorn dual. Computational OT (Peyré & Cuturi's monograph; the POT library) is how single-cell, domain adaptation, and generative-modelling papers in 2022–2026 move mass between empirical measures. Generalized Fenchel–Young losses (NeurIPS 2022) make the $$C$$-transform of that dual into a *training loss* for energy models. If Fenchel duality in 16-03 felt abstract, this is the picture: the conjugate of a transport cost is a potential, and fitting those potentials is supervised learning.

## Sources

- M. Blondel, A. F. T. Martins, V. Niculae, “Learning with Fenchel-Young Losses,” JMLR 21(35), 2020.
- M. Blondel, F. Llinares-López, R. Dadashi, L. Hussenot, M. Geist, “Learning Energy Networks with Generalized Fenchel-Young Losses,” NeurIPS 2022.
- “Learning from Samples: Inverse Problems over Measures via Sharpened Fenchel-Young Losses,” 2025. [arXiv:2505.07124](https://arxiv.org/abs/2505.07124)
- L. Ouyang et al., “Training language models to follow instructions with human feedback,” NeurIPS 2022.
- J. Ji et al., “OmniSafe,” JMLR 25(285), 2024; “Safety Gymnasium,” NeurIPS 2023 Datasets.
- S. Paternain et al., primal-dual methods for constrained RL (2022 line); G. Peyré, M. Cuturi, *Computational Optimal Transport*.

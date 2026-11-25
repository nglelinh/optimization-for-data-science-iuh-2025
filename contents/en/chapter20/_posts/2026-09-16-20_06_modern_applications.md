---
layout: post
title: 20-06 Modern applications of dual methods (2022–2026)
chapter: '20'
order: 14
owner: Nguyen Le Linh
categories:
- chapter20
lang: en
lesson_type: optional
---

In 2017, Federated Averaging (FedAvg) became the standard recipe for training machine learning models across phones and hospitals without centralizing raw data. Yet whenever clients hold *non-IID* (heterogeneous) data, FedAvg suffers from **client drift**: each local optimizer pulls weights toward its own local optimum, and naive averaging stalls far from the global minimizer. Between 2022 and 2026, **FedADMM** and **FedADMM-InSa** solved client drift using the exact lesson of Chapter 20: add a dual variable $$u_i$$ to price the consensus constraint $$w_i = z$$!

## Background Knowledge Map: Dual Methods Inside Modern Federated Learning

- **Federated Consensus Formulation:** Minimizing $$\sum_{i=1}^N f_i(w_i)$$ subject to $$w_i = z$$ casts federated learning directly as Chapter 20's equality-constrained decomposition problem, where client $$i$$ keeps its private loss $$f_i$$ on-device.
- **Why FedAvg Drifts Under Heterogeneity:** FedAvg drops the dual multipliers $$u_i$$ completely. At the global optimum $$z^\star$$, individual local gradients $$\nabla f_i(z^\star) \neq 0$$ even though $$\sum_i \nabla f_i(z^\star) = 0$$—so local SGD steps push clients *away* from $$z^\star$$!
- **Dual Multipliers Cancel Local Bias:** In FedADMM, each client's dual variable converges to $$u_i^\star = -\nabla f_i(z^\star)$$, shifting client $$i$$'s local augmented objective so that $$z^\star$$ becomes a *stationary point of every single client's subproblem*!
- **Inexactness & Self-Adaptive Penalties (FedADMM-InSa, 2024):** Modern federated ADMM allows clients to run just a few local SGD steps (verifying an implementable local residual test) while adapting $$\beta_i^k$$ automatically to handle stragglers and partial participation.

### Step-by-Step Worked Example (Read Slowly): Seeing Dual Variables Cure Client Drift on 2 Heterogeneous Clients

Suppose two clients have conflicting 1D quadratic losses: $$f_1(w_1) = \frac{1}{2}(w_1 - 2)^2$$ (local optimum $$2$$) and $$f_2(w_2) = \frac{1}{2}(w_2 + 2)^2$$ (local optimum $$-2$$). The true global consensus optimum is $$z^\star = 0$$.

1. **Watch FedAvg drift if each client minimizes locally from $$z^0 = 0$$:**
   Client 1 jumps to $$w_1 = 2$$, Client 2 jumps to $$w_2 = -2$$. Even though their average is $$0$$, if Client 1 has weight $$2$$ ($$f_1(w_1) = (w_1 - 2)^2$$, so global optimum is $$z^\star = 2/3$$), taking multiple local GD steps with $$\eta = 0.25$$ pushes Client 1 to $$2$$ and Client 2 to $$-2$$, whose average is $$0 \neq \frac{2}{3}$$—a permanent bias!
2. **Now run FedADMM ($$\beta = 1$$) with dual variables $$u_1, u_2$$ on $$f_1(w_1) = (w_1 - 2)^2$$ and $$f_2(w_2) = \frac{1}{2}(w_2 + 2)^2$$:**
   At the exact global optimum $$z^\star = \frac{2}{3}$$:
   - $$\nabla f_1(2/3) = 2(2/3 - 2) = -\frac{8}{3} \implies u_1^\star = +\frac{8}{3}$$.
   - $$\nabla f_2(2/3) = (2/3 + 2) = +\frac{8}{3} \implies u_2^\star = -\frac{8}{3}$$.
   Check client 1's local augmented Lagrangian stationarity at $$w_1 = z^\star = 2/3$$:
   $$\nabla f_1(w_1) + u_1^\star + \beta(w_1 - z^\star) = -\frac{8}{3} + \frac{8}{3} + 0 = 0!$$
   Check client 2's local stationarity at $$w_2 = z^\star = 2/3$$:
   $$\nabla f_2(w_2) + u_2^\star + \beta(w_2 - z^\star) = +\frac{8}{3} - \frac{8}{3} + 0 = 0!$$
   Because the dual multipliers $$u_i^\star$$ absorb each client's local gradient bias identically, *zero* client drift occurs at $$z^\star$$!

Dual (sub)gradient, dual decomposition, augmented Lagrangians, and the first look at ADMM in this chapter all share one move: *price a consensus or resource constraint and let each block optimise independently*. That is also the move behind federated learning. A 2026 student who has already seen FedAvg in Chapter 29 should recognise FedADMM as Chapter 20 with a server: the dual variable is the running price of “your local model must match the global model.”

## FedADMM: dual variables against client heterogeneity

Zhou and Li (2022/23, [arXiv:2204.10607](https://arxiv.org/abs/2204.10607)) formulate federated empirical risk as a consensus problem and apply an **inexact ADMM**. Clients may solve their augmented-Lagrangian subproblems approximately; the server may skip stragglers; communication need not happen every local step. The dual variables absorb statistical heterogeneity that FedAvg treats only by averaging. Subsequent FedADMM variants (Gong et al. 2022; Wang et al. 2023; Zhang et al. 2021) keep that skeleton.

**FedADMM-InSa** (Song, Wang, and Zuazua, 2024, [arXiv:2402.13989](https://arxiv.org/abs/2402.13989)) adds two missing pieces from this chapter's practice sheet: an *implementable inexactness test* that each client can evaluate from local residuals, and a *self-adaptive penalty* $$\beta_i^k$$ that plays the role of the AL parameter you tuned by hand in 20-03. On their reported tests the combination raises accuracy by about 8% while cutting local work by about 56% versus the baselines they compare. The algorithm is not a new duality theorem; it is dual decomposition with the safeguards Boyd, Parikh, Chu, Peleato, and Eckstein already recommended, engineered for FL's partial participation.

Write the consensus form once,

$$
\min_{w_1,\ldots,w_N,z}\ \sum_{i=1}^N f_i(w_i)\quad\text{s.t.}\quad w_i=z,
$$

and the rest of Chapter 20 is the method: dualise $$w_i=z$$, take an AL term $$\frac{\beta}{2}\|w_i-z\|_2^2$$, and alternate $$w_i$$, $$z$$, and the multipliers. FedAvg is the special case that throws the multipliers away and takes one gradient step on $$f_i$$.

## Decentralised dual constraints: DFedADMM

When there is no server, consensus is a graph. **DFedADMM** and **DFedADMM-SAM** (Li, Shen, Li, Yin, and Tao, 2023, [arXiv:2308.08290](https://arxiv.org/abs/2308.08290)) put a dual variable on each edge (or neighbour disagreement) so that heterogeneous local objectives cannot drift independently. SAM (sharpness-aware minimisation) is an extra local regulariser against heterogeneous overfitting; the *dual* part is Chapter 20. The paper gives nonconvex rates that depend on the spectral gap of the gossip matrix — the same graph Laplacian that appears in classical consensus ADMM.

This is the right reading for students who will meet gossip SGD in distributed systems: first-order gossip is dual decomposition with a unit-step dual update and no AL; DFedADMM restores the AL and the dual memory.

## Federated RL: ADMM on a natural-policy-gradient step

Khodadadian, Chen, Maguluri, and collaborators / the NeurIPS 2023 paper “Improved Communication Efficiency in Federated Natural Policy Gradient via ADMM-based Gradient Updates” replace an $$O(d^2)$$ Fisher solve by an ADMM splitting that communicates $$O(d)$$ numbers per round. Federated NPG is a second-order policy step (a cousin of Chapter 14); the communication reduction is *dual decomposition of that Newton system*. The experiments on MuJoCo tasks show reward on par with full FedNPG and communication comparable to first-order FedPPO.

The pattern to remember: whenever a federated method wants a *coupled* local Newton or projection, ADMM is how you decouple it without sending a matrix.

## Dual decomposition outside the datacenter

The same block-separable dual is how power-system OPF, multi-period energy dispatch, and some privacy-preserving medical models are still solved in 2022–2026: each agent keeps $$x_i$$, a coordinator updates $$\lambda$$ on the linking constraints (flow balance, shared risk). Bayesian-ADMM (2025, [arXiv:2506.13150](https://arxiv.org/abs/2506.13150)) recasts the ADMM fixed point as a variational-Bayes duality and recovers Newton-like and Adam-like federated variants by changing the exponential-family posterior — a survey-level pointer, not a new required algorithm.

Chapter 29 will contrast FedAvg with ADMM as *systems* choices. This lesson is the optimisation reason they differ: **dual variables are the memory of violated consensus**. If you delete them, you get averaging. If you keep them and a quadratic AL, you get the methods of this chapter, which is why they reappear every time federated data are heterogeneous.

## Sources

- S. Zhou, G. Y. Li, “Federated Learning via Inexact ADMM,” 2022. [arXiv:2204.10607](https://arxiv.org/abs/2204.10607)
- Y. Song, Z. Wang, E. Zuazua, “FedADMM-InSa: An Inexact and Self-Adaptive ADMM for Federated Learning,” 2024. [arXiv:2402.13989](https://arxiv.org/abs/2402.13989)
- Q. Li, L. Shen, G. Li, Q. Yin, D. Tao, “DFedADMM: Dual Constraints Controlled Model Inconsistency for Decentralized Federated Learning,” 2023. [arXiv:2308.08290](https://arxiv.org/abs/2308.08290)
- “Improved Communication Efficiency in Federated Natural Policy Gradient via ADMM-based Gradient Updates,” NeurIPS 2023.
- “Federated ADMM from Bayesian Duality,” 2025. [arXiv:2506.13150](https://arxiv.org/abs/2506.13150)
- S. Boyd, N. Parikh, E. Chu, B. Peleato, J. Eckstein, “Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers,” *Found. Trends Mach. Learn.* 2011 (the skeleton all of the above reuse).

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

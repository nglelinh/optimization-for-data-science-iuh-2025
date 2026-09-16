---
layout: post
title: 12-09 Modern applications of the KKT conditions
chapter: '12'
order: 10
owner: Nguyen Le Linh
categories:
- chapter12
lang: en
lesson_type: optional
---

# Modern applications of the KKT conditions

Chapter 12 states the KKT system — primal feasibility, dual feasibility, complementary slackness, and stationarity of the Lagrangian — and works the SVM, water-filling, and $$\ell_1$$ examples. This optional lesson shows where that *system* is solved, differentiated, or read as a price in 2022–2026 software. We do not re-list the four blocks.

## 1. Differentiating through a solver: cvxpylayers and Theseus

If $$x^\star(\theta)$$ is the unique solution of a parametrized convex program, the implicit-function theorem applied to the KKT map $$F(x,u,v;\theta)=0$$ yields $$\mathrm{d}x^\star/\mathrm{d}\theta$$ without unrolling the solver. Agrawal, Amos, Barratt, Boyd, Diamond, and Kolter (NeurIPS 2019) shipped that idea as **cvxpylayers** (PyTorch / JAX / MLX). It is still the default way, in 2024–2026, to put a QP or SOCP *inside* a net: portfolio layers (DeepDow), MPC policies, and sparsemax-type projections.

Pineda, Fan, Monge, Venkataraman, Sodhi, Chen, Ortiz, DeTone, Wang, Anderson, Dong, Amos, and Mukadam (NeurIPS 2022) released **Theseus**, a GPU library for differentiable *nonlinear* least squares used in robotics and vision. The backward pass is again implicit differentiation of the stationarity (Gauss–Newton / Levenberg–Marquardt) conditions — KKT for an equality-constrained or regularised NLS. The 2022 paper is the one to cite; the repo is what a SLAM / bundle-adjustment stack actually imports.

**Course link.** Stationarity $$\nabla_x L=0$$ is the linear system Theseus differentiates. Complementary slackness appears as soon as the layer has inequalities (cvxpylayers).

## 2. SVM support vectors are a KKT statement

The example [12-04]({% multilang_post_url contents/chapter12/21-04-02-12_04_Example_support_vector_machines %}) is not ornamental. Complementary slackness says a point with $$0<\alpha_i<C$$ lies on the margin, a point with $$\alpha_i=0$$ is correctly classified with slack, and a point with $$\alpha_i=C$$ is a bound support vector. Kernel SVM remains a standard tool in 2022–2026 small-$$n$$ scientific ML (chemoinformatics, EEG, tabular clinical data) precisely because that finite set of vectors *is* the model. When a paper reports “47 support vectors,” it is reporting the active set of a KKT system.

## 3. Electricity LMPs and complementary slackness

Locational marginal prices are the dual variables of power-balance and flow limits (Chapter 10). Liang and Dvorkin (2023) invert published LMPs to recover offer prices; the inversion is possible because, at a nondegenerate clearing point, KKT identifies which inequalities bind. Donti, Rolnick, and Kolter (2021) train DC3 so that the network’s output is driven toward a KKT-feasible OPF point. Water-filling in [12-03]({% multilang_post_url contents/chapter12/21-04-02-12_03_Example_water_filling %}) is the same complementary-slackness picture in a Gaussian channel; 5G / 6G power-allocation papers still write that water level as a multiplier of a total-power inequality.

## 4. Fairness: which group constraint is tight?

In a Fairlearn / reductions fit (Weerts et al., 2023), a large multiplier on equalised odds for group $$a$$ means that group’s rate constraint is **binding** — complementary slackness in prose. A zero multiplier means the unconstrained model already satisfied that rate. Reading $$(x^\star,v^\star)$$ is therefore a debugging tool: it tells you *which* sociotechnical constraint is expensive, not only that the Lagrangian was minimised.

## What to remember

KKT is the first-order system that (i) characterises a convex constrained optimum, (ii) can be differentiated to train a layer, and (iii) names the resources that have a price. If a 2024 paper “embeds a QP in a net” or “reports support vectors” or “publishes an LMP,” it is talking about that system.

**Question.** Why does implicit differentiation of KKT need a constraint qualification and a nonsingular KKT Jacobian — and what fails in a Lasso layer when two features are identical?

## Sources

- Agrawal, A., Amos, B., Barratt, S., Boyd, S., Diamond, S., & Kolter, J. Z. (2019). Differentiable convex optimization layers. *NeurIPS*. Library: [cvxpylayers](https://www.cvxpylayers.org/)
- Pineda, L., Fan, T., Monge, M., Venkataraman, S., Sodhi, P., Chen, R. T. Q., Ortiz, J., DeTone, D., Wang, A., Anderson, S., Dong, J., Amos, B., & Mukadam, M. (2022). Theseus: A library for differentiable nonlinear optimization. *NeurIPS*. [arXiv:2207.09442](https://arxiv.org/abs/2207.09442)
- Liang, Z., & Dvorkin, Y. (2023). Data-driven inverse optimization for marginal offer price recovery in electricity markets. *ACM e-Energy ’23*.
- Donti, P. L., Rolnick, D., & Kolter, J. Z. (2021). DC3: A learning method for optimization with hard constraints. *ICLR*.
- Weerts, H., Dudík, M., Edgar, R., Jalali, A., Lutz, R., & Madaio, M. (2023). Fairlearn: Assessing and improving fairness of AI systems. *JMLR*, 24(257).

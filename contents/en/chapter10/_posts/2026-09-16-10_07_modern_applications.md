---
layout: post
title: 10-09 Modern applications of LP duality
chapter: '10'
order: 10
owner: Nguyen Le Linh
categories:
- chapter10
lang: en
lesson_type: optional
---

# Modern applications of LP duality

Chapter 10 derives the dual of a linear program, weak/strong duality, complementary slackness, and the max-flow / min-cut and matrix-game examples. This optional lesson shows four places where those *same* certificates were used in CS and data-science systems from about 2022 to 2026.

A primal LP $$\min\{c^\top x:Ax=b,\,Gx\le h\}$$ and its dual still mean: every feasible dual pair $$(u,v)$$ is a **lower bound**, and at optimality the bound is tight and unused inequalities have zero multipliers.

## 1. Neural-network verification as an LP (then a cut LP)

Asking whether a classifier can change its label inside an $$\ell_\infty$$ box is a nonconvex problem in the ReLU activations. The standard relaxation replaces each ReLU by a triangle / LP outer approximation (Ehlers; Wong and Kolter). Dual variables of that LP are **bound-propagation multipliers**. Zhang, Wang, Xu, Li, Li, Jana, Hsieh, and Kolter (NeurIPS 2022) added **general cutting planes** to that dual (GCP-CROWN) and folded it into **$$\alpha,\beta$$-CROWN**, which won the International Verification of Neural Networks Competition in 2021, 2022, 2023, 2024, and 2025. The engineering is GPU bound-propagation; the certificate is still “the dual of a tightened LP is above zero, hence no adversarial example exists.”

This is Chapter 10’s weak duality used as a **safety proof**, not as a pricing story.

## 2. Electricity markets: clearing LPs and shadow prices

Day-ahead energy markets clear a (mixed-integer) linear program: minimise offer cost subject to power-balance and line limits. The dual of the *linear* relaxation is the vector of **locational marginal prices** (LMPs). After the 2022 European price spike, that dual was no longer a textbook cartoon: it is the number on the invoice. Liang and Dvorkin (ACM e-Energy 2023) use inverse optimization on published schedules and LMPs to recover generators’ offer prices — they invert the KKT / dual map of the clearing LP. Related 2022–2023 work on European day-ahead auctions writes zonal prices explicitly as duals of network-constrained welfare LPs.

**Course link.** Complementary slackness says a congested line ($$Gx=h$$) is the only line that can carry a nonzero congestion price $$v$$. That sentence is this chapter, applied to a grid.

## 3. Max-flow / min-cut after 2022

The theorem in [10-03]({% multilang_post_url contents/chapter10/21-03-22-10_03_Max_flow_and_min_cut %}) is still the dual pair behind image segmentation, closed-world community detection, and reliability cuts in communication networks. Modern large-scale solvers (Gurobi, HiGHS, OR-Tools) expose the dual as a first-class vector; a data-science workflow that “allocates bandwidth” or “cuts a graph into source/sink sets” is reading that vector. The *new* CS use is often a **learned** capacity (a GNN predicts edge weights) followed by a classical max-flow dual as a layer — the same pairing as differentiable optimization in Chapter 12, but the inner problem is an LP.

## 4. Optimal transport as a giant LP

The Kantorovich problem

$$
\min_{\pi\ge 0}\ \langle C,\pi\rangle\quad\text{s.t.}\quad \pi\mathbf{1}=a,\ \pi^\top\mathbf{1}=b
$$

is an LP. Its dual is $$\max_{f,g} f^\top a+g^\top b$$ subject to $$f_i+g_j\le C_{ij}$$ — the **Kantorovich potentials**. Peyré and Cuturi (2019) is the computational monograph; 2022–2026 domain adaptation, dataset distillation, and single-cell alignment still solve a regularised (Sinkhorn) or unregularised version and read the dual as a soft matching. Weak duality is the statement that no coupling can cost less than any feasible pair of potentials.

## What to remember

An LP dual is a **certificate**: of infeasibility (verification), of a price (markets), of a cut (networks), or of a matching cost (transport). If you can write the primal and produce a feasible dual with equal objective, you are done — that is strong duality for LPs, and it is what those four applications compute.

**Question.** In GCP-CROWN, why does *adding* a cutting plane to the primal LP only *raise* the dual lower bound? Which theorem of this chapter is that?

## Sources

- Zhang, H., Wang, S., Xu, K., Li, L., Li, B., Jana, S., Hsieh, C.-J., & Kolter, J. Z. (2022). General cutting planes for bound-propagation-based neural network verification. *NeurIPS*. [arXiv:2208.05740](https://arxiv.org/abs/2208.05740). Tool: [α,β-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN) (VNN-COMP 2021–2025 winner).
- Liang, Z., & Dvorkin, Y. (2023). Data-driven inverse optimization for marginal offer price recovery in electricity markets. *ACM e-Energy ’23*.
- Peyré, G., & Cuturi, M. (2019). Computational optimal transport. *Foundations and Trends in Machine Learning*, 11(5–6). (standard LP/dual reference still used in 2022–2026 OT pipelines)
- Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*, Ch. 5 (LP duality and shadow prices).

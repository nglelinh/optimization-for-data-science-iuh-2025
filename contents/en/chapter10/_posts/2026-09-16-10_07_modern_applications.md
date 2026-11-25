---
layout: post
title: 10-07 Modern applications of LP duality
chapter: '10'
order: 8
owner: Nguyen Le Linh
categories:
- chapter10
lang: en
lesson_type: optional
redirect_from:
  - /contents/en/chapter10/10_09_modern_applications/
---

Linear programming duality might be seventy-five years old, but between 2022 and 2026 it became one of the sharpest weapons in modern computer science and infrastructure engineering. When a neural-network verifier certifies that an autonomous-driving perception model cannot be fooled inside an $$\ell_\infty$$ box, when an electricity grid operator computes real-time locational marginal prices (LMPs) every five minutes, or when a generative model computes Wasserstein optimal transport distances, the core mathematical engine is literally a dual LP certificate!

## Background Knowledge Map: LP Duality in 2022–2026 Systems

- **Pillar 1 — Neural-Network Verification via Dual Bounds ($$\alpha,\beta$$-CROWN):** Relaxing ReLU activations to their convex triangle envelope yields an LP whose *any* dual-feasible point gives a sound, certified lower bound on the worst-case margin—allowing GPU-parallel dual ascent to verify robustness without solving the primal LP to completion.
- **Pillar 2 — Electricity Markets & Locational Marginal Prices (LMPs):** Economic dispatch clears power generation via a large-scale LP subject to transmission-line limits; the optimal dual variables on nodal power-balance constraints *are* the real-time electricity prices paid to generators and charged to utilities.
- **Pillar 3 — Near-Linear-Time Max-Flow / Min-Cut (2022 Breakthrough):** Chen et al. (2022) solved minimum-cost flow and max-flow in almost-linear time $$O(m^{1 + o(1)})$$ using interior-point primal–dual updates and dynamic data structures, closing a decades-old algorithmic frontier.
- **Pillar 4 — Optimal Transport & Kantorovich Duality:** Matching two empirical probability distributions $$\mu, \nu$$ at minimum Earth Mover's cost is a giant LP whose dual maximizes $$\mathbb{E}_\mu[\phi] - \mathbb{E}_\nu[\psi]$$ over $$1$$-Lipschitz Kantorovich potentials—the exact foundation of Wasserstein distances in ML.

### Step-by-Step Worked Example (Read Slowly): Computing a Sound Dual Robustness Certificate for a Tiny ReLU Relaxation

Suppose verifying a neural network boils down to checking whether $$p^\star = \min \{ x_2 : x_2 \ge 0,\; x_2 \ge 2x_1 - 1,\; 0 \le x_1 \le 1 \}$$ is strictly above $$-0.5$$ (safe). We want a **certified lower bound** using *any* dual-feasible multiplier without even solving the primal!

1. **Rewrite constraints in $$\le$$ form:**
   $$-x_2 \le 0 \;(u_1), \quad 2x_1 - x_2 \le 1 \;(u_2), \quad -x_1 \le 0 \;(u_3), \quad x_1 \le 1 \;(u_4).$$
2. **Form the dual objective and constraints ($$c = (0, 1)^\top$$):**
   - Dual objective to maximize: $$-h^\top u = -u_2 - u_4$$.
   - Dual constraints $$-G^\top u = c$$:
     - For $$x_1$$: $$-2u_2 + u_3 - u_4 = 0$$.
     - For $$x_2$$: $$u_1 + u_2 = 1$$.
     - With $$u_1, u_2, u_3, u_4 \ge 0$$.
3. **Evaluate an instant dual-feasible point:** Pick $$u_1 = 1, u_2 = 0, u_3 = 0, u_4 = 0$$.
   - Check feasibility: $$-2(0) + 0 - 0 = 0$$ and $$1 + 0 = 1$$. Valid!
   - Certified lower bound: $$d = -0 - 0 = 0 > -0.5$$!
4. **Why verifiers love the dual:** Even a suboptimal or early-stopped dual point yields a **100% mathematically sound** lower bound ($$p^\star \ge d = 0 > -0.5$$), whereas an early-stopped primal point only gives an upper bound and can never certify safety!

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

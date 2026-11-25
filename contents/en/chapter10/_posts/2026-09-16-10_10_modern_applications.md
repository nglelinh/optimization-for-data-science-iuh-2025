---
layout: post
title: 10-10 Modern applications of LP duality
chapter: '10'
order: 11
owner: Nguyen Le Linh
categories:
- chapter10
lang: en
lesson_type: optional
---

From pricing megawatts across continental power grids to certifying the safety of deep neural networks and matching high-dimensional probability distributions via optimal transport, LP duality is quietly embedded in modern 2022–2026 software stacks. What makes LP duality uniquely valuable in production is not just strong duality at optimality, but **anytime weak duality**: every dual-feasible vector immediately delivers a rock-solid lower bound or shadow-price interpretation that downstream systems can trust in real time.

## Background Knowledge Map: Four Production Pillars of LP Duality

- **Pillar 1 — Anytime Verification Certificates:** In formal verification of ReLU networks, optimizing the LP dual on GPUs produces valid safety lower bounds at *every* iteration, allowing branch-and-bound verifiers to prune safe regions milliseconds after starting.
- **Pillar 2 — Shadow Prices in Grid Dispatch:** In DC optimal power flow (DC-OPF), the primal minimizes generation cost subject to nodal power balance and thermal line caps; complementary slackness reveals exactly which transmission lines are congested (nonzero dual price) and drives locational price differences.
- **Pillar 3 — Modern Max-Flow Solvers:** The 2022 near-linear-time $$m^{1+o(1)}$$ max-flow breakthrough combines primal–dual interior-point barriers with dynamic trees, turning classical network-flow duality into an ultra-fast subroutine for vision, clustering, and logistics.
- **Pillar 4 — Kantorovich Potentials in Optimal Transport:** Dualizing the discrete transport LP reveals potentials $$(\phi, \psi)$$ with $$\phi_i + \psi_j \le C_{ij}$$ that generalize seamlessly to continuous distributions and entropic (Sinkhorn) regularization.

### Step-by-Step Worked Example (Read Slowly): Nodal Shadow Prices (LMPs) in a 2-Bus Power Grid

Consider two cities (Bus 1 and Bus 2) connected by a single transmission line with thermal capacity $$F_{\max} = 30$$ MW. Bus 1 has a cheap generator ($$\$20$$/MWh, capacity $$100$$ MW); Bus 2 has an expensive generator ($$\$50$$/MWh, capacity $$100$$ MW) and local demand $$D_2 = 50$$ MW.

1. **Primal Economic Dispatch LP:** Minimize $$20 g_1 + 50 g_2$$ subject to:
   - Bus 1 balance: $$g_1 - f = 0$$ (dual price $$\lambda_1$$).
   - Bus 2 balance: $$g_2 + f = 50$$ (dual price $$\lambda_2$$).
   - Line thermal cap: $$f \le 30$$ (congestion price $$\mu \ge 0$$), and $$g_1, g_2, f \ge 0$$.
2. **Solve the primal dispatch:** Send as much cheap power as the line allows: $$f^\star = 30$$ MW, $$g_1^\star = 30$$ MW, and generate the remaining $$g_2^\star = 20$$ MW locally at Bus 2. Total cost: $$20(30) + 50(20) = \$1{,}600$$.
3. **Read off the dual LMPs via complementary slackness:**
   - Because $$g_1^\star = 30 > 0$$ (below its 100 MW cap), Bus 1's marginal price must equal Generator 1's cost: $$\lambda_1^\star = \$20\text{/MWh}$$.
   - Because $$g_2^\star = 20 > 0$$ (below its 100 MW cap), Bus 2's marginal price must equal Generator 2's cost: $$\lambda_2^\star = \$50\text{/MWh}$$.
   - Because $$f^\star = 30 > 0$$, dual stationarity on $$f$$ gives $$\lambda_2^\star - \lambda_1^\star - \mu^\star = 0 \implies \mu^\star = 50 - 20 = \$30\text{/MWh}$$ (the exact congestion rent per MW of line capacity!).
4. **Verify strong duality:** Dual value $$= 50 \lambda_2^\star - 30 \mu^\star = 50(50) - 30(30) = 2500 - 900 = \$1{,}600 = p^\star$$!

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

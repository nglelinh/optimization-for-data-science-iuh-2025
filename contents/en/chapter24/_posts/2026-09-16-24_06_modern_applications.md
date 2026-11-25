---
layout: post
title: 24-06 Modern applications of mixed-integer models
chapter: '24'
order: 7
owner: Nguyen Le Linh
categories:
- chapter24
lang: en
lesson_type: optional
---

Mixed-integer models are far from dusty textbook exercises—they quietly coordinate the physical backbone of the 2026 economy. Every time an airline builds legal crew pairings across thousands of flights, a logistics platform routes last-mile delivery vans under tight time windows, or a cloud provider places edge compute nodes to meet latency SLAs, an industrial MILP solver is solving a model built from Chapter 24’s exact templates. Even more exciting, modern ML4CO (Machine Learning for Combinatorial Optimization) research now trains graph neural networks to imitate strong branching inside Branch and Bound.

## Key ideas: From Classic MIP Templates to 2026 Industrial Solvers

- **Set Partitioning for Crew Scheduling:** Airlines model crew pairing as selecting a minimum-cost subset of legal multi-day pairings such that every flight leg is covered exactly once ($$\sum_p a_{fp} x_p = 1$$), solved at scale via column generation (Branch and Price).
- **Capacitated Routing & Assignment:** Last-mile delivery augments classical assignment with vehicle capacity, time windows, and subtour elimination constraints, turning dispatching into a structured MILP solved in rolling real-time horizons.
- **Facility Location for Edge Infrastructure:** Choosing which data centers or warehouses to open ($$y_i \in \{0, 1\}$$) and how to route traffic ($$x_{ij}$$) balances capital expenditure against latency constraints using tight disaggregated linking inequalities $$x_{ij} \le y_i$$.
- **Learning to Branch (ML4CO):** Because strong branching is accurate but expensive, modern hybrid solvers train bipartite graph neural networks on the constraint-variable incidence graph to predict strong-branching scores in microseconds.

### Worked example: Why Disaggregated Linking Cuts Beat Aggregated Constraints in Facility Location

Suppose 1 candidate warehouse ($$y \in \{0, 1\}$$) can serve $$m = 3$$ customers ($$x_1, x_2, x_3 \in [0, 1]$$), and currently only customer 1 is assigned to it ($$x_1 = 1, x_2 = 0, x_3 = 0$$).

1. **Aggregated linking constraint:** $$x_1 + x_2 + x_3 \le 3 y$$.
   - At $$(x_1, x_2, x_3) = (1, 0, 0)$$, the LP relaxation only requires $$1 \le 3y \implies y \ge 1/3$$! The solver pays just $$1/3$$ of the warehouse opening cost in the relaxation.
2. **Disaggregated linking constraints:** $$x_1 \le y,\ x_2 \le y,\ x_3 \le y$$.
   - At $$(x_1, x_2, x_3) = (1, 0, 0)$$, the first inequality immediately forces $$y \ge 1$$—paying **100%** of the warehouse cost even in the LP relaxation!
3. **Takeaway:** Both formulations have the exact same integer solutions, yet disaggregated inequalities eliminate the fractional loophole $$y = 1/3$$ completely—a classic modeling lesson that accelerates real-world facility location MIPs by orders of magnitude.

Chapter 24 is the *modeling* half of mixed-integer programming: binary decisions, assignment, knapsacks, and facility location. Those templates did not stay in textbooks. Crew pairing, last-mile routing, and the placement of warehouses or edge-GPU sites are still solved as MIPs, and since about 2019 a second industry has grown around them: **learning to optimize** — graph neural nets that propose branches, cuts, or warm starts for a MIP solver. This optional note is four data-science-facing applications. Cutting planes, best-subset selection, and neural-net verification wait for [Chapter 25]({% multilang_post_url contents/chapter25/21-03-28-25_Mixed_integer_programming %}).

## 1. Airline crew scheduling, still a living MIP

Crew pairing / rostering is an integer program with duty, rest, and fleet constraints. The public instance **air05** in MIPLIB 2017 (Gleixner, Hendel, Gamrath, et al., *Math. Prog. Comput.* 13:443–490, 2021, [doi:10.1007/s12532-020-00194-3](https://doi.org/10.1007/s12532-020-00194-3)) is the instance every new branching heuristic is still measured on. A 2025 explainability study (crew-scheduling air05 as a bipartite variable–constraint graph; [arXiv:2512.01698](https://arxiv.org/abs/2512.01698)) asks a data-science question that Chapter 24 already prepared: once you *model* the MIP, can a GNN embed that graph well enough to replace hand-crafted solver features? The MIP did not go away; it became the *label generator* for a learning pipeline.

## 2. Assignment and last-mile routing

The assignment problem in 24-02 is the linear oracle inside a great deal of modern logistics. Last-mile delivery and on-demand meal routing are vehicle-routing MIPs (or MIP + column generation) with time windows and driver shifts. Toth and Vigo’s *Vehicle Routing* monograph is the classical reference; the 2020s twist is that travel times and demand are *predicted* by a supervised model, then fed to a MIP that must return a feasible route in minutes. The data scientist owns the forecast; the integer program owns the “one driver, one vehicle, capacity $$Q$$” logic that a neural net will happily violate. That split — learn what you cannot write, optimize what you must certify — is the 2026 default in operations + ML.

## 3. Facility location for warehouses and edge compute

Facility location (also 24-02) is how platforms decide which fulfillment center, cache, or **GPU inference site** to open. Binary $$y_j$$ opens site $$j$$ at cost $$f_j$$; continuous (or integer) flows $$x_{ij}$$ send demand $$i$$ to $$j$$. Cloud and edge-ML papers reuse exactly this skeleton: $$f_j$$ is rack / license cost, $$c_{ij}$$ is latency or egress. The MIP is the same; the “data” in the objective is a learned demand surface. If you can write the 24-02 formulation, you can read those papers.

## 4. Learning to branch and the ML4CO competition

Gasse, Chételat, Ferroni, Charlin, and Lodi, *Exact Combinatorial Optimization with Graph Convolutional Neural Networks*, NeurIPS 2019, taught a GNN to imitate a strong branching expert. The NeurIPS 2021 **ML4CO** competition (Ecole et al.) turned that idea into a public benchmark: learn primal heuristics, configurations, or branching on families of MIPs. Follow-ups through 2024–2025 learn *cut sequences* and even try end-to-end RL solvers; those belong more to Chapter 25 (cutting planes) and are cited there. For this chapter, remember one sentence: a modern MIP application is often a *distribution* of instances, and a data-science model sits *inside* the branch-and-bound loop of 24-05, it does not replace the integrality constraint.

**Exercise.** Take the assignment formulation from 24-02 with $$n=8$$ random costs. Solve it (i) with a MIP solver or `scipy.optimize.linear_sum_assignment` and (ii) by relaxing $$x_{ij}\in[0,1]$$ and rounding. Count how often the LP relaxation is already integral (Birkhoff–von Neumann says *always* for a pure assignment — that is the point). Then add one extra inequality, “person 1 cannot do jobs 1–3,” and watch the relaxation need branching. That tiny edit is the difference between a textbook assignment and a crew-pairing MIP.

## Sources

- A. Gleixner et al., *MIPLIB 2017*, *Math. Prog. Comput.* 13:443–490, 2021.
- M. Gasse, D. Chételat, N. Ferroni, L. Charlin, A. Lodi, NeurIPS 2019 — GNN branching.
- A. Prouvost, A. Chowdhury, et al. / Ecole et al., NeurIPS 2021 ML4CO competition.
- P. Toth and D. Vigo (eds.), *Vehicle Routing: Problems, Methods, and Applications*, SIAM, 2nd ed., 2014.
- D. Bertsimas and J. Tsitsiklis, *Introduction to Linear Optimization* — assignment and facility location as the modeling backbone.
- Air05 GNN embeddings, [arXiv:2512.01698](https://arxiv.org/abs/2512.01698), 2025 — crew scheduling as a graph-learning instance.

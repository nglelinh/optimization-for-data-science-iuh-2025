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

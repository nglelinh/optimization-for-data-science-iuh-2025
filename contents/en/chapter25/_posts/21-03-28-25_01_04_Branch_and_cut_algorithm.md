---
layout: post
title: 25-01-04 Branch and cut algorithm
chapter: '25'
order: '6'
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

For three decades, Branch and Bound and Cutting Planes lived in separate camps: Branch and Bound suffered from weak LP bounds, while pure Cutting Planes bogged down in numerical ill-conditioning. In the early 1990s, Sebastian Ceria, Egon Balas, Gérard Cornuéjols, and Manfred Padberg united them into **Branch and Cut**: run a few rounds of sharp cuts at the root node (and selectively at tree nodes) to tighten the LP relaxation, then branch the moment cuts stop making rapid progress. That single architectural fusion—amplified by presolve, heuristics, and parallelization—drove a documented **billions-fold** speedup in MIP solving between 1990 and today.

## Background Knowledge Map: Architecture of Modern Branch-and-Cut Solvers

- **Root-Node Cut Loops:** Spending extra effort generating Gomory, Mixed-Integer Rounding (MIR), cover, and clique cuts at the root node strengthens *every* descendant in the entire tree simultaneously.
- **Cut-Then-Branch Balance:** Generating too many cuts bloats the LP basis and slows down every dual simplex pivot; generating too few leaves the tree exponentially large. Solvers use cut-management pools to drop inactive cuts and switch to branching once bound improvement stalls.
- **Presolve and Conflict Analysis:** Before the first LP even solves, presolve eliminates redundant variables, tightens variable bounds, and strengthens big-$$M$$ constants; during search, conflict analysis learns nogood clauses from infeasible branches (borrowing from SAT solvers).
- **Local vs. Global Validity of Cuts:** Cuts derived solely from original problem constraints are *globally valid* and can be shared across the entire search tree, whereas cuts derived using a node’s local branching bounds apply only within that subtree.

### Step-by-Step Worked Example (Read Slowly): Tracing One Root Cut + Branch Step in Branch and Cut

Consider $$\max z = 3 x_1 + 2 x_2$$ subject to $$2 x_1 + 2 x_2 \le 5$$, $$x_1 \le 2$$, and $$x_1, x_2 \in \mathbb{Z}_{\ge 0}$$.

1. **Initial LP relaxation at Root:** Pushing $$x_1 = 2$$ (highest coefficient) leaves $$2 x_2 \le 1 \implies x_2 = 0.5$$. So $$x_{\text{LP}} = (2, 0.5)$$ with $$z_{\text{LP}} = 3(2) + 2(0.5) = 7$$.
2. **Root-Node Cutting Plane (before branching!):** Divide $$2x_1 + 2x_2 \le 5$$ by $$2$$ and round down:
   $$x_1 + x_2 \le 2.$$
   Notice $$x_{\text{LP}} = (2, 0.5)$$ has $$2 + 0.5 = 2.5 > 2$$, so the cut slices it off cleanly.
3. **Re-solve Root LP with the cut:** Maximize $$3x_1 + 2x_2$$ subject to $$x_1 + x_2 \le 2$$, $$x_1 \le 2$$, $$x \ge 0$$.
   - Pushing $$x_1 = 2$$ forces $$x_2 = 0$$, giving $$x^{(1)} = (2, 0)$$ with $$z = 6$$.
   - Because $$(2, 0)$$ is already **integer-feasible**, the root node terminates with $$z^\star = 6$$—zero branches required!
   - By contrast, pure Branch and Bound without the root cut would have had to branch on $$x_2 = 0.5$$ into $$x_2 \le 0$$ (giving $$(2, 0), z = 6$$) and $$x_2 \ge 1$$ (giving $$(1.5, 1), z = 6.5$$), then branch *again* on $$x_1 = 1.5$$—exploring 5 nodes instead of 1.

In 1990, Sebastian Ceria at CMU successfully implemented the cutting plane method using the branch and bound algorithm, which is called branch and cut. Since then, cutting planes have become a core component of commercial optimization solvers.

## Branch and cut algorithm

Consider the following integer programming problem where $$f : \mathbb{R}^{n} \to \mathbb{R}$$ and $$C \subseteq \mathbb{R}^{n}$$ is convex and $$J \subseteq \{1, ..., n\}$$.

>$$
>\begin{align}
>\min_{x} & \quad f(x) \\
>\text{subject to } & \quad x \in C \\
>& \quad x_j \in \mathbb{Z}, \quad j \in J \\
>\end{align}
>$$

### Branch and cut algorithm

In the algorithm, we denote the Convex Problem as CP and the Integer Program as IP.

1. Solve the following convex relaxation problem:
   >$$
   >\begin{align}
   >\min_{x} & \quad f(x) \\
   >\text{subject to } & \quad x \in C \\
   >\end{align}
   >$$

2. If (CR) is infeasible $$\Rightarrow$$ (IP) is infeasible

3. If the solution $$x^{\star}$$ of (CR) is (IP) feasible $$\Rightarrow$$ $$x^{\star}$$ is the solution of (IP)

4. If the solution $$x^{\star}$$ of (CR) is (IP) infeasible, choose one of the following two options:
   - 4.1 Add a cut and go to step 1.
   - 4.2 Branch and iteratively solve subproblems.

The branch and cut algorithm combines branch and bound with the cutting plane method, allowing us to choose whether to branch-and-bound or cut in step 4.

## Integer programming technology

State-of-the-art solvers like Gurobi, CPLEX, and FICO include very efficient implementations of algorithms such as simplex and interior-point methods. Particularly, in the case of mixed integer optimization, most solvers use the branch and cut algorithm and extensively utilize the advantages of convex relaxation and warm start.

Compared to about 30 years ago, the performance improvement in Integer programming has been dramatic. Therefore, many real-life problems that could not be solved during that time are now being solved through Integer programming, and with the improvement in computing power, they are expected to be used even more actively.

* Algorithm speed improvement 1990-2016: over $$500,000$$
* Hardware speed improvement 1990-2016: over $$500,000$$
* Total speedup: over $$250$$ billion = $$2.5 \cdot 10^{11}$$
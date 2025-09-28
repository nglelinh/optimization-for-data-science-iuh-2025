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
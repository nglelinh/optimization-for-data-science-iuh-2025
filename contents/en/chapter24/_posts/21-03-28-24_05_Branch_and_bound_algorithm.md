---
layout: post
title: 24-05 Branch and bound algorithm (B&B)
chapter: '24'
order: 6
owner: YoungJae Choung
categories:
- chapter24
lang: en
---

Branch and Bound is the undisputed workhorse of exact discrete optimization—the algorithmic spine of Gurobi, CPLEX, HiGHS, and SCIP. Its idea is deceptively simple: divide and conquer with a sharp pair of scissors. Whenever a relaxation returns a fractional variable $$x_j = 2.4$$, split the universe into two mutually exclusive subproblems ($$x_j \le 2$$ and $$x_j \ge 3$$). The magic lies in **fathoming (pruning)**: the moment a subproblem’s relaxation bound is worse than an already-known integer incumbent, you can discard that entire branch—and potentially billions of descendant solutions—in one stroke.

## Key ideas: The Three Pillars of Branch and Bound

- **Branching (Partitioning the Feasible Set):** Picking a fractional variable $$x_j \notin \mathbb{Z}$$ and adding $$x_j \le \lfloor x_j \rfloor$$ to the left child and $$x_j \ge \lceil x_j \rceil$$ to the right child eliminates the current fractional point without losing *any* integer feasible solution.
- **The Three Fathoming (Pruning) Rules:** A tree node can be permanently closed without further branching if its relaxation is: (1) **infeasible**, (2) **worse than the incumbent** ($$z_{\text{LP}} \ge U$$ for minimization, or $$\le L$$ for maximization), or (3) **already integer-feasible** (which also updates the incumbent!).
- **Node Selection Strategy (BFS vs. DFS vs. Best-First):** Depth-first search finds feasible incumbents quickly using low memory; best-first search always expands the node with the tightest relaxation bound, minimizing total nodes explored to prove optimality.
- **Variable Selection (Strong Branching & Pseudocosts):** Choosing *which* fractional variable to branch on can shrink the search tree by $$100\times$$; strong branching tests candidate splits beforehand to pick the variable that lifts child bounds the most.

### Worked example: Complete Branch-and-Bound Tree by Hand

Maximize $$z = 5 x_1 + 4 x_2$$ subject to $$x_1 + x_2 \le 5$$, $$10 x_1 + 6 x_2 \le 45$$, and $$x_1, x_2 \in \mathbb{Z}_{\ge 0}$$.

1. **Root Node (Node 0):** Solve the LP relaxation. Intersecting $$x_1 + x_2 = 5$$ and $$10 x_1 + 6 x_2 = 45$$ gives $$4 x_1 = 15 \implies x_1 = 3.75,\ x_2 = 1.25$$, with $$z_{\text{LP}} = 5(3.75) + 4(1.25) = 23.75$$. Since $$z$$ must be an integer, global upper bound is $$23$$. Incumbent $$L = -\infty$$.
2. **Branch on $$x_1 = 3.75$$ into Node 1 ($$x_1 \le 3$$) and Node 2 ($$x_1 \ge 4$$):**
   - **Node 1 ($$x_1 \le 3$$):** At $$x_1 = 3$$, $$x_1 + x_2 \le 5 \implies x_2 \le 2$$ (and $$30 + 12 = 42 \le 45$$ is slack). LP optimum is $$(3, 2)$$ with $$z = 5(3) + 4(2) = 23$$! Because $$(3, 2)$$ is **integer-feasible**, update incumbent $$L = 23$$ and **fathom Node 1 by integrality**.
   - **Node 2 ($$x_1 \ge 4$$):** At $$x_1 = 4$$, $$10(4) + 6 x_2 \le 45 \implies x_2 \le 5/6 \approx 0.833$$. LP optimum is $$(4, 5/6)$$ with $$z_{\text{LP}} = 5(4) + 4(5/6) = 23.333$$. Since $$z$$ must be integer, any integer solution in Node 2 has $$z \le \lfloor 23.333 \rfloor = 23 \le L = 23$$!
3. **Fathom Node 2 by bound and terminate:** No integer point in Node 2 can strictly beat our incumbent $$L = 23$$. All active nodes are closed: $$x^\star = (3, 2)$$ with $$z^\star = 23$$ is **provably optimal** in just 3 nodes!

Let's find out the method of solving Integer programs through Branch and bound algorithm and Convex relaxation.

## Definition and properties
Branch and bound algorithm is the most common method for solving integer programs. It is mainly a divide and conquer approach that breaks the original problem into several smaller problems (sub-problems) to approach the correct answer. 

When the constraint set $$X = X_{1} \cup X_{2} \cup \dotsc \cup X_{k}$$ is a union of partitions consisting of each $$X_{i}$$,
> $$ \min_{x \in X} f(x) = \min_{i = 1, \dotsc , k} \lbrace \min_{x \in X_{i}} f(x) \rbrace .$$

We can find the optimal solution by partitioning the region and finding the minimum.

Any feasible solution of a sub-problem can be set as the upper bound $$u(X)$$. To obtain the lower bound, we find the lower bound $$l(X_{i})$$ of each sub-problem. Then, if $$l(X_{i}) \geq u(X)$$, we exclude the sub-problem $$\min_{x \in X_{i}} f(x)$$ corresponding to this part. 
 
The Integer Programming problem (IP) is defined as follows:

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } && x \in C \\\\
> &&&x_j \in \mathbb{Z}, \quad j \in J \\\\
> \end{align}$$
> $$\begin{align}
> \text{where f is convex } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
\quad \text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
> \end{align}
> $$

And when the Convex Relaxation (CR) problem is as follows:

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } &&x \in C \\\\
> \end{align}$$
> $$\begin{align}
> \text{where f is convex } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
\quad \text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
> \end{align}
> $$

The problem is solved recursively.

* If the constraint set is trivial, solve the (CR) problem. If the solution is less than the current upper bound, update the upper bound. Stop.
    * If (CR) is infeasible, then (IP) is also infeasible. Stop.
    * If the solution $$x^{\star}$$ of (CR) is also feasible for (IP), then $$x^{\star}$$ becomes the solution. Stop.
* Find the lower bound of the problem.
    * If the solution $$x^{\star}$$ of (CR) is infeasible for (IP), update the lower bound of (IP).
* If the lower bound is greater than the current upper bound, Stop.
* Split the constraint set and solve each sub-problem recursively.


## After branching

* After branching, solve each subproblem.
* If the lower bound of a subproblem is greater than the current upper bound, there is no need to consider the subproblems below it.
* The most reliable method for computing the lower bound is through convex relaxation, but other methods (e.g., Lagrangian relaxation) are also used.

### Branch and bound, step by step (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/branch-bound_en.mp4"></video>
</div>

Solve the LP relaxation, branch on a fractional variable, and discard any node whose bound cannot beat the best integer solution found so far.

Note: the video solves a maximization problem ($$\max\ 5x_1 + 4x_2$$), while this lesson uses the minimization form. They are equivalent because $$\max_x c^Tx = -\min_x (-c^Tx)$$. In the maximization form the bounds swap roles: the LP relaxation value at a node is an **upper** bound, the best integer solution so far is a **lower** bound, and a node is pruned when its upper bound cannot exceed the best integer value.

### Try it yourself: step through branch and bound

<div class="opx-explainer" data-opx="bnb" data-lang="en"></div>

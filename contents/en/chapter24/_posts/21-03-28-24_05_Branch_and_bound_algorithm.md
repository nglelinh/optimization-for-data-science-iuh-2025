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

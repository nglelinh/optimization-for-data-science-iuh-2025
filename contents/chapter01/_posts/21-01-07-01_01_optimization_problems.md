---

---
layout: post
title: 01-01 Optimization problems?
chapter: "01"
order: 2
owner: "Kyeongmin Woo"
---

An optimization problem is a problem in which, among many possible candidates, we seek the optimal solution (optimal value) or a value close to the optimal. In machine learning, for example, we often find the parameters of a model that minimize or maximize a cost function. This is formulated as an optimization problem.


## Mathematical optimization problems
A mathematical optimization problem can be expressed as follows:

>$$\begin{align*} 
>&\min_{x\in D}\ && f(x) \\
>&\text{subject to} && g_i(x) \le 0,\ i = 1, ..., m \\
>&&& h_j(x) = 0,\ j = 1,\ ..., r
>\end{align*}$$

**Mathematical Optimization Problem in standard form [3]**

* $$x \in \mathbb{R}^n$$ is the optimization variable
* $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ is the objective or cost function
* $$g_i: \mathbb{R}^n \rightarrow \mathbb{R}, i = 1, ..., m$$ are the inequality constraint functions
* $$h_j: \mathbb{R}^n \rightarrow \mathbb{R}, j = 1, ..., r$$ are the equality constraint functions

The vector $$x$$ that minimizes the objective function $$f$$ over the feasible domain (the set of all points satisfying the constraints) is denoted as $$x^*$$ and called the optimal solution. [1]

Constraints can be classified into two types: [2]

1. Explicit constraints: Constraints that are directly specified in the optimization problem. In the standard form above, the constraints expressed by the functions $$g_i$$ and $$h_j$$ are explicit. If there are no explicit constraints, the problem is called an unconstrained problem.
2. Implicit constraints: Constraints that are not directly specified, but arise from the intersection of the domains of the objective and constraint functions.

$$D = dom(f) \cap \bigcap_{i=1}^m {\rm dom}(g_i) \cap \bigcap_{j=1}^r dom(h_j)$$<br/>

**Note:** $$dom(f)$$ means the domain of the function $$f$$.

>**Example: implicit constraint ↔ explicit constraint**
>
>Suppose the optimization problem is given as follows:
>
>$$\begin{align*} \text{minimize } & & \log(x) \end{align*}$$
>
>Here, the domain of the objective function $$\log(x)$$ is $$x > 0$$, so $$x > 0$$ is an implicit constraint. If we write this as an optimization problem with explicit constraints:
>
>$$\begin{align*} &\text{minimize } && \log(x) \\ &\text{subject to } &&x > 0 \end{align*}$$

## Applications

Optimization problems are applied in various fields. [2]

#### Portfolio optimization
* variables: investment amount for each asset
* constraints: budget, minimum/maximum investment per asset, minimum return
* objective: overall risk or return variance

#### Device sizing in electronic circuits
* variables: width and length of each component
* constraints: manufacturing process limitations, maximum area
* objective: power consumption

#### Data fitting
* variables: model parameters
* constraints: prior information (e.g., some parameters are non-negative), parameter restrictions
* objective: error in prediction

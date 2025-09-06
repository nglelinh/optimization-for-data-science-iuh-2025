---
layout: post
title: 01-01 Optimization problems?
chapter: '01'
order: 2
owner: Kyeongmin Woo
categories:
- chapter01
lang: en
lesson_type: required
---

An optimization problem is a problem in which, among many possible candidates, we seek the optimal solution (optimal value) or a value close to the optimal. 

**In data science and machine learning**, optimization is everywhere:
- **Training neural networks**: Finding weights that minimize prediction error
- **Linear regression**: Finding the best-fit line that minimizes squared errors
- **Clustering**: Optimizing cluster centers to minimize within-cluster variance
- **Feature selection**: Choosing the best subset of features to maximize model performance
- **Hyperparameter tuning**: Finding optimal learning rates, regularization parameters, etc.

Every time you train a machine learning model, you're solving an optimization problem!

## Mathematical optimization problems
A mathematical optimization problem can be expressed as follows:

>$$\begin{align*} 
>&\min_{x\in D}\ && f(x) \\
>&\text{subject to} && g_i(x) \le 0,\ i = 1, ..., m \\
>&&& h_j(x) = 0,\ j = 1,\ ..., r
>\end{align*}$$

**Mathematical Optimization Problem in standard form**

* $$x \in \mathbb{R}^n$$ is the optimization variable
* $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ is the objective or cost function
* $$g_i: \mathbb{R}^n \rightarrow \mathbb{R}, i = 1, ..., m$$ are the inequality constraint functions
* $$h_j: \mathbb{R}^n \rightarrow \mathbb{R}, j = 1, ..., r$$ are the equality constraint functions

The vector $$x$$ that minimizes the objective function $$f$$ over the feasible domain (the set of all points satisfying the constraints) is denoted as $$x^*$$ and called the optimal solution.

**Constraints can be classified into two types:**

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

> **💡 Pro Tip**: Start with convex formulations when possible - they're easier to solve and understand. Only move to complex non-convex models when simpler approaches fail to meet your requirements.

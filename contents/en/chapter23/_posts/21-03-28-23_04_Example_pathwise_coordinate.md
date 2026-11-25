---
layout: post
title: 23-04 Example - Pathwise coordinate descent for lasso
chapter: '23'
order: '5'
owner: YoungJae Choung
categories:
- chapter23
lang: en
---

Solving Lasso for a single, arbitrary regularization parameter $$\lambda$$ is rarely what a data scientist actually wants—in cross-validation, you need solutions across an entire grid of 100 values $$\lambda_1 > \lambda_2 > \dots > \lambda_{100}$$. Astonishingly, computing the *entire* 100-point path via **pathwise coordinate descent** (the engine inside Friedman, Hastie, and Tibshirani’s `glmnet`) is often *faster* than solving a single small-$$\lambda$$ problem from scratch! Two engineering ideas make this magic happen: **warm starts** from sparse neighboring solutions and **active-set sweeps** that ignore zero variables until KKT verification.

## Background Knowledge Map: Inside the `glmnet` Pathwise Engine

- **Exact Threshold $$\lambda_{\max}$$:** At $$\lambda_1 = \|X^\top y\|_\infty$$, every coordinate satisfies $$|X_i^\top y| \le \lambda_1$$, so $$\hat{\beta}(\lambda_1) = 0$$ is immediately optimal. Starting here guarantees the path begins at maximum sparsity.
- **Warm Starts Along a Logarithmic Grid:** Decreasing $$\lambda_k$$ on a log-spaced grid ensures that $$\hat{\beta}(\lambda_{k-1})$$ is already very close to $$\hat{\beta}(\lambda_k)$$, drastically cutting the number of iterations needed at each grid point—especially for small, ill-conditioned $$\lambda$$.
- **Active-Set Strategy:** Once a few variables become nonzero (the active set $$\mathcal{A} = \{j : \beta_j \ne 0\}$$), inner-loop coordinate descent iterates *only* over $$\mathcal{A}$$ until convergence. Because $$|\mathcal{A}| \ll p$$, each inner sweep costs $$O(n|\mathcal{A}|)$$ instead of $$O(np)$$.
- **KKT Verification Pass:** After the active set converges, a single full pass checks $$|X_j^\top r| \le \lambda_k$$ for all inactive variables $$j \notin \mathcal{A}$$. If none violate KKT, the solution is globally optimal; otherwise, violators enter $$\mathcal{A}$$ and the inner loop repeats.

### Step-by-Step Worked Example (Read Slowly): Tracing a 3-Step Warm-Start Path

Using $$X = \begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}$$ and $$y = (3, 1, 2)^\top$$, we have $$X^\top y = (4, 5)^\top$$. Let us trace the path across $$\lambda_1 = 5$$, $$\lambda_2 = 4$$, and $$\lambda_3 = 3$$.

1. **Grid point 1 ($$\lambda_1 = \|X^\top y\|_\infty = 5$$):**
   - At $$\beta = (0, 0)^\top$$, $$|X_1^\top y| = 4 \le 5$$ and $$|X_2^\top y| = 5 \le 5$$.
   - Optimal solution: $$\hat{\beta}(5) = (0, 0)^\top$$, active set $$\mathcal{A} = \emptyset$$.
2. **Grid point 2 ($$\lambda_2 = 4$$), warm-started from $$\hat{\beta}(5) = (0, 0)^\top$$:**
   - KKT scan at $$r = y = (3, 1, 2)^\top$$: $$|X_1^\top r| = 4 \le 4$$ (passes), $$|X_2^\top r| = 5 > 4$$ (violates!).
   - Enter coordinate 2 into active set: $$\mathcal{A} = \{2\}$$.
   - Active-set update on $$\beta_2$$: $$\beta_2 = \frac{S_4(5)}{2} = 0.5$$. Updated residual: $$r = (3, 1, 2)^\top - 0.5(1, 0, 1)^\top = (2.5, 1, 1.5)^\top$$.
   - KKT check on inactive coordinate 1: $$|X_1^\top r| = |2.5 + 1| = 3.5 \le 4$$ (passes!).
   - Optimal solution: $$\hat{\beta}(4) = (0, 0.5)^\top$$ in just **1 coordinate update**!
3. **Grid point 3 ($$\lambda_3 = 3$$), warm-started from $$\hat{\beta}(4) = (0, 0.5)^\top$$:**
   - KKT scan on $$r = (2.5, 1, 1.5)^\top$$: $$X_1^\top r = 3.5 > 3$$ (violates!) and $$X_2^\top r = 4 > 3$$ (already in $$\mathcal{A}$$).
   - Expand $$\mathcal{A} = \{1, 2\}$$ and run active-set CD from $$(0, 0.5)^\top$$:
     - $$\beta_1 = \frac{S_3(3.5)}{2} = 0.25$$, $$r \leftarrow (2.25, 0.75, 1.5)^\top$$.
     - $$\beta_2 = \frac{S_3(X_2^\top(r + 0.5 X_2))}{2} = \frac{S_3(2.25 + 1.5 + 1.0)}{2} = \frac{S_3(4.75)}{2} = 0.875$$, $$r \leftarrow (1.875, 0.75, 1.125)^\top$$.
   - Notice how coordinate 1 stayed completely out of the computation until $$\lambda$$ actually dropped below $$3.5$$.

In this section, we will briefly introduce the overview of pathwise coordinate descent for lasso [[Friedman et al. (2007)](https://arxiv.org/pdf/0708.1485.pdf)] [[Friedman et al. (2009)](https://www.jstatsoft.org/article/view/v033i01/v33i01.pdf)].

>**Lasso regression problem:**
>
>$$
>\min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
>$$

In [07-03-03 Example: Lasso Optimality Condition]({% multilang_post_url contents/chapter07/21-03-25-07_03_03_example_lasso_optimality_condition %}), we saw the derivation of the optimality condition for the lasso regression problem. The optimal solution for the above problem satisfies the following condition.

>$$
>\begin{align}
>X_1^T(y-X\beta) &= \lambda v_1\\
>X_2^T(y-X\beta) &= \lambda v_2\\
>\dots\\
>X_p^T(y-X\beta) &= \lambda v_p
>\end{align}
>$$

**Note:** $$X_i, i \in \{1,2,…,p\}$$ means the $$i$$-th column data of the given matrix $$X$$. Here, $$v=(v_1,v_2,\dots,v_p)$$ is the subgradient of $$\beta=(\beta_1,\beta_2,\dots,\beta_p)$$.

$$
v_i, i \in \{1,2,\dots,p \} = \begin{cases}
\{ 1 \} &\text{if $\beta_i > 0$} \\
\{-1 \} &\text{if $\beta_i < 0$} \\
[-1,1] &\text{if $\beta_i = 0$}
\end{cases}
$$

Using the optimality condition, we can determine whether each element of $$\beta$$ corresponds to the current optimal state. Using the coordinate descent algorithm, we can solve the lasso problem more efficiently by updating only the elements that have not yet reached the optimal state.

Also, the larger the value of $$\lambda$$, the faster the coordinate descent algorithm tends to work in lasso regression problems. By utilizing this tendency and gradually reducing $$\lambda$$ (warm start), we can approach the solution more quickly.

## Algorithm

### Outer loop (pathwise strategy):
* Compute optimal solutions in the order $$\lambda_1 > \lambda_2 > \dots > \lambda_r$$.
* Use the result computed at tuning parameter $$\lambda_k$$ to initialize the coordinate descent algorithm for $$\lambda_{k+1}$$. (warm start)

### Inner loop (active set strategy):
* Perform one or a few coordinate cycles. Record the non-zero elements of $$\beta$$ in the active set $$A$$.
* Perform coordinate cycles on the elements recorded in $$A$$ until convergence.
* Check the optimality condition for all elements of $$\beta$$. If there are elements that do not satisfy the condition, add them to $$A$$ and return to step 1.

## Notes

* Generally, the pathwise strategy works much more efficiently than directly finding the solution for a given $$\lambda$$ in the problem.
* The active set strategy takes advantage of sparsity. Because of this, coordinate descent works much faster in lasso regression than ridge regression.
* Pathwise coordinate descent for lasso works as fast as the fastest and most sophisticated algorithms for lasso regression problems.

**Reference:** [Analysis of ridge regression and lasso regression tendencies](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/)
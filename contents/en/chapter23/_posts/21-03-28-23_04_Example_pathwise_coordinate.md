---
layout: post
title: 23-04 Example: Pathwise coordinate descent for lasso
chapter: '23'
order: '5'
owner: YoungJae Choung
categories:
- chapter23
lang: en
---

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
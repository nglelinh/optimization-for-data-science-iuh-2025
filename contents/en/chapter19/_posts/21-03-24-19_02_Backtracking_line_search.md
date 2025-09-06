---
layout: post
title: 19-02 Backtracking line search
chapter: '19'
order: 6
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

**Proximal newton method** may not converge in cases with pure step size $$t_k=1, k=1,2,3, \cdots$$ like newton's method. Therefore, we need to optimize the step size through backtracking line search.

## Backtracking line search algorithm

1. Initialize parameters. ($$0 \lt \alpha \le 1/2, 0 \lt \beta \lt 1$$)
2. At each iteration, compute the Proximal newton direction as $$v = \text{prox}_{H} ( x - H^{-1} \nabla g (x) ) - x$$.
3. Initialize $$t=1$$.
4. If the condition $$f(x + tv) \gt f(x) + \alpha t \nabla g(x)^T v + \alpha (h(x + tv) - h(x))$$ is satisfied, reduce $$t=\beta t$$. Iterate step 4 while this condition is satisfied. ($$f = g + h$$)
5. Execute the Proximal newton update $$x^+ = x + tv$$.
6. If the termination condition is not satisfied, go to step 2.

Intuitively, we find a step size $$t$$ such that we move along direction $$v$$ to a position where the linear approximation of function $$f$$ at $$x$$ is reduced by a factor of $$\alpha$$. Since the $$h$$ part of $$f$$ is not differentiable, we use the discrete derivative $$h(x + tv) - h(x)$$.

## Efficiency of algorithm
There are many methods for performing backtracking line search, and here we have introduced one of them. 

In this method, when computing $$v$$, the prox operator is computed only once. In the case of proximal gradient descent, the prox operator had to be computed iteratively in the inner loop, which is a distinctly different characteristic. Therefore, this method can perform backtracking line search very efficiently when the computation of the prox operator is complex.

### [reference] Method 별  backtracking line search
* Gradient descent [06-02-02 Backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %})
* Proximal gradient descent [09-02 Convergence analysis]({% multilang_post_url contents/chapter09/20-01-08-09_02_convergence_analysis %})
* Newton's method [14-04 Backtracking line search]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %})

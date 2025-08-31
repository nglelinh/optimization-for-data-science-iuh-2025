---
layout: post
title: 08-02-01 Stochastic Subgradient Method
chapter: "08"
order: 12
owner: "Kyeongmin Woo"
---

Let’s consider the problem of minimizing the sum of functions as follows:

>$$
\begin{equation}
\min_x \sum_{i=1}^m f_i(x)
\end{equation}
$$

If we apply the subgradient method to this problem, we need to compute the subgradient for each function $$f_i$$ and sum them. (This is similar to the method introduced in [stochastic gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %})).

In summary, the stochastic subgradient method takes the following form:

>$$
\begin{align}
x^{(k)} = x^{(k-1)} - t_k \cdot g_{i_k}^{(k-1)}, \quad k = 1, 2, 3, . . . 
\end{align}
$$

Here, $$i_k \in \{1,...,m\}$$ is the index chosen at the $$k$$-th iteration. As will be discussed in the next section on the convergence rate of the stochastic subgradient method, the choice of cyclic or random method affects the result. $$g_{i}^{(k-1)} \in \partial f_{i}(x^{k-1})$$, and this update direction is different from the usual [subgradient method]({% multilang_post_url contents/chapter08/20-03-29-08_01_subgradient_method %}) (also called batch subgradient method or full batch subgradient method), where $$\sum_{i=1}^{m} g_i^{(k-1)}$$ is used.

If each $$f_i, i = 1,...,m$$ is differentiable, this algorithm becomes stochastic gradient descent. (The stochastic subgradient method is a more general form)
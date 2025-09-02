---
layout: post
title: 06-05 Stochastic gradient descent
chapter: '06'
order: 15
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

Consider the problem of minimizing the sum of functions as follows.
>
$$ \begin{equation}
\min_x \sum_{i=1}^m f_i(x)
\end{equation} $$

If we apply gradient descent to this problem, we need to compute the gradient for each function $$f_i$$ and sum them up. (That is, the gradient of the sum of functions equals the sum of the gradients of each function.)
>
$$\nabla \sum_{i=1}^m f_i(x) = \sum_{i=1}^m \nabla f_i(x)$$

We apply this result to the following equation to move to the next position. Therefore, we can see that every time we move one step, we need to compute the gradient for all functions.
>
$$ \begin{equation}
x^{(k)} = x^{(k-1)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k-1)}), \,  k=1,2,3,\dots
\end{equation} $$

Gradient descent computes the gradients of all functions and then performs updates all at once. For this reason, gradient descent is called a batch update method. Batch updates have the disadvantage that computational overhead increases significantly as the number of functions increases.

## Stochastic gradient descent
In contrast, the **Stochastic gradient descent (SGD)** method finds the next position by computing the gradient of only one function. As shown in the following equation, SGD selects one function index $$i_k$$ at the $$k$$-th iteration to perform the update.
>
$$ \begin{equation}
x^{(k)} = x^{(k-1)} - t_k \cdot \nabla f_{i_k} (x^{(k-1)}), \, i_k \in \{1,2,\dots,m\}
\end{equation} $$

The function index $$i_k$$ can be selected in the following two ways. 

* **Cyclic rule**: A method that periodically repeats all function indices in the same order $$i_k = 1,2,\dots,m, 1,2,\dots,m, ... $$
* **Randomized rule**: A method that selects function indices uniformly at random $$i_k \in \{1,2,\dots,m\}$$

Generally, the randomized update method is used more frequently.

## Convergence of stochastic gradient descent

What are the differences between **Gradient descent (GD)** and **Stochastic gradient descent (SGD)** methods? Computationally, GD performs updates in a batch manner all at once, while the SGD method performs $$m$$ updates. That is, m stochastic steps $$\approx$$ one batch step.

Then what differences are there in the update process?

In the case of SGD, when m updates are made from step $$k$$ to step $$k+m$$, the process proceeds as follows.
>
$$ \begin{equation}
\text{SGD Cycle rule : } \quad x^{(k+m)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k+i-1)})
\end{equation}
$$

In the case of GD, when one update is made from step $$k$$ to step $$k+1$$, the process proceeds as follows.

>
$$ \begin{equation}
\text{GD Batch : } \quad x^{(k+1)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k)})
\end{equation} 
$$

Therefore, when searching for the optimal value using these two update methods, the directions show the following difference. 
>
$$ \begin{equation}
\sum_{i=1}^{m}[ \nabla f_i (x^{(k+i-1)}) - \nabla f_i (x^{(k)})]
\end{equation} $$

If each $$\nabla f_i(x)$$ does not change significantly with respect to $$x$$, that is, if it is Lipschitz continuous, then SGD converges and consequently the two methods converge to the same optimal solution.

Empirically, the SGD method is known to work effectively when far from the optimal point, but experiences difficulty in convergence when close to the optimal point.

---
layout: post

title: "09-02 Convergence analysis"
chapter: "09"
order: 3
owner: "Kyeongmin Woo"
---
# Convergence analysis
In this section, we analyze the convergence of proximal gradient descent. 

## Convergence Analysis
For the objective function $$f(x) = g(x) + h(x)$$, we assume the following:

* $$g$$ is convex, differentiable, and **dom**$$(g) = \mathbb{R}^n$$, and $$\nabla g$$ is Lipschitz continuous ($$L > 0$$).
* $$h$$ is convex, and $$\text{prox}_{t}(x) = \underset{z} {\text{argmin}} \{ \parallel x - z \parallel_2^2/ (2t) + h(z) \}$$ needs to be computed.

#### Convergence Theorem
> **Proximal gradient descent** satisfies the following equation for a fixed step size $$t \le 1/L$$: 
>\begin{align}
f(x^{(k)}) - f^{\*} \le  \frac{ \lVert x^{(0)} - x^{\*} \rVert^2_2 }{2tk}
\end{align}

Proximal gradient descent has a convergence rate of $$O(1/k)$$ or $$O(1/\epsilon)$$, which is the same performance as gradient descent. However, this performance is based on the number of iterations, not the number of operations. (The number of operations can vary depending on the function $$h$$.)

## Backtracking line search
The backtracking line search method of proximal gradient descent is similar to gradient descent but operates only on the smooth part $$g$$, not the function $$f$$. 

First, set the parameter to $$0 < \beta < 1$$ and start with $$t=1$$. In each iteration, reduce $$t$$ to $$t = \beta t$$ while satisfying the following condition, and update proximal gradient descent if the condition is not met.
> \begin{align}
g(x - tG_t(x)) > g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2
\end{align}

This backtracking condition means that the value of the function $$g$$ at the next step location $$x - tG_t(x)$$ is greater than the value of the Taylor second-order approximation of the function $$g$$.

If $$G_t(x) = \nabla g(x)$$ in this equation, we can see that $$g(x - t \nabla g(x)) > g(x) - \alpha t \lVert \nabla g(x) \rVert_2^2 $$, which becomes identical to the backtracking condition of gradient descent. 

**Note:** For more details on the backtracking of gradient descent, refer to [06-02-02 backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %}).

#### Backtracking line search algorithm
If we summarize this in an algorithm, it is as follows. (However, $$\nabla x = - t G_t(x)$$)

1. Initialize the parameters. ($$0 \lt \beta \lt 1$$, $$0 \lt \alpha \le 1/2$$)
2. In each iteration, initialize $$t = t_{\text{init}}$$. ($$t_{\text{init}} = 1$$)
3. If the condition $$g(x - tG_t(x)) \gt g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2 $$ is satisfied, reduce $$t = \beta t$$. Repeat step 3 while this condition is met.
4. Perform the gradient descent update $$ x^+ = x - t G_t(x) = \text{prox}_t(x - t \nabla g(x))$$.
5. If the termination condition is not met, go back to step 2.

When backtracking in proximal gradient descent, since $$G_t(x)$$ is computed repeatedly, the proximal mapping included in $$G_t(x)$$ is also computed repeatedly. Since the proximal mapping is very costly to compute, the overall computational cost of backtracking can be high.

#### Convergence Theorem
Under the same assumptions as above, the backtracking line search method also satisfies the same performance.

>**Proximal gradient descent** satisfies the following equation for backtracking line search. The step size is $$t_{\text{min}} = \text{min} \{1,\beta /L \}$$.

> $$
f(x^{(k)})−f^{\star} ≤ \frac{\lVert x^{(0)} − x^{\star} \rVert_{2}^{2}}{2 t_{min}k}, \space t_{\text{min}} = \text{min} \{ 1, \beta / L \} \\
$$

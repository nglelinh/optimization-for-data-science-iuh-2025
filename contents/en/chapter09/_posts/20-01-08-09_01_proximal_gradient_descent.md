---
layout: post
title: 09-01 Proximal gradient descent
chapter: "09"
order: 2
owner: "Kyeongmin Woo"
---

# Proximal gradient descent

**Proximal gradient descent** is a method for finding the optimum by decomposing the objective function into a differentiable part and a non-differentiable part. In this section, we will look at how to define functions and find the optimum in proximal gradient descent.

## Decomposable functions
Suppose the objective function $$f$$ can be decomposed into two functions $$g$$ and $$h$$.

>$$f(x) = g(x) + h(x)$$

Here, the two functions $$g$$ and $$h$$ have the following properties:

* $$g$$ is convex and differentiable. (**dom**$$(g) = \mathbb{R}^n$$)
* $$h$$ is convex and non-differentiable.

If $$f$$ is differentiable, you can find the next position using gradient descent:

>$$x^+ = x - t \cdot \nabla f(x)$$

**[Note]** In gradient descent, the function $$f$$ is approximated near $$x$$ by a second-order Taylor expansion, and the Hessian $$\nabla^2 f(x)$$ is replaced by $$\frac{1}{2t} I$$. The minimum of this approximation is chosen as the next position. (See Chapter 6 Gradient descent for details)

> \begin{align}
x^+ = \underset{z}{\text{argmin}}  \underbrace{ f(x) + \nabla f(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2}_{\tilde{f}_t(z)}
\end{align}

However, if $$f$$ is not differentiable, you cannot use gradient descent. But if $$f$$ is composed as $$f = g + h$$, can't we approximate the differentiable part $$g$$ with a quadratic?

This idea leads to **Proximal gradient descent**. In this method, you adjust to the best position that is close to the location predicted by gradient descent for $$g$$ and also makes the non-differentiable function $$h$$ small. This process can be expressed as follows:

>
$$ \begin{align}
x^+ & = \underset{z}{\text{argmin}}   \tilde{g}_t(z) + h(z) \\
& = \underset{z}{\text{argmin}} \ g(x) + \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\
& = \underset{z}{\text{argmin}}  \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + \frac{t}{2} \parallel \nabla g(x) \parallel_2 ^2  + h(z) \\
& = \underset{z}{\text{argmin}}  \frac{1}{2t} \left ( 2t \nabla g(x)^T (z - x) + \parallel z - x \parallel_2 ^2 + t^2 \parallel \nabla g(x) \parallel_2 ^2 \right )  + h(z) \\
& = \underset{z}{\text{argmin}}  \frac{1}{2t} \left ( \parallel z - x \parallel_2 ^2 + 2t \nabla g(x)^T (z - x) + t^2 \parallel \nabla g(x) \parallel_2 ^2 \right ) + h(z) \\
& = \underset{z}{\text{argmin}}   \frac{1}{2t} \parallel z - (x - t \nabla g(x) )\parallel_2 ^2 + h(z) \\
\end{align} $$

When moving from the 2nd to the 3rd line, the term $$g(x)$$ is removed as a constant term with respect to z, and the term $$\frac{t}{2} \parallel \nabla g(x)^T \parallel_2 ^2 $$ is added. In the final equation, the first term $$\frac{1}{2t} \parallel z - (x - t \nabla g(x) )\parallel_2 ^2$$ is the term that brings it closer to the gradient update position of $$g$$, and the second term $$h(z)$$ is the term that reduces $$h$$.

## Proximal gradient descent
Proximal gradient descent starts from an initial point $$x^{(0)}$$ and iteratively applies the following update:

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) )$$, $$k=1,2,3,...$$

Here, $$\text{prox}_{t}$$ is defined as the proximal mapping:

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\arg \min}  \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

If we rewrite this in the update form we have seen so far, it becomes:

> \begin{align}
x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{where} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\
\end{align}

##  What good did this do?
What is the benefit of doing this? Could it be just changing the problem to another form of minimization problem?

The key point is that for most of the main $$h$$ functions, $$\text{prox}_{t}(\cdot)$$ can be computed analytically. In other words, it can be calculated as follows:

* The mapping function $$\text{prox}_{t}(\cdot)$$ depends only on $$h$$, not on $$g$$.
* The function $$g$$ can be very complex, but here we only need to compute the gradient $$\nabla g$$.

The convergence analysis will be done concerning the number of iterations of the algorithm. Note that in each iteration, computing $$\text{prox}_{t}(\cdot)$$ may vary in computational cost depending on $$h$$.

##  Example: ISTA
Let's look at an example of proximal gradient descent. In the previous chapter, the lasso criterion was defined as follows when $$y \in \mathbb{R}^n$$ and $$X \in \mathbb{R}^{n \times p}$$:

> \begin{align}
f(\beta) = \frac{1}{2} \parallel y - X\beta \parallel_2^2 + \lambda \parallel \beta \parallel_1 \\
\end{align}

Here, $$g(\beta) = \frac{1}{2} \parallel y - X\beta \parallel_2^2$$ and $$h(\beta) = \lambda \parallel \beta \parallel_1$$. In this case, the proximal mapping is defined as:

>
$$ \begin{align}
\text{prox}_{t}(\beta) & = \underset{z}{\text{argmin}}  \frac{1}{2t} \parallel \beta - z \parallel_2^2 + \lambda \parallel z \parallel_1 \\
& = S_{\lambda t}(\beta) \\
\end{align} $$

$$S_{\lambda t}(\beta)$$ is the soft-thresholding operator, defined as follows. (For more details, see Chapter 7 Subgradient)

> $$ \begin{align}
[S_{\lambda t}(\beta)]_i =
\begin{cases}
\beta_i - \lambda & \mbox{if } \beta_i \gt \lambda \\
0 & \mbox{if } \lambda \le \beta_i \le \lambda, i = 1, ..., n \\
\beta_i + \lambda & \mbox{if } \beta_i \lt -\lambda \\
\end{cases}
\\
\end{align} $$

Since the gradient of $$g$$ is $$\nabla g(\beta) = -X^{T} (y - X \beta)$$, the proximal gradient update is defined as:

>$$\beta^+ = S_{\lambda t}(\beta + tX^{T} (y - X \beta) )$$

This algorithm is a very simple algorithm called the **iterative soft-thresholding algorithm (ISTA)**. (Beck and Teboulle (2008), "A fast iterative shrinkage-thresholding algorithm for linear inverse problems")

In the following figure, you can clearly see the performance difference between the subgradient method and proximal gradient descent. In terms of the number of iterations, the performance of proximal gradient descent is comparable to that of gradient descent.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/09.01_01_ISTA.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig 1] Example of proximal gradient (ISTA) vs. subgradient method convergence rate [3]</figcaption>
</p>
</figure>

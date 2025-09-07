---
layout: post
title: 15-01-03 Log barrier calculus
chapter: "15"
order: 5
owner: "Minjoo Lee"
categories:
- chapter15
---
The gradient and Hessian of the log barrier function are as follows.
>
\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}

Gradient:
>
\begin{align}
\nabla \phi(x) = - \sum_{i=1}^{m} \frac{1}{h_i(x)} \nabla h_i(x)
\end{align}

Hessian:

>
\begin{align}
\nabla^2 \phi(x) = \sum_{i=1}^{m} \frac{1}{h_i(x)^2} \nabla h_i(x) \nabla h_i(x)^T -  \sum_{i=1}^{m} \frac{1}{h_i(x)} \nabla^2 h_i(x)
\end{align}

## Example: $$\phi(x) = -\sum_{i=1}^{n} \log(x_i)$$
If we compute the gradient and Hessian for the barrier function $$\phi(x) = -\sum_{i=1}^{n} \log(-x_i)$$, we get the following results.
>
\begin{align}
\phi(x) = -\sum_{i=1}^{n} \log(x_i)
\end{align}
Therefore, $$h_i(x) =  -x_i$$ and $$x_i \ge 0$$.

Gradient:
>
$$
\nabla \phi(x) = - 
\begin{bmatrix}
1/x_1 \\\
\vdots \\\
1/x_n \\\
\end{bmatrix}
 = -X^{-1} \mathbb{1}, \qquad X = \text{diag}(x)$$
 
Hessian :
>
$$
\nabla^2 \phi(x) = 
\begin{bmatrix}
1/x_1^2 & \cdots & \\\
\vdots & \ddots & \vdots  \\\
& \cdots & 1/x_n^2 \\\
\end{bmatrix}
 = X^{-2}$$
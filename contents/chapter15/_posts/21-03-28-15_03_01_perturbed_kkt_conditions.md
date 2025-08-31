layout: post
title: 15-03-01 Perturbed KKT conditions
chapter: "15"
order: 8
owner: "Minjoo Lee"
If we derive the KKT conditions from the barrier problem and the original formulation, we get the following.
## KKT conditions for barrier problem
The second term in the KKT conditions for the barrier problem is derived using the gradient of the log barrier function.
>
$$\begin{align}
t \nabla f(x^*(t)) - \sum_{i=1}^{m} \frac{1}{h_i(x^*(t))} \nabla h_i(x^*(t)) + A^Tw = 0  \\\ 
 Ax^*(t) = b, \quad h_i(x^*(t)) \lt 0, \quad i = 1, \cdots , m \\\
\end{align}$$

##  KKT conditions for the original problem
In the KKT conditions for the original problem, complementary slackness gives $$h_i(x^*) \cdot u_i^* = 0$$, but in practice, it is very difficult to know this boundary condition.
>
$$\begin{align}
\nabla f(x^*) + \sum_{i=1}^{m} u_i^* \nabla h_i(x^*) + A^Tv^* = 0 \\\ 
Ax^* = b, \quad h_i(x^*) \le 0, \quad u_i^* \ge 0,   \\\ 
h_i(x^*) \cdot u_i^* = 0,  \quad i = 1, \cdots , m \\\
\end{align}$$


## Redefinition of KKT conditions for barrier problem
So, what is the relationship between these two KKT conditions?

First, let $$u_i(t)$$ and $$v$$ be defined as follows:
>
$$\begin{align}
u_i(t) = - \frac{1}{t h_i(x^*(t))}, \quad v = \frac{1}{t}w
\end{align}$$

Let's redefine the KKT conditions for the barrier problem.

Looking at the redefined problem, we see that the KKT conditions are almost identical to those for the original problem. In this equation, $$u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}$$ becomes 0 as $$t \to \infty$$, which matches $$h_i(x^*) \cdot u_i^* = 0$$ in the original formulation.

>
$$\begin{align}
& \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)) + tA^Tv = 0  \\\ 
& Ax^*(t) = b, \quad u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}, \quad h_i(x^*(t)) \lt 0, \quad u_i(t) \gt 0 , \quad i = 1, \cdots , m \\\
\end{align}$$
---
layout: post
title: 17-04 Special case, linear programming
chapter: '17'
order: 8
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---
In this section, let's look at an example of the Primal-Dual method for LP (linear programming) problems.

## Linear programming
Consider the following primal LP problem.
>$$
>\begin{align}
>    &\min_{x} && {c^Tx} \\\\
>    &\text{subject to } && {Ax = b} \\\\
>    & &&{x ≥ 0} \\\
>\end{align}
>$$
>
> $$\text{for } c ∈R^n, A ∈R^{m×n}, b ∈R^m$$


The dual problem of the above primal LP problem is as follows.
>$$
>\begin{align}
>    &\max_{y,s}  && {b^Ty} \\\\
>    &\text{subject to } && {A^Ty + s = c} \\\\
>    & &&{s ≥ 0} \\\
>\end{align}
>$$


## Optimality conditions and central path equations
The following shows the optimality conditions (KKT Conditions) for the primal-dual problem of the previous LP.
> $$
> \begin{array}{rcl}
> A^Ty + s & = & c \\\
> Ax & = & b \\\
> XS\mathbb{1} & = & 0 \\\
> x,s  & \succeq & 0
> \end{array}
> $$


Central path equations
> $$
> \begin{array}{rcl}
> A^Ty + s & = & c \\\
> Ax & = & b \\\
> XS\mathbb{1} & = & τ\mathbb{1} \\\
> x,s  & > & 0
> \end{array}
> $$


## Primal-dual method vs. barrier method
### Newton steps for primer-dual method
The following is the Newton equation for the primal-dual method for LP problems.

> $$\begin{bmatrix}
0 & A^T & I \\\
A & 0 & 0 \\\
S & 0 & X 
\end{bmatrix}
\begin{bmatrix}
∆x \\\
∆y \\\
∆s 
\end{bmatrix}= −
\begin{bmatrix}
A^Ty + s−c \\\
Ax−b \\\
XS\mathbb{1}−τ\mathbb{1} 
\end{bmatrix}$$

From the optimal condition, we can know the following relationship.

$$XS\mathbb{1} = \tau \mathbb{1} \iff s = \tau X^{−1}\mathbb{1} \iff x = \tau S^{−1}\mathbb{1}$$

Accordingly, we can obtain optimal conditions for the primal barrier problem by removing $$s$$, or obtain optimal conditions for the dual barrier problem by removing $$x$$.

### Newton steps for barrier problems
The following are the primal and dual central path equations for the barrier problem. (Left is primal, right is dual)
> $$
> \begin{array}{rcr}
> A^Ty + τX^{−1}1 & = & c & \qquad \qquad & A^Ty + s & = & c \\\
> Ax & = & b & \qquad \qquad & τAS^{−1}\mathbb{1} & = & b\\\
> x & > & 0 & \qquad \qquad & s & > & 0
> \end{array}
> $$
> 

Using the above central path equations, the Newton steps for primal and dual are as follows.

**Primal Newton step**
> $$\begin{bmatrix}
τX^{−2} & A^T \\\
A & 0
\end{bmatrix}
\begin{bmatrix}
∆x \\\
∆y
\end{bmatrix}= −
\begin{bmatrix}
A^Ty + τX^{−1}\mathbb{1}−c \\\
Ax−b 
\end{bmatrix}$$ 

**Dual Newton step**
> $$\begin{bmatrix}
A^T & I \\\
0 & τAS^{−2}
\end{bmatrix}
\begin{bmatrix}
∆y \\\
∆s
\end{bmatrix}= −
\begin{bmatrix}
A^Ty + s −c \\\
τAS^{−1}\mathbb{1}−b
\end{bmatrix}$$ 


## Example: barrier versus primal-dual
### Standard LP : $$n = 50$$, $$m = 100$$
To verify the performance of the Primal-dual method, let's look at an example of a standard LP problem with $$n = 50$$ variables and $$m = 100$$ equality constraints. (Example from B & V 11.3.2 and 11.7.4)

The Barrier method used various $$\mu$$ values (2, 50, 150) while the primal-dual method fixed $$\mu$$ at 10.
Both methods used $$\alpha = 0.01, \beta = 0.5$$.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter17/barrier_vs_primal_dual.png">
  <figcaption style="text-align: center;">[Fig1] Duality gap (Barrier vs. Primal-dual) [1]</figcaption>
</p>
</figure>

As can be seen from the graph, primal-dual converges quickly while showing high accuracy.

### Sequence of problem : $$n = 2m$$ and $$n$$ growing. 
Now let's look at the performance for a series of problems where $$n = 2m$$ and $$n$$ gradually increases.

* The Barrier method used $$\mu = 100$$ and the outer loop was performed only about 2 times. (The duality gap was reduced to $$10^4$$) 
* The Primal-dual method used $$\mu = 10$$ and stopped execution when the duality gap and feasibility gap were approximately $$10^{-8}$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter17/barrier_vs_primal_dual2.png">
  <figcaption style="text-align: center;">[Fig2] Newton iteration (Barrier vs. Primal-dual) [1]</figcaption>
</p>
</figure>

As can be seen from the above figure, the Primal-dual method finds solutions with higher accuracy but requires some additional iterations.









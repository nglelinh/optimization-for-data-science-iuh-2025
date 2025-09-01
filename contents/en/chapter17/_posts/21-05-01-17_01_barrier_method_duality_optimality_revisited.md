---
layout: post
title: 17-01 Barrier method & duality & optimality revisited
chapter: '17'
order: 2
owner: Minjoo Lee
categories:
- chapter17
lang: en
---

In Chapter 15, we examined the barrier method, and in Chapters 13 and 16, we looked at duality.
Before covering the content of this chapter, we want to briefly review the barrier method and duality.



## Barrier method
When the following primal problem is convex and $$f, h_i , i = 1, . . . m$$ are differentiable,   
> $$\begin{align}
> &\min_{x} && f(x) \\
> &\text{subject to } &&h_{i}(x) \leq 0, i = 1, \dotsc, m \\
> &&& Ax = b \\
> \end{align}$$

Using the log barrier function, the primal problem can be transformed into a barrier problem as follows:

> $$\begin{align}
> & \min_{x} && f(x) + \frac{1}{t} \phi(x) & \qquad & \min_{x} && tf(x) + \phi(x) \\
> & \text{subject to } && Ax = b & \iff \qquad & \text{subject to } && Ax = b \\
> & \text{where } && \phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
> \end{align}$$

The algorithm starts with $$t = t^{(0)}$$ satisfying $$t > 0$$ and increases until $$\frac{m}{t}$$ becomes less than or equal to $$\epsilon$$. At this time, Newton's method is used to find $$x^{\star}(t)$$ for the initial value $$x^{(0)}$$, and the process of finding $$x^{(k+1)} = x^{\star}(t)$$ at each step for $$k = 1, 2, 3, . . .$$ is repeated.

The algorithm can be briefly summarized as follows:

1. Choose $$t^{(0)} \gt 0$$ and $$k := 0$$.
2. Solve the barrier problem at $$t = t^{(0)}$$ to find $$x^{(0)} = x^{\star}(t)$$.
3. While $$m/t \gt \epsilon$$ <br>
  3-1. Update $$t^{(k+1)} = µt$$ where $$(µ > 1)$$ <br>
  3-2. Initialize Newton's method with $$x^{(k)}$$ (warm start)<br>
        Solve the barrier problem at $$t = t^{(k+1)}$$ to find $$x^{(k+1)} = x^{\star}(t)$$.<br>
  end while<br>

* For detailed information, see [15-01-02 Log barrier function & barrier method]({% multilang_post_url contents/chapter15/21-03-28-15_01_02_log_barrier_function_and_barrier_method %})


## Duality
When the following primal problem is given: 
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad f Ax = b \\\\
>    &\quad h(x) \le 0
>\end{align}
>$$

This can be transformed into Lagrangian form as follows:
>$$
>L(x,u,v) = f(x) + u^Th(x) + v^T(Ax - b)
>$$

Using the Lagrangian defined in this way, primal and dual problems can be redefined in the following form. Please refer to Chapter 16 for detailed information.<br>
#### Primal Problem
>$$
>\min_x \mathop{\max_{u,v}}_{u \geq 0} L(x,u,v)
>$$

#### Dual problem
>$$
>\mathop{\max_{u,v}}_{u \geq 0} \min_x L(x,u,v)
>$$

## Optimality conditions

When $$f,h_1,...h_m$$ are convex and differentiable, and the given problem satisfies strong duality, the KKT optimality conditions for this problem are as follows:

> $$
> \begin{array}{rcl}
> ∇f(x) +∇h(x)u + A^Tv & = & 0 & \text{(Stationarity)}\\\
>  Uh(x) & = & 0 & \text{(Complementary Slackness)} \\\
> Ax & = & b & \text{(Primal Feasibility)}\\\
> u,−h(x)  & ≥ & 0 & \text{(Dual Feasibility)}
> \end{array}
> $$

Here, $$U$$ means $$\text{diag}(u)$$, and $$∇h(x)$$ means $$ [ ∇h_1(x) ··· ∇h_m(x) ]$$.

* For detailed information, see [Chapter 12 KKT conditions]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %})

## Central path equations
The function $$f(x)$$ can be redefined as a barrier problem as follows.<br>
In the equation below, $$τ$$ is $$\frac{1}{t}$$, and by making $$τ$$ gradually approach 0 and iteratively finding solutions, we ultimately obtain the solution to the original problem.

>$$
>\begin{align}
>&\min_{x} && {f(x) + τ\phi(x)} \\\\
>& &&{Ax = b} \\\
>& \text{where } && \phi(x) = −\sum_{i=1}^m \log(−h_i(x)).
>\end{align}
>$$

That is, in the above equation, differences from the primal problem occur depending on $$τ$$, and the trajectory generated according to $$τ$$, i.e., the set of solutions to the barrier problem, is called the central path.

And the optimality conditions for this barrier problem are as follows:
> $$
> \begin{array}{rcl}
> ∇f(x) +∇h(x)u + A^Tv  & = & 0 \\\
> Uh(x) & = & −τ\mathbb{1} \\\
> Ax & = & b \\\
> u,−h(x)  & > & 0
> \end{array}
> $$
 
* For detailed information, see [16-02 Optimality conditions]({% multilang_post_url contents/chapter16/21-03-31-16_02_optimality_conditions %})

The **Primal-Dual interior point method** introduced in this chapter is a method that defines the first three equations above as residuals and finds solutions by reducing them to $$0$$.

##### Useful fact
The solution $$(x(τ),u(τ),v(τ))$$ has a duality gap of size $$mτ$$, i.e., $$\frac{m}{t}$$, as follows:
> $$f(x(τ))−\min_x L(x,u(τ),v(τ)) = mτ= \frac{m}{t}$$


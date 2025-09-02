---
layout: post
title: 16-02 Optimality conditions
chapter: '16'
order: 3
owner: Minjoo Lee
categories:
- chapter16
lang: en
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In this section, we will examine the KKT optimality conditions for primal problems and barrier problems respectively, and then compare their differences.
<br/>

## KKT optimality conditions

Let's review the KKT conditions that we covered in Chapter 12. KKT conditions are used as conditions for determining optimality.

### Primal problem
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

When the given primal problem is convex, KKT conditions become sufficient conditions for primal & dual optimality. That is, when $$f, h_1, \dots, h_m$$ are convex and $$l_1, \dots, l_r$$ are affine, if $$x^\star, u^\star, v^\star$$ satisfy the following KKT conditions, then $$x^\star$$ and $$(u^\star, v^\star)$$ are primal & dual optimal with zero duality gap. (We assume that $$f, h_1, \dots, h_m, l_1, \dots, l_r$$ are differentiable.) <br>

* 참고: [12-01 KKT conditions]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %})

### KKT conditions for the given primal problem
>$$
>\begin{align}
>l_i &= 0, \quad i=1, \dots, r\\\\
>u_i^\star, -h_i(x^\star) &\ge 0, \quad i=1, \dots, m\\\\
>u_i^\star h_i(x^\star) &= 0, \quad i=1, \dots, m\\\\
>\nabla f(x^\star) + \sum_{i=1}^m \nabla h_i(x^\star) u^\star_i + \sum_{i=1}^r \nabla l_i(x^\star) v_i^\star &= 0.\\\\
>\end{align}
>$$

## Central path equations

Let's also examine the conditions for determining the optimality of barrier problems.

### Barrier problem

>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad f(x) + \tau \phi(x) \\\\
    &\quad l_j(x) = 0, j = 1, \ldots, r  \\\\
\end{align}$$
>
>$$ \text{where } \phi(x) = - \sum_{i=1}^m \log \big( -h_i(x) \big).$$


By organizing the KKT conditions for barrier problems, we can derive the following optimality conditions. Note the differences in the inequality constraint and complementary slackness conditions compared to the KKT optimality conditions for primal problems examined earlier. (Reference: [15-03-01 Perturbed KKT conditions]({% multilang_post_url contents/chapter15/21-03-28-15_03_01_perturbed_kkt_conditions %}))

### Optimality conditions for barrier problem (and its dual)

>$$
\begin{align}
l_i &= 0, \quad i=1, \dots, r\\\\
u_i(t), -h_i(x^\star(t)) &\gt 0, \quad i=1, \dots, m\\\\
u_i(t) h_i(x^\star(t)) &= -\tau, \quad i=1, \dots, m\\\\
\nabla f(x^\star(t)) + \sum_{i=1}^m \nabla h_i(x^\star(t)) u_i(t) + \sum_{i=1}^r \nabla l_i(x^\star(t)) \hat{v}_i^\star &= 0,\\\\
\end{align} \\\\
$$
>
>$$\text{where } \tau = \frac{1}{t}, u_i(t) = - \frac{1}{t h_i(x^\star(t))}, \quad \hat{v} = \frac{1}{t}v.$$

## Special case: linear programming

### Recall: Primal problem of LP in standard form
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0
>\end{align}
>$$

### Recall: Dual problem of LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>    &\quad s \ge 0
>\end{align}
>$$

Linear programming has the nice property of always satisfying strong duality due to the refined Slater's condition, since the inequality constraints are affine. The optimality conditions for LP are as follows:

>$$
>\begin{align}
>A^T y^\star + s^\star &= c\\\\
>Ax^\star &= b\\\\
>X S \mathbb{1} &= 0\\\\
>x^\star, s^\star &\ge 0,\\\\
>\end{align}$$
> 
>$$text{where }X = Diag(x^\star), S = Diag(s^\star)$$

Note that $$X S \mathbb{1} = 0$$ is equivalent to $$Xs^\star=(x_1^\star s_1^\star, \dots, x_n^\star s_n^\star)=0$$. We use $$X, S$$ notation for convenience in algorithms that will be introduced later.

### Algorithms for linear programming

We introduce two representative methods for solving LP using optimality conditions.

1. Simplex: A method that maintains conditions 1, 2, and 3 while gradually satisfying condition 4.
2. Interior-point methods: A method that maintains condition 4 while gradually satisfying conditions 1, 2, and 3. This will be covered in the next chapter.

## Central path for linear programming

### Recall: Barrier problem for LP
>$$\begin{align}
    \mathop{\text{minimize}}_x &\quad c^Tx - \tau \sum_{i=1}^n \log(x_i)\\\\
    \text{subject to} &\quad Ax = b, \\\\
    \text{where}  &\quad \tau > 0
\end{align}$$


### Recall: Dual problem of Barrier problem for LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

The optimality conditions for the barrier problem of LP are as follows:

>$$
\begin{align}
A^T y^\star + s^\star &= c\\\\
Ax^\star &= b\\\\
X S \mathbb{1} &= \tau \mathbb{1}\\\\
x^\star, s^\star &\gt 0,\\\\
\text{where} &\quad X = Diag(x^\star), S = Diag(s^\star)
\end{align}$$

Conditions 3 and 4 show differences from the KKT conditions of the primal LP.
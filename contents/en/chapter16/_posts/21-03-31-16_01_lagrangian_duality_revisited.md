---
layout: post
title: 16-01 Lagrangian duality revisited
chapter: '16'
order: 2
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

In this section, we will show that primal and dual problems can be defined using the Lagrangian, and use this definition to derive dual problems for standard form linear programming and quadratic programming. Furthermore, we will derive the dual problem for linear programming with barrier problems applied, showing that its form is the same as the barrier problem for the dual problem of linear programming.

<br/>
First, let's define the primal problem and Lagrangian as follows.

#### Primal problem
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

#### Lagrangian
>$$
>L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i (x) + \sum_{j=1}^r v_j l_j (x)
>$$

<br/>
At this point, the primal problem and dual problem can be redefined as problems involving the Lagrangian.

#### Rewritten primal problem
>$$
>\min_x \mathop{\max_{u,v}}_{u \geq 0} L(x,u,v)
>$$

The redefined primal problem does not explicitly state constraints, but it has the effect of acting like an indicator function for any infeasible $$x$$ that violates the constraints.

1. If $$h_i(\hat{x}) \gt 0$$ for some $$i \in [1, m]$$, then $$\hat{x}$$ is an infeasible point. In this case, $$u_i h_i(\hat{x})$$ diverges to $$\infty$$ due to $$\max_{u,v}$$, so it acts as an indicator function for any $$\hat{x}$$ that violates the inequality constraint.
2. If $$l_i(\hat{x}) \neq 0$$ for some $$i \in [1, r]$$, then $$\hat{x}$$ is an infeasible point. In this case, $$v_i l_i(\hat{x})$$ diverges to $$\infty$$ due to $$\max_{u,v}$$, so it acts as an indicator function for any $$\hat{x}$$ that violates the equality constraint.

#### Rewritten dual problem
>$$
>\mathop{\max_{u,v}}_{u \geq 0} \min_x L(x,u,v)
>$$

In the dual problem, relaxation of the domain is necessary, so it should not act as an indicator function for the constraints of the primal problem. Since taking $$\min_x$$ for fixed $$u, v$$ cannot enforce the constraints of the primal problem, the redefined dual problem also has the effect of relaxing the domain. (Reference: [11-02 Lagrange dual function]({% multilang_post_url contents/chapter11/21-03-24-11_02_Lagrange_dual_function %}))

## Weak and strong duality
Let's revisit weak duality and strong duality.

#### Theorem: weak duality
When $$p$$ and $$d$$ are the optimal values for the primal problem and dual problem respectively, the following is always satisfied:


$$
p \ge d
$$

#### Theorem: strong duality (refined Slater's condition)
For the domain set $$D$$, assume that $$f, h_1, \dots, h_p$$ are convex and $$h_{p+1}, \dots, h_m, l_1, \dots, l_r$$ are affine. If there exists $$\hat{x} \in \text{relint}(D)$$ that satisfies the following:
> $$\begin{align}
>h_i(\hat{x}) \ & \lt 0, \ && i=1, \dots, p \\
>h_i(\hat{x}) \ & \le 0, \ && i=p+1, \dots, m \\
>l_j(\hat{x}) \ & = 0, \ && j = 1, \dots, r
\end{align}$$

then $$p = d$$ is guaranteed for the optimal values $$p, d$$ of the primal problem and dual problem.

## Example: linear programming
Let's derive the dual problem of linear programming using the dual problem defined earlier.

#### Primal problem of LP in standard form
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0
>\end{align}
>$$

According to the previous definition, the dual problem of the above problem is as follows:

$$\mathop{\max_{s,y}}_{s\ge0} \min_{x} \: L(x,s,y) = \mathop{\max_{s,y}}_{s\ge0} \min_{x} \: c^Tx - s^Tx + (b-Ax)^T y$$

We substitute the relationship $$c=A^Ty +s$$ obtained by solving $$\nabla_x L = 0$$ into the dual problem.

$$\mathop{\max_{s,y}}_{s\ge0} \: (A^Ty + s)^Tx - s^Tx + (b-Ax)^Ty \quad \text{ s.t. } c=A^Ty +s$$

This can be organized as follows:

#### Dual problem of LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = 0 \\\\
>    &\quad s \ge 0
>\end{align}
>$$


## Example: convex quadratic programming
Now let's derive the dual problem of quadratic programming using the dual problem defined earlier.

#### Primal problem of QP in standard form
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad \frac{1}{2} x^T Q x + c^Tx \\
>    \text{subject to} &\quad Ax = b \\
>    &\quad x \ge 0, \\
>
>\end{align}$$
>
>$$\text{where } Q \text{ is symmetric and positive semidefinite.}$$


According to the previous definition, the dual problem of the above problem is as follows:

$$\mathop{\max_{s,y}}_{s\ge0} \min_{x} \: L(x,s,y) = \mathop{\max_{s,y}}_{s\ge0} \min_{x} \:  \frac{1}{2} x^T Q x + c^Tx - s^Tx + (b-Ax)^T y$$


We substitute the relationship $$Qx = A^Ty +s - c$$ obtained by solving $$\nabla_x L = 0$$ into the dual problem.

$$
\begin{align}
&\mathop{\max_{s,y,x}}_{s\ge0} \: \frac{1}{2} x^T (A^Ty +s - c) + c^Tx - s^Tx + (b-Ax)^T y \quad \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0} \: x^T (A^Ty +s - c) + c^Tx - s^Tx + (b-Ax)^T y -  \frac{1}{2} x^T (A^Ty +s - c) \quad \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0}  \: b^Ty - \frac{1}{2} x^T (A^Ty +s - c) \quad  \text{ s.t. } Qx = A^Ty +s - c\\\\
&= \mathop{\max_{s,y,x}}_{s\ge0}  \: b^Ty - \frac{1}{2} x^T Q x \quad \text{ s.t. } Qx = A^Ty +s - c
\end{align}
$$

This can be organized as follows:

#### Dual problem of QP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y,x} &\quad b^Ty - \frac{1}{2} x^T Q x\\\\
>    \text{subject to} &\quad A^Ty +  s - c = Qx \\\\
>    &\quad s \ge 0
>\end{align}
>$$

The dual problem of a quadratic problem is also a quadratic problem.

## Example: barrier problem for linear programming
The barrier problem for linear programming is defined as follows:

#### Barrier problem for LP
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx - \tau \sum_{i=1}^n \log(x_i)\\
>    \text{subject to} &\quad Ax = b, \\
>\end{align}$$
>
>$$\text{where }\tau > 0.$$


According to the previous definition, the dual problem of the above problem is as follows:
$$
\begin{align}
\max_{y} \min_{x} \: L(x,y) &= \max_{y} \min_{x} \:  c^Tx - \tau \sum_{i=1}^n \log(x_i) + (b-Ax)^T y\\\\
&=  \max_{y} \min_{x} \:  \underbrace{(c-A^Ty)}_{s \doteq c-A^Ty}x - \tau \sum_{i=1}^n \log(x_i) + b^Ty\\\\
&= \max_{y} \min_{x} \: \sum_{i=1}^n \big( s_i^Tx_i - \tau  \log(x_i) \big) + b^Ty  \quad \text{ s.t. } A^Ty +s = c
\end{align}
$$

Here, $$\sum_{i=1}^n \big( s_i^Tx_i - \tau  \log(x_i) \big) + b^Ty$$ will be minimized when $$x_i = \frac{\tau}{s_i}$$. Therefore, let's substitute $$\frac{\tau}{s_i}$$ for $$x_i$$ in the dual problem.

$$
\begin{align}
&\max_{s,y} \: b^Ty + n\tau - \tau \sum_{i=1}^n log(\frac{\tau}{s_i}) \quad \text{ s.t. } A^Ty +s = c\\\\
&= \max_{s,y} \: b^Ty + \tau \sum_{i=1}^n log(s_i) + n\tau - n\tau\log(\tau) \quad \text{ s.t. } A^Ty +s = c\\\\
\end{align}
$$

Since $$n\tau - n\tau\log(\tau)$$ can be omitted from the problem, the dual problem can be organized as follows:

#### Dual problem of Barrier problem for LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

We can see that this problem is identical to the barrier problem for the dual problem of linear programming.

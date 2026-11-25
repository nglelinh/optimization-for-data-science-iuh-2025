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

Here is one of the most astonishing symmetries in convex optimization: take a standard-form linear program, add a logarithmic barrier to its primal inequalities, and compute the Lagrange dual of that barrier problem. You don't get some messy new formula—you get the *exact* logarithmic barrier problem of the **dual** linear program! Seeing how min–max Lagrangians produce LP duals, QP duals, and this primal-dual barrier mirror lays the exact foundation for Chapter 17.

## Background Knowledge Map: Min–Max Lagrangians and Conic/Barrier Duals

- **Pillar 1 — Constraints as Implicit $$\max_{u \ge 0, v}$$ Penalties:** Rewriting the primal as $$\min_x \max_{u \ge 0, v} L(x, u, v)$$ uses $$\max_{u \ge 0} u_i h_i(x)$$ as an exact indicator function for $$h_i(x) \le 0$$, and swapping $$\min$$ and $$\max$$ yields the dual.
- **Pillar 2 — Standard-Form LP & QP Duals:** Applying $$\min_x L(x, u, v)$$ to $$\min c^T x$$ s.t. $$Ax = b, x \ge 0$$ yields $$\max b^T y$$ s.t. $$A^T y \le c$$; for strictly convex QPs $$\frac{1}{2}x^T Q x + c^T x$$, minimizing the quadratic in $$x$$ replaces $$Q$$ with $$-Q^{-1}$$ in the dual.
- **Pillar 3 — Dual of the Primal Barrier = Barrier of the Dual:** For the LP barrier $$\min t c^T x - \sum \log x_i$$ s.t. $$Ax = b$$, minimizing $$L(x, y)$$ over $$x > 0$$ yields $$x_i = 1/(t(c - A^T y)_i)$$ and dual objective $$t b^T y + \sum \log(c - A^T y)_i + \text{const}$$—the exact dual log barrier!
- **Pillar 4 — Automatic Dual Slack Recovery:** Along the central path, $$s(t) = c - A^T y(t) > 0$$ satisfies $$x_i(t) s_i(t) = 1/t$$, linking primal variables and dual slacks symmetrically.

### Step-by-Step Worked Example (Read Slowly): Deriving the Dual of a 1D LP Barrier Problem

Consider the 1D LP $$\min_{x > 0} 3x$$ subject to $$x \ge 0$$ with a single equality constraint $$2x = 4$$? Better yet, to keep a free primal degree of freedom, consider $$\min_{x_1, x_2 > 0} x_1 + 2x_2$$ subject to $$x_1 + x_2 = 1$$ (so $$c = (1, 2)^T$$, $$A = [1, 1]$$, $$b = 1$$).

1. **Write the primal barrier problem ($$t = 1$$):**
   $$\min_{x_1, x_2 > 0} \; x_1 + 2x_2 - \log x_1 - \log x_2 \quad \text{s.t.} \quad x_1 + x_2 = 1.$$
2. **Form the Lagrangian with dual multiplier $$y \in \mathbb{R}$$:**
   $$L(x, y) = x_1 + 2x_2 - \log x_1 - \log x_2 + y(1 - x_1 - x_2) = y + (1 - y)x_1 - \log x_1 + (2 - y)x_2 - \log x_2.$$
3. **Minimize over $$x_1, x_2 > 0$$:**
   - Finite only when $$s_1 = 1 - y > 0$$ and $$s_2 = 2 - y > 0$$ (i.e., $$A^T y < c$$ — strict dual feasibility!).
   - Stationarity gives $$x_1 = \frac{1}{1 - y}$$ and $$x_2 = \frac{1}{2 - y}$$.
   - Substitute back:
     $$g(y) = y + 1 + \log(1 - y) + 1 + \log(2 - y) = y + \log(1 - y) + \log(2 - y) + 2.$$
4. **Recognize the dual:** Maximizing $$g(y)$$ over $$y < 1$$ is *literally* the log-barrier problem for the dual LP $$\max_y y$$ s.t. $$y \le 1, y \le 2$$ (up to the constant $$+2$$)!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In this section, we will show that primal and dual problems can be defined using the Lagrangian, and use this definition to derive dual problems for standard form linear programming and quadratic programming. Furthermore, we will derive the dual problem for linear programming with barrier problems applied, showing that its form is the same as the barrier problem for the dual problem of linear programming.

<br/>
First, let's define the primal problem and Lagrangian as follows.

### Primal problem
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

### Lagrangian
>$$
>L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i (x) + \sum_{j=1}^r v_j l_j (x)
>$$

<br/>
At this point, the primal problem and dual problem can be redefined as problems involving the Lagrangian.

### Rewritten primal problem
>$$
>\min_x \mathop{\max_{u,v}}_{u \geq 0} L(x,u,v)
>$$

The redefined primal problem does not explicitly state constraints, but it has the effect of acting like an indicator function for any infeasible $$x$$ that violates the constraints.

1. If $$h_i(\hat{x}) \gt 0$$ for some $$i \in [1, m]$$, then $$\hat{x}$$ is an infeasible point. In this case, $$u_i h_i(\hat{x})$$ diverges to $$\infty$$ due to $$\max_{u,v}$$, so it acts as an indicator function for any $$\hat{x}$$ that violates the inequality constraint.
2. If $$l_i(\hat{x}) \neq 0$$ for some $$i \in [1, r]$$, then $$\hat{x}$$ is an infeasible point. In this case, $$v_i l_i(\hat{x})$$ diverges to $$\infty$$ due to $$\max_{u,v}$$, so it acts as an indicator function for any $$\hat{x}$$ that violates the equality constraint.

### Rewritten dual problem
>$$
>\mathop{\max_{u,v}}_{u \geq 0} \min_x L(x,u,v)
>$$

In the dual problem, relaxation of the domain is necessary, so it should not act as an indicator function for the constraints of the primal problem. Since taking $$\min_x$$ for fixed $$u, v$$ cannot enforce the constraints of the primal problem, the redefined dual problem also has the effect of relaxing the domain. (Reference: [11-02 Lagrange dual function]({% multilang_post_url contents/chapter11/21-03-24-11_02_Lagrange_dual_function %}))

## Weak and strong duality
Let's revisit weak duality and strong duality.

### Theorem: weak duality
When $$p$$ and $$d$$ are the optimal values for the primal problem and dual problem respectively, the following is always satisfied:


$$
p \ge d
$$

### Theorem: strong duality (refined Slater's condition)
For the domain set $$D$$, assume that $$f, h_1, \dots, h_p$$ are convex and $$h_{p+1}, \dots, h_m, l_1, \dots, l_r$$ are affine. If there exists $$\hat{x} \in \text{relint}(D)$$ that satisfies the following:
> $$\begin{align}
>h_i(\hat{x}) \ & \lt 0, \ && i=1, \dots, p \\
>h_i(\hat{x}) \ & \le 0, \ && i=p+1, \dots, m \\
>l_j(\hat{x}) \ & = 0, \ && j = 1, \dots, r
\end{align}$$

then $$p = d$$ is guaranteed for the optimal values $$p, d$$ of the primal problem and dual problem.

## Example: linear programming
Let's derive the dual problem of linear programming using the dual problem defined earlier.

### Primal problem of LP in standard form
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

### Dual problem of LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = 0 \\\\
>    &\quad s \ge 0
>\end{align}
>$$


## Example: convex quadratic programming
Now let's derive the dual problem of quadratic programming using the dual problem defined earlier.

### Primal problem of QP in standard form
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

### Dual problem of QP
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

### Barrier problem for LP
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

### Dual problem of Barrier problem for LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

We can see that this problem is identical to the barrier problem for the dual problem of linear programming.

---
layout: post
title: 10-02 Duality in general LPs
chapter: '10'
order: 3
owner: Wontak Ryu
categories:
- chapter10
lang: en
lesson_type: required
---

Once you see how multiplier weights generate lower bounds on 2-variable examples, lifting the same construction to general matrix-vector linear programs $$\min \{c^\top x : Ax = b,\; Gx \le h\}$$ takes just three lines of linear algebra. Instead of memorizing arbitrary sign tables, writing the constraints in matrix form shows immediately how $$A$$ and $$G$$ transpose into the dual constraints $$-A^\top v - G^\top u = c$$ and why the dual objective becomes $$-b^\top v - h^\top u$$.

## Background Knowledge Map: Matrix Mechanics of General LP Duality

- **Pillar 1 — Transposition of Constraint Matrices:** Primal constraints map $$x \in \mathbb{R}^n$$ to $$m$$ equalities ($$Ax = b$$) and $$r$$ inequalities ($$Gx \le h$$). Dual multipliers $$v \in \mathbb{R}^m$$ and $$u \in \mathbb{R}_+^r$$ map back via $$A^\top$$ and $$G^\top$$ into $$\mathbb{R}^n$$, coupling every primal variable to one dual constraint.
- **Pillar 2 — Sign Correspondence Dictionary:** Equality primal constraints ($$Ax = b$$) yield *unconstrained* dual variables $$v \in \mathbb{R}^m$$; inequality primal constraints ($$Gx \le h$$) yield *nonnegative* dual variables $$u \ge 0$$. Conversely, unrestricted primal variables $$x \in \mathbb{R}^n$$ yield *equality* dual constraints $$-A^\top v - G^\top u = c$$.
- **Pillar 3 — Standard Form Special Case:** When the primal is $$\min \{c^\top x : Ax = b,\; x \ge 0\}$$ (i.e., $$G = -I, h = 0$$), eliminating $$u \ge 0$$ from $$-A^\top v + u = c$$ produces the famous compact dual $$\max \{b^\top y : A^\top y \le c\}$$ (where $$y = -v$$).
- **Pillar 4 — Primal–Dual Dimension Swap:** A primal with $$n$$ variables and $$m + r$$ constraints produces a dual with $$m + r$$ variables and $$n$$ constraints—so when $$n \gg m + r$$, solving the dual can be dramatically faster than solving the primal directly.

### Step-by-Step Worked Example (Read Slowly): Dualizing a Mixed Equality/Inequality LP in Matrix Form

Consider the primal LP:
$$\min_{x \in \mathbb{R}^2}\; 2x_1 - x_2 \quad \text{s.t.} \quad x_1 + x_2 = 4, \quad x_1 \le 3, \quad -x_2 \le 0.$$

1. **Identify the matrices $$c, A, b, G, h$$:**
   $$c = \begin{pmatrix}2 \\ -1\end{pmatrix}, \quad A = \begin{pmatrix}1 & 1\end{pmatrix}, \quad b = (4), \quad G = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}, \quad h = \begin{pmatrix}3 \\ 0\end{pmatrix}.$$
2. **Introduce dual variables $$v \in \mathbb{R}$$ (for $$Ax = b$$) and $$u = (u_1, u_2)^\top \ge 0$$ (for $$Gx \le h$$):**
   - Dual objective: $$-b^\top v - h^\top u = -4v - 3u_1 - 0 \cdot u_2 = -4v - 3u_1$$.
   - Dual constraints $$-A^\top v - G^\top u = c$$:
     $$-\begin{pmatrix}1\\1\end{pmatrix} v - \begin{pmatrix}u_1 \\ -u_2\end{pmatrix} = \begin{pmatrix}2 \\ -1\end{pmatrix} \implies \begin{cases} -v - u_1 = 2, \\ -v + u_2 = -1, \end{cases} \quad u_1, u_2 \ge 0.$$
3. **Solve the dual by inspection:** From the second equation, $$v = 1 + u_2 \ge 1$$; from the first, $$u_1 = -2 - v \ge 0 \implies v \le -2$$... wait: $$v \ge 1$$ and $$v \le -2$$ cannot both hold! Let's check why:
   Wait—in the primal, $$x_1 + x_2 = 4$$, $$x_1 \le 3$$, $$x_2 \ge 0$$ gives $$x_2 = 4 - x_1 \ge 1$$, so $$x_1$$ can go to $$-\infty$$ ($$x_1 = -100, x_2 = 104$$ is feasible with objective $$2(-100) - 104 = -304 \to -\infty$$)!
4. **Aha! Duality caught unboundedness automatically:** The primal is **unbounded below** ($$p^\star = -\infty$$), which by weak duality *forces* the dual to be **infeasible**—a textbook demonstration of how dual feasibility certifies primal boundedness!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In [10-01]({% multilang_post_url contents/chapter10/21-03-22-10_01_Lower_Bounds_in_Linear_Programs %}), we examined the primal and dual of LP problems with single-dimensional variables. In 10-02, we want to examine the dual for LPs in general form.

The general form of LP is as follows:

Given $$c\in\mathbb{R}^{n},\, A\in\mathbb{R}^{m\times n},\, b\in\mathbb{R}^{m},\, G\in\mathbb{R}^{r\times n},\, h\in\mathbb{R}^{r}$$,

>$$
>\begin{align}
>&\min_{x} &&c^{T}x\\\\
>&\text{subject to} &&Ax = b\\\\
>& &&Gx \leq h.\\\\
>\end{align}
>$$

Similar to the example in 10-01, we define dual variables $$u, v$$ equal in number to the number of constraints,
and can define the objective function of the dual problem and constraints as the sum of products of constraints and each dual variable. 

>$$
>\begin{align}
>& &u^{T}(Ax-b) = 0\\\\
>&{+} &v^{T}(Gx-h)\leq 0\\\\
>&{=} &u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0.\\\\
>\end{align}
>$$

Remember that the dual variable $$u$$ for equality has no constraints, while $$v$$ is a dual variable for inequality and thus has the additional constraint of being positive.
By organizing the last equation to represent the objective function of the primal LP, we get the dual LP.

>$$
>\begin{align}
>u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0 \\\\
>\underbrace{(-A^{T}u-G^{T}v)^{T}}_{=c^{T}}x\geq-b^{T}u-h^{T}v \\\\
>\text{Lower bound is} -b^{T}u-h^{T}v \\\\ 
>\text{for } x \text{ primal feasible, and any u, v satisfies,} \\\\
>c = -A^{T}u-G^{T}v \\\\
>v\geq 0. \\\\
>\end{align}
>$$

That is, when $$c = -A^{T}u-G^{T}v$$, the optimal value of the primal has a lower bound of $$-b^{T}u-h^{T}v$$.

Consequently, the dual LP can be defined as follows.

>$$
>\begin{align}
>&\max_{u,v} &&-b^{T}u-h^{T}v \\\\
>&\text{subject to} &&c = -A^{T}u-G^{T}v \\\\
>& &&v\geq 0.
>\end{align}
>$$


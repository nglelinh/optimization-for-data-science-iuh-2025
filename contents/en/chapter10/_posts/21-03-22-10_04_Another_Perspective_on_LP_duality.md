---
layout: post
title: 10-04 Another Perspective on LP duality
chapter: '10'
order: 5
owner: Wontak Ryu
categories:
- chapter10
lang: en
lesson_type: required
---

Up to now, we derived the LP dual by manually combining inequalities—a clean trick for linear programs, but one that stops working the moment constraints become nonlinear. Here we unlock a far more powerful viewpoint: fold the constraints directly into the objective via a **Lagrangian** $$L(x, u, v) = c^\top x + u^\top(Gx - h) + v^\top(Ax - b)$$, and minimize $$L$$ over *unconstrained* $$x \in \mathbb{R}^n$$! Not only does this reproduce the exact same LP dual in two lines—it serves as the universal bridge to general nonlinear and convex duality in Chapter 11.

## Background Knowledge Map: The Lagrangian Bridge from LPs to General Duality

- **Pillar 1 — Soft Penalty Relaxation:** For any primal-feasible $$x$$ ($$Ax = b, Gx \le h$$) and any $$u \ge 0$$, the extra terms $$u^\top(Gx - h) \le 0$$ and $$v^\top(Ax - b) = 0$$ can only *decrease* the objective: $$L(x, u, v) \le c^\top x$$.
- **Pillar 2 — Unconstrained Infimum as Dual Function:** Minimizing $$L(x, u, v)$$ over all $$x \in \mathbb{R}^n$$ (dropping constraints entirely!) gives $$g(u, v) = \inf_x L(x, u, v) \le \min_{x \in C} L(x, u, v) \le p^\star$$.
- **Pillar 3 — Why Linear Infima Create Hard Dual Constraints:** Rewriting $$L(x, u, v) = (c + G^\top u + A^\top v)^\top x - h^\top u - b^\top v$$ shows that a linear function of $$x$$ is bounded below on $$\mathbb{R}^n$$ *if and only if* its slope is zero: $$c + G^\top u + A^\top v = 0$$. Otherwise $$\inf_x L = -\infty$$!
- **Pillar 4 — Domain Restriction = Dual Feasibility:** Maximizing $$g(u, v)$$ over $$u \ge 0$$ automatically restricts $$(u, v)$$ to the finite domain $$c + G^\top u + A^\top v = 0$$, recovering the exact LP dual without guessing a single multiplier sign.

### Step-by-Step Worked Example (Read Slowly): Computing $$\inf_x L(x, u, v)$$ Explicitly

Consider the 1D LP: minimize $$3x$$ subject to $$x \ge 2$$ (written as $$-x + 2 \le 0$$).

1. **Form the Lagrangian with dual multiplier $$u \ge 0$$:**
   $$L(x, u) = 3x + u(-x + 2) = (3 - u)x + 2u.$$
2. **Minimize $$L(x, u)$$ over all unconstrained $$x \in \mathbb{R}$$:**
   - If $$3 - u > 0$$ (i.e., $$u < 3$$), sending $$x \to -\infty$$ drives $$L(x, u) \to -\infty$$.
   - If $$3 - u < 0$$ (i.e., $$u > 3$$), sending $$x \to +\infty$$ drives $$L(x, u) \to -\infty$$.
   - If $$3 - u = 0$$ (i.e., $$u = 3$$), the $$x$$-term vanishes completely and $$L(x, 3) \equiv 6$$ for every $$x \in \mathbb{R}$$!
3. **Write down the Lagrange dual function $$g(u)$$:**
   $$g(u) = \inf_{x \in \mathbb{R}} L(x, u) = \begin{cases} 6 & \text{if } u = 3, \\ -\infty & \text{otherwise.} \end{cases}$$
4. **Maximize $$g(u)$$ over $$u \ge 0$$:** The only finite point is $$u^\star = 3$$, yielding $$d^\star = 6 = 3(2) = p^\star$$! This exact mechanism—where an unbounded linear infimum enforces an equality constraint—generalizes seamlessly to nonlinear functions in Chapter 11.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>
In the case of duality discussed earlier, for LP, we multiplied the constraints of the primal problem by dual variables, obtained their linear combination, and then organized it to separate out the primal's objective function to obtain a bound. The separated remaining terms (something in the formula below) served as the bound for the primal problem. That is, they became the objective function of the dual problem, and the conditions created during the formula development process became the constraints of the dual problem.
Writing this partial process (the part of the above content that separates out the primal objective function to obtain a bound) as a formula, it looks like this:

>$$
>\begin{align}
>&\min_{x} &&f(x)\\\\
>&\text{subject to} &&Ax = b\\\\
>& &&Gx \leq h\\\\
>\end{align}
>$$

>$$
>\begin{align}
>& &\text{for any }u,\, v\geq 0,\\\\
>& &u^{T}(Ax-b) = 0\\\\
>&{+} &v^{T}(Gx-h)\leq 0\\\\
>&{=} &u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0\\\\
>&{\approx} &f(x)+\text{something}. \\\\
>\end{align}
>$$

However, for optimization problems that are not linear programs, most cannot express the objective function as a linear combination of constraints. 

In this chapter, we examine the perspective of duality that is applicable to more universally common problems (all convex, most non-convex). We will find the duality of LP using this method called Lagrangian, and examine more detailed discussions in Chapter 11.

Looking at the equations up to the linear combination form for the primal LP problem described above, we can understand the following relationship:
>$$
>\begin{align}
>c^{T}x\geq c^{T}x+\overbrace{u^{T} \underbrace{(Ax-b)} _ {=0}+\underbrace{v^{T}} _ {\geq 0} \underbrace{(Gx-h)} _ {\leq 0}} ^ {\leq 0} := L(x,u,v).
>\end{align}
>$$

The right side of the inequality has a value less than or equal to the left side according to the conditions. Also, we define this expression as a function $$L(x, u, v)$$ for x, u, v.
Here, if we call the set satisfying the constraints of the primal LP (primal feasible set) C, we can understand the following relationship:

>$$
>\begin{align}
>C =  \{ x: Ax=b, Gx\leq h \},
>\end{align}
>$$
>$$
>\begin{align}
>f^{*}=\min_{x\in C} f(x) \geq \min_{x\in C}L(x,u,v)\geq \min_{x}L(x,u,v):=g(u,v).\\\\
>\end{align}
>$$

In other words, $$g(u,v)$$ becomes a lower bound of $$f^{*}$$ for any u or $$v$$ satisfying $$v\geq0$$.
Let's examine the lower bound value determined by $$g(u,v)$$.

>$$
>\begin{align}
g(u,v) = min_{x} c^{T}x+u^{T}(Ax-b) + v^{T}(Gx-h) \\\\
= \min_{x} (c+A^{T}u+G^{T}v)^{T}x - b^{T}u-h^{T}v \\\\
\begin{cases}= -b^{T}u-h^{T}v \qquad &\text{if }\ c = -A^{T}u-G^{T}v \\\\
-\infty \qquad &\text{otherwise}.
\end{cases}
>\end{align}
>$$


As can be seen from the equation, when $$c = -A^{T}u-G^{T}v$$ is not satisfied, it has a value of $$-\infty$$ due to the $$x$$ term.
Since we want to find the lower bound closest to $$f^{*}$$, we want to find the value that maximizes $$g(u, v)$$. This is $$-b^{T}u-h^{T}v$$, the value when $$c = -A^{T}u-G^{T}v$$ is satisfied, and this matches the Dual LP we obtained with the first method.

>$$
>\begin{align}
>f^{*} \geq g(u,v), \qquad \text{provided } v \geq 0\\\\
>\text{find the biggest lowerbound  } g(u,v)\\\\
>\max_{u,v} g(u,v)\\\\
>\text{s.t. }v \geq 0. 
>\end{align}
>$$

This method is also applicable to other types of optimization problems that are not in LP form.
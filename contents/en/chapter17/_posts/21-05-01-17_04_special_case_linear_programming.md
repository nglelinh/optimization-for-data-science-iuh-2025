---
layout: post
title: 17-04 Special case, linear programming
chapter: '17'
order: 8
owner: Minjoo Lee
categories:
- chapter17
lang: en
---

Linear programming is where primal-dual interior-point methods truly shine: the objective Hessian $$\nabla^2 f(x)$$ is identically zero, the inequality constraints $$x \ge 0$$ have trivial identity Jacobians, and the entire $$3 \times 3$$ block KKT Newton system collapses via exact block elimination into a single symmetric positive definite (SPD) linear system of size $$m \times m$$—the **normal equations**. Understanding this reduction explains how commercial solvers tackle LPs with millions of variables in seconds using sparse Cholesky factorization.

## Background Knowledge Map: Anatomy of the LP Primal-Dual Newton System

- **Standard-Form LP Primal-Dual Symmetry:** The primal $$\min c^T x \text{ s.t. } Ax = b, x \ge 0$$ and dual $$\max b^T y \text{ s.t. } A^T y + s = c, s \ge 0$$ share the exact complementarity condition $$X S \mathbf{1} = 0$$, where $$X = \operatorname{diag}(x)$$ and $$S = \operatorname{diag}(s)$$.
- **Zero-Hessian Simplification:** Because $$f(x) = c^T x$$ is linear, the top-left block of the KKT matrix is zero, making the linearized dual equation $$A^T \Delta y + \Delta s = -r_d$$ purely algebraic in $$\Delta s$$ and the linearized complementarity equation $$S \Delta x + X \Delta s = -X S \mathbf{1} + \sigma \mu \mathbf{1}$$ diagonal.
- **Normal-Equations Schur Complement:** Eliminating $$\Delta s$$ and $$\Delta x$$ reduces the $$(2n + m)$$-dimensional KKT system to the $$m \times m$$ SPD system $$(A D^2 A^T)\,\Delta y = \text{rhs}$$, where $$D^2 = S^{-1} X = \operatorname{diag}(x_i / s_i) \succ 0$$.
- **Asymmetric Scaling & Mehrotra Predictor-Corrector:** As iterates approach a vertex, $$x_i/s_i \to \infty$$ for basic variables and $$x_i/s_i \to 0$$ for nonbasic variables, making $$A D^2 A^T$$ progressively ill-conditioned—which modern LP solvers handle via stable LDL factorizations and second-order Mehrotra correctors.

### Step-by-Step Worked Example (Read Slowly): Solving the LP Normal Equations Exactly

Consider the LP $$\min 2x_1 + 5x_2$$ subject to $$x_1 + x_2 = 3$$ and $$x_1, x_2 \ge 0$$ (exact optimum $$x^\star = (3, 0), y^\star = 2, s^\star = (0, 3)$$). Start at the strictly feasible primal-dual point $$x = (2, 1)^T$$, $$y = 1$$, $$s = (1, 4)^T$$ (verify: $$x_1 + x_2 = 3$$ and $$A^T y + s = (1,1)^T + (1,4)^T = (2,5)^T = c$$, so $$r_p = 0, r_d = 0$$).

1. **Compute the duality measure $$\mu$$ and target $$\sigma \mu$$:**
   $$\mu = \frac{x^T s}{n} = \frac{2(1) + 1(4)}{2} = 3.$$
   Choose $$\sigma = \frac{1}{3}$$, so $$\sigma \mu = 1$$.
2. **Form the diagonal scaling matrix $$D^2 = S^{-1} X$$:**
   $$D^2 = \operatorname{diag}\!\left(\frac{x_1}{s_1}, \frac{x_2}{s_2}\right) = \operatorname{diag}\!\left(\frac{2}{1}, \frac{1}{4}\right) = \begin{bmatrix} 2 & 0 \\ 0 & 1/4 \end{bmatrix}.$$
3. **Assemble and solve the $$1 \times 1$$ normal equation $$(A D^2 A^T)\,\Delta y = A(x - \sigma \mu S^{-1}\mathbf{1})$$:**
   With $$A = [1, 1]$$:
   $$A D^2 A^T = 2 + \frac{1}{4} = \frac{9}{4}.$$
   Since $$r_p = 0$$ and $$r_d = 0$$, the right-hand side is:
   $$A\left(x - \sigma \mu S^{-1}\mathbf{1}\right) = (2 - 1 \cdot 1) + \left(1 - 1 \cdot \frac{1}{4}\right) = 1 + \frac{3}{4} = \frac{7}{4}.$$
   Wait—let's check the sign! From $$S\Delta x + X\Delta s = \sigma \mu \mathbf{1} - X S \mathbf{1}$$ and $$\Delta s = -A^T \Delta y$$, we get $$\Delta x = S^{-1}(\sigma \mu \mathbf{1} - XS\mathbf{1}) + S^{-1} X A^T \Delta y$$. Multiplying by $$A$$ and using $$A\Delta x = 0$$ gives:
   $$(A D^2 A^T)\,\Delta y = A\left(x - \sigma \mu S^{-1}\mathbf{1}\right) = \frac{7}{4} \implies \Delta y = \frac{7/4}{9/4} = \frac{7}{9}.$$
4. **Recover $$\Delta s$$ and $$\Delta x$$ by back-substitution:**
   $$\Delta s = -A^T \Delta y = \begin{bmatrix} -7/9 \\ -7/9 \end{bmatrix},$$
   $$\Delta x_1 = \frac{1 - 2(1) - 2(-7/9)}{1} = -1 + \frac{14}{9} = +\frac{5}{9}, \qquad \Delta x_2 = \frac{1 - 1(4) - 1(-7/9)}{4} = \frac{-20/9}{4} = -\frac{5}{9}.$$
5. **Verify exact feasibility and gap contraction at $$\theta = 1$$:**
   $$x^+ = \left(\frac{23}{9}, \frac{4}{9}\right)^T > 0, \qquad y^+ = \frac{16}{9}, \qquad s^+ = \left(\frac{2}{9}, \frac{29}{9}\right)^T > 0.$$
   Check: $$x_1^+ + x_2^+ = \frac{27}{9} = 3$$, $$y^+ + s^+ = (2, 5)^T$$, and the duality gap plunged from $$x^T s = 6$$ to $$\frac{46 + 116}{81} = \frac{162}{81} = 2 = 2\sigma\mu$$ in one exact step!

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

### Primal-dual vs. barrier method (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/primal-dual-ipm_en.mp4"></video>
</div>

The barrier method re-centres after each update of $$t$$; the primal-dual method takes a single Newton step on the perturbed KKT conditions in $$(x,\lambda)$$ and cuts the duality gap with far fewer steps.

### Try it yourself: primal-dual vs barrier

<div class="opx-explainer" data-opx="pdipm" data-lang="en"></div>

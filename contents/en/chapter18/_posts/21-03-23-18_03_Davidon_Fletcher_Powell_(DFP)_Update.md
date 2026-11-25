---
layout: post
title: 18-03 Davidon-Fletcher-Powell (DFP) Update
chapter: '18'
order: 4
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

When William Davidon's 1959 Argonne report was later formalized and publicized by Roger Fletcher and Michael Powell in 1963, the **DFP update** became the very first practical quasi-Newton algorithm to guarantee **hereditary positive definiteness**. By upgrading from a rank-1 correction to a carefully crafted **rank-2** symmetric update directly on the inverse Hessian $$H = B^{-1}$$, DFP ensured that every search direction $$p_k = -H_k \nabla f(x^k)$$ is automatically a strict descent direction—as long as $$y_k^T s_k > 0$$.

## Background Knowledge Map: The Mechanics and Geometry of DFP

- **Direct Inverse-Hessian Updating ($$H^+$$):** Updating $$H = B^{-1}$$ via $$H^+ = H - \frac{H y y^T H}{y^T H y} + \frac{s s^T}{y^T s}$$ removes a rank-1 piece along $$Hy$$ and adds a rank-1 piece along $$s$$, delivering the search direction $$p^+ = -H^+ \nabla f$$ in $$O(n^2)$$ time with zero linear solves.
- **Hereditary Positive Definiteness:** If $$H \succ 0$$ and $$y^T s > 0$$, Cauchy–Schwarz gives $$(v^T H v)(y^T H y) \ge (v^T H y)^2$$ for all $$v \neq 0$$, proving $$v^T H^+ v > 0$$ strictly. Descent is mathematically guaranteed at every step.
- **Variational Minimum-Change Interpretation:** DFP is the unique symmetric matrix $$B^+$$ satisfying $$B^+ s = y$$ that minimizes the weighted Frobenius distance $$\|W^{1/2}(B^+ - B)W^{1/2}\|_F$$ for any $$W \succ 0$$ with $$W y = s$$ (for instance, the average inverse Hessian $$\bar{G}^{-1}$$).
- **Why BFGS Eventually Surpassed DFP:** Although DFP is superlinearly convergent on convex problems, it tends to struggle with large eigenvalues of $$H_k$$ (self-correcting slowly when initial curvature is overestimated), motivating its dual twin, BFGS.

### Step-by-Step Worked Example (Read Slowly): One Full DFP Update and Positive-Definiteness Check

Start with $$H_0 = I_2$$ and observe a step $$s = (1, 0)^T$$ with gradient difference $$y = (2, 1)^T$$ (curvature $$y^T s = 2 > 0$$).

1. **Compute the scalar denominators:**
   $$y^T H_0 y = y^T y = 2^2 + 1^2 = 5, \qquad y^T s = 2(1) + 1(0) = 2.$$
2. **Compute the two rank-1 outer products:**
   $$H_0 y (H_0 y)^T = \begin{bmatrix} 2 \\ 1 \end{bmatrix}\begin{bmatrix} 2 & 1 \end{bmatrix} = \begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix}, \qquad s s^T = \begin{bmatrix} 1 \\ 0 \end{bmatrix}\begin{bmatrix} 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}.$$
3. **Assemble $$H_1^{\text{DFP}}$$:**
   $$H_1^{\text{DFP}} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - \frac{1}{5}\begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix} + \frac{1}{2}\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 1 - 0.8 + 0.5 & -0.4 \\ -0.4 & 1 - 0.2 \end{bmatrix} = \begin{bmatrix} 0.7 & -0.4 \\ -0.4 & 0.8 \end{bmatrix}.$$
4. **Verify the inverse secant equation $$H_1^{\text{DFP}} y = s$$:**
   $$\begin{bmatrix} 0.7 & -0.4 \\ -0.4 & 0.8 \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 1.4 - 0.4 \\ -0.8 + 0.8 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} = s \quad \checkmark$$
5. **Verify strict positive definiteness via Sylvester's criterion:**
   Leading minor $$0.7 > 0$$, and determinant $$\det(H_1^{\text{DFP}}) = (0.7)(0.8) - (-0.4)^2 = 0.56 - 0.16 = 0.40 > 0$$. Both eigenvalues are strictly positive ($$\lambda_{1,2} = \frac{1.5 \pm \sqrt{0.65}}{2} \approx 1.153, \; 0.347$$)!

The DFP update is a method that updates $$H (=B^{-1})$$ with a rank-2 symmetric matrix.

>$$H^+ = H + auu^T + bvv^T.$$

If $$H^+$$ computed through the DFP update satisfies the secant equation, then $$s-Hy$$ can be expressed as a linear combination of $$u$$ and $$v$$. (reference: by the secant equation, $$B^+ s =y \Leftrightarrow H^+ y = s$$)

>$$H^+y = Hy + auu^Ty + bvv^Ty = Hy + (au^Ty)u + (bv^Ty)v = s$$
>
>$$\Rightarrow s - Hy = (au^Ty)u + (bv^Ty)v$$

Setting $$u=s, v=Hy$$ and solving for $$a$$ and $$b$$, we derive the updating formula for $$H$$.
>$$
> H^+ = H - \frac{Hyy^TH}{y^THy} + \frac{ss^T}{y^Ts}
>$$

Similar to the SR1 update, we can derive the updating formula for $$B$$ using the [Sherman–Morrison formula](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula).

>$$
>\begin{align}
>B^+ &= B + \frac{(y-Bs)y^T}{y^Ts} + \frac{y(y-Bs)^T}{y^Ts} - \frac{(y-Bs)^Ts}{(y^Ts)^2} yy^T\\\\
> &= \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts} 
>\end{align}
>$$

If $$B$$ is positive definite, then $$\big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big)$$ becomes positive semidefinite. In this case, if $$\frac{yy^T}{y^Ts}$$ is positive definite, then $$B^+ = \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts}$$ is guaranteed to be positive definite. This solves the problem of maintaining positive definiteness that was raised with SR1.

## DFP Update - Alternate Derivation

Recall: if the curvature condition ($$y^Ts > 0, y,s \in \mathbb{R}^n$$) is satisfied, then there exists a symmetric positive definite matrix that satisfies the secant equation.

The DFP update can also be derived by solving the problem of minimizing the weighted Frobenius norm between matrix $$B^+$$ and $$B$$ where $$B^+$$ 1. satisfies symmetry and 2. satisfies the secant equation. (Each different matrix norm corresponds to each different Quasi-Newton method. Among them, the norm that makes it easy to solve this problem while also making it work as a scale-invariant optimization method is the weighted Frobenius norm.)

>Solve
>$$
>\begin{align}
>& \min_{B^+} \: \: && {\|W^{1/2} (B^+ - B) W^{1/2} \|_F} \\\\
>& \text{subject to } && {B^+ = (B^+)^T} \\\\
>    &&& {B^+s = y}  \\\\
>& \text{where } && W \in \mathbb{R}^{n \; \times \;n} \text{ is nonsingular and such that } Wy_k = s_k.
>\end{align}\\\\
>$$

***reference**:

* Frobenius norm: The Frobenius norm of matrix $$A$$ is defined as follows.
$$
\| A \|_{F}  \doteq ( \sum_{i,j} A_{i,j}^2 )^{1/2}
$$

* Weighted Frobenius norm: The weighted Frobenius norm of matrix $$A$$ with weight matrix $$W(W \succ 0)$$ is defined as follows. 
$$
\|A\|_W \doteq \| W^{1/2} A W^{1/2} \|_F
$$
---
layout: post
title: 18-05 The Broyden Class
chapter: '18'
order: 6
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

Looking at SR1, DFP, and BFGS side by side, it is easy to think of them as three separate algebraic inventions discovered by three different groups of mathematicians. In reality, they are all points on a single one-dimensional line! Any affine combination of $$B^+_{\text{BFGS}}$$ and $$B^+_{\text{DFP}}$$ still preserves symmetry and still satisfies the secant equation $$B^+ s = y$$. That one-parameter family—the **Broyden class**—unifies almost all classical quasi-Newton methods and reveals a surprising theorem: with exact line searches on a convex quadratic, *every* member of the Broyden class generates the exact same sequence of iterates!

## Key ideas: Unifying Quasi-Newton Updates

- **Affine Invariance of the Secant Set:** Because $$\{B^+ : B^+ = (B^+)^T, \; B^+ s = y\}$$ is an affine subspace, any combination $$B^+(\phi) = (1 - \phi) B^+_{\text{BFGS}} + \phi B^+_{\text{DFP}}$$ automatically stays symmetric and satisfies $$B^+(\phi) s = y$$.
- **Rank-1 Deviation Structure:** Rewriting the combination as $$B^+(\phi) = B^+_{\text{BFGS}} + \phi (s^T B s)\, v v^T$$ with $$v = \frac{y}{y^T s} - \frac{B s}{s^T B s}$$ shows that every Broyden-class member differs from BFGS by a single positive semidefinite rank-1 term (for $$\phi \ge 0$$).
- **The Restricted Broyden Class ($$\phi \in [0, 1]$$):** Because both $$B^+_{\text{BFGS}}$$ and $$B^+_{\text{DFP}}$$ are positive definite when $$B \succ 0$$ and $$y^T s > 0$$, every convex combination $$\phi \in [0, 1]$$ inherits positive definiteness automatically—and enjoys global convergence on convex functions.
- **SR1 as an Exterior Point:** Setting $$\phi_{\text{SR1}} = \frac{y^T s}{y^T s - s^T B s}$$ recovers SR1 identically. Because $$\phi_{\text{SR1}}$$ can lie outside $$[0, 1]$$ (even becoming negative when $$y^T s < s^T B s$$), we see immediately *why* SR1 can lose positive definiteness while BFGS and DFP cannot.

### Worked example: Generating BFGS, DFP, and SR1 from One Formula

Continue with $$B_0 = I_2$$, $$s = (1, 0)^T$$, $$y = (2, 1)^T$$ (so $$y^T s = 2$$ and $$s^T B_0 s = 1$$).

1. **Compute the Broyden difference vector $$v$$:**
   $$v = \frac{y}{y^T s} - \frac{B_0 s}{s^T B_0 s} = \frac{1}{2}\begin{bmatrix} 2 \\ 1 \end{bmatrix} - \frac{1}{1}\begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0.5 \end{bmatrix}.$$
   Notice $$v^T s = 0$$ automatically—which is why adding any multiple of $$v v^T$$ preserves $$B^+(\phi) s = y$$!
2. **Write the entire Broyden family in closed form:**
   Using $$B_1^{\text{BFGS}} = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 \end{bmatrix}$$ and $$(s^T B_0 s) v v^T = \begin{bmatrix} 0 & 0 \\ 0 & 0.25 \end{bmatrix}$$:
   $$B_1(\phi) = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 + 0.25\phi \end{bmatrix}.$$
3. **Evaluate at the three landmark values of $$\phi$$:**
   - **$$\phi = 0$$ (BFGS):** $$B_1(0) = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 \end{bmatrix}$$.
   - **$$\phi = 1$$ (DFP):** $$B_1(1) = \begin{bmatrix} 2 & 1 \\ 1 & 1.75 \end{bmatrix}$$. (Verify: $$B_1(1)^{-1} = \frac{1}{2.5}\begin{bmatrix} 1.75 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 0.7 & -0.4 \\ -0.4 & 0.8 \end{bmatrix} = H_1^{\text{DFP}}$$!)
   - **$$\phi = \frac{y^T s}{y^T s - s^T B_0 s} = \frac{2}{2 - 1} = 2$$ (SR1):** $$B_1(2) = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$ — matching our SR1 worked example identically!
4. **Bonus check on positive definiteness threshold:**
   $$\det(B_1(\phi)) = 2(1.5 + 0.25\phi) - 1 = 2 + 0.5\phi > 0 \iff \phi > -4$$, illustrating that positive definiteness actually persists slightly into $$\phi < 0$$ up to the critical threshold $$\phi_c$$.

The Broyden class generalizes BFGS, DFP, and SR1 with the following formula.

* **Note:** $$B^+_{\text{BFGS}}$$ and $$B^+_{\text{DFP}}$$ are the $$B^+$$ computed by BFGS and DFP, respectively.

>$$
>B^+ = (1 - \phi)B^+_{\text{BFGS}} + \phi B^+_{\text{DFP}}, \text{ for } \phi \in \mathbb{R}.
>$$

Defining $$v$$ as $$\frac{y}{y^Ts} - \frac{Bs}{s^TBs}$$, the formula above becomes the formula below.

>$$
>B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts} + \phi(s^TBs)vv^T.
>$$

Observe:
* When $$\phi = 0$$, the update above is the same as BFGS.
* When $$\phi = 1$$, the update above is the same as DFP.
* When $$\phi = \frac{y^Ts}{y^Ts - s^TBs}$$, the update above is the same as SR1.

***Reference**: The case where the range of $$\phi$$ is restricted to $$[0, 1]$$ is called the restricted Broyden class [14].

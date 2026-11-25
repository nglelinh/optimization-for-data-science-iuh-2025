---
layout: post
title: 18-02 Symmetric Rank-One Update (SR1)
chapter: '18'
order: 3
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

Suppose you want the absolute simplest symmetric correction to your Hessian approximation $$B$$ that enforces the secant equation $$B^+ s = y$$: adding just a **rank-1** symmetric matrix $$a u u^T$$. Remarkably, imposing symmetry and the secant equation leaves *zero* free parameters—the **Symmetric Rank-One (SR1)** formula is completely unique! Even more remarkably, while SR1 can lose positive definiteness (which once made practitioners nervous), that very freedom lets SR1 capture negative curvature in nonconvex trust-region optimization better than BFGS ever could.

## Key ideas: Uniqueness, Finite Termination, and Trust-Region Power

- **Uniqueness of Rank-1 Secant Updates:** Requiring $$B^+ = B + a u u^T$$ to satisfy $$B^+ s = y$$ forces $$u$$ to be collinear with the secant residual $$y - Bs$$, uniquely determining $$B^+ = B + \frac{(y - Bs)(y - Bs)^T}{(y - Bs)^T s}$$.
- **Self-Duality Under Sherman–Morrison:** Applying the Sherman–Morrison formula to $$B^+$$ yields the exact same rank-1 template for the inverse Hessian $$H^+ = H + \frac{(s - Hy)(s - Hy)^T}{(s - Hy)^T y}$$, just swapping $$(B, s, y) \leftrightarrow (H, y, s)$$.
- **Exact Hessian Recovery on Quadratics:** For any $$n$$-dimensional quadratic with linearly independent steps (even without exact line searches!), SR1 recovers the *exact* Hessian $$B_n = Q$$ in at most $$n$$ steps—a stronger approximation property than BFGS.
- **Denominator Breakdown & Safeguard:** Because $$(y - Bs)^T s$$ can vanish or change sign even when $$y^T s > 0$$, SR1 does not preserve positive definiteness and skips updates whenever $$|(y - Bs)^T s| < r \|s\| \|y - Bs\|$$ (typically $$r = 10^{-8}$$), making it a natural partner for trust-region methods rather than line search.

### Worked example: Exact Hessian Recovery in $$n = 2$$ SR1 Steps

Let $$f(x) = \frac{1}{2} x^T Q x$$ with $$Q = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}$$, and start with $$B_0 = I_2$$. Take two arbitrary linearly independent steps $$s_0 = (1, 0)^T$$ and $$s_1 = (0, 1)^T$$.

1. **Step 1 ($$s_0 = (1, 0)^T$$):**
   The true gradient change is $$y_0 = Q s_0 = (2, 1)^T$$. Compute the secant residual:
   $$r_0 = y_0 - B_0 s_0 = \begin{bmatrix} 2 \\ 1 \end{bmatrix} - \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}.$$
   Denominator: $$r_0^T s_0 = (1)(1) + (1)(0) = 1 \neq 0$$. Update $$B_1$$:
   $$B_1 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} + \frac{1}{1}\begin{bmatrix} 1 \\ 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}.$$
   Verify: $$B_1 s_0 = (2, 1)^T = y_0$$.
2. **Step 2 ($$s_1 = (0, 1)^T$$):**
   The true gradient change is $$y_1 = Q s_1 = (1, 3)^T$$. Compute the new secant residual:
   $$r_1 = y_1 - B_1 s_1 = \begin{bmatrix} 1 \\ 3 \end{bmatrix} - \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}.$$
   Denominator: $$r_1^T s_1 = (0)(0) + (1)(1) = 1 \neq 0$$. Update $$B_2$$:
   $$B_2 = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} + \frac{1}{1}\begin{bmatrix} 0 \\ 1 \end{bmatrix}\begin{bmatrix} 0 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} = Q!$$
3. **Key insight:**
   In exactly $$n = 2$$ rank-1 updates—without needing exact line searches or conjugate directions—SR1 reconstructed the entire $$2 \times 2$$ Hessian $$Q$$ identically!

The SR1 update is a method that updates $$B$$ with a rank-1 symmetric matrix so that $$B^+$$ maintains symmetry and continues to satisfy the secant equation. If a rank-1 symmetric matrix is decomposed as a product of $$a \in \left\{-1, 1\right\}$$ and $$u \in \mathbb{R^n}$$, the update form would be as follows.

>$$B^+ = B + auu^T.$$

## Key Observation
$$a$$ and $$u$$ must be chosen so that $$B^+$$ satisfies the secant equation. Thus, let's substitute the update form introduced above into the secant equation $$y = B^+s$$.

>$$y = B^+s \Rightarrow y = Bs + (au^Ts)u. \quad \text{--- (1)}$$

Since $$(au^Ts)$$ is a scalar, $$u$$ can also be expressed as a product of $$y-Bs$$ and an arbitrary scalar $$\delta$$ $$\big( u = \delta(y - Bs) \big)$$. Let's substitute $$u$$ in (1) with $$\delta(y - Bs)$$.

>$$y-Bs = a\delta^2 \big[ s^T(y - Bs) \big] (y -Bs),$$

The parameters $$\delta$$ and $$a$$ that satisfy the above equation are as follows.

>$$a = \text{sign} \big[ s^T (y - Bs) \big], \quad \delta = \pm | s^T(y-Bs) |^{-1/2}. \quad \text{--- (2)}$$

## The Only SR1 Updating Formula
Using the information obtained from the key observation, we can derive the unique form of SR1 update ([14] section 6.2). <br/>
$$\big( u = \delta (y - Bs)$$ and substituting (2) into $$B^+ = B + auu^T$$. $$\big)$$

>$$
>B^+ = B + \frac{(y-Bs)(y-Bs)^T}{(y-Bs)^Ts}.
>$$
>

## The Update Formula for the Inverse Hessian Approximation

To find $$x^+$$, we need to compute $$B^{-1}$$.

>$$x^+ = x + tp = x - tB^{-1}\nabla f(x)$$

If we can update $$B^{-1}$$ instead of $$B$$, wouldn't we be able to reduce the cost of computing $$B^{-1}$$ every time?

Using the [Sherman–Morrison formula](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula), we can see through the derivation process that $$B^{-1}$$ can also be updated in the same form. ($$H = B^{-1}$$)

>$$
>H^+ = H + \frac{(s-Hy)(s-Hy)^T}{(s-Hy)^Ty}.
>$$

## Shortcomings of SR1

SR1 has the advantage of being very simple, but it has two critical shortcomings.

1. The update can fail when $$(y-Bs)^Ts$$ approaches 0.
2. It cannot maintain the positive definiteness of $$B$$ and $$H$$.

The following sections introduce methods that complement the shortcomings of SR1. 
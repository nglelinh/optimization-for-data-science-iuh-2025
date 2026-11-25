---
layout: post
title: 13-04-02 Conjugates and dual problems
chapter: '13'
order: 7
owner: Wontak Ryu
categories:
- chapter13
lang: en
---

Many optimization problems in machine learning have the additive form $$\min_x f(x) + g(x)$$: a data-fitting loss $$f$$ plus a regularizer or constraint indicator $$g$$. If you try to derive the Lagrange dual by hand from scratch every time, you repeat the same algebraic steps over and over. Conjugates turn that entire derivation into a one-line lookup table: split $$x = z$$, and the dual instantly writes itself as $$\max_u -f^*(u) - g^*(-u)$$.

## Key ideas: Composite Duality via Conjugates

- **Pillar 1 — Consensus Splitting ($$x = z$$):** Replacing $$\min_x f(x) + g(x)$$ with $$\min_{x=z} f(x) + g(z)$$ separates the two terms in the Lagrangian $$f(x) - u^T x + g(z) + u^T z$$.
- **Pillar 2 — Fenchel–Rockafellar Pattern:** Minimizing independently over $$x$$ and $$z$$ directly yields $$g_{\text{dual}}(u) = -f^*(u) - g^*(-u)$$, turning primal sums into dual sums of negative conjugates.
- **Pillar 3 — Constraints Become Support Functions:** When $$g(x) = I_C(x)$$ enforces $$x \in C$$, its conjugate $$I_C^*(-u)$$ is the support function of $$C$$ evaluated at $$-u$$.
- **Pillar 4 — Norm Penalties Become Dual-Norm Balls:** When $$g(x) = \|x\|$$, its conjugate $$g^*(-u)$$ is the indicator of $$\{\|u\|_* \le 1\}$$, converting a nonsmooth primal objective into a smooth dual objective over a simple norm ball.

### Worked example: Dualizing a Quadratic + $$\ell_1$$ Problem in Two Lines

Consider $$\min_{x \in \mathbb{R}^2} \underbrace{\frac{1}{2}\|x - b\|_2^2}_{f(x)} + \underbrace{\|x\|_1}_{g(x)}$$ with $$b = (2.5, -0.4)^T$$.

1. **Look up the two conjugates:**
   - For $$f(x) = \frac{1}{2}\|x - b\|_2^2$$: $$\max_x (u^T x - \frac{1}{2}\|x-b\|_2^2)$$ is attained at $$x = b + u$$, giving $$f^*(u) = \frac{1}{2}\|u\|_2^2 + b^T u$$.
   - For $$g(x) = \|x\|_1$$: $$g^*(-u) = I_{\{\|-u\|_\infty \le 1\}}(u) = I_{\{\|u\|_\infty \le 1\}}(u)$$.
2. **Write the dual problem $$\max_u -f^*(u) - g^*(-u)$$:**
   $$\max_{\|u\|_\infty \le 1} -\frac{1}{2}\|u\|_2^2 - b^T u \iff \min_{\|u\|_\infty \le 1} \frac{1}{2}\|u + b\|_2^2.$$
3. **Solve the dual by clipping $$-b$$ to $$[-1, 1]^2$$:**
   - $$-b = (-2.5, 0.4)^T \implies u^\star = (-1, 0.4)^T$$.
4. **Recover $$x^\star$$ from $$x^\star = b + u^\star$$:**
   $$x^\star = (2.5 - 1,\ -0.4 + 0.4)^T = (1.5,\ 0)^T.$$
   Notice that this matches coordinate-wise soft-thresholding $$S_1(b)$$!
5. **Check strong duality:**
   - Primal value: $$\frac{1}{2}((1.5-2.5)^2 + (0 - (-0.4))^2) + (1.5 + 0) = \frac{1}{2}(1 + 0.16) + 1.5 = 2.08$$.
   - Dual value: $$-\frac{1}{2}(1^2 + 0.4^2) - (2.5(-1) + (-0.4)(0.4)) = -0.58 + 2.5 + 0.16 = 2.08$$.

Conjugates can often be represented through the derivation of dual problems for Lagrangian minimization problems as follows:

> $$−f^{∗}(u) = \min_x f(x)−u^Tx$$

For example, consider the following expression:

> $$ \min_x  f(x) + g(x)$$

The following expression has constraints added to the above expression and is equivalent to it:

> $$ \min_{x,z} f(x) + g(z) \text{ subject to } x = z $$

Converting this to a Lagrange dual function gives:

> $$g(u) = \min_{x,z} f(x) + g(z) + u^T(z−x) = −f^{∗}(u)−g^{∗}(−u)$$

Therefore, the dual problem of the original expression can be defined as follows:
> $$ \max_u −f^{∗}(u)−g^{∗}(−u)$$

#### [Examples]
• Indicator function: The dual of $$ \min_x f(x) + I_C(x)$$ is as follows:
> $$ \max_u −f^{∗}(u)−I^{∗}_C(−u)$$
> 
> where $$I^{∗}_C$$ is the support function of $$C$$

• Norms: 

The dual of $$ \min_x f(x) + \rVert x \rVert $$ is as follows:
$$ \max_u −f^{∗}(u) \text{ subject to } \rVert u \rVert^{∗} ≤ 1 \text{ where } \rVert · \rVert_{∗} \text{ is the dual norm of } \rVert · \rVert$$

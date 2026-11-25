---
layout: post
title: 03-06 Convexity with respect to generalized inequalities
chapter: '03'
order: 14
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

When optimizing over symmetric matrices (as in covariance estimation, control theory, or quantum information), the objective or constraint map $$F(X)$$ itself outputs a *matrix* rather than a scalar. How do we define whether $$F(X) = X^2$$ is "convex" when comparing matrices? By replacing $$\le$$ in Jensen's inequality with the cone inequality $$\preceq_K$$—and the dual characterization shows that $$K$$-convexity holds if and only if every nonnegative scalar projection $$\lambda^T F(x)$$ ($$\lambda \succeq_{K^*} 0$$) is an ordinary scalar convex function.

## Key ideas: Extending Convexity to Vector & Matrix Maps

- **$$K$$-Monotonicity:** $$f: \mathbb{R}^n \to \mathbb{R}$$ is $$K$$-nondecreasing if $$x \preceq_K y \implies f(x) \le f(y)$$; for differentiable $$f$$, this holds iff $$\nabla f(x) \succeq_{K^*} 0$$ everywhere.
- **$$K$$-Convexity:** A map $$f: \mathbb{R}^n \to \mathbb{R}^m$$ is $$K$$-convex (for proper cone $$K \subseteq \mathbb{R}^m$$) iff $$f(\theta x + (1-\theta)y) \preceq_K \theta f(x) + (1-\theta)f(y)$$.
- **Dual Scalarization Test:** $$f$$ is $$K$$-convex iff for *every* $$\lambda \succeq_{K^*} 0$$, the scalar function $$\lambda^T f(x)$$ is convex—turning matrix-convexity proofs into routine scalar convexity checks!
- **Matrix Convexity ($$\mathbb{S}_+^n$$-Convexity):** Lets us prove $$F(X) = X^2$$ and $$F(X) = X^{-1}$$ (on $$\mathbb{S}_{++}^n$$) are matrix-convex, unlocking Schur-complement LMI reformulations.

### Worked example: Proving $$F(X) = X^2$$ Is Matrix-Convex on $$\mathbb{S}^2$$

Verify that $$F(X) = X^2$$ is $$\mathbb{S}_+^2$$-convex on symmetric $$2 \times 2$$ matrices.

1. **Apply the dual characterization:** For any vector $$v \in \mathbb{R}^2$$, the rank-1 matrix $$W = vv^T \in \mathbb{S}_+^2$$ defines a nonnegative dual functional:
   $$\text{tr}(W F(X)) = v^T X^2 v = (Xv)^T (Xv) = \|Xv\|_2^2.$$
   Because $$X \mapsto Xv$$ is linear in $$X$$ and $$\|\cdot\|_2^2$$ is convex, $$X \mapsto \|Xv\|_2^2$$ is convex for every $$v \in \mathbb{R}^2$$ (and hence for every $$W \succeq 0$$, a nonnegative sum of rank-1 terms). Thus $$F(X) = X^2$$ is **matrix-convex**!
2. **Concrete numerical check:** Take $$X = \text{diag}(1, 0)$$, $$Y = \text{diag}(0, 1)$$, and $$\theta = 0.5$$:
   - $$F(0.5X + 0.5Y) = \text{diag}(0.5, 0.5)^2 = \text{diag}(0.25, 0.25)$$.
   - $$0.5 F(X) + 0.5 F(Y) = 0.5\,\text{diag}(1, 0) + 0.5\,\text{diag}(0, 1) = \text{diag}(0.5, 0.5)$$.
   - Difference: $$\text{diag}(0.5, 0.5) - \text{diag}(0.25, 0.25) = \text{diag}(0.25, 0.25) \succeq 0 \quad \checkmark$$.

This section discusses convexity with respect to generalized inequalities, extending the concept of convexity beyond standard real-valued functions.

In spaces other than $$\mathbb{R}$$, we use the definition of cones for generalized inequality expressions that extend the ordering concept commonly used in $$\mathbb{R}$$ space (see [02-01-04]({% multilang_post_url contents/chapter02/21-02-08-02_01_04_Convex_cone %})). In this section, we examine the concepts of monotonicity and convexity that extend beyond $$\mathbb{R}$$ space using the concept of cones.

## Monotonicity with respect to a generalized inequality

Suppose $$K \subseteq \mathbb{R}^n$$ is a proper cone represented by $$\preceq_K$$. A convex cone $$K \subseteq \mathbb{R}^n$$ is a **proper cone** if it satisfies the following conditions:

• $$K$$ is closed (contains its boundary)
• $$K$$ is solid (has nonempty interior)
• $$K$$ is pointed (contains no line)

We define **$$K$$-nondecreasing** as follows:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ is $$K$$-nondecreasing if $$x \preceq_K y \Rightarrow f(x) \leq f(y)$$

Also, when the following condition is satisfied, we say it is **$$K$$-increasing**:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ is $$K$$-increasing if $$x \preceq_K y, x \neq y \Rightarrow f(x) < f(y)$$


### Gradient conditions for monotonicity

For a differentiable function $$f : \mathbb{R} \mapsto \mathbb{R}$$ to be nondecreasing on a convex (i.e., interval) domain means that $$f'(x) \geq 0$$ for all $$x \in \text{dom}f$$, and if $$f'(x) > 0$$ for all $$x \in \text{dom}f$$, then it is increasing. Similarly, monotonicity can be expressed as an extended concept in generalized inequalities.

When the domain is convex, a differentiable function $$f$$ being $$K$$-nondecreasing means satisfying the following equation. Note that unlike simple scalars, the gradient $$\nabla f(x)$$ must be nonnegative in the dual inequality.
> A differentiable function $$f$$ is $$K$$-nondecreasing $$\Longleftrightarrow$$ $$\nabla f(x) \succeq_{K^*} 0$$ for all $$x \in \text{dom}f$$

If the following condition is satisfied, $$f$$ is called **$$K$$-increasing**. As with scalars, the converse does not hold.
> $$\nabla f(x) \succ_{K^*} 0$$ for all $$x \in \text{dom}f$$ $$\Rightarrow$$ $$f$$ is $$K$$-increasing.


### Convexity with respect to generalized inequality

Let $$K \subseteq \mathbb{R}^m$$ be a proper cone associated with the generalized inequality $$\preceq_K$$.
Then, if $$f : \mathbb{R}^n \mapsto \mathbb{R}^m$$ is called **$$K$$-convex** for all $$x, y$$ and $$0 \leq \theta \leq 1$$, the following inequality holds:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}^m$$ is $$K$$-convex $$\Rightarrow$$ $$f(\theta x + (1 - \theta) y) \preceq_K \theta f(x) + (1 - \theta) f(y)$$ with $$0 < \theta < 1$$ for all $$x, y$$.

Also, the condition for **strictly $$K$$-convex** is as follows:
> $$f(\theta x + (1 - \theta) y) \prec_K \theta f(x) + (1 - \theta) f(y)$$ for all $$x \neq y$$ and $$0 < \theta < 1$$.

When $$m = 1$$ and $$K = \mathbb{R}_+$$, this becomes the inequality that satisfies the general convexity we have discussed earlier.

### Dual characterization of $$K$$-convexity

$$f$$ being $$K$$-convex means that the (real-valued) function $$w^T f$$ is convex for all $$w \succeq_{K^*} 0$$. $$f$$ being strictly $$K$$-convex means that the (real-valued) function $$w^T f$$ is strictly convex for all $$w \succeq_{K^*} 0$$. This follows from the definition and properties of dual inequalities.

<br>
### Differentiable $$K$$-convex functions

If a differentiable function $$f$$ is $$K$$-convex and the function domain is convex, then the following equation holds:
> $$f(y) \succeq_K f(x) + Df(x)(y - x)$$ for all $$x, y \in \text{dom}f$$

Here, $$Df(x) \in \mathbb{R}^{m \times n}$$ is the derivative or Jacobian matrix of $$f$$ at point $$x$$.

If $$f$$ is strictly $$K$$-convex and the function domain is convex, then the following equation holds:
> $$f(y) \succ_K f(x) + Df(x)(y - x)$$ for all $$x, y \in \text{dom}f$$, $$x \neq y$$


### Composition theorem

Many results from composition can be generalized to $$K$$-convexity.
For example, if $$g : \mathbb{R}^n \mapsto \mathbb{R}^p$$ is $$K$$-convex, $$h : \mathbb{R}^p \rightarrow \mathbb{R}$$ is convex, and the extended-value extension $$\widetilde{h}$$ of $$h$$ is $$K$$-nondecreasing, then $$h \circ g$$ is convex. This generalizes the fact that the composition of a convex function with a nondecreasing convex function is convex.
(The condition that $$\widetilde{h}$$ is $$K$$-nondecreasing means that $$\text{dom}h - K = \text{dom}h$$.)

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

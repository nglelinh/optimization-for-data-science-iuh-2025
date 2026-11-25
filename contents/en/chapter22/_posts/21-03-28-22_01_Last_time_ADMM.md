---
layout: post
title: '22-01 Last time: ADMM'
chapter: '22'
order: 2
owner: YoungJae Choung
categories:
- chapter22
lang: en
---

Before stepping into projection-free optimization, it pays to pause and look back at the bridge we just crossed: the Alternating Direction Method of Multipliers (ADMM). In large-scale statistical learning, we routinely face composite objectives $$f(x) + g(z)$$ coupled by linear constraints $$Ax + Bz = c$$ where neither proximal operator alone can handle the coupled system. ADMM splits the problem cleanly into separate $$x$$- and $$z$$-subproblems linked by a dual price vector—setting the exact contrast against Frank–Wolfe, which avoids proximal/projection steps altogether in favor of linear oracles.

## Key ideas: Foundations of ADMM and Scaled Dual Form

- **Augmented Lagrangian Regularization:** Adding the quadratic penalty $$\frac{\rho}{2}\|Ax + Bz - c\|_2^2$$ to the ordinary Lagrangian improves conditioning and ensures dual differentiability even when $$f$$ or $$g$$ is not strictly convex, without altering the primal optimal value on the feasible set $$Ax + Bz = c$$.
- **Gauss–Seidel Alternating Minimization:** Rather than minimizing $$L_\rho(x, z, u)$$ jointly over $$(x, z)$$ (which destroys separability), ADMM updates $$x$$ first with $$z$$ fixed, then updates $$z$$ using the freshest $$x^{(k)}$$, exploiting block structure while preserving convergence under mild convexity assumptions.
- **Dual Ascent as Price Adjustment:** The update $$u^{(k)} = u^{(k-1)} + \rho(Ax^{(k)} + Bz^{(k)} - c)$$ uses the primal residual as a gradient ascent step on the dual problem, with step size $$\rho$$ matching the augmentation parameter so that dual feasibility holds automatically at each $$z$$-update.
- **Scaled Form Economy:** Defining the scaled dual variable $$w = u / \rho$$ absorbs the linear term $$u^\top(Ax + Bz - c)$$ into a single completed square $$\frac{\rho}{2}\|Ax + Bz - c + w\|_2^2$$, turning both primal updates into standard proximal operators and simplifying implementation.

### Worked example: One Scaled ADMM Iteration on a Splitting Problem

Consider the 1D consensus-regularized problem $$\min_{x, z \in \mathbb{R}} \frac{1}{2}(x - 4)^2 + |z|$$ subject to $$x - z = 0$$ (so $$A = 1$$, $$B = -1$$, $$c = 0$$). Choose $$\rho = 1$$ and initialize $$z^{(0)} = 0$$, $$w^{(0)} = 0$$.

1. **Exact optimum for reference:** Since $$x = z$$, minimizing $$\frac{1}{2}(x - 4)^2 + |x|$$ gives $$x^\star = z^\star = \operatorname{soft}(4, 1) = 3$$.
2. **Scaled $$x$$-update (quadratic minimization):**
   $$x^{(1)} = \arg\min_x \left\{\frac{1}{2}(x - 4)^2 + \frac{1}{2}(x - z^{(0)} + w^{(0)})^2\right\} = \arg\min_x \left\{\frac{1}{2}(x - 4)^2 + \frac{1}{2}x^2\right\}.$$
   Setting the derivative $$(x - 4) + x = 0$$ yields $$x^{(1)} = 2$$.
3. **Scaled $$z$$-update (proximal soft-thresholding):**
   $$z^{(1)} = \arg\min_z \left\{|z| + \frac{1}{2}(x^{(1)} - z + w^{(0)})^2\right\} = \operatorname{soft}(x^{(1)} + w^{(0)},\ 1/\rho) = \operatorname{soft}(2, 1) = 1.$$
4. **Scaled dual update (running sum of residuals):**
   $$w^{(1)} = w^{(0)} + (x^{(1)} - z^{(1)}) = 0 + (2 - 1) = 1.$$
5. **Check the second iteration to see convergence in action:**
   - $$x^{(2)} = \frac{4 + (z^{(1)} - w^{(1)})}{2} = \frac{4 + (1 - 1)}{2} = 2$$,
   - $$z^{(2)} = \operatorname{soft}(x^{(2)} + w^{(1)}, 1) = \operatorname{soft}(2 + 1, 1) = 2$$,
   - $$w^{(2)} = w^{(1)} + (x^{(2)} - z^{(2)}) = 1 + 0 = 1$$.
   Notice how the primal residual $$r^{(2)} = x^{(2)} - z^{(2)} = 0$$ vanishes while $$w$$ steadily accumulates the dual subgradient needed to push both variables toward $$3$$.

## Last time: ADMM
Let's consider the following optimization problem
> $$\begin{align}
> &\min_{x,z} &&f(x) + g(z)\\\\
> &\text{ subject to } &&Ax + Bz = c 
> \end{align}$$

Converting this to Augmented Lagrangian form gives us the following. (for some $$ρ > 0$$)
> $$ L_ρ(x, z, u) = f(x) + g(z) + u^T(Ax + Bz − c) + \frac{ρ}{2} \| Ax + Bz − c \|^2_2$$

The above equation becomes Strongly Convex with the addition of $$\frac{ρ}{2} \| Ax + Bz − c \|^2_2$$, and this can be transformed into a form useful for parallel processing as shown in the following equation.
* For detailed proof, please refer to the content of the previous chapter.
ADMM: for $$k = 1, 2, 3, . . .$$
> $$x^{(k)} = argmin_{x} L_ρ(x, z^{(k−1)}, u^{(k−1)})$$
> $$z^{(k)} = argmin_{z} L_ρ(x^{(k)}  , z, u^{(k−1)})$$
> $$u^{(k)} = u^{(k−1)} + ρ(Ax^{(k)} + Bz^{(k)} − c)$$
 
## ADMM in scaled form
Let's change the dual variable $$u$$ to the scaled variable $$w = u/ρ$$. Here, the ADMM step can be computed as follows.

> $$x^{(k)} = argmin_{x} f(x) + \frac{ρ}{2} \| Ax + Bz^{(k−1)} − c + w^{(k−1)} \|^2_2$$
> $$z^{(k)} = argmin_{z} g(z) + \frac{ρ}{2} \| Ax^{(k)} + Bz − c + w^{(k−1)} \|^2_2$$ 
> $$w^{(k)} = w^{(k−1)} + Ax^{(k)} + Bz^{(k)} − c$$

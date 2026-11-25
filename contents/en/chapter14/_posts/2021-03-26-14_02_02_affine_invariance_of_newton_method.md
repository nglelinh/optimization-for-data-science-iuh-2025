---
layout: post
title: 14-02-02 Affine invariance of Newton's method
chapter: '14'
order: 7
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

Imagine measuring house sizes in square meters versus square millimeters in a regression model. If you run gradient descent, switching units stretches one axis by a factor of $$10^6$$ and completely ruins your step size and convergence speed. Run Newton's method, and the trajectory doesn't budge by a single millimeter—because Newton's method is **affine invariant**.

## Key ideas: Why Coordinate Changes Cannot Fool Newton

- **Pillar 1 — Chain Rule for Gradient & Hessian:** Under $$x = Ay$$ ($$A$$ nonsingular) and $$g(y) = f(Ay)$$, the derivatives transform covariantly as $$\nabla g(y) = A^T \nabla f(x)$$ and $$\nabla^2 g(y) = A^T \nabla^2 f(x) A$$.
- **Pillar 2 — Exact Cancellation of $$A^T$$:** Inverting the transformed Hessian gives $$(A^T \nabla^2 f(x) A)^{-1} = A^{-1} (\nabla^2 f(x))^{-1} (A^T)^{-1}$$. Multiplying by $$A^T \nabla f(x)$$ cancels $$(A^T)^{-1} A^T = I$$ cleanly!
- **Pillar 3 — Trajectory Identity ($$x^+ = A y^+$$):** Multiplying $$y^+ = y - A^{-1}(\nabla^2 f(x))^{-1}\nabla f(x)$$ on the left by $$A$$ recovers $$x^+ = x - (\nabla^2 f(x))^{-1}\nabla f(x)$$ identically.
- **Pillar 4 — Contrast with Gradient Descent:** In $$x$$-coordinates, gradient descent on $$g(y)$$ maps to $$x^+ = x - t A A^T \nabla f(x)$$. Unless $$A$$ is orthogonal ($$A A^T = I$$), changing coordinates warps the descent direction!

### Worked example: Comparing Newton and GD Under a Non-Orthogonal Change of Basis

Let $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2)$$ (perfectly circular) and apply the shear/scaling transformation $$A = \begin{bmatrix} 2 & 0 \\ 0 & 1/2 \end{bmatrix}$$, so $$x = Ay = (2y_1, \frac{1}{2}y_2)^T$$ and $$g(y) = f(Ay) = 2y_1^2 + \frac{1}{8}y_2^2$$. Start at $$x^{(0)} = (2, 2)^T$$, which corresponds to $$y^{(0)} = A^{-1}x^{(0)} = (1, 4)^T$$.

1. **Gradient Descent ($$t = 0.2$$) in $$x$$-space vs. $$y$$-space:**
   - In $$x$$-space: $$\nabla f(2,2) = (2,2)^T \implies x^{(1)} = (2,2)^T - 0.2(2,2)^T = (1.6, 1.6)^T$$ (straight toward the origin).
   - In $$y$$-space: $$\nabla g(1,4) = (4y_1, \frac{1}{4}y_2)^T = (4, 1)^T \implies y^{(1)} = (1,4)^T - 0.2(4,1)^T = (0.2, 3.8)^T$.
   - Map $$y^{(1)}$$ back to $$x$$-space: $$A y^{(1)} = (0.4, 1.9)^T \ne (1.6, 1.6)^T$$! The direction is completely distorted.
2. **Newton's Method in $$x$$-space vs. $$y$$-space:**
   - In $$x$$-space: $$x^{(1)} = (2,2)^T - I^{-1}(2,2)^T = (0, 0)^T$$.
   - In $$y$$-space: $$\nabla^2 g(y) = \operatorname{diag}(4, 1/4)$$, so $$y^{(1)} = (1,4)^T - \operatorname{diag}(1/4, 4)(4, 1)^T = (1,4)^T - (1,4)^T = (0,0)^T$$.
   - Map back: $$A y^{(1)} = (0,0)^T = x^{(1)}$$! Exact invariance verified.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

One of the important properties of Newton's method is that it is affine invariant. This means that the direction of the update is independent of affine transformations of the coordinate system. For example, gradient descent is variant to affine transformations, so the convergence speed differs depending on the coordinate space.

This page derives the affine invariance property.

## Affine invariance : proof
Let $$f:\mathbb{R}^{n}\rightarrow \mathbb{R}$$ be twice differentiable, and let $$A\in \mathbb{R}^{n\times n}$$ be nonsingular. Also, define $$g(y)$$ as $$f(Ay)$$. $$g(y):=f(Ay)$$. This means that some function $$g$$ that takes $$y$$ as input has the same output as function $$f$$ that takes $$Ay$$ (affine transformed by $$A$$ with respect to $$y$$) as input. To reduce confusion about notation and gradient arguments, we define $$x:=Ay$$.

Using the chain rule to differentiate both sides once and twice, we get the following results:

>$$
>\begin{align}
>\nabla g(y) &= A^{T} \nabla f(x)\\\\
>\nabla^{2} g(y) &= A^{T}\nabla^{2}f(x)A,
>\end{align}
>$$

The Newton step of $$g$$ with respect to $$y$$ is as follows:

>$$
>\begin{align}
>y^{+}  = y-(\nabla^{2}g(y))^{-1}\nabla g(y).
>\end{align}
>$$

Here, instead of function $$g$$, if we transform and organize it in terms of function $$f$$ with respect to $$x$$, we can derive the Newton step for $$x$$ and $$f$$.

>$$
>\begin{align}
>y^{+} &= y-(A^{T}\nabla^{2}f(x)A)^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow y^{+} &= y-A^{-1}(\nabla^{2}f(x))^{-1}(A^{T})^{-1}A^{T} \nabla f(x)\\\\
>\Leftrightarrow Ay^{+} &= Ay-(\nabla^{2}f(x))^{-1}\nabla f(x)\\\\
>\Leftrightarrow x^{+} &= x - \nabla^{2}f(x)^{-1}\nabla f(x).
>\end{align}
>$$

This means that the Newton step is affine invariant, i.e., the updates in coordinate systems transformed by affine transformations represented by non-singular matrices are identical to each other.

Using the same method to check the affine invariance of gradient descent by deriving the step update, we can obtain the following result:

>$$
>\begin{align}
>y^{+} &= y-t_{k}\cdot \nabla g(y)\\\\
>\Leftrightarrow y^{+} &= y-t_{k}\cdot \nabla f(x)A^{T}\\\\
>\Leftrightarrow x^{+} &= x - t_{k}\cdot A\nabla f(x)A^{T}. 
>\end{align}
>$$

In the case of gradient descent, since the Hessian matrix is approximated as $$\frac{1}{t}I$$ for updates, we can see that the direction of the update changes for affine transformed coordinates.
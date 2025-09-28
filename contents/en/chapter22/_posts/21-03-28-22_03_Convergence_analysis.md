---
layout: post
title: 22-03 Convergence analysis
chapter: '22'
order: '4'
owner: YoungJae Choung
categories:
- chapter22
lang: en
---

## Convergence analysis

To find out the convergence characteristics of the Frank-Wolfe method, it is necessary to define the curvature constant of $$f$$ for $$C$$ as follows [Jaggi (2011)]:

>$$M = \max_{x,s,y\in C, y = (1−\gamma)x+\gamma s} \frac{2}{\gamma^2} \Bigl( f(y) − f(x) − \nabla f(x)^T(y − x) \Bigr)$$

where $$\gamma \in [0, 1]$$. Through $$M$$, we can actually measure how far the function tends to be from linear approximation. Here $$M = 0$$ indicates that $$f$$ is linear. $$f(y) - f(x) - \nabla f(x)^T(y - x)$$ is called the Bregman divergence defined by $$f$$.

>**Theorem**: The conditional gradient method using fixed step size $$\gamma_k = 2/(k + 1), k = 1,2,3, ...$$ satisfies the following:
>
>$$f(x^{(k)}) − f^{*} \leq \frac{2M}{k + 2}$$

The number of iterations required to satisfy $$f(x^{(k)}) − f^{*} \leq \epsilon$$ is $$O(1/\epsilon)$$. We want to prove this theory by induction. However, before moving on to the direct proof, we want to introduce one concept that needs to be addressed.

## Basic inequality

The **key inequality** used to prove Frank-Wolfe convergence speed is as follows:

>$$f(x^{(k)}) \leq f(x^{(k−1)}) − \gamma_k g(x^{(k−1)}) + \frac{\gamma^2_k}{2}M$$

where $$g(x) = \max_{s\in C} \nabla f(x)^T(x − s)$$ means the duality gap discussed earlier, and by induction, the ratio follows this inequality.

### [Proof]

To prove the basic inequality, we specify $$x^+ = x^{(k)}, x = x^{(k−1)}, s = s^{(k−1)}, \gamma = \gamma_k$$. Then we organize as follows:

>$$\begin{align}
>f(x^+) &= f\bigl( x + \gamma(s − x) \bigr) \\
>&\leq f(x) + \gamma\nabla f(x)^T(s − x) + \frac{\gamma^2}{2}M \\
>&= f(x) − \gamma g(x) + \frac{\gamma^2}{2}M
>\end{align}$$

In the above equation, the second line used the definition of $$M$$, and the third line used the definition of $$g$$.

Now, using the basic inequality, we use induction to prove our convergence rate theorem. For the case $$k=1$$, we can easily verify that the theorem is satisfied. For any case $$k > 1$$, we assume that $$f(x^{(k−1)}) − f^{*} \leq 2M/(k + 1)$$ is satisfied.

Let's recall the duality gap $$g(x)$$ mentioned earlier:

>$$g(x^{(k−1)}) \leq f(x^{(k−1)}) − f^{*}$$

Let's apply $$\gamma_k = 2/(k + 1)$$ and the basic inequality:

>$$f(x^{(k)}) \leq f(x^{(k−1)}) − 2(f(x^{(k−1)}) − f^{*})/(k + 1) + 4M/2(k + 1)^2$$
>
>$$f(x^{(k)}) − f^{*} \leq (1 − 2/(k + 1))(f(x^{(k−1)}) − f^{*}) + 2M/(k + 1)^2$$
>
>$$f(x^{(k)}) − f^{*} \leq (k − 1)/(k + 1) \times 2M/(k + 1) + 2M/(k + 1)^2 \leq 2M/(k + 2)$$

The proven convergence speed matches the speed known for projected gradient descent when $$\nabla f$$ is Lipschitz. Let's compare the assumptions. In fact, if $$\nabla f$$ is Lipschitz with constant $$L$$, then when $$\text{diam}^2(C) = \max_{x,s\in C} \|x − s\|^2$$, we have $$M \leq \text{diam}^2(C) \cdot L$$. To verify this, we need to remember that $$\nabla f$$ with constant $$L$$ Lipschitz is equivalent to the following:

>$$f(y) − f(x) − \nabla f(x)^T(y − x) \leq \frac{L}{2} \| y − x \|^2_2$$

Maximizing over all $$y = (1-\gamma) x + \gamma s$$ and multiplying by $$\frac{2}{\gamma^2}$$:

>$$M \leq \max_{x,s,y\in C, y=(1−\gamma)x+\gamma s} \frac{2}{\gamma^2} \cdot \frac{L}{2} \| y − x \|^2_2 = \max_{x,s\in C} L \| x − s \|^2_2$$

The boundary of $$M$$ has been determined. Basically, we assume that the bounded curvature is not greater than the curvature assumed for proximal gradient.

## Affine invariance

Let's think about the concepts we learned earlier:

* **Gradient Descent**: $$x^+ = x − t\nabla f(x)$$
* **Pure Newton's Method**: $$x^+ = x − \nabla^2 f(x)^{−1}\nabla f(x)$$

Gradient descent is not affine invariant. That is, scaling coordinates affects the performance of gradient descent. On the other hand, Newton's method is affine invariant. That is, the algorithm behaves the same under all affine transformations of variables. The conditional gradient method is similar to gradient descent but is affine invariant.

**Important property of Frank-Wolfe**: The update is **affine invariant**.

Given nonsingular $$A : \mathbb{R}^n → \mathbb{R}^n$$, we can define $$x = Ax', h(x') = f(Ax')$$. Then Frank-Wolfe for $$h(x')$$ can be computed as follows:

>$$\begin{array}{rcl}
>s' & = & \arg\min_{z\in A^{−1}C} \nabla h(x')^Tz \\
>(x')^+ & = & (1 − \gamma)x' + \gamma s'
>\end{array}$$

Multiplying by $$A$$ gives the same Frank-Wolfe update performed on $$f(x)$$. Even the convergence analysis is affine invariant. The curvature constant $$M$$ of $$h$$ is as follows:

>$$M = \max_{x',s',y'\in A^{−1}C, y'=(1−\gamma)x'+\gamma s'} \frac{2}{\gamma^2} \Bigl( h(y') − h(x') − \nabla h(x')^T(y' − x') \Bigr)$$

Since $$\nabla h(x')^T(y' − x') = \nabla f(x)^T(y − x)$$, it matches $$f$$. However, the affine invariance of the boundary of $$M$$ is not intuitive:

>$$M \leq \max_{x,s\in C} L\|x − s\|^2_2$$

If the diameter of the given $$C$$ is not affine invariant, this is worth considering.

## Inexact updates

We analyzed inaccurate Frank-Wolfe updates [Jaggi (2011)].

Choose $$s^{(k−1)}$$ such that:

>$$\nabla f(x^{(k−1)})^Ts^{(k−1)} \leq \min_{s\in C} \nabla f(x^{(k−1)})^Ts + \frac{M\gamma_k}{2} \cdot \delta$$

where $$\delta \geq 0$$ is an inaccuracy parameter. Using this, we basically get the following ratio:

>**Theorem**: The conditional gradient method using fixed step size $$\gamma_k=2/(k+1), k=1,2,3, ...$$ and inaccuracy parameter $$\delta \geq 0$$ satisfies the following:
>
>$$f(x^{(k)}) − f^{*} \leq \frac{2M}{k + 2} (1 + \delta)$$

**Note**: The optimization error at step $$k$$ is $$\frac{M\gamma_k}{2} \cdot \delta$$. Since $$\gamma_k → 0$$, the error disappears over time as intended.
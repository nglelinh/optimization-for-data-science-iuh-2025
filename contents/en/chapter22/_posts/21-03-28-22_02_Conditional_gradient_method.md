---
layout: post
title: 22-02 Conditional gradient method
chapter: '22'
order: '3'
owner: YoungJae Choung
categories:
- chapter22
lang: en
---

## Projected Gradient Descent

Let's consider a problem with the following constraints.

>$$\min_{x} f(x) \qquad \text{ subject to } x \in C$$

We previously saw that if $$f$$ is convex and smooth, and $$C$$ is also convex, we can use the **projected gradient descent** method. When $$P_{C}$$ is the projection operator for set $$C$$, for the chosen initial value $$x^{(0)}$$ and $$k = 1, 2, 3, ...$$, the following equation holds.

>$$x^{(k)} = P_{C} \bigl( x^{(k−1)} − t_k\nabla f(x^{(k−1)}) \bigr)$$

Projected Gradient Descent can also be represented as a special case of proximal gradient descent, which is essentially motivated by the fact that the $$y$$ value in the local quadratic expansion (2nd Taylor Expansion) becomes the next $$x^{(k)}$$.

>$$x^{(k)} = P_{C} \Bigl( \arg\min_{y} \nabla f(x^{(k−1)})^T(y − x^{(k−1)}) + \frac{1}{2t} \| y − x^{(k−1)} \|^2_2 \Bigr)$$

For more detailed information about Projected Gradient Descent, please reference [9-4]({% multilang_post_url contents/chapter09/20-01-08-09_04_special_cases %}).

## Conditional gradient (Frank-Wolfe) method

Instead of minimizing the quadratic approximation here, let's try something simpler. First, let's examine the point where the value is minimized when we take the inner product of set $$C$$ with $$\nabla f(x)$$. Fundamentally, instead of projection, we can solve problems more conveniently and effectively by minimizing linear functions at points within set $$C$$. Here, we proceed by applying a line search method using convex combinations between the current point and the minimum point.

Let's look at the following formalized method. Choose initial value $$x^{(0)} \in C$$. For $$k = 1, 2, 3, ...$$:

>$$\begin{array}{rcl}
>s^{(k−1)} & \in & \arg\min_{s \in C} \nabla f(x^{(k−1)})^Ts \\
>x^{(k)} & = & (1 − \gamma_k)x^{(k−1)} + \gamma_ks^{(k−1)}
>\end{array}$$

### [Reference]

>$$f(y) \approx f(x) + \nabla f(x)(y-x)$$
>
>$$\arg\min_y f(x) + \nabla f(x)(y-x) \equiv \arg\min_y \nabla f(x)y$$

Here, unlike before, when updating without going through the projection process, we solve the problem using points in the constraint set $$C$$. Basically, the step size is set as $$\gamma_k = \frac{2}{k + 1}, k = 1, 2, 3, ...$$ For any $$0 \leq \gamma_k \leq 1$$, by convexity, $$x^{(k)} \in C$$ is guaranteed. Also, the update proceeds with the following equation:

>$$x^{(k)} = x^{(k−1)} + \gamma_k\bigl( s^{(k−1)} − x^{(k−1)} \bigr)$$

That is, as the algorithm is performed, we move gradually less in the direction of the linear minimizer. In most cases, using the subgradient method on the L1 Ball, which is a special case of coordinate descent, is easier to solve problems than using the projection method.

### [Reference]

An interesting fact is that Frank and Wolfe were post-docs working together with Tucker. They first proposed the algorithm with two different functions. The algorithm was published in 1956 and later published as a paper. For a long time after that, no follow-up papers on this topic came out. However, in recent years, it has gained attention again through Jaggi's insights and has been reintroduced to the world.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/frank_wolfe.png" alt="[Fig 1] Conditional Gradient (Frank-Wolfe) method (From Jaggi 2011)[3]">
  <figcaption style="text-align: center;">[Fig 1] Conditional Gradient (Frank-Wolfe) method (From Jaggi 2011)[3]</figcaption>
</p>
</figure>

## Norm constraints

What happens when $$C = \{x : \| x \| \leq t \}$$ for norm $$\| \cdot \|$$? Let's look at the following:

>$$\begin{align}
>s &\in \arg\min_{\|s\|\leq t} \nabla f(x^{(k−1)})^Ts \\
>&= −t \cdot \arg\max_{\|s\|\leq 1} \nabla f(x^{(k−1)})^Ts \\
>&= −t \cdot \partial \| \nabla f(x^{(k−1)}) \|_{*}
>\end{align}$$

Here $$\| \cdot \|_{*}$$ is the dual norm. In other words, if we know how to compute the subgradient of the dual norm, we can easily perform the Frank-Wolfe step. The key of Frank-Wolfe is that for $$C = \{x : \| x \| \leq t \}$$, it can be obtained more simply or at lower cost than using the projection method, and also requires simpler or lower cost than the prox operator of $$\| \cdot \|$$.

## Example: $$l_1$$ regularization

The following is **$$l_1$$-regularized**:

>$$\min_x f(x) \qquad \text{ subject to } \| x \|_1 \leq t$$

Expanding according to the previous formula, we get $$s^{(k−1)} \in −t\partial \|\nabla f(x^{(k−1)}) \|_\infty$$. The Frank-Wolfe method updates through the following process:

>$$\begin{array}{rcl}
>i_{k−1} & \in & \arg\max_{i=1,...,p} |\nabla_i f(x^{(k−1)})| \\
>x^{(k)} & = & (1 − \gamma_k)x^{(k−1)} − \gamma_kt \cdot \text{sign}(\nabla_{i_{k−1}} f(x^{(k−1)})) \cdot e_{i_{k−1}}
>\end{array}$$

This is a type of coordinate descent (we will look at coordinate descent in detail later).

**Note**: Both require $$O(n)$$ complexity, but projecting onto the $$l_1$$ ball is much simpler.

## Example: $$l_p$$ regularization

The following is an $$l_p$$-regularized problem:

>$$\min_{x} f(x) \qquad \text{ subject to } \| x \|_{p} \leq t$$

When $$1 \leq p \leq \infty$$ and $$q$$ is the dual of $$p$$, we have $$s^{(k−1)} \in −t\partial \| \nabla f(x^{(k−1)}) \|_{q}$$. That is, $$1/p + 1/q = 1$$. We can choose as follows:

>$$s_i^{(k−1)} = −\alpha \cdot \text{sign}(\nabla f_i(x^{(k−1)})) \cdot \left| \nabla f_i(x^{(k−1)}) \right|^{q-1}, \quad i = 1, ..., n$$

Here $$\alpha$$ is a constant such that $$\| s^{(k-1)} \|_{p} = t$$, and the Frank-Wolfe update is the same.

**Note**: For general $$p$$ cases, **projecting onto the p Ball** is much simpler. Except for special cases ($$p = 1, 2, \infty$$), such projections cannot be computed directly (must be processed by optimization).

## Example: trace norm regularization

Let's look at the **trace-regularized** problem:

>$$\min_{X} f(X) \qquad \text{ subject to } \| X \|_{tr} \leq t$$

We have $$S^{(k−1)} \in −t \cdot \partial\| \nabla f(X^{(k−1)}) \|_{op}$$. We can choose $$S^{(k−1)}$$ as follows:

>$$S^{(k−1)} = −t \cdot uv^T$$

Here $$u, v$$ are the left and right singular vectors of $$\nabla f(X^{(k−1)})$$, and the Frank-Wolfe update is the same as usual.

**Note**: This method, if singular value decomposition (SVD) is possible, is much simpler and more efficient than **projecting onto the trace norm ball**.

## Constrained and Lagrange forms

Let's look at the constrained problem once more:

>$$\min_x f(x) \qquad \text{ subject to } \| x \| \leq t$$

The following Lagrange problem is equivalent to the above equation:

>$$\min_x f(x) + \lambda \| x \|$$

The tuning parameters $$t$$ and $$\lambda$$ vary in the interval $$[0,\infty]$$. Also, we should compare the Frank-Wolfe update of $$\| \cdot \|$$ with the proximal operator of $$\| \cdot \|$$.

• **$$l_1$$ norm**: The Frank-Wolfe method updates by scanning the maximum value of the gradient. The proximal operator updates while performing soft-thresholding. Both steps use $$O(n)$$ flops.

• **$$l_p$$ norm**: The Frank-Wolfe update raises each item of the gradient to a power and sums them all, increasing by $$O(n)$$ flops. The proximal operator generally cannot be computed directly.

• **Trace norm**: The Frank-Wolfe update computes only the left and right singular vectors of the gradient. The proximal operator soft-thresholds the singular values of the gradient step by step, requiring singular value decomposition (SVD).

Many different regularizers have derived efficient Frank-Wolfe updates. For example, special polyhedra or cone constraints, sum-of-norms (group-based) regularization, atomic norms, etc.

When comparing the performance of projected gradient technique and conditional gradient technique for Constrained Lasso (here $$n=100, p = 500$$):

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/comparing_projected_and_conditional_gradient.png" alt="[Fig 2] Comparing projected and conditional gradient for constrained lasso problem [3]">
  <figcaption style="text-align: center;">[Fig 2] Comparing projected and conditional gradient for constrained lasso problem [3]</figcaption>
</p>
</figure>

We can see that the Frank-Wolfe method has a convergence rate similar to first-order methods. However, it can actually be slower to converge to high accuracy. (Reference: Here we use fixed step size, but using line search can improve convergence speed.)

## Duality gap

In the Frank-Wolfe iteration process, a duality gap naturally occurs, which actually means the suboptimality gap.

>$$g(x^{(k-1)}) := \max_{s\in C} \nabla f(x^{(k−1)})^T(x^{(k−1)} − s)$$

This is an upper bound of $$f(x^{(k−1)}) − f^{*}$$.

### [Proof]

We can prove using the first-order condition of convexity:

>$$f(s) \geq f(x^{(k−1)}) + \nabla f(x^{(k−1)})^T(s − x^{(k−1)})$$

Minimize both sides for all $$s \in C$$:

>$$f^{*} \geq f(x^{(k−1)}) + \min_{s\in C} \nabla f(x^{(k−1)})^T(s − x^{(k−1)})$$

Finally, rearranging shows that the following equation is an upper bound of the duality gap:

>$$\max_{s\in C} \nabla f(x^{(k−1)})^T(x^{(k−1)} − s) = \nabla f(x^{(k−1)})^T(x^{(k−1)} − s^{(k−1)})$$

### [Note]

Therefore, this quantity comes directly from the Frank-Wolfe update. Why do we call this a "duality gap"? We can rewrite the original problem as follows:

>$$\min_{x} f(x) + I_C(x)$$

Here $$I_C$$ means the indicator function of $$C$$. The dual problem is as follows:

>$$\max_u −f^{*}(u) − I^{*}_C(−u)$$

$$I_C^{*}$$ means the support function of $$C$$. We saw earlier that the conjugate of the indicator function becomes the support function.

### [Recall]

>$$I_C(x) = \begin{cases}
>+\infty & \text{if } x \notin C \\
>0 & \text{if } x \in C
>\end{cases}$$
>
>$$\begin{align}
>I_C^{*} &= \max_{x} \{\langle s, x \rangle - I_C(x)\} \\
>&= \max_{x \in C} \langle s, x \rangle \\
>&= \text{Support function of } C \text{ at } s
>\end{align}$$

When $$x = x^{(k-1)}, u = \nabla f(x^{(k-1)})$$, the duality gap occurring at $$x, u$$ is as follows (derived from 13-04 [Fenchel's inequality]({% multilang_post_url contents/chapter13/21-04-05-13_04_Conjugate_function %})):

>$$f(x) + f^{*}(u) + I^{*}_C(−u) \geq x^Tu + I^{*}_C(−u)$$
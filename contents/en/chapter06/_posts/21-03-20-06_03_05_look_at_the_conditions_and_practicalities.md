---
layout: post
title: 06-03-05 A look at the conditions & Practicalities
chapter: '06'
order: 12
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

## Lipschitz continuity & Strong convexity conditions
Let's examine the conditions for Lipschitz continuity and Strong convexity using $$f(β) = \frac{1}{2} \lVert y−Xβ \rVert_2^2$$ as an example.

### Lipschitz continuity of $$∇f$$ :
* This means $$\nabla^2f(x) \preceq LI$$. <br>
* Since $$∇^2f(β) = X^TX$$, we have $$L = \sigma^2_{max}(X)$$.<br>


### Strong convexity of $$f$$ :
* This means $$\nabla^2f(x) \succeq mI$$.<br>
* Since $$\nabla^2f(β) = X^TX$$, we have $$m = \sigma_{min}^2(X)$$.<br>
* If $$X$$ is an $$n \times p$$ matrix and $$p > n$$, then $$\sigma_{min}(X) = 0$$, so $$f$$ cannot be strongly convex.<br>
* Even if $$\sigma_{min}(X) > 0$$, the condition number $$L/m = \sigma_{max}^2(X)/\sigma_{min}^2(X)$$ can be very large.


If function $$f$$ is strongly convex and has a Lipschitz gradient, then it satisfies the following. You can think of $$f$$ as being sandwiched between two quadratic functions.

>$$mI \preceq \nabla^2f(x) \preceq LI \text{ for all } x ∈ \mathbb{R}^n$$ and $$L > m > 0$$


Satisfying both conditions for all $$x$$ can be very strong. However, if we think more carefully, we can see that this condition is only needed for the following sublevel set.

> $$S = \{x : f(x) \leq f(x^{(0)})\}$$

## Practicalities
### Stopping rule: Stop when $$\lVert ∇f(x) \rVert_2$$ is small.
If $$x^{\star}$$ is the solution, then $$\nabla f(x^{\star}) = 0$$. If $$f$$ is strongly convex, then:
> $$\lVert \nabla f(x) \rVert_2 ≤ \sqrt{2m \epsilon} ⇒ f(x)−f^{\star} ≤ \epsilon$$ </br>

### [Reference] Derivation Process
The derivation process for the above equation is as follows.
Since $$f$$ satisfies Strong Convexity, there exists a constant $$m \ge 0$$ such that:
> $$ \begin{align}
\nabla^2 f(x) \succeq mI \\
\end{align} $$

Let's expand function $$f$$ using the second-order Taylor series.
> $$ \begin{align}
f(y) = f(x) + \nabla f(x)^T(y−x) + \frac{1}{2} (y−x)^T \nabla^2 f(x) (y−x), \space \forall x, y
\end{align} $$

Then, according to the above $$\nabla f(x) \succeq mI$$, we can arrange the last term as a lower bound condition.
> $$ \begin{align}
f(y) &  \ge f(x) + \nabla f(x)^T(y−x) + \frac{m}{2} \lVert y−x \rVert_2^2, \space \forall x, y
\end{align} $$

Differentiating $$f(y)$$ with respect to $$y$$ gives $$\tilde{y} = x - (1/m) \nabla f(x)$$. Substituting $$\tilde{y}$$ into the Taylor expansion gives:

> $$ \begin{align}
f(y) &  \ge f(x) + \nabla f(x)^T(\tilde{y}−x) + \frac{m}{2} \lVert \tilde{y}−x \rVert_2^2 \\
&  = f(x) - \frac{1}{2m} \lVert \nabla f(x) \rVert_2^2
\end{align} $$

Therefore, replacing $$f(y)$$ with $$f^{*}$$ gives:
> $$ \begin{align}
 f^{*}  \ge f(x) - \frac{1}{2m} \lVert \nabla f(x) \rVert_2^2
\end{align} $$

The above stopping rule is derived as follows:

> $$ \begin{align}
f(x) - f^{*} \le \frac{1}{2m} \lVert \nabla f(x) \rVert^2_2 & \le \epsilon \\
\lVert \nabla f(x) \rVert^2_2 & \le 2m\epsilon \\
\lVert \nabla f(x) \rVert_2 & \le \sqrt{2m\epsilon} \\
\end{align} $$


### Advantages and Disadvantages of Gradient Descent

### Pros
* The algorithm is simple and the cost per iteration is low.
* Very fast for well-conditioned, strongly convex problems.

### Cons
* Generally slow because many problems are not strongly convex or well-conditioned.
* Cannot handle non-differentiable functions.
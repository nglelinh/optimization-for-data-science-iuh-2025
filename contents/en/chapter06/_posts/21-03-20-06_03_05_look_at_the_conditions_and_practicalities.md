---
layout: post
title: 06-03-05 A look at the conditions & Practicalities
chapter: '06'
order: 14
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

Convergence theorems look pristine on a chalkboard: "Assume $$f$$ is $$m$$-strongly convex and $$L$$-smooth." Then you open a real dataset with 10,000 features and 500 samples, run least squares, and suddenly $$m = 0$$! This lesson bridges theory and practice by computing exact $$L$$ and $$m$$ values for real machine-learning objectives and revealing what happens when conditions break.

## Key ideas: Computing $$L$$ and $$m$$ in Practice

1. **Least Squares $$f(\beta) = \frac{1}{2}\|y - X\beta\|_2^2$$**: The Hessian is $$\nabla^2 f(\beta) = X^T X$$, so $$L = \sigma_{\max}^2(X)$$ and $$m = \sigma_{\min}^2(X)$$. Whenever $$p > n$$ (more features than samples) or columns are collinear, $$\sigma_{\min}(X) = 0$$, so strong convexity **fails**!
2. **How Ridge Regularization Restores Strong Convexity**: Adding $$\frac{\lambda}{2}\|\beta\|_2^2$$ shifts every Hessian eigenvalue up by $$\lambda$$: $$L = \sigma_{\max}^2(X) + \lambda$$ and $$m = \sigma_{\min}^2(X) + \lambda \ge \lambda > 0$$. The condition number improves dramatically to $$\kappa = \frac{\sigma_{\max}^2(X) + \lambda}{\sigma_{\min}^2(X) + \lambda}$$.
3. **Feature Scaling Directly Controls $$\kappa$$**: If Feature 1 is measured in millimeters ($$10^3$$) and Feature 2 in kilometers ($$10^{-3}$$), the ratio of singular values squared explodes by $$10^{12}$$, crippling gradient descent. Standardizing features to zero mean and unit variance is actually *diagonal preconditioning* that slashes $$\kappa$$.
4. **Cost per Iteration vs. Accuracy Regime**: Each gradient step on least squares costs $$O(np)$$, whereas Newton's method or Cholesky costs $$O(np^2 + p^3)$$. Gradient descent wins when $$p$$ is huge and moderate accuracy ($$\varepsilon \approx 10^{-3}$$) suffices; second-order methods win when $$p$$ is moderate and high accuracy ($$\varepsilon \approx 10^{-10}$$) or high $$\kappa$$ dominates.

### Worked example: How Feature Scaling and Ridge Shrink $$\kappa$$

Consider a two-feature design matrix where Feature 1 is in meters and Feature 2 is in millimeters:
$$X = \begin{bmatrix} 1 & 0 \\ 0 & 100 \end{bmatrix}, \qquad X^T X = \begin{bmatrix} 1 & 0 \\ 0 & 10{,}000 \end{bmatrix}.$$

1. **Raw unscaled OLS ($$\lambda = 0$$)**:
   - $$L = 10{,}000$$, $$m = 1$$, so $$\kappa = 10{,}000$$.
   - Safe step size $$t = 1/L = 10^{-4}$$ shrinks the error along Feature 1 by only $$1 - 10^{-4} = 0.9999$$ per step—needing $$\approx 23{,}000$$ iterations to cut error by $$10\times$$!
2. **Add Ridge regularization $$\lambda = 99$$ (still unscaled)**:
   - $$L = 10{,}099$$, $$m = 100$$, so $$\kappa = 100.99$$ — a **100×** reduction in condition number just from $$\lambda$$!
3. **Standardize features first** (divide column 2 by $$100$$ so $$\tilde{X} = I_2$$):
   - $$\tilde{X}^T \tilde{X} = I_2 \implies L = 1, m = 1, \kappa = 1$$!
   - Gradient descent with $$t = 1$$ converges to the **exact** global optimum in **1 single iteration** instead of 23,000!

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

### Stopping Criteria for Optimization Algorithms

In practice, optimization algorithms need well-defined stopping criteria to determine when to terminate the iterative process. Here are the most common stopping conditions:

#### 1. **Gradient Magnitude Near Zero:**
This is the ideal stopping condition for unconstrained optimization problems, based on the fact that the gradient of the objective function equals zero at local extrema.
$$
\|\nabla f(\mathbf{x}_k)\| \leq \epsilon_1
$$
where $$\mathbf{x}_k$$ is the current point at iteration $$k$$, and $$\epsilon_1$$ is a small positive threshold.

If $$x^{\star}$$ is the solution, then $$\nabla f(x^{\star}) = 0$$. If $$f$$ is strongly convex, then:
> $$\lVert \nabla f(x) \rVert_2 ≤ \sqrt{2m \epsilon} ⇒ f(x)−f^{\star} ≤ \epsilon$$

#### 2. **Small Change in Objective Function Value:**
The algorithm stops when the objective function value no longer changes significantly between consecutive iterations.
$$
|f(\mathbf{x}_{k+1}) - f(\mathbf{x}_k)| \leq \epsilon_2
$$
where $$\epsilon_2$$ is a small positive threshold.

#### 3. **Small Change in Variables (Parameters):**
The algorithm stops when the model parameters no longer change significantly between iterations.
$$
\|\mathbf{x}_{k+1} - \mathbf{x}_k\| \leq \epsilon_3
$$
where $$\epsilon_3$$ is a small positive threshold.

#### 4. **Maximum Number of Iterations:**
To prevent the algorithm from running indefinitely or for too long, an upper limit on the number of iterations is set.
$$
k \geq \text{MaxIterations}
$$
This is a safety stopping condition that ensures the algorithm will terminate within a reasonable time, even if it hasn't achieved perfect convergence.

#### 5. **Maximum Runtime:**
Similar to the maximum iteration limit, the algorithm can be stopped if it has been running for more than an allowed time period.
$$
\text{ElapsedTime} \geq \text{MaxTime}
$$

#### 6. **Combined Conditions:**
In practice, multiple stopping conditions are often used in combination. For example, the algorithm stops if *any* of the above conditions is satisfied. This helps balance between accuracy and computational efficiency.

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
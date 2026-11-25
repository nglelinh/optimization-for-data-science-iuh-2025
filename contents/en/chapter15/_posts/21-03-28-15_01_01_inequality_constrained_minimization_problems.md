---
layout: post
title: 15-01-01 Inequality constrained minimization problems
chapter: '15'
order: 3
owner: Minjoo Lee
categories:
- chapter15
lang: en
---

Consider a linear program in 100 dimensions with 200 inequality constraints. The feasible polytope can easily have more vertices than there are atoms in the observable universe! Active-set methods like Simplex walk along the boundary from vertex to vertex, trying to guess which subset of constraints is binding. Interior-point methods flip the script entirely: ignore the boundary, stay strictly inside the feasible region, and cut straight through the middle in 20–30 Newton steps.

## Background Knowledge Map: Boundary Active-Set vs. Interior-Point Philosophy

- **Pillar 1 — The Binding-Constraint Bottleneck:** At $$x^\star$$, some inequalities satisfy $$h_i(x^\star) = 0$$ (active/binding) while others satisfy $$h_i(x^\star) < 0$$ (inactive); identifying the active set combinatorially is expensive when $$m$$ is large.
- **Pillar 2 — Indicator Reformulation:** Rewriting $$\min f(x)$$ s.t. $$Ax = b, h_i(x) \le 0$$ as $$\min f(x) + \sum_{i=1}^m I_{\mathbb{R}_-}(h_i(x))$$ s.t. $$Ax = b$$ hides the inequalities in an extended-value objective.
- **Pillar 3 — Why Indicators Break Newton:** The indicator $$I_{\mathbb{R}_-}(u)$$ jumps discontinuously from $$0$$ to $$+\infty$$ at $$u = 0$$—it has neither a gradient nor a Hessian at the boundary.
- **Pillar 4 — Smooth Barrier Approximation:** Replacing $$I_{\mathbb{R}_-}(u)$$ with $$-\frac{1}{t}\log(-u)$$ smooths out the vertical cliff into a smooth $$C^\infty$$ curve that approaches $$I_{\mathbb{R}_-}(u)$$ pointwise as $$t \to \infty$$.

### Step-by-Step Worked Example (Read Slowly): Measuring How Closely $$-\frac{1}{t}\log(-u)$$ Approximates $$I_{\mathbb{R}_-}(u)$$

Compare the exact indicator $$I_{\mathbb{R}_-}(u)$$ (which is $$0$$ for $$u \le 0$$ and $$+\infty$$ for $$u > 0$$) with the barrier $$\hat{I}_t(u) = -\frac{1}{t}\log(-u)$$ at three interior points: $$u = -1$$, $$u = -0.1$$, and $$u = -0.001$$.

1. **For $$t = 1$$:**
   - $$u = -1$$: $$\hat{I}_1(-1) = -\log(1) = 0$$.
   - $$u = -0.1$$: $$\hat{I}_1(-0.1) = -\log(0.1) \approx +2.303$$ (strong early push away from wall).
   - $$u = -0.001$$: $$\hat{I}_1(-0.001) \approx +6.908$$.
2. **For $$t = 100$$:**
   - $$u = -1$$: $$\hat{I}_{100}(-1) = 0$$.
   - $$u = -0.1$$: $$\hat{I}_{100}(-0.1) \approx +0.023$$ (almost flat zero—matching $$I_{\mathbb{R}_-}$$!).
   - $$u = -0.001$$: $$\hat{I}_{100}(-0.001) \approx +0.069$$, yet as $$u \to 0^-$$ it *still* shoots smoothly to $$+\infty$$!
3. **Takeaway:** Increasing $$t$$ sharpens the bend right at the boundary $$u = 0$$ without ever losing differentiability.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>
Let's consider the following convex optimization problem.
>
$$\begin{align}
&\min_{x}           && f(x) \\ 
&\text{subject to } && Ax = b \\
                    &&& h_{i}(x) \leq 0, i = 1, \dotsc, m
\end{align}$$

In problems that include inequalities like this, it is difficult to distinguish between binding and non-binding constraints, especially at the boundary of the feasible region. Binding constraints refer to the constraints that affect the solution.

Therefore, the **interior method** is an approach that tries to solve the problem from the interior of the feasible region, not at the boundary.

## Background of interior method
The **interior method** for general problems was proposed in the 1960s by Anthony V. Fiacco and Garth P. McCormick. At the time, it was overshadowed by popular methods like sequential quadratic programming and the active set method, and only gained attention in the 1980s.

The active set method is a theory for determining which constraints affect the optimization result. In the active set method, a constraint is considered active if it is zero, and such constraints are called the active set. However, to find the active set, you need to compute the boundary of the feasible region, and as the number of constraints increases, the computational cost increases.

Recognizing these issues, the interior point method was developed to solve problems from the interior rather than the boundary. For example, in LP, if there are $$m$$ constraints, calculating the boundary requires $$O(m^2)$$ computations, but with the interior method, even for large $$m$$, the solution can be found within 20–30 Newton steps. More details on performance will be discussed later.

* Reference: [Interior point method](https://en.wikipedia.org/wiki/Interior-point_method)
* Reference: [Active set method](https://en.wikipedia.org/wiki/Active_set_method)

## Reducing equality constrained minimization problem
The above problem can be rewritten as $$C := \{x : h_i(x) \le 0, i = 1, \cdots , m \}$$. Inequality constraints can be included in the objective function as an indicator function.

>$$\begin{align}
&\min_{x} \ && f(x) + I_C(x) \\
&\text{subject to }\  && Ax = b \\
\end{align}$$

In this way, the problem can be transformed into an equality constrained minimization problem. However, since the indicator function still includes the boundary, it still has the difficulty of boundary computation from the original problem, and since it is not differentiable, it is difficult to apply Newton's method.

What if we approximate the indicator function $$I_C$$ with a **barrier function**? In that case, the boundary would not be included and since it is differentiable, Newton's method can be applied. 

The method of solving problems redefined with barrier functions in this way is called the barrier method, which is introduced in detail in the next section.
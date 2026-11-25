---
layout: post
title: 06-02-03 Exact line search
chapter: '06'
order: 8
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

If you are walking straight down a canyon trail along $$-\nabla f(x_k)$$, the greedily optimal place to stop is the lowest point along that exact straight line—before the trail starts climbing the opposite wall. That is **Exact Line Search**: at every step, solve the 1D minimization $$s_k = \arg\min_{s \ge 0} f(x_k - s\nabla f(x_k))$$. It produces a striking geometric signature—every consecutive step makes a perfect $$90^\circ$$ right angle!

## Background Knowledge Map: Geometry and Closed Forms of Exact Line Search

1. **Orthogonality of Consecutive Gradients**: Setting $$\frac{d}{ds} f(x_k - s\nabla f(x_k)) = -\nabla f(x_k - s\nabla f(x_k))^T \nabla f(x_k) = 0$$ shows that $$\nabla f(x_{k+1})^T \nabla f(x_k) = 0$$. Geometrically, the search ray stops at the exact point where it is *tangent* to a level curve of $$f$$.
2. **Closed-Form Step Size for Quadratics**: For $$f(x) = \frac{1}{2}x^T Q x - b^T x$$ ($$Q \succ 0$$) with gradient $$g_k = Qx_k - b$$, differentiating $$\phi(s) = f(x_k - s g_k)$$ yields the exact closed-form step:
   $$s_k = \frac{g_k^T g_k}{g_k^T Q g_k}.$$
   Notice this is the reciprocal of the Rayleigh quotient of $$Q$$ along $$g_k$$, always lying in $$[1/\lambda_{\max}, 1/\lambda_{\min}]$$!
3. **Why Exact Line Search Can Still Zig-Zag**: Because consecutive steps are forced to be orthogonal, on an elongated ellipse ($$\kappa \gg 1$$) exact line search bounces back and forth at $$90^\circ$$ angles down the narrow valley—still converging at rate $$\left(\frac{\kappa - 1}{\kappa + 1}\right)^2$$ in objective value (Kantorovich inequality).
4. **When to Use It**: Exact line search shines for quadratic objectives (where $$s_k = \|g_k\|^2 / g_k^T Q g_k$$ costs just one matrix-vector product), whereas for general non-quadratic functions solving the 1D subproblem exactly rarely beats fast Armijo backtracking.

### Step-by-Step Worked Example (Read Slowly): Two Exact Line-Search Steps and the $$90^\circ$$ Orthogonality Check

Minimize $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + 4x_2^2)$$ starting from $$x^{(0)} = (4, 1)$$, where $$Q = \operatorname{diag}(1, 4)$$.

1. **Iteration 1**:
   - Gradient: $$g_0 = Qx^{(0)} = (4, 4)^T$$, with $$f(x^{(0)}) = \frac{1}{2}(16 + 4) = 10$$.
   - Exact step size:
     $$s_0 = \frac{g_0^T g_0}{g_0^T Q g_0} = \frac{4^2 + 4^2}{1(4^2) + 4(4^2)} = \frac{32}{16 + 64} = \frac{32}{80} = 0.4.$$
   - Update: $$x^{(1)} = (4, 1) - 0.4(4, 4) = (2.4,\; -0.6)$$, with $$f(x^{(1)}) = \frac{1}{2}(5.76 + 1.44) = 3.6$$.
2. **Verify orthogonality between $$g_0$$ and $$g_1$$**:
   - New gradient: $$g_1 = Qx^{(1)} = (2.4,\; -2.4)^T$$.
   - Dot product: $$g_0^T g_1 = 4(2.4) + 4(-2.4) = 9.6 - 9.6 = 0$$ — an exact $$90^\circ$$ turn!
3. **Iteration 2**:
   - Exact step size:
     $$s_1 = \frac{2.4^2 + (-2.4)^2}{1(2.4^2) + 4(2.4^2)} = \frac{2}{5} = 0.4.$$
   - Update: $$x^{(2)} = (2.4, -0.6) - 0.4(2.4, -2.4) = (1.44,\; 0.36)$$, with $$f(x^{(2)}) = \frac{1}{2}(2.0736 + 0.5184) = 1.296$$.
   - Check Kantorovich bound: $$\frac{f(x^{(1)})}{f(x^{(0)})} = \frac{3.6}{10} = 0.36 = \left(\frac{4 - 1}{4 + 1}\right)^2 = \left(\frac{3}{5}\right)^2$$ — exact equality with the worst-case bound!

Another way to adapt the step size in gradient descent is **exact line search**.

### What is Exact Line Search?
In exact line search, we move in the direction of the negative gradient and choose the best possible step size.

For the following expression, if $$s > 0$$, the next step $$x - s \nabla f(x)$$ moves away from the current position. By varying $$s$$, we find the step size $$t$$ that minimizes $$f$$:

> $$t = \arg\min_{s \ge 0} f(x - s \nabla f(x))$$

## Exact Line Search Algorithm

The exact line search algorithm can be described as follows:

1. **Step 1**: At current point $$x^{(k)}$$, compute gradient $$\nabla f(x^{(k)})$$
2. **Step 2**: Define univariate function $$\phi(t) = f(x^{(k)} - t \nabla f(x^{(k)}))$$ with $$t \geq 0$$
3. **Step 3**: Find $$t^* = \arg\min_{t \geq 0} \phi(t)$$ by solving $$\phi'(t) = 0$$
4. **Step 4**: Update $$x^{(k+1)} = x^{(k)} - t^* \nabla f(x^{(k)})$$

## Concrete Examples

### Example 1: Simple Quadratic Function (Easy)

Consider the simple objective function:
$$f(x) = \frac{1}{2}x^2 - 3x + 2$$

**Step 1**: Compute gradient
$$\nabla f(x) = x - 3$$

**Step 2**: At starting point $$x^{(0)} = 0$$, we have $$\nabla f(0) = -3$$

**Step 3**: Define line search function
$$\phi(t) = f(0 - t(-3)) = f(3t) = \frac{1}{2}(3t)^2 - 3(3t) + 2 = \frac{9t^2}{2} - 9t + 2$$

**Step 4**: Find minimum by taking derivative
$$\phi'(t) = 9t - 9 = 0 \Rightarrow t^* = 1$$

**Step 5**: Update
$$x^{(1)} = 0 - 1 \cdot (-3) = 3$$

Result: In just one step, we found the optimal solution $$x^* = 3$$ (since $$\nabla f(3) = 0$$).

### Example 2: Multivariable Quadratic Function (Medium)

Consider the objective function:
$$f(x_1, x_2) = x_1^2 + 2x_2^2 - 2x_1 - 4x_2 + 3$$

**Step 1**: Compute gradient
$$\nabla f(x_1, x_2) = \begin{pmatrix} 2x_1 - 2 \\ 4x_2 - 4 \end{pmatrix}$$

**Step 2**: At starting point $$x^{(0)} = (0, 0)$$
$$\nabla f(0, 0) = \begin{pmatrix} -2 \\ -4 \end{pmatrix}$$

**Step 3**: Define line search function
$$x^{(0)} - t \nabla f(x^{(0)}) = \begin{pmatrix} 0 \\ 0 \end{pmatrix} - t \begin{pmatrix} -2 \\ -4 \end{pmatrix} = \begin{pmatrix} 2t \\ 4t \end{pmatrix}$$

$$\phi(t) = f(2t, 4t) = (2t)^2 + 2(4t)^2 - 2(2t) - 4(4t) + 3$$
$$= 4t^2 + 32t^2 - 4t - 16t + 3 = 36t^2 - 20t + 3$$

**Step 4**: Find minimum
$$\phi'(t) = 72t - 20 = 0 \Rightarrow t^* = \frac{20}{72} = \frac{5}{18}$$

**Step 5**: Update
$$x^{(1)} = \begin{pmatrix} 2 \cdot \frac{5}{18} \\ 4 \cdot \frac{5}{18} \end{pmatrix} = \begin{pmatrix} \frac{5}{9} \\ \frac{10}{9} \end{pmatrix}$$

### Example 3: Rosenbrock Function 2D (Hard)

Consider the famous Rosenbrock function:
$$f(x_1, x_2) = 100(x_2 - x_1^2)^2 + (1 - x_1)^2$$

**Step 1**: Compute gradient
$$\nabla f(x_1, x_2) = \begin{pmatrix} -400x_1(x_2 - x_1^2) - 2(1 - x_1) \\ 200(x_2 - x_1^2) \end{pmatrix}$$

**Step 2**: At starting point $$x^{(0)} = (-1, 1)$$
$$\nabla f(-1, 1) = \begin{pmatrix} -400(-1)(1 - 1) - 2(1 - (-1)) \\ 200(1 - 1) \end{pmatrix} = \begin{pmatrix} -4 \\ 0 \end{pmatrix}$$

**Step 3**: Define line search function
$$x^{(0)} - t \nabla f(x^{(0)}) = \begin{pmatrix} -1 \\ 1 \end{pmatrix} - t \begin{pmatrix} -4 \\ 0 \end{pmatrix} = \begin{pmatrix} -1 + 4t \\ 1 \end{pmatrix}$$

$$\phi(t) = f(-1 + 4t, 1) = 100(1 - (-1 + 4t)^2)^2 + (1 - (-1 + 4t))^2$$

This is a more complex function requiring numerical methods to find the minimum.

**Analysis**: With the Rosenbrock function, exact line search becomes complex because:
- The function doesn't have a simple quadratic form
- Numerical methods like Newton-Raphson are needed to solve $$\phi'(t) = 0$$
- There may be multiple local stationary points

### Example 4: Constrained Domain Function (Very Hard)

Consider the problem:
$$\min f(x) = x_1^2 + x_2^2 - 2x_1x_2$$
subject to $$x_1, x_2 \geq 0$$

In this case, exact line search must consider:
$$t^* = \arg\min_{t \geq 0} f(x^{(k)} - t \nabla f(x^{(k)}))$$
such that $$x^{(k)} - t \nabla f(x^{(k)}) \geq 0$$

This leads to a more complex constrained optimization problem.

## Advantages and Disadvantages

### Advantages:
1. **Theoretically optimal**: Each step ensures maximum decrease in objective function along gradient direction
2. **Fast convergence**: For quadratic functions, can converge in one step
3. **No parameter tuning**: No need to choose learning rate

### Disadvantages:
1. **High computational cost**: Each step requires solving a univariate optimization problem
2. **Complex for nonlinear functions**: Requires numerical methods to find minimum
3. **Impractical for large problems**: Computation time becomes prohibitive

## When to Use Exact Line Search?

Exact line search is suitable when:
- **Simple objective functions** (e.g., quadratic)
- **Small dimensions** (typically ≤ 10 variables)
- **High accuracy required** and computational cost is acceptable
- **Special structure** in objective function allows analytical solution

In practice, **backtracking line search** is more efficient and commonly used for most applications.

### Backtracking and exact line search in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/line-search_en.mp4"></video>
</div>

Fixed steps that are too small or too large, the Armijo condition and the shrinks t ← βt, compared with exact search on the lesson's examples.

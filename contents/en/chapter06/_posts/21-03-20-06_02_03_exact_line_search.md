---
layout: post
title: 06-02-03 Exact line search
chapter: '06'
order: 6
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

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

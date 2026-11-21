---
layout: post
title: '06-01-06 Exercises: Step Size and Curvature'
chapter: '06'
order: 4
owner: AI Assistant
categories:
- chapter06
lang: en
lesson_type: exercises
redirect_from:
  - /contents/en/chapter06/06_01_05_hessian_exercises/
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

## Exercise 1: Deriving the Quadratic Approximation

Consider the quadratic approximation used in gradient descent:
$$f(y) \approx f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2$$

**Part A**: Show that minimizing this approximation over $$y$$ gives the gradient descent update $$y = x - t\nabla f(x)$$.

**Part B**: What happens if we change the coefficient to $$\frac{\alpha}{2t}$$ instead of $$\frac{1}{2t}$$? How does this affect the step size?

**Part C**: Interpret the term $$\frac{1}{2t} \|y - x\|_2^2$$ geometrically. What does it prevent?

---

## Exercise 2: Step Size and Function Curvature

Consider two quadratic functions:
- $$f_1(x_1, x_2) = \frac{1}{2}(x_1^2 + x_2^2)$$
- $$f_2(x_1, x_2) = \frac{1}{2}(4x_1^2 + x_2^2)$$

**Part A**: Compute the Hessian matrix (the matrix of second partial derivatives) of both functions.

**Part B**: If we approximate both Hessians by $$\frac{1}{t}I$$, which value of $$t$$ gives the best approximation for each function?

**Part C**: Starting from the point $$(2, 2)$$, perform 3 gradient descent iterations on both functions using your optimal step sizes. Compare the convergence behavior.

---

## Exercise 3: Condition Number and Convergence

For the function $$f(x_1, x_2) = \frac{1}{2}(ax_1^2 + bx_2^2)$$ with $$a > b > 0$$:

**Part A**: What is the condition number $$\kappa = \frac{a}{b}$$? How does it relate to the "shape" of the function?

**Part B**: Show that the optimal step size for the fastest convergence is $$t^* = \frac{2}{a + b}$$.

**Part C**: Compare the convergence speed for:
- $$\kappa = 1$$ ($$a = b = 1$$)
- $$\kappa = 4$$ ($$a = 4, b = 1$$)
- $$\kappa = 100$$ ($$a = 100, b = 1$$)

What happens as the condition number grows?

---

## Exercise 4: Coordinate-wise Step Sizes

Instead of using the same step size for all coordinates, consider:
$$x_1^{(k+1)} = x_1^{(k)} - t_1 \frac{\partial f}{\partial x_1}$$
$$x_2^{(k+1)} = x_2^{(k)} - t_2 \frac{\partial f}{\partial x_2}$$

**Part A**: For $$f(x_1, x_2) = \frac{1}{2}(ax_1^2 + bx_2^2)$$, which choice of $$t_1, t_2$$ makes each coordinate converge in exactly one step?

**Part B**: How does this relate to approximating the Hessian by a diagonal matrix instead of $$\frac{1}{t}I$$?

**Part C**: Implement this coordinate-wise approach and compare it with standard gradient descent on an ill-conditioned quadratic.

---

## Exercise 5: Visualizing the Quality of the Approximation

**Part A**: For $$f(x_1, x_2) = \frac{1}{2}(4x_1^2 + x_2^2)$$, plot the contour lines of the true function and of the quadratic approximation $$f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2$$ around the point $$x = (1, 1)$$.

**Part B**: Try different values of $$t$$ and observe how the quality of the approximation changes.

**Part C**: Which value of $$t$$ makes the approximation's contours look most like those of the true function?

---

## Exercise 6: Strategies for Choosing the Step Size

Compare three step-size strategies on the function $$f(x) = \frac{1}{2}x^T A x$$ with:
$$A = \begin{bmatrix} 10 & 2 \\ 2 & 1 \end{bmatrix}$$

1. **Small fixed step**: $$t = 0.1$$
2. **Large fixed step**: $$t = 0.5$$
3. **Adaptive step**: $$t = \frac{2}{\lambda_{\max} + \lambda_{\min}}$$, where $$\lambda_{\max}, \lambda_{\min}$$ are the largest and smallest eigenvalues of $$A$$

**Part A**: Compute the eigenvalues of $$A$$ and determine the adaptive step size.

**Part B**: Starting from $$(5, 5)$$, run gradient descent with each strategy for 20 iterations.

**Part C**: Plot the convergence curves and trajectories. Which strategy works best, and why?

---

## Exercise 7: True Function vs Quadratic Approximation

Consider the non-quadratic function $$f(x) = e^{x_1} + x_2^2$$.

**Part A**: Compute the gradient and the Hessian of this function.

**Part B**: At the point $$x = (0, 1)$$, compare:
- One gradient descent step with step size $$t = 0.1$$
- One step using the quadratic approximation with the true Hessian
- One step using the quadratic approximation with $$\frac{1}{t}I$$ for $$t = 0.1$$

**Part C**: Which approximation gives a result closer to the true minimizing direction?

---

## Programming Exercises

### Exercise 8: Implement and Compare

Implement the following and compare their performance:

```python
import numpy as np
import matplotlib.pyplot as plt

def quadratic_function(x, A):
    """Compute f(x) = 0.5 * x^T A x"""
    return 0.5 * x.T @ A @ x

def gradient(x, A):
    """Compute the gradient of f(x) = 0.5 * x^T A x"""
    return A @ x

def standard_gd(A, x0, step_size, max_iter=100):
    """Standard gradient descent"""
    x = x0.copy()
    history = [x.copy()]
    
    for i in range(max_iter):
        grad = gradient(x, A)
        x = x - step_size * grad
        history.append(x.copy())
        
        if np.linalg.norm(grad) < 1e-8:
            break
    
    return np.array(history)

def coordinate_wise_gd(A, x0, step_sizes, max_iter=100):
    """Coordinate-wise gradient descent"""
    x = x0.copy()
    history = [x.copy()]
    
    for i in range(max_iter):
        grad = gradient(x, A)
        # Apply a different step size to each coordinate
        x = x - step_sizes * grad
        history.append(x.copy())
        
        if np.linalg.norm(grad) < 1e-8:
            break
    
    return np.array(history)

# Test on different condition numbers
condition_numbers = [1, 4, 16, 64]
x0 = np.array([2.0, 2.0])

for kappa in condition_numbers:
    A = np.array([[kappa, 0], [0, 1]])
    
    # Optimal step size for standard GD
    eigenvals = np.linalg.eigvals(A)
    t_optimal = 2 / (eigenvals.max() + eigenvals.min())
    
    # Optimal coordinate-wise step sizes
    t_coord = 1 / np.diag(A)
    
    # Run both methods
    history_std = standard_gd(A, x0, t_optimal)
    history_coord = coordinate_wise_gd(A, x0, t_coord)
    
    # Plot the results
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.semilogy([quadratic_function(x, A) for x in history_std], 'b-', label='Standard GD')
    plt.semilogy([quadratic_function(x, A) for x in history_coord], 'r--', label='Coordinate-wise GD')
    plt.xlabel('Iteration')
    plt.ylabel('Function value')
    plt.legend()
    plt.title(f'Convergence (κ = {kappa})')
    
    plt.subplot(1, 2, 2)
    plt.plot(history_std[:, 0], history_std[:, 1], 'b-o', label='Standard GD', markersize=3)
    plt.plot(history_coord[:, 0], history_coord[:, 1], 'r--s', label='Coordinate-wise GD', markersize=3)
    plt.xlabel('x₁')
    plt.ylabel('x₂')
    plt.legend()
    plt.title(f'Trajectory (κ = {kappa})')
    plt.axis('equal')
    
    plt.tight_layout()
    plt.show()
```

### Exercise 9: Interactive Visualization

Create an interactive plot that shows:
1. The contour lines of the true function
2. The contour lines of the quadratic approximation
3. The gradient descent trajectory
4. A slider to adjust the step size and see how it affects convergence

**Requirements**:
- Use matplotlib widgets or plotly for interactivity
- Show both well-conditioned and ill-conditioned examples
- Display the approximation error as the step size changes

---

## Solution Outline

### Solution to Exercise 1:
**A**: Take $$\frac{\partial}{\partial y}[f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2] = \nabla f(x) + \frac{1}{t}(y-x) = 0$$
Solving gives $$y = x - t\nabla f(x)$$

**B**: The effective step size becomes $$\frac{t}{\alpha}$$

**C**: The term acts as a "proximity penalty" - it prevents taking a step that is too far from the current point

### Solution to Exercise 2:
**A**: 
- $$\nabla^2 f_1 = I$$
- $$\nabla^2 f_2 = \begin{bmatrix} 4 & 0 \\ 0 & 1 \end{bmatrix}$$

**B**: 
- For $$f_1$$: $$t = 1$$
- For $$f_2$$: $$t = 0.4$$ (minimize the approximation error $$(4-\frac{1}{t})^2 + (1-\frac{1}{t})^2$$ over $$\frac{1}{t}$$, giving $$\frac{1}{t} = \frac{4+1}{2} = 2.5$$)

### Solution to Exercise 3:
**A**: $$\kappa = \frac{a}{b}$$ measures how "stretched" the elliptical contour lines are

**B**: Minimize the convergence factor $$\frac{\kappa-1}{\kappa+1}$$

**C**: A higher condition number → slower convergence, more oscillatory behavior

### Solution to Exercise 4:
**A**: $$t_1 = \frac{1}{a}$$, $$t_2 = \frac{1}{b}$$: then $$x_1^{+} = x_1 - \frac{1}{a}\cdot a x_1 = 0$$ and $$x_2^{+} = 0$$, i.e. convergence in exactly one step.

**B**: This corresponds to approximating the Hessian by the diagonal matrix $$\text{diag}(a, b)$$ (an exact approximation) instead of $$\frac{1}{t}I$$.

**C**: Use $$t_i = 1/A_{ii}$$ (not $$2/A_{ii}$$; a step size of $$2/A_{ii}$$ only flips the sign of the coordinate and oscillates).

### Solution to Exercise 6:
**A**: $$\lambda_{\max} \approx 10.42$$, $$\lambda_{\min} \approx 0.575$$, so $$t = \frac{2}{11} \approx 0.18$$.

**B–C**: Note that $$t = 0.5 > \frac{2}{\lambda_{\max}} \approx 0.19$$, so gradient descent with the large fixed step **diverges**; $$t = 0.1$$ converges but slowly along the low-curvature direction; $$t = \frac{2}{11}$$ gives the best rate.

### Key Learning Outcomes:

1. **Intuition**: the step size is related to an assumed curvature
2. **Practical skill**: how to choose the step size for different problems
3. **Theoretical understanding**: the connection between function properties and optimization behavior
4. **Programming experience**: coding and comparing different approaches

These exercises build understanding without requiring advanced concepts such as Newton's method, focusing instead on the basic relationship between step size, curvature, and convergence behavior.

---
layout: post
title: 06-03-01 Convex function quadratic upper bound
chapter: '06'
order: 8
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

## Introduction

The **quadratic upper bound** is a fundamental property of smooth convex functions that provides a crucial tool for analyzing and designing optimization algorithms. This property establishes that any smooth convex function can be bounded above by a quadratic function, which has important implications for convergence analysis of gradient-based methods.

## Motivation

Why do we care about quadratic upper bounds? 

1. **Algorithm Design**: Many optimization algorithms (like gradient descent) rely on local approximations of the objective function. The quadratic upper bound provides a systematic way to construct these approximations.

2. **Convergence Analysis**: The quadratic upper bound allows us to prove convergence rates for optimization algorithms by bounding how much the function can change.

3. **Step Size Selection**: The Lipschitz constant $$L$$ in the bound directly determines safe step sizes for gradient descent.

## Quadratic Upper Bound Property

**Theorem**: If $$f$$ is convex and $$\nabla f$$ is Lipschitz continuous with constant $$L$$, then $$f$$ satisfies the quadratic upper bound:

> $$ \begin{align}
f(y) & \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2 \quad \forall x, y
\end{align} $$

### Geometric Interpretation

This inequality states that:
- The **linear approximation** $$f(x) + \nabla f(x)^T (y-x)$$ (first-order Taylor expansion) underestimates $$f(y)$$ due to convexity
- The **quadratic upper bound** $$f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2$$ overestimates $$f(y)$$
- The function $$f(y)$$ is "sandwiched" between these two bounds

### Equivalent Characterization

**Corollary**: For any smooth convex function $$f$$, the following function is convex:

> $$ \begin{align}
g(x) & = \frac{L}{2} \| x \|^2_2 - f(x) \quad \text{where } dom(g) = dom(f)
\end{align} $$

This means that $$f(x)$$ can be written as the difference between a quadratic function and a convex function.

## Proof

We will prove both the quadratic upper bound and the equivalent characterization. The proof relies on two key properties of smooth convex functions.

### Prerequisites

**Definition 1 (Monotone Operator)**: In vector space $$X$$, an operator $$T : X \to X^*$$ is monotone if:
> $$(Tu - Tv, u-v) \ge 0, \quad \forall u, v \in X$$

**Property 1 (Monotonicity of Gradient)**: If $$f$$ is convex and differentiable, then $$\nabla f$$ is a monotone operator:
> $$(\nabla f(y) - \nabla f(x))^T (y-x) \ge 0, \quad \forall x, y$$

**Property 2 (Lipschitz Continuity)**: $$\nabla f$$ is Lipschitz continuous with constant $$L$$:
> $$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2, \quad \forall x, y$$

### Proof of Quadratic Upper Bound

**Step 1**: Consider the function $$h(t) = f(x + t(y-x))$$ for $$t \in [0,1]$$. By the fundamental theorem of calculus:

> $$ \begin{align}
f(y) - f(x) &= h(1) - h(0) = \int_0^1 h'(t) dt \\
&= \int_0^1 \nabla f(x + t(y-x))^T (y-x) dt
\end{align} $$

**Step 2**: We can rewrite this as:
> $$ \begin{align}
f(y) - f(x) &= \nabla f(x)^T (y-x) + \int_0^1 [\nabla f(x + t(y-x)) - \nabla f(x)]^T (y-x) dt
\end{align} $$

**Step 3**: Using the Cauchy-Schwarz inequality and Lipschitz continuity:
> $$ \begin{align}
&[\nabla f(x + t(y-x)) - \nabla f(x)]^T (y-x) \\
&\le \|\nabla f(x + t(y-x)) - \nabla f(x)\| \cdot \|y-x\| \\
&\le L \cdot t\|y-x\| \cdot \|y-x\| = Lt\|y-x\|^2
\end{align} $$

**Step 4**: Integrating over $$t \in [0,1]$$:
> $$ \begin{align}
f(y) - f(x) &\le \nabla f(x)^T (y-x) + \int_0^1 Lt\|y-x\|^2 dt \\
&= \nabla f(x)^T (y-x) + L\|y-x\|^2 \int_0^1 t dt \\
&= \nabla f(x)^T (y-x) + \frac{L}{2}\|y-x\|^2
\end{align} $$

Therefore: $$f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2}\|y-x\|^2$$

### Proof of Equivalent Characterization

**Theorem**: The function $$g(x) = \frac{L}{2} \| x \|^2_2 - f(x)$$ is convex.

**Proof**: We need to show that $$\nabla^2 g(x) \succeq 0$$ (positive semidefinite).

Since $$g(x) = \frac{L}{2} \| x \|^2_2 - f(x)$$, we have:
- $$\nabla g(x) = Lx - \nabla f(x)$$
- $$\nabla^2 g(x) = LI - \nabla^2 f(x)$$

For any vector $$v$$, we need to show $$v^T \nabla^2 g(x) v \ge 0$$:

> $$ \begin{align}
v^T \nabla^2 g(x) v &= v^T (LI - \nabla^2 f(x)) v \\
&= L\|v\|^2 - v^T \nabla^2 f(x) v
\end{align} $$

From the Lipschitz continuity of $$\nabla f$$, we can show that $$\nabla^2 f(x) \preceq LI$$, which means:
$$v^T \nabla^2 f(x) v \le L\|v\|^2$$

Therefore: $$v^T \nabla^2 g(x) v = L\|v\|^2 - v^T \nabla^2 f(x) v \ge 0$$

This proves that $$g$$ is convex. $$\square$$

## Examples

### Example 1: Quadratic Function

Consider $$f(x) = \frac{1}{2}x^T A x + b^T x + c$$ where $$A \succeq 0$$ (positive semidefinite).

- $$\nabla f(x) = Ax + b$$
- $$\nabla^2 f(x) = A$$
- If $$\lambda_{max}(A) = L$$, then $$\|\nabla f(x) - \nabla f(y)\| = \|A(x-y)\| \le L\|x-y\|$$

The quadratic upper bound becomes:
$$f(y) \le f(x) + (Ax + b)^T(y-x) + \frac{L}{2}\|y-x\|^2$$

For quadratic functions, this bound is **tight** when $$L = \lambda_{max}(A)$$.

### Example 2: Logistic Loss

Consider the logistic loss $$f(x) = \log(1 + e^{a^T x})$$ where $$a \in \mathbb{R}^n$$.

- $$\nabla f(x) = \frac{e^{a^T x}}{1 + e^{a^T x}} a = \sigma(a^T x) a$$
- $$\nabla^2 f(x) = \sigma(a^T x)(1 - \sigma(a^T x)) aa^T$$

Since $$\sigma(t)(1-\sigma(t)) \le \frac{1}{4}$$ for all $$t$$, we have:
$$\nabla^2 f(x) \preceq \frac{1}{4} aa^T \preceq \frac{\|a\|^2}{4} I$$

Therefore, $$L = \frac{\|a\|^2}{4}$$ and the quadratic upper bound is:
$$f(y) \le f(x) + \sigma(a^T x) a^T(y-x) + \frac{\|a\|^2}{8}\|y-x\|^2$$

### Example 3: Least Squares

For $$f(x) = \frac{1}{2}\|Ax - b\|^2$$ where $$A \in \mathbb{R}^{m \times n}$$:

- $$\nabla f(x) = A^T(Ax - b)$$
- $$\nabla^2 f(x) = A^T A$$
- $$L = \lambda_{max}(A^T A) = \sigma_{max}^2(A)$$ (largest singular value squared)

The quadratic upper bound is:
$$f(y) \le f(x) + (A^T(Ax - b))^T(y-x) + \frac{\sigma_{max}^2(A)}{2}\|y-x\|^2$$

## Applications in Optimization

### 1. Gradient Descent Step Size

The quadratic upper bound directly determines the **maximum safe step size** for gradient descent. If we use step size $$\alpha \le \frac{1}{L}$$, then:

$$f(x - \alpha \nabla f(x)) \le f(x) - \alpha \|\nabla f(x)\|^2 + \frac{L\alpha^2}{2}\|\nabla f(x)\|^2$$

When $$\alpha \le \frac{1}{L}$$, the right-hand side simplifies to:
$$f(x - \alpha \nabla f(x)) \le f(x) - \frac{\alpha}{2}\|\nabla f(x)\|^2$$

This guarantees **sufficient decrease** at each iteration.

### 2. Convergence Rate Analysis

For gradient descent with step size $$\alpha = \frac{1}{L}$$, the quadratic upper bound enables us to prove:

$$f(x_{k+1}) - f^* \le \left(1 - \frac{\mu}{L}\right)(f(x_k) - f^*)$$

where $$\mu$$ is the strong convexity parameter. This gives **linear convergence** with rate $$\left(1 - \frac{\mu}{L}\right)$$.

### 3. Proximal Gradient Methods

In composite optimization $$\min_x f(x) + g(x)$$ where $$f$$ is smooth and $$g$$ is non-smooth, the quadratic upper bound of $$f$$ leads to the proximal gradient update:

$$x_{k+1} = \text{prox}_{\alpha g}\left(x_k - \alpha \nabla f(x_k)\right)$$

where $$\alpha \le \frac{1}{L}$$ ensures convergence.

### 4. Accelerated Methods

Advanced methods like **Nesterov's accelerated gradient** and **FISTA** also rely on the quadratic upper bound to achieve optimal $$O(1/k^2)$$ convergence rates for smooth convex functions.

## Key Takeaways

1. **Fundamental Property**: The quadratic upper bound is a cornerstone of smooth convex optimization theory.

2. **Algorithm Design**: It provides the theoretical foundation for choosing step sizes in gradient-based methods.

3. **Convergence Analysis**: It enables rigorous proofs of convergence rates for optimization algorithms.

4. **Practical Impact**: Understanding $$L$$ helps practitioners tune algorithms effectively.

5. **Geometric Intuition**: It formalizes the idea that smooth convex functions don't "curve too much" - they're bounded above by parabolas.

## Interactive Visualization

The following diagram illustrates the quadratic upper bound property:

```
      f(y)
        |
        |     Quadratic Upper Bound
        |    f(x) + ∇f(x)ᵀ(y-x) + (L/2)||y-x||²
        |   /
        |  /
        | /     True function f(y)
        |/     /
       /|     /
      / |    /
     /  |   /    Linear Approximation
    /   |  /     f(x) + ∇f(x)ᵀ(y-x)
   /    | /
  /     |/
 /      x        y
/       |         →
        |
```

**Key Observations**:
- The **linear approximation** (tangent line) lies below $$f(y)$$ due to convexity
- The **quadratic upper bound** lies above $$f(y)$$ 
- The **true function** $$f(y)$$ is sandwiched between these bounds
- The gap between bounds depends on $$L$$ (Lipschitz constant) and $$\|y-x\|^2$$

## Computational Considerations

### Estimating the Lipschitz Constant

In practice, finding the exact Lipschitz constant $$L$$ can be challenging. Common approaches:

1. **Theoretical Analysis**: For specific function classes (quadratic, logistic, etc.)
2. **Spectral Methods**: $$L = \lambda_{max}(\nabla^2 f)$$ when Hessian is available
3. **Adaptive Methods**: Start with estimate and adjust based on sufficient decrease condition
4. **Line Search**: Use backtracking to find appropriate step sizes

### Practical Algorithm Implementation

```python
def gradient_descent_with_lipschitz(f, grad_f, x0, L_estimate=1.0, max_iter=1000):
    """
    Gradient descent with adaptive Lipschitz constant estimation
    """
    x = x0
    L = L_estimate
    
    for k in range(max_iter):
        grad = grad_f(x)
        
        # Try step with current L estimate
        alpha = 1.0 / L
        x_new = x - alpha * grad
        
        # Check sufficient decrease condition
        if f(x_new) <= f(x) - 0.5 * alpha * np.linalg.norm(grad)**2:
            x = x_new  # Accept step
        else:
            L *= 2  # Increase L estimate and retry
            continue
            
        # Optional: decrease L if step was very conservative
        if k % 10 == 0:
            L *= 0.9
            
    return x
```

This adaptive approach ensures convergence while automatically tuning the Lipschitz constant estimate.
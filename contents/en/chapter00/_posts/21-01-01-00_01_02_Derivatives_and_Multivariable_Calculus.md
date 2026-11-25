---
layout: post
title: 00-01-02 Derivatives and Multivariable Calculus
chapter: '00'
order: 4
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: required
---

Training a modern machine learning model means tuning millions of coupled parameters simultaneously, where nudging one weight ripples through composite layers of transformations. Single-variable slopes are no longer enough: you need partial derivatives to isolate coordinate sensitivities, the gradient to assemble them into a vector, the Hessian to read local bowl-versus-saddle curvature, and the multivariable chain rule—the exact mathematical engine behind backpropagation.

## Key ideas: Multivariable Differential Calculus in Optimization

- **Partial Derivatives & Level Curves:** Partial derivatives measure change along coordinate axes, while level curves $$f(x,y) = c$$ visualize the landscape; the gradient always cuts perpendicularly across level sets.
- **Gradient Vector ($$\nabla f$$):** Packages all first-order partial derivatives into a single vector in $$\mathbb{R}^n$$ whose vanishing ($$\nabla f(x^*) = \mathbf{0}$$) is necessary for unconstrained local optimality.
- **Hessian Matrix ($$\nabla^2 f$$):** Collects all second-order partial derivatives into a symmetric $$n \times n$$ matrix; its positive semidefiniteness certifies local convexity and distinguishes minima from saddles.
- **Multivariable Chain Rule:** Computes derivatives of composed functions $$g(t) = f(x(t))$$ via $$g'(t) = \nabla f(x(t))^T x'(t)$$, enabling exact differentiation along optimization trajectories and through neural network layers.

### Worked example: Gradient, Hessian, and Chain Rule on $$f(x, y) = e^{x^2 + y}$$

Evaluate the local calculus of $$f(x, y) = e^{x^2 + y}$$ at $$(0, 0)$$ and along the path $$\gamma(t) = (t, 2t)$$.

1. **First-order partial derivatives (Gradient):**
   $$\frac{\partial f}{\partial x} = 2x e^{x^2 + y}, \qquad \frac{\partial f}{\partial y} = e^{x^2 + y}.$$
   At $$(0, 0)$$, $$\nabla f(0, 0) = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$.
2. **Second-order partial derivatives (Hessian):**
   $$\frac{\partial^2 f}{\partial x^2} = (2 + 4x^2)e^{x^2 + y}, \quad \frac{\partial^2 f}{\partial x \partial y} = 2x e^{x^2 + y}, \quad \frac{\partial^2 f}{\partial y^2} = e^{x^2 + y}.$$
   At $$(0, 0)$$,
   $$\nabla^2 f(0, 0) = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix},$$
   which is strictly positive definite (eigenvalues $$2$$ and $$1$$), meaning $$f$$ curves upward in every direction around the origin.
3. **Chain rule along $$\gamma(t) = (t, 2t)$$ at $$t = 0$$:** With $$\gamma'(0) = (1, 2)^T$$,
   $$\left.\frac{d}{dt} f(\gamma(t))\right|_{t=0} = \nabla f(0, 0)^T \gamma'(0) = \begin{pmatrix} 0 & 1 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix} = 2.$$
   *Hand check:* Directly substituting gives $$f(t, 2t) = e^{t^2 + 2t}$$, whose derivative $$(2t + 2)e^{t^2 + 2t}$$ at $$t = 0$$ is indeed $$2$$.

This lesson covers derivatives and essential multivariable calculus concepts that form the foundation for optimization theory and algorithms.

---

## Derivatives and Rate of Change

The derivative of a single variable function represents its instantaneous rate of change, which is fundamental to understanding how functions behave locally.

### Basic Derivative Concepts

**Slope between two points:**

$$\text{Slope} = \frac{y_2 - y_1}{x_2 - x_1}$$

**Derivative (instantaneous rate of change):**

$$f'(x_0) = \lim_{x_1 \to x_0} \frac{f(x_1) - f(x_0)}{x_1 - x_0} = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$

The derivative tells us how quickly the function is changing at any given point, which is essential for finding optimal points where the rate of change is zero.

### Level Curves of Functions

Level curves are a fundamental concept in multivariable calculus used to visualize functions of two variables, typically denoted as $$f(x, y)$$. They provide a way to represent a 3D surface in a 2D plane.

A **level curve** of a function $$f(x, y)$$ is the set of all points $$(x, y)$$ in the domain of $$f$$ where the function takes a constant value:

$$f(x, y) = c$$

**Examples:**
- For $$f(x, y) = x^2 + y^2$$, the level curves are circles: $$x^2 + y^2 = c$$
- For $$f(x, y) = x + y$$, the level curves are parallel lines: $$x + y = c$$

Level curves help us understand:
1. The topography of the function
2. Directions of steepest ascent and descent
3. Locations of potential optima

---

## Multivariable Calculus Key Concepts

### Partial Derivatives

For a function $$f(x_1, x_2, \ldots, x_n)$$, the **partial derivative** with respect to $$x_i$$ is:

$$\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, \ldots, x_i + h, \ldots, x_n) - f(x_1, \ldots, x_i, \ldots, x_n)}{h}$$

This measures how $$f$$ changes when only $$x_i$$ varies while all other variables remain fixed.

### Gradient Vector

The **gradient** is a vector composed of all partial derivatives:

$$\nabla f(\mathbf{x}) = \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix}$$

The gradient points in the direction of steepest increase of the function and is perpendicular to level curves.

### Hessian Matrix

The **Hessian matrix** contains all second-order partial derivatives:

$$\nabla^2 f(\mathbf{x}) = \mathbf{H} = \begin{pmatrix} 
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{pmatrix}$$

The Hessian provides information about the curvature of the function and is crucial for:
- Determining the nature of critical points (minimum, maximum, or saddle point)
- Second-order optimization methods like Newton's method

---

## Chain Rule for Multivariable Functions

The chain rule is fundamental for computing derivatives of composite functions, which frequently appear in optimization problems.

### Basic Chain Rule

For a function $$z = f(x, y)$$ where $$x = g(t)$$ and $$y = h(t)$$:

$$ \frac{dz}{dt} = \frac{\partial f}{\partial x} \frac{dx}{dt} + \frac{\partial f}{\partial y} \frac{dy}{dt} $$

### General Chain Rule

For $$z = f(x_1, x_2, \ldots, x_n)$$ where each $$x_i = x_i(t_1, t_2, \ldots, t_m)$$:

$$ \frac{\partial z}{\partial t_j} = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i} \frac{\partial x_i}{\partial t_j} $$

### Applications in Optimization

The chain rule is essential for:

1. **Gradient Computation**: Computing gradients of composite objective functions
2. **Constraint Handling**: Dealing with constraints that are functions of other variables
3. **Algorithm Implementation**: Backpropagation in neural networks and automatic differentiation
4. **Sensitivity Analysis**: Understanding how changes in parameters affect optimal solutions

### Example: Optimization with Constraints

Consider minimizing $$f(x, y) = x^2 + y^2$$ subject to $$g(x, y) = x + y - 1 = 0$$.

Using the constraint to eliminate one variable: $$y = 1 - x$$, so we minimize:
$$h(x) = f(x, 1-x) = x^2 + (1-x)^2$$

Using the chain rule:
$$h'(x) = \frac{\partial f}{\partial x} \cdot 1 + \frac{\partial f}{\partial y} \cdot \frac{d(1-x)}{dx} = 2x + 2(1-x)(-1) = 4x - 2$$

Setting $$h'(x) = 0$$ gives $$x = 1/2$$, so the optimal point is $$(1/2, 1/2)$$.

This demonstrates how multivariable calculus concepts work together to solve optimization problems systematically.

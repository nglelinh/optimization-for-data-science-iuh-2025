---
layout: post
title: 03-02 Operations that preserve convexity
chapter: '03'
order: 6
owner: Minjoo Lee
categories:
- chapter03
lang: en
lesson_type: required
---

Nobody wants to compute a $$500 \times 500$$ Hessian by hand just to prove a regularized empirical loss is convex. Just as Disciplined Convex Programming (DCP) parsers verify convexity symbolically in milliseconds, this lesson teaches you the exact algebraic operations—nonnegative sums, affine pre-compositions, monotone compositions, pointwise suprema, partial minimization, and perspective—that let you prove convexity of intricate objectives by inspection.

## Background Knowledge Map: Disciplined Convexity-Preserving Rules

- **Nonnegative Weighted Sums:** $$\sum_i w_i f_i(x)$$ with $$w_i \ge 0$$ preserves convexity—immediately certifying empirical risk plus regularization ($$\frac{1}{n}\sum \ell_i(w) + \lambda R(w)$$).
- **Composition with an Affine Map:** $$g(x) = f(Ax + b)$$ is convex whenever $$f$$ is convex—turning 1D atoms like $$\log(1 + e^z)$$ into multivariable logistic losses $$\log(1 + e^{-y_i w^T x_i})$$.
- **Scalar & Vector Composition Rules:** $$h(g(x))$$ is convex if $$h$$ is convex & nondecreasing and $$g$$ is convex (or $$h$$ convex & nonincreasing and $$g$$ concave)—remember the curvature-monotonicity sign check!
- **Pointwise Supremum, Minimization & Perspective:** $$\sup_\alpha f_\alpha(x)$$, $$\inf_{y \in C} f(x, y)$$ (when $$f$$ is jointly convex), and $$t f(x/t)$$ ($$t > 0$$) all preserve convexity—explaining why dual functions and quadratic-over-linear terms are convex.

### Step-by-Step Worked Example (Read Slowly): Certifying Convexity Without Computing a Single Hessian

Prove that both functions below are convex using preservation rules alone:

1. **Multivariable log-sum-exp:** $$f(x_1, x_2) = \log\left(e^{2x_1 - x_2} + e^{-x_1 + 3x_2 + 1}\right)$$.
   - Start with the known convex atom $$\text{lse}(z_1, z_2) = \log(e^{z_1} + e^{z_2})$$.
   - Notice $$f(x) = \text{lse}(Ax + b)$$ where $$A = \begin{pmatrix} 2 & -1 \\ -1 & 3 \end{pmatrix}$$ and $$b = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$.
   - By **composition with an affine mapping**, $$f$$ is convex on all of $$\mathbb{R}^2$$.
2. **Exponential of a quadratic:** $$q(x) = e^{x^2}$$ on $$\mathbb{R}$$.
   - Write $$q(x) = h(g(x))$$ with $$g(x) = x^2$$ (convex) and $$h(u) = e^u$$ (convex and **nondecreasing**, since $$h'(u) = e^u > 0$$).
   - By the **scalar composition rule**, $$q(x) = e^{x^2}$$ is convex everywhere (check: $$q''(x) = (2 + 4x^2)e^{x^2} > 0$$).

This section discusses operations that preserve the convexity of convex functions.

- Nonnegative weighted sum
- Composition with affine functions
- Pointwise maximum
- Perspective function
- Linear-fractional function


## Nonnegative weighted sum
Convex functions have the following properties with respect to scalar multiplication and addition:

• When a convex function $$f$$ exists, multiplying it by any nonnegative number still results in a convex function $$f$$.
>$$f$$ is convex $$\Rightarrow \alpha f$$ is convex for $$\alpha \ge 0$$

• When two convex functions ($$f_1, f_2$$) exist, their sum is also convex.
>$$f_1, f_2$$ are convex $$\Rightarrow f_1 + f_2$$ is convex

• A nonnegative weighted sum of convex functions $$f_1, ..., f_m$$ is convex.
>$$f_1, ..., f_n$$ are convex $$\Rightarrow \alpha_1f_1 + \cdots + \alpha_nf_n$$ is convex, $$\alpha_1, ..., \alpha_n \ge 0$$


## Composition
### 1. Affine composition
If function $$f$$ is convex, then $$f(Ax + b)$$ is also convex.
> $$f$$ is convex $$\Rightarrow f(Ax + b)$$ is convex


### 2. General composition
Suppose we have function $$g$$ that maps from $$n$$-dimensional to 1-dimensional space and function $$h$$ that maps from 1-dimensional to 1-dimensional space.
The composition function $$f(x)=h(g(x))$$ is convex or concave in the following cases:

> composition of $$g:\mathbb{R}^n \mapsto \mathbb{R}$$ and $$h:\mathbb{R}\mapsto \mathbb{R}$$:
> $$f(x)=h(g(x))$$

• If $$g$$ is convex, $$h$$ is convex, and $$h$$ is nondecreasing, then $$f$$ is convex.
• If $$g$$ is concave, $$h$$ is convex, and $$h$$ is nonincreasing, then $$f$$ is convex.
• If $$g$$ is concave, $$h$$ is concave, and $$h$$ is nondecreasing, then $$f$$ is concave.
• If $$g$$ is convex, $$h$$ is concave, and $$h$$ is nonincreasing, then $$f$$ is concave.

### [Note]
The monotonicity of the extended-value extension $$\tilde{h}$$ must be preserved. 

### Example
• If $$g$$ is convex, then $$\exp g(x)$$ is convex.
• If $$g$$ is concave and positive, then $$1/g(x)$$ is convex. 

### 3. Vector composition
Suppose we have function $$g$$ that maps from $$n$$-dimensional to $$k$$-dimensional space and function $$h$$ that maps from $$k$$-dimensional to 1-dimensional space.
Then the composition function $$f(x)=h(g(x))=h(g_1(x),g_2(x),...,g_k(x))$$ is convex or concave in the following cases:

>composition of $$g:\mathbb{R}^n\mapsto\mathbb{R}^k$$ and $$h:\mathbb{R}^k\mapsto\mathbb{R}$$:
>$$f(x)=h(g(x))=h(g_1(x),g_2(x),...,g_k(x))$$

• If $$g$$ is convex and $$h$$ is convex, and $$h$$ is nondecreasing in each argument, then $$f$$ is convex.
• If $$g$$ is convex and $$h$$ is concave, and $$h$$ is nonincreasing in each argument, then $$f$$ is concave.

### Example
• If $$g_i$$ are concave and positive, then $$\sum_{i=1}^{m} \log g_i(x)$$ is concave.
• If $$g_i$$ are convex, then $$\log \sum_{i=1}^{m} \exp g_i(x)$$ is convex.


## Pointwise maximum
The pointwise maximum of functions is defined as follows and is convex:
### 1. Pointwise maximum
> $$f_1, f_2$$ are convex functions $$\Rightarrow f(x) = \max \{ f_1(x), f_2(x) \}$$, $$\text{dom } f = \text{dom } f_1 \cap \text{dom } f_2$$ is convex



### 2. Pointwise supremum
If $$f(x, y)$$ is convex in $$x$$ for each $$y \in A$$, then $$g(x) = \sup_{y\in A} f(x, y)$$ is convex.

>$$f(x, y)$$ is convex in $$x$$ for each $$y \in A$$
>$$\Rightarrow g(x) = \sup_{y\in A} f(x, y)$$ with $$\text{dom } g = \{x | (x, y) \in \text{dom} f \text{ for all } y \in A, \sup < \infty \}$$ is convex in $$x$$

## Perspective
If function $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ is convex, then the perspective operation $$g: \mathbb{R}^{n+1} \mapsto \mathbb{R}$$ preserves convexity.

The perspective function $$g: \mathbb{R}^n×\mathbb{R} \mapsto \mathbb{R}$$ of function $$f: \mathbb{R}^n \mapsto \mathbb{R}$$ is:

$$g(x,t) = tf\left(\frac{x}{t}\right), \quad \text{dom } g = \left\{(x,t) \left| \frac{x}{t} \in \text{dom } f, t>0 \right.\right\}$$

If function $$f$$ is convex, then $$g$$ is also convex.

### Example
• When $$t$$ is positive, if $$g(x,t)=x^Tx/t$$ is convex, then $$f(x)=x^Tx$$ is convex.

• **Negative logarithm**
When relative entropy $$g(x,t) =t\log t − t\log x$$ is convex on $$\mathbb{R}_{++}^2$$, then $$f(x)=−\log x$$ is convex.

• If $$f$$ is convex, then $$g(x)=(c^Tx+d)f\left(\frac{Ax+b}{c^Tx+d}\right)$$ is convex under the following condition:
> $$\left\{x \left| c^Tx+d>0, \frac{Ax+b}{c^Tx+d} \in \text{dom } f\right.\right\}$$
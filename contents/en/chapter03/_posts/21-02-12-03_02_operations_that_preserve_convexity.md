---
layout: post
title: 03-02 Operations that preserve convexity
chapter: '03'
order: 6
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

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
---
layout: post
title: 07-02-02 Subgradient Calculus
chapter: '07'
order: 5
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---

Nobody computes ordinary derivatives of complicated expressions by taking $$\lim_{h \to 0}$$ from scratch every time—we use the sum rule, chain rule, and product rule. Subgradients have their own compact **subgradient calculus** (scaling, Minkowski addition, affine composition, and pointwise maxima) that lets you assemble $$\partial f(x)$$ for Lasso, SVMs, and composite losses in seconds.

## Key ideas: The Five Workhorse Rules of Subgradient Calculus

1. **Nonnegative Scaling**: For $$a > 0$$, $$\partial(af)(x) = a\,\partial f(x)$$. (Crucial warning: multiplying by $$a < 0$$ flips convexity to concavity, so scaling only holds for $$a > 0$$!)
2. **Minkowski Addition**: For convex functions $$f_1, f_2$$ (whose domains overlap properly, e.g., finite on $$\mathbb{R}^n$$), $$\partial(f_1 + f_2)(x) = \partial f_1(x) + \partial f_2(x) = \{g_1 + g_2 : g_1 \in \partial f_1(x),\; g_2 \in \partial f_2(x)\}$$.
3. **Affine Composition (Chain Rule)**: If $$h(x) = f(Ax + b)$$, then $$\partial h(x) = A^T \partial f(Ax + b) = \{A^T g : g \in \partial f(Ax + b)\}$$. This single rule handles $$\|Ax - b\|_1$$ and hinge losses $$\max(0, 1 - y_i w^T x_i)$$ effortlessly.
4. **Finite Pointwise Maximum**: If $$f(x) = \max_{i=1,\dots,m} f_i(x)$$, let $$I(x) = \{i : f_i(x) = f(x)\}$$ be the *active* indices achieving the max at $$x$$. Then
   $$\partial f(x) = \operatorname{conv}\!\left(\bigcup_{i \in I(x)} \partial f_i(x)\right).$$

### Worked example: Combining Affine Composition and Addition

Compute the subdifferential of $$f(x_1, x_2) = 3|x_1 - x_2| + \frac{1}{2}x_1^2$$ at the kink point $$x = (2, 2)$$.

1. **Decompose $$f = f_1 + f_2$$**:
   - $$f_1(x) = 3|a^T x|$$ where $$a = (1, -1)^T$$ (scaling + affine composition of $$|\cdot|$$).
   - $$f_2(x) = \frac{1}{2}x_1^2$$ (smooth convex function).
2. **Compute $$\partial f_1(2, 2)$$ via affine composition and scaling**:
   - Evaluate $$a^T x = 2 - 2 = 0$$.
   - Since $$\partial |\cdot|(0) = [-1, 1]$$, the affine composition rule gives $$\partial |a^T x|\big|_{(2,2)} = \{s a : s \in [-1, 1]\}$$.
   - Scaling by $$3 > 0$$ gives
     $$\partial f_1(2, 2) = \left\{\begin{bmatrix} 3s \\ -3s \end{bmatrix} : s \in [-1, 1]\right\}$$
     (the line segment connecting $$(-3, 3)$$ and $$(3, -3)$$).
3. **Compute $$\partial f_2(2, 2)$$**:
   - Since $$f_2$$ is differentiable, $$\partial f_2(2, 2) = \{\nabla f_2(2, 2)\} = \{(2, 0)^T\}$$.
4. **Add the two sets (Minkowski sum)**:
   $$\partial f(2, 2) = \left\{\begin{bmatrix} 2 + 3s \\ -3s \end{bmatrix} : s \in [-1, 1]\right\},$$
   which is the line segment from $$(-1, 3)$$ to $$(5, -3)$$. (Notice $$(0, 0)$$ is *not* on this segment because setting $$-3s = 0 \implies s = 0$ gives $$(2, 0) \neq (0, 0)$$, proving $$(2, 2)$$ is not the minimizer.)

The following basic rules hold for the subdifferential of convex functions:

### Scaling

>
$$
\eqalign{
	ext{if } & a>0, \\
	ext{then } &\partial (af) = a\cdot \partial f
}
$$

### Addition

>
$$\partial(f_1 + f_2) = \partial f_1 + \partial f_2$$

Here, the sum of two sets $$A+B= \{a+b:a\in A, b \in B\}$$ is defined as the set of all possible sums.

### Affine composition

>
$$
\eqalign{
	ext{if } & g(x)=f(Ax+b), \\
	ext{then } & \partial g(x) = A^T \partial f(Ax+b)
}
$$

### Finite pointwise maximum

>
$$
\eqalign{
	ext{if } & f(x)=\max_{i=1,\dots,m} f_i(x), \\
	ext{then } & \partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
}
$$

That is, $$\partial f(x)$$ is defined as the convex hull of the union of the subdifferentials of the functions attaining the value $$f(x)$$ at $$x$$.

### General pointwise maximum

>$$
\eqalign{
	ext{if } & f(x) = \max_{s \in S} f_s(x),\\ 
	ext{then } & \partial f(x) \supseteq cl \left \{ \text{conv} \left(\bigcup_{s:f_s(x)=f(x)} \partial f_s(x)\right) \right\}
}
$$

Here, $$S$$ may be an infinite set, so the union of infinitely many sets may not be closed. Therefore, we take the closure to ensure the subdifferential is a closed set.

On the other hand, if the set $$S$$ is compact (closed and bounded) and the functions $$f_s$$ are continuous with respect to $$s$$, then the equality holds.

For example, consider the following p-norm function $$f(x)$$:
>
\begin{equation}
f(x) =  \vert  \vert x \vert  \vert \_p = \max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx, \qquad 1/p + 1/q =1
\end{equation}

If we let $$f_z(x)=z^Tx$$, then $$z^*$$ such that $$f(x)=f_{z^*}(x)$$ belongs to $$\arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$.

Since $$\partial f_{z^*}(x)=z^*$$, the union $$\bigcup \partial f_{z^*}(x)$$ is the union of all $$z^*$$, which gives us $$\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$.

Here, $$S=\{z: \vert  \vert z \vert  \vert _q \leq 1\}$$ is a compact set, and $$f_z(x)=z^Tx$$ is linear.

By the general pointwise maximum rule, taking the convex hull and then the closure of $$\bigcup \partial f_{z^*}(x)$$ does not add any additional elements to the set.

Therefore, the subgradient of the function $$f(x)$$ is as follows:

>
\begin{equation}
\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^T x
\end{equation}

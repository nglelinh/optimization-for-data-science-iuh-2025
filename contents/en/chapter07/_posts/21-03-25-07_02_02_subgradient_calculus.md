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

---
layout: post
title: 07-02-02 Subgradient Calculus
chapter: "07"
order: 5
owner: "Kyeongmin Woo"
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

한편 집합 $$S$$가 컴팩트하고 (closed and bounded), $$f_s$$ 함수들이 $$s$$에 대해서 연속적이면, 등호 관계가 성립된다. 

예를들어 다음의 p-norm 함수 $$f(x)$$에 대해서,  
>
\begin{equation}
f(x) =  \vert  \vert x \vert  \vert \_p = \max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx, \qquad 1/p + 1/q =1
\end{equation}

$$f_z(x)=z^Tx$$라고 하면, $$f(x)=f_{z^*}(x)$$가 되는 $$z^*$$가 $$\arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$에 속하게 된다. 

한편 $$\partial f_{z^*}(x)=z^*$$ 이므로, $$\bigcup \partial f_{z^*}(x)$$는 모든 $$z^*$$의 합집합으로서, $$\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$ 가 된다.  

여기서 $$S={z: \vert  \vert z \vert  \vert _q \leq 1}$$는 컴팩트 집합이고, $$f_z(x)=z^Tx$$는 선형이므로,

general pointwise maximum 규칙에 의해,  $$\bigcup \partial f_{z^*}(x)$$에 대해서 convex hull을 취한 뒤 closure를 취해도 추가되는 집합의 원소가 존재하지 않는다. 

따라서 $$f(x)$$ 함수의 subgradient는 아래와 같다.

>
\begin{equation}
\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^T x
\end{equation}

---
layout: post
title: 07-03-02 Derivation of First-Order Optimality Condition
chapter: '07'
order: 8
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---

					  \quad & \Longleftrightarrow & &\quad \nabla f(x^{*})^T(y-x^{*}) \geq 0, \text{ for all } y \in C 

If $$f$$ is convex and differentiable, the subgradient optimality condition coincides with the first-order optimality condition, as shown below.

#### Proof
>
$$
\begin{alignat}{2}
f(x^{*}) = \min_{x\in C} f(x)  \quad & \Longleftrightarrow & & \quad f(x^{*}) = \min_x f(x) + I_C(x) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \partial(f(x^{*}) + I_C(x^{*})) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \{\nabla f(x^{*}) \} + \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*}) \in \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*})^Tx^{*} \geq -\nabla f(x^{*})^Ty, \text{ for all }  y \in C \\
                      \quad & \Longleftrightarrow & &\quad \nabla f(x^{*})^T(y-x^{*}) \geq 0, \text{ for all } y \in C 
\end{alignat}
$$
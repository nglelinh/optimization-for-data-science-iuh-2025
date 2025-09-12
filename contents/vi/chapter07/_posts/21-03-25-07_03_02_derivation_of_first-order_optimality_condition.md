---
layout: post
title: 07-03-02 Suy dẫn điều kiện tối ưu bậc một
chapter: '07'
order: 8
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Nếu $$f$$ lồi và khả vi, điều kiện tối ưu gradient dưới trùng với điều kiện tối ưu bậc một, như được chỉ ra dưới đây.

**Điều kiện tối ưu bậc một:**
$$x^* \text{ là tối ưu} \quad \Longleftrightarrow \quad \nabla f(x^*)^T(y - x^*) \geq 0, \text{ với mọi } y \in C$$

### Chứng minh
>
$$
\begin{alignat}{2}
f(x^{*}) = \min_{x\in C} f(x)  \quad & \Longleftrightarrow & & \quad f(x^{*}) = \min_x f(x) + I_C(x) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \partial(f(x^{*}) + I_C(x^{*})) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \{\nabla f(x^{*}) \} + \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*}) \in \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*})^Tx^{*} \geq -\nabla f(x^{*})^Ty, \text{ với mọi }  y \in C \\
                      \quad & \Longleftrightarrow & &\quad \nabla f(x^{*})^T(y-x^{*}) \geq 0, \text{ với mọi } y \in C 
\end{alignat}
$$
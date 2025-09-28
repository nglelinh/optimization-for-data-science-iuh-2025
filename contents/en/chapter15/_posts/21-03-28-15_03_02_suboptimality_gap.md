---
layout: post
title: 15-03-02 Suboptimality gap
order: '9'
owner: Minjoo Lee
categories:
- chapter15
lang: en
---

What is the suboptimality gap between $$f(x^*(t))$$, the solution to the barrier problem obtained in the previous section, and $$f(x^*)$$, the solution to the original problem?

Therefore, we can derive the following equation.

>$$
>\begin{align}
>f(x^*) &\ge f(x^*(t)) + \nabla f(x^*(t))^T (x^* - x^*(t)) \\\\
>h_i(x^*) &\ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t)), \quad i = 1, \cdots, m
>\end{align}
>$$

If convexity is guaranteed, the function is always greater than its tangent, so $$f(x^*) \ge f(x^*(t)) + \nabla f(x^*(t))^T (x^* - x^*(t))$$ holds. (The tangent is the first-order Taylor approximation)

Similarly, since $$h_i(x^*) \ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t))$$ holds, we can derive the following equation:

$$
h_i(x^*(t)) - h_i(x^*) \le \nabla h_i(x^*(t))^T (x^*(t) - x^*), \quad i = 1, \cdots, m
$$

## Derivation of suboptimality gap

Let's use these two equations to derive the suboptimality gap. The right-hand side is derived from the two convexity conditions above.

$$
\begin{align}
f(x^*(t)) - f(x^*) + \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) &\le \left\langle \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)), \quad x^*(t) - x^* \right\rangle \\\\
&= \left\langle -tA^Tv, \quad x^*(t) - x^* \right\rangle \\\\
\end{align}
$$

If we look at the right-hand side of this equation as an inner product, since $$Ax^*(t) = b$$ and $$Ax^* = b$$, the entire term becomes zero.

Therefore, moving the third term of the first equation to the right and simplifying, we get the following result:

$$
\begin{align}
f(x^*(t)) - f(x^*) &\le - \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) \\\\
&= \frac{m}{t} + \sum_{i=1}^{m} u_i(t) h_i(x^*) \\\\
&\le \frac{m}{t}
\end{align}
$$

The first term in the second line becomes $$\frac{m}{t}$$ because it satisfies $$u_i(t) \cdot h_i(x^*(t)) = - \frac{1}{t}$$ from the KKT conditions.

The second term can be removed because $$\sum_{i=1}^{m} u_i(t) h_i(x^*) \le 0$$ from the KKT conditions.

As a result, we can obtain the following suboptimality gap, which becomes a useful stopping criterion for this problem. As a reference, the duality gap can also be derived in the next chapter.

>$$
>\begin{align}
>f(x^*(t)) - f(x^*) \le \frac{m}{t}
>\end{align}
>$$
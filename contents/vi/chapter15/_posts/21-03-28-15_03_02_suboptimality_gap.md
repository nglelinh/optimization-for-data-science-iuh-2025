---
layout: post
title: 15-03-02 Suboptimality gap
order: 9
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---
앞 절에서 구한 barrier problem과 original problem의 solution인 $$f(x^*(t))$$와 $$f(x^*)$$의 suboptimality gap은 어떻게 될까?

What is the suboptimality gap between $$f(x^*(t))$$, the solution to the barrier problem, and $$f(x^*)$$, the solution to the original problem, as derived in the previous section?
따라서, 다음의 식을 구할 수 있다. 
>$$\begin{align}
If convexity is guaranteed, the function is always greater than its tangent, so $$f(x^*) \ge f(x^*(t)) + \nabla f(x^*(t))^T (x^* - x^*(t))$$ holds. (The tangent is the first-order Taylor approximation)
Therefore, we can derive the following equation:


비슷하게 $$h_i(x^*) \ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t))$$가 성립하므로 다음의 식을 구할 수 있다. 

Similarly, since $$h_i(x^*) \ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t))$$ holds, we can derive the following equation:
h_i(x^*(t)) - h_i(x^*) \le \nabla h_i(x^*(t))^T (x^*(t) - x^*), \quad i = i, \cdots , m
\end{align}$$


## Derivation of suboptimality gap
이 두 식에서 suboptimality gap을 유도해 보도록 하겠다. 오른쪽 항은 위의 두 convexity 조건에 의해 도출된다.

Let's use these two equations to derive the suboptimality gap. The right-hand side is derived from the two convexity conditions above.
f(x^*(t)) - f(x^*) + \sum_{i=1}^{m}  u_i(t) (h_i(x^*(t)) - h_i(x^*) ) 
    & \le 	\left\langle \nabla  f(x^*(t))  + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)), \quad x^*(t) - x^* \right\rangle \\\
    & = \left\langle -tA^Tv,  \quad x^*(t) - x^* \right\rangle \\\
\end{align}$$

이 식에서 오른쪽 항을 내적해 보면 $$Ax^*(t) = b$$이고 $$Ax^* = b$$이므로 전체가 0이 된다.
따라서, 첫번째 식의 세번째 항을 오른쪽으로 넘겨서 정리해 보면 다음과 같은 결과를 얻을 수 있다.
If we look at the right-hand side of this equation as an inner product, since $$Ax^*(t) = b$$ and $$Ax^* = b$$, the whole term becomes zero.
Therefore, moving the third term of the first equation to the right and simplifying, we get the following result:
f(x^*(t)) - f(x^*) & \le - \sum_{i=1}^{m}  u_i(t) (h_i(x^*(t)) - h_i(x^*) )  \\\
    & = \frac{m}{t} +  \sum_{i=1}^{m} u_i(t) h_i(x^*) \\\
    & \le \frac{m}{t}   
\end{align}$$

두번째 라인의 첫번째 항은 KKT condition에서 $$u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}$$를 만족하므로  $$\frac{m}{t}$$가 된다.  두번째 항도 KKT condition에서 $$\sum_{i=1}^{m} u_i(t)  h_i(x^*) \le 0$$이므로 제거할 수 있다.


결과적으로 다음과 같은 suboptimality gap을 구할 수 있으며 이는 유용한 stopping criterion이 된다. 참고로, 이 결과는 다음 장에서 duality gap으로도 유도할 수 있다.

>$$\begin{align}
f(x^*(t)) - f(x^*) \le \frac{m}{t}
\end{align}$$
---
layout: post
title: 20-01-01 Convergence Analysis
chapter: '20'
order: 3
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

## Lipschitz gradients and strong convexity
Let's assume $$f$$ is a closed convex function. Then the following equivalence relationship holds. 
>\begin{equation}
\text{$$f$$ is strongly convex with parameter $$d$$ $$\Longleftrightarrow \nabla f^{\ast}$$ Lipschitz with parameter $$1/d$$.} 
\end{equation}

### Proof ###
if, $$g$$가 strongly convex하고 $$x$$at, minimize된다고 하면 다음 relationship,가 성립한다. 
>\begin{equation}
g(y) \geq g(x) + \frac{d}{2}\lVert y-x \rVert_2^2, \text{ for all } y
\end{equation}

우선, $$g(x) = f(x) − u^T x$$를 minimization하는 $$x_u = \nabla f^{\ast}(u)$$and, $$g(x) = f(x) − v^T x$$를 minimization하는 $$x_v = \nabla f^{\ast}(v)$$가 있다고 하자. 

그러면, 위 식으from, 다음 두 부등식을 얻을 수 있다. 
> $$
> \begin{alignat}{1}
> f(x_v) - u^Tx_v \geq f(x_u) - u^T x_u + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 \\
> f(x_u) - v^Tx_u \geq f(x_v) - v^T x_v + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 
> \end{alignat}
> $$

위 두 식을 더하면 다음and, 같은 식을 얻을 수 있다.
>\begin{equation}
f(x_v) - u^Tx_v + f(x_u) - v^Tx_u \geq f(x_u) - u^T x_u +  f(x_v) - v^T x_v + d \lVert x_u - x_v \rVert_2^2.  
\end{equation}

이 식을 재정렬 후 Cauchy-Schwartz를 적용하면 as follows: 정리된다.
> $$
> \begin{align}
> d \lVert x_u - x_v \rVert_2^2 & \leq - u^Tx_v - v^Tx_u + u^T x_u + v^T x_v \\\\
> & = (u-v)^T(x_u - x_v) \\\\
> & \leq \lVert u-v \rVert_2 \lVert x_u - x_v \rVert_2
> \end{align}
> $$

therefore,, 다음and, 같은 relationship,를 확인할 수 있다.

> $$\lVert x_u - x_v \rVert_2 \leq \frac{1}{d} \lVert u-v \rVert_2$$

이to,써 $$\nabla f^{\ast}$$ Lipschitz with parameter $$1/d$$이 증명되었다.

## Convergence guarantees
위 result,and, gradient descent를 combining,, dual objective의 optimal solutionto,의 convergence성을 as follows: 설명할 수 있다.  

* if, $$f$$가 파라미터 $$d$$to, strongly convex 하면, step size $$t_k=d (k=1,2,3, \dots$$)about,서, dual gradient ascent는 $$O(1/\epsilon)$$with, converge한다. 
* if, $$f$$가 파라미터 $$d$$to, strongly convex 하고, $$\nabla f$$는 파라미터 $$L$$to, Lipschitz하면, step size $$t_k=2/(1/d + 1/L)$$ ($$k=1,2,3, \dots$$)about,서, dual gradient ascent는 $$O(\log(1/\epsilon))$$with, converge한다. (linear convergence)




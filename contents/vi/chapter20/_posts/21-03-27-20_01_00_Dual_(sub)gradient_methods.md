---
layout: post
title: 20-01 Dual (sub)gradient methods
chapter: '20'
order: 2
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Even in cases where we cannot find a dual (conjugate) in closed-form, we can use subgradient or gradient methods based on the dual.

For example, consider the following problem. 
>\begin{equation}
\min_x f(x) \text{ subject to } Ax = b
\end{equation}

The dual problem of the above problem is as follows. Here $$f^{\ast}$$ is the conjugate of $$f$$.
>\begin{equation}
\max_u -f^{\ast}(-A^T u) - b^T u
\end{equation}

In this case, if we define $$g(u)$$ as $$-f^{\ast}(-A^Tu)-b^Tu$$, then the subgradient of $$g(u)$$ is as follows.
>\begin{equation}
\partial g(u) = A \partial f^{\ast}(-A^Tu) - b
\end{equation}

In the above expression, $$\partial f^{\ast}(-A^Tu)$$ can be expressed in terms of $$x$$ as follows. 

>\begin{equation}
\partial g(u) = Ax-b \quad \text{where} \quad x \in \arg\min_z f(z) + u^T A z
\end{equation}

## Dual subgradient method
**Dual subgradient method**는 dual problem의 목적식을 maximization하기 for, 시작점 $$u^{(0)}$$at, 시작solution서 $$k=1,2,3,\dots$$about, 다음 step를 iteration한다.
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)} - b) 
> \end{alignat}
> $$

여기서 step size $$t_k(k=1,2,3,\dots$$)는 표준적인 방식with, 선택된다. 

### Strictly Convex인 case,
if, $$f$$가 strictly convex라면 $$f^{\ast}$$는 미분가능solution진다. 

therefore,, algorithm은 $$k=1,2,3,\dots$$about, 다음 step를 iteration하는 **dual gradient ascent**가 된다.
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)}-b) 
> \end{alignat}
> $$

before, 방식and, 다른 점은 $$x^{(k)}$$가 유일하다는 것이다. ($$\text{argmin}$$and,의 relationship,가 $$=$$ relationship,임을 confirming,보라.)

여기서 step size $$t_k(k=1,2,3,\dots$$)도 표준적인 방식with, 선택되며 $$\text{argmin}$$을 수행할 when, proximal gradient나 acceleration도 평소처럼 적용할 수 있다.

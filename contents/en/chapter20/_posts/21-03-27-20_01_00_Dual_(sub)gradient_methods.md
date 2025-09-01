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

Close-form 형태의 dual (conjugate)을 찾을 수 없는 case,to,도 dual basis,의 subgradient or, gradient method를 사용할 수 있다.

for example,, 다음의 problem를 보자. 
>\begin{equation}
\min_x f(x) \text{ subject to } Ax = b
\end{equation}

위 problem의 dual problem는 아래and, 같다. 여기서 $$f^{\ast}$$는 $$f$$의 conjugate이다.
>\begin{equation}
\max_u -f^{\ast}(-A^T u) - b^T u
\end{equation}

이when,, $$g(u)$$를 $$-f^{\ast}(-A^Tu)-b^Tu$$to, 정의하면 $$g(u)$$의 subgradient는 as follows:.
>\begin{equation}
\partial g(u) = A \partial f^{\ast}(-A^Tu) - b
\end{equation}

위 식at, $$\partial f^{\ast}(-A^Tu)$$를 $$x$$to, in summary, 아래and, 같이 표현될 수 있다. 

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

#### Strictly Convex인 case,
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

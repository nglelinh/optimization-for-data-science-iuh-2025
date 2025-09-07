---
layout: post
title: 20-03 Augmented Lagrangians
chapter: '20'
order: 7
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Dual ascent의 단점은 convergence을 보장하기 for, 강한 condition,이 필요하다는 것이다. (convergence을 보장하려면 $$f$$가 strongly convexsolution야 했다.) 이런 단점은 **Augmented Lagrangian method** (or, **Method of multipliers**)by, 개선될 수 있다. 

Primal problem를 아래and, 같이 transformation한다. 
>\begin{equation}
\min_x f(x) + \frac{\rho}{2} \lVert Ax - b \rVert _2^2 \quad \text{ subject to } \quad Ax = b
\end{equation}

여기서 $$\rho > 0$$이다. $$A$$가 full column rank를 갖는다면 목적식은 strongly convex하다. 이는 원래의 problemand, 정확히 동일한 problem가 된다. (Augmented term인 $$Ax - b$$는 0이 되기 because,이다.)

## Augmented Lagrangian Method
**Dual gradient ascent** : $$k=1,2,3,\dots$$about, 다음을 iteration한다. 
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg\min_x f(x) + (u^{(k-1)})^T A x + \frac{\rho}{2} \lVert Ax - b \rVert_2^2  \\
> u^{(k)} & = u^{(k-1)} + \rho (A x^{(k)} - b)
> \end{alignat}
> $$

위 dual algorithmat, $$\rho$$는 step size 역할을 한다, that is, $$t_k=\rho$$이다. 이것은 next,서 그 reason,를 알 수 있다. 

### $$\rho$$가 step size일 when, optimality 증명

$$x^{(k)}$$는 $$f(x) + (u^{(k-1)})^T Ax + \frac{\rho}{2} \lVert Ax - b\rVert _2^2$$ 를 minimization하므to,, 
원래 primal problemto, about, stationary condition,according to,, $$x^{(k)}$$at, 목적식의 subgradient가 아래and, 같이 $$0$$을 포함solution야 한다. 

> $$
> \begin{alignat}{1}
> 0 & \in \partial f(x^{(k)}) + A^T (u^{(k-1)}) + \rho (A x^{(k)} -b))  \\
>   & = \partial f(x^{(k)}) + A^T u^{(k)}
> \end{alignat}
> $$

위식at,, $$u^{(k)} = u^{(k-1)} + \rho (A x^{(k)} - b)$$to, 동작하게 되면, 적당한 condition,하at, $$Ax^{(k)}-b$$가 $$0$$with, 가까워지면서 feasible한 solution를 제공하기 시작하고, 궁극적with, KKT condition,이 만족되고, $$x^{(k)}$$and, $$u^{(k)}$$가 optimalityto, 근접함을 보일 수 있다.  

**Augmented Lagrangian method**의 장점은 훨씬 좋은 convergence성을 갖는다는 것이고, 단점은 problem를 분solution할 수 있는 decomposability를 잃는다는 것이다.

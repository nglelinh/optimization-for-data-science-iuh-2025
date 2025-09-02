---
layout: post
title: 21-01 Last time - Dual method, Augmented Lagrangian method, ADMM, ADMM in scaled
  form
chapter: '21'
order: 2
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

before, 20장at, 우리는 Dual methods, ADMMabout, 살펴보았다. 여기선 ADMM의 응용을 살펴보기to, 앞서, Dual methodsand, Augmented Lagrangian method, ADMM, ADMM in scaled formabout, 정리하고자 한다.

## Dual method
아래의 problem를 let's look at.

>$$
>\begin{align}
>&\min_{x} &&f(x) \\\\
>&\text{ subject to } &&Ax = b
>\end{align}
>$$

여기서 $f$는 strictly convex하고 닫혀있다고 하자. 이 problem의 Lagrangian은 아래and, 같다.
>$$
>\begin{align}
>L(x,u) = f(x)+u^{T}(Ax-b)
>\end{align}
>$$

위 problem의 dual problem는 아래and, 같다.
>$$
>\begin{equation}
>\max_u -f^{\ast}(-A^T u) - b^T u
>\end{equation}
>$$

여기at,의 u는 dual variable이다.

이 식to, about, dual gradient ascent는 아래의 식을 iteration적with, computation한다.($k=1,2,3,...$)
>$$
>\begin{align}
>x^{(k)}&=\underset{x}{\operatorname{argmin}} L(x,u^{(k-1)}) \\\\
>u^{(k)}&= u^{(k-1)} +t_{k}(Ax^{(k)}-b)
>\end{align}
>$$

$$t_{k}$$는 k번째 iteration의 step size이다.

이 dual methodat,는, primal variable $$x$$는 첫번째 식처럼 before, 스텝at, 주어진 $$u^{(k-1)}$$at,의 Lagrangian을 minimization하는 $$x$$값with, 업데이트되고, dual variable $$u$$는 $$Ax-b$$이 gradient direction인 gradient ascent의 형태to, 업데이트가 된다.

이 method의 장점은 $$f$$가 B개의 problemto, 분할이 가능할 when,(decomposable), $$x$$ also, B개의 블록with, 분할하고$$( x =(x_{1}, ...,x_{B})\in \mathbb{R}^{n}, \text{ where }x_{i}\in \mathbb{R}^{n_{i}})$$, matrix A also, B개의 sub-matrix 블록with, decompose가 가능solution서$$(A = [A_{1}, ..., A_{B}] \text{ where }A_{i} \in \mathbb{R}^{m \times n_{i}})$$, 쉽게 병렬화 or, 확장이 가능하여 computation이 용이하다. but, 단점은 convergence성를 보장하기 for, 까다to,운 condition,이 필요하다 ; primal의 feasible을 보장하기 for,, $$f$$가 strongly convex하다는 condition,이 필요하다.[[20-01-01]]({% multilang_post_url contents/chapter20/21-03-27-20_01_01_Convergence_Analysis %})

## Augmented Lagrangian method
Method of multipliers라고도 불리는 Augmented Lagrangian method는 primal problemto, 추가 항을 더하여 computation한다. 이렇게 하면 iteration을 iteration되면서 점difference KKT의 conditions을 만족하게 된다. Dual methodand, comparing, convergence성to, about, condition,(f가 strongly convex)을 완화시킨다. instead of, problem의 분solution(decompose)가 불가능solution지는 단점이 있다. Primal problem의 정의는 as follows:.

>$$
>\begin{align}
>&\min_{x} &&f(x)+\frac{\rho}{2}||Ax-b||_{2}^{2}&\\\\
>&\text{subject to} &&Ax=b
>\end{align}
>$$

여기서 $$\rho>0$$이다. 이 problem의 Lagrangian은 아래and, 같다.

>$$
>\begin{align}
>L_{\rho}(x,u)=f(x)+u^{T}(Ax-b)+\frac{\rho}{2}||Ax-b||_{2}^{2}.
>\end{align}
>$$

Dual gradient ascent는 다음을 iteration한다. ($$k=1,2,3,...$$)
>$$
>\begin{align}
>x^{(k)}&=\underset{x}{\operatorname{argmin}} L_{\rho}(x,u^{(k-1)}) \\\\
>u^{(k)}&= u^{(k-1)} +\rho(Ax^{(k)}-b)
>\end{align}
>$$

이 method의 장점은 위at, 언급하였듯, dual methodto, 비하여 더 나은 convergence condition,을 가진다. 단점은 제product 항이 추가되는 탓to, 분solution가능한 성질(decomposability)을 잃게 된다.

## Alternating direction method of multipliers(ADMM)
ADMM은 dual methodand, augmented Lagrangian method의 장점을 섞은 method이다. problem가 아래의 형태to, 정의 되어있다고 하자.

>$$
>\begin{align}
>\min_{x} f(x)+g(z) \qquad \text{subject to  }Ax+Bz=c
>\end{align}
>$$

이 식to, $$\rho>0$$인 augmented Lagrangian을 정의할 수 있다.
>$$
>\begin{align}
>&L_{\rho} (x,z,u) = f(x)+g(z)+u^{T}(Ax+Bz-c)+\frac{\rho}{2}||Ax+Bz-c||_{2}^{2}\\\\
>\end{align}
>$$

이어서 아래를 iteration하여 variable를 업데이트한다.
>$$
>\begin{align}
>&\text{for k = 1,2,3,...}\\\\
>&x^{(k)}=\underset{x}{\operatorname{argmin}} L_{\rho}(x,z^{(k-1)},u^{(k-1)})\\\\
>&z^{(k)}=\underset{z}{\operatorname{argmin}} L_{\rho}(x^{(k)},z,u^{(k-1)})\\\\
>&u^{(k)}=u^{(k-1)}+\rho(Ax^{(k)}+Bz^{(k)}-c)
>\end{align}
>$$

ADMMat,는 primal variable인 $$x, z$$를 함께 업데이트하지 않고, 순difference적with, 각각 업데이트 한다. and, 순difference적with, 업데이트할 when,는 다른 variable는 가장 최근의 값을 이용한다. that is,, k번째 iterationat, $$z$$를 업데이트 할when,to,는 before, iteration의 값 $$x^{(k-1)}$$이 아닌 $$x^{(k)}$$를 이용하고, u를 업데이트 할when, also, 현재 iterationat, 구한 primal variable $$x^{(k)}, z^{(k)}$$를 바to, 이용한다.

## Alternating direction method of multipliers(ADMM)
ADMM은 제약식 내의 Aand, B가 full rank라는 가정 없이, $$f$$and, $$g$$to, about, 큰 제약 없이(under modeset assumption) 모든 $$\rho > 0$$about, 다음을 만족한다. 

* Residual convergence: $$k$$가 $$\infty$$to, 갈 when,, $$r^{(k)} = A x^{(k)} - B z^{(k)} - c \to 0$$, that is, primal iteration이 feasibilityto, 접근한다.  
* Objective convergence: $$f(x^{(k)}) + g(x^{(k)}) \to f^{\star} + g^{\star}$$, 여기서 $$f^{\star} + g^{\star}$$는 최적의 primal objective 값이다. 
* Dual convergence: $$u^{(k)} \to u^{\star}$$, 여기서 $$u^{\star}$$는 dual solution 이다. 

Convergence rateabout,서는 아직 generally, informing,지진 않았고, 연구가 이루어지고있다. Convergenceto, about, reference문헌은 [21장 소개파트]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})to, 서술되어있다.

## ADMM in scaled form
We can express ADMM in scaled form by changing the dual variable $$u$$ to the scaled variable $$w=u/\rho$$. In summary, the ADMM steps can be represented as follows: 
>$$
>\begin{align}
&x^{(k)} = \underset{x}{\operatorname{argmin}} f(x) + \frac{\rho}{2} ||Ax + Bz^{(k-1)} - c + w^{(k-1)} ||_2^2 \\\\
&z^{(k)} = \arg\min_z g(x) + \frac{\rho}{2} || Ax^{(k)} + Bz - c + w^{(k-1)} ||_2^2  \\\\
&w^{(k)} = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
\end{align}
>$$

Here, $$w^{(k)}$$ can also be expressed as the sum of residuals up to the $$k$$-th iteration as shown below. 
>$$
>\begin{align}
w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
\end{align}
>$$

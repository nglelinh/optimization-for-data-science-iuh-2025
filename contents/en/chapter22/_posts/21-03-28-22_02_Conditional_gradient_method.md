---
layout: post
title: 22-02 Conditional gradient method
chapter: '22'
order: 3
owner: YoungJae Choung
categories:
- chapter22
lang: en
---

## Projected Gradient Descent
아래and, 같은 constraint을 가진 problem를 고려solution 보자.

> $$\min_{x} f(x) \qquad \text{ subject to } x ∈ C $$

$$f$$가 convex이면서 smooth하고, $$C$$ also, convex 이면,  **projected gradient descent** method을 이용할 수 있음을 앞at, 살펴보았다.
$$P_{C}$$가 set $$C$$to, about, projection operator 일 when,, 선택한 초깃값 $$x^{(0)}$$ and, $$k = 1, 2, 3, . . .$$about,서 다음 식이 성립한다.

> $$ x^{(k)} = P_{C } \bigl( x^{(k−1)} − t_k∇f(x^{(k−1)} \bigr)$$

Projected Gradient Descent는 본질적with, local quadratic expansion(2nd Taylor Expansion)at,의 $$y$$값이 다음 $$x^{(k)}$$이 된다는 것을 모티브to, 하는, proximal gradient descent의 스페셜 케이스to, as follows: 나타낼 수도 있다.

> $$x^{(k)} = P_{C} \Bigl( \arg\min_{y} ∇f(x^{(k−1)})^T(y − x^{(k−1)}) + \frac{1}{2t} \| y − x^{(k−1)} \|^2_ 2 \Bigr) $$

Projected Gradient Descentto, about, 좀 더 For detailed information, see [9-4]({% multilang_post_url contents/chapter09/20-01-08-09_04_special_cases %})를  reference 하기 바란다.



## Conditional gradient (Frank-Wolfe) method
여기서 2difference approximation를 minimization 하는 instead of,, 더 간단한 무언가를  시도solution 보자.
first, set $$C$$at, $$\nabla f(x)$$and, inner product했을 when, 값이 minimization되는 점을 let's examine.

근본적with,, Projection instead of, set $$C$$ 안의 점at, 선형function를 minimizing, 더 간편하고 effect,적with, problem를 solution결할 수 있다. 여기서는 현재 포인트at, 최소점 사이to, convex combination을 utilizing, line search method을 applying, 나간다.

다음 정형화된 method을 let's look at.

초깃값 $$x^{(0)} ∈ C$$를 선택한다. $$k = 1, 2, 3, . . . $$

> $$\begin{array}{rcl}
> s^{(k−1)} & ∈ & \arg\min_{s ∈ C} ∇f(x^{(k−1)})^Ts \\\
> x^{(k)} & = & (1 − γ_k)x^{(k−1)} + γ_ks^{(k−1)}
> \end{array}$$

#### [reference]
> $$f(y) \approx f(x) + \nabla f(x)(y-x)$$
> $$\arg\min_y = f(x) + \nabla f(x)(y-x)$$
> $$\equiv \arg\min_y f(x)y$$

여기서, before,and, 다르게 Projection process을 거치지 않고 업데이트를 할 떄, 제약 condition, set $$C$$to, 있는 점을 using, problem를 풀어나간다.

기본적with, step size는 $$γ_k =  \frac{2}{(k + 1)}, k = 1, 2, 3, . . ..$$with, 설정된다.

임의의 $$0 ≤ γ_k ≤ 1$$at, convexityby, $$x^{(k)} ∈ C$$ 임을 보인다.

also, 다음and, 같은 식with, 업데이트가 진행되기도 한다.
> $$ x^{(k)} = x^{(k−1)} + γ_k\bigl( s^{(k−1)} − x^{(k−1)} \bigr) $$


that is,, algorithm 수행됨according to, 선형 minimizer directionwith, 점difference적with, 조금씩 덜 이동하게 된다.
대부분의 case,, co-ordinate descent의 스페셜 케이스인 Ball L1about,서 sub gradient 방식을 사용하는 것이 projection 방식을 사용하는 것 보다 problem를 solution결하기 더 쉽다.


#### [reference]
흥미to,운 in fact,은, Frankand, Wolfe는 Tuckerand, 함께 일하던 post-doc 였다고 informing,져 있으며. 그들은 first, 첫번째to, 이 algorithm을 2 difference functionto, 제안했다고 한다. and, 그 algorithm은 1956년to, 출판되고, 후to, 논문with,도 발표되었다. and, 이 후to, 오랫during, 더 이image 이to, about, 후속 논문은 전혀 나오지 못했다. however, 지난 몇년 during, Jaggi의 통찰력to, 힘임어 세imageto, 소개되면서 다시 주목을 받게 되었다.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/frank_wolfe.png" alt="[Fig 1] Conditional Gradient (Frank-Wolfe) method (From Jaggi 2011)[3]">
  <figcaption style="text-align: center;">[Fig 1] Conditional Gradient (Frank-Wolfe) method (From Jaggi 2011)[3]</figcaption>
</p>
</figure>
<br>

## Norm constraints
norm $$\| · \|$$about, $$C = \{x : \| x \| ≤ t \}$$일 when, 무슨일이 발생할까? 

다음을 let's look at

> $$\begin{align}
> s &∈ \arg\min_{\|s\|≤t} ∇f(x^{(k−1)})^Ts \\\
> &= −t ·  \arg\max_{\|s\|≤1}  ∇f(x^{(k−1)})^Ts \\\
> &= −t · ∂ \| ∇f(x^{(k−1)}) \|_{∗}
> \end{align}$$

여기서 $$\| · \|_{∗}$$는 dual norm을 의마한다.

다시 말solution, dual norm의 subgradient를 computation하는 method을 안다면, Frank-Wolfe step를 쉽게 수행 할 수 있다는 뜻이다.

Frank-Wolfe의 핵심은 $$C = \{x : \| x \| ≤ t \}$$to, projection method을 사용하는 것보다 더 간단하거나 낮은 비용with, 구할 수 있으며, also, when,to,는 $$\| · \|$$의 prox operator보다도 간단하거나 더 낮은 비용을 요한다는 것이다.


## Example: $$l_1$$ regularization
다음은 **$$l_1$$-regularized** 이다.
> $$\min_x f(x) \qquad \text{ subject to } \| x \|_1 ≤ t$$

앞선 공식대to, 전개하면, $$s^{(k−1)} ∈ −t∂ \|∇f(x^{(k−1)}) \|_∞$$ 를 얻을 수 있다.
 
Frank-Wolfe method은 다음의 process을 through, 업데이트 된다.
> $$\begin{array}{rcl}
> i_{k−1} & ∈  & \arg\max_{i=1,...p} ∇_i f(x^{(k−1)}) \\\
> x^{(k)}  & = & (1 − γ_k)x^{(k−1)} − γ_kt · sign ∇_{i_{k−1}} f(x^{(k−1)})· e_{i_{k−1}}
> \end{array}$$

이것은 coordinate descent의 일종이다(coordinate descentabout,서는 나중to, 자세히 let's look at).<br>
Note : 두 가지 모두 $$O(n)$$의 복잡도가 필요but, $$l1$$ ballto, projection 하는 것보다 훨씬 간단하다.

## Example: $$l_p$$ regularization
다음은 $$l_p$$-regularized problem다.

> $$\min_{x}  f(x) \qquad \text{ subject to } \| x \|_{p} ≤ t$$

$$1 ≤ p ≤ ∞$$at, p가 q의 dual일 when,  $$s^{(k−1)} ∈ −t∂ \| ∇f(x^{(k−1)}) \|_{q}$$ 이다. that is,, $$1/p + 1/q = 1$$이다.
 
that is, as follows: 선택할 수 있다. 
> $$s_i^{(k−1)} = −α · sign ∇f_i(x^{(k−1)}) · \left| ∇f_i(x^{(k−1)}) \right|^{p/q}, i = 1, . . . n$$

여기서 $$α$$는 $$\| s^{(k-1)} \|_{q} = t$$and, 같은 constant이고, Frank-Wolfe 업데이트도 동일하다.

Note: 일반 $$p$$의 case, **p Ballto, Projection**하는 것보다 훨씬 간단하다.<br>
특별한 case,($$p = 1, 2, ∞$$)를 제외하고 이러한 projection은 직접 computation할 수 없다(optimizationto, 처리되어야 함).

## Example: trace norm regularization
**trace-regularized** problem를 let's look at
> $$\min_{X} f(X) \qquad \text{ subject to } \| X \|_{tr} ≤ t$$

$$S^{(k−1)} ∈ −t· ∂\| ∇f(X(k−1)) \|_{op}.$$ 이다.

as follows: $$S_i^{(k−1)}$$를 선택할 수 있다.
> $$S_i^{(k−1)} = −t · uv^T$$

여기서 $$u, v$$는 $$∇f(X^{(k−1)})$$의 왼쪽, 오른쪽 singular vector이고, Frank-Wolfe 업데이트는 평소and, 같다.

Note: 이 method은 특이 값 분solution(SVD)가 가능하면, **trace norm ballto, projection**하는 것보다 훨씬 간단하고 효율적with, solution를 구할 수 있는 method이다.


## Constrained and Lagrange forms
제약 condition,이 있는 problem의 solution을 다시 한번 image기solution보자
> $$\min_x f(x) \qquad \text{ subject to } \| x \| ≤ t$$

다음의 Lagrange problem는 위 식and, equivalence이다.
> $$\min_x f(x) + λ \| x \| $$

튜닝 파라미터 $$t$$and, $$λ$$는 [0,∞]구간at, 변한다. also, $$\| · \|$$의 Frank-Wolfe 업데이트를 $$\| · \|$$의  proximal 오퍼레이터and, comparing,야 한다.

• **$$l_1$$ norm**: Frank-Wolfe method은 gradient의 최댓값을 스캔하여 업데이트 한다.
proximal operator soft-threshold를 진행하면서 업데이트 한다. 두 step 모두 $$O(n)$$ flops을 사용 한다.
 
• **$$l_p$$ norm**: 프랭크-울프(Frank-Wolfe) 업데이트는 gradient의 각 항목마다 제product하고 모두 sum산하여 $$O(n)$$ flopwith, 증가시킨다. proximal operator는 generally, 직접 computation할 수 없다.

• **Trace norm**: 프랭크-울프(Frank-Wolfe) 업데이트는 gradient의 image단 왼쪽 및 오른쪽 singular vector를 computation한다. proximal operatorat,는 soft-thresholds gradient step을 진행하며, 특이값 분solution(SVD)를 필요to, 한다.

다른 많은 regularizer들이 효율적인 Frank-Wolfe update를 도출하였다.
예를 들면, special polyhedra or, cone constraints, sum-of-norms (group-based) regularization, atomic norms. 같은 것들이다.


Constrained Lassoto, about, projected gradient techniqueand, conditional gradient technique을 활용했을 when, 성능을 비교하면 as follows:. (여기서 $$n=100, p = 500$$)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/comparing_projected_and_conditional_gradient.png" alt="[Fig 2] Comparing projected and conditional gradient for constrained lasso
problem [3]">
  <figcaption style="text-align: center;">[Fig 2] Comparing projected and conditional gradient for constrained lasso
problem [3]</figcaption>
</p>
</figure>
<br>

프랭크-울프(Frank-Wolfe) method이 first-order method의 convergence율and, 비슷한 양image을 띠고 있는 것을 확인할 수 있을 것이다. however, actually,는 높은 정확도to, convergence하기 for,서는 속도가 더 느려질 수 있다. (reference: 여기서 fixed step size를 사용but,, line search를 using, convergence 속도를 향image시킬 수도 있다.)


## Duality gap
프랭크-울프(Frank-Wolfe) iteration processat, 자연스럽게 duality gap 이 발생되며, 이는 actually, suboptimality gap을 의미한다.
> $$g(x^{(k-1)}) := \max_{s∈C} ∇f(x^{(k−1)})^T(x^{(k−1)} − s) $$

이것은 $$f(x^{(k−1)}) − f^{\star}$$의 upper bound 이다.

##### [Proof]
convexity의 first-order condition을 using, 증명할 수 있다.
> $$f(s) ≥ f(x^{(k−1)}) + ∇f(x^{(k−1)})^T(s − x^{(k−1)})$$

모든 $s ∈ C$about, 양쪽을 minimization 한다.
>  $$f^{\star} ≥ f(x^{(k−1)}) + min_{s∈C} ∇f(x^{(k−1)})^T(s − x^{(k−1)})$$

최종적with,, 다시 정리하여 다음 식은 duality gap이 upper bound임을 showing, 준다.
> $$\max_{s∈C} ∇f(x^{(k−1)})^T(x^{(k−1)} − s) = ∇f(x^{(k−1)})^T(x^{(k−1)} − s^{(k−1)})$$

##### [Note]
therefore, 이 quantity는 Frank-Wolfe 업데이트at, 직접 나온 것이다.
왜 우리는 이를 “duality gap”이라 부를까?

original problem을 다시 써보면 아래and, 같이 쓸 수있다.
> $$\min_{x} f(x) + I_C(x)$$

여기서 $$I_C$$는 $$C$$의 indicator function을 의미한다. dual problem는 아래and, 같다.
> $$\max_u −f^{*} (u) − I^{*}_C(−u)$$

$$I_C^{*}$$가 $$C$$의 support function을 의미한다. Indicator function의 conjugate는 support function 이 됨을 앞서 살펴보았다.

##### [Recall]
> $$
> I_C (X) =  
> \begin{cases}
> +& \infty &if &x &\notin; C \\\
>  & 0      &if &x &\in; C
> \end{cases}
> $$

> $$
> \begin{align}
> I_C^{*} &= \max_{x} \{ <s, x\> - I_C(x)\} \\
>         &= \max_{x \in C} <s, x> \\
>         &= \text{Support function of } C \text{ at } S
> \end{align}
> $$

$$ x = x ^ {(k-1)}, u = ∇f (x ^ {(k-1)}) $$ 일 when,, $$x, u$$at, 발생하는 duality gap은 as follows:. (13-04 [Fenchel's inequality]({% multilang_post_url contents/chapter13/21-04-05-13_04_Conjugate_function %}) from, 유도되기도 한다.)
> $$f(x) + f^{*}(u) + I^{*}_C(−u) ≥ x^Tu + I^{*}_C(−u)$$

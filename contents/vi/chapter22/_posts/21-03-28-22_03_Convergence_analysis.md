---
layout: post
title: 22-03 Convergence analysis
chapter: '22'
order: 4
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---

## Convergence analysis
To find out the convergence characteristics of the Frank-Wolfe method, it is necessary to define the curvature constant of $$f$$ for $$C$$ as follows. [Jaggi (2011)]
> $$M = \max_{x,s,y∈C, y = (1−γ)x+γs} \frac{2}{γ^2} \Bigl( f(y) − f(x) − ∇f(x)^T(y − x) \Bigr)$$
> $$γ ∈ [0, 1]$$

M을 through,서 actually, function가 선형 approximation(linear approximation)from, 얼마나 먼 경향을 가지고 있는지를 측정할 수도 있다.
여기서 $$M = 0$$은 $$f$$가 선형임을 나타낸다. $$f (y) - f (x) - ∇f (x)^T(y - x)$$는 $$f$$by, 정의 된 Bregman divergence 라 부른다.

> Theorem: 고정 스텝 사이즈 $$γk = 2 / (k + 1), k = 1,2,3, ...$$를 이용한 condition,부 그레디언드 method(conditional gradient method)은 다음을 만족한다.
>  $$f(x^{(k)}) − f^{\star} ≤ \frac{2M}{k + 2}$$


$$f(x^{(k)}) − f^{\star} ≤ \epsilon$$를 만족하기 for, 필요한 iteration 횟수는 $$O(1/\epsilon)$$이다.

이제 이 이론은 귀납법with, proving,보고자 한다. however, 바to, 증명with, 넘어가기전 짚고 넘어가야 할 개념을 하나 소개하고자 한다.

## Basic inequality
Frank-Wolfe convergence 속도를 증명하는 데 사용되는 **key inequality**는 as follows:.
> $$f(x^{(k)}) ≤  f(x^{(k−1)}) − γ_kg(x^{(k−1)}) + \frac{γ^2_k}{2}M$$

여기서 $$g(x) = \max_{s∈C} ∇f(x)^T(x − s)$$는 앞서 논의한 duality gap 을 의미하며, 귀납법according to, 이 비율은  inequality를 따르게 된다.

### [Proof] 
Basic inequality를 증명하기 for, $$x^+ = x^{(k)}, x = x^{(k−1)}, s = s^{(k−1)}, γ = γ_k$$ 를 지정한다. and, as follows: 정리한다.
> $$\begin{align}
> f(x^+) &= f\bigl( x + γ(s − x) \bigr) \\\
> &≤ f(x) + γ∇f(x)^T(s − x) + \frac{γ^2}{2}M \\\
> &= f(x) − γg(x) + \frac{γ^2}{2}M
> \end{align}$$

위 수식at, 두 번째 줄은 $$M$$의 정의를 사용했고, 세 번째 줄은 $$g$$의 정의를 사용하였다.

이제, basic inequality를 using,, 우리는 convergence rate theorem을 증명하기 for, 귀납법을 사용한다.

$$k=1$$의 case,, theorem이 만족함을 쉽게 확인할 수 있다.
and, 임의의 $$k > 1$$일 case,, $$f(x^{(k−1)}) − f^{\star} ≤ 2M/(k + 1)$$를 만족함을 가정한다.


앞서 언급한 duality gap $$g(x)$$를 다시 떠올려 보자. 
> $$g(x^{(k−1)}) ≤ f(x^{(k−1)}) − f^{\star}$$
> $$γ_k = 2/(k + 1)$$

and, 이제 basic inequalityto, applying, 보자.
> $$f(x^{(k)}) ≤ f(x^{(k−1)}) − 2(f(x^{(k−1)}) − f^{\star})/(k + 1) + 4M/2(k + 1)^2$$
> $$f(x^{(k)}) − f^{\star} ≤ (1 − 2/(k + 1))(f(x^{(k−1)}) − f^{\star}) + 2M/(k + 1)^2$$
> $$f(x^{(k)}) − f^{\star} ≤ (k − 1/k + 1) × 2M/(k + 1) + 2M/(k + 1)^2 ≤ 2M/(k + 2) $$

이 증명 된 convergence 속도는 ∇f가 립시츠 (Lipschitz) 일 when, projected gradient descent의 informing,진 속helping, 일치한다.

이제 이 가정 들을 comparing, 보자.
in fact, if, $$∇f$$가 constant $$L$$을 가지는 Lipschitz라면 $$diam^2(C) = max_{x,s∈C} ||x − s||^2$$일 when, $$M ≤ diam^2(C) · L$$이다.

이를 확인하기 for, constant $$L$$을 가지는 $$∇f$$ Lipschitz 아래and, 같다는 것을 image기할 필요가 있다.
> $$f(y) − f(x) − ∇f(x)^T(y − x) ≤ \frac{L}{2} \| y − x \|^2_2$$

모든 $$y = (1-γ) x + γs$$를 maximizing, $$\frac{2}{γ^2}$$를 product하면 as follows:.
> $$M ≤ \max_{x,s,y∈C, y=(1−γ)x+γs} \frac{2}{γ^2}·\frac{L}{2} \| y − x \|^2_2 = \max_{x,s∈C} L \| x − s \|^2_2$$

M의 경계가 결정되었다. 기본적with, 경계가 있는 곡률이 proximal gradientabout, 가정한 곡률보다 크지 않다고 가정한다.


## Affine invariance
앞서 배운 개념들을 다시 생각solution 보자.

* Gradient Descent: $$x^+ = x − t∇f(x)$$
* Pure Newton’s Method: $$x^+ = x − ∇^2f(x)^{−1}∇f(x)$$

Gradient descent는 affine invariant하지 않다. that is,, coordinate들을 스케일링 함with, gradient descent의 성능은 향image 된다. 반면, Newton’s method는 affine invariant하다. that is,, 이 algorithm은 variable의 모든 affine transformationat, 동일하게 동작한다.

and, Conditional gradient method는 gradient descentand, 비슷but, affine invariant 하다.

Frank-Wolfe의 중요한 속성 : 업데이트는 **affine invariant** 하다.
Nonsingular $$A : \mathbb{R}^n → \mathbb{R}^n$$가 주어지면, $$x = Ax', h(x') = f(Ax')$$를 정의할 수 있다.
그러면 $$h(x')$$at,의 Frank-Wolfe는 아래and, 같이 computation 가능하다.

> $$\begin{array}{rcl}
> s' & = & \arg\min_{z∈A^{−1}C} ∇h(x')^Tz \\\
> (x')^+ & = & (1 − γ)x' + γs'
> \end{array}$$

$$A$$to, product하면 $$f (x)$$at, 수행되는 것and, 동일한 Frank-Wolfe 업데이트가 나타난다.
심지어 convergence analysis은 affine invariant이다.

$$h$$의 곡률 constant $$M$$은 as follows:.
> $$M = \max_{x',s',y'∈A^{−1}C, y'=(1−γ)x'+γs'} \frac{2}{γ^2} \Bigl( h(y') − h(x') − ∇h(x')^T(y' − x') \Bigr)$$

$$∇h(x')T(y' − x') = ∇f(x)^T(y − x)$$이기 because of, $$f$$and, 일치한다.


however,, affine invariance는 M의 경계at, 직관적이지 않다.

> $$M ≤ \max_{x,s∈C} L||x − s||^2_2$$

주어진 C의 diameter이  affine invariance이 아니라면, 이것은 고민solution 볼 가치가 있다.



## Inexact updates
정확하지 않은 Frank-Wolfe 업데이트를 분석하였다.[Jaggi (2011)]</br>
$$s^{(k−1)}$$를 선택한다. 
> $$∇f(x^{(k−1)})^Ts^{(k−1)} ≤ \min_{s∈C} ∇f(x^{(k−1)})^Ts + \frac{Mγ_k}{2} · δ$$

$$δ ≥ 0$$는 부정확한 파라미터이다. 이를 using,  기본적with, 다음and, 같은 비율을 얻게 된다.

> Theorem: 고정 스텝 magnitude $$γk=2/(k+1),k=1,2,3, ... $$ 및 부정확한 파라미터 δ≥0을 이용한 Conditional gradient method을 using,, 다음을 만족한다.
> $$f(x^{(k)}) − f^{\star} ≤ \frac{2M}{k + 2} (1 + δ)$$

Note: $$k$$ step의 optimization 오difference는 $$\frac{Mγ_k}{2} · δ.$$ 이다. 여기서 $$γ_k → 0$$이므to, 시간이 지날수록 오difference가 사라지는 것을 의도to, 한다.
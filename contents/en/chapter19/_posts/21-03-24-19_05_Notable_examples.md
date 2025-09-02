---
layout: post
title: 19-05 Notable examples
chapter: '19'
order: 9
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

## Glmnet and QUIC
Proximal newton method의 매우 유명한 패키지가 두 가지가 있다.

* **glmnet** (Friedman et al., 2009): $$l_1$$ penalized generalized linear modelsto, about, prox Newton를 구현한 패키지. Coordinate descent를 using,서 inner problem을 푼다.

* **QUIC**  (Hsiesh et al., 2011): graphical lasso problemto, about, prox Newton을 구현한 패키지. Factorization trick을 사용하고 coordinate descent를 using,서 inner problem을 푼다.

두 구현 패키지는 각자의 용도to, 맞춰서 매우 광범위하게 사용되고 있으며 state-of-the-art라고 할 수 있다.

Proximal Newton method는  proximal gradient보다 $$g$$의 gradient을 덜 자주 computation한다. therefore,, computation 비용이 커질수록 proximal newton이 유리하다. also,, inner solver를 신중하게 선택할수록 좋은 성능을 얻을 수 있다.

## Example: lasso logistic regression
Lee et al. (2012)논문at, 제시된 예제를 let's look at.

$$l_1$$ regularized logistic regressionto,대solution 다음 세가지 methodabout,서 성능을 평가하였다.
1.FISTA : accelerated prox grad 2. spaRSA : spectral projected gradient method 3. PN  : proximal Newton

### Dense hessian X (n=5000, p=6000) 예시
데이터 수 n = 5000, feature 개수 p = 6000인 dense feature matrix $$X$$를 갖는 problemabout, 다음and, 같은 성능을 보였다. Hessian이 dense하기 because of, 매우 challenging한 problem라고 할 수 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example1.png" alt="[Fig 1] Dense hessian X (n=5000, p=6000) [2]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Dense hessian X (n=5000, p=6000) [2]</figcaption>
</p>
</figure>

오른쪽은 function 호출 기준with,, 왼쪽은 시간 기준with, 평가한 것with,서, function 호출 기준with, 봤을 when,가 PN의 성능이 매우 우세함을 알 수 있다.

여기서 비용은 $$g$$and, $$\nabla g$$를 computation하는 시간이 대부분이며 particularly, $$\exp$$and, $$\log$$function를 computation하는 시간이 많이 들었다.

### Sparse hessian X (n=542,000, p=47,000) 예시

다음의 case,는 $$X$$가 sparse하기 because of, $$g$$and, $$\nabla g$$를 computation하는 시간이 덜 들었다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example-sparse.png" alt="[Fig 2] Sparse hessian X (n=542,000, p=47,000) [2]" width="70%">
  <figcaption style="text-align: center;">[Fig 2] Sparse hessian X (n=542,000, p=47,000) [2]</figcaption>
</p>
</figure>

## Inexact prox evaluations
Proximal Newton methodat, proximal operation을 computation할 when,  prox operator가 closed form이 아니기 because of, 정확히 computation하지 못한다. 그럼to,도 불구하고, 매우 높은 정확도를 갖는다면 매우 좋은 성질이 될 수 있다.

Lee (2014)at,는 global convergenceand,  local superlinear convergence를 보장하는 inner problem의 stopping rule을 제안했다.

### Three stopping rules
Graphical lasso estimation problemto, inner optimizations을 위한 세 가지 stopping rules을 비교하였다. 이when,, 데이터 개수는 n = 72이고 feature 개수는 p = 1255이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Inexact_prox.png" alt="[Fig 3] Three stopping rules [2]" width="70%">
  <figcaption style="text-align: center;">[Fig 3] Three stopping rules [2]</figcaption>
</p>
</figure>

세 가지 stopping rule은 adaptive, maxiter = 10, exact이다. Maxiter는 inner iteration을 최대 10번to,만 하는 방식이고 exact는 정확한 solution를 구할 when,to, iteration하는 방식이다.

Proximal newton method가 quadratic convergence를 만족하므to, exact는  quadratic convergence를 만족한다고 볼 수 있다. Maxiter=10의 case, 최대 10번의 inner iterationwith,는 quadratic convergence를 만족하지 못but, adaptive의 case, quadratic convergence를 만족하며 세 가지 방식 중 가장 빠르다.

### Stopping rule of usual newton method
일반적인 newton's methodat,는 inner problem은 $$x^{(k-1)}$$의 $$g$$to, about, quadratic approximation인 $$\tilde{g}_{k-1}$$를 minimization한다. and,, $$\eta_k, k=1,2,3,...$$를 choosing,서 다음 condition,을 만족할 when, 중지한다. (이를 forcing sequence라고 한다.)

> \begin{align}
\parallel \nabla \tilde{g}_{k-1}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  \nabla g(x^{(k-1)})  \parallel_2 \\\\
\end{align}

이 condition,은 다음 positionat,의 gradient가 현재 positionat,의 gradient보다 $$\eta_k$$배 만큼 작다는 것을 의미한다. 이when,, Quadratic approximation은 $$\tilde{g}_{k-1}(z) = \nabla g(x)^T (z-x) + \frac{1}{2t} \parallel  z - x \parallel_2^2$$이다.

### Stopping rule of proximal gradient method
Lee et al. (2012)at,는 proximal gradientat,는 gradient instead, generalized gradient를 사용하는 방식을 제안하였다.

> $$
> \begin{align}
\parallel G_{\tilde{f}_{k-1}/M}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  G_{f/M}(x^{(k-1)})  \parallel_2
\end{align}
> $$

여기서 $$\tilde{f}_{k-1} = \tilde{g}_{k-1} + h$$이고 $$mI \preceq \nabla^2 g \preceq MI$$이다.

and,, as follows: $$\eta_k$$를 설정하여 inexact proximal newton이 local superlinear rate를 갖는다는 것을 증명하였다.

> $$
> \begin{align}
> \eta_k \le \min \left\{ \frac{m}{2},  \frac{\parallel  G_{\tilde{f}_{k-2}/M}(x^{(k-1)}) - G_{f/M}(x^{(k-1)})  \parallel_2}{\parallel  G_{f/M}(x^{(k-2)})  \parallel_2} \right\}
> \end{align}
> $$

---
layout: post
title: 21-04 Example - Sparse subspace estimation and sparse plus low rank decomposition
chapter: '21'
order: 5
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

## Sparse subspace estimation
$$S=X^{T}X, X\in \mathbb{R}^{n\times p}$$일when,, 원래의 Xand, projection된 Xand,의 Frobenius norm, that is,, 두 matrix의 distance를 minimization하는 projection를 찾는 problem를 생각solution보자.

>$$
>\begin{align}
>&\min_{P} &&||X-XP||^{2}_{F}\\\\
>&\text{subject to} &&\text{rank(P)=k where P is a projection matrix}
>\end{align}
>$$

이 problem는 projection matrix의 set이 convex set이 아니기 because of, non-convex problem이다. but,, 아래의 convex problemand, 동일함이 informing,져 있다.[[VCLR13]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})] 이는 subspace estimation problem이라고도 불린다.

>$$
>\begin{align}
>&\max_{Y} &&tr(SY)\\\\
>&\text{subject to } &&Y\in F_{k} = \left\{Y\in \mathbb{S}^{p} : 0 \preceq Y \preceq I, tr(Y) = k \right\}
>\end{align}
>$$

[VCLR13]at,는  sparse version(L1 norm이 추가된 형태)의 subspace estimation problem의 solution결을 논한다. 
자세한 유도process은 solution당 논문을 reference한다.
>$$
>\begin{align}
>&\max_{Y} &&tr(SY)-\lambda ||Y||_{1}\\\\
>&\text{subject to } &&Y\in F_{k} 
>\end{align}
>$$

여기서 $$F_{k}$$는 위 식and, 동일하게 Fantope of order k이다.

이다. $$\lambda = 0$$, 인 case, 위의 problem는 일반적인 PCAand, 동일한 problem이다.

위의 problem는 SDP 형태를 가지고 있고, interior point methodto, solution결이 가능하다. but,, 이는 구현이 복잡하고, problem magnitude가 커지면 무척 느려지는 단점이 있다.

이 problem를 ADMMwith, solution결하기 for,, problem를 아래and, 같이 변형한다.
>$$
>\begin{align}
>&\min_{Y,Z} &&-tr(SY)+I_{F_{k}}(Y) + \lambda||Z||_{1}\\\\
>&\text{subject to } &&Y = Z.
>\end{align}
>$$

problem를 in summary, ADMM step은 as follows:. 
 >$$
 >\begin{align}
 >Y^{+} &=  \underset{Y}{\operatorname{argmin}} -tr(SY) + I_{F_{k}}(Y)+\frac{\rho}{2}||Y-Z+W||^{2}_{F}\\\\
 >&=\underset{Y\in F_{k}}{\operatorname{argmin}} \frac{1}{2}||Y-Z+W-\frac{S}{\rho}||^{2}_{F}\\\\
 >&=P_{F_{k}}(Z-W+\frac{S}{\rho})\\\\
 >Z^{+} & = \underset{Z}{\operatorname{argmin}}\lambda||Z||_{1}+\frac{\rho}{2}||Y^{+}-Z+W||^{2}_{F}\\\\
 >&=S_{\frac{\lambda}{\rho}}(Y^{+}+W)\\\\
 >W^{+} &=W+Y^{+}-Z^{+}.
 >\end{align}
 >$$
 
여기서 $$P_{F_{k}}$$는 fantope projection operator이다. 이는 eigendecomposition $$A= U\sum U^{T}, \sum = diag(\sigma_{1},...\sigma_{p})$$의  clippingwith, 정의된다.[[VCLR13]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]:
>$$
>\begin{align}
>P_{F_{k}}(A) = U\Sigma_{\theta}U^{T}, \: \Sigma_{\theta} = diag(\sigma_{1}(\theta),...\sigma_{p}(\theta))
>\end{align}
>$$

각각 $$\sigma_{i}(\theta) = \min\left\{\max\left\{\sigma_{i}-\theta,0\right\},1\right\}$$이고, $$\sum^{p}_{i=1}\sigma_{i}(\theta)=k$$ 이다.

## Sparse plus low rank decomposition
$$M\in \mathbb{R}^{n\times m}$$일when,, sparse plue low rank decomposition problem은 as follows:.[[CLMW09]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]
>$$
>\begin{align}
>&\min_{L,S} &&||L||_{tr}+\lambda||S||_{1}\\\\
>&\text{subject to } &&L+S=M
>\end{align}
>$$

이 problem의 목표는 관측된 matrix M을 low rank matrix Land, sparse matrix Sto, 분solution(decompose)하는 것이다. objective function의 첫번째 항은 L의 trace penaltyto,, L의 singular value의 sum을 minimization한다. 두번째 항은 matrix Sto, about, $$l_{1}$$ normwith,  Sto, about, sparsity를 유도한다. $$\lambda$$는 이 둘을 조절하는 tuning parameter이다. trace normand, $$l_{1}$$ norm 모두 smooth하지 않고, generally, trace norm은 solution를 찾기 어렵다고 informing,져 있다. Sparse subspace estimation problemand, 동일하게 이 problem는 SDP의 형태를 가지고, interior point methodto, solution결 가능but,, 이 also, 복잡하고 속도가 느리다. 이 problemabout,  ADMM은 조금 더 쉬운 update step을 showing,준다.

>$$
>\begin{align}
>L^{+} &= S^{tr}_{\frac{1}{\rho}}(M-S+W)\\\\
>S^{+} &= S^{l_{1}}_{\frac{\lambda}{\rho}}(M-L^{+}+W)\\\\
>W^{+} &= W+M-L^{+}-S^{+}
>\end{align}
>$$

각각 $$S^{tr}_{\frac{1}{\rho}}$$는 matrix soft-thresholding, $$S^{l_{1}}_{\frac{\lambda}{\rho}}$$는 elementwise soft-thresholding이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/candes.png" alt="[Fig 1] Example of sparse plue low rank decomposition on surveliance camera[3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Example of sparse plue low rank decomposition on surveliance camera[3]</figcaption>
</p>
</figure>

[Fig 1]은 sparse plue low rank decomposition을 감시카메라 비디오 영imageto, 분석to, 활용한 예시이다. 고정된 지역을 오랜 시간 촬영하는 감시카메라from,, 대부분의 프레임을 공유하는 low rank 부분을 쉽게 separating,낼 수 있고, sparse한 부분은 특정한 프레임들to, about, 특징적인 부분을 뽑아낸다. for example,서 [Fig 1]의 가운데 column은 low rank, 우측 column은 sparse 부분을 나타낸다. 확인할 수 있듯이, low rank 부분은 거의 모든 프레임at, 나타나는 background, 정보를 가지고 있고, sparse한 부분은 특정한 프레임들at,만 나타나는 특징적인 부분만을 담고 있음을 확인할 수 있다.

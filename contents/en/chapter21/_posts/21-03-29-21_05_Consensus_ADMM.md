---
layout: post
title: 21-05 Consensus ADMM
chapter: '21'
order: 6
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

## Consensus ADMM
아래and, 같은 problem를 생각solution보자.
>$$
>\begin{align}
>\min_{x}\sum^{B}_{i=1} f_{i}(x)
>\end{align}
>$$

위 problemabout, ADMMwith, solution결하기 for,서는, constraint를 introducing,야 했다. 여기서는 update를 병렬적with, operation하기 용이한 형태to, 식을 변형하고자 한다. consensus ADMM이라 불리는 이 접근은 식을 아래and, 같이 reparametrize한다.
>$$
>\begin{align}
>&\min_{x_{1},...,x_{B},x} &&\sum^{B}_{i=1} f_{i}(x_{i})\\\\
>&\text{subject to } &&x_{i}=x, i = 1,...B
>\end{align}
>$$

이를 in summary, decomposable한 ADMM step을 computation할 수 있다.

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2}, i=1,...B\\\\
>x^{(k)} &=\frac{1}{B}\sum_{i=1}^{B}(x_{i}^{(k)}+w_{i}^{(k-1)})\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...,B
>\end{align}
>$$

추가적with, $$\overline{x}=\frac{1}{B}\sum_{i=1}^{B}x_{i}, \overline{w}=\frac{1}{B}\sum_{i=1}^{B}w_{i}$$to, 둘 수 있다. 이렇게 되면, $$k>1$$인 iterationat, $$\overline{w}^{(k)}=0$$임을 쉽게 확인할 수 있고, ADMM update의 두번째 식은 $$x^{(k)}=\overline{x}^{(k)}$$with, 정리된다. therefore, ADMM update식을 아래and, 같이 정리할 수 있다.

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-\overline{x}^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2},  i=1,...B\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-\overline{x}^{(k)},  i=1,...,B.
>\end{align}
>$$

$$i = 1,...B$$to, about, $$x_{i}$$ update는 병렬적with, computation될 수 있다.
정리된 식을 through, consensus ADMMto, about, 직관을 얻을 수 있다. 각  $$x_{i}$$ updateat,는 $$f_{i}(x_{i})$$를 minimization 하려 하고, 동시to, $$l_{2} regularization$$with, 각 $$x_{i}$$를 평균인 $$\overline{x}$$to, 맞추어 간다. if, $$x_{i}$$가 평균보다 커지면, $$w_{i}$$는 증가한다. therefore, 다음 stepat,의 regularization이 커진 $$x_{i}$$를 낮추게 된다.

## General consensus ADMM
Consensus ADMM은 더 일반화된 형태to, creating,질 수 있다. xabout, affine transformationand, 임의의 function $$g$$가 적용된 problem의 형태를 let's look at.

>$$
>\begin{align}
>\min_{x}\sum_{i=1}^{B} f_{i}(a^{T}_{i}x+b_{i})+g(x)
>\end{align}
>$$

이 식about,서도, constraint를 추가하기 for, reparameterize한다.
>$$
>\begin{align}
>&\min_{x_{1},..x_{B},x} &&\sum^{B}_{i=1}f_{i}(a_{i}^{T}x+b)+g(x)\\\\
>&\text{subject to } &&x_{i} = x, i=1,...B
>\end{align}
>$$ 

이어서 분solution가능한 ADMM update를 유도할 수 있다.
>$$
>\begin{align}
>x_{i}^{(k)} &= \underset{x_{i}}{\operatorname{argmin}}f_{i}(a_{i}^{T}x+b_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||^{2}_{2}+g(x)\\\\
>x^{(k)}&=\underset{x}{\operatorname{argmin}} \frac{B\rho}{2}||x-\overline{x}^{(k)}-\overline{w}^{(k-1)}||^{2}_{2}+g(x)\\\\
>w_{i}^{(k)}&=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...B
>\end{align}
>$$ 

Generalized consensus ADMMand, 위at, 유도했던 consensus ADMMand,의 difference이를 in summary, as follows:.

* ADMM step 식이 정리가 되지 않기 because of,, $$\overline{w}^{(k)}=0$$은 더이image 만족하지 않는다.
* $$x_{i}, i=1,...,B$$는 병렬하게 업데이트 가능하다.
*  각각의 $$x_{i}$$ 업데이트는 $$l2$$ 정규화and, 함께 solution당 부분의 loss를 minimization하는 것with, 생각할 수 있다.
*  $$x$$ 업데이트는 임의의 function $$g$$(generally, regularizer)to, about, proximal operation이다.
*  reparmeterization을 어떻게 하는가according to, ADMM algorithm이 다르게 도출된다. 

더 For detailed information, see [reference문헌]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})을 see한다.

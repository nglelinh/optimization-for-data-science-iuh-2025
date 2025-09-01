---
layout: post
title: 18-00 Quasi-Newton methods
chapter: '18'
order: 1
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

1950년대 중반, Argonne 국립 연구소at, 근무 중이었던 물리학자 W.C. Davidon은 coordinate descent method를 using, computation량이 큰 optimization problem를 풀고 있었다. 불행하게도 당시의 컴퓨터가 불안정했던 탓to, computation이 끝나기도 전to, 시스템의 충돌이 빈번히 일어났고, 이to, 좌절한 Davidon은 computation속도를 좀 더 향image시킬 수 있는 method을 찾기to, 결심하게 된다. 그렇게 탄생하게 된 것이 바to, 최초의 Quasi-Newton algorithm이다. 이는 nonlinear optimization을 극적with, 진보시키는 계기가 되었으며, 뒤이어 20여 년 during, 이 methodto, about, 다양한 후속연구들이 등장하였다.

아이러니하게도 [Davidon의 연구](http://www.math.mcgill.ca/dstephens/680/Papers/Davidon91.pdf)는 당시 출판되지 못하고 30년 이image을 technical reportto, 남아있었다. and, 마침내 1991년이 되어서야 [SIAM Journal on Optimization의 첫 번째 판](https://epubs.siam.org/toc/sjope8/1/1)to, 실리게 되었다.

Quasi-Newton methods는 각 iteration(iteration)at, objective functionto, about, gradient만을 필요to, 한다. 이는 이difference 미분을 필요to,하는 newton methods보다 computation적인 부담이 훨씬 적으며 더불어 superlinear convergence를 보인다는 점at, 충분히 매력적인 method이라고 볼 수 있다 [14]. 

## Motivation for Quasi-Newton methods

다음and, 같은 unconstrained, smooth optimization problem이 있다고 solution보자.
> $$
> \min_x \: f(x), \\\\
> \text{where } f \text{ is twice differentiable, and } dom \; f = \mathbb{R}^n.
> $$

위 problemto, about, Gradient descent methodand, Newton's methodat,의 xto, about, 업데이트 method은 각각 아래and, 같다.
>**Gradient descent method:**
>$$
>x^+ = x - t \nabla f(x)
>$$

>**Newton's method:**
>$$
>x^+ = x - t \nabla^2 f(x)^{-1} \nabla f(x)
>$$

Newton's method는 quadratic convergence rate ($$O(\log \log 1/ \epsilon)$$)의 convergence속도를 보이는 장점이 있는 반면to, 아래 두 processby, image당히 큰 computation비용이 발생하는 problem가 있다. 

* Hessian $$\nabla^2 f(x)$$의 computation: Hessian matrix를 computation하고 저장하기 for,서는 $$O(n^2)$$의 메모리를 필요to, 한다. 이는 고difference원의 function를 다루기to, 적절하지 않은 성능이다. (reference: [Hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix#Use_in_optimization) in Wikipedia)
* 방정식 $$\nabla^2 f(x) p = -\nabla f(x)$$의 풀이: 이 방정식을 풀기 for,서는 Hessian $$\nabla^2 f(x)$$to, about, 역matrix을 computationsolution야 한다. (reference: [Computational complexity of Matrix algebra](https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations#Matrix_algebra) in Wikipedia)

Quasi-Newton methodat,는 instead of, $$\nabla^2 f(x)$$를 approximation(approximation)한 $$B$$를 이용한다.
>**Quasi-Newton method:**
>$$
>x^+ = x + tp \\\\
>\text{where } Bp = -\nabla f(x).
>$$

이when, B는 computation하기 쉬워야 하며, also, 방정식 $$Bp = g$$를 풀기to,도 용이solution야 한다. 

## Quasi-Newton Algorithm
Quasi-Newton algorithm은 as follows:.

* Pick initial $$x^0$$ and $$B^0$$
* For $$k = 0, 1, \dots$$
    * Solve $$B^k p^k = - \nabla f(x^k)$$
    * Pick $$t_k$$ and let $$x^{k+1} = x^{k} + t_k p^k$$
    * Update $$B^k$$ to $$B^{k+1}$$
* End for

Optimal pointto, 점진적with, 다가갈 수 있도록 $$B$$를 업데이트 solution가는 것이 이 method의 큰 특징이다. that is,, $$B$$를 through, next step인 $$B^+$$를 구하는 methodabout, 이번 장at, 주to, 논의하게 될 것이다. (**Note:** 편의image $$B^{k+1}, B^k$$and, $$B^+, B$$ 두 가지 표기를 혼용하여 사용하겠다.)
---
layout: post
title: '23-02 Example: linear regression'
chapter: '23'
order: 3
owner: Jinwoo Park
categories:
- chapter23
lang: en
---

Linear regression problem를 as follows: 정by,보겠다.

> $$\min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2,$$
> $$\text{given } y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^{n \times p} \text{ with columns } X_1, \dots, X_p.$$

$$\beta_j,\: j \neq i$$가 고정된 값일when,, 주어진 objective function를 minimization시키는 $$\beta_i$$를 let's find.
($$-i$$는 $$i$$를 제외한 remainder 항을 의미한다. - $$X$$의 case, $$i$$번째 column을 제외한 remainder column.)

$$\begin{align}
0 &= \nabla_i f(\beta)\\\\
&= X_i^T (X\beta - y)\\\\
&= X_i^T (X_i \beta_i + X_{-i} \beta_{-i} - y)\\\\
\Rightarrow\\\\
&\beta_i = \frac{X_i^T (y - X_{-i} \beta_{-i})}{X_i^T X_i}
\end{align}$$

Coordinate descent를 through, $$\beta_i$$ for $$i=1,2,\dots,p,1,2,\dots$$를 iteration하며 업데이트 한다.

## 실험: convergence속도 비교 - GD vs AGD vs CD

아래 그래프는 $$n=100, p=20$$인 linear regression problemabout, coordinate descent, gradient descent, accelerated gradient descent의 convergence속도를 comparing, showing,준다. (가to,axis의 k는 한 step (GD, AGD) or, 한 cycle (CD)을 나타낸다.)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/gd_vs_agd_vs_cd.png" alt="[Fig1] GD vs AGD vs CD [3]">
  <figcaption style="text-align: center;">[Fig1] GD vs AGD vs CD [3]</figcaption>
</p>
</figure>
<br/>

위 result,to, 의하면 coordinate descent는 first-order method의 optimal인 AGD보다도 월등히 좋은 convergence속도를 보인다. 어째서 이런 현image이 발생할 수 있는 것일까? 결론from, 말하자면, coordinate descent는 first-order method보다 더 많은 정보를 활용하므to, AGD를 훌쩍 image회하는 성능을 내는 것이 가능하다. Coordinate descent는 한 cycle 내at, 각 step마다 before, stepat, 갱신된 최신 정보를 이용하기 because,이다. (that is,, CD는 first-order method가 아니다.)

#### Q. 그렇다면 위 실험at, CD의 한 cycle을 GD의 한 stepand, 비교한 것은 공정한 것일까?

**A. 그렇다.** 앞서 소개한 CD의 업데이트 식을 한 step의 시간복잡도가 $$O(n)$$인 형태to, 변형시킬 수 있다. 그렇다면 CDto, about, 한 cycle의 시간복잡도는 $$O(np)$$가 되며 GD의 한 stepand, 같은 시간복잡도를 가지게 된다.

* **Gradient descent update:** $$\beta \leftarrow \beta + tX^T(y-X\beta)$$, $$X\beta$$ operationby, 시간복잡도는 $$O(np)$$ flops가 된다.

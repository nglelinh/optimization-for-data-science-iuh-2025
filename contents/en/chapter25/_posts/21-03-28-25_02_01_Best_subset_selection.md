---
layout: post
title: 25-02-01 Best subset selection
chapter: '25'
order: 8
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

Integer Programming의 대표적인 예시 중 하나인 best subset selection은 $$p$$개의 entry 중to, k개의 entry를 선택하는 problem이다.

## Best subset selection
$$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}$$이고 $$y \in \mathbb{R}^{n}$$일 when, best subset selection problem는 as follows:.

> $$
> \begin{align}
> \min_{\beta} & \quad \frac{1}{2} \parallel y - X\beta \parallel^{2} \\
> \text{subject to } & \quad \parallel \beta \parallel_{0}  \  \leq  k \\
> \end{align}
> $$

이when, $$\parallel \beta \parallel_{0}$$는 $$\beta$$의 nonzero entry의 개수이다.

지금to, 앞 장at,는 이and, 같은 problem를 Lasso problemwith, 정by,서 $$l_1$$ normwith, $$\beta$$를 sparse하게 만들었었다. 이 problem의 case, $$l_0$$ norm을 using,서 0이 아닌 entry 개수를 제약하는 problemto,
정의 되었는데 제약 condition,인 $$\parallel \beta \parallel_{0}  \  \leq  k$$가 non-convex라서 지금to, 배운 convex optimization techniquewith,는 problem를 풀 수 없다.

#### Integer programming formulation
그렇다면 이 problem를 Integer programmingwith, 재정by,보자.

> $$
> \begin{align}
> \min_{\beta, z} & \quad \frac{1}{2} \parallel y - X\beta \parallel^{2} \\
> \text{subject to } & \quad \left\vert  \beta_{i} \right\vert  \leq M_{i} \cdot z_{i} \quad i = 1 \dotsc p \\
> & \quad \sum_{i = 1}^{p} z_{i} \leq k \\
> & \quad z_{ji} \in \lbrace 0, 1 \rbrace \quad i = 1 \dotsc p \\
> \end{align}
> $$

Binary variable $$z_i$$를 introducing,서 $$z_i$$의 sum이 $$k$$보다 작게 만듦with,써 위의 problemand, 동일solution지게 만들었다.  $$M_i$$는 사전to, 알고 있는 $$\left\vert  \beta_{i} \right\vert$$의 image한 값with, $$X$$and, $$y$$를 사전processing,서 computation할 수 있는 값이다.

이제 problem를 Integer Programmingwith, 정의했으므to, 지금from, Integer Programming techniquewith, 풀 수 있다.

## A clever way to get good feasible solutions
problem를 generalizing,서 algorithm을 explaining,보자. Objective function $$g : \mathbb{R}^{p} \to \mathbb{R}$$이 smooth convex이고 $$\nabla g$$가 L-Lipschitz이라고 하자.
>
$$\min_{\beta} g(\beta) \quad \text{subject to} \quad \parallel \beta \parallel_{0} \le k$$

Best subset selection의 case, $$g(\beta) = \frac{1}{2} \parallel X\beta - y \parallel^2_2$$이다.

#### Observation
as follows: 정의된 $$H_k(u)$$ function를 through, $$u \in \mathbb{R}^p$$at, 가장 큰 k개 entry를 구할 수 있다.
>
$$ H_k(u) = \underset{\beta : \parallel \beta_{0} \parallel \le k}{\text{argmin}} \parallel \beta - u \parallel^2_2$$

이when,, $$H_k(u)$$ function는 hard thresholding을 한다. also,, $$u$$를 set $$\beta$$to, projection한 것with, 볼 수도 있다.

#### Discrete first-order algorithm
이제 gradient descentand, function $$H_k(u)$$를 using,서 algorithm을 정by,보자.

1. $$\beta^{(0)}$$with, 시작
2. for $$k = 0, 1, ...$$ <br>
$$\quad \beta^{(i+1)} = H_k \left(\beta^{(i)} - \frac{1}{L} \nabla g(\beta^{(i)})\right)$$<br>
end for<br>

위의 process을 iteration하면 $$\beta^{(i)} \to \bar{\beta}$$to, convergence하게 된다. 이는 위의 minimization problemto, about, local solution이라고 할 수 있다.
>
$$ \bar{\beta} =  H_k \left(\bar{\beta} - \frac{1}{L} \nabla g(\bar{\beta})\right)$$

result,적with, 이 algorithm은 proximal gradient algorithmwith, 볼 수 있다. 왜냐하면 function $$H_k(u)$$가 proximal operator 역할을 하고 있기 because,이다.
## Computational results
#### Mixed integer programming gap
아래 그림at, Subset selection problem의 실험 result,를 let's look at.

왼쪽 그래프at, upper bound는 바to, optimal이 되었지만 lower bound는 천천히 올라오다가 upper boundand, 만나는 지점at,야 optimal임을 알게 된다. 왜냐하면 linear programat,는 solution이 optimal인지 체크할 method이 없으며 upper boundand, lower bound가 같아졌을 when, optimal임을 알 수 있게 된다.
(referenceto, upper boundand, lower bound의 difference를 mixed integer programming gap이라고 한다.)

오른쪽 그림은 동일한 실험 result,를 mixed integer programming gap을 작아지는 모습with, showing,주고 있다. 주황색 그래프는 upper boundand, lower bound의 difference이인 mixed integer programming gap을 representing,며 점점 줄어들고 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_03_subset_results1.png" alt="[Fig1] Dataset n=350, p = 64, k=6 [3]">
  <figcaption style="text-align: center;">$$[Fig1] Dataset n=350, p = 64, k=6 [3]$$</figcaption>
</p>
</figure>
<br>

#### Cold and Warm Starts
다음 그림at, warm start가 cold start보다 전체적with, 성능이 매우 우수함을 showing,주고 있다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_04_subset_results2.png" alt="[Fig2] Cold and Warm Starts [3]">
  <figcaption style="text-align: center;">[Fig2] Cold and Warm Starts [3]</figcaption>
</p>
</figure>
<br>

#### Sparsity Detection
다음 그림at,는 MIP (Mixed Integer Programming)and, Lasso, Step regression, Sparsenet의 sparsity를 비교하고 있다. result,적with, MIP가 가장 sparse한 result,내고 있음을 알 수 있다.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_05_subset_results3.png" alt="[Fig3] Sparsity Detection (synthetic database) [3]">
  <figcaption style="text-align: center;">[Fig3] Sparsity Detection (synthetic database) [3]</figcaption>
</p>
</figure>
<br>

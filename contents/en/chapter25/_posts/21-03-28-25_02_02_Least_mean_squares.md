---
layout: post
title: 25-02-02 Least mean squares
chapter: '25'
order: 9
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

지금to,는 regression problem를 residual의 $$l_2$$ norm이나 $$l_1$$ norm을 minimization하는 problemto, 풀었었다. 이들 method보다 좀 더 robust한 method이 있을까?

Residual의 median을 minimization하도록 regression을 할 case, 좀 더 robust한 regression을 할 수 있다. 이를 **Least Median of Squares**라고 하는데 데이터의 50% 정도가 corrupt되어도 estimator는 corrupt되지 않을 만큼 robust하다. but, 이 problem는 NP-Hard problem이기도 하다!

이 절at,는 Least Median of Squares problem를 일반화한 **Least Quantile of Square**problem를 Integer programmingwith, 어떻게 푸는지 소개한다.
## Least mean squares
$$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}$$이고 $$y \in \mathbb{R}^{n}$$이라고 하자. and, $$\beta \in \mathbb{R}^{p} $$일 when, $$r : = y - X\beta $$이라고 하자.

#### Observe
* Least squares (LS) : $$\beta_{LS} : = \underset{\beta}{\text{argmin}} \sum_{i} r^2_i$$
* Least absolute deviation (LAD) : $$\beta_{LAD} : = \underset{\beta}{\text{argmin}} \sum_{i} \lvert r_{i} \rvert$$
#### Least Median of Squares (LMS)
>$$\beta_{LMS} : = \underset{\beta}{\text{argmin}} (\text{median} \lvert r_{i} \rvert )$$

## Least quantile regression
Least Median of Squares problem를 일반화한 Least Quantile of Squareproblem는 as follows: 정의할 수 있다. 여기서 $$r_{q}$$는 $$q$$번째 ordered absolute residual이다.
#### Least Quantile of Squares (LQS)
>$$\beta_{LQS} : = \underset{\beta}{\text{argmin}} (\lvert r_{(q)} \rvert ), \quad 1 \le q \le n, \quad \lvert r_{1} \rvert \le \lvert r_{2} \rvert \le \cdots \le \lvert r_{n} \rvert$$

#### Key step in the formulation
이제 Least Quantile of Squareproblem를 Integer Programmingwith, 재정by,보자. 이when,, $$r$$의 각 entry $$i$$about, 다음and, 같은 binary variable을 사용한다.

>$$ \lvert r_{i} \rvert \le \lvert r_{(q)} \rvert$ or $\lvert r_{i} \rvert \ge \lvert r_{(q)} \rvert $$

#### Integer programming formulation
$$\bar{\mu_{i}}$$and, $$\mu_{i}$$은 thresholdto, 각각의 개수는 $$k$$개, $$n-k$$개이다.

> $$
> \begin{align}
>   \min_{\beta, \mu, \bar{\mu}, z, \gamma} & \quad {\gamma} \\
>   \text{subject to} & \quad  \gamma \le \lvert r_{i} \rvert + \bar{\mu_{i}}, \quad i = 1, ..., n \\
>   & \quad  \gamma \le \lvert r_{i} \rvert -  \mu_{i}, \quad i = 1, ..., n \\
>   & \quad \bar{\mu_{i}} \le M \cdot z_{i}, \quad i = 1, ..., n \\
>   & \quad \mu_{i} \le M \cdot (1-z_{i}), \quad i = 1, ..., n \\
>   & \quad \sum^{p}_{i=1} z_{i} = q \\
>   & \quad \mu_{i}, \bar{\mu_{i}} \ge 0, \quad i = 1, ..., n \\
>   & \quad z_{i} \in \{0, 1\},  \quad i = 1, ..., n \\
> \end{align}
> $$

이 problemat, 첫번째and, 두번쨰 constraint을 보면 residual의 절대값 $$\lvert r_{i} \rvert$$이 포함되어 있어서 convex relaxationwith, 풀 수가 없다. therefore,, 첫번째and, 두번쨰 constraint을 convex functionwith, converting, 주어야 한다.


## First-order algorithm
$$\lvert r_{i} \rvert$$는 다음and, 같은 형태to, convex function $$H_{q}(\beta)$$to, 재정의할 수 있다.
>
$$ \lvert r_{q} \rvert = \lvert y_{(q)} - x^{T}_{(q)} \beta \rvert = H_{q}(\beta) - H_{q+1}(\beta)$$

이when, $$H_{q}(\beta)$$는 as follows: 정의된다.

> $$
> \begin{align}
> H_{q}(\beta) = \sum^{n}_{i=q} \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert  = &
> \max_{w} \sum^{n}_{i=1} w_i \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert \\
> & \text{subject to} \sum^{n}_{i=1}  w_i  = n − q + 1 \\
> &0 \le w_i \le 1, i = 1, ..., n \\
> \end{align}
> $$

$$H_{q}(\beta)$$는 앞서 정의된 $$\lvert r_{i} \rvert$$을 작은것from, 큰 순with, 나열할 when,, $$q$$번째 이image의 모든 residual의 sum이다. therefore,, $$q$$번째 이image의 residual의 sumat, $$q+1$$번째 이image의 residual의 sum을 빼면 $$q$$번째의 residual 된다는 것을 알 수 있다.

Subgradient algorithmwith, $$H_{q}(\beta) - H_{q+1}(\beta)$$의 local minimum을 구할 수 있다.

* For detailed information, see 논문 [LEAST QUANTILE REGRESSION VIA MODERN OPTIMIZATION](https://arxiv.org/pdf/1310.8625.pdf) see
## Computational results
위의 논문at,  Least Quantile of Squareproblem를 실험한 result,는 다음 그래프at, 볼 수 있다.

#### Mixed integer programming gap
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_06_LQS_results1.png" alt="[Fig1] Mixed integer programming gap [3]">
  <figcaption style="text-align: center;">[Fig1] Mixed integer programming gap [3]</figcaption>
</p>
</figure>
<br>

#### Cold vs Warm Starts
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_07_LQS_results2.png" alt="[Fig2] Cold vs Warm Starts [3]">
  <figcaption style="text-align: center;">[Fig2] Cold vs Warm Starts [3]</figcaption>
</p>
</figure>
<br>

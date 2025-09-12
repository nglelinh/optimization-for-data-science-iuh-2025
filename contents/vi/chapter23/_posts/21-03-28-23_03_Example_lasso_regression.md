---
layout: post
title: '23-03 Example: lasso regression'
chapter: '23'
order: 4
owner: YoungJae Choung
categories:
- chapter23
lang: vi
---


Lasso regression problem를 아래and, 같이 nonsmooth part가 분리되어있는 objective function의 형태to, 정by,보겠다.

> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

**Note:**
$$\|\beta\|_1 = \sum_{i=1}^p | \beta_i |$$

$$\beta_j, j \neq i$$ 가 고정된 값일when,, 주어진 objective function를 minimization시키는 $$\beta_i$$를 let's find.

$$\begin{align}
&0 = \nabla_i f(\beta) = X_i^T X_i \beta_i + X_i^T(X_{-i} \beta_{-i} - y) + \lambda s_i,\\\\
&\text{where } s_i \in \partial |\beta_i|
\Rightarrow 
\beta_i = S_{\lambda / \|X_i\|_2^2} \big( \frac{X_i^T(y-X_{-i} \beta_{-i})}{X_i^TX_i} \big)
\end{align}$$

Solution은 thresholding level이 $$\lambda / \|X_i\|_2^2$$인 soft-thresholding functionand,도 같다. Coordinate descent를 through, $$\beta_i$$ for $$i=1,2,\dots,p,1,2,\dots$$를 iteration하며 업데이트 한다.

## 실험: convergence속도 비교 - PG vs AGD vs CD

아래 그래프는 $$n=100, p=20$$인 lasso regression problemabout, proximal gradient descent, accelerated gradient descent, coordinate descent의 convergence속도를 comparing, showing,준다. (가to,axis의 k는 한 step (PD, AGD) or, 한 cycle (CD)을 나타낸다.)

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/pd_vs_agd_vs_cd.png" alt="[Fig1] PD vs AGD vs CD [3]">
  <figcaption style="text-align: center;">[Fig1] PD vs AGD vs CD [3]</figcaption>
</p>
</figure>
<br><br>

[Linear regression의 예시]({% multilang_post_url contents/chapter23/21-03-28-23_02_Example_linear_regression %})at,and, 마찬가지to, lasso regression problemat,도 coordinate descent는 월등한 convergence속도를 보인다. (First-order method보다 더 많은 정보를 활용한다.)

* **Note:** 위 실험at,의 모든 methods는 각 iteration당 $$O(np)$$ flops의 시간복잡도를 보인다.

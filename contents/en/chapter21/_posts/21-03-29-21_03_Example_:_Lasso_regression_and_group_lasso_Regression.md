---
layout: post
title: 21-03 Example - Lasso regression and group lasso Regression
chapter: '21'
order: 4
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

## Lasso regression
Lasso regression problem를 ADMMwith, solution결solution본다.

$$y\in \mathbb{R}^{n}, X\in \mathbb{R}^{n\times p}$$ 일when, lasso problem는 아래and, 같다.
>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda||\beta||_{1}
>\end{align}
>$$

before,의 여러 장at,, 우리는 lasso problem를 여러가지 methodwith, solution결solution보았다. 대표적with,는 [proximal gradient descent(ISTA)]({% multilang_post_url contents/chapter09/20-01-08-09_01_proximal_gradient_descent %}), [accelerated proximal gradient descent(FISTA)]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}), [barrier method]({% multilang_post_url contents/chapter15/21-03-28-15_barrier_method %}), [primal-dual interior-point method]({% multilang_post_url contents/chapter17/21-05-01-17_primal_dual_interior_point_method %}) 등이 있다. 

ADMMat,는 dual 식을 유도하는 것and, 동일하게, 어떤 식with, 보조 variable(auxiliary variable)을 설정하는가according to, algorithm의 성능이 달라진다. 많은 auxiliary variable의 설정 method 중 아래의 형태가 가장 effect,적인 형태 중 하나to, informing,져 있다.
>$$
>\begin{align}
>&\min_{\beta, \alpha} &&||y-X\beta||^{2}_{2}+\lambda||\alpha||_{1}\\\\
>&\text{subject to} &&\beta-\alpha= 0.
>\end{align}
>$$

이 식about, ADMM update는 아래and, 같이 유도된다. $$\beta$$to, about, 식은 $$\beta$$가 2difference식이므to, 미분을 through, 최솟값을 구할 수 있고, $$\alpha$$to, about, 식은 앞서 [07장(07-03-04)]({% multilang_post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %})at, 다루었던 problemand, 같이 $$\beta^{+}+w$$의 soft-thresholding의 형태to, solution가 됨이 informing,져 있다.
>$$
>\begin{align}
>\beta^{+} &= \underset{\beta}{\operatorname{argmin}}\frac{1}{2}||y-X\beta||^{2}_{2}+\frac{\rho}{2}||\beta-\alpha+w||^{2}_{2}\\\\
>&= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+} &= \underset{\alpha}{\operatorname{argmin}}\lambda||\alpha||_{1}+\frac{\rho}{2}||\beta^{+}-\alpha+w||^{2}_{2}\\\\
>&= S_{\frac{\lambda}{\rho}}(\beta^{+}+w)\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

이 result,는 아래and, 같은 특징들을 갖는다.

* matrix $$X^{T}X+\rho I$$는 $$\rho>0$$이므to, $$X$$to, relationship,없이 always, invertible하다.
* if, factorization(대표적with, Cholesky factorization)을 $$O(\rho^{3})$$ flops 안to, computation하면, $$\beta$$to, about, update는 $$O(\rho^{2})$$ flops가 걸린다.
* $$\alpha$$ update는 soft-thersholding operator $$S_{t}$$를 적용하는 것이 되며, $$S_{t}$$는 [07-03-04]({% multilang_post_url contents/chapter07/21-03-25-07_03_04_example_soft-thresholding %})의 내용and, 동일하다.
* ADMM 스텝은 ridge regression 계수들을 매번 soft-thresholding하는 것and, "거의" 동일하다.
* $$\rho$$를 다르게 주면 다른 result,가 나온다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/lasso.png" alt="[Fig 1] Comparison of various algorithms for lasso regression (50 instances with n = 100, p = 20) [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Comparison of various algorithms for lasso regression (50 instances with n = 100, p = 20) [3]</figcaption>
</p>
</figure>


[Fig 1]은 lasso regression problemto, about, 다양한 algorithm들의 convergence을 비교한 것이다. 모든 algorithm들은 iteration마다 동일한 computation복잡도를 가지고 있다. 그래프의 convergence 속도at, 볼 수 있다시피, ADMM은 proximal gradient descent(검정)and, 비슷한 convergence 속도를 가진다. Accelerated proximal gradient descent(빨강)는 "Nestrov ripples"를 가지지만 조금 더 빠른 convergence 속도를 보인다. also,  ADMM은 $$\rho$$ 값according to, 다른 convergence 속도를 보인다는 특성도 확인할 수 있다. 후to, [23장]({% multilang_post_url contents/chapter23/21-03-28-23_Coordinate_Descent %})at, 논하게 될 Coordinate descent(초록)의 case,는 problemat, 더 많은 정보들을 사용하고, therefore, 다른 method들to, 비solution 빠른 convergence 속도를 가진다. Coordinate descent의 단점은 problem하기 위한 condition,들이 존재한다는 것이다.
$$\rho$$값을 너무 크게 설정하면, objective functionat, $$f+g$$를 minimization 하는 비중이 작고, $$\rho$$값을 너무 작게 설정하면, feasibility가 떨어진다. therefore, 적절한 $$\rho$$값의 설정이 중요하다. For detailed information, see [21장 reference 논문]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}) 중 [BPCPE]at, 논하고 있다.

## Group lasso regression
위and, 동일하게  Group lasso regression problem also, ADMMwith, solution결하는 것about, 살펴보고자 한다. Group lasso regression의 problem정의는 아래and, 같다. $$y\in \mathbb{R}^{n}, X\in \mathbb{R}^{n \times p}$$일when,,

>$$
>\begin{align}
>\min_{\beta}\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\beta_{(g)}||_{2}.
>\end{align}
>$$

Lasso regressionand, 동일하게 problem를 다시 정리할 수 있다.
>$$
>\begin{align}
>&\min_{\beta,\alpha} &&\frac{1}{2}||y-X\beta||^{2}_{2}+\lambda\sum^{G}_{g=1} c_{g}||\beta_{(g)}||_{2}\\\\
>&\text{subject to} &&\beta-\alpha=0.
>\end{align}
>$$

ADMM step은 as follows:.
>$$
>\begin{align}
>\beta^{+} &= (X^{T}X+\rho I)^{-1}(X^{T}y+\rho (\alpha-w))\\\\
>\alpha^{+} &= R_{c_{g}\frac{\lambda}{\rho}}(\beta^{+}_{(g)}+w_{(g)})\qquad \text{g = 1,...G}\\\\
>w^{+} &=w+\beta^{+}-\alpha^{+}
>\end{align}
>$$

이 result,는 아래and, 같은 특징들을 갖는다.

* matrix $$X^{T}X+\rho I$$는 $$\rho>0$$이므to, $$X$$to, relationship,없이 always, invertible하다.
* if, factorization(대표적with, Cholesky factorization)을 $$O(\rho^{3})$$ flops 안to, computation하면, $$\beta$$to, about, update는 $$O(\rho^{2})$$ flops가 걸린다.
* $$\alpha$$ update는 group soft-thresholding operator $$R_{t}$$를 적용하는 것이 되며, $$R_{t}$$는 아래and, 같이 정의된다.

>\begin{align}
>R_{t}(x) = (1-\frac{x}{\lVert x \rVert_{2}})_{+}x
>\end{align}


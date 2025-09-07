---
layout: post
title: '23-04 Example: Pathwise coordinate descent for lasso'
chapter: '23'
order: 5
owner: YoungJae Choung
categories:
- chapter23
lang: en
---

In this section, Pathwise coordinate descent for lassoto, about, 개요를 간단히 소개하도록 한다 [[Friedman et al. (2007)](https://arxiv.org/pdf/0708.1485.pdf)] [[Friedman et al. (2009)](https://www.jstatsoft.org/article/view/v033i01/v33i01.pdf)]. 

>**Lasso regression problem:**
> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

[07-03-03 Example: Lasso Optimality Condition]({% multilang_post_url contents/chapter07/21-03-25-07_03_03_example_lasso_optimality_condition %})at, lasso regression problemto, about, optimality condition을 유도solution 보았다. 위 problemto, about, optimal solution는 다음의 condition,을 만족한다.

>
> $$
> \begin{align}
> X_1^T(y-X\beta) &= \lambda v_1\\
> X_2^T(y-X\beta) &= \lambda v_2\\
> \dots\\
> X_p^T(y-X\beta) &= \lambda v_p
> \end{align}
> $$

**Note:**
$$X_i,i \in \{ 1,2,…,p \}$$는 주어진 matrix $$X$$의 $$i$$번째 열(column) 데이터를 의미한다.

여기서 $$v=(v_1,v_2,\dots,v_p)$$는 $$\beta=(\beta_1,\beta_2,\dots,\beta_p )$$to, about, subgradient다. 
>
$$
v_i, i \in \{1,2,\dots,p \} = 
\begin{cases}
\{ 1 \}  &\text{if $\beta_i > 0$} \\
\{-1 \}  &\text{if $\beta_i < 0$} \\
[-1,1]   &\text{if $\beta_i = 0$}
\end{cases}
$$

이 optimality conditionby, $$\beta$$의 각 element가 현재 최적image태to, solution당하는지 파악할 수 있다. Coordinate descent algorithm을 이용하면 아직 최적image태to, 도달하지 못한 element만을 업데이트하는 방식with, 좀 더 효율적with, lasso problem를 푸는 것이 가능solution진다. also, $$\lambda$$의 값이 클수록 lasso regression problemat, coordinate descent algorithm이 더 빨리 동작하는 경향성을 utilizing, $$\lambda$$를 점점 reducing,가는 방식(warm start)with, solutionto, 더욱 빠르게 접근한다.

## Algorithm

### Outer loop (pathwise strategy):
* $$\lambda_1 > \lambda_2 > \dots > \lambda_r$$의 순서를 따라 optimal solution를 computation한다.
* Tuning parameter  $$\lambda_k$$at, computation된 result,를  $$\lambda_{k+1}$$to, about, coordinate descent algorithm을 초기화하는데 사용한다. (warm start)

### Inner loop (active set strategy):
* 하나 or, 적은 수의 coordinate cycle을 시행한다. and, 0이 아닌 $$\beta$$의 element를 active set $$A$$to, 기록한다.
* $$A$$to, 기록된 element들about,서만 convergence할 when,to, coordinate cycle을 시행한다.
* $$\beta$$의 모든 element들about, optimality condition을 확인한다. condition,을 만족하지 않는 element가 있으면 $$A$$to, 추가하고 step 1with, 다시 돌아간다.

## Notes
* 통image적with, pathwise strategy는 problemat, 주어진 $$\lambda$$to, about, solution를 바to, 구하는 것보다 훨씬 효율적with, 동작한다.
* Active set strategy는 sparsityabout, 이점이 있다. 이 because of, coordinate descent는 ridge regression보다 lasso regressionat, 훨씬 더 빠르게 동작한다. (reference: [ridge regressionand, lasso regression의 경향성 분석](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/))
* Pathwise coordinate descent for lasso는 lasso regression problemabout, 가장 빠르다고 informing,진 다른 algorithm들to, 비견될만큼 빠르게 동작한다.
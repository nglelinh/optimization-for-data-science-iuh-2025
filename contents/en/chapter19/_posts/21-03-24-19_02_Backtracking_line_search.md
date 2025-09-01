---
layout: post
title: 19-02 Backtracking line search
chapter: '19'
order: 6
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

**Proximal newton method**는 newton's methodand, 같이 pure step size $$t_k=1, k=1,2,3, \cdots$$인 case,to, convergence하지 않을 수 있다. therefore,, backtracking line search를 through, step size를 optimizesolution야 한다.

## Backtracking line search algorithm

1. 파라미터를 초기화한다. ($$0 \lt \alpha \le 1/2, 0 \lt \beta \lt 1$$)
2. 각 iterationat, $$v = \text{prox}_{H} ( x - H^{-1} \nabla g (x) ) - x$$to,  Proximal newton direction을 computation한다.
3. $$t=1$$to, 초기화 한다.
4. $$f(x + tv) \gt f(x) + \alpha t \nabla g(x)^T v + \alpha (h(x + tv) - h(x))$$ condition,을 만족하면 $$t=\beta t$$to, 줄인다. 이 condition,이 만족되는 during, step4를 iteration한다. ($$f = g + h$$)
5. Proximal newton update $$x^+ = x + tv$$를 실행한다.
6. 종료 condition,을 만족하지 않으면 step2to, 간다.

직관적with, $$x$$at, function $$f$$의 선형 approximation를 $$\alpha$$배 내to, 있는 positionto, direction $$v$$를 따라 이동하도록 step size $$t$$를 찾는다. and,, $$f$$at, $$h$$ 파트는 미분이 되지 않기 because of, discrete derivative $$h(x + tv) - h(x)$$를 구했다.

## Efficiency of algorithm
Backtracking line search를 수행하기 위한 method들이 많이 있으며 여기서는 그 중 한 method을 소개했다. 

이 method의 case, $$v$$를 computation할 when, prox operator를 한번만 computation한다. Proximal gradient descent의 case, inner loopat, prox operator의 computation을 iterationsolution야 했는데 이 점and, 확연히 구분되는 특징이다. therefore,, 이 method은 prox operator의 computation이 복잡할 case, 매우 효율적with, backtracking line search를 할 수 있다.

#### [reference] Method 별  backtracking line search
* Gradient descent [06-02-02 Backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %})
* Proximal gradient descent [09-02 Convergence analysis]({% multilang_post_url contents/chapter09/20-01-08-09_02_convergence_analysis %})
* Newton's method [14-04 Backtracking line search]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %})

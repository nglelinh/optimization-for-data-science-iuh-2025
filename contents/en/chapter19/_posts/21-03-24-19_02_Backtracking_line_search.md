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

**Proximal newton method** may not converge in cases with pure step size $$t_k=1, k=1,2,3, \cdots$$ like newton's method. Therefore, we need to optimize the step size through backtracking line search.

## Backtracking line search algorithm

1. Initialize parameters. ($$0 \lt \alpha \le 1/2, 0 \lt \beta \lt 1$$)
2. At each iteration, compute the Proximal newton direction as $$v = \text{prox}_{H} ( x - H^{-1} \nabla g (x) ) - x$$.
3. Initialize $$t=1$$.
4. If the condition $$f(x + tv) \gt f(x) + \alpha t \nabla g(x)^T v + \alpha (h(x + tv) - h(x))$$ is satisfied, reduce $$t=\beta t$$. Iterate step 4 while this condition is satisfied. ($$f = g + h$$)
5. Execute the Proximal newton update $$x^+ = x + tv$$.
6. 종료 condition,을 만족하지 않으면 step2to, 간다.

직관적with, $$x$$at, function $$f$$의 선형 approximation를 $$\alpha$$배 내to, 있는 positionto, direction $$v$$를 따라 이동하도록 step size $$t$$를 찾는다. and,, $$f$$at, $$h$$ 파트는 미분이 되지 않기 because of, discrete derivative $$h(x + tv) - h(x)$$를 구했다.

## Efficiency of algorithm
Backtracking line search를 수행하기 위한 method들이 많이 있으며 여기서는 그 중 한 method을 소개했다. 

이 method의 case, $$v$$를 computation할 when, prox operator를 한번만 computation한다. Proximal gradient descent의 case, inner loopat, prox operator의 computation을 iterationsolution야 했는데 이 점and, 확연히 구분되는 특징이다. therefore,, 이 method은 prox operator의 computation이 복잡할 case, 매우 효율적with, backtracking line search를 할 수 있다.

### [reference] Method 별  backtracking line search
* Gradient descent [06-02-02 Backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %})
* Proximal gradient descent [09-02 Convergence analysis]({% multilang_post_url contents/chapter09/20-01-08-09_02_convergence_analysis %})
* Newton's method [14-04 Backtracking line search]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %})

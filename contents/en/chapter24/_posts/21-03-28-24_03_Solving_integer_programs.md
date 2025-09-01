---
layout: post
title: 24-03 Solving integer programs
chapter: '24'
order: 4
owner: YoungJae Choung
categories:
- chapter24
lang: en
---

Integer programwith, 수식을 변형한 뒤, problem를 solution결하려면 relaxationand, 같은 technique이 필요하다. integer programsat, 나타나는 제약 사항 및 problemabout, 어떤 접근을 하는 지 let's examine.

## Hardness of integer programs
Integer program problem를 푸는 것은 convex optimization problem를 푸는 것보다 훨씬 어렵다. 일반적인 Integer programming은 풀 수 있는 가능성 조difference도 모르면서 최소 polynomial time이 걸리는 [NP-hard](https://en.wikipedia.org/wiki/NP-hardness) 이기 because,이다. 이 when,, integer constraintto, about, 제약을 없앰with,써 convex relaxation을 하면, optimal valueto, 다가가는 lower bound를 구할 수 있다.<br><br>
Convex relaxation은 using, problem를 풀면 다음and, 같은 한계가 발생할 수 있다.


 * Feasible integer solution을 구하는 것이 어렵게 될 수 있다.
 * Relaxation condition,at, obtaining,진 optimal solution이 integer programwith, obtaining,지는 optimal solutionand, distance가 있을 수 있다.
 * approximation(Rounding)를 했을 when,의 값이 optimal 값and, 다를 수 있다.


## Algorithmic template for solving integer programs
$$X$$가 convex 이고 integrality constraints를 포함할 when,, integer program은 as follows:.

> $$ z : = \min_{x \in X} f(x) $$

Convex optimizationand, 다르게 feasible point $$x* \in X$$가 optimal 이라는 것을 입증하는 직접적인 "optimality conditions"는 존재하지 않는다. instead,, lower bound $$ \underline{z} \leq z$$, and, upper bound $$ \bar{z} \geq z$$ 를 finding,가면서 $$\underline{z} = \bar{z}$$ to, 가까워지도록 optimal의 approximation치를 찾는 method을 사용 할 수 있다.

#### Algorithmic template
Upper bounds의 감소 시퀀스를 관찰하면,
> $$\bar{z_1} \geq \bar{z_2} \geq \dotsc \bar{z_s} \geq z$$

lower bounds의 증가 시퀀스를 관찰하면,
> $$\underline{z_1} \leq \underline{z_2} \leq \dotsc \underline{z_t} \leq z $$

임의의 $$\epsilon > 0$$about, $$\bar{z_s} - \underline{z_t} \leq \epsilon $$ 이 되는 범위at, $$z$$의 값이 정solution진다.

#### Primal bounds
앞선 $$z$$ 공식according to, 임의의 feasible $$x \in X$$at, always, $$f(x) \geq z$$가 성립하고, 이 when,, $$f(x)$$는 upper bound 이다. but, always, feasible $$x$$를 찾을 수는 없기 because of,, $$x$$값이 solution당 셋to, 포함 된다면 problem가 쉽게 풀리지만, 그렇지 않을 수도 있다.


#### Dual bounds
usually, lower bounds to,도 불리며, relaxation을 through,서 그 값을 찾게 된다. 다음 장at, 자세한 설명을 덧붙인다.

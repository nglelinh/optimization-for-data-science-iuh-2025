---
layout: post
title: 25-01-04 Branch and cut algorithm
chapter: '25'
order: 6
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

1990년 CMU의 Sebastian Ceria는 cutting plane method를 branch and bound algorithm을 using,서 성공적with, 구현을 하였으며 이를 branch and cut이라고 한다. 이when,from, cutting plane은 image용 optimization solver의 핵심적인 컴포넌트가 되었다.

## Branch and cut algorithm
다음and, 같은 integer programming problem가 있다고 하자. 이when, $$f : \mathbb{R}^{n} \to \mathbb{R}$$이고  $$C \subseteq \mathbb{R}^{n}$$는 convex이며 $$J \subseteq {1, ..., n}$$이다.

> $$
> \begin{align}
>           \min_{x} & \quad {f(x)} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

#### Branch and cut algorithm
algorithmat, Convex Problem은 CPto, Integer Program은 IPto, 표기한다.

1. 다음 convex relaxation problem를 푼다.

> $$
> \begin{align}
>           \min_{x} & \quad {f(x)} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

2. (CR) infeasible $$\Rightarrow$$ (IP) infeasible <br>
3. (CR)의 solution $$x^{\star}$$이 (IP) feasible $$\Rightarrow$$ $$x^{\star}$$는 (IP)의 solution <br>
4. (CR)의 solution $$x^{\star}$$이 (IP) infeasible하면 다음 두 가지 중to, 선택 <br>
$$\quad$$4.1 cut을 추가하고 step 1to, 간다. <br>
$$\quad$$4.2 branchsolution서 iteration적with, subproblem을 푼다. <br>

Branch and cut algorithm은 branch and bound and, cutting plane method를 결sum한 algorithmwith,서, step 4at, branch-and-bound를 할지, cut을 할지 선택할 수 있다. 

## Integer programming technology
Gurobi, CPLEX, FICOand, 같은 state-of-the-art solver들은 매우 효율적인 simplex, interior-point method 등의 algorithm 구현을 포함하고 있다. particularly,, mixed integer optimization의 case, 대부분의 solver들은 branch and cut algorithm을 사용하고 있으며 이들은 convex relaxationand, warm start의 이점을 많이 활용하고 있다.

약 30년 전to, 비하면 Integer programming의 성능 향image은 매우 비약적이다. therefore,, 그during, 풀지 못했던  실생활의 많은 problem들이 최근to, Integer programming을 through, solution결되고 있으며 computing power가 향image됨according to, 더욱 적극적with, 활용될 전망이다.

* Algorithmat,의 속도 향image 1990-2016 : over $$500,000$$
* Hardwareat,의 속도 향image 1990-2016 : over $$500,000$$
* Total speedup over $$250$$ billion = $$2:5 \cdot 10^{11}$$

---
layout: post
title: 24-05 Branch and bound algorithm (B&B)
chapter: '24'
order: 6
owner: YoungJae Choung
categories:
- chapter24
lang: en
---

Branch and bound algorithmand, Convex relaxation 을 through, Integer program을 풀어가는 method을 let's find out.

## Definition and properties
Branch and bound algorithm은 integer program을 푸는 가장 보편적인 method이다. 주to, divide and conquer 방식with, 원래의 problem를 여러 개의 작은 problem(sub-problems)to, 쪼개서 정답to, 접근solution나가는 방식이다. 

Constraint set $$X = X_{1} \cup X_{2} \cup \dotsc \cup X_{k}$$ 가 각각의 $$X_{i}$$to, 이루어진 partition의 union일 when,,
> $$ \min_{x \in X} f(x) = \min_{i = 1, \dotsc , k} \lbrace \min_{x \in X_{i}} f(x) \rbrace .$$

영역을 분할하여 minimum을 finding,나가면서 최적의 solution를 구할 수 있다.

Sub-problem의 임의의 feasible solution을 upper bound $$u(X)$$to, 정할 수 있다. lower bound를 얻기 for,서, 각각의 sub-problemat,의 lower bound $$l(X_{i})$$ 를 구한다. and, 나서 if, $$l(X_{i}) \geq u(X)$$ 일 case,to, 이 부분to, solution당하는 sub-problem $$\min_{x \in X_{i}} f(x)$$ 을 제외한다. 
 
Integer Programming problem (IP) problem를 as follows: 정의한다.

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } && x \in C \\\\
> &&&x_j \in \mathbb{Z}, \quad j \in J \\\\
> \end{align}$$
> $$\begin{align}
> \text{where f is convex } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
\quad \text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
> \end{align}
> $$

and, Convex Relaxation (CR) problem가 다음and, 같을 when,,

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } &&x \in C \\\\
> \end{align}$$
> $$\begin{align}
> \text{where f is convex } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \in \mathbb{R}^n 
\quad \text{and} \quad J \in \lbrace 1 \dotsc n \rbrace \\
> \end{align}
> $$

recursive하게 problem를 풀어간다.

* Constraint set이 trivial 하다면, (CR) problem를 푼다. if, solution이 현재 upper bound 보다 적다면, upper bound를 업데이트 한다. Stop.
    * (CR) 이 infeasible 하다면, (IP) 역시 infeasible 하다. Stop.
    * (CR) at,의 solution $$x^{\star}$$가 (IP) at,도 feasible 하다면, $$x^{\star}$$는 solution가 된다. Stop.
* problemat,의 lower bound를 찾는다.
    * (CR) at,의 solution $$x^{\star}$$가 (IP) at,는 infeasible 하다면, (IP) at,의 lower bound 를 갱신한다.
* Lower bound가 현재의 upper bound보다 크다면, Stop.
* Constraint set을 쪼갠다, and, 각각의 sub-problem을 recursive하게 푼다.


## After branching

* Branching after,to, 각각의 subproblem을 푼다.
* if, subproblem의 lower bound가 현재의 upper bound보다 크다면, 그 하부의 subproblem을 고려할 필요가 없다.
* Lower bound를 computation하는 가장 확실한 method은 convex relaxation을 through, 구하는 것이지만, 다른 method들 (e.g., Lagrangian relaxation) also, 사용되기도 한다.

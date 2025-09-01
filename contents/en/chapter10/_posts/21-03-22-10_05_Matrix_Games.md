---
layout: post
title: 10-05 Matrix Games
chapter: '10'
order: 6
owner: Wontak Ryu
categories:
- chapter10
lang: en
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In this chapter, we examine mixed strategies for matrix games, which is an example of primal LP and dual LP in game theory. The setup assumes two players, J and R, and a payout matrix $$P$$.

## Game Setup

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter10/matrix_game.png" alt="Line Segment" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Game Setup[3]</figcaption>
</p>
</figure>

The payout matrix is the amount of reward J must give to R when J chooses strategy $$i$$ (row) and R chooses strategy $$j$$ (column) ($$P_{ij}$$). However, if this value is positive, J gives R a reward equal to the size of the corresponding matrix, and if negative, R gives J a reward equal to the size of the corresponding matrix. 

This setting is also called a zero-sum setting, where if the reward R will receive or must pay is $$r_{R}$$ and J's reward is $$r_{J}$$, then in each game the result of the rewards is $$r_{R} = - r_{J}$$, and the total sum of the two rewards is always 0.  

Also, we assume that both players use mixed strategies. Mixed strategies is the assumption that each player's choice follows a specific probability distribution (or is sampled from a specific probability distribution). 

>$$
>\begin{align}
>x : P(\text{J chooses i}) = x_{i}, \qquad i=1,...m\\\\
>y : P(\text{R chooses j}) = y_{j}, \qquad j=1,...n.\\\\
>\end{align}
>$$

If they know each other's mixed strategy, i.e., probability distribution, each player can calculate the payout they expect to get, i.e., the expected payout.

>$$
>\begin{align}
>\sum_{i=1}^{m}\sum_{j=1}^{n}x_{i}y_{j}P_{ij} = x^{T}Py.\\\\
>\end{align}
>$$

Considering that the sign of the payout matrix is defined as the amount J gives to R, J will try to minimize this expected payout because J wants to give as little as possible to R, and R will try to maximize this expected payout because R wants to receive as much as possible from J.

이제 두 player의 입장에서 각자가 상대의 mixed strategy를 고려하여, 이 expected payout을 최대화(R의 입장) 혹은 최소화(J의 입장)하려는 관점을 살펴보고, 서로가 서로를 optimal하게 행동하는 전제하에, 두 입장에서 유도되는 optimal strategy를 구하고, 결과적으론 Von Neumman's minimax theorem에 의해 두 결과가 같다는 것을 확인할 것이다.

## Minimizing Expected Payout : J's Perspective
먼저 R이 J의 strategy $$x$$를 알고 있다고 가정하자. R은 expected payout $$x^{T}Py$$를 maximize하고자 할 것이다. 

>$$
>\begin{align}
>\max\{x^{T}Py : y\geq0, 1^{T}y = 1\} = \max_{i=1,...n}(P^{T}x)_{i}.\\\\
>\end{align}
>$$

이때 R은 식의 내용처럼 $$(P^{T}x)_{i}$$ 중 가장 큰 값을 갖는 i(row index)를 찾게되고, 이 i에 대응되는 $$y_{i}$$를 1로 가지고 나머지의 row index에 대해선 0을 가지는 strategy가 R에게 있어서 expected payout을 maximize하는 strategy일 것이다.

R이 위처럼 최적으로 행동할 것을 알고 있을 때, J의 최적의 strategy는 밑의 식을 만족하는 distribution $$x$$일 것이다.

>$$
>\begin{align}
>& \min_{x}
>& &\max_{i=1,...n} (P^{T}x)_{i}\\\\
>& \text{subject to}
>& & x\geq 0, 1^{T}x =1.\\\\
>\end{align}
>$$

Convex function의 maximization 또한 convex function이 된다.  이를 첫 번째 관점의 문제 정의라고 칭할 것이다. 또한 이 최적화 문제의 해를 optimal expected payout $$f^{*}_{1}$$이라고 정하자. 또 하나 유념할 점은 게임참가자, 즉 player들이 모두 최적으로 행동한다는 가정이 기본적인 형태의 게임이론 formulation에서 가정이 된다.

## Maximizing Expected Payout : R's Perspective
두 번째 관점으로 J가 R의 strategy $$y$$를 알고 있다고 가정하자. J는 expected payout을 minimize하고자 할 것이다.

>$$
>\begin{align}
>\min \{x^{T}Py : x\geq0, 1^{T}x = 1\} = \min_{j=1,...n}(Py)_{j}.\\\\
>\end{align}
>$$

같은 논리로, J가 위처럼 최적으로 행동할 것을 알고 있을 때 R의 최적의 strategy는 밑의 식을 만족하는 distribution $$y$$이다.

>$$
>\begin{align}
>& \max_{y}  
>& & \min_{j=1,...m} (Py)_{j}\\\\
>&\text{subject to}
>& &y\geq 0, 1^{T}y =1.\\\\
>\end{align}
>$$

위와 마찬가지로 이를 두 번째 관점의 문제 정의라고 칭하고, 이 최적화 문제의 해를 $$f^{*}_{2}$$ 라고 하자. player R이 이 expected payout을 maximize하고자 하기 때문에, 첫 번째, 즉, R이 J의 strategy를 미리 알고 있다는 가정 하에 결정되는 expected payout $$f^{*}_{1} $$이 두 번째 가정보다 더 크거나 같은 값을 가질 것이라 쉽게 예상할 수 있다. ($$f^{*}_{1}\geq f^{*}_{2}$$)
  
## Von Neumann's minimax theorem
  하지만,  Von Neumann's minimax theorem에 따르면 $$f^{*}_{1} = f^{*}_{2}$$가 된다. 실제 minimax theorem은 다음과 같다. 
  
>$$
>\begin{align}
>&\text{Let } X\subset \mathbb{R}^{N} \text{ and }Y\subset \mathbb{R}^{m} \text{ be compact convex sets. }\\\\
> &\text{If } f:X\times Y\rightarrow \mathbb{R} \text{ is a continuous function that is convex-concave, i.e.}\\\\
> &\qquad f(\cdot, y): X\rightarrow\mathbb{R} \text{ is convex for fixed }y, \text{ and}\\\\
> &\qquad f(x, \cdot): Y\rightarrow\mathbb{R} \text{ is concave for fixed }x.\\\\
> &\text{Then we have that} \\\\ 
>&\min_{x\in X} \max_{y\in Y} f(x,y) = \max_{y\in Y} \min_{x\in X} f(x,y).\\\\
>\end{align}
>$$

해당 내용의 증명은 생략한다.

## Proof of each perspective having Primal and Dual relationship
  이제 위 두 가지 관점의 경우에 대한 expected payout이 LP 문제로써 서로 primal, dual 관계이고, Von Neumman's minimax theorem에 의하여 두 결과가 같다는 점을 이용하여, strong duality를 만족함을 보이고자 한다.
  
먼저 첫 번째 관점의 문제를 다음과 같이 reformulate 할 수 있다.

>$$
>\begin{align}
>& \min_{x} \max_{i=1,...m} 
>& &(P^{T}x)_{i}\\\\
>&\text{subject to } 
>& &x\geq 0, 1^{T}x = 1\\\\
>\end{align}
>$$
>
>$$
>\begin{align}
>\Leftrightarrow{} \\\\
>& \min_{x,t}
>& & t \\\\
>&\text{subject to } 
>& &x\geq0, 1^{T}x = 1, P^{T}x \preceq t. \\\\
>\end{align}
>$$

$$t$$를 $$P^{T}x$$의 항들 중 가장 큰 값과 같게 만들어주는 문제로 reformulate 하였다.

이제 여기에 앞서 배운 duality의 두 번째 방법인 Lagrangian을 구하고,  Lagrange dual function $$g$$를 구하면, 

>$$
>\begin{align}
>&L(x, t, u, v, y) &&= t-u^{T}x+v(1-1^{T}x)+y^{T}(P^{T}x-t1)\\\\
>&g(u, v, y) &&= \min_{x,t} \quad L(x, t, u, v, y)\\\\
>&&&= \begin{cases} v \qquad &\text{if } 1-1^{T}y = 0, Py-u-v1=0\\\\
-\infty \qquad &\text{otherwise.} \end{cases}
>\end{align}
>$$

$$u$$는 slack variable이므로, 이를 제거하고 식을 정리하면 다음과 같다.

>$$
>\begin{align}
>&\max_{y,v} \qquad \quad && v\\\\
>&\text{subject to }\quad && y\geq0, 1^{T}y = 1\\\\
>&&& Py\geq v.
>\end{align}
>$$

이는 두 번째 관점의 문제의 primal LP이다. 따라서 두 관점은 dual 관계에 있고 두 문제의 optimal value는 같으므로, strong duality가 성립한다.

일반적으로 LP문제에서는, 향 후의 내용에서 다루지만, primal과 dual 중 하나만 feasible하다면 strong duality가 성립한다.

---
layout: post
title: 20-02-02 Dual Decomposition with Inequality Constraint
chapter: '20'
order: 6
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

다음의 problem를 생각solution 보자. 앞의 problemand, 다른점은 제약식이 부등식의 relationship,를 갖는 것이다. 
> $$
> \begin{equation}
> \min_x \sum_{i=1}^B f_i(x_i) \quad \text{subject to} \quad \sum_{i=1}^B A_i x_i \leq b
> \end{equation}
> $$

## Dual decomposition (projected subgradient method) 
위 problemat,는 dual variable가 always, $$0$$보다 같거나 커야 한다, that is, $$u \geq 0$$. therefore,, 다음 스텝의 $$u$$값을 computation할 when,, $$0$$보다 큰 범위안with, projection을 시켜서 업데이트를 한다. 

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right)_+
> \end{alignat}
> $$

여기서, $$u_{+}$$는 0보다 큰 $$u$$를 의미한다, that is,, $$(u_+)_i = \max \left\{0,u_i \right\}, i=1,\dots,m$$. 
위  process을 $$k=1,2,3,\dots$$about,서 iteration한다. 

### Price coordination interpretation
generally, dual decomposition problem들은 price coordination 관점at, as follows: solution석될 수 있다. (Vandenberghe)
> * $$B$$개의 독립적인 유닛이 있고, 각 유닛은 자신의 결정 variable $$x_i$$를 결정한다. 
> * 각 constraint은 $$B$$개의 유닛이 공유하고 있는 자원to, about, 제약을 의미하며, dual variable $$u_j$$는 자원 $$j$$의 가격을 의미한다. 
> * Dual variable는 아래and, 같이 업데이트되며
 \begin{equation}
 u_j^{+} = (u_j - t s_j)_{+}, \quad  j=1,\dots,m
 \end{equation}
>
> $$\quad$$ 여기서, $$s=b-\sum_{i=1}^B A_ix_i$$는 슬랙 variableto,써 \\
> $$\qquad$$ - $$s_j < 0$$이면, 자원 $$j$$가 over-utilized 되고 있다는 의미이고, therefore,, price $$u_j$$를 증가시킨다 \\
> $$\qquad$$ - $$s_j > 0$$이면, 자원 $$j$$가 under-utilized되고 있다는 의미이고,  therefore,, price $$u_j$$를 감소시킨다 \\
> $$\qquad$$ - price는 향image 음수가 되지 않도록 한다.

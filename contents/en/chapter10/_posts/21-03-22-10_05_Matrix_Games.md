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

Now we will examine the perspective where each player considers the opponent's mixed strategy to maximize (from R's perspective) or minimize (from J's perspective) this expected payout. Under the assumption that both players act optimally against each other, we will derive the optimal strategies from both perspectives and ultimately confirm that the two results are equal according to Von Neumann's minimax theorem.

## Minimizing Expected Payout : J's Perspective
First, assume that R knows J's strategy $$x$$. R will want to maximize the expected payout $$x^{T}Py$$. 

>$$
>\begin{align}
>\max\{x^{T}Py : y\geq0, 1^{T}y = 1\} = \max_{i=1,...n}(P^{T}x)_{i}.\\\\
>\end{align}
>$$

At this point, R will find the i (row index) that has the largest value among $$(P^{T}x)_{i}$$ as shown in the equation, and the strategy that sets the corresponding $$y_{i}$$ to 1 and sets 0 for the remaining row indices will be the strategy that maximizes the expected payout for R.

Knowing that R will act optimally as described above, J's optimal strategy will be the distribution $$x$$ that satisfies the following equation.

>$$
>\begin{align}
>& \min_{x}
>& &\max_{i=1,...n} (P^{T}x)_{i}\\\\
>& \text{subject to}
>& & x\geq 0, 1^{T}x =1.\\\\
>\end{align}
>$$

The maximization of a convex function is also a convex function. We will call this the problem definition from the first perspective. Also, let's define the solution to this optimization problem as the optimal expected payout $$f^{*}_{1}$$. Another point to note is that the assumption that all game participants, i.e., players, act optimally is a fundamental assumption in basic game theory formulations.

## Maximizing Expected Payout : R's Perspective
From the second perspective, assume that J knows R's strategy $$y$$. J will want to minimize the expected payout.

>$$
>\begin{align}
>\min \{x^{T}Py : x\geq0, 1^{T}x = 1\} = \min_{j=1,...n}(Py)_{j}.\\\\
>\end{align}
>$$

By the same logic, knowing that J will act optimally as described above, R's optimal strategy is the distribution $$y$$ that satisfies the following equation.

>$$
>\begin{align}
>& \max_{y}  
>& & \min_{j=1,...m} (Py)_{j}\\\\
>&\text{subject to}
>& &y\geq 0, 1^{T}y =1.\\\\
>\end{align}
>$$

Similarly, we will call this the problem definition from the second perspective, and let the solution to this optimization problem be $$f^{*}_{2}$$. Since player R wants to maximize this expected payout, we can easily expect that the expected payout $$f^{*}_{1}$$ determined under the first assumption, i.e., that R knows J's strategy in advance, will have a value greater than or equal to the second assumption. ($$f^{*}_{1}\geq f^{*}_{2}$$)
  
## Von Neumann's minimax theorem
However, according to Von Neumann's minimax theorem, $$f^{*}_{1} = f^{*}_{2}$$. The actual minimax theorem is as follows. 
  
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

The proof of this content is omitted.

## Proof of each perspective having Primal and Dual relationship
Now we want to show that the expected payouts for the above two perspectives have a primal-dual relationship as LP problems, and that strong duality is satisfied by using the fact that the two results are equal according to Von Neumann's minimax theorem.
  
First, the problem from the first perspective can be reformulated as follows.

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

We have reformulated the problem to make $$t$$ equal to the largest value among the terms of $$P^{T}x$$.

Now, applying the second method of duality we learned earlier, we construct the Lagrangian and obtain the Lagrange dual function $$g$$: 

>$$
>\begin{align}
>&L(x, t, u, v, y) &&= t-u^{T}x+v(1-1^{T}x)+y^{T}(P^{T}x-t1)\\\\
>&g(u, v, y) &&= \min_{x,t} \quad L(x, t, u, v, y)\\\\
>&&&= \begin{cases} v \qquad &\text{if } 1-1^{T}y = 0, Py-u-v1=0\\\\
-\infty \qquad &\text{otherwise.} \end{cases}
>\end{align}
>$$

Since $$u$$ is a slack variable, removing it and organizing the equation gives us the following.

>$$
>\begin{align}
>&\max_{y,v} \qquad \quad && v\\\\
>&\text{subject to }\quad && y\geq0, 1^{T}y = 1\\\\
>&&& Py\geq v.
>\end{align}
>$$

This is the primal LP of the problem from the second perspective. Therefore, the two perspectives are in a dual relationship and since the optimal values of the two problems are equal, strong duality holds.

In general, for LP problems, as we will cover in future content, strong duality holds if only one of the primal and dual is feasible.

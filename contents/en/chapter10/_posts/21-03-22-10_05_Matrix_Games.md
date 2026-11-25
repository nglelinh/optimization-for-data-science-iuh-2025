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

In 1928, John von Neumann proved a theorem that launched modern game theory: in any two-player zero-sum game (like Rock-Paper-Scissors or Matching Pennies), if both players are allowed to randomize using **mixed strategies**, it makes *no difference* who reveals their probability distribution first—the best worst-case payout guaranteed by the maximizer equals the lowest worst-case loss guaranteed by the minimizer! Remarkably, once each player's problem is written as a linear program, von Neumann's minimax theorem turns out to be an immediate one-line corollary of LP strong duality.

## Key ideas: Zero-Sum Games as Primal–Dual Linear Programs

- **Pillar 1 — Mixed Strategies & Expected Payoff:** Players $$J$$ and $$R$$ choose probability vectors $$x \in \Delta_m$$ ($$x \ge 0, \mathbf{1}^\top x = 1$$) and $$y \in \Delta_n$$ ($$y \ge 0, \mathbf{1}^\top y = 1$$). The expected payout from $$J$$ to $$R$$ is the bilinear form $$x^\top P y$$.
- **Pillar 2 — Epigraph Reformulation to LP:** When $$J$$ commits to $$x$$ first, $$R$$'s best response is $$\max_{y \in \Delta_n} x^\top P y = \max_{1 \le j \le n} (P^\top x)_j$$ (attained at a pure strategy). Introducing a scalar epigraph variable $$t$$ converts $$J$$'s minimax problem into the LP $$\min_{x, t} \{ t : P^\top x \le t \mathbf{1},\; \mathbf{1}^\top x = 1,\; x \ge 0 \}$$.
- **Pillar 3 — Opponent's Problem = Exact LP Dual:** Taking the LP dual of $$J$$'s minimization LP introduces multipliers $$y \ge 0$$ (for $$P^\top x \le t\mathbf{1}$$) and $$s \in \mathbb{R}$$ (for $$\mathbf{1}^\top x = 1$$), yielding $$\max_{y, s} \{ s : P y \ge s \mathbf{1},\; \mathbf{1}^\top y = 1,\; y \ge 0 \}$$—which is literally $$R$$'s maximin problem!
- **Pillar 4 — Von Neumann Minimax Theorem via Strong Duality:** Because both LPs are feasible (any uniform distribution works) and bounded (by $$\max |P_{ij}|$$), LP strong duality guarantees $$\min_{x \in \Delta_m} \max_{y \in \Delta_n} x^\top P y = \max_{y \in \Delta_n} \min_{x \in \Delta_m} x^\top P y = v^\star$$, the unique value of the game.

### Worked example: Solving an Asymmetric $$2 \times 2$$ Matrix Game from Both Sides

Consider the payout matrix (from $$J$$ to $$R$$): $$P = \begin{pmatrix} 3 & 0 \\ 1 & 4 \end{pmatrix}$$. Notice there is no pure-strategy saddle point (row maxes are $$3, 4 \implies \min = 3$$; column mins are $$1, 0 \implies \max = 1 < 3$$).

1. **$$J$$'s primal LP (choose $$x = (x_1, 1 - x_1)^\top$$ to minimize $$\max\{3x_1 + (1 - x_1),\; 0x_1 + 4(1 - x_1)\}$$):**
   - Column 1 expected payout: $$1 + 2x_1$$.
   - Column 2 expected payout: $$4 - 4x_1$$.
   - To minimize the maximum of an increasing line and a decreasing line, set them equal:
     $$1 + 2x_1 = 4 - 4x_1 \implies 6x_1 = 3 \implies x_1^\star = \frac{1}{2},\; x_2^\star = \frac{1}{2}.$$
   - Primal value: $$t^\star = 1 + 2(0.5) = 2.0$$.
2. **$$R$$'s dual LP (choose $$y = (y_1, 1 - y_1)^\top$$ to maximize $$\min\{3y_1 + 0(1 - y_1),\; 1y_1 + 4(1 - y_1)\}$$):**
   - Row 1 expected payout: $$3y_1$$.
   - Row 2 expected payout: $$4 - 3y_1$$.
   - Equating both lines:
     $$3y_1 = 4 - 3y_1 \implies 6y_1 = 4 \implies y_1^\star = \frac{2}{3},\; y_2^\star = \frac{1}{3}.$$
   - Dual value: $$s^\star = 3(2/3) = 2.0$$.
3. **Verify von Neumann's theorem:** $$t^\star = 2.0 = s^\star$$! Even though pure strategies had a gap $$1 < 3$$, mixed strategies closed the gap completely via LP strong duality.

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
>x : P(\text{J chooses i}) = x_{i}, \qquad i=1,...,m\\\\
>y : P(\text{R chooses j}) = y_{j}, \qquad j=1,...,n.\\\\
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
>\max\{x^{T}Py : y\geq0, 1^{T}y = 1\} = \max_{j=1,...,n}(P^{T}x)_{j}.\\\\
>\end{align}
>$$

At this point, R will find the i (row index) that has the largest value among $$(P^{T}x)_{i}$$ as shown in the equation, and the strategy that sets the corresponding $$y_{i}$$ to 1 and sets 0 for the remaining row indices will be the strategy that maximizes the expected payout for R.

Knowing that R will act optimally as described above, J's optimal strategy will be the distribution $$x$$ that satisfies the following equation.

>$$
>\begin{align}
>& \min_{x}
>& &\max_{j=1,...,n} (P^{T}x)_{j}\\\\
>& \text{subject to}
>& & x\geq 0, 1^{T}x =1.\\\\
>\end{align}
>$$

The maximization of a convex function is also a convex function. We will call this the problem definition from the first perspective. Also, let's define the solution to this optimization problem as the optimal expected payout $$f^{*}_{1}$$. Another point to note is that the assumption that all game participants, i.e., players, act optimally is a fundamental assumption in basic game theory formulations.

## Maximizing Expected Payout : R's Perspective
From the second perspective, assume that J knows R's strategy $$y$$. J will want to minimize the expected payout.

>$$
>\begin{align}
>\min \{x^{T}Py : x\geq0, 1^{T}x = 1\} = \min_{i=1,...,m}(Py)_{i}.\\\\
>\end{align}
>$$

By the same logic, knowing that J will act optimally as described above, R's optimal strategy is the distribution $$y$$ that satisfies the following equation.

>$$
>\begin{align}
>& \max_{y}  
>& & \min_{i=1,...,m} (Py)_{i}\\\\
>&\text{subject to}
>& &y\geq 0, 1^{T}y =1.\\\\
>\end{align}
>$$

Similarly, we will call this the problem definition from the second perspective, and let the solution to this optimization problem be $$f^{*}_{2}$$. Since player R wants to maximize this expected payout, we can easily expect that the expected payout $$f^{*}_{1}$$ determined under the first assumption, i.e., that R knows J's strategy in advance, will have a value greater than or equal to the second assumption. ($$f^{*}_{1}\geq f^{*}_{2}$$)
  
## Von Neumann's minimax theorem
However, according to Von Neumann's minimax theorem, $$f^{*}_{1} = f^{*}_{2}$$. The actual minimax theorem is as follows. 
  
>$$
>\begin{align}
>&\text{Let } X\subset \mathbb{R}^{m} \text{ and }Y\subset \mathbb{R}^{n} \text{ be compact convex sets. }\\\\
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
>& \min_{x} \max_{j=1,...,n} 
>& &(P^{T}x)_{j}\\\\
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

### A matrix game: minimax and duality (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/matrix-game_en.mp4"></video>
</div>

J minimises the highest line, R maximises the lowest one, and both reach the same value: the minimax theorem, which is LP duality.

### Try it yourself: the game from both sides

<div class="opx-explainer" data-opx="mgame" data-lang="en"></div>

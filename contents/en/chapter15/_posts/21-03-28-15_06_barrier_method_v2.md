---
layout: post
title: 15-06 Barrier method v.2
order: '12'
owner: Minjoo Lee
categories:
- chapter15
lang: en
---

In the previous algorithm, we generated solutions along the central path, but in reality, the central path is just a means to reach the optimal solution ("means to an end"). Therefore, it is not necessary to solve the problem exactly.

### Algorithm

For this reason, Barrier method v.2 solves the barrier problem approximately. However, in step 2, $$x^{(0)} \approx x^*(t)$$ and in step 3-2, $$x^{(k+1)} \approx x^*(t)$$ are now approximations.

The steps of the algorithm are the same as those in Barrier method v.1.

1. Choose $$t^{(0)} > 0$$ and set $$k := 0$$.
2. At $$t = t^{(0)}$$, solve the barrier problem to obtain $$x^{(0)} \approx x^*(t)$$.
3. While $$m/t > \epsilon$$<br>
   3-1. Choose $$t^{(k+1)} > t^{(k)}$$.<br>
   3-2. Initialize Newton's method with $$x^{(k)}$$ (warm start)<br>
        At $$t = t^{(k+1)}$$, solve the barrier problem to obtain $$x^{(k+1)} \approx x^*(t)$$.<br>
   end while<br>

In Barrier method v.2, the following two issues are very important:

* How close should each approximation be?
* How many Newton steps are needed at each centering step?

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_04.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Fig 1] Analysis of Newton iterations and suboptimality gap with respect to m [1]</figcaption>
</p>
</figure>

In the following figure, you can see that when the barrier method is applied to a problem with $$m$$ constraints, linear convergence occurs even as $$m$$ becomes large. That is, it has a log scale with respect to $$m$$.

From a different perspective, the Newton steps needed (to reduce the initial suboptimal gap (duality gap) of $$10^4$$) increase slowly with respect to $$m$$. Looking at the figure below, even when $$m$$ increases significantly, about 20-30 Newton steps are needed for each centering step. However, one Newton step varies greatly depending on the size of the problem.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_05.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Fig 2] Analysis of the number of Newton iterations as m increases [1]</figcaption>
</p>
</figure>
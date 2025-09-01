---
layout: post
title: 15-06 Barrier method v.2
order: 12
owner: Minjoo Lee
categories:
- chapter15
lang: en
---
이전 알고리즘에서는 central path에 있는 solution을 생성했는데, 실제 central path는 optimal로 가는 과정("means to an end")일 뿐이다. 따라서, 문제를 정확히 풀 필요는 없다.

In the previous algorithm, we generated solutions along the central path, but in reality, the central path is just a means to reach the optimal solution. Therefore, it is not necessary to solve the problem exactly.

#### Algorithm
For this reason, Barrier method v.2 solves the barrier problem approximately.

단, 단계 2의  $$x^{(0)} \approx x^*(t)$$와 단계 3-2의 $$x^{(k+1)} \approx x^*(t)$$ 부분이 approximation으로 바뀌었다.
The steps of the algorithm are the same as those in Barrier method v.1.
1. $$t^{(0)} \gt 0$$이고 $$k := 0$$을 선택한다.
However, in step 2, $$x^{(0)} \approx x^*(t)$$ and in step 3-2, $$x^{(k+1)} \approx x^*(t)$$ are now approximations.
3. While $$m/t \gt \epsilon$$ <br>
1. Choose $$t^{(0)} > 0$$ and set $$k := 0$$.
2. At $$t = t^{(0)}$$, solve the barrier problem to obtain $$x^{(0)} \approx x^*(t)$$.
3. While $$m/t > \epsilon$$ <br>
  3-1. Choose $$t^{(k+1)} > t^{(k)}$$. <br>
  3-2. Initialize Newton's method with $$x^{(k)}$$. (warm start)<br>
        At $$t = t^{(k+1)}$$, solve the barrier problem to obtain $$x^{(k+1)} \approx x^*(t)$$.<br>
  end while<br>
Barrier method v.2에서는 다음 두 가지 사항이 매우 중요하다.<br>

* 얼마나 근사를 잘 할 수 있는가? (How close should each approximation be?)
In Barrier method v.2, the following two issues are very important:<br>

* How close should each approximation be?
* How many Newton steps are needed at each centering step?

<figure class="image" style="align: center;">
In the following figure, you can see that when the barrier method is applied to a problem with $$m$$ constraints, linear convergence occurs even as $$m$$ becomes large. That is, it has a log scale with respect to $$m$$.
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_04.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] m에 대해 newton iteration과 suboptimality gap 분석 [1]</figcaption>
</p>
</figure>


다르게 보면 ($$10^4$$인 초기 suboptimal gap (duality gap)을 줄이기 위해 필요한) newton step은 $$m$$에 대해 천천히 증가한다. 아래 그림을 보면 $$m$$이 크게 증하하더라도 각 centering step 별로 20~30 newton step 정도만 필요하다. 단, 한 newton step은 문제의 크기에 따라 크게 달라진다.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_05.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 2] m의 증가와 newton iteration 수 분석 [1]</figcaption>
</p>
</figure>

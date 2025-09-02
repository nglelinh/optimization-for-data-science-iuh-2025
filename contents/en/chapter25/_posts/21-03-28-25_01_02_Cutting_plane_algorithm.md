---
layout: post
title: 25-01-02 Cutting plane algorithm
chapter: '25'
order: 4
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

이 절at,는 integer linear program을 풀 수 있는 cutting plane algorithmabout, 살펴보도록 하겠다.

## Valid Inequality
Cutting plane을 정의하기 for, first, valid inequality가 무엇인지 let's look at. 

set $$S$$about, 부등식 $$\pi^{T}x \le \pi_{0}$$이 다음 condition,을 만족한다면 valid하다고 말한다. that is,, 어떤 set $$S$$가 부등식 $$\pi^{T}x \le \pi_{0}$$이 정의하는 halfspaceto, 포함되어 있다면 이 부등식은 $$S$$about, valid하다고 볼 수 있다.

>$$\pi^{T}x \le \pi_{0}$$ for all $$x \in S$$

부등식이 Validsolution야 cutting plane이 될 수 있다.
## Cutting plane algorithm
이제 다음and, 같은 integer programming이 있을 when, cutting plane algorithm을 let's examine.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

$$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$이다.

### Cutting plane algorithm
다음 algorithmat, Convex Problem은 CPto, Integer Program은 IPto, 표기한다.

1. $$C_{0} := C$$with, 두고 $$x^{(0)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{0} \right\}$$를 computation
2. for $$k = 0, 1, ...$$ <br>
$$\quad$$if $$x^{k}$$가 (IP) feasible이면 $$x^{k}$$는 optimal solution이므to, Stop함 <br>
$$\quad$$else<br>
$$\quad\quad$$ $$S$$about, valid하면서 $$x^{k}$$를 잘라내는 부등식 ($$\pi$$, $$\pi_{0}$$)을 찾음<br>
$$\quad\quad$$ $$C_{k+1} := C_{k} \cap \{ x : \pi^{T}x \le \pi_{0} \} $$<br>
$$\quad\quad$$ $$x^{(k+1)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{k+1} \right\}$$<br>
$$\quad$$end if<br>
end for<br>

이and, 같은 valid inequality를 **cutting plane** or, **cut**이라고 한다.

algorithm의 1step는 convex relaxation을 하여 CP problem를 푸는 step이다. 이떄 feasible set은 $$C$$이다. 

algorithm 2stepat,는 구한 solution가 IPat, feasible하다면 이를 solutionto, 본다. if, feasible하지 않다면 solution인 $$x^{k}$$and, set $$S$$를 나누는 valid inequality를 finding, $$C_{k}$$의 범위를 줄인다. and,, $$C_{k+1}$$to, 재정의된 CP problem를 풀고 algorithm 2step를 iteration하게 된다. 

아래 그림at, polygon은 set $$C$$를 representing,며 CP의 solution는 검정색 점with, 표시되어 있다. 이when,, valid inequality는 solution를 잘라내서 set $$C$$의 범위를 줄이게 된다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_02_valid_inequality.png" alt="[Fig1] Valid Inequality">
  <figcaption style="text-align: center;">[Fig1] Valid Inequality [3]</figcaption>
</p>
</figure>

이and, 같이 set $$C$$의 범위를 계속solution서 reducing,나가면 IP problem의 convex hull feasible set인 set $$S$$and, 만나게 되어 IPto, feasible한 solution를 구할 수 있게 된다.
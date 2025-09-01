---
layout: post
title: 25-01-01 Convexification
chapter: '25'
order: 3
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

Integer program을 동일한 convex problemwith, transformation하는 것을 convexification이라고 한다. Convexification을 하게 되면 feasible set이 polyhedron 형태가 되어 cutting plane algorithmat, valid한 cutting plane을 쉽게 찾을 수 있다.

## Convexification
Integer program을 convexification하려면 objective function이 linearsolution야 한다. 이when,, Integer program의 constraint는 convex set인 $$C$$and, integer set인 $${x_j}$$to, 구성된다.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

이when,, feasible set은 convex hull $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$to, 재정의할 수 있다. 이 convex hull $$S$$to, 정의된 feasible set을 using, 원래 problemand, 동일한 convex problem을 as follows: 정의할 수 있다. and,, 이러한 process을 convexification이라고 한다. 

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  x \in S \\
> \end{align}
> $$

아래 그림을 보면 파란색 영역이 $$C$$이고 빨간색 점들이 $${x_j}$$이며, 이 두 setwith, 구성된 convex hull $$S$$는 빨간색 영역이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Fig1] Cutting Plane">
  <figcaption style="text-align: center;">[Fig1] Cutting Plane</figcaption>
</p>
</figure>
출처: https://commons.wikimedia.org/wiki/File:Cutting_plane_algorithm2.png <br><br>

이 두 식이 동일한 reason,는 objective function이 linear하기 because,이다. 

## Special case: integer linear programs
위의 convexification process을 다음and, 같은 integer linear programto, applying,보자.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\
> \text{subject to } & \quad  Ax \le b \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

Integer linear programat, convex hull $$S$$는 as follows: 정의된다.

> **Theorem** : if, $$A, b$$가 rational number라면 다음 set은 polygon이다.
$$S := \text{conv} \left \{ x : Ax \le b,  x_j \in \mathbb{Z}, j \in J \right \}$$

그렇다면 integer linear program은 linear program일까? of course, 그렇다. but,, 이when, polyhedron $$S$$의 형태는 부등식이 기하급수적with, 많은 매우 많은 복잡한 다각형이 될 수 있다. therefore,, generally, linear program을 풀기 위한 methodand,는 다른 methodwith, problem를 풀어야 한다.

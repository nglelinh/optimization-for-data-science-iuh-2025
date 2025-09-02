---
layout: post
title: 25-01 Cutting Planes
chapter: '25'
order: 2
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

The cutting plane method is an approach that changes an integer linear program to a convex problem and finds a solution. If this solution is not included in the original feasible set, it uses cuts to progressively guide the newly obtained solution to be included in the original feasible set by cutting out the region where the solution exists. Here, a cut is a line (or hyperplane) that cuts the feasible set, also called a cutting plane.

## Concept of cutting plane
개념적with, 아래 그림and, 같이 original feasible setand, feasible set 사이to, 직선을 그어서 original feasible set이 아닌 영역을 잘라내는 방식이라고 생각하면 된다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Fig1] Cutting Plane">
  <figcaption style="text-align: center;">[Fig1] Cutting Plane</figcaption>
</p>
</figure>

* 빨간색 영역 : original integer linear program의 feasible set
* 파란색 영역 : convex relaxation problem의 feasible set
* 녹색 직선 :  cutting plane (cutting plane은 파란색and, 빨간색 영역의 사이to, 존재한다.)

자세한 algorithm은 본문at, 다시 소개하도록 하겠다.


## A bit of history on cutting planes
Cutting plane method는 이론으from, 실용적인 methodwith, 발전solution 오기to, 매우 오래 시간이 걸렸다. 

1954년to, Dantzig, Fulkerson, Johnson이 TSP(traveling salesman problem)를 풀기 for, 처음with, Cutting plane method를 제안했으며, 1958년to, 수학자인 Gomory가 임의의 integer linear program을 풀 수 있는 범용적인 cutting plane method를 제안했다. however, 그 after, 약 30년 during, Gomory cut은 실제 problem를 풀기to,는 실용적이지 않은 image태to, 묻혀있었다.

1990년 CMU의 Sebastian Ceria는  cutting plane method를 branch and bound algorithm을 using,서 성공적with, 구현을 하였으며 이를 branch and cut이라고 한다. 이when,from, cutting plane은 image용 optimization solver의 핵심적인 컴포넌트가 되었다.
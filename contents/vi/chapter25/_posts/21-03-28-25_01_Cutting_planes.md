---
layout: post
title: 25-01 Cutting Planes
chapter: '25'
order: 2
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

The cutting plane method is an approach that changes an integer linear program to a convex problem and finds a solution. If this solution is not included in the original feasible set, it uses cuts to progressively guide the newly obtained solution to be included in the original feasible set by cutting out the region where the solution exists. Here, a cut is a line (or hyperplane) that cuts the feasible set, also called a cutting plane.

## Concept of cutting plane
Conceptually, it can be thought of as a method that draws a line between the original feasible set and the feasible set to cut out regions that are not part of the original feasible set, as shown in the figure below. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Fig1] Cutting Plane">
  <figcaption style="text-align: center;">[Fig1] Cutting Plane</figcaption>
</p>
</figure>

* Red region: feasible set of the original integer linear program
* Blue region: feasible set of the convex relaxation problem
* Green line: cutting plane (the cutting plane exists between the blue and red regions)

The detailed algorithm will be introduced again in the main text.


## A bit of history on cutting planes
It took a very long time for the cutting plane method to develop from theory to a practical method. 

In 1954, Dantzig, Fulkerson, and Johnson first proposed the cutting plane method to solve the TSP (traveling salesman problem), and in 1958, mathematician Gomory proposed a general cutting plane method that could solve arbitrary integer linear programs. However, for about 30 years after that, Gomory cuts remained buried in an impractical state for solving real problems.

In 1990, Sebastian Ceria at CMU successfully implemented the cutting plane method using the branch and bound algorithm, which is called branch and cut. Since then, cutting planes have become a core component of commercial optimization solvers.
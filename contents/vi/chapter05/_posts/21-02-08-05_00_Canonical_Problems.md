---
layout: post
title: 05 Canonical Problems
chapter: '05'
order: 1
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

# Canonical Problems

In [Chapter 1](/chapter01/2021/01/07/optimization_problems/), we learned that a convex optimization problem is defined as follows:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_00_optimization_problem.png" alt="[Fig1] Convex Optimization Problem in standard form [3]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Convex Optimization Problem in standard form [3]</figcaption>
</p>
</figure>

* The domain set is convex
* The objective function $$ f $$ and the inequality constraint function $$ g_i $$ are convex
* The equality constraint function $$ h_j $$ is affine

Depending on the type of objective and constraint functions, optimization problems are classified into several categories. In this chapter, we will learn about six major subclasses:

- Linear Programming (LP)
- Quadratic Programming (QP)
- Quadratically Constrained Quadratic Programming (QCQP)
- Second-Order Cone Programming (SOCP)
- Semidefinite Programming (SDP)
- Conic Programming (CP)

These problems have the following inclusion relationships and become more general as you move down the list:

$$ LP \subseteq QP \subseteq QCQP \subseteq SOCP \subseteq SDP \subseteq CP $$
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_00_canonical_problems.jpeg" alt="[Fig2] Canonical Problems" width="90%">
  <figcaption style="text-align: center;">[Fig2] Canonical Problems</figcaption>
</p>
</figure>
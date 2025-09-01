---
layout: post
title: 17-02 Primal-dual interior-point method
chapter: '17'
order: 3
owner: Minjoo Lee
categories:
- chapter17
lang: en
---
Like the barrier method, the **primal-dual interior-point method** also aims to (approximately) compute points on the central path. However, the two methods have several differences.

## Primal-dual interior-point method와 barrier method의 차이점
* Generally performs **one Newton step** per iteration. (That is, there is no additional loop for the centering step.)
* **Does not necessarily need to be feasible**. (Pushes toward feasible regions through backtracking line search.)
* Generally **more effective**. Particularly shows superior performance compared to linear convergence under appropriate conditions.
* Somewhat less intuitive compared to the barrier method.

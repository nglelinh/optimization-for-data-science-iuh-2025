---
layout: post
title: 25-01-02 Cutting plane algorithm
chapter: '25'
order: '4'
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

In this section, we will examine the cutting plane algorithm that can solve integer linear programs.

## Valid Inequality

To define cutting planes, let's first look at what valid inequalities are. An inequality $$\pi^{T}x \le \pi_{0}$$ is said to be valid for set $$S$$ if it satisfies the following condition. That is, if a set $$S$$ is contained in the halfspace defined by the inequality $$\pi^{T}x \le \pi_{0}$$, then this inequality can be considered valid for $$S$$.

>$$\pi^{T}x \le \pi_{0} \text{ for all } x \in S$$

An inequality must be valid to become a cutting plane.

## Cutting plane algorithm

Now let's examine the cutting plane algorithm when we have the following integer programming problem:

>$$
>\begin{align}
>\min_{x} & \quad c^{T}x \\
>\text{subject to } & \quad x \in C \\
>& \quad x_j \in \mathbb{Z}, \quad j \in J \\
>\end{align}
>$$

where $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$.

### Cutting plane algorithm

In the following algorithm, we denote the Convex Problem as CP and the Integer Program as IP.

1. Set $$C_{0} := C$$ and compute $$x^{(0)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{0} \right\}$$
2. for $$k = 0, 1, ..$$
   - if $$x^{k}$$ is (IP) feasible, then $$x^{k}$$ is the optimal solution, so Stop
   - else
     - Find a valid inequality $$(\pi, \pi_{0})$$ for $$S$$ that cuts off $$x^{k}$$
     - $$C_{k+1} := C_{k} \cap \{ x : \pi^{T}x \le \pi_{0} \}$$
     - $$x^{(k+1)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{k+1} \right\}$$
   - end if
   - end for

Such valid inequalities are called **cutting planes** or **cuts**. Step 1 of the algorithm involves convex relaxation to solve the CP problem. At this time, the feasible set is $$C$$. In step 2 of the algorithm, if the obtained solution is feasible for IP, we consider this solution optimal. If it is not feasible, we find a valid inequality that separates the solution $$x^{k}$$ from the set $$S$$, thereby reducing the scope of $$C_{k}$$. Then, we redefine $$C_{k+1}$$ to solve the CP problem and iterate step 2 of the algorithm.

In the figure below, the polygon represents the set $$C$$, and the CP solution is represented by the black dot. In this case, a valid inequality cuts off the solution to reduce the scope of the set $$C$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_02_valid_inequality.png" alt="[Fig1] Valid Inequality">
  <figcaption style="text-align: center;">[Fig1] Valid Inequality [3]</figcaption>
</p>
</figure>

By continuously reducing the scope of the set $$C$$ in this way, we eventually meet the feasible set $$S$$, which is the convex hull of the IP problem, allowing us to find a solution that is feasible for IP.
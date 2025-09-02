---
layout: post
title: 03-04-02 Basic properties of quasiconvex functions
chapter: '03'
order: 10
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

This section covers the basic properties of quasiconvex functions, including their relationship to convex functions and their behavior under various operations.

## Modified Jensen's inequality
Quasiconvex functions can be defined through Jensen's inequality as follows:
>$$f(\theta x + (1 - \theta)y) \leq \max\{f(x), f(y)\}$$ for all $$x, y \in \text{dom}f, 0 \leq \theta \leq 1$$

The figure below shows that if function $$f$$ is quasiconvex, then the value of $$f$$ along the line segment between two points does not exceed the maximum of $$f$$ at the endpoints.
<br><br>

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.10_quasiconvex_function_on_R_4uChnEm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1]</figcaption>
</p>
</figure>
**quasiconvex function on $$\mathbb{R}$$. The values of $$f$$ between $$x$$ and $$y$$ are less than $$\max\{f(x), f(y)\}$$.**

<br>

## Quasiconvex function on $$\mathbb{R}$$
A continuous function $$f : \mathbb{R} \mapsto \mathbb{R}$$ is quasiconvex if and only if it satisfies at least one of the following conditions:

• $$f$$ is nondecreasing
• $$f$$ is nonincreasing  
• There exists a point $$c \in \text{dom} f$$ such that $$f$$ is nonincreasing on $$\{t \in \text{dom}f \mid t \leq c\}$$ and nondecreasing on $$\{t \in \text{dom}f \mid t \geq c\}$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.11_quasiconvex_function_on_R_2_PPQpNiU.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2]</figcaption>
</p>
</figure>
**quasiconvex function on $$\mathbb{R}$$. It is nonincreasing for $$t \leq c$$ where $$t \in \text{dom} f$$, and nondecreasing for $$t \geq c$$ where $$t \in \text{dom} f$$.**

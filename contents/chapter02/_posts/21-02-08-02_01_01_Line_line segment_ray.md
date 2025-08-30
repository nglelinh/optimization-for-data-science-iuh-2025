---
layout: post
title: 02-01-01 Line, line segment, ray
chapter: "02"
order: 2
owner: "Wontak Ryu"
---

To define affine sets, convex sets, and cones, let's first look at lines, line segments, and rays.

A line is an infinitely extending straight path passing through two points in both directions. In contrast, a line segment is a straight path defined only between two points, and a ray starts at one point and extends infinitely in one direction through another point. The figure below shows a line and a line segment. Depending on the range of the parameter $$\theta$$, you can imagine how a line, line segment, or ray is defined.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.01_Line_Segment.png" alt="Line Segment" width="70%">
  <figcaption style="text-align: center;">$$\text{[Fig1] } x_1\text{ and } x_2 \text{ defining a Line and Line Segment [1]}$$</figcaption>
</p>
</figure>

[Reference] When you use two points included in a set to create a line, line segment, or ray, whether these are included in the set determines the definition of the set. (You can also define sets using multiple points and their affine, convex, or conic combinations. Details will be explained in the following sections.)

## Line

A **Line** passing through two points $$x_1$$ and $$x_2$$ is defined as:
> $$y = \theta x_1 + (1 - \theta) x_2$$ with $$\theta \in \mathbb{R}$$

## Line segment

A **Line segment** is defined by restricting $$\theta$$ to the interval [0, 1]:
> $$y = \theta x_1 + (1 - \theta) x_2$$ with $$0 \le \theta \le 1$$

Alternatively, you can express it as:
> $$y = x_2 + \theta (x_1 - x_2)$$ with $$0 \le \theta \le 1$$

## Ray

A **Ray** starts at one point and extends infinitely in one direction:
> $$y = x_2 + \theta (x_1 - x_2)$$ with $$\theta \ge 0$$

Or equivalently:
> $$y = \theta x_1 + (1 - \theta) x_2$$ with $$\theta \ge 0$$



Now you can see that the range of $$\theta$$ is $$\theta \in \mathbb{R}$$ for lines, $$0 \le \theta \le 1$$ for line segments, and $$\theta \ge 0$$ for rays. Furthermore, you will find that the ranges of $$\theta$$ are the same in the affine sets, convex sets, and conic sets that we will define later.


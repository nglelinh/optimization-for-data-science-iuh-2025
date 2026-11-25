---
layout: post
title: 02-01-01 Line, line segment, ray
chapter: '02'
order: 3
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

Every line-search algorithm in optimization reduces an $$n$$-dimensional problem to a 1-dimensional walk along a ray $$x_k + t d$$ ($$t \ge 0$$), while every proof of convexity checks values along a line segment $$\theta x_1 + (1-\theta)x_2$$ ($$0 \le \theta \le 1$$). Mastering the exact parameter domains of lines, segments, and rays turns high-dimensional geometry into effortless 1D algebra.

## Background Knowledge Map: One-Dimensional Geometric Primitives

- **Line ($$\theta \in \mathbb{R}$$):** $$y(\theta) = \theta x_1 + (1-\theta)x_2$$ extends infinitely in both directions through $$x_1$$ and $$x_2$$—the simplest nontrivial affine set.
- **Line Segment ($$\theta \in [0, 1]$$):** Restricting $$\theta$$ to $$[0, 1]$$ traps $$y(\theta)$$ between endpoints $$x_1$$ and $$x_2$$—the exact test object for convexity.
- **Ray ($$t \ge 0$$):** $$y(t) = x_0 + t v$$ starts at basepoint $$x_0$$ and shoots infinitely along direction $$v \neq 0$$—used for line search and unbounded recession directions of feasible sets.
- **Parameterization Equivalence:** Writing $$y(\theta) = x_2 + \theta(x_1 - x_2)$$ reveals the direction vector $$v = x_1 - x_2$$ explicitly so you can read velocity and endpoints at a glance.

### Step-by-Step Worked Example (Read Slowly): Parameterizing a Line, Segment, and Ray in $$\mathbb{R}^2$$

Given $$x_1 = (1, 2)^T$$ and $$x_2 = (5, 0)^T$$, form $$y(\theta) = \theta x_1 + (1-\theta)x_2 = (5 - 4\theta,\; 2\theta)^T$$.

1. **Point on the line segment ($$\theta = 0.25 \in [0, 1]$$):**
   $$y(0.25) = (5 - 1,\; 0.5)^T = (4, 0.5)^T.$$
   This sits one-quarter of the way from $$x_2$$ toward $$x_1$$.
2. **Point on the infinite line but outside the segment ($$\theta = 1.5 \notin [0, 1]$$):**
   $$y(1.5) = (5 - 6,\; 3)^T = (-1, 3)^T.$$
   Notice it overshoots $$x_1$$ along the same collinear slope $$-1/2$$.
3. **Ray starting at $$x_1$$ through $$x_2$$:** Direction is $$v = x_2 - x_1 = (4, -2)^T$$, so $$r(t) = (1, 2)^T + t(4, -2)^T$$ for $$t \ge 0$$. At $$t = 2$$, $$r(2) = (9, -2)^T$$, continuing past $$x_2$$ (which corresponds to $$t = 1$$).

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


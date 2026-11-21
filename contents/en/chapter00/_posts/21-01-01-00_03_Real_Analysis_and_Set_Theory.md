---
layout: post
title: 00-03 Real Analysis And Set Theory
chapter: '00'
order: 11
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: required
---

Convex optimization is analysis on *sets*: a feasible region, an epigraph, a cone of dual multipliers. Before Chapter 02 defines convex sets, we need the vocabulary of open and closed sets, interiors, and sequences.

## Why this block exists

- **Feasible sets** are subsets of $$\mathbb{R}^n$$. Closedness decides whether a minimizing sequence has a limit *inside* the set; boundedness plus closedness (Heine–Borel in finite dimension) gives existence of a minimizer for a continuous objective.
- **Open sets and interiors** appear in constraint qualifications (Slater: a point in the relative interior of the inequalities) that make KKT conditions necessary in Chapter 12.
- **Sequences and limits** are how we even state “$$x^{(k)}\to x^\star$$” for gradient descent.

A set $$C\subseteq\mathbb{R}^n$$ is **closed** if it contains all its limit points, **open** if it is a neighborhood of each of its points, and **compact** (in $$\mathbb{R}^n$$) if and only if it is closed and bounded. The **epigraph**

$$
\operatorname{epi} f = \bigl\{(x,t): f(x)\le t\bigr\}
$$

is a set in $$\mathbb{R}^{n+1}$$; $$f$$ is lower semicontinuous precisely when $$\operatorname{epi} f$$ is closed. That one sentence is the analysis backbone of “does this loss attain its infimum?”

## Lessons in this block

1. Set theory fundamentals (unions, intersections, complements, products — the algebra of constraints)
2. Topology in real analysis (open/closed sets, interiors, sequences)

After these two lessons you should be able to say, without hesitation, whether $$\{x: \|x\|_2 \le 1\}$$ is compact and whether $$\{x: \|x\|_2 < 1\}$$ can contain a minimizer of a function that decreases toward the boundary.

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

Before running an algorithm to minimize $$f(x)$$ over a feasible region $$C$$, a mathematician asks a deceptively simple question: *does a minimum even exist?* Minimizing $$e^x$$ over $$\mathbb{R}$$ or $$1/x$$ over $$(1, \infty)$$ chases an infimum that is never attained. Set theory and real analysis give us the exact vocabulary—open, closed, bounded, compact, infimum—needed to guarantee that optimization problems are well-posed before we spend a single CPU cycle solving them.

## Background Knowledge Map: Foundations of Well-Posed Optimization

- **Set Algebra for Constraints:** Every feasible region is an intersection of constraint sets $$C = \bigcap_i C_i$$; set operations let us manipulate feasible domains cleanly and apply De Morgan's laws when reasoning about infeasibility.
- **Infimum vs. Minimum:** The infimum $$\inf_{x \in C} f(x)$$ always exists in $$\mathbb{R} \cup \{-\infty\}$$, whereas a *minimum* requires an actual point $$x^* \in C$$ attaining that value.
- **Open, Closed, and Boundary Points:** Strict inequalities define open sets (no boundary to land on), while non-strict inequalities define closed sets that contain their own limit points.
- **Compactness & Weierstrass's Theorem:** In $$\mathbb{R}^n$$, closed and bounded sets are compact; any continuous objective on a nonempty compact set is guaranteed to attain both its global minimum and maximum.

### Step-by-Step Worked Example (Read Slowly): Attained Minimum vs. Unattained Infimum

Compare minimizing $$f(x) = \frac{1}{x}$$ over three different domains:

1. **Open unbounded domain $$D_1 = (1, \infty)$$:** As $$x \to \infty$$, $$1/x \to 0$$, yet $$1/x > 0$$ for every $$x \in D_1$$. Thus $$\inf_{x \in D_1} f(x) = 0$$, but **no minimizer exists**.
2. **Half-open bounded domain $$D_2 = (0, 1]$$:** On $$D_2$$, $$f(x) \ge 1$$ with equality at $$x^* = 1 \in D_2$$, so $$\min_{x \in D_2} f(x) = 1$$ exists; however, $$f(x) \to +\infty$$ as $$x \to 0^+$$, so no maximum exists because $$D_2$$ is not closed.
3. **Compact domain $$D_3 = [1, 4]$$:** $$D_3$$ is closed and bounded (compact by Heine–Borel), and $$f(x) = 1/x$$ is continuous on $$D_3$$. By Weierstrass's theorem, both extrema are attained:
   $$\min_{x \in [1, 4]} \frac{1}{x} = \frac{1}{4} \text{ (at } x = 4\text{)}, \qquad \max_{x \in [1, 4]} \frac{1}{x} = 1 \text{ (at } x = 1\text{)}.$$

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

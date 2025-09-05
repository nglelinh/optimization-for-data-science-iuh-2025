---
layout: post
title: 02-03 Operations that preserve convexity of convex set
chapter: '02'
order: 9
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

This section discusses operations that preserve the convexity of convex sets. These operations are useful for determining convexity or constructing desired convex sets from simple ones like hyperplanes, halfspaces, and norm balls.

Operations that preserve convexity include:

* Intersection
* Affine functions
* Perspective function
* Linear-fractional functions

## Intersection

The intersection of convex sets is convex. That is, if $$S_1$$ and $$S_2$$ are convex, then $$S_1 \cap S_2$$ is convex. This property holds even for infinitely many sets. (Subspaces, affine sets, and convex cones are also closed under intersection.)

Convexity can be expressed as the intersection of infinitely many halfspaces, and the converse also holds. That is, a closed convex set $$S$$ can be defined as the intersection of all halfspaces containing $$S$$:

> $$S = \bigcap \{\mathcal{H} \mid \mathcal{H} \text{ halfspace }, S \subseteq \mathcal{H}\}$$

## Affine functions

Let $$A \in \mathbb{R}^{m \times n}$$ and $$b \in \mathbb{R}^{m}$$. The function $$f : \mathbb{R}^n \to \mathbb{R}^m$$ defined by $$f(x) = Ax + b$$ is called an affine function.

If $$C \subseteq \mathbb{R}^n$$ is convex and $$D \subseteq \mathbb{R}^m$$ is convex, then:

* The affine image $$f(C) = \{f(x) \mid x \in C\}$$ is convex.
* The affine preimage $$f^{-1}(D) = \{x \mid f(x) \in D\}$$ is convex.

Applying affine functions such as scaling and translation, projection, sum of two sets, and partial sum to convex sets results in convex sets.

The solution set of a linear matrix inequality $$\{x \mid x_1 A_1 + \cdots + x_m A_m \preceq B\}$$ (with $$A_i, B \in S^n$$) is also convex.

A hyperbolic cone $$\{x \mid x^T P x < (c^T x)^2, c^T x > 0\}$$ (with $$P \subseteq S^n_+$$, $$c \in \mathbb{R}^n$$) is also convex.

## Perspective function

The **perspective function** models how objects appear smaller when farther away and larger when closer, similar to how a camera projects images. The object is in $$\mathbb{R}^{n+1}$$ and its image is in $$\mathbb{R}^n$$.

The perspective function is defined as $$P : \mathbb{R}^{n+1} \to \mathbb{R}^{n}$$ with **dom** $$P = \mathbb{R}^{n} \times \mathbb{R}_{++}$$ and $$P(z,t) = z/t$$, where $$\mathbb{R}_{++} = \{x \in \mathbb{R} \mid x > 0\}$$. This function normalizes the last coordinate to 1 and drops it, reducing the dimension from $$\mathbb{R}^{n+1}$$ to $$\mathbb{R}^n$$. If $$C \subseteq$$ **dom** $$P$$ is convex, then the image $$P(C) = \{P(x) \mid x \in C\}$$ is also convex.

The perspective function works like a pinhole camera: objects farther from the pinhole are projected smaller. The figure below illustrates this principle, showing that objects within the same captured ray are projected identically.

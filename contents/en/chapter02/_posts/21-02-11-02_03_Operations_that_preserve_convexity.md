---
layout: post
title: 02-03 Operations that preserve convexity of convex set
chapter: '02'
order: 11
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

Checking the line-segment definition $$\theta x + (1-\theta)y \in C$$ directly on a messy feasible region with 50 constraints is tedious and error-prone. Instead, convex analysts use a compositional calculus: start from simple convex building blocks (halfspaces, balls, cones) and apply operations guaranteed to preserve convexity—intersection, affine maps, perspective maps, and linear-fractional maps—to certify convexity in two lines.

## Key ideas: The Calculus of Convex Sets

- **Arbitrary Intersections:** If every $$S_\alpha$$ is convex (even uncountably many!), $$\bigcap_\alpha S_\alpha$$ is convex—this single rule proves polyhedra, $$\mathbb{S}_+^n$$, and robust uncertainty constraints are convex.
- **Affine Images & Preimages:** If $$S$$ is convex and $$f(x) = Ax + b$$ is affine, both the image $$f(S)$$ (scaling, rotation, translation, projection) and inverse image $$f^{-1}(S)$$ are convex.
- **Minkowski Sums & Direct Products:** Sums $$S_1 + S_2$$ and Cartesian products $$S_1 \times S_2$$ of convex sets stay convex, letting us combine independent constraint blocks cleanly.
- **Perspective & Linear-Fractional Functions:** $$P(z, t) = z/t$$ (for $$t > 0$$) and compositions $$x \mapsto \frac{Ax + b}{c^T x + d}$$ (for $$c^T x + d > 0$$) preserve convexity of both images and preimages—key to geometric and fractional programming.

### Worked example: Affine Image and Perspective Map on Simple Convex Sets

1. **Affine image of the unit square $$S = [0, 1]^2$$:** Apply $$f(x) = Ax + b$$ with
   $$A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}, \qquad b = \begin{pmatrix} 1 \\ -1 \end{pmatrix}.$$
   Evaluate $$f$$ on the four vertices of $$S$$:
   - $$f(0, 0) = (1, -1)^T$$, $$f(1, 0) = (3, -1)^T$$, $$f(0, 1) = (2, 2)^T$$, $$f(1, 1) = (4, 2)^T$$.
   Because affine maps preserve convex combinations, $$f(S)$$ is the convex parallelogram spanned by these four vertices. Check the midpoint $$(0.5, 0.5)^T \in S$$: $$f(0.5, 0.5) = (2.5, 0.5)^T$$, which equals the average of all four image vertices.
2. **Perspective normalization:** Apply $$P(z, t) = z/t$$ ($$t > 0$$) to the ray point $$(z_1, z_2, t) = (2, 4, 2)$$ in $$\mathbb{R}^2 \times \mathbb{R}_{++}$$:
   $$P(2, 4, 2) = \left(\frac{2}{2}, \frac{4}{2}\right) = (1, 2).$$
   Scaling the input to $$(6, 12, 6)$$ maps to the exact same normalized point $$(1, 2)$$, illustrating how perspective projects cones cleanly onto convex slices.

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

---
layout: post
title: 03 Convex functions
chapter: '03'
order: 1
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

Chapter 02 taught us how to build well-behaved feasible *regions*; Chapter 03 teaches us how to recognize and construct well-behaved *objectives*—convex functions, their Fenchel conjugates, quasiconvex extensions, and log-concave densities. Once you see that a function's convexity is simply the convexity of the bowl-shaped set sitting above its graph (its epigraph), every theorem in this chapter locks together into one unified picture.

## Key ideas: The Architecture of Chapter 03

- **Core Characterizations:** Connect the chord inequality (definition), tangent lower bounds (first-order), nonnegative curvature (second-order), and epigraph geometry.
- **Convexity-Preserving Calculus:** Build complex convex objectives (like regularized logistic or Huber losses) from simple atoms via weighted sums, compositions, pointwise maxima, and perspective.
- **Fenchel Conjugacy ($$f^*$$):** Dualizes a convex function by re-indexing it by slope instead of position—the algebraic heart of Lagrange duality and proximal operators.
- **Generalized Convexity:** Extend convexity to unimodal *quasiconvex* functions (solved via convex feasibility bisection), *log-concave* probability densities, and vector-valued *$$K$$-convex* functions.

### Worked example: Checking the Chord Inequality on $$f(x) = x^2$$

Test $$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$$ on $$f(x) = x^2$$ with $$x = 0$$, $$y = 4$$, and $$\theta = 0.25$$.

1. **Compute the convex combination of inputs and its function value:**
   $$z = 0.25(0) + 0.75(4) = 3 \implies f(z) = 3^2 = 9.$$
2. **Compute the matching point on the secant chord connecting $$(0, 0)$$ and $$(4, 16)$$:**
   $$0.25 f(0) + 0.75 f(4) = 0.25(0) + 0.75(16) = 12.$$
3. **Compare:** $$9 < 12$$, showing that the graph of $$x^2$$ bows strictly beneath its chord—a visual signature of strict convexity.

In this chapter, we will study the definition, examples, key properties of convex functions, and operations that preserve convexity.

An optional follow-up, [03-08 Applications and recent developments]({% multilang_post_url contents/chapter03/2026-09-16-03_08_Applications_Recent %}), revisits log-sum-exp in calibration, neural collapse, and contrastive losses.

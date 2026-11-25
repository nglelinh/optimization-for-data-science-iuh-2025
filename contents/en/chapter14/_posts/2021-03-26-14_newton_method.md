---
layout: post
title: 14 Newton's Method
chapter: '14'
order: 1
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

Picture descending a steep, narrow canyon in thick fog. Gradient descent feels only the local slope under your boots, so it zigzags endlessly from one canyon wall to the other. Newton's method pulls out a curvature map—the Hessian matrix $$\nabla^2 f(x)$$—fits a local parabolic bowl to the terrain, and jumps directly to the bottom of that bowl, doubling the number of accurate decimal digits on every single step once you are close to the solution.

## Background Knowledge Map: The Architecture of Second-Order Optimization

- **Pillar 1 — Local Quadratic Modeling:** Replacing $$f$$ at $$x$$ with its second-order Taylor expansion turns a general nonlinear minimization into a closed-form linear system $$\nabla^2 f(x)\,\Delta x_{\text{nt}} = -\nabla f(x)$$.
- **Pillar 2 — Affine Invariance & Conditioning Immunity:** Because $$\nabla^2 f(x)^{-1}$$ rescales every direction by its exact local curvature, Newton's method is completely blind to poorly scaled coordinates or stretched level sets.
- **Pillar 3 — Damped Global Convergence + Quadratic Local Finish:** Pairing Newton's direction with backtracking line search guarantees steady global decrease first (damped phase) and explosive $$O(\log\log(1/\epsilon))$$ quadratic convergence near $$x^\star$$ (pure phase).
- **Pillar 4 — Self-Concordance & Practical Trade-Offs:** Self-concordant functions yield affine-invariant iteration bounds free of unknown Lipschitz constants, while structured Hessians and quasi-Newton methods tame the $$O(n^3)$$ cost of solving dense linear systems.

### Step-by-Step Worked Example (Read Slowly): Watching Quadratic Convergence on a 1D Convex Function

Consider minimizing $$f(x) = e^x + e^{-x} - 2x$$ (strictly convex, since $$f''(x) = e^x + e^{-x} > 0$$) starting from $$x^{(0)} = 0$$. Its exact minimizer satisfies $$f'(x^\star) = e^{x^\star} - e^{-x^\star} - 2 = 0 \implies \sinh(x^\star) = 1 \implies x^\star = \ln(1 + \sqrt{2}) \approx 0.8813736$$.

1. **Iteration 1 (at $$x^{(0)} = 0$$):**
   - $$f'(0) = 1 - 1 - 2 = -2$$, $$\quad f''(0) = 1 + 1 = 2$$.
   - Newton update: $$x^{(1)} = 0 - \frac{-2}{2} = 1.0$$. Error drops from $$0.8814$$ to $$|1.0 - 0.8814| = 0.1186$$.
2. **Iteration 2 (at $$x^{(1)} = 1.0$$):**
   - $$f'(1) = e - e^{-1} - 2 \approx 2.71828 - 0.36788 - 2 = 0.35040$$.
   - $$f''(1) = e + e^{-1} \approx 3.08616$$.
   - Newton update: $$x^{(2)} = 1.0 - \frac{0.35040}{3.08616} \approx 0.88646$$. Error collapses from $$0.1186$$ to $$0.00509$$!
3. **Iteration 3 (at $$x^{(2)} \approx 0.88646$$):**
   - $$f'(0.88646) \approx 0.01441$$, $$\quad f''(0.88646) \approx 2.8386$$.
   - Newton update: $$x^{(3)} \approx 0.88646 - 0.00508 = 0.88138$$. Error plunges to $$\approx 10^{-5}$$—doubling the accurate digits in a single step!

In this chapter, we look at Newton's Method.

Newton's method is an approach for finding the minimum of a function with a twice differentiable function using the second-order Taylor expansion. It finds the minimum by approximating the function and iteratively updating the solution. Near the optimum, it achieves quadratic convergence and is much faster than gradient descent.

## References and further readings
* S. Boyd and L. Vandenberghe (2004), "Convex optimization", Chapter 9 and 10
* Y. Nesterov (1998), "Introductory lectures on convex optimization: a basic course", Chapter 2
* Y. Nesterov and A. Nemirovskii (1994), "Interior-point polynomial methods in convex programming", Chapter 2
* J. Nocedal and S. Wright (2006), "Numerical optimization", Chapters 6 and 7
* L. Vandenberghe, Lecture notes for EE 236C, UCLA, Spring 2011-2012

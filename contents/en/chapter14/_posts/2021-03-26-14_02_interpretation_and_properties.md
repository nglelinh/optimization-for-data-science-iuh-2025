---
layout: post
title: 14-02 Interpretation & Properties
chapter: '14'
order: 5
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

Why has a 300-year-old root-finding algorithm remained the gold standard of numerical optimization in the 21st century? Before diving into full convergence proofs, we step back to see the three conceptual pillars that make Newton's method unique: its equivalence to finding a root of $$\nabla f(x) = 0$$, its complete immunity to linear coordinate rescaling (affine invariance), and its explosive local convergence rate.

## Background Knowledge Map: Core Structural Properties of Newton's Method

- **Pillar 1 — Optimization as Root Finding:** For unconstrained smooth convex functions, minimizing $$f(x)$$ is identical to solving the nonlinear system $$F(x) = \nabla f(x) = 0$$, where the Jacobian $$DF(x)$$ is the Hessian $$\nabla^2 f(x)$$.
- **Pillar 2 — Affine Invariance:** Changing variables via $$x = Ay$$ (for any invertible $$A$$) leaves the Newton trajectory completely unchanged: $$x^{(k)} = A y^{(k)}$$ at every iteration $$k$$.
- **Pillar 3 — Local Quadratic Convergence:** Once $$x^{(k)}$$ enters a neighborhood of $$x^\star$$ with nonsingular, Lipschitz Hessian, the error shrinks like $$\|x^{(k+1)} - x^\star\| \le K \|x^{(k)} - x^\star\|^2$$.
- **Pillar 4 — The Need for Globalization:** Because pure Newton can overshoot or diverge far from $$x^\star$$, these local properties motivate adding backtracking line search in the next sections.

### Step-by-Step Worked Example (Read Slowly): Seeing Root-Finding and Affine Invariance Together

Consider minimizing $$f(x) = \frac{1}{2}x^2 - \ln(x)$$ on $$x > 0$$ (minimum at $$x^\star = 1$$) and its rescaled twin $$g(y) = f(5y) = \frac{25}{2}y^2 - \ln(5y)$$ (minimum at $$y^\star = 0.2$$).

1. **Root-finding view of $$f$$:** Set $$F(x) = f'(x) = x - \frac{1}{x} = 0$$ with $$F'(x) = f''(x) = 1 + \frac{1}{x^2}$$.
   Starting at $$x^{(0)} = 2$$:
   $$x^{(1)} = 2 - \frac{2 - 0.5}{1 + 0.25} = 2 - \frac{1.5}{1.25} = 2 - 1.2 = 0.8.$$
2. **Now run Newton on the rescaled function $$g(y)$$ from $$y^{(0)} = \frac{x^{(0)}}{5} = 0.4$$:**
   - $$g'(y) = 25y - \frac{1}{y} \implies g'(0.4) = 10 - 2.5 = 7.5$$.
   - $$g''(y) = 25 + \frac{1}{y^2} \implies g''(0.4) = 25 + 6.25 = 31.25$$.
   - $$y^{(1)} = 0.4 - \frac{7.5}{31.25} = 0.4 - 0.24 = 0.16.$$
3. **Check affine invariance:** $$5 y^{(1)} = 5(0.16) = 0.8 = x^{(1)}$$! Even though the gradient and curvature blew up by factors of $$5$$ and $$25$$, Newton's path is mathematically identical.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In this chapter, before examining the properties of Newton's method, we learn about applying Newton's method to root finding problems of objective functions.

Subsequently, we will examine two important properties of Newton's method: Affine invariance and Local convergence.
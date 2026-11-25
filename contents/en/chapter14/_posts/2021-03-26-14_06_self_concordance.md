---
layout: post
title: 14-06 Self concordance
chapter: '14'
order: 12
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

There is an embarrassing paradox in the classical convergence proof of Section 14-05: Newton's method itself is completely affine invariant, yet its classical iteration bound depends heavily on the constants $$m, L, M$$—which change wildly whenever you rescale your coordinates, and are almost never known in practice (and blow up to $$\infty$$ for log barriers!). Nesterov and Nemirovskii resolved this paradox with a single brilliant property: **self-concordance**.

## Key ideas: Why Self-Concordance Was Invented

- **Pillar 1 — Eliminating Unknown Constants ($$m, L, M$$):** Classical bounds fail on functions like $$-\log(x)$$ whose Hessian $$1/x^2$$ is unbounded near $$0$$; self-concordance bounds the third derivative *relative to the local second derivative*.
- **Pillar 2 — Affine-Invariant Theory Matching an Affine-Invariant Algorithm:** Because self-concordance is preserved under all invertible affine maps $$x = Ay + b$$, its iteration-complexity bound is completely independent of coordinate scaling.
- **Pillar 3 — The Engine of Interior-Point Methods:** Logarithmic barrier functions $$-\sum \log(-h_i(x))$$ are self-concordant, which is why interior-point methods enjoy polynomial-time global complexity guarantees in Chapter 15.
- **Pillar 4 — Scale-Free Neighborhoods via $$\lambda(x)$$:** For self-concordant functions, the Newton decrement $$\lambda(x)$$ alone dictates when backtracking stops and quadratic convergence begins—no $$m$$ or $$M$$ needed.

### Worked example: Why Classical Constants Fail on $$f(x) = -\log x$$ While Self-Concordance Succeeds

Consider $$f(x) = -\log(x)$$ on $$\operatorname{dom}(f) = (0, \infty)$$.

1. **Test the classical Lipschitz conditions from Section 14-05:**
   - $$f''(x) = \frac{1}{x^2}$$ and $$f'''(x) = -\frac{2}{x^3}$$.
   - As $$x \to 0^+$$, $$f''(x) \to +\infty$$ (so no finite upper bound $$L$$ exists) and $$|f'''(x)| \to +\infty$$ (so no finite Hessian Lipschitz constant $$M$$ exists!).
   - As $$x \to +\infty$$, $$f''(x) \to 0$$ (so no positive strong-convexity constant $$m > 0$$ exists!).
   - Conclusion: Classical $$m, L, M$$ analysis says *nothing* about $$-\log(x)$$.
2. **Test the self-concordance ratio $$\frac{|f'''(x)|}{2 (f''(x))^{3/2}}$$:**
   $$\frac{|f'''(x)|}{2\,(f''(x))^{3/2}} = \frac{2/x^3}{2\,(1/x^2)^{3/2}} = \frac{2/x^3}{2/x^3} = 1 \quad \text{for ALL } x > 0!$$
3. **Check affine invariance under $$g(y) = -\log(ay)$$ ($$a > 0$$):**
   - $$g''(y) = 1/y^2$$, $$g'''(y) = -2/y^3$$—the ratio is *still* identically $$1$$ for every $$a > 0$$!

In the previous convergence analysis of Newton's method, there are two major issues. [1]

First, in practical problems, it is difficult to find the Lipschitz constant L, the lower and upper bounds of strong convexity m, M, etc., which are included in the formulas. Because of this, while we can observe convergence and convergence rate, it is almost impossible to analyze how many Newton steps are needed in practice.

Second, although Newton's method itself is affine invariant, the convergence analysis of Newton's method is not affine invariant. For general functions, the values of the Lipschitz constant or strong convexity bounds change depending on the coordinate transformation.

Therefore, in this chapter, we introduce self-concordant functions, which address the above two issues.

Self-concordant functions are important and meaningful for three main reasons:

1. The log barrier functions used in interior-point methods are self-concordant functions.
2. In the analysis of Newton's method for self-concordant functions, terms involving constants do not appear.
3. Self-concordance is affine-invariant. That is, the number of Newton iterations required is independent of affine transformations of the coordinate system.
---
layout: post
title: 14-06-01 Definition of self-concordant functions
chapter: '14'
order: 13
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

How do you guarantee that a function's curvature doesn't change too violently as you take a Newton step, *without* fixing a global Euclidean scale? You measure the rate of change of curvature ($$|f'''(x)|$$) in units of the current curvature itself ($$f''(x)^{3/2}$$). That dimensionless inequality, $$|f'''(x)| \le 2 f''(x)^{3/2}$$, is the exact definition of a self-concordant function.

## Key ideas: Calculus of Self-Concordant Functions

- **Pillar 1 — The 1D Defining Inequality:** A $$C^3$$ convex function $$f: \mathbb{R} \to \mathbb{R}$$ is self-concordant iff $$|f'''(x)| \le 2 f''(x)^{3/2}$$ everywhere on its domain (equivalently, $$\left|\frac{d}{dx}\big(f''(x)^{-1/2}\big)\right| \le 1$$).
- **Pillar 2 — Lifting to $$\mathbb{R}^n$$ via Line Restrictions:** A multivariate function $$f: \mathbb{R}^n \to \mathbb{R}$$ is self-concordant iff every 1D slice $$g(t) = f(x + tv)$$ is self-concordant in $$t$$.
- **Pillar 3 — Closure Under Addition and Affine Composition:** Sums of self-concordant functions are self-concordant (via $$(u^{3/2} + v^{3/2})^{2/3} \le u + v$$), and composing with $$Ax + b$$ preserves self-concordance automatically.
- **Pillar 4 — Canonical Building Blocks:** Affine functions, convex quadratics ($$f''' = 0$$), $$-\log(x)$$, and $$-\log\det(X)$$ on $$\mathbb{S}^n_{++}$$ are all self-concordant—forming the toolkit for LP, QP, SOCP, and SDP barriers.

### Worked example: Checking Which Functions Are Self-Concordant

Test three 1D convex functions against $$|f'''(x)| \le 2 f''(x)^{3/2}$$:

1. **Log-barrier of a linear inequality $$f(x) = -\log(b - ax)$$ on $$ax < b$$:**
   - $$f'(x) = \frac{a}{b-ax}$$, $$\quad f''(x) = \frac{a^2}{(b-ax)^2}$$, $$\quad f'''(x) = \frac{2a^3}{(b-ax)^3}$$.
   - Check: $$|f'''(x)| = \frac{2|a|^3}{(b-ax)^3} = 2\left(\frac{a^2}{(b-ax)^2}\right)^{3/2} = 2 f''(x)^{3/2}$$. **Self-concordant!**
2. **Scaled logarithm $$f(x) = -\alpha \log(x)$$ ($$\alpha > 0$$):**
   - $$f''(x) = \frac{\alpha}{x^2}$$, $$\quad |f'''(x)| = \frac{2\alpha}{x^3}$$.
   - Compare with $$2 f''(x)^{3/2} = \frac{2\alpha^{3/2}}{x^3}$$.
   - Holds iff $$\alpha \le \alpha^{3/2} \iff \alpha \ge 1$$! Thus $$-0.5\log(x)$$ is *not* self-concordant, while $$-2\log(x)$$ is.
3. **Exponential $$f(x) = e^x$$ on $$\mathbb{R}$$:**
   - $$f''(x) = e^x$$, $$f'''(x) = e^x$$. Condition requires $$e^x \le 2 e^{3x/2} \iff e^{-x/2} \le 2$$, which **fails** as $$x \to -\infty$$! Thus $$e^x$$ is *not* self-concordant.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>
## Self-concordant on $$R$$
A convex function $$f : R \rightarrow R$$ is defined as self-concordant when it satisfies the following equation:
>$$\begin{align}
>\|f^{'''}(x)\| \leq 2f^{''}(x)^{3/2} \qquad \text{for all }x\in \text{dom }f.
>\end{align}$$

As simple examples, linear functions ($$ax+b$$) and (convex) quadratic functions are self-concordant because their third derivative values are 0.

## Self-concordant on $$R^{n}$$
A function $$f : R^{n}\rightarrow R$$ is defined as self-concordant when it is self-concordant for any line segment within the domain, that is, for all line segments included in the domain. For example, for all $$x\in dom\, f$$ and all $$v$$, when $$g(t) = f(x+tv)$$ is defined, if $$g(t)$$ is self-concordant, then f is defined as a self-concordant function in the domain of $$\mathbb{R}^{n}$$.

## Example of self-concordance function

1) $$f : \mathbb{R}^{n}_{++}\rightarrow \mathbb{R}$$, $$f(x) = -\sum^{n}_{i=1}log(x_{i})$$.

It can be easily verified that $$f(t) = -\log{t}$$. Furthermore, the sum of self-concordant functions is also self-concordant. When there are self-concordant functions $$f_{1}, f_{2} : R\rightarrow R$$, the sum of self-concordant functions is also self-concordant as shown below.[3]
>$$\begin{align}
>|f_{1}^{'''}(x)+f_{2}^{'''}(x)|  \leq & |f^{'''}_{1}(x)|+|f^{'''}_{2}(x)|\\\\
> \leq &2\big( f^{''}_{1}(x)^{3/2}+f^{''}_{2}(x)^{3/2}\big)\\\\
>\leq &2\big( f^{''}_{1}(x)+f^{''}_{2}(x) \big)^{3/2}.
>\end{align}$$

The last step uses the following property:
>$$\begin{align}
>(u^{3/2}+v^{3/2})^{2/3} \leq u+v, \qquad u, v \geq 0.
>\end{align}$$


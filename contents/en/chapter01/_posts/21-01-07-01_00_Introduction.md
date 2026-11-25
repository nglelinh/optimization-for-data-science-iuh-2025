---
layout: post
title: 01 Introduction
chapter: '01'
order: 1
owner: Kyeongmin Woo
categories:
- chapter01
lang: en
lesson_type: required
---

In 1993, R. Tyrrell Rockafellar wrote a sentence that reshaped modern applied mathematics: *"The great watershed in optimization isn't between linearity and nonlinearity, but convexity and nonconvexity."* Chapter 01 opens the door to why that watershed matters—showing how casting an engineering, finance, or machine learning problem in convex form transforms an intractable search through exponential local traps into a reliable, polynomial-time computation.

## Key ideas: The Architecture of Chapter 01

- **Standard Problem Formulation:** Translating real-world decisions into decision variables $$x$$, an objective $$f_0(x)$$, inequality constraints $$f_i(x) \le 0$$, and equality constraints $$h_j(x) = 0$$.
- **The Convexity Watershed:** Recognizing when the objective and feasible region are convex so that *every local minimum is automatically a global minimum*.
- **Modeling vs. Algorithm Selection:** Understanding the two-step workflow of recognizing/reformulating convexity first, then matching problem structure (LP, QP, SOCP, SDP, nonsmooth composite) to specialized solvers.
- **Historical & Modern Perspective:** Tracing how simplex, ellipsoid, interior-point, and modern first-order splitting methods made convex optimization a universal computational primitive.

### Worked example: Nonconvex Traps vs. Convex Global Certifiability

Compare two 1D unconstrained objectives: $$f_1(x) = x^4 - 4x^2 + x$$ (nonconvex) and $$f_2(x) = x^2 - 4x + 5$$ (convex).

1. **Analyze the nonconvex function $$f_1(x)$$:**
   $$f_1'(x) = 4x^3 - 8x + 1, \qquad f_1''(x) = 12x^2 - 8.$$
   - At $$x \approx 1.35$$, $$f_1'(1.35) \approx 0$$ and $$f_1''(1.35) \approx 13.87 > 0$$, giving a **local minimum** $$f_1(1.35) \approx -2.62$$.
   - At $$x \approx -1.47$$, $$f_1'(-1.47) \approx 0$$ and $$f_1''(-1.47) \approx 17.93 > 0$$, giving a strictly lower **global minimum** $$f_1(-1.47) \approx -5.45$$.
   A local solver started at $$x_0 = 2$$ gets permanently trapped at $$x \approx 1.35$$.
2. **Analyze the convex function $$f_2(x)$$:**
   $$f_2'(x) = 2x - 4 = 0 \implies x^* = 2, \qquad f_2''(x) = 2 > 0 \text{ everywhere}.$$
   From *any* starting point $$x_0 \in \mathbb{R}$$, descent converges to the unique global minimum $$f_2(2) = 1$$.

This chapter is the front door to the course: what an optimization problem *is*, why **convex** problems are the ones we can certify, and what the rest of the semester will buy you as a data-science student.

A mathematical program asks for a point $$x$$ in a feasible set that makes an objective as small (or as large) as possible:

$$
\begin{align}
\underset{x}{\text{minimize}} \quad & f(x) \\
\text{subject to} \quad & x \in \mathcal{C}.
\end{align}
$$

In machine learning the same template is everywhere. Training a predictor is usually **empirical risk minimization**

$$
\min_w \frac{1}{n}\sum_{i=1}^n \ell\bigl(h_w(x_i), y_i\bigr) + \lambda R(w),
$$

with $$\ell$$ a loss and $$R$$ a regularizer. Feature selection, portfolio weights, maximum-likelihood parameters, and the dual of a support-vector machine are the same idea with different $$f$$ and $$\mathcal{C}$$.

**Convex** programs — convex $$f$$ over a convex $$\mathcal{C}$$ — are special: every local minimizer is global, first-order conditions are often sufficient, and we have reliable algorithms (gradient, proximal, interior-point). Nonconvex deep networks still use those algorithms; [Chapter 28]({{ site.baseurl }}/contents/en/chapter28/) asks why the landscape is often kinder than the worst-case theory.

## What this chapter contains

1. **Optimization problems** — variables, objectives, constraints, feasibility.
2. **Convex optimization problems** — the definition you will reuse every week.
3. **Goals and topics** — how Chapters 02–25 (classical spine) and 26–29 (2026 modern track) fit together.
4. **A brief history** — from linear programming to autodiff-driven deep learning.

Read the next lesson for the standard form with inequality and equality constraints; then decide, for a problem you already know (least squares, logistic regression, *k*-means), which pieces are convex.

An optional close-out, [01-05 Applications and recent developments]({% multilang_post_url contents/chapter01/2026-09-16-01_05_Applications_Recent %}), applies the same template to compute-optimal LLMs, predict-then-optimize, and fairness constraints.

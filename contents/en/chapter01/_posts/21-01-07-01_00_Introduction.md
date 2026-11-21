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

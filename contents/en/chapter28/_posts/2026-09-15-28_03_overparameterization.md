---
layout: post
title: 28-03 Overparameterization
chapter: '28'
order: 4
owner: Nguyen Le Linh
categories:
- chapter28
lang: en
lesson_type: required
---


A model is **overparameterized** when the number of parameters $$d$$ substantially exceeds the number of effective constraints coming from the data (classically $$d \gg n$$ for interpolating $$n$$ scalar labels). Then the equation $$F(w)=0$$ (or “train loss $$\approx 0$$”) can have a **huge set** of solutions. Training is no longer “find the unique minimizer”; it is “which interpolator does the algorithm pick?”

That is the implicit-bias viewpoint: gradient descent on an underdetermined least-squares problem converges to the **min-norm** interpolator in the span of the features; on separable linear classification it maximizes the margin in the limit (Soudry et al., and a large follow-up literature). Deep nets are not linear, but the slogan remains: **the optimizer is part of the inductive bias**.

Overparameterization also changes the *shape* of $$F$$. In many random-feature and wide-net limits the loss becomes *locally* benign: once you are close enough, every critical point that SGD finds interpolates, and saddles become less relevant than **which** interpolating point you land on. This is why “nonconvex ⇒ unusable local minima” is the wrong slogan for modern deep learning, even though the function is still nonconvex.

**Polyak–Łojasiewicz (PL) condition** (pointer, not a full lecture). If

$$
\tfrac12 \|\nabla F(w)\|_2^2 \ge \mu \bigl(F(w)-F^\star\bigr)
$$

for some $$\mu>0$$, then gradient descent enjoys a linear rate *without convexity*. Some overparameterized least-squares and certain wide-net regimes satisfy PL locally. The optional lesson [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}) reuses the Chapter 06 proof on that inequality (Karimi, Nutini, Schmidt, [arXiv:1608.04636](https://arxiv.org/abs/1608.04636)); this page only needs the slogan.

**Exercise.** Fit $$n=20$$ scalar points with a degree-$$50$$ polynomial by (i) the numpy least-squares min-norm solution and (ii) GD from two random starts. Compare test error on a smooth underlying function. Same train loss, different interpolators.

---
layout: post
title: 22 Conditional Gradient (Frank-Wolfe) Method
chapter: '22'
order: 1
owner: YoungJae Choung
categories:
- chapter22
lang: en
---

This chapter will examine the Frank-Wolfe algorithm proposed by Marguerite Frank and Philip Wolfe in 1956.

The Frank-Wolfe algorithm is an iterative first-order optimization algorithm for constrained convex optimization, also called the conditional gradient method, reduced gradient method, and convex combination algorithm.

This method was originally proposed by Marguerite Frank and Philip Wolfe in 1956. The Frank-Wolfe algorithm considers a linear approximation of the objective function at each iteration and moves toward the minimizer of this linear function.

[15] Wikipedia. [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)

## 2026 applications (optional)

The linear-minimization oracle is why Frank–Wolfe survived into the 2020s: structured SVMs, semi-relaxed optimal transport (color transfer), 1-D unbalanced OT, and constrained explanations of neural nets (rate-distortion maps on an $$\ell_1$$ ball or the Birkhoff polytope). See the optional survey [22-06 Modern applications of Frank–Wolfe]({% multilang_post_url contents/chapter22/2026-09-16-22_06_modern_applications %}). Use it after 22-02 / 22-04, not instead of the convergence analysis.

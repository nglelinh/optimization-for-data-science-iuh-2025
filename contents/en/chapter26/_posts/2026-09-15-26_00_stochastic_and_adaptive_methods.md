---
layout: post
title: 26 Stochastic and adaptive methods for ML
chapter: '26'
order: 1
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: required
---


# Stochastic and adaptive methods for ML

Chapters 06–09 treated **full-batch** first-order methods: one gradient (or proximal step) that sees every training pair. Modern machine learning almost never does that. This chapter is the 2026 default stack for empirical risk minimization

$$
\min_w F(w) = \frac{1}{n}\sum_{i=1}^n f_i(w), \qquad f_i(w) = \ell\bigl(h_w(x_i), y_i\bigr).
$$

You already met a cousin in [06-05 Stochastic gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %}) and the stochastic subgradient notes in Chapter 08. Here we treat SGD and minibatches as *the* algorithm, then add the two ingredients every deep-learning library ships: **momentum / Nesterov** and **diagonal adaptive scaling** (AdaGrad → RMSProp intuition → Adam → AdamW). A last lesson surveys variance reduction (SVRG / SAGA) so you know when the convex theory is sharper than Adam.

## Why a separate chapter

Full-batch gradient descent on ImageNet or a language-model corpus is not a step-size problem — it is a *memory and wall-clock* problem. An unbiased (or nearly unbiased) gradient estimator built from one example or a minibatch of size $$B\ll n$$ lets us take many more parameter steps per hour. The price is noise. Adaptive methods spend that noise on a per-coordinate learning rate; momentum spends it on a velocity that remembers consistent directions.

Peer syllabi that treat this as core rather than a remark: MIT 6.7220 (S25), EPFL CS-439, USC CSCI 599, BU EC525.

## Lessons

1. SGD and minibatches — estimators, shuffling, the $$O(1/\sqrt{T})$$ story
2. Momentum and Nesterov — heavy ball vs look-ahead; Distill-style intuition
3. AdaGrad to Adam — diagonal preconditioning
4. AdamW and training practice — decoupled weight decay, schedules, clipping
5. Variance reduction (survey) — SVRG / SAGA, and when mini-batch Adam still wins
6. Modern adaptive optimizers (optional survey) — SAM, Sophia, Muon against the AdamW baseline

Interactive SGD cartoons sit in [`interactive_math/optimization`](https://github.com/nglelinh/interactive_math/tree/main/optimization). SAM, Muon, and Sophia stay **further reading** — not assessed this term — but they now have a dedicated optional lesson: [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %}).

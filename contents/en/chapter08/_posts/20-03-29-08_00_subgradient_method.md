---
layout: post
title: '08 Subgradient Method'
chapter: '08'
order: 1
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

In this section, we will look at the subgradient method, which can be applied to convex functions that may not be differentiable, using the concept of subgradients. We will also explore the convergence properties and rate of the subgradient method with examples.

## Modern applications (2022–2026)

An optional companion lesson places the same (projected, stochastic) subgradient loop in adversarial PGD / RobustBench, Fairlearn rate constraints, and nonsmooth ReLU training. See [08-11 Modern applications of the subgradient method]({% multilang_post_url contents/chapter08/2026-09-16-08_11_modern_applications %}). When the finite-sum objective *is* smooth, the $$O(1/\sqrt{T})$$ noise floor of this chapter’s stochastic method can be removed by SVRG / SAGA — that lesson is [26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %}), next to the SGD track.
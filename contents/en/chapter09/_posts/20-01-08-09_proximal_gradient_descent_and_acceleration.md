---
layout: post
title: Proximal gradient descent and acceleration
chapter: '09'
order: 1
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

# Proximal gradient descent and acceleration

This chapter introduces proximal gradient descent and acceleration techniques for optimization problems involving composite functions.

## Overview
- Proximal gradient descent is used for problems where the objective can be split into a differentiable part and a non-differentiable part.
- Acceleration methods, such as Nesterov's acceleration and FISTA, can improve convergence rates.

## Structure
- Section 1: Proximal gradient descent
- Section 2: Convergence analysis
- Section 3: Matrix completion example
- Section 4: Special cases
- Section 5: Acceleration methods — start at the Distill-style picture in [09-05]({% multilang_post_url contents/chapter09/20-01-08-09_05_acceleration %}), then the FISTA algebra in 09-05-01; the stochastic / constant-$$\beta$$ cousin is [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %})

Refer to each section for details and mathematical formulations.

## Modern applications (2022–2026)

An optional companion lesson follows the same proximal-gradient / FISTA template into PnP imaging, FISTA-Net / pFISTA-DR unrolling, and production elastic-net paths. See [09-06 Modern applications of proximal GD and acceleration]({% multilang_post_url contents/chapter09/2026-09-16-09_06_modern_applications %}).

---
layout: post
title: 06 Gradient Descent
chapter: '06'
order: 1
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

In this chapter, we explore **Gradient Descent**, one of the most fundamental and important methods in optimization. 

In optimization algorithms, choosing the search direction and step size is crucial for convergence speed and success. Gradient descent moves in the direction of the negative gradient. The step size can be fixed or adaptively chosen, and we will discuss both approaches in this chapter.

For gradient descent to converge, certain preconditions must be met. If these conditions are satisfied, we can analyze how quickly gradient descent converges. If strong convexity holds, convergence is even faster, and we will examine the convergence rate in such cases.

We will also look at applications of gradient descent, including gradient boosting and stochastic gradient descent.

A later optional lesson, [06-08 Applications and recent developments]({% multilang_post_url contents/chapter06/2026-09-16-06_08_Applications_Recent %}), contrasts the Lipschitz theory with the edge of stability, Lion, and schedule-free averaging (2021–2024). The linear rate of 06-03-04 can be reused on some *nonconvex* ERMs under the Polyak–Łojasiewicz condition; that bridge is the optional note [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}).
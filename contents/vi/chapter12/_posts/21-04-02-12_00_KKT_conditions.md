---
layout: post
title: 12 KKT Conditions
chapter: '12'
order: 1
owner: Wontak Ryu
categories:
- chapter12
lang: vi
---

When the primal problem is convex, the Karush–Kuhn–Tucker (KKT) conditions become sufficient conditions for primal & dual optimal points with zero duality gap. Additionally, when the objective function and constraint functions of the primal problem are differentiable and satisfy strong duality, the primal & dual optimal points always satisfy the KKT conditions. KKT conditions hold a very important position in optimization. These conditions allow some special problems to be solved analytically, and many convex optimization algorithms can be interpreted as methods for solving KKT conditions [1]. In this chapter, we will learn about the definition and properties of KKT conditions and look at some examples based on them.

*As a side note*, KKT conditions were originally introduced to the world by Harold W. Kuhn and Albert W. Tucker in 1951, and at that time they were called KT (Kuhn-Tucker) conditions. Later, scholars discovered that the necessary conditions for this problem had been addressed by William Karush's master's thesis in 1939, and from then on, Karush's name was included and they became known as KKT (Karush–Kuhn–Tucker) conditions [3].
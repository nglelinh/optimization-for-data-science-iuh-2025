---
layout: post
title: 12 KKT Conditions
chapter: "12"
order: 1
owner: "Wontak Ryu"
---

When the primal problem is convex, the Karush–Kuhn–Tucker (KKT) conditions become sufficient conditions for primal & dual optimal points with zero duality gap. Additionally, when the objective function and constraint functions of the primal problem are differentiable and satisfy strong duality, the primal & dual optimal points always satisfy the KKT conditions. KKT conditions hold a very important position in optimization. These conditions allow some special problems to be solved analytically, and many convex optimization algorithms can be interpreted as methods for solving KKT conditions [1]. In this chapter, we will learn about the definition and properties of KKT conditions and look at some examples based on them.

*여담으로* KKT conditions는 본래 Harold W. Kuhn과 Albert W. Tucker에 의해 1951년에 세상에 알려졌고, 당시에는 KT (Kuhn-Tucker) conditions로 불렸다. 그리고 이후 학자들에 의해 이 문제의 necessary conditions가 1939년 William Karush의 석사 논문에 의해 다루어졌음이 발견되었는데, 그 때부터 Karush의 이름이 포함되어 KKT (Karush–Kuhn–Tucker) conditions로 불리게 된다 [3].
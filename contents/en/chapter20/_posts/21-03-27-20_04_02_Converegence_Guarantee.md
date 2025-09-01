---
layout: post
title: 20-04-02 Converegence Guarantee
chapter: '20'
order: 10
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

$$f$$and, $$g$$to, about, 적당한 condition, 아래at, (Aand, B가 full rank일 필요는 없다), ADMM은 모든 $$\rho > 0$$about,서 다음을 만족한다. 

* **Residual convergence**: $$k$$가 $$\infty$$to, 갈 when,, $$r^{(k)} = A x^{(k)} - B z^{(k)} - c \to 0$$, that is, primal iteration이 feasibilityto, 접근한다.  
* **Objective convergence**: $$f(x^{(k)} + g(x^{(k)} \to f^{\ast} + g^{\ast}$$, 여기서 $$f^{\ast} + g^{\ast}$$는 최적의 primal objective 값이다. 
* **Dual convergence**: $$u^{(k)} \to u^{\ast}$$, 여기서 $$u^{\ast}$$는 dual solution 이다. 

정확한 convergence속도는 아직 informing,지지 않았으며, 현재 많은 연구가 진행중이다. 대략적with,는 first-order method and, 비슷하거나 약간 더 빠르게 동작한다. 

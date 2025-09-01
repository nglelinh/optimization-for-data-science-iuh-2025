---
layout: post
title: 19-03 When would we use proximal Newton?
chapter: '19'
order: 7
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

Proximal newton method는 언제 using,야 좋은가? 

Proximal newton method의 유용성을 이solution하기 for,  다음 problemabout, proximal newton methodand, proximal gradient descent를 comparing, 보자.

**Problem** : $$\min_x g(x) + h(x)$$

## Proximal gradient descent vs. proximal newton

| **Proximal gradient descent** |**Proximal Newton** | 
| -------- | -------- |
| $$\frac{1}{2} \parallel b - x \parallel_2^2 + h(x)$$ minimization  | $$b^T x + x^T A x + h(x)$$ minimization | 
| Prox operator가 대부분 closed formwith, 정의됨  | Prox operator가 대부분 closed formwith, 정의되지 않음 
| iteration이 저렴 | iteration이 아주 비쌈 (newton method보다 비쌈)| 
| Gradient descent convergence 속도 <br> $$O(1/\epsilon)$$  | Newton's method convergence 속도 <br> $$O(\log \log 1/\epsilon)$$ | 

두 method은 비슷solution 보이지만 실제 매우 다른 일을 한다. 

therefore,, proximal newton method는 아주 적은 iteration을 기대할 수 있는 scaled prox operator(quadratic + $$h$$)to, about, 빠른 inner optimizer를 가질 when, 사용할 수 있다. $$h$$가 separable function일 when, inner optimizerto, 가장 많이 사용되는 method이 coordinate descent이다.
---
layout: post
title: 19-06 Proximal quasi-Newton methods
chapter: '19'
order: 10
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

problem가 커질수록 Hessian의 computation 비용이 매우 높아진다. **Proximal quasi-Newton method**는 각 stepat, Hessian $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$를 computation하지 않는 방식with, superlinear or, linear convergence의 convergence 속도를 제공한다.

## Proximal quasi-Newton method
* Lee (2014)는 Hessian을  BFGS-styleto, update하는 방식을 제안했다. 이 method은 매우 잘 실행되며 local superlinear convergence의 convergence 속도를 갖는다.
* Tseng and Yun (2009)은  Hessian을 blockwiseto, approximation하는 방식을 제안했다. 이 method은 $$f = g + h$$at, $$h$$가 일부 optimization variableto, 의존하는 부분with, 나뉠 수 있을 when,만 작동한다. Hessian을 blockwiseto, computation하면 computation이 매우 빨라진다. 이 method은 linear convergence의 convergence 속도를 갖는다.

Quasi-Newton은 Hessian computation이 힘들when, 뿐 아니라 Hessian이 singular이거나 near singular인 ill-conditionat,도 유용하다.

#### reference 논문
* J. Lee and Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions"
* P. Tseng and S. Yun (2009), "A coordinate gradient descent method for nonsmooth separable minimization"

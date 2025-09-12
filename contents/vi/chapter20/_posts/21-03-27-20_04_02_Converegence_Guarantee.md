---
layout: post
title: 20-04-02 Convergence Guarantee
chapter: '20'
order: 10
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

# Convergence Guarantee for ADMM

Under appropriate conditions on $$f$$ and $$g$$ (note that $$A$$ and $$B$$ do not need to be full rank), ADMM satisfies the following for all $$\rho > 0$$:

* **Residual convergence**: As $$k \to \infty$$, $$r^{(k)} = Ax^{(k)} + Bz^{(k)} - c \to 0$$, meaning the primal iterates approach feasibility.

* **Objective convergence**: $$f(x^{(k)}) + g(z^{(k)}) \to f^{\ast} + g^{\ast}$$, where $$f^{\ast} + g^{\ast}$$ is the optimal primal objective value.

* **Dual convergence**: $$u^{(k)} \to u^{\ast}$$, where $$u^{\ast}$$ is the dual solution.

The exact convergence rate is not yet fully understood, and much research is currently ongoing in this area. Roughly speaking, ADMM performs similarly to or slightly better than first-order methods. 

---
layout: post
title: 27 Automatic differentiation
chapter: '27'
order: 1
owner: Nguyen Le Linh
categories:
- chapter27
lang: en
lesson_type: required
---


# Automatic differentiation

Every optimizer in Chapter 26 needs a gradient. In 2026 that gradient is almost never derived on paper and almost never a numerical finite difference. **Automatic differentiation (AD)** evaluates *exact* derivatives of a program by systematically applying the chain rule to elementary operations.

This chapter answers three questions:

1. What is a **computational graph**, and how is a loss “just a program”?
2. How does **forward-mode** AD compute Jacobian–vector products?
3. Why is **backpropagation** reverse-mode AD, and why is reverse mode the right default when we have one scalar loss and millions of parameters?

The survey to keep on your desk is Baydin, Pearlmutter, Radul, Siskind, *Automatic Differentiation in Machine Learning: a Survey*, JMLR 18(153), 2018, [jmlr.org/papers/v18/17-468.html](https://www.jmlr.org/papers/v18/17-468.html). Nocedal & Wright already treated “calculating derivatives” as part of numerical optimization; AD is that chapter after software caught up.

## Lessons

1. Computational graphs
2. Forward mode
3. Reverse mode and backpropagation
4. Autodiff frameworks and scientific ML (optional) — PyTorch, JAX, Enzyme, PINNs

Manual reverse mode on a three-node net versus `torch.autograd` is the lab: if they disagree, your graph or your `detach` is wrong — not the definition of a derivative. The optional software map is [27-04]({% multilang_post_url contents/chapter27/2026-09-16-27_04_autodiff_frameworks %}).

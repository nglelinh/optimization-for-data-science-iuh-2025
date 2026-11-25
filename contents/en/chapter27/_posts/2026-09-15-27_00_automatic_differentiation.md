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

Every optimizer in Chapter 26 assumes a magic oracle hands you $$\nabla F(w)$$ on demand. Yet for a billion-parameter neural network, deriving gradients by hand is impossible, symbolic algebra explodes into megabytes of redundant expressions, and finite differences suffer both catastrophic roundoff error and $$O(d)$$ cost. **Automatic Differentiation (AD)** is the quiet miracle that resolves all three failures at once: by applying the chain rule mechanically to elementary operations inside a computational graph, reverse-mode AD computes the *exact* gradient of a scalar loss with respect to a billion parameters in roughly **2–3×** the cost of a single forward pass.

## Background Knowledge Map: The Four Pillars of Automatic Differentiation

- **Not Symbolic, Not Finite Differences:** Finite differences approximate derivatives via $$\frac{f(x+h)-f(x)}{h}$$ (truncation + cancellation error, $$O(d)$$ evaluations). Symbolic differentiation manipulates closed-form formulas (expression swell). AD differentiates *numerical execution traces* at machine precision.
- **Computational Graphs (DAGs):** Every differentiable program unrolls into a Directed Acyclic Graph of elementary primitives ($$+, \times, \exp, \text{matmul}$$) whose local derivatives are known analytically.
- **Forward Mode (JVP) vs. Reverse Mode (VJP):** Forward mode propagates input tangents $$\dot{v} = J_v \dot{x}$$ in one pass (ideal when inputs $$n \ll m$$ outputs). Reverse mode propagates output adjoints $$\bar{v} = J_v^\top \bar{y}$$ backward from the loss (ideal when $$n \gg m = 1$$, i.e., deep learning!).
- **Higher-Order & Implicit Differentiation:** Composing JVPs and VJPs yields exact Hessian-vector products in $$O(1)$$ passes, while implicit differentiation (IFF / unrolling) computes hypergradients for bilevel optimization.

### Step-by-Step Worked Example (Read Slowly): Why Finite Differences Fail While AD Is Exact

Consider $$f(x) = \sin(x^2)$$ at $$x = 2.0$$, where the exact derivative is $$f'(2) = 2x\cos(x^2) = 4\cos(4) \approx -2.61457448$$.

1. **Finite difference with $$h = 10^{-1}$$ (truncation error):**
   $$\frac{\sin(2.1^2) - \sin(2.0^2)}{0.1} = \frac{\sin(4.41) - \sin(4.0)}{0.1} \approx \frac{-0.9546 - (-0.7568)}{0.1} = -1.978$$ (off by $$24\%$$!).
2. **Finite difference with $$h = 10^{-15}$$ (floating-point cancellation):** In IEEE-754 float64, $$x + h$$ loses almost all significant digits of $$h$$, producing pure rounding garbage!
3. **Automatic Differentiation (forward tangent trace at $$x = 2, \dot{x} = 1$$):**
   - $$v_1 = x = 2$$, $$\dot{v}_1 = 1$$.
   - $$v_2 = v_1^2 = 4$$, $$\dot{v}_2 = 2 v_1 \dot{v}_1 = 4$$.
   - $$v_3 = \sin(v_2) = \sin(4)$$, $$\dot{v}_3 = \cos(v_2)\dot{v}_2 = 4\cos(4) \approx -2.61457448$$.
   AD returns the **exact** derivative to all 16 digits of float64 precision in a single pass with zero step-size tuning!

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
5. Bilevel optimization and hypergradients (optional) — HPO / meta as one nested template

Manual reverse mode on a three-node net versus `torch.autograd` is the lab: if they disagree, your graph or your `detach` is wrong — not the definition of a derivative. The optional software map is [27-04]({% multilang_post_url contents/chapter27/2026-09-16-27_04_autodiff_frameworks %}). The nested HPO / MAML template — unrolling versus implicit differentiation — is [27-05]({% multilang_post_url contents/chapter27/2026-09-18-27_05_bilevel_hypergrad %}).

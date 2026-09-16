---
layout: post
title: 27-04 Autodiff frameworks and scientific ML
chapter: '27'
order: 5
owner: Nguyen Le Linh
categories:
- chapter27
lang: en
lesson_type: optional
---


Lessons 27-01 to 27-03 are the mathematics: computational graphs, forward-mode JVPs, reverse-mode VJPs / backprop. This optional note is where those modes live in *software* in 2022–2026. Baydin, Pearlmutter, Radul, and Siskind, *JMLR* 18(153), 2018, [jmlr.org/papers/v18/17-468.html](https://www.jmlr.org/papers/v18/17-468.html), remains the survey on your desk; the frameworks below are the ones you will actually import.

## 1. PyTorch: tape reverse-mode, then compile

Paszke et al., *Automatic differentiation in PyTorch* (NIPS Autodiff workshop, 2017) and the later *PyTorch: An Imperative Style, High-Performance Deep Learning Library* (NeurIPS 2019) built reverse-mode AD on a dynamic tape: run the forward Python, record `grad_fn`, play the tape backward. That is 27-03 with an allocator. **PyTorch 2.0** (2023) added `torch.compile` (TorchDynamo + Inductor): the same reverse-mode graph is captured, compiled, and still differentiated. For this course the rule is unchanged. If `torch.autograd.grad` disagrees with your hand-written adjoint, your graph or your `detach` is wrong — not the definition of a derivative. Use PyTorch when the model is a dynamic net, the ecosystem is vision / LLM, and you want a tape you can print.

## 2. JAX: composable JVPs and VJPs

Bradbury, Frostig, Hawkins, Johnson, Leary, Maclaurin, Necula, Paszke, VanderPlas, Wanderman-Milne, and Zhang, *JAX: composable transformations of Python+NumPy programs*, 2018–, [github.com/google/jax](https://github.com/google/jax), treat `grad`, `vmap`, `jit`, and `pmap` as *function transformations*. Forward-mode `jax.jvp` and reverse-mode `jax.vjp` / `jax.grad` are the two modes of this chapter, exposed as first-class APIs. Arrays are immutable; the program you differentiate is a pure function. That restriction is why scientific-ML groups (physics-informed nets, molecular potentials, differentiable simulators) standardized on JAX in 2022–2026: you can `vmap` a simulation and then `grad` the residual. Use JAX when you need nested JVPs/VJPs, batching, or a compiler (XLA) more than a pretrained-model zoo.

## 3. Enzyme: differentiate after the compiler

Moses and Churavy, *Instead of rewriting foreign code for machine learning, automatically synthesize fast gradients*, NeurIPS 2020, run reverse-mode AD on **LLVM IR**, so C++, Fortran, Julia, and Rust become differentiable without a source rewrite. Moses, Churavy, Paehler, et al., *Reverse-Mode Automatic Differentiation and Optimization of GPU Kernels via Enzyme*, SC 2021, and Moses, Narayanan, Paehler, et al., *Scalable Automatic Differentiation of Multiple Parallel Paradigms*, SC 2022, extend the same idea to CUDA, OpenMP, MPI, and Julia tasks. Enzyme-JAX (2023–) registers those kernels as JAX primitives, so `jax.grad` can see a Fortran heat solver. This is the 2020s answer to “our production simulator is not a PyTorch module.”

## 4. Scientific machine learning / PINNs

A physics-informed network minimizes a residual $$r_\theta(x)=\mathcal{L}[u_\theta](x)$$ whose derivatives w.r.t. *inputs* $$x$$ (not only parameters $$\theta$$) come from AD. Raissi, Perdikaris, and Karniadakis, *J. Comput. Phys.* 378:686–707, 2019, is the classic; Karniadakis, Kevrekidis, Lu, Perdikaris, Wang, and Yang, *Nature Reviews Physics* 3:422–440, 2021, is the survey that made PINNs a data-science topic. The 2022–2025 wave (better causal/weighted residuals, operator learning, hybrid Enzyme+JAX simulators) still stands on reverse-mode in $$\theta$$ and often *forward-mode* or nested reverse in $$x$$. That is why Chapter 27 taught both modes: a PINN is the example where “one scalar loss, millions of parameters” is *not* the only AD query.

```python
# JAX: reverse-mode for parameters, forward-mode JVP if you need a directional derivative
import jax, jax.numpy as jnp

def loss(w, x, y):
    return jnp.mean((x @ w - y) ** 2)

w = jnp.zeros(3)
g = jax.grad(loss)(w, jnp.ones((8, 3)), jnp.zeros(8))  # VJP, one scalar
_, jvp = jax.jvp(lambda v: v @ v, (w,), (jnp.ones(3),))  # directional
```

**Exercise.** Implement $$f(w)=\|Aw-b\|_2^2$$ in NumPy, PyTorch, and (if installed) JAX. Compare `2 A.T @ (A@w-b)` to `torch.autograd` and `jax.grad`. Then time a *Jacobian* of an 8-output map with (i) eight reverse-mode calls and (ii) eight forward-mode JVPs — forward should win, which is the 27-02 lesson in software form.

## Sources

- A. G. Baydin et al., *JMLR* 18(153), 2018 — AD survey.
- A. Paszke et al., NeurIPS 2019 — PyTorch.
- J. Bradbury et al., 2018– — JAX.
- W. S. Moses and V. Churavy, NeurIPS 2020; Moses et al., SC 2021 & SC 2022 — Enzyme.
- M. Raissi, P. Perdikaris, G. E. Karniadakis, *J. Comput. Phys.* 378, 2019 — PINNs.
- G. E. Karniadakis et al., *Nat. Rev. Phys.* 3:422–440, 2021 — physics-informed ML survey.

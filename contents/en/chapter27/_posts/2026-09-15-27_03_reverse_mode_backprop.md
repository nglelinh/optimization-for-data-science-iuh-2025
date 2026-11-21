---
layout: post
title: 27-03 Reverse mode and backpropagation
chapter: '27'
order: 4
owner: Nguyen Le Linh
categories:
- chapter27
lang: en
lesson_type: required
---


**Reverse-mode AD** attaches to every node $$v$$ an **adjoint** $$\bar v = \frac{\partial \ell}{\partial v}$$ for a scalar output $$\ell$$. After the forward sweep stores intermediates, we go *backward*:

$$
\bar u \mathrel{+}= \bar v\cdot \partial_u h
\quad\text{when } v=h(u,\ldots).
$$

One reverse sweep produces the full gradient $$\nabla_w \ell$$ — a **vector–Jacobian product** $$(\nabla \ell)^\top J$$. Cost is a small constant times the forward cost, *independent of the number of parameters*. That single sentence is why deep learning is computationally possible.

**Backpropagation** is reverse-mode AD applied to a layered net, with the adjoint of a layer being the familiar $$\delta$$:

$$
\delta^{(\ell)} = \bigl(W^{(\ell+1)\top}\delta^{(\ell+1)}\bigr)\odot \phi'(z^{(\ell)}).
$$

Nothing mystical: matrix multiplies are elementary nodes with known local Jacobians.

```python
# Scalar toy: ℓ = (w2 * relu(w1 * x) - y)**2
# Manual reverse vs a tiny tape
x, y = 1.5, 0.3
w1, w2 = 0.8, -0.4
z = w1 * x
h = max(z, 0.0)
pred = w2 * h
ell = (pred - y) ** 2
# reverse
d_ell = 1.0
d_pred = d_ell * 2 * (pred - y)
d_w2 = d_pred * h
d_h = d_pred * w2
d_z = d_h * (1.0 if z > 0 else 0.0)
d_w1 = d_z * x
print(d_w1, d_w2)
```

Compare with PyTorch: build the same expression as tensors with `requires_grad=True` and call `ell.backward()`.

**Memory.** Reverse mode stores the forward tape. Checkpointing / rematerialization trades compute for RAM — the reason gradient checkpointing appears in large-model training. That is an implementation footnote, not a different derivative.

When you have *many* outputs and few inputs, prefer forward mode. When you have one loss and a sea of weights, prefer reverse. Mixed mode (forward-over-reverse Hessian–vector products) is how some second-order and bilevel methods stay linear in dimension.

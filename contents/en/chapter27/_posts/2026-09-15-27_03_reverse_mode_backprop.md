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

Here is the single most consequential complexity theorem in modern deep learning: suppose you have a scalar loss $$\ell(w)$$ that depends on $$d = 10^9$$ weights. Forward-mode AD would require $$10^9$$ passes to compute $$\nabla \ell(w)$$. **Reverse-mode AD** (popularized in neural networks as **backpropagation**) flips the chain rule backward from the scalar output $$\ell$$—computing *all* $$10^9$$ partial derivatives simultaneously in **one** backward pass at a total cost bounded by a small constant multiple (typically $$\le 4\times$$) of evaluating $$\ell$$ itself!

## Key ideas: Adjoints, VJPs, and the Cheap-Gradient Principle

- **Adjoints ($$\bar{v} = \frac{\partial \ell}{\partial v}$$):** Reverse mode attaches a scalar sensitivity $$\bar{v}$$ to every node measuring how much a tiny bump in $$v$$ changes the final loss $$\ell$$. We seed $$\bar{\ell} = 1$$ and walk the DAG in *reverse* topological order.
- **Accumulating Fan-Out Gradients (`+=`):** Whenever node $$u$$ feeds multiple children $$v^{(1)}, v^{(2)}$$, its adjoint *accumulates* via $$\bar{u} \mathrel{+}= \bar{v}^{(j)} \frac{\partial v^{(j)}}{\partial u}$$—the exact reason frameworks warn you to zero gradients between batches!
- **One Pass = One Row of the Jacobian (VJP):** Seeding $$\bar{y} = u \in \mathbb{R}^m$$ computes the Vector-Jacobian Product $$u^\top J_f(x)$$. When $$m = 1$$ (scalar loss), a single reverse pass hands you the entire gradient $$\nabla_x \ell \in \mathbb{R}^n$$ regardless of how huge $$n$$ is (Baur–Strassen Cheap-Gradient Principle).
- **The Memory Price of Reversal:** Because local derivatives like $$\frac{\partial (uv)}{\partial u} = v$$ depend on forward values, reverse mode must cache forward intermediates on a tape—making activation memory, not FLOPs, the primary bottleneck of large-scale training.

### Worked example: Full Forward + Reverse Adjoint Trace on a 2-Layer ReLU Loss

Evaluate $$\ell = (w_2 \cdot \operatorname{relu}(w_1 x) - y)^2$$ at $$x = 2$$, $$y = 5$$, $$w_1 = 1.5$$, $$w_2 = 2.0$$, and find $$\frac{\partial \ell}{\partial w_1}$$ and $$\frac{\partial \ell}{\partial w_2}$$ via reverse-mode AD.

1. **Forward pass (record intermediates on tape):**
   - $$z_1 = w_1 x = (1.5)(2) = 3.0$$.
   - $$a_1 = \operatorname{relu}(z_1) = 3.0$$ (active since $$z_1 > 0$$).
   - $$\hat{y} = w_2 a_1 = (2.0)(3.0) = 6.0$$.
   - $$e = \hat{y} - y = 6.0 - 5.0 = 1.0$$.
   - $$\ell = e^2 = 1.0$$.
2. **Reverse pass (seed $$\bar{\ell} = 1$$ and walk backward):**
   - $$\bar{e} = \bar{\ell} \cdot 2e = 1 \cdot 2(1.0) = 2.0$$.
   - $$\bar{\hat{y}} = \bar{e} \cdot 1 = 2.0$$.
   - $$\bar{w}_2 = \bar{\hat{y}} \cdot a_1 = 2.0 \cdot 3.0 = 6.0$$.
   - $$\bar{a}_1 = \bar{\hat{y}} \cdot w_2 = 2.0 \cdot 2.0 = 4.0$$.
   - $$\bar{z}_1 = \bar{a}_1 \cdot \mathbf{1}[z_1 > 0] = 4.0 \cdot 1 = 4.0$$.
   - $$\bar{w}_1 = \bar{z}_1 \cdot x = 4.0 \cdot 2 = 8.0$$.
3. **Result:** In a single reverse sweep, we obtained the exact gradient $$\bigl(\frac{\partial \ell}{\partial w_1}, \frac{\partial \ell}{\partial w_2}\bigr) = (8.0,\ 6.0)$$, matching the analytic derivatives $$2(w_2 w_1 x - y) w_2 x = 2(1)(2)(2) = 8$$ and $$2(w_2 w_1 x - y)(w_1 x) = 2(1)(3) = 6$$.

**Reverse-mode AD** attaches to every node $$v$$ an **adjoint** $$\bar v = \frac{\partial \ell}{\partial v}$$ for a scalar output $$\ell$$. After the forward sweep stores intermediates, we go *backward*:

$$
\bar u \mathrel{+}= \bar v\cdot \partial_u h
\quad\text{when } v=h(u,\ldots).
$$

One reverse sweep produces the full gradient $$\nabla_w \ell$$ — a **vector–Jacobian product** $$(\nabla \ell)^\top J$$. Cost is a small constant times the forward cost, *independent of the number of parameters*. That single sentence is why deep learning is computationally possible.

**Backpropagation** is reverse-mode AD applied to a layered net, with the adjoint at layer $$k$$ being the familiar $$\delta^{(k)}$$ (we write $$k$$ for the layer index, since $$\ell$$ already denotes the loss):

$$
\delta^{(k)} = \bigl(W^{(k+1)\top}\delta^{(k+1)}\bigr)\odot \phi'(z^{(k)}).
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

### Forward and reverse mode in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/autodiff-forward-reverse_en.mp4"></video>
</div>

The computation graph of x₁x₂ + sin x₁: tangents and dual numbers, adjoints flowing backward, the ReLU toy of lesson 27-03, and counting sweeps.

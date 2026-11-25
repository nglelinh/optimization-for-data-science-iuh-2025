---
layout: post
title: 14-07 Comparison to first-order method
chapter: '14'
order: 15
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

If Newton's method converges in 10 iterations while gradient descent needs 10,000, why doesn't everyone use Newton's method for deep learning? The answer lies in a single number: $$n^3$$. When $$n = 500$$, inverting a Hessian takes milliseconds and Newton crushes gradient descent; when $$n = 10^8$$ (a neural network), storing the $$n \times n$$ Hessian alone would require 40 petabytes of RAM!

## Background Knowledge Map: The First-Order vs. Second-Order Trade-Off

- **Pillar 1 — Memory Scaling ($$O(n^2)$$ vs. $$O(n)$$):** Dense Newton must store $$\frac{n(n+1)}{2}$$ Hessian entries, whereas gradient descent only stores an $$n$$-vector.
- **Pillar 2 — Per-Iteration Compute ($$O(n^3)$$ vs. $$O(n)$$):** Dense Cholesky factorization costs $$\frac{1}{3}n^3$$ flops per Newton step, versus $$O(n)$$ flops for a gradient step.
- **Pillar 3 — Conditioning & Accuracy Regime:** Gradient descent stalls when the condition number $$\kappa = L/m$$ is large or when high accuracy ($$\epsilon = 10^{-10}$$) is needed; Newton is immune to $$\kappa$$ and thrives on high-precision targets.
- **Pillar 4 — Crossover Dimension:** For moderate $$n$$ (up to a few thousand) or sparse/structured Hessians, Newton wins in wall-clock time; for huge unstructured $$n$$ with low-accuracy targets (e.g., $$\epsilon = 10^{-2}$$), first-order methods dominate.

### Step-by-Step Worked Example (Read Slowly): Wall-Clock Cost Crossover Between GD and Newton

Compare solving a dense strongly convex problem of dimension $$n$$ with condition number $$\kappa = 1000$$ to accuracy $$\epsilon = 10^{-8}$$:
- Gradient descent needs roughly $$K_{\text{GD}} \approx \kappa \ln(1/\epsilon) \approx 1000 \times 18.4 \approx 18{,}400$$ iterations, costing $$\approx 2n^2$$ flops each (for a dense matrix-vector product) $$\implies \text{Total GD flops} \approx 36{,}800\,n^2$$.
- Newton's method needs roughly $$K_{\text{NT}} \approx 12$$ iterations, costing $$\approx \frac{1}{3}n^3$$ flops each $$\implies \text{Total Newton flops} \approx 4\,n^3$$.

1. **Case 1: $$n = 100$$:**
   - GD: $$36{,}800 \times 10^4 = 3.68 \times 10^8$$ flops.
   - Newton: $$4 \times 10^6$$ flops. **Newton is ~92× faster!**
2. **Case 2: $$n = 1{,}000$$:**
   - GD: $$3.68 \times 10^{10}$$ flops.
   - Newton: $$4 \times 10^9$$ flops. **Newton is ~9× faster!**
3. **Case 3: $$n = 50{,}000$$:**
   - GD: $$9.2 \times 10^{13}$$ flops (memory: 400 KB for vector).
   - Newton: $$5 \times 10^{14}$$ flops (and **20 GB** just to store the dense Hessian!). **GD wins on both time and memory.**

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>

In this chapter, we compare Newton's method and gradient descent from a general perspective. Let the dimension of the domain be $$n$$.

| Item | Newton's method | Gradient descent |
| -------- | -------- | -------- |
| Memory     | $$O(n^{2})$$ (storage for $$n \times n$$ Hessian matrix)     | $$O(n)$$ (storage for $$n$$-dimensional gradient) |
| Computation     | $$O(n^{3})$$ flops (computation for $$n \times n$$ linear system)     | $$O(n)$$ flops (computation for $$n$$-dimensional vector addition)     |
| Backtracking     | $$O(n)$$ | $$O(n)$$  |
| Conditioning     | Affine invariant, less affected by conditioning  | Can be strongly affected by conditioning |
| Fragility     | Sensitive to bugs or numerical errors | More robust than Newton's method |

## Example

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/gd(1).jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Logistic regression [3]</figcaption>
</p>
</figure>

Figure 1 above is a logistic regression example discussed in [14-04]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %}). If you plot the x-axis as actual computation time, you see the following. In convergence analysis, Newton's method has two phases. In practice, after a certain time, you can observe fast convergence (quadratic convergence). In the initial damped phase of Newton's method, the convergence rate is similar to gradient descent. However, since $$O(n^{3})$$ computation is required, the actual computation time may be slower. After backtracking line search is no longer needed, you observe quadratic convergence and very fast progress.

### Try it yourself: Newton vs. gradient descent

<div class="opx-explainer" data-opx="newton" data-lang="en"></div>

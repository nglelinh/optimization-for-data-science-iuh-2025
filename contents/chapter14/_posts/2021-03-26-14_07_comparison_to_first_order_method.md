---
layout: post
title: 14-07 Comparison to first-order method
chapter: "14"
order: 13
owner: "Minjoo Lee"
---
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

Figure 1 above is a logistic regression example discussed in [14-04]({% post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %}). If you plot the x-axis as actual computation time, you see the following. In convergence analysis, Newton's method has two phases. In practice, after a certain time, you can observe fast convergence (quadratic convergence). In the initial damped phase of Newton's method, the convergence rate is similar to gradient descent. However, since $$O(n^{3})$$ computation is required, the actual computation time may be slower. After backtracking line search is no longer needed, you observe quadratic convergence and very fast progress.
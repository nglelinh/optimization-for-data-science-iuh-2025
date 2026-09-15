---
layout: post
title: 26-02 Momentum and Nesterov acceleration
chapter: '26'
order: 3
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: required
---


Gradient descent on a badly conditioned quadratic zig-zags: the step that is safe for the sharp eigenvalue is painfully small along the flat one. **Momentum** keeps a velocity that accumulates consistent gradient components and cancels oscillating ones.

**Polyak heavy ball** (1964) uses a frictionless-looking recurrence

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k), \\
w_{k+1} &= w_k - \eta v_{k+1},
\end{align}
$$

with $$\beta\in[0,1)$$ (PyTorch’s `SGD(momentum=…)` is this family, up to whether the gradient is scaled before or after mixing).

**Nesterov acceleration** evaluates the gradient at a *look-ahead* point:

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k - \eta \beta v_k), \\
w_{k+1} &= w_k - \eta v_{k+1}.
\end{align}
$$

On smooth convex problems, Nesterov’s method achieves the optimal first-order rate $$O(1/T^2)$$ for function values (cf. FISTA in Chapter 09). On deep nets the picture is empirical: large $$\beta$$ ($$0.9$$, sometimes $$0.99$$) is a curvature-aware low-pass filter, not a theorem you should quote for ResNets.

The best classroom visual remains Goh, *[Why Momentum Really Works](http://distill.pub/2017/momentum)* (Distill, 2017). Pair it with the quadratic-valley thought experiment: without momentum you bounce off the walls; with momentum you build speed down the corridor.

<div class="content-box insight-box">
<strong>Theory ≠ practice reminder.</strong> Nesterov’s proof needs a carefully scheduled $$\beta_k$$ and a convex smooth $$F$$. Deep-learning “Nesterov” is usually a constant-$$\beta$$ look-ahead on a nonconvex loss. Use the proof to understand <em>why</em> look-ahead damps, not to predict CIFAR accuracy.
</div>

**Exercise.** Implement heavy-ball and Nesterov on $$F(w)=\tfrac12 w^\top \operatorname{diag}(1,100)\,w$$. Plot the two trajectories from the same start. Which value of $$\beta$$ first stops the visible zig-zag?

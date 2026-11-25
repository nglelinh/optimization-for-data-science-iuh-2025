---
layout: post
title: 13-04 Conjugate function
chapter: '13'
order: 5
owner: Wontak Ryu
categories:
- chapter13
lang: en
---

Think of a convex function $$f(x)$$ as the cost of producing $$x$$ units of a good, and suppose the market pays a unit price $$y$$ per unit sold. Your profit is $$y^T x - f(x)$$. The maximum profit you can earn at price $$y$$—namely $$f^*(y) = \max_x (y^T x - f(x))$$—is the **Fenchel conjugate** of $$f$$. Remarkably, knowing the optimal profit curve $$f^*(y)$$ for every price $$y$$ lets you reconstruct the original convex cost curve $$f(x)$$ without losing a single bit of information.

## Background Knowledge Map: The Fenchel Conjugate Engine

- **Pillar 1 — Pointwise Supremum Guarantees Convexity:** Because $$y \mapsto y^T x - f(x)$$ is affine in $$y$$ for every fixed $$x$$, $$f^*(y)$$ is *always* convex—even if the original function $$f$$ is nonconvex.
- **Pillar 2 — Fenchel–Young Inequality & Tightness:** For every $$x, y$$, $$f(x) + f^*(y) \ge x^T y$$. Equality holds if and only if $$y \in \partial f(x)$$, linking slopes directly to primal-dual optimality.
- **Pillar 3 — Biconjugate Duality ($$f^{**} = f$$):** For any closed, proper convex function, conjugating twice recovers $$f$$ exactly, giving the dual representation of a convex function as the envelope of all its supporting hyperplanes.
- **Pillar 4 — Core Dictionary of Conjugates:** Quadratics map to inverse-Hessian quadratics ($$\frac{1}{2}x^T Q x \leftrightarrow \frac{1}{2}y^T Q^{-1} y$$), set indicators $$I_C$$ map to support functions $$I_C^*$$, and norms $$\|\cdot\|$$ map to dual-norm unit-ball indicators $$I_{\{\|\cdot\|_*\le 1\}}$$.

### Step-by-Step Worked Example (Read Slowly): Computing a Conjugate and Verifying Fenchel's Inequality

Consider the scalar exponential cost $$f(x) = e^x$$ on $$\mathbb{R}$$.

1. **Set up the conjugate definition:**
   $$f^*(y) = \sup_{x \in \mathbb{R}} \left(yx - e^x\right).$$
2. **Analyze the three regimes of $$y$$:**
   - **If $$y < 0$$:** Letting $$x \to -\infty$$ makes $$yx \to +\infty$$ while $$e^x \to 0$$, so $$f^*(y) = +\infty$$.
   - **If $$y = 0$$:** $$\sup_x (-e^x) = 0$$ (approached as $$x \to -\infty$$), so $$f^*(0) = 0$$.
   - **If $$y > 0$$:** Differentiate $$g(x) = yx - e^x$$: $$g'(x) = y - e^x = 0 \implies x^\star = \ln y$$ (a global max since $$g''(x) = -e^x < 0$$). Substituting back:
     $$f^*(y) = y \ln y - y.$$
3. **Check Fenchel's inequality numerically:** Pick $$x = 1$$ and $$y = e^2 \approx 7.389$$.
   - $$f(1) + f^*(e^2) = e + (e^2 \cdot 2 - e^2) = e + e^2 \approx 2.718 + 7.389 = 10.107$$.
   - $$xy = 1 \cdot e^2 \approx 7.389 \le 10.107$$ (strict inequality because $$y = e^2 \ne f'(1) = e$$).
4. **Verify equality at $$y = f'(x)$$:** At $$x = 1$$ and $$y = e$$, $$f(1) + f^*(e) = e + (e \ln e - e) = e = 1 \cdot e = xy$$.

For a given function $$f : \mathbb{R}^n → \mathbb{R}$$, the conjugate $$f^{∗} : \mathbb{R}^n → \mathbb{R}$$ is defined as follows:

> $$f^{∗}(y) = \max_x y^Tx−f(x)$$


<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter13/conjugate_function.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Illustration of conjugate function [1]</figcaption>
</p>


### [Note] 
$$f^{∗}$$ is always convex since it is the pointwise maximum of convex (affine) functions $$y^Tx - f(x)$$.
(Here, $$f$$ does not necessarily need to be convex.)
$$f^{∗}(y)$$ is the maximum gap between the linear function $$y^Tx$$ and $$f(x)$$.
(From B & V page 91)

Conjugation for differentiable $$f$$ is called the Legendre transform.

#### Properties: 
• Fenchel’s inequality: for any $$x,y, f(x) + f^{∗}(y) ≥ x^Ty$$
> $$f(x) + f^{∗}(y) ≥ x^Ty \iff f^{*}(y) \ge x^Ty - f(x)$$
> $$ f^{*}(y) = \max_z z^Ty - f(x)$$

• The conjugate of a conjugate is $$f^{∗∗}$$, so $$f^{∗∗} ≤ f$$ holds.<br>
• If $$f$$ is closed and convex, then $$f^{∗∗} = f$$. <br>
• If $$f$$ is closed and convex, then for all $$x,y$$, the following holds:<br>
> $$\begin{align}
> x ∈ ∂f^{∗}(y) &\iff y ∈ ∂f(x) \\\
> &\iff f(x) + f^{∗}(y) = x^Ty \\\
> \end{align}$$

• If $$f(u,v) = f_1(u) + f_2(v)$$, then $$f^{∗}(w,z) = f_1^{∗}(w) + f_2^{∗}(z)$$ holds. 



#### Examples: 
• Let's examine the case where $$f(x)$$ is a simple quadratic as follows:
> $$f(x) = \frac{1}{2}x^TQx$$, where $$Q \succ 0$$

Then $$y^Tx− \frac{1}{2}x^TQx$$ is strictly concave in $$y$$ and reaches its maximum at $$x = Q^{−1}y$$. That is, $$f^{∗}(y) = \frac{1}{2}y^TQ^{−1}y$$. 



### [Proof]
> $$\begin{align}
> f^{*}(y) & =  \max_x \left( y^Tx -\frac{1}{2}x^TQx \right) \\\
> & = -\min_x \left(\frac{1}{2}x^TQx- y^Tx \right), x^{\star} = Q^{-1}y  \\\
> & = -\frac{1}{2}y^TQ^{-1}QQ^{-1}y + y^TQ^{-1}y \\\
> & = \frac{1}{2}y^TQ^{-1}y  \\\
> \end{align}$$

> Fenchel's inequality: for any $$x, y$$
> $$\frac{1}{2} x^TQx + \frac{1}{2} y^TQ^{-1}y \ge x^Ty$$

• Indicator function: If $$f(x) = I_C(x)$$, then its conjugate is as follows:

> $$f^{∗}(y) = I^{∗}_C(y) = \max_{x ∈ C} y^Tx$$ called the **support function** of $$C$$

• Norm: If $$f(x) = \|x\|$$, then its conjugate is as follows:
> $$f^{∗}(y) = I_{\\{ z : \rVert z \rVert_{∗} ≤ 1 \\}}(y)$$ where $$\rVert · \rVert_{∗}$$ is the dual norm of $$\rVert · \rVert$$ 


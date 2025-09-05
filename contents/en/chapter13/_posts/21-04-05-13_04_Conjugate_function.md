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


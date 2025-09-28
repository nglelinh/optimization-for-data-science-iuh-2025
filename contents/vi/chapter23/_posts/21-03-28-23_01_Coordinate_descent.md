---
layout: post
title: 23-01 Phương Pháp Coordinate Descent
chapter: '23'
order: 2
owner: YoungJae Choung
categories:
- chapter23
lang: vi
---

In this chapter, we introduce a method called coordinate descent that is extremely simple, efficient, and highly scalable. First, let's start with some simple questions and answers.

**Q1. When function $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ is convex and differentiable, if the point where $$f$$ is minimized along each coordinate axis is $$x$$, is this $$x$$ a global minimizer?**

**A1: Yes. Since $$\nabla f(x) = 0$$, $$x$$ is a global minimizer of $$f$$.**

The above question is equivalent to asking whether $$f(x + \delta e_i) \ge f(x)$$ is satisfied for all $$\delta, i$$ when $$e_i = (0, \dots, 1, \dots, 0) \in \mathbb{R}^n$$ is the $$i$$-th standard basis vector. That is, since we cannot make $$f$$ smaller by moving in any coordinate axis direction from $$x$$, the partial derivatives in all axis directions become 0.

$$
\nabla f(x) = \big( \frac{\partial f}{\partial x_1}(x), \dots, \frac{\partial f}{\partial x_n}(x) \big) = (0, \dots, 0) = 0
$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/smooth_function.png" alt="[Fig1] Smooth convex function f [3]">
  <figcaption style="text-align: center;">$$[Fig1] \; Smooth \; convex \; function \; f \; [3]$$ </figcaption>
</p>
</figure>


<br/>

**Q2. Then, when $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ is convex but 'non-differentiable' function, is the point $$x$$ where $$f$$ is minimized along each coordinate axis always a global minimizer?**

**A2: No. In this case, we cannot assert that $$x$$ is a global minimizer of $$f$$. (Counterexample: Fig2 below)** 

Looking at the contour lines on the right side of the counterexample below, we can see that although the marked point is not the global minimum, $$f$$ cannot be made smaller by moving in any coordinate axis direction. (To make $$f$$ smaller, one must be able to move inside the contour lines.) This is because at this position, all inner regions of the contour lines are contained within the two tangent lines parallel to the coordinate axes. On the other hand, when $$f$$ is a differentiable convex function, only one tangent line exists at any point on the contour lines, so this phenomenon does not occur.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/non-smooth_function.png" alt="[Fig2] Counterexample: Non-smooth convex function f [3]">
  <figcaption style="text-align: center;">$$[Fig2] \; Counterexample: Non \, smooth \; convex \; function \; f \; [3]$$ </figcaption>
</p>
</figure>
<br/>

**Q3. When $$f$$ can be expressed as the sum of a differentiable convex function $$g$$ and a convex function $$h$$, is the point $$x$$ where $$f$$ is minimized along each coordinate axis always a global minimizer? (That is, $$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$)**

**A3. Yes. This is because it satisfies the following for any $$y$$.**
$$\begin{align}
f(y) - f(x) &\ge \nabla g(x)^T (y-x) + \sum_{i=1}^{n} \big[ h_i(y_i) - h_i(x_i) \big] \\\\
&= \sum_{i=1}^{n} \big[ \underbrace{\nabla_i g(x) (y_i - x_i) + h_i(y_i) - h_i(x_i)}_{\ge 0} \big] \ge 0
\end{align}$$

**Proof:**

>Let $$F_i(x_i) = g(x_i ; x_{-i}) + h_i(x_i)$$. ($$g(x_i ; x_{-i})$$ means viewing only the $$i$$-th element of $$x$$ as a variable, and the rest as fixed values.)
>
> $$
> \begin{align}
> & \: 0 \in \partial F_i (x_i) \\\\
> \Leftrightarrow & \: 0 \in \{ \nabla_i g(x) \} + \partial h_i(x_i)\\\\
> \Leftrightarrow & \: - \nabla_i g(x) \in \partial h_i(x\_i)
> \end{align}
> $$

By the [definition of subgradient]({% multilang_post_url contents/chapter07/21-03-25-07_01_subgradient %}),

> $$
> \begin{align}
> & h_i(y_i) \ge h_i(x_i) - \nabla_i g(x) (y_i - x_i)\\\\
> \Leftrightarrow & \nabla_i g(x) (y_i - x_i) + h_i(y_i) - h_i(x_i) \ge 0.
> \end{align}
> $$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/separable_non-smooth.png" alt="[Fig3] Convex function f with separable non-smooth parts [3]">
  <figcaption style="text-align: center;">$$[Fig3] \; Convex \; function \; f \; with \; separable \; non \,smooth \; parts \; [3]$$ </figcaption>
</p>
</figure>
<br/>

## Conclusion

The minimizer of $$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$ with $$g$$ convex, differentiable and $$h_i$$ convex can be found using **coordinate descent**. Coordinate descent iterates the following cycle. (Assume that an appropriate initial value $$x^{(0)}$$ is set.)

>**Coordinate Descent:** <br/>
>$$\:$$ For $$k = 1,2,3,\dots$$,
>
>$$
>\begin{align}
>x_1^{(k)} &\in \text{arg}\min_{x_1} \: f(x_1, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_2^{(k)} &\in \text{arg}\min_{x_2} \: f(x_1^{(k)}, x_2, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_3^{(k)} &\in \text{arg}\min_{x_3} \: f(x_1^{(k)}, x_2^{(k)}, x_3, \dots, x_n^{(k-1)})\\\\
>& \dots\\\\
>x_n^{(k)} &\in \text{arg}\min_{x_n} \: f(x_1^{(k)}, x_2^{(k)}, x_3^{(k)}, \dots, x_n)
>\end{align}
>$$

### Notes:

* The process of obtaining $$x_{i+1}^{(k)}, \dots, x_{n}^{(k)}$$ uses the newly obtained $$x_i^{(k)}$$ in the $$k$$-th cycle.
* The order of coordinate axes in the cycle can be arbitrarily specified.
* Two or more coordinate axes can be grouped together and processed as blocks.

The coordinate descent introduced above corresponds to exact coordinatewise minimization. Another approach is inexact coordinatewise minimization using gradients. (Assuming $$f$$ is a differentiable convex function)

>**Coordinate Descent (inexact coordinatewise minimization):** <br/>
>$$\:$$ For $$k = 1,2,3,\dots$$,
>
>$$
>\begin{align}
>x_1^{(k)} &= x_1^{(k-1)} - t_{k,1} \cdot \nabla_1 f(x_1^{(k-1)}, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_2^{(k)} &= x_2^{(k-1)} - t_{k,2} \cdot \nabla_2 f(x_1^{(k)}, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_3^{(k)} &= x_3^{(k-1)} - t_{k,3} \cdot \nabla_3 f(x_1^{(k)}, x_2^{(k)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>& \dots\\\\
>x_n^{(k)} &= x_n^{(k-1)} - t_{k,n} \cdot \nabla_n f(x_1^{(k)}, x_2^{(k)}, x_3^{(k)}, \dots, x_n^{(k-1)})
>\end{align}
>$$


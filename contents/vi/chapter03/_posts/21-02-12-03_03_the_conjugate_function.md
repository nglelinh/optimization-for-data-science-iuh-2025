---
layout: post
title: 03-03 The conjugate function
chapter: '03'
order: 7
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

This section introduces the conjugate function, a key concept in convex analysis and duality theory.

The conjugate function is used to transform an optimization problem into its corresponding dual problem, which will be discussed in detail in a later section on Lagrange Duality. When differentiating in the context of Lagrange Duality, one can directly substitute using the conjugate function without performing explicit differentiation.

For a given function $$f$$, the conjugate is defined as follows:

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/conjugate_function.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Conjugate function [2]</figcaption>
</p>
</figure>

Key properties of the conjugate function include:

- If $$f$$ is not convex, its conjugate $$f^∗$$ is still convex.

#### Example
>• *Negative logarithm* $$f(x)=−\log x$$

> $$f∗(y)=\sup_{x>0} (xy+ \log x)$$ 
> $$=
\begin{cases}
-1-\log(-y), & y < 0 \\ 
\infty, & \text{ otherwise}
\end{cases}
$$

>• *Strictly convex quadratic* $$f(x) = (1/2)x^TQx$$ with $$Q∈S_{++}^n$$

>$$
\begin{align}
f∗(y)=\sup_{x} (y^Tx−(1/2)x^TQx)
& = {1 \over 2}y^TQ^−1y 
\end{align}
$$


These topics will be covered in more detail in Chapter 13.


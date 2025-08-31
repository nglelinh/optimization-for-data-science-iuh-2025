---
layout: post
title: 03-01-01 Definition
chapter: "03"
order: 3
owner: "Minjoo Lee"
---
## Convex function

A function $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ is convex if its domain is a convex set and for any two points $$x, y \in \text{dom}f$$, the function satisfies:

> $$f(\theta x+(1-\theta)y) \le \theta f(x)+(1-\theta)f(y)$$,
>
> with $$0 \le \theta \le 1$$, for all $$x,y \in \text{dom} f$$

This means that for any two points $$x, y$$, the value of $$f$$ at their convex combination is less than or equal to the convex combination of their function values. Geometrically, the graph of $$f$$ lies below the line segment connecting $$f(x)$$ and $$f(y)$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/convex_function01.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Convex Function [2]</figcaption>
</p>
</figure>

## Strictly convex
A function $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ is strictly convex if for any two distinct points $$x, y \in \text{dom}f$$ and $$0 < \theta < 1$$:

> $$f(\theta x+(1-\theta)y)<\theta f(x)+(1-\theta)f(y)$$,
>
> with $$0<\theta<1$$, $$x \neq y$$, for all $$x, y \in \text{dom}f$$

## Strongly convex
A function $$f$$ is strongly convex if $$f - \frac{m}{2}\| x \|_{2}^{2}$$, with $$m > 0$$, is convex.

### [Note] strongly convex ⇒ strictly convex ⇒ convex

## Concave function
A function $$f$$ is concave if $$-f$$ is convex.

All affine functions $$f(x) = a^T x+b$$ satisfy:
> $$
\begin{aligned}
f(\theta x+(1-\theta)y) &= a^T (\theta x+(1-\theta)y) +b \\
&= \theta a^T x + (1-\theta) a^T y + \theta b + (1-\theta) b \\
&= \theta f(x)+(1-\theta)f(y) \\
\end{aligned} 
$$
> $$\text{for all } x,y \in \text{dom} f, \text{with } \theta \le \theta \le 1$$

That is, affine functions are always convex, and simultaneously concave.

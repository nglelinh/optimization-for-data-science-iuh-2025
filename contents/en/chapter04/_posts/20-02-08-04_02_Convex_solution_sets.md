---
layout: post
title: 04-02 Convex solution sets
chapter: '04'
order: 3
owner: YoungJae Choung
categories:
- chapter04
lang: en
---
Let's understand the properties of convex solution sets. <br>
Let $$X_{opt}$$ denote the set of solutions to a convex problem:

>$$
\begin{aligned}
X_{opt} =
&\text{arg}\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, i = 1, .., m \\
&&&h_{j}(x) = 0, j = 1, .., r  \\\\
\end{aligned}
$$

## Key property 1
> $$X_{opt}$$ is a convex set.

### Proof
> If $$x$$ and $$y$$ are solutions:
> 1. The domain set $$D$$ is convex, so for $$0 \le t \le 1$$, $$tx+ (1-t)y \in D$$.
> 2. $$g_i, i=1,\dotsc,m$$ and $$h_j, j=1, \dotsc,r$$ are convex and affine functions, so the following conditions hold:
    $$
    \begin{aligned}
       g_{i}(tx + (1-t)y) \leq tg_i(x) + (1-t)g_i(y) \leq 0, \\
       h_{j}(tx + (1-t)y) = th_j(x) + (1-t)h_j(y) = 0 \\
    \end{aligned}
    $$
> 3. $$f$$ is a convex function, so:
    >
    >\begin{aligned}
    >  f(tx+(1-t)y) &\leq tf(x) + (1-t)f(y) \\
    >  = tf^{\star} + (1-t) f^{\star} \\
    >  = f^{\star}
    >\end{aligned}
    >where $$f^{\star} - $$ minimum value.
    >Thus, $$tx + (1-t)y$$ is also a solution.

### Geometric interpretation
In a convex function, any local optimum is also a global optimum. <br>
If the solution set contains multiple elements, it must look like the following:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/multiple-optima.png" alt="[Fig1] geometric interpretation of convexity of the solution set">
  <figcaption style="text-align: center;">[Fig1] geometric interpretation of convexity of the solution set</figcaption>
</p>
</figure>
<br>

## Key property 2
>If $$f$$ is strictly convex, then the solution is unique. That is, $$X_{opt}$$ contains only one element.

$$f$$ being strictly convex means that $$f$$ always satisfies the following property:
>$$f(tx + (1-t)y) < tf(x) + (1-t)f(y),$$
>
>$$\text{where } 0 < t < 1, x \neq y, \text{ and } x, y \in \text{dom } f.$$

That is, $$f$$ is downward convex with no flat segments, and the solution of $$f$$ is unique.

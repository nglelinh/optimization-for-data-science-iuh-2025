---
layout: post
title: 12-03 Example water-filling
chapter: '12'
order: 4
owner: Wontak Ryu
categories:
- chapter12
lang: en
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Suppose we have the following convex optimization problem.

>$$
>\begin{align}
>    &\min_{x} &&{- \sum_{i=1}^n \log(\alpha_i + x_i)} \\\\
>    &\text{subject to} &&{x \succeq 0, 1^Tx = 1},\\\\
>&\text{where } \alpha_i > 0.
>\end{align}
>$$

This problem is about allocating power to n communication channels and arose in information theory. The variable $$x_i$$ represents the output of the transmitter allocated to the i-th channel, and $$\log(\alpha_i + x_i)$$ represents the capacity or communication rate of that channel. That is, this problem is to determine how much power should be allocated to each channel to maximize the total communication rate [1].

Let the Lagrange multipliers for the inequality constraint $$x^\star \succeq 0$$ and equality constraint $$1^Tx^\star = 1$$ be $$\lambda^\star \in \mathbb{R}^n$$ and $$\nu^\star \in \mathbb{R}$$ respectively. The KKT conditions for the given problem are as follows.
>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>\lambda^\star \succeq 0, \\\\
>\lambda_i^\star x_i^\star = 0, \text{    } i = 1, \dots, n, \\\\
> -1 / (\alpha_i + x_i^\star) - \lambda_i^\star + \nu^\star = 0,  \text{    } i= 1, \dots, n.
>\end{align}
> $$

Using the equations obtained from KKT conditions, we can find $$x^\star, \lambda^\star, \nu^\star$$ analytically. First, we eliminate $$\lambda^\star$$ from the equations using it as a slack variable.
>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>x_i^\star(\nu^\star - 1 / (\alpha_i + x_i^\star)) = 0, \text{    } i = 1, \dots, n, \\\\
> \nu^\star \ge 1/(\alpha_i + x_i^\star),  \text{    } i= 1, \dots, n.
>\end{align}
> $$

This is organized as follows by stationarity and complementary slackness.
> $$
> x_i^\star = 
> \begin{cases}
> 1 / \nu^\star - \alpha_i &\nu^\star < 1/\alpha_i \ \\\\
> 0 &\nu^\star \ge 1/\alpha_i\\\\
> \end{cases}
> = \max\{0, 1/\nu^\star - \alpha_i \}, \quad i = 1, \dots, n.
> $$

Also, by the condition $$1^T x^\star = 1$$, $$x_i^\star, i = 1, \dots, n$$ sum to 1.
> $$
> \sum_{i=1}^n \max\{0, 1/\nu^\star - \alpha_i \} = 1.
> $$

The left side of the equation is a piecewise-linear increasing function of $$1/\nu^\star$$, so this equation has a unique solution for fixed $$\alpha_i$$.

This solution method is called water-filling. When $$\alpha_i$$ is the ground level for patch $$i$$, this problem can be thought of as pouring water into each region so that the water level becomes $$1/\nu^\star$$ as shown in the figure below. We pour water until the total amount of water becomes 1.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl}}/img/chapter_img/chapter12/water-fill.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Illustration of water-filling algorithm [1]</figcaption>
</p>
</figure>

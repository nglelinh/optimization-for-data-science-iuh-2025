---
layout: post
title: 12-05 Constrained and Lagrange forms
chapter: '12'
order: 6
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

In statistics and machine learning, we often move between **constrained form** and **Lagrange form**. Let us define the constrained form and Lagrangian form as follows.

#### Constrained Form ((C) hereafter)
>$$ 
>\min_x \: f(x) \quad \text{ subject to } h(x) \le t,\\\\
>\text{where } t \in \mathbb{R} \text{ is a tuning parameter.}
>$$

#### Lagrange Form ((L) hereafter)
>$$ 
>\min_x \: f(x) + \lambda \cdot h(x),\\\\
>\text{where } \lambda \ge 0 \text{ is a tuning parameter.}
>$$

When $$f, h$$ are convex, let us examine the cases where the two problems yield the same solution.

1. **(C) to (L):** When (C) is strictly feasible (satisfies Slater's condition) and satisfies strong duality, if there exists a dual solution $$\lambda^\star \ge 0$$ that minimizes the following objective function for the solution $$x^\star$$ of (C), then $$x^\star$$ is also a solution of (L). 

$$f(x) + \lambda \cdot (h(x) - t)$$
   
2. **(L) to (C):** If $$x^\star$$ is a solution of (L) and (C) with $$t = h(x^\star)$$ satisfies the KKT conditions, then $$x^\star$$ is also a solution of (C). This is because $$\lambda^\star, x^\star$$ that satisfy the KKT conditions of (L) also satisfy the KKT conditions of (C) with $$t = h(x^\star)$$.


>**$$\rightarrow$$ (L)의 KKT conditions:**
>
> $$
> \begin{align}
> \nabla_x f(x^\star) + \lambda^\star \nabla_x h(x^\star) &= 0\\\\
> \lambda^\star &\ge 0\\\\
> \end{align}
> $$
>
>
>**$$\rightarrow$$ $$t = h(x^\star)$$인 (C)의 KKT conditions:**
>
> $$
> \begin{align}
> \nabla_x f(x^\star) + \lambda^\star \nabla_x h(x^\star) &= 0\\\\
> \lambda^\star &\ge 0\\\\
> \lambda^\star (\underbrace{h(x^\star) - h(x^\star)}_{=0}) &= 0
> \end{align}
> $$


In conclusion, 1 and 2 show the following relationships respectively.


<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/conclusion.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Conclusion [3]</figcaption>
</p>
</figure>


So, under what circumstances do (C) and (L) show perfect equivalence?<br/>
For example, when $$h(x) \ge 0$$ (such as norm), $$t = 0$$, and $$\lambda = \infty$$, perfect equivalence is shown. Due to the given conditions, the constraint in (C) becomes $$h(x) = 0$$, and by setting $$\lambda$$ to $$\infty$$, (L) also imposes the same constraint ($$h(x) = 0$$). 
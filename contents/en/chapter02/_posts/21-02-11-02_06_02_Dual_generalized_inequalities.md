---
layout: post
title: 02-06-02 Dual generalized inequalities
chapter: '02'
order: 14
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

If we can define a generalized inequality using a proper cone, we can also define a dual generalized inequality using the dual cone, provided the dual cone is proper.

This section defines dual generalized inequalities using a proper dual cone and redefines minimum and minimal elements using dual inequalities.

## Dual generalized inequalities

Given a proper dual cone, the generalized inequality is defined as follows. For a point $$y$$, if the inner product with every $$x$$ in $$K$$ is nonnegative, then $$y$$ is nonnegative in the dual cone $$K^*$$.

Here, $$\succeq_{K^*}$$ is called the **dual** of $$\succeq_K$$, i.e., the **dual generalized inequality**.

> $$y \succeq_{K^*} 0 \iff y^T x \ge 0$$ for all $$x \succeq_K 0$$

### Key properties of generalized and dual inequalities

* $$x \preceq_K y$$ if and only if $$\lambda^T x \le \lambda^T y$$ for all $$\lambda \succeq_{K^*} 0$$.
* $$x \prec_K y$$ if and only if $$\lambda^T x < \lambda^T y$$ for all $$\lambda \succeq_{K^*} 0, \lambda \ne 0$$.

If $$K = K^{**}$$, the dual generalized inequality associated with $$\preceq_K^*$$ is $$\preceq_K$$, so these properties are preserved even if the roles of generalized and dual inequalities are switched.

For example, $$\lambda \preceq_K^* \mu$$ if and only if $$\lambda^T x \le \mu^T x$$ for all $$x \succeq_K 0$$.

## Minimum and minimal elements via dual inequalities

For a generalized inequality induced by a proper cone $$K$$, we can use dual generalized inequalities to characterize the minimum and minimal elements of a (possibly nonconvex) set $$S \subseteq \mathbb{R}^m$$.

### Minimum element

For all $$ \lambda \succ_K^* 0$$ and $$z \in S$$,

If $$x$$ is the unique minimizer of $$\lambda^T z$$, then with respect to the generalized inequality $$ \succ_K^* $$, $$x$$ is the minimum of $$S$$. (A minimizer is a value of the dependent variable that minimizes a function; here, the function is $$\lambda^T z$$, the variable is $$z$$, and the minimizer is $$x$$.)

Geometrically, this means that for some $$ \lambda \succ_K^* 0 $$, the hyperplane $$\{ z \mid  \lambda^T (z-x) = 0 \}$$ is a strict supporting hyperplane for $$S$$ at $$x$$. (A strict supporting hyperplane means the hyperplane intersects $$S$$ only at $$x$$.) $$S$$ need not be convex. The figure below shows a minimum $$x$$ and a strict supporting hyperplane.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_02_Minimum_element.png" alt="[Fig1] Minimum element [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Minimum element [1]</figcaption>
</p>
</figure>

### Minimal element

The necessary and sufficient conditions for minimal elements differ slightly.

For $$\lambda \succ_K^* 0$$ and $$z \in S$$, if $$x$$ is a minimizer of $$\lambda^T z$$, then $$x \in S$$ is minimal. In other words, if $$x$$ is minimal, then $$\lambda^T z$$ does not have a unique minimizer. Therefore, for the same $$\lambda$$, there can be multiple minimal elements, and there can be multiple minimal elements for different $$\lambda$$.

The figure below illustrates the existence of multiple minimal elements. The region with the thick black line at the bottom left indicates the area where minimal elements exist.
Here, $$x_1$$ is the minimizer of $$\lambda^T_1 z$$ and since $$\lambda_1 \succ_K^* 0$$, it is minimal. Another minimizer, $$x_2$$, also exists.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_05_Minimal_element.png" alt="[Fig2] Minimal element [1]" width="70%">
  <figcaption style="text-align: center;">[Fig2] Minimal element [1]</figcaption>
</p>
</figure>

However, the converse is not true. Even if a point $$x$$ is minimal in a set $$S$$, it may not be the minimizer of $$\lambda^T z$$ for some $$\lambda$$ and $$z \in S$$. The figure below shows an example of a minimal element that is not a minimizer. Here, the convexity of the set seems to play a crucial role in this converse not being true.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_06_Minimal_element2.png" alt="[Fig3] An example of a minimal element that is not a minimizer [1]" width="70%">
  <figcaption style="text-align: center;">[Fig3] An example of a minimal element that is not a minimizer [1]</figcaption>
</p>
</figure>

This converse theorem does not strengthen with $$\lambda_1 \succ_K^* 0$$. In the left figure below, $$x_1 \in S_1$$ is minimal, but not the minimizer of $$\lambda_1^T x_1$$. The right figure shows that $$x_2 \in S_2$$ is not minimal, but is the minimizer of $$\lambda_2^T x_2$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_07_Minimal_element3.png" alt="[Fig4] Examples where the converse does not strengthen with $$\lambda_1 \succ_K^* 0$$ [1]" width="70%">
  <figcaption style="text-align: center;">$$\text{[Fig4] Examples where the converse does not strengthen with } \lambda_1 \succ_K^* 0 \text{ [1]}$$</figcaption>
</p>
</figure>

### Optimal production frontier
Consider a product that needs to be produced using n resources (labor, electricity, natural gas, water, etc.).
This product can be produced in several ways. For each production method, there is a resource vector $$x \in \mathbb{R}$$, where $$x_i$$ denotes the amount of resource $$i$$ consumed. It is assumed that the resource consumption $$x_i$$ is nonnegative, and the resources have high value.

The production set $$P \subseteq \mathbb{R}^n$$ is defined as the set of all resource vectors $$x$$. A production method with a minimal resource vector is called **Pareto optimal** or **efficient**. The set of minimal elements of $$P$$ is called the **efficient production frontier**.

Let's briefly look at Pareto optimality.

Suppose there are two production methods, one with resource vector $$x$$ ($$P_x$$) and the other with resource vector $$y$$ ($$P_y$$). If for all $$i$$, $$x_i \le y_i$$, and for some $$i$$, $$x_i \lt y_i$$, then we can say that $$P_x$$ is better than $$P_y$$. In other words, a method that does not use more resources than another, or uses at least one resource less, is considered better. That is, this corresponds to the case where $$x \preceq y$$ and $$x \ne y$$.
If there is no method better than $$P_x$$, then $$P_x$$ is said to be Pareto optimal.

By minimizing the following expression, we can find the Pareto optimal production method. Here, $$ \lambda_i$$ can be considered as the price of resource $$i$$. Minimizing $$ \lambda^T x$$ with respect to $$P$$ yields the cheapest production method. Since the prices are positive, the result of the minimization is always Pareto optimal.

> $$ \lambda^T x =$$ $$ \lambda^T_1 x_1 + \lambda^T_2 x_2 + ... + \lambda^T_n x_n, \lambda \succ 0 $$

The figure below illustrates this situation well. In the figure, $$x_1, x_2, x_3$$ are Pareto optimal, while $$x_4, x_5$$ are not.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_08_Pareto_optimal.png" alt="[Fig5] Optimal production frontier [1]" width="70%">
  <figcaption style="text-align: center;">[Fig5] Optimal production frontier [1]</figcaption>
</p>
</figure>


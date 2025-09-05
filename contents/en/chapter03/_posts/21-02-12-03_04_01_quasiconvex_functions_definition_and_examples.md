---
layout: post
title: '03-04-01 Quasiconvex functions: definition and examples'
chapter: '03'
order: 9
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

A function $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ is quasiconvex if all its sublevel sets $$\{x \mid f(x) \leq \alpha\}$$ are convex for every $$\alpha \in \mathbb{R}$$.

**Quasiconvex functions generalize convex functions** and appear frequently in optimization problems.

## Definition

A function $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ is called **quasiconvex** (or **unimodal**) if its domain $$\text{dom}f$$ and all sublevel sets $$S_{\alpha}$$ (see [03-01-03]({% multilang_post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %})) are convex.

>$$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ is quasiconvex if $$\text{dom}f$$ and
>$$S_{\alpha} =\{x \in \text{dom}f \mid f(x) \leq \alpha\}$$ for $$\alpha \in \mathbb{R}$$ are convex.

If function $$-f$$ is quasiconvex, then $$f$$ is called **quasiconcave**.
>$$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ is quasiconcave if $$\text{dom}f$$ and
>$$S_{\alpha} = \{ x \in \text{dom}f \mid f(x) \geq \alpha \}$$ for $$\alpha \in \mathbb{R}$$ are convex.

When $$f$$ is both quasiconvex and quasiconcave, it is called **quasilinear**, and the function's domain and all level sets $$\{x \mid f(x)=\alpha\}$$ are convex. The following figure shows an example of a quasiconvex function.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig3.9_quasiconvex_ftn_cAsoUpr.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] quasiconvex function on R [1]</figcaption>
</p>
</figure>


For $$\alpha$$, the $$\alpha$$-sublevel set $$S_{\alpha}$$ is convex, namely the interval $$[a,b]$$. The $$\beta$$-sublevel set $$S_{\beta}$$ is the interval $$(-\infty,c]$$. **Convex functions have convex sublevel sets and are quasiconvex, but the converse is not true.**
> $$f$$ : convex $$\Longrightarrow$$ $$f$$ : quasiconvex


<br>
## Examples

Let's examine various examples of quasiconvex functions.

### Logarithm
$$\log x$$ on $$\mathbb{R}_{++}$$ is quasiconvex. (It is also quasiconcave, so it has the property of being quasilinear.)
> $$\log x$$ on $$\mathbb{R}_{++}$$

### Ceiling function
The ceiling function is quasiconvex (and also quasiconcave).
>$$\text{ceil}(x) = \inf \{z \in \mathbb{Z} \mid z \geq x\}$$

### Length of vector
If we define the length of $$x \in \mathbb{R}^n$$ as the largest index of nonzero components,
>$$f(x) = \max\{i \mid x_i \neq 0\}$$

This satisfies
>$$f(x) \leq \alpha \iff x_i = 0$$ for $$i = \lfloor\alpha\rfloor + 1,...,n$$ on $$\mathbb{R}^n$$

which defines a subspace, so it is quasiconvex.
(Note: A subspace is closed under addition and scalar multiplication. Any subspace of $$\mathbb{R}^n$$ is also a convex set.)

### Linear-fractional function
Under the following conditions, function $$f$$ is both quasiconvex and quasiconcave, i.e., quasilinear.
>$$f(x) = \frac{a^Tx+b}{c^Tx+d}$$ with $$\text{dom}f =\{x \mid c^Tx + d > 0\}$$

### Distance ratio function
For $$a, b \in \mathbb{R}^n$$, when function $$f$$ is defined as follows, representing the ratio of Euclidean distances from $$x$$ to $$a$$ and from $$x$$ to $$b$$,
$$f$$ is quasiconvex on the halfspace $$\{x \mid \|x - a\|_2 \leq \|x - b\|_2 \}$$.

> $$f(x) = \frac{\|x - a\|_2}{\|x - b\|_2}$$

Under the condition $$\alpha \leq 1$$, this becomes a convex set in the form of a Euclidean ball, so $$f$$ is quasiconvex.

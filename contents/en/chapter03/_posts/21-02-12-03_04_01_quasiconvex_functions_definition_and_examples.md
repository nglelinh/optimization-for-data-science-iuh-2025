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

Maximizing return-to-risk ratios, minimizing unit production cost $$\frac{\text{fixed} + \text{variable}}{\text{output}}$$, or minimizing the ratio of distances to two targets all produce **linear-fractional** objectives that fail the ordinary Hessian test for convexity. Yet every one of them is *quasiconvex*: multiplying both sides of $$\frac{a^T x + b}{c^T x + d} \le \alpha$$ by the positive denominator instantly turns the nonlinear ratio into a single linear halfspace!

## Background Knowledge Map: Recognizing Canonical Quasiconvex Functions

- **Sublevel Set Criterion:** Check directly whether $$\{x \in \text{dom}\,f : f(x) \le \alpha\}$$ is a convex set for every $$\alpha \in \mathbb{R}$$.
- **Quasilinear Functions (Monotone 1D & Logs):** Functions like $$\log x$$ ($$x > 0$$) and $$\lceil x \rceil$$ are both quasiconvex and quasiconcave because every sublevel and superlevel set is a half-line.
- **Linear-Fractional Functions:** $$f(x) = \frac{a^T x + b}{c^T x + d}$$ on $$c^T x + d > 0$$ is quasilinear—its sublevel sets are halfspaces, making fractional linear programming solvable by bisection or Charnes–Cooper transformation.
- **Distance Ratios & Vector Length:** Ratios $$\frac{\|x - a\|_2}{\|x - b\|_2}$$ on the halfspace where $$\|x - a\|_2 \le \|x - b\|_2$$ and the non-smooth "last nonzero index" length function are classic quasiconvex benchmarks.

### Step-by-Step Worked Example (Read Slowly): Sublevel Halfspace of a Linear-Fractional Function

Verify that $$f(x_1, x_2) = \frac{2x_1 + x_2 + 1}{x_1 + x_2 + 2}$$ is quasiconvex on $$D = \{(x_1, x_2) : x_1 + x_2 + 2 > 0\}$$.

1. **Clear the strictly positive denominator in $$f(x) \le \alpha$$:**
   $$\frac{2x_1 + x_2 + 1}{x_1 + x_2 + 2} \le \alpha \iff 2x_1 + x_2 + 1 \le \alpha(x_1 + x_2 + 2).$$
2. **Collect terms into standard halfspace form:**
   $$(2 - \alpha)x_1 + (1 - \alpha)x_2 + (1 - 2\alpha) \le 0.$$
3. **Inspect the sublevel set $$S_\alpha$$:** For every fixed $$\alpha \in \mathbb{R}$$, this is a single linear inequality intersected with the open halfspace $$D$$—an intersection of two convex halfspaces, hence **convex**!
   - *Concrete check at $$\alpha = 1$$:* $$(2 - 1)x_1 + (1 - 1)x_2 + (1 - 2) \le 0 \iff x_1 \le 1$$, a clean vertical halfspace.

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

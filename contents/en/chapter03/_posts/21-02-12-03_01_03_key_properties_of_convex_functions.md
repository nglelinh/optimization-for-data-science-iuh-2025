---
layout: post
title: 03-01-03 Key properties of convex functions
chapter: '03'
order: 5
owner: Minjoo Lee
categories:
- chapter03
lang: en
---
## Epigraph characterization
As discussed in Section 1.2, $$f$$ is convex if and only if its epigraph is a convex set, and vice versa.

> $$f$$ is convex $$\iff epi(f) = \{(x,t) \in \mathbb{R}^{n+1} \mid x \in \text{dom} f, f(x) \le t \}$$ is a convex set

## Convex sublevel sets
If a function $$f$$ is convex, its sublevel sets are also convex.

> $$\{x \in \text{dom } f: f(x) \leq t\}$$, for all $$t \in \mathbb{R}$$

### [Note] Sublevel set
For a function $$f:\mathbb{R}^n \mapsto \mathbb{R}$$, $$C_\alpha = \{x \in \text{dom} f | f(x) \leq \alpha\}$$ is called the *$$\alpha$$-sublevel set*.

## First-order characterization
If a function $$f$$ is **differentiable**, the following holds:
If the domain $$\text{dom} f$$ is convex and for all $$x, y \in \text{dom} f$$, $$f(y) \geq f(x) +\nabla f(x)^T(y-x)$$, then $$f$$ is convex, and vice versa.

> $$f$$ is convex $$\iff \text{dom}f$$ is convex, and $$f(y) \geq f(x) +\nabla f(x)^T(y-x)$$ for all $$x,y \in \text{dom} f$$

The figure below illustrates the first-order condition for a differentiable convex function $$f$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/1st_order_condition.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Convex Function [1]</figcaption>
</p>
</figure>

## Second-order characterization
If a function $$f$$ is twice differentiable, it has the following property:

- If the second derivative $$\nabla^2f(x)$$ is positive semidefinite for all $$x \in \text{dom} f$$ and $$\text{dom} f$$ is convex, then $$f$$ is convex, and vice versa.
> $$f$$ is convex $$\iff \nabla^2f(x) \succeq 0$$ for all $$x \in \text{dom} f, \text{dom} f$$: convex

- If the second derivative $$\nabla^2f(x)$$ is positive definite for all $$x \in \text{dom} f$$, then $$f$$ is strictly convex.
> if $$\nabla^2f(x) \succ 0$$ for all $$x \in \text{dom} f$$, then $$f$$ is strictly convex

- In other words, the curvature is always nonnegative.


## Jensen's inequality

Let $$f$$ be a convex function and $$w_1, ..., w_n$$ be positive weights such that $$\sum_{i=1}^{n} w_i = 1$$. Then, the following inequality holds:

$$\sum_{i=1}^{n} w_i f(x_i) \geq f \left ( \sum_{i=1}^{n} w_i x_i \right )$$


If a function $$f$$ is convex, it satisfies the following inequality:
>$$f(tx_1 + (1 - t)x_2) \le tf(x_1) + (1 - t)f(x_2) \text{ for } 0 \le t \le 1 $$

>*Extension*:<br>
>$$X$$ is a random variable supported on $$\text{dom } f$$, then $$f(E[X]) \le E[f(X)]$$

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/jensen_inequality.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2] Jensen's Inequality [2]</figcaption>
</p>
</figure>

### **Isn't Jensen's inequality exactly the definition of a convex function?** 

The answer is no—Jensen's inequality is a consequence and generalization of the convexity definition, not the definition itself.

- This extends the two-point case ($$k=2$$) in the definition to any finite number of points (and can be further generalized to integrals for probability measures).
- **Why It's a Generalization:** The basic definition is for two points (binary convex combination). Jensen applies it iteratively to more points. For instance:
  - For $$k=2$$, Jensen reduces exactly to the definition.
  - For $$k=3$$, you can apply the definition recursively: First combine two points, then with the third.

---
### Short Example

Let's use the convex function $$f(x) = x^2$$.
Consider two numbers: $$x_1 = 1$$ and $$x_2 = 3$$.
We want to compare $$f\left(\frac{x_1+x_2}{2}\right)$$ with $$\frac{f(x_1)+f(x_2)}{2}$$.

1.  **Calculate the function of the average:**
    The average of $$x_1$$ and $$x_2$$ is $$\frac{1+3}{2} = \frac{4}{2} = 2$$.
    Applying the function: $$f(2) = 2^2 = 4$$.

2.  **Calculate the average of the function values:**
    $$f(x_1) = f(1) = 1^2 = 1$$.
    $$f(x_2) = f(3) = 3^2 = 9$$.
    The average of these function values is $$\frac{1+9}{2} = \frac{10}{2} = 5$$.

Comparing the two results: $$4 \le 5$$.
This demonstrates Jensen's inequality: $$f\left(\frac{1+3}{2}\right) \le \frac{f(1)+f(3)}{2}$$.
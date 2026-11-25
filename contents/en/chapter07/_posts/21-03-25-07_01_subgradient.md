---
layout: post
title: 07-01 Subgradient
chapter: '07'
order: 2
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
lesson_type: required
---

At a smooth point on a convex bowl, you can lay a flat wooden board underneath the bowl and there is only one angle that touches it without poking through—the tangent plane. Now press that same board underneath the sharp tip of a V-shaped cone: suddenly you can rock the board back and forth across a whole range of angles, and *every* tilt still supports the cone from below! Every valid tilt is a **subgradient**.

## Background Knowledge Map: Definition and Geometry of Subgradients

1. **The Global Underestimator Inequality**: A vector $$g \in \mathbb{R}^n$$ is a subgradient of $$f$$ at $$x$$ if
   $$f(y) \ge f(x) + g^T(y - x) \quad \text{for all } y \in \operatorname{dom}(f).$$
   Notice this is a *global* inequality—not a local limit—which is why it works cleanly at corners where two-sided limits fail to exist.
2. **Consistency with Gradients**: If $$f$$ is convex and differentiable at $$x$$, then $$\nabla f(x)$$ is the *unique* subgradient at $$x$$. Conversely, if a convex function has a unique subgradient at an interior point $$x$$, then $$f$$ is differentiable at $$x$$.
3. **Existence Everywhere in the Interior**: Every convex function has at least one subgradient at every point in the relative interior of its domain (guaranteed by the Supporting Hyperplane Theorem applied to the convex epigraph $$\operatorname{epi}(f)$$).
4. **Canonical Nonsmooth Building Blocks**:
   - Absolute value $$|x|$$: $$g = \operatorname{sign}(x)$$ for $$x \neq 0$$, and any $$g \in [-1, 1]$$ at $$x = 0$$.
   - Euclidean norm $$\|x\|_2$$: $$g = x/\|x\|_2$$ for $$x \neq 0$$, and any $$\|g\|_2 \le 1$$ at $$x = 0$$.
   - Pointwise maximum $$\max\{f_1(x), f_2(x)\}$$: any convex combination of gradients of the *active* branches achieving the maximum.

### Step-by-Step Worked Example (Read Slowly): Verifying Subgradients of $$f(x) = \|x\|_2$$ at $$x = 0$$

For the Euclidean norm $$f(x) = \|x\|_2$$ on $$\mathbb{R}^2$$, verify directly from the definition which vectors $$g \in \mathbb{R}^2$$ are subgradients at $$x = (0, 0)$$.

1. **Plug $$x = 0$$ into the subgradient inequality**:
   $$\|y\|_2 \ge \|0\|_2 + g^T(y - 0) \iff g^T y \le \|y\|_2 \quad \text{for all } y \in \mathbb{R}^2.$$
2. **Test a valid vector $$g = (0.6, 0.8)$$** (with $$\|g\|_2 = \sqrt{0.36 + 0.64} = 1$$):
   - By Cauchy–Schwarz, $$g^T y \le \|g\|_2 \|y\|_2 = 1 \cdot \|y\|_2 = \|y\|_2$$ for every $$y \in \mathbb{R}^2$$.
   - Hence $$g = (0.6, 0.8)$$ **is a valid subgradient** at $$0$$!
3. **Test an invalid vector $$g = (1, 1)$$** (with $$\|g\|_2 = \sqrt{2} > 1$$):
   - Choose $$y = g = (1, 1)$$. Then $$g^T y = 1 + 1 = 2$$, whereas $$\|y\|_2 = \sqrt{2} \approx 1.414 < 2$$.
   - The inequality $$f(y) \ge g^T y$$ fails! Thus $$g = (1, 1)$$ pokes *above* the cone and is **not** a subgradient.
4. **Conclusion**: $$\partial \|0\|_2 = \{g \in \mathbb{R}^2 : \|g\|_2 \le 1\}$$, the closed unit Euclidean ball.

# Subgradient

For a convex function $$f:\mathbb{R}^n \to \mathbb{R}$$, a subgradient at $$x$$ is any vector $$g \in \mathbb{R}^n$$ that satisfies:

> $$
\begin{equation}\label{subgradient}
f(y) \geq f(x) + g^T(y-x), \text{ for all } y
\end{equation}
$$

The subgradient defined above:

- Generalizes the gradient for convex functions to cases where the function is not differentiable.
- For convex functions, a subgradient always exists. If $$f$$ is differentiable at $$x$$, then $$\nabla f(x)$$ is the unique subgradient.
- For non-convex functions, a subgradient may be defined similarly, but it may not always exist depending on the function.

Below are examples of subgradients for some functions.

### Example 1

<center>
$$f:\mathbb{R} \to \mathbb{R}, f(x) =  \vert x \vert $$
</center>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-1.png" alt="Subgradient1" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Fig 1] Subgradient of } f(x)= \vert x \vert \text{ [3]}$$</figcaption>
</figure>

- For $$x \neq 0$$, $$ \vert y \vert \geq \vert x \vert + g^T(y-x)$$ must hold. That is,

$$ \vert y \vert - g^Ty \geq \vert x \vert - g^Tx $$. If $$ \vert x \vert - g^Tx = 0 $$, i.e., $$g=\text{sign}(x)$$, then the condition holds for all $$y$$. Thus, $$g=\text{sign}(x)$$ ([Wikipedia: Sign function](https://en.wikipedia.org/wiki/Sign_function)).
- For $$x=0$$, $$ \vert y \vert \geq g^Ty $$ must hold. Therefore, $$g \in [-1,1]$$.

### Example 2

<center>
$$f:\mathbb{R}^n \to \mathbb{R}, f(x) =  \| x \|_1$$ 
</center>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-3.png" alt="Subgradient2" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Fig 2] Subgradient of }f(x)= \| x \|_1\text{ [3]}$$</figcaption>
</figure>

At a point $$x=(x_1,x_2,\dots,x_n)$$,

- For $$x_i \neq 0, i \in \{1,2,\dots,n\}$$, since it is differentiable at $$x_i$$, we have $$g_i=\text{sign}(x_i)$$

- For $$x_i=0, i \in \{1,2,\dots,n\}$$, we have $$g_i \in [-1,1]$$


### Example3

<center>
$$f:\mathbb{R}^n \to \mathbb{R}, f(x) =  \vert x \vert _2$$
</center>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-2.png" alt="Subgradient3" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Fig 3] Subgradient of }f(x)= \vert x \vert _2\text{ [3]}$$</figcaption>
</figure>

- For $$x \neq 0$$, since it is differentiable, we have $$g=\nabla \sqrt{x^Tx} = \frac{1}{2}(x^Tx)^{-\frac{1}{2}} (2x) = \frac{x}{\vert x \vert _2}$$

- For $$x=0$$, we have $$ \vert y \vert _2 \geq g^Ty \Longrightarrow  \vert y \vert _2 \geq  \vert g \vert _2 \vert y \vert _2 \cos \theta$$. Therefore, $$g \in \{z: \vert z \vert _2 \leq 1 \}$$


### Example4

$$f(x) = \max f_1(x),f_2(x) $$, where $$f_1,f_2:\mathbb{R}^n \to \mathbb{R}$$ are both convex and differentiable functions.  

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-4.png" alt="Subgradient4" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Fig 4] Subgradient of }f(x)=\max f_1(x),f_2(x) \text{ [3]}$$</figcaption>
</figure>

- For $$f_1(x) > f_2(x)$$, we have $$g = \nabla f_1(x)$$

- For $$f_1(x) < f_2(x)$$, we have $$g = \nabla f_2(x)$$

- For $$f_1(x) = f_2(x)$$, we have $$g \in \{\theta_1 \nabla f_1(x) + \theta_2 \nabla f_2(x): \theta_1 + \theta_2 = 1, \theta_1 \geq 0, \theta_2 \geq 0 \}$$  

### Subgradients at a kink

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/subgradient-fan_en.mp4"></video>
</div>

At a kink of $$f(x)=\max_i f_i(x)$$, many lines stay below the graph and touch it at that point; every one of their slopes is a subgradient.

### Try it yourself: subgradients at a kink

<div class="opx-explainer" data-opx="subg" data-lang="en"></div>

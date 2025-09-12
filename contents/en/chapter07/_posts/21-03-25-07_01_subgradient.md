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

---
layout: post
title: 07-01 Gradient dưới (Subgradient)
chapter: '07'
order: 2
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
lesson_type: required
---

# Gradient dưới (Subgradient)

Đối với một hàm lồi $$f:\mathbb{R}^n \to \mathbb{R}$$, gradient dưới tại $$x$$ là bất kỳ vector $$g \in \mathbb{R}^n$$ nào thỏa mãn:

> $$
\begin{equation}\label{subgradient}
f(y) \geq f(x) + g^T(y-x), \text{ với mọi } y
\end{equation}
$$

Gradient dưới được định nghĩa ở trên:

- Tổng quát hóa gradient cho các hàm lồi trong trường hợp hàm không khả vi.
- Đối với các hàm lồi, gradient dưới luôn tồn tại. Nếu $$f$$ khả vi tại $$x$$, thì $$\nabla f(x)$$ là gradient dưới duy nhất.
- Đối với các hàm không lồi, gradient dưới có thể được định nghĩa tương tự, nhưng nó có thể không luôn tồn tại tùy thuộc vào hàm.

Dưới đây là các ví dụ về gradient dưới cho một số hàm.

### Ví dụ 1

<center>
$$f:\mathbb{R} \to \mathbb{R}, f(x) =  \vert x \vert $$
</center>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-1.png" alt="Subgradient1" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Hình 1] Gradient dưới của } f(x)= \vert x \vert \text{ [3]}$$</figcaption>
</figure>

- Với $$x \neq 0$$, $$ \vert y \vert \geq \vert x \vert + g^T(y-x)$$ phải được thỏa mãn. Tức là,

$$ \vert y \vert - g^Ty \geq \vert x \vert - g^Tx $$. Nếu $$ \vert x \vert - g^Tx = 0 $$, tức là $$g=\text{sign}(x)$$, thì điều kiện này được thỏa mãn với mọi $$y$$. Do đó, $$g=\text{sign}(x)$$ ([Wikipedia: Hàm dấu](https://en.wikipedia.org/wiki/Sign_function)).
- Với $$x=0$$, $$ \vert y \vert \geq g^Ty $$ phải được thỏa mãn. Do đó, $$g \in [-1,1]$$.

### Ví dụ 2

<center>
$$f:\mathbb{R}^n \to \mathbb{R}, f(x) =  \| x \|_1$$ 
</center>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-3.png" alt="Subgradient2" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Hình 2] Gradient dưới của }f(x)= \| x \|_1\text{ [3]}$$</figcaption>
</figure>

Tại một điểm $$x=(x_1,x_2,\dots,x_n)$$,

- Với $$x_i \neq 0, i \in \{1,2,\dots,n\}$$, vì hàm khả vi tại $$x_i$$, ta có $$g_i=\text{sign}(x_i)$$

- Với $$x_i=0, i \in \{1,2,\dots,n\}$$, ta có $$g_i \in [-1,1]$$


### Ví dụ 3

<center>
$$f:\mathbb{R}^n \to \mathbb{R}, f(x) =  \vert x \vert _2$$
</center>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-2.png" alt="Subgradient3" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Hình 3] Gradient dưới của }f(x)= \vert x \vert _2\text{ [3]}$$</figcaption>
</figure>

- Với $$x \neq 0$$, vì hàm khả vi, ta có $$g=\nabla \sqrt{x^Tx} = \frac{1}{2}(x^Tx)^{-\frac{1}{2}} (2x) = \frac{x}{\vert x \vert _2}$$

- Với $$x=0$$, ta có $$ \vert y \vert _2 \geq g^Ty \Longrightarrow  \vert y \vert _2 \geq  \vert g \vert _2 \vert y \vert _2 \cos \theta$$. Do đó, $$g \in \{z: \vert z \vert _2 \leq 1 \}$$


### Ví dụ 4

$$f(x) = \max f_1(x),f_2(x) $$, trong đó $$f_1,f_2:\mathbb{R}^n \to \mathbb{R}$$ đều là các hàm lồi và khả vi.  

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-4.png" alt="Subgradient4" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Hình 4] Gradient dưới của }f(x)=\max f_1(x),f_2(x) \text{ [3]}$$</figcaption>
</figure>

- Với $$f_1(x) > f_2(x)$$, ta có $$g = \nabla f_1(x)$$

- Với $$f_1(x) < f_2(x)$$, ta có $$g = \nabla f_2(x)$$

- Với $$f_1(x) = f_2(x)$$, ta có $$g \in \{\theta_1 \nabla f_1(x) + \theta_2 \nabla f_2(x): \theta_1 + \theta_2 = 1, \theta_1 \geq 0, \theta_2 \geq 0 \}$$  

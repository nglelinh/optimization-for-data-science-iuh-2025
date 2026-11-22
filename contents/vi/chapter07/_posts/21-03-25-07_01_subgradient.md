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

Đối với một hàm lồi $$f:\mathbb{R}^n \to \mathbb{R}$$, gradient dưới (subgradient) của $$f$$ tại điểm $$x$$ là bất kỳ vector $$g \in \mathbb{R}^n$$ nào thỏa mãn:

> $$
\begin{equation}\label{subgradient}
f(y) \geq f(x) + g^T(y-x), \text{ với mọi } y
\end{equation}
$$

Từ định nghĩa trên, ta có một số nhận xét cơ bản về gradient dưới:

- Đây là sự tổng quát hóa của gradient cho các hàm lồi trong trường hợp hàm không khả vi.
- Với mọi hàm lồi, gradient dưới luôn tồn tại. Nếu $$f$$ khả vi tại $$x$$, thì $$\nabla f(x)$$ là gradient dưới duy nhất tại điểm đó.
- Với hàm không lồi, gradient dưới vẫn có thể được định nghĩa theo cùng bất đẳng thức trên, nhưng có thể không tồn tại tùy thuộc vào từng hàm cụ thể.

Dưới đây là một số ví dụ về gradient dưới của các hàm thường gặp.

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

- Với $$x \neq 0$$, bất đẳng thức $$ \vert y \vert \geq \vert x \vert + g^T(y-x)$$ phải đúng với mọi $$y$$, tương đương với $$ \vert y \vert - g^Ty \geq \vert x \vert - g^Tx $$. Khi $$ \vert x \vert - g^Tx = 0 $$, tức là $$g=\text{sign}(x)$$, bất đẳng thức này luôn thỏa mãn với mọi $$y$$. Do đó, $$g=\text{sign}(x)$$ ([Wikipedia: Hàm dấu](https://en.wikipedia.org/wiki/Sign_function)).
- Với $$x=0$$, điều kiện trở thành $$ \vert y \vert \geq g^Ty $$ với mọi $$y$$, suy ra $$g \in [-1,1]$$.

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

Tại điểm $$x=(x_1,x_2,\dots,x_n)$$:

- Với $$x_i \neq 0, i \in \{1,2,\dots,n\}$$, vì hàm khả vi theo tọa độ $$x_i$$, ta có $$g_i=\text{sign}(x_i)$$.
- Với $$x_i=0, i \in \{1,2,\dots,n\}$$, ta có $$g_i \in [-1,1]$$.

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

- Với $$x \neq 0$$, hàm khả vi nên ta có $$g=\nabla \sqrt{x^Tx} = \frac{1}{2}(x^Tx)^{-\frac{1}{2}} (2x) = \frac{x}{\vert x \vert _2}$$.
- Với $$x=0$$, điều kiện là $$ \vert y \vert _2 \geq g^Ty \Longrightarrow  \vert y \vert _2 \geq  \vert g \vert _2 \vert y \vert _2 \cos \theta$$ với mọi $$y$$. Do đó, $$g \in \{z: \vert z \vert _2 \leq 1 \}$$.

### Ví dụ 4

Xét $$f(x) = \max f_1(x),f_2(x) $$, trong đó $$f_1,f_2:\mathbb{R}^n \to \mathbb{R}$$ đều là các hàm lồi và khả vi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-4.png" alt="Subgradient4" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Hình 4] Gradient dưới của }f(x)=\max f_1(x),f_2(x) \text{ [3]}$$</figcaption>
</figure>

- Với $$f_1(x) > f_2(x)$$, ta có $$g = \nabla f_1(x)$$.
- Với $$f_1(x) < f_2(x)$$, ta có $$g = \nabla f_2(x)$$.
- Với $$f_1(x) = f_2(x)$$, ta có $$g \in \{\theta_1 \nabla f_1(x) + \theta_2 \nabla f_2(x): \theta_1 + \theta_2 = 1, \theta_1 \geq 0, \theta_2 \geq 0 \}$$.

### Gradient dưới tại điểm gấp khúc

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/subgradient-fan_vi.mp4"></video>
</div>

Tại điểm gấp khúc của $$f(x)=\max_i f_i(x)$$, có nhiều đường thẳng nằm dưới đồ thị và tiếp xúc với đồ thị tại điểm đó; hệ số góc của mỗi đường thẳng như vậy đều là một gradient dưới.

### Tự tay thử: gradient dưới tại điểm gấp khúc

<div class="opx-explainer" data-opx="subg" data-lang="vi"></div>

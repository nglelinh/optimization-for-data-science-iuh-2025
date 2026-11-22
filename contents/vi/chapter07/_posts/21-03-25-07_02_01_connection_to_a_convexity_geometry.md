---
layout: post
title: 07-02-01 Liên hệ với hình học tập lồi
chapter: '07'
order: 4
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Đối với một tập lồi $$C \subseteq \mathbb{R}^n$$, xét hàm chỉ thị $$I_C: \mathbb{R}^n \to \mathbb{R}$$ được định nghĩa như sau:

>
$$
I_C(x) = I\{x \in C \} =
\begin{cases}
0               &\text{nếu } x \in C \\
\infty         &\text{nếu } x \notin C 
\end{cases}
$$

Vi phân dưới của hàm chỉ thị có ý nghĩa hình học sau:

### Bổ đề
Với mọi $$x \in C$$, vi phân dưới $$\partial I_C(x)$$ trùng với nón pháp tuyến $$\mathcal{N}_C(x)$$ của tập $$C$$ tại $$x$$:

>
\begin{equation}
\mathcal{N}_C(x) = \{g \in \mathbb{R}^n | g^Tx \geq g^Ty \text{  với mọi  } y \in C \}
\end{equation}

### Chứng minh

Theo định nghĩa, một gradient dưới $$g$$ của $$I_C$$ tại $$x$$ phải thỏa mãn:
>
\begin{equation}
I_C(y) \geq I_C(x) + g^T(y-x) \text{ với mọi } y
\end{equation}

Vì $$x \in C$$ nên $$I_C(x)=0$$, do đó bất đẳng thức trên trở thành:
>
\begin{equation}
I_C(y) \geq g^T(y-x) \text{ với mọi } y
\end{equation}

Ta xét hai trường hợp của $$y$$:

Thứ nhất, với mọi $$y \in C$$, ta có $$I_C(y) = 0$$, nên:
>
\begin{equation}
I_C(y) = 0 \geq g^T(y-x)
\end{equation}

Điều này tương đương với $$g^Tx \geq g^Ty$$ với mọi $$y \in C$$.

Thứ hai, với mọi $$y \notin C$$, ta có $$I_C(y) = \infty$$, nên bất đẳng thức
>
$$I_C(y)=\infty \geq g^T(y-x)$$

luôn đúng với mọi vector $$g$$.

Kết hợp cả hai trường hợp, tập hợp tất cả các gradient dưới của $$I_C$$ tại $$x \in C$$ chính là:
>
$$\{g \in \mathbb{R}^n | g^Tx \geq g^Ty \text{ với mọi } y \in C\}$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_02_subgrad-5.png" alt="connection_to_convexity_geometry" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Hình 1] Nón pháp tuyến [1]</figcaption>
</figure>
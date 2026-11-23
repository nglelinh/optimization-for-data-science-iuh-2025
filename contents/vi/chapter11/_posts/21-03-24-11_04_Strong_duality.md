---
layout: post
title: 11-04 Tính đối ngẫu mạnh
chapter: '11'
order: 5
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

Khi giá trị tối ưu của bài toán gốc và bài toán đối ngẫu bằng nhau ($$f^* = g^*$$), ta nói **tính đối ngẫu mạnh (strong duality)** thỏa mãn. **Điều kiện Slater** là một điều kiện đủ phổ biến bảo đảm tính đối ngẫu mạnh.

## Điều kiện Slater

Nếu bài toán gốc là bài toán tối ưu lồi và tồn tại ít nhất một điểm $$x \in \mathbb{R}^n$$ **khả thi chặt** (strictly feasible), tức thỏa mãn:

>
$$
\begin{equation}
h_1(x)<0,\dots,h_m(x)<0, \text{ and } l_1(x) = 0,\dots,l_r(x) = 0,
\end{equation}
$$

thì tính đối ngẫu mạnh được thỏa mãn ($$f^* = g^*$$).

**Lưu ý quan trọng:** Đối với các ràng buộc bất đẳng thức là hàm affine, điều kiện bất đẳng thức chặt ($$< 0$$) không bắt buộc — chỉ cần thỏa mãn bất đẳng thức không chặt ($$\leq 0$$).

## Ví dụ: Bài toán đối ngẫu của Support Vector Machine (SVM)

Cho $$y \in \{-1, 1\}^n$$ và ma trận dữ liệu $$X \in \mathbb{R}^{n \times p}$$ (với các hàng của $$X$$ là các mẫu $$x_1^T, \dots, x_n^T$$), bài toán SVM lề mềm được phát biểu như sau:

>
$$
\begin{alignat}{1}
\min_{\beta, \beta_0, \xi} & \quad \frac{1}{2}\parallel\beta\parallel_2^2 + C \sum_{i=1}^n \xi_i   \\\\
                                  s.t. & \quad \xi_i \geq 0, i=1,\dots,n   \\\\
                                       & \quad y_i(x_i^T \beta + \beta_0) \geq 1 - \xi_i, i=1,\dots,n
\end{alignat}
$$

Đưa vào các biến đối ngẫu $$v, w \geq 0$$, ta lập hàm Lagrangian:

>
$$
\begin{equation}
L(\beta,\beta_0,\xi,v,w) = \frac{1}{2} \parallel\beta\parallel_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i +  \sum_{i=1}^n w_i (1-\xi_i - y_i(x_i^T\beta + \beta_0))
\end{equation}
$$

Cực tiểu hóa theo $$\beta, \beta_0, \xi$$, ta thu được hàm đối ngẫu Lagrange:

>
$$
g(v,w) = 
\begin{cases}
-\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw, &\text{if $w=C1-v, w^Ty=0$} \\\\
-\infty, &\text{otherwise}
\end{cases}
$$

trong đó $$\tilde{X} = \text{diag}(y) X$$. Khử biến bù $$v \geq 0$$ (từ $$w = C\mathbf{1} - v$$ suy ra $$w \leq C\mathbf{1}$$), ta thu được bài toán đối ngẫu của SVM:

>
$$
\begin{alignat}{1}
\max_{w}  & \quad -\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw \\\\
     s.t. &  \quad 0 \leq w \leq C1, w^Ty = 0
\end{alignat}
$$

Vì bài toán gốc có hàm mục tiêu lồi, các ràng buộc bất đẳng thức đều là hàm affine theo $$(\beta, \beta_0, \xi)$$ và luôn tồn tại điểm khả thi, nên điều kiện Slater được thỏa mãn và tính đối ngẫu mạnh đúng đối với SVM.

### Đối ngẫu mạnh và Slater trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/strong-duality-slater_vi.mp4"></video>
</div>

Hàm đối ngẫu g(λ) nằm dưới p*, khoảng cách đối ngẫu làm chứng chỉ, hình (u, t) của đường tì, và một bài lồi không thỏa Slater có khoảng cách bằng 1.

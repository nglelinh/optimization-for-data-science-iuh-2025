---
layout: post
title: 11-02 Hàm đối ngẫu Lagrange
chapter: '11'
order: 3
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

Gọi $$C$$ là tập khả thi của bài toán gốc và $$f^*$$ là giá trị tối ưu gốc. Khi cực tiểu hóa $$L(x,u,v)$$ trên toàn bộ biến $$x$$, ta thu được cận dưới sau:

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

Hàm $$g(u,v)$$ được gọi là **hàm đối ngẫu Lagrange** và cung cấp một cận dưới cho $$f^*$$ với mọi cặp đối ngẫu khả thi $$u \geq 0, v$$.

Minh họa trong Hình 2:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_7.png" width="70%">
  <figcaption style="text-align: center;">[Hình 2] Ví dụ về hàm đối ngẫu Lagrangian[1]</figcaption>
</p>
</figure>

* Đường ngang đứt nét biểu thị giá trị tối ưu gốc $$f^*$$.
* Trục hoành là biến đối ngẫu $$\lambda$$.
* Đường liền nét biểu thị đồ thị hàm đối ngẫu $$g(\lambda)$$.

## Ví dụ: Quy hoạch bậc hai (Quadratic Program)

### 1) Trường hợp xác định dương ($$Q \succ 0$$)

Xét bài toán quy hoạch bậc hai với ma trận đối xứng xác định dương $$Q \succ 0$$:

>
$$
\begin{alignat}{1}
\min_x  & \quad \frac{1}{2}x^T Q x + c^T x \\\\
       s.t. & \quad Ax = b, \\\\
            & \quad x \geq 0
\end{alignat}
$$

#### Hàm Lagrangian
>
$$
\begin{equation}
L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^Tx + v^T (Ax-b)
\end{equation}
$$

#### Hàm đối ngẫu Lagrange

Để cực tiểu hóa $$L(x,u,v)$$ theo $$x$$, ta lấy đạo hàm theo $$x$$ và cho bằng không:

$$
\begin{equation}
Qx + (c - u + A^T v) = 0,
\end{equation}
$$

tức là:

$$
\begin{equation}
Qx = -(c - u + A^T v).
\end{equation}
$$

Vì $$Q \succ 0$$ là ma trận xác định dương nên khả nghịch, suy ra $$x^* = -Q^{-1}(c - u + A^T v)$$. Thay $$x^*$$ vào hàm Lagrangian, ta thu được:

$$
\begin{alignat}{1}
& \frac{1}{2} (c - u + A^T v)^T (Q^{-1})^T Q Q^{-1}(c - u + A^T v) - (c - u + A^T v)^T Q^{-1} (c - u + A^T v) - b^T v \\\
= & \frac{1}{2} (c - u + A^T v)^T Q^{-1}(c - u + A^T v) - (c - u + A^T v)^T Q^{-1} (c - u + A^T v) - b^T v \\\
= & -\frac{1}{2} (c-u+A^Tv)^T Q^{-1} (c-u+A^T v) - b^T v
\end{alignat}
$$

Do đó:

>
$$
\begin{equation}
g(u,v) = \min_x L(x,u,v) = -\frac{1}{2} (c-u+A^Tv)^T Q^{-1} (c-u+A^T v) - b^T v
\end{equation}
$$

Với mọi $$u \geq 0$$ và $$v$$, biểu thức này cho một cận dưới của giá trị tối ưu gốc $$f^*$$.

### 2) Trường hợp nửa xác định dương ($$Q \succeq 0$$)

Xét lại bài toán trên khi $$Q \succeq 0$$ là ma trận nửa xác định dương.

#### Hàm Lagrangian
>
$$
\begin{equation}
L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^Tx + v^T (Ax-b)
\end{equation}
$$

#### Hàm đối ngẫu Lagrange

Tương tự trường hợp xác định dương, điều kiện cực tiểu theo $$x$$ là:

$$
\begin{equation}
Qx = -(c-u+A^T v)
\end{equation}
$$

Vì $$Q \succeq 0$$ có thể suy biến (không khả nghịch), ta chia thành hai trường hợp:

1. $$c - u + A^T v \in \operatorname{col}(Q)$$ (tương đương $$c - u + A^T v \perp \operatorname{null}(Q)$$ do $$Q$$ đối xứng): phương trình có nghiệm $$x^* = -Q^+(c - u + A^T v)$$, trong đó $$Q^+$$ là nghịch đảo giả Moore–Penrose của $$Q$$.
2. $$c - u + A^T v \notin \operatorname{col}(Q)$$: phương trình vô nghiệm và $$L(x,u,v)$$ không bị chặn dưới theo $$x$$, nên giá trị cực tiểu bằng $$-\infty$$.

Tóm lại, hàm đối ngẫu Lagrange là:

>
$$
g(u,v) =
\begin{cases}
-\frac{1}{2} (c-u+A^T v)^T Q^{+} (c - u + A^T v) - b^T v  & \text{if $c-u+A^T v \perp \text{null}(Q)$} \\\\
-\infty  & \text{otherwise}
\end{cases}
$$

Với mọi $$u \geq 0$$ và $$v$$ thỏa mãn $$c - u + A^T v \perp \operatorname{null}(Q)$$, $$g(u,v)$$ là một cận dưới hữu hạn (không tầm thường) của $$f^*$$.

## Ví dụ: Quy hoạch bậc hai trong không gian 2 chiều

Trong Hình 3, $$f(x_1, x_2)$$ là một hàm bậc hai xét trên miền không âm ($$x \ge 0$$), và hàm đối ngẫu $$g(u_1, u_2)$$ là một hàm bậc hai xét trên miền $$u \ge 0$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_10.png" width="70%">
  <figcaption style="text-align: center;">[Hình 3] Ví dụ về chương trình bậc hai trong 2D</figcaption>
</p>
</figure>

* Điểm màu xanh biểu thị giá trị tối ưu đối ngẫu, còn điểm màu đỏ biểu thị giá trị tối ưu gốc.
* Với mọi $$u \ge 0$$, hàm đối ngẫu $$g(u)$$ luôn cho một cận dưới của $$f^*$$.
* Giá trị cực đại của hàm đối ngẫu $$g(u)$$ trùng khớp với giá trị tối ưu gốc $$f^*$$.

### Hàm đối ngẫu trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/dual-lower-bound_vi.mp4"></video>
</div>

Với mọi $$\lambda\ge 0$$, giá trị nhỏ nhất của hàm Lagrange $$g(\lambda)=\min_x L(x,\lambda)$$ là một cận dưới của $$p^*$$, và bài toán đối ngẫu cực đại hóa cận dưới đó.

### Tự tay thử: kéo nhân tử

<div class="opx-explainer" data-opx="d1" data-lang="vi"></div>

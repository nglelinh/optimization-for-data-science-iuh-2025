---
layout: post
title: 02-02-02 Ví dụ về hình nón lồi
chapter: '02'
order: 8
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Các ví dụ về hình nón lồi bao gồm hình nón chuẩn, hình nón pháp tuyến và hình nón nửa xác định dương.

## Hình nón chuẩn

**Hình nón chuẩn** là một hình nón được định nghĩa bởi tất cả các điểm $$(x, t)$$ sao cho $$\| x \| \le t$$ trong $$\mathbb{R}^{n+1}$$, trong đó chuẩn có thể là bất kỳ chuẩn nào.

> $$C = \{(x, t) : \| x \| \le t\} \subseteq \mathbb{R}^{n+1}$$, với chuẩn $$\|·\|$$

Hình dưới đây cho thấy hình nón chuẩn cho chuẩn $$l_2$$ $$\|·\|_2$$, còn được gọi là hình nón bậc hai hoặc hình nón kem.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.08_Norm_Cone.png" alt="[Hình1] Hình Nón Chuẩn [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Hình Nón Chuẩn [1]</figcaption>
</p>
</figure>

## Hình nón pháp tuyến

Với một tập $$C$$ và một điểm $$x \in C$$, **hình nón pháp tuyến** được định nghĩa như sau:

> $$N_C(x) = \{ g: g^T (y - x) \le 0, \text{ với mọi } y \in C \}$$

Hình nón pháp tuyến bao gồm tất cả các vector $$g$$ sao cho tích vô hướng với $$y-x$$ luôn nhỏ hơn hoặc bằng không với mọi $$y \in C$$. Điều này có nghĩa là góc giữa $$g$$ và $$y-x$$ nằm trong khoảng từ 90 đến 270 độ (tức là $$\cos\theta < 0$$).

* Nếu $$x$$ nằm trên biên, thì $$g$$ duy nhất là pháp tuyến của siêu phẳng hỗ trợ.
* Nếu $$x$$ là một đỉnh, có nhiều siêu phẳng hỗ trợ, vậy $$g$$ tạo thành hình quạt.
* Nếu $$x$$ nằm trong phần trong, thì $$g$$ duy nhất là vector không.

Hình dưới đây cho thấy vector pháp tuyến.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.04_2_Normal_Cone.png" alt="[Hình2] Hình Nón Pháp Tuyến [3]" width="70%">
  <figcaption style="text-align: center;">[Hình2] Hình Nón Pháp Tuyến [3]</figcaption>
</p>
</figure>


## Hình nón nửa xác định dương

**Hình nón nửa xác định dương** $$\mathbb{S}^n_+$$ được định nghĩa như sau, trong đó $$\mathbb{S}^n$$ biểu diễn các ma trận đối xứng $$n \times n$$:

> $$\mathbb{S}^n_+ = \{ X \in \mathbb{S}^n : X \succeq 0 \}$$

$$\mathbb{S}^n_+$$ là một hình nón lồi vì với $$\theta_1, \theta_2 \ge 0$$ và $$A, B \in \mathbb{S}^n_+$$, ta có $$\theta_1 A + \theta_2 B \in \mathbb{S}^n_+$$. Đây được gọi là **hình nón nửa xác định dương**.

Hình dưới đây cho thấy biên của hình nón nửa xác định dương trong $$\mathbb{S}^2_+$$ được vẽ trong $$(x, y, z) \in \mathbb{R}^3$$. Vì ma trận $$X$$ là nửa xác định dương, định thức của nó phải không âm.

$$
X = 
\begin{bmatrix}
x, y \\
y, z
\end{bmatrix}
\in \mathbb{S}^2_+ \iff x \ge 0, z \ge 0, xz \ge y^2$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.10_Positive_Semidefinite_Cone.png" alt="[Hình3] Hình nón nửa xác định dương [1]" width="70%">
  <figcaption style="text-align: center;">[Hình3] Hình nón nửa xác định dương [1]</figcaption>
</p>
</figure>

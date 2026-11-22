---
layout: post
title: 02-02-02 Ví dụ về hình nón lồi
chapter: '02'
order: 10
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Các ví dụ tiêu biểu về hình nón lồi gồm hình nón chuẩn, hình nón pháp tuyến và hình nón nửa xác định dương.

## Hình nón chuẩn

**Hình nón chuẩn** là tập hợp các điểm $$(x, t) \in \mathbb{R}^{n+1}$$ thỏa mãn $$\| x \| \le t$$, với $$\|\cdot\|$$ là một chuẩn bất kỳ trên $$\mathbb{R}^n$$:

> $$C = \{(x, t) : \| x \| \le t\} \subseteq \mathbb{R}^{n+1}$$, với chuẩn $$\|·\|$$

Hình dưới đây minh họa hình nón chuẩn ứng với chuẩn $$\ell_2$$ ($$\|·\|_2$$), còn gọi là hình nón bậc hai (second-order cone) hay hình nón kem.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.08_Norm_Cone.png" alt="[Hình1] Hình Nón Chuẩn [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Hình Nón Chuẩn [1]</figcaption>
</p>
</figure>

## Hình nón pháp tuyến

Cho một tập $$C$$ và điểm $$x \in C$$, **hình nón pháp tuyến** tại $$x$$ được định nghĩa là:

> $$N_C(x) = \{ g: g^T (y - x) \le 0, \text{ với mọi } y \in C \}$$

Hình nón pháp tuyến chứa tất cả các vector $$g$$ có tích vô hướng không dương với $$y - x$$ với mọi $$y \in C$$, nghĩa là góc $$\theta$$ giữa $$g$$ và $$y - x$$ thỏa mãn $$\cos\theta \le 0$$ (từ $$90^\circ$$ đến $$270^\circ$$).

* Nếu $$x$$ nằm trên phần biên trơn của $$C$$, các vector $$g \ne 0$$ cùng phương với vector pháp tuyến ngoài duy nhất của siêu phẳng hỗ trợ tại $$x$$.
* Nếu $$x$$ là một đỉnh, tồn tại nhiều siêu phẳng hỗ trợ nên tập các vector $$g$$ tạo thành hình quạt.
* Nếu $$x$$ nằm ở phần trong của $$C$$, vector duy nhất thuộc $$N_C(x)$$ là vector không.

Hình dưới đây minh họa các vector pháp tuyến tương ứng với từng vị trí của $$x$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.04_2_Normal_Cone.png" alt="[Hình2] Hình Nón Pháp Tuyến [3]" width="70%">
  <figcaption style="text-align: center;">[Hình2] Hình Nón Pháp Tuyến [3]</figcaption>
</p>
</figure>

## Hình nón nửa xác định dương

Ký hiệu $$\mathbb{S}^n$$ là tập các ma trận đối xứng cỡ $$n \times n$$. **Hình nón nửa xác định dương** $$\mathbb{S}^n_+$$ được định nghĩa là:

> $$\mathbb{S}^n_+ = \{ X \in \mathbb{S}^n : X \succeq 0 \}$$

Tập $$\mathbb{S}^n_+$$ là một hình nón lồi vì với mọi $$\theta_1, \theta_2 \ge 0$$ và $$A, B \in \mathbb{S}^n_+$$, ta luôn có $$\theta_1 A + \theta_2 B \in \mathbb{S}^n_+$$.

Hình dưới đây minh họa biên của hình nón nửa xác định dương $$\mathbb{S}^2_+$$ trong không gian tọa độ $$(x, y, z) \in \mathbb{R}^3$$. Một ma trận đối xứng $$2 \times 2$$ là nửa xác định dương khi và chỉ khi các phần tử trên đường chéo và định thức của nó đều không âm:

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

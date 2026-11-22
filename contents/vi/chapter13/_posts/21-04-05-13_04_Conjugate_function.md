---
layout: post
title: 13-04 Hàm liên hợp
chapter: '13'
order: 5
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Với một hàm cho trước $$f : \mathbb{R}^n \to \mathbb{R}$$, **hàm liên hợp** (conjugate function) $$f^{*} : \mathbb{R}^n \to \mathbb{R}$$ được định nghĩa như sau:

> $$f^{*}(y) = \max_x (y^Tx - f(x))$$

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter13/conjugate_function.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Minh họa hàm liên hợp [1]</figcaption>
</p>
</figure>

### Lưu ý

Hàm $$f^{*}$$ luôn là hàm lồi vì nó là cực đại theo từng điểm của một họ các hàm affine $$y \mapsto y^Tx - f(x)$$ (ngay cả khi $$f$$ không lồi). Về mặt hình học, $$f^{*}(y)$$ đo khoảng cách cực đại theo phương thẳng đứng giữa hàm tuyến tính $$y^Tx$$ và đồ thị của $$f(x)$$ (Boyd & Vandenberghe, trang 91).

Khi $$f$$ khả vi, phép lấy hàm liên hợp còn được gọi là **biến đổi Legendre**.

#### Tính chất

* **Bất đẳng thức Fenchel:** Với mọi $$x, y$$, ta có $$f(x) + f^{*}(y) \ge x^Ty$$.
> $$f(x) + f^{*}(y) \ge x^Ty \iff f^{*}(y) \ge x^Ty - f(x)$$
> $$f^{*}(y) = \max_z (z^Ty - f(z))$$

* Hàm liên hợp của hàm liên hợp được ký hiệu là $$f^{**}$$, và bất đẳng thức $$f^{**} \le f$$ luôn đúng.<br>
* Nếu $$f$$ là hàm đóng và lồi, thì $$f^{**} = f$$.<br>
* Nếu $$f$$ là hàm đóng và lồi, thì với mọi $$x, y$$ ta có các tương đương sau:<br>
> $$\begin{align}
> x \in \partial f^{*}(y) &\iff y \in \partial f(x) \\\
> &\iff f(x) + f^{*}(y) = x^Ty \\\
> \end{align}$$

* Nếu hàm tách biến theo dạng $$f(u,v) = f_1(u) + f_2(v)$$, thì $$f^{*}(w,z) = f_1^{*}(w) + f_2^{*}(z)$$.

#### Ví dụ

* **Hàm bậc hai:** Xét $$f(x) = \frac{1}{2}x^TQx$$, trong đó $$Q \succ 0$$.

Khi đó, hàm $$x \mapsto y^Tx - \frac{1}{2}x^TQx$$ là hàm lõm chặt theo $$x$$ và đạt cực đại duy nhất tại $$x = Q^{-1}y$$. Thay vào định nghĩa ta được $$f^{*}(y) = \frac{1}{2}y^TQ^{-1}y$$.

### Chứng minh
> $$\begin{align}
> f^{*}(y) & =  \max_x \left( y^Tx -\frac{1}{2}x^TQx \right) \\\
> & = -\min_x \left(\frac{1}{2}x^TQx- y^Tx \right), \quad x^{\star} = Q^{-1}y  \\\
> & = -\frac{1}{2}y^TQ^{-1}QQ^{-1}y + y^TQ^{-1}y \\\
> & = \frac{1}{2}y^TQ^{-1}y  \\\
> \end{align}$$

> Từ đó thu được bất đẳng thức Fenchel tương ứng với mọi $$x, y$$:
> $$\frac{1}{2} x^TQx + \frac{1}{2} y^TQ^{-1}y \ge x^Ty$$

* **Hàm chỉ thị:** Nếu $$f(x) = I_C(x)$$, thì hàm liên hợp của nó là:

> $$f^{*}(y) = I^{*}_C(y) = \max_{x \in C} y^Tx$$ (được gọi là **hàm hỗ trợ** của tập $$C$$).

* **Hàm chuẩn:** Nếu $$f(x) = \|x\|$$, thì hàm liên hợp của nó là:

> $$f^{*}(y) = I_{\{ z : \lVert z \rVert_{*} \le 1 \}}(y)$$, trong đó $$\lVert \cdot \rVert_{*}$$ là chuẩn đối ngẫu của $$\lVert \cdot \rVert$$.

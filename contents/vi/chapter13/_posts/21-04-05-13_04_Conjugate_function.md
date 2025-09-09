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

Với một hàm cho trước $$f : \mathbb{R}^n → \mathbb{R}$$, hàm liên hợp $$f^{∗} : \mathbb{R}^n → \mathbb{R}$$ được định nghĩa như sau:

> $$f^{∗}(y) = \max_x y^Tx−f(x)$$


<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter13/conjugate_function.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Illustration of conjugate function [1]</figcaption>
</p>


### [Lưu ý] 
$$f^{∗}$$ luôn là hàm lồi vì nó là cực đại điểm của các hàm lồi (affine) $$y^Tx - f(x)$$.
(Ở đây, $$f$$ không nhất thiết phải là hàm lồi.)
$$f^{∗}(y)$$ là khoảng cách cực đại giữa hàm tuyến tính $$y^Tx$$ và $$f(x)$$.
(Từ B & V trang 91)

Phép liên hợp cho $$f$$ khả vi được gọi là biến đổi Legendre.

#### Tính chất: 
• Bất đẳng thức Fenchel: với mọi $$x,y, f(x) + f^{∗}(y) ≥ x^Ty$$
> $$f(x) + f^{∗}(y) ≥ x^Ty \iff f^{*}(y) \ge x^Ty - f(x)$$
> $$ f^{*}(y) = \max_z z^Ty - f(x)$$

• Hàm liên hợp của hàm liên hợp là $$f^{∗∗}$$, do đó $$f^{∗∗} ≤ f$$ luôn đúng.<br>
• Nếu $$f$$ đóng và lồi, thì $$f^{∗∗} = f$$. <br>
• Nếu $$f$$ đóng và lồi, thì với mọi $$x,y$$, điều sau đây đúng:<br>
> $$\begin{align}
> x ∈ ∂f^{∗}(y) &\iff y ∈ ∂f(x) \\\
> &\iff f(x) + f^{∗}(y) = x^Ty \\\
> \end{align}$$

• Nếu $$f(u,v) = f_1(u) + f_2(v)$$, thì $$f^{∗}(w,z) = f_1^{∗}(w) + f_2^{∗}(z)$$ đúng. 



#### Ví dụ: 
• Hãy xem xét trường hợp $$f(x)$$ là một hàm bậc hai đơn giản như sau:
> $$f(x) = \frac{1}{2}x^TQx$$, trong đó $$Q \succ 0$$

Khi đó $$y^Tx− \frac{1}{2}x^TQx$$ là hàm lõm chặt theo $$y$$ và đạt cực đại tại $$x = Q^{−1}y$$. Tức là, $$f^{∗}(y) = \frac{1}{2}y^TQ^{−1}y$$. 



### [Chứng minh]
> $$\begin{align}
> f^{*}(y) & =  \max_x \left( y^Tx -\frac{1}{2}x^TQx \right) \\\
> & = -\min_x \left(\frac{1}{2}x^TQx- y^Tx \right), x^{\star} = Q^{-1}y  \\\
> & = -\frac{1}{2}y^TQ^{-1}QQ^{-1}y + y^TQ^{-1}y \\\
> & = \frac{1}{2}y^TQ^{-1}y  \\\
> \end{align}$$

> Bất đẳng thức Fenchel: với mọi $$x, y$$
> $$\frac{1}{2} x^TQx + \frac{1}{2} y^TQ^{-1}y \ge x^Ty$$

• Hàm chỉ thị: Nếu $$f(x) = I_C(x)$$, thì hàm liên hợp của nó như sau:

> $$f^{∗}(y) = I^{∗}_C(y) = \max_{x ∈ C} y^Tx$$ được gọi là **hàm hỗ trợ** của $$C$$

• Chuẩn: Nếu $$f(x) = \|x\|$$, thì hàm liên hợp của nó như sau:
> $$f^{∗}(y) = I_{\\{ z : \rVert z \rVert_{∗} ≤ 1 \\}}(y)$$ trong đó $$\rVert · \rVert_{∗}$$ là chuẩn đối ngẫu của $$\rVert · \rVert$$ 


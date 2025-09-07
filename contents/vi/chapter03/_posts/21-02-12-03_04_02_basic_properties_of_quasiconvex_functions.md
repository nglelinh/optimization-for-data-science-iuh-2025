---
layout: post
title: 03-04-02 Các tính chất cơ bản của hàm giả lồi
chapter: '03'
order: 10
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Phần này đề cập các tính chất cơ bản của hàm giả lồi, bao gồm mối quan hệ của chúng với hàm lồi và hành vi của chúng dưới các phép toán khác nhau.

## Bất đẳng thức Jensen biến đổi
Các hàm giả lồi có thể được định nghĩa thông qua bất đẳng thức Jensen như sau:
>$$f(\theta x + (1 - \theta)y) \leq \max\{f(x), f(y)\}$$ với mọi $$x, y \in \text{dom}f, 0 \leq \theta \leq 1$$

Hình dưới đây cho thấy rằng nếu hàm $$f$$ là giả lồi, thì giá trị của $$f$$ dọc theo đoạn thẳng giữa hai điểm không vượt quá giá trị lớn nhất của $$f$$ tại các điểm cuối.
<br><br>

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.10_quasiconvex_function_on_R_4uChnEm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1]</figcaption>
</p>
</figure>
**hàm giả lồi trên $$\mathbb{R}$$. Các giá trị của $$f$$ giữa $$x$$ và $$y$$ nhỏ hơn $$\max\{f(x), f(y)\}$$.**

<br>

## Hàm giả lồi trên $$\mathbb{R}$$
Một hàm liên tục $$f : \mathbb{R} \mapsto \mathbb{R}$$ là giả lồi khi và chỉ khi nó thỏa mãn ít nhất một trong các điều kiện sau:

• $$f$$ không giảm
• $$f$$ không tăng  
• Tồn tại một điểm $$c \in \text{dom} f$$ sao cho $$f$$ không tăng trên $$\{t \in \text{dom}f \mid t \leq c\}$$ và không giảm trên $$\{t \in \text{dom}f \mid t \geq c\}$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.11_quasiconvex_function_on_R_2_PPQpNiU.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2]</figcaption>
</p>
</figure>
**hàm giả lồi trên $$\mathbb{R}$$. Nó không tăng với $$t \leq c$$ trong đó $$t \in \text{dom} f$$, và không giảm với $$t \geq c$$ trong đó $$t \in \text{dom} f$$.**

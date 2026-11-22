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

Phần này trình bày các tính chất cơ bản của hàm giả lồi, bao gồm bất đẳng thức Jensen biến đổi và đặc trưng của hàm giả lồi liên tục một biến.

## Bất đẳng thức Jensen biến đổi

Hàm $$f$$ là giả lồi khi và chỉ khi miền xác định $$\text{dom}f$$ lồi và thỏa mãn bất đẳng thức Jensen biến đổi sau:
>$$f(\theta x + (1 - \theta)y) \leq \max\{f(x), f(y)\}$$ với mọi $$x, y \in \text{dom}f$$, $$0 \leq \theta \leq 1$$

Nói cách khác, dọc theo đoạn thẳng nối hai điểm $$x$$ và $$y$$, giá trị của hàm giả lồi $$f$$ không bao giờ vượt quá giá trị lớn hơn trong hai giá trị $$f(x)$$ và $$f(y)$$.
<br><br>

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.10_quasiconvex_function_on_R_4uChnEm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1]</figcaption>
</p>
</figure>
**Hàm giả lồi trên $$\mathbb{R}$$: giá trị của $$f$$ giữa $$x$$ và $$y$$ luôn nhỏ hơn hoặc bằng $$\max\{f(x), f(y)\}$$.**

<br>

## Hàm giả lồi trên $$\mathbb{R}$$

Một hàm liên tục $$f : \mathbb{R} \mapsto \mathbb{R}$$ là giả lồi khi và chỉ khi nó thỏa mãn ít nhất một trong ba điều kiện sau:

* $$f$$ không giảm trên $$\text{dom}f$$.
* $$f$$ không tăng trên $$\text{dom}f$$.
* Tồn tại một điểm $$c \in \text{dom} f$$ sao cho $$f$$ không tăng trên $$\{t \in \text{dom}f \mid t \leq c\}$$ và không giảm trên $$\{t \in \text{dom}f \mid t \geq c\}$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.11_quasiconvex_function_on_R_2_PPQpNiU.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2]</figcaption>
</p>
</figure>
**Hàm giả lồi trên $$\mathbb{R}$$: không tăng với $$t \leq c$$ và không giảm với $$t \geq c$$ ($$t \in \text{dom} f$$).**

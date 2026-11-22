---
layout: post
title: 03-04-04 Các phép toán bảo toàn tính giả lồi
chapter: '03'
order: 12
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Phần này trình bày các phép toán bảo toàn tính giả lồi của hàm số.

## Maximum trọng số không âm

Nếu $$f_1, \dots, f_m$$ là các hàm giả lồi và $$w_i \geq 0$$, thì maximum có trọng số không âm của chúng cũng là hàm giả lồi:
>$$f = \max\{w_1f_1, ... ,w_mf_m\}$$ với $$w_i \geq 0$$ là giả lồi

Tổng quát hơn cho họ vô hạn các hàm:
>$$f(x) = \sup_{y \in C}(w(y)g(x,y))$$ với $$w(y) \geq 0$$,
>trong đó $$g(x,y)$$ là hàm giả lồi theo $$x$$ với mọi $$y \in C$$.

<br>

## Hợp thành

Nếu $$g : \mathbb{R}^n \mapsto \mathbb{R}$$ là hàm giả lồi và $$h : \mathbb{R} \mapsto \mathbb{R}$$ không giảm, thì hàm hợp thành $$f = h \circ g$$ cũng là hàm giả lồi:
> $$f = h \circ g$$ là giả lồi nếu $$h$$ không giảm và $$g$$ là giả lồi.

Hợp thành một hàm giả lồi với biến đổi affine hoặc biến đổi tuyến tính-phân thức cũng bảo toàn tính giả lồi: nếu $$f$$ là hàm giả lồi thì $$g(x) = f(Ax + b)$$ giả lồi, và $$\tilde{g}(x) = f((Ax + b)/(c^Tx + d))$$ giả lồi trên miền $$\{x \mid c^Tx + d > 0,\; (Ax + b)/(c^Tx + d) \in \text{dom}f\}$$.

<br>

## Cực tiểu hóa từng phần

Nếu $$f(x, y)$$ là hàm giả lồi đồng thời theo $$(x, y)$$ và $$C$$ là một tập lồi, thì phép lấy infimum theo $$y \in C$$ bảo toàn tính giả lồi:
> $$g(x) = \inf_{y \in C} f(x,y)$$ là giả lồi nếu $$f$$ giả lồi theo $$(x,y)$$ và $$C$$ là một tập lồi.

<br>

## Biểu diễn thông qua họ các hàm lồi

Các tập mức dưới của một hàm giả lồi $$f$$ có thể được biểu diễn bằng các bất đẳng thức liên quan đến một họ hàm lồi $$\phi_t : \mathbb{R}^n \mapsto \mathbb{R}$$ (tham số hóa bởi $$t \in \mathbb{R}$$) sao cho:
>$$f(x) \leq t \Longleftrightarrow \phi_t(x) \leq 0$$

Nói cách khác, tập mức dưới mức $$t$$ của hàm giả lồi $$f$$ trùng với tập mức dưới mức 0 của hàm lồi $$\phi_t$$. Hơn nữa, với mọi $$x \in \mathbb{R}^n$$ và mọi $$s \geq t$$, họ hàm này thỏa mãn tính lồng nhau:
>$$\phi_t(x) \leq 0 \Rightarrow \phi_s(x) \leq 0 \text{ với } s \geq t$$

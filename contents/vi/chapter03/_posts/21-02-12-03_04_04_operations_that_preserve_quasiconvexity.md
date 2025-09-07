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

Phần này thảo luận các phép toán bảo toàn tính giả lồi của các hàm.

## Maximum trọng số không âm

Khi $$f$$ là một hàm giả lồi, maximum trọng số không âm $$f$$ là giả lồi.
>$$f = \max\{w_1f_1, ... ,w_mf_m\}$$ với $$w_i \geq 0$$ là giả lồi

Khái niệm này có thể được mở rộng như sau:
>$$f(x) = \sup_{y \in C}(w(y)g(x,y))$$ với $$w(y) \geq 0$$, 
>trong đó $$g(x,y)$$ là giả lồi theo $$x$$ với mọi $$y$$.

<br>

## Hợp thành

Nếu $$g : \mathbb{R}^n \mapsto \mathbb{R}$$ là giả lồi và $$h : \mathbb{R} \mapsto \mathbb{R}$$ không giảm, thì hợp thành $$f$$ thỏa mãn tính giả lồi.
> $$f = h \circ g$$ là giả lồi nếu $$h$$ không giảm và $$g$$ là giả lồi.
 
Hợp thành một hàm giả lồi với các biến đổi affine hoặc tuyến tính-phân thức cho ra một hàm giả lồi.
Nếu $$f$$ là giả lồi, thì $$g(x) = f(Ax + b)$$ cũng là giả lồi, và $$\tilde{g}(x) = f((Ax + b)/(c^Tx + d))$$ cũng là giả lồi trên tập $$\{x \mid c^Tx + d > 0, (Ax + b)/(c^Tx + d) \in \text{dom}f\}$$.

<br>

## Cực tiểu hóa

Nếu $$f(x, y)$$ thỏa mãn tính giả lồi và $$C$$ là một tập lồi, thì điều kiện sau đây đúng:
> $$g(x) = \inf_{y \in C} f(x,y)$$ là giả lồi nếu $$f$$ là giả lồi theo $$(x,y)$$ và $$C$$ là một tập lồi.

<br>

## Biểu diễn thông qua họ các hàm lồi

Các tập mức dưới của một hàm giả lồi $$f$$ có thể được biểu diễn bằng các bất đẳng thức của các hàm lồi. Một họ các hàm lồi là $$\phi_t : \mathbb{R}^n \mapsto \mathbb{R}$$ với $$t \in \mathbb{R}$$, được định nghĩa như sau:
>$$f(x) \leq t \Longleftrightarrow \phi_t(x) \leq 0$$

Tức là, tập mức dưới $$t$$ của hàm giả lồi $$f(x)$$ trở thành tập mức dưới 0 của hàm lồi $$\phi_t$$. Ở đây, $$t$$ biểu thị chỉ số của hàm lồi $$\phi$$. Với mọi $$x \in \mathbb{R}^n$$, điều sau được thỏa mãn:
>$$\phi_t(x) \leq 0 \Rightarrow \phi_s(x) \leq 0 \text{ với } s \geq t$$


---
layout: post
title: 03-06 Tính lồi đối với bất đẳng thức tổng quát
chapter: '03'
order: 14
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Phần này mở rộng khái niệm tính đơn điệu và tính lồi từ các hàm giá trị thực thông thường sang các hàm giá trị vector thông qua bất đẳng thức tổng quát.

Trong các không gian nhiều chiều, ta dùng hình nón thích hợp để định nghĩa bất đẳng thức tổng quát, mở rộng quan hệ thứ tự quen thuộc trên $$\mathbb{R}$$ (xem bài [02-01-04]({% multilang_post_url contents/chapter02/21-02-08-02_01_04_Convex_cone %})).

## Tính đơn điệu đối với bất đẳng thức tổng quát

Giả sử $$K \subseteq \mathbb{R}^n$$ là một **hình nón thích hợp** sinh ra bất đẳng thức tổng quát $$\preceq_K$$, tức là một hình nón lồi thỏa mãn:

* $$K$$ là tập đóng (chứa biên của nó).
* $$K$$ là hình nón đặc (có phần trong khác rỗng).
* $$K$$ là hình nón nhọn (không chứa đường thẳng nào).

Hàm $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ được gọi là **không giảm theo $$K$$** nếu:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ không giảm theo $$K$$ nếu $$x \preceq_K y \Rightarrow f(x) \leq f(y)$$

Tương tự, $$f$$ được gọi là **tăng theo $$K$$** nếu:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ tăng theo $$K$$ nếu $$x \preceq_K y, x \neq y \Rightarrow f(x) < f(y)$$

### Điều kiện gradient cho tính đơn điệu

Với hàm khả vi một biến $$f : \mathbb{R} \mapsto \mathbb{R}$$ trên một khoảng, $$f$$ không giảm khi và chỉ khi $$f'(x) \geq 0$$ với mọi $$x \in \text{dom}f$$, và nếu $$f'(x) > 0$$ với mọi $$x \in \text{dom}f$$ thì $$f$$ tăng. Khái niệm này mở rộng sang bất đẳng thức tổng quát như sau:

Khi $$\text{dom}f$$ lồi, một hàm khả vi $$f$$ không giảm theo $$K$$ khi và chỉ khi gradient $$\nabla f(x)$$ không âm theo bất đẳng thức tổng quát đối ngẫu:
> Hàm khả vi $$f$$ không giảm theo $$K$$ $$\Longleftrightarrow$$ $$\nabla f(x) \succeq_{K^*} 0$$ với mọi $$x \in \text{dom}f$$

Tương tự, ta có điều kiện đủ cho tính tăng theo $$K$$ (như trường hợp một biến, chiều ngược lại không nhất thiết đúng):
> $$\nabla f(x) \succ_{K^*} 0$$ với mọi $$x \in \text{dom}f$$ $$\Longrightarrow$$ $$f$$ tăng theo $$K$$.

## Tính lồi đối với bất đẳng thức tổng quát

Cho $$K \subseteq \mathbb{R}^m$$ là hình nón thích hợp gắn với bất đẳng thức tổng quát $$\preceq_K$$. Hàm $$f : \mathbb{R}^n \mapsto \mathbb{R}^m$$ được gọi là **lồi theo $$K$$** nếu miền xác định $$\text{dom}f$$ lồi và với mọi $$x, y \in \text{dom}f$$ cùng mọi $$0 \leq \theta \leq 1$$:
> $$f(\theta x + (1 - \theta) y) \preceq_K \theta f(x) + (1 - \theta) f(y)$$

Hàm $$f$$ được gọi là **lồi chặt theo $$K$$** nếu với mọi $$x, y \in \text{dom}f$$ ($$x \neq y$$) và $$0 < \theta < 1$$:
> $$f(\theta x + (1 - \theta) y) \prec_K \theta f(x) + (1 - \theta) f(y)$$

Khi $$m = 1$$ và $$K = \mathbb{R}_+$$, định nghĩa này trở về đúng định nghĩa hàm lồi thông thường.

### Đặc trưng đối ngẫu của tính lồi theo $$K$$

Theo tính chất của bất đẳng thức tổng quát đối ngẫu:
* $$f$$ lồi theo $$K$$ khi và chỉ khi hàm giá trị thực $$w^T f$$ lồi với mọi $$w \succeq_{K^*} 0$$.
* $$f$$ lồi chặt theo $$K$$ khi và chỉ khi hàm giá trị thực $$w^T f$$ lồi chặt với mọi $$w \succeq_{K^*} 0, w \neq 0$$.

<br>

### Hàm lồi theo $$K$$ khả vi

Một hàm khả vi $$f$$ có miền xác định lồi là lồi theo $$K$$ khi và chỉ khi:
> $$f(y) \succeq_K f(x) + Df(x)(y - x)$$ với mọi $$x, y \in \text{dom}f$$

trong đó $$Df(x) \in \mathbb{R}^{m \times n}$$ là ma trận đạo hàm (Jacobian) của $$f$$ tại $$x$$.

Tương tự, $$f$$ lồi chặt theo $$K$$ khi và chỉ khi:
> $$f(y) \succ_K f(x) + Df(x)(y - x)$$ với mọi $$x, y \in \text{dom}f$$, $$x \neq y$$

### Định lý hợp thành

Nhiều quy tắc hợp thành cũng mở rộng cho tính lồi theo $$K$$. Chẳng hạn, nếu $$g : \mathbb{R}^n \mapsto \mathbb{R}^p$$ lồi theo $$K$$, $$h : \mathbb{R}^p \rightarrow \mathbb{R}$$ lồi và phần mở rộng giá trị thực mở rộng $$\widetilde{h}$$ không giảm theo $$K$$, thì hàm hợp $$h \circ g$$ là hàm lồi. Kết quả này tổng quát hóa quy tắc hợp thành của hàm lồi với hàm lồi không giảm. (Điều kiện $$\widetilde{h}$$ không giảm theo $$K$$ đòi hỏi $$h$$ không giảm theo $$K$$ trên $$\text{dom}h$$ và $$\text{dom}h - K = \text{dom}h$$.)

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

Phần này thảo luận tính lồi đối với bất đẳng thức tổng quát, mở rộng khái niệm tính lồi vượt ra ngoài các hàm giá trị thực chuẩn.

Trong các không gian khác với $$\mathbb{R}$$, chúng ta sử dụng định nghĩa của nón cho các biểu thức bất đẳng thức tổng quát mở rộng khái niệm thứ tự thường được sử dụng trong không gian $$\mathbb{R}$$ (xem [02-01-04]({% multilang_post_url contents/chapter02/21-02-08-02_01_04_Convex_cone %})). Trong phần này, chúng ta xem xét các khái niệm về tính đơn điệu và tính lồi mở rộng ra ngoài không gian $$\mathbb{R}$$ sử dụng khái niệm nón.

## Tính đơn điệu đối với bất đẳng thức tổng quát

Giả sử $$K \subseteq \mathbb{R}^n$$ là một nón thích hợp được biểu thị bởi $$\preceq_K$$. Một nón lồi $$K \subseteq \mathbb{R}^n$$ là một **nón thích hợp** nếu nó thỏa mãn các điều kiện sau:

• $$K$$ đóng (chứa biên của nó)
• $$K$$ rắn (có nội tâm khác rỗng)
• $$K$$ nhọn (không chứa đường thẳng)

Chúng ta định nghĩa **không giảm theo $$K$$** như sau:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ là không giảm theo $$K$$ nếu $$x \preceq_K y \Rightarrow f(x) \leq f(y)$$

Cũng vậy, khi điều kiện sau được thỏa mãn, chúng ta nói nó là **tăng theo $$K$$**:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ là tăng theo $$K$$ nếu $$x \preceq_K y, x \neq y \Rightarrow f(x) < f(y)$$


### Điều kiện gradient cho tính đơn điệu

Với một hàm khả vi $$f : \mathbb{R} \mapsto \mathbb{R}$$ không giảm trên miền lồi (tức là khoảng) có nghĩa là $$f'(x) \geq 0$$ với mọi $$x \in \text{dom}f$$, và nếu $$f'(x) > 0$$ với mọi $$x \in \text{dom}f$$, thì nó là tăng. Tương tự, tính đơn điệu có thể được biểu thị như một khái niệm mở rộng trong bất đẳng thức tổng quát.

Khi miền là lồi, một hàm khả vi $$f$$ không giảm theo $$K$$ có nghĩa là thỏa mãn phương trình sau. Lưu ý rằng khác với vô hướng đơn giản, gradient $$\nabla f(x)$$ phải không âm trong bất đẳng thức đối ngẫu.
> Một hàm khả vi $$f$$ không giảm theo $$K$$ $$\Longleftrightarrow$$ $$\nabla f(x) \succeq_{K^*} 0$$ với mọi $$x \in \text{dom}f$$

Nếu điều kiện sau được thỏa mãn, $$f$$ được gọi là **tăng theo $$K$$**. Như với vô hướng, điều ngược lại không đúng.
> $$\nabla f(x) \succ_{K^*} 0$$ với mọi $$x \in \text{dom}f$$ $$\Rightarrow$$ $$f$$ tăng theo $$K$$.


### Tính lồi đối với bất đẳng thức tổng quát

Gọi $$K \subseteq \mathbb{R}^m$$ là một nón thích hợp liên kết với bất đẳng thức tổng quát $$\preceq_K$$.
Khi đó, nếu $$f : \mathbb{R}^n \mapsto \mathbb{R}^m$$ được gọi là **lồi theo $$K$$** với mọi $$x, y$$ và $$0 \leq \theta \leq 1$$, bất đẳng thức sau đây đúng:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}^m$$ là lồi theo $$K$$ $$\Rightarrow$$ $$f(\theta x + (1 - \theta) y) \preceq_K \theta f(x) + (1 - \theta) f(y)$$ với $$0 < \theta < 1$$ cho mọi $$x, y$$.

Cũng vậy, điều kiện cho **lồi chặt theo $$K$$** là như sau:
> $$f(\theta x + (1 - \theta) y) \prec_K \theta f(x) + (1 - \theta) f(y)$$ với mọi $$x \neq y$$ và $$0 < \theta < 1$$.

Khi $$m = 1$$ và $$K = \mathbb{R}_+$$, điều này trở thành bất đẳng thức thỏa mãn tính lồi tổng quát mà chúng ta đã thảo luận trước đó.

### Đặc trưng đối ngẫu của tính lồi theo $$K$$

$$f$$ là lồi theo $$K$$ có nghĩa là hàm (giá trị thực) $$w^T f$$ là lồi với mọi $$w \succeq_{K^*} 0$$. $$f$$ là lồi chặt theo $$K$$ có nghĩa là hàm (giá trị thực) $$w^T f$$ là lồi chặt với mọi $$w \succeq_{K^*} 0$$. Điều này theo sau từ định nghĩa và tính chất của bất đẳng thức đối ngẫu.

<br>
### Các hàm lồi theo $$K$$ khả vi

Nếu một hàm khả vi $$f$$ là lồi theo $$K$$ và miền hàm là lồi, thì phương trình sau đây đúng:
> $$f(y) \succeq_K f(x) + Df(x)(y - x)$$ với mọi $$x, y \in \text{dom}f$$

Ở đây, $$Df(x) \in \mathbb{R}^{m \times n}$$ là đạo hàm hoặc ma trận Jacobian của $$f$$ tại điểm $$x$$.

Nếu $$f$$ là lồi chặt theo $$K$$ và miền hàm là lồi, thì phương trình sau đây đúng:
> $$f(y) \succ_K f(x) + Df(x)(y - x)$$ với mọi $$x, y \in \text{dom}f$$, $$x \neq y$$


### Định lý hợp thành

Nhiều kết quả từ hợp thành có thể được tổng quát hóa cho tính lồi theo $$K$$.
Ví dụ, nếu $$g : \mathbb{R}^n \mapsto \mathbb{R}^p$$ là lồi theo $$K$$, $$h : \mathbb{R}^p \rightarrow \mathbb{R}$$ là lồi, và phần mở rộng giá trị mở rộng $$\widetilde{h}$$ của $$h$$ là không giảm theo $$K$$, thì $$h \circ g$$ là lồi. Điều này tổng quát hóa sự thật rằng hợp thành của một hàm lồi với một hàm lồi không giảm là lồi.
(Điều kiện $$\widetilde{h}$$ không giảm theo $$K$$ có nghĩa là $$\text{dom}h - K = \text{dom}h$$.)

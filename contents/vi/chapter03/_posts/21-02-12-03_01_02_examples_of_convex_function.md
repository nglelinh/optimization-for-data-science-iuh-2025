---
layout: post
title: 03-01-02 Ví dụ về hàm lồi
chapter: '03'
order: 4
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Phần này xem xét các ví dỡ điển hình của hàm lồi, bao gồm:

* Hàm mũ
* Hàm lũy thừa
* Hàm affine
* Hàm bậc hai
* Hàm mất mát bình phương nhỏ nhất
* Chuẩn
* Hàm chỉ thị
* Hàm hỗ trợ
* Hàm max

## Hàm một biến
* Hàm mũ:
Với bất kỳ số thực $$a$$, $$e^{ax}$$ là hàm lồi.
> $$e^{ax}$$ là hàm lồi với mọi $$a \in \mathbb{R}$$

* Hàm lũy thừa:
Với $$x, a \in \mathbb{R}_{+}$$, tùy thuộc vào khoảng giá trị của $$a$$, $$x^a$$ có thể là hàm lồi hoặc lõm.
> $$x^{a}$$ là hàm lồi trên $$\mathbb{R}_{+}$$ với mọi $$a \geq 1$$ hoặc $$a \leq 0$$
> $$x^{a}$$ là hàm lõm trên $$\mathbb{R}_{+}$$ với mọi $$0 \leq a \leq 1$$

## Hàm affine
Như đã đề cập trong [03-01-01]({% multilang_post_url contents/chapter03/21-02-12-03_01_01_convex_functions_definition %}), tất cả các hàm affine đều vừa lồi vừa lõm.

* Trên $$\mathbb{R}$$ và $$\mathbb{R}^n$$:
> $$a^Tx + b$$ vừa lồi vừa lõm

* Trên $$\mathbb{R}^{m \times n}$$:
> $$\text{tr}(A^TX) + b = \sum_{i=1}^m\sum_{j=1}^n A_{ij}X_{ij} + b$$ vừa lồi vừa lõm

## Hàm bậc hai
Xem xét hàm bậc hai $$f(x)=\frac{1}{2}x^TPx+q^Tx+r$$, trong đó $$\nabla f(x)= Px+q$$ và $$\nabla^2f(x) = P$$. Nếu $$P$$ là ma trận nửa xác định dương, thì $$f(x)$$ là hàm lồi.
Với $$P \succeq 0$$:
> $$f(x)=\frac{1}{2}x^TPx+q^Tx+r$$ là hàm lồi với $$P \in \mathbb{S}^n, q \in \mathbb{R}^n, r \in \mathbb{R}$$

**H: Tại sao $$f(x)$$ lồi nếu $$P$$ là ma trận nửa xác định dương?**
Đáp: Trong hàm bậc hai, đạo hàm bậc hai là ma trận Hessian. Ma trận Hessian xác định độ cong của hàm, và nếu nó là nửa xác định dương, hàm sẽ cong lên trên. (Tức là, độ cong theo hướng của các vector riêng của Hessian là không âm.) Do đó, nếu đạo hàm bậc hai là nửa xác định dương, hàm sẽ lồi.

## Hàm mất mát bình phương nhỏ nhất
Với bất kỳ ma trận $$A$$, $$A^TA$$ luôn là ma trận nửa xác định dương, có nghĩa là $$\left \| Ax - b \right \|_{2}^{2}$$ luôn là hàm lồi.

> $$f(x) = \| Ax - b \|_{2}^{2}$$ là hàm lồi với mọi $$A$$

## Chuẩn
Tất cả các chuẩn trên $$\mathbb{R}^n$$ đều là hàm lồi.
Gọi $$f:\mathbb{R}^n \mapsto \mathbb{R}$$ là một chuẩn. Theo định nghĩa,
>$$
\begin{aligned}
f(\theta x+(1−\theta)y) \le \theta f(x)+(1−\theta)f(y), \text{  với } 0 \le \theta \le 1, \text{ cho mọi } x,y \in \text{dom} f,
\end{aligned}
$$
>$$
\begin{aligned}
\|x\|_{p} = \left(\sum_{i=1}^{n} x_i^p\right)^{1/p} \text{ với } p \geq 1, \|x\| = \max_{i=1,.., n} |x_i|\\
\end{aligned} 
$$

## Hàm chỉ thị
Với một tập $$C$$ cho trước, nếu hàm chỉ thị được định nghĩa là vô cực ($$\infty$$) cho các phần tử không thuộc $$C$$ và bằng không cho các phần tử thuộc $$C$$, thì hàm chỉ thị là hàm lồi.

Nói cách khác, bằng cách định nghĩa hàm có giá trị vô cực bên ngoài tập $$C$$ và bằng không bên trong nó, tính chất lồi được bảo toàn.

>$$I_{C} (x) =
\begin{cases}
0, & x \in C\\
\infty, & x \notin C\\
\end{cases}
$$

## Hàm hỗ trợ
Xem xét một tập $$C$$. Bất kể $$C$$ có lồi hay không, hàm hỗ trợ của $$C$$ đều là hàm lồi.
> $$I_{C}^{*} (x)$$ = $$\max_{y\in C} x^Ty$$ là hàm lồi

Để tìm hiểu thêm về định nghĩa hàm hỗ trợ, tham khảo [định nghĩa trên Wikipedia](https://en.wikipedia.org/wiki/Support_function).

## Hàm max
Hàm max của một tập hữu hạn các hàm lồi là hàm lồi.
Nói cách khác, đường bao trên được hình thành bằng cách nối các giá trị lớn nhất của một tập các hàm lồi là hàm lồi.
> $$f(x) = \max \{x_1,..., x_n\}$$ là hàm lồi

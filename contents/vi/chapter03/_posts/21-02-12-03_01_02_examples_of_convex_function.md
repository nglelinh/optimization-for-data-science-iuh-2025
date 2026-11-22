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

Phần này điểm qua các ví dụ điển hình về hàm lồi, gồm:

* Hàm mũ
* Hàm lũy thừa
* Hàm affine
* Hàm bậc hai
* Hàm mất mát bình phương tối thiểu
* Chuẩn
* Hàm chỉ thị
* Hàm hỗ trợ
* Hàm max

## Hàm một biến

* **Hàm mũ:** Với mọi số thực $$a$$, hàm $$e^{ax}$$ là hàm lồi trên $$\mathbb{R}$$.
> $$e^{ax}$$ là hàm lồi với mọi $$a \in \mathbb{R}$$

* **Hàm lũy thừa:** Với $$x \in \mathbb{R}_{++}$$ (tức $$x > 0$$) và $$a \in \mathbb{R}$$, tính lồi hay lõm của $$x^a$$ phụ thuộc vào giá trị của số mũ $$a$$:
> $$x^{a}$$ là hàm lồi trên $$\mathbb{R}_{++}$$ với mọi $$a \geq 1$$ hoặc $$a \leq 0$$
> $$x^{a}$$ là hàm lõm trên $$\mathbb{R}_{++}$$ với mọi $$0 \leq a \leq 1$$

## Hàm affine

Như đã nêu trong bài [03-01-01]({% multilang_post_url contents/chapter03/21-02-12-03_01_01_convex_functions_definition %}), mọi hàm affine đều vừa lồi vừa lõm.

* Trên $$\mathbb{R}$$ và $$\mathbb{R}^n$$:
> $$a^Tx + b$$ vừa lồi vừa lõm

* Trên $$\mathbb{R}^{m \times n}$$:
> $$\text{tr}(A^TX) + b = \sum_{i=1}^m\sum_{j=1}^n A_{ij}X_{ij} + b$$ vừa lồi vừa lõm

## Hàm bậc hai

Xét hàm bậc hai $$f(x)=\frac{1}{2}x^TPx+q^Tx+r$$, có gradient $$\nabla f(x)= Px+q$$ và ma trận Hessian $$\nabla^2f(x) = P$$. Nếu $$P$$ là ma trận nửa xác định dương ($$P \succeq 0$$) thì $$f(x)$$ là hàm lồi:
> $$f(x)=\frac{1}{2}x^TPx+q^Tx+r$$ là hàm lồi với $$P \in \mathbb{S}^n_+$$, $$q \in \mathbb{R}^n$$, $$r \in \mathbb{R}$$

**Hỏi: Tại sao $$f(x)$$ lồi khi $$P$$ là ma trận nửa xác định dương?**
**Đáp:** Đối với hàm bậc hai, ma trận Hessian $$\nabla^2 f(x) = P$$ phản ánh độ cong của hàm theo mọi phương. Khi $$P \succeq 0$$, độ cong theo mọi hướng đều không âm (đồ thị luôn hướng bề lõm lên trên), nên hàm là hàm lồi.

## Hàm mất mát bình phương tối thiểu

Với mọi ma trận $$A$$, ma trận $$A^TA$$ luôn nửa xác định dương, do đó hàm $$\left \| Ax - b \right \|_{2}^{2}$$ luôn là hàm lồi:

> $$f(x) = \| Ax - b \|_{2}^{2}$$ là hàm lồi với mọi $$A$$

## Chuẩn

Mọi chuẩn trên $$\mathbb{R}^n$$ đều là hàm lồi. Nếu $$f:\mathbb{R}^n \mapsto \mathbb{R}$$ là một chuẩn thì theo bất đẳng thức tam giác và tính thuần nhất bậc một, ta có:
>$$
\begin{aligned}
f(\theta x+(1-\theta)y) \le \theta f(x)+(1-\theta)f(y), \text{ với } 0 \le \theta \le 1, \text{ cho mọi } x,y \in \text{dom} f,
\end{aligned}
$$
>$$
\begin{aligned}
\|x\|_{p} = \left(\sum_{i=1}^{n} |x_i|^p\right)^{1/p} \text{ với } p \geq 1, \quad \|x\|_\infty = \max_{i=1,.., n} |x_i|\\
\end{aligned} 
$$

## Hàm chỉ thị

Với một **tập lồi** $$C$$ cho trước, hàm chỉ thị $$I_C$$ nhận giá trị $$0$$ với các điểm thuộc $$C$$ và $$+\infty$$ với các điểm ngoài $$C$$ là một hàm lồi:

>$$I_{C} (x) =
\begin{cases}
0, & x \in C\\
\infty, & x \notin C\\
\end{cases}
$$

## Hàm hỗ trợ

Xét một tập $$C$$ bất kỳ. Dù $$C$$ có lồi hay không, hàm hỗ trợ của $$C$$ luôn là hàm lồi:
> $$I_{C}^{*} (x) = \sup_{y\in C} x^Ty$$ là hàm lồi

Xem thêm [định nghĩa hàm hỗ trợ trên Wikipedia](https://en.wikipedia.org/wiki/Support_function).

## Hàm max

Giá trị lớn nhất theo từng điểm của một họ hữu hạn các hàm lồi là một hàm lồi; về mặt hình học, bao trên của các đồ thị hàm lồi vẫn là một hàm lồi. Đặc biệt:
> $$f(x) = \max \{x_1,..., x_n\}$$ là hàm lồi

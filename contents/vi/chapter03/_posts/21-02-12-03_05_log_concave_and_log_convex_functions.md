---
layout: post
title: 03-05 Hàm log-lõm và log-lồi
chapter: '03'
order: 13
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Phần này giới thiệu các hàm log-lõm và log-lồi, quan trọng trong xác suất, thống kê và tối ưu hóa.

## Định nghĩa

Các định nghĩa của hàm log-lõm và log-lồi như sau.

### $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ là Lõm logarithm hoặc log-lõm
Nếu $$f(x) > 0$$ với mọi $$x \in \text{dom}f$$ và $$\log f$$ là lõm, thì $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ được gọi là lõm logarithm hoặc log-lõm.
> $$f$$ là log-lõm với $$f(x) > 0$$ cho mọi $$x \in \text{dom}f$$ : <br>
>$$f(\theta x + (1 - \theta) y) \geq f(x)^\theta f(y)^{1-\theta}$$ với $$0 \leq \theta \leq 1$$.

### $$f : \mathbb{R}^n \mapsto \mathbb{R} $$ là Lồi logarithm hoặc log-lồi
Nếu $$f(x) > 0$$ với mọi $$x \in \text{dom}f$$ và $$\log f$$ là lồi, thì $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ được gọi là lồi logarithm hoặc log-lồi. Do đó, nếu $$f$$ là log-lồi, thì $$1/f$$ là log-lõm.
> $$f$$ là log-lồi với $$f(x) > 0$$ cho mọi $$x \in \text{dom}f$$ $$\Longleftrightarrow \frac{1}{f}$$ là log-lõm.

Đôi khi tiện lợi khi cho phép giá trị $$f$$ bằng 0, trong trường hợp này $$\log f(x) = -\infty$$. Trong các trường hợp như vậy, nếu hàm giá trị mở rộng $$\log f$$ là lõm, thì $$f$$ có thể được gọi là log-lõm.

**Các hàm log-lồi và log-lõm lần lượt là giả lồi và giả lõm, vì logarithm là hàm đơn điệu tăng.**

## Ví dụ
### Hàm affine
Nếu $$f$$ được định nghĩa như sau, thì nó là log-lõm.
>$$f(x) = a^Tx + b$$ trên $$\{x \mid a^Tx + b > 0\}$$

### Lũy thừa
$$f(x) = x^a$$ trên $$\mathbb{R}_{++}$$ là log-lồi khi $$a \leq 0$$ và log-lõm khi $$a \geq 0$$.

### Hàm mũ
$$f(x) = e^{ax}$$ vừa là log-lồi vừa là log-lõm.

### Hàm phân phối tích lũy của mật độ Gauss
$$\Phi(x) = \frac{1}{ \sqrt{2 \pi } }  \int_ {-\infty} ^x e^{-u^2/2} du $$ là log-lõm.

### Hàm Gamma
$$\Gamma (x) = \int_0^\infty u^{x-1}e^{-u} du $$
là log-lồi với $$x \geq 1$$.

### Định thức
$$\det X$$ là log-lõm trên $$S^n_{++}$$.

### Định thức chia vết
$$\det X / \text{tr} X$$ là log-lõm trên $$S^n_{++}$$.

<br>
## Tính chất

### Các hàm log-lồi / lõm khả vi hai lần
Nếu $$f$$ khả vi hai lần và $$\text{dom} f$$ lồi, thì phương trình sau đây đúng:<br>
>$$\nabla ^2 \log f(x) = \frac{1}{f(x)} \nabla ^2f(x) - \frac{1}{f(x)^2}\nabla f(x) \nabla f(x)^T$$

$$f$$ là log-lồi $$\Longleftrightarrow$$ $$f(x) \nabla ^2 f(x) \succeq \nabla f(x)\nabla f(x)^T$$ với mọi $$x \in \text{dom} f$$, và <br>
$$f$$ là log-lõm $$\Longleftrightarrow$$ $$f(x) \nabla ^2 f(x) \preceq \nabla f(x)\nabla f(x)^T$$ với mọi $$x \in \text{dom} f$$.

<br>
### Nhân
Tính log-lồi và log-lõm đóng dưới phép nhân và nhân với số dương. 
Nếu $$f$$ và $$g$$ là log-lõm, thì tích theo điểm $$h(x) = f(x)g(x)$$ cũng là log-lõm. 
Điều này là vì $$\log h(x) = \log f(x) + \log g(x)$$, và cả $$\log f(x)$$ và $$\log g(x)$$ đều là các hàm lõm.

### Cộng và Tích phân
Nói chung, tổng của các hàm log-lõm không phải là log-lõm. Tuy nhiên, tính log-lồi được bảo toàn dưới phép cộng.
Ví dụ, gọi $$f$$ và $$g$$ là các hàm log-lồi, tức là $$F = \log f$$ và $$G = \log g$$ là lồi.
Bằng các quy tắc hợp thành cho hàm lồi, điều sau đây đúng:<br>

>$$\log(exp F + exp G) = \log(f + g)$$

Điều này là lồi. (Vế trái là lồi vì: 1. các hàm log-lồi là lồi, 2. áp dụng hàm mũ cho hàm lồi bảo toàn tính lồi, 3. tổng của các hàm lồi là lồi, và 4. logarithm của hàm lồi là lồi.
Do đó, toàn bộ kết quả là lồi.) Kết luận, tổng của hai hàm log-lồi là log-lồi. 

Tổng quát hóa điều này, nếu $$f(x, y)$$ là log-lồi với mọi $$y \in C$$, thì $$g(x)$$ là log-lồi.
>$$g(x) = \int_C^{} f(x,y) dy $$ 

### Tích phân của các hàm log-lõm
Trong một số trường hợp, tính log-lõm cũng được bảo toàn dưới phép tích phân. Nếu $$f : \mathbb{R}^n \times \mathbb{R}^m \mapsto \mathbb{R}$$ là log-lõm, thì $$g(x)$$ là một hàm log-lõm với $$x \in \mathbb{R}^n$$.
>$$f : \mathbb{R}^n \mapsto \mathbb{R}$$ là log-lõm $$\Longrightarrow$$ $$g(x) = \int_{}^{} f(x,y) dy$$ là log-lõm , $$x \in \mathbb{R}^n$$ với mọi $$y \in C$$.

Dựa trên điều này, chúng ta có thể xác nhận rằng phân phối biên của một mật độ xác suất log-lõm là log-lõm.<br>

Tính log-lõm cũng đóng dưới các phép toán tích chập. Nếu $$f$$ và $$g$$ là log-lõm trên $$\mathbb{R}^n$$, thì tích chập của chúng cũng là log-lõm. 
>$$f$$, $$g$$ là log-lõm trên $$\mathbb{R}^n \Longrightarrow (f \ast g)(x) = \int_{}^{} f(x-y)g(y) dy$$ là log-lõm.<br>

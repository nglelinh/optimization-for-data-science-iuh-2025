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

Phần này giới thiệu các hàm log-lõm và log-lồi — hai lớp hàm quan trọng trong xác suất, thống kê và tối ưu hóa.

## Định nghĩa

### Hàm lõm logarithm (log-lõm)
Một hàm $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ thỏa mãn $$f(x) > 0$$ với mọi $$x \in \text{dom}f$$ được gọi là **lõm logarithm** (hay **log-lõm**) nếu $$\log f$$ là hàm lõm:
> $$f$$ là log-lõm với $$f(x) > 0$$ cho mọi $$x \in \text{dom}f$$ khi và chỉ khi:<br>
>$$f(\theta x + (1 - \theta) y) \geq f(x)^\theta f(y)^{1-\theta}$$ với mọi $$x, y \in \text{dom}f$$ và $$0 \leq \theta \leq 1$$.

### Hàm lồi logarithm (log-lồi)
Một hàm $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ thỏa mãn $$f(x) > 0$$ với mọi $$x \in \text{dom}f$$ được gọi là **lồi logarithm** (hay **log-lồi**) nếu $$\log f$$ là hàm lồi. Do đó, $$f$$ là log-lồi khi và chỉ khi $$1/f$$ là log-lõm:
> $$f$$ là log-lồi với $$f(x) > 0$$ cho mọi $$x \in \text{dom}f$$ $$\Longleftrightarrow \frac{1}{f}$$ là log-lõm.

Trong một số bối cảnh, ta cho phép $$f$$ nhận giá trị bằng 0 với quy ước $$\log 0 = -\infty$$; khi đó $$f$$ vẫn được gọi là log-lõm nếu hàm giá trị thực mở rộng $$\log f$$ là hàm lõm.

**Vì hàm logarithm đơn điệu tăng, mọi hàm log-lồi đều là hàm giả lồi và mọi hàm log-lõm đều là hàm giả lõm.**

## Ví dụ

### Hàm affine
Hàm affine dương sau đây là hàm log-lõm:
>$$f(x) = a^Tx + b$$ trên $$\{x \mid a^Tx + b > 0\}$$

### Hàm lũy thừa
$$f(x) = x^a$$ trên $$\mathbb{R}_{++}$$ là hàm log-lồi khi $$a \leq 0$$ và là hàm log-lõm khi $$a \geq 0$$.

### Hàm mũ
$$f(x) = e^{ax}$$ vừa là hàm log-lồi vừa là hàm log-lõm.

### Hàm phân phối tích lũy của phân phối chuẩn (Gauss)
$$\Phi(x) = \frac{1}{ \sqrt{2 \pi } } \int_{-\infty}^x e^{-u^2/2} du$$ là hàm log-lõm.

### Hàm Gamma
$$\Gamma(x) = \int_0^\infty u^{x-1}e^{-u} du$$ là hàm log-lồi với $$x \geq 1$$ (thực tế đúng trên toàn bộ $$\mathbb{R}_{++}$$).

### Định thức
$$\det X$$ là hàm log-lõm trên $$\mathbb{S}^n_{++}$$.

### Tỉ số giữa định thức và vết
$$\det X / \text{tr} X$$ là hàm log-lõm trên $$\mathbb{S}^n_{++}$$.

<br>

## Tính chất

### Hàm log-lồi và log-lõm khả vi hai lần
Nếu $$f$$ khả vi hai lần trên miền lồi $$\text{dom} f$$ và $$f(x) > 0$$, ta có:
>$$\nabla^2 \log f(x) = \frac{1}{f(x)} \nabla^2 f(x) - \frac{1}{f(x)^2}\nabla f(x) \nabla f(x)^T$$

Do đó:<br>
$$f$$ là log-lồi $$\Longleftrightarrow$$ $$f(x) \nabla^2 f(x) \succeq \nabla f(x)\nabla f(x)^T$$ với mọi $$x \in \text{dom} f$$, và<br>
$$f$$ là log-lõm $$\Longleftrightarrow$$ $$f(x) \nabla^2 f(x) \preceq \nabla f(x)\nabla f(x)^T$$ với mọi $$x \in \text{dom} f$$.

<br>

### Phép nhân
Tính log-lồi và tính log-lõm được bảo toàn qua phép nhân và phép nhân với hằng số dương. Chẳng hạn, nếu $$f$$ và $$g$$ là log-lõm thì tích theo điểm $$h(x) = f(x)g(x)$$ cũng là log-lõm, vì $$\log h(x) = \log f(x) + \log g(x)$$ là tổng của hai hàm lõm.

### Phép cộng và tích phân của hàm log-lồi
Nhìn chung, tổng của hai hàm log-lõm không nhất thiết log-lõm; tuy nhiên tính log-lồi được bảo toàn qua phép cộng. Thật vậy, nếu $$f$$ và $$g$$ là các hàm log-lồi thì $$F = \log f$$ và $$G = \log g$$ đều lồi. Áp dụng quy tắc hợp thành vector cho hàm log-sum-exp (là hàm lồi và không giảm theo từng biến), ta thấy:

>$$\log(\exp F + \exp G) = \log(f + g)$$

là một hàm lồi, do đó $$f + g$$ là hàm log-lồi.

Tổng quát hóa sang dạng tích phân: nếu $$f(x, y)$$ là log-lồi theo $$x$$ với mọi $$y \in C$$, thì hàm $$g(x)$$ sau đây cũng là log-lồi:
>$$g(x) = \int_C f(x,y)\, dy$$

### Tích phân và tích chập của hàm log-lõm
Tính log-lõm cũng được bảo toàn khi lấy tích phân theo một nhóm biến: nếu $$f : \mathbb{R}^n \times \mathbb{R}^m \mapsto \mathbb{R}$$ là hàm log-lõm đồng thời theo $$(x, y)$$, thì hàm biên $$g(x)$$ là log-lõm theo $$x \in \mathbb{R}^n$$:
>$$f : \mathbb{R}^n \times \mathbb{R}^m \mapsto \mathbb{R}$$ là log-lõm $$\Longrightarrow$$ $$g(x) = \int f(x,y)\, dy$$ là log-lõm theo $$x \in \mathbb{R}^n$$.

Từ kết quả này suy ra mọi phân phối biên của một mật độ xác suất log-lõm đều là hàm log-lõm.<br>

Tính log-lõm cũng được bảo toàn qua phép tích chập: nếu $$f$$ và $$g$$ là các hàm log-lõm trên $$\mathbb{R}^n$$ thì tích chập của chúng cũng là hàm log-lõm:
>$$f, g$$ là log-lõm trên $$\mathbb{R}^n \Longrightarrow (f \ast g)(x) = \int f(x-y)g(y)\, dy$$ là log-lõm.<br>

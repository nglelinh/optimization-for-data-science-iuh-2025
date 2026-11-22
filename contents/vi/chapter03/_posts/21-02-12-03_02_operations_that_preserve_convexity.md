---
layout: post
title: 03-02 Các phép toán bảo toàn tính lồi
chapter: '03'
order: 6
owner: Minjoo Lee
categories:
- chapter03
lang: vi
lesson_type: required
---

Phần này trình bày các phép toán bảo toàn tính lồi của hàm số:

- Tổng trọng số không âm
- Hợp thành với hàm affine và hợp thành tổng quát
- Maximum và supremum theo điểm
- Hàm phối cảnh
- Hàm tuyến tính-phân thức

## Tổng trọng số không âm

Các hàm lồi đóng đối với phép nhân với số không âm và phép cộng:

* Nhân một hàm lồi $$f$$ với số thực không âm $$\alpha \ge 0$$ vẫn thu được một hàm lồi:
>$$f$$ lồi $$\Rightarrow \alpha f$$ lồi với $$\alpha \ge 0$$

* Tổng của hai hàm lồi $$f_1, f_2$$ là một hàm lồi:
>$$f_1, f_2$$ lồi $$\Rightarrow f_1 + f_2$$ lồi

* Tổng trọng số không âm của các hàm lồi $$f_1, \dots, f_n$$ là hàm lồi:
>$$f_1, ..., f_n$$ lồi $$\Rightarrow \alpha_1f_1 + \cdots + \alpha_nf_n$$ lồi, $$\alpha_1, ..., \alpha_n \ge 0$$

## Hợp thành

### 1. Hợp thành với ánh xạ affine
Nếu $$f$$ là hàm lồi thì hàm $$g(x) = f(Ax + b)$$ cũng là hàm lồi:
> $$f$$ lồi $$\Rightarrow f(Ax + b)$$ lồi

### 2. Hợp thành vô hướng
Xét hàm $$g:\mathbb{R}^n \mapsto \mathbb{R}$$ và hàm $$h:\mathbb{R}\mapsto \mathbb{R}$$. Hàm hợp thành $$f(x)=h(g(x))$$ có tính lồi hoặc lõm theo các quy tắc sau:

> hợp thành của $$g:\mathbb{R}^n \mapsto \mathbb{R}$$ và $$h:\mathbb{R}\mapsto \mathbb{R}$$:
> $$f(x)=h(g(x))$$

* Nếu $$g$$ lồi, $$h$$ lồi và $$\tilde{h}$$ không giảm, thì $$f$$ lồi.
* Nếu $$g$$ lõm, $$h$$ lồi và $$\tilde{h}$$ không tăng, thì $$f$$ lồi.
* Nếu $$g$$ lõm, $$h$$ lõm và $$\tilde{h}$$ không giảm, thì $$f$$ lõm.
* Nếu $$g$$ lồi, $$h$$ lõm và $$\tilde{h}$$ không tăng, thì $$f$$ lõm.

### [Lưu ý]
Tính đơn điệu phải đúng cho phần mở rộng giá trị thực mở rộng $$\tilde{h}$$ của $$h$$ (gán $$+\infty$$ ngoài $$\text{dom } h$$ khi $$h$$ lồi, hoặc $$-\infty$$ khi $$h$$ lõm).

### Ví dụ
* Nếu $$g$$ lồi thì $$\exp g(x)$$ lồi.
* Nếu $$g$$ lõm và dương thì $$1/g(x)$$ lồi.

### 3. Hợp thành vector
Xét $$g:\mathbb{R}^n \mapsto \mathbb{R}^k$$ và $$h:\mathbb{R}^k \mapsto \mathbb{R}$$, với hàm hợp thành $$f(x)=h(g(x))=h(g_1(x),g_2(x),\dots,g_k(x))$$:

> hợp thành của $$g:\mathbb{R}^n\mapsto\mathbb{R}^k$$ và $$h:\mathbb{R}^k\mapsto\mathbb{R}$$:
> $$f(x)=h(g(x))=h(g_1(x),g_2(x),...,g_k(x))$$

* Nếu mỗi $$g_i$$ lồi, $$h$$ lồi và $$\tilde{h}$$ không giảm theo từng đối số, thì $$f$$ lồi.
* Nếu mỗi $$g_i$$ lồi, $$h$$ lõm và $$\tilde{h}$$ không tăng theo từng đối số, thì $$f$$ lõm.

### Ví dụ
* Nếu các hàm $$g_i$$ lõm và dương thì $$\sum_{i=1}^{m} \log g_i(x)$$ lõm.
* Nếu các hàm $$g_i$$ lồi thì $$\log \sum_{i=1}^{m} \exp g_i(x)$$ lồi.

## Maximum và supremum theo điểm

### 1. Maximum theo điểm
> $$f_1, f_2$$ là các hàm lồi $$\Rightarrow f(x) = \max \{ f_1(x), f_2(x) \}$$ (với $$\text{dom } f = \text{dom } f_1 \cap \text{dom } f_2$$) là hàm lồi.

### 2. Supremum theo điểm
Nếu $$f(x, y)$$ lồi theo $$x$$ với mọi $$y \in A$$ thì $$g(x) = \sup_{y\in A} f(x, y)$$ cũng là hàm lồi theo $$x$$:

>$$f(x, y)$$ lồi theo $$x$$ với mọi $$y \in A$$
>$$\Rightarrow g(x) = \sup_{y\in A} f(x, y)$$ với $$\text{dom } g = \{x \mid (x, y) \in \text{dom} f \text{ với mọi } y \in A, \sup_{y \in A} f(x, y) < \infty \}$$ lồi theo $$x$$

## Hàm phối cảnh

Hàm phối cảnh $$g: \mathbb{R}^n \times \mathbb{R} \mapsto \mathbb{R}$$ của một hàm $$f: \mathbb{R}^n \mapsto \mathbb{R}$$ được định nghĩa là:

$$g(x,t) = tf\left(\frac{x}{t}\right), \quad \text{dom } g = \left\{(x,t) \left| \frac{x}{t} \in \text{dom } f, t>0 \right.\right\}$$

Phép biến đổi phối cảnh bảo toàn tính lồi: nếu $$f$$ lồi thì $$g$$ cũng lồi.

### Ví dụ
* **Hàm bậc hai chia tuyến tính:** Vì $$f(x) = x^Tx$$ là hàm lồi, nên hàm phối cảnh của nó $$g(x,t) = x^Tx/t$$ là hàm lồi với $$t > 0$$.

* **Entropy tương đối (từ logarithm âm):** Vì $$f(x) = -\log x$$ là hàm lồi trên $$\mathbb{R}_{++}$$, nên hàm phối cảnh của nó — entropy tương đối $$g(x,t) = t\log t - t\log x$$ — là hàm lồi trên $$\mathbb{R}_{++}^2$$.

* **Kết hợp với biến đổi affine:** Nếu $$f$$ lồi thì hàm $$g(x)=(c^Tx+d)f\left(\frac{Ax+b}{c^Tx+d}\right)$$ là hàm lồi trên miền:
> $$\left\{x \left| c^Tx+d>0, \frac{Ax+b}{c^Tx+d} \in \text{dom } f\right.\right\}$$
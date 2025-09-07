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

Phần này thảo luận các phép toán bảo toàn tính lồi của các hàm lồi.

- Tổng trọng số không âm
- Hợp thành với hàm affine
- Maximum theo điểm
- Hàm phối cảnh
- Hàm tuyến tính-phân thức


## Tổng trọng số không âm
Các hàm lồi có các tính chất sau đối với phép nhân vô hướng và phép cộng:

• Khi một hàm lồi $$f$$ tồn tại, nhân nó với bất kỳ số không âm nào vẫn cho ra một hàm lồi $$f$$.
>$$f$$ lồi $$\Rightarrow \alpha f$$ lồi với $$\alpha \ge 0$$

• Khi hai hàm lồi ($$f_1, f_2$$) tồn tại, tổng của chúng cũng lồi.
>$$f_1, f_2$$ lồi $$\Rightarrow f_1 + f_2$$ lồi

• Tổng trọng số không âm của các hàm lồi $$f_1, ..., f_m$$ là hàm lồi.
>$$f_1, ..., f_n$$ lồi $$\Rightarrow \alpha_1f_1 + \cdots + \alpha_nf_n$$ lồi, $$\alpha_1, ..., \alpha_n \ge 0$$


## Hợp thành
### 1. Hợp thành affine
Nếu hàm $$f$$ lồi, thì $$f(Ax + b)$$ cũng lồi.
> $$f$$ lồi $$\Rightarrow f(Ax + b)$$ lồi


### 2. Hợp thành tổng quát
Giả sử chúng ta có hàm $$g$$ ánh xạ từ không gian $$n$$ chiều sang không gian 1 chiều và hàm $$h$$ ánh xạ từ không gian 1 chiều sang không gian 1 chiều.
Hàm hợp thành $$f(x)=h(g(x))$$ lồi hoặc lõm trong các trường hợp sau:

> hợp thành của $$g:\mathbb{R}^n \mapsto \mathbb{R}$$ và $$h:\mathbb{R}\mapsto \mathbb{R}$$:
> $$f(x)=h(g(x))$$

• Nếu $$g$$ lồi, $$h$$ lồi, và $$h$$ không giảm, thì $$f$$ lồi.
• Nếu $$g$$ lõm, $$h$$ lồi, và $$h$$ không tăng, thì $$f$$ lồi.
• Nếu $$g$$ lõm, $$h$$ lõm, và $$h$$ không giảm, thì $$f$$ lõm.
• Nếu $$g$$ lồi, $$h$$ lõm, và $$h$$ không tăng, thì $$f$$ lõm.

### [Lưu ý]
Tính đơn điệu của phần mở rộng giá trị mở rộng $$\tilde{h}$$ phải được bảo toàn. 

### Ví dụ
• Nếu $$g$$ lồi, thì $$\exp g(x)$$ lồi.
• Nếu $$g$$ lõm và dương, thì $$1/g(x)$$ lồi. 

### 3. Hợp thành vector
Giả sử chúng ta có hàm $$g$$ ánh xạ từ không gian $$n$$ chiều sang không gian $$k$$ chiều và hàm $$h$$ ánh xạ từ không gian $$k$$ chiều sang không gian 1 chiều.
Khi đó hàm hợp thành $$f(x)=h(g(x))=h(g_1(x),g_2(x),...,g_k(x))$$ lồi hoặc lõm trong các trường hợp sau:

>hợp thành của $$g:\mathbb{R}^n\mapsto\mathbb{R}^k$$ và $$h:\mathbb{R}^k\mapsto\mathbb{R}$$:
>$$f(x)=h(g(x))=h(g_1(x),g_2(x),...,g_k(x))$$

• Nếu $$g$$ lồi và $$h$$ lồi, và $$h$$ không giảm theo từng đối số, thì $$f$$ lồi.
• Nếu $$g$$ lồi và $$h$$ lõm, và $$h$$ không tăng theo từng đối số, thì $$f$$ lõm.

### Ví dụ
• Nếu $$g_i$$ lõm và dương, thì $$\sum_{i=1}^{m} \log g_i(x)$$ lõm.
• Nếu $$g_i$$ lồi, thì $$\log \sum_{i=1}^{m} \exp g_i(x)$$ lồi.


## Maximum theo điểm
Maximum theo điểm của các hàm được định nghĩa như sau và là hàm lồi:
### 1. Maximum theo điểm
> $$f_1, f_2$$ là các hàm lồi $$\Rightarrow f(x) = \max \{ f_1(x), f_2(x) \}$$, $$\text{dom } f = \text{dom } f_1 \cap \text{dom } f_2$$ là hàm lồi



### 2. Supremum theo điểm
Nếu $$f(x, y)$$ lồi theo $$x$$ với mọi $$y \in A$$, thì $$g(x) = \sup_{y\in A} f(x, y)$$ lồi.

>$$f(x, y)$$ lồi theo $$x$$ với mọi $$y \in A$$
>$$\Rightarrow g(x) = \sup_{y\in A} f(x, y)$$ với $$\text{dom } g = \{x | (x, y) \in \text{dom} f \text{ với mọi } y \in A, \sup < \infty \}$$ lồi theo $$x$$

## Phối cảnh
Nếu hàm $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ lồi, thì phép toán phối cảnh $$g: \mathbb{R}^{n+1} \mapsto \mathbb{R}$$ bảo toàn tính lồi.

Hàm phối cảnh $$g: \mathbb{R}^n×\mathbb{R} \mapsto \mathbb{R}$$ của hàm $$f: \mathbb{R}^n \mapsto \mathbb{R}$$ là:

$$g(x,t) = tf\left(\frac{x}{t}\right), \quad \text{dom } g = \left\{(x,t) \left| \frac{x}{t} \in \text{dom } f, t>0 \right.\right\}$$

Nếu hàm $$f$$ lồi, thì $$g$$ cũng lồi.

### Ví dụ
• Khi $$t$$ dương, nếu $$g(x,t)=x^Tx/t$$ lồi, thì $$f(x)=x^Tx$$ lồi.

• **Logarithm âm**
Khi entropy tương đối $$g(x,t) =t\log t − t\log x$$ lồi trên $$\mathbb{R}_{++}^2$$, thì $$f(x)=−\log x$$ lồi.

• Nếu $$f$$ lồi, thì $$g(x)=(c^Tx+d)f\left(\frac{Ax+b}{c^Tx+d}\right)$$ lồi dưới điều kiện sau:
> $$\left\{x \left| c^Tx+d>0, \frac{Ax+b}{c^Tx+d} \in \text{dom } f\right.\right\}$$
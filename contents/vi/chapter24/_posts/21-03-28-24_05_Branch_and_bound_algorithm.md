---
layout: post
title: '24-05 Thuật toán nhánh và cận (B&B)'
chapter: '24'
order: 6
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

Hãy tìm hiểu cách giải quy hoạch nguyên bằng thuật toán nhánh và cận (Branch and bound) và nới lỏng lồi.

## Định nghĩa và tính chất
Thuật toán nhánh và cận là phương pháp phổ biến nhất để giải quy hoạch nguyên. Về cơ bản đó là cách tiếp cận chia để trị, chia bài toán gốc thành nhiều bài toán nhỏ hơn (bài toán con) để tiến gần đến đáp án đúng. 

Khi tập ràng buộc $$X = X_{1} \cup X_{2} \cup \dotsc \cup X_{k}$$ là hợp của một phân hoạch gồm các $$X_{i}$$,
> $$ \min_{x \in X} f(x) = \min_{i = 1, \dotsc , k} \lbrace \min_{x \in X_{i}} f(x) \rbrace .$$

Ta có thể tìm nghiệm tối ưu bằng cách phân hoạch miền và tìm giá trị nhỏ nhất.

Mọi nghiệm khả thi của một bài toán con đều có thể được đặt làm cận trên $$u(X)$$. Để thu được cận dưới, ta tìm cận dưới $$l(X_{i})$$ của từng bài toán con. Sau đó, nếu $$l(X_{i}) \geq u(X)$$, ta loại bài toán con $$\min_{x \in X_{i}} f(x)$$ tương ứng với phần này. 
 
Bài toán quy hoạch nguyên (IP) được định nghĩa như sau:

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } && x \in C \\\\
> &&&x_j \in \mathbb{Z}, \quad j \in J \\\\
> \end{align}$$
> $$\begin{align}
> \text{trong đó } f \text{ lồi, } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n 
> \quad \text{và} \quad J \subseteq \lbrace 1 \dotsc n \rbrace \\\\
> \end{align}
> $$

Và bài toán nới lỏng lồi (CR) như sau:

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } &&x \in C \\\\
> \end{align}$$
> $$\begin{align}
> \text{trong đó } f \text{ lồi, } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n 
> \quad \text{và} \quad J \subseteq \lbrace 1 \dotsc n \rbrace \\\\
> \end{align}
> $$

Bài toán được giải đệ quy.

* Nếu tập ràng buộc là tầm thường (trivial), giải bài toán (CR). Nếu nghiệm nhỏ hơn cận trên hiện tại thì cập nhật cận trên. Dừng.
    * Nếu (CR) vô nghiệm (không khả thi) thì (IP) cũng không khả thi. Dừng.
    * Nếu nghiệm $$x^{\star}$$ của (CR) cũng khả thi cho (IP) thì $$x^{\star}$$ là nghiệm. Dừng.
* Tìm cận dưới của bài toán.
    * Nếu nghiệm $$x^{\star}$$ của (CR) không khả thi cho (IP), cập nhật cận dưới của (IP).
* Nếu cận dưới lớn hơn cận trên hiện tại, Dừng.
* Chia tập ràng buộc và giải đệ quy từng bài toán con.


## Sau khi phân nhánh

* Sau khi phân nhánh, giải từng bài toán con.
* Nếu cận dưới của một bài toán con lớn hơn cận trên hiện tại thì không cần xét các bài toán con bên dưới nó.
* Phương pháp đáng tin cậy nhất để tính cận dưới là nới lỏng lồi, nhưng các phương pháp khác (ví dụ nới lỏng Lagrange) cũng được dùng.

### Nhánh cận trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/branch-bound_vi.mp4"></video>
</div>

Giải LP nới lỏng, rẽ nhánh theo biến phân số, và loại bỏ mọi nút mà cận không thể vượt nghiệm nguyên tốt nhất đã tìm được.

### Tự tay thử: duyệt qua nhánh cận

<div class="opx-explainer" data-opx="bnb" data-lang="vi"></div>

---
layout: post
title: '25-01-02 Thuật toán mặt phẳng cắt'
chapter: '25'
order: 4
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Trong phần này, ta sẽ xem thuật toán mặt phẳng cắt có thể giải quy hoạch tuyến tính nguyên.

## Bất đẳng thức hợp lệ (Valid Inequality)
Để định nghĩa mặt phẳng cắt, trước hết hãy xem bất đẳng thức hợp lệ là gì. 

Một bất đẳng thức $$\pi^{T}x \le \pi_{0}$$ được gọi là hợp lệ đối với tập $$S$$ nếu thỏa mãn điều kiện sau. Nghĩa là, nếu tập $$S$$ nằm trong nửa không gian xác định bởi bất đẳng thức $$\pi^{T}x \le \pi_{0}$$ thì bất đẳng thức này được coi là hợp lệ đối với $$S$$.

>$$\pi^{T}x \le \pi_{0}$$ với mọi $$x \in S$$

Một bất đẳng thức phải hợp lệ thì mới trở thành mặt phẳng cắt.
## Thuật toán mặt phẳng cắt
Bây giờ hãy xem thuật toán mặt phẳng cắt khi có quy hoạch nguyên sau.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\\\
> \text{subject to } & \quad  x \in C \\\\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\\\
> \end{align}
> $$

Với $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$.

### Thuật toán mặt phẳng cắt
Trong thuật toán sau, bài toán lồi được ký hiệu là CP và quy hoạch nguyên là IP.

1. Đặt $$C_{0} := C$$ và tính $$x^{(0)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{0} \right\}$$
2. với $$k = 0, 1, ...$$ <br>
$$\quad$$nếu $$x^{(k)}$$ khả thi cho (IP) thì $$x^{(k)}$$ là nghiệm tối ưu nên dừng <br>
$$\quad$$ngược lại<br>
$$\quad\quad$$ tìm bất đẳng thức ($$\pi$$, $$\pi_{0}$$) hợp lệ đối với $$S$$ và cắt bỏ $$x^{(k)}$$<br>
$$\quad\quad$$ $$C_{k+1} := C_{k} \cap \{ x : \pi^{T}x \le \pi_{0} \} $$<br>
$$\quad\quad$$ $$x^{(k+1)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{k+1} \right\}$$<br>
$$\quad$$kết thúc nếu<br>
kết thúc vòng lặp<br>

Bất đẳng thức hợp lệ như vậy được gọi là **mặt phẳng cắt (cutting plane)** hoặc **lát cắt (cut)**.

Bước 1 của thuật toán là bước giải bài toán CP bằng nới lỏng lồi. Khi đó tập khả thi là $$C$$. 

Ở bước 2 của thuật toán, nếu nghiệm tìm được khả thi cho IP thì lấy làm nghiệm. Nếu không khả thi, ta tìm một bất đẳng thức hợp lệ tách nghiệm $$x^{(k)}$$ khỏi tập $$S$$ và thu hẹp phạm vi của $$C_{k}$$. Sau đó giải bài toán CP được định nghĩa lại trên $$C_{k+1}$$ và lặp lại bước 2. 

Trong hình dưới, đa giác biểu diễn tập $$C$$ và nghiệm của CP được đánh dấu bằng chấm đen. Khi đó, bất đẳng thức hợp lệ cắt bỏ nghiệm và thu hẹp phạm vi của tập $$C$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_02_valid_inequality.png" alt="[Hình 1] Bất đẳng thức hợp lệ">
  <figcaption style="text-align: center;">[Hình 1] Bất đẳng thức hợp lệ [3]</figcaption>
</p>
</figure>

Cứ thu hẹp phạm vi của tập $$C$$ như vậy, cuối cùng ta gặp tập $$S$$, tức tập khả thi bao lồi của bài toán IP, và có thể tìm được nghiệm khả thi cho IP.

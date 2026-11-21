---
layout: post
title: '19-01-03 Ánh xạ proximal có tỉ lệ (Scaled proximal map)'
chapter: '19'
order: 5
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

**Phương pháp Newton proximal** có thể được viết lại theo cùng dạng với **proximal gradient descent**.

## Ánh xạ proximal có tỉ lệ
Nếu $$H \succ 0$$, **ánh xạ proximal có tỉ lệ (scaled proximal map)** được định nghĩa như sau.

> \begin{align}
\text{prox}_{H}(x) = \underset{z}{\text{argmin}}  \frac{1}{2} \parallel x - z \parallel_H^2 + h(z)
\end{align}

Ở đây $$\parallel x\parallel_H^2 = x^THx$$ là bình phương chuẩn $$H$$. Khi $$H = \frac{1}{t} I$$, ta thu được **ánh xạ proximal không tỉ lệ** thông thường.

Nói chung, **ánh xạ proximal có tỉ lệ** có các tính chất tốt giống như prox thông thường.

* **tính duy nhất**: nghiệm là duy nhất (điều này đúng vì $$H \succ 0$$ làm bài toán lồi chặt).
* **tính không giãn (non-expansiveness)**: ánh xạ không làm giãn khoảng cách (điều này đúng vì ánh xạ proximal có tỉ lệ là tổng quát hóa của toán tử chiếu, vốn không giãn).

#### [Ghi chú] Tính không giãn của toán tử chiếu
Với hai điểm $$x$$, $$y$$ và toán tử chiếu $$P_C$$ lên tập lồi $$C$$, tính không giãn nghĩa là $$\parallel P_C(x) - P_C(y) \parallel_2 \le \parallel x - y \parallel_2$$. Nói cách khác, $$P_C$$ là 1-Lipschitz, điều này đúng bất cứ khi nào $$C$$ lồi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_03_projection_operator.png" alt="[Hình 1] Phép chiếu lên tập lồi C [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Phép chiếu lên tập lồi C [3]</figcaption>
</p>
</figure>

## Cập nhật Newton proximal
Sử dụng **ánh xạ proximal có tỉ lệ**, cập nhật Newton proximal có thể được viết lại như sau.

> $$
> \begin{align}
> z^{+} & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2} (z - x)^T H (z - x) + h(z) \\\\
> & =\underset{z}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2 + h(z)
> \end{align}
> $$

Tương đương:

> $$
> \begin{align}
> z^{(k)} & = \text{prox}_{H^{(k-1)}} ( x^{(k-1)} - (H^{(k-1)})^{-1} \nabla g (x^{(k-1)}) ) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

Một cách trực quan, ta thực hiện một bước Newton trên $$g$$, áp dụng toán tử prox có tỉ lệ theo $$H^{(k-1)}$$, rồi di chuyển theo hướng đó.

Từ đây ta thấy:

* Khi $$h(z) = 0$$, toán tử proximal là phép đồng nhất và ta thu lại cập nhật Newton thông thường.
* Nếu thay $$H^{(k-1)}$$ bằng $$\frac{1}{r_k} I$$ và đặt $$t_k = 1$$, ta thu được cập nhật proximal gradient với kích thước bước $$r_k$$.
* Độ khó của prox không chỉ phụ thuộc vào $$h$$ mà còn phụ thuộc vào cấu trúc Hessian của $$g$$. Ví dụ, nếu $$H$$ là ma trận đường chéo hoặc dải (banded) thì bài toán dễ hơn nhiều so với khi $$H$$ dày đặc (dense).

Như vậy, phương pháp Newton proximal tổng quát hóa cả proximal gradient descent lẫn phương pháp Newton.

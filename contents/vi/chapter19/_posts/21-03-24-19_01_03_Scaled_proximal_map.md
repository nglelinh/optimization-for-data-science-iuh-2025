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

**Phương pháp Newton proximal** có thể được viết lại dưới dạng hoàn toàn tương đồng với **proximal gradient descent** nhờ khái niệm ánh xạ proximal có tỉ lệ.

## Ánh xạ proximal có tỉ lệ
Với ma trận xác định dương $$H \succ 0$$, **ánh xạ proximal có tỉ lệ (scaled proximal map)** ứng với hàm $$h$$ được định nghĩa là:

> \begin{align}
\text{prox}_{H}(x) = \underset{z}{\text{argmin}} \ \frac{1}{2} \parallel x - z \parallel_H^2 + h(z)
\end{align}

trong đó $$\parallel x \parallel_H^2 = x^THx$$ là bình phương chuẩn cảm sinh bởi $$H$$. Khi $$H = \frac{1}{t} I$$, biểu thức này quay về **ánh xạ proximal thông thường**.

Nhìn chung, **ánh xạ proximal có tỉ lệ** giữ nguyên các tính chất tốt của toán tử prox chuẩn:

* **Tính duy nhất:** Nghiệm cực tiểu là duy nhất vì $$H \succ 0$$ làm bài toán con lồi chặt.
* **Tính không giãn (non-expansiveness):** Ánh xạ không làm tăng khoảng cách theo chuẩn $$H$$ (tổng quát hóa trực tiếp tính không giãn của phép chiếu lên tập lồi).

#### [Ghi chú] Tính không giãn của toán tử chiếu
Với hai điểm $$x, y$$ và toán tử chiếu Euclid $$P_C$$ lên tập lồi $$C$$, tính không giãn có nghĩa là $$\parallel P_C(x) - P_C(y) \parallel_2 \le \parallel x - y \parallel_2$$. Nói cách khác, $$P_C$$ là ánh xạ 1-Lipschitz với mọi tập lồi $$C$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.01_03_projection_operator.png" alt="[Hình 1] Phép chiếu lên tập lồi C [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Phép chiếu lên tập lồi C [3]</figcaption>
</p>
</figure>

## Biểu diễn cập nhật Newton proximal
Sử dụng **ánh xạ proximal có tỉ lệ**, bài toán con của phương pháp Newton proximal có thể viết gọn lại như sau:

> $$
> \begin{align}
> z^{+} & = \underset{z}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2} (z - x)^T H (z - x) + h(z) \\\\
> & =\underset{z}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2 + h(z)
> \end{align}
> $$

Do đó, phép cập nhật Newton proximal tương đương với:

> $$
> \begin{align}
> z^{(k)} & = \text{prox}_{H^{(k-1)}} ( x^{(k-1)} - (H^{(k-1)})^{-1} \nabla g (x^{(k-1)}) ) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

Về mặt trực giác, thuật toán thực hiện một bước Newton trên phần trơn $$g$$, áp dụng toán tử proximal có tỉ lệ theo ma trận $$H^{(k-1)}$$, rồi di chuyển theo hướng thu được.

Từ công thức trên có thể rút ra ba nhận xét quan trọng:

* Khi $$h(z) = 0$$, toán tử proximal trở thành phép đồng nhất và ta thu lại phương pháp Newton cổ điển.
* Khi thay $$H^{(k-1)}$$ bằng $$\frac{1}{r_k} I$$ và đặt $$t_k = 1$$, ta thu lại proximal gradient descent với kích thước bước $$r_k$$.
* Độ khó tính toán của toán tử prox không chỉ phụ thuộc vào $$h$$ mà còn phụ thuộc mạnh vào cấu trúc của ma trận $$H$$: nếu $$H$$ là ma trận đường chéo hoặc ma trận dải (banded), việc giải bài toán con dễ hơn nhiều so với khi $$H$$ dày đặc (dense).

Như vậy, phương pháp Newton proximal thống nhất cả proximal gradient descent và phương pháp Newton trong cùng một khuôn khổ.

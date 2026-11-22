---
layout: post
title: '25-01-01 Lồi hóa (Convexification)'
chapter: '25'
order: 3
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Quá trình biến đổi một bài toán quy hoạch nguyên thành một bài toán tối ưu lồi tương đương được gọi là lồi hóa (convexification). Trong trường hợp quy hoạch tuyến tính nguyên, tập khả thi sau khi lồi hóa trở thành một đa diện (polyhedron), tạo cơ sở lý thuyết để xây dựng các mặt phẳng cắt hợp lệ.

## Lồi hóa

Xét bài toán quy hoạch nguyên với hàm mục tiêu tuyến tính, tập ràng buộc lồi $$C$$ và ràng buộc nguyên trên tập chỉ số $$J$$:

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\\\
> \text{subject to } & \quad  x \in C \\\\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J
> \end{align}
> $$

Định nghĩa bao lồi của tập các điểm khả thi nguyên là $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$. Thay tập khả thi ban đầu bằng $$S$$, ta thu được bài toán tối ưu lồi tương đương:

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\\\
> \text{subject to } & \quad  x \in S
> \end{align}
> $$

Trong Hình 1, vùng xanh là tập lồi $$C$$, các điểm đỏ là những điểm thỏa mãn ràng buộc nguyên, và vùng đỏ chính là bao lồi $$S$$ của các điểm đó.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Hình 1] Mặt phẳng cắt">
  <figcaption style="text-align: center;">[Hình 1] Mặt phẳng cắt</figcaption>
</p>
</figure>

Nguồn: https://commons.wikimedia.org/wiki/File:Cutting_plane_algorithm2.png

Hai bài toán có cùng giá trị tối ưu (và mọi điểm cực trị của $$S$$ đều là điểm nguyên) chính vì hàm mục tiêu $$c^T x$$ là hàm tuyến tính.

## Trường hợp đặc biệt: quy hoạch tuyến tính nguyên

Áp dụng lồi hóa cho bài toán quy hoạch tuyến tính nguyên:

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\\\
> \text{subject to } & \quad  Ax \le b \\\\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J
> \end{align}
> $$

Ta có kết quả nền tảng sau về bao lồi $$S$$:

> **Định lý:** Nếu các phần tử của $$A$$ và $$b$$ là số hữu tỉ thì tập
> $$S := \text{conv} \left \{ x : Ax \le b, \; x_j \in \mathbb{Z}, \; j \in J \right \}$$
> là một đa diện (polyhedron).

Về mặt lý thuyết, điều này đồng nghĩa quy hoạch tuyến tính nguyên có thể viết dưới dạng một quy hoạch tuyến tính trên đa diện $$S$$. Tuy nhiên, trên thực tế đa diện $$S$$ có thể cần số lượng bất đẳng thức lớn theo hàm mũ để mô tả đầy đủ. Do đó ta không thể liệt kê trước toàn bộ $$S$$ mà phải giải gián tiếp bằng các kỹ thuật như mặt phẳng cắt hay nhánh và cắt.

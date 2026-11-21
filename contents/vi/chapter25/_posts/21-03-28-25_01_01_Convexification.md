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

Việc biến một quy hoạch nguyên thành một bài toán lồi tương đương được gọi là lồi hóa (convexification). Khi thực hiện lồi hóa, tập khả thi trở thành một đa diện (polyhedron), giúp dễ tìm các mặt phẳng cắt hợp lệ cho thuật toán mặt phẳng cắt.

## Lồi hóa
Để lồi hóa một quy hoạch nguyên, hàm mục tiêu phải tuyến tính. Khi đó các ràng buộc của quy hoạch nguyên gồm một tập lồi $$C$$ và ràng buộc nguyên trên các biến $$x_j$$.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\\\
> \text{subject to } & \quad  x \in C \\\\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\\\
> \end{align}
> $$

Khi đó, tập khả thi có thể được định nghĩa lại là bao lồi $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$. Dùng tập khả thi xác định bởi bao lồi $$S$$ này, ta có thể định nghĩa một bài toán lồi tương đương với bài toán gốc như sau. Quá trình này được gọi là lồi hóa.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\\\
> \text{subject to } & \quad  x \in S \\\\
> \end{align}
> $$

Trong hình dưới, vùng xanh là $$C$$, các điểm đỏ là các điểm nguyên, và bao lồi $$S$$ tạo bởi hai tập này là vùng đỏ.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Hình 1] Mặt phẳng cắt">
  <figcaption style="text-align: center;">[Hình 1] Mặt phẳng cắt</figcaption>
</p>
</figure>
Nguồn: https://commons.wikimedia.org/wiki/File:Cutting_plane_algorithm2.png <br><br>

Lý do hai công thức này tương đương là vì hàm mục tiêu tuyến tính. 

## Trường hợp đặc biệt: quy hoạch tuyến tính nguyên
Hãy áp dụng quá trình lồi hóa trên cho quy hoạch tuyến tính nguyên sau.

> $$
> \begin{align}
>           \min_{x} & \quad {c^{T}x} \\\\
> \text{subject to } & \quad  Ax \le b \\\\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\\\
> \end{align}
> $$

Bao lồi $$S$$ của quy hoạch tuyến tính nguyên được định nghĩa như sau:

> **Định lý**: Nếu $$A, b$$ là các số hữu tỉ thì tập sau là một đa diện (polyhedron).
$$S := \text{conv} \left \{ x : Ax \le b,  x_j \in \mathbb{Z}, j \in J \right \}$$

Vậy quy hoạch tuyến tính nguyên có phải là một quy hoạch tuyến tính không? Tất nhiên là có. Tuy nhiên, trong trường hợp này, đa diện $$S$$ có thể trở thành một đa diện rất phức tạp với số bất đẳng thức lớn theo hàm mũ. Vì vậy, nói chung ta cần giải bài toán bằng các phương pháp khác với các phương pháp giải quy hoạch tuyến tính.

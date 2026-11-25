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

Một câu hỏi lý thuyết đẹp đến ngỡ ngàng: *nếu bài toán quy hoạch nguyên khó vì tập khả thi rời rạc và không lồi, liệu ta có thể "bọc" toàn bộ các điểm nguyên khả thi bằng một tập lồi nhỏ nhất (bao lồi) rồi giải như một bài toán tối ưu lồi bình thường không?*

Câu trả lời là **có** — quá trình đó gọi là **lồi hóa (convexification)**. Khi hàm mục tiêu là tuyến tính $$c^T x$$, cực tiểu trên một tập rời rạc luôn trùng khớp hoàn toàn với cực tiểu trên bao lồi $$S$$ của nó, bởi giá trị nhỏ nhất của hàm tuyến tính luôn đạt tại một đỉnh cực trị — mà mọi đỉnh cực trị của $$S$$ chính là các điểm nguyên khả thi ban đầu!

## Kiến thức cần nhớ: Ba trụ cột của phép Lồi hóa

Để hiểu vì sao lồi hóa vừa là "chén thánh" lý thuyết, vừa không thể thực hiện trực tiếp một lần cho xong trong thực tế, hãy nắm ba trụ cột sau:

- **Tương đương tối ưu trên Bao lồi (Convex Hull Equivalence):** Với hàm mục tiêu tuyến tính $$c^T x$$, mọi điểm $$x \in S = \operatorname{conv}(X)$$ là tổ hợp lồi $$\sum \lambda_i x^{(i)}$$ của các điểm nguyên $$x^{(i)} \in X$$, nên $$c^T x = \sum \lambda_i (c^T x^{(i)}) \ge \min_{i} c^T x^{(i)}$$. Do đó $$\min_{x \in S} c^T x = \min_{x \in X} c^T x$$ — không hề bị nới lỏng chút nào!
- **Định lý Meyer (1974) về tính đa diện:** Khi $$C = \{x : Ax \le b\}$$ là một đa diện hữu tỷ (mọi hệ số của $$A, b$$ là số hữu tỷ), bao lồi nguyên $$S = \operatorname{conv}(\{x \in C : x_j \in \mathbb{Z}\})$$ cũng là một **đa diện** (biểu diễn được bằng hữu hạn bất đẳng thức tuyến tính). Nói cách khác, về nguyên tắc, mọi MILP hữu tỷ đều là một LP!
- **Nghịch lý kích thước (Exponential Number of Facets):** Dù $$S$$ chỉ có hữu hạn mặt biên, số lượng bất đẳng thức cần để mô tả trọn vẹn $$S$$ có thể tăng theo hàm mũ theo số chiều $$n$$. Vì vậy, thay vì dựng toàn bộ $$S$$ từ đầu, ta chỉ xây dựng *cục bộ* vài mặt biên ngay quanh vùng chứa nghiệm tối ưu bằng thuật toán mặt phẳng cắt.

### Giải thích: Tự tay dựng toàn bộ bao lồi nguyên $$S$$ của một đa diện 2 chiều

Xét đa diện nới lỏng $$P = \{(x_1, x_2) \in \mathbb{R}^2 : x_1 \ge 0,\; x_2 \ge 0,\; 3x_1 + 2x_2 \le 5\}$$. Hãy tìm chính xác bao lồi nguyên $$S = \operatorname{conv}(P \cap \mathbb{Z}^2)$$.

1. **Liệt kê tất cả điểm nguyên khả thi trong $$P$$:**
   - Với $$x_1 = 0$$: $$2x_2 \le 5 \Rightarrow x_2 \in \{0, 1, 2\}$$, cho các điểm $$(0, 0), (0, 1), (0, 2)$$.
   - Với $$x_1 = 1$$: $$3 + 2x_2 \le 5 \Rightarrow x_2 \in \{0, 1\}$$, cho các điểm $$(1, 0), (1, 1)$$.
   - Với $$x_1 \ge 2$$: $$3(2) = 6 > 5$$ — không còn điểm nguyên nào!
   Tổng cộng có đúng 5 điểm nguyên: $$(0,0), (1,0), (0,1), (1,1), (0,2)$$.
2. **Xác định các đỉnh cực trị và mặt biên (facets) của $$S$$:**
   Bốn đỉnh ngoài cùng tạo nên bao lồi là $$(0,0), (1,0), (1,1), (0,2)$$ (điểm $$(0,1)$$ nằm trên cạnh nối $$(0,0)$$ và $$(0,2)$$).
   Bốn cạnh biên bao quanh tứ giác này cho hệ bất đẳng thức tuyến tính chính xác của $$S$$:
   $$x_1 \ge 0, \qquad x_2 \ge 0, \qquad x_1 \le 1, \qquad x_1 + x_2 \le 2.$$
   (Kiểm tra: cạnh nối $$(1,1)$$ và $$(0,2)$$ chính là đường thẳng $$x_1 + x_2 = 2$$!).
3. **Kiểm chứng sức mạnh lồi hóa với hàm mục tiêu $$\min -x_1 - 0.1 x_2$$:**
   - Trên $$P$$ ban đầu: LP dừng tại đỉnh phân số $$(5/3,\; 0) \approx (1.667, 0)$$ với giá trị $$-1.667$$.
   - Trên bao lồi $$S$$: LP chạy thẳng tới đỉnh nguyên $$(1, 1)$$ với giá trị chính xác $$-1.1$$! Mọi hàm mục tiêu tuyến tính $$c_1 x_1 + c_2 x_2$$ bất kỳ tối ưu trên $$S$$ đều cho ra đúng đỉnh nguyên!

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

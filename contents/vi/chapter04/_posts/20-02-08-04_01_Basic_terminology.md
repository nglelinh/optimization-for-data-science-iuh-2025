---
layout: post
title: 04-01 Thuật ngữ cơ bản
chapter: '04'
order: 2
owner: YoungJae Choung
categories:
- chapter04
lang: vi
lesson_type: required
---
## Cơ bản về Tối ưu hóa Lồi

Hãy cùng ôn tập các thuật ngữ cơ bản được sử dụng trong các bài toán tối ưu hóa lồi. Một bài toán tối ưu hóa lồi được định nghĩa như sau:

>$$
\begin{aligned}
&\text{minimize}_{x \in D} &&{f(x)} \\
&\text{subject to} &&{g_{i}(x) \leq 0, \quad i = 1, \dotsc, m} \\
&&&{h_{j}(x) = 0, \quad j = 1, \dotsc, r},\\\\
\end{aligned}
$$

>trong đó $$f$$ và $$g_{i}$$, $$i=1,\dotsc, m$$ đều là hàm lồi,
>$$h_j, j = 1, \dotsc, r$$ đều là hàm affine,
>và miền tối ưu hóa là $$D = dom(f) \cap \bigcap_{i=1}^{m} dom(g_{i}) \cap  \bigcap_{j=1}^r dom(h_{j})$$.

* $$f$$ được gọi là **hàm tiêu chí** hoặc **hàm mục tiêu**.
* $$g_{i}(x)$$ được gọi là **hàm ràng buộc bất đẳng thức**.
* $$h_{j}(x)$$ được gọi là **hàm ràng buộc đẳng thức**.
* Nếu $$x \in D$$ và $$g_{i}(x) \leq 0$$ với mọi $$i$$ và $$h_{j}(x) = 0$$ với mọi $$j$$, thì $$x$$ là một **điểm khả thi**.
* Với tất cả các điểm khả thi $$x$$, giá trị nhỏ nhất của $$f(x)$$ được gọi là **giá trị tối ưu**, ký hiệu là $$f^{\star}$$.
* Nếu $$x$$ khả thi và $$f(x) = f^{\star}$$, thì $$x$$ được gọi là **tối ưu**, một **nghiệm**, hoặc một **điểm cực tiểu**.
* Nếu $$x$$ khả thi và $$f(x) \le f^{\star} + \epsilon$$, thì $$x$$ được gọi là **$$\epsilon$$-dưới tối ưu**.
* Nếu $$x$$ khả thi và $$g_i(x) = 0$$, thì $$g_i$$ **hoạt động** tại $$x$$.
* Một bài toán cực tiểu hóa lồi có thể được chuyển đổi thành bài toán cực đại hóa lõm.

>$$
\begin{aligned}
&\text{maximize}_{x \in D} &&-f(x)\\
&\text{subject to} &&g_{i}(x) \leq 0, i = 1, .., m\\
&&&h_{j}(x) = 0, j = 1, \dotsc, r,\\\\
\end{aligned}
$$

>trong đó $$f$$ và $$g_{i}$$, $$i=1,\dotsc, m$$ đều là hàm lồi,
>$$h_j, j = 1, \dotsc, r$$ đều là hàm affine,
>và miền tối ưu hóa là $$D = dom(f) \cap \bigcap_{i=1}^{m} dom(g_{i}) \cap  \bigcap_{j=1}^r dom(h_{j})$$.

### Tập Khả thi

Tập khả thi (còn được gọi là miền khả thi hoặc không gian nghiệm) là tập hợp tất cả các điểm khả thi. Nó biểu diễn tất cả các lựa chọn được phép bởi các điều kiện của bài toán.

Tập khả thi, thường được ký hiệu bởi $$S$$ hoặc $$\mathcal{F}$$, được định nghĩa như sau:

> $$ S = \{ \mathbf{x} \in X \mid g_i(\mathbf{x}) \le 0 \text{ với mọi } i=1, \dots, m, \text{ và } h_j(\mathbf{x}) = 0 \text{ với mọi } j=1, \dots, r \} $$

### Tính chất của Tập Khả thi

1.  **Tính lồi:** Nếu tất cả các hàm ràng buộc bất đẳng thức $g_i(\mathbf{x})$ đều lồi và tất cả các hàm ràng buộc đẳng thức $h_j(\mathbf{x})$ đều affine (tuyến tính), thì tập khả thi $S$ là một **tập lồi**. Tính chất này rất quan trọng trong tối ưu hóa lồi, vì nó đảm bảo rằng bất kỳ cực trị địa phương nào cũng là cực trị toàn cục.
2.  **Tính bị chặn:** Một tập khả thi có thể **bị chặn** (được bao quanh trong một vùng hữu hạn) hoặc **không bị chặn** (mở rộng vô hạn theo một hướng nào đó).
3.  **Tập rỗng:** Có thể tập khả thi là tập rỗng ($S = \emptyset$). Điều này có nghĩa là không có điểm nào thỏa mãn tất cả các ràng buộc đã cho, và bài toán tối ưu hóa được gọi là **không khả thi**.
4.  **Đa diện/Đa hình** (**Polytope/Polyhedron**): Trong quy hoạch tuyến tính, nếu tập khả thi khác rỗng và bị chặn, nó được gọi là **đa diện** (polytope). Nếu nó khác rỗng nhưng có thể không bị chặn, nó được gọi là **đa hình** (polyhedron). Cả hai đều là tập lồi.
5.  **Đỉnh (Điểm cực trị):** Đối với các bài toán quy hoạch tuyến tính, nếu một nghiệm tối ưu tồn tại, nó luôn có thể được tìm thấy tại một trong các đỉnh (còn được gọi là điểm cực trị hoặc điểm góc) của tập khả thi. Đây là cơ sở cho các thuật toán như phương pháp Simplex.
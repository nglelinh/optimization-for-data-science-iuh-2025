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

Phần này ôn tập các thuật ngữ cơ bản thường dùng trong các bài toán tối ưu hóa lồi. Một bài toán tối ưu hóa lồi được phát biểu dưới dạng chuẩn như sau:

>$$
\begin{aligned}
&\text{minimize}_{x \in D} &&{f(x)} \\
&\text{subject to} &&{g_{i}(x) \leq 0, \quad i = 1, \dotsc, m} \\
&&&{h_{j}(x) = 0, \quad j = 1, \dotsc, r},\\\\
\end{aligned}
$$

>trong đó $$f$$ và $$g_{i}$$ ($$i=1,\dotsc, m$$) đều là các hàm lồi, $$h_j$$ ($$j = 1, \dotsc, r$$) đều là các hàm affine, và miền xác định của bài toán là $$D = \operatorname{dom}(f) \cap \bigcap_{i=1}^{m} \operatorname{dom}(g_{i}) \cap \bigcap_{j=1}^r \operatorname{dom}(h_{j})$$.

* $$f$$ được gọi là **hàm tiêu chí** hoặc **hàm mục tiêu** (objective function).
* $$g_{i}(x)$$ được gọi là **hàm ràng buộc bất đẳng thức** (inequality constraint function).
* $$h_{j}(x)$$ được gọi là **hàm ràng buộc đẳng thức** (equality constraint function).
* Nếu $$x \in D$$ thỏa mãn $$g_{i}(x) \leq 0$$ với mọi $$i$$ và $$h_{j}(x) = 0$$ với mọi $$j$$, thì $$x$$ được gọi là một **điểm khả thi** (feasible point).
* Trên tập tất cả các điểm khả thi $$x$$, giá trị nhỏ nhất của $$f(x)$$ được gọi là **giá trị tối ưu** (optimal value), ký hiệu là $$f^{\star}$$.
* Nếu $$x$$ khả thi và $$f(x) = f^{\star}$$, thì $$x$$ được gọi là **điểm tối ưu**, **nghiệm tối ưu**, hoặc **điểm cực tiểu** (minimizer).
* Nếu $$x$$ khả thi và $$f(x) \le f^{\star} + \epsilon$$ (với $$\epsilon > 0$$), thì $$x$$ được gọi là điểm **$$\epsilon$$-cận tối ưu** ($$\epsilon$$-suboptimal).
* Nếu $$x$$ khả thi và $$g_i(x) = 0$$, ta nói ràng buộc $$g_i$$ là **ràng buộc tích cực** (hay *hoạt động*, active constraint) tại $$x$$.
* Mọi bài toán cực tiểu hóa lồi đều có thể chuyển tương đương thành một bài toán cực đại hóa lõm:

>$$
\begin{aligned}
&\text{maximize}_{x \in D} &&-f(x)\\
&\text{subject to} &&g_{i}(x) \leq 0, \quad i = 1, \dotsc, m\\
&&&h_{j}(x) = 0, \quad j = 1, \dotsc, r,\\\\
\end{aligned}
$$

>trong đó $$f$$ và $$g_{i}$$ ($$i=1,\dotsc, m$$) đều là các hàm lồi, $$h_j$$ ($$j = 1, \dotsc, r$$) đều là các hàm affine, và miền xác định của bài toán là $$D = \operatorname{dom}(f) \cap \bigcap_{i=1}^{m} \operatorname{dom}(g_{i}) \cap \bigcap_{j=1}^r \operatorname{dom}(h_{j})$$.

### Tập khả thi

Tập khả thi (còn gọi là miền khả thi hoặc không gian nghiệm khả thi) là tập hợp tất cả các điểm khả thi, biểu diễn toàn bộ các phương án thỏa mãn đồng thời mọi ràng buộc của bài toán.

Tập khả thi, thường ký hiệu là $$S$$ hoặc $$\mathcal{F}$$, được định nghĩa như sau:

> $$ S = \{ \mathbf{x} \in X \mid g_i(\mathbf{x}) \le 0 \text{ với mọi } i=1, \dots, m, \text{ và } h_j(\mathbf{x}) = 0 \text{ với mọi } j=1, \dots, r \} $$

### Tính chất của tập khả thi

1. **Tính lồi:** Nếu tất cả các hàm ràng buộc bất đẳng thức $$g_i(\mathbf{x})$$ đều lồi và tất cả các hàm ràng buộc đẳng thức $$h_j(\mathbf{x})$$ đều affine, thì tập khả thi $$S$$ là một **tập lồi**. Đây là tính chất nền tảng của tối ưu hóa lồi, góp phần đảm bảo mọi cực tiểu địa phương cũng là cực tiểu toàn cục.
2. **Tính bị chặn:** Một tập khả thi có thể **bị chặn** (nằm gọn trong một vùng hữu hạn) hoặc **không bị chặn** (trải dài vô hạn theo ít nhất một hướng).
3. **Tập rỗng:** Tập khả thi có thể rỗng ($$S = \emptyset$$), nghĩa là không tồn tại điểm nào thỏa mãn đồng thời mọi ràng buộc. Khi đó, bài toán tối ưu hóa được gọi là **không khả thi** (infeasible).
4. **Đa diện lồi bị chặn và tập đa diện (Polytope / Polyhedron):** Trong quy hoạch tuyến tính, tập khả thi khác rỗng và bị chặn được gọi là **đa diện lồi bị chặn** (polytope). Nếu tập khả thi khác rỗng nhưng có thể không bị chặn, nó được gọi là **tập đa diện** (polyhedron). Cả hai đều là tập lồi.
5. **Đỉnh (điểm cực biên):** Đối với bài toán quy hoạch tuyến tính, nếu tồn tại nghiệm tối ưu (và tập khả thi không chứa đường thẳng), thì luôn tồn tại ít nhất một nghiệm tối ưu nằm tại một đỉnh (còn gọi là điểm cực biên) của tập khả thi. Tính chất này là cơ sở của các thuật toán duyệt đỉnh như phương pháp đơn hình (Simplex).
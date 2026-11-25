---
layout: post
title: 11-03 Bài toán đối ngẫu Lagrange
chapter: '11'
order: 4
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

Sau khi đã có trong tay hàm đối ngẫu $$g(u, v)$$ — cỗ máy sản xuất vô số cận dưới $$g(u, v) \le f^*$$ — câu hỏi tiếp theo gần như tự bật ra: *trong tất cả các cận dưới ấy, cận dưới nào là **tốt nhất (lớn nhất)**?* Để tìm nó, ta chỉ việc cực đại hóa $$g(u, v)$$ theo $$u \ge 0$$ và $$v \in \mathbb{R}^r$$. Đó chính xác là **bài toán đối ngẫu Lagrange**!

Điều kỳ diệu biến bài toán đối ngẫu thành vũ khí hạng nặng trong tối ưu hóa không lồi (như quy hoạch nguyên, bài toán phân cụm, hay hàm bậc bốn đa đỉnh trong bài học này) là: dù bài toán gốc không lồi và đầy rẫy cực tiểu địa phương, **bài toán đối ngẫu Lagrange luôn là một bài toán tối ưu lồi** (cực đại hóa hàm lõm trên miền lồi $$u \ge 0$$)! Nhờ vậy, ta luôn có thể giải bài toán đối ngẫu tới tối ưu toàn cục $$g^*$$ một cách đáng tin cậy để lấy cận dưới chặt nhất cho $$f^*$$.

## Bản đồ kiến thức nền: Ba trụ cột của bài toán đối ngẫu Lagrange

- **Phát biểu chuẩn của bài toán đối ngẫu:**
  $$\max_{u, v} \; g(u, v) \quad \text{s.t.} \quad u \ge 0 \quad (\text{và ẩn ý } (u, v) \in \operatorname{dom} g).$$
  Tối ưu hóa bài toán này cho ta giá trị đối ngẫu tối ưu $$g^* = d^*$$, luôn thỏa **đối ngẫu yếu** $$g^* \le f^*$$.
- **Tính lồi tuyệt đối của bài toán đối ngẫu:** Vì $$g(u, v)$$ lõm nên $$-g(u, v)$$ lồi, và tập ràng buộc $$u \ge 0$$ (cùng miền hữu dụng $$\operatorname{dom} g$$) là tập lồi. Do đó, mọi thuật toán tối ưu lồi (như subgradient, proximal, điểm trong) đều áp dụng được trực tiếp lên bài toán đối ngẫu!
- **Chuyển ràng buộc ẩn thành ràng buộc tường minh:** Khi viết bài toán đối ngẫu trên giấy, ta thường đưa các điều kiện làm cho $$g(u, v) > -\infty$$ (như $$-A^T u - G^T v = c$$ trong LP hay $$p \in \operatorname{col}(Q)$$ trong QP) ra làm ràng buộc tường minh để dễ giải và dễ nhìn.

### Khung giải thích (nên đọc chậm): Giải tay bài toán đối ngẫu cho một bài toán gốc *không lồi*

Xét bài toán không lồi 1 biến (vì miền khả thi là hai điểm rời rạc $$x = \pm 1$$):
$$\min_{x \in \mathbb{R}} \; f(x) = x \quad \text{s.t.} \quad l(x) = x^2 - 1 = 0.$$
Dễ thấy miền khả thi chỉ gồm $$x = -1$$ và $$x = 1$$, nên giá trị tối ưu gốc là $$f^* = -1$$ (tại $$x^* = -1$$).

1. **Lập hàm Lagrangian và tìm hàm đối ngẫu $$g(v)$$ ($$v \in \mathbb{R}$$):**
   $$L(x, v) = x + v(x^2 - 1) = v x^2 + x - v.$$
   - Nếu $$v \le 0$$: đồ thị là đường thẳng hoặc parabol úp xuống, nên $$\inf_x L(x, v) = -\infty$$!
   - Nếu $$v > 0$$: parabol ngửa lên, đạt cực tiểu tại $$2vx + 1 = 0 \implies x = -\frac{1}{2v}$$. Thay vào:
     $$g(v) = v\left(\frac{1}{4v^2}\right) - \frac{1}{2v} - v = -\frac{1}{4v} - v.$$
2. **Giải bài toán đối ngẫu (hoàn toàn lồi!):**
   $$\max_{v > 0} \; g(v) = -\frac{1}{4v} - v.$$
   Kiểm tra tính lõm: $$g''(v) = -\frac{1}{2v^3} < 0$$ với mọi $$v > 0$$!
   Cho đạo hàm $$g'(v) = \frac{1}{4v^2} - 1 = 0 \implies v^* = \frac{1}{2} > 0$$.
3. **So sánh $$g^*$$ và $$f^*$$:**
   $$g^* = g\left(\frac{1}{2}\right) = -\frac{1}{2} - \frac{1}{2} = -1 = f^*!$$
   Dù bài toán gốc không lồi (hai điểm rời rạc!), bài toán đối ngẫu lại trơn, lõm, và trong ví dụ đặc biệt này thậm chí đạt $$g^* = f^*$$ (trong khi với nhiều bài toán không lồi khác như hàm bậc bốn ở phần thân bài, ta sẽ gặp $$g^* < f^*$$).

Xét bài toán tối ưu tổng quát sau:

>
$$
\begin{alignat}{1}
\min_x & \quad f(x)  \\
s.t.   & \quad h_i(x) \leq 0, i=1,\dots,m  \\
       & \quad l_j(x) = 0, j=1,\dots,r
\end{alignat}
$$

Hàm đối ngẫu $$g(u,v)$$ thỏa mãn $$f^* \geq g(u,v)$$ với mọi $$u \geq 0$$ và $$v$$. Để tìm cận dưới chặt nhất có thể cho $$f^*$$, ta cực đại hóa $$g(u,v)$$ trên miền $$u \geq 0$$. Bài toán thu được gọi là **bài toán đối ngẫu Lagrange**:

>
$$
\begin{alignat}{1}
\max_{u,v} & \quad g(u,v)   \\
           s.t. & \quad u \geq 0
\end{alignat}
$$

Ký hiệu giá trị tối ưu của bài toán đối ngẫu là $$g^*$$, khi đó ta luôn có $$f^* \geq g^*$$. Tính chất này được gọi là **tính đối ngẫu yếu (weak duality)** và luôn đúng bất kể bài toán gốc có lồi hay không. Hơn nữa, **bài toán đối ngẫu luôn là một bài toán tối ưu lồi**, ngay cả khi bài toán gốc không lồi.

Thật vậy, theo định nghĩa, $$g(u,v)$$ là hàm lõm theo $$(u,v)$$ và ràng buộc $$u \geq 0$$ xác định một tập lồi, nên bài toán đối ngẫu là bài toán cực đại hóa một hàm lõm trên một tập lồi:

>
$$
\begin{alignat}{1}
 g(u,v) & = \min_x \{ f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x) \}  \\ 
        & = - \underbrace{\max_x \{ -f(x) - \sum_{i=1}^m u_i h_i(x) - \sum_{j=1}^r v_j l_j(x) \}}_{\text{pointwise maximum of convex functions in $(u,v)$}}
\end{alignat}
$$

## Ví dụ: Cực tiểu hóa hàm bậc bốn không lồi

Xét bài toán cực tiểu hóa hàm không lồi $$f(x) = x^4 - 50x^2 + 100x$$ với ràng buộc $$x \geq -4.5$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter11/dual-gen_13.png" width="70%">
  <figcaption style="text-align: center;">[Hình 4] Ví dụ về tối thiểu hóa hàm bậc bốn không lồi</figcaption>
</p>
</figure>

Trong ví dụ này, hàm đối ngẫu $$g(u)$$ có biểu thức phức tạp:

>
$$
\begin{equation}
 g(u) = \min_{i=1,2,3} \{F_i^4(u) - 50 F_i^2(u) + 100 F_i(u) \}
\end{equation}
$$

trong đó, với $$i = 1, 2, 3$$:

>
$$
\begin{alignat}{1}
F_i(u) = & \frac{- a_i}{12\cdot 2^{1/3}} \left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3} \\ 
           & - 100 \cdot 2^{1/3} \frac{1}{\left( 432(100-u)-(432^2(100-u)^2 - 4\cdot 1200^3)^{1/2} \right )^{1/3}}
\end{alignat}
$$

và $$a_1 = 1$$, $$a_2 = (-1 + i\sqrt{3})/2$$, $$a_3 = (-1 - i\sqrt{3})/2$$.

Nếu chỉ nhìn vào công thức giải tích trên thì rất khó kiểm tra trực tiếp tính lõm của $$g$$; tuy nhiên, theo tính chất tổng quát của hàm đối ngẫu Lagrange, ta biết chắc chắn rằng $$g(u)$$ là một hàm lõm.

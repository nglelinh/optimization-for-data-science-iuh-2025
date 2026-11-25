---
layout: post
title: 11 Tính đối ngẫu trong chương trình tổng quát
chapter: '11'
order: 1
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

Ở Chương 10, tính đối ngẫu trong quy hoạch tuyến tính hiện lên đẹp như một bộ máy đồng hồ Thụy Sĩ: mọi hàm đều thẳng tắp, mọi ràng buộc đều phẳng lì, và chỉ cần nhân tổ hợp tuyến tính là ta có ngay bài toán đối ngẫu khớp chặt $$p^* = d^*$$. Nhưng bước ra ngoài thế giới thực — từ huấn luyện máy vector hỗ trợ (SVM) bậc hai, phân bổ công suất truyền thông logarit, đến tối ưu bền vững theo phân phối (DRO) — hàm mục tiêu và ràng buộc không còn tuyến tính nữa. Liệu phép màu đối ngẫu có sụp đổ khi đường thẳng uốn cong thành parabol, logarit hay thậm chí là những hàm không lồi gồ ghề?

Chương 11 trả lời câu hỏi đó bằng một trong những khung lý thuyết vĩ đại nhất của giải tích hiện đại: **tính đối ngẫu Lagrange (Lagrange Duality)**. Bằng cách đưa mọi ràng buộc vào hàm mục tiêu qua **hàm Lagrangian** $$L(x, u, v)$$ rồi cực tiểu hóa tự do theo $$x$$, ta không những mở rộng trọn vẹn đối ngẫu LP sang *mọi* bài toán tối ưu tổng quát (kể cả không lồi!), mà còn phát hiện ra một sự thật phi thường: **bài toán đối ngẫu Lagrange luôn là bài toán tối ưu lồi**, bất kể bài toán gốc có rối rắm hay không lồi đến đâu!

## Kiến thức cần nhớ: Bốn trụ cột của tính đối ngẫu trong bài toán tổng quát

- **Từ đối ngẫu LP đến hàm Lagrangian tổng quát:** Thay vì chỉ dùng phép tổ hợp tuyến tính cho $$Ax = b, Gx \le h$$, hàm Lagrangian $$L(x, u, v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)$$ áp dụng cho mọi hàm mục tiêu $$f$$ và ràng buộc phi tuyến $$h_i, l_j$$.
- **Hàm đối ngẫu Lagrange $$g(u, v) = \inf_x L(x, u, v)$$ luôn lõm:** Vì $$g(u, v)$$ là infimum theo từng điểm của một họ các hàm *affine* theo $$(u, v)$$, nó luôn là hàm lõm! Nhờ đó bài toán đối ngẫu $$\max_{u \ge 0, v} g(u, v)$$ luôn là bài toán tối ưu lồi.
- **Đối ngẫu yếu (luôn đúng) vs. Đối ngẫu mạnh (cần điều kiện Slater):** Ta luôn có $$d^* \le p^*$$ cho mọi bài toán tối ưu (kể cả không lồi). Với bài toán gốc lồi, chỉ cần tồn tại một điểm khả thi chặt (điều kiện Slater), khoảng cách đối ngẫu bằng đúng $$0$$ ($$d^* = p^*$$).
- **Khoảng cách đối ngẫu và đối ngẫu kép:** Hiệu $$f(x) - g(u, v)$$ vừa là thước đo chất lượng nghiệm trực tuyến để dừng thuật toán, vừa mở đường dẫn sang hệ điều kiện tối ưu KKT ở Chương 12.

### Giải thích: Bước nhảy từ LP sang bài toán bậc hai qua hàm Lagrangian

Xét bài toán phi tuyến đơn giản nhất:
$$\min_{x \in \mathbb{R}} \; f(x) = x^2 \quad \text{s.t.} \quad h(x) = 2 - x \le 0 \; (\text{tức } x \ge 2).$$
Rõ ràng nghiệm gốc là $$x^* = 2$$ với $$p^* = 4$$.

1. **Lập hàm Lagrangian (nhân tử $$u \ge 0$$):**
   $$L(x, u) = x^2 + u(2 - x) = x^2 - ux + 2u.$$
2. **Tìm hàm đối ngẫu $$g(u) = \min_{x \in \mathbb{R}} L(x, u)$$:**
   Lấy đạo hàm theo $$x$$ bằng $$0$$: $$2x - u = 0 \implies x(u) = \frac{u}{2}$$.
   Thay lại vào $$L$$:
   $$g(u) = \left(\frac{u}{2}\right)^2 - u\left(\frac{u}{2}\right) + 2u = 2u - \frac{u^2}{4}.$$
   Chú ý: dù $$f(x) = x^2$$ là hàm lồi, $$g(u) = 2u - \frac{u^2}{4}$$ là một parabol úp ngược (**hàm lõm**!).
3. **Giải bài toán đối ngẫu $$\max_{u \ge 0} \left(2u - \frac{u^2}{4}\right)$$:**
   Đạo hàm $$g'(u) = 2 - \frac{u}{2} = 0 \implies u^* = 4 \ge 0$$.
   Giá trị đối ngẫu tối ưu: $$d^* = g(4) = 2(4) - \frac{16}{4} = 4 = p^*$$! Không cần bất kỳ ràng buộc tuyến tính nào, cỗ máy Lagrange vẫn bắt chính xác đáy $$4$$.

### Ôn tập: Tính đối ngẫu trong quy hoạch tuyến tính

Cho $$c \in \mathbb{R}^n$$, $$A \in \mathbb{R}^{m \times n}$$, $$b \in \mathbb{R}^m$$, $$G \in \mathbb{R}^{r \times n}$$, $$h \in \mathbb{R}^r$$.

#### Bài toán gốc (Primal LP)
>
$$
\begin{alignat}{1}
\min_{x} & \quad c^T x   \\\\ 
  s.t.   & \quad Ax = b  \\\\
         & \quad Gx \leq h 
\end{alignat}
$$

#### Bài toán đối ngẫu (Dual LP)
>
$$
\begin{alignat}{1}
\max_{u,v} & \quad -b^T u - h^T v   \\\\
         s.t. & \quad - A^T u - G^T v = c  \\\\
             & \quad v \geq 0 
\end{alignat}
$$

### Cách giải thích 1

Với mọi $$u$$, mọi $$v \geq 0$$ và mọi $$x$$ khả thi của bài toán gốc, ta có:

>
$$
\begin{equation}
u^T (Ax-b) + v^T(Gx-h) \leq 0
\end{equation}
$$

Biến đổi bất đẳng thức này, ta thu được:

>
$$
\begin{equation}
(-A^Tu - G^Tv)^T x \geq -b^Tu - h^T v
\end{equation}
$$

Do đó, nếu $$c = -A^Tu - G^Tv$$, thì $$-b^Tu - h^Tv$$ là một cận dưới cho giá trị tối ưu của bài toán gốc.

### Cách giải thích 2

Với mọi $$u$$, mọi $$v \geq 0$$ và mọi $$x$$ khả thi của bài toán gốc, ta có:

>
$$
\begin{equation}
c^T x \geq c^T x + u^T (Ax-b) + v^T (Gx -h) := L(x,u,v)
\end{equation}
$$

Gọi $$C$$ là tập khả thi của bài toán gốc và $$f^*$$ là giá trị tối ưu gốc, khi đó:

>
$$
\begin{equation}
f^* \geq \min_{x \in C} L(x,u,v) \geq \min_x L(x,u,v) := g(u,v)
\end{equation}
$$

Nói cách khác, $$g(u,v)$$ luôn là một cận dưới của $$f^*$$, với biểu thức tường minh:

>
$$
g(u,v) =
\begin{cases}
-b^T u - h^T v & \text{nếu $c=-A^Tu - G^T v$} \\\\
-\infty            & \text{trường hợp khác} 
\end{cases}
$$

Cách giải thích thứ hai cho ra cùng bài toán đối ngẫu như cách thứ nhất, nhưng hoàn toàn tổng quát và áp dụng được cho mọi bài toán tối ưu bất kỳ (kể cả các bài toán không lồi).

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm trình bày cách sử dụng đối ngẫu Lagrange như tín hiệu huấn luyện hoặc chứng chỉ trong tối ưu bền vững theo phân phối (DRO), mạng nơ-ron giải AC-OPF (DC3 / OPF-DNN), phương pháp quy giảm công bằng của Fairlearn và SVM nhân (kernel SVM). Xem [11-08 Ứng dụng hiện đại của đối ngẫu Lagrange]({% multilang_post_url contents/chapter11/2026-09-16-11_08_modern_applications %}).

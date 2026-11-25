---
layout: post
title: 24-04 Nới Lỏng
chapter: '24'
order: 5
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

Nếu ví quy hoạch nguyên như một khối đá gồ ghề khó đẽo, thì **phép nới lỏng (relaxation)** là nghệ thuật đặt khối đá đó vào bên trong một chiếc hộp lồi trơn tru hơn để ước lượng nhanh đáy thấp nhất của nó. Một phép nới lỏng tốt phải đi trên sợi dây cân bằng tinh tế giữa hai yêu cầu ngược chiều: **đủ dễ để giải thật nhanh**, nhưng cũng **đủ chặt để cận dưới nằm thật sát nghiệm nguyên thật**.

Trong bài học này, ta đối chiếu hai vũ khí tạo cận dưới quan trọng nhất của tối ưu rời rạc: **nới lỏng lồi** (bỏ trực tiếp ràng buộc nguyên) và **nới lỏng Lagrange** (giữ nguyên ràng buộc nguyên nhưng đưa các ràng buộc khó lên hàm mục tiêu kèm nhân tử phạt $$\lambda$$).

## Bản đồ kiến thức nền: Ba trụ cột của lý thuyết Nới lỏng

Để chọn đúng phép nới lỏng cho từng cấu trúc bài toán, hãy nắm chắc ba trụ cột sau:

- **Hai điều kiện vàng của một phép nới lỏng:** Bài toán $$\min_{x \in Y} g(x)$$ là nới lỏng của $$\min_{x \in X} f(x)$$ khi và chỉ khi (1) mở rộng tập khả thi $$X \subseteq Y$$, và (2) đánh giá thấp hàm mục tiêu $$g(x) \le f(x)$$ trên mọi $$x \in X$$. Hai điều kiện đơn giản này bảo đảm ngay lập tức $$\min_{Y} g \le \min_{X} f$$.
- **Nới lỏng lồi (Convex / LP Relaxation):** Cách tự nhiên nhất là xóa bỏ điều kiện $$x_j \in \mathbb{Z}$$ (giữ nguyên $$x \in C$$). Nó luôn giải được trong thời gian đa thức, nhưng chất lượng cận dưới phụ thuộc cực mạnh vào cách ta *viết* các ràng buộc của $$C$$ (ví dụ ràng buộc rời rạc $$x_{ij} \le y_j$$ cho cận chặt hơn hẳn ràng buộc gộp).
- **Nới lỏng Lagrange (Lagrangian Relaxation) và Bài toán đối ngẫu Lagrange:** Khi bài toán gồm các ràng buộc "dễ" (cho phép tách biến hoặc giải nhanh trên tập nguyên) trộn với vài ràng buộc "khó" $$Ax \le b$$, ta đưa $$Ax - b$$ lên hàm mục tiêu với nhân tử $$\lambda \ge 0$$. Tối đa hóa hàm đối ngẫu $$g(\lambda)$$ cho ra cận dưới **luôn bằng hoặc chặt hơn** nới lỏng LP tiêu chuẩn!

### Khung giải thích (nên đọc chậm): Tính tay Nới lỏng Lagrange và đối chiếu với Nới lỏng LP

Xét bài toán quy hoạch nguyên 0–1 cực tiểu hóa:

$$
z^\star = \min_{x_1, x_2 \in \{0, 1\}}\ 2x_1 + 5x_2 \qquad \text{thỏa mãn } x_1 + 2x_2 \ge 2.
$$

Quan sát nhanh: chỉ có hai nghiệm nguyên khả thi là $$(0, 1)$$ (giá trị $$5$$) và $$(1, 1)$$ (giá trị $$7$$), nên nghiệm đúng là $$z^\star = 5$$.

1. **Tính cận dưới bằng nới lỏng LP (cho $$x_1, x_2 \in [0, 1]$$):**
   Vì $$x_1$$ có tỷ số chi phí/đóng góp là $$2/1 = 2$$ rẻ hơn $$x_2$$ ($$5/2 = 2.5$$), LP lấy hết $$x_1 = 1$$ rồi bù thêm $$x_2 = 0.5$$ để vừa đủ $$1 + 2(0.5) = 2$$.
   Giá trị LP: $$z_{\text{LP}} = 2(1) + 5(0.5) = 4.5 \le 5$$.
2. **Tính cận dưới bằng nới lỏng Lagrange:**
   Ta giữ nguyên tập nguyên $$x_1, x_2 \in \{0, 1\}$$ và đưa ràng buộc $$2 - x_1 - 2x_2 \le 0$$ lên hàm mục tiêu với nhân tử $$\lambda \ge 0$$:
   $$L(x, \lambda) = 2x_1 + 5x_2 + \lambda(2 - x_1 - 2x_2) = 2\lambda + (2 - \lambda)x_1 + (5 - 2\lambda)x_2.$$
   Hàm đối ngẫu $$g(\lambda) = \min_{x_1, x_2 \in \{0, 1\}} L(x, \lambda)$$ **tách rời hoàn toàn** thành 2 quyết định độc lập (chọn $$x_i = 1$$ nếu hệ số âm, chọn $$0$$ nếu hệ số dương):
   $$g(\lambda) = 2\lambda + \min(0,\; 2 - \lambda) + \min(0,\; 5 - 2\lambda).$$
3. **Thử các giá trị $$\lambda$$ để tìm cận dưới tốt nhất:**
   - Tại $$\lambda = 2$$: $$g(2) = 4 + 0 + 0 = 4$$.
   - Tại $$\lambda = 2.5$$: $$g(2.5) = 5 + \min(0, -0.5) + \min(0, 0) = 5 - 0.5 = 4.5$$.
   - Tại $$\lambda = 3$$: $$g(3) = 6 + (-1) + (-1) = 4$$.
   Giá trị đối ngẫu Lagrange cực đại đạt $$4.5$$ tại $$\lambda^\star = 2.5$$ — minh họa rõ cả tính tách biến tuyệt đẹp lẫn cơ chế cực đại hóa hàm lõm từng khúc $$g(\lambda)$$!

Mục này trình bày định nghĩa tổng quát của phép nới lỏng (relaxation) cùng hai phương pháp phổ biến để tạo cận dưới cho quy hoạch nguyên: nới lỏng lồi (convex relaxation) và nới lỏng Lagrange (Lagrangian relaxation).

## Điều kiện của phép nới lỏng

Xét bài toán tối ưu gốc:
> $$\min_{x \in X} f(x)$$

Một bài toán tối ưu khác có dạng sau được gọi là một *nới lỏng* của bài toán gốc:

> $$\begin{align}
> &\min_{x \in Y} \: g(x)\\\\
> &\text{sao cho}\\\\
> &\text{① } X \subseteq Y \quad \text{và}\\\\ 
> &\text{② } g(x) \leq f(x) \text{ với mọi } x \in X 
> \end{align}$$ 

Nếu hàm mục tiêu $$g(x)$$ trùng với $$f(x)$$ thì chỉ cần thỏa mãn điều kiện ①; nếu $$g(x)$$ khác $$f(x)$$ thì phải thỏa mãn cả hai điều kiện. Từ hai điều kiện này, giá trị tối ưu của bài toán nới lỏng luôn là một cận dưới của giá trị tối ưu của bài toán gốc.

## Nới lỏng lồi

Với bài toán quy hoạch nguyên hỗn hợp:
> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } && x \in C \\\\
> &&&x_j \in \mathbb{Z}, \quad j \in J
> \end{align} $$
> $$\begin{align}
> \text{trong đó } f \text{ lồi, } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n 
> \quad \text{và} \quad J \subseteq \lbrace 1, \dotsc, n \rbrace
> \end{align}
> $$

bài toán nới lỏng lồi thu được bằng cách bỏ các ràng buộc nguyên $$x_j \in \mathbb{Z}$$:
> $$
> \begin{align}
> &\min_{x} && f(x) \\\\
> &\text{subject to } && x \in C
> \end{align} $$
> $$\begin{align}
> \text{trong đó } f \text{ lồi, } f: \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n.
> \end{align}
> $$

## Nới lỏng Lagrange

Xét bài toán có thêm ràng buộc tuyến tính $$Ax \leq b$$ bên cạnh tập ràng buộc $$X$$ (có thể chứa cả các ràng buộc nguyên):

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } &&Ax \leq b \\\\
> &&& x_{j} \in \mathbb{Z}, \quad x \in X 
> \end{align}
> $$

Đưa ràng buộc $$Ax \leq b$$ lên hàm mục tiêu với nhân tử Lagrange $$u \geq 0$$, ta thu được hàm đối ngẫu Lagrange:

> $$
> \begin{align}
> L(u) = &\min_{x} &&f(x) + u^{\top}(Ax-b) \\\\
> &\text{subject to } &&x \in X
> \end{align}
> $$

Phép nới lỏng này mở rộng tập khả thi, và với mọi $$x$$ thỏa mãn $$Ax \leq b$$ cùng $$u \geq 0$$, ta luôn có $$f(x) + u^{\top}(Ax - b) \leq f(x)$$. Vì vậy $$L(u)$$ là một cận dưới hợp lệ với mọi $$u \geq 0$$. Cận dưới chặt nhất thu được bằng cách giải bài toán đối ngẫu Lagrange $$\max_{u \geq 0} L(u)$$. Do $$L(u)$$ là cận dưới theo từng điểm của một họ hàm affine theo $$u$$, $$L(u)$$ luôn là hàm lõm, nên bài toán đối ngẫu là bài toán cực đại hóa hàm lõm (tương đương tối ưu lồi).

Áp dụng nới lỏng Lagrange cho bài toán đặt cơ sở ở mục 24-02 bằng cách nới lỏng ràng buộc đẳng thức $$\sum_j x_{ij} = 1$$ với nhân tử không ràng buộc dấu $$v$$:

> $$
> \begin{align}
> L(v) = &\min_{x, y} && \sum_{j = 1}^{n} f_{j}y_{j} + \sum_{i = 1}^{m}\sum_{j = 1}^{n}(c_{ij} - v_{i})x_{ij} + \sum_{i = 1}^{m} v_{i} \\\\
> &\text{subject to } && x_{ij} \leq y_{j}, \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n \\\\
> &&& x_{ij}, y_{j} \in \lbrace 0, 1 \rbrace, \quad i = 1, \dotsc, m, \quad j = 1, \dotsc, n 
> \end{align}
> $$

Với mỗi vector $$v$$ cố định, bài toán con $$L(v)$$ có nghiệm dạng đóng rất dễ tính:
> $$ x_{ij}(v) =\begin{cases}1 & \text{nếu } c_{ij} - v_{i} < 0 \text{ và } \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
> 0 & \text{ngược lại,} \end{cases}$$
> $$ y_{j}(v) =\begin{cases}1 & \text{nếu } \sum_{l} (c_{lj} - v_{l})^{-} + f_{j} < 0 \\\\
> 0 & \text{ngược lại.} \end{cases} $$

Cách giải này vừa cung cấp cận dưới $$L(v)$$ vừa gợi ý nghiệm gốc heuristic. Để tìm cận dưới tốt nhất, ta có thể chuyển $$\max_{v} L(v)$$ thành $$\min_{v} -L(v)$$ và giải bằng phương pháp dưới đạo hàm (subgradient method).

---
layout: post
title: 04-06 Loại bỏ ràng buộc đẳng thức
chapter: '04'
order: 7
owner: YoungJae Choung
categories:
- chapter04
lang: vi
---

Giả sử bạn phải tìm vị trí thấp nhất của một thung lũng trong không gian 3 chiều, nhưng bị buộc phải đi dọc theo một con đường thẳng cắt ngang thung lũng đó. Bạn có cần mang theo cả bản đồ 3D phức tạp không? Hoàn toàn không! Vì mọi vị trí trên con đường thẳng chỉ cần đúng **một tọa độ duy nhất** (số mét tính từ điểm xuất phát) để xác định.

Đó chính là tinh thần của kỹ thuật **loại bỏ ràng buộc đẳng thức tuyến tính** $$Ax = b$$. Thay vì mang gánh nặng các phương trình ràng buộc vào thuật toán giải, ta tham số hóa toàn bộ tập nghiệm của $$Ax = b$$ dưới dạng $$x = Fz + x_0$$, biến bài toán có ràng buộc đẳng thức thành bài toán nhỏ gọn hơn theo biến tự do $$z$$ mà vẫn giữ nguyên vẹn tính lồi.

## Kiến thức cần nhớ: Đại số tuyến tính đằng sau việc khử $$Ax = b$$

Để thực hiện phép khử này chính xác và biết khi nào *nên* hay *không nên* dùng nó trong thực tế, hãy nắm ba trụ cột:

- **Cấu trúc không gian nghiệm của hệ tuyến tính (Affine Subspace Parametrization):** Tập nghiệm của $$Ax = b$$ (nếu khác rỗng) luôn có dạng $$x_0 + \operatorname{null}(A)$$, trong đó $$x_0$$ là một nghiệm riêng bất kỳ ($$Ax_0 = b$$) và các cột của ma trận $$F$$ tạo thành cơ sở của không gian hạt nhân $$\operatorname{null}(A)$$ (tức $$AF = 0$$).
- **Bảo toàn tính lồi dưới hợp thành affine (Affine Composition):** Khi thay $$x = Fz + x_0$$ vào hàm mục tiêu $$f(x)$$ và ràng buộc bất đẳng thức $$g_i(x)$$, ta thu được $$\tilde{f}(z) = f(Fz + x_0)$$ và $$\tilde{g}_i(z) = g_i(Fz + x_0)$$. Vì hợp thành của hàm lồi với ánh xạ affine luôn lồi, bài toán mới chắc chắn vẫn là bài toán tối ưu hóa lồi!
- **Đánh đổi tính toán: Kích thước vs. Độ thưa (Sparsity Trade-off):** Khử ràng buộc đẳng thức giúp giảm số chiều biến từ $$n$$ xuống $$n - \operatorname{rank}(A)$$, cực kỳ hiệu quả với bài toán cỡ vừa. Tuy nhiên, với bài toán cực lớn có ma trận $$A$$ thưa, ma trận $$F$$ thường bị **dày đặc (dense)**, nên các bộ giải lớn thường giữ nguyên $$Ax = b$$ và giải hệ KKT thưa thay vì khử trực tiếp.

### Giải thích: Khử ràng buộc đẳng thức và giải tay bài toán 3 biến về 1 biến

Xét bài toán tối ưu lồi trong $$\mathbb{R}^3$$:
$$\min_{x \in \mathbb{R}^3} \; f(x) = x_1^2 + 2x_2^2 + x_3^2 \quad \text{thỏa mãn} \quad \begin{cases} x_1 + x_2 + x_3 = 3 \\ x_1 - x_3 = 1 \end{cases}$$

1. **Bước 1 — Tìm một nghiệm riêng $$x_0$$:**
   Chọn thử $$x_3 = 0 \implies x_1 = 1$$, từ phương trình đầu suy ra $$x_2 = 2$$. Vậy $$x_0 = (1, 2, 0)^T$$ thỏa mãn hệ $$Ax = b$$.
2. **Bước 2 — Tìm cơ sở $$F$$ của không gian hạt nhân $$Av = 0$$:**
   Hệ thuần nhất: $$v_1 + v_2 + v_3 = 0$$ và $$v_1 - v_3 = 0 \implies v_1 = v_3$$ và $$v_2 = -2v_3$$.
   Chọn $$v_3 = 1$$ ta được vector cơ sở duy nhất $$F = (1, -2, 1)^T$$.
3. **Bước 3 — Tham số hóa $$x = Fz + x_0$$ (với $$z \in \mathbb{R}$$):**
   $$x_1 = 1 + z, \qquad x_2 = 2 - 2z, \qquad x_3 = z.$$
   Kiểm tra nhanh: $$x_1 + x_2 + x_3 = (1+z) + (2-2z) + z = 3$$ và $$x_1 - x_3 = 1$$ đúng với mọi $$z \in \mathbb{R}$$!
4. **Bước 4 — Giải bài toán không ràng buộc 1 biến theo $$z$$:**
   $$\tilde{f}(z) = (1 + z)^2 + 2(2 - 2z)^2 + z^2 = (1 + 2z + z^2) + 2(4 - 8z + 4z^2) + z^2 = 10z^2 - 14z + 9.$$
   Đạo hàm $$\tilde{f}'(z) = 20z - 14 = 0 \implies z^\star = 0.7$$.
5. **Bước 5 — Khôi phục nghiệm gốc:**
   $$x^\star = F(0.7) + x_0 = (1.7,\; 0.6,\; 0.7)^T, \qquad f^\star = 10(0.49) - 14(0.7) + 9 = 4.1.$$
   Cả hai ràng buộc đẳng thức đều thỏa mãn chính xác ($$1.7+0.6+0.7=3$$, $$1.7-0.7=1$$) mà không cần dùng đến nhân tử Lagrange!

---

Phần này trình bày kỹ thuật loại bỏ các ràng buộc đẳng thức tuyến tính trong bài toán tối ưu hóa lồi nhằm đơn giản hóa tập khả thi hoặc cấu trúc bài toán.

Xét bài toán tối ưu hóa lồi có dạng:

>$$
\begin{aligned}
&\min_{x} &&f(x)\\
&\text{subject to } &&g_{i}(x) \leq 0, \quad i = 1, \dotsc, m\\
&&&{Ax = b}.\\
\end{aligned}
$$

Giả sử $$x_{0}$$ là một nghiệm riêng bất kỳ thỏa mãn $$Ax_{0} = b$$ và $$M$$ là ma trận sao cho không gian cột của nó trùng với không gian hạch của $$A$$, tức là $$\text{col}(M) = \text{null}(A)$$. Khi đó, mọi điểm $$x$$ thỏa mãn ràng buộc đẳng thức $$Ax = b$$ đều có thể biểu diễn dưới dạng:
>$$x = My + x_{0}$$

Thật vậy, $$Ax = A(My + x_{0}) = AMy + Ax_{0} = 0 + b = b$$. Do đó, bằng cách thay thế $$x = My + x_{0}$$ vào bài toán gốc, ta loại bỏ hoàn toàn ràng buộc đẳng thức và thu được bài toán tương đương:

>$$
\begin{aligned}
&\min_y &&f(My+x_0)\\
&\text{subject to} &&g_{i}(My+x_{0}) \leq 0, \quad i = 1, \dotsc, m.\\
\end{aligned}
$$

Tuy nhiên, trong thực tế cần cân nhắc kỹ trước khi áp dụng phương pháp này vì hai hạn chế chính:
1. Việc tìm ma trận $$M$$ (chẳng hạn qua phân tích QR hoặc SVD) thường tốn kém về mặt tính toán khi kích thước bài toán lớn.
2. Nếu ma trận bài toán theo biến gốc $$x$$ có cấu trúc thưa, việc chuyển sang biến $$y$$ qua ma trận dày đặc $$M$$ có thể phá vỡ tính thưa và làm tăng chi phí tính toán.

---
layout: post
title: 13-02 Giải bài toán nguyên thủy thông qua đối ngẫu
chapter: '13'
order: 3
owner: Wontak Ryu
categories:
- chapter13
lang: vi
lesson_type: required
---

Hãy tưởng tượng bạn phải phân bổ ngân sách cho $$n = 10{,}000$$ chiến dịch quảng cáo khác nhau sao cho tổng chi phí đúng bằng một hạn mức $$b$$ cố định, đồng thời cực tiểu hóa tổng hàm tổn thất riêng $$f_i(x_i)$$ của từng chiến dịch. Nếu giải trực tiếp trong không gian nguyên thủy, bạn phải điều phối đồng thời $$10{,}000$$ biến bị trói chặt vào nhau bởi phương trình $$\sum a_i x_i = b$$.

Thế nhưng, khi bước sang không gian đối ngẫu, toàn bộ $$10{,}000$$ biến nguyên thủy đột ngột biến mất, chỉ còn lại **đúng một biến vô hướng $$v$$** — đóng vai trò như "giá bóng" của một đồng ngân sách! Một khi tìm được mức giá cân bằng $$v^\star$$ bằng tìm kiếm nhị phân hay phương pháp Newton 1 chiều, từng chiến dịch $$i$$ chỉ việc tự tối ưu độc lập theo công thức đóng. Đó chính là sức mạnh tách biến kinh điển của việc giải bài toán nguyên thủy thông qua đối ngẫu.

## Bản đồ kiến thức nền: Cơ chế khôi phục nghiệm nguyên thủy từ đối ngẫu

- **Điều kiện dừng KKT và đối ngẫu mạnh:** Khi đối ngẫu mạnh giữ vững, nghiệm nguyên thủy tối ưu $$x^\star$$ bắt buộc phải là một điểm cực tiểu của hàm Lagrange $$L(x, u^\star, v^\star)$$ tại nhân tử tối ưu.
- **Tính duy nhất nhờ lồi chặt (Strict Convexity):** Cần hết sức cẩn thận: nếu $$L(x, u^\star, v^\star)$$ có nhiều điểm cực tiểu (ví dụ khi $$f$$ tuyến tính từng khúc), một điểm cực tiểu tùy ý có thể còn không khả thi cho bài toán gốc! Nhưng khi $$f$$ **lồi chặt**, điểm cực tiểu của $$L(x, u^\star, v^\star)$$ là duy nhất nên chắc chắn trùng khít với $$x^\star$$.
- **Cấu trúc tách biến (Separability):** Khi hàm mục tiêu là tổng $$\sum_{i=1}^n f_i(x_i)$$ và chỉ có ít ràng buộc ghép chung, phép lấy cực tiểu theo $$x$$ tự động rã thành $$n$$ bài toán 1 chiều độc lập, liên kết với nhau qua hàm liên hợp $$f_i^*$$.

### Khung giải thích (nên đọc chậm): Giải bài toán phân bổ 3 biến qua đối ngẫu 1 chiều

Xét bài toán tách biến 3 chiều:

$$\min_{x \in \mathbb{R}^3} \frac{1}{2}x_1^2 + x_2^2 + \frac{3}{2}x_3^2 \qquad \text{với điều kiện } x_1 + x_2 + x_3 = 11.$$

1. **Tính hàm liên hợp của từng thành phần:**
   - Với $$f_1(x_1) = \frac{1}{2}x_1^2$$: $$f_1'(x_1) = x_1 = v \implies x_1 = v$$ và $$f_1^*(v) = \frac{1}{2}v^2$$.
   - Với $$f_2(x_2) = x_2^2$$: $$f_2'(x_2) = 2x_2 = v \implies x_2 = \frac{v}{2}$$ và $$f_2^*(v) = \frac{1}{4}v^2$$.
   - Với $$f_3(x_3) = \frac{3}{2}x_3^2$$: $$f_3'(x_3) = 3x_3 = v \implies x_3 = \frac{v}{3}$$ và $$f_3^*(v) = \frac{1}{6}v^2$$.
2. **Lập bài toán đối ngẫu 1 chiều theo $$v$$:** Theo công thức $$g(v) = bv - \sum_{i=1}^3 f_i^*(a_i v)$$ với $$b = 11, a_i = 1$$:
   $$g(v) = 11v - \left(\frac{1}{2} + \frac{1}{4} + \frac{1}{6}\right)v^2 = 11v - \frac{11}{12}v^2.$$
3. **Giải bài toán đối ngẫu:** Lấy đạo hàm $$g'(v) = 11 - \frac{11}{6}v = 0 \implies v^\star = 6$$. Giá trị đối ngẫu tối ưu là $$g(6) = 66 - \frac{11}{12}(36) = 33$$.
4. **Khôi phục nghiệm nguyên thủy duy nhất (vì các $$f_i$$ đều lồi chặt):**
   $$x_1^\star = v^\star = 6, \qquad x_2^\star = \frac{v^\star}{2} = 3, \qquad x_3^\star = \frac{v^\star}{3} = 2.$$
   Kiểm tra lại: tổng $$x_1^\star + x_2^\star + x_3^\star = 6 + 3 + 2 = 11$$ (khả thi!) và $$f(x^\star) = \frac{1}{2}(36) + 9 + \frac{3}{2}(4) = 18 + 9 + 6 = 33 = g(v^\star)$$.

---

### Một hệ quả quan trọng của điều kiện dừng

Khi tính đối ngẫu mạnh được thỏa mãn và ta đã tìm được nghiệm đối ngẫu tối ưu $$(u^{\star}, v^{\star})$$, nghiệm nguyên thủy tối ưu $$x^{\star}$$ có thể được xác định bằng cách cực tiểu hóa hàm Lagrangian sau:

> $$ \min_x f(x) + \sum_{i=1}^m u_i^{\star} h_i(x) + \sum_{j=1}^r v^{\star}_j l_j(x)$$

Trong nhiều trường hợp, bài toán không ràng buộc này cho phép biểu diễn tường minh đặc trưng của nghiệm nguyên thủy theo nghiệm đối ngẫu. Đặc biệt, nếu bài toán cực tiểu hóa Lagrangian trên có nghiệm duy nhất, thì nghiệm đó chính là nghiệm nguyên thủy tối ưu $$x^{\star}$$. Cách tiếp cận này rất hữu ích khi bài toán đối ngẫu dễ giải hơn nhiều so với bài toán nguyên thủy.

### Ví dụ (Boyd & Vandenberghe, trang 249)

Xét bài toán tách biến có một ràng buộc đẳng thức tuyến tính:

> $$ \min_x \sum_{i=1}^n f_i(x_i) \qquad \text{ với điều kiện }\qquad a^Tx = b$$

Hàm đối ngẫu Lagrange được tính như sau:

> $$\begin{align}
> g(v) &= \min_x \sum_{i=1}^n f_i(x_i) + v(b−a^Tx) \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −va^Tx \\\
> &= bv + \min_x \sum_{i=1}^n f_i(x_i) −v \sum_{i=1}^n a_ix_i \\\
> &= bv + \sum_{i=1}^n (\underbrace{\min_{x_i} \{ f_i(x_i) − a_ivx_i \}}_{-f^{*}_i(a_iv)}) \\\
> &= bv − \sum_{i=1}^n f^{*}_i (a_iv)
> \end{align}$$

Ở đây $$f_i^{*}$$ là hàm liên hợp của $$f_i$$.

Do đó, bài toán đối ngẫu là:

> $$ \max_v bv − \sum^n_{i=1} f^{*}_i (a_iv)$$

Đổi dấu hàm mục tiêu để chuyển về dạng cực tiểu hóa, ta được:

> $$ \min_v \sum^n_{i=1} f^{*}_i (a_iv) − bv$$

Đây là bài toán tối ưu hóa lồi chỉ theo một biến vô hướng $$v$$, nên thường dễ giải hơn nhiều so với bài toán nguyên thủy có $$n$$ biến.

Sau khi tìm được $$v^{\star}$$, nghiệm nguyên thủy $$x^{\star}$$ được xác định từ:

> $$ \min_{x} \sum^n_{i=1} (f_i(x_i) − a_iv^{\star}x_i)$$

Nếu mỗi hàm $$f_i$$ lồi chặt, bài toán này có nghiệm duy nhất; khi các $$f_i$$ khả vi, từng thành phần $$x_i^{\star}$$ được tìm trực tiếp bằng cách giải phương trình $$\nabla f_i(x_i) = a_i v^{\star}$$ với mỗi $$i$$.

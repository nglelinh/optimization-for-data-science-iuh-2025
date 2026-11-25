---
layout: post
title: 07-03-02 Suy dẫn điều kiện tối ưu bậc một
chapter: '07'
order: 8
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
lesson_type: required
---

Ở Chương 04, ta từng chứng minh điều kiện tối ưu bậc nhất cho bài toán có ràng buộc $$\min_{x \in C} f(x)$$ là $$\nabla f(x^\star)^T(y - x^\star) \ge 0 \; \forall y \in C$$ bằng lập luận đạo hàm theo hướng trên đoạn thẳng nối $$x^\star$$ và $$y$$. Giờ đây, với hai công cụ cực sắc của Chương 07 là **hàm chỉ thị $$I_C$$** và **điều kiện $$0 \in \partial \tilde{f}(x^\star)$$**, bạn sẽ thấy toàn bộ định lý Chương 04 rơi ra tự nhiên chỉ trong **ba dòng đại số thuần túy**!

Cách nhìn này không chỉ đẹp về mặt thẩm mỹ toán học: nó còn mở đường trực tiếp sang các bài toán có ràng buộc nhưng hàm mục tiêu **không khả vi** (thay $$\nabla f(x^\star)$$ bằng một subgradient $$g \in \partial f(x^\star)$$ thỏa $$g^T(y - x^\star) \ge 0$$!).

## Bản đồ kiến thức nền: Ba bước hợp nhất Tối ưu có ràng buộc vào Subgradient

Chuỗi suy dẫn trong bài học này kết nối trọn vẹn Chương 04 và Chương 07 qua ba mắt xích:

- **Mắt xích 1 — Nhúng tập ràng buộc vào hàm mục tiêu:** Biến $$\min_{x \in C} f(x)$$ thành bài toán không ràng buộc $$\min_{x \in \mathbb{R}^n} \big(f(x) + I_C(x)\big)$$.
- **Mắt xích 2 — Áp dụng điều kiện tối ưu & Quy tắc tổng:**
  $$0 \in \partial(f + I_C)(x^\star) = \partial f(x^\star) + \partial I_C(x^\star) = \{\nabla f(x^\star)\} + N_C(x^\star).$$
  (Điều kiện chính quy đảm bảo quy tắc tổng: $$\operatorname{dom}(f) \cap C$$ thỏa điều kiện tương đối trong — luôn đúng khi $$f$$ xác định trên toàn $$\mathbb{R}^n$$!)
- **Mắt xích 3 — Dịch $$-\nabla f(x^\star) \in N_C(x^\star)$$ sang bất đẳng thức:** Theo định nghĩa nón pháp tuyến, vector $$v = -\nabla f(x^\star) \in N_C(x^\star)$$ có nghĩa là:
  $$(-\nabla f(x^\star))^T(y - x^\star) \le 0 \iff \nabla f(x^\star)^T(y - x^\star) \ge 0 \quad \forall y \in C.$$

### Khung giải thích (nên đọc chậm): Kiểm chứng $$-\nabla f(x^\star) \in N_C(x^\star)$$ trên một bài toán có ràng buộc cụ thể

Xét bài toán $$\min_{x \in C} \; f(x_1, x_2) = \frac{1}{2}(x_1 - 3)^2 + \frac{1}{2}(x_2 - 2)^2$$ trên hình vuông $$C = [0, 1] \times [0, 1]$$.

1. **Bước 1 — Đề xuất nghiệm tối ưu $$x^\star = (1, 1)$$ (góc trên–phải của hình vuông):**
   Tính gradient tại $$x^\star = (1, 1)$$:
   $$\nabla f(1, 1) = (1 - 3,\; 1 - 2)^T = (-2,\; -1)^T.$$
2. **Bước 2 — Tính hướng âm gradient $$-\nabla f(x^\star)$$:**
   $$-\nabla f(1, 1) = (+2,\; +1)^T.$$
3. **Bước 3 — Kiểm tra xem $$-\nabla f(x^\star)$$ có nằm trong Nón pháp tuyến $$N_C(1, 1)$$ không:**
   Ở bài trước ta đã tính $$N_C(1, 1) = \{(g_1, g_2) : g_1 \ge 0,\; g_2 \ge 0\} = \mathbb{R}_+^2$$.
   Rõ ràng $$(+2, +1)^T \in \mathbb{R}_+^2 = N_C(1, 1)$$!
4. **Kết luận:** Vì $$0 = \nabla f(1, 1) + (+2, +1)^T \in \partial f(1, 1) + \partial I_C(1, 1)$$, điểm $$(1, 1)$$ là nghiệm tối ưu toàn cục duy nhất! Nếu thử điểm $$(1, 0.5)$$ (cạnh phải, nơi $$N_C = \{(g_1, 0) : g_1 \ge 0\}$$), ta có $$-\nabla f(1, 0.5) = (2, 1.5)^T \notin N_C(1, 0.5)$$ (vì thành phần thứ 2 khác 0!), lập tức loại ngay!

---

Khi $$f$$ là hàm lồi và khả vi trên tập lồi $$C$$, điều kiện tối ưu theo gradient dưới trùng với điều kiện tối ưu bậc một như sau.

**Điều kiện tối ưu bậc một:**
$$x^* \text{ là tối ưu} \quad \Longleftrightarrow \quad \nabla f(x^*)^T(y - x^*) \geq 0, \text{ với mọi } y \in C$$

### Chứng minh
>
$$
\begin{alignat}{2}
f(x^{*}) = \min_{x\in C} f(x)  \quad & \Longleftrightarrow & & \quad f(x^{*}) = \min_x f(x) + I_C(x) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \partial(f(x^{*}) + I_C(x^{*})) \\
                      \quad & \Longleftrightarrow & &\quad 0 \in \{\nabla f(x^{*}) \} + \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*}) \in \mathcal{N}_C(x^{*}) \\
                      \quad & \Longleftrightarrow & &\quad - \nabla f(x^{*})^Tx^{*} \geq -\nabla f(x^{*})^Ty, \text{ với mọi }  y \in C \\
                      \quad & \Longleftrightarrow & &\quad \nabla f(x^{*})^T(y-x^{*}) \geq 0, \text{ với mọi } y \in C 
\end{alignat}
$$
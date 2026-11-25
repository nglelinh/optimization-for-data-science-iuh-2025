---
layout: post
title: 03-01 Tính chất cơ bản và ví dụ
chapter: '03'
order: 2
owner: Minjoo Lee
categories:
- chapter03
lang: vi
lesson_type: required
---

Khi cầm một hàm mục tiêu nhiều biến trên tay — ví dụ hàm mất mát của hồi quy ridge, chuẩn vector hay hàm entropy — câu hỏi đầu tiên của nhà tối ưu là: *đây có phải hàm lồi không, và cách chứng minh nhanh nhất là gì?* Không có một công thức duy nhất cho mọi hàm: có hàm kiểm tra bằng Hessian mất 10 giây, có hàm không khả vi (như $$|x|$$) phải dùng định nghĩa hoặc epigraph, lại có hàm chỉ cần nhìn thấy cấu trúc tổng bình phương là kết luận được ngay.

Phần 03-01 trang bị trọn bộ định nghĩa cơ bản, danh mục ví dụ mẫu mực và các đặc trưng bậc nhất – bậc hai cho hàm lồi.

## Bản đồ kiến thức nền: Ba bộ công cụ nhận diện hàm lồi

- **Công cụ hình học (Định nghĩa Jensen & Epigraph):** Dùng được cho mọi hàm (kể cả hàm không trơn như chuẩn $$\ell_1$$, hàm chỉ thị $$I_C$$); nối trực tiếp với tính lồi của tập $$\operatorname{epi} f$$.
- **Công cụ giải tích (Đặc trưng bậc 1 & bậc 2):** Với hàm khả vi, kiểm tra chặn dưới tiếp tuyến hoặc Hessian $$\nabla^2 f(x) \succeq 0$$ trên miền lồi.
- **Công cụ cắt lát 1D (Restriction to a line):** Một hàm $$n$$ biến $$f(x)$$ là lồi khi và chỉ khi mọi lát cắt một biến $$g(t) = f(x_0 + t v)$$ đều lồi theo $$t \in \mathbb{R}$$ — cực kỳ lợi hại để chứng minh tính lồi của hàm trên ma trận như $$-\log\det(X)$$!

### Khung giải thích (nên đọc chậm): Chứng minh $$f(x_1, x_2) = x_1^2 + x_1 x_2 + x_2^2$$ lồi theo 3 cách khác nhau

Xét hàm bậc hai hai biến $$f(x_1, x_2) = x_1^2 + x_1 x_2 + x_2^2$$ trên $$\mathbb{R}^2$$:

1. **Cách 1 — Kiểm tra nhanh bất đẳng thức Jensen trên một cặp điểm:** Chọn $$x = (2, 0),\ y = (0, 2)$$ (đều có $$f = 4$$) và trung điểm $$z = (1, 1)$$:
   $$f(1, 1) = 1 + 1 + 1 = 3 \le \frac{f(2, 0) + f(0, 2)}{2} = \frac{4 + 4}{2} = 4.$$
2. **Cách 2 — Chứng minh chặt bằng ma trận Hessian:**
   $$\nabla^2 f(x) = \begin{pmatrix}2 & 1\\ 1 & 2\end{pmatrix}.$$
   Vết bằng $$4$$, định thức bằng $$4 - 1 = 3 > 0 \implies$$ giá trị riêng $$\lambda_1 = 3 > 0,\ \lambda_2 = 1 > 0$$. Do $$\nabla^2 f \succ 0$$ mọi nơi, $$f$$ không chỉ lồi mà còn **1-lồi mạnh**!
3. **Cách 3 — Phân tích thành tổng các hàm lồi sơ cấp:**
   $$f(x_1, x_2) = \frac{1}{2}x_1^2 + \frac{1}{2}x_2^2 + \frac{1}{2}(x_1 + x_2)^2.$$
   Mỗi số hạng đều có dạng bình phương hàm tuyến tính (lồi), nên tổng của chúng chắc chắn lồi mà không cần tính định thức!

---

Phần này trình bày định nghĩa hàm lồi, các họ hàm lồi thường gặp và những tính chất đặc trưng cơ bản của chúng.
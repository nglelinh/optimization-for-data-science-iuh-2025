---
layout: post
title: '19-01-02 Phương pháp Newton proximal'
chapter: '19'
order: 4
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Ở phần trước, ta đã thấy **phương pháp Newton proximal** thay thế độ cong đẳng hướng $$\frac{1}{t} I$$ trong **proximal gradient descent** bằng ma trận Hessian cục bộ $$\nabla^2 g(x)$$. Ý tưởng này từng được nghiên cứu sớm trong thống kê dưới tên gọi "local score".

Dưới đây là cách xây dựng tường minh thuật toán **Newton proximal**.

## Thuật toán
Mỗi vòng lặp của phương pháp Newton proximal gồm hai bước: tìm hướng cập nhật $$v$$ và chọn độ dài bước $$t_k$$.

* **Bước 1:** Khởi tạo từ điểm ban đầu $$x^{(0)}$$ và lặp với $$k = 1, 2, 3, \dots$$

* **Bước 2:** Tìm hướng bước $$v^{(k)}$$ bằng cách giải bài toán con bậc hai có điều chuẩn:

> \begin{align}
v^{(k)} & = \underset{v}{\text{argmin}} \ \nabla g(x^{(k-1)})^T v + \frac{1}{2} v^T H^{(k-1)} v + h(x^{(k-1)} + v)
\end{align}

trong đó $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$ là ma trận Hessian của $$g$$ tại $$x^{(k-1)}$$.

* **Bước 3:** Cập nhật điểm lặp theo hướng $$v^{(k)}$$ với độ dài bước $$t_k$$:

> \begin{align}
x^{(k)} & =x^{(k-1)} + t_k v^{(k)}
\end{align}

Khi chọn cố định $$t_k = 1$$, ta thu được phương pháp Newton proximal thuần túy. Trong thực tế, độ dài bước $$t_k$$ thường được xác định qua tìm kiếm theo đường lui (backtracking line search).

#### Cách viết theo điểm đích $$z$$
Nếu biểu diễn bài toán con theo điểm đích $$z = x^{(k-1)} + v$$ thay vì hướng $$v$$, công thức cập nhật trở thành:

> $$
> \begin{align}
> z^{(k)} & = \underset{z}{\text{argmin}} \ \nabla g(x^{(k-1)})^T (z - x^{(k-1)}) + \frac{1}{2} (z - x^{(k-1)})^T H^{(k-1)} (z - x^{(k-1)}) + h(z) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

Về mặt trực giác, ở bước đầu ta tìm điểm trung gian $$z^{(k)}$$ cực tiểu hóa mô hình bậc hai của $$g$$ cộng với $$h$$, sau đó di chuyển từ $$x^{(k-1)}$$ về phía $$z^{(k)}$$ theo tỷ lệ $$t_k \in (0, 1]$$ (không nhất thiết đi trọn bước tới $$z^{(k)}$$).

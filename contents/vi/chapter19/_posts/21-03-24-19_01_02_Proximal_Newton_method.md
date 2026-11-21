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

Ở phần trước, chúng ta đã giải thích rằng **phương pháp Newton proximal** dùng Hessian cục bộ $$\nabla^2 g(x)$$ thay cho độ cong cầu $$\frac{1}{t} I$$ trong công thức của **proximal gradient descent**. Phương pháp Newton proximal là một ý tưởng cũ, được nghiên cứu trong thống kê dưới tên "local score".

Bây giờ hãy xem **phương pháp Newton proximal** có thể được xây dựng như thế nào.

## Thuật toán
Thuật toán Newton proximal gồm việc tìm hướng $$v$$ của bước tiếp theo rồi chọn kích thước bước $$t_k$$.

* Bước 1: Bắt đầu từ điểm ban đầu $$x^{(0)}$$, lặp lại các bước sau. ($$k=1,2,3,...$$)

* Bước 2: Tìm hướng $$v$$ của bước tiếp theo.

> \begin{align}
v^{(k)} & = \underset{v}{\text{argmin}} \ \nabla g(x^{(k-1)})^T v + \frac{1}{2} v^T H^{(k-1)} v + h(x^{(k-1)} + v)
\end{align}

Ở đây $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$ là Hessian của $$g$$ tại $$x^{(k-1)}$$.

* Bước 3: Chọn kích thước bước để di chuyển theo hướng $$v^{(k)}$$.

> \begin{align}
x^{(k)} & =x^{(k-1)} + t_k v^{(k)}
\end{align}

Ở đây $$t_k$$ là kích thước bước; với $$t_k=1$$ đây là phương pháp Newton proximal thuần túy.

Khác với proximal gradient descent, kích thước bước được chọn bằng backtracking line search.

#### Góc nhìn theo vị trí tiếp theo
Nếu biểu diễn theo vị trí tiếp theo $$z$$ thay vì hướng $$v$$, ta được như sau.

> $$
> \begin{align}
> z^{(k)} & = \underset{z}{\text{argmin}} \ \nabla g(x^{(k-1)})^T (z - x^{(k-1)}) + \frac{1}{2} (z - x^{(k-1)})^T H^{(k-1)} (z - x^{(k-1)}) + h(z) \\\\
> x^{(k)} & =x^{(k-1)} + t_k (z^{(k)} - x^{(k-1)} )
> \end{align}
> $$

Một cách trực quan, ở bước đầu tiên ta tìm điểm thay thế (surrogate) $$z$$ cực tiểu hóa mô hình bậc hai của hàm mục tiêu. Sau đó ta di chuyển từ $$x^{(k-1)}$$ theo hướng của $$z$$, nhưng không phải lúc nào cũng đi hết tới $$z$$.

---
layout: post
title: '15-01-03 Giải tích của hàm chắn logarit'
chapter: "15"
order: 5
owner: "Minjoo Lee"
categories:
- chapter15
lang: vi
---

Để đưa bài toán chắn $$\min t f(x) + \phi(x)$$ vào động cơ Newton, ta bắt buộc phải tính nhanh và chính xác **gradient $$\nabla \phi(x)$$** cùng **ma trận Hessian $$\nabla^2 \phi(x)$$** của hàm chắn logarit. Nếu nhìn vào tổng $$-\sum_{i=1}^m \log(-h_i(x))$$ có vẻ cồng kềnh, thì kết quả đạo hàm lại có cấu trúc đại số gọn gàng đến bất ngờ!

Đặc biệt khi các ràng buộc là tuyến tính $$h_i(x) = a_i^T x - b_i \le 0$$ (như trong LP và QP), đạo hàm cấp hai $$\nabla^2 h_i(x) = 0$$ biến mất hoàn toàn, khiến ma trận Hessian của hàm chắn trở thành một ma trận dạng $$A^T D^2 A$$ đối xứng, xác định dương (khi $$A$$ đủ hạng) — cực kỳ thuận lợi cho phân rã Cholesky!

## Kiến thức cần nhớ: Công thức giải tích và cấu trúc đại số của $$\phi(x)$$

- **Gradient của hàm chắn:** Áp dụng quy tắc dây chuyền cho $$-\log(-h_i(x))$$:
  $$\nabla \phi(x) = -\sum_{i=1}^m \frac{1}{h_i(x)} \nabla h_i(x) = \sum_{i=1}^m \frac{1}{-h_i(x)} \nabla h_i(x).$$
  Chú ý dấu: vì $$-h_i(x) > 0$$, mỗi thành phần $$\frac{1}{-h_i(x)} \nabla h_i(x)$$ hướng **ra ngoài tường** (theo hướng tăng $$h_i$$), nên hướng giảm $$-\nabla \phi(x)$$ luôn **đẩy ngược vào trong miền khả thi**!
- **Hessian của hàm chắn:** Gồm đúng hai phần đều nửa xác định dương:
  $$\nabla^2 \phi(x) = \sum_{i=1}^m \frac{1}{h_i(x)^2} \nabla h_i(x)\nabla h_i(x)^T - \sum_{i=1}^m \frac{1}{h_i(x)} \nabla^2 h_i(x).$$
  Phần thứ nhất là tổng các ma trận hạng 1 nửa xác định dương; phần thứ hai cũng nửa xác định dương vì $$-1/h_i(x) > 0$$ và $$\nabla^2 h_i(x) \succeq 0$$!
- **Trường hợp ràng buộc tuyến tính $$Bx \le d$$:** Đặt độ dư $$s_i = d_i - b_i^T x > 0$$, ta viết cực gọn dạng ma trận: $$\nabla \phi(x) = B^T s^{-1}$$ và $$\nabla^2 \phi(x) = B^T \operatorname{diag}(s^{-2}) B$$.

### Giải thích: Tính tay gradient và Hessian của hàm chắn trên miền đa giác 2D

Xét 3 ràng buộc tuyến tính trên $$\mathbb{R}^2$$: $$h_1(x) = -x_1 \le 0$$, $$h_2(x) = -x_2 \le 0$$, và $$h_3(x) = x_1 + x_2 - 3 \le 0$$.
Hàm chắn là $$\phi(x) = -\log(x_1) - \log(x_2) - \log(3 - x_1 - x_2)$$. Hãy tính $$\nabla \phi$$ và $$\nabla^2 \phi$$ tại điểm trong $$x = (1, 1)^T$$:

1. **Tính các độ dư $$-h_i(x)$$ và gradient $$\nabla h_i(x)$$ tại $$x = (1, 1)^T$$:**
   - $$-h_1 = 1$$, $$\nabla h_1 = (-1, 0)^T$$.
   - $$-h_2 = 1$$, $$\nabla h_2 = (0, -1)^T$$.
   - $$-h_3 = 3 - 1 - 1 = 1$$, $$\nabla h_3 = (1, 1)^T$$.
2. **Tính $$\nabla \phi(1, 1)$$:**
   $$\nabla \phi(1, 1) = \frac{1}{1}\begin{bmatrix} -1 \\ 0 \end{bmatrix} + \frac{1}{1}\begin{bmatrix} 0 \\ -1 \end{bmatrix} + \frac{1}{1}\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}!$$
   Không ngẫu nhiên đâu: $$(1, 1)^T$$ chính là **tâm giải tích** của tam giác này!
3. **Tính $$\nabla^2 \phi(1, 1)$$ (do $$\nabla^2 h_i = 0$$):**
   $$\nabla^2 \phi(1, 1) = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} + \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}.$$
   Kiểm tra tính xác định dương: vết $$2 + 2 = 4 > 0$$ và định thức $$2(2) - 1^2 = 3 > 0 \implies \nabla^2 \phi(1, 1) \succ 0$$!

---

Với hàm chắn logarit:
>
\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}

gradient và ma trận Hessian của $$\phi(x)$$ lần lượt là:

**Gradient:**
>
\begin{align}
\nabla \phi(x) = - \sum_{i=1}^{m} \frac{1}{h_i(x)} \nabla h_i(x)
\end{align}

**Hessian:**

>
\begin{align}
\nabla^2 \phi(x) = \sum_{i=1}^{m} \frac{1}{h_i(x)^2} \nabla h_i(x) \nabla h_i(x)^T -  \sum_{i=1}^{m} \frac{1}{h_i(x)} \nabla^2 h_i(x)
\end{align}

## Ví dụ: $$\phi(x) = -\sum_{i=1}^{n} \log(x_i)$$
Xét hàm chắn cho ràng buộc không âm:
>
\begin{align}
\phi(x) = -\sum_{i=1}^{n} \log(x_i)
\end{align}

Ở đây, các ràng buộc bất đẳng thức là $$h_i(x) = -x_i \le 0$$ (tức $$x_i \ge 0$$), và miền xác định của hàm chắn $$\phi$$ là $$x_i > 0$$ với mọi $$i$$.

**Gradient:**
>
$$
\nabla \phi(x) = - 
\begin{bmatrix}
1/x_1 \\\
\vdots \\\
1/x_n \\\
\end{bmatrix}
 = -X^{-1} \mathbb{1}, \qquad X = \text{diag}(x)$$
 
**Hessian:**
>
$$
\nabla^2 \phi(x) = 
\begin{bmatrix}
1/x_1^2 & \cdots & \\\
\vdots & \ddots & \vdots  \\\
& \cdots & 1/x_n^2 \\\
\end{bmatrix}
 = X^{-2}$$

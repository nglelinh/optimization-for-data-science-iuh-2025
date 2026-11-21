---
layout: post
title: '19-07 Phương pháp Newton chiếu (Projected Newton)'
chapter: '19'
order: 11
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

## Vấn đề của Newton chiếu là gì?
Khi $$h$$ là hàm chỉ thị $$h = I_C(x)$$ của một tập lồi $$C$$, bài toán trở thành

>$$ \min_{x} \ g(x) \quad  \text{subject to}  \quad  x \in C$$

Do đó, khi $$h(x) = I_C(x)$$, proximal gradient descent trở thành **projected gradient descent** (gradient descent chiếu). Nghĩa là projected gradient descent là một trường hợp đặc biệt của proximal gradient descent.

Còn Newton proximal khi $$h(x) = I_C(x)$$ thì sao? Trong trường hợp này cập nhật là

> $$
> \begin{align}
> z^{+} & =\underset{z \in C}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2  \\\\
> &= \underset{z \in C}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2} (z - x)^T H (z - x)  \\\\
> \end{align}
> $$

Nếu $$H = I$$ thì đây là phép chiếu của $$x - \nabla g(x)$$ lên tập $$C$$, nhưng với $$H \neq I$$ tổng quát thì nó không phải là phép chiếu. (Nếu $$H = I$$ thì chuẩn $$H$$ là chuẩn $$l_2$$; phép chiếu đòi hỏi chuẩn $$l_2$$ thông thường chứ không phải chuẩn $$H$$.)
Do đó, phương pháp Newton chiếu không phải là trường hợp đặc biệt của phương pháp Newton proximal.

## Newton chiếu cho ràng buộc hộp (box constraints)
Trong trường hợp đặc biệt của ràng buộc hộp, có thể áp dụng Newton chiếu (Bertsekas, 1982; Kim et al., 2010; Schmidt et al., 2011).

Xét bài toán

>$$ \min_{x} \ g(x) \quad  \text{subject to}  \quad  l \le x \le u $$

Với điểm xuất phát $$x^{(0)}$$ và hằng số nhỏ $$\epsilon \gt 0$$, phương pháp Newton chiếu lặp lại các bước sau ($$k = 1, 2, 3, ...$$).

* Bước 1: Định nghĩa tập ràng buộc chặt (binding set).

> \begin{align}
B_{k-1} & = \\{ i : x_i^{(k-1)} \le l_i + \epsilon \quad \text{and} \quad  \nabla_i g(x^{(k-1)}) \gt 0 \\} \quad  \cup \quad 
\\{ i : x_i^{(k-1)} \ge u_i - \epsilon  \quad \text{and} \quad  \nabla_i g(x^{(k-1)}) \lt 0 \\} 
\end{align}

Trong bước tối ưu, các biến này bị đẩy ra biên của hộp. Đẩy càng nhiều biến như vậy thì hàm mục tiêu càng giảm.

* Bước 2: Định nghĩa tập tự do (free set) $$F_{k-1} = \left\{1,....,n \right\} \backslash B_{k-1}$$.
* Bước 3: Tính nghịch đảo của ma trận con chính của Hessian trên các biến tự do.

>$$ S^{(k-1)} = [(\nabla^2 g(x^{(k-1)}))_{F_{k-1}}]^{-1}$$

* Bước 4: Thực hiện bước Newton trên các biến tự do rồi chiếu.

> $$
> \begin{align}
> x^{(k)} = P_{[l, u]} \left( x^{(k-1)} - t_k \begin{bmatrix} S^{(k-1)} & 0 \\
> 0 & I \end{bmatrix} 
> \begin{bmatrix} \nabla_{F_{k-1}} g(x^{(k-1)}) \\ \nabla_{B_{k-1}} g(x^{(k-1)}) \end{bmatrix}
> \right)
> \end{align}
> $$

Ở đây $$P_{[l,u]}$$ là phép chiếu lên $$[l, u] = [l_1, u_1] \times \cdots \times [l_n, u_n]$$.

Trong biểu thức ma trận, bước Newton được thực hiện cho các biến tự do, còn với các biến chặt thì chỉ thực hiện bước gradient thông thường. Ngoài ra, phép chiếu là phép toán đơn giản: với mỗi tọa độ nằm ngoài hộp, ta chỉ cần đặt nó bằng $$l_i$$ hoặc $$u_i$$ thích hợp.

Phương pháp này phù hợp khi bài toán rất lớn (ví dụ số chiều cao) và hầu hết các biến ở gần biên, khiến tập tự do rất nhỏ.

Những loại bài toán nào có ràng buộc hộp? Khá nhiều bài toán, chẳng hạn:

*  Bình phương tối thiểu không âm (nonnegative least squares)
*  Đối ngẫu của máy vector hỗ trợ (SVM dual)
*  Đối ngẫu của graphical lasso
*  Đối ngẫu của fused lasso (khử nhiễu total variation)

## Tính chất hội tụ
* Bertsekas (1982) chỉ ra rằng, dưới các giả thiết thích hợp, Newton chiếu xác định đúng các ràng buộc chặt sau một số hữu hạn vòng lặp. Từ đó nó trùng với phương pháp Newton trên các biến tự do.
*  Bertsekas (1982) cũng chứng minh hội tụ siêu tuyến tính.
*  Kim et al. (2010) và Schmidt et al. (2011) đề xuất các phương pháp quasi-Newton chiếu dùng cập nhật kiểu BFGS.

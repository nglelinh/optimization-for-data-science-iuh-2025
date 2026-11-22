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

## Vấn đề đặt ra với phương pháp Newton chiếu
Khi $$h$$ là hàm chỉ thị $$h(x) = I_C(x)$$ của một tập lồi $$C$$, bài toán tổng hợp trở thành bài toán tối ưu có ràng buộc:

>$$ \min_{x} \ g(x) \quad  \text{subject to}  \quad  x \in C$$

Trong trường hợp này, proximal gradient descent suy biến chính xác thành **hạ gradient chiếu (projected gradient descent)** — tức projected gradient descent là một trường hợp đặc biệt của proximal gradient descent.

Tuy nhiên, điều tương tự không xảy ra với Newton proximal khi $$h(x) = I_C(x)$$. Khi đó, bài toán con của Newton proximal có dạng:

> $$
> \begin{align}
> z^{+} & =\underset{z \in C}{\text{argmin}} \ \frac{1}{2} \parallel x - H^{-1} \nabla g(x) - z \parallel_H^2  \\\\
> &= \underset{z \in C}{\text{argmin}} \ \nabla g(x)^T (z - x) + \frac{1}{2} (z - x)^T H (z - x)  \\\\
> \end{align}
> $$

Chỉ khi $$H = I$$ biểu thức này mới là phép chiếu Euclid của $$x - \nabla g(x)$$ lên tập $$C$$; với ma trận $$H \neq I$$ tổng quát, đây là phép chiếu theo chuẩn $$H$$ (tức một bài toán quy hoạch bậc hai trên $$C$$) chứ không phải phép chiếu theo chuẩn $$\ell_2$$ thông thường. Vì vậy, phương pháp Newton chiếu không phải là trường hợp đặc biệt của phương pháp Newton proximal.

## Phương pháp Newton chiếu cho ràng buộc hộp (Box Constraints)
Với trường hợp đặc biệt là ràng buộc hộp, có thể xây dựng thuật toán Newton chiếu hiệu quả (Bertsekas, 1982; Kim et al., 2010; Schmidt et al., 2011).

Xét bài toán:

>$$ \min_{x} \ g(x) \quad  \text{subject to}  \quad  l \le x \le u $$

Với điểm khởi tạo $$x^{(0)}$$ và hằng số nhỏ $$\epsilon \gt 0$$, thuật toán lặp các bước sau ($$k = 1, 2, 3, \dots$$):

* **Bước 1:** Xác định tập chỉ số bị ràng buộc chặt (binding set):

> \begin{align}
B_{k-1} & = \\{ i : x_i^{(k-1)} \le l_i + \epsilon \quad \text{and} \quad  \nabla_i g(x^{(k-1)}) \gt 0 \\} \quad  \cup \quad 
\\{ i : x_i^{(k-1)} \ge u_i - \epsilon  \quad \text{and} \quad  \nabla_i g(x^{(k-1)}) \lt 0 \\} 
\end{align}

Đây là các tọa độ đang nằm sát biên hộp và có hướng giảm $$-\nabla_i g$$ chỉ ra ngoài tập khả thi.

* **Bước 2:** Xác định tập biến tự do (free set) $$F_{k-1} = \left\{1, \dots, n \right\} \setminus B_{k-1}$$.
* **Bước 3:** Tính nghịch đảo của khối ma trận con chính của Hessian trên tập biến tự do:

>$$ S^{(k-1)} = [(\nabla^2 g(x^{(k-1)}))_{F_{k-1}}]^{-1}$$

* **Bước 4:** Thực hiện bước Newton trên các biến tự do, bước gradient trên các biến bị ràng buộc chặt, rồi chiếu lên hộp:

> $$
> \begin{align}
> x^{(k)} = P_{[l, u]} \left( x^{(k-1)} - t_k \begin{bmatrix} S^{(k-1)} & 0 \\
> 0 & I \end{bmatrix} 
> \begin{bmatrix} \nabla_{F_{k-1}} g(x^{(k-1)}) \\ \nabla_{B_{k-1}} g(x^{(k-1)}) \end{bmatrix}
> \right)
> \end{align}
> $$

trong đó $$P_{[l,u]}$$ là phép chiếu lên hình hộp $$[l, u] = [l_1, u_1] \times \cdots \times [l_n, u_n]$$.

Phép chiếu lên hộp rất đơn giản: với mỗi tọa độ vượt ra ngoài đoạn $$[l_i, u_i]$$, ta chỉ cần cắt về đúng biên $$l_i$$ hoặc $$u_i$$ tương ứng. Phương pháp này đặc biệt hiệu quả với bài toán có số chiều lớn mà đa số biến nằm sát biên, khiến tập biến tự do $$F_{k-1}$$ nhỏ và việc nghịch đảo Hessian trên $$F_{k-1}$$ có chi phí thấp.

Một số bài toán tiêu biểu có dạng ràng buộc hộp:

* Bình phương tối thiểu không âm (nonnegative least squares)
* Bài toán đối ngẫu của máy vector hỗ trợ (SVM dual)
* Bài toán đối ngẫu của graphical lasso
* Bài toán đối ngẫu của fused lasso (khử nhiễu biến phân toàn phần — total variation denoising)

## Tính chất hội tụ
* Bertsekas (1982) chứng minh rằng dưới các giả thiết thích hợp, phương pháp Newton chiếu nhận diện đúng tập ràng buộc chặt sau một số hữu hạn vòng lặp; từ thời điểm đó trở đi, thuật toán trùng với phương pháp Newton trên các biến tự do.
* Bertsekas (1982) cũng chứng minh tốc độ hội tụ siêu tuyến tính (và bậc hai khi dùng Hessian chính xác).
* Kim et al. (2010) và Schmidt et al. (2011) phát triển thêm các phương pháp quasi-Newton chiếu sử dụng cập nhật kiểu BFGS.

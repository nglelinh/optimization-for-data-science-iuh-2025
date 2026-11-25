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

Khi $$h(x) = I_C(x)$$ là hàm chỉ thị của một tập ràng buộc lồi $$C$$, ta dễ bị cám dỗ bởi một suy nghĩ tưởng chừng hiển nhiên: *ở phương pháp bậc nhất, ta chỉ việc bước một bước gradient rồi chiếu Euclid lên $$C$$; vậy ở phương pháp bậc hai, sao không bước một bước Newton $$-H^{-1}\nabla g(x)$$ rồi chiếu Euclid lên $$C$$?* Cú sốc toán học của bài 19-07 là: **cách chiếu ngây thơ đó SAI HOÀN TOÀN — nó có thể dẫn bạn đi ngược lên dốc và làm tăng hàm mục tiêu!** Để có một phương pháp Newton chiếu đúng đắn, phép chiếu phải được thực hiện trong chuẩn $$H$$ (chính là Newton proximal), hoặc dùng chiến lược tách tập ràng buộc hoạt động thông minh của Bertsekas (1982).

## Bản đồ kiến thức nền: Ba trụ cột để tránh bẫy "Newton chiếu ngây thơ"

Hãy nắm rõ ba khái niệm sau để không bao giờ mắc lỗi khi kết hợp Newton với ràng buộc:

- **Chiếu Euclid vs. Chiếu theo chuẩn $$H$$:** Phép chiếu Euclid $$P_C(x - H^{-1}\nabla g(x))$$ không nhất thiết tạo ra hướng giảm khi $$H$$ không phải bội của ma trận đơn vị. Ngược lại, chiếu theo chuẩn $$H$$ — tức $$\arg\min_{z \in C} \frac{1}{2}\|z - (x - H^{-1}\nabla g(x))\|_H^2$$ — chính là Newton proximal với $$h = I_C$$ và **luôn** đảm bảo hướng giảm!
- **Ràng buộc hộp (Box Constraints, $$l \le x \le u$$) và hai tập biến của Bertsekas:** Với ràng buộc đơn giản $$x \ge 0$$, Bertsekas (1982) chia các tọa độ thành hai nhóm: **tập ràng buộc hoạt động** $$\mathcal{B}$$ (các biến đang chạm biên $$x_i = 0$$ và gradient đẩy ra ngoài $$\nabla_i g(x) > 0$$) và **tập biến tự do** $$\mathcal{F}$$ (phần còn lại).
- **Tách khối Hessian để chiếu Euclid trở nên hợp lệ:** Bằng cách xóa sạch các phần tử chéo giữa khối $$\mathcal{B}$$ và khối $$\mathcal{F}$$ trong ma trận nghịch đảo độ cong $$D_k$$ (dùng $$H_{\mathcal{F}\mathcal{F}}^{-1}$$ trên tập tự do và ma trận đường chéo dương trên tập hoạt động), Bertsekas chứng minh phép chiếu Euclid $$P_C(x - t D_k \nabla g(x))$$ **luôn là hướng giảm** và vẫn giữ tốc độ hội tụ bậc hai khi tập hoạt động ổn định!

### Khung giải thích (nên đọc chậm): Phản ví dụ tính tay cho thấy chiếu Euclid bước Newton làm TĂNG hàm mục tiêu

Xét hàm bậc hai lồi chặt 2 biến trên góc phần tư không âm $$C = \{x \in \mathbb{R}^2 : x_1 \ge 0, x_2 \ge 0\}$$:

$$g(x) = \frac{1}{2}x^T H x - b^T x, \qquad H = \begin{bmatrix} 2 & 1.5 \\ 1.5 & 2 \end{bmatrix} \succ 0, \qquad b = \begin{bmatrix} 1 \\ -1 \end{bmatrix}.$$

Xuất phát tại điểm biên $$x^{(0)} = (0, 0)^T \in C$$, ta có $$g(0, 0) = 0$$ và $$\nabla g(0) = -b = (-1, 1)^T$$:

1. **Cách ngây thơ (tính bước Newton không ràng buộc rồi chiếu Euclid lên $$C$$):**
   - Ma trận nghịch đảo: $$H^{-1} = \frac{1}{4 - 2.25}\begin{bmatrix} 2 & -1.5 \\ -1.5 & 2 \end{bmatrix} = \frac{1}{1.75}\begin{bmatrix} 2 & -1.5 \\ -1.5 & 2 \end{bmatrix}$$.
   - Bước Newton không ràng buộc: $$x_{\text{Newton}} = 0 - H^{-1}\nabla g(0) = H^{-1}b = \frac{1}{1.75}\begin{bmatrix} 3.5 \\ -3.5 \end{bmatrix} = \begin{bmatrix} 2 \\ -2 \end{bmatrix}$$.
   - Chiếu Euclid lên $$x \ge 0$$: $$z_{\text{ngây thơ}} = P_C(2, -2) = (2, 0)^T$$.
   - **Kiểm tra giá trị hàm mục tiêu:**
     $$g(2, 0) = \frac{1}{2}(2)(2^2) - (1)(2) = 4 - 2 = +2 > 0 = g(0, 0)!$$
     Thậm chí dọc theo tia $$x(t) = (2t, 0)$$ với $$t = 1$$, hàm mục tiêu tăng vọt từ $$0$$ lên $$+2$$!
2. **Cách đúng (Newton proximal / chiếu theo chuẩn $$H$$ hoặc Projected Newton Bertsekas):**
   - Tọa độ $$x_2 = 0$$ có $$\nabla_2 g(0) = +1 > 0$$ (nằm trong tập hoạt động $$\mathcal{B} = \{2\}$$), còn $$x_1$$ có $$\nabla_1 g(0) = -1 < 0$$ (tự do $$\mathcal{F} = \{1\}$$).
   - Giải trên tập tự do $$x_2 = 0$$ với độ cong $$H_{11} = 2$$: $$z_1 = 0 - H_{11}^{-1}(-1) = 0.5 \implies z_{\text{đúng}} = (0.5, 0)^T$$.
   - **Kiểm tra giá trị hàm:** $$g(0.5, 0) = \frac{1}{2}(2)(0.25) - (1)(0.5) = 0.25 - 0.5 = -0.25 < 0$$ — đạt đúng cực tiểu toàn cục trên $$C$$ ngay sau 1 bước!

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

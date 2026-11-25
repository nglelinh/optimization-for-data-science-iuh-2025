---
layout: post
title: 03-07 Chuẩn Euclidean - L2 - là Lồi
chapter: '03'
order: 15
owner: AI Assistant
categories:
- chapter03
lang: vi
---

Chuẩn Euclid $$f(x) = \|x\|_2 = \sqrt{x_1^2 + \cdots + x_n^2}$$ là một trong những hàm xuất hiện dày đặc nhất trong tối ưu hóa — từ phạt điều chuẩn Group Lasso, bài toán định vị cơ sở Fermat–Weber, cho đến các ràng buộc hình nón bậc hai (SOCP). Thế nhưng một câu hỏi rất thú vị là: đồ thị của $$\|x\|_2$$ có dạng một **hình nón nhọn ở gốc tọa độ** (không khả vi tại $$x = 0$$!), vậy làm sao chứng minh chặt chẽ nó là hàm lồi trên toàn $$\mathbb{R}^n$$?

Bài học này trình bày cả ba phương pháp chứng minh kinh điển (định nghĩa + Cauchy–Schwarz, phân tích Hessian tại $$x \ne 0$$, và bất đẳng thức tam giác) — một bài tập tuyệt vời để luyện đủ mọi góc nhìn giải tích lồi.

## Kiến thức cần nhớ: Ba góc nhìn chứng minh $$\|x\|_2$$ là hàm lồi

- **Góc nhìn 1 — Đại số (Định nghĩa + Cauchy–Schwarz):** Bình phương hai vế của bất đẳng thức Jensen rồi áp dụng $$x^T y \le \|x\|_2 \|y\|_2$$; ngắn gọn, không cần đạo hàm và đúng luôn tại điểm nhọn $$x = 0$$.
- **Góc nhìn 2 — Giải tích bậc hai (Hessian trên $$\mathbb{R}^n \setminus \{0\}$$):** Tính tường minh $$\nabla^2 f(x) = \frac{1}{\|x\|_2}\left(I - \frac{x x^T}{\|x\|_2^2}\right)$$ — chính là phép chiếu trực giao lên không gian vuông góc với $$x$$ chia cho $$\|x\|_2$$, nên luôn bán xác định dương!
- **Góc nhìn 3 — Hình học chuẩn (Bất đẳng thức tam giác + Đồng nhất dương):** Áp dụng ngay cho **mọi chuẩn** $$\|\cdot\|$$ bất kỳ ($$\ell_1, \ell_2, \ell_\infty, \ell_p$$) chỉ trong đúng 2 dòng!
- **Lưu ý phân biệt quan trọng:** $$\|x\|_2$$ lồi nhưng **không lồi chặt** (dọc theo bất kỳ tia $$t v$$ nào với $$t \ge 0$$, hàm là đường thẳng tuyến tính!); ngược lại bình phương chuẩn $$\|x\|_2^2$$ là **2-lồi mạnh** và trơn khắp nơi!

### Giải thích: Tính tay ma trận Hessian của $$f(x) = \|x\|_2$$ tại $$x = (3, 4)^T$$

Xét $$f(x_1, x_2) = \sqrt{x_1^2 + x_2^2}$$ tại điểm $$x = (3, 4)^T$$ (có $$\|x\|_2 = 5$$):

1. **Tính vector gradient:**
   $$\nabla f(x) = \frac{x}{\|x\|_2} = \begin{pmatrix}3/5\\ 4/5\end{pmatrix} = \begin{pmatrix}0.6\\ 0.8\end{pmatrix}.$$
2. **Tính ma trận Hessian $$\nabla^2 f(x) = \frac{1}{\|x\|_2}\left(I - \frac{x x^T}{\|x\|_2^2}\right)$$:**
   $$\frac{x x^T}{\|x\|_2^2} = \frac{1}{25}\begin{pmatrix}9 & 12\\ 12 & 16\end{pmatrix} \implies \nabla^2 f(3, 4) = \frac{1}{5}\left[\begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix} - \frac{1}{25}\begin{pmatrix}9 & 12\\ 12 & 16\end{pmatrix}\right] = \frac{1}{125}\begin{pmatrix}16 & -12\\ -12 & 9\end{pmatrix}.$$
3. **Phân tích giá trị riêng và ý nghĩa hình học:**
   - Vết: $$\operatorname{tr} = \frac{16 + 9}{125} = \frac{25}{125} = \frac{1}{5} = 0.2$$; định thức: $$\det = \frac{16\cdot 9 - (-12)^2}{125^2} = \frac{144 - 144}{125^2} = 0$$.
   - Hai giá trị riêng là $$\lambda_1 = 0.2 > 0$$ (theo phương tiếp tuyến vuông góc với $$x$$, nơi mặt nón cong tròn) và $$\lambda_2 = 0$$ (theo phương bán kính $$x = (3, 4)^T$$, nơi mặt nón là đường thẳng không cong!).
   Vì $$\lambda_1, \lambda_2 \ge 0$$, ta có $$\nabla^2 f(3, 4) \succeq 0$$ — khớp tuyệt đối với hình học mặt nón!

---

**Chuẩn Euclidean** (hay chuẩn $$\ell_2$$) của một vector $$x \in \mathbb{R}^n$$ được định nghĩa là:

$$\|x\|_2 = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2} = \sqrt{x^T x}$$

Trong bài này, chúng ta chứng minh hàm chuẩn Euclidean là hàm lồi bằng ba cách khác nhau:
1. **Chứng minh trực tiếp từ định nghĩa** kết hợp bất đẳng thức Cauchy–Schwarz
2. **Kiểm tra điều kiện bậc hai** (phân tích ma trận Hessian)
3. **Sử dụng bất đẳng thức tam giác**

## Phương pháp 1: Chứng minh dựa trên định nghĩa

<div class="textbook-theorem" markdown="1">
**Định lý**: Chuẩn Euclidean $$f(x) = \|x\|_2$$ là hàm lồi trên $$\mathbb{R}^n$$.
</div>

**Chứng minh**:
Cần chỉ ra rằng với mọi $$x, y \in \mathbb{R}^n$$ và mọi $$\theta \in [0,1]$$:

$$\|\theta x + (1-\theta) y\|_2 \leq \theta \|x\|_2 + (1-\theta) \|y\|_2$$

Đặt $$z = \theta x + (1-\theta) y$$. Ta có:

$$\begin{align}
\|z\|_2^2 &= \|\theta x + (1-\theta) y\|_2^2 \\
&= (\theta x + (1-\theta) y)^T (\theta x + (1-\theta) y) \\
&= \theta^2 x^T x + 2\theta(1-\theta) x^T y + (1-\theta)^2 y^T y \\
&= \theta^2 \|x\|_2^2 + 2\theta(1-\theta) x^T y + (1-\theta)^2 \|y\|_2^2
\end{align}$$

Theo **bất đẳng thức Cauchy–Schwarz**, $$x^T y \leq \|x\|_2 \|y\|_2$$, nên:

$$\|z\|_2^2 \leq \theta^2 \|x\|_2^2 + 2\theta(1-\theta) \|x\|_2 \|y\|_2 + (1-\theta)^2 \|y\|_2^2 = (\theta \|x\|_2 + (1-\theta) \|y\|_2)^2$$

Vì hai vế đều không âm, lấy căn bậc hai hai vế ta thu được:

$$\|\theta x + (1-\theta) y\|_2 \leq \theta \|x\|_2 + (1-\theta) \|y\|_2$$

Điều này chứng minh chuẩn Euclidean là hàm lồi. $$\square$$

## Phương pháp 2: Kiểm tra điều kiện bậc hai (phân tích Hessian)

Đối với hàm khả vi hai lần trên miền lồi, ta có thể kiểm tra tính lồi bằng cách chứng minh ma trận Hessian nửa xác định dương.

**Phân tích**:
Hàm $$f(x) = \|x\|_2 = \sqrt{x^T x}$$ không khả vi tại gốc tọa độ $$x = 0$$. Với mọi $$x \neq 0$$, các đạo hàm riêng bậc nhất và bậc hai là:

$$\frac{\partial f}{\partial x_i} = \frac{x_i}{\|x\|_2}$$

$$\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{1}{\|x\|_2} \delta_{ij} - \frac{x_i x_j}{\|x\|_2^3}$$

Do đó ma trận Hessian là:
$$H = \frac{1}{\|x\|_2} I - \frac{1}{\|x\|_2^3} x x^T = \frac{1}{\|x\|_2} \left( I - \frac{x x^T}{\|x\|_2^2} \right)$$

**Kiểm tra tính nửa xác định dương**:
Với mọi vector $$v \in \mathbb{R}^n$$:
$$v^T H v = \frac{1}{\|x\|_2} \left( \|v\|_2^2 - \frac{(x^T v)^2}{\|x\|_2^2} \right)$$

Theo bất đẳng thức Cauchy–Schwarz, $$(x^T v)^2 \leq \|x\|_2^2 \|v\|_2^2$$, suy ra:
$$\|v\|_2^2 - \frac{(x^T v)^2}{\|x\|_2^2} \geq 0$$

Như vậy $$H \succeq 0$$ tại mọi $$x \neq 0$$. (Tính lồi trên toàn $$\mathbb{R}^n$$ bao gồm cả điểm $$x = 0$$ được đảm bảo bởi Phương pháp 1 hoặc Phương pháp 3.)

## Phương pháp 3: Dùng bất đẳng thức tam giác

Chuẩn Euclidean thỏa mãn **bất đẳng thức tam giác** (bất đẳng thức Minkowski):
$$\|u + v\|_2 \leq \|u\|_2 + \|v\|_2$$

Đặt $$u = \theta x$$ và $$v = (1-\theta) y$$ với $$\theta \in [0,1]$$. Áp dụng bất đẳng thức tam giác và tính thuần nhất bậc một của chuẩn, ta có ngay:
$$\|\theta x + (1-\theta) y\|_2 = \|u + v\|_2 \leq \|u\|_2 + \|v\|_2 = \theta \|x\|_2 + (1-\theta) \|y\|_2$$

Cách chứng minh này cho thấy tính lồi thực chất là hệ quả trực tiếp của hai tiên đề cơ bản của mọi chuẩn.

## Các tính chất và ứng dụng chính

### Các tính chất liên quan
1. **Lồi chặt dọc theo đường thẳng không qua gốc:** Chuẩn Euclidean là hàm **lồi chặt** dọc theo mọi đường thẳng không đi qua gốc tọa độ.
2. **Tính thuần nhất:** $$\|\alpha x\|_2 = \lvert\alpha\rvert \|x\|_2$$ với mọi số thực $$\alpha$$.
3. **Tính dưới cộng:** $$\|x + y\|_2 \leq \|x\|_2 + \|y\|_2$$ (bất đẳng thức tam giác).

### Ứng dụng trong tối ưu hóa
Tính lồi của chuẩn Euclidean mang lại nhiều hệ quả quan trọng:
1. **Bài toán bình phương tối thiểu:** Hàm mục tiêu $$\|Ax - b\|_2^2$$ là hàm lồi.
2. **Chính quy hóa (regularization):** Các số hạng phạt dạng $$\lambda \|x\|_2$$ (với $$\lambda \ge 0$$) bảo toàn tính lồi của bài toán.
3. **Tối ưu có ràng buộc:** Các ràng buộc dạng $$\|x\|_2 \leq r$$ xác định miền khả thi lồi.

## Kết luận

Chúng ta đã chứng minh chuẩn Euclidean là hàm lồi theo ba hướng tiếp cận:
1. **Định nghĩa trực tiếp:** Kết hợp khai triển bình phương và bất đẳng thức Cauchy–Schwarz.
2. **Kiểm tra đạo hàm bậc hai:** Chứng minh ma trận Hessian nửa xác định dương với mọi $$x \neq 0$$.
3. **Bất đẳng thức tam giác:** Dùng trực tiếp bất đẳng thức tam giác và tính thuần nhất của chuẩn.

Tính chất lồi này là nền tảng cho nhiều bài toán và thuật toán trong tối ưu hóa, học máy, xử lý tín hiệu và giải tích số.

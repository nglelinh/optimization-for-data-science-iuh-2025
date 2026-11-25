---
layout: post
title: '20 Các phương pháp đối ngẫu (Dual Methods)'
chapter: '20'
order: 1
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Trong rất nhiều bài toán tối ưu lớn — từ điều phối điện lưới quốc gia đến huấn luyện mô hình học máy trên hàng trăm máy chủ — khó khăn lớn nhất không nằm ở hàm mục tiêu, mà nằm ở **các ràng buộc liên kết** buộc mọi biến phải phụ thuộc lẫn nhau. Chương 20 mở ra một chiến lược chuyển hướng ngoạn mục: thay vì đối đầu trực diện với ràng buộc trong không gian gốc, ta chuyển sang **không gian đối ngẫu** thông qua hàm liên hợp $$f^*$$ và nhân tử Lagrange $$u$$. Khi biến đối ngẫu đóng vai trò như "bảng giá điều phối", bài toán khổng lồ bỗng tách rời thành hàng trăm bài toán con độc lập — mở đường cho phân rã đối ngẫu, hàm Lagrange tăng cường và thuật toán nổi tiếng **ADMM**.

## Bản đồ kiến thức nền: Bốn trạm dừng chân cốt lõi của Chương 20

Để thấy rõ mạch logic xuyên suốt Chương 20 (vì sao ta phải đi từ phương pháp đối ngẫu cơ bản đến tận ADMM), hãy nhìn bốn nấc thang tiến hóa sau:

- **Hàm liên hợp Fenchel ($$f^*(y) = \sup_x (y^T x - f(x))$$) và bài toán đối ngẫu:** Cho phép viết gọn bài toán đối ngẫu của $$\min f(x) \text{ s.t. } Ax = b$$ thành $$\max_u -f^*(-A^T u) - b^T u$$, và nối trực tiếp dưới vi phân của hàm đối ngẫu với phần dư ràng buộc $$Ax - b$$.
- **Tăng (dưới) gradient đối ngẫu & Phân rã đối ngẫu (Dual Ascent / Decomposition):** Tối ưu hóa không ràng buộc trên biến đối ngẫu $$u$$. Khi $$f(x) = \sum_i f_i(x_i)$$ tách biến, bước cập nhật gốc tự động phân rã song song hoàn toàn — nhưng lại đòi hỏi điều kiện ngặt nghèo (như $$f$$ lồi chặt/mạnh) mới hội tụ ổn định.
- **Hàm Lagrange tăng cường (Augmented Lagrangian):** Cộng thêm số hạng phạt bậc hai $$\frac{\rho}{2}\|Ax - b\|_2^2$$ để ép hội tụ vững chắc dưới điều kiện rất nhẹ — nhưng số hạng bình phương lại làm **mất tính phân rã song song**.
- **ADMM (Alternating Direction Method of Multipliers):** Tách thành hai khối biến $$Ax + Bz = c$$ và cập nhật luân phiên theo kiểu Gauss–Seidel, kết hợp trọn vẹn **tính phân rã** của dual decomposition với **độ bền hội tụ** của augmented Lagrangian!

### Khung giải thích (nên đọc chậm): Tính tay hàm liên hợp $$f^*$$ và giải bài toán có ràng buộc qua không gian đối ngẫu

Xét bài toán lồi 2 biến có ràng buộc đẳng thức liên kết hai biến:

$$\min_{x_1, x_2} \; \underbrace{\frac{1}{2}x_1^2 + x_2^2}_{f(x)} \qquad \text{với điều kiện} \qquad x_1 + x_2 = 3.$$

1. **Tính hàm liên hợp $$f^*(y_1, y_2) = \sup_{x_1, x_2} \left(y_1 x_1 + y_2 x_2 - \frac{1}{2}x_1^2 - x_2^2\right)$$:**
   - Đạo hàm theo $$x_1$$ bằng $$0$$: $$y_1 - x_1 = 0 \implies x_1 = y_1$$, giá trị cực đại là $$\frac{1}{2}y_1^2$$.
   - Đạo hàm theo $$x_2$$ bằng $$0$$: $$y_2 - 2x_2 = 0 \implies x_2 = \frac{y_2}{2}$$, giá trị cực đại là $$\frac{1}{4}y_2^2$$.
   - Vậy $$f^*(y_1, y_2) = \frac{1}{2}y_1^2 + \frac{1}{4}y_2^2$$.
2. **Lập bài toán đối ngẫu 1 biến $$u \in \mathbb{R}$$ (với $$A = [1, 1], b = 3$$):**
   $$g(u) = -f^*(-u, -u) - 3u = -\left(\frac{1}{2}u^2 + \frac{1}{4}u^2\right) - 3u = -\frac{3}{4}u^2 - 3u.$$
3. **Giải bài toán đối ngẫu không ràng buộc và khôi phục nghiệm gốc:**
   - Đạo hàm $$g'(u) = -\frac{3}{2}u - 3 = 0 \implies u^\star = -2$$, giá trị đối ngẫu $$g(-2) = -3 + 6 = 3$$.
   - Khôi phục nghiệm gốc từ $$x^\star = \nabla f^*(-A^T u^\star) = \nabla f^*(2, 2) = (2, \; 1)^T$$!
   Kiểm tra lại: $$x_1^\star + x_2^\star = 3$$ và $$f(2, 1) = \frac{1}{2}(4) + 1 = 3 = g(-2)$$ — đối ngẫu mạnh đạt chính xác!

---

Trong chương này, chúng ta tìm hiểu các phương pháp giải bài toán tối ưu thông qua bài toán đối ngẫu: phương pháp hạ dưới vi phân đối ngẫu (dual subgradient), phân rã đối ngẫu (dual decomposition), hàm Lagrange tăng cường (augmented Lagrangian), đồng thời giới thiệu sơ lược ý tưởng của phương pháp nhân tử hướng luân phiên (Alternating Direction Method of Multipliers — ADMM).

Trước hết, hãy ôn lại ngắn gọn hai nội dung nền tảng từ các chương trước: phương pháp Newton proximal và hàm liên hợp (conjugate function).

## Ôn tập: phương pháp Newton proximal
Xét bài toán tổng hợp:
>\begin{equation}
\min_x g(x) + h(x)
\end{equation}

trong đó $$g$$ và $$h$$ là các hàm lồi, $$g$$ khả vi hai lần và $$h$$ có cấu trúc đơn giản.

Bắt đầu từ điểm khởi tạo $$x^{(0)} \in \mathbb{R}^n$$, ở mỗi vòng lặp $$k = 1, 2, 3, \dots$$, phương pháp Newton proximal tìm hướng cập nhật $$v^{(k)}$$:
>\begin{alignat}{1}
v^{(k)} & = \arg \min_v \nabla g({x^{(k-1)}})^T v +  \frac{1}{2} v^T \nabla^2 g(x^{(k-1)}) v + h(x^{(k-1)} + v) 
\end{alignat}

sau đó cập nhật điểm lặp với độ dài bước $$t_k$$ (xác định bằng backtracking line search):
>\begin{equation}
x^{(k)} = x^{(k-1)} + t_k v^{(k)}, \quad k=1,2,3,\dots 
\end{equation}

> * Chi phí mỗi vòng lặp cao (việc giải bài toán con tìm $$v^{(k)}$$ nói chung khó).
> * Tuy nhiên, dưới các giả thiết thích hợp, phương pháp chỉ cần rất ít vòng lặp và đạt tốc độ hội tụ bậc hai cục bộ.


## Ôn tập: hàm liên hợp (conjugate function)
Với hàm $$f: \mathbb{R}^n \to \mathbb{R}$$, hàm liên hợp $$f^*$$ được định nghĩa là:
>\begin{equation}
f^*(y) = \max_x y^Tx - f(x)
\end{equation}

(1) Hàm liên hợp thường xuất hiện trong các bài toán đối ngẫu dưới dạng tương đương:
>\begin{equation}
-f^{\ast}(y) = \min_x f(x) - y^Tx
\end{equation}

(2) Nếu $$f$$ là hàm lồi và đóng, thì $$f^{**} = f$$. Hơn nữa:
>\begin{equation}
x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz
\end{equation}

#### Chứng minh
Trước hết, ta chứng minh $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$.

#### Bước 1: $$y \in \partial f(x) \Longrightarrow x \in \partial f^{\ast}(y)$$
> Giả sử $$y \in \partial f(x)$$. Khi đó $$x$$ cực đại hóa hàm $$z \mapsto y^Tz - f(z)$$, nên $$f^{\ast}(y) = y^Tx - f(x)$$. Với mọi $$w$$, ta có $$f^{\ast}(w) \ge w^Tx - f(x) = f^{\ast}(y) + x^T(w - y)$$, điều này chứng tỏ $$x \in \partial f^{\ast}(y)$$.

#### Bước 2: $$x \in \partial f^{\ast}(y) \Longrightarrow y \in \partial f(x)$$
> Áp dụng Bước 1 cho hàm $$f^{\ast}$$: nếu $$x \in \partial f^{\ast}(y)$$ thì $$y \in \partial f^{\ast\ast}(x)$$. Vì $$f^{\ast\ast} = f$$ nên suy ra $$y \in \partial f(x)$$.

#### Bước 3: $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$
> Tương đương $$y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$ suy trực tiếp từ định nghĩa dưới vi phân ($$0 \in \partial(f(x) - y^Tx)$$). Kết hợp với Bước 1 và Bước 2, ta thu được điều phải chứng minh.


(3) Nếu $$f$$ lồi chặt thì:
> $$
> \begin{equation}
> \nabla f^{\ast}(y) = \arg\min_z f(z) - y^T z
> \end{equation}
> $$

#### Chứng minh

> Nếu $$f$$ lồi chặt thì hàm $$z \mapsto f(z) - y^Tz$$ có điểm cực tiểu duy nhất. Theo tính chất (2) ở trên, dưới vi phân $$\partial f^{\ast}(y)$$ chỉ gồm đúng một phần tử — đó chính là gradient $$\nabla f^{\ast}(y)$$. Do đó $$f^{\ast}$$ là hàm khả vi.

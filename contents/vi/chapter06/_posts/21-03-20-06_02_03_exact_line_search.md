---
layout: post
title: 06-02-03 Tìm kiếm đường chính xác
chapter: '06'
order: 8
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Nếu bạn đứng trên sườn núi và đã chọn xong hướng đi $$-\nabla f(x_k)$$, câu hỏi tham lam nhất có thể đặt ra là: *trên tia thẳng xuất phát từ $$x_k$$ theo hướng $$-\nabla f(x_k)$$, điểm nào có cao độ thấp nhất tuyệt đối?* Tìm ra chính xác điểm đáy dọc theo tia đó gọi là **Tìm kiếm đường chính xác (Exact Line Search)**.

Nghe qua tưởng chừng đây phải là chiến lược "vô địch" — nhưng hình học lại dành cho ta một cú ngoặt đầy bất ngờ: vì tại điểm đáy của tia tìm kiếm, tia đó **tiếp xúc** với đường đồng mức của $$f$$, nên gradient ở bước kế tiếp sẽ **vuông góc hoàn toàn** với gradient bước hiện tại ($$\nabla f(x_{k+1})^T \nabla f(x_k) = 0$$)! Kết quả là quỹ đạo của Exact Line Search trên các thung lũng elip hẹp tạo thành những đường gấp khúc **vuông góc 90°** kinh điển!

## Bản đồ kiến thức nền: Hình học trực giao và Công thức đóng của Exact Line Search

Ba trụ cột sau tóm gọn toàn bộ bản chất toán học của Exact Line Search:

- **Điều kiện trực giao giữa hai bước liên tiếp:** Đặt $$\phi(s) = f(x_k - s g_k)$$ với $$g_k = \nabla f(x_k)$$. Tại bước tối ưu $$t_k = \arg\min_{s > 0} \phi(s)$$, đạo hàm $$\phi'(t_k) = -\nabla f(x_k - t_k g_k)^T g_k = -g_{k+1}^T g_k = 0$$. Vậy hai hướng bước liên tiếp luôn **vuông góc tuyệt đối**!
- **Công thức đóng cho hàm bậc hai:** Với $$f(x) = \frac{1}{2} x^T Q x - b^T x$$ ($$Q \succ 0$$), giải $$\phi'(s) = 0$$ cho ngay công thức nghiệm đóng tuyệt đẹp:
  $$t_k = \frac{g_k^T g_k}{g_k^T Q g_k} = \frac{\|g_k\|_2^2}{g_k^T Q g_k}.$$
  Lưu ý: chỉ cần 1 phép nhân ma trận–vector $$Q g_k$$ để tính chính xác $$t_k$$!
- **Tốc độ hội tụ & Bất đẳng thức Kantorovich:** Với hàm bậc hai có chỉ số điều kiện $$\kappa = \lambda_{\max}/\lambda_{\min}$$, Exact Line Search đạt tỷ lệ giảm sai số mỗi bước bị chặn bởi $$\left(\frac{\kappa - 1}{\kappa + 1}\right)^2$$. Nếu $$\kappa = 1000$$, tỷ lệ này là $$0.996$$ — dù tìm bước chính xác 100%, thuật toán vẫn bị bẫy zíc-zắc vuông góc làm chậm lại!

### Khung giải thích (nên đọc chậm): Chạy tay 2 bước Exact Line Search và kiểm chứng góc vuông 90°

Xét hàm bậc hai $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + 4x_2^2)$$ với $$Q = \begin{pmatrix} 1 & 0 \\ 0 & 4 \end{pmatrix}$$, xuất phát từ $$x_0 = (4, 1)^T$$:

1. **Bước $$k = 0$$:**
   - Gradient: $$g_0 = Q x_0 = (4,\; 4)^T \implies \|g_0\|_2^2 = 16 + 16 = 32$$.
   - Mẫu số: $$g_0^T Q g_0 = 1(4)^2 + 4(4)^2 = 16 + 64 = 80$$.
   - Bước tối ưu chính xác: $$t_0 = \frac{32}{80} = 0.4$$.
   - Cập nhật: $$x_1 = (4, 1)^T - 0.4(4, 4)^T = (2.4,\; -0.6)^T$$.
   - Giá trị hàm: giảm từ $$f(x_0) = \frac{1}{2}(16 + 4) = 10$$ xuống $$f(x_1) = \frac{1}{2}(5.76 + 1.44) = 3.6$$ (tỷ lệ $$3.6/10 = 0.36 = \left(\frac{4-1}{4+1}\right)^2$$ — khớp chính xác tuyệt đối với định lý Kantorovich!).
2. **Bước $$k = 1$$ & Kiểm chứng trực giao:**
   - Gradient mới: $$g_1 = Q x_1 = (2.4,\; -2.4)^T$$.
   - Tích vô hướng $$g_1^T g_0 = (2.4)(4) + (-2.4)(4) = 9.6 - 9.6 = 0$$! Hai hướng đi **vuông góc chính xác 90°**!
   - Bước mới: $$t_1 = \frac{2.4^2 + 2.4^2}{1(2.4)^2 + 4(2.4)^2} = \frac{2}{5} = 0.4$$, cho $$x_2 = (1.44,\; 0.36)^T$$ và $$f(x_2) = 1.296 = 0.36 \cdot f(x_1)$$.

---

Một cách tiếp cận khác để chọn kích thước bước thích ứng trong gradient descent là **tìm kiếm đường chính xác (exact line search)**.

### Tìm kiếm Đường chính xác là gì?

Trong tìm kiếm đường chính xác, tại mỗi bước lặp ta di chuyển dọc theo hướng ngược chiều gradient và chọn kích thước bước tối ưu nhất trên tia tìm kiếm đó.

Với $$s \ge 0$$, điểm $$x - s \nabla f(x)$$ dịch chuyển từ vị trí hiện tại theo hướng $$-\nabla f(x)$$. Bằng cách cực tiểu hóa hàm mục tiêu theo $$s$$, ta xác định kích thước bước $$t$$ tối ưu:

> $$t = \arg\min_{s \ge 0} f(x - s \nabla f(x))$$

## Thuật toán Exact Line Search

Thuật toán gồm bốn bước lặp:

1. **Bước 1**: Tại điểm hiện tại $$x^{(k)}$$, tính gradient $$\nabla f(x^{(k)})$$.
2. **Bước 2**: Định nghĩa hàm một biến $$\phi(t) = f(x^{(k)} - t \nabla f(x^{(k)}))$$ với $$t \geq 0$$.
3. **Bước 3**: Tìm $$t^* = \arg\min_{t \geq 0} \phi(t)$$ bằng cách giải phương trình $$\phi'(t) = 0$$ (và kiểm tra điều kiện cực tiểu).
4. **Bước 4**: Cập nhật $$x^{(k+1)} = x^{(k)} - t^* \nabla f(x^{(k)})$$.

## Các Ví dụ Minh họa

### Ví dụ 1: Hàm Bậc hai Một biến (Cơ bản)

Xét hàm mục tiêu:
$$f(x) = \frac{1}{2}x^2 - 3x + 2$$

**Bước 1**: Tính gradient
$$\nabla f(x) = x - 3$$

**Bước 2**: Tại điểm xuất phát $$x^{(0)} = 0$$, ta có $$\nabla f(0) = -3$$.

**Bước 3**: Xây dựng hàm tìm kiếm đường
$$\phi(t) = f(0 - t(-3)) = f(3t) = \frac{1}{2}(3t)^2 - 3(3t) + 2 = \frac{9t^2}{2} - 9t + 2$$

**Bước 4**: Tìm cực tiểu bằng cách lấy đạo hàm
$$\phi'(t) = 9t - 9 = 0 \Rightarrow t^* = 1$$

**Bước 5**: Cập nhật
$$x^{(1)} = 0 - 1 \cdot (-3) = 3$$

Kết quả: Chỉ sau một bước, thuật toán đã tìm được nghiệm tối ưu $$x^* = 3$$ (vì $$\nabla f(3) = 0$$).

### Ví dụ 2: Hàm Bậc hai Nhiều biến (Trung bình)

Xét hàm mục tiêu:
$$f(x_1, x_2) = x_1^2 + 2x_2^2 - 2x_1 - 4x_2 + 3$$

**Bước 1**: Tính gradient
$$\nabla f(x_1, x_2) = \begin{pmatrix} 2x_1 - 2 \\ 4x_2 - 4 \end{pmatrix}$$

**Bước 2**: Tại điểm xuất phát $$x^{(0)} = (0, 0)$$
$$\nabla f(0, 0) = \begin{pmatrix} -2 \\ -4 \end{pmatrix}$$

**Bước 3**: Xây dựng hàm tìm kiếm đường
$$x^{(0)} - t \nabla f(x^{(0)}) = \begin{pmatrix} 0 \\ 0 \end{pmatrix} - t \begin{pmatrix} -2 \\ -4 \end{pmatrix} = \begin{pmatrix} 2t \\ 4t \end{pmatrix}$$

$$\phi(t) = f(2t, 4t) = (2t)^2 + 2(4t)^2 - 2(2t) - 4(4t) + 3$$
$$= 4t^2 + 32t^2 - 4t - 16t + 3 = 36t^2 - 20t + 3$$

**Bước 4**: Tìm cực tiểu
$$\phi'(t) = 72t - 20 = 0 \Rightarrow t^* = \frac{20}{72} = \frac{5}{18}$$

**Bước 5**: Cập nhật
$$x^{(1)} = \begin{pmatrix} 2 \cdot \frac{5}{18} \\ 4 \cdot \frac{5}{18} \end{pmatrix} = \begin{pmatrix} \frac{5}{9} \\ \frac{10}{9} \end{pmatrix}$$

### Ví dụ 3: Hàm Rosenbrock 2D (Khó)

Xét hàm Rosenbrock:
$$f(x_1, x_2) = 100(x_2 - x_1^2)^2 + (1 - x_1)^2$$

**Bước 1**: Tính gradient
$$\nabla f(x_1, x_2) = \begin{pmatrix} -400x_1(x_2 - x_1^2) - 2(1 - x_1) \\ 200(x_2 - x_1^2) \end{pmatrix}$$

**Bước 2**: Tại điểm xuất phát $$x^{(0)} = (-1, 1)$$
$$\nabla f(-1, 1) = \begin{pmatrix} -400(-1)(1 - 1) - 2(1 - (-1)) \\ 200(1 - 1) \end{pmatrix} = \begin{pmatrix} -4 \\ 0 \end{pmatrix}$$

**Bước 3**: Xây dựng hàm tìm kiếm đường
$$x^{(0)} - t \nabla f(x^{(0)}) = \begin{pmatrix} -1 \\ 1 \end{pmatrix} - t \begin{pmatrix} -4 \\ 0 \end{pmatrix} = \begin{pmatrix} -1 + 4t \\ 1 \end{pmatrix}$$

$$\phi(t) = f(-1 + 4t, 1) = 100(1 - (-1 + 4t)^2)^2 + (1 - (-1 + 4t))^2$$

Hàm một biến này là đa thức bậc bốn phức tạp, nên cần dùng phương pháp số để tìm cực tiểu.

**Nhận xét**: Với hàm Rosenbrock, tìm kiếm đường chính xác trở nên tốn kém vì:
- Hàm mục tiêu không có dạng bậc hai đơn giản.
- Cần áp dụng phương pháp số như Newton–Raphson để giải $$\phi'(t) = 0$$.
- Có thể tồn tại nhiều điểm dừng cục bộ dọc theo tia tìm kiếm.

### Ví dụ 4: Bài toán Có Ràng buộc Miền (Rất khó)

Xét bài toán:
$$\min f(x) = x_1^2 + x_2^2 - 2x_1x_2$$
với ràng buộc $$x_1, x_2 \geq 0$$.

Trong trường hợp này, tìm kiếm đường chính xác phải giải bài toán có ràng buộc:
$$t^* = \arg\min_{t \geq 0} f(x^{(k)} - t \nabla f(x^{(k)}))$$
sao cho $$x^{(k)} - t \nabla f(x^{(k)}) \geq 0$$.

Ràng buộc miền làm cho việc xác định kích thước bước chính xác trở nên phức tạp hơn.

## Ưu điểm và Nhược điểm

### Ưu điểm:
1. **Tối ưu theo hướng hiện tại**: Mỗi bước đảm bảo giảm tối đa giá trị hàm mục tiêu dọc theo hướng ngược chiều gradient.
2. **Hội tụ nhanh trong trường hợp đặc biệt**: Đối với hàm bậc hai một biến hoặc hàm bậc hai đẳng hướng, thuật toán hội tụ chỉ sau một bước.
3. **Không cần tinh chỉnh tốc độ học**: Loại bỏ nhu cầu chọn trước tham số tốc độ học cố định.

### Nhược điểm:
1. **Chi phí tính toán cao**: Mỗi lần lặp đòi hỏi giải một bài toán tối ưu một biến.
2. **Phức tạp với hàm phi tuyến**: Cần dùng phương pháp giải số để tìm cực tiểu của $$\phi(t)$$.
3. **Kém thực tế với bài toán quy mô lớn**: Chi phí đánh giá hàm ở mỗi bước quá cao.

## Khi nào Nên Dùng Tìm kiếm Đường chính xác?

Tìm kiếm đường chính xác phù hợp khi:
- **Hàm mục tiêu đơn giản** (ví dụ: hàm bậc hai có công thức nghiệm đóng cho $$t^*$$).
- **Số chiều nhỏ** (thường $$\le 10$$ biến).
- **Yêu cầu độ chính xác cao** và có thể chấp nhận chi phí tính toán lớn hơn.
- **Hàm mục tiêu có cấu trúc đặc biệt** cho phép giải tích trực tiếp.

Trong thực tế, **tìm kiếm đường lùi (backtracking line search)** thường hiệu quả hơn và được sử dụng phổ biến hơn cho đa số ứng dụng.

### Tìm kiếm đường lùi và chính xác trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/line-search_vi.mp4"></video>
</div>

Bước cố định quá nhỏ hay quá lớn, điều kiện Armijo và các lần lùi t ← βt, so với tìm kiếm chính xác trên ví dụ của bài.

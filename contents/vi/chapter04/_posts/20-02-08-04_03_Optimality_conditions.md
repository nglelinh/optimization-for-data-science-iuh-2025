---
layout: post
title: 04-03 Điều kiện tối ưu
chapter: '04'
order: 4
owner: YoungJae Choung
categories:
- chapter04
lang: vi
lesson_type: required
---

Trong giải tích năm nhất đại học, câu thần chú đầu tiên ai cũng thuộc lòng để tìm cực tiểu là: *"lấy đạo hàm và cho bằng không"*. Nhưng ngay khi bước ra thế giới thực — nơi bạn không thể đầu tư số tiền âm, không thể sản xuất vượt công suất nhà máy, hay không thể đặt xác suất lớn hơn 1 — câu thần chú ấy lập tức thất bại: điểm tối ưu thường nằm ép sát vào biên tập khả thi, nơi gradient hoàn toàn khác không!

Vậy làm sao ta biết chắc một điểm nằm trên biên thực sự là đáy sâu nhất? Câu trả lời của tối ưu hóa lồi mang vẻ đẹp hình học đáng kinh ngạc: **tại điểm tối ưu $$x^\star$$, hướng giảm nhanh nhất $$-\nabla f(x^\star)$$ phải chỉ thẳng ra ngoài tập khả thi**, sao cho mọi bước đi hợp lệ $$y - x^\star$$ vào bên trong tập khả thi đều tạo góc tù (hoặc vuông) với $$-\nabla f(x^\star)$$, tức $$\nabla f(x^\star)^T (y - x^\star) \ge 0$$.

## Bản đồ kiến thức nền: Từ đạo hàm cổ điển đến điều kiện tối ưu có ràng buộc

Bài học này nối liền giải tích nhiều biến với hình học lồi qua bốn trụ cột:

- **Điều kiện tối ưu bậc nhất (First-Order Optimality / Variational Inequality):** Với hàm lồi khả vi $$f$$ trên tập khả thi lồi $$C$$, bất đẳng thức $$\nabla f(x^\star)^T (y - x^\star) \ge 0 \; \forall y \in C$$ là điều kiện **vừa cần vừa đủ** cho tối ưu toàn cục. Khi $$x^\star$$ nằm ở phần trong của $$C$$, nó tự động thu gọn về $$\nabla f(x^\star) = 0$$.
- **Nón pháp tuyến (Normal Cone):** Viết lại bất đẳng thức trên dưới dạng $$(-\nabla f(x^\star))^T (y - x^\star) \le 0$$ cho thấy $$-\nabla f(x^\star)$$ thuộc nón pháp tuyến $$N_C(x^\star)$$ — tập mọi vector "chống lại" mọi hướng đi vào $$C$$.
- **Không gian tiếp tuyến & Điều kiện bậc hai (Second-Order Conditions):** Đối với bài toán tổng quát (kể cả chưa chắc lồi), thông tin đạo hàm bậc nhất chỉ cho biết độ dốc, còn ma trận Hessian $$\nabla^2 f(x^\star)$$ đo độ cong. Trên không gian các hướng khả thi, Hessian nửa xác định dương là điều kiện cần, và xác định dương chặt là điều kiện đủ cho cực tiểu địa phương chặt.
- **Liên hệ với Nhân tử Lagrange & KKT:** Khi tập $$C$$ được mô tả bằng các bất đẳng thức và đẳng thức cụ thể, điều kiện $$-\nabla f(x^\star) \in N_C(x^\star)$$ sẽ bung ra thành hệ phương trình KKT nổi tiếng mà ta sẽ học sâu hơn ở các chương đối ngẫu.

### Khung giải thích (nên đọc chậm): Kiểm chứng điều kiện tối ưu bậc nhất trên ba trường hợp điển hình

Xét hàm mục tiêu lồi $$f(x_1, x_2) = \frac{1}{2}(x_1 - 2)^2 + \frac{1}{2}(x_2 + 1)^2$$, có gradient $$\nabla f(x) = (x_1 - 2,\; x_2 + 1)^T$$, cực tiểu hóa trên góc phần tư không âm $$C = \{x \in \mathbb{R}^2 : x_1 \ge 0,\; x_2 \ge 0\}$$.

1. **Ứng viên 1 (sai): $$x^{(1)} = (1, 0)$$.**
   - Gradient: $$\nabla f(1, 0) = (-1, 1)^T$$.
   - Chọn điểm khả thi $$y = (2, 0) \in C$$. Khi đó $$y - x^{(1)} = (1, 0)^T$$ và
     $$\nabla f(x^{(1)})^T (y - x^{(1)}) = (-1)(1) + (1)(0) = -1 < 0.$$
   - Kết luận: Vi phạm điều kiện tối ưu! Đi theo hướng $$(1,0)$$ làm giảm $$f$$ (thực tế $$f(2,0)=0.5 < f(1,0)=1$$).

2. **Ứng viên 2 (đúng): $$x^\star = (2, 0)$$.**
   - Gradient: $$\nabla f(2, 0) = (0, 1)^T \neq 0$$! Dù gradient khác không, hãy kiểm tra với **mọi** $$y = (y_1, y_2) \in C$$ (tức $$y_1 \ge 0, y_2 \ge 0$$):
     $$\nabla f(x^\star)^T (y - x^\star) = 0 \cdot (y_1 - 2) + 1 \cdot (y_2 - 0) = y_2 \ge 0.$$
   - Kết luận: Thỏa mãn với mọi $$y \in C$$! Vì $$f$$ lồi và $$C$$ lồi, $$x^\star = (2, 0)$$ chắc chắn là nghiệm tối ưu toàn cục, với $$f^\star = 0.5$$.

3. **Kiểm tra điều kiện bậc hai:** Ma trận Hessian $$\nabla^2 f(x^\star) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \succ 0$$ xác định dương chặt trên mọi hướng khác không, khẳng định thêm rằng $$x^\star = (2, 0)$$ là cực tiểu chặt duy nhất.

---

## Điều kiện tối ưu bậc nhất

Để ôn lại các tính chất của hàm lồi, xem [Chương 3: Các Tính chất Chính của Hàm Lồi]({% multilang_post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %}).

Xét bài toán tối ưu hóa lồi:

>$$
\begin{aligned}
&\min_x &&f(x) \\
&\text{subject to} &&x \in C
\end{aligned}
$$

Đối với một bài toán lồi có hàm mục tiêu $$f$$ **khả vi** và tập khả thi $$C$$ lồi, điều kiện cần và đủ để điểm khả thi $$x \in C$$ là điểm tối ưu là:

> $$\nabla f(x)^{T}(y-x) \geq 0 \quad \text{với mọi } y \in C$$

Đây được gọi là *điều kiện bậc nhất cho tính tối ưu* (first-order optimality condition).

Phương trình $$\nabla f(x)^{T}(y-x) = 0$$ xác định một siêu phẳng tựa đi qua $$x$$ đối với tập $$C$$, trong đó vectơ $$-\nabla f(x)$$ là hướng giảm nhanh nhất của hàm $$f$$ tại $$x$$. <br><br>

Khi điều kiện trên được thỏa mãn, toàn bộ tập $$C$$ nằm trong nửa không gian đối diện với hướng $$-\nabla f(x)$$, nghĩa là không tồn tại hướng dịch chuyển khả thi nào từ $$x$$ làm giảm giá trị hàm mục tiêu; do đó $$x$$ là điểm tối ưu.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/first-order-condition.png" alt="[Fig1] geometric interpretation of first-order condition for optimality [3]">
  <figcaption style="text-align: center;">[Hình 1] Minh họa hình học cho điều kiện tối ưu bậc nhất [3]</figcaption>
</p>
</figure>
<br>

### Trường hợp đặc biệt quan trọng
Khi $$C = \mathbb{R}^n$$ (bài toán tối ưu hóa không ràng buộc), điều kiện tối ưu bậc nhất rút gọn thành:
> $$\nabla f(x) = 0$$

Trong trường hợp này, mọi hướng trong $$\mathbb{R}^n$$ đều là hướng khả thi, nên điều kiện $$\nabla f(x) = 0$$ có nghĩa là tại $$x$$ không còn hướng nào giúp giảm giá trị của $$f$$.

---

## Nền tảng toán học cho điều kiện bậc hai

Trong khi các điều kiện bậc nhất sử dụng gradient $$\nabla f(x)$$, các điều kiện bậc hai sử dụng **ma trận Hessian**:

$$H_f(x) = \nabla^2 f(x) = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}$$

Ma trận Hessian mô tả **độ cong** của hàm tại điểm $$x$$, cung cấp thông tin về hình dạng cục bộ của hàm mục tiêu quanh điểm đang xét.

## Điều kiện tối ưu bậc hai

Xét bài toán tối ưu hóa không ràng buộc:
$$\min_x f(x)$$

trong đó $$f: \mathbb{R}^n \to \mathbb{R}$$ khả vi liên tục cấp hai.

### Điều kiện cần bậc hai

Nếu $$x^*$$ là điểm cực tiểu địa phương của $$f$$, thì:

1. **Điều kiện cần bậc nhất:** $$\nabla f(x^*) = 0$$
2. **Điều kiện cần bậc hai:** $$\nabla^2 f(x^*) \succeq 0$$ (ma trận nửa xác định dương)

### Điều kiện đủ bậc hai

Nếu tại điểm $$x^*$$ thỏa mãn đồng thời:

1. $$\nabla f(x^*) = 0$$ (điều kiện bậc nhất)
2. $$\nabla^2 f(x^*) \succ 0$$ (ma trận xác định dương)

thì $$x^*$$ là **điểm cực tiểu địa phương chặt** của $$f$$.

## Tính xác định dương của ma trận đối xứng

Một ma trận đối xứng $$A$$ được gọi là:
- **Xác định dương** ($$A \succ 0$$) nếu $$v^T A v > 0$$ với mọi $$v \neq 0$$.
- **Nửa xác định dương** ($$A \succeq 0$$) nếu $$v^T A v \geq 0$$ với mọi $$v$$.

**Các tiêu chuẩn kiểm tra tính xác định dương trong thực tế:**
1. **Tiêu chuẩn giá trị riêng:** Tất cả các giá trị riêng của $$A$$ đều dương.
2. **Tiêu chuẩn Sylvester (định thức con chính dẫn đầu):** Tất cả các định thức con chính dẫn đầu của $$A$$ đều dương.
3. **Phân tích Cholesky:** Tồn tại ma trận tam giác dưới $$L$$ có các phần tử đường chéo dương sao cho $$A = L L^T$$.

## Giải thích hình học

Các điều kiện bậc hai cho biết **độ cong** của đồ thị hàm số tại điểm dừng:

- **$$\nabla^2 f(x^*) \succ 0$$:** Đồ thị cong lên theo mọi hướng → **cực tiểu địa phương chặt**.
- **$$\nabla^2 f(x^*) \prec 0$$:** Đồ thị cong xuống theo mọi hướng → **cực đại địa phương chặt**.
- **$$\nabla^2 f(x^*) \succeq 0$$:** Độ cong không âm theo mọi hướng → **có thể là điểm cực tiểu** (cần kiểm tra thêm ở bậc cao hơn).
- **Hessian bất định:** Độ cong dương theo một số hướng và âm theo một số hướng khác → **điểm yên ngựa**.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter04/second-order-conditions.png" alt="Second-order optimality conditions visualization" width="80%" height="80%">
 <figcaption style="text-align: center;">[Hình 2] Minh họa hình học về các điều kiện tối ưu bậc hai</figcaption>
</p>
</figure>

## Các ví dụ minh họa

### Ví dụ 1: Hàm bậc hai
Xét hàm $$f(x_1, x_2) = x_1^2 + 2x_2^2 + x_1 x_2$$.

**Bước 1: Tìm điểm dừng**
$$\nabla f(x) = \begin{bmatrix} 2x_1 + x_2 \\ 4x_2 + x_1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Giải hệ phương trình trên thu được điểm dừng duy nhất $$x^* = (0, 0)$$.

**Bước 2: Tính ma trận Hessian**
$$\nabla^2 f(x) = \begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix}$$

**Bước 3: Kiểm tra tính xác định dương**
- Giá trị riêng: từ phương trình đặc trưng $$\lambda^2 - 6\lambda + 7 = 0$$, ta có $$\lambda_1 = \frac{6 + \sqrt{8}}{2} = 3 + \sqrt{2} > 0$$ và $$\lambda_2 = \frac{6 - \sqrt{8}}{2} = 3 - \sqrt{2} > 0$$.
- Định thức con chính dẫn đầu: $$\Delta_1 = 2 > 0$$ và $$\Delta_2 = \det = 8 - 1 = 7 > 0$$.

**Kết luận:** $$\nabla^2 f(0,0) \succ 0$$, do đó $$(0,0)$$ là điểm cực tiểu địa phương chặt (và cũng là cực tiểu toàn cục vì $$f$$ lồi chặt).

### Ví dụ 2: Hàm không lồi
Xét hàm $$f(x_1, x_2) = x_1^4 + x_2^4 - 2x_1^2 - 2x_2^2$$.

**Bước 1: Tìm các điểm dừng**
$$\nabla f(x) = \begin{bmatrix} 4x_1^3 - 4x_1 \\ 4x_2^3 - 4x_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Các điểm dừng là: $$(0,0)$$, $$(\pm 1, 0)$$, $$(0, \pm 1)$$, và $$(\pm 1, \pm 1)$$.

**Bước 2: Phân tích tại $$(0,0)$$**
$$\nabla^2 f(0,0) = \begin{bmatrix} -4 & 0 \\ 0 & -4 \end{bmatrix} \prec 0$$

**Kết luận:** $$(0,0)$$ là điểm cực đại địa phương chặt.

**Bước 3: Phân tích tại $$(1,1)$$**
$$\nabla^2 f(1,1) = \begin{bmatrix} 8 & 0 \\ 0 & 8 \end{bmatrix} \succ 0$$

**Kết luận:** $$(1,1)$$ là điểm cực tiểu địa phương chặt.

### Ví dụ 3: Điểm yên ngựa
Xét hàm $$f(x_1, x_2) = x_1^2 - x_2^2$$.

**Phân tích tại $$(0,0)$$:**
- $$\nabla f(0,0) = (0,0)$$ ✓
- $$\nabla^2 f(0,0) = \begin{bmatrix} 2 & 0 \\ 0 & -2 \end{bmatrix}$$ (ma trận bất định)

**Kết luận:** $$(0,0)$$ là một điểm yên ngựa (không phải cực tiểu cũng không phải cực đại).

## Tối ưu hóa có ràng buộc: Điều kiện bậc hai

Đối với bài toán tối ưu hóa có ràng buộc đẳng thức:
$$\min_x f(x) \text{ subject to } h_i(x) = 0, \, i = 1,\ldots,m$$

ta sử dụng **ma trận Hessian có viền** (bordered Hessian) của hàm Lagrange:
$$\mathcal{L}(x,\lambda) = f(x) + \sum_{i=1}^m \lambda_i h_i(x)$$

**Điều kiện đủ bậc hai:** Tại điểm dừng thỏa mãn điều kiện chính quy, nếu ma trận Hessian có viền có quán tính phù hợp (số giá trị riêng âm bằng đúng số ràng buộc $$m$$ và $$n$$ giá trị riêng còn lại đều dương), thì điểm đó là điểm cực tiểu địa phương chặt.

## So sánh điều kiện bậc nhất và điều kiện bậc hai

| Khía cạnh | Điều kiện bậc nhất | Điều kiện bậc hai |
|-----------|--------------------|-------------------|
| **Thông tin sử dụng** | Gradient (độ dốc) | Ma trận Hessian (độ cong) |
| **Điều kiện cần** | $$\nabla f(x^*) = 0$$ | $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succeq 0$$ |
| **Điều kiện đủ (không ràng buộc)** | Không đủ với hàm tổng quát (chỉ đủ nếu $$f$$ lồi) | $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succ 0$$ |
| **Mức độ chặt** | Yếu hơn | Mạnh hơn |
| **Chi phí tính toán** | $$O(n)$$ | $$O(n^2)$$ |
| **Khả năng phân loại** | Chỉ xác định điểm dừng | Phân biệt cực tiểu, cực đại và điểm yên ngựa |

## Công cụ minh họa tương tác

Khám phá trực quan cách hoạt động của các điều kiện bậc hai trong thực tế:

<div style="text-align: center; margin: 20px 0;">
    <a href="../second_order_conditions_interactive.html" target="_blank" 
       style="display: inline-block; padding: 12px 24px; background-color: #e74c3c; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        🎯 Khởi động Công cụ Khám phá Điều kiện Bậc Hai
    </a>
</div>

Công cụ tương tác này minh họa:
- **Phân tích giá trị riêng của ma trận Hessian** cho nhiều dạng hàm khác nhau.
- **Phân loại trực quan** các điểm dừng (cực tiểu, cực đại, điểm yên ngựa).
- **Đồ thị đường đồng mức** thể hiện hành vi độ cong cục bộ của hàm số.
- **Các bước tính toán chi tiết** cho kiểm tra điều kiện bậc hai.

### Điều kiện tối ưu bậc nhất trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/first-order-optimality_vi.mp4"></video>
</div>

∇f(x*)ᵀ(y − x*) ≥ 0 trên một tam giác: kiểm tra bằng các đỉnh, nón pháp tuyến, gradient chiếu, nghiệm ở đỉnh, và 9 điểm dừng của ví dụ không lồi.

## Tóm tắt và điểm chính

Các điều kiện tối ưu bậc hai cho phép **đặc trưng hóa chính xác hơn** bản chất của các điểm dừng:

### **Kết quả chính:**
1. **Điều kiện cần:** $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succeq 0$$.
2. **Điều kiện đủ:** $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succ 0$$.
3. **Khả năng phân loại:** Phân biệt rõ ràng giữa điểm cực tiểu, điểm cực đại và điểm yên ngựa.

### **Ý nghĩa thực tế:**
- **Thiết kế thuật toán:** Là cơ sở của các phương pháp kiểu Newton.
- **Kiểm tra tính lồi:** Hỗ trợ xác minh tính lồi của hàm khả vi cấp hai.
- **Độ tin cậy lý thuyết:** Cung cấp điều kiện chặt hơn so với chỉ dùng thông tin bậc nhất.
- **Liên kết lý thuyết:** Góp phần kết nối phân tích cực trị địa phương với tối ưu toàn cục.

### **Cân nhắc về tính toán:**
- **Chi phí:** Việc tính và lưu trữ ma trận Hessian có độ phức tạp $$O(n^2)$$.
- **Xấp xỉ Hessian:** Các phương pháp tựa Newton (Quasi-Newton) giúp giảm chi phí này khi số chiều $$n$$ lớn.
- **Ổn định số:** Việc tính giá trị riêng hoặc phân tích ma trận đòi hỏi cài đặt số cẩn thận.

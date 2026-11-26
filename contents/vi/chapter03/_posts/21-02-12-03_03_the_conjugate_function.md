---
layout: post
title: 03-03 Hàm liên hợp
chapter: '03'
order: 7
owner: Minjoo Lee
categories:
- chapter03
lang: vi
lesson_type: required
---

Trong vật lý cơ học, phép biến đổi Legendre đổi góc nhìn từ vị trí–vận tốc sang vị trí–động lượng để chuyển phương trình Lagrange thành phương trình Hamilton đầy đối xứng. Trong tối ưu hóa lồi, Werner Fenchel mở rộng ý tưởng đó cho *mọi* hàm số (kể cả không trơn, không lồi!) thành **hàm liên hợp Fenchel** $$f^*(y) = \sup_{x \in \operatorname{dom} f}(y^T x - f(x))$$: thay vì mô tả một đường cong bằng tập các điểm $$(x, f(x))$$, ta mô tả nó bằng tập hợp tất cả các **siêu phẳng tiếp tuyến có độ dốc $$y$$**!

Hàm liên hợp là chiếc chìa khóa mở thẳng cánh cửa sang lý thuyết đối ngẫu Fenchel–Rockafellar và đối ngẫu Lagrange trong các chương tiếp theo.

## Kiến thức cần nhớ: Bốn tính chất kỳ diệu của Hàm liên hợp $$f^*$$

- **Ý nghĩa hình học (Độ chênh lớn nhất theo độ dốc $$y$$):** $$f^*(y)$$ đo khoảng cách thẳng đứng lớn nhất giữa đường thẳng đi qua gốc có độ dốc $$y$$ (là $$y^T x$$) và đồ thị $$f(x)$$; nói cách khác, $$-f^*(y)$$ chính là tung độ gốc của tiếp tuyến có độ dốc $$y$$ nằm sát ngay dưới đồ thị $$f$$.
- **$$f^*$$ LUÔN là hàm lồi:** Vì $$f^*(y) = \sup_x (y^T x - f(x))$$ là cận trên đúng theo $$x$$ của một họ các hàm **affine** theo $$y$$, nên dù $$f$$ ban đầu có không lồi đến đâu, $$f^*$$ vẫn luôn là hàm lồi đóng!
- **Bất đẳng thức Fenchel–Young:** Từ định nghĩa suy ra ngay $$f(x) + f^*(y) \ge y^T x$$ với mọi $$x, y$$; dấu bằng xảy ra đúng khi $$y \in \partial f(x)$$ (với hàm trơn là $$y = \nabla f(x)$$).
- **Liên hợp kép (Biconjugate $$f^{**}$$):** Nếu $$f$$ là hàm lồi đóng, thì $$f^{**} = f$$ — biến đổi hai lần đưa ta trở về chính xác hàm ban đầu không mất một chút thông tin nào!

### Giải thích: Tính tay hàm liên hợp $$f^*(y)$$ của $$f(x) = 2x^2$$ và kiểm chứng Fenchel–Young

Xét hàm bậc hai lồi chặt $$f(x) = 2x^2$$ trên $$\mathbb{R}$$:

1. **Thiết lập bài toán cực đại hóa theo $$x$$ (giữ $$y$$ cố định):**
   $$f^*(y) = \sup_{x \in \mathbb{R}} \left(yx - 2x^2\right).$$
2. **Tìm điểm đạt cực đại:** Hàm $$\phi(x) = yx - 2x^2$$ là parabol úp xuống (lõm chặt). Cho đạo hàm theo $$x$$ bằng $$0$$:
   $$\phi'(x) = y - 4x = 0 \implies x^*(y) = \frac{y}{4}.$$
3. **Thay ngược $$x^*$$ để thu được công thức đóng của $$f^*(y)$$:**
   $$f^*(y) = y\left(\frac{y}{4}\right) - 2\left(\frac{y}{4}\right)^2 = \frac{y^2}{4} - \frac{y^2}{8} = \frac{y^2}{8}.$$
   (Tổng quát: liên hợp của $$\frac{1}{2}a x^2$$ là $$\frac{1}{2a} y^2$$ — độ cong $$a$$ bị nghịch đảo thành $$1/a$$!)
4. **Kiểm chứng bất đẳng thức Fenchel–Young $$f(x) + f^*(y) \ge xy$$:**
   - Tại $$x = 3,\ y = 4$$: $$f(3) + f^*(4) = 18 + 2 = 20 > 3 \cdot 4 = 12$$ (dấu chặt).
   - Tại $$x = 1,\ y = f'(1) = 4$$: $$f(1) + f^*(4) = 2 + 2 = 4 = 1 \cdot 4$$ (**đạt dấu bằng**!).

---

Phần này giới thiệu hàm liên hợp (còn gọi là liên hợp lồi hoặc liên hợp Fenchel) — một khái niệm cốt lõi trong giải tích lồi và lý thuyết đối ngẫu, dùng để biến đổi và phân tích các bài toán tối ưu.

## Định nghĩa và nền tảng toán học

Với một hàm $$f: \mathbb{R}^n \to \mathbb{R}$$, **hàm liên hợp** $$f^*: \mathbb{R}^n \to \mathbb{R}$$ được định nghĩa là:

$$f^*(y) = \sup_{x \in \text{dom}(f)} \{y^T x - f(x)\}$$

trong đó $$\sup$$ ký hiệu supremum (cận trên đúng) lấy trên toàn bộ miền xác định của $$f$$.

### Ý nghĩa hình học

Hàm liên hợp có cách hiểu hình học trực quan:
- $$f^*(y)$$ là **hiệu lớn nhất** giữa hàm tuyến tính $$y^T x$$ và hàm gốc $$f(x)$$.
- Về mặt hình học, với siêu phẳng có hệ số góc $$y$$, giá trị $$-f^*(y)$$ là tung độ gốc lớn nhất sao cho siêu phẳng $$y^T x - f^*(y)$$ vẫn nằm phía dưới đồ thị của $$f$$.
- Phép lấy liên hợp chuyển biểu diễn hàm từ không gian biến gốc (không gian nguyên thủy) sang không gian đối ngẫu của các vector độ dốc.

### Vai trò của hàm liên hợp

Hàm liên hợp được sử dụng để:
1. Chuyển bài toán tối ưu gốc thành **bài toán đối ngẫu** tương ứng.
2. Xây dựng công cụ phân tích cho **lý thuyết đối ngẫu** (trình bày ở Chương 11).
3. Cho phép thay thế trực tiếp trong **đối ngẫu Lagrange** mà không cần tính đạo hàm tường minh.
4. Thiết lập liên hệ giữa nghiệm tối ưu nguyên thủy và nghiệm tối ưu đối ngẫu.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/conjugate_function.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hàm liên hợp [2]</figcaption>
</p>
</figure>

### Giải thích trực quan

1. **Hàm tuyến tính và tính lồi:** Với mỗi $$x$$ cố định, hàm $$y \mapsto \langle y, x \rangle - f(x)$$ là hàm affine theo $$y$$, nên vừa lồi vừa lõm. Khi lấy supremum theo $$x$$ của một họ hàm affine như vậy, ta thu được bao trên của chúng.

2. **Bao trên của các đường thẳng luôn tạo thành mặt lồi:** Trong không gian 2D, mỗi hàm affine ứng với một đường thẳng; bao trên của tập các đường thẳng đó không thể có phần lõm xuống nên luôn là một đường cong lồi.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/conjugate_function_2.svg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 2] Giải thích trực quan hàm liên hợp [2]</figcaption>
</p>
</figure>

## Các tính chất cơ bản

### 1. Tính lồi
- **$$f^*$$ luôn là hàm lồi**, bất kể $$f$$ ban đầu có lồi hay không.
- Lý do là $$f^*(y)$$ là supremum theo điểm của họ các hàm affine $$y \mapsto y^T x - f(x)$$, mà supremum của một họ hàm lồi luôn là hàm lồi.

### 2. Bất đẳng thức Fenchel
Với mọi $$x \in \text{dom}(f)$$ và $$y \in \text{dom}(f^*)$$:
$$f(x) + f^*(y) \geq x^T y$$

Bất đẳng thức này thiết lập quan hệ cận dưới cơ bản giữa một hàm và hàm liên hợp của nó.

### 3. Liên hợp kép
- Trong trường hợp tổng quát: $$f^{**} \leq f$$.
- **Nếu $$f$$ đóng và lồi:** $$f^{**} = f$$ (khôi phục lại chính xác hàm ban đầu).

### 4. Quan hệ dưới vi phân
Nếu $$f$$ đóng và lồi, thì với mọi $$x, y$$:
$$y \in \partial f(x) \iff x \in \partial f^*(y) \iff f(x) + f^*(y) = x^T y$$

Quan hệ này thể hiện tính đối xứng giữa không gian nguyên thủy và không gian đối ngẫu.

## Các ví dụ chi tiết

### Ví dụ 1: Logarithm âm
Xét $$f(x) = -\log x$$ với $$x > 0$$.

**Tính toán:**
$$f^*(y) = \sup_{x>0} \{xy + \log x\}$$

Lấy đạo hàm theo $$x$$ và cho bằng 0:
$$\frac{d}{dx}(xy + \log x) = y + \frac{1}{x} = 0$$

Ta thu được $$x^* = -\frac{1}{y}$$ (chỉ hợp lệ khi $$y < 0$$; khi $$y \ge 0$$, biểu thức tiến ra $$+\infty$$ khi $$x \to +\infty$$).

**Kết quả:**
$$f^*(y) = \begin{cases}
-1 - \log(-y), & \text{nếu } y < 0 \\
+\infty, & \text{nếu } y \geq 0
\end{cases}$$

### Ví dụ 2: Hàm bậc hai
Xét $$f(x) = \frac{1}{2}x^T Q x$$ với $$Q \succ 0$$ (đối xứng xác định dương).

**Tính toán:**
$$f^*(y) = \sup_{x} \{y^T x - \frac{1}{2}x^T Q x\}$$

Đặt gradient theo $$x$$ bằng 0:
$$\nabla_x (y^T x - \frac{1}{2}x^T Q x) = y - Qx = 0 \implies x^* = Q^{-1}y$$

Thay $$x^*$$ trở lại biểu thức:
$$f^*(y) = y^T Q^{-1} y - \frac{1}{2}(Q^{-1}y)^T Q (Q^{-1}y) = \frac{1}{2}y^T Q^{-1} y$$

### Ví dụ 3: Giá trị tuyệt đối (một chiều)
Xét $$f(x) = \lvert x \rvert$$ với $$x \in \mathbb{R}$$.

$$f^*(y) = \sup_{x} \{yx - \lvert x \rvert\}$$

**Xét hai trường hợp:**
- Nếu $$\lvert y \rvert \leq 1$$: $$yx - \lvert x \rvert \le 0$$ với mọi $$x$$, nên supremum bằng 0 (đạt tại $$x = 0$$).
- Nếu $$\lvert y \rvert > 1$$: biểu thức không bị chặn trên nên supremum bằng $$+\infty$$.

**Kết quả:**
$$f^*(y) = \begin{cases}
0, & \text{nếu } \lvert y \rvert \leq 1 \\
+\infty, & \text{nếu } \lvert y \rvert > 1
\end{cases}$$

Đây chính là **hàm chỉ thị** của đoạn $$[-1, 1]$$.

### Ví dụ 4: Hàm mũ
Xét $$f(x) = e^x$$ với $$x \in \mathbb{R}$$.

$$f^*(y) = \sup_{x} \{yx - e^x\}$$

Đặt đạo hàm theo $$x$$ bằng 0: $$y - e^x = 0 \implies x^* = \log y$$ (với $$y > 0$$). Khi $$y = 0$$, $$\sup_x (-e^x) = 0$$; khi $$y < 0$$, cho $$x \to -\infty$$ thì $$yx - e^x \to +\infty$$.

**Kết quả:**
$$f^*(y) = \begin{cases}
y \log y - y, & \text{nếu } y > 0 \\
0, & \text{nếu } y = 0 \\
+\infty, & \text{nếu } y < 0
\end{cases}$$

## Ứng dụng trong tối ưu hóa

Hàm liên hợp xuất hiện trong nhiều nội dung quan trọng (sẽ được trình bày kỹ hơn ở Chương 11 và Chương 13):

1. **Đối ngẫu Lagrange:** Chuyển bài toán gốc sang bài toán đối ngẫu.
2. **Đối ngẫu Fenchel:** Khung lý thuyết tổng quát cho đối ngẫu trong tối ưu lồi.
3. **Toán tử gần kề (proximal operator):** Nền tảng của nhiều thuật toán tối ưu hiện đại.
4. **Giải tích biến phân:** Phân tích bài toán tối ưu thông qua các cặp hàm liên hợp.

## Trực quan hóa tương tác

Bạn có thể khám phá cách hoạt động của hàm liên hợp qua công cụ tương tác sau:

<div style="text-align: center; margin: 20px 0;">
    <a href="../conjugate_function_interactive.html" target="_blank" 
       style="display: inline-block; padding: 12px 24px; background-color: #3498db; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        🎯 Khởi động Công cụ Khám phá Hàm Liên hợp Tương tác
    </a>
</div>

Công cụ này cho phép:
- Quan sát song song đồ thị của các hàm quen thuộc và hàm liên hợp của chúng
- Điều chỉnh tham số để theo dõi sự thay đổi của hàm liên hợp
- Khảo sát các đường tiếp tuyến ứng với ý nghĩa hình học của phép lấy liên hợp
- So sánh nhiều ví dụ kèm lời giải thích toán học

## Tóm tắt

Những điểm chính cần ghi nhớ về hàm liên hợp:

1. **Định nghĩa:** $$f^*(y) = \sup_x \{y^T x - f(x)\}$$, chuyển hàm từ không gian nguyên thủy sang không gian đối ngẫu.
2. **Tính lồi:** $$f^*$$ luôn lồi, không phụ thuộc vào tính lồi của $$f$$.
3. **Bất đẳng thức Fenchel:** $$f(x) + f^*(y) \geq x^T y$$.
4. **Liên hệ đối ngẫu:** Khi $$f$$ đóng và lồi, $$f^{**} = f$$, làm cầu nối giữa bài toán nguyên thủy và đối ngẫu trong tối ưu lồi, đối ngẫu Lagrange, các phương pháp gần kề và giải tích biến phân.

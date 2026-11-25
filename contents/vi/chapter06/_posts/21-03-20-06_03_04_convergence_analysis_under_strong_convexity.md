---
layout: post
title: 06-03-04 Convergence analysis under strong convexity
chapter: '06'
order: 13
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Nếu tốc độ hội tụ $$O(1/k)$$ của hàm lồi trơn giống như việc bạn bước đi đều đặn về phía đích, thì khi hàm sở hữu thêm tính **lồi mạnh (strong convexity)**, hành trình ấy biến thành một chuyến tàu siêu tốc: khoảng cách đến nghiệm co lại theo **cấp số nhân** — mỗi vài vòng lặp lại gặt thêm một chữ số thập phân chính xác!

Tại sao một điều kiện tưởng chừng nhỏ như $$\nabla^2 f(x) \succeq m I$$ ($$m > 0$$) lại tạo ra bước nhảy vọt từ $$O(1/\epsilon)$$ xuống $$O(\log(1/\epsilon))$$? Bởi vì tính lồi mạnh đảm bảo **đáy hàm không bao giờ bị bẹt phẳng**: hễ bạn còn cách xa nghiệm tối ưu, độ dốc $$\|\nabla f(x)\|_2$$ chắc chắn còn đủ lớn để đẩy bạn đi nhanh về phía đích (bất đẳng thức Polyak–Łojasiewicz)!

## Kiến thức cần nhớ: Bốn mảnh ghép của Hội tụ Tuyến tính

Để hiểu tận gốc định lý hội tụ dưới tính lồi mạnh, hãy ghép bốn trụ cột sau:

- **Định nghĩa Lồi mạnh $$m$$ (Cận dưới bậc hai):** $$f(y) \ge f(x) + \nabla f(x)^T(y-x) + \frac{m}{2}\|y-x\|_2^2 \; \forall x, y$$ (tương đương $$\nabla^2 f(x) \succeq m I$$ hay $$f(x) - \frac{m}{2}\|x\|_2^2$$ là hàm lồi). Nói trực quan: luôn có thể lót một chiếc bát parabol độ cong $$m$$ nằm gọn *dưới* đồ thị $$f$$.
- **Bất đẳng thức Polyak–Łojasiewicz (PL):** Cực tiểu hóa hai vế của cận dưới bậc hai theo $$y$$ cho ta mối liên hệ vàng giữa độ lớn gradient và sai số hàm mục tiêu:
  $$\|\nabla f(x)\|_2^2 \ge 2m \big(f(x) - f^\star\big).$$
  Hễ còn cách đáy xa, gradient không bao giờ được phép quá nhỏ!
- **Ghép Bổ đề Giảm + Bất đẳng thức PL:** Từ $$f(x^+) \le f(x) - \frac{t}{2}\|\nabla f(x)\|_2^2$$ (với $$t \le 1/L$$), thay $$\|\nabla f(x)\|_2^2 \ge 2m(f(x) - f^\star)$$ cho ngay trong 1 dòng:
  $$f(x^+) - f^\star \le (1 - mt)\big(f(x) - f^\star\big) \implies f(x^{(k)}) - f^\star \le (1 - mt)^k \big(f(x^{(0)}) - f^\star\big).$$
- **Vai trò của Chỉ số điều kiện $$\kappa = L/m$$:** Đặt $$t = 1/L$$, hệ số co là $$c = 1 - m/L = 1 - 1/\kappa$$. Muốn sai số nhỏ hơn $$\epsilon$$, số vòng lặp cần thiết là $$k = O\big(\kappa \log(1/\epsilon)\big)$$ — phụ thuộc *logarit* vào $$\epsilon$$ nhưng *tuyến tính* vào $$\kappa$$!

### Giải thích: Chứng minh và tính số cụ thể tốc độ co lũy thừa theo $$\kappa$$

Xét hàm Ridge Regression 2 biến $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + 5x_2^2) + \frac{1}{2}\lambda(x_1^2 + x_2^2)$$ với $$\lambda = 1$$.
Ta có $$f(x) = \frac{1}{2}(2x_1^2 + 6x_2^2)$$, Hessian $$H = \operatorname{diag}(2, 6)$$.

1. **Bước 1 — Xác định $$m$$, $$L$$ và $$\kappa$$:**
   $$m = 2, \qquad L = 6, \qquad \kappa = \frac{L}{m} = 3.$$
2. **Bước 2 — Tính hệ số co với bước chuẩn $$t = 1/L = 1/6$$:**
   $$1 - mt = 1 - \frac{2}{6} = \frac{2}{3} \approx 0.6667.$$
   (Thậm chí nếu dùng bước $$t = \frac{2}{L+m} = \frac{2}{8} = 0.25$$, khoảng cách co với hệ số $$\frac{\kappa-1}{\kappa+1} = 0.5$$ và sai số hàm co với hệ số $$0.25$$ mỗi bước!)
3. **Bước 3 — Kiểm chứng bằng số tại $$x^{(0)} = (3, 1)^T$$ với $$t = 1/6$$:**
   - $$f(x^{(0)}) = 9 + 3 = 12$$.
   - $$\nabla f(x^{(0)}) = (6, 6)^T \implies x^{(1)} = (3, 1)^T - \frac{1}{6}(6, 6)^T = (2, 0)^T$$.
   - $$f(x^{(1)}) = 4 + 0 = 4$$.
   - Kiểm tra bất đẳng thức lý thuyết: $$f(x^{(1)}) = 4 \le \frac{2}{3} \cdot 12 = 8$$ — hoàn toàn đúng! Chỉ cần $$k = \left\lceil \frac{\ln(12 / 10^{-6})}{\ln(3/2)} \right\rceil = 41$$ bước là chắc chắn đạt sai số $$10^{-6}$$!

---

Một hàm $$f$$ khả vi được gọi là lồi mạnh với hằng số $$m > 0$$ nếu thỏa mãn điều kiện sau:
> $$ \begin{align}
f(y) \ge f(x) + \nabla f(x)^T(y-x) + \frac{m}{2} \| y-x \|_2^2, \quad \forall x, y
\end{align} $$

Nói cách khác, $$f$$ có một cận dưới bậc hai. Khi $$f$$ khả vi hai lần, hằng số $$m$$ được chặn trên bởi giá trị riêng nhỏ nhất của ma trận Hessian của $$f$$.

Tổng quát hơn, hàm $$f$$ lồi mạnh với hằng số $$m > 0$$ khi và chỉ khi:
> $$ \begin{align}
g(x) = f(x) - \frac{m}{2} \| x \|_2^2 \quad \text{là hàm lồi trên miền xác định của } f
\end{align} $$

## Định lý Hội tụ

Khi $$f$$ vừa có gradient liên tục Lipschitz với hằng số $$L$$ vừa lồi mạnh với hằng số $$m$$, ta có kết quả sau:

Thuật toán **gradient descent** với kích thước bước cố định ($$t \le 2/(m + L)$$) hoặc tìm kiếm đường lùi thỏa mãn:
> $$ \begin{align}
f(x^{(k)}) - f^* \le c^k \frac{L}{2} \| x^{(0)} - x^* \|_2^2, \quad c = 1 - \frac{m}{L}, \quad 0 < c < 1
\end{align} $$

## Chứng minh

Vì $$f$$ có gradient liên tục Lipschitz với hằng số $$L$$, hàm $$f$$ thỏa mãn cận trên bậc hai (xem [06-03-01]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})).

Với bước cập nhật gradient descent $$x^+ = x - t \nabla f(x)$$ và chọn kích thước bước $$t = 1/L$$, ta thu được:
> $$ \begin{align}
f(x^+) \le f(x) - \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Trừ hai vế cho $$f(x^*)$$:
> $$ \begin{align}
f(x^+) - f(x^*) \le f(x) - f(x^*) - \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Do $$f$$ lồi mạnh với hằng số $$m$$, ta có bất đẳng thức:
> $$ \begin{align}
f(x) - f(x^*) \le \frac{1}{2m} \| \nabla f(x) \|_2^2
\end{align} $$

Thay bất đẳng thức này vào vế phải ở trên, ta được:
> $$ \begin{align}
f(x^+) - f(x^*) & \le f(x) - f(x^*) - \frac{m}{L} ( f(x) - f(x^*) ) \\
& = \left(1 - \frac{m}{L} \right) ( f(x) - f(x^*) ) \\
& = c ( f(x) - f(x^*) )
\end{align} $$

Áp dụng quy nạp qua $$k$$ bước lặp:
> $$ \begin{align}
f(x^{(k)}) - f(x^*) \le c^k ( f(x^{(0)}) - f(x^*) )
\end{align} $$

Mặt khác, từ cận trên bậc hai áp dụng tại $$y = x^{(0)}$$ và $$x = x^*$$:
> $$ \begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \lVert y - x \rVert^2_2 \quad \forall x, y
\end{align} $$

Vì $$\nabla f(x^*) = 0$$, ta thu được:
> $$ \begin{align}
f(x^{(0)}) & \le f(x^{*}) + \nabla f(x^{*})^T (x^{(0)}- x^{*} ) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\
& = f(x^{*}) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2
\end{align} $$

Suy ra:
> $$ \begin{align}
f(x^{(0)}) - f(x^{*}) & \le \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2
\end{align} $$

Thay vào bất đẳng thức quy nạp trước đó, ta có:
> $$ \begin{align}
f(x^{(k)}) - f(x^{*}) & \le c^k \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2
\end{align} $$

Điều này hoàn tất chứng minh định lý hội tụ của gradient descent dưới giả thiết lồi mạnh.

## Hội tụ Tuyến tính

Khi $$f$$ lồi mạnh, sai số giảm theo tốc độ $$O(c^k)$$, tức là hội tụ theo cấp số nhân (hội tụ tuyến tính). Để đạt $$f(x^{(k)}) - f^{*} \le \epsilon$$, thuật toán chỉ cần $$O(\log(1/\epsilon))$$ vòng lặp (so với $$O(1/\epsilon)$$ vòng lặp khi không có tính lồi mạnh).

Trên đồ thị bán logarit, tốc độ hội tụ $$O(c^k)$$ có dạng một đường thẳng như minh họa dưới đây.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06.03_01_01_Line_Convergence.png" alt="Line_Convergence" width="60%" height="60%">
  <figcaption style="text-align: center;">[Hình 1] Hội tụ tuyến tính [1]</figcaption>
</p>
</figure>

Ở đây, hằng số $$c = 1 - \frac{m}{L}$$ phụ thuộc trực tiếp vào chỉ số điều kiện $$L/m$$ (tỉ số giữa giá trị riêng lớn nhất và nhỏ nhất của Hessian). Chỉ số điều kiện càng lớn thì $$c$$ càng gần 1 và tốc độ hội tụ càng chậm.

Cấu trúc đại số của chứng minh này — kết hợp bổ đề giảm (descent lemma) với một cận dưới liên hệ $$\|\nabla f\|^2$$ và độ chênh lệch giá trị hàm — vẫn giữ nguyên hiệu lực khi giả thiết lồi mạnh được nới lỏng thành bất đẳng thức Polyak–Łojasiewicz. Nội dung mở rộng tùy chọn về tốc độ hội tụ hiện đại này, cùng ví dụ bài toán bình phương tối thiểu quá tham số (nơi nghiệm cực tiểu không duy nhất), được trình bày tại [28-05 Điều kiện PL và câu chuyện tốc độ hiện đại]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}).

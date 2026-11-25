---
layout: post
title: 06-02-02 Tìm kiếm đường lùi
chapter: '06'
order: 7
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Trong hầu hết các bài toán tối ưu phi tuyến thực tế (như hồi quy logistic hay tối ưu hàm log-sum-exp), việc tính trước hằng số Lipschitz toàn cục $$L$$ rất khó, hoặc $$L$$ toàn cục quá lớn so với độ cong thực tế ở vùng thuật toán đang đi qua. Nếu chọn bước cố định $$1/L$$ toàn cục, bạn buộc phải "bò từng milimet" ngay cả trên những vùng phẳng rộng thênh thang!

**Tìm kiếm đường lùi (Backtracking Line Search / Điều kiện Armijo)** giải quyết triệt để vấn đề này bằng một cơ chế thông minh đến kinh ngạc: ở mỗi bước, cứ mạnh dạn thử bước dài $$t = 1$$ trước; chỉ khi thấy hàm mục tiêu *không giảm đủ mạnh* so với kỳ vọng tuyến tính, ta mới rút ngắn bước đi theo hệ số $$\beta \in (0, 1)$$ cho đến khi đạt chuẩn!

## Bản đồ kiến thức nền: Cơ chế "Đường thẳng Armijo" trong Backtracking

Ba trụ cột sau làm rõ ý nghĩa hình học và cách chọn tham số của Backtracking Line Search:

- **Điều kiện giảm đủ Armijo (Sufficient Decrease Condition):** Với $$\alpha \in (0, 0.5]$$ (thường chọn $$\alpha = 0.01 \text{ đến } 0.3$$), ta chấp nhận bước $$t$$ khi:
  $$f(x - t\nabla f(x)) \le f(x) - \alpha t \|\nabla f(x)\|_2^2.$$
  Về mặt hình học, vế phải là một đường thẳng có độ dốc *thoai thoải hơn* tiếp tuyến tại $$x$$ (chỉ lấy một phần $$\alpha$$ của độ dốc ban đầu). Ta chỉ cần đồ thị hàm số nằm **dưới** đường thẳng này!
- **Tại sao vòng lặp `while` luôn dừng sau hữu hạn bước?** Vì theo khai triển Taylor bậc nhất, với $$t$$ đủ nhỏ ta có $$f(x - t\nabla f(x)) \approx f(x) - t\|\nabla f(x)\|_2^2 < f(x) - \alpha t\|\nabla f(x)\|_2^2$$ (do $$\alpha < 1$$). Thậm chí với hàm $$L$$-trơn, điều kiện chắc chắn thỏa mãn ngay khi $$t \le \frac{2(1-\alpha)}{L}$$ (hoặc $$t \le 1/L$$ khi $$\alpha \le 0.5$$)!
- **Chọn tham số $$\alpha$$ và $$\beta$$ trong thực tế:** $$\beta \in (0, 1)$$ là hệ số co bước (thường chọn $$\beta = 0.5$$ hoặc $$0.8$$). Chọn $$\beta$$ lớn (như $$0.8$$) tìm được bước sát tối ưu hơn nhưng tốn nhiều lần thử hàm hơn; $$\beta = 0.5$$ là điểm cân bằng kinh điển vừa nhanh vừa chắc chắn.

### Khung giải thích (nên đọc chậm): Chạy tay vòng lặp Backtracking Line Search từng phép thử

Xét hàm $$f(x) = x^2 + e^x$$ tại $$x = 1$$. Ta có:
- $$f(1) = 1 + e \approx 3.7183$$.
- $$f'(1) = 2(1) + e \approx 4.7183$$, suy ra $$(f'(1))^2 \approx 22.262$$.
Dùng Backtracking với $$t_{\text{init}} = 1,\; \alpha = 0.3,\; \beta = 0.5$$. Điều kiện cần thỏa:
$$f(1 - 4.7183 t) \le 3.7183 - 0.3 \cdot t \cdot 22.262 = 3.7183 - 6.6786 t.$$

1. **Lần thử 1 ($$t = 1$$):**
   - Điểm thử: $$x_{\text{try}} = 1 - 4.7183 = -3.7183$$.
   - Vế trái: $$f(-3.7183) = (-3.7183)^2 + e^{-3.7183} \approx 13.826 + 0.024 = 13.850$$.
   - Vế phải: $$3.7183 - 6.6786 = -2.960$$.
   - So sánh: $$13.850 \le -2.960$$? **Sai!** (Bước $$t=1$$ nhảy quá đà lên tận $$13.85$$!). Co bước $$t \leftarrow 0.5$$.
2. **Lần thử 2 ($$t = 0.5$$):**
   - Điểm thử: $$x_{\text{try}} = 1 - 2.3591 = -1.3591$$.
   - Vế trái: $$f(-1.3591) \approx 1.847 + 0.257 = 2.104$$.
   - Vế phải: $$3.7183 - 3.3393 = 0.379$$.
   - So sánh: $$2.104 \le 0.379$$? **Sai!** (Dù hàm đã giảm từ $$3.72$$ xuống $$2.10$$, mức giảm chưa đạt chuẩn Armijo!). Co bước $$t \leftarrow 0.25$$.
3. **Lần thử 3 ($$t = 0.25$$):**
   - Điểm thử: $$x_{\text{try}} = 1 - 1.1796 = -0.1796$$.
   - Vế trái: $$f(-0.1796) \approx 0.032 + 0.836 = 0.868$$.
   - Vế phải: $$3.7183 - 1.6697 = 2.049$$.
   - So sánh: $$0.868 \le 2.049$$? **ĐÚNG!** Dừng vòng lặp, chấp nhận $$t = 0.25$$ và cập nhật $$x_1 = -0.1796$$ (giảm hàm mục tiêu hơn 4 lần ngay bước đầu tiên!).

---

Quy tắc cập nhật cơ bản của gradient descent là:
$$x_{k+1} = x_k - t_k \nabla f(x_k),$$
trong đó $$x_k$$ là vector tham số tại lần lặp $$k$$, $$\nabla f(x_k)$$ là gradient và $$t_k > 0$$ là kích thước bước (tốc độ học).

Nếu sử dụng kích thước bước cố định, mức cập nhật không thích nghi với sự thay đổi độ cong của hàm số, dễ dẫn đến vượt quá cực tiểu hoặc tiến triển chậm ở các vùng điều kiện xấu. Để khắc phục, ta có thể chọn kích thước bước một cách thích ứng tại từng bước lặp. Một phương pháp phổ biến là **tìm kiếm đường lùi (backtracking line search)**.

### Tìm kiếm Đường lùi là gì?

Phương pháp này thử một kích thước bước từ vị trí hiện tại; nếu bước thử quá lớn (không làm hàm mục tiêu giảm đủ mức yêu cầu), thuật toán sẽ thu nhỏ kích thước bước lại. Hình dưới đây minh họa cách tìm kiếm đường lùi xác định kích thước bước.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Backtracking_Line_Search.png" alt="backtrackinglinesearch1" width="100%" height="100%">
  <figcaption style="text-align: center;">[Hình 1] Tìm kiếm đường lùi [3]</figcaption>
</p>
</figure>

Các phương pháp tìm kiếm đường (line search) chọn $$t_k$$ nhằm đảm bảo mức giảm đủ lớn của $$f$$ dọc theo hướng giảm $$d_k = -\nabla f(x_k)$$. Tìm kiếm đường chính xác giải bài toán $$t_k = \arg\min_{t > 0} f(x_k + t d_k)$$, nhưng việc này tốn kém về tính toán đối với các hàm $$f$$ không phải bậc hai. Tìm kiếm đường không chính xác (inexact line search) khắc phục bằng cách chỉ đòi hỏi mức giảm vừa đủ; trong đó, tìm kiếm đường lùi được dùng rộng rãi nhờ tính đơn giản và đảm bảo lý thuyết tốt.

Trên hàm lồi $$f$$, xét mặt cắt dọc theo hướng giảm $$\Delta x$$. Đường tiếp tuyến phía dưới luôn nằm dưới đồ thị hàm lồi nên không thể dùng làm ngưỡng kiểm tra bước nhảy. Do đó, tìm kiếm đường lùi sử dụng một đường thẳng phía trên có độ dốc thoải hơn (nhân thêm hệ số $$\alpha \in (0, 1/2]$$). Nếu $$f(x + t \Delta x)$$ nằm phía trên đường thẳng này thì bước $$t$$ quá lớn; ngược lại, nếu nằm phía dưới thì bước $$t$$ được chấp nhận.

Khi bước thử quá lớn, $$t$$ được nhân liên tiếp với $$\beta \in (0, 1)$$ cho đến khi giá trị hàm rơi xuống dưới đường thẳng kiểm tra. Giá trị $$t$$ cuối cùng luôn nằm trong khoảng $$0 < t \le t_0$$.

### Thuật toán Tìm kiếm Đường lùi

Với hướng giảm $$\Delta x = - \nabla f(x)$$, thuật toán được tóm tắt như sau:

1. Khởi tạo các tham số $$0 < \beta < 1$$ và $$0 < \alpha \le 1/2$$.
2. Tại mỗi lần lặp, đặt $$t = t_{\text{init}}$$ (thường chọn $$t_{\text{init}} = 1$$).
3. Trong khi $$f(x - t \nabla f(x)) > f(x) - \alpha t \|\nabla f(x)\|_2^2$$, cập nhật $$t = \beta t$$.
4. Cập nhật $$x^+ = x - t \nabla f(x)$$.
5. Nếu tiêu chuẩn dừng chưa được thỏa mãn, quay lại bước 2.

Tìm kiếm đường lùi đơn giản và hiệu quả trong thực tế. Tham số $$\alpha$$ kiểm soát độ dốc của đường thẳng điều kiện giảm đủ, còn $$\beta$$ xác định mức độ thu nhỏ bước ở mỗi lần lùi. Thông thường, người ta chọn $$\alpha = 1/2$$ và $$\beta$$ gần với 1.

### Ví dụ về Tìm kiếm Đường lùi

Nhờ kích thước bước thích ứng, số bước cập nhật chính giảm đáng kể so với kích thước bước cố định (ví dụ: 12 bước cập nhật so với 100 bước trên cùng bài toán). Kể cả khi tính thêm các bước thử lùi, tổng số lần đánh giá hàm để hội tụ vào khoảng 40 bước.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Convergence.png" alt="backtrackinglinesearch1" width="70%" height="70%">
  <figcaption style="text-align: center;">[Hình 2] Hội tụ với tìm kiếm đường lùi [3]</figcaption>
</p>
</figure>

### Trực giác của Điều kiện Giảm đủ

Xét xấp xỉ bậc hai của $$f$$ quanh $$x$$:
> $$f(y) \approx f(x) + \nabla f(x)^T(y-x) + \frac{1}{2t} \|y - x\|_2^2$$

Thay $$y = x - t \nabla f(x)$$ vào vế phải, ta được:
> $$
> \begin{align}
> f(x - t \nabla f(x)) &\approx f(x) - t \|\nabla f(x)\|_2^2 + \frac{1}{2}t \|\nabla f(x)\|_2^2 = f(x) - \frac{t}{2} \|\nabla f(x)\|_2^2
> \end{align}
> $$

### Tìm kiếm đường lùi và chính xác trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/line-search_vi.mp4"></video>
</div>

Bước cố định quá nhỏ hay quá lớn, điều kiện Armijo và các lần lùi t ← βt, so với tìm kiếm chính xác trên ví dụ của bài.

---
layout: post
title: '08-01-01 Lựa chọn kích thước bước'
chapter: '08'
order: 3
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
lesson_type: required
---

Nếu bạn bịt mắt đi xuống một khe núi hẹp mà không thể đo xem bước tiếp theo có thấp hơn chỗ đang đứng hay không, bạn sẽ quyết định độ dài mỗi bước như thế nào? Bước quá to thì bạn cứ nhảy qua nhảy lại giữa hai vách núi mãi không dừng; bước thu nhỏ quá nhanh thì bạn kiệt sức đứng im giữa chừng khi chưa kịp chạm đáy. Đó chính xác là thế lưỡng nan của **lựa chọn kích thước bước** trong phương pháp subgradient.

Khác với gradient descent nơi backtracking line search tự động dò bước an toàn nhờ điều kiện giảm Armijo, phương pháp subgradient không có bảo chứng giảm đơn điệu nên buộc phải đặt lịch kích thước bước ngay từ đầu. Chính hai điều kiện tưởng chừng trừu tượng của giải tích chuỗi — $$\sum_{k=1}^{\infty} t_k = \infty$$ và $$\sum_{k=1}^{\infty} t_k^2 < \infty$$ — lại gói trọn đúng trực giác vật lý: tổng quãng đường phải vô hạn để đi tới bất kỳ điểm tối ưu nào dù xa đến đâu, nhưng bước phải nhỏ dần đủ nhanh để dập tắt hoàn toàn dao động quanh điểm gãy.

## Bản đồ kiến thức nền: Ba trụ cột đằng sau lịch kích thước bước

Để chọn đúng quy tắc bước cho bài toán thực tế và hiểu gốc rễ toán học của chúng, hãy kết nối ba mảng kiến thức sau:

- **Chuỗi số điều hòa và chuỗi $$p$$-series (Giải tích thực):** Điều kiện không khả tổng $$\sum t_k = \infty$$ nhưng khả tổng bình phương $$\sum t_k^2 < \infty$$ chọn đúng vùng "vàng" $$t_k \sim c / k^p$$ với $$\frac{1}{2} < p \le 1$$. Chẳng hạn $$t_k = 1/k$$ thỏa cả hai ($$\sum 1/k = \infty$$, $$\sum 1/k^2 = \pi^2/6 < \infty$$), còn $$t_k = 1/\sqrt{k}$$ vi phạm điều kiện thứ hai vì $$\sum 1/k = \infty$$.
- **Đánh đổi giữa thiên lệch (bias) và độ dao động (variance/floor):** Với bước cố định $$t_k = t$$, thuật toán không bao giờ dừng lại hẳn tại điểm gãy mà dao động trong một vùng bán kính tỷ lệ thuận với $$t$$ (sai số dư bậc $$G^2 t / 2$$). Giảm $$t$$ giúp đáy sai số nhỏ hơn nhưng kéo dài thời gian tiếp cận từ xa.
- **Lịch bước theo ngân sách vòng lặp hữu hạn (Horizon-aware Steps):** Trong thực hành, ta hiếm khi chạy vô hạn bước. Nếu biết trước sẽ chạy đúng $$K$$ vòng lặp, chọn bước cố định tối ưu $$t = \frac{R}{G\sqrt{K}}$$ (hoặc bước giảm dần $$t_k = \frac{c}{\sqrt{k}}$$) thường cho tốc độ nhanh hơn nhiều so với $$t_k = 1/k$$ vốn co bước quá sớm.

### Khung giải thích (nên đọc chậm): So sánh 3 lịch bước bằng tay trên hàm $$f(x) = |x|$$

Xét bài toán cực tiểu hóa $$f(x) = |x|$$ (nghiệm $$x^* = 0$$, $$g(x) = \operatorname{sign}(x)$$ với $$|g| = 1$$).

1. **Bước cố định $$t_k = 1$$ từ $$x^{(0)} = 1.5$$:**
   - $$x^{(1)} = 1.5 - 1(1) = 0.5$$ ($$f = 0.5$$)
   - $$x^{(2)} = 0.5 - 1(1) = -0.5$$ ($$f = 0.5$$)
   - $$x^{(3)} = -0.5 - 1(-1) = 0.5$$ ($$f = 0.5$$)
   Thuật toán mắc kẹt mãi trong chu kỳ dao động $$0.5 \leftrightarrow -0.5$$, không bao giờ tiến dưới mức sai số $$0.5$$.
2. **Bước giảm quá nhanh $$t_k = (0.5)^k$$ từ $$x^{(0)} = 3$$ (vi phạm $$\sum t_k = \infty$$):**
   - Tổng quãng đường tối đa có thể đi sau vô hạn bước là $$\sum_{k=1}^{\infty} (0.5)^k = 0.5 + 0.25 + 0.125 + \dots = 1.$$
   - Vì vậy $$x^{(k)} > 3 - 1 = 2$$ với mọi $$k$$! Thuật toán "chết máy" ngay tại $$x = 2$$ dù cách nghiệm $$x^* = 0$$ tới 2 đơn vị.
3. **Bước giảm dần đúng chuẩn $$t_k = 1/k$$ từ $$x^{(0)} = 1.5$$ (thỏa $$\sum t_k = \infty$$ và $$\sum t_k^2 < \infty$$):**
   - $$x^{(1)} = 1.5 - 1(1) = 0.5$$
   - $$x^{(2)} = 0.5 - 0.5(1) = 0$$ — chạm đúng nghiệm tối ưu $$x^* = 0$$!
   Ngay cả khi không chạm trúng $$0$$ ở bước 2 (ví dụ bắt đầu từ $$x^{(0)} = 1.4$$), biên độ dao động quanh $$0$$ sẽ co dần theo $$1/k \to 0$$, bảo đảm hội tụ về đúng $$f^* = 0$$.

Có nhiều cách để lựa chọn **kích thước bước** trong phương pháp subgradient. Dưới đây là hai cách phổ biến:

- **Kích thước bước cố định**: $$t_k = t$$ với mọi $$k = 1, 2, 3, ...$$
- **Kích thước bước giảm dần**: dãy $$t_k$$ thỏa mãn đồng thời hai điều kiện:

>\begin{align}
> \sum_{k=1}^{\infty} t_k = \infty, \quad \sum_{k=1}^{\infty} t_k^{2} < \infty
>\end{align}

### Ví dụ về kích thước bước giảm dần

> $$\begin{align}
& t_k = \frac{1}{k}, k = 1,2,3,... \\
& \sum_{k=1}^{\infty}t_k = \infty \quad \text{(Chuỗi điều hòa)} \\
& \sum_{k=1}^{\infty}t^2_k \approx 1.644934 < \infty \quad \text{(Bài toán Basel)}
\end{align} $$

Một đặc điểm quan trọng của phương pháp subgradient là kích thước bước thường phải được chọn trước, khác với gradient descent. Nói cách khác, không giống tìm kiếm đường thẳng lùi (backtracking line search) trong gradient descent, kích thước bước ở đây không tự điều chỉnh theo độ cong cục bộ của hàm mục tiêu.

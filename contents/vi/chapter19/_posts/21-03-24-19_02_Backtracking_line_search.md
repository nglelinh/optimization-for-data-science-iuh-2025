---
layout: post
title: '19-02 Backtracking line search'
chapter: '19'
order: 6
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Cũng giống như phương pháp Newton cổ điển có thể "nhảy vọt" ra xa vô cùng nếu xuất phát ở vùng xa nghiệm và cứ cố chấp lấy bước đơn vị $$t_k = 1$$, phương pháp Newton proximal cũng cần một "bộ phanh" bảo đảm hội tụ toàn cục. Bộ phanh đó chính là **tìm kiếm theo đường lui (backtracking line search)** phiên bản tổng hợp: vì hàm $$h$$ không khả vi nên không thể thay bằng $$\nabla h(x)^T v$$, ta giữ nguyên độ chênh lệch thực $$h(x + tv) - h(x)$$ (hoặc cận trên tuyến tính $$t(h(x+v) - h(x))$$) trong điều kiện Armijo!

## Kiến thức cần nhớ: Ba cơ chế bảo đảm an toàn của Backtracking tổng hợp

Để hiểu vì sao điều kiện dừng backtracking trong bài vừa luôn kết thúc sau hữu hạn bước, vừa tự động nhận $$t = 1$$ khi gần nghiệm, hãy chú ý ba điểm:

- **Đạo hàm có hướng của hàm tổng hợp $$f = g + h$$:** Với mọi $$t \in (0, 1]$$, nhờ tính lồi của $$h$$, ta luôn có $$h(x + tv) - h(x) \le t(h(x + v) - h(x))$$. Do đó, đại lượng $$\Delta(x, v) = \nabla g(x)^T v + h(x + v) - h(x) \le -v^T H v < 0$$ đóng vai trò tốc độ giảm kỳ vọng theo hướng $$v$$.
- **Điều kiện giảm đủ Armijo tổng hợp:** Yêu cầu $$f(x + tv) \le f(x) + \alpha t \nabla g(x)^T v + \alpha(h(x + tv) - h(x))$$ (với $$0 < \alpha \le 1/2$$) đảm bảo mức giảm thực tế đạt ít nhất một tỉ lệ $$\alpha$$ của mức giảm mô hình bậc nhất–tổng hợp.
- **Chuyển pha tự động sang bước đơn vị $$t = 1$$:** Khi $$x$$ tiến đủ gần $$x^\star$$ và $$\alpha < 1/2$$, khai triển Taylor bậc hai cho thấy điều kiện Armijo **luôn được thỏa mãn ngay tại $$t = 1$$**. Nhờ vậy, backtracking không bao giờ cản trở tốc độ hội tụ bậc hai cục bộ của Newton proximal!

### Giải thích: Chạy tay backtracking line search trên hàm mũ có phạt $$\ell_1$$

Xét bài toán $$f(x) = \underbrace{e^x - x}_{g(x)} + \underbrace{0.5 |x|}_{h(x)}$$ tại $$x = 2$$, với $$\alpha = 0.25, \beta = 0.5$$:

1. **Tính giá trị ban đầu và hướng Newton proximal $$v$$ tại $$x = 2$$:**
   - $$g(2) = e^2 - 2 \approx 5.3891$$, $$h(2) = 1.0 \implies f(2) \approx 6.3891$$.
   - $$g'(2) = e^2 - 1 \approx 6.3891$$, $$H = g''(2) = e^2 \approx 7.3891$$.
   - Hướng Newton proximal: $$x + v = S_{0.5/7.3891}\!\left(2 - \frac{6.3891}{7.3891}\right) = S_{0.0677}(1.1353) = 1.0676 \implies v = -0.9324$$.
2. **Thử bước đơn vị $$t = 1$$ ($$x^+ = 1.0676$$):**
   - Giá trị thực mới: $$f(1.0676) = e^{1.0676} - 1.0676 + 0.5(1.0676) \approx 2.9084 - 1.0676 + 0.5338 = 2.3746$$.
   - Ngưỡng vế phải Armijo:
     $$f(2) + 0.25(1)(6.3891)(-0.9324) + 0.25(0.5338 - 1.0) = 6.3891 - 1.4893 - 0.1166 = 4.7832.$$
   - So sánh: $$2.3746 \le 4.7832$$ — **thỏa mãn ngay ở lần thử đầu tiên!** Bước $$t = 1$$ được chấp nhận ngay lập tức.
3. **Khi nào backtracking phải thu nhỏ $$t$$?** Nếu hàm $$g$$ có độ cong tăng vọt đột ngột ở phía bước đi (ví dụ $$g(x) = e^{-5x} + x^2$$ tại $$x = 1$$ khiến bước $$t = 1$$ nhảy sang vùng $$x < 0$$ nơi $$e^{-5x}$$ bùng nổ), thì $$f(x + v) > \text{ngưỡng}$$, và vòng lặp sẽ tự động giảm $$t = 0.5, 0.25, \dots$$ cho tới khi rơi vào vùng giảm thực sự.

---

Tương tự phương pháp Newton cổ điển, **phương pháp Newton proximal** có thể không hội tụ nếu luôn dùng bước đơn vị $$t_k = 1$$ ($$k = 1, 2, 3, \dots$$). Vì vậy, cần chọn độ dài bước phù hợp bằng tìm kiếm theo đường lui (backtracking line search).

## Thuật toán tìm kiếm theo đường lui (Backtracking line search)

1. Khởi tạo các tham số $$0 \lt \alpha \le 1/2$$ và $$0 \lt \beta \lt 1$$.
2. Ở mỗi vòng lặp, tính hướng Newton proximal $$v = \text{prox}_{H} ( x - H^{-1} \nabla g (x) ) - x$$.
3. Khởi tạo $$t = 1$$.
4. Khi điều kiện $$f(x + tv) \gt f(x) + \alpha t \nabla g(x)^T v + \alpha (h(x + tv) - h(x))$$ còn đúng, giảm $$t = \beta t$$ và lặp lại kiểm tra (với $$f = g + h$$).
5. Cập nhật nghiệm $$x^+ = x + tv$$.
6. Nếu chưa đạt điều kiện dừng, quay lại bước 2.

Về mặt trực giác, ta tìm độ dài bước $$t$$ sao cho mức giảm thực tế của $$f = g + h$$ dọc theo hướng $$v$$ đạt ít nhất tỷ lệ $$\alpha$$ so với mức giảm dự báo cục bộ. Do phần $$h$$ không khả vi, sự thay đổi của nó được đánh giá trực tiếp qua hiệu $$h(x + tv) - h(x)$$ thay vì đạo hàm.

## Hiệu quả tính toán
Có nhiều biến thể của backtracking line search; cách trình bày ở trên có một ưu điểm tính toán rất đáng chú ý: toán tử prox chỉ cần tính **một lần duy nhất** để xác định hướng $$v$$ trước khi vào vòng lặp giảm $$t$$. Trái lại, trong proximal gradient descent tiêu chuẩn, toán tử prox thường phải được tính lại ở mỗi lần thử độ dài bước bên trong vòng lặp. Nhờ đó, lược đồ này đặc biệt hiệu quả khi việc đánh giá toán tử prox có tỉ lệ tốn kém.

### [Tham khảo] Backtracking line search cho các phương pháp khác
* Gradient descent: [06-02-02 Backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %})
* Proximal gradient descent: [09-02 Phân tích hội tụ]({% multilang_post_url contents/chapter09/20-01-08-09_02_convergence_analysis %})
* Phương pháp Newton: [14-04 Backtracking line search]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %})

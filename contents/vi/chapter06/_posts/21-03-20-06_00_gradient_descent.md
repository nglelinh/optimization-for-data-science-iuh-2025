---
layout: post
title: 06 Gradient Descent
chapter: '06'
order: 1
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Hãy tưởng tượng bạn bị thả xuống một sườn núi mịt mù sương trắng vào lúc chập tối, không có bản đồ toàn cảnh, chỉ có chiếc đèn pin rọi đủ thấy độ dốc ngay dưới chân mình. Làm sao để đi xuống tận đáy thung lũng? Quy tắc trực giác nhất của con người cũng chính là thuật toán làm nên cuộc cách mạng trí tuệ nhân tạo hiện đại: **cảm nhận hướng dốc xuống gắt nhất tại chỗ đang đứng, bước đi một bước vừa phải, rồi lặp lại**!

Chương 06 mở ra thế giới của các **thuật toán tối ưu hóa bậc nhất** bắt đầu từ **Gradient Descent (Hạ Gradient)**. Nếu các chương trước trả lời câu hỏi *"thế nào là một bài toán lồi đẹp và điều kiện tối ưu trông ra sao?"*, thì từ chương này trở đi ta trả lời câu hỏi thực chiến hơn nhiều: *"làm sao máy tính thực sự tìm ra nghiệm $$x^\star$$ với hàng triệu hay hàng tỷ biến?"*

## Kiến thức cần nhớ: Bốn trụ cột của Chương 06 — Gradient Descent

Toàn bộ 23 bài học trong chương này xoay quanh bốn câu hỏi cốt lõi của phương pháp hạ gradient:

- **Cơ chế bước nhảy & Hình học độ cong:** Tại sao quy tắc $$x^{(k+1)} = x^{(k)} - t_k \nabla f(x^{(k)})$$ lại xuất phát từ việc cực tiểu hóa một parabol xấp xỉ địa phương thay cho ma trận Hessian đầy đủ?
- **Chiến lược chọn kích thước bước (Step Size Selection):** Bước quá nhỏ thì đi mãi không tới đích; bước quá lớn thì vọt qua đáy và phân kỳ. Chương này phân tích ba chiến lược kinh điển: bước cố định (fixed), tìm kiếm đường lùi (backtracking) và tìm kiếm đường chính xác (exact line search).
- **Lý thuyết hội tụ định lượng (Convergence Analysis):** Dưới điều kiện $$L$$-trơn (gradient Lipschitz), GD hội tụ với tốc độ $$O(1/k)$$; nếu thêm tính lồi mạnh $$m$$, tốc độ nhảy vọt lên hội tụ tuyến tính $$O(c^k)$$ phụ thuộc vào chỉ số điều kiện $$\kappa = L/m$$.
- **Mở rộng thực chiến cho Học máy quy mô lớn:** Từ Gradient Boosting (hạ gradient trong không gian hàm), Stochastic Gradient Descent (SGD cho dữ liệu lớn), Momentum (quán tính phá thế zíc-zắc), cho đến Điều chuẩn (Ridge/Lasso) và các thuật toán hiện đại như Lion hay Schedule-Free.

### Giải thích: Chạy tay 3 bước Gradient Descent để cảm nhận nhịp hội tụ

Xét hàm lồi bậc hai đơn giản $$f(x) = \frac{1}{2}(x - 4)^2$$ với đạo hàm $$f'(x) = x - 4$$ và nghiệm tối ưu $$x^\star = 4,\; f^\star = 0$$. Bắt đầu từ $$x^{(0)} = 0$$ với kích thước bước cố định $$t = 0.5$$:

1. **Bước $$k = 0$$:** $$x^{(0)} = 0 \implies f'(0) = -4$$. Cập nhật:
   $$x^{(1)} = 0 - 0.5(-4) = 2, \qquad f(2) = \frac{1}{2}(-2)^2 = 2.$$
2. **Bước $$k = 1$$:** $$x^{(1)} = 2 \implies f'(2) = -2$$. Cập nhật:
   $$x^{(2)} = 2 - 0.5(-2) = 3, \qquad f(3) = \frac{1}{2}(-1)^2 = 0.5.$$
3. **Bước $$k = 2$$:** $$x^{(2)} = 3 \implies f'(3) = -1$$. Cập nhật:
   $$x^{(3)} = 3 - 0.5(-1) = 3.5, \qquad f(3.5) = \frac{1}{2}(-0.5)^2 = 0.125.$$
4. **Quy luật hiện ra:** Sau mỗi bước, khoảng cách tới nghiệm $$|x^{(k)} - 4|$$ giảm đúng một nửa ($$4 \to 2 \to 1 \to 0.5$$), còn sai số hàm mục tiêu giảm đi **4 lần** ($$8 \to 2 \to 0.5 \to 0.125$$)! Nhưng nếu ta chọn tham lam $$t = 2.5$$, thì $$x^{(1)} = 10,\; x^{(2)} = -5,\; x^{(3)} = 17.5 \to \infty$$ — phân kỳ ngay lập tức!

---

Trong chương này, chúng ta sẽ tìm hiểu **Gradient Descent** (thuật toán hạ gradient), một trong những phương pháp cơ bản và quan trọng nhất trong tối ưu hóa.

Trong các thuật toán tối ưu hóa, việc lựa chọn hướng tìm kiếm và kích thước bước đóng vai trò quyết định đối với tốc độ và khả năng hội tụ. Gradient descent di chuyển theo hướng ngược chiều gradient (hướng gradient âm). Kích thước bước có thể được giữ cố định hoặc điều chỉnh thích ứng, và cả hai cách tiếp cận này sẽ được trình bày trong chương này.

Để gradient descent hội tụ, hàm mục tiêu cần thỏa mãn một số điều kiện nhất định. Khi các điều kiện này được đáp ứng, ta có thể phân tích tốc độ hội tụ của thuật toán. Nếu hàm mục tiêu có thêm tính lồi mạnh, quá trình hội tụ sẽ diễn ra nhanh hơn đáng kể; chương này cũng sẽ phân tích cụ thể tốc độ hội tụ trong trường hợp đó.

Bên cạnh nền tảng lý thuyết, chúng ta sẽ xem xét các ứng dụng và biến thể quan trọng của gradient descent, bao gồm gradient boosting và stochastic gradient descent.

Bài đọc tùy chọn [06-08 Ứng dụng và phát triển gần đây]({% multilang_post_url contents/chapter06/2026-09-16-06_08_Applications_Recent %}) đối chiếu lý thuyết Lipschitz cổ điển với hiện tượng mép ổn định (edge of stability), thuật toán Lion và phương pháp trung bình không lịch bước (schedule-free averaging) giai đoạn 2021–2024. Tốc độ hội tụ tuyến tính ở mục 06-03-04 vẫn có thể áp dụng cho một số bài toán cực tiểu hóa rủi ro thực nghiệm (ERM) *không lồi* thỏa mãn điều kiện Polyak–Łojasiewicz; nội dung liên kết này được trình bày trong ghi chú tùy chọn [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}).

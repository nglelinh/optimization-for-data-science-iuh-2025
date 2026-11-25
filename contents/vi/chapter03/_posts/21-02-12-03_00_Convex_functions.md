---
layout: post
title: 03 Hàm lồi
chapter: '03'
order: 1
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Nếu Chương 02 vẽ nên "sân chơi" nơi thuật toán được phép di chuyển (tập lồi), thì Chương 03 xây dựng "địa hình" độ cao trên sân chơi đó: **hàm lồi**. Vẻ đẹp của một hàm lồi nằm ở hai phép màu hình học: mọi dây cung nối hai điểm trên đồ thị luôn nằm phía trên đường cong, và mọi mặt phẳng tiếp tuyến tại bất kỳ điểm nào cũng nằm hoàn toàn bên dưới đồ thị — trở thành một "chặn dưới toàn cục" giúp ta biết chắc mình còn cách đáy tối đa bao xa.

Chương 03 sẽ dẫn bạn qua định nghĩa hàm lồi, kho ví dụ kinh điển, các phép toán bảo toàn tính lồi, hàm liên hợp Fenchel, hàm giả lồi, hàm log-lõm và tính lồi theo bất đẳng thức tổng quát.

## Bản đồ kiến thức nền: Bốn nhánh trụ cột của Chương 03

- **Định nghĩa và ba đặc trưng (Bậc 0, Bậc 1, Bậc 2):** Bất đẳng thức Jensen (không cần khả vi), chặn dưới tiếp tuyến $$f(y) \ge f(x) + \nabla f(x)^T(y-x)$$ (khả vi cấp 1) và Hessian bán xác định dương $$\nabla^2 f(x) \succeq 0$$ (khả vi cấp 2).
- **Quy tắc lắp ghép bảo toàn tính lồi (Disciplined Convex Programming):** Tổng trọng số dương, cực đại từng điểm (pointwise max), hợp thành affine, hàm phối cảnh và cực tiểu hóa từng phần — công cụ nhận diện hàm lồi không cần tính Hessian.
- **Hàm liên hợp Fenchel ($$f^*$$):** Phép biến đổi sang không gian độ dốc $$y$$, tạo ra cặp bất đẳng thức Fenchel–Young và là viên gạch cốt lõi xây dựng bài toán đối ngẫu ở Chương 05.
- **Mở rộng tính lồi (Giả lồi, Log-lõm và Lồi theo nón $$K$$):** Bao phủ những hàm cực kỳ quan trọng trong xác suất và kinh tế học (như mật độ chuẩn Gauss hay hàm phân thức tuyến tính) vốn không lồi theo nghĩa cổ điển nhưng vẫn giải tối ưu hiệu quả.

### Khung giải thích (nên đọc chậm): Chặn dưới tiếp tuyến toàn cục của hàm lồi $$x^2$$ so với hàm không lồi $$x^3$$

Đặc trưng bậc nhất phát biểu: hàm khả vi $$f$$ lồi khi và chỉ khi tiếp tuyến tại *mọi* điểm $$x$$ luôn nằm dưới đồ thị: $$f(y) \ge f(x) + f'(x)(y - x)\ \forall y$$.

1. **Thử với hàm lồi $$f(x) = x^2$$ tại $$x = 1$$:**
   - Tiếp tuyến: $$T(y) = f(1) + f'(1)(y - 1) = 1 + 2(y - 1) = 2y - 1$$.
   - Kiểm tra tại $$y = 3$$: $$f(3) = 9 \ge T(3) = 2(3) - 1 = 5$$.
   - Kiểm tra tổng quát: $$f(y) - T(y) = y^2 - (2y - 1) = (y - 1)^2 \ge 0$$ với mọi $$y \in \mathbb{R}$$!
2. **Thử với hàm không lồi $$g(x) = x^3$$ tại $$x = 1$$:**
   - Tiếp tuyến: $$T_g(y) = 1 + 3(y - 1) = 3y - 2$$.
   - Kiểm tra tại $$y = -3$$: $$g(-3) = -27$$, trong khi tiếp tuyến cho $$T_g(-3) = 3(-3) - 2 = -11$$!
   Vì $$-27 < -11$$, đồ thị đã "đâm xuyên" xuống dưới tiếp tuyến — xác nhận ngay $$x^3$$ **không lồi** trên $$\mathbb{R}$$!

---

Chương này trình bày định nghĩa, các ví dụ tiêu biểu, các tính chất cơ bản của hàm lồi và những phép toán bảo toàn tính lồi.

Xem thêm bài tùy chọn [03-08 Ứng dụng và phát triển gần đây]({% multilang_post_url contents/chapter03/2026-09-16-03_08_Applications_Recent %}) về vai trò của hàm log-sum-exp trong hiệu chỉnh xác suất, hiện tượng neural collapse và hàm mất mát đối sánh.

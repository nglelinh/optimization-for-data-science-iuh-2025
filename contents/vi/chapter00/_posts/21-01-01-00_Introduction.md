---
layout: post
title: 00 Giới thiệu
chapter: '00'
order: 1
owner: GitHub Copilot
lang: vi
categories:
- chapter00
---

Mỗi khi một chiếc xe tự lái chọn quỹ đạo tránh vật cản trong vài mili-giây, một hãng hàng không xếp lịch bay cho hàng nghìn chuyến trong bão, hay một mô hình ngôn ngữ lớn cập nhật hàng tỷ trọng số trên cụm GPU, bên dưới tất cả đều đang vận hành cùng một nhịp tim toán học: **tối ưu hóa**. Nhưng để đọc được "bản nhạc" của tối ưu hóa lồi — nơi một bất đẳng thức hình học đơn giản có thể tiết kiệm hàng triệu phép tính — trước hết ta cần làm chủ bộ ngôn ngữ nền tảng gồm giải tích, đại số tuyến tính, tôpô tập hợp và xác suất.

Chương 00 không phải là phần ôn tập khô khan để lướt qua cho xong, mà là xưởng rèn công cụ giúp bạn biến trực giác hình học thành lập luận chặt chẽ trước khi bước vào các thuật toán tối ưu hóa hiện đại.

## Kiến thức cần nhớ: Bốn trụ cột toán học của Tối ưu hóa

Để hiểu sâu vì sao một thuật toán hội tụ, khi nào nghiệm tối ưu tồn tại, và làm sao xử lý dữ liệu nhiễu, tối ưu hóa đứng vững trên bốn trụ cột liên kết chặt chẽ:

- **Giải tích đa biến (Multivariable Calculus):** Cung cấp ngôn ngữ mô tả tốc độ biến thiên cục bộ của hàm mục tiêu thông qua đạo hàm riêng, vector gradient $$\nabla f(x)$$, ma trận Hessian $$\nabla^2 f(x)$$ và khai triển Taylor. Đây là la bàn chỉ hướng giảm nhanh nhất tại mỗi bước lặp.
- **Đại số tuyến tính (Linear Algebra):** Biến hệ phương trình ràng buộc, phép chiếu và độ cong bậc hai thành ngôn ngữ gọn gàng của vector, ma trận, giá trị riêng và dạng toàn phương $$x^T Q x$$. Mọi bước tính trong lập trình tối ưu thực tế đều quy về đại số tuyến tính số.
- **Lý thuyết tập hợp và Tôpô thực (Set Theory & Real Topology):** Định nghĩa chính xác "miền khả thi" (tập đóng, tập mở, tập compact, tập biên) và trả lời câu hỏi quan trọng trước khi chạy bất kỳ thuật toán nào: *liệu nghiệm tối ưu toàn cục có thực sự tồn tại hay không?*
- **Xác suất và Thống kê (Probability & Statistics):** Khi dữ liệu có nhiễu hoặc bài toán mang yếu tố ngẫu nhiên (như tối ưu hóa ngẫu nhiên SGD hay ước lượng hợp lý tối đa MLE), xác suất biến việc khớp mô hình thành bài toán cực tiểu hóa hàm mất mát kỳ vọng.

### Giải thích: Bốn trụ cột cùng giải một bài toán tối ưu nhỏ

Xét bài toán cực tiểu hóa hàm bậc hai một biến trên một đoạn đóng:

$$
\min_{x \in [4, 6]} f(x) = (x - 3)^2 + 2.
$$

Hãy quan sát cả bốn trụ cột phối hợp từng bước:

1. **Giải tích (tìm điểm dừng không ràng buộc):** Đạo hàm $$f'(x) = 2(x - 3) = 0 \Rightarrow x_{\text{uncon}} = 3$$, với $$f''(x) = 2 > 0$$ (độ cong dương). Nếu không có ràng buộc, đáy của parabol nằm tại $$x = 3$$ với $$f(3) = 2$$.
2. **Tập hợp và Tôpô (kiểm tra miền khả thi):** Miền khả thi $$D = [4, 6]$$ là tập đóng và bị chặn (compact) trên $$\mathbb{R}$$, và $$f$$ liên tục, nên theo định lý Weierstrass chắc chắn tồn tại nghiệm tối ưu toàn cục trên $$D$$. Tuy nhiên $$x_{\text{uncon}} = 3 \notin [4, 6]$$!
3. **Hình học và hướng giảm tại biên:** Trên toàn đoạn $$[4, 6]$$, ta có $$f'(x) = 2(x-3) \ge 2 > 0$$, nghĩa là hàm luôn tăng khi đi sang phải. Do đó điểm thấp nhất bắt buộc rơi vào biên trái $$x^* = 4$$, cho giá trị tối ưu $$f(4) = (4 - 3)^2 + 2 = 3$$.
4. **Bài học cốt lõi:** Đặt đạo hàm bằng $$0$$ chỉ đúng khi nghiệm nằm trong phần trong (interior) của miền khả thi; khi có ràng buộc, nghiệm tối ưu rất thường nằm ngay trên **biên**, nơi hướng giảm $$-f'(x^*)$$ bị chặn bởi tường ràng buộc.

---

Tối ưu hóa giữ vai trò trung tâm trong khoa học dữ liệu. Dù bạn đang huấn luyện mạng nơ-ron, cực tiểu hóa sai số trong các mô hình hồi quy hay phân bổ tài nguyên trong hệ thống gợi ý, về bản chất bạn đều đang giải bài toán tìm nghiệm "tốt nhất" trong một tập hợp lớn các phương án khả dĩ. Để giải quyết hiệu quả các bài toán này, bạn cần nắm vững ngôn ngữ toán học nền tảng. Trong chương này, chúng ta sẽ ôn lại những kiến thức cốt lõi từ đại số tuyến tính, lý thuyết tập hợp, giải tích và xác suất, giúp bạn sẵn sàng làm việc với gradient, ma trận, ràng buộc và tính bất định trong các bài toán tối ưu hóa.

Bài đọc tùy chọn ở cuối chương, [00-05 Ứng dụng và phát triển gần đây]({% multilang_post_url contents/chapter00/2026-09-16-00_05_Applications_Recent %}), kết nối các công cụ nền tảng này với vi phân tự động (autodiff), LoRA và mô hình khuếch tán (2022–2025).
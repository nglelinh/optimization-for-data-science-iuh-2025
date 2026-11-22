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

Trong chương này, chúng ta sẽ tìm hiểu **Gradient Descent** (thuật toán hạ gradient), một trong những phương pháp cơ bản và quan trọng nhất trong tối ưu hóa.

Trong các thuật toán tối ưu hóa, việc lựa chọn hướng tìm kiếm và kích thước bước đóng vai trò quyết định đối với tốc độ và khả năng hội tụ. Gradient descent di chuyển theo hướng ngược chiều gradient (hướng gradient âm). Kích thước bước có thể được giữ cố định hoặc điều chỉnh thích ứng, và cả hai cách tiếp cận này sẽ được trình bày trong chương này.

Để gradient descent hội tụ, hàm mục tiêu cần thỏa mãn một số điều kiện nhất định. Khi các điều kiện này được đáp ứng, ta có thể phân tích tốc độ hội tụ của thuật toán. Nếu hàm mục tiêu có thêm tính lồi mạnh, quá trình hội tụ sẽ diễn ra nhanh hơn đáng kể; chương này cũng sẽ phân tích cụ thể tốc độ hội tụ trong trường hợp đó.

Bên cạnh nền tảng lý thuyết, chúng ta sẽ xem xét các ứng dụng và biến thể quan trọng của gradient descent, bao gồm gradient boosting và stochastic gradient descent.

Bài đọc tùy chọn [06-08 Ứng dụng và phát triển gần đây]({% multilang_post_url contents/chapter06/2026-09-16-06_08_Applications_Recent %}) đối chiếu lý thuyết Lipschitz cổ điển với hiện tượng mép ổn định (edge of stability), thuật toán Lion và phương pháp trung bình không lịch bước (schedule-free averaging) giai đoạn 2021–2024. Tốc độ hội tụ tuyến tính ở mục 06-03-04 vẫn có thể áp dụng cho một số bài toán cực tiểu hóa rủi ro thực nghiệm (ERM) *không lồi* thỏa mãn điều kiện Polyak–Łojasiewicz; nội dung liên kết này được trình bày trong ghi chú tùy chọn [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}).

---
layout: post
title: 28 Phong cảnh không lồi cho học sâu
chapter: '28'
order: 1
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: required
---


# Địa hình hàm mất mát không lồi trong học sâu

Tính lồi là nền tảng bảo đảm ở các Chương 02–25: mọi cực tiểu địa phương đều là cực tiểu toàn cục và điều kiện bậc nhất đủ để chứng nhận nghiệm tối ưu. Tuy nhiên, hàm mất mát huấn luyện $$F(w)$$ của mạng nơ-ron sâu là **không lồi**. Chương này khảo sát cụ thể những dạng phi lồi thực sự xuất hiện trong học sâu.

Ta sẽ phân loại các **điểm tới hạn** ($$\nabla F(w)=0$$) dựa trên dấu trị riêng của ma trận Hessian thành cực tiểu, cực đại và **điểm yên ngựa (saddle point)**. Từ đó, ta thấy vì sao trong không gian nhiều chiều, các điểm yên ngựa mới là trở ngại phổ biến hơn các cực tiểu địa phương kém, và vì sao trạng thái **quá tham số hóa** (số tham số lớn hơn số ràng buộc dữ liệu) lại khiến nhiều điểm cực tiểu đạt khả năng nội suy dữ liệu huấn luyện.

Các giáo trình tối ưu hiện đại như EPFL CS-439 và USC CSCI 599 xem đây là phần kiến thức cốt lõi cho học sâu. Chương này dừng ở các định nghĩa chính xác cùng trực giác hình học, không đi vào các giới hạn phương trình đạo hàm riêng trường trung bình (mean-field PDE).

Bạn có thể mở mô phỏng [loss_function_landscapes.html](https://nglelinh.github.io/interactive_math/optimization/loss_function_landscapes.html) trong quá trình đọc.

## Nội dung các bài

1. Điểm tới hạn và điểm yên ngựa.
2. Thoát khỏi điểm yên ngựa và hình học địa hình hàm mất mát.
3. Quá tham số hóa (và giới thiệu điều kiện PL).
4. Các hiện tượng địa hình hiện đại (tùy chọn) — liên thông mode, grokking, double descent, cực tiểu phẳng.
5. Điều kiện Polyak–Łojasiewicz (PL) và tốc độ hội tụ tuyến tính (tùy chọn) — kết quả của Karimi và cộng sự, mở rộng chứng minh Chương 06 mà không cần tính lồi.

Bài tùy chọn [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}) xây dựng cầu nối từ tốc độ hội tụ lồi mạnh ở 06-03-04 sang lớp bài toán không lồi thỏa điều kiện PL, còn các hiện tượng thực nghiệm giai đoạn 2022–2026 được tổng hợp tại [28-04]({% multilang_post_url contents/chapter28/2026-09-16-28_04_modern_landscapes %}).

---
layout: post
title: '22 Phương pháp Gradient có điều kiện (Frank-Wolfe)'
chapter: '22'
order: 1
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---

Chương này trình bày thuật toán Frank-Wolfe do Marguerite Frank và Philip Wolfe đề xuất năm 1956.

Thuật toán Frank-Wolfe là một phương pháp tối ưu lặp bậc nhất dành cho bài toán tối ưu lồi có ràng buộc, còn được gọi là phương pháp gradient có điều kiện (conditional gradient method), phương pháp gradient rút gọn (reduced gradient method) hoặc thuật toán tổ hợp lồi (convex combination algorithm). Tại mỗi vòng lặp, thuật toán xấp xỉ tuyến tính hàm mục tiêu xung quanh điểm hiện tại, tìm cực tiểu của hàm tuyến tính đó trên tập ràng buộc, rồi di chuyển theo hướng tới điểm cực tiểu vừa tìm được.

[15] Wikipedia. [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)

## Ứng dụng giai đoạn 2022–2026 (tùy chọn)

Nhờ chỉ cần một bộ giải cực tiểu tuyến tính (linear minimization oracle) thay vì phép chiếu, thuật toán Frank–Wolfe tiếp tục được ứng dụng rộng rãi trong thập niên 2020: từ SVM có cấu trúc, bài toán vận chuyển tối ưu bán nới lỏng (ứng dụng chuyển màu ảnh), vận chuyển tối ưu không cân bằng 1 chiều, cho đến các phương pháp giải thích mạng nơ-ron có ràng buộc (tối ưu độ méo–tốc độ trên hình cầu $$\ell_1$$ hoặc đa diện Birkhoff). Bạn có thể tham khảo bài đọc tùy chọn [22-05 Ứng dụng hiện đại của Frank–Wolfe]({% multilang_post_url contents/chapter22/2026-09-16-22_05_modern_applications %}) sau khi học xong các mục 22-02 đến 22-04; bài đọc này bổ sung bối cảnh ứng dụng và không thay thế phần phân tích hội tụ.

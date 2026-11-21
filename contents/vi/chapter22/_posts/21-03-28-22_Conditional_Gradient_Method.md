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

Chương này sẽ xem xét thuật toán Frank-Wolfe do Marguerite Frank và Philip Wolfe đề xuất năm 1956.

Thuật toán Frank-Wolfe là một thuật toán tối ưu bậc nhất lặp cho tối ưu lồi có ràng buộc, còn được gọi là phương pháp gradient có điều kiện, phương pháp gradient rút gọn (reduced gradient method) và thuật toán tổ hợp lồi (convex combination algorithm).

Phương pháp này ban đầu do Marguerite Frank và Philip Wolfe đề xuất năm 1956. Thuật toán Frank-Wolfe xét một xấp xỉ tuyến tính của hàm mục tiêu tại mỗi vòng lặp và di chuyển về phía điểm cực tiểu của hàm tuyến tính này.

[15] Wikipedia. [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)

## Ứng dụng 2026 (tùy chọn)

Oracle cực tiểu tuyến tính là lý do Frank–Wolfe sống tới thập niên 2020: SVM cấu trúc, vận chuyển tối ưu bán nới (chuyển màu), OT không cân 1-D, và giải thích mạng nơ-ron có ràng buộc (bản đồ méo-tốc độ trên quả cầu $$\ell_1$$ hoặc đa diện Birkhoff). Xem khảo sát tùy chọn [22-06 Ứng dụng hiện đại của Frank–Wolfe]({% multilang_post_url contents/chapter22/2026-09-16-22_06_modern_applications %}). Đọc sau 22-02 / 22-04, không thay phân tích hội tụ.

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

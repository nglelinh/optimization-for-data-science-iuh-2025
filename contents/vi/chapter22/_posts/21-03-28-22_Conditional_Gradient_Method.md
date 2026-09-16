---
layout: post
title: 22 Conditional Gradient (Frank-Wolfe) Method
chapter: '22'
order: 1
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---

This chapter will examine the Frank-Wolfe algorithm proposed by Marguerite Frank and Philip Wolfe in 1956.

The Frank-Wolfe algorithm is an iterative first-order optimization algorithm for constrained convex optimization, also called the conditional gradient method, reduced gradient method, and convex combination algorithm.

This method was originally proposed by Marguerite Frank and Philip Wolfe in 1956. The Frank-Wolfe algorithm considers a linear approximation of the objective function at each iteration and moves toward the minimizer of this linear function.

[15] Wikipedia. [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)

## Ứng dụng 2026 (tùy chọn)

Oracle cực tiểu tuyến tính là lý do Frank–Wolfe sống tới thập niên 2020: SVM cấu trúc, vận chuyển tối ưu bán nới (chuyển màu), OT không cân 1-D, và giải thích mạng nơ-ron có ràng buộc (bản đồ méo-tốc độ trên quả cầu $$\ell_1$$ hoặc đa diện Birkhoff). Xem khảo sát tùy chọn [22-06 Ứng dụng hiện đại của Frank–Wolfe]({% multilang_post_url contents/chapter22/2026-09-16-22_06_modern_applications %}). Đọc sau 22-02 / 22-04, không thay phân tích hội tụ.

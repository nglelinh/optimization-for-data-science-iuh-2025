---
layout: post
title: 26 Phương pháp ngẫu nhiên và thích nghi cho học máy
chapter: '26'
order: 1
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---


# Phương pháp ngẫu nhiên và thích nghi cho học máy

Các Chương 06–09 xử lý phương pháp bậc nhất **cả lô** (full-batch): một gradient (hoặc bước proximal) nhìn mọi cặp huấn luyện. Học máy hiện đại hầu như không làm vậy. Chương này là ngăn xếp mặc định 2026 cho tối thiểu hóa rủi ro thực nghiệm

$$
\min_w F(w) = \frac{1}{n}\sum_{i=1}^n f_i(w), \qquad f_i(w) = \ell\bigl(h_w(x_i), y_i\bigr).
$$

Bạn đã gặp họ hàng trong [06-05 Stochastic gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %}) và các ghi chú subgradient ngẫu nhiên ở Chương 08. Ở đây SGD và minibatch là *thuật toán*, rồi ta thêm hai thành phần mọi thư viện học sâu đều chuyển: **momentum / Nesterov** và **co giãn thích nghi theo tọa độ** (AdaGrad → trực giác RMSProp → Adam → AdamW). Bài cuối khảo sát giảm phương sai (SVRG / SAGA) để biết khi nào lý thuyết lồi sắc hơn Adam.

## Vì sao tách chương

Gradient descent cả lô trên ImageNet hoặc ngữ liệu mô hình ngôn ngữ không phải bài toán bước — đó là bài toán *bộ nhớ và thời gian tường*. Một ước lượng gradient không chệch (hoặc gần không chệch) từ một mẫu hoặc minibatch kích thước $$B\ll n$$ cho phép nhiều bước tham số hơn mỗi giờ. Cái giá là nhiễu. Phương pháp thích nghi tiêu nhiễu đó vào tốc độ học từng tọa độ; momentum tiêu vào một vận tốc nhớ các hướng ổn định.

Giáo trình đồng cấp coi đây là lõi, không phải chú thích: MIT 6.7220 (S25), EPFL CS-439, USC CSCI 599, BU EC525.

## Các bài

1. SGD và minibatch — ước lượng, xáo trộn, câu chuyện $$O(1/\sqrt{T})$$
2. Momentum và Nesterov — heavy ball so với nhìn trước; trực giác kiểu Distill
3. Từ AdaGrad đến Adam — tiền điều kiện đường chéo
4. AdamW và thực hành huấn luyện — weight decay tách, lịch, clipping
5. Giảm phương sai (khảo sát) — SVRG / SAGA, và khi nào mini-batch Adam vẫn thắng
6. Bộ tối ưu thích nghi hiện đại (khảo sát tùy chọn) — SAM, Sophia, Muon so với baseline AdamW

Hoạt họa SGD nằm trong [`interactive_math/optimization`](https://github.com/nglelinh/interactive_math/tree/main/optimization). SAM, Muon, Sophia vẫn là **đọc thêm** — không kiểm tra kỳ này — nhưng nay có bài tùy chọn riêng: [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %}).

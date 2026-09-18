---
layout: post
title: '08 Phương pháp Subgradient'
chapter: '08'
order: 1
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Trong phần này, chúng ta sẽ tìm hiểu về phương pháp subgradient, có thể được áp dụng cho các hàm lồi có thể không khả vi, sử dụng khái niệm subgradient. Chúng ta cũng sẽ khám phá các tính chất hội tụ và tốc độ hội tụ của phương pháp subgradient thông qua các ví dụ.

## Ứng dụng hiện đại (2022–2026)

Một bài tùy chọn đi kèm đặt cùng vòng subgradient (chiếu, ngẫu nhiên) vào PGD đối kháng / RobustBench, ràng buộc tỷ lệ Fairlearn, và huấn luyện ReLU không trơn. Xem [08-11 Ứng dụng hiện đại của phương pháp subgradient]({% multilang_post_url contents/chapter08/2026-09-16-08_11_modern_applications %}). Khi mục tiêu tổng hữu hạn *thật sự* trơn, sàn nhiễu $$O(1/\sqrt{T})$$ của phương pháp ngẫu nhiên chương này có thể được gỡ bằng SVRG / SAGA — bài đó là [26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %}), cạnh mạch SGD.
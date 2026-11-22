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

Trong chương này, chúng ta tìm hiểu phương pháp subgradient — thuật toán áp dụng cho các hàm lồi không nhất thiết khả vi, được xây dựng dựa trên khái niệm gradient dưới. Chúng ta cũng sẽ phân tích tính chất hội tụ và tốc độ hội tụ của phương pháp này thông qua các ví dụ cụ thể.

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm liên hệ trực tiếp vòng lặp subgradient (bao gồm biến thể có chiếu và ngẫu nhiên) với các ứng dụng như PGD trong huấn luyện đối kháng / RobustBench, bài toán ràng buộc tỷ lệ trong Fairlearn, và huấn luyện mạng ReLU không trơn. Xem [08-09 Ứng dụng hiện đại của phương pháp subgradient]({% multilang_post_url contents/chapter08/2026-09-16-08_09_modern_applications %}). Khi hàm mục tiêu dạng tổng hữu hạn *thực sự* trơn, giới hạn nhiễu $$O(1/\sqrt{T})$$ của phương pháp ngẫu nhiên trong chương này có thể được khắc phục bằng các kỹ thuật giảm phương sai như SVRG / SAGA — xem [26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %}), nằm cùng nhóm bài về SGD.

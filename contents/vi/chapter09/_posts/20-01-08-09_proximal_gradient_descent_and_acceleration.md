---
layout: post
title: Phương pháp gradient gần kề và tăng tốc
chapter: '09'
order: 1
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Phương pháp gradient gần kề và tăng tốc

Chương này giới thiệu phương pháp gradient gần kề (proximal gradient descent) cùng các kỹ thuật tăng tốc cho các bài toán tối ưu có hàm mục tiêu dạng tổng hợp.

## Tổng quan
- Phương pháp gradient gần kề được dùng cho các bài toán mà hàm mục tiêu có thể tách thành một phần khả vi và một phần không khả vi.
- Các kỹ thuật tăng tốc như tăng tốc Nesterov và FISTA giúp cải thiện đáng kể tốc độ hội tụ.

## Cấu trúc chương
- Phần 1: Phương pháp gradient gần kề
- Phần 2: Phân tích hội tụ
- Phần 3: Ví dụ về hoàn thiện ma trận
- Phần 4: Các trường hợp đặc biệt
- Phần 5: Các phương pháp tăng tốc — bắt đầu từ góc nhìn trực quan kiểu Distill ở [09-05]({% multilang_post_url contents/chapter09/20-01-08-09_05_acceleration %}), tiếp theo là phần trình bày giải tích về FISTA ở 09-05-01; biến thể ngẫu nhiên với hệ số $$\beta$$ cố định được trình bày tại [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %}).

Tham khảo từng bài học dưới đây để xem chi tiết thuật toán và phân tích toán học.

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm nối tiếp khuôn mẫu proximal gradient / FISTA sang các ứng dụng như tái tạo ảnh plug-and-play (PnP), trải phẳng thuật toán (unrolling) trong FISTA-Net / pFISTA-DR, và đường chính quy hóa elastic net trong thực tế. Xem [09-06 Ứng dụng hiện đại của proximal GD và tăng tốc]({% multilang_post_url contents/chapter09/2026-09-16-09_06_modern_applications %}).

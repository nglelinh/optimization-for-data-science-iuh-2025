---
layout: post
title: '09-05-04 Tăng tốc có luôn hữu ích không?'
chapter: '09'
order: 10
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Tăng tốc có luôn hữu ích không?

Mặc dù các phương pháp tăng tốc như FISTA đạt tốc độ hội tụ lý thuyết nhanh hơn, trong thực tế việc dùng tăng tốc không phải lúc nào cũng mang lại hiệu quả tốt hơn.

## Khi nào tăng tốc có thể kém hiệu quả
- Với các bài toán có điều kiện xấu, thành phần động lượng có thể gây dao động mạnh hoặc làm giảm độ ổn định số học.
- Trên một số bài toán không trơn hoặc có cấu trúc phức tạp, tăng tốc chưa chắc cải thiện tốc độ hội tụ thực tế.
- Hiện tượng "gợn sóng Nesterov" khiến giá trị hàm mục tiêu không giảm đơn điệu qua các bước lặp.

## Kinh nghiệm thực hành
- Ưu tiên dùng phương pháp tăng tốc khi phần trơn của bài toán có điều kiện tốt.
- Theo dõi chặt chẽ giá trị hàm mục tiêu và độ ổn định trong quá trình chạy thuật toán.
- Nếu quan sát thấy dao động lớn hoặc mất ổn định, cân nhắc áp dụng cơ chế khởi động lại (restart) hoặc quay về phương pháp gradient gần kề tiêu chuẩn.
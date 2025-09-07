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

Các phương pháp tăng tốc như FISTA có thể đạt được tốc độ hội tụ nhanh hơn về mặt lý thuyết, nhưng trong thực tế, tăng tốc không luôn có lợi.

## Khi nào tăng tốc có thể không giúp được
- Nếu bài toán có điều kiện xấu, tăng tốc có thể gây dao động hoặc mất ổn định.
- Đối với một số bài toán không trơn, tăng tốc có thể không cải thiện hội tụ.
- Hiện tượng "gợn sóng Nesterov" có thể gây ra hành vi không đơn điệu trong giá trị hàm mục tiêu.

## Lời khuyên thực tế
- Sử dụng các phương pháp tăng tốc khi bài toán có điều kiện tốt và trơn.
- Giám sát hội tụ và ổn định khi áp dụng tăng tốc.
- Nếu xảy ra mất ổn định, hãy xem xét chuyển sang các phương pháp gradient gần kề tiêu chuẩn.
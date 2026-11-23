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
- Nếu bài toán có điều kiện tốt (số điều kiện $$\kappa = L/\mu$$ nhỏ), phương pháp gradient gần kề thường đã hội tụ nhanh, với tốc độ tuyến tính. Khi đó tăng tốc lợi rất ít, thậm chí động lượng có thể làm chậm hơn một chút. Ví dụ, với một bài Lasso 2 chiều có $$\kappa = 3$$, ISTA cần 14 vòng lặp còn FISTA cần 16 vòng.
- Tăng tốc có lợi nhất khi bài toán có điều kiện xấu ($$\kappa$$ lớn). Lúc đó gradient gần kề thường chạy rất chậm, còn FISTA giảm số vòng lặp đi nhiều lần. Đổi lại, giá trị hàm mục tiêu có thể dao động.
- Nếu $$g$$ không trơn, hoặc $$\nabla g$$ không có hằng số Lipschitz phù hợp, thì đảm bảo $$O(1/k^2)$$ không còn áp dụng được.
- Hiện tượng "gợn sóng Nesterov" khiến giá trị hàm mục tiêu không giảm đơn điệu: nó có thể tăng lên vài vòng rồi mới giảm tiếp.

## Kinh nghiệm thực hành
- Nên dùng tăng tốc khi phần trơn của bài toán có điều kiện xấu, vì đó là lúc tăng tốc có lợi nhất.
- Khi bài toán có điều kiện tốt, phương pháp gradient gần kề thường là đủ.
- Theo dõi giá trị hàm mục tiêu. Nếu dao động lớn, dùng cơ chế khởi động lại (restart, đặt lại $$t_k = 1$$ khi hàm mục tiêu tăng) thay vì bỏ hẳn tăng tốc.

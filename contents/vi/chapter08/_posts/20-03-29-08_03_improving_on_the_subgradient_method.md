---
layout: post
title: '08-03 Cải tiến Phương pháp Subgradient'
chapter: '08'
order: 16
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Phương pháp subgradient có lợi thế vì có thể được sử dụng cho các hàm lồi không khả vi, làm cho nó tổng quát hơn. Tuy nhiên, tốc độ hội tụ của nó là $$O(1/\epsilon^{2})$$, chậm hơn nhiều so với tốc độ hội tụ của gradient descent là $$O(1/\epsilon)$$.

Có cách nào để kết hợp điểm mạnh của gradient descent và phương pháp subgradient không? Trong phần tiếp theo, chúng ta sẽ tìm hiểu về phương pháp proximal gradient descent, kết hợp ưu điểm của cả hai thuật toán.
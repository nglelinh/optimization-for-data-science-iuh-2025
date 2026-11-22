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

Phương pháp subgradient có ưu điểm là áp dụng được cho các hàm lồi không khả vi, nên có phạm vi sử dụng rộng hơn gradient descent. Tuy nhiên, tốc độ hội tụ $$O(1/\epsilon^{2})$$ của nó chậm hơn nhiều so với tốc độ $$O(1/\epsilon)$$ của gradient descent.

Liệu có thể kết hợp ưu điểm của cả hai phương pháp không? Trong chương tiếp theo, chúng ta sẽ tìm hiểu **phương pháp gradient gần kề (proximal gradient descent)**, giúp giữ được tốc độ hội tụ tốt trên lớp bài toán tổng hợp có thành phần không khả vi.
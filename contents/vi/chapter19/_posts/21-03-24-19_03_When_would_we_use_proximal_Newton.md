---
layout: post
title: '19-03 Khi nào nên dùng Newton proximal?'
chapter: '19'
order: 7
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Khi nào phương pháp Newton proximal là lựa chọn phù hợp?

Để trả lời câu hỏi này, ta so sánh phương pháp Newton proximal với proximal gradient descent trên bài toán tổng hợp:

**Bài toán:** $$\min_x g(x) + h(x)$$

## So sánh Proximal gradient descent và Newton proximal

| **Proximal gradient descent** |**Newton proximal** | 
| -------- | -------- |
| Ở mỗi bước cực tiểu hóa $$\frac{1}{2} \parallel b - x \parallel_2^2 + h(x)$$ | Ở mỗi bước cực tiểu hóa $$b^T x + x^T A x + h(x)$$ | 
| Toán tử prox thường có nghiệm dạng đóng | Toán tử prox thường không có nghiệm dạng đóng |
| Chi phí mỗi vòng lặp thấp | Chi phí mỗi vòng lặp rất cao (cao hơn cả phương pháp Newton) | 
| Tốc độ hội tụ tương tự gradient descent: <br> $$O(1/\epsilon)$$ | Tốc độ hội tụ tương tự phương pháp Newton: <br> $$O(\log \log (1/\epsilon))$$ | 

Dù có dạng công thức tương đồng, hai phương pháp vận hành rất khác nhau về đánh đổi chi phí.

Vì vậy, phương pháp Newton proximal đặc biệt đáng dùng khi ta có một bộ giải bên trong đủ nhanh cho bài toán prox có tỉ lệ (dạng toàn phương $$+\ h$$), nhờ đó tận dụng ưu thế chỉ cần rất ít vòng lặp ngoài. Khi $$h$$ là hàm tách biến (separable), bộ giải bên trong phổ biến nhất là phương pháp hạ theo tọa độ (coordinate descent).

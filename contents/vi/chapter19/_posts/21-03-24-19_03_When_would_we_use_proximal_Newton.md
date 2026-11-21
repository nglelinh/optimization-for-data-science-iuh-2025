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

Khi nào phương pháp Newton proximal là lựa chọn tốt?

Để hiểu khi nào nó hữu ích, hãy so sánh phương pháp Newton proximal với proximal gradient descent trên bài toán sau.

**Bài toán**: $$\min_x g(x) + h(x)$$

## Proximal gradient descent so với Newton proximal

| **Proximal gradient descent** |**Newton proximal** | 
| -------- | -------- |
| Ở mỗi bước cực tiểu hóa $$\frac{1}{2} \parallel b - x \parallel_2^2 + h(x)$$ | Ở mỗi bước cực tiểu hóa $$b^T x + x^T A x + h(x)$$ | 
| Toán tử prox thường có dạng đóng | Toán tử prox thường không có dạng đóng |
| Vòng lặp rẻ | Vòng lặp rất đắt (đắt hơn phương pháp Newton) | 
| Tốc độ hội tụ của gradient descent <br> $$O(1/\epsilon)$$ | Tốc độ hội tụ của phương pháp Newton <br> $$O(\log \log 1/\epsilon)$$ | 

Hai phương pháp trông giống nhau, nhưng thực tế làm những việc rất khác nhau.

Do đó, phương pháp Newton proximal đáng dùng khi ta có một bộ tối ưu bên trong nhanh cho bài toán prox có tỉ lệ (dạng toàn phương $$+\ h$$), để chỉ cần rất ít vòng lặp ngoài. Khi $$h$$ là hàm tách biến (separable), bộ tối ưu bên trong được dùng phổ biến nhất là coordinate descent.

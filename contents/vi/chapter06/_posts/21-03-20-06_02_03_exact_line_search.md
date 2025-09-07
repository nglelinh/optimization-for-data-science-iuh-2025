---
layout: post
title: 06-02-03 Tìm kiếm đường chính xác
chapter: '06'
order: 6
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Một cách khác để thích ứng kích thước bước trong gradient descent là **tìm kiếm đường chính xác**.

### Tìm kiếm Đường chính xác là gì?
Trong tìm kiếm đường chính xác, chúng ta di chuyển theo hướng của gradient âm và chọn kích thước bước tốt nhất có thể.

Đối với biểu thức sau, nếu $$s > 0$$, bước tiếp theo $$x - s \nabla f(x)$$ di chuyển ra khỏi vị trí hiện tại. Bằng cách thay đổi $$s$$, chúng ta tìm kích thước bước $$t$$ làm giảm thiểu $$f$$:

> $$t = \arg\min_{s \ge 0} f(x - s \nabla f(x))$$

Tìm kiếm đường chính xác hiệu quả cho các bài toán tối ưu hóa một biến, nhưng đối với các bài toán nhiều biến, việc tìm kiếm toàn diện kích thước bước tối ưu thường không thực tế. Trong thực tế, tìm kiếm lùi hiệu quả hơn và được sử dụng phổ biến hơn.
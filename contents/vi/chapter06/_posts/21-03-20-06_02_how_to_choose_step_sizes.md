---
layout: post
title: 06-02 Cách chọn kích thước bước
chapter: '06'
order: 5
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

Khi thực hiện gradient descent, **kích thước bước** quyết định mức độ cập nhật của biến $$x$$ ở mỗi lần lặp, qua đó ảnh hưởng trực tiếp đến tốc độ và khả năng hội tụ về nghiệm tối ưu. Mục này giới thiệu ba phương pháp chính để lựa chọn kích thước bước:

- Kích thước bước cố định (fixed step size)
- Tìm kiếm đường lùi (backtracking line search)
- Tìm kiếm đường chính xác (exact line search)
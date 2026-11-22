---
layout: post
title: '20-04-02 Đảm bảo hội tụ'
chapter: '20'
order: 10
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

# Đảm bảo hội tụ của ADMM

Dưới các điều kiện chuẩn rất nhẹ trên $$f$$ và $$g$$ (đáng chú ý là $$A$$ và $$B$$ không cần có hạng đầy đủ), ADMM đảm bảo các tính chất hội tụ sau với mọi $$\rho > 0$$:

* **Hội tụ phần dư:** Khi $$k \to \infty$$, $$r^{(k)} = Ax^{(k)} + Bz^{(k)} - c \to 0$$, tức là các điểm lặp tiến dần về tập khả thi gốc.

* **Hội tụ giá trị hàm mục tiêu:** $$f(x^{(k)}) + g(z^{(k)}) \to f^{\ast} + g^{\ast}$$, trong đó $$f^{\ast} + g^{\ast}$$ là giá trị tối ưu của bài toán gốc.

* **Hội tụ biến đối ngẫu:** $$u^{(k)} \to u^{\ast}$$, trong đó $$u^{\ast}$$ là nghiệm tối ưu đối ngẫu.

Tốc độ hội tụ tổng quát của ADMM phụ thuộc vào tính chất cụ thể của bài toán (như tính lồi mạnh hay độ trơn) và là chủ đề có nhiều kết quả nghiên cứu chuyên sâu. Về mặt thực hành, tốc độ hội tụ của ADMM thường tương đương hoặc nhỉnh hơn một chút so với các phương pháp bậc nhất.

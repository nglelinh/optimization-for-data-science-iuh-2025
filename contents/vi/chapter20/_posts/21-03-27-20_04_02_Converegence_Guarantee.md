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

Với các điều kiện thích hợp trên $$f$$ và $$g$$ (lưu ý rằng $$A$$ và $$B$$ không cần có hạng đầy đủ), ADMM thỏa mãn các điều sau với mọi $$\rho > 0$$:

* **Hội tụ phần dư**: Khi $$k \to \infty$$, $$r^{(k)} = Ax^{(k)} + Bz^{(k)} - c \to 0$$, nghĩa là các điểm lặp gốc tiến đến tính khả thi.

* **Hội tụ hàm mục tiêu**: $$f(x^{(k)}) + g(z^{(k)}) \to f^{\ast} + g^{\ast}$$, trong đó $$f^{\ast} + g^{\ast}$$ là giá trị mục tiêu gốc tối ưu.

* **Hội tụ đối ngẫu**: $$u^{(k)} \to u^{\ast}$$, trong đó $$u^{\ast}$$ là nghiệm đối ngẫu.

Tốc độ hội tụ chính xác vẫn chưa được hiểu đầy đủ, và hiện có nhiều nghiên cứu đang diễn ra trong lĩnh vực này. Nói đại khái, ADMM hoạt động tương tự hoặc tốt hơn một chút so với các phương pháp bậc nhất.

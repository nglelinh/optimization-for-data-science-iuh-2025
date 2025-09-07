---
layout: post
title: '08-01 Phương pháp Subgradient'
chapter: '08'
order: 2
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Giả sử miền của hàm số là $${R}^n$$ và có một hàm lồi $$f$$ có thể không khả vi tại mọi điểm.

Phương pháp subgradient được định nghĩa bằng cách thay thế gradient trong phương pháp gradient descent bằng một subgradient. ($$\nabla f(x^{(k-1)}) \to g(x^{(k-1)})$$)

>$$ x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}, \quad k = 1, 2, 3, . . . $$

Ở đây, $$g^{(k-1)} \in \partial f(x^{(k-1)})$$, tức là $$g^{(k-1)}$$ là một subgradient của $$f$$ tại $$x^{(k-1)}$$.

## Phương pháp subgradient (không phải "descent" subgradient)

Khác với gradient descent, phương pháp subgradient không luôn đảm bảo giảm giá trị hàm số ở mỗi bước (do đó tên gọi không phải là "descent" subgradient). Vì vậy, khi sử dụng phương pháp subgradient, quan trọng là phải theo dõi kết quả tốt nhất tại mỗi lần lặp.

>$$f(x_{best}^{(k)}) = \min_{i=0,...k} f(x^{(i)})$$ 

$$f(x^{(k)}_{best})$$ biểu thị giá trị nhỏ nhất của hàm $$f$$ thu được trong $$k$$ lần lặp của phương pháp subgradient.

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

Giả sử $$f$$ là một hàm lồi xác định trên $${R}^n$$ và có thể không khả vi tại một số điểm.

Phương pháp subgradient được xây dựng bằng cách thay thế gradient trong phương pháp gradient descent bằng một subgradient ($$\nabla f(x^{(k-1)}) \to g(x^{(k-1)})$$):

>$$ x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}, \quad k = 1, 2, 3, . . . $$

trong đó $$g^{(k-1)} \in \partial f(x^{(k-1)})$$ là một subgradient của $$f$$ tại $$x^{(k-1)}$$.

## Vì sao gọi là "phương pháp subgradient" (chứ không phải "subgradient descent")

Khác với gradient descent, phương pháp subgradient không đảm bảo giá trị hàm mục tiêu luôn giảm sau mỗi bước lặp (do đó thuật toán không được gọi là "subgradient descent"). Vì vậy, trong quá trình chạy thuật toán, cần lưu lại giá trị tốt nhất đạt được tính đến bước hiện tại:

>$$f(x_{best}^{(k)}) = \min_{i=0,...k} f(x^{(i)})$$ 

Ở đây, $$f(x^{(k)}_{best})$$ ký hiệu giá trị nhỏ nhất của hàm $$f$$ thu được sau $$k$$ bước lặp.

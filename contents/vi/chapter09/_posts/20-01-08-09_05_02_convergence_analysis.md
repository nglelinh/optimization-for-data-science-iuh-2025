---
layout: post
title: '09-05-02 Phân tích hội tụ'
chapter: '09'
order: 8
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Phân tích hội tụ

Trong phần này, chúng ta phân tích sự hội tụ của phương pháp gradient gần kề tăng tốc.

## Định lý hội tụ
Giả sử $$g$$ là hàm lồi và khả vi, $$h$$ là hàm lồi, và $$\nabla g$$ liên tục Lipschitz với hằng số $$L > 0$$. Khi đó, phương pháp gradient gần kề tăng tốc với kích thước bước cố định $$t \le 1/L$$ thỏa mãn:

> $$f(x^{(k)}) - f^* \le \frac{2L \lVert x^{(0)} - x^* \rVert^2_2}{(k+1)^2}$$

Điều này có nghĩa là tốc độ hội tụ là $$O(1/k^2)$$, nhanh hơn phương pháp gradient gần kề tiêu chuẩn.

## Tìm kiếm đường thẳng lùi
Tìm kiếm đường thẳng lùi cho phương pháp gradient gần kề tăng tốc tương tự như đối với phương pháp gradient gần kề tiêu chuẩn, nhưng kích thước bước được chọn một cách thích ứng.

Để biết thêm chi tiết, tham khảo Beck và Teboulle (2009), "A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems" (FISTA).

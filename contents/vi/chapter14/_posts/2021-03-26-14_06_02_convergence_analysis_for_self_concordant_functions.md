---
layout: post
title: 14-06-02 Phân tích hội tụ cho các hàm tự hài hòa
chapter: '14'
order: 14
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---
Đối với các hàm tự hài hòa, kết quả phân tích hội tụ của phương pháp Newton có dạng:

>Định lý (Nesterov và Nemirovskii): Phương pháp Newton với tìm kiếm đường backtracking cần tối đa số vòng lặp sau để đạt được $$f(x^{(k)})-f^{\star}\leq \epsilon$$:
>\begin{align}
>C(\alpha, \beta)\big( f(x^{(0)})-f^{\star} \big) + \log\log{(1/\epsilon)},
>\end{align}
>trong đó $$C(\alpha, \beta)$$ là hằng số chỉ phụ thuộc vào hai tham số backtracking $$\alpha, \beta$$.

Chứng minh định lý này có cấu trúc tương tự phân tích hội tụ tổng quát của phương pháp Newton, nhưng khai thác các tính chất của hàm tự hài hòa để loại bỏ sự phụ thuộc vào các hằng số $$L, m, M$$ (xem [1], tr. 503).
---
layout: post
title: 14-06-02 Phân tích hội tụ cho các hàm tự hài hòa
chapter: '14'
order: 12
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---
Đối với các hàm tự hài hòa, kết quả phân tích hội tụ như sau:

>Định lý (Nesterov và Nemirovskii): Phương pháp Newton với tìm kiếm đường backtracking yêu cầu số lần lặp sau để đạt được $$f(x^{(k)})-f^{\star}\leq \epsilon$$:
>\begin{align}
>C(\alpha, \beta)\big( f(x^{(0)}-f^{\star} \big) + \log\log{(1/\epsilon)},
>\end{align}
>trong đó $$C(\alpha, \beta)$$ là một hằng số phụ thuộc vào $$\alpha, \beta$$.

Chứng minh trên tương tự như phân tích hội tụ cho phương pháp Newton, nhưng sử dụng các tính chất của các hàm tự hài hòa để sắp xếp các bước. (Xem [1], tr.503)
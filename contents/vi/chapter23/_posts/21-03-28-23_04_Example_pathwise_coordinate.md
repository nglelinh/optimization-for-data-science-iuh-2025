---
layout: post
title: '23-04 Ví dụ: Pathwise coordinate descent cho lasso'
chapter: '23'
order: 5
owner: YoungJae Choung
categories:
- chapter23
lang: vi
---

Mục này trình bày tổng quan thuật toán hạ theo tọa độ dọc đường chính quy hóa (pathwise coordinate descent) cho bài toán hồi quy Lasso [[Friedman et al. (2007)](https://arxiv.org/pdf/0708.1485.pdf)] [[Friedman et al. (2009)](https://www.jstatsoft.org/article/view/v033i01/v33i01.pdf)].

>**Bài toán hồi quy Lasso:**
> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

Ở [07-03-03 Ví dụ: Điều kiện tối ưu của Lasso]({% multilang_post_url contents/chapter07/21-03-25-07_03_03_example_lasso_optimality_condition %}), ta đã suy ra điều kiện tối ưu bậc nhất cho bài toán này. Nghiệm tối ưu $$\beta$$ thỏa mãn hệ điều kiện sau:

>
> $$
> \begin{align}
> X_1^T(y-X\beta) &= \lambda v_1\\\\
> X_2^T(y-X\beta) &= \lambda v_2\\\\
> \dots\\\\
> X_p^T(y-X\beta) &= \lambda v_p
> \end{align}
> $$

**Lưu ý:** $$X_i$$ ($$i \in \{ 1,2,\dots,p \}$$) là cột thứ $$i$$ của ma trận $$X$$, còn $$v=(v_1,v_2,\dots,v_p)$$ là một dưới đạo hàm (subgradient) của $$\|\beta\|_1$$ tại $$\beta=(\beta_1,\beta_2,\dots,\beta_p)$$:

>
$$
v_i, i \in \{1,2,\dots,p \} = 
\begin{cases}
\{ 1 \}  &\text{if $\beta_i > 0$} \\
\{-1 \}  &\text{if $\beta_i < 0$} \\
[-1,1]   &\text{if $\beta_i = 0$}
\end{cases}
$$

Nhờ hệ điều kiện tối ưu này, ta có thể kiểm tra riêng từng thành phần của $$\beta$$ xem đã tối ưu hay chưa, từ đó chỉ tập trung cập nhật những tọa độ chưa thỏa điều kiện. Ngoài ra, coordinate descent trên Lasso hội tụ rất nhanh khi $$\lambda$$ lớn (vì nghiệm rất thưa); tận dụng tính chất này bằng cách giảm dần $$\lambda$$ và dùng nghiệm trước làm điểm khởi tạo (warm start) giúp tăng tốc đáng kể.

## Thuật toán

### Vòng ngoài (chiến lược pathwise):
* Giải lần lượt theo dãy tham số giảm dần $$\lambda_1 > \lambda_2 > \dots > \lambda_r$$.
* Dùng nghiệm tối ưu tìm được tại $$\lambda_k$$ làm điểm khởi tạo (warm start) cho coordinate descent tại $$\lambda_{k+1}$$.

### Vòng trong (chiến lược tập hoạt động — active set):
* Thực hiện một hoặc vài chu trình tọa độ đầy đủ, rồi ghi nhận các tọa độ khác 0 của $$\beta$$ vào tập hoạt động $$A$$.
* Lặp các chu trình coordinate descent chỉ trên tập $$A$$ cho đến khi hội tụ.
* Kiểm tra điều kiện tối ưu cho toàn bộ $$p$$ tọa độ của $$\beta$$; nếu có tọa độ nào vi phạm, bổ sung tọa độ đó vào $$A$$ và quay lại bước trước.

## Ghi chú

* Về mặt thực nghiệm, giải dọc theo đường tham số $$\lambda$$ (pathwise) thường nhanh hơn nhiều so với việc giải trực tiếp tại một giá trị $$\lambda$$ nhỏ riêng lẻ.
* Chiến lược tập hoạt động tận dụng triệt để tính thưa của nghiệm; do đó coordinate descent cho hồi quy Lasso chạy nhanh hơn nhiều so với hồi quy ridge (tham khảo: [phân tích so sánh hồi quy ridge và lasso](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/)).
* Pathwise coordinate descent hiện vẫn là một trong những thuật toán nhanh nhất cho bài toán hồi quy Lasso.

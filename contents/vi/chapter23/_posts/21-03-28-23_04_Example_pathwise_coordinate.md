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

Trong phần này, ta giới thiệu ngắn gọn tổng quan về Pathwise coordinate descent cho lasso [[Friedman et al. (2007)](https://arxiv.org/pdf/0708.1485.pdf)] [[Friedman et al. (2009)](https://www.jstatsoft.org/article/view/v033i01/v33i01.pdf)]. 

>**Bài toán hồi quy lasso:**
> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

Ở [07-03-03 Ví dụ: Điều kiện tối ưu của Lasso]({% multilang_post_url contents/chapter07/21-03-25-07_03_03_example_lasso_optimality_condition %}) ta đã suy ra điều kiện tối ưu cho bài toán hồi quy lasso. Nghiệm tối ưu của bài toán trên thỏa mãn các điều kiện sau.

>
> $$
> \begin{align}
> X_1^T(y-X\beta) &= \lambda v_1\\\\
> X_2^T(y-X\beta) &= \lambda v_2\\\\
> \dots\\\\
> X_p^T(y-X\beta) &= \lambda v_p
> \end{align}
> $$

**Note:**
$$X_i,i \in \{ 1,2,…,p \}$$ là dữ liệu cột thứ $$i$$ của ma trận $$X$$ đã cho.

Ở đây $$v=(v_1,v_2,\dots,v_p)$$ là một dưới đạo hàm (subgradient) của $$\|\beta\|_1$$ tại $$\beta=(\beta_1,\beta_2,\dots,\beta_p )$$. 
>
$$
v_i, i \in \{1,2,\dots,p \} = 
\begin{cases}
\{ 1 \}  &\text{if $\beta_i > 0$} \\
\{-1 \}  &\text{if $\beta_i < 0$} \\
[-1,1]   &\text{if $\beta_i = 0$}
\end{cases}
$$

Nhờ điều kiện tối ưu này, ta có thể biết từng phần tử của $$\beta$$ hiện đã ở trạng thái tối ưu hay chưa. Với thuật toán coordinate descent, ta có thể giải bài toán lasso hiệu quả hơn bằng cách chỉ cập nhật các phần tử chưa đạt trạng thái tối ưu. Ngoài ra, coordinate descent trên bài toán hồi quy lasso có xu hướng chạy nhanh hơn khi $$\lambda$$ lớn; tận dụng điều này, bằng cách giảm dần $$\lambda$$ (warm start), ta tiếp cận nghiệm nhanh hơn nữa.

## Thuật toán

### Vòng ngoài (chiến lược pathwise):
* Tính nghiệm tối ưu theo thứ tự $$\lambda_1 > \lambda_2 > \dots > \lambda_r$$.
* Kết quả tính được tại tham số điều chỉnh $$\lambda_k$$ được dùng để khởi tạo thuật toán coordinate descent cho $$\lambda_{k+1}$$. (warm start)

### Vòng trong (chiến lược active set):
* Thực hiện một hoặc một vài chu trình tọa độ. Các phần tử khác 0 của $$\beta$$ được ghi vào tập active set $$A$$.
* Thực hiện các chu trình tọa độ chỉ trên các phần tử thuộc $$A$$ cho đến khi hội tụ.
* Kiểm tra điều kiện tối ưu cho mọi phần tử của $$\beta$$. Nếu có phần tử không thỏa điều kiện thì thêm nó vào $$A$$ và quay lại bước đầu của vòng trong.

## Ghi chú
* Về mặt thực nghiệm, chiến lược pathwise hoạt động hiệu quả hơn nhiều so với việc giải trực tiếp bài toán tại một giá trị $$\lambda$$ cho trước.
* Chiến lược active set có lợi thế nhờ tính thưa. Vì vậy coordinate descent chạy nhanh hơn nhiều với hồi quy lasso so với hồi quy ridge. (tham khảo: [phân tích xu hướng của hồi quy ridge và lasso](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/))
* Pathwise coordinate descent cho lasso chạy nhanh ngang với các thuật toán khác được biết là nhanh nhất cho bài toán hồi quy lasso.

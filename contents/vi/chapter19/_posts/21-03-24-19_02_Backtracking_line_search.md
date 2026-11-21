---
layout: post
title: '19-02 Backtracking line search'
chapter: '19'
order: 6
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

**Phương pháp Newton proximal** có thể không hội tụ trong các trường hợp dùng kích thước bước thuần túy $$t_k=1, k=1,2,3, \cdots$$ giống như phương pháp Newton. Do đó, ta cần tối ưu kích thước bước thông qua backtracking line search.

## Thuật toán backtracking line search

1. Khởi tạo các tham số. ($$0 \lt \alpha \le 1/2, 0 \lt \beta \lt 1$$)
2. Ở mỗi vòng lặp, tính hướng Newton proximal $$v = \text{prox}_{H} ( x - H^{-1} \nabla g (x) ) - x$$.
3. Khởi tạo $$t=1$$.
4. Nếu điều kiện $$f(x + tv) \gt f(x) + \alpha t \nabla g(x)^T v + \alpha (h(x + tv) - h(x))$$ được thỏa mãn, giảm $$t=\beta t$$. Lặp lại bước 4 chừng nào điều kiện này còn thỏa mãn. ($$f = g + h$$)
5. Thực hiện cập nhật Newton proximal $$x^+ = x + tv$$.
6. Nếu điều kiện dừng chưa thỏa mãn, quay lại bước 2.

Một cách trực quan, ta tìm kích thước bước $$t$$ sao cho khi di chuyển theo hướng $$v$$ đến một vị trí mà xấp xỉ tuyến tính của hàm $$f$$ tại $$x$$ giảm đi một hệ số $$\alpha$$. Vì phần $$h$$ của $$f$$ không khả vi, ta dùng đạo hàm rời rạc $$h(x + tv) - h(x)$$.

## Hiệu quả của thuật toán
Có nhiều cách thực hiện backtracking line search, và ở đây chúng tôi giới thiệu một trong số đó.

Trong phương pháp này, khi tính $$v$$, toán tử prox chỉ được tính một lần. Trong trường hợp proximal gradient descent, toán tử prox phải được tính lặp đi lặp lại trong vòng lặp bên trong, đây là một đặc điểm khác biệt rõ rệt. Do đó, phương pháp này có thể thực hiện backtracking line search rất hiệu quả khi việc tính toán tử prox phức tạp.

### [tham khảo] Backtracking line search theo từng phương pháp
* Gradient descent [06-02-02 Backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %})
* Proximal gradient descent [09-02 Phân tích hội tụ]({% multilang_post_url contents/chapter09/20-01-08-09_02_convergence_analysis %})
* Phương pháp Newton [14-04 Backtracking line search]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %})

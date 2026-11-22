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

Tương tự phương pháp Newton cổ điển, **phương pháp Newton proximal** có thể không hội tụ nếu luôn dùng bước đơn vị $$t_k = 1$$ ($$k = 1, 2, 3, \dots$$). Vì vậy, cần chọn độ dài bước phù hợp bằng tìm kiếm theo đường lui (backtracking line search).

## Thuật toán tìm kiếm theo đường lui (Backtracking line search)

1. Khởi tạo các tham số $$0 \lt \alpha \le 1/2$$ và $$0 \lt \beta \lt 1$$.
2. Ở mỗi vòng lặp, tính hướng Newton proximal $$v = \text{prox}_{H} ( x - H^{-1} \nabla g (x) ) - x$$.
3. Khởi tạo $$t = 1$$.
4. Khi điều kiện $$f(x + tv) \gt f(x) + \alpha t \nabla g(x)^T v + \alpha (h(x + tv) - h(x))$$ còn đúng, giảm $$t = \beta t$$ và lặp lại kiểm tra (với $$f = g + h$$).
5. Cập nhật nghiệm $$x^+ = x + tv$$.
6. Nếu chưa đạt điều kiện dừng, quay lại bước 2.

Về mặt trực giác, ta tìm độ dài bước $$t$$ sao cho mức giảm thực tế của $$f = g + h$$ dọc theo hướng $$v$$ đạt ít nhất tỷ lệ $$\alpha$$ so với mức giảm dự báo cục bộ. Do phần $$h$$ không khả vi, sự thay đổi của nó được đánh giá trực tiếp qua hiệu $$h(x + tv) - h(x)$$ thay vì đạo hàm.

## Hiệu quả tính toán
Có nhiều biến thể của backtracking line search; cách trình bày ở trên có một ưu điểm tính toán rất đáng chú ý: toán tử prox chỉ cần tính **một lần duy nhất** để xác định hướng $$v$$ trước khi vào vòng lặp giảm $$t$$. Trái lại, trong proximal gradient descent tiêu chuẩn, toán tử prox thường phải được tính lại ở mỗi lần thử độ dài bước bên trong vòng lặp. Nhờ đó, lược đồ này đặc biệt hiệu quả khi việc đánh giá toán tử prox có tỉ lệ tốn kém.

### [Tham khảo] Backtracking line search cho các phương pháp khác
* Gradient descent: [06-02-02 Backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %})
* Proximal gradient descent: [09-02 Phân tích hội tụ]({% multilang_post_url contents/chapter09/20-01-08-09_02_convergence_analysis %})
* Phương pháp Newton: [14-04 Backtracking line search]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %})

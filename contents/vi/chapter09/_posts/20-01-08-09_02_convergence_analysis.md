---
layout: post
title: '09-02 Phân tích hội tụ'
chapter: '09'
order: 3
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---
# Phân tích hội tụ
Trong phần này, chúng ta phân tích tính chất hội tụ của phương pháp gradient gần kề đối với bước cố định và tìm kiếm đường thẳng lùi.

## Giả thiết hội tụ
Đối với hàm mục tiêu $$f(x) = g(x) + h(x)$$, ta giả thiết:

* $$g$$ là hàm lồi, khả vi, **dom**$$(g) = \mathbb{R}^n$$, và $$\nabla g$$ liên tục Lipschitz với hằng số $$L > 0$$.
* $$h$$ là hàm lồi, và ánh xạ gần kề $$\text{prox}_{t}(x) = \underset{z} {\text{argmin}} \{ \parallel x - z \parallel_2^2/ (2t) + h(z) \}$$ có thể tính được.

### Định lý hội tụ với kích thước bước cố định
> **Phương pháp gradient gần kề** với kích thước bước cố định $$t \le 1/L$$ thỏa mãn: 
>\begin{align}
f(x^{(k)}) - f^{\*} \le  \frac{ \lVert x^{(0)} - x^{\*} \rVert^2_2 }{2tk}
\end{align}

Như vậy, phương pháp gradient gần kề đạt tốc độ hội tụ $$O(1/k)$$ hay $$O(1/\epsilon)$$, tương đương với gradient descent trên hàm trơn. Tuy nhiên, đánh giá này tính theo số bước lặp chứ không phải tổng số phép toán (vì chi phí tính $$\text{prox}_t$$ phụ thuộc vào hàm $$h$$).

## Tìm kiếm đường thẳng lùi (Backtracking line search)
Tìm kiếm đường thẳng lùi cho phương pháp gradient gần kề có nguyên lý tương tự gradient descent, nhưng điều kiện kiểm tra chỉ áp dụng trên phần trơn $$g$$ chứ không phải toàn bộ hàm $$f$$.

Chọn tham số $$0 < \beta < 1$$ và khởi tạo $$t=1$$. Ở mỗi bước lặp, ta lặp lại phép co $$t = \beta t$$ chừng nào điều kiện sau còn đúng, và thực hiện bước cập nhật khi điều kiện này không còn thỏa mãn:
> \begin{align}
g(x - tG_t(x)) > g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2
\end{align}

Điều kiện trên kiểm tra xem giá trị của $$g$$ tại điểm đề xuất $$x - tG_t(x)$$ có vượt quá cận trên bậc hai của $$g$$ hay không.

Khi $$h = 0$$ (nên $$G_t(x) = \nabla g(x)$$), bất đẳng thức này trở thành $$g(x - t \nabla g(x)) > g(x) - \frac{t}{2} \lVert \nabla g(x) \rVert_2^2$$, trùng với điều kiện lùi của gradient descent với $$\alpha = 1/2$$.

**Ghi chú:** Xem thêm chi tiết về tìm kiếm đường thẳng lùi cho gradient descent tại [06-02-02 backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %}).

### Thuật toán tìm kiếm đường thẳng lùi
Tóm tắt quy trình thực hiện (với độ dịch chuyển $$\Delta x = - t G_t(x)$$):

1. Khởi tạo tham số co bước $$0 \lt \beta \lt 1$$.
2. Ở mỗi bước lặp, đặt lại $$t = t_{\text{init}}$$ (thường chọn $$t_{\text{init}} = 1$$).
3. Nếu điều kiện $$g(x - tG_t(x)) \gt g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2 $$ thỏa mãn, cập nhật $$t = \beta t$$ và lặp lại bước kiểm tra này.
4. Thực hiện bước cập nhật gradient gần kề: $$ x^+ = x - t G_t(x) = \text{prox}_t(x - t \nabla g(x))$$.
5. Nếu chưa thỏa mãn điều kiện dừng, quay lại bước 2.

Lưu ý rằng trong mỗi lần thử $$t$$ khi lùi, ta phải tính lại $$G_t(x)$$, kéo theo việc tính lại ánh xạ gần kề $$\text{prox}_t$$. Nếu $$\text{prox}_t$$ có chi phí tính toán cao, tổng chi phí của tìm kiếm đường thẳng lùi sẽ tăng lên đáng kể.

### Định lý hội tụ với tìm kiếm đường thẳng lùi
Dưới cùng các giả thiết như trên, phương pháp gradient gần kề kết hợp tìm kiếm đường thẳng lùi vẫn giữ được bậc tốc độ hội tụ $$O(1/k)$$.

>**Phương pháp gradient gần kề** với tìm kiếm đường thẳng lùi thỏa mãn bất đẳng thức sau, với $$t_{\text{min}} = \text{min} \{1,\beta /L \}$$:

> $$
f(x^{(k)})−f^{\star} ≤ \frac{\lVert x^{(0)} − x^{\star} \rVert_{2}^{2}}{2 t_{min}k}, \space t_{\text{min}} = \text{min} \{ 1, \beta / L \} \\
$$

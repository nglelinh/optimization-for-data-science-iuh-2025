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
Trong phần này, chúng ta phân tích sự hội tụ của phương pháp gradient gần kề.

## Phân tích hội tụ
Đối với hàm mục tiêu $$f(x) = g(x) + h(x)$$, chúng ta giả định như sau:

* $$g$$ là hàm lồi, khả vi, và **dom**$$(g) = \mathbb{R}^n$$, và $$\nabla g$$ liên tục Lipschitz ($$L > 0$$).
* $$h$$ là hàm lồi, và $$\text{prox}_{t}(x) = \underset{z} {\text{argmin}} \{ \parallel x - z \parallel_2^2/ (2t) + h(z) \}$$ cần được tính toán.

### Định lý hội tụ
> **Phương pháp gradient gần kề** thỏa mãn phương trình sau với kích thước bước cố định $$t \le 1/L$$: 
>\begin{align}
f(x^{(k)}) - f^{\*} \le  \frac{ \lVert x^{(0)} - x^{\*} \rVert^2_2 }{2tk}
\end{align}

Phương pháp gradient gần kề có tốc độ hội tụ $$O(1/k)$$ hoặc $$O(1/\epsilon)$$, đây là hiệu suất tương tự như gradient descent. Tuy nhiên, hiệu suất này dựa trên số lần lặp, không phải số phép toán. (Số phép toán có thể thay đổi tùy thuộc vào hàm $$h$$.)

## Tìm kiếm đường thẳng lùi (Backtracking line search)
Phương pháp tìm kiếm đường thẳng lùi của gradient gần kề tương tự như gradient descent nhưng chỉ hoạt động trên phần trơn $$g$$, không phải hàm $$f$$.

Đầu tiên, đặt tham số $$0 < \beta < 1$$ và bắt đầu với $$t=1$$. Trong mỗi lần lặp, giảm $$t$$ thành $$t = \beta t$$ trong khi thỏa mãn điều kiện sau, và cập nhật gradient gần kề nếu điều kiện không được thỏa mãn.
> \begin{align}
g(x - tG_t(x)) > g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2
\end{align}

Điều kiện lùi này có nghĩa là giá trị của hàm $$g$$ tại vị trí bước tiếp theo $$x - tG_t(x)$$ lớn hơn giá trị của xấp xỉ Taylor bậc hai của hàm $$g$$.

Nếu $$G_t(x) = \nabla g(x)$$ trong phương trình này, chúng ta có thể thấy rằng $$g(x - t \nabla g(x)) > g(x) - \alpha t \lVert \nabla g(x) \rVert_2^2 $$, điều này trở nên giống hệt với điều kiện lùi của gradient descent.

**Ghi chú:** Để biết thêm chi tiết về backtracking của gradient descent, tham khảo [06-02-02 backtracking line search]({% multilang_post_url contents/chapter06/21-03-20-06_02_02_backtracking_line_search %}).

### Thuật toán tìm kiếm đường thẳng lùi
Nếu chúng ta tóm tắt điều này trong một thuật toán, nó như sau. (Tuy nhiên, $$\nabla x = - t G_t(x)$$)

1. Khởi tạo các tham số. ($$0 \lt \beta \lt 1$$, $$0 \lt \alpha \le 1/2$$)
2. Trong mỗi lần lặp, khởi tạo $$t = t_{\text{init}}$$. ($$t_{\text{init}} = 1$$)
3. Nếu điều kiện $$g(x - tG_t(x)) \gt g(x) - t \nabla g(x)^T G_t(x) + \frac{t}{2} \parallel G_t(x) \parallel_2 ^2 $$ được thỏa mãn, giảm $$t = \beta t$$. Lặp lại bước 3 trong khi điều kiện này được thỏa mãn.
4. Thực hiện cập nhật gradient descent $$ x^+ = x - t G_t(x) = \text{prox}_t(x - t \nabla g(x))$$.
5. Nếu điều kiện dừng không được thỏa mãn, quay lại bước 2.

Khi lùi trong gradient gần kề, vì $$G_t(x)$$ được tính toán lặp đi lặp lại, ánh xạ gần kề được bao gồm trong $$G_t(x)$$ cũng được tính toán lặp đi lặp lại. Vì ánh xạ gần kề rất tốn kém để tính toán, chi phí tính toán tổng thể của backtracking có thể cao.

### Định lý hội tụ
Dưới các giả định tương tự như trên, phương pháp tìm kiếm đường thẳng lùi cũng thỏa mãn hiệu suất tương tự.

>**Phương pháp gradient gần kề** thỏa mãn phương trình sau cho tìm kiếm đường thẳng lùi. Kích thước bước là $$t_{\text{min}} = \text{min} \{1,\beta /L \}$$.

> $$
f(x^{(k)})−f^{\star} ≤ \frac{\lVert x^{(0)} − x^{\star} \rVert_{2}^{2}}{2 t_{min}k}, \space t_{\text{min}} = \text{min} \{ 1, \beta / L \} \\
$$

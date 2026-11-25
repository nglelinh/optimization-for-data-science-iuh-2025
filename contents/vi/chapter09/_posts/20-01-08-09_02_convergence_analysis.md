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

Vì sao phương pháp gradient gần kề lại vượt xa phương pháp subgradient cả một bậc tốc độ — từ $$O(1/\epsilon^2)$$ nhảy vọt lên $$O(1/\epsilon)$$ — dù cùng giải bài toán không trơn? Câu trả lời nằm trong **độ dốc tổng quát (generalized gradient map)** $$G_t(x) = \frac{1}{t}\big(x - \operatorname{prox}_{t h}(x - t\nabla g(x))\big)$$. Khi viết lại vòng lặp dưới dạng $$x^+ = x - t G_t(x)$$, ta nhận ra một phép màu giải tích: gần như toàn bộ chứng minh hội tụ của gradient descent trên hàm trơn được "tái sinh" gần như nguyên vẹn!

Tuy nhiên, trong thực hành có một trở ngại quen thuộc: ta hiếm khi biết trước hằng số Lipschitz $$L$$ của $$\nabla g$$ (chẳng hạn với ma trận $$A$$ khổng lồ, tính giá trị kỳ dị lớn nhất $$\|A\|_2^2$$ rất tốn kém). Đó là lý do nửa sau bài học giới thiệu **tìm kiếm đường thẳng lùi (backtracking line search)** cho bài toán tổng hợp — một điều kiện dừng tinh gọn chỉ kiểm tra độ cong trên riêng phần trơn $$g$$ mà vẫn bảo toàn nguyên vẹn tốc độ $$O(1/k)$$.

## Bản đồ kiến thức nền: Bốn trụ cột của chứng minh hội tụ gradient gần kề

- **Bất đẳng thức trơn $$L$$-Lipschitz của $$\nabla g$$:** Mọi hàm $$g$$ có $$\nabla g$$ liên tục $$L$$-Lipschitz đều bị chặn trên bởi parabol:
  $$g(y) \le g(x) + \nabla g(x)^T(y - x) + \frac{L}{2}\|y - x\|_2^2.$$
  Điều kiện $$t \le 1/L$$ đảm bảo mô hình parabol dùng trong bước prox luôn nằm trên $$g(y)$$.
- **Bản đồ gradient tổng quát $$G_t(x)$$ và tính giảm đơn điệu:** Định nghĩa $$G_t(x) = \frac{x - x^+}{t}$$. Theo điều kiện tối ưu của bài toán con prox, $$G_t(x) - \nabla g(x) \in \partial h(x^+)$$. Từ đó suy ra bất đẳng thức giảm cốt lõi cho mọi điểm $$z$$:
  $$f(x^+) \le f(z) + G_t(x)^T(x - z) - \frac{t}{2}\|G_t(x)\|_2^2.$$
  Đặt $$z = x$$ cho ngay $$f(x^+) \le f(x) - \frac{t}{2}\|G_t(x)\|_2^2$$ (giảm chặt đơn điệu!); đặt $$z = x^*$$ và cộng dồn cho ra ngay cận $$\frac{\|x^{(0)} - x^*\|_2^2}{2 t k}$$.
- **Tìm kiếm đường thẳng lùi (Backtracking Line Search):** Khi không biết $$L$$, ta bắt đầu từ $$t$$ lớn và nhân $$t \leftarrow \beta t$$ ($$\beta \in (0, 1)$$) cho tới khi thỏa điều kiện chặn trên parabol cho riêng phần trơn $$g$$:
  $$g(x - t G_t(x)) \le g(x) - t\nabla g(x)^T G_t(x) + \frac{t}{2}\|G_t(x)\|_2^2.$$
  Lưu ý: mỗi lần thu nhỏ $$t$$ phải tính lại $$x^+ = \operatorname{prox}_{t h}(x - t\nabla g(x))$$, nên $$h$$ cần có prox thật nhẹ.
- **Bảo toàn hằng số tốc độ khi dùng backtracking:** Vì điều kiện backtracking chắc chắn dừng ngay khi $$t \le 1/L$$, bước được chọn luôn thỏa $$t_k \ge \min(t_0, \beta/L)$$, nên cận hội tụ chỉ tăng thêm tối đa một hệ số hằng $$1/\beta$$.

### Khung giải thích (nên đọc chậm): Kiểm chứng tay điều kiện backtracking và cận $$O(1/k)$$

Xét $$g(x) = 2x^2$$ (nên $$\nabla g(x) = 4x$$ và $$L = 4$$, ngưỡng an toàn là $$1/L = 0.25$$) và $$h(x) = |x|$$ (nghiệm tối ưu $$x^* = 0, f^* = 0$$). Bắt đầu từ $$x^{(0)} = 1$$, giả sử ta *không biết* $$L = 4$$ và thử backtracking với $$t = 1.0$$, hệ số thu hẹp $$\beta = 0.5$$.

1. **Thử $$t = 1.0$$:**
   - $$v = x^{(0)} - 1.0 \cdot \nabla g(1) = 1 - 4 = -3$$.
   - $$x^+ = S_{1.0}(-3) = -2$$, suy ra $$G_1(1) = \frac{1 - (-2)}{1} = 3$$.
   - Kiểm tra điều kiện backtracking trên $$g(x) = 2x^2$$:
     - Vế trái: $$g(x^+) = 2(-2)^2 = 8$$.
     - Vế phải: $$g(1) - 1(4)(3) + \frac{1}{2}(3)^2 = 2 - 12 + 4.5 = -5.5$$.
     - Vì $$8 > -5.5$$, điều kiện **vi phạm** $$\implies$$ thu nhỏ $$t \leftarrow 0.5$$!
2. **Thử $$t = 0.5$$:**
   - $$v = 1 - 0.5(4) = -1$$, $$x^+ = S_{0.5}(-1) = -0.5$$, $$G_{0.5}(1) = \frac{1 - (-0.5)}{0.5} = 3$$.
   - Vế trái: $$g(-0.5) = 0.5$$; vế phải: $$2 - 0.5(4)(3) + \frac{0.5}{2}(9) = 2 - 6 + 2.25 = -1.75$$. Vẫn vi phạm ($$0.5 > -1.75$$) $$\implies$$ thu nhỏ $$t \leftarrow 0.25$$!
3. **Thử $$t = 0.25$$ (chạm đúng $$1/L$$):**
   - $$v = 1 - 0.25(4) = 0$$, $$x^+ = S_{0.25}(0) = 0$$, $$G_{0.25}(1) = \frac{1 - 0}{0.25} = 4$$.
   - Vế trái: $$g(0) = 0$$; vế phải: $$2 - 0.25(4)(4) + \frac{0.25}{2}(16) = 2 - 4 + 2 = 0$$.
   - Thỏa mãn $$0 \le 0$$! Thuật toán chấp nhận $$t = 0.25$$ và nhảy thẳng tới đúng nghiệm tối ưu $$x^{(1)} = 0$$!

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

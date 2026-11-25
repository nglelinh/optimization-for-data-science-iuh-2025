---
layout: post
title: '08-02-01 Phương pháp Subgradient Ngẫu nhiên'
chapter: '08'
order: 12
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Nếu bạn đứng giữa một căn phòng đông người đang tranh cãi và muốn tìm hướng đi chung của cả phòng, bạn có hai lựa chọn: hỏi lần lượt từng người theo vòng tròn quanh bàn (tuần hoàn — *cyclic*), hoặc rút thăm ngẫu nhiên một người để hỏi ở mỗi bước (*randomized*). Trong tối ưu hóa tổng hữu hạn $$\min_x \sum_{i=1}^m f_i(x)$$, hai cách chọn chỉ số $$i_k$$ này tạo ra hai biến thể cốt lõi của phương pháp subgradient ngẫu nhiên.

Tưởng như chỉ là chi tiết cài đặt nhỏ, nhưng sự khác biệt giữa chọn tuần hoàn và chọn ngẫu nhiên lại có tác động mạnh đến cả lý thuyết lẫn thực tế: dữ liệu sắp xếp theo thứ tự xấu (ví dụ toàn bộ mẫu dương đứng trước, mẫu âm đứng sau) có thể làm biến thể tuần hoàn chao đảo theo chu kỳ dài, trong khi rút thăm ngẫu nhiên (hoặc xáo trộn dữ liệu mỗi epoch) phá vỡ hoàn toàn các mẫu tuần hoàn bất lợi đó.

## Bản đồ kiến thức nền: Ba trụ cột của thuật toán subgradient ngẫu nhiên

- **Công thức cập nhật một mẫu (hoặc mini-batch):** Thay vì tính $$\sum_{i=1}^m g_i^{(k-1)}$$, ta chọn một chỉ số $$i_k \in \{1, \dots, m\}$$ và cập nhật $$x^{(k)} = x^{(k-1)} - t_k g_{i_k}^{(k-1)}$$ với $$g_{i_k}^{(k-1)} \in \partial f_{i_k}(x^{(k-1)})$$. Dùng mini-batch cỡ $$B$$ là trung dung giữa $$B = 1$$ (nhanh, nhiễu cao) và $$B = m$$ (chậm, không nhiễu).
- **Quy tắc tuần hoàn (Cyclic) vs. Quy tắc ngẫu nhiên (Randomized):** Quy tắc tuần hoàn quét $$1, 2, \dots, m, 1, 2, \dots$$ đảm bảo mọi mẫu được thăm đúng một lần mỗi epoch, nhưng dễ bị thiên lệch nếu thứ tự dữ liệu có cấu trúc. Quy tắc ngẫu nhiên chọn độc lập đều trên $$\{1, \dots, m\}$$ đảm bảo tính không chệch ở mọi bước và tránh mọi thứ tự đối kháng.
- **Lịch bước và tính tương thích với bài toán không trơn:** Giống hệt phương pháp subgradient batch, ta không thể dùng line search trên từng $$f_{i_k}$$ đơn lẻ (vì làm giảm $$f_{i_k}$$ có thể phá hỏng các $$f_j$$ khác), nên phải chọn bước cố định nhỏ hoặc bước giảm dần thỏa $$\sum t_k = \infty, \sum t_k^2 < \infty$$.

### Khung giải thích (nên đọc chậm): Chạy tay 3 bước subgradient ngẫu nhiên để tìm trung vị của 3 điểm

Xét bài toán tìm trung vị của 3 số $$\{1, 2, 5\}$$:
$$\min_{x \in \mathbb{R}} \; f(x) = |x - 1| + |x - 2| + |x - 5| = f_1(x) + f_2(x) + f_3(x).$$
Nghiệm tối ưu chính xác là trung vị $$x^* = 2$$ với $$f^* = 1 + 0 + 3 = 4$$. Bắt đầu tại $$x^{(0)} = 0$$ ($$f(0) = 8$$) với lịch bước $$t_k = 1/k$$.

1. **Bước 1 ($$t_1 = 1$$), rút ngẫu nhiên $$i_1 = 3$$ ($$f_3(x) = |x - 5|$$):**
   Tại $$x^{(0)} = 0 < 5$$, $$g_3(0) = -1$$.
   $$x^{(1)} = 0 - 1(-1) = 1.0, \quad f(1) = 0 + 1 + 4 = 5.$$
2. **Bước 2 ($$t_2 = 0.5$$), rút ngẫu nhiên $$i_2 = 1$$ ($$f_1(x) = |x - 1|$$):**
   Tại $$x^{(1)} = 1$$, chọn $$g_1(1) = 0 \in [-1, 1]$$.
   $$x^{(2)} = 1.0 - 0.5(0) = 1.0, \quad f(1) = 5.$$
3. **Bước 3 ($$t_3 = 1/3 \approx 0.333$$), rút ngẫu nhiên $$i_3 = 2$$ ($$f_2(x) = |x - 2|$$):**
   Tại $$x^{(2)} = 1 < 2$$, $$g_2(1) = -1$$.
   $$x^{(3)} = 1.0 - \frac{1}{3}(-1) = 1.333, \quad f(1.333) = 0.333 + 0.667 + 3.667 = 4.667.$$
Chỉ sau **3 phép tính subgradient đơn lẻ** (tương đương đúng 1 vòng lặp batch!), giá trị hàm đã tụt từ $$8$$ xuống $$4.667$$ — rất gần đáy $$f^* = 4$$.

Xét bài toán cực tiểu hóa tổng của $$m$$ hàm lồi sau:

>$$
\begin{equation}
\min_x \sum_{i=1}^m f_i(x)
\end{equation}
$$

Nếu áp dụng phương pháp subgradient tiêu chuẩn, ở mỗi bước lặp ta phải tính subgradient cho toàn bộ $$m$$ hàm $$f_i$$ rồi cộng lại (tương tự như động cơ dẫn đến [stochastic gradient descent]({% multilang_post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %})).

Thay vì tính trên toàn bộ tổng, phương pháp subgradient ngẫu nhiên chỉ cập nhật theo một hàm thành phần tại mỗi bước:

>$$
\begin{align}
x^{(k)} = x^{(k-1)} - t_k \cdot g_{i_k}^{(k-1)}, \quad k = 1, 2, 3, . . . 
\end{align}
$$

Trong đó, $$i_k \in \{1,...,m\}$$ là chỉ số được chọn tại bước lặp thứ $$k$$, và $$g_{i}^{(k-1)} \in \partial f_{i}(x^{k-1})$$. Cách chọn chỉ số $$i_k$$ — theo thứ tự tuần hoàn (cyclic) hay chọn ngẫu nhiên (randomized) — sẽ ảnh hưởng đến tốc độ hội tụ, như sẽ phân tích ở bài tiếp theo. Hướng cập nhật này khác với [phương pháp subgradient]({% multilang_post_url contents/chapter08/20-03-29-08_01_subgradient_method %}) thông thường (còn gọi là phương pháp subgradient batch hoặc full batch), vốn dùng tổng $$\sum_{i=1}^{m} g_i^{(k-1)}$$.

Khi mọi hàm $$f_i$$ ($$i = 1,...,m$$) đều khả vi, thuật toán này trở về đúng stochastic gradient descent; do đó, phương pháp subgradient ngẫu nhiên là một dạng tổng quát hơn.
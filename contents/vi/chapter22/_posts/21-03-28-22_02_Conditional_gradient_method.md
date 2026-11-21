---
layout: post
title: 22-02 Phương pháp gradient có điều kiện
chapter: '22'
order: '3'
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---

## Gradient descent có chiếu (Projected Gradient Descent)

Hãy xét bài toán có ràng buộc sau.

>$$\min_{x} f(x) \qquad \text{ thỏa mãn } x \in C$$

Trước đây ta đã thấy rằng nếu $$f$$ lồi và trơn, và $$C$$ cũng lồi, ta có thể dùng phương pháp **projected gradient descent**. Gọi $$P_{C}$$ là toán tử chiếu lên tập $$C$$; với giá trị khởi tạo $$x^{(0)}$$ và $$k = 1, 2, 3, ...$$, ta có công thức sau.

>$$x^{(k)} = P_{C} \bigl( x^{(k−1)} − t_k\nabla f(x^{(k−1)}) \bigr)$$

Projected gradient descent cũng có thể được biểu diễn như một trường hợp đặc biệt của gradient gần kề (proximal gradient descent), vốn xuất phát từ việc giá trị $$y$$ trong khai triển bậc hai cục bộ (khai triển Taylor bậc hai) trở thành $$x^{(k)}$$ tiếp theo.

>$$x^{(k)} = P_{C} \Bigl( \arg\min_{y} \nabla f(x^{(k−1)})^T(y − x^{(k−1)}) + \frac{1}{2t} \| y − x^{(k−1)} \|^2_2 \Bigr)$$

Để biết thêm chi tiết về Projected Gradient Descent, hãy xem [9-4]({% multilang_post_url contents/chapter09/20-01-08-09_04_special_cases %}).

## Phương pháp gradient có điều kiện (Frank-Wolfe)

Thay vì cực tiểu hóa xấp xỉ bậc hai ở đây, ta thử một cách đơn giản hơn. Trước hết, hãy xem điểm làm cực tiểu tích vô hướng của các điểm trong tập $$C$$ với $$\nabla f(x)$$. Về bản chất, thay vì chiếu, ta có thể giải bài toán thuận tiện và hiệu quả hơn bằng cách cực tiểu hóa hàm tuyến tính trên các điểm của tập $$C$$. Sau đó ta tiến hành bằng cách dùng tổ hợp lồi giữa điểm hiện tại và điểm cực tiểu đó.

Hãy xem phương pháp được hình thức hóa như sau. Chọn giá trị khởi tạo $$x^{(0)} \in C$$. Với $$k = 1, 2, 3, ...$$:

>$$\begin{array}{rcl}
>s^{(k−1)} & \in & \arg\min_{s \in C} \nabla f(x^{(k−1)})^Ts \\
>x^{(k)} & = & (1 − \gamma_k)x^{(k−1)} + \gamma_ks^{(k−1)}
>\end{array}$$

### [Tham khảo]

>$$f(y) \approx f(x) + \nabla f(x)(y-x)$$
>
>$$\arg\min_y f(x) + \nabla f(x)(y-x) \equiv \arg\min_y \nabla f(x)y$$

Ở đây, khác với trước, khi cập nhật mà không qua bước chiếu, ta giải bài toán bằng các điểm trong tập ràng buộc $$C$$. Về cơ bản, kích thước bước được đặt là $$\gamma_k = \frac{2}{k + 1}, k = 1, 2, 3, ...$$ Với mọi $$0 \leq \gamma_k \leq 1$$, do tính lồi nên $$x^{(k)} \in C$$ được đảm bảo. Ngoài ra, cập nhật còn có thể viết như sau:

>$$x^{(k)} = x^{(k−1)} + \gamma_k\bigl( s^{(k−1)} − x^{(k−1)} \bigr)$$

Nghĩa là, khi thuật toán chạy, ta di chuyển dần dần ít hơn theo hướng của điểm cực tiểu tuyến tính. Trong nhiều trường hợp, dùng phương pháp này trên hình cầu L1 (một trường hợp đặc biệt của coordinate descent) dễ giải hơn so với dùng phép chiếu.

### [Tham khảo]

Một điều thú vị là Frank và Wolfe là các nghiên cứu sinh sau tiến sĩ làm việc cùng với Tucker. Họ lần đầu đề xuất thuật toán với hai hàm khác nhau. Thuật toán được công bố năm 1956 và sau đó được đăng thành bài báo. Trong một thời gian dài sau đó, không có bài báo tiếp nối nào về chủ đề này. Tuy nhiên, những năm gần đây nó lại được chú ý nhờ những hiểu biết của Jaggi và được giới thiệu trở lại.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/frank_wolfe.png" alt="[Hình 1] Phương pháp gradient có điều kiện (Frank-Wolfe) (Jaggi 2011)[3]">
  <figcaption style="text-align: center;">[Hình 1] Phương pháp gradient có điều kiện (Frank-Wolfe) (Jaggi 2011)[3]</figcaption>
</p>
</figure>

## Ràng buộc chuẩn

Điều gì xảy ra khi $$C = \{x : \| x \| \leq t \}$$ với chuẩn $$\| \cdot \|$$? Hãy xem:

>$$\begin{align}
>s &\in \arg\min_{\|s\|\leq t} \nabla f(x^{(k−1)})^Ts \\
>&= −t \cdot \arg\max_{\|s\|\leq 1} \nabla f(x^{(k−1)})^Ts \\
>&= −t \cdot \partial \| \nabla f(x^{(k−1)}) \|_{*}
>\end{align}$$

Ở đây $$\| \cdot \|_{*}$$ là chuẩn đối ngẫu. Nói cách khác, nếu ta biết cách tính dưới đạo hàm của chuẩn đối ngẫu, ta có thể dễ dàng thực hiện bước Frank-Wolfe. Điểm mấu chốt của Frank-Wolfe là với $$C = \{x : \| x \| \leq t \}$$, bước này có thể thu được đơn giản hơn hoặc rẻ hơn phương pháp chiếu, và cũng đơn giản hơn hoặc rẻ hơn toán tử prox của $$\| \cdot \|$$.

## Ví dụ: chính quy hóa $$l_1$$

Sau đây là bài toán **chính quy hóa $$l_1$$**:

>$$\min_x f(x) \qquad \text{ thỏa mãn } \| x \|_1 \leq t$$

Khai triển theo công thức trước, ta được $$s^{(k−1)} \in −t\partial \|\nabla f(x^{(k−1)}) \|_\infty$$. Phương pháp Frank-Wolfe cập nhật qua quy trình sau:

>$$\begin{array}{rcl}
>i_{k−1} & \in & \arg\max_{i=1,...,p} |\nabla_i f(x^{(k−1)})| \\
>x^{(k)} & = & (1 − \gamma_k)x^{(k−1)} − \gamma_kt \cdot \text{sign}(\nabla_{i_{k−1}} f(x^{(k−1)})) \cdot e_{i_{k−1}}
>\end{array}$$

Đây là một dạng của coordinate descent (ta sẽ xem coordinate descent chi tiết ở phần sau).

**Lưu ý**: Cả hai đều cần độ phức tạp $$O(n)$$, nhưng phép chiếu lên hình cầu $$l_1$$ đơn giản hơn nhiều.

## Ví dụ: chính quy hóa $$l_p$$

Sau đây là bài toán chính quy hóa $$l_p$$:

>$$\min_{x} f(x) \qquad \text{ thỏa mãn } \| x \|_{p} \leq t$$

Khi $$1 \leq p \leq \infty$$ và $$q$$ là đối ngẫu của $$p$$, ta có $$s^{(k−1)} \in −t\partial \| \nabla f(x^{(k−1)}) \|_{q}$$, tức là $$1/p + 1/q = 1$$. Ta có thể chọn như sau:

>$$s_i^{(k−1)} = −\alpha \cdot \text{sign}(\nabla f_i(x^{(k−1)})) \cdot \left| \nabla f_i(x^{(k−1)}) \right|^{q-1}, \quad i = 1, ..., n$$

Ở đây $$\alpha$$ là hằng số sao cho $$\| s^{(k-1)} \|_{p} = t$$, và cập nhật Frank-Wolfe vẫn như cũ.

**Lưu ý**: Với trường hợp $$p$$ tổng quát, **phép chiếu lên hình cầu p** đơn giản hơn nhiều. Trừ các trường hợp đặc biệt ($$p = 1, 2, \infty$$), những phép chiếu như vậy không thể tính trực tiếp (phải xử lý bằng tối ưu hóa).

## Ví dụ: chính quy hóa chuẩn vết (trace norm)

Hãy xem bài toán **chính quy hóa vết**:

>$$\min_{X} f(X) \qquad \text{ thỏa mãn } \| X \|_{tr} \leq t$$

Ta có $$S^{(k−1)} \in −t \cdot \partial\| \nabla f(X^{(k−1)}) \|_{op}$$. Ta có thể chọn $$S^{(k−1)}$$ như sau:

>$$S^{(k−1)} = −t \cdot uv^T$$

Ở đây $$u, v$$ là các vector kỳ dị trái và phải của $$\nabla f(X^{(k−1)})$$, và cập nhật Frank-Wolfe vẫn như thường lệ.

**Lưu ý**: Phương pháp này, nếu có thể phân rã giá trị kỳ dị (SVD), đơn giản và hiệu quả hơn nhiều so với **phép chiếu lên hình cầu chuẩn vết**.

## Dạng ràng buộc và dạng Lagrange

Hãy xem lại bài toán có ràng buộc một lần nữa:

>$$\min_x f(x) \qquad \text{ thỏa mãn } \| x \| \leq t$$

Bài toán Lagrange sau tương đương với bài toán trên:

>$$\min_x f(x) + \lambda \| x \|$$

Các tham số điều chỉnh $$t$$ và $$\lambda$$ thay đổi trong khoảng $$[0,\infty]$$. Ngoài ra, ta nên so sánh cập nhật Frank-Wolfe của $$\| \cdot \|$$ với toán tử gần kề (proximal operator) của $$\| \cdot \|$$.

• **Chuẩn $$l_1$$**: Phương pháp Frank-Wolfe cập nhật bằng cách quét tìm giá trị lớn nhất của gradient. Toán tử gần kề cập nhật bằng co ngưỡng mềm (soft-thresholding). Cả hai bước đều dùng $$O(n)$$ flops.

• **Chuẩn $$l_p$$**: Cập nhật Frank-Wolfe nâng từng thành phần của gradient lên lũy thừa rồi cộng tất cả, tốn $$O(n)$$ flops. Toán tử gần kề nói chung không thể tính trực tiếp.

• **Chuẩn vết**: Cập nhật Frank-Wolfe chỉ tính các vector kỳ dị trái và phải của gradient. Toán tử gần kề co ngưỡng mềm các giá trị kỳ dị của bước gradient, đòi hỏi phân rã giá trị kỳ dị (SVD).

Nhiều bộ chính quy hóa khác nhau đã có các cập nhật Frank-Wolfe hiệu quả, chẳng hạn các ràng buộc đa diện hoặc nón đặc biệt, chính quy hóa tổng các chuẩn (theo nhóm), chuẩn nguyên tử, v.v.

Khi so sánh hiệu năng của kỹ thuật projected gradient và kỹ thuật gradient có điều kiện cho bài Lasso có ràng buộc (ở đây $$n=100, p = 500$$):

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/comparing_projected_and_conditional_gradient.png" alt="[Hình 2] So sánh gradient có chiếu và gradient có điều kiện cho bài lasso có ràng buộc [3]">
  <figcaption style="text-align: center;">[Hình 2] So sánh gradient có chiếu và gradient có điều kiện cho bài lasso có ràng buộc [3]</figcaption>
</p>
</figure>

Ta thấy phương pháp Frank-Wolfe có tốc độ hội tụ tương tự các phương pháp bậc nhất. Tuy nhiên, thực tế nó có thể hội tụ chậm hơn khi cần độ chính xác cao. (Tham khảo: ở đây dùng kích thước bước cố định, nhưng dùng line search có thể cải thiện tốc độ hội tụ.)

## Khoảng cách đối ngẫu (Duality gap)

Trong quá trình lặp Frank-Wolfe, một khoảng cách đối ngẫu xuất hiện một cách tự nhiên, và thực chất nó chính là khoảng cách tới tối ưu (suboptimality gap).

>$$g(x^{(k-1)}) := \max_{s\in C} \nabla f(x^{(k−1)})^T(x^{(k−1)} − s)$$

Đây là một cận trên của $$f(x^{(k−1)}) − f^{*}$$.

### [Chứng minh]

Ta có thể chứng minh bằng điều kiện bậc nhất của tính lồi:

>$$f(s) \geq f(x^{(k−1)}) + \nabla f(x^{(k−1)})^T(s − x^{(k−1)})$$

Cực tiểu hóa cả hai vế theo mọi $$s \in C$$:

>$$f^{*} \geq f(x^{(k−1)}) + \min_{s\in C} \nabla f(x^{(k−1)})^T(s − x^{(k−1)})$$

Cuối cùng, sắp xếp lại cho thấy biểu thức sau là cận trên của khoảng cách đối ngẫu:

>$$\max_{s\in C} \nabla f(x^{(k−1)})^T(x^{(k−1)} − s) = \nabla f(x^{(k−1)})^T(x^{(k−1)} − s^{(k−1)})$$

### [Ghi chú]

Do đó, đại lượng này đến trực tiếp từ cập nhật Frank-Wolfe. Vì sao ta gọi đây là "khoảng cách đối ngẫu"? Ta có thể viết lại bài toán gốc như sau:

>$$\min_{x} f(x) + I_C(x)$$

Ở đây $$I_C$$ là hàm chỉ thị của $$C$$. Bài toán đối ngẫu là:

>$$\max_u −f^{*}(u) − I^{*}_C(−u)$$

$$I_C^{*}$$ là hàm tựa (support function) của $$C$$. Ta đã thấy trước đó rằng liên hợp của hàm chỉ thị chính là hàm tựa.

### [Nhắc lại]

>$$I_C(x) = \begin{cases}
>+\infty & \text{nếu } x \notin C \\
>0 & \text{nếu } x \in C
>\end{cases}$$
>
>$$\begin{align}
>I_C^{*} &= \max_{x} \{\langle s, x \rangle - I_C(x)\} \\
>&= \max_{x \in C} \langle s, x \rangle \\
>&= \text{Hàm tựa của } C \text{ tại } s
>\end{align}$$

Khi $$x = x^{(k-1)}, u = \nabla f(x^{(k-1)})$$, khoảng cách đối ngẫu tại $$x, u$$ như sau (suy ra từ 13-04 [bất đẳng thức Fenchel]({% multilang_post_url contents/chapter13/21-04-05-13_04_Conjugate_function %})):

>$$f(x) + f^{*}(u) + I^{*}_C(−u) \geq x^Tu + I^{*}_C(−u)$$

### Frank-Wolfe trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/frank-wolfe_vi.mp4"></video>
</div>

Mỗi bước chọn đỉnh $$s$$ làm cực tiểu $$\langle \nabla f(x), s\rangle$$ và chuyển tới $$(1-\gamma_k)x + \gamma_k s$$, nên điểm lặp không bao giờ rời $$C$$.

### Tự tay thử: các bước Frank-Wolfe

<div class="opx-explainer" data-opx="fw" data-lang="vi"></div>

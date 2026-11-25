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

Hãy tưởng tượng bạn đang đứng trong một căn phòng đa giác lồi và muốn tìm điểm thấp nhất của một mặt sàn cong mềm mại. Phương pháp Projected Gradient Descent (PGD) bảo bạn cứ bước thẳng xuống dốc; nếu lỡ đâm xuyên ra ngoài tường, hãy tìm điểm gần nhất trên tường để kéo mình quay lại. Nghe rất hợp lý — cho đến khi căn phòng là một quả cầu chuẩn vết của ma trận $$10{,}000 \times 10{,}000$$, nơi việc "tìm điểm gần nhất trên tường" tốn hàng giờ tính toán mỗi bước.

Phương pháp **gradient có điều kiện (Frank–Wolfe)** đảo ngược hoàn toàn tư duy đó: thay vì bước ra ngoài rồi chiếu vào trong, ta đứng nguyên trong phòng, nhìn theo hướng dốc xuống mạnh nhất, chọn **góc tường** nằm xa nhất theo hướng đó, rồi bước một đoạn thẳng về phía góc tường ấy. Không bao giờ ra khỏi miền khả thi, không bao giờ cần phép chiếu, và mỗi bước chỉ thêm đúng một "nguyên tử" cấu trúc vào nghiệm.

## Kiến thức cần nhớ: Bốn mảnh ghép cốt lõi của bài học

Bài học này đặt nền móng cho toàn bộ Chương 22 thông qua bốn trụ cột liên kết chặt chẽ:

- **Chuẩn đối ngẫu (Dual Norm) và Bộ giải LMO:** Với ràng buộc dạng chuẩn $$\|x\| \le t$$, bài toán tuyến tính $$\min_{\|s\| \le t} \nabla f(x)^T s$$ có liên hệ trực tiếp với chuẩn đối ngẫu $$\|\nabla f(x)\|_* = \max_{\|s\| \le 1} \nabla f(x)^T s$$. Vì chuẩn đối ngẫu của $$\ell_1$$ là $$\ell_\infty$$ và của chuẩn vết là chuẩn phổ, LMO rút gọn thành thao tác cực rẻ: tìm phần tử lớn nhất hoặc cặp vector kỳ dị hàng đầu.
- **Tính thưa và Hạng thấp tự nhiên (Implicit Sparsity & Low-Rank):** Vì $$x^{(k)}$$ là tổ hợp lồi của điểm khởi tạo và các đỉnh $$s^{(0)}, \dots, s^{(k-1)}$$, sau $$k$$ bước, nghiệm của Frank–Wolfe trên quả cầu $$\ell_1$$ có nhiều nhất $$k$$ tọa độ khác $$0$$ (nếu khởi tạo từ $$0$$), và trên quả cầu chuẩn vết có hạng không vượt quá $$k$$.
- **Tương đương giữa dạng ràng buộc và dạng Lagrange:** Trong thống kê và học máy, bài toán $$\min_{\|x\| \le t} f(x)$$ (dạng ràng buộc dùng cho Frank–Wolfe) và $$\min_x f(x) + \lambda \|x\|$$ (dạng phạt Lagrange dùng cho Proximal Gradient) sinh ra cùng một họ nghiệm tối ưu khi tham số $$t$$ và $$\lambda$$ biến thiên tương ứng.
- **Khoảng cách đối ngẫu (Duality Gap):** Đại lượng $$g(x) = \max_{s \in C} \nabla f(x)^T (x - s)$$ luôn lớn hơn hoặc bằng $$f(x) - f^\star$$ nhờ tính lồi bậc nhất của $$f$$. Nó vừa là chứng chỉ dừng chính xác, vừa là đại lượng trung tâm trong chứng minh hội tụ ở bài sau.

### Giải thích: Tính tay Frank–Wolfe trên quả cầu $$\ell_1$$ và kiểm tra khoảng cách đối ngẫu

Xét bài toán cực tiểu hóa $$f(x_1, x_2) = \frac{1}{2}(x_1 - 2)^2 + \frac{1}{2}(x_2 - 0.5)^2$$ trên quả cầu $$\ell_1$$ đơn vị $$C = \{(x_1, x_2) : |x_1| + |x_2| \le 1\}$$, khởi tạo từ $$x^{(0)} = (0, 0)$$.

1. **Tính gradient tại $$x^{(0)} = (0, 0)$$:**
   $$\nabla f(0, 0) = (-2,\; -0.5)$$. Giá trị hàm mục tiêu ban đầu là $$f(0, 0) = \frac{1}{2}(4 + 0.25) = 2.125$$.
2. **Giải LMO trên quả cầu $$\ell_1$$:**
   Ta cần cực tiểu hóa $$-2s_1 - 0.5s_2$$ với $$|s_1| + |s_2| \le 1$$. Quy tắc chuẩn $$\ell_1$$ chỉ ra ngay: tìm tọa độ có trị tuyệt đối gradient lớn nhất (ở đây $$|-2| = 2 > |-0.5|$$, tức tọa độ $$i = 1$$) và gán dấu ngược lại: $$s^{(0)} = (1, 0)$$.
3. **Tính khoảng cách đối ngẫu tại $$x^{(0)}$$:**
   $$g(x^{(0)}) = \nabla f(x^{(0)})^T (x^{(0)} - s^{(0)}) = (-2)(0 - 1) + (-0.5)(0 - 0) = 2$$.
   Điều này đảm bảo ngay lập tức rằng $$f(x^{(0)}) - f^\star \le 2$$, tức $$f^\star \ge 2.125 - 2 = 0.125$$.
4. **Cập nhật bước $$k = 1$$ với $$\gamma_1 = \frac{2}{1 + 1} = 1$$:**
   $$x^{(1)} = (1 - 1)(0, 0) + 1 \cdot (1, 0) = (1, 0)$$, thu được $$f(x^{(1)}) = \frac{1}{2}(1 - 2)^2 + \frac{1}{2}(0 - 0.5)^2 = 0.625$$.
5. **Kiểm tra điều kiện dừng tại $$x^{(1)} = (1, 0)$$:**
   Ta có $$\nabla f(1, 0) = (-1,\; -0.5)$$. Tọa độ có trị tuyệt đối gradient lớn nhất vẫn là $$i = 1$$ ($$|-1| = 1 > |-0.5|$$), nên LMO lại trả về $$s^{(1)} = (1, 0)$$. Khoảng cách đối ngẫu lúc này là:
   $$g(x^{(1)}) = \nabla f(x^{(1)})^T (x^{(1)} - s^{(1)}) = 0.$$
   Vì $$0 \le f(x^{(1)}) - f^\star \le g(x^{(1)}) = 0$$, ta khẳng định chắc chắn $$x^\star = (1, 0)$$ là nghiệm tối ưu toàn cục — đồng thời thấy rõ tính thưa (chỉ có 1 tọa độ khác 0) được bảo toàn tuyệt đối!

## Gradient descent có chiếu (Projected Gradient Descent)

Xét bài toán tối ưu có ràng buộc sau:

>$$ \min_{x} f(x) \qquad \text{ thỏa mãn } x \in C $$

Như đã biết, nếu $$f$$ là hàm lồi, trơn và tập $$C$$ là tập lồi, ta có thể dùng phương pháp **gradient descent có chiếu (projected gradient descent)**. Gọi $$P_{C}$$ là toán tử chiếu lên tập $$C$$; khởi tạo $$x^{(0)}$$ và lặp với $$k = 1, 2, 3, \ldots$$:

>$$x^{(k)} = P_{C} \bigl( x^{(k−1)} − t_k\nabla f(x^{(k−1)}) \bigr)$$

Phương pháp này cũng là một trường hợp đặc biệt của proximal gradient descent, trong đó bước tiếp theo $$x^{(k)}$$ thu được bằng cách chiếu điểm cực tiểu của xấp xỉ bậc hai cục bộ (khai triển Taylor bậc hai) lên tập $$C$$:

>$$x^{(k)} = P_{C} \Bigl( \arg\min_{y} \nabla f(x^{(k−1)})^T(y − x^{(k−1)}) + \frac{1}{2t} \| y − x^{(k−1)} \|^2_2 \Bigr)$$

Xem thêm chi tiết về Projected Gradient Descent tại [9-4]({% multilang_post_url contents/chapter09/20-01-08-09_04_special_cases %}).

## Phương pháp gradient có điều kiện (Frank-Wolfe)

Thay vì cực tiểu hóa xấp xỉ bậc hai rồi thực hiện phép chiếu, ta xét một cách tiếp cận đơn giản hơn: cực tiểu hóa trực tiếp xấp xỉ bậc nhất (hàm tuyến tính) của $$f$$ trên tập ràng buộc $$C$$, sau đó cập nhật điểm mới bằng tổ hợp lồi giữa điểm hiện tại và điểm cực tiểu vừa tìm được.

Cụ thể, chọn điểm khởi tạo $$x^{(0)} \in C$$. Với $$k = 1, 2, 3, \ldots$$:

>$$\begin{array}{rcl}
>s^{(k−1)} & \in & \arg\min_{s \in C} \nabla f(x^{(k−1)})^Ts \\
>x^{(k)} & = & (1 − \gamma_k)x^{(k−1)} + \gamma_ks^{(k−1)}
>\end{array}$$

### [Tham khảo]

>$$f(y) \approx f(x) + \nabla f(x)^T(y-x)$$
>
>$$\arg\min_y \bigl(f(x) + \nabla f(x)^T(y-x)\bigr) \equiv \arg\min_y \nabla f(x)^T y$$

Khác với phương pháp có chiếu, thuật toán này không cần thực hiện phép chiếu mà luôn làm việc trực tiếp trên các điểm thuộc $$C$$. Kích thước bước mặc định thường chọn là $$\gamma_k = \frac{2}{k + 1}$$ với $$k = 1, 2, 3, \ldots$$ Vì $$0 \leq \gamma_k \leq 1$$ và $$C$$ là tập lồi, mọi điểm lặp đều tự động thỏa mãn $$x^{(k)} \in C$$. Bước cập nhật cũng có thể viết dưới dạng:

>$$x^{(k)} = x^{(k−1)} + \gamma_k\bigl( s^{(k−1)} − x^{(k−1)} \bigr)$$

Nghĩa là khi số vòng lặp tăng lên, bước di chuyển về phía điểm cực tiểu tuyến tính nhỏ dần. Trong nhiều bài toán, chẳng hạn tối ưu trên hình cầu $$\ell_1$$, bước giải tuyến tính này đơn giản hơn nhiều so với bước chiếu.

### [Tham khảo]

Một chi tiết lịch sử thú vị là Marguerite Frank và Philip Wolfe từng là nghiên cứu sinh sau tiến sĩ làm việc cùng Albert Tucker. Hai ông bà công bố thuật toán này vào năm 1956. Sau một thời gian dài ít được chú ý, thuật toán Frank-Wolfe đã được quan tâm trở lại rộng rãi trong học máy nhờ các phân tích và mở rộng của Martin Jaggi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/frank_wolfe.png" alt="[Hình 1] Phương pháp gradient có điều kiện (Frank-Wolfe) (Jaggi 2011)[3]">
  <figcaption style="text-align: center;">[Hình 1] Phương pháp gradient có điều kiện (Frank-Wolfe) (Jaggi 2011)[3]</figcaption>
</p>
</figure>

## Ràng buộc chuẩn

Xét trường hợp tập ràng buộc là hình cầu chuẩn $$C = \{x : \| x \| \leq t \}$$ với một chuẩn $$\| \cdot \|$$ bất kỳ. Khi đó:

>$$\begin{align}
>s &\in \arg\min_{\|s\|\leq t} \nabla f(x^{(k−1)})^Ts \\
>&= −t \cdot \arg\max_{\|s\|\leq 1} \nabla f(x^{(k−1)})^Ts \\
>&= −t \cdot \partial \| \nabla f(x^{(k−1)}) \|_{*}
>\end{align}$$

trong đó $$\| \cdot \|_{*}$$ là chuẩn đối ngẫu của $$\| \cdot \|$$. Như vậy, chỉ cần tính được một dưới đạo hàm của chuẩn đối ngẫu là ta thực hiện được bước Frank-Wolfe. Lợi thế chính của Frank-Wolfe trên $$C = \{x : \| x \| \leq t \}$$ là bước này thường đơn giản và ít tốn kém hơn đáng kể so với phép chiếu lên $$C$$ hoặc toán tử proximal của $$\| \cdot \|$$.

## Ví dụ: chính quy hóa $$l_1$$

Xét bài toán **chính quy hóa $$l_1$$**:

>$$\min_x f(x) \qquad \text{ thỏa mãn } \| x \|_1 \leq t$$

Áp dụng công thức trên với chuẩn đối ngẫu là chuẩn $$l_\infty$$, ta có $$s^{(k−1)} \in −t\partial \|\nabla f(x^{(k−1)}) \|_\infty$$. Bước cập nhật Frank-Wolfe trở thành:

>$$\begin{array}{rcl}
>i_{k−1} & \in & \arg\max_{i=1,...,p} |\nabla_i f(x^{(k−1)})| \\
>x^{(k)} & = & (1 − \gamma_k)x^{(k−1)} − \gamma_kt \cdot \text{sign}(\nabla_{i_{k−1}} f(x^{(k−1)})) \cdot e_{i_{k−1}}
>\end{array}$$

Cách cập nhật này có dạng tương đồng với phương pháp hạ tọa độ (coordinate descent, sẽ trình bày chi tiết ở chương sau).

**Lưu ý**: Cả hai phương pháp đều có thể thực hiện trong độ phức tạp $$O(n)$$, nhưng bước cập nhật Frank-Wolfe đơn giản hơn nhiều so với phép chiếu lên hình cầu $$l_1$$.

## Ví dụ: chính quy hóa $$l_p$$

Xét bài toán chính quy hóa $$l_p$$:

>$$\min_{x} f(x) \qquad \text{ thỏa mãn } \| x \|_{p} \leq t$$

Với $$1 \leq p \leq \infty$$ và $$q$$ là số mũ liên hợp của $$p$$ (thỏa mãn $$1/p + 1/q = 1$$), ta có $$s^{(k−1)} \in −t\partial \| \nabla f(x^{(k−1)}) \|_{q}$$. Ta có thể chọn tường minh:

>$$s_i^{(k−1)} = −\alpha \cdot \text{sign}(\nabla f_i(x^{(k−1)})) \cdot \left| \nabla f_i(x^{(k−1)}) \right|^{q-1}, \quad i = 1, \ldots, n$$

trong đó $$\alpha$$ là hằng số chuẩn hóa sao cho $$\| s^{(k−1)} \|_{p} = t$$, sau đó thực hiện bước tổ hợp lồi Frank-Wolfe như bình thường.

**Lưu ý**: Với $$p$$ tổng quát, bước cập nhật Frank-Wolfe đơn giản hơn rất nhiều so với **phép chiếu lên hình cầu $$l_p$$**. Ngoại trừ các trường hợp đặc biệt ($$p = 1, 2, \infty$$), phép chiếu lên hình cầu $$l_p$$ không có công thức dạng đóng mà phải giải một bài toán tối ưu con riêng.

## Ví dụ: chính quy hóa chuẩn vết (trace norm)

Xét bài toán **chính quy hóa chuẩn vết**:

>$$\min_{X} f(X) \qquad \text{ thỏa mãn } \| X \|_{tr} \leq t$$

Chuẩn đối ngẫu của chuẩn vết là chuẩn toán tử $$\|\cdot\|_{op}$$, nên $$S^{(k−1)} \in −t \cdot \partial\| \nabla f(X^{(k−1)}) \|_{op}$$. Ta có thể chọn:

>$$S^{(k−1)} = −t \cdot uv^T$$

trong đó $$u, v$$ là cặp vector kỳ dị trái và phải ứng với giá trị kỳ dị lớn nhất của $$\nabla f(X^{(k−1)})$$, rồi cập nhật Frank-Wolfe như thường lệ.

**Lưu ý**: Vì chỉ cần tìm cặp vector kỳ dị hàng đầu thay vì phân rã SVD đầy đủ, bước Frank-Wolfe đơn giản và hiệu quả hơn nhiều so với **phép chiếu lên hình cầu chuẩn vết**.

## Dạng ràng buộc và dạng Lagrange

Xét lại bài toán dạng ràng buộc:

>$$\min_x f(x) \qquad \text{ thỏa mãn } \| x \| \leq t$$

và bài toán dạng Lagrange tương đương:

>$$\min_x f(x) + \lambda \| x \|$$

khi các tham số điều chỉnh $$t$$ và $$\lambda$$ biến thiên trong $$[0,\infty)$$. Ta có thể so sánh chi phí giữa bước cập nhật Frank-Wolfe và toán tử proximal của chuẩn $$\| \cdot \|$$:

* **Chuẩn $$l_1$$**: Frank-Wolfe chỉ cần quét tìm thành phần có trị tuyệt đối lớn nhất của gradient, còn toán tử proximal dùng co ngưỡng mềm (soft-thresholding). Cả hai đều tốn $$O(n)$$ phép tính.
* **Chuẩn $$l_p$$**: Frank-Wolfe chỉ cần lũy thừa từng thành phần của gradient rồi chuẩn hóa với chi phí $$O(n)$$ phép tính, trong khi toán tử proximal nhìn chung không có công thức đóng.
* **Chuẩn vết**: Frank-Wolfe chỉ cần tìm cặp vector kỳ dị hàng đầu của gradient, còn toán tử proximal phải co ngưỡng mềm toàn bộ các giá trị kỳ dị, đòi hỏi phân rã SVD đầy đủ.

Ngoài ra, nhiều bộ chính quy hóa khác cũng có bước Frank-Wolfe hiệu quả, chẳng hạn các ràng buộc đa diện hay nón đặc biệt, chính quy hóa tổng các chuẩn theo nhóm, chuẩn nguyên tử (atomic norm), v.v.

[Hình 2] so sánh hiệu năng giữa projected gradient và conditional gradient trên bài toán Lasso có ràng buộc ($$n=100, p = 500$$):

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/comparing_projected_and_conditional_gradient.png" alt="[Hình 2] So sánh gradient có chiếu và gradient có điều kiện cho bài lasso có ràng buộc [3]">
  <figcaption style="text-align: center;">[Hình 2] So sánh gradient có chiếu và gradient có điều kiện cho bài lasso có ràng buộc [3]</figcaption>
</p>
</figure>

Quan sát cho thấy Frank-Wolfe có tốc độ hội tụ tương đồng với các phương pháp bậc nhất ở giai đoạn đầu, nhưng thường hội tụ chậm hơn khi cần độ chính xác cao. (Lưu ý rằng thí nghiệm trên dùng kích thước bước cố định; sử dụng tìm kiếm đường thẳng — line search — có thể cải thiện tốc độ hội tụ.)

## Khoảng cách đối ngẫu (Duality gap)

Một ưu điểm tự nhiên của quá trình lặp Frank-Wolfe là nó cung cấp trực tiếp một khoảng cách đối ngẫu, đóng vai trò cận trên cho sai số tối ưu (suboptimality gap):

>$$g(x^{(k-1)}) := \max_{s\in C} \nabla f(x^{(k−1)})^T(x^{(k−1)} − s)$$

Đại lượng này luôn thỏa mãn $$f(x^{(k−1)}) − f^{*} \leq g(x^{(k-1)})$$.

### [Chứng minh]

Theo điều kiện bậc nhất của hàm lồi:

>$$f(s) \geq f(x^{(k−1)}) + \nabla f(x^{(k−1)})^T(s − x^{(k−1)})$$

Lấy cực tiểu cả hai vế theo mọi $$s \in C$$:

>$$f^{*} \geq f(x^{(k−1)}) + \min_{s\in C} \nabla f(x^{(k−1)})^T(s − x^{(k−1)})$$

Chuyển vế, ta thu được cận trên của sai số tối ưu:

>$$f(x^{(k−1)}) - f^{*} \leq \max_{s\in C} \nabla f(x^{(k−1)})^T(x^{(k−1)} − s) = \nabla f(x^{(k−1)})^T(x^{(k−1)} − s^{(k−1)})$$

### [Ghi chú]

Như vậy, cận trên này thu được miễn phí ngay từ bước cập nhật Frank-Wolfe. Để thấy vì sao nó được gọi là "khoảng cách đối ngẫu", hãy viết lại bài toán gốc dưới dạng:

>$$\min_{x} f(x) + I_C(x)$$

với $$I_C$$ là hàm chỉ thị của tập $$C$$. Bài toán đối ngẫu tương ứng là:

>$$\max_u −f^{*}(u) − I^{*}_C(−u)$$

trong đó $$I_C^{*}$$ là hàm tựa (support function) của $$C$$ (hàm liên hợp của hàm chỉ thị chính là hàm tựa).

### [Nhắc lại]

>$$I_C(x) = \begin{cases}
>+\infty & \text{nếu } x \notin C \\
>0 & \text{nếu } x \in C
>\end{cases}$$
>
>$$\begin{align}
>I_C^{*}(s) &= \max_{x} \{\langle s, x \rangle - I_C(x)\} \\
>&= \max_{x \in C} \langle s, x \rangle \\
>&= \text{Hàm tựa của } C \text{ tại } s
>\end{align}$$

Đặt $$x = x^{(k-1)}$$ và $$u = \nabla f(x^{(k-1)})$$, theo [bất đẳng thức Fenchel]({% multilang_post_url contents/chapter13/21-04-05-13_04_Conjugate_function %}) (mục 13-04), khoảng cách đối ngẫu tại cặp $$(x, u)$$ thỏa mãn:

>$$f(x) + f^{*}(u) + I^{*}_C(−u) \geq x^Tu + I^{*}_C(−u)$$

(và dấu bằng xảy ra khi $$u = \nabla f(x)$$, cho đúng đại lượng $$g(x) = \max_{s \in C} \nabla f(x)^T(x - s)$$).

### Frank-Wolfe: tiến về một đỉnh, không cần chiếu (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/frank-wolfe_vi.mp4"></video>
</div>

Ở mỗi vòng lặp, thuật toán chọn điểm cực trị $$s$$ cực tiểu hóa $$\langle \nabla f(x), s\rangle$$ và cập nhật $$x$$ sang $$(1-\gamma_k)x + \gamma_k s$$, nên điểm lặp luôn nằm trong tập $$C$$.

### Tự tay thử: các bước Frank-Wolfe

<div class="opx-explainer" data-opx="fw" data-lang="vi"></div>

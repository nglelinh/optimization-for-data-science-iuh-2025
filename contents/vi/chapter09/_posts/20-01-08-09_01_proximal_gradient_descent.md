---
layout: post
title: '09-01 Phương pháp gradient gần kề'
chapter: '09'
order: 2
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Phương pháp gradient gần kề (Proximal gradient descent)

**Phương pháp gradient gần kề** là một phương pháp tìm điểm tối ưu bằng cách phân tách hàm mục tiêu thành một phần khả vi và một phần không khả vi. Trong phần này, chúng ta sẽ tìm hiểu cách định nghĩa các hàm và tìm điểm tối ưu trong phương pháp gradient gần kề.

## Hàm có thể phân tách
Giả sử hàm mục tiêu $$f$$ có thể được phân tách thành hai hàm $$g$$ và $$h$$.

>$$f(x) = g(x) + h(x)$$

Ở đây, hai hàm $$g$$ và $$h$$ có các tính chất sau:

* $$g$$ là hàm lồi và khả vi. (**dom**$$(g) = \mathbb{R}^n$$)
* $$h$$ là hàm lồi và không khả vi.

Nếu $$f$$ khả vi, bạn có thể tìm vị trí tiếp theo bằng phương pháp gradient descent:

>$$x^+ = x - t \cdot \nabla f(x)$$

**[Ghi chú]** Trong gradient descent, hàm $$f$$ được xấp xỉ gần $$x$$ bằng khai triển Taylor bậc hai, và ma trận Hessian $$\nabla^2 f(x)$$ được thay thế bởi $$\frac{1}{2t} I$$. Điểm cực tiểu của xấp xỉ này được chọn làm vị trí tiếp theo. (Xem Chi tiết trong Chương 6 Gradient descent)

> \begin{align}
x^+ = \underset{z}{\text{argmin}}  \underbrace{ f(x) + \nabla f(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2}_{\tilde{f}_t(z)}
\end{align}

Tuy nhiên, nếu $$f$$ không khả vi, bạn không thể sử dụng gradient descent. Nhưng nếu $$f$$ được cấu thành như $$f = g + h$$, liệu chúng ta có thể xấp xỉ phần khả vi $$g$$ bằng một hàm bậc hai không?

Ý tưởng này dẫn đến **Phương pháp gradient gần kề**. Trong phương pháp này, bạn điều chỉnh đến vị trí tốt nhất gần với vị trí được dự đoán bởi gradient descent cho $$g$$ và cũng làm cho hàm không khả vi $$h$$ nhỏ. Quá trình này có thể được biểu diễn như sau:

>
$$ \begin{align}
x^+ & = \underset{z}{\text{argmin}}   \tilde{g}_t(z) + h(z) \\
& = \underset{z}{\text{argmin}} \ g(x) + \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\
& = \underset{z}{\text{argmin}}  \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + \frac{t}{2} \parallel \nabla g(x) \parallel_2 ^2  + h(z) \\
& = \underset{z}{\text{argmin}}  \frac{1}{2t} \left ( 2t \nabla g(x)^T (z - x) + \parallel z - x \parallel_2 ^2 + t^2 \parallel \nabla g(x) \parallel_2 ^2 \right )  + h(z) \\
& = \underset{z}{\text{argmin}}  \frac{1}{2t} \left ( \parallel z - x \parallel_2 ^2 + 2t \nabla g(x)^T (z - x) + t^2 \parallel \nabla g(x) \parallel_2 ^2 \right ) + h(z) \\
& = \underset{z}{\text{argmin}}   \frac{1}{2t} \parallel z - (x - t \nabla g(x) )\parallel_2 ^2 + h(z) \\
\end{align} $$

Khi chuyển từ dòng thứ 2 sang dòng thứ 3, số hạng $$g(x)$$ được loại bỏ như một số hạng hằng số đối với z, và số hạng $$\frac{t}{2} \parallel \nabla g(x)^T \parallel_2 ^2 $$ được thêm vào. Trong phương trình cuối cùng, số hạng đầu tiên $$\frac{1}{2t} \parallel z - (x - t \nabla g(x) )\parallel_2 ^2$$ là số hạng đưa nó gần hơn với vị trí cập nhật gradient của $$g$$, và số hạng thứ hai $$h(z)$$ là số hạng làm giảm $$h$$.

## Phương pháp gradient gần kề
Phương pháp gradient gần kề bắt đầu từ một điểm ban đầu $$x^{(0)}$$ và lặp lại việc áp dụng cập nhật sau:

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) )$$, $$k=1,2,3,...$$

Ở đây, $$\text{prox}_{t}$$ được định nghĩa là ánh xạ gần kề (proximal mapping):

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\arg \min}  \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

Nếu chúng ta viết lại điều này dưới dạng cập nhật mà chúng ta đã thấy cho đến nay, nó trở thành:

> \begin{align}
x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{trong đó} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\
\end{align}

## Điều này có lợi ích gì?
Lợi ích của việc làm này là gì? Có phải chỉ là thay đổi bài toán thành một dạng bài toán tối ưu khác không?

Điểm quan trọng là đối với hầu hết các hàm $$h$$ chính, $$\text{prox}_{t}(\cdot)$$ có thể được tính toán một cách giải tích. Nói cách khác, nó có thể được tính toán như sau:

* Hàm ánh xạ $$\text{prox}_{t}(\cdot)$$ chỉ phụ thuộc vào $$h$$, không phụ thuộc vào $$g$$.
* Hàm $$g$$ có thể rất phức tạp, nhưng ở đây chúng ta chỉ cần tính gradient $$\nabla g$$.

Phân tích hội tụ sẽ được thực hiện liên quan đến số lần lặp của thuật toán. Lưu ý rằng trong mỗi lần lặp, việc tính toán $$\text{prox}_{t}(\cdot)$$ có thể khác nhau về chi phí tính toán tùy thuộc vào $$h$$.

## Ví dụ: ISTA
Hãy xem một ví dụ về phương pháp gradient gần kề. Trong chương trước, tiêu chí lasso được định nghĩa như sau khi $$y \in \mathbb{R}^n$$ và $$X \in \mathbb{R}^{n \times p}$$:

> \begin{align}
f(\beta) = \frac{1}{2} \parallel y - X\beta \parallel_2^2 + \lambda \parallel \beta \parallel_1 \\
\end{align}

Ở đây, $$g(\beta) = \frac{1}{2} \parallel y - X\beta \parallel_2^2$$ và $$h(\beta) = \lambda \parallel \beta \parallel_1$$. Trong trường hợp này, ánh xạ gần kề được định nghĩa là:

>
$$ \begin{align}
\text{prox}_{t}(\beta) & = \underset{z}{\text{argmin}}  \frac{1}{2t} \parallel \beta - z \parallel_2^2 + \lambda \parallel z \parallel_1 \\
& = S_{\lambda t}(\beta) \\
\end{align} $$

$$S_{\lambda t}(\beta)$$ là toán tử ngưỡng mềm (soft-thresholding operator), được định nghĩa như sau. (Để biết thêm chi tiết, xem Chương 7 Subgradient)

> $$ \begin{align}
[S_{\lambda t}(\beta)]_i =
\begin{cases}
\beta_i - \lambda & \mbox{nếu } \beta_i \gt \lambda \\
0 & \mbox{nếu } -\lambda \le \beta_i \le \lambda, i = 1, ..., n \\
\beta_i + \lambda & \mbox{nếu } \beta_i \lt -\lambda \\
\end{cases}
\\
\end{align} $$

Vì gradient của $$g$$ là $$\nabla g(\beta) = -X^{T} (y - X \beta)$$, cập nhật gradient gần kề được định nghĩa là:

>$$\beta^+ = S_{\lambda t}(\beta + tX^{T} (y - X \beta) )$$

Thuật toán này là một thuật toán rất đơn giản được gọi là **thuật toán ngưỡng mềm lặp (iterative soft-thresholding algorithm - ISTA)**. (Beck và Teboulle (2008), "A fast iterative shrinkage-thresholding algorithm for linear inverse problems")

Trong hình dưới đây, bạn có thể thấy rõ sự khác biệt về hiệu suất giữa phương pháp subgradient và phương pháp gradient gần kề. Về mặt số lần lặp, hiệu suất của phương pháp gradient gần kề có thể so sánh với gradient descent.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/09.01_01_ISTA.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 1] Ví dụ về tốc độ hội tụ của gradient gần kề (ISTA) so với phương pháp subgradient [3]</figcaption>
</p>
</figure>

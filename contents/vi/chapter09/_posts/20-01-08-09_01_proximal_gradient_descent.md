---
layout: post
title: '09-01 Phương pháp gradient gần kề (Proximal gradient descent)'
chapter: '09'
order: 2
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

**Phương pháp gradient gần kề (proximal gradient descent)** là phương pháp tối ưu dựa trên việc phân tách hàm mục tiêu thành một phần khả vi và một phần không khả vi. Trong bài này, chúng ta trình bày cách xây dựng thuật toán và áp dụng nó cho bài toán Lasso.

## Hàm mục tiêu có thể phân tách
Giả sử hàm mục tiêu $$f$$ có thể viết dưới dạng tổng của hai hàm $$g$$ và $$h$$:

>$$f(x) = g(x) + h(x)$$

trong đó:

* $$g$$ là hàm lồi và khả vi, với **dom**$$(g) = \mathbb{R}^n$$.
* $$h$$ là hàm lồi và có thể không khả vi.

Nếu $$f$$ khả vi, ta có thể cập nhật điểm lặp bằng phương pháp gradient descent:

>$$x^+ = x - t \cdot \nabla f(x)$$

**[Ghi chú]** Trong gradient descent, hàm $$f$$ được xấp xỉ quanh $$x$$ bằng khai triển Taylor bậc hai với ma trận Hessian $$\nabla^2 f(x)$$ được thay thế bằng $$\frac{1}{t} I$$. Điểm cực tiểu của hàm xấp xỉ bậc hai này chính là điểm lặp tiếp theo (xem chi tiết tại Chương 6 về Gradient descent):

> \begin{align}
x^+ = \underset{z}{\text{argmin}}  \underbrace{ f(x) + \nabla f(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2}_{\tilde{f}_t(z)}
\end{align}

Khi $$f$$ không khả vi, ta không thể áp dụng trực tiếp gradient descent. Tuy nhiên, với cấu trúc $$f = g + h$$, ta có thể xấp xỉ bậc hai riêng cho phần khả vi $$g$$ và giữ nguyên phần không khả vi $$h$$.

Ý tưởng này dẫn đến **phương pháp gradient gần kề**: ở mỗi bước, ta tìm điểm mới vừa gần vị trí cập nhật gradient của $$g$$, vừa làm nhỏ giá trị của $$h$$:

>
$$ \begin{align}
x^+ & = \underset{z}{\text{argmin}}   \tilde{g}_t(z) + h(z) \\
& = \underset{z}{\text{argmin}} \ g(x) + \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\
& = \underset{z}{\text{argmin}}  \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + \frac{t}{2} \parallel \nabla g(x) \parallel_2 ^2  + h(z) \\
& = \underset{z}{\text{argmin}}  \frac{1}{2t} \left ( 2t \nabla g(x)^T (z - x) + \parallel z - x \parallel_2 ^2 + t^2 \parallel \nabla g(x) \parallel_2 ^2 \right )  + h(z) \\
& = \underset{z}{\text{argmin}}  \frac{1}{2t} \left ( \parallel z - x \parallel_2 ^2 + 2t \nabla g(x)^T (z - x) + t^2 \parallel \nabla g(x) \parallel_2 ^2 \right ) + h(z) \\
& = \underset{z}{\text{argmin}}   \frac{1}{2t} \parallel z - (x - t \nabla g(x) )\parallel_2 ^2 + h(z) \\
\end{align} $$

Từ dòng thứ hai sang dòng thứ ba, ta bỏ hằng số $$g(x)$$ (không phụ thuộc vào $$z$$) và cộng thêm hằng số $$\frac{t}{2} \parallel \nabla g(x) \parallel_2 ^2$$ để hoàn thiện bình phương. Ở biểu thức cuối cùng, số hạng $$\frac{1}{2t} \parallel z - (x - t \nabla g(x) )\parallel_2 ^2$$ kéo $$z$$ lại gần điểm cập nhật gradient của $$g$$, còn số hạng $$h(z)$$ thúc đẩy việc giảm giá trị của $$h$$.

## Thuật toán gradient gần kề
Xuất phát từ điểm ban đầu $$x^{(0)}$$, phương pháp gradient gần kề lặp lại bước cập nhật:

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) )$$, $$k=1,2,3,...$$

trong đó $$\text{prox}_{t}$$ là **ánh xạ gần kề (proximal mapping)** của $$h$$:

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\arg \min}  \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

Ta cũng có thể viết bước cập nhật dưới dạng tương tự gradient descent bằng cách định nghĩa ánh xạ gradient tổng quát $$G_t(x)$$:

> \begin{align}
x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{trong đó} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\
\end{align}

## Ưu điểm của cách tiếp cận này
Thoạt nhìn, bước cập nhật trên dường như chỉ chuyển bài toán ban đầu sang một bài toán tối ưu con khác. Tuy nhiên, giá trị thực tiễn của phương pháp nằm ở hai điểm:

* Với nhiều hàm $$h$$ phổ biến trong thực tế, ánh xạ $$\text{prox}_{t}(\cdot)$$ có thể tính được trực tiếp bằng công thức dạng đóng.
* Ánh xạ $$\text{prox}_{t}(\cdot)$$ chỉ phụ thuộc vào $$h$$, không phụ thuộc vào $$g$$; ngay cả khi $$g$$ phức tạp, ta chỉ cần tính được gradient $$\nabla g$$.

Các kết quả phân tích hội tụ tiếp theo được tính theo số bước lặp của thuật toán. Cần lưu ý rằng chi phí tính toán trên mỗi bước lặp còn phụ thuộc vào độ phức tạp khi tính $$\text{prox}_{t}(\cdot)$$ đối với từng hàm $$h$$ cụ thể.

## Ví dụ: ISTA
Xét lại bài toán Lasso với $$y \in \mathbb{R}^n$$ và $$X \in \mathbb{R}^{n \times p}$$:

> \begin{align}
f(\beta) = \frac{1}{2} \parallel y - X\beta \parallel_2^2 + \lambda \parallel \beta \parallel_1 \\
\end{align}

Tách hàm mục tiêu thành $$g(\beta) = \frac{1}{2} \parallel y - X\beta \parallel_2^2$$ và $$h(\beta) = \lambda \parallel \beta \parallel_1$$. Khi đó, ánh xạ gần kề của $$h$$ là:

>
$$ \begin{align}
\text{prox}_{t}(\beta) & = \underset{z}{\text{argmin}}  \frac{1}{2t} \parallel \beta - z \parallel_2^2 + \lambda \parallel z \parallel_1 \\
& = S_{\lambda t}(\beta) \\
\end{align} $$

trong đó $$S_{\lambda t}(\beta)$$ là toán tử ngưỡng mềm (soft-thresholding operator) với ngưỡng $$\lambda t$$ (xem chi tiết tại Chương 7):

> $$ \begin{align}
[S_{\lambda t}(\beta)]_i =
\begin{cases}
\beta_i - \lambda t & \mbox{nếu } \beta_i \gt \lambda t \\
0 & \mbox{nếu } -\lambda t \le \beta_i \le \lambda t, \quad i = 1, ..., p \\
\beta_i + \lambda t & \mbox{nếu } \beta_i \lt -\lambda t \\
\end{cases}
\\
\end{align} $$

Vì $$\nabla g(\beta) = -X^{T} (y - X \beta)$$, bước cập nhật gradient gần kề trở thành:

>$$\beta^+ = S_{\lambda t}(\beta + tX^{T} (y - X \beta) )$$

Thuật toán này được gọi là **thuật toán ngưỡng mềm lặp (Iterative Soft-Thresholding Algorithm — ISTA)** (Beck và Teboulle (2008), "A fast iterative shrinkage-thresholding algorithm for linear inverse problems").

Hình dưới đây minh họa sự khác biệt rõ rệt về tốc độ hội tụ giữa phương pháp subgradient và phương pháp gradient gần kề: xét theo số bước lặp, hiệu suất của phương pháp gradient gần kề tương đương với gradient descent.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/09.01_01_ISTA.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 1] Ví dụ về tốc độ hội tụ của gradient gần kề (ISTA) so với phương pháp subgradient [3]</figcaption>
</p>
</figure>

### Co ngưỡng mềm trong 15 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/prox-shrink_vi.mp4"></video>
</div>

Ánh xạ gần kề của $$\lambda\|x\|_1$$ đưa các thành phần nhỏ về đúng 0 và co các thành phần còn lại một đoạn $$\lambda$$: $$\operatorname{sign}(y)\max(|y|-\lambda,0)$$.

### Tự tay thử: ISTA trên một bài toán Lasso nhỏ

<div class="opx-explainer" data-opx="ista" data-lang="vi"></div>

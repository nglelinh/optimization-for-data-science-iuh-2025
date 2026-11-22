---
layout: post
title: 06-02-02 Tìm kiếm đường lùi
chapter: '06'
order: 7
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Quy tắc cập nhật cơ bản của gradient descent là:
$$x_{k+1} = x_k - t_k \nabla f(x_k),$$
trong đó $$x_k$$ là vector tham số tại lần lặp $$k$$, $$\nabla f(x_k)$$ là gradient và $$t_k > 0$$ là kích thước bước (tốc độ học).

Nếu sử dụng kích thước bước cố định, mức cập nhật không thích nghi với sự thay đổi độ cong của hàm số, dễ dẫn đến vượt quá cực tiểu hoặc tiến triển chậm ở các vùng điều kiện xấu. Để khắc phục, ta có thể chọn kích thước bước một cách thích ứng tại từng bước lặp. Một phương pháp phổ biến là **tìm kiếm đường lùi (backtracking line search)**.

### Tìm kiếm Đường lùi là gì?

Phương pháp này thử một kích thước bước từ vị trí hiện tại; nếu bước thử quá lớn (không làm hàm mục tiêu giảm đủ mức yêu cầu), thuật toán sẽ thu nhỏ kích thước bước lại. Hình dưới đây minh họa cách tìm kiếm đường lùi xác định kích thước bước.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Backtracking_Line_Search.png" alt="backtrackinglinesearch1" width="100%" height="100%">
  <figcaption style="text-align: center;">[Hình 1] Tìm kiếm đường lùi [3]</figcaption>
</p>
</figure>

Các phương pháp tìm kiếm đường (line search) chọn $$t_k$$ nhằm đảm bảo mức giảm đủ lớn của $$f$$ dọc theo hướng giảm $$d_k = -\nabla f(x_k)$$. Tìm kiếm đường chính xác giải bài toán $$t_k = \arg\min_{t > 0} f(x_k + t d_k)$$, nhưng việc này tốn kém về tính toán đối với các hàm $$f$$ không phải bậc hai. Tìm kiếm đường không chính xác (inexact line search) khắc phục bằng cách chỉ đòi hỏi mức giảm vừa đủ; trong đó, tìm kiếm đường lùi được dùng rộng rãi nhờ tính đơn giản và đảm bảo lý thuyết tốt.

Trên hàm lồi $$f$$, xét mặt cắt dọc theo hướng giảm $$\Delta x$$. Đường tiếp tuyến phía dưới luôn nằm dưới đồ thị hàm lồi nên không thể dùng làm ngưỡng kiểm tra bước nhảy. Do đó, tìm kiếm đường lùi sử dụng một đường thẳng phía trên có độ dốc thoải hơn (nhân thêm hệ số $$\alpha \in (0, 1/2]$$). Nếu $$f(x + t \Delta x)$$ nằm phía trên đường thẳng này thì bước $$t$$ quá lớn; ngược lại, nếu nằm phía dưới thì bước $$t$$ được chấp nhận.

Khi bước thử quá lớn, $$t$$ được nhân liên tiếp với $$\beta \in (0, 1)$$ cho đến khi giá trị hàm rơi xuống dưới đường thẳng kiểm tra. Giá trị $$t$$ cuối cùng luôn nằm trong khoảng $$0 < t \le t_0$$.

### Thuật toán Tìm kiếm Đường lùi

Với hướng giảm $$\Delta x = - \nabla f(x)$$, thuật toán được tóm tắt như sau:

1. Khởi tạo các tham số $$0 < \beta < 1$$ và $$0 < \alpha \le 1/2$$.
2. Tại mỗi lần lặp, đặt $$t = t_{\text{init}}$$ (thường chọn $$t_{\text{init}} = 1$$).
3. Trong khi $$f(x - t \nabla f(x)) > f(x) - \alpha t \|\nabla f(x)\|_2^2$$, cập nhật $$t = \beta t$$.
4. Cập nhật $$x^+ = x - t \nabla f(x)$$.
5. Nếu tiêu chuẩn dừng chưa được thỏa mãn, quay lại bước 2.

Tìm kiếm đường lùi đơn giản và hiệu quả trong thực tế. Tham số $$\alpha$$ kiểm soát độ dốc của đường thẳng điều kiện giảm đủ, còn $$\beta$$ xác định mức độ thu nhỏ bước ở mỗi lần lùi. Thông thường, người ta chọn $$\alpha = 1/2$$ và $$\beta$$ gần với 1.

### Ví dụ về Tìm kiếm Đường lùi

Nhờ kích thước bước thích ứng, số bước cập nhật chính giảm đáng kể so với kích thước bước cố định (ví dụ: 12 bước cập nhật so với 100 bước trên cùng bài toán). Kể cả khi tính thêm các bước thử lùi, tổng số lần đánh giá hàm để hội tụ vào khoảng 40 bước.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Convergence.png" alt="backtrackinglinesearch1" width="70%" height="70%">
  <figcaption style="text-align: center;">[Hình 2] Hội tụ với tìm kiếm đường lùi [3]</figcaption>
</p>
</figure>

### Trực giác của Điều kiện Giảm đủ

Xét xấp xỉ bậc hai của $$f$$ quanh $$x$$:
> $$f(y) \approx f(x) + \nabla f(x)^T(y-x) + \frac{1}{2t} \|y - x\|_2^2$$

Thay $$y = x - t \nabla f(x)$$ vào vế phải, ta được:
> $$
> \begin{align}
> f(x - t \nabla f(x)) &\approx f(x) - t \|\nabla f(x)\|_2^2 + \frac{1}{2}t \|\nabla f(x)\|_2^2 = f(x) - \frac{t}{2} \|\nabla f(x)\|_2^2
> \end{align}
> $$
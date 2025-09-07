---
layout: post
title: 06-02-02 Tìm kiếm đường lùi
chapter: '06'
order: 5
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Quy tắc cập nhật cơ bản là:
$$x_{k+1} = x_k - t_k \nabla f(x_k),$$
trong đó $$ x_k $$ là vector tham số tại lần lặp $$ k $$, $$\nabla f(x_k) $$ là gradient, và $$ t_k > 0 $$ là kích thước bước (tốc độ học).

Nếu sử dụng kích thước bước cố định trong gradient descent, tốc độ hội tụ luôn giống nhau, điều này có thể gây vấn đề trong các vùng điều kiện xấu (nơi cực tiểu bị bỏ lỡ hoặc tiến độ chậm). Để giải quyết điều này, kích thước bước có thể được chọn một cách thích ứng để phù hợp với độ cong của hàm. Một phương pháp như vậy là **tìm kiếm đường lùi**.

### Tìm kiếm Đường lùi là gì?
Phương pháp này thử một bước từ vị trí hiện tại, và nếu bước quá lớn, nó sẽ lùi lại. Hình dưới đây cho thấy cách tìm kiếm đường lùi xác định kích thước bước.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Backtracking_Line_Search.png" alt="backtrackinglinesearch1" width="100%" height="100%">
  <figcaption style="text-align: center;">[Hình1] Tìm kiếm Đường lùi [3]</figcaption>
</p>
</figure>

Các phương pháp tìm kiếm đường động chọn $$ t_k $$ để đảm bảo tiến độ đủ, thường bằng cách giảm thiểu $$ f $$ dọc theo hướng tìm kiếm $$ d_k = -\nabla f(x_k) $$ (gradient âm cho giảm).
Tìm kiếm đường chính xác tìm $$ t_k = \arg\min_{t > 0} f(x_k + t d_k) $$, nhưng điều này tốn kém về tính toán cho $$ f $$ không phải bậc hai. Tìm kiếm đường không chính xác xấp xỉ điều này một cách hiệu quả, và tìm kiếm đường lùi là một phương pháp không chính xác phổ biến do tính đơn giản và đảm bảo của nó.

Trong hàm lồi $$f$$, vùng tìm kiếm bị giới hạn trong một đường thẳng. Đường thẳng dưới là một bước từ vị trí hiện tại $$x$$ theo hướng giảm. Nếu $$f$$ luôn ở trên đường thẳng, rất khó để đánh giá liệu bước có quá lớn hay phù hợp. Trong tìm kiếm đường lùi, đường thẳng trên được sử dụng, đây là một bước theo hướng giảm được tỉ lệ bởi $$t$$. Nếu $$f(x + t \Delta x)$$ ở trên đường thẳng, bước quá lớn; nếu ở dưới, bước phù hợp.

Nếu bước quá lớn, $$t$$ được giảm cho đến khi $$f$$ rơi xuống dưới đường thẳng. $$t$$ cuối cùng nằm trong khoảng $$0 \le t \le t_0$$.

### Thuật toán Tìm kiếm Đường lùi

Tóm tắt như sau (với $$\Delta x = - \nabla f(x)$$):

1. Khởi tạo tham số ($$0 < \beta < 1$$, $$0 < t \le 1/2$$).
2. Đối với mỗi lần lặp, đặt $$t = t_{init}$$ ($$t_{init} = 1$$).
3. Trong khi $$f(x - t \nabla f(x)) > f(x) - t \|\nabla f(x)\|_2^2$$, đặt $$t = \beta t$$.
4. Cập nhật $$x^+ = x - t \nabla f(x)$$.
5. Nếu tiêu chuẩn dừng chưa được đáp ứng, lặp lại từ bước 2.

Tìm kiếm đường lùi đơn giản và hiệu quả. Tham số $$t$$ xác định hướng, và $$\beta$$ xác định mức độ lùi lại. Thường $$t = 1/2$$ và $$\beta$$ được chọn gần 1.

### Ví dụ Tìm kiếm Đường lùi
Với kích thước bước thích ứng, sự hội tụ nhanh hơn nhiều so với kích thước bước cố định (ví dụ: 12 bước so với 100 bước cho cùng một bài toán). Bao gồm các bước lùi, tổng sự hội tụ đạt được trong khoảng 40 bước.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Convergence.png" alt="backtrackinglinesearch1" width="70%" height="70%">
  <figcaption style="text-align: center;">[Hình2] Hội tụ [3]</figcaption>
</p>
</figure>

### Trực giác về Tìm kiếm Đường lùi
Một xấp xỉ bậc hai cho $$f$$ là:
> $$f(y) \approx f(x) + \nabla f(x)^T(y-x) + \frac{1}{2t} \|y - x\|_2^2$$

Đối với $$y = x - t \nabla f(x)$$:
> $$
> \begin{align}
> f(x - t \nabla f(x)) &\approx f(x) - t \|\nabla f(x)\|_2^2 + \frac{1}{2}t \|\nabla f(x)\|_2^2
> \end{align}
>$$
---
layout: post
title: 03-01-03 Các tính chất chính của hàm lồi
chapter: '03'
order: 5
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---
## Đặc trưng epigraph
Như đã thảo luận trong Mục 1.2, $$f$$ lồi khi và chỉ khi epigraph của nó là một tập lồi, và ngược lại.

> $$f$$ lồi $$\iff epi(f) = \{(x,t) \in \mathbb{R}^{n+1} \mid x \in \text{dom} f, f(x) \le t \}$$ là một tập lồi

## Tập mức dưới lồi
Nếu một hàm $$f$$ lồi, các tập mức dưới của nó cũng lồi.

> $$\{x \in \text{dom } f: f(x) \leq t\}$$, với mọi $$t \in \mathbb{R}$$

### [Lưu ý] Tập mức dưới
Với một hàm $$f:\mathbb{R}^n \mapsto \mathbb{R}$$, $$C_\alpha = \{x \in \text{dom} f | f(x) \leq \alpha\}$$ được gọi là *tập mức dưới $$\alpha$$*.

## Đặc trưng bậc nhất
Nếu một hàm $$f$$ **khả vi**, điều sau đây đúng:
Nếu miền $$\text{dom} f$$ lồi và với mọi $$x, y \in \text{dom} f$$, $$f(y) \geq f(x) +\nabla f(x)^T(y-x)$$, thì $$f$$ lồi, và ngược lại.

> $$f$$ lồi $$\iff \text{dom}f$$ lồi, và $$f(y) \geq f(x) +\nabla f(x)^T(y-x)$$ với mọi $$x,y \in \text{dom} f$$

Hình dưới đây minh họa điều kiện bậc nhất cho một hàm lồi khả vi $$f$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/1st_order_condition.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hàm Lồi [1]</figcaption>
</p>
</figure>

Điều kiện này được gọi là **điều kiện đường tiếp tuyến** (hoặc điều kiện siêu phẳng tiếp tuyến trong không gian nhiều chiều). Nó cơ bản nói rằng một hàm lồi luôn nằm trên hoặc trên tất cả các đường tiếp tuyến (hoặc siêu phẳng) của nó. Bất kể bạn vẽ đường tiếp tuyến ở đâu trên hàm lồi, giá trị thực tế của hàm sẽ không bao giờ xuống dưới đường tiếp tuyến đó.

### Ví dụ

Xem xét hàm lồi đơn giản $$f(x) = x^2$$. Đạo hàm của nó (là gradient trong 1D) là $$f'(x) = 2x$$.

Hãy chọn một điểm tùy ý $$x_0$$. Phương trình của đường tiếp tuyến với $$f(x)$$ tại $$x_0$$ được cho bởi:
$$L(x) = f(x_0) + f'(x_0)(x - x_0)$$

Thế $$f(x_0) = x_0^2$$ và $$f'(x_0) = 2x_0$$:
$$L(x) = x_0^2 + 2x_0(x - x_0)$$

Điều kiện lồi yêu cầu rằng với mọi $$x$$:
$$f(x) \geq L(x)$$
$$x^2 \geq x_0^2 + 2x_0(x - x_0)$$

Hãy rút gọn vế phải:
$$x^2 \geq x_0^2 + 2x_0x - 2x_0^2$$
$$x^2 \geq 2x_0x - x_0^2$$

Bây giờ, chuyển tất cả các số hạng sang một bên:
$$x^2 - 2x_0x + x_0^2 \geq 0$$

Biểu thức này là một bình phương hoàn hảo:
$$(x - x_0)^2 \geq 0$$

Bất đẳng thức này luôn đúng với bất kỳ số thực $$x$$ và $$x_0$$, vì bình phương của bất kỳ số thực nào luôn không âm. Điều này xác nhận rằng $$f(x) = x^2$$ thỏa mãn điều kiện đường tiếp tuyến và thực sự là một hàm lồi.

## Đặc trưng bậc hai
Nếu một hàm $$f$$ khả vi hai lần, nó có tính chất sau:

- Nếu đạo hàm bậc hai $$\nabla^2f(x)$$ là nửa xác định dương với mọi $$x \in \text{dom} f$$ và $$\text{dom} f$$ lồi, thì $$f$$ lồi, và ngược lại.
> $$f$$ lồi $$\iff \nabla^2f(x) \succeq 0$$ với mọi $$x \in \text{dom} f, \text{dom} f$$: lồi

- Nếu đạo hàm bậc hai $$\nabla^2f(x)$$ là xác định dương với mọi $$x \in \text{dom} f$$, thì $$f$$ lồi chặt.
> nếu $$\nabla^2f(x) \succ 0$$ với mọi $$x \in \text{dom} f$$, thì $$f$$ lồi chặt

- Nói cách khác, độ cong luôn không âm.


## Bất đẳng thức Jensen

Gọi $$f$$ là một hàm lồi và $$w_1, ..., w_n$$ là các trọng số dương sao cho $$\sum_{i=1}^{n} w_i = 1$$. Khi đó, bất đẳng thức sau đây đúng:

$$\sum_{i=1}^{n} w_i f(x_i) \geq f \left ( \sum_{i=1}^{n} w_i x_i \right )$$


Nếu một hàm $$f$$ lồi, nó thỏa mãn bất đẳng thức sau:
>$$f(tx_1 + (1 - t)x_2) \le tf(x_1) + (1 - t)f(x_2) \text{ với } 0 \le t \le 1 $$

>*Mở rộng*:<br>
>$$X$$ là một biến ngẫu nhiên được hỗ trợ trên $$\text{dom } f$$, thì $$f(E[X]) \le E[f(X)]$$

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/jensen_inequality.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 2] Bất đẳng thức Jensen [2]</figcaption>
</p>
</figure>

### **Bất đẳng thức Jensen có phải chính xác là định nghĩa của hàm lồi không?** 

Câu trả lời là không—Bất đẳng thức Jensen là một hệ quả và sự tổng quát hóa của định nghĩa tính lồi, chứ không phải là định nghĩa.

- Điều này mở rộng trường hợp hai điểm ($$k=2$$) trong định nghĩa thành bất kỳ số hữu hạn điểm (và có thể được tổng quát hóa thêm thành tích phân cho các đo lường xác suất).
- **Tại sao đây là một sự tổng quát hóa:** Định nghĩa cơ bản là cho hai điểm (tổ hợp lồi nhị phân). Jensen áp dụng nó một cách lặp đi lặp lại cho nhiều điểm hơn. Ví dụ:
  - Với $$k=2$$, Jensen rút gọn chính xác thành định nghĩa.
  - Với $$k=3$$, bạn có thể áp dụng định nghĩa một cách đệ quy: Trước tiên kết hợp hai điểm, sau đó với điểm thứ ba.

---
### Ví dụ ngắn

Hãy sử dụng hàm lồi $$f(x) = x^2$$.
Xem xét hai số: $$x_1 = 1$$ và $$x_2 = 3$$.
Chúng ta muốn so sánh $$f\left(\frac{x_1+x_2}{2}\right)$$ với $$\frac{f(x_1)+f(x_2)}{2}$$.

1.  **Tính hàm của giá trị trung bình:**
    Giá trị trung bình của $$x_1$$ và $$x_2$$ là $$\frac{1+3}{2} = \frac{4}{2} = 2$$.
    Áp dụng hàm: $$f(2) = 2^2 = 4$$.

2.  **Tính giá trị trung bình của các giá trị hàm:**
    $$f(x_1) = f(1) = 1^2 = 1$$.
    $$f(x_2) = f(3) = 3^2 = 9$$.
    Giá trị trung bình của các giá trị hàm này là $$\frac{1+9}{2} = \frac{10}{2} = 5$$.

So sánh hai kết quả: $$4 \le 5$$.
Điều này minh họa bất đẳng thức Jensen: $$f\left(\frac{1+3}{2}\right) \le \frac{f(1)+f(3)}{2}$$.
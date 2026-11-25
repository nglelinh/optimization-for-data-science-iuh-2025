---
layout: post
title: 23-01 Phương Pháp Coordinate Descent
chapter: '23'
order: 2
owner: YoungJae Choung
categories:
- chapter23
lang: vi
---

Một câu hỏi kinh điển thường làm người mới học tối ưu giật mình: *nếu tôi đứng tại một điểm mà bước sang trái cũng lên dốc, bước sang phải cũng lên dốc, bước lên trên hay xuống dưới đều lên dốc — vậy tôi đã ở đáy thung lũng chưa?*

Nếu mặt địa hình trơn láng (khả vi), câu trả lời chắc chắn là **có**. Nhưng chỉ cần mặt địa hình có một vết gấp nhọn chạy chéo góc $$45^\circ$$, bạn hoàn toàn có thể bị **mắc kẹt giữa sườn núi**: mọi bước đi dọc theo trục Bắc–Nam hay Đông–Tây đều leo dốc, trong khi chỉ cần đi chéo Đông–Bắc là thung lũng sâu thẳm mở ra ngay trước mắt! Toàn bộ bài học này xoay quanh việc phân định rạch ròi ranh giới giữa khi nào hạ theo tọa độ thành công và khi nào nó thất bại.

## Bản đồ kiến thức nền: Ba trụ cột lý thuyết của định lý hội tụ Tseng

Ba câu hỏi Q1–Q2–Q3 trong bài chính là ba nấc thang dẫn tới kết quả kinh điển của Paul Tseng (2001):

- **Trường hợp trơn (Smooth Convex Functions):** Khi $$f$$ khả vi trên $$\mathbb{R}^n$$, cực tiểu theo từng trục tọa độ suy ra mọi đạo hàm riêng $$\frac{\partial f}{\partial x_i}(x) = 0$$, đồng nghĩa $$\nabla f(x) = 0$$ — điều kiện đủ cho cực tiểu toàn cục của hàm lồi.
- **Trường hợp không trơn không tách được (Non-Separable Nonsmooth):** Khi xuất hiện một hạng tử không trơn ghép nhiều biến với nhau (như $$|x_1 - x_2|$$ hoặc $$\max(x_1, x_2)$$), dưới vi phân $$\partial f(x)$$ không phân rã thành tích Descartes của các dưới vi phân riêng lẻ; điểm tối ưu theo từng trục có thể không phải cực tiểu toàn cục.
- **Cấu trúc hợp thành tách được (Composite Separable Structure):** Khi hàm mục tiêu có dạng $$f(x) = g(x) + \sum_{i=1}^n h_i(x_i)$$ với $$g$$ lồi khả vi và từng $$h_i$$ lồi (có thể không trơn nhưng chỉ phụ thuộc riêng vào $$x_i$$), mọi góc nhọn đều **song song với các trục tọa độ**. Nhờ đó, định lý Tseng đảm bảo cực tiểu theo từng tọa độ luôn là cực tiểu toàn cục — chiếc chìa khóa mở cửa cho Lasso và hàng loạt mô hình thưa!

### Khung giải thích (nên đọc chậm): Phản ví dụ tính tay — điểm bị "kẹt" trên hàm lồi không tách được

Hãy tự tay kiểm chứng một phản ví dụ cụ thể cho Câu hỏi Q2 để thấy rõ vì sao sự không tách được lại bẫy chết Coordinate Descent. Xét hàm lồi:

$$
f(x_1, x_2) = (x_1 + x_2 - 2)^2 + 5|x_1 - x_2|
$$

tại điểm $$x = (0, 0)$$, nơi giá trị hàm là $$f(0, 0) = (-2)^2 + 0 = 4$$.

1. **Kiểm tra cực tiểu dọc theo trục $$x_1$$ (giữ cố định $$x_2 = 0$$):**
   Hàm một biến là $$\phi_1(x_1) = (x_1 - 2)^2 + 5|x_1|$$.
   - Nếu $$x_1 > 0$$: $$\phi_1'(x_1) = 2(x_1 - 2) + 5 = 2x_1 + 1 > 0$$ (hàm tăng ngặt khi đi sang phải!).
   - Nếu $$x_1 < 0$$: $$\phi_1'(x_1) = 2(x_1 - 2) - 5 = 2x_1 - 9 < 0$$ (hàm tăng ngặt khi đi sang trái!).
   Do đó, $$x_1 = 0$$ là **cực tiểu toàn cục duy nhất** dọc theo trục $$x_1$$.
2. **Kiểm tra cực tiểu dọc theo trục $$x_2$$ (giữ cố định $$x_1 = 0$$):**
   Vì hàm đối xứng theo $$x_1, x_2$$, hàm $$\phi_2(x_2) = (x_2 - 2)^2 + 5|x_2|$$ cũng đạt **cực tiểu toàn cục duy nhất** tại $$x_2 = 0$$.
3. **Thế nhưng $$(0, 0)$$ KHÔNG phải cực tiểu toàn cục:**
   Thử bước chéo dọc đường $$x_1 = x_2$$ tới điểm $$(1, 1)$$:
   $$f(1, 1) = (1 + 1 - 2)^2 + 5|1 - 1| = 0 < 4 = f(0, 0)!$$
4. **Kết luận trực giác:** Vết gấp không trơn của $$5|x_1 - x_2|$$ chạy dọc theo đường chéo $$x_1 = x_2$$ (chéo $$45^\circ$$ so với các trục). Khi Coordinate Descent chỉ được phép đi ngang hoặc đi dọc, nó bị kẹt cứng tại $$(0, 0)$$ dù đáy thung lũng $$f = 0$$ nằm ngay trước mặt! Ngược lại, nếu thay $$5|x_1 - x_2|$$ bằng chuẩn $$\ell_1$$ tách được $$5|x_1| + 5|x_2|$$, mọi vết gấp đều nằm dọc trục tọa độ nên hiện tượng kẹt này không bao giờ xảy ra.

Chương này giới thiệu phương pháp hạ theo tọa độ (coordinate descent) — một thuật toán tối ưu đơn giản, hiệu quả và có khả năng mở rộng tốt. Trước khi đi vào công thức, hãy bắt đầu với ba câu hỏi nền tảng về điều kiện tối ưu theo từng trục tọa độ.

**Q1. Với hàm $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ lồi và khả vi, nếu điểm $$x$$ làm cực tiểu $$f$$ dọc theo từng trục tọa độ, thì $$x$$ có phải là điểm cực tiểu toàn cục không?**

**A1. Có. Khi đó $$\nabla f(x) = 0$$ nên $$x$$ là điểm cực tiểu toàn cục của $$f$$.**

Điều kiện cực tiểu theo từng trục tọa độ nghĩa là $$f(x + \delta e_i) \ge f(x)$$ với mọi $$\delta \in \mathbb{R}$$ và mọi $$i = 1, \dots, n$$, trong đó $$e_i = (0, \dots, 1, \dots, 0) \in \mathbb{R}^n$$ là vector cơ sở chuẩn thứ $$i$$. Vì không thể làm giảm $$f$$ khi dịch chuyển dọc theo bất kỳ trục tọa độ nào từ $$x$$, mọi đạo hàm riêng tại $$x$$ đều bằng 0:

$$
\nabla f(x) = \big( \frac{\partial f}{\partial x_1}(x), \dots, \frac{\partial f}{\partial x_n}(x) \big) = (0, \dots, 0) = 0
$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/smooth_function.png" alt="[Hình 1] Hàm lồi trơn f [3]">
  <figcaption style="text-align: center;">$$[Hình 1] \; Hàm \; lồi \; trơn \; f \; [3]$$ </figcaption>
</p>
</figure>


<br/>

**Q2. Nếu $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ là hàm lồi nhưng *không khả vi*, điểm $$x$$ đạt cực tiểu dọc theo từng trục tọa độ có luôn là cực tiểu toàn cục không?**

**A2. Không. Trong trường hợp này, $$x$$ chưa chắc là điểm cực tiểu toàn cục của $$f$$ (xem phản ví dụ ở Hình 2).** 

Quan sát các đường đồng mức bên phải ở Hình 2: dù điểm đánh dấu không phải cực tiểu toàn cục, giá trị $$f$$ vẫn không thể giảm nếu chỉ đi dọc theo các trục tọa độ (muốn giảm $$f$$, ta phải đi vào phần bên trong của đường đồng mức). Nguyên nhân là tại điểm góc không trơn đó, toàn bộ phần bên trong đường đồng mức nằm kẹp giữa hai đường thẳng song song với các trục tọa độ. Khi $$f$$ khả vi, mỗi điểm trên đường đồng mức chỉ có duy nhất một tiếp tuyến nên hiện tượng kẹt này không xảy ra.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/non-smooth_function.png" alt="[Hình 2] Phản ví dụ: hàm lồi không trơn f [3]">
  <figcaption style="text-align: center;">$$[Hình 2] \; Phản \; ví \; dụ: \; hàm \; lồi \; không \; trơn \; f \; [3]$$ </figcaption>
</p>
</figure>
<br/>

**Q3. Nếu $$f$$ là tổng của một hàm lồi khả vi $$g$$ và một hàm lồi không trơn *tách được theo từng tọa độ*, tức $$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$, thì điểm $$x$$ cực tiểu theo từng trục tọa độ có luôn là cực tiểu toàn cục không?**

**A3. Có. Với mọi $$y \in \mathbb{R}^n$$, ta luôn có:**

$$\begin{align}
f(y) - f(x) &\ge \nabla g(x)^T (y-x) + \sum_{i=1}^{n} \big[ h_i(y_i) - h_i(x_i) \big] \\\\
&= \sum_{i=1}^{n} \big[ \underbrace{\nabla_i g(x) (y_i - x_i) + h_i(y_i) - h_i(x_i)}_{\ge 0} \big] \ge 0
\end{align}$$

<div class="textbook-proof" markdown="1">
**Chứng minh:**
</div>

>Đặt $$F_i(x_i) = g(x_i ; x_{-i}) + h_i(x_i)$$, trong đó $$g(x_i ; x_{-i})$$ coi thành phần thứ $$i$$ là biến số còn tất cả các thành phần khác giữ cố định. Vì $$x_i$$ cực tiểu hóa $$F_i$$:
>
> $$
> \begin{align}
> & \: 0 \in \partial F_i (x_i) \\\\
> \Leftrightarrow & \: 0 \in \{ \nabla_i g(x) \} + \partial h_i(x_i)\\\\
> \Leftrightarrow & \: - \nabla_i g(x) \in \partial h_i(x_i)
> \end{align}
> $$

Theo [định nghĩa của dưới đạo hàm (subgradient)]({% multilang_post_url contents/chapter07/21-03-25-07_01_subgradient %}), ta suy ra với mọi $$y_i$$:

> $$
> \begin{align}
> & h_i(y_i) \ge h_i(x_i) - \nabla_i g(x) (y_i - x_i)\\\\
> \Leftrightarrow & \nabla_i g(x) (y_i - x_i) + h_i(y_i) - h_i(x_i) \ge 0.
> \end{align}
> $$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/separable_non-smooth.png" alt="[Hình 3] Hàm lồi f có các phần không trơn tách được [3]">
  <figcaption style="text-align: center;">$$[Hình 3] \; Hàm \; lồi \; f \; có \; các \; phần \; không \; trơn \; tách \; được \; [3]$$ </figcaption>
</p>
</figure>
<br/>

## Kết luận

Điểm cực tiểu của hàm có dạng $$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$ (với $$g$$ lồi khả vi và các $$h_i$$ lồi) có thể tìm bằng **coordinate descent**. Xuất phát từ một điểm khởi tạo $$x^{(0)}$$, thuật toán lặp lại chu trình cập nhật sau:

>**Coordinate Descent:** <br/>
>$$\:$$ Với $$k = 1,2,3,\dots$$,
>
>$$
>\begin{align}
>x_1^{(k)} &\in \text{arg}\min_{x_1} \: f(x_1, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_2^{(k)} &\in \text{arg}\min_{x_2} \: f(x_1^{(k)}, x_2, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_3^{(k)} &\in \text{arg}\min_{x_3} \: f(x_1^{(k)}, x_2^{(k)}, x_3, \dots, x_n^{(k-1)})\\\\
>& \dots\\\\
>x_n^{(k)} &\in \text{arg}\min_{x_n} \: f(x_1^{(k)}, x_2^{(k)}, x_3^{(k)}, \dots, x_n)
>\end{align}
>$$

### Lưu ý:

* Trong chu trình thứ $$k$$, bước cập nhật các tọa độ $$x_{i+1}^{(k)}, \dots, x_{n}^{(k)}$$ sử dụng ngay giá trị mới $$x_i^{(k)}$$ vừa tính được.
* Thứ tự duyệt các tọa độ trong mỗi chu trình có thể chọn tùy ý (tuần hoàn, ngẫu nhiên hoặc theo quy tắc tham lam).
* Có thể nhóm nhiều tọa độ thành từng khối để cập nhật đồng thời (block coordinate descent).

Phiên bản trên thực hiện cực tiểu hóa chính xác theo từng tọa độ. Ngoài ra, với hàm $$f$$ lồi và khả vi, ta cũng có thể dùng phiên bản cực tiểu hóa không chính xác bằng một bước gradient theo từng tọa độ:

>**Coordinate Descent (cực tiểu hóa không chính xác theo từng tọa độ):** <br/>
>$$\:$$ Với $$k = 1,2,3,\dots$$,
>
>$$
>\begin{align}
>x_1^{(k)} &= x_1^{(k-1)} - t_{k,1} \cdot \nabla_1 f(x_1^{(k-1)}, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_2^{(k)} &= x_2^{(k-1)} - t_{k,2} \cdot \nabla_2 f(x_1^{(k)}, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_3^{(k)} &= x_3^{(k-1)} - t_{k,3} \cdot \nabla_3 f(x_1^{(k)}, x_2^{(k)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>& \dots\\\\
>x_n^{(k)} &= x_n^{(k-1)} - t_{k,n} \cdot \nabla_n f(x_1^{(k)}, x_2^{(k)}, x_3^{(k)}, \dots, x_n^{(k-1)})
>\end{align}
>$$

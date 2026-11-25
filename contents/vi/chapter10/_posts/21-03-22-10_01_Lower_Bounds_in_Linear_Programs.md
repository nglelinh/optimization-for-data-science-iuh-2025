---
layout: post
title: 10-01 Cận dưới trong Chương trình Tuyến tính
chapter: '10'
order: 2
owner: Wontak Ryu
categories:
- chapter10
lang: vi
lesson_type: required
---

Giả sử đồng nghiệp đưa cho bạn một bài toán tối ưu cực tiểu hóa $$\min c^T x$$ và tuyên bố: *"Tôi chạy máy tính cả đêm tìm được nghiệm $$x$$ cho giá trị bằng $$14$$, chắc chắn là tối ưu rồi!"* Làm thế nào bạn có thể **chứng minh chắc nịch** rằng không tồn tại một nghiệm nào khác cho giá trị $$13.99$$ mà không cần phải vét cạn vô số điểm trong không gian nhiều chiều?

Câu trả lời đầy tinh tế của bài học này là: hãy đi tìm một **chứng chỉ cận dưới (lower bound certificate)**! Nếu bạn có thể nhân các bất đẳng thức ràng buộc của bài toán với những hệ số không âm khéo chọn rồi cộng vế theo vế để thu được đúng hàm mục tiêu $$c^T x \ge 14$$, thì bất kỳ ai cũng phải tâm phục khẩu phục rằng $$14$$ là đáy tuyệt đối. Và tuyệt vời hơn nữa: chính bài toán đi tìm bộ hệ số nhân cho cận dưới *lớn nhất có thể* đó chính là **bài toán đối ngẫu của LP**!

## Kiến thức cần nhớ: Ba trực giác từ bài toán tìm cận dưới

- **Tổ hợp tuyến tính bảo toàn dấu bất đẳng thức:** Nếu ta có các ràng buộc $$a_i^T x \ge b_i$$ và nhân từng bất đẳng thức với trọng số **không âm** $$u_i \ge 0$$ rồi cộng lại, chiều bất đẳng thức được bảo toàn hoàn toàn: $$\left(\sum u_i a_i\right)^T x \ge \sum u_i b_i$$. (Còn với ràng buộc đẳng thức $$a_j^T x = b_j$$, trọng số $$v_j$$ có thể mang dấu tùy ý vì đẳng thức nhân số âm vẫn là đẳng thức!)
- **Khớp hệ số hàm mục tiêu:** Khi chọn $$(u, v)$$ sao cho tổ hợp tuyến tính vế trái bằng đúng $$c^T x$$ (hoặc nhỏ hơn $$c^T x$$ nếu $$x \ge 0$$), vế phải $$b^T u$$ lập tức trở thành một cận dưới hợp lệ cho mọi $$x$$ khả thi — tức là $$b^T u \le \min c^T x$$.
- **Tối đa hóa cận dưới $$\implies$$ Bài toán đối ngẫu:** Vì ta muốn chứng chỉ cận dưới mạnh nhất (chặt nhất) có thể, ta cực đại hóa $$b^T u$$ trên tất cả các bộ nhân hợp lệ. Đó chính là cách bài toán đối ngẫu ra đời một cách hoàn toàn tự nhiên, không hề gượng ép!

### Giải thích: Tự tay dựng chứng chỉ cận dưới cho một LP 2 biến

Xét bài toán cực tiểu hóa:
$$\min_{x_1, x_2 \ge 0} \; 3x_1 + 5x_2 \quad \text{s.t.} \quad \begin{cases} x_1 + x_2 \ge 4 & \text{(nhân với } u_1 \ge 0\text{)} \\ x_1 + 3x_2 \ge 6 & \text{(nhân với } u_2 \ge 0\text{)} \end{cases}$$

1. **Thử một nghiệm khả thi để lấy cận trên:** Chọn $$x = (3, 1)$$: kiểm tra $$3+1 = 4 \ge 4$$ và $$3+3 = 6 \ge 6$$ (khả thi!). Giá trị hàm mục tiêu là $$3(3) + 5(1) = 14$$. Vậy ta biết chắc $$p^* \le 14$$.
2. **Dựng cận dưới bằng cách cộng hai ràng buộc:**
   Nhân ràng buộc (1) với $$u_1 \ge 0$$ và ràng buộc (2) với $$u_2 \ge 0$$ rồi cộng vế theo vế:
   $$(u_1 + u_2)x_1 + (u_1 + 3u_2)x_2 \ge 4u_1 + 6u_2.$$
   Để vế trái chặn dưới $$3x_1 + 5x_2$$ với mọi $$x_1, x_2 \ge 0$$, ta chỉ cần:
   $$u_1 + u_2 \le 3 \quad \text{và} \quad u_1 + 3u_2 \le 5.$$
3. **Chọn bộ nhân tối ưu và chốt chứng chỉ:**
   Giải hệ $$u_1 + u_2 = 3, \; u_1 + 3u_2 = 5$$ ta được $$u_1 = 2 \ge 0, \; u_2 = 1 \ge 0$$.
   Thay vào bất đẳng thức:
   $$2(x_1 + x_2) + 1(x_1 + 3x_2) = 3x_1 + 5x_2 \ge 2(4) + 1(6) = 14!$$
   Vì vừa có cận trên $$p^* \le 14$$ (tại $$x = (3, 1)$$), vừa có cận dưới $$p^* \ge 14$$ (chứng chỉ $$u = (2, 1)$$), ta kết luận chắc chắn 100% rằng $$p^* = 14$$!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

## Ví dụ 1: Trường hợp ràng buộc chứa trực tiếp hàm mục tiêu

Giả sử chúng ta muốn tìm một cận dưới $$B$$ cho giá trị tối ưu của một bài toán lồi cho trước:

>$$
>\begin{align}
>B \leq \min_{x} f(x).
>\end{align}
>$$

Hãy xét cụ thể bài toán tìm cận dưới trong quy hoạch tuyến tính (LP), đi từ các trường hợp đơn giản đến dạng tổng quát. Trước hết, xét ví dụ LP đơn giản nhất:

>$$
>\begin{align}
>&\min_{x, y}  
>& &{x+y} \\\\
>&\text{với điều kiện} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

Trong bài toán này, chính ràng buộc đã cung cấp trực tiếp cận dưới cho hàm mục tiêu, nên ta dễ dàng thấy ngay $$B = 2$$.

Tiếp theo, hãy xét trường hợp ràng buộc không cho sẵn cận dưới một cách trực tiếp như vậy.

## Ví dụ 2: Trường hợp hàm mục tiêu là tổ hợp tuyến tính của các ràng buộc (1)

>$$
>\begin{align}
>&\min_{x, y}  
>& & {x+3y} \\\\
>&\text{với điều kiện} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

Nếu $$x,\, y$$ là một nghiệm khả thi, thì khi nhân các bất đẳng thức ràng buộc với những hằng số không âm rồi cộng lại, ta vẫn thu được một bất đẳng thức đúng. Do đó, bằng cách chọn hệ số thích hợp để biểu diễn hàm mục tiêu dưới dạng tổ hợp tuyến tính không âm của các ràng buộc, ta có thể suy ra cận dưới $$B$$:

>$$
>\begin{align}
>& &{x + y \geq 2}\\\\
>&{+} &{0x \geq 0}\\\\
>&{+} &{2y \geq 0}\\\\
>&{=} &{x + 3y \geq 2}\\\\
>
>& &{\text{Cận dưới}\ B = 2.}
>\end{align}
>$$

Tổng quát hóa hơn nữa với các hệ số tùy ý $$p, q$$ trong hàm mục tiêu, ta xét bài toán:

>$$
>\begin{align}
>&\min_{x, y}  
>& &{px+qy} \\\\
>&\text{với điều kiện} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

Tương tự như trên, ta nhân ba ràng buộc lần lượt với các hằng số $$a, b, c$$ rồi cộng lại để khớp với hàm mục tiêu:

>$$
>\begin{align}
>& &{a(x+y) \geq 2a} \\\\
>&{+} &{bx \geq 0} \\\\
>&{+} &{cy \geq 0} \\\\
>&{=} &{(a+b)x+(a+c)y \geq 2a} \\\\
>&&\text{Cận dưới}\ B=2a, \\
>&&\text{với bất kỳ a,b,c thỏa mãn điều kiện dưới đây}\\\\
>& &{a + b = p}\\\\
>& &{a + c = q}\\\\
>& &{a,b,c \geq 0.}\\\\
>\end{align}
>$$

Để $$2a$$ thực sự là một cận dưới, các hệ số $$a, b, c$$ phải không âm (vì nhân bất đẳng thức với số âm sẽ làm đổi chiều dấu), đồng thời hệ số của $$x$$ và $$y$$ sau khi cộng phải trùng với hàm mục tiêu, tức là $$a + b = p$$ và $$a + c = q$$.

Để tìm cận dưới chặt nhất (lớn nhất), ta lập một bài toán tối ưu mới với mục tiêu cực đại hóa $$2a$$, trong đó các điều kiện đảm bảo cận dưới trở thành ràng buộc của bài toán mới:

>$$
>\begin{align}
>&\max_{a, b, c}  
>& &{2a} \\\\
>&\text{với điều kiện} 
>& &{a + b = p}\\\\
>& & &{a + c = q}\\\\
>& & &{a, b, c \geq 0}\\\\
>\end{align}
>$$

Bài toán LP ban đầu được gọi là **LP gốc (primal LP)**, còn bài toán cực đại hóa cận dưới vừa xây dựng được gọi là **LP đối ngẫu (dual LP)**. Lưu ý rằng số biến của bài toán đối ngẫu bằng số ràng buộc của bài toán gốc.

>$$
>\begin{align}
>\text{LP Nguyên thủy}\qquad
>&\qquad \min_{x, y}  &{px+qy} \\\\
>&\qquad \text{với điều kiện} &{x + y \geq 2}\\\\
>&\qquad &{x, y \geq 0}\\\\
>\\\\
>\\\\
>\text{LP Đối ngẫu}\qquad
>&\qquad \max_{a, b, c}  &{2a} \\\\
>&\qquad \text{với điều kiện} &{a + b = p}\\\\
>&\qquad &{a + c = q}\\\\
>&\qquad &{a, b, c \geq 0}\\\\
>\end{align}
>$$

## Ví dụ 3: Trường hợp hàm mục tiêu là tổ hợp tuyến tính của các ràng buộc (2)

Xét ví dụ cuối cùng, trong đó có cả bất đẳng thức ngược chiều ($$\leq$$) và ràng buộc đẳng thức ($$=$$):

>$$
>\begin{align}
>&\min_{x, y}  &{px+qy} \\\\
>&\text{với điều kiện} &{x \geq 0}\\\\
>& &{y \leq 1}\\\\
>& &{3x + y = 2}\\\\
>\\\\
>& &{ax \geq 0}\\\\
>&{+} &{-by \geq -b}\\\\
>&{+} &{3cx + cy = 2c}\\\\
>&{=} &{(a+3c)x+(-b+c)y \geq 2c-b}
>\\\\
>\\\\
>&& \text{Cận dưới}  \ B=2c-b, \\
>&& \text{với bất kỳ a,b,c thỏa mãn điều kiện dưới đây}\\\\
>& &{a + 3c = p}\\\\
>& &{-b + c = q}\\\\
>& &{a,b \geq 0}\\\\
>\end{align}
>$$

Ở đây, vì $$c$$ nhân với hai vế của một phương trình đẳng thức nên $$c$$ có thể nhận bất kỳ giá trị thực nào (không bị ràng buộc dấu).

Từ đó, bài toán LP đối ngẫu được viết như sau:

>$$
>\begin{align}
>&\qquad \max_{a, b, c}  &{2c-b} \\\\
>&\qquad \text{với điều kiện} &{a + 3c = p}\\\\
>&\qquad &{-b + c = q}\\\\
>&\qquad &{a, b \geq 0}\\\\
>\end{align}
>$$

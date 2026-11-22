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

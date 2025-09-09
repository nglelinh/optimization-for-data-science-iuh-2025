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

## Ví dụ 1: Dạng mà ràng buộc chứa hàm mục tiêu

Giả sử chúng ta muốn tìm giá trị cận dưới B của giá trị tối ưu cho một bài toán lồi cho trước.

>$$
>\begin{align}
>B \leq \min_{x} f(x).
>\end{align}
>$$

Hãy xét cụ thể cận dưới của các chương trình tuyến tính. Chúng ta sẽ xem xét các trường hợp từ đơn giản đến dạng tổng quát theo thứ tự.
Đầu tiên, lấy dạng đơn giản nhất của bài toán LP làm ví dụ

>$$
>\begin{align}
>&\min_{x, y}  
>& &{x+y} \\\\
>&\text{với điều kiện} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

Bài toán trên đã bao gồm cận dưới của hàm mục tiêu trong ràng buộc, vì vậy chúng ta có thể dễ dàng thấy rằng $$B=2$$.

Hơn nữa, hãy xem xét trường hợp mà ràng buộc không bao gồm cận dưới.

## Ví dụ 2: Dạng mà hàm mục tiêu có thể được biểu diễn như tổ hợp tuyến tính của các ràng buộc (1)

>$$
>\begin{align}
>&\min_{x, y}  
>& & {x+3y} \\\\
>&\text{với điều kiện} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

Nếu $$x,\, y$$ là khả thi, thì việc nhân ba ràng buộc với các giá trị vô hướng và cộng hoặc trừ chúng vẫn thỏa mãn cả ba ràng buộc. Do đó, đối với bài toán LP như vậy, quá trình nhân các ràng buộc với các giá trị vô hướng và cộng hoặc trừ chúng, tức là biểu diễn hàm mục tiêu như tổ hợp tuyến tính của các ràng buộc, là có thể, và kết quả là chúng ta có thể tìm $$B$$. 

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

Tổng quát hóa hơn nữa bằng cách áp dụng các biến tùy ý để biểu diễn hàm mục tiêu, chúng ta có được như sau:

>$$
>\begin{align}
>&\min_{x, y}  
>& &{px+qy} \\\\
>&\text{với điều kiện} 
>& &{x + y \geq 2}\\\\
>& & &{x, y \geq 0.}\\\\
>\end{align}
>$$

Tương tự như ví dụ thứ hai, bằng cách nhân các ràng buộc với các giá trị vô hướng a, b, c tương ứng, hàm mục tiêu có thể được biểu diễn như tổ hợp tuyến tính của ba ràng buộc này.

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


Để cận dưới thỏa mãn là 2a như trên, vì dấu bất đẳng thức sẽ bị đảo ngược trong quá trình nhân với các giá trị vô hướng và điều này sẽ không thỏa mãn, các điều kiện $$a, b, c$$ phải dương và tổng các giá trị vô hướng phải bằng hàm mục tiêu, tức là các điều kiện $$a+b = p$$ và $$a+c = q$$ phải được thỏa mãn.

Một bài toán tối ưu mới có thể được định nghĩa bằng cách tối đa hóa kết quả cận dưới thu được như trên. Trong trường hợp này, các điều kiện thỏa mãn cận dưới trở thành các ràng buộc trong bài toán này.

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

Bài toán LP ban đầu ở trên được gọi là LP nguyên thủy, và dạng định nghĩa lại bài toán tối ưu bằng cách tối đa hóa cận dưới trong LP nguyên thủy được gọi là LP đối ngẫu. Lưu ý rằng số lượng biến tối ưu trong bài toán đối ngẫu bằng số lượng ràng buộc trong bài toán nguyên thủy.

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

## Ví dụ 3: Dạng mà hàm mục tiêu có thể được biểu diễn như tổ hợp tuyến tính của các ràng buộc (2)

Như một ví dụ cuối cùng, hãy xem xét một dạng mà các dấu bất đẳng thức trong ràng buộc bị đảo ngược và bao gồm các ràng buộc đẳng thức.

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

Ở đây, c là giá trị vô hướng được nhân với cả hai vế của đẳng thức, vì vậy bất kỳ giá trị nào cũng có thể được nhân mà không có hạn chế.

Do đó, LP đối ngẫu có thể được định nghĩa như sau.

>$$
>\begin{align}
>&\qquad \max_{a, b, c}  &{2c-b} \\\\
>&\qquad \text{với điều kiện} &{a + 3c = p}\\\\
>&\qquad &{-b + c = q}\\\\
>&\qquad &{a, b \geq 0}\\\\
>\end{align}
>$$

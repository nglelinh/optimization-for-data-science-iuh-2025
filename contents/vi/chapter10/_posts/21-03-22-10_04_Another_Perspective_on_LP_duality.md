---
layout: post
title: 10-04 Góc nhìn khác về tính đối ngẫu LP
chapter: '10'
order: 5
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
Trong trường hợp tính đối ngẫu được thảo luận trước đó, đối với LP, chúng ta đã nhân các ràng buộc của bài toán nguyên thủy với các biến đối ngẫu, thu được tổ hợp tuyến tính của chúng, và sau đó tổ chức nó để tách ra hàm mục tiêu của bài toán nguyên thủy nhằm có được một cận. Các số hạng còn lại được tách ra (một cái gì đó trong công thức dưới đây) đóng vai trò là cận cho bài toán nguyên thủy. Tức là, chúng trở thành hàm mục tiêu của bài toán đối ngẫu, và các điều kiện được tạo ra trong quá trình phát triển công thức trở thành các ràng buộc của bài toán đối ngẫu.

Viết quá trình một phần này (phần của nội dung trên tách ra hàm mục tiêu nguyên thủy để có được một cận) dưới dạng công thức, nó trông như thế này:

>$$
>\begin{align}
>&\min_{x} &&f(x)\\\\
>&\text{subject to} &&Ax = b\\\\
>& &&Gx \leq h\\\\
>\end{align}
>$$

>$$
>\begin{align}
>& &\text{for any }u,\, v\geq 0,\\\\
>& &u^{T}(Ax-b) = 0\\\\
>&{+} &v^{T}(Gx-h)\leq 0\\\\
>&{=} &u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0\\\\
>&{\approx} &f(x)+\text{something}. \\\\
>\end{align}
>$$

Tuy nhiên, đối với các bài toán tối ưu hóa không phải là chương trình tuyến tính, hầu hết không thể biểu diễn hàm mục tiêu như một tổ hợp tuyến tính của các ràng buộc.

Trong chương này, chúng ta xem xét góc nhìn về tính đối ngẫu có thể áp dụng cho các bài toán phổ biến hơn (tất cả bài toán lồi, hầu hết bài toán không lồi). Chúng ta sẽ tìm tính đối ngẫu của LP bằng phương pháp này được gọi là Lagrangian, và xem xét các thảo luận chi tiết hơn trong Chương 11.

Nhìn vào các phương trình cho đến dạng tổ hợp tuyến tính cho bài toán LP nguyên thủy được mô tả ở trên, chúng ta có thể hiểu mối quan hệ sau:
>$$
>\begin{align}
>c^{T}x\geq c^{T}x+\overbrace{u^{T} \underbrace{(Ax-b)} _ {=0}+\underbrace{v^{T}} _ {\geq 0} \underbrace{(Gx-h)} _ {\leq 0}} ^ {\leq 0} := L(x,u,v).
>\end{align}
>$$

Vế phải của bất đẳng thức có giá trị nhỏ hơn hoặc bằng vế trái theo các điều kiện. Ngoài ra, chúng ta định nghĩa biểu thức này là một hàm $$L(x, u, v)$$ cho x, u, v.
Ở đây, nếu chúng ta gọi tập hợp thỏa mãn các ràng buộc của LP nguyên thủy (tập khả thi nguyên thủy) là C, chúng ta có thể hiểu mối quan hệ sau:

>$$
>\begin{align}
>C =  \{ x: Ax=b, Gx\leq h \},
>\end{align}
>$$
>$$
>\begin{align}
>f^{*}=\min_{x\in C} f(x) \geq \min_{x\in C}L(x,u,v)\geq \min_{x}L(x,u,v):=g(u,v).\\\\
>\end{align}
>$$

Nói cách khác, $$g(u,v)$$ trở thành cận dưới của $$f^{*}$$ cho bất kỳ u hoặc $$v$$ nào thỏa mãn $$v\geq0$$.
Hãy xem xét giá trị cận dưới được xác định bởi $$g(u,v)$$.

>$$
>\begin{align}
g(u,v) = min_{x} c^{T}x+u^{T}(Ax-b) + v^{T}(Gx-h) \\\\
= \min_{x} (c+A^{T}u+G^{T}v)^{T}x - b^{T}u-h^{T}v \\\\
\begin{cases}= -b^{T}u-h^{T}v \qquad &\text{if }\ c = -A^{T}u-G^{T}v \\\\
-\infty \qquad &\text{otherwise}.
\end{cases}
>\end{align}
>$$


Như có thể thấy từ phương trình, khi $$c = -A^{T}u-G^{T}v$$ không được thỏa mãn, nó có giá trị $$-\infty$$ do số hạng $$x$$.
Vì chúng ta muốn tìm cận dưới gần nhất với $$f^{*}$$, chúng ta muốn tìm giá trị làm tối đa hóa $$g(u, v)$$. Đây là $$-b^{T}u-h^{T}v$$, giá trị khi $$c = -A^{T}u-G^{T}v$$ được thỏa mãn, và điều này khớp với LP đối ngẫu mà chúng ta thu được bằng phương pháp đầu tiên.

>$$
>\begin{align}
>f^{*} \geq g(u,v), \qquad \text{provided } v \geq 0\\\\
>\text{find the biggest lowerbound  } g(u,v)\\\\
>\max_{u,v} g(u,v)\\\\
>\text{s.t. }v \geq 0. 
>\end{align}
>$$

Phương pháp này cũng có thể áp dụng cho các loại bài toán tối ưu hóa khác không ở dạng LP.
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

Trong cách tiếp cận ở các bài trước, để xây dựng đối ngẫu của một LP, ta nhân các ràng buộc của bài toán gốc với các biến đối ngẫu, lấy tổ hợp tuyến tính rồi biến đổi để tách riêng hàm mục tiêu gốc nhằm thu được một cận dưới. Phần số hạng còn lại (ký hiệu là $$\text{something}$$ trong biểu thức dưới đây) đóng vai trò là cận dưới của bài toán gốc — tức hàm mục tiêu của bài toán đối ngẫu — còn các điều kiện phát sinh trong quá trình biến đổi trở thành ràng buộc của bài toán đối ngẫu.

Tóm tắt lại quá trình này bằng công thức:

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

Tuy nhiên, với các bài toán tối ưu không phải là quy hoạch tuyến tính, nhìn chung ta không thể biểu diễn hàm mục tiêu dưới dạng tổ hợp tuyến tính của các ràng buộc.

Trong bài này, chúng ta xét một góc nhìn tổng quát hơn về tính đối ngẫu, áp dụng được cho mọi bài toán tối ưu (cả lồi lẫn không lồi): phương pháp **Lagrangian**. Ta sẽ dùng cách tiếp cận này để xây dựng lại đối ngẫu của LP, trước khi nghiên cứu sâu hơn trong Chương 11.

Từ tổ hợp tuyến tính của các ràng buộc trong bài toán LP gốc, với mọi $$x$$ khả thi và mọi $$u$$, $$v \geq 0$$, ta có bất đẳng thức:

>$$
>\begin{align}
>c^{T}x\geq c^{T}x+\overbrace{u^{T} \underbrace{(Ax-b)} _ {=0}+\underbrace{v^{T}} _ {\geq 0} \underbrace{(Gx-h)} _ {\leq 0}} ^ {\leq 0} := L(x,u,v).
>\end{align}
>$$

Do $$Ax - b = 0$$, $$Gx - h \leq 0$$ và $$v \geq 0$$, vế phải luôn nhỏ hơn hoặc bằng vế trái. Ta định nghĩa vế phải là hàm $$L(x, u, v)$$ theo các biến $$x, u, v$$. Gọi $$C$$ là tập khả thi của LP gốc, ta suy ra chuỗi bất đẳng thức:

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

Nói cách khác, với mọi $$u$$ và $$v \geq 0$$, giá trị $$g(u, v)$$ luôn là một cận dưới của giá trị tối ưu gốc $$f^{*}$$. Hãy tính tường minh hàm $$g(u, v)$$ đối với LP:

>$$
>\begin{align}
g(u,v) = min_{x} c^{T}x+u^{T}(Ax-b) + v^{T}(Gx-h) \\\\
= \min_{x} (c+A^{T}u+G^{T}v)^{T}x - b^{T}u-h^{T}v \\\\
\begin{cases}= -b^{T}u-h^{T}v \qquad &\text{if }\ c = -A^{T}u-G^{T}v \\\\
-\infty \qquad &\text{otherwise}.
\end{cases}
>\end{align}
>$$

Từ biểu thức trên, nếu $$c + A^{T}u + G^{T}v \neq 0$$ thì hàm tuyến tính theo $$x$$ không bị chặn dưới, nên giá trị cực tiểu bằng $$-\infty$$. Để tìm cận dưới chặt nhất cho $$f^{*}$$, ta cực đại hóa $$g(u, v)$$ trên miền $$v \geq 0$$. Khi đó, ta buộc phải có $$c = -A^{T}u - G^{T}v$$ và hàm mục tiêu trở thành $$-b^{T}u - h^{T}v$$ — trùng khớp hoàn toàn với bài toán LP đối ngẫu thu được theo cách tiếp cận đầu tiên:

>$$
>\begin{align}
>f^{*} \geq g(u,v), \qquad \text{provided } v \geq 0\\\\
>\text{find the biggest lowerbound  } g(u,v)\\\\
>\max_{u,v} g(u,v)\\\\
>\text{s.t. }v \geq 0. 
>\end{align}
>$$

Ưu điểm của cách tiếp cận này là nó có thể mở rộng trực tiếp cho các bài toán tối ưu tổng quát ngoài LP.
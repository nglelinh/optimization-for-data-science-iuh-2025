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

Ở các bài đầu chương, ta xây dựng bài toán đối ngẫu LP bằng một "mẹo đại số" rất khéo: nhân các ràng buộc với biến đối ngẫu rồi cộng vế theo vế để ghép thành hàm mục tiêu. Mẹo đó chạy rất trơn trên hàm tuyến tính, nhưng hãy thử đặt câu hỏi: *nếu sang Chương 11 hàm mục tiêu là $$x^4 + e^x$$ và ràng buộc là hình cầu $$\|x\|_2^2 \le 1$$ thì cộng tuyến tính sao nổi?*

Bài học này mở ra **góc nhìn thứ hai — góc nhìn hàm Lagrangian** — chiếc cầu vàng nối thẳng Chương 10 sang toàn bộ lý thuyết đối ngẫu phi tuyến ở Chương 11 và điều kiện KKT ở Chương 12! Thay vì coi ràng buộc như bức tường cứng nhắc, ta chuyển chúng thành "khoản phạt mềm" cộng thẳng vào hàm mục tiêu $$L(x, u, v) = c^T x + u^T(Ax - b) + v^T(Gx - h)$$, rồi cực tiểu hóa tự do theo $$x \in \mathbb{R}^n$$. Phép cực tiểu hóa một hàm tuyến tính trên toàn không gian có tính chất cực kỳ sắc bén: nó chỉ hữu hạn khi độ dốc bằng $$0$$ (sinh ra đúng ràng buộc đối ngẫu!), còn ngược lại thì tụt thẳng xuống $$-\infty$$!

## Kiến thức cần nhớ: Ba trụ cột của góc nhìn Lagrangian cho LP

- **Hàm Lagrangian và trò chơi phạt mềm:** Định nghĩa $$L(x, u, v) = c^T x + u^T(Ax - b) + v^T(Gx - h)$$ với $$v \ge 0$$. Với mọi điểm $$x$$ khả thi ($$Ax = b$$ và $$Gx \le h$$), ta luôn có $$u^T(Ax - b) = 0$$ và $$v^T(Gx - h) \le 0$$, nên $$L(x, u, v) \le c^T x$$ — tức $$L$$ luôn là một bản xấp xỉ nằm dưới hàm mục tiêu gốc trên miền khả thi.
- **Nới lỏng miền lấy cực tiểu ($$\min_{x \in C} \ge \min_{x \in \mathbb{R}^n}$$):** Bằng cách bỏ hoàn toàn ràng buộc $$x \in C$$ và lấy cực tiểu hóa tự do $$g(u, v) = \min_{x \in \mathbb{R}^n} L(x, u, v)$$, ta chắc chắn thu được một cận dưới $$g(u, v) \le p^*$$.
- **Điều kiện hữu hạn của infimum tuyến tính (Đọc ra miền khả thi đối ngẫu):** Gom nhóm theo $$x$$:
  $$L(x, u, v) = (c + A^T u + G^T v)^T x - b^T u - h^T v.$$
  Một hàm tuyến tính $$w^T x$$ trên toàn $$\mathbb{R}^n$$ có infimum bằng $$0$$ nếu $$w = 0$$, và bằng $$-\infty$$ nếu $$w \ne 0$$! Chính điều kiện $$w = c + A^T u + G^T v = 0$$ lập tức tạo ra ràng buộc của bài toán đối ngẫu LP!

### Giải thích: Tính tay hàm đối ngẫu $$g(v) = \inf_x L(x, v)$$ cho một LP 1 biến

Xét bài toán cực tiểu hóa 1 biến:
$$\min_{x \in \mathbb{R}} \; 4x \quad \text{s.t.} \quad 2 - x \le 0 \; (\text{tức } x \ge 2).$$
(Hiển nhiên nghiệm gốc là $$x^* = 2$$, $$p^* = 8$$.)

1. **Lập hàm Lagrangian với biến đối ngẫu $$v \ge 0$$:**
   $$L(x, v) = 4x + v(2 - x) = (4 - v)x + 2v.$$
2. **Cực tiểu hóa tự do theo $$x \in \mathbb{R}$$ để tìm hàm đối ngẫu $$g(v)$$:**
   - Nếu $$v \ne 4$$ (ví dụ $$v = 2$$): $$L(x, 2) = 2x + 4$$. Cho $$x \to -\infty$$ thì $$L(x, 2) \to -\infty$$! Vậy $$g(v) = -\infty$$ (cận dưới vô dụng).
   - Nếu $$v = 4$$: hệ số của $$x$$ triệt tiêu sạch ($$4 - 4 = 0$$), nên $$L(x, 4) = 0 \cdot x + 2(4) = 8$$ với mọi $$x \in \mathbb{R}$$! Vậy $$g(4) = 8$$.
   Tóm lại:
   $$g(v) = \begin{cases} 8 & \text{nếu } v = 4, \\ -\infty & \text{nếu } v \ne 4. \end{cases}$$
3. **Cực đại hóa $$g(v)$$ theo $$v \ge 0$$:**
   Ta buộc phải đặt ràng buộc ẩn $$4 - v = 0$$ (để tránh $$-\infty$$) và tối đa hóa $$2v$$, cho nghiệm $$v^* = 4$$ và $$d^* = 8 = p^*$$! Đây chính là cầu nối trực tiếp sang bài toán tổng quát của Chương 11.

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
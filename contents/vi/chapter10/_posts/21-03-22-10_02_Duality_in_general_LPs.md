---
layout: post
title: 10-02 Tính đối ngẫu trong LP tổng quát
chapter: '10'
order: 3
owner: Wontak Ryu
categories:
- chapter10
lang: vi
lesson_type: required
---

Ở bài 10-01, ta đã tìm cận dưới bằng tay cho vài ví dụ hai biến đơn giản. Nhưng khi đối mặt với một bài toán quy hoạch tuyến tính tổng quát ngoài đời thực — có hàng nghìn biến, pha trộn cả ràng buộc đẳng thức $$Ax = b$$ lẫn bất đẳng thức $$Gx \le h$$ — ta cần một "cỗ máy đại số" tổng quát biến mọi bài toán LP dạng ma trận thành bài toán đối ngẫu chỉ trong một bước duy nhất mà không lo nhầm dấu!

Bài học này thiết lập đúng cỗ máy chuẩn mực đó. Chỉ cần nhớ một quy tắc vàng duy nhất về dấu của biến đối ngẫu (ràng buộc đẳng thức $$\leftrightarrow$$ biến đối ngẫu tự do; ràng buộc bất đẳng thức $$\leftrightarrow$$ biến đối ngẫu không âm) và phép chuyển vị ma trận ($$A \to A^T, G \to G^T$$), bạn có thể viết ngay bài toán đối ngẫu cho bất kỳ LP nào dù cồng kềnh đến đâu.

## Bản đồ kiến thức nền: Bốn quy tắc tổng quát hóa đối ngẫu LP

- **Cặp dạng chuẩn tổng quát:**
  - *Primal:* $$\min_x c^T x \;\text{ s.t. }\; Ax = b,\; Gx \le h$$.
  - *Dual:* $$\max_{u, v} -b^T u - h^T v \;\text{ s.t. }\; -A^T u - G^T v = c,\; v \ge 0$$ (với $$u$$ tự do dấu).
- **Quy tắc chuyển đổi trực giác (nhân ràng buộc với biến đối ngẫu):** Cộng $$u^T(Ax - b) = 0$$ và $$v^T(Gx - h) \le 0$$ (với $$v \ge 0$$) vào hàm mục tiêu $$c^T x$$, rồi gom hệ số của $$x$$ thành $$(c + A^T u + G^T v)^T x - b^T u - h^T v$$. Để chặn dưới không phụ thuộc vào $$x \in \mathbb{R}^n$$ tự do, hệ số đứng trước $$x$$ bắt buộc phải bằng $$0$$!
- **Tính đối ngẫu yếu (luôn đúng không điều kiện):** Với mọi $$x$$ khả thi gốc và $$(u, v)$$ khả thi đối ngẫu, ta luôn có $$-b^T u - h^T v \le c^T x$$. Hệ quả tức thì: nếu bài toán gốc không bị chặn dưới ($$p^* = -\infty$$) thì bài toán đối ngẫu chắc chắn **vô nghiệm**!
- **Tính đối ngẫu mạnh trong LP:** Miễn là bài toán gốc khả thi và có giá trị tối ưu hữu hạn, bài toán đối ngẫu cũng có nghiệm tối ưu và $$p^* = d^*$$ (chứng minh nhờ Bổ đề Farkas / Định lý tách siêu phẳng).

### Khung giải thích (nên đọc chậm): Chuyển đổi tay một LP hỗn hợp (có cả `=` và `\le`) sang đối ngẫu

Xét LP 2 biến có cả ràng buộc đẳng thức lẫn bất đẳng thức:
$$\min_{x_1, x_2 \in \mathbb{R}} \; 2x_1 + x_2 \quad \text{s.t.} \quad x_1 + x_2 = 3, \quad -x_1 \le -1 \; (\text{tức } x_1 \ge 1).$$

1. **Nhận diện ma trận chuẩn:**
   $$c = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \quad A = \begin{pmatrix} 1 & 1 \end{pmatrix}, \; b = 3, \quad G = \begin{pmatrix} -1 & 0 \end{pmatrix}, \; h = -1.$$
2. **Viết bài toán đối ngẫu theo công thức ma trận ($$u \in \mathbb{R}, v \ge 0$$):**
   - Hàm mục tiêu đối ngẫu: $$\max -b^T u - h^T v = \max \; -3u + v$$.
   - Ràng buộc $$-A^T u - G^T v = c$$:
     $$\begin{cases} -u + v = 2 \\ -u = 1 \end{cases} \quad \text{với } v \ge 0.$$
3. **Giải tay cả hai bài toán để đối chiếu đối ngẫu mạnh:**
   - *Giải Dual:* Từ $$-u = 1 \implies u^* = -1$$; thay vào $$-(-1) + v = 2 \implies v^* = 1 \ge 0$$. Giá trị đối ngẫu tối ưu: $$d^* = -3(-1) + 1 = 4$$.
   - *Giải Primal:* Vì $$x_2 = 3 - x_1$$, hàm mục tiêu trở thành $$2x_1 + (3 - x_1) = x_1 + 3$$ với ràng buộc $$x_1 \ge 1$$. Nghiệm tối ưu là $$x_1^* = 1, x_2^* = 2$$, giá trị gốc tối ưu $$p^* = 2(1) + 2 = 4 = d^*$$!
   Cả hai khớp nhau tuyệt đối từng dấu trừ!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trong bài [10-01]({% multilang_post_url contents/chapter10/21-03-22-10_01_Lower_Bounds_in_Linear_Programs %}), chúng ta đã tìm hiểu bài toán gốc và bài toán đối ngẫu cho các bài toán LP đơn giản với biến vô hướng. Trong bài này, ta sẽ mở rộng cách xây dựng đối ngẫu cho LP ở dạng tổng quát.

Xét bài toán LP tổng quát với $$c\in\mathbb{R}^{n},\, A\in\mathbb{R}^{m\times n},\, b\in\mathbb{R}^{m},\, G\in\mathbb{R}^{r\times n},\, h\in\mathbb{R}^{r}$$:

>$$
>\begin{align}
>&\min_{x} &&c^{T}x\\\\
>&\text{với điều kiện} &&Ax = b\\\\
>& &&Gx \leq h.\\\\
>\end{align}
>$$

Tương tự như trong bài 10-01, ta đưa vào các biến đối ngẫu $$u \in \mathbb{R}^m$$ và $$v \in \mathbb{R}^r$$ tương ứng với từng nhóm ràng buộc, rồi nhân các ràng buộc với biến đối ngẫu tương ứng và cộng lại:

>$$
>\begin{align}
>& &u^{T}(Ax-b) = 0\\\\
>&{+} &v^{T}(Gx-h)\leq 0\\\\
>&{=} &u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0.\\\\
>\end{align}
>$$

Lưu ý rằng biến đối ngẫu $$u$$ ứng với ràng buộc đẳng thức không bị ràng buộc về dấu, trong khi $$v$$ ứng với ràng buộc bất đẳng thức phải thỏa mãn điều kiện không âm ($$v \geq 0$$). Biến đổi bất đẳng thức cuối để làm xuất hiện hàm mục tiêu của LP gốc, ta thu được cận dưới:

>$$
>\begin{align}
>u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0 \\\\
>\underbrace{(-A^{T}u-G^{T}v)^{T}}_{=c^{T}}x\geq-b^{T}u-h^{T}v \\\\
>\text{Cận dưới là} -b^{T}u-h^{T}v \\\\ 
>\text{với } x \text{ khả thi nguyên thủy, và bất kỳ u, v thỏa mãn,} \\\\
>c = -A^{T}u-G^{T}v \\\\
>v\geq 0. \\\\
>\end{align}
>$$

Như vậy, với mọi cặp $$(u, v)$$ thỏa mãn $$c = -A^{T}u - G^{T}v$$ và $$v \geq 0$$, biểu thức $$-b^{T}u - h^{T}v$$ là một cận dưới của giá trị tối ưu bài toán gốc.

Cực đại hóa cận dưới này, ta thu được bài toán LP đối ngẫu:

>$$
>\begin{align}
>&\max_{u,v} &&-b^{T}u-h^{T}v \\\\
>&\text{với điều kiện} &&c = -A^{T}u-G^{T}v \\\\
>& &&v\geq 0.
>\end{align}
>$$

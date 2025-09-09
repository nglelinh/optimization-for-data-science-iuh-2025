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

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trong [10-01]({% multilang_post_url contents/chapter10/21-03-22-10_01_Lower_Bounds_in_Linear_Programs %}), chúng ta đã xem xét nguyên thủy và đối ngẫu của các bài toán LP với các biến một chiều. Trong 10-02, chúng ta muốn xem xét đối ngẫu cho LP ở dạng tổng quát.

Dạng tổng quát của LP như sau:

Cho $$c\in\mathbb{R}^{n},\, A\in\mathbb{R}^{m\times n},\, b\in\mathbb{R}^{m},\, G\in\mathbb{R}^{r\times n},\, h\in\mathbb{R}^{r}$$,

>$$
>\begin{align}
>&\min_{x} &&c^{T}x\\\\
>&\text{với điều kiện} &&Ax = b\\\\
>& &&Gx \leq h.\\\\
>\end{align}
>$$

Tương tự như ví dụ trong 10-01, chúng ta định nghĩa các biến đối ngẫu $$u, v$$ có số lượng bằng số lượng ràng buộc,
và có thể định nghĩa hàm mục tiêu của bài toán đối ngẫu và các ràng buộc như tổng của các tích của ràng buộc và mỗi biến đối ngẫu.

>$$
>\begin{align}
>& &u^{T}(Ax-b) = 0\\\\
>&{+} &v^{T}(Gx-h)\leq 0\\\\
>&{=} &u^{T}(Ax-b) + v^{T}(Gx-h)\leq 0.\\\\
>\end{align}
>$$

Nhớ rằng biến đối ngẫu $$u$$ cho đẳng thức không có ràng buộc, trong khi $$v$$ là biến đối ngẫu cho bất đẳng thức và do đó có ràng buộc bổ sung là phải dương.
Bằng cách sắp xếp phương trình cuối để biểu diễn hàm mục tiêu của LP nguyên thủy, chúng ta có được LP đối ngẫu.

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

Tức là, khi $$c = -A^{T}u-G^{T}v$$, giá trị tối ưu của nguyên thủy có cận dưới là $$-b^{T}u-h^{T}v$$.

Do đó, LP đối ngẫu có thể được định nghĩa như sau.

>$$
>\begin{align}
>&\max_{u,v} &&-b^{T}u-h^{T}v \\\\
>&\text{với điều kiện} &&c = -A^{T}u-G^{T}v \\\\
>& &&v\geq 0.
>\end{align}
>$$


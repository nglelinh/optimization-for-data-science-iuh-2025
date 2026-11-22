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

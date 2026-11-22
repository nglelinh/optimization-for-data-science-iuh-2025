---
layout: post
title: 12-01 Điều kiện Karush-Kuhn-Tucker
chapter: '12'
order: 2
owner: Wontak Ryu
categories:
- chapter12
lang: vi
lesson_type: required
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Xét bài toán tối ưu hóa tổng quát sau:

>$$
>\begin{align}
>    &\min_{x} &&{f(x)} \\\\
>    &\text{với điều kiện } &&{h_i(x) \le 0, \text{ } i=1,\dots,m} \\\\
>    & &&{l_j(x) = 0, \text{ } j=1,\dots,r}.\\\\
>\end{align}
>$$

**Các điều kiện Karush–Kuhn–Tucker (KKT)** (gọi tắt là **điều kiện KKT**) bao gồm bốn nhóm điều kiện sau [3]:

* $$0 \in \partial \big( f(x) + \sum_{i=1}^{m} \lambda_i h_i(x) + \sum_{j=1}^{r} \nu_j l_j(x) \big)$$ (**Điều kiện dừng**): Khi cố định $$\lambda, \nu$$, dưới vi phân (subdifferential) của hàm Lagrangian theo $$x$$ chứa vector $$0$$.
* $$\lambda_i \cdot h_i(x) = 0 \text{ với mọi } i$$ (**Điều kiện bù yếu**): Với mỗi $$i$$, ít nhất một trong hai đại lượng $$\lambda_i$$ và $$h_i(x)$$ bằng $$0$$.
* $$h_i(x) \le 0, l_j(x) = 0 \text{ với mọi } i, j$$ (**Tính khả thi nguyên thủy**): Điểm $$x$$ thỏa mãn toàn bộ các ràng buộc của bài toán nguyên thủy.
* $$\lambda_i \ge 0 \text{ với mọi } i$$ (**Tính khả thi đối ngẫu**): Các nhân tử tương ứng với ràng buộc bất đẳng thức thỏa mãn điều kiện không âm của bài toán đối ngẫu.

## Điều kiện đủ

Đối với bài toán nguyên thủy lồi, nếu tồn tại bộ $$(x^\star, \lambda^\star, \nu^\star)$$ thỏa mãn các điều kiện KKT, thì biến đổi sau cho thấy $$(x^\star, \lambda^\star, \nu^\star)$$ là cặp nghiệm tối ưu nguyên thủy và đối ngẫu với khoảng cách đối ngẫu bằng không:

>$$
>\begin{align}
>    g(\lambda^\star, \nu^\star) &= \min_x L(x, \lambda^\star, \nu^\star) \\\\
>                                &= L(x^\star, \lambda^\star, \nu^\star) \\\\
>                                &= f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                                &= f(x^\star)
>\end{align}
>$$

1. Hàm $$L(x,\lambda^\star,\nu^\star) = f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x)$$ là hàm lồi theo $$x$$ (vì là tổng các hàm lồi với hệ số không âm đối với $$h_i$$ và các hàm affine $$l_j$$).
2. Vì $$0 \in \partial \big( f(x^\star) + \sum_{i=1}^{m} \lambda_i^\star h_i(x^\star) + \sum_{j=1}^{r} \nu_j^\star l_j(x^\star) \big)$$, nên $$\min_x L(x, \lambda^\star, \nu^\star) = L(x^\star, \lambda^\star, \nu^\star)$$.
3. Nhờ điều kiện bù yếu và tính khả thi nguyên thủy, ta có $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$.

## Điều kiện cần

Ngược lại, nếu $$(x^\star, \lambda^\star, \nu^\star)$$ là nghiệm tối ưu nguyên thủy và đối ngẫu với khoảng cách đối ngẫu bằng không (chẳng hạn khi bài toán thỏa mãn điều kiện Slater), thì mọi bất đẳng thức trong chuỗi dưới đây đều trở thành đẳng thức, suy ra $$(x^\star, \lambda^\star, \nu^\star)$$ thỏa mãn các điều kiện KKT:

>$$
>\begin{align}
>    f(x^\star) &= g(\lambda^\star, \nu^\star) \\\\
>                   &= \min_x  \big( f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x) \big) \\\\
>                   &\le f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                   &\le f(x^\star)
>\end{align}
>$$

1. Đẳng thức $$f(x^\star) = g(\lambda^\star, \nu^\star)$$ thể hiện khoảng cách đối ngẫu bằng không.
2. Để có $$f(x^\star) + \sum_{i=1}^m \underbrace{\lambda_i^\star h_i(x^\star)}_{0} + \sum_{j=1}^r \underbrace{\nu_j^\star l_j(x^\star)}_{0} = f(x^\star)$$, điều kiện bù yếu và tính khả thi nguyên thủy phải được thỏa mãn.
3. Khi đẳng thức này đúng, mọi bất đẳng thức trong chuỗi suy dẫn trên đều là đẳng thức; đặc biệt $$x^\star$$ đạt cực tiểu của $$L(x, \lambda^\star, \nu^\star)$$, dẫn đến điều kiện dừng.

## Tổng kết

Tóm lại, đối với bài toán tối ưu lồi, các điều kiện KKT là:

* Điều kiện đủ cho cặp nghiệm tối ưu nguyên thủy và đối ngẫu có khoảng cách đối ngẫu bằng không.
* Điều kiện cần cho cặp nghiệm tối ưu nguyên thủy và đối ngẫu khi tính đối ngẫu mạnh được thỏa mãn.

Nói cách khác, với các bài toán thỏa mãn tính đối ngẫu mạnh, ta có tương đương sau:

>$$
>\begin{align}
>    x^\star, \lambda^\star, \nu^\star \text{ là nghiệm nguyên thủy và đối ngẫu} \\\\
>    \Leftrightarrow x^\star, \lambda^\star, \nu^\star \text{ thỏa mãn các điều kiện KKT} \\\\
>\end{align}
>$$
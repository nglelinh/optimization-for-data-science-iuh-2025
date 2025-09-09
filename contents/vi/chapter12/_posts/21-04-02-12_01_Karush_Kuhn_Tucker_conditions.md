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

Hãy xem xét bài toán tối ưu hóa tổng quát sau đây.

>$$
>\begin{align}
>    &\min_{x} &&{f(x)} \\\\
>    &\text{với điều kiện } &&{h_i(x) \le 0, \text{ } i=1,\dots,m} \\\\
>    & &&{l_j(x) = 0, \text{ } j=1,\dots,r}.\\\\
>\end{align}
>$$

**Điều kiện Karush–Kuhn–Tucker (KKT)** hoặc **điều kiện KKT** bao gồm các điều kiện sau [3].

* $$0 \in \partial \big( f(x) + \sum_{i=1}^{m} \lambda_i h_i(x) + \sum_{j=1}^{r} \nu_j l_j(x) \big)$$ (Tính dừng): Khi $$\lambda, \nu$$ được cố định, subdifferential theo $$x$$ chứa 0. 
* $$\lambda_i \cdot h_i(x) = 0 \text{ với mọi } i$$ (Bù yếu): Ít nhất một trong $$\lambda_i$$ và $$h_i$$ có giá trị 0.
* $$h_i(x) \le 0, l_j(x) = 0 \text{ với mọi } i, j$$ (Tính khả thi Nguyên thủy): Chỉ ra liệu các ràng buộc của bài toán nguyên thủy có được thỏa mãn hay không.
* $$\lambda_i \ge 0 \text{ với mọi } i$$ (Tính khả thi Đối ngẫu): Chỉ ra liệu các ràng buộc của bài toán đối ngẫu có được thỏa mãn hay không.

## Tính đủ
Đối với một bài toán nguyên thủy lồi, khi tồn tại $$x^\star, \lambda^\star, \nu^\star$$ thỏa mãn các điều kiện KKT, quá trình sau đây chỉ ra rằng $$x^\star, \lambda^\star, \nu^\star$$ là nghiệm nguyên thủy & đối ngẫu với độ lệch đối ngẫu bằng không.

>$$
>\begin{align}
>    g(\lambda^\star, \nu^\star) &= \min_x L(x, \lambda^\star, \nu^\star) \\\\
>                                &= L(x^\star, \lambda^\star, \nu^\star) \\\\
>                                &= f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                                &= f(x^\star)
>\end{align}
>$$

1. $$L(x,\lambda^\star,\nu^\star) = f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x)$$ là một hàm lồi. (tổng của các hàm lồi) 
2. $$0 \in \partial \big( f(x^\star) + \sum_{i=1}^{m} \lambda_i^\star h_i(x^\star) + \sum_{j=1}^{r} \nu_j^\star l_j(x^\star) \big)$$ do đó $$\min_x L(x, \lambda^\star, \nu^\star) = L(x^\star, \lambda^\star, \nu^\star)$$.
3. Bởi bù yếu và tính khả thi nguyên thủy, $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$.

## Tính cần thiết
Khi $$x^\star, \lambda^\star, \nu^\star$$ là nghiệm nguyên thủy & đối ngẫu với độ lệch đối ngẫu bằng không (ví dụ, thỏa mãn điều kiện Slater), tất cả các bất đẳng thức dưới đây trở thành đẳng thức, vì vậy trong bài toán này $$x^\star, \lambda^\star, \nu^\star$$ thỏa mãn các điều kiện KKT.
>$$
>\begin{align}
>    f(x^\star) &= g(\lambda^\star, \nu^\star) \\\\
>                   &= \min_x  \big( f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x) \big) \\\\
>                   &\le f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                   &\le f(x^\star)
>\end{align}
>$$

1. $$f(x^\star) = g(\lambda^\star, \nu^\star)$$ có nghĩa là độ lệch đối ngẫu bằng không.
2. Để thỏa mãn $$f(x^\star) + \sum_{i=1}^m \underbrace{\lambda_i^\star h_i(x^\star)}_{0} + \sum_{j=1}^r \underbrace{\nu_j^\star l_j(x^\star)}_{0} = f(x^\star)$$, bù yếu và tính khả thi nguyên thủy phải được thỏa mãn.
3. Nếu $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$ được thỏa mãn, tất cả các bất đẳng thức trong suy dẫn trên trở thành đẳng thức.

## Tổng hợp
Tóm lại, các điều kiện KKT là:

* Điều kiện đủ cho nghiệm nguyên thủy & đối ngẫu với độ lệch đối ngẫu bằng không.
* Nếu tính đối ngẫu mạnh được giữ, chúng trở thành điều kiện cần thiết cho nghiệm nguyên thủy & đối ngẫu.

Tức là, đối với các bài toán thỏa mãn tính đối ngẫu mạnh, mối quan hệ sau được giữ.
>$$
>\begin{align}
>    x^\star, \lambda^\star, \nu^\star \text{ là nghiệm nguyên thủy và đối ngẫu} \\\\
>    \Leftrightarrow x^\star, \lambda^\star, \nu^\star \text{ thỏa mãn các điều kiện KKT} \\\\
>\end{align}
>$$
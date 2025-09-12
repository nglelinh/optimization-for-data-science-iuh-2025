---
layout: post
title: 12-02 Ví dụ bài toán bậc hai với ràng buộc đẳng thức
chapter: '12'
order: 3
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

Một [chương trình bậc hai]() chỉ với các ràng buộc đẳng thức như sau.
>$$
>\begin{align}
>    &\min_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{với điều kiện} &&{Ax = b},\\\\
>&\text{trong đó } &&P \in \mathbb{S}_{+}^n \text{ và } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}
>$$

Bài toán này là lồi và không có ràng buộc bất đẳng thức, vì vậy nó thỏa mãn điều kiện Slater (Tính đối ngẫu mạnh). Nếu các nghiệm nguyên thủy & đối ngẫu là $$x^\star, \nu^\star$$, thì theo các điều kiện KKT, chúng thỏa mãn các điều kiện sau [1].

* Tính dừng: $$Px^\star + q + A^T\nu^\star = 0$$
* Bù yếu: Vì không có ràng buộc bất đẳng thức, điều này không cần được xem xét.
* Tính khả thi nguyên thủy & đối ngẫu: $$Ax^\star = b$$

Những điều kiện này có thể được biểu diễn một cách ngắn gọn bằng cách sử dụng ma trận khối, được gọi là ma trận KKT [3].
> $$
> \begin{bmatrix}
>     P       & A^T  \\\\
>     A       & 0  \\\\
> \end{bmatrix}
> \begin{bmatrix}
>     x^\star  \\\\
>     \nu^\star  \\\\
> \end{bmatrix}
> =
> \begin{bmatrix}
>     -q  \\\\
>     b  \\\\
> \end{bmatrix}
> $$

Giải phương trình ma trận này cho ta các nghiệm nguyên thủy & đối ngẫu cho bài toán đã cho.

Một sự thật thú vị là bài toán này cũng có thể được xem như việc tính toán bước Newton cho một bài toán có ràng buộc đẳng thức [3]. Đối với bài toán $$min_x f(x) \text{ với điều kiện } Ax = b$$, nếu chúng ta đặt P, q, r như sau, thì hàm mục tiêu của chương trình bậc hai trở nên giống hệt với khai triển Taylor bậc hai của $$f(x)$$.<br/>
> $$P = \nabla^2 f(x^{(k-1)})$$, $$q = \nabla f(x^{(k-1)})$$, $$r = f(x^{(k-1)})$$
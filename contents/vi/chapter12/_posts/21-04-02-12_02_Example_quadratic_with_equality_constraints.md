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

Xét một [bài toán quy hoạch bậc hai]() chỉ có các ràng buộc đẳng thức như sau:

>$$
>\begin{align}
>    &\min_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{với điều kiện} &&{Ax = b},\\\\
>&\text{trong đó } &&P \in \mathbb{S}_{+}^n \text{ và } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}
>$$

Bài toán này là bài toán lồi và không có ràng buộc bất đẳng thức, do đó thỏa mãn điều kiện Slater (tức tính đối ngẫu mạnh được đảm bảo). Nếu $$x^\star, \nu^\star$$ là cặp nghiệm tối ưu nguyên thủy và đối ngẫu, theo các điều kiện KKT chúng phải thỏa mãn [1]:

* **Điều kiện dừng:** $$Px^\star + q + A^T\nu^\star = 0$$
* **Điều kiện bù yếu:** Không xuất hiện do bài toán không có ràng buộc bất đẳng thức.
* **Tính khả thi nguyên thủy và đối ngẫu:** $$Ax^\star = b$$

Hệ điều kiện trên có thể viết gọn dưới dạng phương trình ma trận khối, trong đó ma trận hệ số được gọi là **ma trận KKT** [3]:

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

Giải hệ phương trình tuyến tính này cho ta đồng thời nghiệm nguyên thủy $$x^\star$$ và nghiệm đối ngẫu $$\nu^\star$$.

Một điểm đáng chú ý là bài toán trên cũng tương ứng với việc tính bước Newton cho bài toán tối ưu có ràng buộc đẳng thức [3]. Cụ thể, với bài toán $$\min_x f(x) \text{ với điều kiện } Ax = b$$, nếu đặt $$P, q, r$$ theo công thức dưới đây thì hàm mục tiêu của bài toán quy hoạch bậc hai chính là khai triển Taylor bậc hai của $$f$$ tại điểm lặp trước đó $$x^{(k-1)}$$:<br/>
> $$P = \nabla^2 f(x^{(k-1)})$$, $$q = \nabla f(x^{(k-1)})$$, $$r = f(x^{(k-1)})$$
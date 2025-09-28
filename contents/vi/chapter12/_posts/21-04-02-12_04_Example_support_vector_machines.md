---
layout: post
title: 12-04 Ví dụ máy vector hỗ trợ (SVM)
chapter: '12'
order: 5
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

Bài toán máy vector hỗ trợ (SVM) cho các tập không tách được như sau.

>$$
>\begin{align}
>    &\min_{\beta, \beta-0, \xi} &&{\frac{1}{2} \rVert\beta\rVert_2^2 + C\sum_{i=1}^n \xi_i} \\\\
>    &\text{với điều kiện} &&{\xi_i \ge 0, \quad i = 1, \dots, n}\\\\
>    & && y_i (x_i^T \beta + \beta-0) \ge 1 - \xi_i, \quad i = 1, \dots, n,\\\\
>&&&\text{cho trước } y \in \{-1, 1\}^n \text{ và } X \in \mathbb{R}^{n \times p}.
>\end{align}
>$$

Khi các nhân tử Lagrange cho hai ràng buộc bất đẳng thức của bài toán đã cho lần lượt là $$v^\star, w^\star \geq 0$$, hàm Lagrangian như sau.
>$$L(\beta, \beta-0, \xi, v^\star, w^\star) = \frac{1}{2} \rVert\beta\rVert_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i^\star \xi_i + \sum_{i=1}^n w_i^\star (1 - \xi_i - y_i ( x_i^T \beta + \beta_0))$$

Sử dụng hàm Lagrangian ở trên, chúng ta có thể tìm các điều kiện sau đây làm cho bài toán này thỏa mãn điều kiện tính dừng KKT. (Suy ra các điều kiện mà hàm Lagrangian trở thành 0 khi đạo hàm theo $$\beta, \beta_0, \xi$$ tương ứng)
>$$
>0 = \sum_{i=1}^n w_i^\star y_i, \quad \beta = \sum_{i=1}^n w_i^\star y_i x_i, \quad w^\star = C \cdot 1 - v^\star
>$$

Cũng vậy, bù yếu cho hai ràng buộc bất đẳng thức như sau.
> $$
> v_i^\star \xi_i = 0, \quad w_i^\star (1 - \xi_i - y_i (x_i^T \beta + \beta-0)) =0, \quad i = 1, \dots, n.
> $$

Tức là, tại điểm tối ưu, $$\beta^\star = \sum_{i=1}^n w_i^\star y_i x_i$$ được thỏa mãn, và khi $$y_i (x_i^T \beta^\star + \beta-0^\star) = 1 - \xi_i^\star$$, $$w_i^\star$$ trở thành khác không, và điểm i như vậy được gọi là **điểm hỗ trợ**.

* Đối với điểm hỗ trợ i mà $$\xi_i^\star = 0$$, $$x_i$$ nằm trên siêu phẳng và $$w_i^\star \in (0, C]$$.
* Đối với điểm hỗ trợ i mà $$\xi_i^\star \neq 0$$, $$x_i$$ nằm ở phía đối diện của siêu phẳng và $$w_i^\star = C$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/svm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$ \text{[Fig1] Illustration of support points with }\ \xi^\star \neq 0 \text{ [3]}$$ </figcaption>
</p>
</figure>

Trước khi tối ưu hóa bài toán SVM, chúng ta có thể sử dụng phương pháp trên để lọc ra các điểm không hỗ trợ (bằng cách lọc ra các điểm không hỗ trợ, chúng ta có thể tăng hiệu quả tính toán). Thực tế, các điều kiện KKT không đóng vai trò trực tiếp trong việc đưa ra nghiệm của bài toán này, nhưng chúng ta có thể thu được trực giác để hiểu rõ hơn về bài toán SVM thông qua chúng [3].

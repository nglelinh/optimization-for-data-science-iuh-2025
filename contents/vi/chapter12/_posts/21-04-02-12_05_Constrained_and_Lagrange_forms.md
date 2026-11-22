---
layout: post
title: 12-05 Dạng ràng buộc và dạng Lagrange
chapter: '12'
order: 6
owner: Wontak Ryu
categories:
- chapter12
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trong thống kê và học máy, ta thường chuyển đổi qua lại giữa **dạng ràng buộc** và **dạng Lagrange**. Hai dạng bài toán này được định nghĩa như sau:

### Dạng ràng buộc (ký hiệu là (C))
>$$ 
>\min_x \: f(x) \quad \text{ với điều kiện } h(x) \le t,\\\\
>\text{trong đó } t \in \mathbb{R} \text{ là tham số điều chỉnh.}
>$$

### Dạng Lagrange (ký hiệu là (L))
>$$ 
>\min_x \: f(x) + \lambda \cdot h(x),\\\\
>\text{trong đó } \lambda \ge 0 \text{ là tham số điều chỉnh.}
>$$

Khi $$f$$ và $$h$$ đều là các hàm lồi, xét mối quan hệ tương đương về nghiệm giữa hai bài toán:

1. **Từ (C) sang (L):** Nếu bài toán (C) khả thi chặt (thỏa mãn điều kiện Slater) nên có tính đối ngẫu mạnh, thì ứng với nghiệm $$x^\star$$ của (C), tồn tại nhân tử đối ngẫu $$\lambda^\star \ge 0$$ sao cho $$x^\star$$ cực tiểu hóa hàm mục tiêu

$$f(x) + \lambda^\star \cdot (h(x) - t),$$

và do đó $$x^\star$$ cũng là nghiệm của (L) với $$\lambda = \lambda^\star$$.
   
2. **Từ (L) sang (C):** Nếu $$x^\star$$ là nghiệm của (L) với tham số $$\lambda^\star \ge 0$$, thì $$x^\star$$ cũng là nghiệm của (C) khi đặt $$t = h(x^\star)$$. Lý do là cặp $$(x^\star, \lambda^\star)$$ thỏa mãn các điều kiện KKT của (L) thì đồng thời cũng thỏa mãn toàn bộ các điều kiện KKT của (C) tại $$t = h(x^\star)$$.


>**$$\rightarrow$$ Điều kiện KKT của (L):**
>
> $$
> \begin{align}
> \nabla_x f(x^\star) + \lambda^\star \nabla_x h(x^\star) &= 0\\\\
> \lambda^\star &\ge 0\\\\
> \end{align}
> $$
>
>
>**$$\rightarrow$$ Điều kiện KKT của (C) khi $$t = h(x^\star)$$:**
>
> $$
> \begin{align}
> \nabla_x f(x^\star) + \lambda^\star \nabla_x h(x^\star) &= 0\\\\
> \lambda^\star &\ge 0\\\\
> \lambda^\star (\underbrace{h(x^\star) - h(x^\star)}_{=0}) &= 0
> \end{align}
> $$


Tóm lại, hai chiều suy luận ở mục 1 và mục 2 cho thấy mối liên hệ sau giữa tập nghiệm của (C) và (L):


<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/conclusion.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Kết luận [3]</figcaption>
</p>
</figure>


Vậy khi nào (C) và (L) tương đương hoàn toàn ngay cả tại biên?<br/>
Chẳng hạn, khi $$h(x) \ge 0$$ (như hàm chuẩn), $$t = 0$$ và $$\lambda = \infty$$, hai dạng tương đương hoàn toàn. Với $$t = 0$$ và $$h(x) \ge 0$$, ràng buộc trong (C) trở thành $$h(x) = 0$$; tương tự, khi đặt $$\lambda = \infty$$, bài toán (L) cũng áp đặt đúng ràng buộc $$h(x) = 0$$.

### Tự tay thử: dạng ràng buộc và dạng Lagrange

<div class="opx-explainer" data-opx="cl" data-lang="vi"></div>

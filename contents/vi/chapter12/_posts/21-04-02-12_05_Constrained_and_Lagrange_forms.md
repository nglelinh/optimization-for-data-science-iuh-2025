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

Trong thống kê và học máy, chúng ta thường chuyển đổi giữa **dạng ràng buộc** và **dạng Lagrange**. Hãy định nghĩa dạng ràng buộc và dạng Lagrangian như sau.

### Dạng Ràng buộc ((C) sau đây)
>$$ 
>\min_x \: f(x) \quad \text{ với điều kiện } h(x) \le t,\\\\
>\text{trong đó } t \in \mathbb{R} \text{ là tham số điều chỉnh.}
>$$

### Dạng Lagrange ((L) sau đây)
>$$ 
>\min_x \: f(x) + \lambda \cdot h(x),\\\\
>\text{trong đó } \lambda \ge 0 \text{ là tham số điều chỉnh.}
>$$

Khi $$f, h$$ là lồi, hãy xem xét các trường hợp mà hai bài toán cho cùng một nghiệm.

1. **(C) đến (L):** Khi (C) là khả thi chặt chẽ (thỏa mãn điều kiện Slater) và thỏa mãn tính đối ngẫu mạnh, nếu tồn tại một nghiệm đối ngẫu $$\lambda^\star \ge 0$$ tối thiểu hóa hàm mục tiêu sau đây cho nghiệm $$x^\star$$ của (C), thì $$x^\star$$ cũng là nghiệm của (L). 

$$f(x) + \lambda \cdot (h(x) - t)$$
   
2. **(L) đến (C):** Nếu $$x^\star$$ là nghiệm của (L) và (C) với $$t = h(x^\star)$$ thỏa mãn các điều kiện KKT, thì $$x^\star$$ cũng là nghiệm của (C). Điều này là vì $$\lambda^\star, x^\star$$ thỏa mãn các điều kiện KKT của (L) cũng thỏa mãn các điều kiện KKT của (C) với $$t = h(x^\star)$$.


>**$$\rightarrow$$ (L)의 KKT conditions:**
>
> $$
> \begin{align}
> \nabla_x f(x^\star) + \lambda^\star \nabla_x h(x^\star) &= 0\\\\
> \lambda^\star &\ge 0\\\\
> \end{align}
> $$
>
>
>**$$\rightarrow$$ $$t = h(x^\star)$$인 (C)의 KKT conditions:**
>
> $$
> \begin{align}
> \nabla_x f(x^\star) + \lambda^\star \nabla_x h(x^\star) &= 0\\\\
> \lambda^\star &\ge 0\\\\
> \lambda^\star (\underbrace{h(x^\star) - h(x^\star)}_{=0}) &= 0
> \end{align}
> $$


Tóm lại, 1 và 2 lần lượt cho thấy các mối quan hệ sau.


<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/conclusion.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Kết luận [3]</figcaption>
</p>
</figure>


Vậy, trong những hoàn cảnh nào (C) và (L) thể hiện sự tương đương hoàn hảo?<br/>
Ví dụ, khi $$h(x) \ge 0$$ (như chuẩn), $$t = 0$$, và $$\lambda = \infty$$, sự tương đương hoàn hảo được thể hiện. Do các điều kiện đã cho, ràng buộc trong (C) trở thành $$h(x) = 0$$, và bằng cách đặt $$\lambda$$ thành $$\infty$$, (L) cũng áp đặt cùng một ràng buộc ($$h(x) = 0$$). 
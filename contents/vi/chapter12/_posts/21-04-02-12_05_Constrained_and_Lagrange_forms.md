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

Trong sách giáo khoa thống kê và thư viện học máy (như `scikit-learn`), bạn sẽ thấy bài toán Lasso hay Ridge regression đôi khi được viết dưới **dạng ràng buộc (C)**:
$$\min_\beta \; \frac{1}{2}\|y - X\beta\|_2^2 \quad \text{s.t.} \quad \|\beta\|_1 \le t,$$
nhưng lúc khác lại viết dưới **dạng phạt / dạng Lagrange (L)**:
$$\min_\beta \; \frac{1}{2}\|y - X\beta\|_2^2 + \lambda \|\beta\|_1.$$
Rất nhiều người học mặc nhiên cho rằng hai dạng này "tương đương nhau" — nhưng chính xác thì chúng tương đương theo nghĩa nào? Có phải *mọi* $$t$$ đều ứng với một $$\lambda$$, và *mọi* $$\lambda$$ đều ứng với một $$t$$ không?

Bài học này dùng đúng công cụ **điều kiện KKT** để trả lời câu hỏi ấy một cách sắc bén và chính xác tuyệt đối: nếu bài toán lồi và thỏa Slater, **cả hai dạng quét qua chính xác cùng một họ nghiệm tối ưu** (đường chính quy hóa — regularization path)! Tuy nhiên, khi bài toán *không lồi* (như hồi quy best-subset dùng chuẩn $$\ell_0$$), sự tương đương này có thể sụp đổ: dạng Lagrange có thể bỏ sót cả những nghiệm hoàn hảo của dạng ràng buộc!

## Bản đồ kiến thức nền: Ba trụ cột của sự tương đương giữa dạng (C) và dạng (L)

- **Chiều thuận (Từ dạng Lagrange (L) $$\to$$ dạng ràng buộc (C)) — LUÔN ĐÚNG (kể cả không lồi!):** Nếu $$x^*$$ là nghiệm tối ưu của $$\min_x f(x) + \lambda h(x)$$ với $$\lambda \ge 0$$, chỉ cần đặt $$t = h(x^*)$$, lập tức $$x^*$$ cũng là nghiệm tối ưu của $$\min_{h(x) \le t} f(x)$$! (Chứng minh 2 dòng: với mọi $$x$$ có $$h(x) \le t = h(x^*)$$, ta có $$f(x) \ge f(x) + \lambda(h(x) - h(x^*)) \ge f(x^*)$$!)
- **Chiều ngược (Từ dạng ràng buộc (C) $$\to$$ dạng Lagrange (L)) — CẦN TÍNH LỒI + SLATER:** Nếu $$x^*$$ là nghiệm của (C) với ngân sách $$t$$, nhờ tính lồi và điều kiện Slater tồn tại nhân tử Lagrange tối ưu $$\lambda^* \ge 0$$ sao cho $$x^*$$ thỏa điều kiện dừng $$0 \in \partial f(x^*) + \lambda^* \partial h(x^*)$$ — mà đó chính xác là điều kiện tối ưu của dạng (L) với $$\lambda = \lambda^*$$!
- **Ánh xạ nghịch biến giữa ngân sách $$t$$ và lực phạt $$\lambda$$:** Ngân sách $$t$$ càng nhỏ (ràng buộc càng chặt), lực phạt $$\lambda$$ tương ứng càng lớn; khi $$t$$ lớn hơn hoặc bằng $$h(x_{\text{unconstrained}}^*)$$ (ràng buộc lỏng), lực phạt tương ứng bằng đúng $$\lambda = 0$$!

### Khung giải thích (nên đọc chậm): Tính tay ánh xạ 1–1 giữa ngân sách $$t$$ và lực phạt $$\lambda$$ trên Ridge 1D

Xét bài toán Ridge 1D với nghiệm không ràng buộc là $$x_{\text{OLS}} = 5$$:
- **Dạng ràng buộc (C):** $$\min_x \frac{1}{2}(x - 5)^2 \;\text{ s.t. }\; \frac{1}{2}x^2 \le t$$ (với $$t > 0$$).
- **Dạng Lagrange (L):** $$\min_x \frac{1}{2}(x - 5)^2 + \lambda \cdot \frac{1}{2}x^2$$ (với $$\lambda \ge 0$$).

1. **Giải dạng Lagrange (L) theo $$\lambda \ge 0$$:**
   Đạo hàm $$(x - 5) + \lambda x = 0 \implies x^*(\lambda) = \frac{5}{1 + \lambda}$$.
2. **Tìm ngân sách $$t$$ tương ứng cho từng giá trị $$\lambda$$:**
   - Chọn $$\lambda = 1.5$$: nghiệm là $$x^* = \frac{5}{1 + 1.5} = 2.0$$. Đặt ngân sách $$t = \frac{1}{2}(2.0)^2 = 2.0$$.
   - Kiểm tra ngược dạng ràng buộc (C) với $$t = 2.0$$ (tức $$|x| \le 2$$): để $$(x - 5)^2$$ nhỏ nhất trên $$[-2, 2]$$, hiển nhiên chọn $$x^* = 2.0$$ — trùng khít! Và nhân tử KKT tại $$x^* = 2$$ là $$u^* = -\frac{2 - 5}{2} = 1.5 = \lambda$$!
3. **Trường hợp ràng buộc lỏng ($$t \ge 12.5$$, tức $$|x| \ge 5$$):**
   Với mọi $$t \ge 12.5$$, nghiệm dạng (C) luôn đứng yên tại $$x^* = 5$$, và tất cả các giá trị $$t \in [12.5, \infty)$$ đều ánh xạ vào duy nhất một giá trị $$\lambda = 0$$!

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

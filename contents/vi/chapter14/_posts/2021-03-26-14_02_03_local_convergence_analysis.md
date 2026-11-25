---
layout: post
title: 14-02-03 Phân tích hội tụ cục bộ
chapter: '14'
order: 8
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Phương pháp Newton nổi tiếng với tốc độ "thần thánh" — gọi là **hội tụ bậc hai (quadratic convergence)** — nhưng định lý chỉ cấp giấy bảo hành tốc độ ấy khi bạn **đã đứng đủ gần nghiệm tối ưu $$x^\star$$**. Câu hỏi tự nhiên là: *thế nào là "đủ gần", và những giả thiết nào trên hàm $$f$$ quyết định bán kính của vùng an toàn đó?*

Mục này đặt nền tảng định lượng đầu tiên cho lý thuyết hội tụ Newton thuần túy. Bạn sẽ thấy ba điều kiện kinh điển (lồi mạnh $$m$$, Hessian Lipschitz $$M$$ và điểm khởi tạo đủ gần $$x^\star$$) kết hợp với nhau để tạo ra hệ số co rút bậc hai $$\|x^{(k+1)} - x^\star\|_2 \le \frac{M}{2m}\|x^{(k)} - x^\star\|_2^2$$ — đồng thời cảnh báo một ví dụ phân kỳ điển hình khi vi phạm giả thiết khởi tạo.

## Bản đồ kiến thức nền: Bốn yếu tố quyết định vùng hội tụ cục bộ

- **Tính lồi mạnh (hằng số $$m > 0$$):** Đảm bảo $$\nabla^2 f(x) \succeq m I$$, tức là độ cong không bao giờ quá phẳng nên nghịch đảo Hessian bị chặn trên: $$\|(\nabla^2 f(x))^{-1}\|_2 \le \frac{1}{m}$$.
- **Tính Lipschitz của Hessian (hằng số $$M > 0$$):** Đảm bảo độ cong không thay đổi quá đột ngột ($$\|\nabla^2 f(x) - \nabla^2 f(y)\|_2 \le M\|x - y\|_2$$), giúp mô hình parabol Taylor bậc hai bám sát hàm thật trong vùng lân cận.
- **Định lý hội tụ cục bộ bậc hai:** Khi $$\|x^{(k)} - x^\star\|_2 < \frac{2m}{M}$$, sai số bước sau thỏa $$\|x^{(k+1)} - x^\star\|_2 \le \frac{M}{2m}\|x^{(k)} - x^\star\|_2^2$$. Sai số $$10^{-2}$$ lập tức rơi xuống cỡ $$10^{-4}$$, rồi $$10^{-8}$$, rồi $$10^{-16}$$!
- **Nguy cơ phân kỳ ngoài bán kính hội tụ:** Nếu khởi tạo vượt quá ngưỡng $$\frac{2m}{M}$$, hệ số co rút lớn hơn $$1$$ khiến bước Newton thuần túy phóng vọt qua đáy và dao động hoặc phân kỳ.

### Khung giải thích (nên đọc chậm): Tính trực tiếp bán kính hội tụ cục bộ và theo dõi sai số bình phương

Xét bài toán 1 chiều cực tiểu hóa $$f(x) = \frac{1}{2}x^2 + \frac{1}{6}x^3$$ trên miền $$x \in (-0.5, 0.5)$$, với nghiệm tối ưu là $$x^\star = 0$$.

1. **Xác định các hằng số $$m$$ và $$M$$ trên đoạn $$[-0.5, 0.5]$$:**
   - $$f'(x) = x + \frac{1}{2}x^2$$, $$f''(x) = 1 + x$$, $$f'''(x) = 1$$.
   - Trên $$[-0.5, 0.5]$$, độ cong nhỏ nhất là $$m = \min f''(x) = 1 - 0.5 = 0.5$$.
   - Hằng số Lipschitz của Hessian là $$M = \max \vert f'''(x) \vert = 1$$.
   - Tỷ số hội tụ cục bộ: $$\frac{M}{2m} = \frac{1}{2(0.5)} = 1$$, nên bán kính đảm bảo co rút chặt là $$\vert x^{(0)} - x^\star \vert < 1$$ (nằm gọn trong miền xét).
2. **Kiểm tra công thức sai số từng bước từ $$x^{(0)} = 0.2$$:**
   - **Bước 1:** $$f'(0.2) = 0.22$$, $$f''(0.2) = 1.2 \implies x^{(1)} = 0.2 - \frac{0.22}{1.2} = \frac{0.02}{1.2} \approx 0.01667$$.
     Đối chiếu cận lý thuyết: $$\frac{M}{2m}(0.2)^2 = 1 \cdot 0.04 = 0.04$$ (thực tế $$0.01667 \le 0.04$$).
   - **Bước 2:** $$f'(0.01667) \approx 0.01681$$, $$f''(0.01667) \approx 1.01667 \implies x^{(2)} \approx 0.000137$$.
     Đối chiếu cận lý thuyết: $$1 \cdot (0.01667)^2 \approx 0.000278$$ (thực tế $$0.000137 \le 0.000278$$).
   Chỉ sau 2 bước từ $$0.2$$, sai số đã co lại hơn **1.400 lần**!

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
});
</script>

Tính chất quan trọng thứ hai của phương pháp Newton là hội tụ cục bộ: sự hội tụ được đảm bảo khi điểm khởi tạo đủ gần nghiệm và các điều kiện thích hợp được thỏa mãn. Vì phương pháp Newton thuần túy trong [14-01]({% multilang_post_url contents/chapter14/2021-03-26-14_01_newton_method %}) không đảm bảo hội tụ toàn cục, ở các mục sau ta sẽ xây dựng phương pháp Newton có giảm chấn (damped Newton method) bằng cách điều chỉnh kích thước bước với tìm kiếm đường backtracking như trong [Chương 6]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}), rồi phân tích tốc độ hội tụ của nó.

>Định lý: Cho $$F : \mathbb{R}^{n}\, \rightarrow  \, \mathbb{R}^{n}$$ khả vi liên tục và $$x^{\star} \in \mathbb{R}^{n}$$ là một nghiệm của $$F$$, tức $$F(x^{\star})=0$$.
>Nếu $$F^{'}(x^{\star})$$ không suy biến, thì hai khẳng định (a) và (b) sau đây đúng: \\
>(a) Tồn tại $$\delta > 0$$ sao cho nếu $$\| x^{(0)}-x^{\star} \|<\delta$$ thì phương pháp Newton xác định và đạt hội tụ siêu tuyến tính:
>\begin{align}
>\lim_{ k \rightarrow \infty } \frac{ \|\| x^{ (k+1) }-x^{ \star } \|\| } { \|\| x^{ (k) }-x^{ \star } \|\| } =0.
>\end{align} \\
>(b) Nếu $$F^{'}$$ liên tục Lipschitz trong lân cận của $$x^{\star}$$, thì tồn tại hằng số $$K > 0$$ sao cho dãy nghiệm đạt hội tụ bậc hai:
>\begin{align}
>\|\|x^{ (k+1) } - x^{ \star }\|\| \leq K \|\| x^{ (k) }-x^{ \star }\|\|^{2}.
>\end{align}

## Chứng minh (a)
>Khai triển Taylor bậc nhất của $$F(x^{\star})$$ quanh $$x^{k}$$ với ký hiệu little-o cho phần dư bậc cao hơn:
>\begin{align}
>0=F(x^{\star}) = F(x^{k}) +\nabla F(x^{k})(x^{\star}-x^{k})+o(\|\|x^{k}-x^{\star}\|\|).\\
>\end{align}
>Nhân cả hai vế bên trái với $$\nabla F(x^{k})^{-1}$$ rồi chuyển vế. Do $$\nabla F(x^{k})^{-1}$$ bị chặn trong lân cận $$x^{\star}$$, tích của nó với $$o(\|\|x^{k}-x^{\star}\|\|)$$ vẫn là $$o(\|\|x^{k}-x^{\star}\|\|)$$:
>\begin{align}
>x^{k}-x^{\star}-\nabla F(x^{k})^{-1} F(x^{k}) = o(\|\|x^{k}-x^{\star}\|\|).
>\end{align}
>Thay công thức cập nhật Newton $$x^{k+1}=x^{k}-\nabla F(x^{k})^{-1}F(x^{k})$$, ta thu được:
>\begin{align}
>x^{k+1}-x^{\star}=o(\|\|x^{k}-x^{\star}\|\|).
>\end{align}
>Do đó, với $$x^{k} \neq x^{\star}$$, từ định nghĩa giới hạn của ký hiệu little-o [[wikipedia](https://en.wikipedia.org/wiki/Big_O_notation)] ta suy ra (a):

>\begin{align}
>\lim_{k\rightarrow \infty} \frac{\|\|x^{k+1}-x^{\star}\|\|}{\|\|x^{k}-x^{\star}\|\|} = \lim_{k\rightarrow \infty}\frac{o(\|\|x^{k}-x^{\star}\|\|)}{\|\|x^{k}-x^{\star}\|\|} = 0.
>\end{align}

## Chứng minh (b)
Cách chứng minh tương tự như phần chứng minh tốc độ hội tụ bậc hai trong giai đoạn thuần túy (Pure phase) ở bài [[14-05]({% multilang_post_url contents/chapter14/2021-03-26-14_05_convergence_analysis %})], nên được lược bỏ tại đây.

## Ví dụ: trường hợp phân kỳ
Dưới đây là một ví dụ minh họa trường hợp phương pháp Newton thuần túy không hội tụ.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/1_.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Phương pháp Newton thuần túy áp dụng cho bài toán tìm nghiệm: trường hợp phân kỳ</figcaption>
</p>
</figure>

[image-link](https://slideplayer.com/slide/4998677/)

Như minh họa trong hình, tùy thuộc vào điểm khởi tạo $$x_0$$, dãy lặp có thể phân kỳ.

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

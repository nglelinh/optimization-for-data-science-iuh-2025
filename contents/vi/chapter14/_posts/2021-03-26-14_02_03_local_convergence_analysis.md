---
layout: post
title: 14-02-03 Phân tích hội tụ cục bộ
order: 7
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
});
</script>

Tính chất quan trọng thứ hai của phương pháp Newton là sự hội tụ được đảm bảo gần nghiệm khi các điều kiện nhất định được thỏa mãn. Điều này được gọi là hội tụ cục bộ. Vì phương pháp Newton thuần túy mà chúng ta đã thảo luận từ [14-01]({% multilang_post_url contents/chapter14/2021-03-26-14_01_newton_method %}) không đảm bảo hội tụ, sau này chúng ta sẽ thiết kế phương pháp Newton có giảm chấn để đảm bảo hội tụ bằng cách điều chỉnh kích thước bước sử dụng cùng phương pháp tìm kiếm đường backtracking được đề cập trong [Chương 6]({% multilang_post_url contents/chapter06/21-03-20-06_00_gradient_descent %}), và phân tích sự hội tụ của nó.


>Định lý: Cho $$F : \mathbb{R}^{n}\, \rightarrow  \, \mathbb{R}^{n}$$ liên tục khả vi, và cho $$x^{\star} \in \mathbb{R}^{n}$$ là một nghiệm của hàm $$F$$, tức là $$F(x^{\star})=0$$.
>Nếu $$F^{'}(x^{\star})$$ không suy biến, thì các điều kiện (a) và (b) sau được thỏa mãn: \\
>(a) Nếu tồn tại một $$\delta$$ dương (>0) sao cho $$\| x^{(0)}-x^{\star} \|<\delta$$ và phương pháp Newton được định nghĩa, thì phương trình sau (hội tụ siêu tuyến tính) được thỏa mãn:
>\begin{align}
>\lim_{ k \rightarrow \infty } \frac{ \|\| x^{ (k+1) }-x^{ \star } \|\| } { \|\| x^{ (k) }-x^{ \star } \|\| } =0.
>\end{align} \\
>(b) Nếu $$F^{'}$$ liên tục Lipschitz gần $$x^{\star}$$, thì tồn tại một K dương (>0) sao cho phương trình sau (hội tụ bậc hai) được thỏa mãn:
>\begin{align}
>\|\|x^{ (k+1) } - x^{ \star }\|\| \leq K \|\| x^{ (k) }-x^{ \star }\|\|^{2}.
>\end{align}

## Chứng minh (a)
>Chúng ta sắp xếp $$F(x^{\star})$$ đến bậc 1 sử dụng khai triển Taylor. Vì các số hạng bậc 2 và cao hơn được giới hạn bởi một bội số hằng của chuẩn của số hạng bậc 1, chúng ta có thể biểu diễn nó bằng ký hiệu little-o như sau:
>\begin{align}
>0=F(x^{\star}) = F(x^{k}) +\nabla F(x^{k})(x^{\star}-x^{k})+o(\|\|x^{k}-x^{\star}\|\|).\\
>\end{align}
>Nhân cả hai vế với $$\nabla F(x^{k})^{-1}$$ và sắp xếp. Vì little-o được xử lý như một số hạng hằng số, nó có thể được bỏ qua.
>\begin{align}
>x^{k}-x^{\star}-\nabla F(x^{k})^{-1} F(x^{k}) = o(\|\|x^{k}-x^{\star}\|\|).
>\end{align}
>Sử dụng phương pháp Newton $$x^{k+1}=x^{k}-\nabla F(x^{k})^{-1}F(x^{k})$$, chúng ta có thể thu được kết quả sau:
>\begin{align}
>x^{k+1}-x^{\star}=o(\|\|x^{k}-x^{\star}\|\|),
>\end{align}
>Do đó, khi $$x^{k} \neq x^{\star}$$, chúng ta có thể chứng minh (a) bằng định nghĩa giới hạn của little-o [[wikipedia](https://en.wikipedia.org/wiki/Big_O_notation)].

>\begin{align}
>\lim_{k\rightarrow \infty} \frac{\|\|x^{k+1}-x^{\star}\|\|}{\|\|x^{k}-x^{\star}\|\|} = \lim_{k\rightarrow \infty}\frac{o(\|\|x^{k}-x^{\star}\|\|)}{\|\|x^{k}-x^{\star}\|\|}.
>\end{align}

## Chứng minh (b)
Quá trình này giống hệt với việc chứng minh rằng tốc độ hội tụ trong giai đoạn Damped của [[14-05]({% multilang_post_url contents/chapter14/2021-03-26-14_05_convergence_analysis %})] là bậc hai. Do đó, nó được bỏ qua.

## Ví dụ : trường hợp phân kỳ
Chúng ta xem xét ngắn gọn một ví dụ mà sự hội tụ không được đảm bảo với phương pháp Newton thuần túy.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/1_.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] phương pháp Newton thuần túy áp dụng cho tìm nghiệm : trường hợp phân kỳ </figcaption>
</p>
</figure>

[image-link](https://slideplayer.com/slide/4998677/)

Như được hiển thị trong hình, tùy thuộc vào điểm khởi tạo $$x_0$$, nghiệm có thể phân kỳ.

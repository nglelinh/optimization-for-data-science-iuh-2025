---
layout: post
title: 01-02 Bài toán tối ưu hóa lồi
chapter: '01'
order: 3
owner: Kyeongmin Woo
categories:
- chapter01
lang: vi
lesson_type: required
---

Bài toán tối ưu hóa lồi là một lớp đặc biệt quan trọng của bài toán tối ưu hóa.

>$$\begin{align*} 
>&\min_{x\in D}\ &&f(x) \\
>&\text{với điều kiện} && g_i(x) \le 0,\ i = 1, ..., m \\
>&&& h_j(x) = 0,\ j = 1,\ ..., r
>\end{align*}$$

**Bài toán tối ưu hóa lồi ở dạng chuẩn [3]**

Trong dạng chuẩn này, hàm mục tiêu $$f$$ và các hàm ràng buộc bất đẳng thức $$g_i$$ là các hàm lồi, còn các hàm ràng buộc đẳng thức $$h_j$$ là các hàm affine (hàm tuyến tính cộng với một hằng số):
>$$h_j,\ j = 1, ..., r$$ là hàm affine: $$h_j(x) = a_{j}^T x + b_{j},\ j=1, ..., r$$

Vậy thế nào là một hàm lồi? Để trả lời câu hỏi này, trước hết ta cần định nghĩa tập lồi.

## Tập lồi

Đoạn thẳng nối hai điểm $$x_1$$ và $$x_2$$ được định nghĩa là tập các điểm có dạng:

>$$x = \theta x_1 + (1 - \theta) x_2$$ với $$0 \le \theta \le 1$$

Một tập hợp được gọi là **tập lồi** nếu đoạn thẳng nối hai điểm $$x_1, x_2$$ bất kỳ thuộc tập đều nằm hoàn toàn trong tập đó. Nói cách khác, tập $$C$$ là tập lồi nếu:

>$$x_1, x_2 \in C$$, $$0 \le \theta \le 1$$  $$\Rightarrow$$ $$\theta x_1 + (1-\theta)x_2 \in C$$

Chẳng hạn, trong hình minh họa dưới đây, chỉ có hình ngoài cùng bên trái là tập lồi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/Convex_set.png" alt="Convex Set" width="70%">
  <figcaption style="text-align: center;">[Hình1] Trái: tập lồi; giữa & phải: tập không lồi [2]</figcaption>
</p>
</figure>

## Hàm lồi

Một hàm số $$f$$ được gọi là **hàm lồi** nếu thỏa mãn điều kiện sau:

>$$f: \mathbb{R}^n \rightarrow \mathbb{R} $$ là lồi nếu $$ dom(f) $$ là tập lồi và
>
>$$f(\theta x + (1 - \theta)y) \le \theta f(x) + (1-\theta)f(y) $$ với mọi $$ x, y \in dom(f),\ 0 \le \theta \le 1$$

Về mặt hình học, với hai điểm bất kỳ $$(x, f(x))$$ và $$(y, f(y))$$ trên đồ thị của $$f$$, đoạn thẳng nối hai điểm đó luôn nằm phía trên (hoặc trùng với) đồ thị trên đoạn giữa $$x$$ và $$y$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/Convex_function.png" alt="Convex Function" width="70%">
  <figcaption style="text-align: center;">[Hình2] Hàm lồi [2]</figcaption>
</p>
</figure>

## Mối quan hệ giữa tập lồi và hàm lồi

Tập lồi và hàm lồi liên hệ chặt chẽ với nhau qua khái niệm biểu đồ trên (epigraph):
> Một hàm $$f$$ là hàm lồi khi và chỉ khi biểu đồ trên (epigraph) của nó là một tập lồi.

Tiền tố *epi* nghĩa là "phía trên", do đó **epigraph** của $$f$$ là tập hợp tất cả các điểm nằm trên hoặc phía trên đồ thị của $$f$$. Về mặt toán học:

>$$
\eqalign{
& \text{epigraph của } f: \mathbb{R}^n \rightarrow \mathbb{R}\\
& \text{epi } f = \{(x, t) \in \mathbb{R}^{n+1} \mid x \in \text{ dom } f, f(x) \le t\}
}
$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/epigraph.png" alt="Epigraph" width="70%">
  <figcaption style="text-align: center;">[Hình3] Epigraph [2]</figcaption>
</p>
</figure>

Nếu $$f$$ là hàm lồi thì $$\text{epi } f$$ là tập lồi, và ngược lại. Đây là tính chất cốt lõi kết nối hình học của tập lồi với giải tích của hàm lồi.

## Hàm lồi và hàm lõm

Một hàm $$f$$ được gọi là **hàm lõm** nếu $$-f$$ là hàm lồi. Tương đương, $$f$$ lõm nếu $$dom(f)$$ là tập lồi và:

>$$f(\theta x + (1 - \theta)y) \ge \theta f(x) + (1-\theta)f(y) $$ với mọi $$ x, y \in dom(f),\ 0 \le \theta \le 1$$

Về mặt hình học, đoạn thẳng nối hai điểm bất kỳ trên đồ thị hàm lõm luôn nằm phía dưới đồ thị: hàm lõm "cong xuống", còn hàm lồi "cong lên".

Vì sao trong lý thuyết tối ưu ta tập trung vào hàm lồi mà ít trình bày riêng về hàm lõm?
- Hàm lõm chỉ là phiên bản đổi dấu của hàm lồi. Mọi bài toán cực đại hóa hàm lõm $$f$$ đều có thể chuyển ngay thành bài toán cực tiểu hóa hàm lồi $$-f$$.

## Tính chất cốt lõi của bài toán tối ưu hóa lồi

Một tính chất nổi bật khiến bài toán tối ưu hóa lồi dễ giải hơn nhiều so với bài toán không lồi là:
> Nếu bài toán tối ưu hóa là lồi và $$x$$ là điểm cực tiểu địa phương, thì $$x$$ cũng là điểm cực tiểu toàn cục.

Ta chứng minh mệnh đề này bằng phản chứng:

>**Chứng minh bằng phản chứng:**
>
>Giả sử $$x$$ là điểm cực tiểu địa phương của bài toán tối ưu hóa lồi nhưng không phải cực tiểu toàn cục. Khi đó, tồn tại bán kính $$\rho > 0$$ sao cho $$f(x) \le f(z)$$ với mọi điểm khả thi $$z$$ thỏa mãn $$\|z - x\|_2 \le \rho$$. Mặt khác, vì $$x$$ không phải cực tiểu toàn cục nên tồn tại một điểm khả thi $$y$$ sao cho $$f(y) < f(x)$$. Do $$f(y) < f(x)$$, nhất thiết phải có $$\|y - x\|_2 > \rho$$.
>
>Đặt $$\theta=\frac{\rho}{2\|y-x\|_2}$$ (khi đó $$0 < \theta < \frac{1}{2} < 1$$) và xét điểm $$z = \theta y + (1 - \theta) x = x + \theta( y - x)$$. Ta có:
>
>1. Vì miền khả thi của bài toán tối ưu hóa lồi là tập lồi, $$z$$ là tổ hợp lồi của hai điểm khả thi $$x, y$$ nên $$z$$ cũng khả thi.
>
>2. $$\|z - x\|_2 = \theta \|y - x\|_2 = \frac{\rho}{2} < \rho$$.
>
>3. $$f(z) \le \theta f(y) + (1 - \theta) f(x) < \theta f(x) + (1 - \theta) f(x) = f(x)$$.
>
>Hai điều (2) và (3) mâu thuẫn với giả thiết $$x$$ là cực tiểu địa phương trong hình cầu bán kính $$\rho$$. Vậy mọi điểm cực tiểu địa phương $$x$$ đều là điểm cực tiểu toàn cục.

## Tổ hợp lồi

Tổ hợp lồi của các điểm $$x_1, ..., x_k$$ được định nghĩa là:

> $$x = \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k$$ với $$\theta_1 + \cdots + \theta_k = 1, \theta_i \ge 0$$

Nếu $$D$$ là tập lồi và $$x_1, x_2, ..., x_k \in D$$, thì mọi tổ hợp lồi $$x$$ của chúng cũng thuộc $$D$$.

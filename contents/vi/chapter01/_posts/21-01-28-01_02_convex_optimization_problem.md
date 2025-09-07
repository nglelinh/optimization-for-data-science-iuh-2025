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

Bài toán tối ưu hóa lồi là một loại bài toán tối ưu hóa.

>$$\begin{align*} 
>&\min_{x\in D}\ &&f(x) \\
>&\text{với điều kiện} && g_i(x) \le 0,\ i = 1, ..., m \\
>&&& h_j(x) = 0,\ j = 1,\ ..., r
>\end{align*}$$

**Bài toán Tối ưu hóa Lồi ở dạng chuẩn [3]**

Ở đây, hàm mục tiêu $$f$$ và các hàm ràng buộc bất đẳng thức $$g_i$$ là lồi, và các hàm ràng buộc đẳng thức $$h_j$$ là affine. Một hàm affine là một hàm tuyến tính cộng với một hằng số:
>$$h_j,\ j = 1, ..., r$$ là affine: $$h_j(x) = a_{j}^T x + b_{j},\ j=1, ..., r$$

Điều gì có nghĩa là một hàm lồi? Để hiểu điều này, trước tiên chúng ta cần hiểu tập lồi.

## Tập lồi
Một đoạn thẳng nối hai điểm $$x_1$$ và $$x_2$$ được định nghĩa là:

>$$x = \theta x_1 + (1 - \theta) x_2$$ với $$0 \le \theta \le 1$$

Cho một tập hợp, nếu đoạn thẳng giữa bất kỳ hai điểm $$x_1$$ và $$x_2$$ nào trong tập cũng được chứa trong tập đó, chúng ta gọi nó là tập lồi. Nói cách khác, một tập $$C$$ là lồi nếu:

>$$x_1, x_2 \in C$$, $$0 \le \theta \le 1$$  $$\Rightarrow$$ $$\theta x_1 + (1-\theta)x_2 \in C$$

Ví dụ, trong hình dưới đây, chỉ có hình bên trái nhất là tập lồi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/Convex_set.png" alt="Convex Set" width="70%">
  <figcaption style="text-align: center;">[Hình1] trái: tập lồi, giữa & phải: tập không lồi [2]</figcaption>
</p>
</figure>

## Hàm lồi
Một hàm lồi được định nghĩa như sau:

>$$f: \mathbb{R}^n \rightarrow \mathbb{R} $$ là lồi nếu $$ dom(f) $$ là tập lồi và,
>
>$$f(\theta x + (1 - \theta)y) \le \theta f(x) + (1-\theta)f(y) $$ với mọi $$ x, y \in dom(f),\ 0 \le \theta \le 1$$

Về mặt hình học, điều này có nghĩa là với bất kỳ hai điểm $$(x, f(x))$$ và $$(y, f(y))$$ nào trên đồ thị của $$f$$, đoạn thẳng nối chúng nằm phía trên đồ thị giữa $$x$$ và $$y$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/Convex_function.png" alt="Convex Function" width="70%">
  <figcaption style="text-align: center;">[Hình2] Hàm Lồi [2]</figcaption>
</p>
</figure>

## Mối quan hệ giữa tập lồi và hàm lồi
Có một mối quan hệ chặt chẽ giữa hàm lồi và tập lồi:
> Một hàm $$f$$ là lồi khi và chỉ khi epigraph của nó là tập lồi.

Epigraph là gì? 'Epi' có nghĩa là 'phía trên', vì vậy epigraph của $$f$$ là tập hợp các điểm phía trên đồ thị của $$f$$. Chính thức, epigraph được định nghĩa là:

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

Nếu $$f$$ là hàm lồi, thì $$\text{epi } f$$ luôn là tập lồi, và ngược lại. Đây là tính chất quan trọng kết nối định nghĩa của hàm lồi và tập lồi.

## Hàm lồi và hàm lõm

Một hàm $$f$$ là lõm nếu $$-f$$ là lồi. Tương đương, $$f$$ là lõm nếu:

>$$f(\theta x + (1 - \theta)y) \ge \theta f(x) + (1-\theta)f(y) $$ với mọi $$ x, y \in dom(f),\ 0 \le \theta \le 1$$

Về mặt hình học, điều này có nghĩa là đoạn thẳng nối bất kỳ hai điểm nào trên đồ thị nằm dưới đồ thị của hàm số. Một hàm lõm "cong xuống" trong khi hàm lồi "cong lên".

Còn về hàm lõm thì sao? Tại sao chúng ta nhấn mạnh hàm lồi nhiều đến vậy, và dường như "bỏ qua" hàm lõm?
- Chúng ta "không quan tâm" đến hàm lõm riêng biệt vì chúng chỉ là hình ảnh phản chiếu của hàm lồi. Luôn chuyển đổi việc tối đa hóa hàm lõm $$f$$ thành tối thiểu hóa hàm lồi $$-f$$.

## Tính chất tốt của bài toán tối ưu hóa lồi
Một điểm cực tiểu địa phương của hàm lồi luôn là cực tiểu toàn cục. Đối với bài toán tối ưu hóa lồi, nghiệm thường dễ tìm hơn so với bài toán không lồi, vì hàm lồi có tính chất sau:
> Nếu $$f$$ là lồi và $$x$$ là điểm tối ưu địa phương (tức là cực tiểu địa phương), thì $$x$$ cũng là điểm tối ưu toàn cục.

Hãy chứng minh điều này bằng phản chứng:

>**Chứng minh bằng phản chứng:**
>
>Giả sử với hàm lồi $$f$$, $$x$$ là điểm tối ưu địa phương nhưng không phải tối ưu toàn cục. Gọi $$y$$ là điểm tối ưu toàn cục khả thi, nên với mọi $$\rho$$ dương, $$\|y - x\|_2 > \rho$$ và $$f(y) < f(x)$$. (Vì $$x$$ tối ưu địa phương, nếu $$\|x - y\|_2 \le \rho$$ thì $$f(x) \le f(y)$$, điều này mâu thuẫn với việc $$y$$ tối ưu toàn cục.)
>Bây giờ, với $$\theta=\frac{\rho}{2\|y-x\|_2}$$, gọi $$z = \theta y + (1 - \theta) x = x + \theta( y - x)$$. Khi đó:
>
>1. $$z$$ là tổ hợp lồi của hai điểm khả thi $$x, y$$, nên nó cũng khả thi.
>
>2. $$\|z - x\|_2 = \theta \|y - x\|_2 = \frac{\rho}{2} < \rho$$.
>
>3. $$f(z) \le \theta f(y) + (1 - \theta) f(x) < \theta f(x) + (1 - \theta) f(x) = f(x)$$
>
>Điểm 2 và 3 mâu thuẫn với giả thiết rằng $$x$$ là điểm tối ưu địa phương, nên bằng phản chứng, bất kỳ điểm tối ưu địa phương $$x$$ nào cũng là tối ưu toàn cục.

## Tổ hợp lồi

Tổ hợp lồi của $$x_1, ..., x_k$$ được định nghĩa là:

> $$x = \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k$$ với $$\theta_1 + \cdots + \theta_k = 1, \theta_i \ge 0$$

Nếu $$D$$ là tập lồi và $$x_1, x_2, ..., x_k \in D$$, thì $$x \in D$$ cũng vậy.


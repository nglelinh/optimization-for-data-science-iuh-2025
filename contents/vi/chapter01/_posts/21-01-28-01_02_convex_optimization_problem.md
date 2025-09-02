---
layout: post
title: 01-02 Convex optimization problem
chapter: '01'
order: 3
owner: Kyeongmin Woo
categories:
- chapter01
lang: vi
---

Bài toán tối ưu lồi (convex optimization problem) là một loại bài toán tối ưu hóa.

>$$\begin{align*} 
>&\min_{x\in D}\ &&f(x) \\
>&\text{subject to} && g_i(x) \le 0,\ i = 1, ..., m \\
>&&& h_j(x) = 0,\ j = 1,\ ..., r
>\end{align*}$$

**Bài toán Tối ưu Lồi dạng chuẩn [3]**

Ở đây, hàm mục tiêu $$f$$ và các hàm ràng buộc bất đẳng thức $$g_i$$ là lồi, và các hàm ràng buộc đẳng thức $$h_j$$ là affine. Hàm affine là hàm tuyến tính cộng với một hằng số:
>$$h_j,\ j = 1, ..., r$$ là affine: $$h_j(x) = a_{j}^T x + b_{j},\ j=1, ..., r$$

Vậy một hàm lồi có nghĩa là gì? Để hiểu điều này, trước tiên chúng ta cần hiểu về tập lồi.

## Tập lồi
Đoạn thẳng nối hai điểm $$x_1$$ và $$x_2$$ được định nghĩa như sau:

>$$x = \theta x_1 + (1 - \theta) x_2$$ với $$0 \le \theta \le 1$$

Cho một tập hợp, nếu đoạn thẳng giữa bất kỳ hai điểm $$x_1$$ và $$x_2$$ nào trong tập đó cũng được chứa trong tập đó, chúng ta gọi nó là tập lồi. Nói cách khác, một tập $$C$$ là lồi nếu:

>$$x_1, x_2 \in C$$, $$0 \le \theta \le 1$$  $$\Rightarrow$$ $$\theta x_1 + (1-\theta)x_2 \in C$$

Ví dụ, trong hình dưới đây, chỉ có hình ngoài cùng bên trái là tập lồi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/Convex_set.png" alt="Convex Set" width="70%">
  <figcaption style="text-align: center;">[Fig1] trái: tập lồi, giữa & phải: tập không lồi [2]</figcaption>
</p>
</figure>

## Hàm lồi
Hàm lồi được định nghĩa như sau:

>$$f: \mathbb{R}^n \rightarrow \mathbb{R} $$ là lồi nếu $$ dom(f) $$ là một tập lồi và,
>
>$$f(\theta x + (1 - \theta)y) \le \theta f(x) + (1-\theta)f(y) $$ với mọi $$ x, y \in dom(f),\ 0 \le \theta \le 1$$

Về mặt hình học, điều này có nghĩa là đối với bất kỳ hai điểm $$(x, f(x))$$ và $$(y, f(y))$$ nào trên đồ thị của $$f$$, đoạn thẳng nối chúng nằm phía trên đồ thị giữa $$x$$ và $$y$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/Convex_function.png" alt="Convex Function" width="70%">
  <figcaption style="text-align: center;">[Fig2] Hàm Lồi [2]</figcaption>
</p>
</figure>

## Mối quan hệ giữa tập lồi và hàm lồi
Có một mối quan hệ chặt chẽ giữa hàm lồi và tập lồi:
> Một hàm $$f$$ là lồi khi và chỉ khi epigraph của nó là một tập lồi.

Epigraph là gì? 'Epi' có nghĩa là 'phía trên', vì vậy epigraph của $$f$$ là tập hợp các điểm phía trên đồ thị của $$f$$. Chính thức, epigraph được định nghĩa như sau:

>$$
\eqalign{
& \text{epigraph của } f: \mathbb{R}^n \rightarrow \mathbb{R}\\
& \text{epi } f = \{(x, t) \in \mathbb{R}^{n+1} \mid x \in \text{ dom } f, f(x) \le t\}
}
$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter01/epigraph.png" alt="Epigraph" width="70%">
  <figcaption style="text-align: center;">[Fig3] Epigraph [2]</figcaption>
</p>
</figure>

Nếu $$f$$ là một hàm lồi, thì $$\text{epi } f$$ luôn là một tập lồi, và ngược lại. Đây là một tính chất quan trọng kết nối các định nghĩa của hàm lồi và tập lồi.

## Hàm lồi và hàm lõm

Một hàm $$f$$ được gọi là lõm (concave) nếu $$-f$$ là lồi. Tương đương, hàm $$f$$ là lõm nếu:

>$$f(\theta x + (1 - \theta)y) \ge \theta f(x) + (1-\theta)f(y) $$ với mọi $$ x, y \in dom(f),\ 0 \le \theta \le 1$$

Về mặt hình học, đối với hàm lõm, đoạn thẳng nối bất kỳ hai điểm nào trên đồ thị sẽ nằm phía dưới đồ thị.

## Tính chất đặc biệt của bài toán tối ưu lồi
Cực tiểu địa phương của một hàm lồi luôn là cực tiểu toàn cục. Đối với các bài toán tối ưu lồi, nghiệm thường dễ tìm hơn so với các bài toán không lồi, bởi vì các hàm lồi có tính chất sau:
> Nếu $$f$$ là lồi và $$x$$ là một điểm tối ưu địa phương (tức là cực tiểu địa phương), thì $$x$$ cũng là một điểm tối ưu toàn cục.

Hãy chứng minh điều này bằng phương pháp phản chứng:

>**Chứng minh bằng phản chứng:**
>
>Giả sử đối với hàm lồi $$f$$, $$x$$ là một điểm tối ưu địa phương nhưng không phải là điểm tối ưu toàn cục. Gọi $$y$$ là một điểm tối ưu toàn cục khả thi, vậy với bất kỳ $$\rho$$ dương nào, $$\|y - x\|_2 > \rho$$ và $$f(y) < f(x)$$. (Vì $$x$$ là tối ưu địa phương, nếu $$\|x - y\|_2 \le \rho$$ thì $$f(x) \le f(y)$$, điều này mâu thuẫn với việc $$y$$ là tối ưu toàn cục.)
>Bây giờ, với $$\theta=\frac{\rho}{2\|y-x\|_2}$$, đặt $$z = \theta y + (1 - \theta) x = x + \theta( y - x)$$. Khi đó:
>
>1. $$z$$ là tổ hợp lồi của hai điểm khả thi $$x, y$$, vậy nó cũng khả thi.
>
>2. $$\|z - x\|_2 = \theta \|y - x\|_2 = \frac{\rho}{2} < \rho$$.
>
>3. $$f(z) \le \theta f(y) + (1 - \theta) f(x) < \theta f(x) + (1 - \theta) f(x) = f(x)$$
>
>Điểm 2 và 3 mâu thuẫn với giả thiết rằng $$x$$ là một điểm tối ưu địa phương, vì vậy bằng phản chứng, bất kỳ điểm tối ưu địa phương $$x$$ nào cũng là tối ưu toàn cục.

## Tổ hợp lồi

Tổ hợp lồi của $$x_1, ..., x_k$$ được định nghĩa như sau:

> $$x = \theta_1 x_1 + \theta_2 x_2 + \cdots + \theta_k x_k$$ với $$\theta_1 + \cdots + \theta_k = 1, \theta_i \ge 0$$

Nếu $$D$$ là một tập lồi và $$x_1, x_2, ..., x_k \in D$$, thì $$x \in D$$.

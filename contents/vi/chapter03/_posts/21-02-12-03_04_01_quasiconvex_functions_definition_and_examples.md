---
layout: post
title: '03-04-01 Hàm giả lồi: định nghĩa và ví dụ'
chapter: '03'
order: 9
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Một hàm $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ là giả lồi nếu tất cả các tập mức dưới $$\{x \mid f(x) \leq \alpha\}$$ đều lồi với mọi $$\alpha \in \mathbb{R}$$.

**Các hàm giả lồi tổng quát hóa các hàm lồi** và xuất hiện thường xuyên trong các bài toán tối ưu.

## Định nghĩa

Một hàm $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ được gọi là **giả lồi** (hoặc **đơn môđ**) nếu miền xác định $$\text{dom}f$$ và tất cả các tập mức dưới $$S_{\alpha}$$ (xem [03-01-03]({% multilang_post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %})) đều lồi.

>$$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ là giả lồi nếu $$\text{dom}f$$ và
>$$S_{\alpha} =\{x \in \text{dom}f \mid f(x) \leq \alpha\}$$ với $$\alpha \in \mathbb{R}$$ đều lồi.

Nếu hàm $$-f$$ là giả lồi, thì $$f$$ được gọi là **giả lõm**.
>$$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ là giả lõm nếu $$\text{dom}f$$ và
>$$S_{\alpha} = \{ x \in \text{dom}f \mid f(x) \geq \alpha \}$$ với $$\alpha \in \mathbb{R}$$ đều lồi.

Khi $$f$$ vừa giả lồi vừa giả lõm, nó được gọi là **giả tuyến tính**, và miền xác định của hàm và tất cả các tập mức $$\{x \mid f(x)=\alpha\}$$ đều lồi. Hình dưới đây cho thấy một ví dụ về hàm giả lồi.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig3.9_quasiconvex_ftn_cAsoUpr.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] hàm giả lồi trên R [1]</figcaption>
</p>
</figure>


Với $$\alpha$$, tập mức dưới $$\alpha$$ là $$S_{\alpha}$$ lồi, cụ thể là khoảng $$[a,b]$$. Tập mức dưới $$\beta$$ là $$S_{\beta}$$ là khoảng $$(-\infty,c]$$. **Các hàm lồi có các tập mức dưới lồi và là giả lồi, nhưng điều ngược lại không đúng.**
> $$f$$ : lồi $$\Longrightarrow$$ $$f$$ : giả lồi


<br>
## Ví dụ

Hãy xem xét các ví dụ khác nhau về hàm giả lồi.

### Logarithm
$$\log x$$ trên $$\mathbb{R}_{++}$$ là giả lồi. (Nó cũng là giả lõm, nên nó có tính chất giả tuyến tính.)
> $$\log x$$ trên $$\mathbb{R}_{++}$$

### Hàm lấy phần nguyên trên
Hàm lấy phần nguyên trên là giả lồi (và cũng là giả lõm).
>$$\text{ceil}(x) = \inf \{z \in \mathbb{Z} \mid z \geq x\}$$

### Độ dài của vector
Nếu chúng ta định nghĩa độ dài của $$x \in \mathbb{R}^n$$ là chỉ số lớn nhất của các thành phần khác không,
>$$f(x) = \max\{i \mid x_i \neq 0\}$$

Điều này thỏa mãn
>$$f(x) \leq \alpha \iff x_i = 0$$ với $$i = \lfloor\alpha\rfloor + 1,...,n$$ trên $$\mathbb{R}^n$$

điều này định nghĩa một không gian con, nên nó là giả lồi.
(Lưu ý: Một không gian con đóng dưới phép cộng và nhân vô hướng. Bất kỳ không gian con nào của $$\mathbb{R}^n$$ cũng là một tập lồi.)

### Hàm tuyến tính-phân thức
Dưới các điều kiện sau, hàm $$f$$ vừa giả lồi vừa giả lõm, tức là giả tuyến tính.
>$$f(x) = \frac{a^Tx+b}{c^Tx+d}$$ với $$\text{dom}f =\{x \mid c^Tx + d > 0\}$$

### Hàm tỉ lệ khoảng cách
Với $$a, b \in \mathbb{R}^n$$, khi hàm $$f$$ được định nghĩa như sau, biểu thị tỉ lệ của khoảng cách Euclidean từ $$x$$ đến $$a$$ và từ $$x$$ đến $$b$$,
$$f$$ là giả lồi trên nửa không gian $$\{x \mid \|x - a\|_2 \leq \|x - b\|_2 \}$$.

> $$f(x) = \frac{\|x - a\|_2}{\|x - b\|_2}$$

Dưới điều kiện $$\alpha \leq 1$$, điều này trở thành một tập lồi dưới dạng một quả cầu Euclidean, nên $$f$$ là giả lồi.

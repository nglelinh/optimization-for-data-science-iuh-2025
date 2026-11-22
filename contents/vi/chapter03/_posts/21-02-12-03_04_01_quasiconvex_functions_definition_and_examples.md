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

Một hàm $$f:\mathbb{R}^n \rightarrow \mathbb{R}$$ được gọi là giả lồi nếu miền xác định và mọi tập mức dưới $$\{x \mid f(x) \leq \alpha\}$$ của nó đều là tập lồi với mọi $$\alpha \in \mathbb{R}$$. **Hàm giả lồi là sự tổng quát hóa của hàm lồi** và xuất hiện thường xuyên trong các bài toán tối ưu.

## Định nghĩa

Một hàm $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ được gọi là **giả lồi** (hoặc **đơn đỉnh — unimodal**) nếu miền xác định $$\text{dom}f$$ và tất cả các tập mức dưới $$S_{\alpha}$$ (xem bài [03-01-03]({% multilang_post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %})) đều là tập lồi:

>$$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ là giả lồi nếu $$\text{dom}f$$ và
>$$S_{\alpha} =\{x \in \text{dom}f \mid f(x) \leq \alpha\}$$ với mọi $$\alpha \in \mathbb{R}$$ đều lồi.

Nếu $$-f$$ là hàm giả lồi thì $$f$$ được gọi là **giả lõm**:
>$$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ là giả lõm nếu $$\text{dom}f$$ và
>$$S_{\alpha} = \{ x \in \text{dom}f \mid f(x) \geq \alpha \}$$ với mọi $$\alpha \in \mathbb{R}$$ đều lồi.

Hàm $$f$$ vừa giả lồi vừa giả lõm được gọi là **giả tuyến tính**; khi đó miền xác định và mọi tập mức $$\{x \in \text{dom}f \mid f(x)=\alpha\}$$ đều là tập lồi. Hình dưới đây minh họa một hàm giả lồi trên $$\mathbb{R}$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig3.9_quasiconvex_ftn_cAsoUpr.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] hàm giả lồi trên R [1]</figcaption>
</p>
</figure>

Trong hình trên, tập mức dưới $$S_{\alpha}$$ là đoạn $$[a,b]$$ và tập mức dưới $$S_{\beta}$$ là khoảng $$(-\infty,c]$$ — cả hai đều là tập lồi. **Mọi hàm lồi đều có các tập mức dưới lồi nên đều là hàm giả lồi, nhưng chiều ngược lại không đúng:**
> $$f$$ lồi $$\Longrightarrow$$ $$f$$ giả lồi

<br>

## Ví dụ

Dưới đây là một số ví dụ quen thuộc về hàm giả lồi.

### Logarithm
Hàm $$\log x$$ trên $$\mathbb{R}_{++}$$ là hàm giả lồi (đồng thời là hàm giả lõm, nên là hàm giả tuyến tính):
> $$\log x$$ trên $$\mathbb{R}_{++}$$

### Hàm làm tròn lên (ceil)
Hàm lấy phần nguyên trên vừa giả lồi vừa giả lõm:
>$$\text{ceil}(x) = \inf \{z \in \mathbb{Z} \mid z \geq x\}$$

### Độ dài của vector
Định nghĩa độ dài của vector $$x \in \mathbb{R}^n$$ là chỉ số lớn nhất của các thành phần khác không:
>$$f(x) = \max\{i \mid x_i \neq 0\}$$

Với mọi $$\alpha \ge 0$$, tập mức dưới thỏa mãn:
>$$f(x) \leq \alpha \iff x_i = 0$$ với mọi $$i = \lfloor\alpha\rfloor + 1,\dots,n$$

Đây là một không gian con tuyến tính của $$\mathbb{R}^n$$ (nên là tập lồi), do đó $$f$$ là hàm giả lồi.

### Hàm tuyến tính-phân thức
Hàm tuyến tính-phân thức sau đây vừa giả lồi vừa giả lõm, tức là hàm giả tuyến tính:
>$$f(x) = \frac{a^Tx+b}{c^Tx+d}$$ với $$\text{dom}f =\{x \mid c^Tx + d > 0\}$$

### Hàm tỉ số khoảng cách
Với hai điểm cố định $$a, b \in \mathbb{R}^n$$, xét hàm tỉ số giữa khoảng cách Euclidean từ $$x$$ đến $$a$$ và từ $$x$$ đến $$b$$:

> $$f(x) = \frac{\|x - a\|_2}{\|x - b\|_2}$$

Hàm $$f$$ là giả lồi trên nửa không gian $$\{x \mid \|x - a\|_2 \leq \|x - b\|_2 \}$$. Thật vậy, với mọi $$\alpha \leq 1$$, tập mức dưới $$\{x \mid \|x - a\|_2 \le \alpha \|x - b\|_2\}$$ là một hình cầu Euclidean (hoặc một nửa không gian khi $$\alpha = 1$$), nên là tập lồi.

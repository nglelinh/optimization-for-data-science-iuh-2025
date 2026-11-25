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

Khi nhắc đến "lồi", ta thường hình dung một chiếc bát uốn cong lên trên. Thế nhưng một hàm cong xuống như $$\log x$$, một hàm bậc thang rời rạc như $$\lceil x \rceil$$, hay một phân thức tuyến tính $$\frac{a^T x + b}{c^T x + d}$$ đều có chung một cấu trúc hình học quý giá: nếu bạn cắt ngang đồ thị ở bất kỳ độ cao $$\alpha$$ nào, phần nằm dưới nhát cắt luôn tạo thành một **tập lồi** không bị tách thành nhiều mảnh!

Bài học này đi sâu vào định nghĩa chính thức của hàm giả lồi, hàm giả lõm, hàm giả tuyến tính và phân tích từng ví dụ kinh điển.

## Kiến thức cần nhớ: Bốn họ ví dụ mẫu của Hàm giả lồi

- **Mọi hàm đơn điệu trên $$\mathbb{R}$$:** Như $$\log x$$ (vừa giả lồi vừa giả lõm $$\implies$$ **giả tuyến tính / quasilinear**), $$x^3$$ hay hàm làm tròn lên $$\lceil x \rceil$$ (thậm chí không liên tục nhưng tập mức dưới vẫn là nửa khoảng $$(-\infty, \lfloor \alpha \rfloor]$$ lồi!).
- **Hàm phân thức tuyến tính:** $$f(x) = \frac{a^T x + b}{c^T x + d}$$ trên miền $$c^T x + d > 0$$ là hàm **giả tuyến tính** — nền tảng của Quy hoạch phân thức tuyến tính (Linear-Fractional Programming, ví dụ tối ưu hóa tỷ số lợi nhuận trên chi phí).
- **Tỷ số khoảng cách và bậc của đa thức:** Khoảng cách tỉ đối $$\|x - a\|_2 / \|x - b\|_2$$ trên nửa không gian gần $$a$$ hơn, hay độ dài (bậc) của tín hiệu rời rạc trong xử lý tín hiệu số.
- **Phân biệt giả lồi và giả lõm:** $$f$$ giả lõm $$\iff -f$$ giả lồi $$\iff$$ mọi tập mức **trên** $$\{x : f(x) \ge \alpha\}$$ đều là tập lồi.

### Giải thích: Kiểm chứng tập mức dưới của hàm phân thức tuyến tính $$f(x) = \frac{2x + 1}{x + 1}$$

Xét $$f(x) = \frac{2x + 1}{x + 1}$$ trên miền lồi $$x > -1$$:

1. **Giải bất đẳng thức tập mức dưới $$f(x) \le \alpha$$:**
   Vì mẫu số $$x + 1 > 0$$, ta được phép nhân chéo không đổi chiều dấu:
   $$\frac{2x + 1}{x + 1} \le \alpha \iff 2x + 1 \le \alpha(x + 1) \iff (2 - \alpha)x \le \alpha - 1.$$
   Đây là một **bất đẳng thức tuyến tính** theo $$x$$, nên tập nghiệm luôn là một nửa không gian (giao với $$x > -1$$ là một khoảng lồi!).
2. **Thử giá trị cụ thể $$\alpha = 1.5$$:**
   $$(2 - 1.5)x \le 1.5 - 1 \iff 0.5 x \le 0.5 \iff x \le 1 \implies S_{1.5} = (-1, 1] \text{ (tập lồi!)}.$$
3. **Tại sao $$f$$ không phải hàm lồi?** Tính đạo hàm:
   $$f'(x) = \frac{1}{(x + 1)^2} > 0, \qquad f''(x) = -\frac{2}{(x + 1)^3} < 0 \quad (\forall x > -1).$$
   Hàm thực chất **lõm chặt**, nhưng vì đơn điệu tăng nên vẫn là hàm **giả lồi** (thậm chí giả tuyến tính)!

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

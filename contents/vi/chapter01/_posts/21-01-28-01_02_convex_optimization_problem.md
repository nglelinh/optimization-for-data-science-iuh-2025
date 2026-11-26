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

Tại sao một kỹ sư khi gặp một bài toán mới thường cố gắng biến đổi nó về **dạng lồi** bằng mọi giá? Bởi vì ngay khoảnh khắc bài toán khoác lên chiếc áo lồi — hàm mục tiêu lồi, ràng buộc bất đẳng thức lồi và ràng buộc đẳng thức affine — ta lập tức nhận được "tấm thẻ bảo hiểm toàn cục": bất kỳ cực tiểu địa phương nào mà thuật toán tìm thấy chắc chắn là **cực tiểu toàn cục tốt nhất có thể**. Không cần đoán mò hàng trăm điểm khởi tạo ngẫu nhiên, cũng không sợ bỏ lỡ nghiệm tốt hơn ở một góc khuất nào đó của không gian.

Bài học này giới thiệu trọn vẹn định nghĩa chuẩn của bài toán tối ưu hóa lồi, cầu nối hình học qua epigraph và chứng minh kinh điển cho tính chất "địa phương = toàn cục".

## Kiến thức cần nhớ: Kiến trúc của một bài toán tối ưu hóa lồi

- **Tập lồi (Convex Set):** Chứa trọn đoạn thẳng nối hai điểm bất kỳ trong tập. Trong bài toán lồi, miền khả thi luôn là tập lồi (giao của các tập mức dưới của $$g_i$$ và các siêu phẳng $$h_j(x) = 0$$).
- **Hàm lồi và Epigraph:** Hàm $$f$$ lồi khi và chỉ khi vùng nằm trên đồ thị của nó ($$\operatorname{epi} f$$) là một tập lồi. Đây là cây cầu nối giải tích (hàm số) với hình học (tập hợp).
- **Vì sao ràng buộc đẳng thức $$h_j(x) = 0$$ bắt buộc phải là affine?** Nếu viết $$h(x) = 0$$ thành cặp $$h(x) \le 0$$ và $$-h(x) \le 0$$, thì cả $$h$$ và $$-h$$ cùng phải lồi — điều này chỉ xảy ra khi $$h$$ là hàm affine $$a^T x + b$$! (Ví dụ $$x_1^2 + x_2^2 = 1$$ là đường tròn rỗng ruột, không phải tập lồi.)
- **Tính chất toàn cục (Local = Global):** Chứng minh bằng phản chứng chỉ dùng đúng định nghĩa tập lồi và bất đẳng thức hàm lồi cho tổ hợp $$\theta y + (1-\theta)x$$.

### Giải thích: Kiểm tra tính lồi và giải tay một bài toán lồi có cả 2 loại ràng buộc

Xét bài toán:
$$\min_{x_1, x_2} f(x_1, x_2) = x_1^2 + 2x_2^2 \quad \text{với điều kiện} \quad g_1(x) = 3 - x_1 - x_2 \le 0,\quad h_1(x) = x_1 - x_2 - 1 = 0.$$

1. **Kiểm tra cấu trúc lồi:**
   - Hàm mục tiêu $$f(x) = x_1^2 + 2x_2^2$$ có Hessian $$\operatorname{diag}(2, 4) \succ 0$$ nên lồi chặt.
   - Ràng buộc bất đẳng thức $$g_1(x) = 3 - x_1 - x_2$$ là hàm affine (vừa lồi vừa lõm).
   - Ràng buộc đẳng thức $$h_1(x) = x_1 - x_2 - 1$$ là hàm affine.
   Vậy đây là **bài toán tối ưu hóa lồi chuẩn**.
2. **Khử ràng buộc đẳng thức:** Từ $$x_1 - x_2 - 1 = 0 \implies x_1 = x_2 + 1$$. Thay vào bất đẳng thức:
   $$3 - (x_2 + 1) - x_2 \le 0 \iff 2 - 2x_2 \le 0 \iff x_2 \ge 1.$$
3. **Cực tiểu hóa hàm một biến thu gọn:**
   $$\phi(x_2) = (x_2 + 1)^2 + 2x_2^2 = 3x_2^2 + 2x_2 + 1, \qquad x_2 \ge 1.$$
   Đạo hàm $$\phi'(x_2) = 6x_2 + 2 > 0$$ với mọi $$x_2 \ge 1$$, nên $$\phi$$ tăng nghiêm ngặt trên $$[1, \infty)$$.
4. **Nghiệm tối ưu toàn cục:** Đạt tại $$x_2^* = 1 \implies x_1^* = 2$$, giá trị tối ưu $$p^* = 2^2 + 2(1)^2 = 6$$. Kiểm chứng bất đẳng thức lồi giữa $$x^* = (2, 1)$$ và một điểm khả thi khác $$y = (3, 2)$$ ($$f(y) = 17$$): trung điểm $$z = (2.5, 1.5)$$ thỏa ràng buộc và có $$f(z) = 6.25 + 4.5 = 10.75 \le \frac{6 + 17}{2} = 11.5$$.

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

### Video ngắn: Lồi vs. Không lồi & Kiến trúc Bài toán Lồi

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:8px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/convex-vs-nonconvex_vi.mp4"></video>
</div>

Video dài khoảng 29 giây (có thuyết minh tiếng Việt): ranh giới thực sự trong tối ưu hóa theo Boyd–Vandenberghe và cấu trúc chuẩn tắc của bài toán lồi.

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

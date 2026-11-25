---
layout: post
title: 03-04-02 Các tính chất cơ bản của hàm giả lồi
chapter: '03'
order: 10
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Bất đẳng thức Jensen cho hàm lồi yêu cầu giá trị tại trung điểm không vượt quá *trung bình có trọng số* của hai đầu mút: $$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$$. Với hàm giả lồi, yêu cầu đó được nới lỏng vừa đủ: giá trị tại điểm nằm giữa chỉ cần không vượt quá **giá trị lớn hơn** trong hai đầu mút, tức $$f(\theta x + (1-\theta)y) \le \max\{f(x), f(y)\}$$!

Chỉ một thay đổi nhỏ từ "trung bình" sang "$$\max$$" nhưng vẫn đủ sức loại bỏ mọi đỉnh nhô lên chắn giữa hai điểm thấp — giải thích vì sao hàm giả lồi trên $$\mathbb{R}$$ không bao giờ có hai thung lũng tách rời.

## Bản đồ kiến thức nền: Ba tính chất cơ bản của Hàm giả lồi

- **Bất đẳng thức Jensen biến đổi:** $$f$$ giả lồi $$\iff \operatorname{dom} f$$ lồi và $$f(\theta x + (1-\theta)y) \le \max\{f(x), f(y)\}$$ với mọi $$x, y \in \operatorname{dom} f,\ \theta \in [0, 1]$$.
- **Đặc trưng hàm giả lồi liên tục trên $$\mathbb{R}$$:** Một hàm liên tục một biến là giả lồi khi và chỉ khi nó thuộc đúng 1 trong 3 dạng: (1) không giảm, (2) không tăng, hoặc (3) tồn tại điểm mốc $$c$$ sao cho không tăng với $$x \le c$$ và không giảm với $$x \ge c$$.
- **Cảnh báo về điểm dừng "bằng phẳng":** Khác với hàm lồi, một hàm giả lồi có thể có **cực tiểu địa phương không phải cực tiểu toàn cục** nếu có một đoạn bằng phẳng ngang (plateau) — ví dụ hàm bậc thang hoặc $$f(x) = 0$$ trên $$[1, 2]$$ nhưng giảm xuống $$-1$$ ở $$x = 0$$!

### Khung giải thích (nên đọc chậm): Kiểm chứng Jensen biến đổi trên $$f(x) = \ln x$$ ($$x > 0$$)

Xét $$f(x) = \ln x$$ trên miền $$x > 0$$ với hai điểm $$x = 1$$ và $$y = e^2 \approx 7.389$$, chọn $$\theta = 0.5$$:

1. **Tính giá trị tại hai đầu mút và trung điểm:**
   - $$f(1) = \ln 1 = 0$$; $$f(e^2) = \ln(e^2) = 2$$.
   - Trung điểm: $$z = \frac{1 + 7.389}{2} = 4.1945 \implies f(z) = \ln(4.1945) \approx 1.434$$.
2. **So sánh với Jensen thường (cho hàm lồi):**
   - Trung bình hai đầu mút: $$0.5 f(1) + 0.5 f(e^2) = 0.5(0) + 0.5(2) = 1.0$$.
   - Ta thấy $$f(z) \approx 1.434 > 1.0 \implies$$ **vi phạm** Jensen thường (vì $$\ln x$$ lõm, không lồi).
3. **So sánh với Jensen biến đổi (cho hàm giả lồi):**
   - Giá trị lớn hơn của hai đầu mút: $$\max\{f(1), f(e^2)\} = \max\{0, 2\} = 2.0$$.
   - Ta thấy $$f(z) \approx 1.434 \le 2.0 \implies$$ **thỏa mãn** Jensen biến đổi!

---

Phần này trình bày các tính chất cơ bản của hàm giả lồi, bao gồm bất đẳng thức Jensen biến đổi và đặc trưng của hàm giả lồi liên tục một biến.

## Bất đẳng thức Jensen biến đổi

Hàm $$f$$ là giả lồi khi và chỉ khi miền xác định $$\text{dom}f$$ lồi và thỏa mãn bất đẳng thức Jensen biến đổi sau:
>$$f(\theta x + (1 - \theta)y) \leq \max\{f(x), f(y)\}$$ với mọi $$x, y \in \text{dom}f$$, $$0 \leq \theta \leq 1$$

Nói cách khác, dọc theo đoạn thẳng nối hai điểm $$x$$ và $$y$$, giá trị của hàm giả lồi $$f$$ không bao giờ vượt quá giá trị lớn hơn trong hai giá trị $$f(x)$$ và $$f(y)$$.
<br><br>

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.10_quasiconvex_function_on_R_4uChnEm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1]</figcaption>
</p>
</figure>
**Hàm giả lồi trên $$\mathbb{R}$$: giá trị của $$f$$ giữa $$x$$ và $$y$$ luôn nhỏ hơn hoặc bằng $$\max\{f(x), f(y)\}$$.**

<br>

## Hàm giả lồi trên $$\mathbb{R}$$

Một hàm liên tục $$f : \mathbb{R} \mapsto \mathbb{R}$$ là giả lồi khi và chỉ khi nó thỏa mãn ít nhất một trong ba điều kiện sau:

* $$f$$ không giảm trên $$\text{dom}f$$.
* $$f$$ không tăng trên $$\text{dom}f$$.
* Tồn tại một điểm $$c \in \text{dom} f$$ sao cho $$f$$ không tăng trên $$\{t \in \text{dom}f \mid t \leq c\}$$ và không giảm trên $$\{t \in \text{dom}f \mid t \geq c\}$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/Fig.3.11_quasiconvex_function_on_R_2_PPQpNiU.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig2]</figcaption>
</p>
</figure>
**Hàm giả lồi trên $$\mathbb{R}$$: không tăng với $$t \leq c$$ và không giảm với $$t \geq c$$ ($$t \in \text{dom} f$$).**

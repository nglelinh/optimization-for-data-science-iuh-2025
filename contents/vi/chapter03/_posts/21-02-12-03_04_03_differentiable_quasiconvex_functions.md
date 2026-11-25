---
layout: post
title: 03-04-03 Hàm giả lồi khả vi
chapter: '03'
order: 11
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Với hàm lồi khả vi, ma trận Hessian phải bán xác định dương theo **mọi hướng** $$v \in \mathbb{R}^n$$. Còn với hàm giả lồi khả vi, điều kiện đó được nới lỏng một cách đầy tinh tế: ta chỉ cần đường cong không uốn xuống theo những hướng **vuông góc với gradient** (tức các hướng nằm dọc theo siêu mặt mức $$f(x) = c$$)! Nhờ trực giác hình học này, điều kiện bậc nhất và bậc hai của hàm giả lồi trở nên vô cùng dễ hiểu và dễ kiểm tra.

Bài học này thiết lập hai tiêu chuẩn vi phân cốt lõi để nhận diện hàm giả lồi khả vi.

## Bản đồ kiến thức nền: Hình học vi phân của Hàm giả lồi

- **Điều kiện bậc nhất:** Hàm khả vi $$f$$ trên miền lồi là giả lồi khi và chỉ khi:
  $$f(y) \le f(x) \implies \nabla f(x)^T (y - x) \le 0.$$
  *Ý nghĩa hình học:* Tại mọi điểm $$x$$ có $$\nabla f(x) \ne 0$$, vector $$\nabla f(x)$$ định nghĩa một **siêu phẳng hỗ trợ** cho tập mức dưới $$\{y : f(y) \le f(x)\}$$!
- **Sự khác biệt tinh tế với hàm lồi:** Với hàm giả lồi, $$\nabla f(x^*) = 0$$ **không đủ** để suy ra $$x^*$$ là cực tiểu toàn cục (ví dụ $$f(x) = x^3$$ có $$f'(0) = 0$$ nhưng $$0$$ là điểm uốn, không phải cực tiểu!).
- **Điều kiện bậc hai (trên siêu phẳng tiếp xúc mức):** Nếu $$f$$ giả lồi khả vi cấp 2 thì với mọi $$x$$ và mọi vector $$y$$ trực giao với gradient ($$\nabla f(x)^T y = 0$$), ta phải có $$y^T \nabla^2 f(x) y \ge 0$$ — Hessian chỉ có thể có tối đa **một** giá trị riêng âm (dọc theo phương gradient)!

### Khung giải thích (nên đọc chậm): Kiểm tra điều kiện bậc nhất trên $$f(x) = x^3$$ và bác bỏ $$g(x) = -x^2$$

Áp dụng trực tiếp tiêu chuẩn $$f(y) \le f(x) \implies f'(x)(y - x) \le 0$$:

1. **Hàm giả lồi $$f(x) = x^3$$ ($$f'(x) = 3x^2 \ge 0$$):**
   - Chọn $$x = 1,\ y = -1$$: ta có $$f(-1) = -1 \le f(1) = 1$$.
   - Kiểm tra vế phải: $$f'(1)(y - x) = 3(1)^2 (-1 - 1) = -6 \le 0$$ (thỏa mãn!).
   - Tổng quát, $$y^3 \le x^3 \iff y - x \le 0$$, nhân thêm $$3x^2 \ge 0$$ luôn cho $$3x^2(y - x) \le 0$$ $$\implies x^3$$ chắc chắn giả lồi!
2. **Hàm KHÔNG giả lồi $$g(x) = -x^2$$ ($$g'(x) = -2x$$):**
   - Chọn $$x = 1,\ y = -2$$: ta có $$g(-2) = -4 \le g(1) = -1$$ (vế trái đúng).
   - Kiểm tra vế phải: $$g'(1)(y - x) = (-2)(-2 - 1) = (-2)(-3) = +6 > 0$$!
   Vế phải dương mâu thuẫn với điều kiện bậc nhất $$\implies g(x) = -x^2$$ **không phải** hàm giả lồi (quả thật tập mức dưới $$\{-x^2 \le -1\} = (-\infty, -1] \cup [1, \infty)$$ bị tách làm hai mảnh rời nhau!).

---

Phần này trình bày các điều kiện đặc trưng bậc nhất và bậc hai cho hàm giả lồi khả vi.

## Điều kiện bậc nhất

Cho hàm khả vi $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ có miền xác định $$\text{dom}f$$ lồi. Khi đó $$f$$ là hàm giả lồi khi và chỉ khi:
>$$f$$ là giả lồi $$\iff$$ $$f(y) \leq f(x) \Rightarrow \nabla f(x)^T(y-x) \leq 0$$ với mọi $$x, y \in \text{dom}f$$

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/3.12_Three_level_curves_OV6vtPq.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1]</figcaption>
</p>
</figure>
**Ba đường mức của một hàm giả lồi $$f$$: gradient $$\nabla f(x)$$ là vector pháp tuyến của một siêu phẳng hỗ trợ tập mức dưới $$\{z \mid f(z) \leq f(x)\}$$ tại $$x$$.**

Điều kiện bậc nhất của hàm giả lồi có dạng khá giống đặc trưng bậc nhất của hàm lồi (xem bài [03-01-03]({% multilang_post_url contents/chapter03/21-02-12-03_01_03_key_properties_of_convex_functions %})), nhưng vẫn có khác biệt quan trọng: với hàm lồi, $$\nabla f(x) = 0$$ suy ra $$x$$ là điểm cực tiểu toàn cục, còn với hàm giả lồi thì điều này không nhất thiết đúng.

<br>

## Điều kiện bậc hai

Khi $$f$$ khả vi hai lần và là hàm giả lồi, với mọi $$x \in \text{dom}f$$ và mọi $$y \in \mathbb{R}^n$$ ta có:
>$$f$$ là giả lồi, $$y^T \nabla f(x) = 0 \Longrightarrow y^T \nabla^2 f(x)y \geq 0$$ với mọi $$x \in \text{dom} f$$, mọi $$y \in \mathbb{R}^n$$ <br>

Trong trường hợp một biến trên $$\mathbb{R}$$, điều kiện này rút gọn thành:

>$$f$$ là giả lồi, $$f'(x) = 0 \Rightarrow f''(x) \geq 0$$

Nghĩa là tại mọi điểm dừng (đạo hàm bậc nhất bằng 0), đạo hàm bậc hai phải không âm. Trong không gian $$\mathbb{R}^n$$, điều kiện bậc hai kéo theo hai hệ quả sau:

1. Nếu $$\nabla f(x) = 0$$ thì ma trận Hessian phải nửa xác định dương: $$\nabla^2f(x) \succeq 0$$.
2. Nếu $$\nabla f(x) \neq 0$$ thì $$y^T \nabla f(x) = 0 \Rightarrow y^T \nabla^2 f(x)y \geq 0$$, tức là ma trận Hessian $$\nabla^2 f(x)$$ nửa xác định dương trên không gian con $$(n-1)$$ chiều $$\nabla f(x)^\perp$$ (tập các vector vuông góc với $$\nabla f(x)$$).

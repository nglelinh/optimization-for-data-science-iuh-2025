---
layout: post
title: 07-01 Gradient dưới (Subgradient)
chapter: '07'
order: 2
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
lesson_type: required
---

Trong giải tích cổ điển, định nghĩa đạo hàm dựa trên giới hạn cục bộ $$\lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$: hễ độ dốc bên trái khác độ dốc bên phải, giới hạn đứt gãy và ta "chịu thua". Nhưng với hàm lồi, ta lại nhớ đến một tính chất toàn cục tuyệt đẹp từ Chương 03: tiếp tuyến của hàm lồi khả vi luôn nằm **hoàn toàn bên dưới** đồ thị hàm số: $$f(y) \ge f(x) + \nabla f(x)^T(y - x)$$.

Nhà toán học R. Tyrrell Rockafellar và các bậc tiền bối đã lật ngược tính chất ấy thành chính **định nghĩa** của **Gradient dưới (Subgradient)**: không cần giới hạn, không cần khả vi — bất kỳ vector $$g$$ nào tạo ra một mặt phẳng đỡ toàn cục nằm dưới đồ thị $$f$$ đi qua $$(x, f(x))$$ đều xứng đáng được gọi là một subgradient!

## Kiến thức cần nhớ: Bốn góc nhìn cốt lõi về Subgradient

Để tính thành thạo subgradient trên mọi hàm không trơn (từ $$\ell_1$$, $$\ell_2$$ đến hàm cực đại), hãy nắm bốn trụ cột:

- **Định nghĩa toàn cục bằng bất đẳng thức tuyến tính:** $$g \in \mathbb{R}^n$$ là subgradient của $$f$$ tại $$x$$ nếu $$f(y) \ge f(x) + g^T(y - x)$$ với mọi $$y \in \mathbb{R}^n$$. Dù định nghĩa này có thể viết cho mọi hàm, với hàm **lồi** trên phần trong miền xác định, subgradient *luôn luôn tồn tại*!
- **Trùng khớp hoàn toàn tại điểm khả vi:** Nếu $$f$$ lồi và khả vi tại $$x$$, thì subgradient tồn tại duy nhất và bằng chính $$\nabla f(x)$$.
- **Bốn ví dụ khuôn mẫu bắt buộc nhớ:**
  1. Giá trị tuyệt đối $$|x|$$: $$g = \operatorname{sign}(x)$$ khi $$x \neq 0$$, và $$g \in [-1, 1]$$ khi $$x = 0$$.
  2. Chuẩn Euclidean $$\|x\|_2$$: $$g = x / \|x\|_2$$ khi $$x \neq 0$$, và $$\|g\|_2 \le 1$$ khi $$x = 0$$.
  3. Chuẩn $$\ell_1$$ $$\|x\|_1$$: từng tọa độ $$g_i = \operatorname{sign}(x_i)$$ nếu $$x_i \neq 0$$, và $$g_i \in [-1, 1]$$ nếu $$x_i = 0$$.
  4. Hàm cực đại $$f(x) = \max(f_1(x), f_2(x))$$: tại điểm giao $$f_1(x) = f_2(x)$$, mọi tổ hợp lồi của $$\nabla f_1(x)$$ và $$\nabla f_2(x)$$ đều là subgradient!
- **Khác biệt lớn với Gradient — Không phải hướng giảm!** Một cú sốc thú vị: $$-g$$ với $$g \in \partial f(x)$$ **không nhất thiết** là hướng làm giảm $$f(x)$$ (chỉ đảm bảo làm giảm *khoảng cách tới $$x^\star$$* với bước đủ nhỏ!).

### Giải thích: Tính tay tập subgradient của hàm cực đại $$f(x) = \max(2x - 1,\; -x + 2)$$

Xét hàm lồi từng mảnh $$f(x) = \max(f_1(x), f_2(x))$$ với $$f_1(x) = 2x - 1$$ (độ dốc $$2$$) và $$f_2(x) = -x + 2$$ (độ dốc $$-1$$):

1. **Bước 1 — Tìm điểm gãy khúc (nơi hai đường thẳng cắt nhau):**
   $$2x - 1 = -x + 2 \iff 3x = 3 \implies x = 1.$$
   Tại $$x = 1$$, ta có $$f(1) = 1$$.
2. **Bước 2 — Tính subgradient tại 3 vùng:**
   - Khi $$x > 1$$: $$f(x) = 2x - 1$$ khả vi $$\implies$$ subgradient duy nhất $$g = 2$$.
   - Khi $$x < 1$$: $$f(x) = -x + 2$$ khả vi $$\implies$$ subgradient duy nhất $$g = -1$$.
   - Tại điểm gãy khúc $$x = 1$$: mọi tổ hợp lồi $$\theta(2) + (1-\theta)(-1)$$ với $$\theta \in [0, 1]$$, tức mọi $$g \in [-1, 2]$$!
3. **Bước 3 — Kiểm chứng bằng số với $$g = 0.5 \in [-1, 2]$$ tại $$x = 1$$:**
   Đường thẳng đỡ là $$L(y) = f(1) + 0.5(y - 1) = 1 + 0.5(y - 1)$$.
   - Thử $$y = 3$$: $$f(3) = \max(5, -1) = 5 \ge L(3) = 2$$ (đúng!).
   - Thử $$y = -1$$: $$f(-1) = \max(-3, 3) = 3 \ge L(-1) = 0$$ (đúng!).
   - Thử $$g = 0 \in [-1, 2]$$: vì $$0$$ nằm trong $$[-1, 2]$$, ta biết ngay $$x^\star = 1$$ là điểm cực tiểu toàn cục với $$f^\star = 1$$!

---

# Gradient dưới (Subgradient)

Đối với một hàm lồi $$f:\mathbb{R}^n \to \mathbb{R}$$, gradient dưới (subgradient) của $$f$$ tại điểm $$x$$ là bất kỳ vector $$g \in \mathbb{R}^n$$ nào thỏa mãn:

> $$
\begin{equation}\label{subgradient}
f(y) \geq f(x) + g^T(y-x), \text{ với mọi } y
\end{equation}
$$

Từ định nghĩa trên, ta có một số nhận xét cơ bản về gradient dưới:

- Đây là sự tổng quát hóa của gradient cho các hàm lồi trong trường hợp hàm không khả vi.
- Với mọi hàm lồi, gradient dưới luôn tồn tại. Nếu $$f$$ khả vi tại $$x$$, thì $$\nabla f(x)$$ là gradient dưới duy nhất tại điểm đó.
- Với hàm không lồi, gradient dưới vẫn có thể được định nghĩa theo cùng bất đẳng thức trên, nhưng có thể không tồn tại tùy thuộc vào từng hàm cụ thể.

Dưới đây là một số ví dụ về gradient dưới của các hàm thường gặp.

### Ví dụ 1

<center>
$$f:\mathbb{R} \to \mathbb{R}, f(x) =  \vert x \vert $$
</center>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-1.png" alt="Subgradient1" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Hình 1] Gradient dưới của } f(x)= \vert x \vert \text{ [3]}$$</figcaption>
</figure>

- Với $$x \neq 0$$, bất đẳng thức $$ \vert y \vert \geq \vert x \vert + g^T(y-x)$$ phải đúng với mọi $$y$$, tương đương với $$ \vert y \vert - g^Ty \geq \vert x \vert - g^Tx $$. Khi $$ \vert x \vert - g^Tx = 0 $$, tức là $$g=\text{sign}(x)$$, bất đẳng thức này luôn thỏa mãn với mọi $$y$$. Do đó, $$g=\text{sign}(x)$$ ([Wikipedia: Hàm dấu](https://en.wikipedia.org/wiki/Sign_function)).
- Với $$x=0$$, điều kiện trở thành $$ \vert y \vert \geq g^Ty $$ với mọi $$y$$, suy ra $$g \in [-1,1]$$.

### Ví dụ 2

<center>
$$f:\mathbb{R}^n \to \mathbb{R}, f(x) =  \| x \|_1$$ 
</center>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-3.png" alt="Subgradient2" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Hình 2] Gradient dưới của }f(x)= \| x \|_1\text{ [3]}$$</figcaption>
</figure>

Tại điểm $$x=(x_1,x_2,\dots,x_n)$$:

- Với $$x_i \neq 0, i \in \{1,2,\dots,n\}$$, vì hàm khả vi theo tọa độ $$x_i$$, ta có $$g_i=\text{sign}(x_i)$$.
- Với $$x_i=0, i \in \{1,2,\dots,n\}$$, ta có $$g_i \in [-1,1]$$.

### Ví dụ 3

<center>
$$f:\mathbb{R}^n \to \mathbb{R}, f(x) =  \vert x \vert _2$$
</center>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-2.png" alt="Subgradient3" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Hình 3] Gradient dưới của }f(x)= \vert x \vert _2\text{ [3]}$$</figcaption>
</figure>

- Với $$x \neq 0$$, hàm khả vi nên ta có $$g=\nabla \sqrt{x^Tx} = \frac{1}{2}(x^Tx)^{-\frac{1}{2}} (2x) = \frac{x}{\vert x \vert _2}$$.
- Với $$x=0$$, điều kiện là $$ \vert y \vert _2 \geq g^Ty \Longrightarrow  \vert y \vert _2 \geq  \vert g \vert _2 \vert y \vert _2 \cos \theta$$ với mọi $$y$$. Do đó, $$g \in \{z: \vert z \vert _2 \leq 1 \}$$.

### Ví dụ 4

Xét $$f(x) = \max f_1(x),f_2(x) $$, trong đó $$f_1,f_2:\mathbb{R}^n \to \mathbb{R}$$ đều là các hàm lồi và khả vi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_01_subgrad-4.png" alt="Subgradient4" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">$$\text{[Hình 4] Gradient dưới của }f(x)=\max f_1(x),f_2(x) \text{ [3]}$$</figcaption>
</figure>

- Với $$f_1(x) > f_2(x)$$, ta có $$g = \nabla f_1(x)$$.
- Với $$f_1(x) < f_2(x)$$, ta có $$g = \nabla f_2(x)$$.
- Với $$f_1(x) = f_2(x)$$, ta có $$g \in \{\theta_1 \nabla f_1(x) + \theta_2 \nabla f_2(x): \theta_1 + \theta_2 = 1, \theta_1 \geq 0, \theta_2 \geq 0 \}$$.

### Gradient dưới tại điểm gấp khúc

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/subgradient-fan_vi.mp4"></video>
</div>

Tại điểm gấp khúc của $$f(x)=\max_i f_i(x)$$, có nhiều đường thẳng nằm dưới đồ thị và tiếp xúc với đồ thị tại điểm đó; hệ số góc của mỗi đường thẳng như vậy đều là một gradient dưới.

### Tự tay thử: gradient dưới tại điểm gấp khúc

<div class="opx-explainer" data-opx="subg" data-lang="vi"></div>

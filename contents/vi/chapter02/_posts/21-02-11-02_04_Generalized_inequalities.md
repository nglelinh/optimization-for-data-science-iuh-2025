---
layout: post
title: 02-04 Bất đẳng thức tổng quát
chapter: '02'
order: 12
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Trên trục số thực $$\mathbb{R}$$, ta luôn so sánh được hai số bất kỳ: $$3 < 5$$ hay $$7 \ge 2$$. Nhưng khi bạn tối ưu hóa một thiết kế xe hơi với hai mục tiêu xung đột — **giá rẻ** và **an toàn cao** — hoặc khi bạn muốn so sánh hai ma trận hiệp phương sai $$A$$ và $$B$$, dấu "$$\le$$" thông thường không còn đủ nữa. **Bất đẳng thức tổng quát** ($$x \preceq_K y \iff y - x \in K$$) giải quyết bài toán này một cách tinh tế bằng cách dùng một **hình nón thích hợp** $$K$$ làm thước đo thứ tự!

Bài học này mở rộng khái niệm so sánh từ số thực sang vector và ma trận, đồng thời phân biệt hai khái niệm cực kỳ quan trọng trong tối ưu hóa đa mục tiêu: **phần tử tối tiểu (minimum)** và **phần tử cực tiểu (minimal / Pareto optimal)**.

## Kiến thức cần nhớ: Bốn mảnh ghép của thứ tự theo hình nón

- **Hình nón thích hợp (Proper Cone $$K$$):** Phải hội tụ đủ 4 điều kiện: lồi, đóng, đặc (có phần trong khác rỗng) và nhọn (không chứa cả đường thẳng nào, tức $$K \cap (-K) = \{0\}$$). Nhờ 4 tính chất này, quan hệ $$\preceq_K$$ thỏa mãn phản xạ, phản đối xứng, bắc cầu và bảo toàn phép cộng/nhân dương.
- **Hai ví dụ mẫu mực:** $$K = \mathbb{R}_+^n$$ sinh ra so sánh từng thành phần trên vector ($$x_i \le y_i\ \forall i$$); $$K = \mathbb{S}_+^n$$ sinh ra thứ tự Loewner trên ma trận đối xứng ($$A \preceq B \iff B - A \succeq 0$$).
- **Thứ tự bộ phận (Partial Order):** Khác với $$\mathbb{R}$$, hai đối tượng có thể **không so sánh được** với nhau (không $$x \preceq_K y$$ cũng không $$y \preceq_K x$$).
- **Tối tiểu (Minimum) so với Cực tiểu (Minimal):** Phần tử tối tiểu nhỏ hơn *mọi* phần tử khác (thường không tồn tại trong bài toán đa mục tiêu); phần tử cực tiểu (Pareto) là phần tử không bị bất kỳ phần tử nào khác vượt trội hơn hẳn.

### Giải thích: So sánh hai cặp ma trận theo thứ tự Loewner ($$K = \mathbb{S}_+^2$$)

Xét ba ma trận đối xứng $$2\times 2$$:
$$A = \begin{pmatrix}3 & 1\\ 1 & 2\end{pmatrix}, \qquad B = \begin{pmatrix}2 & 0\\ 0 & 1\end{pmatrix}, \qquad C = \begin{pmatrix}3 & 0\\ 0 & 0\end{pmatrix}.$$

1. **So sánh $$B$$ và $$A$$:** Tính hiệu:
   $$A - B = \begin{pmatrix}1 & 1\\ 1 & 1\end{pmatrix}.$$
   Ma trận $$A - B$$ có vết $$2$$, định thức $$0 \implies$$ giá trị riêng $$\lambda_1 = 2 \ge 0,\ \lambda_2 = 0 \ge 0$$. Vậy $$A - B \in \mathbb{S}_+^2$$, tức $$B \preceq_{\mathbb{S}_+^2} A$$!
2. **So sánh $$B$$ và $$C$$:** Tính hiệu:
   $$C - B = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}.$$
   Giá trị riêng là $$\lambda_1 = +1 > 0$$ và $$\lambda_2 = -1 < 0$$. Do có cả trị riêng dương và âm, $$C - B \notin \mathbb{S}_+^2$$ và $$B - C \notin \mathbb{S}_+^2$$.
3. **Kết luận:** $$B$$ và $$C$$ **không so sánh được** theo thứ tự Loewner — minh họa trực quan cho tính chất thứ tự bộ phận của bất đẳng thức tổng quát!

---

Trên trục số thực một chiều $$\mathbb{R}$$, với hai số bất kỳ như 1 và 2, ta luôn so sánh được 2 lớn hơn 1. Tuy nhiên, trong không gian thực $$n$$ chiều $$\mathbb{R}^n$$, việc so sánh hai điểm $$x_1$$ và $$x_2$$ không còn hiển nhiên như vậy.

Phần này giới thiệu **bất đẳng thức tổng quát** để xác định quan hệ thứ tự giữa các điểm trong $$\mathbb{R}^n$$, cùng hai khái niệm phần tử tối tiểu (minimum) và phần tử cực tiểu (minimal) của một tập hợp.

## Hình nón thích hợp

Một hình nón lồi $$K \subseteq \mathbb{R}^n$$ được gọi là **hình nón thích hợp** (proper cone) nếu thỏa mãn ba điều kiện sau:

* $$K$$ là tập đóng (chứa biên của chính nó).
* $$K$$ là hình nón đặc (solid), tức là phần trong của nó khác rỗng.
* $$K$$ là hình nón nhọn (pointed), tức là không chứa đường thẳng nào đi qua gốc tọa độ ($$x \in K, -x \in K \implies x = 0$$).

Nếu một hình nón lồi đóng và nhọn chỉ nằm trong một không gian con có số chiều từ $$n-1$$ trở xuống, phần trong của nó trong $$\mathbb{R}^n$$ sẽ rỗng vì nó không thể chứa bất kỳ hình cầu mở $$n$$ chiều nào. Khi đó, hình nón không đặc và không phải là hình nón thích hợp. Ví dụ, một hình quạt 2D đóng và nhọn đặt trong không gian $$\mathbb{R}^3$$ không phải là hình nón thích hợp.

Xem thêm *[Wikipedia: Interior (topology)](https://en.wikipedia.org/wiki/Interior_(topology))* để biết định nghĩa về phần trong của một tập hợp.

## Bất đẳng thức tổng quát

Dựa trên một hình nón thích hợp $$K$$, ta định nghĩa một quan hệ thứ tự bộ phận trong $$\mathbb{R}^n$$ gọi là **bất đẳng thức tổng quát**, mang nhiều tính chất tương tự thứ tự thông thường trên $$\mathbb{R}$$:

> $$x \preceq_{K} y \iff y - x \in K$$

Tương tự, bất đẳng thức tổng quát nghiêm ngặt được định nghĩa bởi:

> $$x \prec_{K} y \iff y - x \in $$ **int** $$K$$

Khi $$K = \mathbb{R}_{+}$$, quan hệ $$\preceq_{K}$$ chính là dấu $$\le$$ quen thuộc trên $$\mathbb{R}$$.

### Tính chất của bất đẳng thức tổng quát

Bất đẳng thức tổng quát $$\preceq_{K}$$ có các tính chất sau:

* **Bảo toàn dưới phép cộng**: nếu $$x \preceq_{K} y$$ và $$u \preceq_{K} v$$ thì $$ x+u \preceq_{K} y +v$$.
* **Tính bắc cầu**: nếu $$x \preceq_{K} y$$ và $$y \preceq_{K} z$$ thì $$x \preceq_{K}  z$$.
* **Bảo toàn dưới phép nhân vô hướng không âm**: nếu $$x \preceq_{K} y$$ và $$\alpha \ge 0$$ thì $$\alpha x \preceq_{K} \alpha y$$.
* **Tính phản xạ**: $$x \preceq_{K} x$$.
* **Tính phản đối xứng**: nếu $$x \preceq_{K} y$$ và $$y \preceq_{K} x$$ thì $$x = y$$.
* **Bảo toàn qua giới hạn**: nếu $$x_i \preceq_{K}  y_i$$ với mọi $$i = 1, 2, \dots$$, $$x_i \to x$$ và $$y_i \to y$$ khi $$i \to \infty$$, thì $$x \preceq_{K} y$$.

Bất đẳng thức tổng quát nghiêm ngặt $$\prec_{K}$$ cũng có các tính chất tương ứng (trừ tính phản xạ và tính bảo toàn qua giới hạn).

## Phần tử tối tiểu và cực tiểu

Điểm khác biệt quan trọng nhất giữa thứ tự thông thường trên $$\mathbb{R}$$ và bất đẳng thức tổng quát trong $$\mathbb{R}^n$$ nằm ở **tính toàn phần (thứ tự tuyến tính)**. Trên $$\mathbb{R}$$, hai số bất kỳ luôn so sánh được với nhau ($$x \le y$$ hoặc $$y \le x$$), nhưng với bất đẳng thức tổng quát thì không nhất thiết như vậy. Vì thế, khái niệm nhỏ nhất được tách thành hai khái niệm phân biệt: tối tiểu và cực tiểu.

### Phần tử tối tiểu

Điểm $$x \in S$$ được gọi là phần tử **tối tiểu** (minimum) của tập $$S$$ nếu $$x \preceq_{K} y$$ với mọi $$y \in S$$. Phần tử **tối đại** (maximum) được định nghĩa tương tự. Nếu tập $$S$$ có phần tử tối tiểu thì phần tử đó là duy nhất.

Về mặt tập hợp, $$x \in S$$ là phần tử tối tiểu của $$S$$ khi và chỉ khi $$S \subseteq x + K$$, trong đó $$x + K$$ là tập tất cả các điểm so sánh được với $$x$$ và lớn hơn hoặc bằng $$x$$ theo $$\preceq_{K}$$.

### Phần tử cực tiểu

Điểm $$x \in S$$ được gọi là phần tử **cực tiểu** (minimal) của tập $$S$$ nếu không tồn tại điểm $$y \in S$$ nào khác $$x$$ sao cho $$y \preceq_{K} x$$ (tức là với mọi $$y \in S$$, $$y \preceq_{K} x \implies y = x$$). Phần tử **cực đại** (maximal) được định nghĩa tương tự. Khác với phần tử tối tiểu, một tập hợp có thể có nhiều phần tử cực tiểu.

Về mặt tập hợp, $$x \in S$$ là phần tử cực tiểu của $$S$$ khi và chỉ khi $$(x - K) \cap S = \{x\}$$, trong đó $$x - K$$ là tập tất cả các điểm so sánh được với $$x$$ và nhỏ hơn hoặc bằng $$x$$ theo $$\preceq_{K}$$.

Khi $$K = \mathbb{R}_{+}$$, hai khái niệm phần tử tối tiểu và phần tử cực tiểu trùng nhau.

### Tối tiểu và cực tiểu trong hình nón $$\mathbb{R}^2_{+}$$

Xét hình nón $$K = \mathbb{R}^2_{+}$$. Bất đẳng thức $$x \preceq_{K} y$$ có nghĩa là $$y$$ nằm ở phía trên bên phải của $$x$$. Do đó, với $$x \in S$$, nói $$x$$ là phần tử tối tiểu nghĩa là mọi điểm của $$S$$ đều nằm ở phía trên bên phải của $$x$$; còn nói $$x$$ là phần tử cực tiểu nghĩa là không có điểm nào khác của $$S$$ nằm ở phía dưới bên trái của $$x$$.

Trong hình dưới đây, tập $$S_1$$ có phần tử tối tiểu $$x_1$$ vì vùng $$x_1 + K$$ (tô màu xám nhạt) bao trọn $$S_1$$ ($$S_1 \subseteq x_1 + K$$). Tập $$S_2$$ có phần tử cực tiểu $$x_2$$ vì vùng $$x_2 - K$$ (tô màu xám nhạt) chỉ giao với $$S_2$$ tại đúng điểm $$x_2$$ ($$(x_2 - K) \cap S_2 = \{x_2\}$$).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_01_Minimum_and_minimal.png" alt="[Hình1] Phần tử tối tiểu và cực tiểu [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Phần tử tối tiểu và cực tiểu [1]</figcaption>
</p>
</figure>
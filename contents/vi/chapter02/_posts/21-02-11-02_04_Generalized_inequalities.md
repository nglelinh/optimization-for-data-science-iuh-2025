---
layout: post
title: 02-04 Bất đẳng thức tổng quát
chapter: '02'
order: 10
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Trong không gian thực một chiều $$\mathbb{R}$$, cho hai số 1 và 2, chúng ta có thể nói 2 lớn hơn 1. Nhưng trong không gian thực $$n$$ chiều $$\mathbb{R}^n$$, cho hai điểm $$x_1$$ và $$x_2$$, liệu chúng ta có thể nói điểm nào lớn hơn? Điều này không đơn giản.

Phần này giới thiệu **bất đẳng thức tổng quát** để so sánh thứ tự giữa hai điểm trong $$\mathbb{R}^n$$, và cũng thảo luận về các khái niệm phần tử cực tiểu và tối tiểu của một tập hợp.

## Hình nón thích hợp

Một hình nón lồi $$K \subseteq \mathbb{R}^n$$ được gọi là **hình nón thích hợp** nếu nó thỏa mãn:

* K là đóng (bao gồm biên của nó).
* K là rắn (phần trong của nó không rỗng).
* K là nhọn (không chứa bất kỳ đường thẳng nào) (tức là $$x \in K, -x \in K \implies x = 0$$).

Nếu một hình nón lồi nhọn & đóng được định nghĩa trong một không gian con có chiều $$n-1$$ hoặc ít hơn, phần trong của nó sẽ rỗng, vì nó không thể chứa một hình cầu mở trong $$n$$ chiều. Do đó, nó không rắn và không thể là hình nón thích hợp. Ví dụ, một hình nón lồi nhọn & đóng hình quạt 2D trong $$\mathbb{R}^3$$ không phải là hình nón thích hợp.

Xem *[Wikipedia: Interior (topology)](https://en.wikipedia.org/wiki/Interior_(topology))* để biết định nghĩa về phần trong.

## Bất đẳng thức tổng quát

Sử dụng một hình nón thích hợp, chúng ta có thể định nghĩa một thứ tự từng phần trong $$\mathbb{R}^n$$ được gọi là **bất đẳng thức tổng quát**. Nó có các tính chất tương tự như thứ tự tiêu chuẩn trong $$\mathbb{R}$$:

> $$x \preceq_{K} y \iff y − x \in K$$

Tương tự, thứ tự từng phần nghiêm ngặt được định nghĩa như:

> $$x \prec_{K} y \iff y − x \in $$ **int** $$K$$

Nếu $$K = \mathbb{R}_{+}$$, thì $$\preceq_{K}$$ là $$\le$$ thông thường trong $$\mathbb{R}$$.

### Tính chất của bất đẳng thức tổng quát

Bất đẳng thức tổng quát $$\preceq_{K}$$ thỏa mãn:

* **Bảo toàn dưới phép cộng**: nếu $$x \preceq_{K} y$$ và $$u \preceq_{K} v$$, thì $$ x+u \preceq_{K} y +v$$.
* **Bắc cầu**: nếu $$x \preceq_{K} y$$ và $$y \preceq_{K} z$$ thì $$x \preceq_{K}  z$$.
* **Bảo toàn dưới co giãn không âm**: nếu $$x \preceq_{K} y$$ và $$α \ge 0$$ thì $$αx \preceq_{K} αy$$.
* **Phản xạ**: $$x \preceq_{K} x$$.
* **Phản đối xứng**: nếu $$x \preceq_{K} y$$ và $$y \preceq_{K} x$$, thì $$x = y$$.
* **Bảo toàn dưới giới hạn**: nếu $$x_i \preceq_{K}  y_i$$ với $$i = 1, 2, ..., x_i \to x$$ và $$y_i \to y$$ khi $$i \to ∞$$, thì $$x \preceq_{K} y$$.

Bất đẳng thức tổng quát nghiêm ngặt có các tính chất tương ứng.

## Phần tử tối tiểu và cực tiểu

Sự khác biệt quan trọng nhất giữa thứ tự trong $$\mathbb{R}$$ và thứ tự tổng quát trong $$\mathbb{R}^n$$ là **thứ tự tuyến tính**. Trong $$\mathbb{R}$$, chúng ta có thể so sánh bất kỳ hai điểm nào với $$x \lt y$$ hoặc $$x \gt y$$, nhưng bất đẳng thức tổng quát không thể luôn làm điều này. Do đó, việc định nghĩa các khái niệm cực đại và cực tiểu trong bối cảnh bất đẳng thức tổng quát được dự kiến sẽ phức tạp hơn nhiều.

### Phần tử tối tiểu

Nếu $$x \in S$$ thỏa mãn $$x \preceq_{K} y$$ với mọi $$y \in S$$, thì $$x$$ là phần tử **tối tiểu** của tập $$S$$. Tương tự, **tối đại** có thể được định nghĩa theo cách tương tự. Nếu một tối tiểu tồn tại trong một tập hợp, nó là duy nhất. Tức là, chỉ tồn tại một tối tiểu.

Nếu một điểm $$x \in S$$ là tối tiểu của $$S$$, thì $$S \subseteq x + K$$. Ở đây, $$x + K$$ có nghĩa là (theo $$\preceq_{K}$$) tất cả các điểm đều có thể so sánh với $$x$$ và lớn hơn hoặc bằng $$x$$.

### Phần tử cực tiểu

Một khái niệm tương tự là **cực tiểu**. Nếu $$x \in S$$ và với mọi $$y \in S$$, điều kiện $$y \preceq_{K} x$$ chỉ đúng khi $$y=x$$, thì $$x$$ là phần tử **cực tiểu** của tập $$S$$. Tương tự, **cực đại** có thể được định nghĩa theo cách tương tự. Một tập hợp có thể có nhiều phần tử cực tiểu.

Nếu một điểm $$x \in S$$ là cực tiểu trong $$S$$, thì $$(x - K) \cap S = \{x\}$$. Ở đây, $$x - K$$ có nghĩa là (theo $$\preceq_{K}$$) tất cả các điểm đều có thể so sánh với $$x$$ và nhỏ hơn hoặc bằng $$x$$.

Trong trường hợp $$K = \mathbb{R}_{+}$$, cực tiểu và tối tiểu là giống nhau và tương ứng với định nghĩa chung của tối tiểu.

### Tối tiểu và cực tiểu trong hình nón $$\mathbb{R}^2_{+}$$

Xét hình nón $$\mathbb{R}^2_{+}$$ $$K$$. Bất đẳng thức $$x \preceq_{K} y$$ có nghĩa là $$y$$ nằm ở phía trên bên phải của $$x$$. Khi $$x \in S$$, nói rằng $$x$$ là tối tiểu có nghĩa là tất cả các điểm trong $$S$$ đều nằm ở phía trên bên phải của $$x$$. Nói rằng $$x$$ là cực tiểu có nghĩa là không có điểm nào trong $$S$$ nằm ở phía dưới bên trái của $$x$$.

Trong hình dưới đây, $$S_1$$ có một tối tiểu $$x_1$$. Tập $$x + K$$ được hiển thị bằng màu xám nhạt, và vì $$S_1 \subseteq x + K$$, $$x_1$$ là tối tiểu. $$S_2$$ có một phần tử cực tiểu $$x_2$$. Tập $$x - K$$ được hiển thị bằng màu xám nhạt, và vì $$(x - K) \cap S = \{x\}$$, $$x_2$$ là cực tiểu.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_01_Minimum_and_minimal.png" alt="[Hình1] Phần tử tối tiểu và cực tiểu [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Phần tử tối tiểu và cực tiểu [1]</figcaption>
</p>
</figure>
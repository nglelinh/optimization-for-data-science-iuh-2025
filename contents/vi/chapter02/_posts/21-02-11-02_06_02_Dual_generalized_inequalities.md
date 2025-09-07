---
layout: post
title: 02-06-02 Bất đẳng thức tổng quát đối ngẫu
chapter: '02'
order: 14
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Nếu chúng ta có thể định nghĩa một bất đẳng thức tổng quát sử dụng một hình nón thích hợp, chúng ta cũng có thể định nghĩa một bất đẳng thức tổng quát đối ngẫu sử dụng hình nón đối ngẫu, với điều kiện hình nón đối ngẫu là thích hợp.

Phần này định nghĩa bất đẳng thức tổng quát đối ngẫu sử dụng một hình nón đối ngẫu thích hợp và định nghĩa lại các phần tử tối tiểu và cực tiểu sử dụng bất đẳng thức đối ngẫu.

## Bất đẳng thức tổng quát đối ngẫu

Cho một hình nón đối ngẫu thích hợp, bất đẳng thức tổng quát được định nghĩa như sau. Với một điểm $$y$$, nếu tích vô hướng với mọi $$x$$ trong $$K$$ đều không âm, thì $$y$$ là không âm trong hình nón đối ngẫu $$K^*$$.

Ở đây, $$\succeq_{K^*}$$ được gọi là **đối ngẫu** của $$\succeq_K$$, tức là **bất đẳng thức tổng quát đối ngẫu**.

> $$y \succeq_{K^*} 0 \iff y^T x \ge 0$$ với mọi $$x \succeq_K 0$$

### Tính chất chính của bất đẳng thức tổng quát và đối ngẫu

* $$x \preceq_K y$$ khi và chỉ khi $$\lambda^T x \le \lambda^T y$$ với mọi $$\lambda \succeq_{K^*} 0$$.
* $$x \prec_K y$$ khi và chỉ khi $$\lambda^T x < \lambda^T y$$ với mọi $$\lambda \succeq_{K^*} 0, \lambda \ne 0$$.

Nếu $$K = K^{**}$$, bất đẳng thức tổng quát đối ngẫu liên kết với $$\preceq_K^*$$ là $$\preceq_K$$, vậy các tính chất này được bảo toàn ngay cả khi vai trò của bất đẳng thức tổng quát và đối ngẫu được hoán đổi.

Ví dụ, $$\lambda \preceq_K^* \mu$$ khi và chỉ khi $$\lambda^T x \le \mu^T x$$ với mọi $$x \succeq_K 0$$.

## Phần tử tối tiểu và cực tiểu thông qua bất đẳng thức đối ngẫu

Với một bất đẳng thức tổng quát được cảm sinh bởi một hình nón thích hợp $$K$$, chúng ta có thể sử dụng bất đẳng thức tổng quát đối ngẫu để đặc trưng cho các phần tử tối tiểu và cực tiểu của một tập (có thể không lồi) $$S \subseteq \mathbb{R}^m$$.

### Phần tử tối tiểu

Với mọi $$ \lambda \succ_K^* 0$$ và $$z \in S$$,

Nếu $$x$$ là bộ tối ưu hóa duy nhất của $$\lambda^T z$$, thì đối với bất đẳng thức tổng quát $$ \succ_K^* $$, $$x$$ là tối tiểu của $$S$$. (Bộ tối ưu hóa là một giá trị của biến phụ thuộc làm tối thiểu hóa một hàm; ở đây, hàm là $$\lambda^T z$$, biến là $$z$$, và bộ tối ưu hóa là $$x$$.)

Về mặt hình học, điều này có nghĩa là với một số $$ \lambda \succ_K^* 0 $$, siêu phẳng $$\{ z \mid  \lambda^T (z-x) = 0 \}$$ là một siêu phẳng hỗ trợ nghiêm ngặt cho $$S$$ tại $$x$$. (Siêu phẳng hỗ trợ nghiêm ngặt có nghĩa là siêu phẳng giao với $$S$$ chỉ tại $$x$$.) $$S$$ không cần phải lồi. Hình dưới đây cho thấy một tối tiểu $$x$$ và một siêu phẳng hỗ trợ nghiêm ngặt.


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_02_Minimum_element.png" alt="[Hình1] Phần tử tối tiểu [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Phần tử tối tiểu [1]</figcaption>
</p>
</figure>

### Phần tử cực tiểu

Các điều kiện cần và đủ cho phần tử cực tiểu hơi khác một chút.

Với $$\lambda \succ_K^* 0$$ và $$z \in S$$, nếu $$x$$ là bộ tối ưu hóa của $$\lambda^T z$$, thì $$x \in S$$ là cực tiểu. Nói cách khác, nếu $$x$$ là cực tiểu, thì $$\lambda^T z$$ không có bộ tối ưu hóa duy nhất. Do đó, với cùng một $$\lambda$$, có thể có nhiều phần tử cực tiểu, và có thể có nhiều phần tử cực tiểu cho các $$\lambda$$ khác nhau.

Hình dưới đây minh họa sự tồn tại của nhiều phần tử cực tiểu. Vùng có đường màu đen dày ở phía dưới bên trái chỉ ra khu vực mà các phần tử cực tiểu tồn tại.
Ở đây, $$x_1$$ là bộ tối ưu hóa của $$\lambda^T_1 z$$ và vì $$\lambda_1 \succ_K^* 0$$, nó là cực tiểu. Một bộ tối ưu hóa khác, $$x_2$$, cũng tồn tại.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_05_Minimal_element.png" alt="[Hình2] Phần tử cực tiểu [1]" width="70%">
  <figcaption style="text-align: center;">[Hình2] Phần tử cực tiểu [1]</figcaption>
</p>
</figure>

Tuy nhiên, điều ngược lại không đúng. Ngay cả khi một điểm $$x$$ là cực tiểu trong một tập $$S$$, nó có thể không phải là bộ tối ưu hóa của $$\lambda^T z$$ với một số $$\lambda$$ và $$z \in S$$. Hình dưới đây cho thấy một ví dụ về phần tử cực tiểu không phải là bộ tối ưu hóa. Ở đây, tính lồi của tập hợp dường như đóng vai trò quan trọng trong việc điều ngược lại này không đúng.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_06_Minimal_element2.png" alt="[Hình3] Một ví dụ về phần tử cực tiểu không phải là bộ tối ưu hóa [1]" width="70%">
  <figcaption style="text-align: center;">[Hình3] Một ví dụ về phần tử cực tiểu không phải là bộ tối ưu hóa [1]</figcaption>
</p>
</figure>

Định lý ngược lại này không được tăng cường với $$\lambda_1 \succ_K^* 0$$. Trong hình bên trái dưới đây, $$x_1 \in S_1$$ là cực tiểu, nhưng không phải là bộ tối ưu hóa của $$\lambda_1^T x_1$$. Hình bên phải cho thấy $$x_2 \in S_2$$ không phải là cực tiểu, nhưng là bộ tối ưu hóa của $$\lambda_2^T x_2$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_07_Minimal_element3.png" alt="[Hình4] Các ví dụ mà điều ngược lại không được tăng cường với $$\lambda_1 \succ_K^* 0$$ [1]" width="70%">
  <figcaption style="text-align: center;">$$\text{[Hình4] Các ví dụ mà điều ngược lại không được tăng cường với } \lambda_1 \succ_K^* 0 \text{ [1]}$$</figcaption>
</p>
</figure>

### Biên sản xuất tối ưu
Xét một sản phẩm cần được sản xuất sử dụng n tài nguyên (lao động, điện, khí tự nhiên, nước, v.v.).
Sản phẩm này có thể được sản xuất theo nhiều cách. Với mỗi phương pháp sản xuất, có một vector tài nguyên $$x \in \mathbb{R}$$, trong đó $$x_i$$ biểu thị lượng tài nguyên $$i$$ được tiêu thụ. Giả định rằng tiêu thụ tài nguyên $$x_i$$ không âm, và các tài nguyên có giá trị cao.

Tập sản xuất $$P \subseteq \mathbb{R}^n$$ được định nghĩa là tập hợp tất cả các vector tài nguyên $$x$$. Một phương pháp sản xuất với vector tài nguyên cực tiểu được gọi là **tối ưu Pareto** hoặc **hiệu quả**. Tập hợp các phần tử cực tiểu của $$P$$ được gọi là **biên sản xuất hiệu quả**.

Hãy xem xét ngắn gọn về tính tối ưu Pareto.

Giả sử có hai phương pháp sản xuất, một với vector tài nguyên $$x$$ ($$P_x$$) và một với vector tài nguyên $$y$$ ($$P_y$$). Nếu với mọi $$i$$, $$x_i \le y_i$$, và với một số $$i$$, $$x_i \lt y_i$$, thì chúng ta có thể nói rằng $$P_x$$ tốt hơn $$P_y$$. Nói cách khác, một phương pháp không sử dụng nhiều tài nguyên hơn phương pháp khác, hoặc sử dụng ít nhất một tài nguyên ít hơn, được coi là tốt hơn. Tức là, điều này tương ứng với trường hợp $$x \preceq y$$ và $$x \ne y$$.
Nếu không có phương pháp nào tốt hơn $$P_x$$, thì $$P_x$$ được gọi là tối ưu Pareto.

Bằng cách tối thiểu hóa biểu thức sau, chúng ta có thể tìm phương pháp sản xuất tối ưu Pareto. Ở đây, $$ \lambda_i$$ có thể được coi như giá của tài nguyên $$i$$. Tối thiểu hóa $$ \lambda^T x$$ đối với $$P$$ cho ra phương pháp sản xuất rẻ nhất. Vì các giá cả đều dương, kết quả của việc tối thiểu hóa luôn là tối ưu Pareto.

> $$ \lambda^T x =$$ $$ \lambda^T_1 x_1 + \lambda^T_2 x_2 + ... + \lambda^T_n x_n, \lambda \succ 0 $$

Hình dưới đây minh họa tình huống này một cách rõ ràng. Trong hình, $$x_1, x_2, x_3$$ là tối ưu Pareto, trong khi $$x_4, x_5$$ thì không.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_08_Pareto_optimal.png" alt="[Hình5] Biên sản xuất tối ưu [1]" width="70%">
  <figcaption style="text-align: center;">[Hình5] Biên sản xuất tối ưu [1]</figcaption>
</p>
</figure>
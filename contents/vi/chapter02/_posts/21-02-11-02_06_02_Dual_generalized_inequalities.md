---
layout: post
title: 02-06-02 Bất đẳng thức tổng quát đối ngẫu
chapter: '02'
order: 16
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Khi một hình nón thích hợp $$K$$ sinh ra bất đẳng thức tổng quát $$\preceq_K$$, hình nón đối ngẫu $$K^*$$ của nó cũng là một hình nón thích hợp, và do đó cũng xác định một bất đẳng thức tổng quát tương ứng.

Phần này định nghĩa bất đẳng thức tổng quát đối ngẫu dựa trên $$K^*$$ và sử dụng nó để đặc trưng cho các phần tử tối tiểu và cực tiểu của một tập hợp.

## Bất đẳng thức tổng quát đối ngẫu

Với hình nón đối ngẫu thích hợp $$K^*$$, một điểm $$y$$ được xem là không âm theo thứ tự đối ngẫu nếu tích vô hướng của nó với mọi $$x \in K$$ đều không âm. Quan hệ $$\succeq_{K^*}$$ được gọi là **đối ngẫu** của $$\succeq_K$$, hay **bất đẳng thức tổng quát đối ngẫu**:

> $$y \succeq_{K^*} 0 \iff y^T x \ge 0$$ với mọi $$x \succeq_K 0$$

### Tính chất chính của bất đẳng thức tổng quát và đối ngẫu

* $$x \preceq_K y$$ khi và chỉ khi $$\lambda^T x \le \lambda^T y$$ với mọi $$\lambda \succeq_{K^*} 0$$.
* $$x \prec_K y$$ khi và chỉ khi $$\lambda^T x < \lambda^T y$$ với mọi $$\lambda \succeq_{K^*} 0, \lambda \ne 0$$.

Vì $$K$$ là hình nón thích hợp nên $$K = K^{**}$$, tức là bất đẳng thức tổng quát đối ngẫu của $$\preceq_{K^*}$$ chính là $$\preceq_K$$. Do vậy, các tính chất trên vẫn đúng khi hoán đổi vai trò giữa $$K$$ và $$K^*$$.

Ví dụ, $$\lambda \preceq_{K^*} \mu$$ khi và chỉ khi $$\lambda^T x \le \mu^T x$$ với mọi $$x \succeq_K 0$$.

## Phần tử tối tiểu và cực tiểu thông qua bất đẳng thức đối ngẫu

Với bất đẳng thức tổng quát sinh bởi hình nón thích hợp $$K$$, ta có thể dùng bất đẳng thức tổng quát đối ngẫu để đặc trưng cho phần tử tối tiểu và cực tiểu của một tập $$S \subseteq \mathbb{R}^m$$ (không nhất thiết lồi).

### Phần tử tối tiểu

Điểm $$x \in S$$ là phần tử tối tiểu của $$S$$ theo bất đẳng thức tổng quát $$\preceq_K$$ khi và chỉ khi với mọi $$\lambda \succ_{K^*} 0$$, $$x$$ là điểm cực tiểu hóa duy nhất của hàm tuyến tính $$\lambda^T z$$ trên $$z \in S$$.

Về mặt hình học, với mỗi $$\lambda \succ_{K^*} 0$$, siêu phẳng $$\{ z \mid \lambda^T (z - x) = 0 \}$$ là siêu phẳng hỗ trợ nghiêm ngặt cho $$S$$ tại $$x$$ (chỉ giao với $$S$$ tại duy nhất điểm $$x$$). Tính chất này không đòi hỏi $$S$$ phải lồi. Hình dưới đây minh họa một phần tử tối tiểu $$x$$ cùng siêu phẳng hỗ trợ nghiêm ngặt.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_02_Minimum_element.png" alt="[Hình1] Phần tử tối tiểu [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Phần tử tối tiểu [1]</figcaption>
</p>
</figure>

### Phần tử cực tiểu

Điều kiện đối với phần tử cực tiểu yếu hơn so với phần tử tối tiểu.

Nếu tồn tại một vector $$\lambda \succ_{K^*} 0$$ sao cho $$x$$ cực tiểu hóa $$\lambda^T z$$ trên $$z \in S$$, thì $$x \in S$$ chắc chắn là một phần tử cực tiểu của $$S$$. Khác với phần tử tối tiểu, điều kiện này chỉ cần đúng với *một* $$\lambda \succ_{K^*} 0$$ (không cần mọi $$\lambda$$) và điểm cực tiểu hóa cũng không cần duy nhất. Do đó, ứng với cùng một $$\lambda$$ hoặc các $$\lambda$$ khác nhau, tập $$S$$ có thể có nhiều phần tử cực tiểu.

Hình dưới đây minh họa trường hợp có nhiều phần tử cực tiểu (nằm trên đường viền đậm ở góc dưới bên trái). Tại đây, $$x_1$$ cực tiểu hóa $$\lambda_1^T z$$ với $$\lambda_1 \succ_{K^*} 0$$ nên $$x_1$$ là phần tử cực tiểu; tương tự, $$x_2$$ là một phần tử cực tiểu khác ứng với $$\lambda_2$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_05_Minimal_element.png" alt="[Hình2] Phần tử cực tiểu [1]" width="70%">
  <figcaption style="text-align: center;">[Hình2] Phần tử cực tiểu [1]</figcaption>
</p>
</figure>

Tuy nhiên, chiều ngược lại nhìn chung không đúng: một điểm $$x$$ có thể là phần tử cực tiểu của $$S$$ nhưng không cực tiểu hóa $$\lambda^T z$$ trên $$S$$ với bất kỳ $$\lambda \succ_{K^*} 0$$ nào. Hình dưới đây minh họa một ví dụ khi $$S$$ không lồi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_06_Minimal_element2.png" alt="[Hình3] Một ví dụ về phần tử cực tiểu không phải là bộ tối ưu hóa [1]" width="70%">
  <figcaption style="text-align: center;">[Hình3] Một ví dụ về phần tử cực tiểu không phải là bộ tối ưu hóa [1]</figcaption>
</p>
</figure>

Ngay cả khi $$S$$ là tập lồi, chiều ngược lại chỉ đảm bảo tồn tại $$\lambda \succeq_{K^*} 0$$ ($$\lambda \ne 0$$), chứ không nhất thiết $$\lambda \succ_{K^*} 0$$. Trong hình bên trái dưới đây, $$x_1 \in S_1$$ là phần tử cực tiểu nhưng không cực tiểu hóa $$\lambda_1^T z$$ với bất kỳ $$\lambda_1 \succ_{K^*} 0$$ nào. Hình bên phải cho thấy khi chỉ có $$\lambda_2 \succeq_{K^*} 0, \lambda_2 \ne 0$$, điểm $$x_2 \in S_2$$ tuy cực tiểu hóa $$\lambda_2^T z$$ trên $$S_2$$ nhưng lại không phải là phần tử cực tiểu.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_07_Minimal_element3.png" alt="[Hình4] Các ví dụ mà điều ngược lại không được tăng cường với $$\lambda_1 \succ_{K^*} 0$$ [1]" width="70%">
  <figcaption style="text-align: center;">$$\text{[Hình4] Các ví dụ mà điều ngược lại không được tăng cường với } \lambda_1 \succ_{K^*} 0 \text{ [1]}$$</figcaption>
</p>
</figure>

### Biên sản xuất tối ưu

Xét bài toán sản xuất một sản phẩm sử dụng $$n$$ loại tài nguyên (như lao động, điện, khí tự nhiên, nước, v.v.). Mỗi phương án sản xuất tương ứng với một vector tài nguyên $$x \in \mathbb{R}^n$$, trong đó $$x_i$$ là lượng tài nguyên thứ $$i$$ tiêu thụ (giả sử $$x_i \ge 0$$ và mỗi tài nguyên đều có chi phí dương).

Tập sản xuất $$P \subseteq \mathbb{R}^n$$ là tập hợp tất cả các vector tài nguyên khả thi $$x$$. Một phương án sản xuất có vector tài nguyên là phần tử cực tiểu của $$P$$ (theo $$\mathbb{R}^n_+$$) được gọi là **tối ưu Pareto** hay **hiệu quả**. Tập hợp tất cả các phần tử cực tiểu của $$P$$ được gọi là **biên sản xuất hiệu quả**.

Xét hai phương án sản xuất với vector tài nguyên $$x$$ (ký hiệu $$P_x$$) và $$y$$ (ký hiệu $$P_y$$). Nếu $$x_i \le y_i$$ với mọi $$i$$ và tồn tại ít nhất một chỉ số $$i$$ sao cho $$x_i < y_i$$ (tức là $$x \preceq y$$ và $$x \ne y$$), thì $$P_x$$ tốt hơn $$P_y$$ vì không dùng nhiều hơn bất kỳ tài nguyên nào và tiết kiệm được ít nhất một tài nguyên. Nếu không có phương án nào tốt hơn $$P_x$$ thì $$P_x$$ là phương án tối ưu Pareto.

Ta có thể tìm phương án tối ưu Pareto bằng cách cực tiểu hóa tổng chi phí tài nguyên sau đây trên tập $$P$$, trong đó $$\lambda_i > 0$$ đóng vai trò đơn giá của tài nguyên thứ $$i$$. Vì mọi đơn giá đều dương ($$\lambda \succ 0$$), mọi nghiệm cực tiểu hóa đều là phương án tối ưu Pareto:

> $$ \lambda^T x = \lambda_1 x_1 + \lambda_2 x_2 + \cdots + \lambda_n x_n, \quad \lambda \succ 0 $$

Hình dưới đây minh họa trực quan: các điểm $$x_1, x_2, x_3$$ là tối ưu Pareto, còn $$x_4, x_5$$ thì không.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_08_Pareto_optimal.png" alt="[Hình5] Biên sản xuất tối ưu [1]" width="70%">
  <figcaption style="text-align: center;">[Hình5] Biên sản xuất tối ưu [1]</figcaption>
</p>
</figure>
---
layout: post
title: 02-02-01 Ví dụ về tập lồi
chapter: '02'
order: 9
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Từ phương trình đường tròn đơn giản đến tập nghiệm của một hệ hàng nghìn ràng buộc tài chính hay tập ma trận hiệp phương sai hợp lệ, thế giới các tập lồi phong phú hơn tưởng tượng rất nhiều. Biết đọc ngay cấu trúc hình học của **nửa không gian**, **hình cầu chuẩn**, **ellipsoid** và **đa diện (polyhedra)** sẽ giúp bạn nhận ra ngay một bài toán thuộc lớp LP, QP hay SOCP ngay từ lần đọc đầu tiên.

Bài học này phân tích chi tiết công thức, trực giác hình học và chứng minh tính lồi của những tập lồi kinh điển nhất.

## Kiến thức cần nhớ: Bốn họ tập lồi chủ lực

- **Siêu phẳng và Nửa không gian:** $$a^T x = b$$ và $$a^T x \le b$$ — là những khối cơ bản nhất; mọi tập lồi đóng đều có thể biểu diễn thành giao của (có thể vô hạn) các nửa không gian!
- **Đa diện (Polyhedron) và Đơn hình (Simplex):** Giao hữu hạn của các nửa không gian và siêu phẳng $$\{x : Ax \preceq b,\ Cx = d\}$$. Tập nghiệm khả thi của mọi bài toán LP là một đa diện.
- **Hình cầu Euclid và Hình cầu chuẩn (Norm Balls):** $$B(x_c, r) = \{x : \|x - x_c\| \le r\}$$ luôn lồi nhờ tính đồng nhất dương và bất đẳng thức tam giác của chuẩn.
- **Ellipsoid:** $$\mathcal{E} = \{x : (x - x_c)^T P^{-1}(x - x_c) \le 1\}$$ với $$P \succ 0$$ — chính là ảnh biến dạng tuyến tính của hình cầu đơn vị, trong đó độ dài các bán trục bằng căn bậc hai các giá trị riêng $$\sqrt{\lambda_i(P)}$$.

### Giải thích: Đọc bán trục và kiểm tra điểm thuộc một Ellipsoid

Xét ellipsoid trong $$\mathbb{R}^2$$ có tâm $$x_c = (1, 0)^T$$ và ma trận hình dạng $$P = \begin{pmatrix}9 & 0\\ 0 & 4\end{pmatrix} \succ 0$$:

1. **Viết phương trình tường minh:** Ma trận nghịch đảo là $$P^{-1} = \begin{pmatrix}1/9 & 0\\ 0 & 1/4\end{pmatrix}$$, nên:
   $$\mathcal{E} = \left\{(x_1, x_2) : \frac{(x_1 - 1)^2}{9} + \frac{x_2^2}{4} \le 1\right\}.$$
2. **Đọc kích thước hình học từ giá trị riêng của $$P$$:**
   - Bán trục theo phương $$x_1$$ dài $$\sqrt{9} = 3$$ (trải từ $$x_1 = -2$$ đến $$x_1 = 4$$).
   - Bán trục theo phương $$x_2$$ dài $$\sqrt{4} = 2$$ (trải từ $$x_2 = -2$$ đến $$x_2 = 2$$).
3. **Kiểm tra hai điểm cụ thể:**
   - Điểm $$p = (3, 1)^T$$: $$\frac{(3 - 1)^2}{9} + \frac{1^2}{4} = \frac{4}{9} + \frac{1}{4} = \frac{25}{36} \approx 0.694 < 1 \implies$$ nằm **chặt bên trong** $$\mathcal{E}$$.
   - Điểm $$q = (4, 1)^T$$: $$\frac{(4 - 1)^2}{9} + \frac{1^2}{4} = 1 + 0.25 = 1.25 > 1 \implies$$ nằm **ngoài** $$\mathcal{E}$$.

---

Tập lồi xuất hiện dưới nhiều dạng khác nhau, từ các tập đơn giản như điểm và đường thẳng cho đến siêu phẳng, nửa không gian, hình cầu, ellipsoid, đa diện và hình nón.

## Siêu phẳng

Siêu phẳng là tập con affine $$(n-1)$$ chiều chia không gian $$n$$ chiều thành hai phần, trong đó $$a$$ là vector pháp tuyến và $$b$$ xác định vị trí của siêu phẳng so với gốc tọa độ. Siêu phẳng vừa là tập lồi vừa là tập affine.

> {$$x : a^T x = b$$} với $$ a \in \mathbb{R}^n, a \ne 0, b \in \mathbb{R}$$

Trong hình dưới đây, với điểm $$x_0$$ nằm trên siêu phẳng, mọi điểm $$x$$ thuộc siêu phẳng đều thỏa mãn $$(x - x_0)$$ vuông góc với $$a$$. Do đó $$a^T (x - x_0) = 0$$, tức là $$a^T x = b$$ với $$b = a^T x_0$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.05_Hyperplane.png" alt="[Hình1] Siêu phẳng [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Siêu phẳng [1]</figcaption>
</p>
</figure>

## Nửa không gian

Nửa không gian là mỗi phần không gian nằm về một phía của siêu phẳng. Một siêu phẳng $$a^T x = b$$ chia không gian thành hai nửa không gian. Nửa không gian là tập lồi nhưng không phải tập affine.

> {$$x : a^T x \le b$$} hoặc {$$x : a^T x \ge b$$}  với $$ a \in \mathbb{R}^n, a \ne 0, b \in \mathbb{R}$$

Với siêu phẳng $$a^T x = b$$, nửa không gian $$a^T x \ge b$$ nằm về phía vector pháp tuyến $$a$$, còn nửa không gian $$a^T x \le b$$ nằm về phía $$-a$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.06_Halfspace.png" alt="[Hình2] Nửa không gian [1]" width="70%">
  <figcaption style="text-align: center;">[Hình2] Nửa không gian [1]</figcaption>
</p>
</figure>

*Lưu ý:* Phần trong của $$\{x : a^T x \le b\}$$, tức tập $$\{x : a^T x \lt b\}$$, được gọi là nửa không gian mở.

### Tính chất quan trọng: Nửa không gian là tập lồi

Xét hai điểm bất kỳ $x_1$ và $x_2$ thuộc nửa không gian:
- Cả hai điểm đều thỏa mãn $a^T x_1 \leq b$ và $a^T x_2 \leq b$.

Xét tổ hợp lồi bất kỳ $x_\theta = \theta x_1 + (1 - \theta)x_2$ với $\theta \in [0, 1]$. Ta kiểm tra điều kiện thuộc nửa không gian:
$$a^T x_\theta = a^T(\theta x_1 + (1 - \theta)x_2) = \theta(a^T x_1) + (1 - \theta)(a^T x_2) \leq \theta b + (1 - \theta)b = b$$

Vì $x_\theta$ thỏa mãn bất đẳng thức nên mọi điểm trên đoạn thẳng nối $x_1$ và $x_2$ đều nằm trong nửa không gian; suy ra nửa không gian là tập lồi.

## Hình cầu Euclidean

Hình cầu Euclidean tâm $$x_c$$, bán kính $$r \ge 0$$ là tập hợp tất cả các điểm cách $$x_c$$ một khoảng không vượt quá $$r$$ theo chuẩn Euclidean $$\|u\|_2 = (u^T u)^{1/2}$$:

> $$B(x_c, r) = \{ x \mid \|x - x_c \|_2 \le r \} = \{ x \mid (x - x_c)^T (x - x_c) \le r^2 \} \text{ với } r \ge 0$$

Hình cầu Euclidean cũng có thể được biểu diễn tương đương dưới dạng:

> $$B(x_c, r) = \{ x_c + ru \mid \| u \|_2 \le 1 \} $$

## Ellipsoid

Ellipsoid là tập lồi tổng quát hóa hình cầu Euclidean, được định nghĩa như sau:

> $$\mathcal{E} = \{x \mid (x - x_c)^T P^{-1} (x - x_c) \le 1 \} $$

Trong đó $$P = P^T \succ 0$$ là ma trận đối xứng xác định dương. Vector $$x_c$$ là tâm của ellipsoid, còn ma trận $$P$$ quyết định độ dài các bán trục theo từng phương xuất phát từ tâm: độ dài các bán trục bằng $$\sqrt{\lambda_i}$$, với $$\lambda_i$$ là các giá trị riêng của $$P$$. Khi $$P = r^2 I$$, ellipsoid trở thành hình cầu Euclidean bán kính $$r$$.

Hình dưới đây minh họa một ellipsoid với tâm $$x_c$$ và các trục chính, trục phụ.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_Ellipsoid.png" alt="[Hình3] Ellipsoid [1]" width="70%">
  <figcaption style="text-align: center;">[Hình3] Ellipsoid [1]</figcaption>
</p>
</figure>

Ellipsoid cũng có thể được viết dưới dạng:

> $$\mathcal{E} = \{ x_c + Au \mid \|u\|_2 \le 1 \} $$

với $$A$$ là ma trận vuông không suy biến. Khi chọn $$A = P^{1/2}$$ (đối xứng xác định dương), hai cách biểu diễn trùng nhau. Nếu $$A$$ đối xứng nửa xác định dương nhưng suy biến, tập thu được gọi là ellipsoid suy biến, có chiều affine bằng hạng của $$A$$ và vẫn là tập lồi.

## Hình cầu chuẩn

Hình cầu chuẩn là tập hợp các điểm cách tâm $$x_c$$ không quá $$r$$ theo một chuẩn bất kỳ $$\|\cdot\|$$ trên $$\mathbb{R}^n$$ (thay vì chỉ dùng chuẩn Euclidean):

> $$ \{ x \mid \|x - x_c \| \le r  \} $$

Với chuẩn $$\ell_p$$ được định nghĩa là:

> $$ \| x  \|_{p} = \left( \sum_{i=1}^n |x_i|^{p} \right)^{1/p} \text{ với  } p \ge 1$$

hình dạng của hình cầu chuẩn thay đổi tùy theo giá trị của $$p$$. Hình cầu chuẩn luôn lồi khi $$p \ge 1$$. Hai hình dưới đây lần lượt minh họa hình dạng hình cầu chuẩn trong không gian 3D và 2D ứng với các giá trị $$p$$ khác nhau.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_2_norm_ball.png" alt="[Hình4] Hình cầu chuẩn [1]" width="70%">
  <figcaption style="text-align: center;">[Hình4] Hình cầu chuẩn [1]</figcaption>
</p>
</figure>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.07_3_norm_ball2.png" alt="[Hình4] Hình cầu chuẩn [2]" width="70%">
  <figcaption style="text-align: center;">[Hình4] Hình cầu chuẩn [2]</figcaption>
</p>
</figure>

## Đa diện

Đa diện là tập nghiệm của một hệ hữu hạn các bất đẳng thức và đẳng thức tuyến tính. Các tập affine (không gian con, siêu phẳng, đường thẳng), tia, đoạn thẳng và nửa không gian đều là những trường hợp riêng của đa diện. Đa diện là tập lồi; một đa diện bị chặn được gọi là polytope.

> $$\mathcal{P} = \{ x \mid a^T_i x \le b_i, i = 1, ..., m, c_j^Tx  = d_j, j = 1, ..., p\}$$

Vì mỗi đẳng thức $$c_j^T x = d_j$$ tương đương với hai bất đẳng thức $$c_j^T x \le d_j$$ và $$c_j^T x \ge d_j$$, nên mọi đa diện đều có thể biểu diễn chỉ bằng các bất đẳng thức tuyến tính.

Hình dưới đây minh họa một đa diện ngũ giác tạo bởi giao của năm nửa không gian, với các vector pháp tuyến hướng ra ngoài $$a_1, ..., a_5$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.09_Polyhedra.png" alt="[Hình5] Đa diện [1]" width="70%">
  <figcaption style="text-align: center;">[Hình5] Đa diện [1]</figcaption>
</p>
</figure>

Dưới dạng ma trận, đa diện được viết gọn như sau:

> $$\mathcal{P} =  \{ x \mid Ax \preceq b, Cx  = d \}$$
trong đó
$$
A = 
\begin{bmatrix}
a^T_1 \\
\vdots \\
a^T_m
\end{bmatrix}, 
$$
$$
C = 
\begin{bmatrix}
c^T_1 \\
\vdots \\
c^T_p
\end{bmatrix}
$$

### Đơn hình

Đơn hình là đa diện đơn giản nhất có phần trong khác rỗng trong không gian $$n$$ chiều, được tạo thành từ $$n+1$$ điểm.

Tổng quát, cho $$k + 1$$ điểm $$v_0, ..., v_k \in \mathbb{R}^n$$ độc lập affine (nghĩa là các vector $$v_1 - v_0, ..., v_k - v_0$$ độc lập tuyến tính). Đơn hình tương ứng được định nghĩa là bao lồi của $$k+1$$ điểm này:

> $$C = \mathbb{conv} \{v_0, ... , v_k\} = \{ \theta_0 v_0 + \cdots + \theta_k v_k  \mid \theta \succeq 0, 1^T \theta = 1 \}$$

Hình dưới đây minh họa các đơn hình từ 0 đến 3 chiều: điểm (0D), đoạn thẳng (1D), tam giác (2D) và tứ diện (3D).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.02_10_Simplex.png" alt="[Hình6] Đơn hình [nguồn - wikipedia]" width="70%">
  <figcaption style="text-align: center;">[Hình6] Đơn hình [nguồn - wikipedia]</figcaption>
</p>
</figure>

Một ví dụ phổ biến là đơn hình xác suất:

> $$C = \mathbb{conv} \{e_1, ..., e_n \} = \{ \theta \mid \theta \succeq 0, 1^T \theta = 1\}$$

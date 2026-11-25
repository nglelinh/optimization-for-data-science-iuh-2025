---
layout: post
title: 13-04 Hàm liên hợp
chapter: '13'
order: 5
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Một đường cong lồi trơn tru có thể được mô tả theo hai cách hoàn toàn tương đương. Cách quen thuộc nhất là liệt kê từng điểm $$(x, f(x))$$ nằm trên đường cong. Nhưng từ thế kỷ 18, nhà toán học Adrien-Marie Legendre — và sau này là Werner Fenchel trong tối ưu lồi hiện đại — đã chỉ ra một góc nhìn thứ hai đầy bất ngờ: bạn có thể mô tả trọn vẹn hàm $$f$$ bằng tập hợp **tất cả các đường tiếp tuyến** có độ dốc $$y$$ nằm ngay dưới đồ thị của nó!

Mỗi đường thẳng có độ dốc $$y$$ được xác định bởi tung độ gốc (hay độ dịch chuyển lớn nhất) để nó chạm sát vào đồ thị $$f(x)$$: đó chính là **hàm liên hợp** $$f^*(y) = \sup_x (y^T x - f(x))$$. Không cần $$f$$ phải lồi hay khả vi, $$f^*$$ luôn luôn là một hàm lồi vì nó là supremum theo từng điểm của một họ các hàm tuyến tính theo $$y$$.

## Bản đồ kiến thức nền: Bốn tính chất vàng của hàm liên hợp Fenchel

- **Ý nghĩa hình học của độ dốc và tung độ gốc:** Khoảng cách lớn nhất theo phương thẳng đứng giữa đường thẳng $$y^T x$$ và đồ thị $$f(x)$$ chính là $$f^*(y)$$. Khi $$f$$ khả vi lồi, điểm $$x$$ đạt cực đại thỏa $$\nabla f(x) = y$$, nghĩa là phép liên hợp biến đổi hàm theo biến vị trí $$x$$ thành hàm theo biến độ dốc $$y$$.
- **Tính lồi tự động:** Dù hàm gốc $$f$$ lồi lõm tùy ý, $$f^*(y)$$ luôn là hàm lồi và đóng. Vì thế, bài toán đối ngẫu lập qua $$f^*$$ luôn có cấu trúc lồi đẹp đẽ.
- **Bất đẳng thức Fenchel–Young:** Với mọi $$x, y$$, ta luôn có $$f(x) + f^*(y) \ge y^T x$$. Dấu bằng xảy ra khi và chỉ khi $$y \in \partial f(x)$$ (tức là $$y$$ là dưới-gradient của $$f$$ tại $$x$$).
- **Định lý Fenchel–Moreau (liên hợp kép):** Nếu $$f$$ là hàm lồi và đóng (nửa liên tục dưới), thì lấy liên hợp hai lần sẽ trả lại chính xác hàm ban đầu: $$f^{**} = f$$.

### Khung giải thích (nên đọc chậm): Tự tay tính hàm liên hợp của hai hàm kinh điển

Hãy tính $$f^*(y) = \sup_x (yx - f(x))$$ cho một hàm trơn và một hàm không trơn (chuẩn $$\ell_1$$) trong 1 chiều:

1. **Hàm bậc hai $$f(x) = \frac{1}{2}ax^2$$ (với $$a > 0$$):**
   - Xét hàm theo $$x$$: $$h(x) = yx - \frac{1}{2}ax^2$$.
   - Đạo hàm $$h'(x) = y - ax = 0 \implies x^\star = \frac{y}{a}$$ (vì $$h''(x) = -a < 0$$ nên đây là cực đại toàn cục).
   - Thay lại: $$f^*(y) = y\left(\frac{y}{a}\right) - \frac{1}{2}a\left(\frac{y}{a}\right)^2 = \frac{y^2}{2a}$$.
   - Kiểm tra nhanh với $$a = 2, x = 3, y = 4$$: $$f(3) = 9$$, $$f^*(4) = \frac{16}{4} = 4$$; vế trái $$f(3) + f^*(4) = 13$$, còn $$yx = 12 \le 13$$ (thỏa Fenchel–Young; dấu bằng đạt khi $$y = ax = 6$$: $$f(3) + f^*(6) = 9 + 9 = 18 = 6 \cdot 3$$).
2. **Hàm giá trị tuyệt đối $$f(x) = \vert x \vert$$:**
   - Ta cần tìm $$\sup_x (yx - \vert x \vert)$$.
   - Nếu $$\vert y \vert \le 1$$: với mọi $$x$$, $$yx \le \vert y \vert \cdot \vert x \vert \le \vert x \vert$$, nên $$yx - \vert x \vert \le 0$$, và đạt giá trị $$0$$ tại $$x = 0$$. Vậy $$f^*(y) = 0$$.
   - Nếu $$\vert y \vert > 1$$ (ví dụ $$y = 2$$): chọn $$x \to +\infty$$ thì $$2x - x = x \to +\infty$$. Vậy $$f^*(y) = +\infty$$.
   - Kết luận: liên hợp của $$\vert x \vert$$ là hàm chỉ thị $$I_{[-1, 1]}(y)$$ của đoạn đơn vị $$[-1, 1]$$!

---

Với một hàm cho trước $$f : \mathbb{R}^n \to \mathbb{R}$$, **hàm liên hợp** (conjugate function) $$f^{*} : \mathbb{R}^n \to \mathbb{R}$$ được định nghĩa như sau:

> $$f^{*}(y) = \max_x (y^Tx - f(x))$$

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter13/conjugate_function.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Minh họa hàm liên hợp [1]</figcaption>
</p>
</figure>

### Lưu ý

Hàm $$f^{*}$$ luôn là hàm lồi vì nó là cực đại theo từng điểm của một họ các hàm affine $$y \mapsto y^Tx - f(x)$$ (ngay cả khi $$f$$ không lồi). Về mặt hình học, $$f^{*}(y)$$ đo khoảng cách cực đại theo phương thẳng đứng giữa hàm tuyến tính $$y^Tx$$ và đồ thị của $$f(x)$$ (Boyd & Vandenberghe, trang 91).

Khi $$f$$ khả vi, phép lấy hàm liên hợp còn được gọi là **biến đổi Legendre**.

#### Tính chất

* **Bất đẳng thức Fenchel:** Với mọi $$x, y$$, ta có $$f(x) + f^{*}(y) \ge x^Ty$$.
> $$f(x) + f^{*}(y) \ge x^Ty \iff f^{*}(y) \ge x^Ty - f(x)$$
> $$f^{*}(y) = \max_z (z^Ty - f(z))$$

* Hàm liên hợp của hàm liên hợp được ký hiệu là $$f^{**}$$, và bất đẳng thức $$f^{**} \le f$$ luôn đúng.<br>
* Nếu $$f$$ là hàm đóng và lồi, thì $$f^{**} = f$$.<br>
* Nếu $$f$$ là hàm đóng và lồi, thì với mọi $$x, y$$ ta có các tương đương sau:<br>
> $$\begin{align}
> x \in \partial f^{*}(y) &\iff y \in \partial f(x) \\\
> &\iff f(x) + f^{*}(y) = x^Ty \\\
> \end{align}$$

* Nếu hàm tách biến theo dạng $$f(u,v) = f_1(u) + f_2(v)$$, thì $$f^{*}(w,z) = f_1^{*}(w) + f_2^{*}(z)$$.

#### Ví dụ

* **Hàm bậc hai:** Xét $$f(x) = \frac{1}{2}x^TQx$$, trong đó $$Q \succ 0$$.

Khi đó, hàm $$x \mapsto y^Tx - \frac{1}{2}x^TQx$$ là hàm lõm chặt theo $$x$$ và đạt cực đại duy nhất tại $$x = Q^{-1}y$$. Thay vào định nghĩa ta được $$f^{*}(y) = \frac{1}{2}y^TQ^{-1}y$$.

### Chứng minh
> $$\begin{align}
> f^{*}(y) & =  \max_x \left( y^Tx -\frac{1}{2}x^TQx \right) \\\
> & = -\min_x \left(\frac{1}{2}x^TQx- y^Tx \right), \quad x^{\star} = Q^{-1}y  \\\
> & = -\frac{1}{2}y^TQ^{-1}QQ^{-1}y + y^TQ^{-1}y \\\
> & = \frac{1}{2}y^TQ^{-1}y  \\\
> \end{align}$$

> Từ đó thu được bất đẳng thức Fenchel tương ứng với mọi $$x, y$$:
> $$\frac{1}{2} x^TQx + \frac{1}{2} y^TQ^{-1}y \ge x^Ty$$

* **Hàm chỉ thị:** Nếu $$f(x) = I_C(x)$$, thì hàm liên hợp của nó là:

> $$f^{*}(y) = I^{*}_C(y) = \max_{x \in C} y^Tx$$ (được gọi là **hàm hỗ trợ** của tập $$C$$).

* **Hàm chuẩn:** Nếu $$f(x) = \|x\|$$, thì hàm liên hợp của nó là:

> $$f^{*}(y) = I_{\{ z : \lVert z \rVert_{*} \le 1 \}}(y)$$, trong đó $$\lVert \cdot \rVert_{*}$$ là chuẩn đối ngẫu của $$\lVert \cdot \rVert$$.

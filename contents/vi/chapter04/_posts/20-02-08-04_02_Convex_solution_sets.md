---
layout: post
title: 04-02 Tập nghiệm lồi
chapter: '04'
order: 3
owner: YoungJae Choung
categories:
- chapter04
lang: vi
lesson_type: required
---

Hãy tưởng tượng bạn thả một viên bi vào một chiếc bát đáy phẳng rồi thả nó vào một địa hình đồi núi lởm chởm. Ở địa hình đồi núi, hai vị trí thấp nhất có thể nằm ở hai thung lũng tách biệt bởi một đỉnh núi cao — đi từ nghiệm này sang nghiệm kia buộc bạn phải leo lên dốc. Nhưng trong chiếc bát lồi đáy phẳng, nếu có hai vị trí cùng thấp nhất, thì toàn bộ đoạn thẳng nối giữa chúng cũng nằm phẳng lì dưới đáy bát!

Đó chính là trực giác tuyệt đẹp đứng sau **tập nghiệm tối ưu của bài toán lồi**: tập $$X_{\text{opt}}$$ luôn là một tập lồi, và ngay khi hàm mục tiêu có độ cong dương chặt (lồi chặt), chiếc bát mất hoàn toàn đáy phẳng — chỉ còn lại **duy nhất một điểm tối ưu** trên toàn không gian.

## Kiến thức cần nhớ: Từ hình học tập lồi đến tính duy nhất của nghiệm

Để hiểu trọn vẹn sức mạnh của hai tính chất tập nghiệm trong bài học này, ta cần đặt chúng trên ba trụ cột:

- **Tổ hợp lồi & Bất đẳng thức Jensen (Convex Combinations):** Nếu $$x, y \in X_{\text{opt}}$$ đều đạt giá trị nhỏ nhất $$f^\star$$, thì mọi điểm giữa $$z = \theta x + (1-\theta)y$$ ($$\theta \in [0,1]$$) vừa thuộc tập khả thi lồi, vừa thỏa $$f(z) \le \theta f(x) + (1-\theta)f(y) = f^\star$$. Bởi $$f^\star$$ đã là nhỏ nhất, dấu bằng buộc phải xảy ra!
- **Tính lồi chặt & Tính duy nhất (Strict Convexity & Uniqueness):** Khi $$f$$ lồi chặt, bất đẳng thức Jensen trở thành bất đẳng thức ngặt $$f(z) < \theta f(x) + (1-\theta)f(y) = f^\star$$ với mọi $$x \neq y$$ và $$\theta \in (0,1)$$. Điều này tạo ra mâu thuẫn ngay lập tức với định nghĩa $$f^\star$$ — chứng minh chỉ có thể tồn tại nhiều nhất một nghiệm.
- **Ý nghĩa trong Học máy & Điều chuẩn (Regularization):** Nhiều bài toán như hồi quy tuyến tính thiếu hạng ($$n < p$$) hay Lasso ($$\ell_1$$) chỉ lồi chứ không lồi chặt, dẫn đến vô số nghiệm tối ưu nằm trên một đa diện lồi. Việc cộng thêm thành phần Ridge $$\frac{\lambda}{2}\|x\|_2^2$$ ($$\lambda > 0$$) làm hàm mục tiêu trở nên lồi chặt, ép tập nghiệm co lại thành một điểm duy nhất ổn định.

### Giải thích: So sánh bài toán có vô số nghiệm lồi và bài toán có nghiệm duy nhất

Xét hai bài toán trên cùng tập khả thi hình vuông $$\mathcal{F} = \{(x_1, x_2) : 0 \le x_1 \le 2,\; 0 \le x_2 \le 2\}$$:

**Bài toán A (Lồi nhưng không lồi chặt):** $$\min_{(x_1, x_2) \in \mathcal{F}} \; f_A(x_1, x_2) = |x_1 + x_2 - 2|.$$
1. Vì $$f_A(x) \ge 0$$ với mọi $$x$$, giá trị nhỏ nhất có thể là $$f_A^\star = 0$$ khi $$x_1 + x_2 = 2$$.
2. Kiểm tra hai nghiệm phân biệt $$x^{(1)} = (2, 0)$$ và $$x^{(2)} = (0, 2)$$: cả hai đều thuộc $$\mathcal{F}$$ và cho $$f_A = 0$$.
3. Lấy trung điểm $$z = 0.5 x^{(1)} + 0.5 x^{(2)} = (1, 1)$$: ta có $$z \in \mathcal{F}$$ và $$f_A(1, 1) = |1 + 1 - 2| = 0 = f_A^\star$$. Tập nghiệm $$X_{\text{opt}}$$ là cả đoạn thẳng nối $$(2,0)$$ đến $$(0,2)$$ — một tập lồi có vô số điểm!

**Bài toán B (Thêm điều chuẩn lồi chặt):** $$\min_{(x_1, x_2) \in \mathcal{F}} \; f_B(x_1, x_2) = |x_1 + x_2 - 2| + 0.1(x_1^2 + x_2^2).$$
1. Thành phần $$0.1(x_1^2 + x_2^2)$$ có Hessian $$0.2 I \succ 0$$ nên $$f_B$$ là hàm **lồi chặt**.
2. Thử tính giá trị trên đoạn thẳng $$x_1 + x_2 = 2$$: tại $$(2, 0)$$ và $$(0, 2)$$, $$f_B = 0 + 0.1(4 + 0) = 0.4$$. Nhưng tại trung điểm $$(1, 1)$$, $$f_B(1, 1) = 0 + 0.1(1 + 1) = 0.2 < 0.4$$!
3. Vì $$f_B$$ lồi chặt, nghiệm tối ưu toàn cục là duy nhất (thực tế nằm tại $$x_1 = x_2 = \frac{1}{1.1} \approx 0.9091$$ nếu tính đạo hàm dọc đường $$x_1 = x_2$$, nhưng trên vùng $$x_1 + x_2 < 2$$ ta có $$f_B(t,t) = (2-2t) + 0.2t^2$$ giảm cho tới $$t=1$$ vì đạo hàm $$-2 + 0.4t < 0$$ với $$t \le 1$$, nên nghiệm duy nhất đúng là $$(1, 1)$$ với $$f_B^\star = 0.2$$!).

---

Phần này trình bày các tính chất cơ bản của tập nghiệm trong một bài toán tối ưu hóa lồi. <br>
Gọi $$X_{opt}$$ là tập nghiệm tối ưu của một bài toán lồi:

>$$
\begin{aligned}
X_{opt} =
&\text{arg}\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, \quad i = 1, \dotsc, m \\
&&&h_{j}(x) = 0, \quad j = 1, \dotsc, r  \\\\
\end{aligned}
$$

## Tính chất chính 1
> $$X_{opt}$$ là một tập lồi.

### Chứng minh
> Giả sử $$x$$ và $$y$$ đều là nghiệm tối ưu của bài toán:
> 1. Vì miền xác định $$D$$ là tập lồi nên với mọi $$0 \le t \le 1$$, ta có $$tx + (1-t)y \in D$$.
> 2. Vì $$g_i$$ ($$i=1,\dotsc,m$$) là các hàm lồi và $$h_j$$ ($$j=1, \dotsc,r$$) là các hàm affine, nên điểm $$tx + (1-t)y$$ cũng thỏa mãn mọi ràng buộc:
    $$
    \begin{aligned}
       g_{i}(tx + (1-t)y) &\leq tg_i(x) + (1-t)g_i(y) \leq 0, \\
       h_{j}(tx + (1-t)y) &= th_j(x) + (1-t)h_j(y) = 0.
    \end{aligned}
    $$
> 3. Vì $$f$$ là hàm lồi, ta có:
    $$
    \begin{aligned}
      f(tx+(1-t)y) &\leq tf(x) + (1-t)f(y) \\
      &= tf^{\star} + (1-t) f^{\star} \\
      &= f^{\star},
    \end{aligned}
    $$
    trong đó $$f^{\star}$$ là giá trị tối ưu của bài toán. Do $$tx + (1-t)y$$ là điểm khả thi nên $$f(tx+(1-t)y) \ge f^{\star}$$, suy ra $$f(tx+(1-t)y) = f^{\star}$$. Vậy $$tx + (1-t)y$$ cũng là một nghiệm tối ưu.

### Giải thích hình học
Với một bài toán tối ưu hóa lồi, mọi cực tiểu địa phương đều là cực tiểu toàn cục. <br>
Nếu tập nghiệm chứa nhiều hơn một phần tử, thì mọi tổ hợp lồi của các nghiệm cũng là nghiệm, nên tập nghiệm có dạng phẳng ở đáy như minh họa dưới đây:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/multiple-optima.png" alt="[Fig1] geometric interpretation of convexity of the solution set">
  <figcaption style="text-align: center;">[Hình 1] Minh họa hình học về tính lồi của tập nghiệm</figcaption>
</p>
</figure>
<br>

## Tính chất chính 2
> Nếu $$f$$ là hàm lồi chặt, thì nghiệm tối ưu (nếu tồn tại) là duy nhất, tức là $$X_{opt}$$ chứa tối đa một phần tử.

Hàm $$f$$ được gọi là lồi chặt nếu với mọi $$x \neq y \in \text{dom } f$$ và mọi $$0 < t < 1$$, ta luôn có:
>$$f(tx + (1-t)y) < tf(x) + (1-t)f(y).$$

Về mặt hình học, đồ thị của hàm lồi chặt cong hướng lên và không chứa bất kỳ đoạn thẳng phẳng nào, do đó bài toán không thể có hai điểm cực tiểu phân biệt.

---
layout: post
title: 04-05 Biến đổi và thay đổi biến
chapter: '04'
order: 6
owner: YoungJae Choung
categories:
- chapter04
lang: vi
---

Trong nhiều bài toán thiết kế mạch điện, quy hoạch mạng truyền thông hay định giá kinh tế, các công thức hiện ra toàn tích lũy thừa như $$x_1^{0.5} x_2^{-1.2} + 3 x_1 x_2 \le 1$$. Nhìn bằng mắt thường, tập khả thi cong queo và hàm mục tiêu hoàn toàn **phi lồi** — ai cũng muốn bỏ cuộc và gọi thuật toán tìm kiếm cục bộ. Thế nhưng chỉ cần đặt $$y_i = \log x_i$$ và lấy logarit hai vế, toàn bộ bức tranh cong queo ấy bỗng "duỗi thẳng" thành một bài toán tối ưu hóa lồi hoàn hảo!

Bài học này trao cho bạn hai chiếc kính biến hình quyền lực nhất trong tối ưu hóa: **biến đổi đơn điệu hàm mục tiêu** (Định lý 1) và **đổi biến song ánh** (Định lý 2). Nắm vững chúng giúp bạn nhận ra rất nhiều bài toán "giả phi lồi" thực chất là bài toán lồi đang cải trang.

## Bản đồ kiến thức nền: Nghệ thuật phát hiện "tính lồi ẩn"

Bốn nguyên tắc dưới đây quyết định khi nào một phép biến đổi giữ nguyên hoàn toàn tập nghiệm tối ưu:

- **Biến đổi đơn điệu tăng của hàm mục tiêu (Monotone Transformation):** Nếu $$h: \mathbb{R} \to \mathbb{R}$$ là hàm tăng ngặt, thì cực tiểu hóa $$f(x)$$ hoàn toàn tương đương với cực tiểu hóa $$h(f(x))$$. Ví dụ kinh điển: thay vì cực tiểu hóa chuẩn Euclidean $$\|Ax - b\|_2$$ (không trơn tại $$0$$), ta cực tiểu hóa $$\|Ax - b\|_2^2$$ (hàm bậc hai trơn đẹp) vì $$h(t) = t^2$$ tăng ngặt trên $$[0, \infty)$$.
- **Đổi biến khả nghịch (Change of Variables):** Thay $$x = \phi(z)$$ với $$\phi$$ là song ánh giữa miền mới và miền cũ biến bài toán theo $$x$$ thành bài toán theo $$z$$. Nghiệm cũ khôi phục ngay lập tức qua $$x^\star = \phi(z^\star)$$.
- **Phép biến đổi Logarit trong Quy hoạch Hình học (Log-Transform / GP):** Đặt $$x_i = e^{y_i}$$ biến mọi tích lũy thừa dương $$c x_1^{a_1} \cdots x_n^{a_n}$$ thành hàm mũ $$e^{a^T y + \log c}$$, rồi lấy $$\log$$ đưa về hàm **log-sum-exp** vốn luôn lồi!
- **Cẩn trọng với tính lồi của ràng buộc:** Biến đổi đơn điệu $$h$$ giữ nguyên *tập nghiệm*, nhưng không tự động biến bài toán thành *lồi* — bạn phải chọn $$h$$ hoặc $$\phi$$ sao cho hàm mục tiêu mới và các hàm ràng buộc mới thực sự lồi.

### Khung giải thích (nên đọc chậm): "Giải mã" một bài toán phi lồi bằng phép đổi biến logarit

Xét bài toán tối ưu trên $$x_1 > 0,\; x_2 > 0$$:
$$\min_{x_1, x_2 > 0} \; f(x_1, x_2) = \frac{1}{x_1 x_2} \quad \text{thỏa mãn} \quad x_1 + 2x_2 \le 4.$$

1. **Nhận diện vẻ ngoài phi lồi:** Đặt $$x_1 = e^{y_1}$$, $$x_2 = e^{y_2}$$ với $$y_1, y_2 \in \mathbb{R}$$.
2. **Chuyển hàm mục tiêu:**
   $$f(e^{y_1}, e^{y_2}) = e^{-y_1 - y_2}.$$
   Lấy $$\log$$ (hàm tăng ngặt trên $$(0, \infty)$$) cho hàm mục tiêu mới cực kỳ đơn giản:
   $$\tilde{f}(y_1, y_2) = \log(e^{-y_1 - y_2}) = -y_1 - y_2 \quad (\text{hàm tuyến tính!}).$$
3. **Chuyển ràng buộc:** $$x_1 + 2x_2 \le 4 \iff e^{y_1} + 2e^{y_2} \le 4$$. Lấy $$\log$$ hai vế:
   $$\log(e^{y_1} + 2e^{y_2}) - \log 4 \le 0.$$
   Hàm $$\log(e^{y_1} + e^{y_2 + \log 2})$$ là hàm log-sum-exp, nên **luôn lồi**!
4. **Giải trực tiếp trên bài toán lồi mới:**
   Muốn cực tiểu hóa $$-y_1 - y_2$$ (tức cực đại hóa $$y_1 + y_2$$) dưới ràng buộc $$e^{y_1} + 2e^{y_2} \le 4$$, bất đẳng thức AM-GM cho $$e^{y_1} + 2e^{y_2} \ge 2\sqrt{2 e^{y_1 + y_2}}$$, dấu bằng xảy ra khi $$e^{y_1} = 2e^{y_2} = 2$$.
   Suy ra $$y_1^\star = \log 2$$, $$y_2^\star = 0$$.
5. **Khôi phục nghiệm gốc:** $$x_1^\star = e^{\log 2} = 2$$, $$x_2^\star = e^0 = 1$$. Kiểm tra ràng buộc gốc: $$2 + 2(1) = 4 \le 4$$, giá trị tối ưu gốc là $$f^\star = \frac{1}{2 \cdot 1} = 0.5$$.

---

Phần này trình bày các kỹ thuật biến đổi hàm và đổi biến trong tối ưu hóa, giúp đơn giản hóa hoặc viết lại bài toán về dạng tương đương thuận lợi hơn.

Bằng cách biến đổi hàm mục tiêu hoặc các hàm ràng buộc mà vẫn giữ nguyên tập nghiệm tương ứng, đôi khi ta có thể phát hiện "tính lồi ẩn" của những bài toán ban đầu trông có vẻ không lồi.

### Định lý 1
Nếu $$h : \mathbb{R} \rightarrow \mathbb{R}$$ là một hàm đơn điệu tăng chặt, thì hai bài toán sau là tương đương:

>$$
>\begin{align}
>   &\min_{x} f(x) \text{ subject to } x \in C \\
>   \Longleftrightarrow \quad &\min_{x} h(f(x)) \text{ subject to } x \in C
>\end{align}
>$$

### Định lý 2
Nếu ánh xạ $$\phi: \mathbb{R}^{n} \rightarrow \mathbb{R}^{m}$$ là một song ánh (hoặc đơn ánh có ảnh bao phủ tập khả thi $$C$$), thì có thể đổi biến bài toán tối ưu hóa như sau:

>$$
>\begin{align}
>    &\min_{x} f(x) \text{ subject to } x \in C \\\\ 
>    \Longleftrightarrow \quad &\min_{y} f(\phi(y)) \text{ subject to } \phi(y) \in C
>\end{align}
>$$

### Ví dụ: Quy hoạch hình học

Một hàm $$f: \mathbb{R}_{++}^n \rightarrow \mathbb{R}$$ có dạng sau được gọi là **đơn thức dương** (monomial):
> $$f(x) = \gamma x_{1}^{a_{1}} x_{2}^{a_{2}} \dotsb x_{n}^{a_{n}} \text{ với } \gamma > 0, \; a_{1}, \dotsc, a_{n} \in \mathbb{R}.$$

Tổng của các đơn thức dương được gọi là **đa thức dương** (posynomial):
> $$g(x) = \sum_{k=1}^{p} \gamma_{k} x_{1}^{a_{k1}} x_{2}^{a_{k2}} \dotsb x_{n}^{a_{kn}} \text{ với } \gamma_{k} > 0, \; a_{k1}, \dotsc, a_{kn} \in \mathbb{R}.$$

Một **bài toán quy hoạch hình học** (geometric program) được phát biểu như sau (dạng gốc không phải là bài toán lồi):
>$$
\begin{align}
&\min_{x} &&f(x) \\
&\text{subject to } &&g_{i}(x) \leq 1, \quad i = 1, \dotsc, m\\
&&&h_{j}(x) = 1, \quad j = 1, \dotsc, r,\\\\
\end{align}
$$

>trong đó $$f$$ và $$g_{i}$$ ($$i=1, \dotsc, m$$) là các đa thức dương, còn $$h_{j}$$ ($$j=1, \dotsc, r$$) là các đơn thức dương.

Hãy chứng minh rằng mọi bài toán quy hoạch hình học đều tương đương với một bài toán tối ưu hóa lồi.

### Chứng minh
> Với một đơn thức dương $$f(x) = \gamma x_{1}^{a_{1}} x_{2}^{a_{2}} \dotsb x_{n}^{a_{n}}$$, đặt phép đổi biến $$y_{i} = \log x_{i}$$ (tức $$x_i = e^{y_i}$$) và $$b = \log \gamma$$. Theo **Định lý 2**, phép đổi biến này bảo toàn tính tương đương của bài toán và đưa $$f$$ về dạng:
> $$\gamma (e^{y_{1}})^{a_{1}} (e^{y_{2}})^{a_{2}} \dotsb (e^{y_{n}})^{a_{n}} = e^{a^Ty + b}.$$
>
> Tương tự, mỗi đa thức dương trở thành $$\sum_{k=1}^{p} e^{a_{k}^{T}y + b_{k}}$$.
>
> Tiếp theo, áp dụng phép biến đổi đơn điệu tăng chặt $$\log(\cdot)$$ theo **Định lý 1**, ta thu được dạng $$\log \big( \sum_{k=1}^{p} e^{a_{k}^{T}y + b_{k}} \big)$$ mà vẫn giữ nguyên tính tương đương của bài toán.
>
> Như vậy, bài toán quy hoạch hình học ban đầu tương đương với bài toán sau, vốn là một bài toán tối ưu hóa lồi (vì hàm log-sum-exp là hàm lồi và ràng buộc đẳng thức là affine):
>
>$$
\begin{align}
&\min_{y} \quad &&{\log \big( \sum_{k=1}^{p_{0}} e^{a_{0k}^{T}y + b_{0k}} \big)} \\
&\text{subject to} &&{
         \log \big( \sum_{k=1}^{p_{i}} e^{a_{ik}^{T}y + b_{ik}} \big)
         \leq 0
         , \quad i = 1, \dotsc, m
}\\
&&&c_{j}^{T}y + d_{j} = 0, \quad j = 1, \dotsc, r.\\\\
\end{align}
$$

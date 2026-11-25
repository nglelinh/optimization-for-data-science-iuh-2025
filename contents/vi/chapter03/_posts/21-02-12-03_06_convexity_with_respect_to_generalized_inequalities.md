---
layout: post
title: 03-06 Tính lồi đối với bất đẳng thức tổng quát
chapter: '03'
order: 14
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Khi tối ưu hóa một hệ thống truyền thông, danh mục đầu tư đa mục tiêu hay thiết kế ma trận hiệp phương sai trong Quy hoạch bán xác định (SDP), hàm mục tiêu không còn trả về một số thực đơn lẻ mà trả về một **vector** hoặc một **ma trận đối xứng**! Làm sao định nghĩa "hàm giá trị ma trận $$f(X) = X^2$$ là hàm lồi"? Ta chỉ cần ghép Chương 02 (bất đẳng thức tổng quát $$\preceq_K$$) với Chương 03 (bất đẳng thức Jensen) để thu được khái niệm **tính lồi theo hình nón $$K$$** ($$K$$-convexity)!

Bài học này tổng quát hóa tính đơn điệu, tính lồi, đặc trưng đối ngẫu và quy tắc hợp thành cho các hàm giá trị vector và ma trận.

## Bản đồ kiến thức nền: Bốn mảnh ghép của Tính lồi theo $$K$$

- **Tính đơn điệu theo $$K$$ ($$K$$-monotonicity):** Với hai hình nón thích hợp $$K_1, K_2$$, hàm $$f$$ gọi là không giảm nếu $$x \preceq_{K_1} y \implies f(x) \preceq_{K_2} f(y)$$. Ví dụ kinh điển: trên $$\mathbb{S}_+^n$$, $$f(X) = X^{-1}$$ là hàm **giảm** theo thứ tự Loewner ($$0 \prec X \preceq Y \implies Y^{-1} \preceq X^{-1}$$).
- **Tính lồi theo $$K$$ ($$K$$-convexity):** $$f(\theta x + (1-\theta)y) \preceq_K \theta f(x) + (1-\theta)f(y)$$ với mọi $$\theta \in [0, 1]$$.
- **Đặc trưng đối ngẫu cực kỳ thanh lịch:** $$f$$ là $$K$$-lồi khi và chỉ khi với **mọi** $$w \succeq_{K^*} 0$$, hàm vô hướng $$w^T f(x)$$ là hàm lồi thông thường! Quy tắc này biến việc kiểm tra tính lồi trên ma trận thành kiểm tra hàm số thực quen thuộc.
- **Điều kiện bậc nhất và hợp thành:** Mở rộng trực tiếp tiếp tuyến $$f(y) \succeq_K f(x) + Df(x)(y - x)$$ và quy tắc hợp thành $$h(g(x))$$ cho hàm nhiều chiều.

### Khung giải thích (nên đọc chậm): Kiểm chứng tính lồi ma trận ($$\mathbb{S}_+^2$$-lồi) của $$f(X) = X^2$$

Xét hàm giá trị ma trận $$f(X) = X^2$$ trên không gian ma trận đối xứng $$\mathbb{S}^2$$ với hình nón $$K = \mathbb{S}_+^2$$. Lấy hai ma trận:
$$A = \begin{pmatrix}2 & 0\\ 0 & 0\end{pmatrix}, \qquad B = \begin{pmatrix}0 & 0\\ 0 & 2\end{pmatrix}, \qquad \theta = 0.5.$$

1. **Tính giá trị tại trung điểm $$M = \frac{A + B}{2}$$:**
   $$M = \begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix} \implies f(M) = M^2 = \begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix}.$$
2. **Tính trung bình hai đầu mút:**
   $$\frac{f(A) + f(B)}{2} = \frac{1}{2}\begin{pmatrix}4 & 0\\ 0 & 0\end{pmatrix} + \frac{1}{2}\begin{pmatrix}0 & 0\\ 0 & 4\end{pmatrix} = \begin{pmatrix}2 & 0\\ 0 & 2\end{pmatrix}.$$
3. **Kiểm tra hiệu theo hình nón $$\mathbb{S}_+^2$$:**
   $$\frac{f(A) + f(B)}{2} - f(M) = \begin{pmatrix}2 & 0\\ 0 & 2\end{pmatrix} - \begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix} = \begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix} \succeq 0.$$
   Vậy $$f\left(\frac{A+B}{2}\right) \preceq_{\mathbb{S}_+^2} \frac{f(A)+f(B)}{2}$$! (Thậm chí chứng minh tổng quát rất đẹp: với mọi $$z \in \mathbb{R}^n$$, $$z^T X^2 z = \|Xz\|_2^2$$ là hàm lồi theo $$X$$, suy ra ngay theo đặc trưng đối ngẫu rằng $$X^2$$ là $$\mathbb{S}_+^n$$-lồi — nhưng chú ý $$X^3$$ lại *không* lồi trên ma trận!)

---

Phần này mở rộng khái niệm tính đơn điệu và tính lồi từ các hàm giá trị thực thông thường sang các hàm giá trị vector thông qua bất đẳng thức tổng quát.

Trong các không gian nhiều chiều, ta dùng hình nón thích hợp để định nghĩa bất đẳng thức tổng quát, mở rộng quan hệ thứ tự quen thuộc trên $$\mathbb{R}$$ (xem bài [02-01-04]({% multilang_post_url contents/chapter02/21-02-08-02_01_04_Convex_cone %})).

## Tính đơn điệu đối với bất đẳng thức tổng quát

Giả sử $$K \subseteq \mathbb{R}^n$$ là một **hình nón thích hợp** sinh ra bất đẳng thức tổng quát $$\preceq_K$$, tức là một hình nón lồi thỏa mãn:

* $$K$$ là tập đóng (chứa biên của nó).
* $$K$$ là hình nón đặc (có phần trong khác rỗng).
* $$K$$ là hình nón nhọn (không chứa đường thẳng nào).

Hàm $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ được gọi là **không giảm theo $$K$$** nếu:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ không giảm theo $$K$$ nếu $$x \preceq_K y \Rightarrow f(x) \leq f(y)$$

Tương tự, $$f$$ được gọi là **tăng theo $$K$$** nếu:
> $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ tăng theo $$K$$ nếu $$x \preceq_K y, x \neq y \Rightarrow f(x) < f(y)$$

### Điều kiện gradient cho tính đơn điệu

Với hàm khả vi một biến $$f : \mathbb{R} \mapsto \mathbb{R}$$ trên một khoảng, $$f$$ không giảm khi và chỉ khi $$f'(x) \geq 0$$ với mọi $$x \in \text{dom}f$$, và nếu $$f'(x) > 0$$ với mọi $$x \in \text{dom}f$$ thì $$f$$ tăng. Khái niệm này mở rộng sang bất đẳng thức tổng quát như sau:

Khi $$\text{dom}f$$ lồi, một hàm khả vi $$f$$ không giảm theo $$K$$ khi và chỉ khi gradient $$\nabla f(x)$$ không âm theo bất đẳng thức tổng quát đối ngẫu:
> Hàm khả vi $$f$$ không giảm theo $$K$$ $$\Longleftrightarrow$$ $$\nabla f(x) \succeq_{K^*} 0$$ với mọi $$x \in \text{dom}f$$

Tương tự, ta có điều kiện đủ cho tính tăng theo $$K$$ (như trường hợp một biến, chiều ngược lại không nhất thiết đúng):
> $$\nabla f(x) \succ_{K^*} 0$$ với mọi $$x \in \text{dom}f$$ $$\Longrightarrow$$ $$f$$ tăng theo $$K$$.

## Tính lồi đối với bất đẳng thức tổng quát

Cho $$K \subseteq \mathbb{R}^m$$ là hình nón thích hợp gắn với bất đẳng thức tổng quát $$\preceq_K$$. Hàm $$f : \mathbb{R}^n \mapsto \mathbb{R}^m$$ được gọi là **lồi theo $$K$$** nếu miền xác định $$\text{dom}f$$ lồi và với mọi $$x, y \in \text{dom}f$$ cùng mọi $$0 \leq \theta \leq 1$$:
> $$f(\theta x + (1 - \theta) y) \preceq_K \theta f(x) + (1 - \theta) f(y)$$

Hàm $$f$$ được gọi là **lồi chặt theo $$K$$** nếu với mọi $$x, y \in \text{dom}f$$ ($$x \neq y$$) và $$0 < \theta < 1$$:
> $$f(\theta x + (1 - \theta) y) \prec_K \theta f(x) + (1 - \theta) f(y)$$

Khi $$m = 1$$ và $$K = \mathbb{R}_+$$, định nghĩa này trở về đúng định nghĩa hàm lồi thông thường.

### Đặc trưng đối ngẫu của tính lồi theo $$K$$

Theo tính chất của bất đẳng thức tổng quát đối ngẫu:
* $$f$$ lồi theo $$K$$ khi và chỉ khi hàm giá trị thực $$w^T f$$ lồi với mọi $$w \succeq_{K^*} 0$$.
* $$f$$ lồi chặt theo $$K$$ khi và chỉ khi hàm giá trị thực $$w^T f$$ lồi chặt với mọi $$w \succeq_{K^*} 0, w \neq 0$$.

<br>

### Hàm lồi theo $$K$$ khả vi

Một hàm khả vi $$f$$ có miền xác định lồi là lồi theo $$K$$ khi và chỉ khi:
> $$f(y) \succeq_K f(x) + Df(x)(y - x)$$ với mọi $$x, y \in \text{dom}f$$

trong đó $$Df(x) \in \mathbb{R}^{m \times n}$$ là ma trận đạo hàm (Jacobian) của $$f$$ tại $$x$$.

Tương tự, $$f$$ lồi chặt theo $$K$$ khi và chỉ khi:
> $$f(y) \succ_K f(x) + Df(x)(y - x)$$ với mọi $$x, y \in \text{dom}f$$, $$x \neq y$$

### Định lý hợp thành

Nhiều quy tắc hợp thành cũng mở rộng cho tính lồi theo $$K$$. Chẳng hạn, nếu $$g : \mathbb{R}^n \mapsto \mathbb{R}^p$$ lồi theo $$K$$, $$h : \mathbb{R}^p \rightarrow \mathbb{R}$$ lồi và phần mở rộng giá trị thực mở rộng $$\widetilde{h}$$ không giảm theo $$K$$, thì hàm hợp $$h \circ g$$ là hàm lồi. Kết quả này tổng quát hóa quy tắc hợp thành của hàm lồi với hàm lồi không giảm. (Điều kiện $$\widetilde{h}$$ không giảm theo $$K$$ đòi hỏi $$h$$ không giảm theo $$K$$ trên $$\text{dom}h$$ và $$\text{dom}h - K = \text{dom}h$$.)

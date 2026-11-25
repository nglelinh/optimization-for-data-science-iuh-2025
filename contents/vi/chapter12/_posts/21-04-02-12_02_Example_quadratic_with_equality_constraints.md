---
layout: post
title: 12-02 Ví dụ bài toán bậc hai với ràng buộc đẳng thức
chapter: '12'
order: 3
owner: Wontak Ryu
categories:
- chapter12
lang: vi
lesson_type: required
---

Nếu có một hệ phương trình xuất hiện ở khắp mọi nơi trong kỹ thuật — từ tối ưu hóa danh mục đầu tư Markowitz, phương pháp Newton có ràng buộc đẳng thức (Chương 14), bộ lọc Kalman, đến cơ học kết cấu phần tử hữu hạn — thì đó chính là **hệ phương trình khối KKT (KKT Matrix System)** của bài toán quy hoạch bậc hai có ràng buộc đẳng thức!

Vẻ đẹp phi thường của ví dụ đầu tiên này nằm ở chỗ: vì bài toán chỉ có ràng buộc đẳng thức $$Ax = b$$ (không có bất đẳng thức $$h_i \le 0$$), điều kiện bù và ràng buộc dấu $$u \ge 0$$ biến mất hoàn toàn! Hai điều kiện KKT còn lại (dừng $$Px^* + q + A^T v^* = 0$$ và khả thi $$Ax^* = b$$) ghép khít vào nhau thành **một hệ phương trình tuyến tính duy nhất** dạng ma trận khối đối xứng. Giải một bài toán tối ưu bậc hai có ràng buộc quy về đúng một phép giải hệ tuyến tính!

## Kiến thức cần nhớ: Ba trụ cột của QP ràng buộc đẳng thức và hệ khối KKT

- **Bài toán QP ràng buộc đẳng thức:** $$\min_x \frac{1}{2}x^T P x + q^T x + r$$ sao cho $$Ax = b$$ với $$P \succeq 0$$ (lồi). Vì mọi ràng buộc đều affine, bài toán lồi tự động thỏa điều kiện Slater tinh gọn nên KKT là điều kiện **cần và đủ**.
- **Hệ phương trình khối KKT (Saddle-point System):**
  $$\begin{bmatrix} P & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x^* \\ v^* \end{bmatrix} = \begin{bmatrix} -q \\ b \end{bmatrix}.$$
  Chú ý rằng ma trận KKT này đối xứng nhưng **không xác định dương** (nó là ma trận bất định — indefinite — có cả trị riêng dương và âm do khối $$0$$ ở góc dưới phải).
- **Điều kiện khả nghịch và phương pháp phần bù Schur (Schur Complement):** Khi $$P \succ 0$$ và $$A$$ có hạng hàng đầy đủ, ma trận khối KKT khả nghịch duy nhất! Ta có thể khử $$x^* = -P^{-1}(q + A^T v^*)$$ rồi thay vào $$Ax^* = b$$ để giải hệ nhỏ hơn $$(A P^{-1} A^T) v^* = -(A P^{-1} q + b)$$ với ma trận Schur $$A P^{-1} A^T \succ 0$$ xác định dương!

### Giải thích: Giải tay hệ ma trận khối KKT cho QP 2 biến

Giải bài toán cực tiểu hóa năng lượng có ràng buộc:
$$\min_{x_1, x_2} \; x_1^2 + 2x_2^2 \quad \text{s.t.} \quad x_1 + x_2 = 3.$$
Ở đây $$f(x) = \frac{1}{2} x^T \begin{pmatrix} 2 & 0 \\ 0 & 4 \end{pmatrix} x$$ nên $$P = \begin{pmatrix} 2 & 0 \\ 0 & 4 \end{pmatrix} \succ 0$$, $$q = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$, $$A = \begin{pmatrix} 1 & 1 \end{pmatrix}$$, $$b = 3$$.

1. **Lập hệ phương trình khối KKT $$3 \times 3$$:**
   $$\begin{pmatrix} 2 & 0 & 1 \\ 0 & 4 & 1 \\ 1 & 1 & 0 \end{pmatrix} \begin{pmatrix} x_1^* \\ x_2^* \\ v^* \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 3 \end{pmatrix}.$$
2. **Giải bằng phép khử Schur (khử $$x_1^*, x_2^*$$ theo $$v^*$$):**
   - Hàng 1: $$2x_1^* + v^* = 0 \implies x_1^* = -\frac{v^*}{2}$$.
   - Hàng 2: $$4x_2^* + v^* = 0 \implies x_2^* = -\frac{v^*}{4}$$.
   - Thay vào hàng 3 ($$x_1^* + x_2^* = 3$$):
     $$-\frac{v^*}{2} - \frac{v^*}{4} = 3 \implies -\frac{3}{4} v^* = 3 \implies v^* = -4.$$
3. **Thay ngược lại tìm $$x^*$$ và kiểm chứng:**
   $$x_1^* = -\frac{-4}{2} = 2, \qquad x_2^* = -\frac{-4}{4} = 1.$$
   Kiểm tra: $$x_1^* + x_2^* = 3$$, giá trị tối ưu $$2^2 + 2(1)^2 = 6$$. Nhận xét vật lý thú vị: biến $$x_1$$ có độ cứng $$2$$ (nhẹ hơn một nửa so với $$x_2$$ có độ cứng $$4$$) nên gánh gấp đôi tải trọng ($$2$$ so với $$1$$)!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Xét một [bài toán quy hoạch bậc hai]() chỉ có các ràng buộc đẳng thức như sau:

>$$
>\begin{align}
>    &\min_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{với điều kiện} &&{Ax = b},\\\\
>&\text{trong đó } &&P \in \mathbb{S}_{+}^n \text{ và } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}
>$$

Bài toán này là bài toán lồi và không có ràng buộc bất đẳng thức, do đó thỏa mãn điều kiện Slater (tức tính đối ngẫu mạnh được đảm bảo). Nếu $$x^\star, \nu^\star$$ là cặp nghiệm tối ưu nguyên thủy và đối ngẫu, theo các điều kiện KKT chúng phải thỏa mãn [1]:

* **Điều kiện dừng:** $$Px^\star + q + A^T\nu^\star = 0$$
* **Điều kiện bù yếu:** Không xuất hiện do bài toán không có ràng buộc bất đẳng thức.
* **Tính khả thi nguyên thủy và đối ngẫu:** $$Ax^\star = b$$

Hệ điều kiện trên có thể viết gọn dưới dạng phương trình ma trận khối, trong đó ma trận hệ số được gọi là **ma trận KKT** [3]:

> $$
> \begin{bmatrix}
>     P       & A^T  \\\\
>     A       & 0  \\\\
> \end{bmatrix}
> \begin{bmatrix}
>     x^\star  \\\\
>     \nu^\star  \\\\
> \end{bmatrix}
> =
> \begin{bmatrix}
>     -q  \\\\
>     b  \\\\
> \end{bmatrix}
> $$

Giải hệ phương trình tuyến tính này cho ta đồng thời nghiệm nguyên thủy $$x^\star$$ và nghiệm đối ngẫu $$\nu^\star$$.

Một điểm đáng chú ý là bài toán trên cũng tương ứng với việc tính bước Newton cho bài toán tối ưu có ràng buộc đẳng thức [3]. Cụ thể, với bài toán $$\min_x f(x) \text{ với điều kiện } Ax = b$$, nếu đặt $$P, q, r$$ theo công thức dưới đây thì hàm mục tiêu của bài toán quy hoạch bậc hai chính là khai triển Taylor bậc hai của $$f$$ tại điểm lặp trước đó $$x^{(k-1)}$$:<br/>
> $$P = \nabla^2 f(x^{(k-1)})$$, $$q = \nabla f(x^{(k-1)})$$, $$r = f(x^{(k-1)})$$
---
layout: post
title: 18-01 Phương trình Secant và Điều kiện Độ cong
chapter: '18'
order: '2'
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Trong không gian 1 chiều, biết hai điểm liên tiếp trên đồ thị đạo hàm là đủ xác định duy nhất một đường cát tuyến có độ dốc $$B_{k+1} = y_k / s_k$$. Nhưng khi bước sang không gian $$n$$ chiều, phương trình cát tuyến $$B_{k+1} s_k = y_k$$ chỉ cung cấp $$n$$ phương trình tuyến tính, trong khi một ma trận đối xứng $$B_{k+1}$$ có tới $$\frac{n(n+1)}{2}$$ ẩn số! Chính sự "thiếu phương trình" này đã mở ra bài toán thú vị nhất của Chương 18: cần bổ sung những điều kiện hình học nào (như điều kiện độ cong $$y_k^T s_k > 0$$) để ma trận $$B_{k+1}$$ vừa xác định dương, vừa giữ lại được tri thức độ cong tích lũy từ các bước trước?

## Kiến thức cần nhớ: Ba trụ cột của phương trình Secant và điều kiện độ cong

Để hiểu sâu cơ sở toán học của mọi công thức cập nhật Quasi-Newton, hãy nắm rõ ba ý tưởng sau:

- **Định lý giá trị trung bình cho ánh xạ gradient:** Theo công thức tích phân Taylor, $$y_k = \nabla f(x_{k+1}) - \nabla f(x_k) = \left(\int_0^1 \nabla^2 f(x_k + \tau s_k)\,d\tau\right) s_k$$. Như vậy, phương trình secant $$B_{k+1} s_k = y_k$$ yêu cầu $$B_{k+1}$$ khớp chính xác với **Hessian trung bình** dọc theo đoạn bước đi $$s_k$$.
- **Điều kiện độ cong $$y_k^T s_k > 0$$ và tính xác định dương:** Muốn tồn tại ma trận đối xứng xác định dương $$B_{k+1} \succ 0$$ thỏa mãn $$B_{k+1} s_k = y_k$$, điều kiện cần và đủ là $$s_k^T y_k = s_k^T B_{k+1} s_k > 0$$. Về mặt hình học, điều này nghĩa là đạo hàm theo hướng $$s_k$$ phải tăng lên khi ta đi từ $$x_k$$ sang $$x_{k+1}$$ (hàm cong lên dọc theo hướng đi).
- **Vai trò của điều kiện Wolfe với hàm không lồi:** Với hàm lồi chặt, $$y_k^T s_k > 0$$ luôn tự động đúng. Với hàm không lồi tổng quát, điều kiện độ cong Wolfe $$\nabla f(x_{k+1})^T s_k \ge c_2 \nabla f(x_k)^T s_k$$ (với $$c_2 \in (0, 1)$$) chính là chốt chặn bảo đảm $$y_k^T s_k \ge (c_2 - 1)\nabla f(x_k)^T s_k > 0$$.

### Giải thích: Tính tay cặp $$(s, y)$$ và kiểm chứng điều kiện độ cong trên mặt paraboloid 2D

Xét hàm bậc hai lồi chặt 2 biến $$f(x_1, x_2) = x_1^2 + 3x_2^2$$, có gradient $$\nabla f(x) = (2x_1, \; 6x_2)^T$$ và Hessian thực không đổi $$G = \begin{bmatrix} 2 & 0 \\ 0 & 6 \end{bmatrix}$$. Giả sử ta bước từ $$x^0 = (1, 1)^T$$ tới $$x^1 = (0, 0.5)^T$$:

1. **Tính vector bước đi $$s^0$$ và biến thiên gradient $$y^0$$:**
   - $$s^0 = x^1 - x^0 = (0 - 1, \; 0.5 - 1)^T = (-1, \; -0.5)^T$$.
   - $$\nabla f(x^0) = (2, 6)^T$$, $$\nabla f(x^1) = (0, 3)^T$$.
   - $$y^0 = \nabla f(x^1) - \nabla f(x^0) = (-2, \; -3)^T$$.
2. **Kiểm tra điều kiện độ cong:**
   $$(y^0)^T s^0 = (-2)(-1) + (-3)(-0.5) = 2 + 1.5 = 3.5 > 0.$$
   Điều kiện độ cong thỏa mãn chặt chẽ, chứng tỏ chắc chắn tồn tại ma trận đối xứng xác định dương $$B^1$$ thỏa mãn phương trình secant!
3. **Kiểm tra phương trình secant với Hessian thực:**
   $$G s^0 = \begin{bmatrix} 2 & 0 \\ 0 & 6 \end{bmatrix} \begin{bmatrix} -1 \\ -0.5 \end{bmatrix} = \begin{bmatrix} -2 \\ -3 \end{bmatrix} = y^0.$$
4. **Thấy ngay tính "thiếu ẩn":** Ma trận đường chéo $$B_{\text{khác}} = \begin{bmatrix} 2 & 0 \\ 0 & 6 \end{bmatrix}$$ không phải nghiệm duy nhất! Chẳng hạn $$B_{\text{mới}} = \begin{bmatrix} 1.5 & 1 \\ 1 & 8 \end{bmatrix}$$ cũng đối xứng, xác định dương ($$\det = 12 - 1 = 11 > 0$$) và thỏa mãn $$B_{\text{mới}} s^0 = (-1.5 - 0.5, \; -1 - 4)^T = (-2, \; -5)^T$$ (chưa khớp), còn nếu chọn $$B_{\text{mới}} = \begin{bmatrix} 1.5 & 1 \\ 1 & 4 \end{bmatrix}$$ thì $$B_{\text{mới}} s^0 = (-2, \; -3)^T = y^0$$ và $$\det = 6 - 1 = 5 > 0$$! Vì có vô số ma trận $$B^1 \succ 0$$ thỏa mãn secant, các bài tiếp theo (SR1, DFP, BFGS) sẽ đặt thêm nguyên lý "thay đổi ít nhất so với $$B^0$$".

---

# Phương trình Secant

Như đã trình bày ở phần trước, $$B$$ là ma trận xấp xỉ Hessian $$\nabla^2 f(x)$$. Để $$B$$ mang các tính chất tương tự Hessian thực, nó cần thỏa mãn một điều kiện gọi là **phương trình secant (secant equation)**.

Với $$x^{k+1} = x^k + s^k$$ và $$f$$ khả vi hai lần, khai triển Taylor bậc nhất của $$\nabla f(x^k + s^k)$$ cho thấy Hessian thực thỏa mãn xấp xỉ:

>$$
\nabla f(x^k + s^k) \approx \nabla f(x^k) + \nabla^2 f(x^k) s^k$$

Thay $$\nabla^2 f(x^k)$$ bằng ma trận xấp xỉ mới $$B^{k+1}$$, ta yêu cầu phương trình sau được thỏa mãn chính xác:

>$$
\nabla f(x^k + s^k) = \nabla f(x^k) + B^{k+1} s^k$$

Đặt $$s^k = x^{k+1} - x^k$$ và $$y^k = \nabla f(x^{k+1}) - \nabla f(x^k)$$, phương trình trên được viết gọn thành **phương trình secant**:

>$$
B^{k+1} s^k = y^k
$$

# Ý nghĩa hình học của phương trình Secant

Trong trường hợp một chiều với $$x$$ là trục hoành và $$\nabla f(x)$$ là trục tung, $$B^{k+1}$$ chính là hệ số góc của cát tuyến đi qua hai điểm $$(x^k, \nabla f(x^k))$$ và $$(x^{k+1}, \nabla f(x^{k+1}))$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/intuition_of_secant_eq.png" alt="[Fig1] Trực quan về phương trình secant" width="70%">
  <figcaption style="text-align: center;">[Fig1] Trực quan về phương trình secant</figcaption>
</p>
</figure>

# Các điều kiện xác định $$B^+$$

Từ ma trận $$B$$ hiện tại, ta đặt ra ba yêu cầu để xác định ma trận cập nhật $$B^+$$:

1. **$$B^+$$ đối xứng:** Phản ánh tính đối xứng của ma trận Hessian.
2. **$$B^+$$ gần $$B$$ nhất:** Giúp xác định duy nhất $$B^+$$. Vì $$B$$ đã tích lũy thông tin độ cong từ các bước trước, ta chọn ma trận gần $$B$$ nhất (theo một chuẩn thích hợp) trong số các ma trận thỏa mãn phương trình secant.
3. **Bảo toàn tính xác định dương ($$B \succ 0 \Rightarrow B^+ \succ 0$$):** Đảm bảo hướng cập nhật $$p = -(B^+)^{-1}\nabla f(x)$$ luôn là hướng giảm của hàm mục tiêu (tham khảo: [Phân tích Hessian](https://web.stanford.edu/group/sisl/k12/optimization/MO-unit4-pdfs/4.10applicationsofhessians.pdf)).

# Điều kiện độ cong (Curvature Condition)

Nếu $$B^+$$ xác định dương và thỏa mãn phương trình secant $$B^+ s = y$$, thì nhất thiết phải có:

>$$
s^T y = s^T B^+ s > 0.
$$

(tham khảo: [Ma trận xác định dương trên Wikipedia](https://en.wikipedia.org/wiki/Positive-definite_matrix))

Bất đẳng thức $$s^T y > 0$$ được gọi là **điều kiện độ cong (curvature condition)**. Khi điều kiện này thỏa mãn (và $$s \neq 0$$), luôn tồn tại ma trận đối xứng xác định dương $$B^+$$ thỏa mãn phương trình secant $$B^+ s = y$$.
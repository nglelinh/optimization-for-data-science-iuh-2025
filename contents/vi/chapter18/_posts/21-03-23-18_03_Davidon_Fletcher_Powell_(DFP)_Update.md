---
layout: post
title: 18-03 Cập nhật Davidon-Fletcher-Powell (DFP)
chapter: '18'
order: 4
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Vì cập nhật hạng 1 (SR1) không đủ bậc tự do để vừa khớp phương trình secant vừa luôn bảo toàn tính xác định dương, W. C. Davidon (1959) — sau đó được R. Fletcher và M. J. D. Powell (1963) làm sáng tỏ và phổ biến — đã chuyển sang **cập nhật đối xứng hạng 2** trực tiếp trên ma trận nghịch đảo Hessian $$H = B^{-1}$$. Công thức DFP mở ra một bước ngoặt lịch sử: chỉ cần điều kiện độ cong $$y^T s > 0$$ được giữ vững, ma trận $$H^+$$ **luôn luôn** xác định dương, đảm bảo hướng tìm kiếm $$-H^+ \nabla f$$ không bao giờ đi ngược lên dốc!

## Bản đồ kiến thức nền: Bốn góc nhìn giúp hiểu trọn vẹn công thức DFP

Thay vì học thuộc lòng hai phân số trong công thức DFP, hãy nhìn bản chất hình học và biến phân đằng sau nó:

- **Cập nhật trực tiếp nghịch đảo Hessian $$H^+ = H + auu^T + bvv^T$$:** Chọn hai hướng tự nhiên nhất là $$u = s$$ (bước đi thực tế) và $$v = Hy$$ (bước đi mà xấp xỉ cũ $$H$$ dự đoán) cho phép trừ đi phần sai lệch cũ $$-\frac{Hyy^T H}{y^T H y}$$ và cộng vào thông tin độ cong mới $$+\frac{ss^T}{y^T s}$$.
- **Bảo toàn tính xác định dương (Hereditary Positive Definiteness):** Nhờ bất đẳng thức Cauchy–Schwarz trên tích vô hướng cảm sinh bởi $$H \succ 0$$, nếu $$y^T s > 0$$ thì $$z^T H^+ z > 0$$ với mọi $$z \ne 0$$. Không còn nỗi lo hướng đi bị đảo dấu như ở SR1!
- **Diễn giải biến phân (Minimum-Change Principle):** Công thức DFP cho $$B^+$$ thực chất là nghiệm duy nhất của bài toán tìm ma trận đối xứng $$B^+$$ thỏa mãn $$B^+ s = y$$ có khoảng cách chuẩn Frobenius có trọng số $$\|W^{1/2}(B^+ - B)W^{1/2}\|_F$$ nhỏ nhất — tức "sửa đổi $$B$$ ít nhất có thể".
- **Hạn chế thực nghiệm so với BFGS:** Dù đẹp về lý thuyết, DFP nhạy cảm hơn với tìm kiếm đường thẳng không chính xác (inexact line search) và đôi khi bị kẹt khi xấp xỉ Hessian sinh ra trị riêng quá nhỏ — lý do mà BFGS dần thay thế nó ở bài tiếp theo.

### Khung giải thích (nên đọc chậm): Tính tay một bước DFP cho $$H$$ và kiểm tra $$H^+ y = s$$

Khởi tạo $$H_0 = I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$ với cặp bước đi và biến thiên gradient $$s = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$, $$y = \begin{bmatrix} 2 \\ 1 \end{bmatrix}$$:

1. **Kiểm tra điều kiện độ cong và tính các đại lượng vô hướng:**
   - $$y^T s = (2)(1) + (1)(0) = 2 > 0$$ (đảm bảo $$H_1 \succ 0$$!).
   - $$H_0 y = y = (2, 1)^T \implies y^T H_0 y = 2^2 + 1^2 = 5$$.
2. **Tính hai số hạng hiệu chỉnh hạng 1:**
   - Số hạng trừ: $$-\frac{(H_0 y)(H_0 y)^T}{y^T H_0 y} = -\frac{1}{5}\begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} -0.8 & -0.4 \\ -0.4 & -0.2 \end{bmatrix}$$.
   - Số hạng cộng: $$+\frac{ss^T}{y^T s} = +\frac{1}{2}\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0.5 & 0 \\ 0 & 0 \end{bmatrix}$$.
3. **Cộng vào $$H_0 = I$$ để thu được $$H_1$$:**
   $$H_1 = \begin{bmatrix} 1 - 0.8 + 0.5 & 0 - 0.4 + 0 \\ 0 - 0.4 + 0 & 1 - 0.2 + 0 \end{bmatrix} = \begin{bmatrix} 0.7 & -0.4 \\ -0.4 & 0.8 \end{bmatrix}.$$
4. **Kiểm chứng phương trình secant ngược $$H_1 y = s$$ và tính xác định dương:**
   - $$H_1 y = \begin{bmatrix} 0.7 & -0.4 \\ -0.4 & 0.8 \end{bmatrix}\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 1.4 - 0.4 \\ -0.8 + 0.8 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} = s$$ — chính xác tuyệt đối!
   - Định thức $$\det(H_1) = (0.7)(0.8) - (-0.4)^2 = 0.56 - 0.16 = 0.40 > 0$$ và vết $$= 1.5 > 0$$, khẳng định $$H_1 \succ 0$$.

---

Cập nhật DFP là phương pháp cập nhật ma trận xấp xỉ nghịch đảo Hessian $$H = B^{-1}$$ bằng một ma trận đối xứng hạng 2:

>$$H^+ = H + auu^T + bvv^T.$$

Nếu $$H^+$$ thỏa mãn phương trình secant ($$B^+ s = y \Leftrightarrow H^+ y = s$$), thì $$s - Hy$$ phải là một tổ hợp tuyến tính của $$u$$ và $$v$$:

>$$H^+y = Hy + auu^Ty + bvv^Ty = Hy + (au^Ty)u + (bv^Ty)v = s$$
>
>$$\Rightarrow s - Hy = (au^Ty)u + (bv^Ty)v$$

Chọn $$u = s, v = Hy$$ rồi giải tìm hai hệ số $$a$$ và $$b$$, ta thu được công thức cập nhật DFP cho $$H$$:
>$$
> H^+ = H - \frac{Hyy^TH}{y^THy} + \frac{ss^T}{y^Ts}
>$$

Tương tự trường hợp SR1, áp dụng [công thức Sherman–Morrison](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula) (hai lần), ta suy ra công thức cập nhật tương ứng cho $$B$$:

>$$
>\begin{align}
>B^+ &= B + \frac{(y-Bs)y^T}{y^Ts} + \frac{y(y-Bs)^T}{y^Ts} - \frac{(y-Bs)^Ts}{(y^Ts)^2} yy^T\\\\
> &= \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts} 
>\end{align}
>$$

Khi $$B$$ xác định dương và điều kiện độ cong $$y^Ts > 0$$ được thỏa mãn, số hạng thứ nhất $$\big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big)$$ và số hạng thứ hai $$\frac{yy^T}{y^Ts}$$ đều nửa xác định dương, đồng thời với mọi $$z \neq 0$$ hai dạng toàn phương tương ứng không thể đồng thời triệt tiêu (vì $$y^Tz = 0 \Rightarrow z^TB^+z = z^TBz > 0$$). Nhờ đó, $$B^+$$ luôn được đảm bảo xác định dương, khắc phục nhược điểm của SR1.

## Suy luận thay thế cho cập nhật DFP

Nhắc lại rằng nếu điều kiện độ cong $$y^Ts > 0$$ ($$y, s \in \mathbb{R}^n$$) được thỏa mãn, thì tồn tại ma trận đối xứng xác định dương thỏa mãn phương trình secant.

Cập nhật DFP còn có thể được suy ra trực tiếp bằng cách cực tiểu hóa khoảng cách theo chuẩn Frobenius có trọng số giữa $$B^+$$ và $$B$$ dưới hai ràng buộc: (1) $$B^+$$ đối xứng và (2) $$B^+$$ thỏa mãn phương trình secant. (Mỗi chuẩn ma trận khác nhau dẫn tới một công thức Quasi-Newton khác nhau; chuẩn Frobenius có trọng số vừa dễ giải giải tích vừa đảm bảo tính bất biến theo tỷ lệ của phương pháp.)

>Giải bài toán:
>$$
>\begin{align}
>& \min_{B^+} \: \: && {\|W^{1/2} (B^+ - B) W^{1/2} \|_F} \\\\
>& \text{thỏa mãn } && {B^+ = (B^+)^T} \\\\
>    &&& {B^+s = y}  \\\\
>& \text{trong đó } && W \in \mathbb{R}^{n \; \times \;n} \text{ là ma trận đối xứng xác định dương thỏa mãn } Wy_k = s_k.
>\end{align}\\\\
>$$

**Tham khảo:**

* **Chuẩn Frobenius:** Chuẩn Frobenius của ma trận $$A$$ được định nghĩa là:
$$
\| A \|_{F}  \doteq \left( \sum_{i,j} A_{i,j}^2 \right)^{1/2}
$$

* **Chuẩn Frobenius có trọng số:** Với ma trận trọng số $$W \succ 0$$, chuẩn Frobenius có trọng số của $$A$$ được định nghĩa là:
$$
\|A\|_W \doteq \| W^{1/2} A W^{1/2} \|_F
$$
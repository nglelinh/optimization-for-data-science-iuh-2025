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
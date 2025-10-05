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

Cập nhật DFP là một phương pháp cập nhật $$H (=B^{-1})$$ với một ma trận đối xứng hạng-2.

>$$H^+ = H + auu^T + bvv^T.$$

Nếu $$H^+$$ được tính thông qua cập nhật DFP thỏa mãn phương trình secant, thì $$s-Hy$$ có thể được biểu diễn dưới dạng tổ hợp tuyến tính của $$u$$ và $$v$$. (tham khảo: theo phương trình secant, $$B^+ s =y \Leftrightarrow H^+ y = s$$)

>$$H^+y = Hy + auu^Ty + bvv^Ty = Hy + (au^Ty)u + (bv^Ty)v = s$$
>
>$$\Rightarrow s - Hy = (au^Ty)u + (bv^Ty)v$$

Đặt $$u=s, v=Hy$$ và giải cho $$a$$ và $$b$$, chúng ta suy ra công thức cập nhật cho $$H$$.
>$$
> H^+ = H - \frac{Hyy^TH}{y^THy} + \frac{ss^T}{y^Ts}
>$$

Tương tự như cập nhật SR1, chúng ta có thể suy ra công thức cập nhật cho $$B$$ bằng cách sử dụng [công thức Sherman–Morrison](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula).

>$$
>\begin{align}
>B^+ &= B + \frac{(y-Bs)y^T}{y^Ts} + \frac{y(y-Bs)^T}{y^Ts} - \frac{(y-Bs)^Ts}{(y^Ts)^2} yy^T\\\\
> &= \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts} 
>\end{align}
>$$

Nếu $$B$$ là xác định dương, thì $$\big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big)$$ trở thành nửa xác định dương. Trong trường hợp này, nếu $$\frac{yy^T}{y^Ts}$$ là xác định dương, thì $$B^+ = \big( I - \frac{ys^T}{y^Ts} \big) B \big( I - \frac{sy^T}{y^Ts} \big) + \frac{yy^T}{y^Ts}$$ được đảm bảo là xác định dương. Điều này giải quyết vấn đề duy trì tính xác định dương đã được nêu ra với SR1.

## Cập nhật DFP - Suy luận Thay thế

Nhớ lại: nếu điều kiện độ cong ($$y^Ts > 0, y,s \in \mathbb{R}^n$$) được thỏa mãn, thì tồn tại một ma trận đối xứng xác định dương thỏa mãn phương trình secant.

Cập nhật DFP cũng có thể được suy ra bằng cách giải bài toán cực tiểu hóa chuẩn Frobenius có trọng số giữa ma trận $$B^+$$ và $$B$$ trong đó $$B^+$$ 1. thỏa mãn tính đối xứng và 2. thỏa mãn phương trình secant. (Mỗi chuẩn ma trận khác nhau tương ứng với mỗi phương pháp Quasi-Newton khác nhau. Trong số đó, chuẩn làm cho việc giải quyết bài toán này dễ dàng đồng thời cũng làm cho nó hoạt động như một phương pháp tối ưu bất biến tỷ lệ là chuẩn Frobenius có trọng số.)

>Giải
>$$
>\begin{align}
>& \min_{B^+} \: \: && {\|W^{1/2} (B^+ - B) W^{1/2} \|_F} \\\\
>& \text{thỏa mãn } && {B^+ = (B^+)^T} \\\\
>    &&& {B^+s = y}  \\\\
>& \text{trong đó } && W \in \mathbb{R}^{n \; \times \;n} \text{ là ma trận khả nghịch và } Wy_k = s_k.
>\end{align}\\\\
>$$

***Tham khảo**:

* Chuẩn Frobenius: Chuẩn Frobenius của ma trận $$A$$ được định nghĩa như sau.
$$
\| A \|_{F}  \doteq ( \sum_{i,j} A_{i,j}^2 )^{1/2}
$$

* Chuẩn Frobenius có trọng số: Chuẩn Frobenius có trọng số của ma trận $$A$$ với ma trận trọng số $$W(W \succ 0)$$ được định nghĩa như sau. 
$$
\|A\|_W \doteq \| W^{1/2} A W^{1/2} \|_F
$$
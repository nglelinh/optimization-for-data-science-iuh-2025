---
layout: post
title: 18-04 Cập nhật Broyden-Fletcher-Goldfarb-Shanno (BFGS)
chapter: '18'
order: '5'
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Năm 1970, một sự trùng hợp kỳ diệu xảy ra trong lịch sử tối ưu hóa: bốn nhà toán học — Charles Broyden, Roger Fletcher, Donald Goldfarb và David Shanno — đã độc lập công bố cùng một công thức cập nhật chỉ trong vòng vài tháng! Họ đơn giản chỉ hoán đổi vai trò của $$B$$ và $$H$$ trong công thức DFP, đặt bài toán "thay đổi ít nhất" lên ma trận nghịch đảo $$H^+$$ thay vì $$B^+$$. Thế nhưng sự hoán đổi tưởng chừng đối xứng hoàn toàn ấy lại tạo ra **thuật toán Quasi-Newton thành công nhất mọi thời đại**: BFGS tự hiệu chỉnh sai số độ cong vượt trội hơn hẳn DFP và vẫn là bộ giải mặc định trong `scipy.optimize` suốt hơn nửa thế kỷ.

## Kiến thức cần nhớ: Vì sao BFGS trở thành tiêu chuẩn vàng của tối ưu hóa trơn?

Bốn trụ cột sau giải thích sức mạnh cả về đại số lẫn thực nghiệm của công thức BFGS:

- **Đối ngẫu cấu trúc với DFP:** Công thức BFGS cho $$B^+$$ có dạng y hệt công thức DFP cho $$H^+$$ (chỉ đổi $$H \leftrightarrow B, s \leftrightarrow y$$), và ngược lại công thức BFGS cho $$H^+$$ là dạng nhân hai bên $$(I - \rho s y^T) H (I - \rho y s^T) + \rho s s^T$$ với $$\rho = 1/(y^T s)$$.
- **Bảo toàn tính xác định dương miễn là $$y^T s > 0$$:** Viết $$z^T H^+ z = [(I - \rho y s^T)z]^T H [(I - \rho y s^T)z] + \rho (s^T z)^2$$ cho thấy ngay tổng hai số hạng không âm chỉ bằng $$0$$ khi $$z = 0$$ (vì $$H \succ 0$$ và $$\rho > 0$$).
- **Khả năng tự hiệu chỉnh (Self-Correcting Property):** Khi xấp xỉ Hessian $$B_k$$ dự đoán độ cong quá lớn (hoặc $$H_k$$ có trị riêng quá nhỏ làm bước đi bị kẹt), BFGS tự động sửa lại trị riêng xấu chỉ sau vài vòng lặp dưới tìm kiếm đường thẳng không chính xác, trong khi DFP có thể ì ạch rất lâu.
- **Nền tảng cho L-BFGS quy mô lớn:** Dạng nhân hai bên $$H^+ = V^T H V + \rho s s^T$$ cho phép khai triển đệ quy $$H_k \nabla f_k$$ mà không cần lưu ma trận $$n \times n$$ — chìa khóa trực tiếp dẫn sang L-BFGS ở bài 18-07.

### Giải thích: Tính tay một bước BFGS trên đúng dữ liệu bài DFP và so sánh trực tiếp

Dùng lại đúng dữ liệu ở bài 18-03: $$B_0 = H_0 = I$$, $$s = (1, 0)^T$$, $$y = (2, 1)^T$$ ($$y^T s = 2 \implies \rho = 0.5$$):

1. **Tính $$B_1$$ theo công thức BFGS:**
   - Ta có $$s^T B_0 s = 1$$, $$B_0 s = (1, 0)^T$$.
   - $$B_1 = I - \frac{(B_0 s)(B_0 s)^T}{s^T B_0 s} + \frac{yy^T}{y^T s} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} + \frac{1}{2}\begin{bmatrix} 4 & 2 \\ 2 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 \end{bmatrix}.$$
2. **Kiểm chứng phương trình secant và tính xác định dương:**
   - $$B_1 s = (2, 1)^T = y$$ — khớp chính xác!
   - $$\det(B_1) = (2)(1.5) - 1 = 2 > 0$$, vết $$= 3.5 > 0 \implies B_1 \succ 0$$.
3. **Tính $$H_1$$ trực tiếp bằng công thức BFGS hai bên và đối chiếu với $$B_1^{-1}$$:**
   - Ma trận $$V = I - \rho s y^T = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - 0.5\begin{bmatrix} 2 & 1 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & -0.5 \\ 0 & 1 \end{bmatrix}$$.
   - $$H_1 = V I V^T + 0.5 s s^T = \begin{bmatrix} 0.25 & -0.5 \\ -0.5 & 1 \end{bmatrix} + \begin{bmatrix} 0.5 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0.75 & -0.5 \\ -0.5 & 1 \end{bmatrix}.$$
   - Nhân thử kiểm chứng: $$B_1 H_1 = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 \end{bmatrix}\begin{bmatrix} 0.75 & -0.5 \\ -0.5 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$$!
4. **So sánh với DFP:** Trên cùng dữ liệu, DFP cho $$H_1^{\text{DFP}} = \begin{bmatrix} 0.7 & -0.4 \\ -0.4 & 0.8 \end{bmatrix}$$ (tức $$B_1^{\text{DFP}} = \begin{bmatrix} 2 & 1 \\ 1 & 1.75 \end{bmatrix}$$), còn BFGS cho $$B_1^{\text{BFGS}} = \begin{bmatrix} 2 & 1 \\ 1 & 1.5 \end{bmatrix}$$ — hai ma trận chỉ khác nhau ở phần tử góc dưới bên phải, chính là hướng vuông góc với $$s$$!

---

Ý tưởng của cập nhật BFGS hoàn toàn tương tự DFP, chỉ khác ở chỗ vai trò của $$B$$ và $$H$$ được hoán đổi cho nhau. Công thức BFGS được suy ra bằng cách giải bài toán tối ưu sau:

>Giải bài toán:
>$$
>\begin{align}
>& \min_{H^+} \: \: && {\|W^{1/2} (H^+ - H) W^{1/2} \|_F} \\\\
>& \text{thỏa mãn } && {H^+ = (H^+)^T} \\\\
>    &&& {H^+y = s}  \\\\
>& \text{trong đó } && W \in \mathbb{R}^{n \; \times \;n} \text{ là ma trận đối xứng xác định dương thỏa mãn } Ws_k = y_k.
>\end{align}\\\\
>$$

Từ đây, ta thu được công thức cập nhật cho $$B$$ và $$H$$:

>$$
>B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts}
>$$

và

>$$
>\begin{align}
>H^+ &= H + \frac{(s-Hy)s^T}{y^Ts} + \frac{s(s-Hy)^T}{y^Ts} - \frac{(s-Hy)^Ty}{(y^Ts)^2} ss^T\\\\
> &= \big( I - \frac{sy^T}{y^Ts} \big) H \big( I - \frac{ys^T}{y^Ts} \big) + \frac{ss^T}{y^Ts}
>\end{align}
>$$

Tương tự DFP, BFGS bảo toàn tính xác định dương: nếu $$B \succ 0$$ và điều kiện độ cong $$s^Ty > 0$$ được thỏa mãn, thì $$B^+ \succ 0$$ (và tương ứng $$H \succ 0 \Rightarrow H^+ \succ 0$$).

Ưu điểm nổi bật của BFGS là **khả năng tự hiệu chỉnh (self-correcting)**: nếu ma trận $$H$$ ở một vòng lặp là xấp xỉ kém của Hessian nghịch đảo, các bước cập nhật tiếp theo có thể nhanh chóng điều chỉnh lại sai lệch này. Trong khi đó, DFP kém hiệu quả hơn nhiều trong việc tự hiệu chỉnh xấp xỉ Hessian kém, nên trên thực tế BFGS thường cho hiệu năng vượt trội hơn [14].

### BFGS so với gradient descent (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/bfgs-vs-gd_vi.mp4"></video>
</div>

BFGS chỉ dùng thông tin gradient để dựng dần ma trận xấp xỉ Hessian nghịch đảo $$H$$, giúp bước đi $$-H\nabla f$$ tiệm cận hướng Newton mà không cần tính trực tiếp Hessian.

### Tự tay thử: BFGS so với gradient descent

<div class="opx-explainer" data-opx="bfgs" data-lang="vi"></div>

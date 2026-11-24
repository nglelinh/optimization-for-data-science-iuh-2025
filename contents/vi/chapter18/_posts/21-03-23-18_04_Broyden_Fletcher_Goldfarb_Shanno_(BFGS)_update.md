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

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

Ý tưởng của BFGS giống như DFP. Sự khác biệt duy nhất là vai trò của B và H được đảo ngược. BFGS được suy ra bằng cách giải bài toán sau.

>Giải
>$$
>\begin{align}
>& \min_{H^+} \: \: && {\|W^{1/2} (H^+ - H) W^{1/2} \|_F} \\\\
>& \text{thỏa mãn } && {H^+ = (H^+)^T} \\\\
>    &&& {H^+y = s}  \\\\
>& \text{trong đó } && W \in \mathbb{R}^{n \; \times \;n} \text{ là ma trận khả nghịch và } Ws_k = y_k.
>\end{align}\\\\
>$$

Các công thức cập nhật được suy ra cho $$H$$ và $$B$$ như sau.

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

BFGS cũng duy trì tính xác định dương giống như DFP. (Nếu $$B$$ là xác định dương và $$s^Ty > 0$$, thì $$B^+$$ là xác định dương.)

Ưu điểm của BFGS là có tính chất tự hiệu chỉnh. Nếu ma trận $$H$$ trong một vòng lặp là một xấp xỉ kém của Hessian nghịch đảo, thì $$H$$ có thể được điều chỉnh trong một vài bước tiếp theo. DFP không có khả năng tự hiệu chỉnh trong trường hợp xấp xỉ sai về Hessian, do đó hiệu suất của BFGS thường tốt hơn [14].

### Quasi-Newton trong 15 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/bfgs-vs-gd_vi.mp4"></video>
</div>

BFGS chỉ dùng các gradient để dựng dần một xấp xỉ Hessian nghịch đảo $$H$$, nên bước đi $$-H\nabla f$$ gần giống Newton mà không cần tính Hessian.

### Tự tay thử: BFGS so với gradient descent

<div class="opx-explainer" data-opx="bfgs" data-lang="vi"></div>

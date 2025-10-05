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

Ưu điểm của BFGS là có tính chất tự hi교chỉnh. Nếu ma trận $$H$$ trong một vòng lặp là một xấp xỉ kém của Hessian nghịch đảo, thì $$H$$ có thể được điều chỉnh trong một vài bước tiếp theo. DFP không có khả năng tự hiệu chỉnh trong trường hợp xấp xỉ sai về Hessian, do đó hiệu suất của BFGS thường tốt hơn [14].
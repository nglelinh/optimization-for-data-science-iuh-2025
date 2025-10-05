---
layout: post
title: 18-02 Cập nhật Hạng-một Đối xứng (SR1)
chapter: '18'
order: 3
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Cập nhật SR1 là một phương pháp cập nhật $$B$$ với một ma trận đối xứng hạng-1 sao cho $$B^+$$ duy trì tính đối xứng và tiếp tục thỏa mãn phương trình secant. Nếu một ma trận đối xứng hạng-1 được phân tích thành tích của $$a \in \left\{-1, 1\right\}$$ và $$u \in \mathbb{R^n}$$, dạng cập nhật sẽ như sau.

>$$B^+ = B + auu^T.$$

## Quan sát Chính
$$a$$ và $$u$$ phải được chọn sao cho $$B^+$$ thỏa mãn phương trình secant. Do đó, hãy thay thế dạng cập nhật được giới thiệu ở trên vào phương trình secant $$y = B^+s$$.

>$$y = B^+s \Rightarrow y = Bs + (au^Ts)u. \quad \text{--- (1)}$$

Vì $$(au^Ts)$$ là một số vô hướng, $$u$$ cũng có thể được biểu diễn dưới dạng tích của $$y-Bs$$ và một số vô hướng tùy ý $$\delta$$ $$\big( u = \delta(y - Bs) \big)$$. Hãy thay thế $$u$$ trong (1) bằng $$\delta(y - Bs)$$.

>$$y-Bs = a\delta^2 \big[ s^T(y - Bs) \big] (y -Bs),$$

Các tham số $$\delta$$ và $$a$$ thỏa mãn phương trình trên như sau.

>$$a = \text{sign} \big[ s^T (y - Bs) \big], \quad \delta = \pm | s^T(y-Bs) |^{-1/2}. \quad \text{--- (2)}$$

## Công thức Cập nhật SR1 Duy nhất
Sử dụng thông tin thu được từ quan sát chính, chúng ta có thể suy ra dạng duy nhất của cập nhật SR1 ([14] mục 6.2). <br/>
$$\big( u = \delta (y - Bs)$$ và thay thế (2) vào $$B^+ = B + auu^T$$. $$\big)$$

>$$
>B^+ = B + \frac{(y-Bs)(y-Bs)^T}{(y-Bs)^Ts}.
>$$
>

## Công thức Cập nhật cho Xấp xỉ Nghịch đảo Hessian

Để tìm $$x^+$$, chúng ta cần tính $$B^{-1}$$.

>$$x^+ = x + tp = x - tB^{-1}\nabla f(x)$$

Nếu chúng ta có thể cập nhật $$B^{-1}$$ thay vì $$B$$, liệu chúng ta có thể giảm chi phí tính toán $$B^{-1}$$ mỗi lần không?

Sử dụng [công thức Sherman–Morrison](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula), chúng ta có thể thấy qua quá trình suy luận rằng $$B^{-1}$$ cũng có thể được cập nhật dưới cùng một dạng. ($$H = B^{-1}$$)

>$$
>H^+ = H + \frac{(s-Hy)(s-Hy)^T}{(s-Hy)^Ty}.
>$$

## Nhược điểm của SR1

SR1 có ưu điểm là rất đơn giản, nhưng nó có hai nhược điểm nghiêm trọng.

1. Việc cập nhật có thể thất bại khi $$(y-Bs)^Ts$$ tiến về 0.
2. Nó không thể duy trì tính xác định dương của $$B$$ và $$H$$.

Các phần sau đây giới thiệu các phương pháp bổ sung cho những nhược điểm của SR1.
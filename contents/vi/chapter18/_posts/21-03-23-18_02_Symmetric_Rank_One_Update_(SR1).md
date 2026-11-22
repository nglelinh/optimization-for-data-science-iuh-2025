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

Cập nhật hạng-một đối xứng (Symmetric Rank-One — SR1) cộng thêm vào $$B$$ một ma trận đối xứng hạng 1 sao cho $$B^+$$ giữ được tính đối xứng và thỏa mãn phương trình secant. Biểu diễn ma trận đối xứng hạng 1 dưới dạng tích của $$a \in \left\{-1, 1\right\}$$ và vector $$u \in \mathbb{R}^n$$, công thức cập nhật có dạng:

>$$B^+ = B + auu^T.$$

## Quan sát chính
Ta cần chọn $$a$$ và $$u$$ để $$B^+$$ thỏa mãn phương trình secant $$y = B^+s$$. Thay dạng cập nhật trên vào phương trình secant:

>$$y = B^+s \Rightarrow y = Bs + (au^Ts)u. \quad \text{--- (1)}$$

Vì $$au^Ts$$ là một đại lượng vô hướng, vector $$u$$ phải cùng phương với $$y - Bs$$, tức là $$u = \delta(y - Bs)$$ với $$\delta$$ là một số thực khác 0. Thay $$u = \delta(y - Bs)$$ vào (1):

>$$y-Bs = a\delta^2 \big[ s^T(y - Bs) \big] (y -Bs),$$

Để đẳng thức trên đúng (khi $$y - Bs \neq 0$$ và $$s^T(y - Bs) \neq 0$$), ta cần chọn $$a$$ và $$\delta$$ như sau:

>$$a = \text{sign} \big[ s^T (y - Bs) \big], \quad \delta = \pm | s^T(y-Bs) |^{-1/2}. \quad \text{--- (2)}$$

## Công thức cập nhật SR1 duy nhất
Thay $$u = \delta (y - Bs)$$ cùng các giá trị trong (2) vào $$B^+ = B + auu^T$$, ta thu được công thức cập nhật SR1 duy nhất ([14] mục 6.2):

>$$
>B^+ = B + \frac{(y-Bs)(y-Bs)^T}{(y-Bs)^Ts}.
>$$

## Công thức cập nhật cho xấp xỉ nghịch đảo Hessian

Để tính bước cập nhật $$x^+$$, ta cần tác động của $$B^{-1}$$:

>$$x^+ = x + tp = x - tB^{-1}\nabla f(x)$$

Nếu có thể cập nhật trực tiếp $$H = B^{-1}$$ thay vì cập nhật $$B$$ rồi giải hệ tuyến tính, ta sẽ tránh được chi phí nghịch đảo ma trận ở mỗi vòng lặp. Áp dụng [công thức Sherman–Morrison](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula), ta thu được công thức cập nhật tương ứng cho $$H = B^{-1}$$ có cấu trúc hoàn toàn tương tự:

>$$
>H^+ = H + \frac{(s-Hy)(s-Hy)^T}{(s-Hy)^Ty}.
>$$

## Nhược điểm của SR1

Dù rất đơn giản, cập nhật SR1 có hai nhược điểm đáng kể:

1. Phép cập nhật có thể mất ổn định hoặc không xác định khi mẫu số $$(y - Bs)^Ts$$ tiến về $$0$$.
2. Không đảm bảo bảo toàn tính xác định dương của $$B$$ và $$H$$ (ngay cả khi điều kiện độ cong $$s^Ty > 0$$ được thỏa mãn).

Các phần tiếp theo sẽ trình bày những công thức cập nhật khắc phục hai hạn chế này của SR1.
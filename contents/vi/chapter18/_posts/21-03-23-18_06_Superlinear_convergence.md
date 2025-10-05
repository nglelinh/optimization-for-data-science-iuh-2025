---
layout: post
title: 18-06 Hội tụ Siêu tuyến tính
chapter: '18'
order: '7'
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

# Giả thiết 1:
> Ma trận Hessian $$G$$ là liên tục Lipschitz tại $$x^∗$$, nghĩa là,
> $$\| G(x) − G(x^∗) \| \le L \| x − x^∗ \|,
>$$
với mọi $$x$$ gần $$x^∗$$, trong đó $$L$$ là một hằng số dương.

# Giả thiết 2: Điều kiện Wolfe
> Giả sử $$t$$ được chọn (thông qua backtracking) sao cho
> $$
f(x + tp) \le f(x) + \alpha_1 t \nabla f(x)^T p
>$$
và
> $$
\nabla f(x + tp)^T p \ge \alpha_2 \nabla f(x)^T p
>$$
với $$0 < \alpha_1 < \alpha_2 < 1.$$

* Điều kiện đầu tiên của điều kiện Wolfe đảm bảo rằng $$t$$ không được chọn quá lớn.
* Điều kiện thứ hai của điều kiện Wolfe đảm bảo rằng $$t$$ không được chọn quá nhỏ.

DFP và BFGS cho thấy hội tụ siêu tuyến tính dưới hai giả thiết trên. (tham khảo: [Tốc độ hội tụ trên Wikipedia](https://en.wikipedia.org/wiki/Rate_of_convergence))

>$$
>\lim_{k \rightarrow \infty} \frac{ \| x^{k+1} - x^\ast \| }{ \| x^k - x^\ast \| } = 0.
>$$

# Định lý Dennis-Moré

Khi hướng tìm kiếm của phương pháp Quasi-Newton xấp xỉ đủ tốt hướng Newton tại nghiệm và độ dài bước thỏa mãn điều kiện Wolfe trong quá trình hội tụ, thì tồn tại điều kiện đủ cho hướng tìm kiếm để có hội tụ siêu tuyến tính [14].

>Giả sử $$f$$ khả vi, $$x^k \rightarrow x^\ast$$ sao cho $$\nabla f(x^\ast) = 0$$ và $$\nabla^2 f(x^\ast)$$ là xác định dương.
>
>$$
\lim_{k \rightarrow \infty} \frac{\| \nabla f(x^k) + \nabla^2 f(x^k) p^k \| }{\| p^k \|} = 0.
>$$
>
>Nếu hướng tìm kiếm $$p^k$$ thỏa mãn điều kiện trên, thì tồn tại $$k_0$$ sao cho:
>
> 1. Với $$k \ge k_0$$, độ dài bước $$t_k=1$$ thỏa mãn điều kiện Wolfe.
> 2. Nếu vậy, với $$k \ge k_0$$ và $$t_k = 1$$, thì $$x^k \rightarrow x^\ast$$ với hội tụ siêu tuyến tính.
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
> Ma trận Hessian $$G$$ liên tục Lipschitz tại $$x^*$$, nghĩa là tồn tại hằng số dương $$L$$ sao cho:
> $$\| G(x) - G(x^*) \| \le L \| x - x^* \|$$
với mọi $$x$$ đủ gần $$x^*$$.

# Giả thiết 2: Điều kiện Wolfe
> Giả sử độ dài bước $$t$$ được chọn (thông qua tìm kiếm theo đường thẳng) sao cho thỏa mãn đồng thời hai bất đẳng thức:
> $$
f(x + tp) \le f(x) + \alpha_1 t \nabla f(x)^T p
>$$
và
> $$
\nabla f(x + tp)^T p \ge \alpha_2 \nabla f(x)^T p
>$$
với $$0 < \alpha_1 < \alpha_2 < 1$$.

* Điều kiện Wolfe thứ nhất (điều kiện giảm đủ) đảm bảo độ dài bước $$t$$ không quá lớn.
* Điều kiện Wolfe thứ hai (điều kiện độ cong) đảm bảo độ dài bước $$t$$ không quá nhỏ.

Dưới hai giả thiết trên, cả DFP và BFGS đều đạt tốc độ hội tụ siêu tuyến tính (tham khảo: [Tốc độ hội tụ trên Wikipedia](https://en.wikipedia.org/wiki/Rate_of_convergence)):

>$$
>\lim_{k \rightarrow \infty} \frac{ \| x^{k+1} - x^\ast \| }{ \| x^k - x^\ast \| } = 0.
>$$

# Định lý Dennis–Moré

Định lý Dennis–Moré cung cấp điều kiện đủ (và cần) cho hướng tìm kiếm của phương pháp Quasi-Newton đạt hội tụ siêu tuyến tính khi hướng đó tiệm cận đủ sát hướng Newton gần nghiệm [14]:

> Giả sử $$f$$ khả vi liên tục hai lần, dãy $$x^k \rightarrow x^\ast$$ với $$\nabla f(x^\ast) = 0$$ và $$\nabla^2 f(x^\ast)$$ xác định dương. Xét điều kiện:
>
>$$
\lim_{k \rightarrow \infty} \frac{\| \nabla f(x^k) + \nabla^2 f(x^k) p^k \| }{\| p^k \|} = 0.
>$$
>
> Nếu hướng tìm kiếm $$p^k$$ thỏa mãn điều kiện trên, thì tồn tại chỉ số $$k_0$$ sao cho:
>
> 1. Với mọi $$k \ge k_0$$, độ dài bước đơn vị $$t_k = 1$$ thỏa mãn điều kiện Wolfe.
> 2. Khi chọn $$t_k = 1$$ với mọi $$k \ge k_0$$, dãy $$x^k$$ hội tụ siêu tuyến tính về $$x^\ast$$.
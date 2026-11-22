---
layout: post
title: 13-01 Ứng dụng của đối ngẫu
chapter: '13'
order: 2
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

### Hai ứng dụng chính của đối ngẫu

Hãy cùng điểm lại hai tính chất ứng dụng chính của lý thuyết đối ngẫu đã giới thiệu ở Chương 11.

* **Khoảng cách đối ngẫu làm tiêu chí dừng:** Khi $$x$$ khả thi nguyên thủy và $$(u, v)$$ khả thi đối ngẫu, hiệu giữa giá trị mục tiêu nguyên thủy $$f(x)$$ và giá trị hàm đối ngẫu $$g(u, v)$$ được gọi là **khoảng cách đối ngẫu** (duality gap) giữa $$x$$ và $$(u, v)$$:

> $$f(x) - f^{\star} \le f(x) - g(u, v)$$

Khi khoảng cách đối ngẫu bằng $$0$$ (zero duality gap), nghiệm nguyên thủy và nghiệm đối ngẫu đều đạt tối ưu. Ngoài ra, giá trị hàm đối ngẫu $$g(u, v)$$ luôn là một **cận dưới** của giá trị tối ưu $$f^{\star}$$ (tức $$g(u, v) \le f^{\star}$$); xem lại chi tiết tại [[Chương 11]]({% multilang_post_url contents/chapter11/21-03-24-11_00_Duality_in_General_Programs %}). Từ đó ta có suy dẫn sau:

#### Chứng minh
> $$\begin{align*}
> f^{\star} &\ge g(u, v) \\
> -f^{\star} &\le -g(u, v) \\
> f(x)-f^{\star} &\le \underbrace{f(x)-g(u, v)}_{\text{khoảng cách đối ngẫu}}\\
> g^{\star}-g(u, v) &\le \underbrace{f(x)-g(u, v)}_{\text{khoảng cách đối ngẫu}}\\
> \end{align*}$$

Nhờ chặn trên sai số tối ưu này, khoảng cách đối ngẫu thường được dùng trực tiếp làm tiêu chí dừng cho các thuật toán tối ưu hóa.

* **Tìm nghiệm nguyên thủy thông qua nghiệm đối ngẫu:** Khi tính đối ngẫu mạnh được thỏa mãn và ta đã biết nghiệm đối ngẫu tối ưu $$(u^{\star}, v^{\star})$$, nghiệm nguyên thủy tối ưu $$x^{\star}$$ phải cực tiểu hóa hàm Lagrangian $$L(x, u^{\star}, v^{\star})$$ theo $$x$$ (tức thỏa mãn điều kiện dừng). Tính chất này cho phép suy ra nghiệm nguyên thủy từ nghiệm đối ngẫu.

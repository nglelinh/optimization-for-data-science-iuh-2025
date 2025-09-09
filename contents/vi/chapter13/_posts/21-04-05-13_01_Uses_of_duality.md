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
Hãy cùng xem lại hai đặc điểm chính của đối ngẫu đã được đề cập trong Chương 11.

• Khi $$x$$ là khả thi nguyên thủy và $$u,v$$ là khả thi đối ngẫu, hiệu số giữa bài toán nguyên thủy $$f(x)$$ và bài toán đối ngẫu $$g(u,v)$$ được gọi là **khoảng cách đối ngẫu** (duality gap) giữa $$x$$ và $$u,v$$.
> $$f(x)-f^{\star}  \le f(x)-g(u, v)$$

Khi khoảng cách đối ngẫu bằng 0, điều này được gọi là khoảng cách đối ngẫu bằng không, có nghĩa là nghiệm của bài toán đối ngẫu là tối ưu.
Ngoài ra, cận trên $$g(u, v)$$ luôn nhỏ hơn hoặc bằng giá trị tối ưu $$f^{\star}$$. Để biết lý do chi tiết, vui lòng tham khảo nội dung trong [[Chương 11]]({% multilang_post_url contents/chapter11/21-03-24-11_00_Duality_in_General_Programs %}).
Do đó, có thể thực hiện suy luận sau đây.

#### [Chứng minh]
> $$\begin{align*}
> f^{\star} &\ge g(u, v) \\
> -f^{\star} &\le -g(u, v) \\
> f(x)-f^{\star} &\le \underbrace{f(x)-g(u, v)}_{\text{khoảng cách đối ngẫu}}\\
> g^{\star}-g(x) &\le \underbrace{f(x)-g(u, v)}_{\text{khoảng cách đối ngẫu}}\\
> \end{align*}$$


Hơn nữa, khoảng cách đối ngẫu có thể được sử dụng làm tiêu chí dừng cho các thuật toán.
• Khi nghiệm đối ngẫu tối ưu $$u^{\star}, v^{\star}$$ được cho, trong điều kiện đối ngẫu mạnh, nghiệm nguyên thủy tối thiểu hóa Lagrangian $$L (x, u^{\star}, v^{\star})$$ cho tất cả $$x$$ (tức là thỏa mãn điều kiện dừng).

Điều này có thể được sử dụng để tính toán nghiệm nguyên thủy.

---
layout: post
title: '19-04 Phân tích hội tụ'
chapter: '19'
order: 8
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Để phân tích sự hội tụ của phương pháp Newton proximal, chúng ta trình bày theo chứng minh của Lee, Sun và Saunders (2014) [1].

[1] J. Lee, Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions".

Xét các giả thiết sau:

* $$f = g + h$$, trong đó $$g$$ và $$h$$ lồi, còn $$g$$ khả vi hai lần (trơn).
* $$mI \preceq \nabla^2 g(x) \preceq LI$$ (với $$0 < m \le L$$).
* Hessian $$\nabla^2 g(x)$$ liên tục Lipschitz với hằng số $$M$$.
* Ánh xạ $$\text{prox}_H(\cdot)$$ được tính chính xác ở mỗi vòng lặp.

Các giả thiết trên kéo theo $$f$$ lồi mạnh (nên có nghiệm tối ưu duy nhất); giả thiết tính chính xác $$\text{prox}_H(\cdot)$$ được đặt ra để thuận tiện cho phân tích lý thuyết (trường hợp tính gần đúng sẽ xét ở phần sau).
 
## Định lý hội tụ

> **Phương pháp Newton proximal** kết hợp backtracking line search hội tụ toàn cục, và đạt tốc độ hội tụ bậc hai cục bộ:
> \begin{align}
\parallel x^{(k)} - x^{\star} \parallel_2 \le \frac{M}{2m} \parallel x^{(k-1)} - x^{\star} \parallel_2^2
\end{align}

Sau một số hữu hạn bước $$k \ge k_0$$, để đạt $$f(x^{(k)}) - f^{\star} \le \epsilon$$ chỉ cần $$O(\log \log (1/\epsilon))$$ vòng lặp ngoài (lưu ý mỗi vòng lặp đòi hỏi đánh giá một ánh xạ prox có tỉ lệ).

## Phác thảo chứng minh
Để chứng minh **hội tụ toàn cục**, ta chỉ ra rằng ở mọi vòng lặp, điều kiện dừng của backtracking line search luôn được thỏa mãn khi độ dài bước $$t$$ thỏa mãn:

> \begin{align}
t \le \min \left\\{ 1, \frac{2m}{L} (1-\alpha) \right\\} \\\\
\end{align}

Từ cận dưới dương này của độ dài bước, có thể suy ra hướng cập nhật hội tụ về $$0$$ và dãy lặp hội tụ về cực tiểu toàn cục $$x^{\star}$$.

Để chứng minh **hội tụ bậc hai cục bộ**, khi điểm lặp đã đủ gần $$x^{\star}$$, bước đơn vị $$t = 1$$ luôn được chấp nhận bởi backtracking line search và bất đẳng thức sau được thỏa mãn:

> $$
> \begin{align}
> \parallel x^{+} - x^{\star} \parallel_2 & \le \frac{1}{\sqrt{m}} \parallel x^{+} - x^{\star} \parallel_H \\\\
> & =  \frac{1}{\sqrt{m}} \parallel \text{prox}_H(x - H^{-1} \nabla g(x) )  - \text{prox}_H(x^{\star} - H^{-1} \nabla g(x^{\star}) )  \parallel_H \\\\
> & \le \frac{M}{2m} \parallel x - x^{\star} \parallel_2^2 \\\\
> \end{align}
> $$

Tóm gọn lại:

> \begin{align}
\parallel x^{+} - x^{\star} \parallel_2 \ \le \ \frac{1}{\sqrt{m}} \parallel x^{+} - x^{\star} \parallel_H \  \le \ \frac{M}{2m} \parallel x - x^{\star} \parallel_2^2
\end{align}

* Bất đẳng thức đầu tiên sử dụng cận dưới trị riêng $$mI \preceq H$$, còn đẳng thức suy ra từ định nghĩa của $$x^+$$ và tính chất điểm bất động của nghiệm tối ưu $$x^{\star} = \text{prox}_H(x^{\star} - H^{-1}\nabla g(x^{\star}))$$.

* Bất đẳng thức thứ hai sử dụng tính không giãn của toán tử proximal theo chuẩn $$H$$, tính chất Lipschitz bậc hai với hằng số $$M$$ của $$\nabla^2 g$$ và cận dưới trị riêng $$m$$.

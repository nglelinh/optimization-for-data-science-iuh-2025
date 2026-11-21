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

Để phân tích sự hội tụ của phương pháp Newton proximal, chúng ta sẽ đi theo chứng minh của Lee (2014) [1].

[1] J. Lee and Y. Sun and M. Saunders (2014), Proximal Newton-type methods for minimizing

Để chứng minh sự hội tụ, ta đưa ra các giả thiết sau:

* $$f = g + h$$, $$g$$ và $$h$$ lồi và $$g$$ khả vi hai lần (trơn)
* $$mI \preceq \nabla^2 g(x) \preceq LI$$.
* $$\nabla^2 g(x)$$ Lipschitz với hằng số $$M$$
* $$\text{prox}_H(\cdot)$$ có thể được tính chính xác

Các giả thiết trên kéo theo hàm là lồi chặt; còn giả thiết $$\text{prox}_H(\cdot)$$ có thể được tính chính xác được đưa ra vì điều này không dễ đạt được trong thực tế.
 
## Định lý hội tụ

> **Phương pháp Newton proximal** hội tụ toàn cục khi dùng backtracking line search, và
> \begin{align}
\parallel x^{(k)} - x^{\star} \parallel_2 \le \frac{M}{2m} \parallel x^{(k-1)} - x^{\star} \parallel_2^2
\end{align}

Điều này được gọi là **hội tụ bậc hai cục bộ (local quadratic convergence)**. Sau $$k \ge k_0$$, để thỏa mãn $$f(x^{(k)}) - f^{\star} \le \epsilon$$ cần $$O(\log \log (1/\epsilon))$$ vòng lặp. Tuy nhiên, mỗi vòng lặp dùng một prox có tỉ lệ.

## Phác thảo chứng minh
Để chứng minh **hội tụ toàn cục**, ta có thể chỉ ra rằng ở bất kỳ bước nào, điều kiện thoát backtracking đối với kích thước bước $$t$$ được thỏa mãn như sau.

> \begin{align}
t \le \min \left\\{ 1, \frac{2m}{L} (1-\alpha) \right\\} \\\\
\end{align}

Với bất đẳng thức này, ta có thể chỉ ra rằng khi đạt cực tiểu toàn cục thì hướng cập nhật hội tụ về 0.

Để chứng minh **hội tụ bậc hai cục bộ**, sau đủ nhiều vòng lặp, bước Newton thuần túy $$t=1$$ thỏa mãn các điều kiện thoát backtracking, và bất đẳng thức sau đúng.

> $$
> \begin{align}
> \parallel x^{+} - x^{\star} \parallel_2 & \le \frac{1}{\sqrt(m)} \parallel x^{+} - x^{\star} \parallel_H \\\\
> & =  \frac{1}{\sqrt(m)} \parallel \text{prox}_H(x - H^{-1} \nabla g(x) )  - \text{prox}_H(x^{\star} - H^{-1} \nabla g(x^{\star}) )  \parallel_H \\\\
> & \le \frac{M}{2m} \parallel x - x^{\star} \parallel_2^2 \\\\
> \end{align}
> $$

Tóm tắt lại, ta được:

> \begin{align}
\parallel x^{+} - x^{\star} \parallel_2 \ \le \ \frac{1}{\sqrt(m)} \parallel x^{+} - x^{\star} \parallel_H \  \le \ \frac{M}{2m} \parallel x - x^{\star} \parallel_2^2
\end{align}

* Bất đẳng thức đầu tiên đúng nhờ cận giá trị riêng nhỏ nhất, và đẳng thức đúng vì $$\text{prox}_H(\cdot)$$ trở thành phép đồng nhất tại điểm $$x^+$$ và cực tiểu toàn cục $$x^{\star}$$ (theo định nghĩa của chúng).

* Bất đẳng thức thứ hai đúng nhờ tính không giãn của toán tử proximal, giả thiết Lipschitz và cận giá trị riêng lớn nhất.

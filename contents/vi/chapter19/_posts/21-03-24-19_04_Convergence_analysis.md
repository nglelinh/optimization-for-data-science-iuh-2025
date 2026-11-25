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

Nhìn vào bài toán tổng hợp $$f(x) = g(x) + h(x)$$, nhiều người từng nghi ngờ: *sự có mặt của hàm không khả vi $$h(x)$$ có phá hỏng tốc độ hội tụ bậc hai trứ danh của phương pháp Newton không?* Định lý kinh điển của Lee, Sun và Saunders (2014) đã đưa ra câu trả lời đầy bất ngờ: **KHÔNG!** Miễn là phần trơn $$g$$ lồi mạnh và có Hessian liên tục Lipschitz, phương pháp Newton proximal vẫn thừa kế nguyên vẹn hai giai đoạn hội tụ của Newton cổ điển — hội tụ toàn cục nhờ backtracking, rồi bứt tốc **hội tụ bậc hai cục bộ** với bước đơn vị $$t_k = 1$$!

## Kiến thức cần nhớ: Bốn giả thiết và cơ chế chứng minh hội tụ bậc hai

Để nắm chắc định lý hội tụ của Lee, Sun và Saunders (2014), hãy xem vai trò chính xác của từng giả thiết:

- **Lồi mạnh và trơn của $$g$$ ($$mI \preceq \nabla^2 g(x) \preceq LI$$):** Đảm bảo Hessian $$H_k$$ luôn khả nghịch và có số điều kiện bị chặn bởi $$L/m$$, đồng thời nghiệm tối ưu $$x^\star$$ là duy nhất.
- **Hessian liên tục Lipschitz ($$\|\nabla^2 g(x) - \nabla^2 g(y)\|_2 \le M\|x - y\|_2$$):** Khống chế sai số của mô hình bậc hai cục bộ ở bậc $$O(\|x - x^\star\|^2)$$, là nguồn gốc trực tiếp tạo ra số mũ bình phương trong hội tụ bậc hai.
- **Tính điểm bất động và không giãn của $$\operatorname{prox}_H$$:** Nghiệm tối ưu $$x^\star$$ chính là điểm bất động $$x^\star = \operatorname{prox}_H(x^\star - H^{-1}\nabla g(x^\star))$$. Kết hợp với tính không giãn theo chuẩn $$H$$ giúp đánh giá trực tiếp $$\|x^+ - x^\star\|_H$$ theo sai số bậc hai của gradient!
- **Trường hợp giải gần đúng bài toán con (Inexact Proximal Newton):** Trong thực tế không ai giải bài toán con chính xác tuyệt đối. Miễn là sai số bài toán con giảm nhanh tỉ lệ với $$\|v^{(k)}\|$$ (tiêu chuẩn cưỡng bức Eisenstat–Walker), thuật toán vẫn giữ được hội tụ siêu tuyến tính hoặc bậc hai!

### Giải thích: Theo dõi con số hội tụ bậc hai qua công thức $$\|x^{(k+1)} - x^\star\| \le \frac{M}{2m}\|x^{(k)} - x^\star\|^2$$

Giả sử một bài toán tổng hợp có các hằng số $$m = 1$$ (lồi mạnh), $$M = 2$$ (Lipschitz của Hessian). Khi đó hệ số hội tụ bậc hai là $$C = \frac{M}{2m} = \frac{2}{2(1)} = 1$$, và vùng hội tụ bậc hai bắt đầu khi $$e_k = \|x^{(k)} - x^\star\|_2 < \frac{1}{C} = 1$$ (với $$t_k = 1$$).

Hãy theo dõi sai số $$e_k$$ bắt đầu từ lúc thuật toán vừa bước vào vùng cục bộ với $$e_0 = 0.1$$:

1. **Vòng lặp 1:** $$e_1 \le 1 \cdot (0.1)^2 = 10^{-2}$$ (2 chữ số chính xác).
2. **Vòng lặp 2:** $$e_2 \le 1 \cdot (10^{-2})^2 = 10^{-4}$$ (4 chữ số chính xác).
3. **Vòng lặp 3:** $$e_3 \le 1 \cdot (10^{-4})^2 = 10^{-8}$$ (8 chữ số chính xác).
4. **Vòng lặp 4:** $$e_4 \le 1 \cdot (10^{-8})^2 = 10^{-16}$$ — **chạm giới hạn độ chính xác dấu phẩy động 64-bit (machine epsilon) chỉ sau 4 vòng lặp!**

So sánh với Proximal Gradient trên cùng bài toán (giả sử $$L = 10$$, tỉ lệ co $$1 - m/L = 0.9$$): muốn giảm sai số từ $$0.1$$ xuống $$10^{-16}$$, PGD cần tới $$\frac{\ln(10^{15})}{\ln(1/0.9)} \approx \mathbf{328}$$ vòng lặp! Đó chính là sức mạnh của tốc độ $$O(\log\log(1/\epsilon))$$.

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

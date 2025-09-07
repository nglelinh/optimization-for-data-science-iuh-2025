---
layout: post
title: 06-03-01 Cận trên bậc hai của hàm lồi
chapter: '06'
order: 8
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

## Cận Trên Bậc Hai

Nếu $$f$$ là lồi và $$\nabla f$$ liên tục Lipschitz, thì $$f$$ có cận trên bậc hai sau (trong đó $$L$$ là hằng số Lipschitz):

> $$ \begin{align}
f(y) & \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2 \quad \forall x, y
\end{align} $$

Ngoài ra, đối với bất kỳ hàm lồi $$g$$ nào, hàm $$f$$ có cận trên bậc hai:

> $$ \begin{align}
g(x) & = \frac{L}{2} \| x \|^2_2 - f(x) \quad \text{là lồi với mọi } x \text{ với } dom(g) = dom(f)
\end{align} $$

## Chứng minh

### Toán tử Đơn điệu
Nếu $$f$$ là lồi, thì $$\nabla f(x)$$ là một toán tử đơn điệu:

> $$(\nabla f(y) - \nabla f(x))^T (y-x) \ge 0$$

Tham khảo: Trong không gian vector $$X$$, toán tử $$T : X \to X^*$$ là đơn điệu nếu:
> $$(Tu - Tv, u-v) \ge 0$$, $$\forall u, v \in X$$

### Liên tục Lipschitz
$$\nabla f$$ liên tục Lipschitz với hằng số $$L$$:
>$$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2 $$ với mọi $$x, y$$

### Chứng minh $$g$$ là lồi
Đặt $$g(x) = \frac{L}{2} \| x \|^2_2 - f(x)$$. Sử dụng bất đẳng thức Cauchy-Schwarz, chúng ta có thể chỉ ra:
> $$ \begin{align}
(\nabla f(x) - \nabla f(y))^T (x-y) & \le \| \nabla f(x) - \nabla f(y) \| \| x - y \| \le L \| x - y \|^2
\end{align} $$

Vì $$\nabla g(x) = Lx - \nabla f(x)$$, thế vào biểu thức trên cho kết quả mong muốn.
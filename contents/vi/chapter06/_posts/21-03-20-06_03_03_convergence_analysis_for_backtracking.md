---
layout: post
title: 06-03-03 Convergence analysis for backtracking
chapter: '06'
order: 12
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

Giả sử $$f$$ lồi, khả vi với $$dom(f) = \mathbb{R}^n$$ và $$\nabla f$$ liên tục Lipschitz với hằng số $$L > 0$$:
>$$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2 \quad \text{với mọi } x, y$$

Tham khảo: [[Wikipedia: Lipschitz continuity](https://en.wikipedia.org/wiki/Lipschitz_continuity)]

## Định lý Hội tụ

Thuật toán **gradient descent** kết hợp tìm kiếm đường lùi (backtracking line search) thỏa mãn:
> $$ \begin{align}
f(x^{(k)}) - f^* \le \frac{\| x^{(0)} - x^* \|_2^2}{2 t_{min} k}, \quad t_{min} = \min \{ 1, \beta/L \}
\end{align} $$

Tốc độ hội tụ của tìm kiếm đường lùi có cùng bậc $$O(1/k)$$ như trường hợp kích thước bước cố định, trong đó $$t$$ được thay bởi $$t_{min}$$. Nếu $$\beta$$ không quá nhỏ thì cận hội tụ tương đương với kích thước bước cố định ($$\beta/L$$ so với $$1/L$$), trong khi không cần biết trước hằng số $$L$$.

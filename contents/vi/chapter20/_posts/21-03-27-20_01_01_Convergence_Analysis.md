---
layout: post
title: '20-01-01 Phân tích hội tụ'
chapter: '20'
order: 3
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

## Tính đối ngẫu giữa gradient Lipschitz và tính lồi mạnh
Giả sử $$f$$ là hàm lồi đóng. Khi đó, mối tương đương sau luôn đúng:
> $$f \text{ lồi mạnh với tham số } d \Longleftrightarrow \nabla f^{\ast} \text{ liên tục Lipschitz với tham số } 1/d.$$

### Chứng minh
Ta chứng minh chiều "$$\Rightarrow$$". Nếu hàm $$g$$ lồi mạnh với tham số $$d$$ và đạt cực tiểu tại $$x$$ thì:
>\begin{equation}
g(y) \geq g(x) + \frac{d}{2}\lVert y-x \rVert_2^2, \quad \forall y
\end{equation}

Gọi $$x_u = \nabla f^{\ast}(u)$$ là điểm cực tiểu của $$x \mapsto f(x) - u^T x$$, và $$x_v = \nabla f^{\ast}(v)$$ là điểm cực tiểu của $$x \mapsto f(x) - v^T x$$. Áp dụng bất đẳng thức trên cho hai hàm này, ta có:
> $$
> \begin{alignat}{1}
> f(x_v) - u^Tx_v \geq f(x_u) - u^T x_u + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 \\
> f(x_u) - v^Tx_u \geq f(x_v) - v^T x_v + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 
> \end{alignat}
> $$

Cộng hai bất đẳng thức theo vế:
>\begin{equation}
f(x_v) - u^Tx_v + f(x_u) - v^Tx_u \geq f(x_u) - u^T x_u +  f(x_v) - v^T x_v + d \lVert x_u - x_v \rVert_2^2.  
\end{equation}

Rút gọn và áp dụng bất đẳng thức Cauchy–Schwarz:
> $$
> \begin{align}
> d \lVert x_u - x_v \rVert_2^2 & \leq - u^Tx_v - v^Tx_u + u^T x_u + v^T x_v \\\\
> & = (u-v)^T(x_u - x_v) \\\\
> & \leq \lVert u-v \rVert_2 \lVert x_u - x_v \rVert_2
> \end{align}
> $$

Chia hai vế cho $$d \lVert x_u - x_v \rVert_2$$ (khi $$x_u \neq x_v$$), ta thu được:

> $$\lVert x_u - x_v \rVert_2 \leq \frac{1}{d} \lVert u-v \rVert_2$$

chứng tỏ $$\nabla f^{\ast}$$ liên tục Lipschitz với hằng số $$1/d$$.

## Đảm bảo hội tụ
Kết hợp tính chất trên với kết quả hội tụ của gradient descent, ta thu được các đảm bảo hội tụ cho phương pháp tăng gradient đối ngẫu (dual gradient ascent):

* Nếu $$f$$ lồi mạnh với tham số $$d$$, thì dual gradient ascent với độ dài bước $$t_k = d$$ ($$k = 1, 2, 3, \dots$$) hội tụ với tốc độ $$O(1/\epsilon)$$.
* Nếu $$f$$ vừa lồi mạnh với tham số $$d$$ vừa có $$\nabla f$$ liên tục Lipschitz với tham số $$L$$, thì dual gradient ascent với độ dài bước $$t_k = 2/(1/d + 1/L)$$ ($$k = 1, 2, 3, \dots$$) hội tụ tuyến tính với tốc độ $$O(\log(1/\epsilon))$$.

(Các công thức độ dài bước trên giả sử $$\lVert A \rVert_2 \le 1$$; tổng quát, gradient đối ngẫu liên tục Lipschitz với hằng số $$\lVert A \rVert_2^2 / d$$ nên độ dài bước cần được nhân thêm hệ số $$1/\lVert A \rVert_2^2$$.)

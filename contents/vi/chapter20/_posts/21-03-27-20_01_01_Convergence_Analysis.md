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

## Gradient Lipschitz và tính lồi mạnh
Giả sử $$f$$ là hàm lồi đóng. Khi đó tương đương sau đây đúng.
>\begin{equation}
\text{$$f$$ lồi mạnh với tham số $$d$$ $$\Longleftrightarrow \nabla f^{\ast}$$ Lipschitz với tham số $$1/d$$.} 
\end{equation}

### Chứng minh ###
Ta chứng minh chiều "$$\Rightarrow$$". Nếu $$g$$ lồi mạnh với tham số $$d$$ và đạt cực tiểu tại $$x$$ thì
>\begin{equation}
g(y) \geq g(x) + \frac{d}{2}\lVert y-x \rVert_2^2, \text{ với mọi } y
\end{equation}

Gọi $$x_u = \nabla f^{\ast}(u)$$ là điểm cực tiểu của $$g(x) = f(x) − u^T x$$, và $$x_v = \nabla f^{\ast}(v)$$ là điểm cực tiểu của $$g(x) = f(x) − v^T x$$.

Khi đó bất đẳng thức trên cho ta hai bất đẳng thức sau.
> $$
> \begin{alignat}{1}
> f(x_v) - u^Tx_v \geq f(x_u) - u^T x_u + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 \\
> f(x_u) - v^Tx_u \geq f(x_v) - v^T x_v + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 
> \end{alignat}
> $$

Cộng hai bất đẳng thức, ta được
>\begin{equation}
f(x_v) - u^Tx_v + f(x_u) - v^Tx_u \geq f(x_u) - u^T x_u +  f(x_v) - v^T x_v + d \lVert x_u - x_v \rVert_2^2.  
\end{equation}

Sắp xếp lại và áp dụng bất đẳng thức Cauchy–Schwarz, ta được
> $$
> \begin{align}
> d \lVert x_u - x_v \rVert_2^2 & \leq - u^Tx_v - v^Tx_u + u^T x_u + v^T x_v \\\\
> & = (u-v)^T(x_u - x_v) \\\\
> & \leq \lVert u-v \rVert_2 \lVert x_u - x_v \rVert_2
> \end{align}
> $$

Do đó

> $$\lVert x_u - x_v \rVert_2 \leq \frac{1}{d} \lVert u-v \rVert_2$$

điều này chứng tỏ $$\nabla f^{\ast}$$ Lipschitz với tham số $$1/d$$.

## Đảm bảo hội tụ
Kết hợp kết quả này với phân tích của gradient descent, ta thu được các đảm bảo hội tụ sau cho hàm mục tiêu đối ngẫu.

* Nếu $$f$$ lồi mạnh với tham số $$d$$ thì dual gradient ascent với kích thước bước $$t_k=d$$ ($$k=1,2,3, \dots$$) hội tụ với tốc độ $$O(1/\epsilon)$$.
* Nếu $$f$$ lồi mạnh với tham số $$d$$ và $$\nabla f$$ Lipschitz với tham số $$L$$ thì dual gradient ascent với kích thước bước $$t_k=2/(1/d + 1/L)$$ ($$k=1,2,3, \dots$$) hội tụ với tốc độ $$O(\log(1/\epsilon))$$ (hội tụ tuyến tính).

(Các kích thước bước này giả sử $$\lVert A \rVert_2 \le 1$$; nói chung gradient đối ngẫu Lipschitz với hằng số $$\lVert A \rVert_2^2 / d$$, nên các kích thước bước cần được nhân với $$1/\lVert A \rVert_2^2$$.)

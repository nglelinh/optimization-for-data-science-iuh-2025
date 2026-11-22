---
layout: post
title: '07-03-05 Ví dụ: Khoảng cách đến tập lồi'
chapter: '07'
order: 11
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Hàm khoảng cách từ một điểm $$x$$ đến một tập lồi đóng $$C$$ được định nghĩa như sau:
>
\begin{alignat}{1}
dist(x,C) & = \min_{y \in C} \| y-x \|_2 \\
      & = \| x-P_C(x) \|_2 \\
      & \geq 0 
\end{alignat}

Trong đó, $$P_C(x)$$ là phép chiếu Euclid của $$x$$ lên tập $$C$$, tức là điểm trong $$C$$ gần $$x$$ nhất. Với $$x \notin C$$ (nên $$\|x - P_C(x)\|_2 > 0$$), vi phân dưới của hàm khoảng cách là:
>
\begin{equation}
\partial dist(x,C) = \{\frac{x-P_C(x)}{ \| x-P_C(x) \|_2}\}
\end{equation}

### Chứng minh

Đặt $$u=P_C(x)$$. Theo điều kiện tối ưu bậc một cho bài toán chiếu lên tập lồi $$C$$, ta có:
>
\begin{equation}
(x-u)^T(y-u) \leq 0 \ \text{ với mọi } y \in C
\end{equation}

Suy ra tập $$C$$ nằm trong nửa không gian đóng $$H$$:
>
\begin{equation}
C \subseteq H = \{y:(x-u)^T(y-u) \leq 0 \}
\end{equation}

Ta xét hai trường hợp của $$y$$:

(i) Với $$y \in H$$, ta có:
>
\begin{equation}
(x-u)^T(y-u) \leq 0
\end{equation}

Do $$dist(y,C)\geq 0$$, nên hiển nhiên:
>
\begin{equation}
dist(y,C) \geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ với mọi } y \in H
\end{equation}

(ii) Với $$y \notin H$$, ta viết:
>
\begin{equation}
(x-u)^T(y-u) = \| x-u \|_2 \| y-u \|_2 \cos\theta,
\end{equation}

trong đó $$\theta$$ là góc giữa hai vector $$x-u$$ và $$y-u$$. Khi đó:
>
$$
\eqalign{
dist(y,C) &\geq dist(y,H) \\
&= \| y-u \|_2 \cos \theta \\
&= \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ với mọi }y \notin H
}
$$

Từ (i) và (ii), bất đẳng thức sau đúng với mọi $$y$$:
>
$$
\eqalign{
dist(y,C) &\geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \\
&= \frac{(x-u)^T(y-x+x-u)}{ \| x-u \|_2}\\
& = \| x-u \|_2 + \left(\frac{x-u}{ \| x-u \|_2}\right)^T(y-x)
}
$$

Do đó, tại $$x \notin C$$, hàm $$dist(x,C)$$ có gradient dưới là:
>
$$g=\frac{x-u}{ \| x-u \|_2}=\frac{x-P_C(x)}{ \| x-P_C(x) \|_2} $$

Hơn nữa, vì vi phân dưới $$\partial dist(x,C)$$ tại $$x \notin C$$ chỉ gồm một phần tử duy nhất, hàm $$dist(x,C)$$ khả vi tại $$x$$ và đạo hàm của nó trùng với gradient dưới nói trên.

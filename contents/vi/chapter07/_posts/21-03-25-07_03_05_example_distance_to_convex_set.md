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

Hàm khoảng cách đến một tập lồi đóng $$C$$ được định nghĩa như sau:
>
\begin{alignat}{1}
dist(x,C) & = \min_{y \in C} \| y-x \|_2 \\
      & = \| x-P_C(x) \|_2 \\
      & \geq 0 
\end{alignat}

Ở đây, $$P_C(x)$$ là phép chiếu của điểm $$x$$ lên tập $$C$$, tức là điểm gần nhất trong $$C$$ với $$x$$. Gradient dưới của hàm khoảng cách là:
>
\begin{equation}
\partial dist(x,C) = \{\frac{x-P_C(x)}{ \| x-P_C(x) \|_2}\}
\end{equation}

### Chứng minh

Nếu $$u=P_C(x)$$, thì theo điều kiện tối ưu bậc một,
>
\begin{equation}
(x-u)^T(y-u) \leq 0 \ \text{ với mọi } y \in C
\end{equation}

Do đó,
>
\begin{equation}
C \subseteq H = \{y:(x-u)^T(y-u) \leq 0 \}
\end{equation}

(i) Với $$y \in H$$,
>
\begin{equation}
(x-u)^T(y-u) \leq 0
\end{equation}

Mặt khác, vì $$dist(y,C)\geq 0$$,
>
\begin{equation}
dist(y,C) \geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ với mọi } y \in H
\end{equation}

(ii) Với $$y \notin H$$,
>
\begin{equation}
(x-u)^T(y-u) = \| x-u \|_2 \| y-u \|_2 \cos\theta,
\end{equation}

trong đó $$\theta$$ là góc giữa $$x-u$$ và $$y-u$$. Khi đó,
>
$$
\eqalign{
dist(y,C) &\geq dist(y,H) \\

&= \| y-u \|_2 \cos \theta \\
&= \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \text{ với mọi }y \notin H
}
$$

Do đó, từ (i) và (ii), với mọi $$y$$,
>
$$
\eqalign{
dist(y,C) &\geq \frac{(x-u)^T(y-u)}{ \| x-u \|_2} \\
&= \frac{(x-u)^T(y-x+x-u)}{ \| x-u \|_2}\\
& = \| x-u \|_2 + \left(\frac{x-u}{ \| x-u \|_2}\right)^T(y-x)
}
$$

Kết luận, $$dist(x,C)$$ có gradient dưới sau tại $$x$$:
>
$$g=\frac{x-u}{ \| x-u \|_2}=\frac{x-P_C(x)}{ \| x-P_C(x) \|_2} $$

Hơn nữa, vi phân dưới $$\partial dist(x,C)$$ chỉ chứa một phần tử, nên $$dist(x,C)$$ khả vi và đạo hàm của nó trùng với gradient dưới.

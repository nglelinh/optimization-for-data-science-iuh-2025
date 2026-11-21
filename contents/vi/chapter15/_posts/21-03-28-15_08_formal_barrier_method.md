---
layout: post
title: '15-08 Phương pháp chắn chính thức'
chapter: "15"
categories:
- chapter16
order: 14
owner: "Minjoo Lee"
lang: vi
---

Nếu một hàm lồi $$\phi : D \to \mathbb{R}$$ xác định trên tập lồi mở $$D \subset \mathbb{R}^n$$ thỏa mãn các điều kiện sau thì hàm đó là một **hàm chắn tự hòa hợp (self-concordant barrier)** với tham số $$\nu$$.

* $$\phi$$ là hàm tự hòa hợp (self-concordant)
* Với mọi $$x \in D$$, đại lượng giảm Newton (Newton decrement) bị chặn bởi hằng số $$\nu$$ như sau.

> $$\lambda(x)^2 = \nabla \phi(x) (\nabla^2 \phi(x))^{-1} \nabla \phi(x) \le \nu$$

Hãy xét bài toán LP sau. (Ở đây $$\bar{D}$$ là bao đóng của miền $$D$$.)
>
$$\begin{align}
&\min_{x} \           && c^Tx \\
&\text{subject to } \ && x \in \bar{D}  \\
\end{align}$$

Bài toán này có thể được xấp xỉ như sau.
>
$$\begin{align}
&\min_{x} && tc^Tx + \phi(x) \\
\end{align}$$

Ở đây, đặt $$\phi_t(x) := tc^Tx + \phi(x)$$ và gọi $$\lambda_t(x)$$ là đại lượng giảm Newton tương ứng.

Quan sát then chốt: khi $$t^+ > t$$
>
$$\begin{align}
\lambda_{t^+}(x) \le & \frac{t^+}{t}\lambda_t(x) + \left ( \frac{t^+}{t} -1 \right ) \sqrt{\nu}  \\\
\end{align}$$

## Định lý

>$$\begin{align}
& \text{nếu} \quad \lambda_t(x) \le \frac{1}{9} \quad \text{và} \quad \frac{t^+}{t} \le 1 + \frac{1}{8 \sqrt{\nu}} \quad \text{thì} \quad \lambda_{t^+}(x^+) \le \frac{1}{9}  \\
& \qquad \qquad \text{với} \quad x^+ = x - (\nabla^2 \phi_{t^+}(x))^{-1} \nabla \phi_{t^+}(x)
\end{align}$$

Kết luận, nếu bắt đầu từ $$x^{(0)}, t^{(0)}$$ sao cho $$\lambda_{t^{(0)}}(x^{(0)}) \lt \frac{1}{9}$$ và chọn $$\mu := 1 + \frac{1}{8 \sqrt{\nu}}$$ thì mỗi bước centering chỉ cần một bước Newton là đủ.

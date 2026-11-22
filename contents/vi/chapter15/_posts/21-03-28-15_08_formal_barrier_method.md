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

Một hàm lồi $$\phi : D \to \mathbb{R}$$ xác định trên tập lồi mở $$D \subset \mathbb{R}^n$$ được gọi là **hàm chắn tự hài hòa (self-concordant barrier)** với tham số $$\nu$$ nếu thỏa mãn hai điều kiện:

* $$\phi$$ là hàm tự hài hòa (self-concordant).
* Với mọi $$x \in D$$, bình phương đại lượng giảm Newton (Newton decrement) của $$\phi$$ bị chặn bởi $$\nu$$:

> $$\lambda(x)^2 = \nabla \phi(x)^T (\nabla^2 \phi(x))^{-1} \nabla \phi(x) \le \nu$$

Xét bài toán quy hoạch tuyến tính (LP) sau, với $$\bar{D}$$ là bao đóng của miền $$D$$:
>
$$\begin{align}
&\min_{x} \           && c^Tx \\
&\text{subject to } \ && x \in \bar{D}  \\
\end{align}$$

Bài toán này được xấp xỉ bởi bài toán chắn không ràng buộc:
>
$$\begin{align}
&\min_{x} && tc^Tx + \phi(x) \\
\end{align}$$

Đặt $$\phi_t(x) := tc^Tx + \phi(x)$$ và gọi $$\lambda_t(x)$$ là đại lượng giảm Newton tương ứng của $$\phi_t$$.

Nhận xét quan trọng: khi tăng tham số lên $$t^+ > t$$, ta có bất đẳng thức:
>
$$\begin{align}
\lambda_{t^+}(x) \le & \frac{t^+}{t}\lambda_t(x) + \left ( \frac{t^+}{t} -1 \right ) \sqrt{\nu}  \\\
\end{align}$$

## Định lý

>$$
>\begin{align}
>& \text{nếu} \quad \lambda_t(x) \le \frac{1}{9} \quad \text{và} \quad \frac{t^+}{t} \le 1 + \frac{1}{8 \sqrt{\nu}} \quad \text{thì} \quad \lambda_{t^+}(x^+) \le \frac{1}{9}  \\
>& \qquad \qquad \text{với} \quad x^+ = x - (\nabla^2 \phi_{t^+}(x))^{-1} \nabla \phi_{t^+}(x)
>\end{align}
>$$

Kết quả này cho thấy nếu xuất phát từ $$x^{(0)}, t^{(0)}$$ thỏa $$\lambda_{t^{(0)}}(x^{(0)}) \lt \frac{1}{9}$$ và chọn hệ số tăng $$\mu := 1 + \frac{1}{8 \sqrt{\nu}}$$, thì mỗi bước định tâm chỉ cần đúng một bước Newton là đủ duy trì điều kiện bám đường trung tâm.

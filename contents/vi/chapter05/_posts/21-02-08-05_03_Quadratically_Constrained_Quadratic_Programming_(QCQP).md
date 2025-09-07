---
layout: post
title: 05-03 Quy Hoạch Bậc Hai với Ràng buộc Bậc Hai (QCQP)
chapter: '05'
order: 4
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

Nếu các hàm ràng buộc bất đẳng thức trong một chương trình bậc hai được thay thế bằng các hàm bậc hai lồi, bài toán được gọi là *Chương trình Bậc hai với Ràng buộc Bậc hai* (QCQP).

### Chương trình Bậc hai với Ràng buộc Bậc hai
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ với } i = 0, \dotsc, m, \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

## QP và QCQP tương đương
Nếu $$P_i = 0$$ với mọi $$i = 1, \dotsc, m$$ trong các ràng buộc QCQP, bài toán rút gọn thành một QP. Do đó, QP là một trường hợp đặc biệt của QCQP, và $$QP \subseteq QCQP$$.

### Nhắc lại: Chương trình Bậc hai
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P \in \mathbb{S}_{+}^n, G \in \mathbb{R}^{m \times n}, \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align} $$
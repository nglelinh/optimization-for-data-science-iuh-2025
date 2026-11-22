---
layout: post
title: 05-03 Quy Hoạch Bậc Hai với Ràng buộc Bậc Hai (QCQP)
chapter: '05'
order: 9
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

Nếu các ràng buộc bất đẳng thức tuyến tính trong một bài toán quy hoạch bậc hai được thay bằng các ràng buộc bậc hai lồi, ta thu được **bài toán quy hoạch bậc hai có ràng buộc bậc hai** (Quadratically Constrained Quadratic Programming - QCQP).

### Bài toán Quy hoạch Bậc hai có Ràng buộc Bậc hai
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, \quad i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ với } i = 0, \dotsc, m, \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

## Mối quan hệ giữa QP và QCQP
Khi $$P_i = 0$$ với mọi $$i = 1, \dotsc, m$$ trong các ràng buộc của QCQP, bài toán rút gọn về một bài toán QP. Do đó, QP là một trường hợp đặc biệt của QCQP, ký hiệu $$QP \subseteq QCQP$$.

### Nhắc lại: Bài toán Quy hoạch Bậc hai
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P \in \mathbb{S}_{+}^n, \; G \in \mathbb{R}^{m \times n}, \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align} $$
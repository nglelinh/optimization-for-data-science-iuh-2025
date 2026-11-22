---
layout: post
title: 05-06 Quy Hoạch Nón (CP)
chapter: '05'
order: 12
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

Nếu ràng buộc bất đẳng thức thông thường trong một bài toán LP tổng quát được thay bằng một **bất đẳng thức tổng quát theo nón lồi** $$K$$, ta thu được **bài toán quy hoạch nón** (Conic Programming - CP).

### Bài toán Quy hoạch Nón
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Fx + g \preceq_K 0} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&c, x \in \mathbb{R}^{n}, \; A \in \mathbb{R}^{p \times n}, \text{ và } b \in \mathbb{R}^{p}.
>\end{align}$$

* $$F: \mathbb{R}^n \rightarrow Y$$ là một ánh xạ tuyến tính và $$g \in Y$$, với $$Y$$ là một không gian Euclid hữu hạn chiều và $$K \subseteq Y$$ là một nón lồi chính quy.
* LP là trường hợp đặc biệt khi $$K = \mathbb{R}_{+}^m$$, do đó $$\text{LP} \subseteq \text{CP}$$.
* SDP là trường hợp đặc biệt khi $$K = \mathbb{S}_{+}^k$$, do đó $$\text{SDP} \subseteq \text{CP}$$.
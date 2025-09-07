---
layout: post
title: 05-06 Quy Hoạch Nón (CP)
chapter: '05'
order: 7
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

Nếu ràng buộc bất đẳng thức trong một LP tổng quát được thay thế bằng một ràng buộc bất đẳng thức tổng quát, bài toán được gọi là *Chương trình Nón* (CP).

### Chương trình Nón
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Fx + g \preceq_K 0} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&c, x \in \mathbb{R}^{n}, A \in \mathbb{R}^{p \times n}, \text{ và } b \in \mathbb{R}^{p}.
>\end{align}$$

* $$F: \mathbb{R}^n \rightarrow Y$$ là một ánh xạ tuyến tính, $$g \in Y$$, với không gian Euclidean $$Y$$.
* LP là trường hợp đặc biệt khi $$K = \mathbb{R}_{+}^n$$, tức là, LP $$\subseteq$$ CP.
* SDP là trường hợp đặc biệt khi $$K = \mathbb{S}_{+}^n$$, tức là, SDP $$\subseteq$$ CP.
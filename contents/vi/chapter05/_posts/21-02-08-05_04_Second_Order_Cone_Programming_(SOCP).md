---
layout: post
title: 05-04 Quy Hoạch Nón Bậc Hai (SOCP)
chapter: '05'
order: 5
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

Nếu các ràng buộc bất đẳng thức trong một LP tổng quát được thay thế bằng các ràng buộc nón bậc hai (là các hàm affine), bài toán được gọi là *Chương trình Nón Bậc hai* (SOCP).

### Chương trình Nón Bậc hai

>$$
>\begin{align}
>    &\text{minimize}_{x} &&{f^T x} \\\\
>    &\text{subject to } &&{\| A_i x + b_i \|_2 \leq c_i^T x + d_i, i = 1, \dotsc, m}\\\\
>    & &&{Fx = g},\\\\
>    & \text{where } &&x \in \mathbb{R}^n \text{ là biến tối ưu, } A_i  \in \mathbb{R}^{n_i \times n}, \text{ và } F \in \mathbb{R}^{p \times n}.
>\end{align} $$

### Nhắc lại: Nón chuẩn
Một *nón chuẩn* là một nón lồi trong $$\mathbb{R}^{n+1}$$ được định nghĩa bởi tất cả các điểm $$(x, t)$$ sao cho $$\| x \| \le t$$ với một chuẩn nào đó $$\| \cdot \|$$.

>$$\left\{(x, t) : \| x \| \le t \right\} \text{, với chuẩn } \| \cdot \|$$

Hình dưới đây cho thấy nón chuẩn cho chuẩn $$l_2$$ $$\| \cdot \|_2$$, cũng được gọi là nón bậc hai hoặc nón kem.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_04_Norm_Cone.png" alt="[Fig1] Nón Chuẩn [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Nón Chuẩn [1]</figcaption>
</p>
</figure>

## QCQP và SOCP tương đương
Một QCQP có thể được tái công thức thành một SOCP trong một số trường hợp, tức là, $$QCQP \subseteq SOCP$$.

### Nhắc lại: Chương trình Bậc hai với Ràng buộc Bậc hai
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ với } i = 0, \dotsc, m, \text{ và } A \in \mathbb{R}^{p \times n}
>\end{align} $$
>
**Step 1.** For convenience, QCQP can be reformulated in different ways to fit SOCP structure.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{x^T P_0 x + 2q_0^T x + r_0} \\\\
>    &\text{subject to } &&{x^T P_i x + 2q_i^T x + r_i \leq 0}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } && P_i \in \mathbb{S}_{+}^n \text{ for } i = 0, \dotsc, m \text{, and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}\\
>$$
>

**Step 2.** Since $$P_0$$ is a positive semidefinite matrix, any $$ \tilde{P_0}$$ satisfying $$P_0 = \tilde{P_0}\tilde{P_0}$$ is also a positive semidefinite matrix. This $$\tilde{P_0}$$ can be obtained through eigendecomposition. Using this, the objective function of the QCQP can be transformed as follows:

* $$P_0 = Q_0 \Lambda_0 \Lambda_0 Q_0^T$$
* $$I = Q_0 \Lambda_0 \Lambda_0^{-1} Q_0^{-1} = Q_0 \Lambda_0^{-1} \Lambda_0 Q_0^{-1}$$

> $$
> \begin{align}
> {x^T P_0 x + 2q_0^T x + r_0} &= {x^T P_0 x + q_0^T x + x^T q_0 + q_0^T P_0^{-1} q_0 - q_0^T P_0^{-1} q_0 + r_0}\\\\
> &= {x^T Q_0 \Lambda_0 \Lambda_0 Q_0^T x} +
>      {q_0^T Q_0 \Lambda_0^{-1} \Lambda_0 Q_0^{-1} x} + {x^T Q_0 \Lambda_0 \Lambda_0^{-1} Q_0^{-1} q_0} +
>      {q_0^T Q_0 \Lambda_0^{-1} \Lambda_0^{-1} Q_0^T q_0} - {q_0^T P_0^{-1} q_0 + r_0}\\\\
> &=(\Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0)^T(\Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0) - {q_0^T P_0^{-1} q_0 + r_0}\\\\
> &=\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2 - {q_0^T P_0^{-1} q_0 + r_0}\\\\
> \end{align}
> $$

**Step 3.** The same procedure as in Step 2 is applied to the inequality constraint functions, and then substituted into the QCQP from Step 1.

>$$
>\begin{align}
>    &\text{minimize}_{x} &&{\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2 - {q_0^T P_0^{-1} q_0 + r_0}} \\\\
>    &\text{subject to } &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq {q_i^T P_i^{-1} q_i + r_i}}, i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$
>

**Step 4.** The term $${q_0^T P_0^{-1} q_0 + r_0}$$ in the objective function is a constant and can be omitted.
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{\| \Lambda_0 Q_0^T x + \Lambda_0^{-1} Q_0^T q_0 \|_2^2} \\\\
>    &\text{subject to } &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq {q_i^T P_i^{-1} q_i + r_i} }, i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$

**Step 5.** Introducing a scalar variable $$t$$, the same problem as in Step 4 can be defined.
>$$
>\begin{align}
>    &\text{minimize}_{x, t} &&{t} \\\\
>    &\text{subject to } &&\lVert{\Lambda_{0} Q_0^T x + \Lambda_0^{-1} Q_0^T q_0} \rVert_2^2 \leq t\\\\
>    & &&{\| \Lambda_i Q_i^T x + \Lambda_i^{-1} Q_i^T q_i \|_2^2 \leq {q_i^T P_i^{-1} q_i + r_i} }, i = 1, \dotsc, m\\\\
>    & &&{Ax = b}.\\\\
>\end{align}
>$$

Phần trên đại diện cho một trường hợp đặc biệt của SOCP. Do đó, mối quan hệ $$QCQP \subseteq SOCP$$ được thỏa mãn.

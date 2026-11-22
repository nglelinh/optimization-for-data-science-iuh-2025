---
layout: post
title: '17-05 Điều kiện tối ưu cho quy hoạch bán xác định (SDP)'
chapter: '17'
order: 9
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Trong phần này, chúng ta xét phương pháp điểm trong gốc-đối ngẫu áp dụng cho bài toán quy hoạch bán xác định (SDP — semidefinite programming).

## Quy hoạch bán xác định (SDP)
Bài toán SDP gốc được phát biểu như sau:
>$$
>\begin{align}
>    &\min_{X} && {C \cdot X} \\\\
>    &\text{subject to } && {A_i \cdot X = b_i, i = 1,...,m} \\\\
>    & &&{X \succeq 0}
>\end{align}
>$$


Bài toán SDP đối ngẫu tương ứng là:
>$$
>\begin{align}
>    &\max_{y} && {b^Ty} \\\\
>    &\text{subject to } && {\sum^m_{i=1} y_iA_i + S = C} \\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

Nhắc lại rằng tích vô hướng vết (trace inner product) trên không gian ma trận đối xứng $$\mathbb{S}^n$$ được định nghĩa là:
> $$X \cdot S = \text{trace}(XS)$$

## Điều kiện tối ưu cho SDP
Cặp bài toán SDP gốc và đối ngẫu có thể được viết gọn bằng toán tử tuyến tính $$\mathcal{A}: \mathbb{S}^n \to \mathbb{R}^m$$ và toán tử liên hợp $$\mathcal{A}^*$$ của nó:

>$$
>\begin{align}
>    &\min_{X} && {C \cdot X} & \qquad \qquad \qquad & \max_{y,S}  && {b^Ty} \\\\
>    &\text{subject to } && {\mathcal{A}(X) = b} & \qquad \qquad \qquad & \text{subject to } && {\mathcal{A}^{*}(y) + S = C} \\\\
>    & &&{X \succeq 0} & \qquad \qquad \qquad & &&{S \succeq 0}
>\end{align}
>$$


Giả sử tính đối ngẫu mạnh được thỏa mãn, thì $$X^{\star}$$ và $$(y^{\star}, S^{\star})$$ là cặp nghiệm tối ưu gốc – đối ngẫu khi và chỉ khi $$(X^{\star}, y^{\star}, S^{\star})$$ thỏa mãn hệ điều kiện sau:

> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & 0 \\\
> X,S & \succeq & 0
> \end{array}
> $$


## Đường trung tâm cho SDP
**Bài toán chắn gốc**
>$$
>\begin{align}
>    &\min_{X} && {C \cdot X - \tau \log\det(X)} \\\\
>    &\text{subject to } && {\mathcal{A}(X) = b} 
>\end{align}
>$$


**Bài toán chắn đối ngẫu**
>$$
>\begin{align}
>    &\max_{y, S} && {b^Ty + \tau \log\det(S)} \\\\
>    &\text{subject to } && {\mathcal{A}^*(y) + S = C} 
>\end{align}
>$$


**Điều kiện tối ưu cho các bài toán chắn gốc và đối ngẫu**
> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & \tau I \\\
> X,S & \succ & 0
> \end{array}
> $$


## Bước Newton
Hệ phương trình đường trung tâm gốc:
> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + \tau X^{-1} & = & C \\\
> \mathcal{A}(X) & = & b \\\
> X & \succ & 0
> \end{array}
> $$


Phương trình Newton tương ứng (sử dụng vi phân $$d(X^{-1}) = -X^{-1} \Delta X X^{-1}$$):
> $$-\tau X^{-1}\Delta X X^{-1} +\mathcal{A}^*(\Delta y) = -(\mathcal{A}^*(y) + \tau X^{-1} -C)$$
> $$\mathcal{A}(\Delta X) = -(\mathcal{A}(X)-b)$$

Hệ phương trình đường trung tâm và phương trình Newton cho bài toán đối ngẫu theo $$(y, S)$$ được xây dựng hoàn toàn tương tự.

## Bước Newton gốc-đối ngẫu 
Hệ phương trình đường trung tâm gốc-đối ngẫu:
> $$\begin{bmatrix}
\mathcal{A}^*(y) + S - C  \\\
\mathcal{A}(X) - b \\\
XS
\end{bmatrix} =
\begin{bmatrix}
0 \\\
0 \\\
\tau I
\end{bmatrix}
, \quad X, S \succ 0
$$

Hệ bước Newton:
> $$\begin{bmatrix}
0 & \mathcal{A}^* & I \\\
\mathcal{A} & 0 & 0 \\\
S & 0 & X 
\end{bmatrix}
\begin{bmatrix}
\Delta X \\\
\Delta y \\\
\Delta S
\end{bmatrix}= -
\begin{bmatrix}
\mathcal{A}^*(y) + S - C \\\
\mathcal{A}(X) - b \\\
XS - \tau I 
\end{bmatrix}$$

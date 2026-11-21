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

Trong phần này chúng ta xem một ví dụ về phương pháp gốc-đối ngẫu cho bài toán SDP (quy hoạch bán xác định, semidefinite programming).

## SDP (quy hoạch bán xác định)
Bài toán SDP gốc được định nghĩa như sau.
>$$
>\begin{align}
>    &\min_{X} && {C \cdot X} \\\\
>    &\text{subject to } && {A_i \cdot X = b_i, i = 1,...,m} \\\\
>    & &&{X \succeq 0}
>\end{align}
>$$


Bài toán SDP đối ngẫu được định nghĩa như sau.
>$$
>\begin{align}
>    &\max_{y} && {b^Ty} \\\\
>    &\text{subject to } && {\sum^m_{i=1} y_iA_i + S = C} \\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

Nhắc lại rằng tích vô hướng vết (trace inner product) trên $$\mathbb{S}^n$$ được viết là
> $$X \cdot S = \text{trace}(XS)$$

## Điều kiện tối ưu cho SDP
Bài toán SDP gốc và đối ngẫu có thể được viết bằng ánh xạ tuyến tính như sau.

>$$
>\begin{align}
>    &\min_{X} && {C \cdot X} & \qquad \qquad \qquad & \max_{y,S}  && {b^Ty} \\\\
>    &\text{subject to } && {\mathcal{A}(X) = b} & \qquad \qquad \qquad & \text{subject to } && {\mathcal{A}^{*}(y) + S = C} \\\\
>    & &&{X \succeq 0} & \qquad \qquad \qquad & &&{S \succeq 0}
>\end{align}
>$$


Ở đây $$\mathcal{A}: \mathbb{S}^n \to \mathbb{R}^m$$ là một ánh xạ tuyến tính.

Giả sử đối ngẫu mạnh thỏa mãn, thì $$X^{\star}$$ và $$(y^{\star}, S^{\star})$$ là các nghiệm tối ưu của bài toán gốc và đối ngẫu khi và chỉ khi $$(X^{\star}, y^{\star}, S^{\star})$$ thỏa mãn các điều kiện sau.

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
Phương trình đường trung tâm gốc 
> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + \tau X^{-1} & = & C \\\
> \mathcal{A}(X) & = & b \\\
> X & \succ & 0
> \end{array}
> $$


Phương trình Newton
> $$\tau X^{-1}\Delta X X^{-1} +\mathcal{A}^*(\Delta y) = -(\mathcal{A}^*(y) + \tau X^{-1} -C)$$
> $$\mathcal{A}(\Delta X) = -(\mathcal{A}(X)-b)$$

Phương trình đường trung tâm và phương trình Newton cho bài toán đối ngẫu, bao gồm $$(y,S)$$, được định nghĩa tương tự.

## Bước Newton gốc-đối ngẫu 
Phương trình đường trung tâm gốc-đối ngẫu 
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

Bước Newton:
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

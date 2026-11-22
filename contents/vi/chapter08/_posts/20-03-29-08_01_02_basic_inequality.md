---
layout: post
title: '08-01-02 Bất đẳng thức cơ bản'
chapter: '08'
order: 4
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Định lý hội tụ và tốc độ hội tụ của phương pháp subgradient đều được suy ra từ bất đẳng thức cơ bản dưới đây.

## Bất đẳng thức cơ bản

>$$
\begin{align}
f_{best}^{k} - f^* \quad \le \quad \frac{R^{2}+G^{2}\sum_{i=1}^{k}\alpha_{i}^{2}}{2\sum_{i=1}^{k}\alpha_{i}} 
\end{align}
$$

## Chứng minh

Nếu $$x^*$$ là một điểm tối ưu của hàm $$f$$, ta có khai triển bình phương khoảng cách:

>$$
\begin{alignat}{1}
 \Vert x^{(k+1)}-x^* \Vert _2^{2} & \quad = \quad  \Vert x^{(k)}-\alpha_k g^{(k)}-x^* \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert (x^{(k)}-x^*)-\alpha_k g^{(k)} \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert x^{(k)}-x^* \Vert _2^2 - 2 \alpha_k g^{(k)T}(x^{(k)}-x^*)+\alpha_k^2 \Vert g^{(k)} \Vert _2^2 \\
\end{alignat} $$

Theo định nghĩa của subgradient, ta có:

>$$
\begin{alignat}{1}
f(x^*) \ge f(x^{(k)}) + g^{(k)T}(x^*-x^{(k)}) & \quad \Longleftrightarrow \quad f(x^*)-f(x^{(k)}) \ge  g^{(k)T}(x^*-x^{(k)}) \\
                     & \quad  \Longleftrightarrow \quad f(x^{(k)}) - f(x^*) \le  g^{(k)T}(x^{(k)}-x^*) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(f(x^{(k)}) - f(x^*)) \ge  -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \le -2\alpha_{k}(f(x^{(k)})-f(x^*)) \\
\end{alignat} $$

Thay bất đẳng thức này vào biểu thức khai triển ở trên và cộng dồn theo các bước lặp, ta thu được bất đẳng thức cơ bản đã phát biểu ở đầu bài.

---
layout: post
title: '08-01-02 Basic Inequality'
chapter: '08'
order: 4
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

The convergence theorem and convergence rate of the subgradient method can be proved using the following basic inequality.

## Basic Inequality

>$$
\begin{align}
f_{best}^{k} - f^* \quad \le \quad \frac{R^{2}+G^{2}\sum_{i=1}^{k}\alpha_{i}^{2}}{2\sum_{i=1}^{k}\alpha_{i}} 
\end{align}
$$

## Proof
If $$x^*$$ is the optimal point of the function $$f$$, then the following equation holds:

>$$
\begin{alignat}{1}
 \Vert x^{(k+1)}-x^* \Vert _2^{2} & \quad = \quad  \Vert x^{(k)}-\alpha_k g^{(k)}-x^* \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert (x^{(k)}-x^*)-\alpha_k g^{(k)} \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert x^{(k)}-x^* \Vert _2^2 - 2 \alpha_k g^{(k)T}(x^{(k)}-x^*)+\alpha_k^2 \Vert g^{(k)} \Vert _2^2 \\
\end{alignat} $$

From the definition of subgradient, the following inequality holds:

>$$
\begin{alignat}{1}
f(x^*) \ge f(x^{(k)}) + g^{(k)T}(x^*-x^{(k)}) & \quad \Longleftrightarrow \quad f(x^*)-f(x^{(k)}) \ge  g^{(k)T}(x^*-x^{(k)}) \\
                     & \quad  \Longleftrightarrow \quad f(x^{(k)} - f(x^*)) \le  g^{(k)T}(x^{(k)}-x^*) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(f(x^{(k)}) - f(x^*)) \ge  -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \le -2\alpha_{k}(f(x^{(k)})-f(x^*)) \\
\end{alignat} $$

Using the above equations and inequalities, the following inequality can be derived:

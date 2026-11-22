---
layout: post
title: 05-02-02 Quy Hoạch Hình Học
chapter: '05'
order: 6
owner: Copilot
categories:
- chapter05
lang: vi
---

Phần này giới thiệu một lớp bài toán tối ưu ban đầu trông không lồi khi nhìn vào hàm mục tiêu và các ràng buộc gốc, nhưng có thể chuyển đổi tương đương về dạng bài toán tối ưu hóa lồi nhờ phép đổi biến thích hợp.

Trước tiên, ta cần hai định nghĩa cơ bản:

## 1. Đơn thức dương và Đa thức dương

Một hàm $$f: \mathbb{R}^n \to \mathbb{R}$$ xác định trên miền $$\text{dom } f = \mathbb{R}^n_{++}$$ (mọi thành phần đều dương chặt) có dạng:

$$f(x) = c x_1^{a_1} x_2^{a_2} \ldots x_n^{a_n} \quad \quad (24)$$

trong đó $$c > 0$$ và $$a_i \in \mathbb{R}$$, được gọi là **hàm đơn thức dương** (monomial).

Tổng của các đơn thức dương:

$$f(x) = \sum_{k=1}^K c_k x_1^{a_{1k}} x_2^{a_{2k}} \ldots x_n^{a_{nk}} \quad \quad (25)$$

với $$c_k > 0$$, được gọi là **hàm đa thức dương** (posynomial).

## 2. Bài toán Quy hoạch Hình học

Một bài toán tối ưu có dạng:

$$\begin{align}
x &= \arg\min_x f_0(x) \\
\text{subject to: } &f_i(x) \leq 1, \quad i = 1, 2, \ldots, m \quad \quad (26) \\
&h_j(x) = 1, \quad j = 1, 2, \ldots, p
\end{align}$$

trong đó $$f_0, f_1, \ldots, f_m$$ là các đa thức dương và $$h_1, \ldots, h_p$$ là các đơn thức dương, được gọi là **bài toán Quy hoạch Hình học (Geometric Programming - GP)**. Điều kiện $$x \succ 0$$ luôn được ngầm hiểu.

Lưu ý rằng nếu $$f$$ là một đa thức dương và $$h$$ là một đơn thức dương, thì thương $$f/h$$ cũng là một đa thức dương.

**Ví dụ:**

$$\begin{align}
(x, y, z) &= \arg\min_{x,y,z} x/y \\
\text{subject to: } &1 \leq x \leq 2 \\
&x^3 + 2y/z \leq \sqrt{y} \\
&x/y = z
\end{align}$$

Bài toán này có thể viết lại về dạng chuẩn của GP:

$$\begin{align}
(x, y, z) &= \arg\min_{x,y,z} xy^{-1} \\
\text{subject to: } &x^{-1} \leq 1 \\
&(1/2)x \leq 1 \\
&x^3 y^{-1/2} + 2y^{1/2}z^{-1} \leq 1 \\
&xy^{-1}z^{-1} = 1
\end{align}$$

Ở dạng gốc này, bài toán không phải là bài toán lồi vì hàm mục tiêu và các ràng buộc đều không lồi.

## 3. Chuyển đổi GP về dạng lồi

Ta có thể chuyển đổi bài toán GP về dạng lồi bằng phép đổi biến logarit như sau:

Đặt $$y_i = \log(x_i)$$, tức là $$x_i = \exp(y_i)$$. Nếu $$f$$ là một đơn thức dương theo $$x$$, thì:

$$f(x) = c(\exp(y_1))^{a_1} \ldots (\exp(y_n))^{a_n} = \exp(a^T y + b)$$

trong đó $$b = \log(c)$$. Hàm $$g(y) = \exp(a^T y + b)$$ là một hàm lồi theo $$y$$ (vì hợp thành của một hàm lồi với một hàm affine luôn bảo toàn tính lồi; ở đây hàm $$\exp$$ là hàm lồi và $$a^T y + b$$ là hàm affine).

Tương tự, đa thức dương trong phương trình (25) được viết lại thành:

$$f(x) = \sum_{k=1}^K \exp(a_k^T y + b_k)$$

trong đó $$a_k = [a_{1k}, \ldots, a_{nk}]^T$$ và $$b_k = \log(c_k)$$. Biểu thức này là tổng các hàm mũ của hàm affine nên là hàm lồi theo $$y$$.

Bài toán GP (26) do đó được viết lại thành:

$$\begin{align}
y &= \arg\min_y \sum_{k=1}^{K_0} \exp(a_{0k}^T y + b_{0k}) \\
\text{subject to: } &\sum_{k=1}^{K_i} \exp(a_{ik}^T y + b_{ik}) \leq 1, \quad i = 1, \ldots, m \quad \quad (27) \\
&\exp(g_j^T y + h_j) = 1, \quad j = 1, \ldots, p
\end{align}$$

trong đó $$a_{ik} \in \mathbb{R}^n$$ ($$i = 0, 1, \ldots, m$$) và $$g_j \in \mathbb{R}^n$$ ($$j = 1, \ldots, p$$).

Áp dụng phép biến đổi đơn điệu tăng $$\log(\cdot)$$ cho hàm mục tiêu và hai vế của các ràng buộc, đồng thời sử dụng tính chất hàm $$\log \sum_{k} \exp(a_k^T y + b_k)$$ (log-sum-exp) là hàm lồi, ta viết lại bài toán (27) về dạng lồi:

**Bài toán GP ở dạng lồi:**

$$\begin{align}
\text{minimize}_y \quad &\tilde{f}_0(y) = \log\left(\sum_{k=1}^{K_0} \exp(a_{0k}^T y + b_{0k})\right) \\
\text{subject to: } &\tilde{f}_i(y) = \log\left(\sum_{k=1}^{K_i} \exp(a_{ik}^T y + b_{ik})\right) \leq 0, \quad i = 1, \ldots, m \quad \quad (28) \\
&\tilde{h}_j(y) = g_j^T y + h_j = 0, \quad j = 1, \ldots, p
\end{align}$$

Như vậy, bài toán GP tương đương với một bài toán tối ưu hóa lồi, vì hàm mục tiêu và các hàm ràng buộc bất đẳng thức trong (28) đều là hàm lồi, còn các ràng buộc đẳng thức là hàm affine. Dạng (28) thường được gọi là **bài toán quy hoạch hình học ở dạng lồi** để phân biệt với dạng gốc (26).
---
layout: post
title: 05-02-02 Quy Hoạch Hình Học
chapter: '05'
order: 9
owner: Copilot
categories:
- chapter05
lang: vi
---

Trong phần này, chúng ta sẽ thấy một lớp các bài toán có vẻ không lồi khi nhìn vào hàm mục tiêu và các hàm ràng buộc, nhưng có thể được biến đổi thành dạng lồi thông qua nhiều kỹ thuật.

Trước tiên, chúng ta cần một số định nghĩa:

## 5.2.1. Đơn thức và Đa thức dương

Một hàm $$f: \mathbb{R}^n \to \mathbb{R}$$ với miền $$\text{dom } f = \mathbb{R}^n_{++}$$ (tất cả các phần tử đều dương) có dạng:

$$f(x) = c x_1^{a_1} x_2^{a_2} \ldots x_n^{a_n} \quad \quad (24)$$

trong đó $$c > 0$$ và $$a_i \in \mathbb{R}$$, được gọi là **hàm đơn thức**.

Một tổng các đơn thức:

$$f(x) = \sum_{k=1}^K c_k x_1^{a_{1k}} x_2^{a_{2k}} \ldots x_n^{a_{nk}} \quad \quad (25)$$

trong đó $$c_k > 0$$, được gọi là **hàm đa thức dương**, hoặc đơn giản là **đa thức dương**.

## 5.2.2. Quy hoạch Hình học

Một bài toán tối ưu có dạng:

$$\begin{align}
x &= \arg\min_x f_0(x) \\
\text{subject to: } &f_i(x) \leq 1, \quad i = 1, 2, \ldots, m \quad \quad (26) \\
&h_j(x) = 1, \quad j = 1, 2, \ldots, p
\end{align}$$

trong đó $$f_0, f_1, \ldots, f_m$$ là các đa thức dương và $$h_1, \ldots, h_p$$ là các đơn thức, được gọi là **Quy hoạch Hình học (GP)**. Điều kiện $$x \succ 0$$ là ngầm định.

Lưu ý rằng nếu $$f$$ là một đa thức dương và $$h$$ là một đơn thức, thì $$f/h$$ là một đa thức dương.

**Ví dụ:**

$$\begin{align}
(x, y, z) &= \arg\min_{x,y,z} x/y \\
\text{subject to: } &1 \leq x \leq 2 \\
&x^3 + 2y/z \leq \sqrt{y} \\
&x/y = z
\end{align}$$

Điều này có thể được viết lại dưới dạng GP:

$$\begin{align}
(x, y, z) &= \arg\min_{x,y,z} xy^{-1} \\
\text{subject to: } &x^{-1} \leq 1 \\
&(1/2)x \leq 1 \\
&x^3 y^{-1/2} + 2y^{1/2}z^{-1} \leq 1 \\
&xy^{-1}z^{-1} = 1
\end{align}$$

Bài toán này rõ ràng là không lồi vì cả hàm mục tiêu và các hàm ràng buộc đều không lồi.

## 5.2.3. Biến đổi GP về Dạng Lồi

GP có thể được biến đổi về dạng lồi như sau:

Gọi $$y_i = \log(x_i)$$, tức là, $$x_i = \exp(y_i)$$. Nếu $$f$$ là một hàm đơn thức của $$x$$, thì:

$$f(x) = c(\exp(y_1))^{a_1} \ldots (\exp(y_n))^{a_n} = \exp(a^T y + b)$$

trong đó $$b = \log(c)$$. Bây giờ, hàm $$g(y) = \exp(a^T y + b)$$ là một hàm lồi theo $$y$$. (Người đọc có thể chứng minh bằng định nghĩa rằng hợp thành của hai hàm lồi là một hàm lồi. Trong trường hợp này, cả hàm $$\exp$$ và hàm affine đều là các hàm lồi.)

Tương tự, đa thức dương trong phương trình (25) có thể được viết như:

$$f(x) = \sum_{k=1}^K \exp(a_k^T y + b_k)$$

trong đó $$a_k = [a_{1k}, \ldots, a_{nk}]^T$$ và $$b_k = \log(c_k)$$. Bây giờ, đa thức dương đã được viết dưới dạng tổng các hàm $$\exp$$ của các hàm affine (và do đó là một hàm lồi, nhớ lại rằng tổng các hàm lồi là lồi).

The GP problem (26) is rewritten as:

$$\begin{align}
y &= \arg\min_y \sum_{k=1}^{K_0} \exp(a_{0k}^T y + b_{0k}) \\
\text{subject to: } &\sum_{k=1}^{K_i} \exp(a_{ik}^T y + b_{ik}) \leq 1, \quad i = 1, \ldots, m \quad \quad (27) \\
&\exp(g_j^T y + h_j) = 1, \quad j = 1, \ldots, p
\end{align}$$

where $$a_{ik} \in \mathbb{R}^n$$, $$i = 1, \ldots, p$$ and $$g_i \in \mathbb{R}^n$$.

Với nhận xét rằng hàm $$\log \sum_{i=1}^m \exp(g_i(x))$$ là một hàm lồi nếu $$g_i$$ là các hàm lồi (chúng ta bỏ qua chứng minh), chúng ta có thể viết lại bài toán (27) dưới dạng lồi bằng cách lấy $$\log$$ của các hàm như sau:

**GP ở dạng lồi:**

$$\begin{align}
\text{minimize}_y \quad &\tilde{f}_0(y) = \log\left(\sum_{k=1}^{K_0} \exp(a_{0k}^T y + b_{0k})\right) \\
\text{subject to: } &\tilde{f}_i(y) = \log\left(\sum_{k=1}^{K_i} \exp(a_{ik}^T y + b_{ik})\right) \leq 0, \quad i = 1, \ldots, m \quad \quad (28) \\
&\tilde{h}_j(y) = g_j^T y + h_j = 0, \quad j = 1, \ldots, p
\end{align}$$

Bây giờ chúng ta có thể nói rằng GP tương đương với một bài toán tối ưu lồi vì hàm mục tiêu và các hàm ràng buộc bất đẳng thức trong (28) đều là các hàm lồi, trong khi các ràng buộc đẳng thức ở dạng affine. Dạng này thường được gọi là **chương trình hình học ở dạng lồi** (để phân biệt với định nghĩa gốc của GP).
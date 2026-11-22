---
layout: post
title: '21-02 Mối liên hệ với toán tử proximal'
chapter: '21'
order: 3
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

# Mối liên hệ với toán tử proximal

Xét bài toán tối ưu một biến với hàm mục tiêu là tổng của hai hàm:
>$$
>\begin{align}
>\min_{x} f(x)+g(x)
>\end{align}
>$$

Ta có thể viết lại bài toán này bằng cách tách biến và thêm một ràng buộc đẳng thức:
>$$
>\begin{align}
>\min_{x, z} f(x)+g(z) \qquad \text{subject to  }x=z
>\end{align}
>$$

## Các bước ADMM dưới dạng proximal

Áp dụng ADMM dạng chuẩn hóa cho bài toán trên, ta thu được các bước cập nhật:
>$$
>\begin{align}
>&x^{(k)} = {\operatorname{prox}}_{f,\frac{1}{\rho}}(z^{(k-1)}-w^{(k-1)})\\\\
>&z^{(k)} = {\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{(k)}+w^{(k-1)})\\\\
>&w^{(k)}=w^{(k-1)}+x^{(k)}-z^{(k)}
>\end{align}
>$$

trong đó $$\operatorname{prox}_{f,\frac{1}{\rho}}$$ và $$\operatorname{prox}_{g,\frac{1}{\rho}}$$ lần lượt là các toán tử proximal của $$f$$ và $$g$$ với tham số $$\frac{1}{\rho}$$.

## Định nghĩa toán tử proximal

Nhắc lại rằng với một hàm lồi $$f$$, [toán tử proximal]({% multilang_post_url contents/chapter19/21-03-24-19_01_01_Reminder:_proximal_gradient_descent %}) được định nghĩa là:
>$$
>\begin{align}
>{\operatorname{prox}}_{f, \lambda}(v) = \underset{x}{\operatorname{argmin}}\left(f(x)+\frac{1}{2\lambda}||x-v||_{2}^{2}\right). 
>\end{align}
>$$

## Suy diễn các bước cập nhật proximal

Gọi $$x^{+}, z^{+}, w^{+}$$ là các giá trị mới của $$x, z, w$$ sau một vòng lặp. Ta suy ra biểu thức proximal của từng bước như sau:

### Cập nhật cho $$x$$:
>$$
>\begin{align}
>x^{+}& = \underset{x}{\operatorname{argmin}}f(x)+\frac{\rho}{2}||x-z+w||^{2}_{2}\\\\
>& =\underset{x}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(z-w)-x||^{2}_{2}+f(x)\\\\
>& ={\operatorname{prox}}_{f,\frac{1}{\rho}}(z-w)
>\end{align}
>$$

### Cập nhật cho $$z$$:
>$$
>\begin{align}
>z^{+}& = \underset{z}{\operatorname{argmin}}g(z)+\frac{\rho}{2}||x^{+}-z+w||^{2}_{2}\\\\
>& =\underset{z}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(x^{+}+w)-z||^{2}_{2}+g(z)\\\\
>& ={\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{+}+w)
>\end{align}
>$$

## Nhận xét chính

Trong bài toán ADMM tổng quát, ràng buộc có dạng $$Ax+Bz = c$$, còn ở đây ràng buộc đơn giản là $$x=z$$. Khi quan hệ tuyến tính giữa $$x$$ và $$z$$ là phép đồng nhất, hai bước cập nhật biến gốc của ADMM trở thành hai phép tính toán tử proximal liên tiếp trên $$f$$ và $$g$$.

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

Xét bài toán tối ưu một biến tách thành hai hàm:
>$$
>\begin{align}
>\min_{x} f(x)+g(x)
>\end{align}
>$$

Bài toán này cũng có thể được biểu diễn bằng cách thêm một ràng buộc:
>$$
>\begin{align}
>\min_{x, z} f(x)+g(z) \qquad \text{subject to  }x=z
>\end{align}
>$$

## Các bước ADMM dưới dạng proximal

Các bước ADMM cho bài toán này là:
>$$
>\begin{align}
>&x^{(k)} = {\operatorname{prox}}_{f,\frac{1}{\rho}}(z^{(k-1)}-w^{(k-1)})\\\\
>&z^{(k)} = {\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{(k)}+w^{(k-1)})\\\\
>&w^{(k)}=w^{(k-1)}+x^{(k)}-z^{(k)}
>\end{align}
>$$

trong đó $$\operatorname{prox}_{f,\frac{1}{\rho}}$$ và $$\operatorname{prox}_{g,\frac{1}{\rho}}$$ lần lượt là các toán tử proximal của $$f$$ và $$g$$ với tham số $$\frac{1}{\rho}$$.

## Định nghĩa toán tử proximal

Nhắc lại rằng với hàm lồi $$f$$, [toán tử proximal]({% multilang_post_url contents/chapter19/21-03-24-19_01_01_Reminder:_proximal_gradient_descent %}) được định nghĩa là:
>$$
>\begin{align}
>{\operatorname{prox}}_{f, \lambda}(v) = \underset{x}{\operatorname{argmin}}\left(f(x)+\frac{1}{2\lambda}||x-v||_{2}^{2}\right). 
>\end{align}
>$$

## Suy ra các cập nhật proximal

Quá trình suy ra các cập nhật ADMM theo toán tử proximal như sau.

Gọi $$x^{+}, z^{+}, w^{+}$$ là các giá trị cập nhật của $$x, z, w$$ sau một bước.

### Cập nhật cho x:
>$$
>\begin{align}
>x^{+}& = \underset{x}{\operatorname{argmin}}f(x)+\frac{\rho}{2}||x-z+w||^{2}_{2}\\\\
>& =\underset{x}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(z-w)-x||^{2}_{2}+f(x)\\\\
>& ={\operatorname{prox}}_{f,\frac{1}{\rho}}(z-w)
>\end{align}
>$$

### Cập nhật cho z:
>$$
>\begin{align}
>z^{+}& = \underset{z}{\operatorname{argmin}}g(z)+\frac{\rho}{2}||x^{+}-z+w||^{2}_{2}\\\\
>& =\underset{z}{\operatorname{argmin}}\frac{1}{2\cdot\frac{1}{\rho}}||(x^{+}+w)-z||^{2}_{2}+g(z)\\\\
>& ={\operatorname{prox}}_{g,\frac{1}{\rho}}(x^{+}+w)
>\end{align}
>$$

## Nhận định then chốt

Ràng buộc ADMM ban đầu là $$Ax+Bz = c$$, còn ở đây ràng buộc là $$x=z$$. Nghĩa là, khi quan hệ biến đổi tuyến tính giữa $$x$$ và $$z$$ là phép đồng nhất, ta có thể biến đổi các cập nhật ADMM ban đầu thành các cập nhật proximal.

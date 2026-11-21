---
layout: post
title: '21-05 ADMM đồng thuận (Consensus ADMM)'
chapter: '21'
order: 6
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

# ADMM đồng thuận

## ADMM đồng thuận cơ bản

Xét bài toán sau:
>$$
>\begin{align}
>\min_{x}\sum^{B}_{i=1} f_{i}(x)
>\end{align}
>$$

Để giải bài toán này bằng ADMM, ta cần đưa vào các ràng buộc. Ở đây, ta muốn biến đổi phương trình về dạng dễ tính toán song song. Cách tiếp cận này, gọi là ADMM đồng thuận, tham số hóa lại phương trình như sau:
>$$
>\begin{align}
>&\min_{x_{1},...,x_{B},x} &&\sum^{B}_{i=1} f_{i}(x_{i})\\\\
>&\text{subject to } &&x_{i}=x, i = 1,...B
>\end{align}
>$$

## Thuật toán ADMM

Điều này cho phép ta tính các bước ADMM phân rã được:

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2}, i=1,...B\\\\
>x^{(k)} &=\frac{1}{B}\sum_{i=1}^{B}(x_{i}^{(k)}+w_{i}^{(k-1)})\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...,B
>\end{align}
>$$

## Dạng đơn giản hóa

Ngoài ra, ta có thể định nghĩa $$\overline{x}=\frac{1}{B}\sum_{i=1}^{B}x_{i}, \overline{w}=\frac{1}{B}\sum_{i=1}^{B}w_{i}$$. Từ đó có thể dễ dàng kiểm tra rằng $$\overline{w}^{(k)}=0$$ với các vòng lặp $$k>1$$, và phương trình thứ hai của cập nhật ADMM đơn giản thành $$x^{(k)}=\overline{x}^{(k)}$$. Do đó, ta có thể đơn giản hóa các phương trình cập nhật ADMM như sau:

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-\overline{x}^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2},  i=1,...B\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-\overline{x}^{(k)},  i=1,...,B.
>\end{align}
>$$

## Trực giác

Các cập nhật $$x_{i}$$ với $$i = 1,...,B$$ có thể được tính song song.

Từ các phương trình đã đơn giản hóa, ta có thể có được trực giác về ADMM đồng thuận. Mỗi cập nhật $$x_{i}$$ cố gắng cực tiểu hóa $$f_{i}(x_{i})$$ đồng thời dùng chính quy hóa $$l_{2}$$ để kéo từng $$x_{i}$$ về gần giá trị trung bình $$\overline{x}$$. Nếu $$x_{i}$$ lớn hơn trung bình thì $$w_{i}$$ tăng lên. Do đó, chính quy hóa ở bước tiếp theo sẽ làm giảm $$x_{i}$$ đã bị phình to.

## ADMM đồng thuận tổng quát

ADMM đồng thuận có thể được tổng quát hóa thành dạng tổng quát hơn. Hãy xem dạng bài toán với các phép biến đổi affine của $$x$$ và hàm bất kỳ $$g$$:

>$$
>\begin{align}
>\min_{x}\sum_{i=1}^{B} f_{i}(a^{T}_{i}x+b_{i})+g(x)
>\end{align}
>$$

Với phương trình này, ta cũng tham số hóa lại bằng cách thêm các ràng buộc:
>$$
>\begin{align}
>&\min_{x_{1},..x_{B},x} &&\sum^{B}_{i=1}f_{i}(a_{i}^{T}x_{i}+b_{i})+g(x)\\\\
>&\text{subject to } &&x_{i} = x, i=1,...B
>\end{align}
>$$ 

Sau đó ta có thể suy ra các cập nhật ADMM phân rã được:
>$$
>\begin{align}
>x_{i}^{(k)} &= \underset{x_{i}}{\operatorname{argmin}}f_{i}(a_{i}^{T}x_{i}+b_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||^{2}_{2}\\\\
>x^{(k)}&=\underset{x}{\operatorname{argmin}} \frac{B\rho}{2}||x-\overline{x}^{(k)}-\overline{w}^{(k-1)}||^{2}_{2}+g(x)\\\\
>w_{i}^{(k)}&=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...B
>\end{align}
>$$ 

## Những điểm khác biệt chính

Những khác biệt giữa ADMM đồng thuận tổng quát và ADMM đồng thuận đã suy ra ở trên có thể tóm tắt như sau:

* Vì các phương trình bước ADMM không đơn giản hóa được, $$\overline{w}^{(k)}=0$$ không còn được thỏa mãn.
* $$x_{i}, i=1,...,B$$ có thể được cập nhật song song.
* Mỗi cập nhật $$x_{i}$$ có thể xem như cực tiểu hóa phần mất mát tương ứng cùng với chính quy hóa $$l_2$$.
* Cập nhật $$x$$ là một phép toán proximal cho hàm bất kỳ $$g$$ (thường là một số hạng chính quy hóa).
* Các thuật toán ADMM khác nhau được suy ra tùy theo cách tham số hóa lại.

Thông tin chi tiết xem [các bài báo tham khảo]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).

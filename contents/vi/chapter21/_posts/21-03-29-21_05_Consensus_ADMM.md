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

Xét bài toán tối ưu tổng các hàm mục tiêu sau:
>$$
>\begin{align}
>\min_{x}\sum^{B}_{i=1} f_{i}(x)
>\end{align}
>$$

Để áp dụng ADMM và đồng thời biến đổi bài toán sang dạng dễ tính toán song song, phương pháp ADMM đồng thuận (consensus ADMM) tham số hóa lại bài toán bằng cách gán cho mỗi thành phần một bản sao biến cục bộ $$x_i$$ kèm ràng buộc đồng nhất:
>$$
>\begin{align}
>&\min_{x_{1},...,x_{B},x} &&\sum^{B}_{i=1} f_{i}(x_{i})\\\\
>&\text{subject to } &&x_{i}=x, i = 1,...B
>\end{align}
>$$

## Thuật toán ADMM

Cách tách biến này cho phép suy ra các bước cập nhật ADMM phân rã được theo từng khối:

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2}, i=1,...B\\\\
>x^{(k)} &=\frac{1}{B}\sum_{i=1}^{B}(x_{i}^{(k)}+w_{i}^{(k-1)})\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...,B
>\end{align}
>$$

## Dạng rút gọn

Đặt $$\overline{x}=\frac{1}{B}\sum_{i=1}^{B}x_{i}$$ và $$\overline{w}=\frac{1}{B}\sum_{i=1}^{B}w_{i}$$. Dễ dàng kiểm tra rằng $$\overline{w}^{(k)}=0$$ với mọi vòng lặp $$k \ge 1$$, nhờ đó bước cập nhật biến toàn cục rút gọn thành $$x^{(k)}=\overline{x}^{(k)}$$. Khi đó, thuật toán được viết gọn lại như sau:

>$$
>\begin{align}
>x^{(k)}_{i} &= \underset{x_{i}}{\operatorname{argmin}} f_{i}(x_{i})+\frac{\rho}{2}||x_{i}-\overline{x}^{(k-1)}+w_{i}^{(k-1)}||_{2}^{2},  i=1,...B\\\\
>w_{i}^{(k)} &=w_{i}^{(k-1)}+x_{i}^{(k)}-\overline{x}^{(k)},  i=1,...,B.
>\end{align}
>$$

## Trực giác

Các bước cập nhật $$x_{i}$$ ($$i = 1,\ldots,B$$) hoàn toàn độc lập nên có thể tính song song.

Từ dạng rút gọn trên, ta có thể hiểu trực quan cơ chế của ADMM đồng thuận: mỗi bước cập nhật $$x_{i}$$ vừa tìm cách cực tiểu hóa hàm mục tiêu riêng $$f_{i}(x_{i})$$, vừa chịu số hạng phạt $$l_{2}$$ kéo $$x_{i}$$ tiến về giá trị trung bình toàn cục $$\overline{x}$$. Nếu $$x_{i}$$ lớn hơn mức trung bình, biến đối ngẫu $$w_{i}$$ sẽ tăng lên, khiến số hạng phạt ở vòng lặp kế tiếp tạo lực kéo mạnh hơn để giảm $$x_{i}$$ về lại gần trung bình.

## ADMM đồng thuận tổng quát

ADMM đồng thuận có thể mở rộng cho lớp bài toán có phép biến đổi affine của $$x$$ và thêm một hàm chính quy hóa bất kỳ $$g$$:

>$$
>\begin{align}
>\min_{x}\sum_{i=1}^{B} f_{i}(a^{T}_{i}x+b_{i})+g(x)
>\end{align}
>$$

Ta tiếp tục tham số hóa lại bài toán bằng các ràng buộc đồng thuận:
>$$
>\begin{align}
>&\min_{x_{1},..x_{B},x} &&\sum^{B}_{i=1}f_{i}(a_{i}^{T}x_{i}+b_{i})+g(x)\\\\
>&\text{subject to } &&x_{i} = x, i=1,...B
>\end{align}
>$$ 

Từ đó thu được các bước cập nhật ADMM phân rã được:
>$$
>\begin{align}
>x_{i}^{(k)} &= \underset{x_{i}}{\operatorname{argmin}}f_{i}(a_{i}^{T}x_{i}+b_{i})+\frac{\rho}{2}||x_{i}-x^{(k-1)}+w_{i}^{(k-1)}||^{2}_{2}\\\\
>x^{(k)}&=\underset{x}{\operatorname{argmin}} \frac{B\rho}{2}||x-\overline{x}^{(k)}-\overline{w}^{(k-1)}||^{2}_{2}+g(x)\\\\
>w_{i}^{(k)}&=w_{i}^{(k-1)}+x_{i}^{(k)}-x^{(k)}, i=1,...B
>\end{align}
>$$ 

## Những điểm khác biệt chính

So với dạng cơ bản, ADMM đồng thuận tổng quát có các đặc điểm sau:

* Do bước cập nhật $$x^{(k)}$$ không còn rút gọn thành trung bình đơn thuần, tính chất $$\overline{w}^{(k)}=0$$ không còn giữ nguyên.
* Các biến cục bộ $$x_{i}$$ ($$i=1,\ldots,B$$) vẫn được cập nhật song song.
* Mỗi bước cập nhật $$x_{i}$$ tương ứng với việc cực tiểu hóa thành phần mất mát cục bộ kết hợp với số hạng phạt $$l_2$$.
* Bước cập nhật biến toàn cục $$x$$ trở thành một phép tính toán tử proximal đối với hàm $$g$$ (thường là số hạng chính quy hóa).
* Các cách tham số hóa lại khác nhau sẽ dẫn đến những biến thể thuật toán ADMM khác nhau.

Chi tiết tham khảo thêm tại [danh mục bài báo tham khảo của Chương 21]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).

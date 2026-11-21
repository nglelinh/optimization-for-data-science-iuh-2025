---
layout: post
title: 21-06 Faster convergence with subprogram parametrization - example of the 2d
  fused lasso problem
chapter: '21'
order: 7
owner: Hooncheol Shin
lesson_type: optional
categories:
- chapter21
lang: vi
---

# Hội tụ nhanh hơn nhờ tham số hóa bài toán con

## Giới thiệu

Một tính chất rất thú vị của ADMM là khi giải bài toán, nếu ta tham số hóa các bài toán con nhỏ theo một cách đặc biệt thì nó có thể cho hiệu năng hội tụ nhanh hơn nhiều so với các phương pháp thông thường. Trong ví dụ ADMM đồng thuận trước đó, các cập nhật tối ưu theo từng khối biến, tương tự block coordinate descent. Do đó, ADMM cũng có thể đạt hội tụ nhanh bằng cách cập nhật các khối biến theo các hướng gần như trực giao.

## Ví dụ fused lasso 2D

Trong phần này, ta sẽ minh họa các khái niệm trên qua ví dụ, thiết kế các ràng buộc phụ sao cho các cập nhật gốc đi theo các hướng không tương quan (de-correlated).

Thông tin chi tiết xem [RT16], [WSK14], [BS14].

Hãy xem xét bài toán fused lasso 2D hay khử nhiễu total variation 2D, một trong các ví dụ ta đã xem ở [Chương 1]({% multilang_post_url contents/chapter01/21-01-07-01_01_optimization_problems %}). Cho một ảnh $$Y\in \mathbb{R}^{d\times d}$$, bài toán được định nghĩa như sau:

>$$
>\begin{align}
>\min_{\Theta}\frac{1}{2}||Y-\Theta||^{2}_{F}+\lambda \sum_{i,j}(|\Theta_{i,j}-\Theta_{i+1,j}|+|\Theta_{i,j}-\Theta_{\Theta_{i,j+1}}|).
>\end{align}
>$$

Trong bài toán này, mỗi điểm ảnh có một tham số, và ma trận tham số này là $$\Theta\in \mathbb{R}^{d\times d}$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/2dfussed.png" alt="[Hình 1] Diễn giải số hạng phạt trong fused lasso 2D [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Diễn giải số hạng phạt trong fused lasso 2D [3]</figcaption>
</p>
</figure>

[Hình 1] minh họa trực quan số hạng phạt, tức số hạng thứ hai của hàm mục tiêu. Như thấy từ bài toán đã định nghĩa, nó nhằm giảm sự chênh lệch giữa một điểm ảnh và các điểm ảnh kề theo chiều ngang và chiều dọc. Nghĩa là số hạng phạt này làm cho giá trị của các điểm ảnh lân cận giống nhau.

## Dạng vector

Viết gọn số hạng phạt bằng một toán tử, bài toán trở thành:
>$$
>\begin{align}
>\min_{\theta}\frac{1}{2}||y-\theta||^{2}_{F} + \lambda||D\theta||_{1}.
>\end{align}
>$$

trong đó $$D\in \mathbb{R}^{m\times n}$$ là toán tử sai phân 2D tương ứng với phương trình gốc.

## Các dạng cập nhật ADMM cho bài toán fused lasso 2D

Bây giờ ta muốn tạo các bước ADMM theo hai cách bằng việc áp dụng các ràng buộc phụ.

Cách thứ nhất là suy ra ADMM từ dạng vector tạo bởi toán tử sai phân 2D.

>$$
>\begin{align}
>\min_{\theta, z}\frac{1}{2}||y-\theta||^{2}_{2}+\lambda||z||_{1} \qquad \text{subject to   }z = D\theta,
>\end{align}
>$$

Các bước ADMM khi đó được suy ra như sau:
>$$
>\begin{align}
>\theta^{(k)} &= (I+\rho D^{T}D)^{-1}(y+\rho D^{T}(z^{(k-1)}+w^{(k-1)}))\\\\
>z^{(k)} &= S_{\frac{\lambda}{\rho}}(D\theta^{(k)}-w^{(k-1)})\\\\
>w^{(k)} &= w^{(k-1)}+z^{(k-1)}-D\theta ^{(k)}.
>\end{align}
>$$

## Độ phức tạp tính toán - dạng vector

Giải cho $$\theta$$ tương đương với giải hệ tuyến tính $$(I+\rho D^{T}D)^{-1}$$. Ở đây, $$D^{T}D$$ trở thành ma trận Laplace $$L=D^{T}D$$ của lưới 2D, có thể giải trong $$O(n)$$ phép tính. Cập nhật $$z$$ cũng cần $$O(n)$$ phép tính vì chỉ áp dụng toán tử soft thresholding $$S_{t}$$. Do đó, giải ADMM dạng vector mất thời gian $$O(n)$$.

## ADMM dạng ma trận

Cách thứ hai là suy ra ADMM dạng ma trận, giống hệt định nghĩa bài toán gốc.
>$$
>\begin{align}
>&\min_{\Theta, Z} &&\frac{1}{2}||Y-\Theta||^{2}_{F}+\lambda\sum_{i,j}(|\Theta_{i,j}-\Theta_{i+1,j}+|Z_{i+1,j}-Z_{i,j+1}|)\\\\
>&\text{subject to } &&\Theta = Z
>\end{align}
>$$

Các bước ADMM như sau:
>$$
>\begin{align}
>\Theta_{\cdot \\ , j}^{(k)} &= FL^{1d}_{ \frac{\lambda}{(1+\rho)} } \bigg( \frac{ Y+\rho( Z^{(k-1)}_{\cdot \\ , j}-W_{\cdot \\ ,j}^{(k-1)} ) } {1+\rho} \bigg),\qquad j=1,...,d\\\\
>Z_{i, \cdot}^{(k)} &= FL^{1d}_{\frac{\lambda}{\rho}} \bigg(\Theta_{i, \cdot}^{(k)} + W_{i, \cdot}^{(k-1)} \bigg), \qquad j=1,...,d\\\\
>W^{(k)} &= W^{(k-1)} + \Theta^{(k)} - Z^{(k)} \\\\
>\end{align}
>$$
trong đó $$FL_{\tau}^{1d}(a)$$ là fused lasso 1D, được định nghĩa là $$FL_{\tau}^{1d}(a) = \underset{x}{\operatorname{argmin}}\frac{1}{2}||a-x||^{2}_{2}+\tau\sum_{i=1}^{d-1}|x_{i}-x_{i+1}|$$.

## Độ phức tạp tính toán - dạng ma trận

ADMM dạng ma trận cũng có thể thực hiện với độ phức tạp thời gian $$O(n)$$. Cả $$\Theta$$ và $$Z$$ đều có dạng fused lasso 1D, vốn có độ phức tạp thời gian $$O(n)$$.

[Hình 2] cho thấy số hạng phạt gốc được tách thành các bài toán fused lasso 1D như thế nào.
 
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/2dfussedlasso.png" alt="[Hình 2] Diễn giải các cập nhật ADMM dạng ma trận cho fused lasso 2D [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 2] Diễn giải các cập nhật ADMM dạng ma trận cho fused lasso 2D [3]</figcaption>
</p>
</figure>


## Thí nghiệm khử nhiễu ảnh

Bây giờ hãy xem lại bài toán khử nhiễu ảnh đã xét ở Chương 1.

[Hình 3] cho thấy dữ liệu và các ảnh đã khử nhiễu. [Hình 4] cho thấy so sánh hai phương pháp ADMM. ADMM "chuyên biệt" dạng ma trận, định nghĩa ràng buộc bằng cách phân rã theo hướng dọc/ngang, cho hiệu năng hội tụ nhanh hơn nhiều so với "ADMM chuẩn" suy ra ở dạng vector.

[Hình 5] cho thấy chất lượng ảnh theo các vòng lặp ADMM.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/ll1.png" alt="[Hình 3] Dữ liệu và ảnh nghiệm chính xác (ảnh 300x200: n = 60.000). Trái: ảnh gốc trước khi khử nhiễu, phải: nghiệm chính xác của ảnh đã khử nhiễu [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 3] Dữ liệu và ảnh nghiệm chính xác (ảnh 300x200: n = 60.000). Trái: ảnh gốc trước khi khử nhiễu, phải: nghiệm chính xác của ảnh đã khử nhiễu [3]</figcaption>
</p>
</figure>


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/ll2.png" alt="[Hình 4] Đường hội tụ của hai thuật toán ADMM. Đen: chuẩn (dạng vector), đỏ: chuyên biệt (dạng ma trận) [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 4] Đường hội tụ của hai thuật toán ADMM. Đen: chuẩn (dạng vector), đỏ: chuyên biệt (dạng ma trận) [3]</figcaption>
</p>
</figure>


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/admm_iteration_visualized.png" alt="[Hình 5] Các điểm lặp ADMM sau k = 10, 30, 50, 100 vòng lặp [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 5] Các điểm lặp ADMM sau k = 10, 30, 50, 100 vòng lặp [3]</figcaption>
</p>
</figure>

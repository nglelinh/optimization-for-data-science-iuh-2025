---
layout: post
title: '09-04 Các trường hợp đặc biệt'
chapter: '09'
order: 5
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Các trường hợp đặc biệt

Phương pháp gradient gần kề còn được gọi là phương pháp gradient descent tổng hợp (composite gradient descent) hoặc gradient descent tổng quát (generalized gradient descent).

Lý do phương pháp này mang tính **"tổng quát"** là vì nó bao hàm các thuật toán quen thuộc sau như những trường hợp đặc biệt:

- $$h = 0 \to$$ phương pháp gradient descent
- $$h = I_C \to$$ phương pháp gradient descent có chiếu (projected gradient descent)
- $$g = 0 \to$$ thuật toán tối ưu gần kề (proximal minimization algorithm)

Nhờ cùng nằm trong khuôn khổ chung này, tất cả các thuật toán trên đều thừa hưởng tốc độ hội tụ $$O(1/\epsilon)$$.

## Gradient descent có chiếu (Projected gradient descent)
Với $$I_C(x)$$ là hàm chỉ thị của một tập lồi đóng $$C \subseteq \mathbb{R}^n$$, bài toán tối ưu có ràng buộc trên tập $$C$$ có thể được viết lại thành bài toán không ràng buộc như sau (lưu ý $$C$$ cần là tập đóng để phép chiếu được xác định duy nhất):

> $$ \min_{x \in C} g(x) \iff \min_x g(x) + I_C(x)$$
>
> $$I_C(x) = 
>\begin{cases}
>0, & x \in C \\
>\infty, & x \notin C
>\end{cases}$$

Khi đó, ánh xạ gần kề của $$I_C$$ là:

> $$
>\begin{align}
>\text{prox}_t(x)  
>&= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + I_C(z) \\
>& = \underset{z \in C}{\text{argmin}} \lVert x−z \rVert_2^2
>\end{align} $$

Do đó $$\text{prox}_t(x) = P_C(x)$$ chính là phép chiếu Euclid lên tập $$C$$.

Bước cập nhật gradient gần kề trở thành $$x^+ = P_C (x−t \nabla g(x) )$$: sau khi thực hiện một bước gradient descent, ta chiếu điểm vừa thu được trở về tập khả thi $$C$$.

Trong hình minh họa dưới đây, hình chữ nhật màu hồng là tập khả thi $$C$$. Khi bước gradient descent đưa điểm lặp ra ngoài $$C$$, phép chiếu $$P_C$$ đưa điểm đó quay lại điểm gần nhất thuộc $$C$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/projected_gradient_descent.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 1] Projected Gradient Descent [3]</figcaption>
</p>
</figure>

## Thuật toán tối ưu gần kề (Proximal Minimization Algorithm)

Xét bài toán cực tiểu hóa một hàm lồi $$h$$ không nhất thiết khả vi, tương ứng với trường hợp $$g(x) = 0$$:
>
\begin{align}
\min_x h(x)
\end{align}

Công thức lặp gradient gần kề rút gọn thành:
> $$
\begin{align}
x^{(k)} &= \text{prox}_{t_k} \big(x^{(k-1)} - t_k \nabla g ( x^{(k-1)} ) \big) , \qquad k = 1, 2, 3, ... \\
&= \text{prox}_{t_k} \big(x^{(k-1)} \big) ,  \qquad \qquad \qquad \qquad \; k = 1, 2, 3, ... \\
\end{align} $$

Hay viết tường minh:
> $$x^+ = \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

Thuật toán này được gọi là **thuật toán tối ưu gần kề (PMA)**. Về số bước lặp, PMA hội tụ nhanh hơn phương pháp subgradient; tuy nhiên, thuật toán chỉ thực sự hữu ích khi ánh xạ gần kề của $$h$$ có thể tính được hiệu quả (ví dụ ở dạng đóng).

## Khi ánh xạ gần kề không thể tính chính xác
Về mặt lý thuyết, khi áp dụng phương pháp gradient gần kề cho $$f = g + h$$, ta giả định bài toán con xác định $$\text{prox}_t(x)$$ được giải chính xác:
>  $$\text{prox}_t(x )= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

Nếu bài toán con này chỉ được giải xấp xỉ, nhìn chung không tự động đảm bảo kết quả hội tụ ban đầu. Tuy nhiên, nếu sai số xấp xỉ của toán tử gần kề giảm đủ nhanh và được kiểm soát chặt chẽ, tốc độ hội tụ ban đầu vẫn được bảo toàn (Schmidt et al. (2011), Convergence rates of inexact proximal-gradient methods for convex optimization).

Trong thực hành, khi phải tính gần đúng $$\text{prox}_t$$, người ta thường giải bài toán con với độ chính xác cao.

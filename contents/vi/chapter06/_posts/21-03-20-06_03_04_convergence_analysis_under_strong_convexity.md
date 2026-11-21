---
layout: post
title: 06-03-04 Convergence analysis under strong convexity
chapter: '06'
order: 11
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Nếu $$f$$ thỏa mãn điều kiện sau thì $$f$$ lồi mạnh (giả sử $$f$$ khả vi hai lần và $$m > 0$$):
> $$ \begin{align}
f(y) \ge f(x) + \nabla f(x)^T(y-x) + \frac{m}{2} \| y-x \|_2^2, \quad \forall x, y
\end{align} $$

Ở đây $$f$$ có một cận dưới bậc hai, và hằng số $$m$$ được xác định bởi giá trị riêng nhỏ nhất của Hessian của $$f$$.

Với một hàm $$f$$ bất kỳ, $$f$$ lồi mạnh nếu:
> $$ \begin{align}
g(x) = f(x) - \frac{m}{2} \| x \|_2^2 \quad \text{là hàm lồi với mọi } x \text{ và } m > 0
\end{align} $$

## Định lý hội tụ
Với tính liên tục Lipschitz và tính lồi mạnh, định lý sau đây được thỏa mãn (với $$L$$ là hằng số Lipschitz và $$m$$ là hằng số lồi mạnh):

**Gradient descent** với kích thước bước cố định ($$t \le 2/(m + L)$$) hoặc backtracking line search thỏa mãn:
> $$ \begin{align}
f(x^{(k)}) - f^* \le c^k \frac{L}{2} \| x^{(0)} - x^* \|_2^2, \quad c = (1 - \frac{m}{L}), \quad 0 < c < 1
\end{align} $$

## Chứng minh
Nếu $$\nabla f$$ liên tục Lipschitz và $$f$$ lồi mạnh thì $$f$$ có một cận trên bậc hai (xem [06-03-02]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})).

Với gradient descent $$x^+ = x - t \nabla f(x)$$, kích thước bước $$t = 1/L$$ cho ta:
> $$ \begin{align}
f(x^+) \le f(x) -  \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Trừ cả hai vế cho $$f(x^*)$$:
> $$ \begin{align}
f(x^+) - f(x^*) \le f(x) - f(x^*) -  \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Vì $$f$$ lồi mạnh nên thỏa mãn điều kiện:
> $$ \begin{align}
f(x) - f(x^*) \le \frac{1}{2m} \| \nabla f(x) \|_2^2
\end{align} $$

Thay vào, ta được:
> $$ \begin{align}
f(x^+) - f(x^*) & \le f(x) - f(x^*) -  \frac{m}{L} ( f(x) - f(x^*) ) \\
& =  (1 -  \frac{m}{L} ) ( f(x) - f(x^*) ) \\
& = c  ( f(x) - f(x^*) ) \\
\end{align} $$

Lặp lại quá trình này, ta được:
> $$ \begin{align}
f(x^{(k)}) - f(x^*) \le c^k ( f(x^{(0)}) - f(x^*) ) \\
\end{align} $$

Từ khai triển Taylor (cận trên bậc hai) của hàm với $$y = x^{(0)}$$ và $$x = x^*$$:
> $$ \begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \lVert y - x \rVert^2_2  \space \space \forall x, y
\end{align} $$

Do $$\nabla f(x^*) = 0$$, ta có:
> $$ \begin{align}
f(x^{(0)}) & \le f(x^{*}) + \nabla f(x^{*})^T (x^{(0)}- x^{*} ) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\\\
& =  f(x^{*}) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\\\
\end{align} $$

Sắp xếp lại:
> $$ \begin{align}
f(x^{(0)}) - f(x^{*}) & \le \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\\\
\end{align} $$

Thay vào bất đẳng thức trước đó, ta được:
> $$ \begin{align}
f(x^{(k)}) - f(x^{*}) & \le c^k \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2  \\\
\end{align} $$

Điều này chứng minh định lý hội tụ của gradient descent dưới tính lồi mạnh.

## Hội tụ tuyến tính
Khi $$f$$ lồi mạnh, tốc độ hội tụ là $$O(c^k)$$, tức là hội tụ theo hàm mũ.
Để đạt $$f(x^{(k)}) - f^{*} \le \epsilon$$ cần $$O(\log(1/\epsilon))$$ vòng lặp.
(Nếu không có tính lồi mạnh thì cần $$O(1/\epsilon)$$ vòng lặp.)

Tốc độ hội tụ $$O(c^k)$$ trông như một đường thẳng trên đồ thị bán logarit, như hình dưới đây.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06.03_01_01_Line_Convergence.png" alt="Line_Convergence" width="60%" height="60%">
  <figcaption style="text-align: center;">[Hình 1] Hội tụ tuyến tính [1]</figcaption>
</p>
</figure>

Ở đây, hằng số $$c$$ trong $$O(c^k)$$ bằng $$1 - \frac{m}{L}$$ và phụ thuộc vào số điều kiện $$L/m$$. Số điều kiện càng lớn thì hội tụ càng chậm (số điều kiện là tỉ số giữa giá trị riêng lớn nhất và giá trị riêng nhỏ nhất).

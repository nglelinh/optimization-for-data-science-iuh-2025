---
layout: post
title: 06-03-04 Convergence analysis under strong convexity
chapter: '06'
order: 13
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Một hàm $$f$$ khả vi được gọi là lồi mạnh với hằng số $$m > 0$$ nếu thỏa mãn điều kiện sau:
> $$ \begin{align}
f(y) \ge f(x) + \nabla f(x)^T(y-x) + \frac{m}{2} \| y-x \|_2^2, \quad \forall x, y
\end{align} $$

Nói cách khác, $$f$$ có một cận dưới bậc hai. Khi $$f$$ khả vi hai lần, hằng số $$m$$ được chặn trên bởi giá trị riêng nhỏ nhất của ma trận Hessian của $$f$$.

Tổng quát hơn, hàm $$f$$ lồi mạnh với hằng số $$m > 0$$ khi và chỉ khi:
> $$ \begin{align}
g(x) = f(x) - \frac{m}{2} \| x \|_2^2 \quad \text{là hàm lồi trên miền xác định của } f
\end{align} $$

## Định lý Hội tụ

Khi $$f$$ vừa có gradient liên tục Lipschitz với hằng số $$L$$ vừa lồi mạnh với hằng số $$m$$, ta có kết quả sau:

Thuật toán **gradient descent** với kích thước bước cố định ($$t \le 2/(m + L)$$) hoặc tìm kiếm đường lùi thỏa mãn:
> $$ \begin{align}
f(x^{(k)}) - f^* \le c^k \frac{L}{2} \| x^{(0)} - x^* \|_2^2, \quad c = 1 - \frac{m}{L}, \quad 0 < c < 1
\end{align} $$

## Chứng minh

Vì $$f$$ có gradient liên tục Lipschitz với hằng số $$L$$, hàm $$f$$ thỏa mãn cận trên bậc hai (xem [06-03-01]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})).

Với bước cập nhật gradient descent $$x^+ = x - t \nabla f(x)$$ và chọn kích thước bước $$t = 1/L$$, ta thu được:
> $$ \begin{align}
f(x^+) \le f(x) - \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Trừ hai vế cho $$f(x^*)$$:
> $$ \begin{align}
f(x^+) - f(x^*) \le f(x) - f(x^*) - \frac{1}{2L} \| \nabla f(x) \|_2^2
\end{align} $$

Do $$f$$ lồi mạnh với hằng số $$m$$, ta có bất đẳng thức:
> $$ \begin{align}
f(x) - f(x^*) \le \frac{1}{2m} \| \nabla f(x) \|_2^2
\end{align} $$

Thay bất đẳng thức này vào vế phải ở trên, ta được:
> $$ \begin{align}
f(x^+) - f(x^*) & \le f(x) - f(x^*) - \frac{m}{L} ( f(x) - f(x^*) ) \\
& = \left(1 - \frac{m}{L} \right) ( f(x) - f(x^*) ) \\
& = c ( f(x) - f(x^*) )
\end{align} $$

Áp dụng quy nạp qua $$k$$ bước lặp:
> $$ \begin{align}
f(x^{(k)}) - f(x^*) \le c^k ( f(x^{(0)}) - f(x^*) )
\end{align} $$

Mặt khác, từ cận trên bậc hai áp dụng tại $$y = x^{(0)}$$ và $$x = x^*$$:
> $$ \begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \lVert y - x \rVert^2_2 \quad \forall x, y
\end{align} $$

Vì $$\nabla f(x^*) = 0$$, ta thu được:
> $$ \begin{align}
f(x^{(0)}) & \le f(x^{*}) + \nabla f(x^{*})^T (x^{(0)}- x^{*} ) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2 \\
& = f(x^{*}) + \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2
\end{align} $$

Suy ra:
> $$ \begin{align}
f(x^{(0)}) - f(x^{*}) & \le \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2
\end{align} $$

Thay vào bất đẳng thức quy nạp trước đó, ta có:
> $$ \begin{align}
f(x^{(k)}) - f(x^{*}) & \le c^k \frac{L}{2} \lVert x^{(0)} - x^{*} \rVert^2_2
\end{align} $$

Điều này hoàn tất chứng minh định lý hội tụ của gradient descent dưới giả thiết lồi mạnh.

## Hội tụ Tuyến tính

Khi $$f$$ lồi mạnh, sai số giảm theo tốc độ $$O(c^k)$$, tức là hội tụ theo cấp số nhân (hội tụ tuyến tính). Để đạt $$f(x^{(k)}) - f^{*} \le \epsilon$$, thuật toán chỉ cần $$O(\log(1/\epsilon))$$ vòng lặp (so với $$O(1/\epsilon)$$ vòng lặp khi không có tính lồi mạnh).

Trên đồ thị bán logarit, tốc độ hội tụ $$O(c^k)$$ có dạng một đường thẳng như minh họa dưới đây.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06.03_01_01_Line_Convergence.png" alt="Line_Convergence" width="60%" height="60%">
  <figcaption style="text-align: center;">[Hình 1] Hội tụ tuyến tính [1]</figcaption>
</p>
</figure>

Ở đây, hằng số $$c = 1 - \frac{m}{L}$$ phụ thuộc trực tiếp vào chỉ số điều kiện $$L/m$$ (tỉ số giữa giá trị riêng lớn nhất và nhỏ nhất của Hessian). Chỉ số điều kiện càng lớn thì $$c$$ càng gần 1 và tốc độ hội tụ càng chậm.

Cấu trúc đại số của chứng minh này — kết hợp bổ đề giảm (descent lemma) với một cận dưới liên hệ $$\|\nabla f\|^2$$ và độ chênh lệch giá trị hàm — vẫn giữ nguyên hiệu lực khi giả thiết lồi mạnh được nới lỏng thành bất đẳng thức Polyak–Łojasiewicz. Nội dung mở rộng tùy chọn về tốc độ hội tụ hiện đại này, cùng ví dụ bài toán bình phương tối thiểu quá tham số (nơi nghiệm cực tiểu không duy nhất), được trình bày tại [28-05 Điều kiện PL và câu chuyện tốc độ hiện đại]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}).

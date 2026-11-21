---
layout: post
title: '19-05 Các ví dụ đáng chú ý'
chapter: '19'
order: 9
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

## Glmnet và QUIC
Có hai gói phần mềm rất nổi tiếng được xây dựng trên phương pháp Newton proximal.

* **glmnet** (Friedman et al., 2009): cài đặt prox Newton cho các mô hình tuyến tính tổng quát (generalized linear models) có phạt $$l_1$$. Bài toán bên trong được giải bằng coordinate descent.

* **QUIC** (Hsieh et al., 2011): cài đặt prox Newton cho bài toán graphical lasso. Nó dùng một mẹo phân rã (factorization trick) và giải bài toán bên trong bằng coordinate descent.

Cả hai gói đều được sử dụng rộng rãi cho các mục đích tương ứng và có thể coi là hiện đại nhất (state of the art).

Phương pháp Newton proximal tính gradient của $$g$$ ít thường xuyên hơn proximal gradient descent. Do đó, $$g$$ càng đắt để tính thì Newton proximal càng có lợi. Việc chọn bộ giải bên trong cẩn thận cũng giúp đạt hiệu năng tốt hơn.

## Ví dụ: hồi quy logistic lasso
Hãy xem ví dụ trong Lee et al. (2012).

Với hồi quy logistic chính quy hóa $$l_1$$, ba phương pháp sau được so sánh:
1. FISTA: proximal gradient tăng tốc 2. spaRSA: phương pháp gradient chiếu phổ (spectral projected gradient) 3. PN: Newton proximal

#### Hessian dày đặc (n=5000, p=6000)
Bài toán đầu tiên có ma trận đặc trưng dày đặc $$X$$ với n = 5000 mẫu và p = 6000 đặc trưng. Vì Hessian dày đặc nên đây là bài toán rất thách thức. Hiệu năng quan sát được như sau.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example1.png" alt="[Hình 1] Hessian dày đặc X (n=5000, p=6000) [2]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Hessian dày đặc X (n=5000, p=6000) [2]</figcaption>
</p>
</figure>

Đồ thị bên phải đo hiệu năng theo số lần gọi hàm và đồ thị bên trái đo theo thời gian. Xét theo số lần gọi hàm, PN rõ ràng vượt trội.

Ở đây phần lớn chi phí dành cho việc tính $$g$$ và $$\nabla g$$, đặc biệt là việc tính các hàm $$\exp$$ và $$\log$$.

#### Hessian thưa (n=542,000, p=47,000)

Trong trường hợp tiếp theo $$X$$ thưa nên việc tính $$g$$ và $$\nabla g$$ tốn ít thời gian hơn.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example-sparse.png" alt="[Hình 2] Hessian thưa X (n=542,000, p=47,000) [2]" width="70%">
  <figcaption style="text-align: center;">[Hình 2] Hessian thưa X (n=542,000, p=47,000) [2]</figcaption>
</p>
</figure>

## Tính prox không chính xác
Khi phương pháp Newton proximal tính toán tử proximal, prox nói chung không có dạng đóng nên không thể tính chính xác. Tuy vậy, nếu prox được tính với độ chính xác cao thì đó là một tính chất rất tốt.

Lee (2014) đã đề xuất các quy tắc dừng cho bài toán bên trong, đảm bảo hội tụ toàn cục và hội tụ siêu tuyến tính cục bộ.

#### Ba quy tắc dừng
Ba quy tắc dừng cho tối ưu bên trong được so sánh trên bài toán ước lượng graphical lasso với n = 72 mẫu và p = 1255 đặc trưng.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Inexact_prox.png" alt="[Hình 3] Ba quy tắc dừng [2]" width="70%">
  <figcaption style="text-align: center;">[Hình 3] Ba quy tắc dừng [2]</figcaption>
</p>
</figure>

Ba quy tắc dừng là adaptive, maxiter = 10 và exact. Maxiter thực hiện tối đa 10 vòng lặp bên trong; exact lặp cho đến khi tìm được nghiệm chính xác.

Vì phương pháp Newton proximal hội tụ bậc hai, quy tắc exact thể hiện hội tụ bậc hai. Với maxiter = 10, tối đa 10 vòng lặp bên trong là không đủ để giữ hội tụ bậc hai, trong khi quy tắc adaptive đạt được hội tụ bậc hai và là nhanh nhất trong ba quy tắc.

#### Quy tắc dừng của phương pháp Newton thông thường
Trong phương pháp Newton thông thường, bài toán bên trong cực tiểu hóa xấp xỉ bậc hai $$\tilde{g}_{k-1}$$ của $$g$$ tại $$x^{(k-1)}$$. Ta chọn một dãy $$\eta_k, k=1,2,3,...$$ (gọi là dãy cưỡng bức, forcing sequence) và dừng khi điều kiện sau được thỏa mãn.

> \begin{align}
\parallel \nabla \tilde{g}_{k-1}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  \nabla g(x^{(k-1)})  \parallel_2 \\\\
\end{align}

Điều kiện này nói rằng gradient của mô hình tại điểm tiếp theo nhỏ hơn gradient tại điểm hiện tại tối đa $$\eta_k$$ lần. Ở đây xấp xỉ bậc hai là $$\tilde{g}_{k-1}(z) = \nabla g(x^{(k-1)})^T (z-x^{(k-1)}) + \frac{1}{2} (z - x^{(k-1)})^T \nabla^2 g(x^{(k-1)}) (z - x^{(k-1)})$$.

#### Quy tắc dừng của phương pháp Newton proximal
Lee et al. (2012) đề xuất dùng gradient tổng quát thay cho gradient trong trường hợp proximal.

> $$
> \begin{align}
\parallel G_{\tilde{f}_{k-1}/M}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  G_{f/M}(x^{(k-1)})  \parallel_2
\end{align}
> $$

Ở đây $$\tilde{f}_{k-1} = \tilde{g}_{k-1} + h$$ và $$mI \preceq \nabla^2 g \preceq MI$$.

Sau đó họ chứng minh rằng nếu $$\eta_k$$ được chọn như sau thì phương pháp Newton proximal không chính xác có tốc độ siêu tuyến tính cục bộ.

> $$
> \begin{align}
> \eta_k \le \min \left\{ \frac{m}{2},  \frac{\parallel  G_{\tilde{f}_{k-2}/M}(x^{(k-1)}) - G_{f/M}(x^{(k-1)})  \parallel_2}{\parallel  G_{f/M}(x^{(k-2)})  \parallel_2} \right\}
> \end{align}
> $$

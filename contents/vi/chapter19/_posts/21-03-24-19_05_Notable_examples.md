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
Có hai thư viện phần mềm nổi tiếng được xây dựng dựa trên phương pháp Newton proximal:

* **glmnet** (Friedman et al., 2009): Cài đặt Newton proximal cho các mô hình tuyến tính tổng quát (generalized linear models) có phạt $$\ell_1$$, với bài toán con bên trong giải bằng hạ theo tọa độ (coordinate descent).

* **QUIC** (Hsieh et al., 2011): Cài đặt Newton proximal cho bài toán graphical lasso, kết hợp kỹ thuật phân rã ma trận và giải bài toán con bên trong bằng hạ theo tọa độ.

Cả hai thư viện đều được sử dụng rộng rãi và là chuẩn tham chiếu trong lĩnh vực ứng dụng tương ứng.

Phương pháp Newton proximal đánh giá gradient của $$g$$ ít lần hơn nhiều so với proximal gradient descent. Do đó, chi phí tính $$g$$ và $$\nabla g$$ càng lớn thì Newton proximal càng phát huy lợi thế, đặc biệt khi kết hợp với một bộ giải bên trong phù hợp.

## Ví dụ: hồi quy logistic lasso
Xét thí nghiệm thực nghiệm trong Lee et al. (2012) trên bài toán hồi quy logistic có điều chuẩn $$\ell_1$$, so sánh ba thuật toán:

1. **FISTA:** Proximal gradient tăng tốc.
2. **spaRSA:** Phương pháp gradient chiếu phổ (spectral projected gradient).
3. **PN:** Phương pháp Newton proximal.

#### Trường hợp Hessian dày đặc ($$n = 5000, p = 6000$$)
Bài toán đầu tiên có ma trận đặc trưng dày đặc $$X$$ với $$n = 5000$$ mẫu và $$p = 6000$$ đặc trưng. Do Hessian dày đặc, đây là trường hợp rất thách thức. Kết quả hiệu năng như sau:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example1.png" alt="[Hình 1] Hessian dày đặc X (n=5000, p=6000) [2]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Hessian dày đặc X (n=5000, p=6000) [2]</figcaption>
</p>
</figure>

Đồ thị bên phải đo hiệu năng theo số lần đánh giá hàm và đồ thị bên trái đo theo thời gian chạy. Xét theo số lần đánh giá hàm, PN vượt trội rõ rệt. Trong bài toán này, phần lớn thời gian nằm ở việc tính $$g$$ và $$\nabla g$$ (đặc biệt là các hàm $$\exp$$ và $$\log$$).

#### Trường hợp Hessian thưa ($$n = 542{,}000, p = 47{,}000$$)

Trong thí nghiệm thứ hai, ma trận đặc trưng $$X$$ thưa nên thời gian tính $$g$$ và $$\nabla g$$ giảm đáng kể:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Lasso_Example-sparse.png" alt="[Hình 2] Hessian thưa X (n=542,000, p=47,000) [2]" width="70%">
  <figcaption style="text-align: center;">[Hình 2] Hessian thưa X (n=542,000, p=47,000) [2]</figcaption>
</p>
</figure>

## Tính toán tử prox không chính xác
Trong phương pháp Newton proximal, toán tử prox có tỉ lệ nhìn chung không có nghiệm dạng đóng nên phải giải gần đúng bằng thuật toán lặp bên trong. Tuy vậy, ta vẫn muốn giữ được tốc độ hội tụ nhanh mà không lãng phí công tính toán ở các vòng ngoài đầu tiên.

Lee, Sun và Saunders (2014) đề xuất các quy tắc dừng cho bộ giải bên trong nhằm vẫn bảo đảm hội tụ toàn cục và tốc độ hội tụ siêu tuyến tính (hoặc bậc hai) cục bộ.

#### So sánh ba quy tắc dừng
Ba quy tắc dừng cho bài toán con bên trong được so sánh trên bài toán ước lượng graphical lasso với $$n = 72$$ mẫu và $$p = 1255$$ đặc trưng:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter19/09.05_Inexact_prox.png" alt="[Hình 3] Ba quy tắc dừng [2]" width="70%">
  <figcaption style="text-align: center;">[Hình 3] Ba quy tắc dừng [2]</figcaption>
</p>
</figure>

Ba quy tắc dừng gồm: `adaptive` (thích nghi), `maxiter = 10` (chạy tối đa 10 vòng lặp bên trong) và `exact` (giải đến độ chính xác rất cao).

Quy tắc `exact` thể hiện rõ tốc độ hội tụ bậc hai nhưng tốn nhiều thời gian cho mỗi bước ngoài. Với `maxiter = 10`, số vòng lặp bên trong không đủ để duy trì hội tụ bậc hai. Trong khi đó, quy tắc `adaptive` vừa giữ được hội tụ bậc hai vừa đạt thời gian chạy nhanh nhất trong ba phương án.

#### Quy tắc dừng trong phương pháp Newton cổ điển
Trong phương pháp Newton không chính xác cổ điển, bài toán con bên trong cực tiểu hóa mô hình bậc hai $$\tilde{g}_{k-1}$$ của $$g$$ tại $$x^{(k-1)}$$. Ta chọn một dãy cưỡng bức (forcing sequence) $$\eta_k \ (k = 1, 2, 3, \dots)$$ và dừng giải bài toán con khi:

> \begin{align}
\parallel \nabla \tilde{g}_{k-1}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  \nabla g(x^{(k-1)})  \parallel_2 \\\\
\end{align}

Điều kiện này yêu cầu chuẩn gradient của mô hình bậc hai tại điểm mới nhỏ hơn tối đa $$\eta_k$$ lần chuẩn gradient hiện tại, trong đó $$\tilde{g}_{k-1}(z) = \nabla g(x^{(k-1)})^T (z-x^{(k-1)}) + \frac{1}{2} (z - x^{(k-1)})^T \nabla^2 g(x^{(k-1)}) (z - x^{(k-1)})$$.

#### Quy tắc dừng trong phương pháp Newton proximal
Lee et al. (2012) mở rộng quy tắc trên cho trường hợp bài toán tổng hợp bằng cách thay gradient bằng ánh xạ gradient tổng quát:

> $$
> \begin{align}
\parallel G_{\tilde{f}_{k-1}/M}(x^{(k)}) \parallel_2 & \le \eta_k \parallel  G_{f/M}(x^{(k-1)})  \parallel_2
\end{align}
> $$

trong đó $$\tilde{f}_{k-1} = \tilde{g}_{k-1} + h$$ và $$mI \preceq \nabla^2 g \preceq MI$$.

Các tác giả chứng minh rằng nếu chọn dãy $$\eta_k$$ thỏa mãn điều kiện dưới đây, phương pháp Newton proximal không chính xác vẫn đạt tốc độ hội tụ siêu tuyến tính cục bộ:

> $$
> \begin{align}
> \eta_k \le \min \left\{ \frac{m}{2},  \frac{\parallel  G_{\tilde{f}_{k-2}/M}(x^{(k-1)}) - G_{f/M}(x^{(k-1)})  \parallel_2}{\parallel  G_{f/M}(x^{(k-2)})  \parallel_2} \right\}
> \end{align}
> $$

---
layout: post
title: '21-04 Ví dụ: Ước lượng không gian con thưa và phân rã thưa cộng hạng thấp'
chapter: '21'
order: 5
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

# Ví dụ: Ước lượng không gian con thưa và phân rã thưa cộng hạng thấp

## Ước lượng không gian con thưa

Cho $$S=X^{T}X, X\in \mathbb{R}^{n\times p}$$, xét bài toán tìm một phép chiếu cực tiểu hóa khoảng cách theo chuẩn Frobenius giữa $$X$$ gốc và $$X$$ sau khi chiếu:

>$$
>\begin{align}
>&\min_{P} &&||X-XP||^{2}_{F}\\\\
>&\text{subject to} &&\text{rank(P)=k where P is a projection matrix}
>\end{align}
>$$

Bài toán này không lồi vì tập các ma trận chiếu không phải là tập lồi. Tuy nhiên, nó được biết là tương đương với bài toán lồi sau [[VCLR13]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]. Đây cũng được gọi là bài toán ước lượng không gian con.

>$$
>\begin{align}
>&\max_{Y} &&tr(SY)\\\\
>&\text{subject to } &&Y\in F_{k} = \left\{Y\in \mathbb{S}^{p} : 0 \preceq Y \preceq I, tr(Y) = k \right\}
>\end{align}
>$$

[VCLR13] bàn về việc giải phiên bản thưa (thêm chuẩn L1) của bài toán ước lượng không gian con. Để biết chi tiết suy diễn, hãy xem bài báo tương ứng.
>$$
>\begin{align}
>&\max_{Y} &&tr(SY)-\lambda ||Y||_{1}\\\\
>&\text{subject to } &&Y\in F_{k} 
>\end{align}
>$$

trong đó $$F_{k}$$ là Fantope bậc k, như định nghĩa ở phương trình trên.

Khi $$\lambda = 0$$, bài toán trên tương đương với PCA chuẩn.

Bài toán này có dạng SDP và có thể giải bằng các phương pháp điểm trong. Tuy nhiên, cách tiếp cận này phức tạp để cài đặt và trở nên rất chậm khi kích thước bài toán tăng.

## Công thức hóa ADMM

Để giải bài toán này bằng ADMM, ta viết lại như sau:
>$$
>\begin{align}
>&\min_{Y,Z} &&-tr(SY)+I_{F_{k}}(Y) + \lambda||Z||_{1}\\\\
>&\text{subject to } &&Y = Z.
>\end{align}
>$$

## Thuật toán ADMM

Tóm tắt bài toán, các bước ADMM như sau:
 >$$
 >\begin{align}
 >Y^{+} &=  \underset{Y}{\operatorname{argmin}} -tr(SY) + I_{F_{k}}(Y)+\frac{\rho}{2}||Y-Z+W||^{2}_{F}\\\\
 >&=\underset{Y\in F_{k}}{\operatorname{argmin}} \frac{1}{2}||Y-Z+W-\frac{S}{\rho}||^{2}_{F}\\\\
 >&=P_{F_{k}}(Z-W+\frac{S}{\rho})\\\\
 >Z^{+} & = \underset{Z}{\operatorname{argmin}}\lambda||Z||_{1}+\frac{\rho}{2}||Y^{+}-Z+W||^{2}_{F}\\\\
 >&=S_{\frac{\lambda}{\rho}}(Y^{+}+W)\\\\
 >W^{+} &=W+Y^{+}-Z^{+}.
 >\end{align}
 >$$
 
trong đó $$P_{F_{k}}$$ là toán tử chiếu lên fantope. Nó được định nghĩa bằng cách cắt (clipping) các giá trị riêng trong phân rã trị riêng $$A= U\Sigma U^{T}, \Sigma = diag(\sigma_{1},...\sigma_{p})$$ [[VCLR13]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]:
>$$
>\begin{align}
>P_{F_{k}}(A) = U\Sigma_{\theta}U^{T}, \: \Sigma_{\theta} = diag(\sigma_{1}(\theta),...\sigma_{p}(\theta))
>\end{align}
>$$

trong đó mỗi $$\sigma_{i}(\theta) = \min\left\{\max\left\{\sigma_{i}-\theta,0\right\},1\right\}$$ và $$\sum^{p}_{i=1}\sigma_{i}(\theta)=k$$.

## Phân rã thưa cộng hạng thấp
Cho $$M\in \mathbb{R}^{n\times m}$$, bài toán phân rã thưa cộng hạng thấp như sau [[CLMW09]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]:
>$$
>\begin{align}
>&\min_{L,S} &&||L||_{tr}+\lambda||S||_{1}\\\\
>&\text{subject to } &&L+S=M
>\end{align}
>$$

## Mô tả bài toán

Mục tiêu của bài toán này là phân rã ma trận quan sát $$M$$ thành một ma trận hạng thấp $$L$$ và một ma trận thưa $$S$$. Số hạng đầu của hàm mục tiêu là phạt vết (trace) của $$L$$, tức cực tiểu hóa tổng các giá trị kỳ dị của $$L$$. Số hạng thứ hai dùng chuẩn $$l_{1}$$ trên ma trận $$S$$ để tạo tính thưa cho $$S$$. $$\lambda$$ là tham số điều chỉnh cân bằng hai số hạng này. Cả chuẩn vết lẫn chuẩn $$l_{1}$$ đều không trơn, và nói chung chuẩn vết được biết là khó tối ưu. Giống bài toán ước lượng không gian con thưa, bài toán này có dạng SDP và có thể giải bằng các phương pháp điểm trong, nhưng cách này cũng phức tạp và chậm. Với bài toán này, ADMM cho các bước cập nhật dễ hơn phần nào.

>$$
>\begin{align}
>L^{+} &= S^{tr}_{\frac{1}{\rho}}(M-S+W)\\\\
>S^{+} &= S^{l_{1}}_{\frac{\lambda}{\rho}}(M-L^{+}+W)\\\\
>W^{+} &= W+M-L^{+}-S^{+}
>\end{align}
>$$

trong đó $$S^{tr}_{\frac{1}{\rho}}$$ là soft-thresholding ma trận (trên các giá trị kỳ dị) và $$S^{l_{1}}_{\frac{\lambda}{\rho}}$$ là soft-thresholding theo từng phần tử.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/candes.png" alt="[Hình 1] Ví dụ phân rã thưa cộng hạng thấp trên video camera giám sát [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Ví dụ phân rã thưa cộng hạng thấp trên video camera giám sát [3]</figcaption>
</p>
</figure>

## Ví dụ ứng dụng

[Hình 1] cho thấy ví dụ áp dụng phân rã thưa cộng hạng thấp vào phân tích video camera giám sát. Từ các camera giám sát quay một vùng cố định trong thời gian dài, ta dễ dàng tách phần hạng thấp chứa phần chung của hầu hết các khung hình, còn phần thưa trích ra các phần đặc trưng ở các khung hình cụ thể. Ví dụ, ở [Hình 1], cột giữa biểu diễn phần hạng thấp và cột phải biểu diễn phần thưa. Như có thể kiểm chứng, phần hạng thấp chứa thông tin nền xuất hiện trong gần như mọi khung hình, còn phần thưa chỉ chứa các phần đặc trưng chỉ xuất hiện ở một số khung hình cụ thể.

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

Hãy tưởng tượng một camera an ninh quay cố định một hành lang suốt nhiều giờ: phần nền (tường, sàn, cửa) gần như đứng yên nên tạo thành một **ma trận hạng thấp (low-rank)** $$L$$, còn người đi lại chỉ chiếm một phần nhỏ khung hình nên tạo thành một **ma trận thưa (sparse)** $$S$$. Làm thế nào tách khung hình quan sát $$M = L + S$$ thành đúng phần nền $$L$$ và phần người di chuyển $$S$$? Bài 21-04 giới thiệu hai bài toán ma trận kinh điển — **Ước lượng không gian con thưa (Sparse PCA / Fantope)** và **Phân rã thưa cộng hạng thấp (Robust PCA)** — nơi ADMM tỏa sáng bằng cách ghép hai toán tử proximal ma trận cực kỳ thanh lịch: ngưỡng mềm phần tử và **ngưỡng giá trị kỳ dị (Singular Value Thresholding)**!

## Bản đồ kiến thức nền: Bốn trụ cột của tối ưu hóa ma trận bằng ADMM

Để đọc hiểu dễ dàng các ký hiệu không gian ma trận $$\mathbb{S}^p, \mathcal{F}_k, \|L\|_*$$ trong bài này, hãy nắm rõ bốn khái niệm nền:

- **Nới lỏng lồi Fantope $$\mathcal{F}_k$$ cho không gian con hạng $$k$$:** Tập các ma trận chiếu hạng $$k$$ không lồi. Bao lồi của nó là tập Fantope $$\mathcal{F}_k = \{Y \in \mathbb{S}^p : 0 \preceq Y \preceq I, \; \operatorname{tr}(Y) = k\}$$ — cho phép viết bài toán Sparse PCA dưới dạng bài toán tối ưu lồi giải được bằng ADMM!
- **Chuẩn hạt nhân $$\|L\|_* = \sum_i \sigma_i(L)$$ làm đại diện lồi cho hạng ma trận:** Hệt như chuẩn $$\ell_1$$ là bao lồi chặt nhất của số phần tử khác không ($$\|x\|_0$$) cho vector, chuẩn hạt nhân (tổng các giá trị kỳ dị) là bao lồi chặt nhất của $$\operatorname{rank}(L)$$ trên hình cầu đơn vị phổ!
- **Ngưỡng giá trị kỳ dị (SVT) là toán tử proximal của chuẩn hạt nhân:** Với phân rã SVD $$A = U\Sigma V^T$$, ta có $$\operatorname{prox}_{\tau\|\cdot\|_*}(A) = U \operatorname{diag}((\sigma_i - \tau)_+) V^T$$ — chỉ cần co các giá trị kỳ dị bằng ngưỡng mềm rồi nhân ghép lại!
- **Phân rã 3 khối thành 2 khối trong Robust PCA:** Bài toán $$\min \|L\|_* + \lambda\|S\|_1 \text{ s.t. } L + S = M$$ khớp hoàn hảo với khung ADMM hai khối ($$A = I, B = I, c = M$$): bước $$L$$ gọi SVT, bước $$S$$ gọi ngưỡng mềm phần tử, cực kỳ gọn gàng!

### Khung giải thích (nên đọc chậm): Chạy tay 1 bước SVT + Ngưỡng mềm phân rã ma trận $$2 \times 2$$

Xét ma trận quan sát đường chéo $$M = \begin{bmatrix} 5 & 0 \\ 0 & 1.5 \end{bmatrix}$$ (giả sử ta muốn tách $$M = L + S$$ với $$L$$ hạng thấp và $$S$$ thưa), tham số phạt $$\lambda = 1$$, $$\rho = 0.5$$ (nên ngưỡng SVT cho $$L$$ là $$\tau_L = 1/\rho = 2$$ và ngưỡng mềm cho $$S$$ là $$\tau_S = \lambda/\rho = 2$$). Khởi tạo $$S^{(0)} = 0, W^{(0)} = 0$$:

1. **Bước 1 — Cập nhật thành phần hạng thấp $$L^{(1)} = \operatorname{SVT}_{2}(M - S^{(0)} - W^{(0)})$$: **
   - Các giá trị kỳ dị của $$M$$ là $$\sigma_1 = 5$$ và $$\sigma_2 = 1.5$$.
   - Áp dụng ngưỡng mềm với $$\tau_L = 2$$:
     $$\sigma_1^+ = (5 - 2)_+ = 3, \qquad \sigma_2^+ = (1.5 - 2)_+ = 0.$$
   - Thu được $$L^{(1)} = \begin{bmatrix} 3 & 0 \\ 0 & 0 \end{bmatrix}$$ — **hạng ma trận lập tức giảm từ 2 xuống 1!**
2. **Bước 2 — Cập nhật thành phần thưa $$S^{(1)} = S_{2}(M - L^{(1)} - W^{(0)})$$:**
   - Phần dư còn lại: $$M - L^{(1)} = \begin{bmatrix} 2 & 0 \\ 0 & 1.5 \end{bmatrix}$$.
   - Áp dụng ngưỡng mềm từng phần tử với $$\tau_S = 2$$: $$S^{(1)} = \begin{bmatrix} (2-2)_+ & 0 \\ 0 & (1.5-2)_+ \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$ (nếu chọn $$\lambda = 0.5$$ thì $$\tau_S = 1$$ cho $$S^{(1)} = \operatorname{diag}(1, 0.5)$$).
3. **Bước 3 — Cập nhật biến đối ngẫu:** $$W^{(1)} = W^{(0)} + L^{(1)} + S^{(1)} - M$$, đẩy phần còn lại sang vòng sau để $$L^{(k)} + S^{(k)}$$ hội tụ chính xác về $$M$$!

---

# Ví dụ: Ước lượng không gian con thưa và phân rã thưa cộng hạng thấp

## Ước lượng không gian con thưa

Cho $$S=X^{T}X$$ với $$X\in \mathbb{R}^{n\times p}$$, xét bài toán tìm ma trận chiếu $$P$$ cực tiểu hóa khoảng cách theo chuẩn Frobenius giữa ma trận dữ liệu gốc $$X$$ và ảnh chiếu $$XP$$:

>$$
>\begin{align}
>&\min_{P} &&||X-XP||^{2}_{F}\\\\
>&\text{subject to} &&\text{rank(P)=k where P is a projection matrix}
>\end{align}
>$$

Bài toán này không lồi vì tập các ma trận chiếu hạng $$k$$ không phải là tập lồi. Tuy nhiên, nó tương đương với bài toán lồi sau [[VCLR13]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})], thường gọi là bài toán ước lượng không gian con:

>$$
>\begin{align}
>&\max_{Y} &&tr(SY)\\\\
>&\text{subject to } &&Y\in F_{k} = \left\{Y\in \mathbb{S}^{p} : 0 \preceq Y \preceq I, tr(Y) = k \right\}
>\end{align}
>$$

Tài liệu [VCLR13] nghiên cứu phiên bản thưa (bổ sung số hạng phạt chuẩn $$l_1$$) của bài toán ước lượng không gian con; chi tiết suy diễn có thể xem trong bài báo gốc:
>$$
>\begin{align}
>&\max_{Y} &&tr(SY)-\lambda ||Y||_{1}\\\\
>&\text{subject to } &&Y\in F_{k} 
>\end{align}
>$$

trong đó $$F_{k}$$ là tập Fantope bậc $$k$$ như đã định nghĩa ở trên.

Khi $$\lambda = 0$$, bài toán trên quy về PCA chuẩn.

Bài toán này thuộc lớp quy hoạch nửa xác định (SDP) nên có thể giải bằng các phương pháp điểm trong, nhưng cách tiếp cận đó khá phức tạp khi cài đặt và chạy rất chậm khi kích thước bài toán lớn.

## Công thức hóa ADMM

Để áp dụng ADMM, ta viết lại bài toán dưới dạng tách biến:
>$$
>\begin{align}
>&\min_{Y,Z} &&-tr(SY)+I_{F_{k}}(Y) + \lambda||Z||_{1}\\\\
>&\text{subject to } &&Y = Z.
>\end{align}
>$$

## Thuật toán ADMM

Các bước cập nhật ADMM thu được như sau:
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

trong đó $$P_{F_{k}}$$ là toán tử chiếu lên tập Fantope, được định nghĩa bằng cách cắt ngưỡng (clipping) các trị riêng trong phân rã trị riêng $$A= U\Sigma U^{T}, \Sigma = diag(\sigma_{1},\ldots,\sigma_{p})$$ [[VCLR13]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]:
>$$
>\begin{align}
>P_{F_{k}}(A) = U\Sigma_{\theta}U^{T}, \: \Sigma_{\theta} = diag(\sigma_{1}(\theta),\ldots,\sigma_{p}(\theta))
>\end{align}
>$$

với mỗi $$\sigma_{i}(\theta) = \min\left\{\max\left\{\sigma_{i}-\theta,0\right\},1\right\}$$ và $$\theta$$ được chọn sao cho $$\sum^{p}_{i=1}\sigma_{i}(\theta)=k$$.

## Phân rã thưa cộng hạng thấp

Cho ma trận $$M\in \mathbb{R}^{n\times m}$$, bài toán phân rã thưa cộng hạng thấp được phát biểu như sau [[CLMW09]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]:
>$$
>\begin{align}
>&\min_{L,S} &&||L||_{tr}+\lambda||S||_{1}\\\\
>&\text{subject to } &&L+S=M
>\end{align}
>$$

## Mô tả bài toán

Mục tiêu là phân rã ma trận quan sát $$M$$ thành tổng của một ma trận hạng thấp $$L$$ và một ma trận thưa $$S$$. Số hạng thứ nhất phạt chuẩn vết (trace norm / chuẩn hạt nhân) của $$L$$, tức tổng các giá trị kỳ dị của $$L$$; số hạng thứ hai dùng chuẩn $$l_{1}$$ lên ma trận $$S$$ để khuyến khích tính thưa, còn $$\lambda$$ là tham số cân bằng hai thành phần. Cả chuẩn vết lẫn chuẩn $$l_{1}$$ đều không trơn, và chuẩn vết nói chung khá tốn kém khi tối ưu. Tương tự bài toán ước lượng không gian con thưa, bài toán này có thể đưa về SDP để giải bằng phương pháp điểm trong nhưng khá nặng nề và chậm. Với ADMM, các bước cập nhật trở nên gọn hơn đáng kể:

>$$
>\begin{align}
>L^{+} &= S^{tr}_{\frac{1}{\rho}}(M-S+W)\\\\
>S^{+} &= S^{l_{1}}_{\frac{\lambda}{\rho}}(M-L^{+}+W)\\\\
>W^{+} &= W+M-L^{+}-S^{+}
>\end{align}
>$$

trong đó $$S^{tr}_{\frac{1}{\rho}}$$ là toán tử co ngưỡng mềm theo ma trận (tác động lên các giá trị kỳ dị) và $$S^{l_{1}}_{\frac{\lambda}{\rho}}$$ là co ngưỡng mềm theo từng phần tử.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/candes.png" alt="[Hình 1] Ví dụ phân rã thưa cộng hạng thấp trên video camera giám sát [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Ví dụ phân rã thưa cộng hạng thấp trên video camera giám sát [3]</figcaption>
</p>
</figure>

## Ví dụ ứng dụng

[Hình 1] minh họa ứng dụng của phân rã thưa cộng hạng thấp trong phân tích video từ camera giám sát. Khi camera quay một khu vực cố định trong thời gian dài, thành phần hạng thấp sẽ nắm bắt phần nền chung xuất hiện ở hầu hết các khung hình, trong khi thành phần thưa tách riêng các vật thể chuyển động hoặc chi tiết chỉ xuất hiện cục bộ ở một số khung hình. Trong [Hình 1], cột giữa tương ứng với thành phần hạng thấp (phông nền tĩnh) và cột phải tương ứng với thành phần thưa (các đối tượng chuyển động).

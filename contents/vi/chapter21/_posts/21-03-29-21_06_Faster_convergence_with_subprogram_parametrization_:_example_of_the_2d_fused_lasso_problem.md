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

Một sai lầm phổ biến của người mới dùng ADMM là nghĩ rằng với mỗi bài toán chỉ có *một* cách tách biến duy nhất. Bài 21-06 sẽ thay đổi hoàn toàn tư duy đó bằng một ví dụ ngoạn mục: **Fused Lasso 2D** (khử nhiễu ảnh bằng biến phân toàn phần Total Variation 2D). Nếu tách biến theo kiểu cơ bản $$D\beta = z$$, ta phải giải một hệ phương trình tuyến tính 2D lớn ở mỗi vòng lặp và hai khối biến bị tương quan mạnh nên hội tụ khá chậm. Nhưng chỉ cần khéo léo tách bài toán 2D thành **hai bộ chuỗi 1D trực giao (hàng ngang và cột dọc)**, mỗi bài toán con lập tức giải chính xác trong thời gian tuyến tính $$O(n)$$ và tốc độ hội tụ tăng vọt!

## Kiến thức cần nhớ: Ba nguyên lý thiết kế tham số hóa bài toán con cho ADMM

Để biết cách "chế tạo" một phiên bản ADMM chạy nhanh gấp nhiều lần phiên bản sách giáo khoa, hãy ghi nhớ ba nguyên lý sau:

- **Tách theo hướng ít tương quan (De-correlated Splitting):** Tương tự hạ tọa độ theo khối (block coordinate descent), ADMM hội tụ nhanh nhất khi các khối biến cập nhật theo những phương hình học gần trực giao nhau (như chiều ngang vs. chiều dọc trên lưới ảnh 2D).
- **Khai thác bộ giải bài toán con tuyến tính $$O(n)$$:** Bài toán Fused Lasso 1D (khử nhiễu trên một đường thẳng $$m$$ điểm) có thuật toán quy hoạch động giải **chính xác tuyệt đối** trong thời gian $$O(m)$$ (thuật toán Johnson 2013 / Condat 2013). Do đó, tách lưới 2D thành các chuỗi 1D theo hàng và theo cột cho phép giải song song toàn bộ các hàng rồi toàn bộ các cột mà không cần giải hệ tuyến tính lớn!
- **Cân bằng giữa chi phí mỗi vòng và số vòng lặp:** Một cách tách biến tốt có thể hơi phức tạp hơn về công thức toán tử proximal, nhưng nếu nó gom được nhiều cấu trúc của bài toán vào mỗi khối (giảm độ lỏng của ràng buộc phụ), tổng thời gian chạy sẽ giảm đi theo cấp số nhân.

### Giải thích: So sánh trực tiếp độ phức tạp hai cách tách ADMM cho ảnh $$100 \times 100$$

Xét bài toán khử nhiễu ảnh Fused Lasso 2D trên một bức ảnh nhỏ $$100 \times 100$$ điểm ảnh (tổng cộng $$n = 10{,}000$$ biến $$\beta_{i,j}$$, với $$19{,}800$$ cặp cạnh kề ngang–dọc):

1. **Cách tách chuẩn ($$D\beta = z$$, trong đó $$D$$ là ma trận sai phân 2D):**
   - **Bước $$\beta$$:** Phải giải hệ tuyến tính $$(I + \rho D^T D)\beta = y + \rho D^T(z - w)$$ kích thước $$10{,}000 \times 10{,}000$$ (ma trận Laplace 2D có băng rộng $$100$$). Nếu dùng phân tích Cholesky dải, chi phí cỡ $$O(n \cdot 100^2) \approx 10^8$$ phép toán để khởi tạo và $$O(n \cdot 100) \approx 10^6$$ phép toán mỗi vòng.
   - **Bước $$z$$:** Ngưỡng mềm từng cạnh $$O(n)$$, nhưng vì toàn bộ liên kết lưới bị đẩy sang biến $$z$$, thông tin lan truyền chậm qua từng cạnh đơn lẻ nên cần nhiều vòng lặp.
2. **Cách tách trực giao Hàng – Cột ($$\beta = z_1 = z_2$$ với phạt ngang trong $$z_1$$ và phạt dọc trong $$z_2$$):**
   - **Bước $$z_1$$ (phạt theo hàng):** Tách thành **100 bài toán Fused Lasso 1D độc lập** dài 100 điểm, mỗi bài giải chính xác trong $$O(100)$$ phép toán $$\implies$$ tổng chỉ $$O(n) \approx 10^4$$ phép toán và chạy song song được trên 100 luồng!
   - **Bước $$z_2$$ (phạt theo cột):** Tách thành **100 bài toán Fused Lasso 1D độc lập** theo cột, tổng cũng chỉ $$O(n) \approx 10^4$$ phép toán!
   - Nhờ mỗi bước đã tối ưu chính xác trọn vẹn cả một hàng hoặc cả một cột, thông tin lan truyền xuyên toàn bộ bức ảnh chỉ sau vài vòng lặp!

---

# Hội tụ nhanh hơn nhờ tham số hóa bài toán con

## Giới thiệu

Một tính chất đáng chú ý của ADMM là tốc độ hội tụ có thể cải thiện đáng kể nếu ta tham số hóa các bài toán con một cách phù hợp. Trong ví dụ ADMM đồng thuận trước đó, thuật toán tối ưu lần lượt theo từng khối biến, khá tương đồng với phương pháp hạ tọa độ theo khối (block coordinate descent). Nhờ vậy, khi thiết kế các khối biến cập nhật theo những hướng gần như trực giao hoặc ít tương quan với nhau, ADMM có thể hội tụ nhanh hơn nhiều so với cách tách biến tiêu chuẩn.

## Ví dụ fused lasso 2D

Phần này minh họa ý tưởng trên bằng cách thiết kế các ràng buộc phụ sao cho các bước cập nhật biến gốc đi theo những hướng không tương quan (de-correlated). Chi tiết nghiên cứu có thể xem trong [RT16], [WSK14], [BS14].

Xét bài toán fused lasso 2D (hay khử nhiễu biến phân toàn phần 2D — 2D total variation denoising) đã giới thiệu ở [Chương 1]({% multilang_post_url contents/chapter01/21-01-07-01_01_optimization_problems %}). Cho một ảnh quan sát $$Y\in \mathbb{R}^{d\times d}$$, bài toán được phát biểu như sau:

>$$
>\begin{align}
>\min_{\Theta}\frac{1}{2}||Y-\Theta||^{2}_{F}+\lambda \sum_{i,j}(|\Theta_{i,j}-\Theta_{i+1,j}|+|\Theta_{i,j}-\Theta_{i,j+1}|).
>\end{align}
>$$

Ở đây mỗi điểm ảnh ứng với một tham số trong ma trận $$\Theta\in \mathbb{R}^{d\times d}$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/2dfussed.png" alt="[Hình 1] Diễn giải số hạng phạt trong fused lasso 2D [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 1] Diễn giải số hạng phạt trong fused lasso 2D [3]</figcaption>
</p>
</figure>

[Hình 1] minh họa trực quan số hạng phạt thứ hai trong hàm mục tiêu. Số hạng này phạt độ chênh lệch giữa mỗi điểm ảnh với các điểm ảnh kề nó theo cả phương ngang và phương dọc, nhờ đó khuyến khích các điểm ảnh lân cận nhận giá trị tương đồng nhau.

## Dạng vector

Viết gọn số hạng phạt bằng một toán tử tuyến tính, bài toán có dạng:
>$$
>\begin{align}
>\min_{\theta}\frac{1}{2}||y-\theta||^{2}_{2} + \lambda||D\theta||_{1}.
>\end{align}
>$$

trong đó $$D\in \mathbb{R}^{m\times n}$$ là ma trận toán tử sai phân 2D tương ứng với phương trình gốc.

## Các dạng cập nhật ADMM cho bài toán fused lasso 2D

Ta xây dựng hai biến thể ADMM khác nhau thông qua hai cách đặt ràng buộc phụ.

Cách thứ nhất xuất phát từ dạng vector với toán tử sai phân 2D:

>$$
>\begin{align}
>\min_{\theta, z}\frac{1}{2}||y-\theta||^{2}_{2}+\lambda||z||_{1} \qquad \text{subject to   }z = D\theta,
>\end{align}
>$$

Các bước cập nhật ADMM tương ứng là:
>$$
>\begin{align}
>\theta^{(k)} &= (I+\rho D^{T}D)^{-1}(y+\rho D^{T}(z^{(k-1)}+w^{(k-1)}))\\\\
>z^{(k)} &= S_{\frac{\lambda}{\rho}}(D\theta^{(k)}-w^{(k-1)})\\\\
>w^{(k)} &= w^{(k-1)}+z^{(k)}-D\theta ^{(k)}.
>\end{align}
>$$

## Độ phức tạp tính toán — dạng vector

Bước cập nhật $$\theta$$ đòi hỏi giải hệ phương trình tuyến tính với ma trận hệ số $$(I+\rho D^{T}D)$$. Vì $$L=D^{T}D$$ là ma trận Laplace của lưới 2D, hệ này có thể giải với chi phí $$O(n)$$ phép tính (hoặc gần tuyến tính tùy bộ giải lưới). Bước cập nhật $$z$$ chỉ áp dụng toán tử co ngưỡng mềm $$S_{t}$$ nên cũng tốn $$O(n)$$ phép tính. Như vậy, mỗi vòng lặp của ADMM dạng vector có độ phức tạp $$O(n)$$.

## ADMM dạng ma trận

Cách thứ hai giữ nguyên cấu trúc ma trận của bài toán gốc và tách thành phần sai phân dọc cho $$\Theta$$, sai phân ngang cho $$Z$$:
>$$
>\begin{align}
>&\min_{\Theta, Z} &&\frac{1}{2}||Y-\Theta||^{2}_{F}+\lambda\sum_{i,j}(|\Theta_{i,j}-\Theta_{i+1,j}|+|Z_{i,j}-Z_{i,j+1}|)\\\\
>&\text{subject to } &&\Theta = Z
>\end{align}
>$$

Các bước cập nhật ADMM thu được như sau:
>$$
>\begin{align}
>\Theta_{\cdot \\ , j}^{(k)} &= FL^{1d}_{ \frac{\lambda}{(1+\rho)} } \bigg( \frac{ Y_{\cdot \\ , j}+\rho( Z^{(k-1)}_{\cdot \\ , j}-W_{\cdot \\ ,j}^{(k-1)} ) } {1+\rho} \bigg),\qquad j=1,...,d\\\\
>Z_{i, \cdot}^{(k)} &= FL^{1d}_{\frac{\lambda}{\rho}} \bigg(\Theta_{i, \cdot}^{(k)} + W_{i, \cdot}^{(k-1)} \bigg), \qquad i=1,...,d\\\\
>W^{(k)} &= W^{(k-1)} + \Theta^{(k)} - Z^{(k)} \\\\
>\end{align}
>$$
trong đó $$FL_{\tau}^{1d}(a)$$ là bài toán fused lasso 1D, định nghĩa là $$FL_{\tau}^{1d}(a) = \underset{x}{\operatorname{argmin}}\frac{1}{2}||a-x||^{2}_{2}+\tau\sum_{i=1}^{d-1}|x_{i}-x_{i+1}|$$.

## Độ phức tạp tính toán — dạng ma trận

ADMM dạng ma trận cũng đạt độ phức tạp $$O(n)$$ cho mỗi vòng lặp, vì cả hai bước cập nhật $$\Theta$$ (theo từng cột) và $$Z$$ (theo từng hàng) đều quy về các bài toán fused lasso 1D, vốn có thuật toán giải trong thời gian tuyến tính theo số phần tử.

[Hình 2] minh họa cách số hạng phạt ban đầu được tách thành các bài toán con fused lasso 1D theo cột và theo hàng.
 
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/2dfussedlasso.png" alt="[Hình 2] Diễn giải các cập nhật ADMM dạng ma trận cho fused lasso 2D [3]" width="70%">
  <figcaption style="text-align: center;">[Hình 2] Diễn giải các cập nhật ADMM dạng ma trận cho fused lasso 2D [3]</figcaption>
</p>
</figure>


## Thí nghiệm khử nhiễu ảnh

Quay lại bài toán khử nhiễu ảnh ở Chương 1, [Hình 3] trình bày ảnh đầu vào và nghiệm chính xác sau khi khử nhiễu. [Hình 4] so sánh tốc độ hội tụ của hai biến thể ADMM: biến thể ADMM "chuyên biệt" dạng ma trận (tách ràng buộc theo phương dọc và phương ngang) hội tụ nhanh hơn rõ rệt so với "ADMM chuẩn" dạng vector.

[Hình 5] minh họa chất lượng ảnh tái tạo sau các mốc vòng lặp ADMM khác nhau.

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

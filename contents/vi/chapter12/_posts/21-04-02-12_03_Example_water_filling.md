---
layout: post
title: 12-03 Ví dụ thuật toán water-filling
chapter: '12'
order: 4
owner: Wontak Ryu
categories:
- chapter12
lang: vi
---

Giả sử bạn là kỹ sư viễn thông thiết kế bộ phát Wi-Fi / 5G dùng kỹ thuật ghép kênh phân chia tần số trực giao (OFDM). Bạn có tổng công suất phát cố định là $$1$$ đơn vị để chia cho $$n$$ kênh tần số song song, mỗi kênh có mức nhiễu nền $$\alpha_i > 0$$ khác nhau — kênh sạch thì $$\alpha_i$$ nhỏ, kênh nhiễu nặng thì $$\alpha_i$$ lớn. Theo định lý dung lượng kênh của Claude Shannon, tổng tốc độ truyền dữ liệu tỷ lệ với $$\sum_{i=1}^n \log(\alpha_i + x_i)$$. Câu hỏi là: **bạn nên dồn công suất vào kênh sạch hay cứu giúp kênh nhiễu?**

Khi đặt bút viết 4 điều kiện KKT cho bài toán lồi này, một bức tranh vật lý đẹp đến mức trở thành biểu tượng kinh điển của lý thuyết thông tin lập tức hiện ra: nghiệm tối ưu có dạng $$x_i^* = \max(0, w - \alpha_i)$$! Hãy tưởng tượng bạn xây một bể nước có đáy gồ ghề với độ cao từng bậc bằng mức nhiễu $$\alpha_i$$, rồi đổ đúng $$1$$ lít nước (tổng công suất) vào bể. Nước tự động dâng ngang đến một **mực nước chung $$w = 1/\nu^*$$**: những kênh sạch (đáy thấp $$\alpha_i < w$$) nhận nhiều công suất nhất, còn những kênh quá nhiễu (đáy cao hơn mực nước $$\alpha_i \ge w$$) bị **bỏ mặc hoàn toàn với $$x_i^* = 0$$**!

## Kiến thức cần nhớ: Bốn trụ cột của bài toán Đổ nước (Water-Filling)

- **Mô hình tối ưu lồi từ định lý Shannon:** Cực tiểu hóa $$-\sum_{i=1}^n \log(\alpha_i + x_i)$$ với ràng buộc $$x_i \ge 0$$ (không âm) và $$\sum_{i=1}^n x_i = 1$$ (ngân sách công suất). Vì $$-\log$$ lồi và mọi ràng buộc tuyến tính, KKT là điều kiện cần và đủ.
- **Khử nhân tử $$u_i$$ bằng điều kiện bù:** Từ điều kiện dừng $$-\frac{1}{\alpha_i + x_i^*} - u_i^* + \nu^* = 0$$, ta suy ra $$u_i^* = \nu^* - \frac{1}{\alpha_i + x_i^*} \ge 0$$. Kết hợp với điều kiện bù $$u_i^* x_i^* = 0$$ lập tức chia các kênh làm hai nhóm:
  - Kênh được cấp nguồn ($$x_i^* > 0$$): $$u_i^* = 0 \implies \alpha_i + x_i^* = \frac{1}{\nu^*} = w$$.
  - Kênh bị tắt ($$x_i^* = 0$$): $$u_i^* \ge 0 \implies \alpha_i \ge \frac{1}{\nu^*} = w$$.
- **Công thức nghiệm đóng theo mực nước $$w = 1/\nu^*$$:** Gộp hai nhánh lại ta được đúng một công thức duy nhất: $$x_i^* = \max(0, w - \alpha_i)$$, trong đó mực nước $$w$$ là nghiệm duy nhất của phương trình đơn điệu tăng từng khúc $$\sum_{i=1}^n \max(0, w - \alpha_i) = 1$$!
- **Thuật toán tìm mực nước $$O(n \log n)$$:** Chỉ cần sắp xếp $$\alpha_1 \le \alpha_2 \le \dots \le \alpha_n$$ tăng dần rồi thử dần số kênh hoạt động $$k = 1, 2, \dots, n$$ (hoặc dùng tìm kiếm nhị phân theo $$w$$) là tìm ra nghiệm chính xác tuyệt đối!

### Giải thích: Tính tay bài toán Water-Filling cho 3 kênh tần số

Cho 3 kênh với mức nhiễu nền $$\alpha_1 = 0.2$$ (rất sạch), $$\alpha_2 = 0.5$$ (trung bình), $$\alpha_3 = 1.5$$ (rất nhiễu), và tổng công suất $$\sum_{i=1}^3 x_i = 1.0$$.

1. **Thử giả thiết cả 3 kênh đều được cấp nguồn ($$k = 3$$):**
   $$(w - 0.2) + (w - 0.5) + (w - 1.5) = 1.0 \implies 3w = 3.2 \implies w \approx 1.067.$$
   Kiểm tra kênh 3: $$x_3 = w - 1.5 = 1.067 - 1.5 = -0.433 < 0$$ (vi phạm $$x_3 \ge 0$$!) $$\implies$$ kênh 3 quá nhiễu, chắc chắn $$x_3^* = 0$$!
2. **Thử giả thiết chỉ 2 kênh đầu hoạt động ($$k = 2$$):**
   $$(w - 0.2) + (w - 0.5) = 1.0 \implies 2w - 0.7 = 1.0 \implies w = 0.85.$$
   Kiểm tra cả 3 kênh với mực nước $$w = 0.85$$ (tức nhân tử đối ngẫu $$\nu^* = 1/0.85 \approx 1.176$$):
   - Kênh 1: $$x_1^* = \max(0, 0.85 - 0.2) = 0.65 > 0$$ ($$\alpha_1 + x_1^* = 0.85$$).
   - Kênh 2: $$x_2^* = \max(0, 0.85 - 0.5) = 0.35 > 0$$ ($$\alpha_2 + x_2^* = 0.85$$).
   - Kênh 3: $$x_3^* = \max(0, 0.85 - 1.5) = 0$$ (vì đáy $$\alpha_3 = 1.5 > 0.85$$ nằm cao hơn hẳn mặt nước!).
3. **Kiểm chứng tổng công suất và nhân tử $$u_3^*$$:**
   Tổng $$0.65 + 0.35 + 0 = 1.0$$ (chính xác!). Và $$u_3^* = \nu^* - \frac{1}{\alpha_3} = \frac{1}{0.85} - \frac{1}{1.5} \approx 0.510 > 0$$ thỏa mãn cả 4 điều kiện KKT!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Xét bài toán tối ưu hóa lồi sau:

>$$
>\begin{align}
>    &\min_{x} &&{- \sum_{i=1}^n \log(\alpha_i + x_i)} \\\\
>    &\text{với điều kiện} &&{x \succeq 0, 1^Tx = 1},\\\\
>&\text{trong đó } \alpha_i > 0.
>\end{align}
>$$

Bài toán này xuất hiện trong lý thuyết thông tin, gắn với việc phân bổ công suất cho $$n$$ kênh truyền thông. Biến $$x_i$$ biểu diễn công suất phát phân bổ cho kênh thứ $$i$$, còn $$\log(\alpha_i + x_i)$$ biểu diễn dung lượng hay tốc độ truyền của kênh đó. Như vậy, mục tiêu là phân bổ tổng công suất cố định vào các kênh sao cho tổng tốc độ truyền đạt cực đại [1].

Gọi $$\lambda^\star \in \mathbb{R}^n$$ và $$\nu^\star \in \mathbb{R}$$ lần lượt là các nhân tử Lagrange ứng với ràng buộc bất đẳng thức $$x^\star \succeq 0$$ và ràng buộc đẳng thức $$1^Tx^\star = 1$$. Các điều kiện KKT của bài toán là:

>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>\lambda^\star \succeq 0, \\\\
>\lambda_i^\star x_i^\star = 0, \text{    } i = 1, \dots, n, \\\\
> -1 / (\alpha_i + x_i^\star) - \lambda_i^\star + \nu^\star = 0,  \text{    } i= 1, \dots, n.
>\end{align}
> $$

Từ hệ điều kiện KKT trên, ta có thể tìm $$x^\star, \lambda^\star, \nu^\star$$ theo dạng giải tích. Trước hết, khử $$\lambda^\star$$ bằng cách coi nó như biến phụ không âm ($$\lambda_i^\star = \nu^\star - 1/(\alpha_i + x_i^\star) \ge 0$$):

>$$
>\begin{align}
>x^\star \succeq 0, \\\\
>1^Tx^\star = 1, \\\\
>x_i^\star(\nu^\star - 1 / (\alpha_i + x_i^\star)) = 0, \text{    } i = 1, \dots, n, \\\\
> \nu^\star \ge 1/(\alpha_i + x_i^\star),  \text{    } i= 1, \dots, n.
>\end{align}
> $$

Kết hợp điều kiện dừng và điều kiện bù yếu, ta thu được biểu thức nghiệm:

> $$
> x_i^\star = 
> \begin{cases}
> 1 / \nu^\star - \alpha_i &\nu^\star < 1/\alpha_i \ \\\\
> 0 &\nu^\star \ge 1/\alpha_i\\\\
> \end{cases}
> = \max\{0, 1/\nu^\star - \alpha_i \}, \quad i = 1, \dots, n.
> $$

Theo ràng buộc $$1^T x^\star = 1$$, tổng các thành phần $$x_i^\star$$ ($$i = 1, \dots, n$$) bằng $$1$$:

> $$
> \sum_{i=1}^n \max\{0, 1/\nu^\star - \alpha_i \} = 1.
> $$

Vế trái là một hàm tuyến tính từng khúc và tăng theo $$1/\nu^\star$$, nên với các giá trị $$\alpha_i$$ cố định, phương trình trên có nghiệm duy nhất cho $$1/\nu^\star$$.

Phương pháp giải này được gọi là **water-filling (đổ nước)**. Nếu xem $$\alpha_i$$ là độ cao đáy của ngăn thứ $$i$$, bài toán tương đương với việc đổ nước vào các ngăn cho đến khi mực nước chung đạt mức $$1/\nu^\star$$ và tổng lượng nước đổ vào bằng $$1$$, như minh họa trong hình dưới đây.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl}}/img/chapter_img/chapter12/water-fill.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Minh họa thuật toán water-filling [1]</figcaption>
</p>
</figure>

### KKT qua ví dụ đổ nước trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/kkt-water-filling_vi.mp4"></video>
</div>

Giải bài đổ nước với α = (0,1; 0,4; 0,8; 1,2) bằng bốn điều kiện KKT, đọc ý nghĩa của λ, và ba cách đoán sai bị KKT loại.

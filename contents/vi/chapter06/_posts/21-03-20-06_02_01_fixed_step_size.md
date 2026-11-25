---
layout: post
title: 06-02-01 Kích thước bước cố định
chapter: '06'
order: 6
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Chọn một con số $$t$$ cố định rồi chạy thẳng từ đầu đến cuối vòng lặp là cách tiếp cận giản dị nhất thế giới — không tốn thêm bất kỳ phép tính hàm mục tiêu nào để dò bước. Chính sự gọn nhẹ ấy khiến kích thước bước cố định (hoặc lịch giảm bước định sẵn) trở thành lựa chọn số một khi huấn luyện mạng nơ-ron trên hàng triệu mẫu dữ liệu, nơi đánh giá lại toàn bộ hàm mất mát cho line search là quá đắt đỏ.

Nhưng sự đơn giản đi kèm một lằn ranh sinh tử sắc như dao cạo: chỉ cần bước cố định vượt quá ngưỡng $$2/L$$ một chút thôi, thuật toán chuyển ngay từ hội tụ êm ả sang dao động bùng nổ! Bài học này làm rõ chính xác ba vùng hành vi của bước cố định: quá nhỏ, vừa đủ, và quá lớn.

## Kiến thức cần nhớ: Ba chế độ động lực của Bước cố định

Hiểu kích thước bước cố định qua ba trụ cột định lượng sau:

- **Vùng an toàn $$0 < t \le 1/L$$ (Đảm bảo giảm đơn điệu):** Khi $$f$$ có gradient $$L$$-Lipschitz, mọi bước $$t \le 1/L$$ đều bảo đảm $$f(x_{k+1}) \le f(x_k) - \frac{t}{2}\|\nabla f(x_k)\|_2^2$$ — hàm mục tiêu giảm nghiêm ngặt sau từng bước mà không bao giờ bật lên!
- **Vùng dao động nhưng vẫn hội tụ $$1/L < t < 2/L$$:** Trên hàm bậc hai $$L$$-trơn, bước đi vượt qua đáy theo phương dốc nhất nên quỹ đạo nhảy qua nhảy lại (overshoot), nhưng biên độ vẫn co dần vì $$|1 - tL| < 1$$.
- **Vùng phân kỳ $$t \ge 2/L$$:** Khi $$t = 2/L$$, thuật toán nhảy qua lại vô hạn giữa $$+x_0$$ và $$-x_0$$ mà không giảm thêm chút nào. Khi $$t > 2/L$$, biên độ nhân lên theo cấp số nhân $$|1 - tL|^k \to \infty$$!

### Giải thích: Quan sát chính xác 4 kịch bản bước cố định trên $$f(x) = 2x^2$$

Với $$f(x) = 2x^2$$, ta có $$f'(x) = 4x$$ và độ cong $$L = f''(x) = 4$$. Vậy $$1/L = 0.25$$ và ngưỡng tới hạn $$2/L = 0.5$$. Xuất phát từ $$x_0 = 1$$, quy tắc cập nhật là $$x_{k+1} = x_k - 4t x_k = (1 - 4t)x_k$$:

1. **$$t = 0.05$$ (quá nhỏ, $$t \ll 1/L$$):** $$x_k = (0.8)^k$$. Sau 3 bước: $$1 \to 0.8 \to 0.64 \to 0.512$$ (hội tụ đơn điệu nhưng chậm rề rề).
2. **$$t = 0.25$$ (lý tưởng, $$t = 1/L$$):** $$x_k = (0)^k$$. Sau 1 bước: $$1 \to 0$$ (chạm đáy tức thì!).
3. **$$t = 0.45$$ (vùng dao động, $$1/L < t < 2/L$$):** $$x_k = (-0.8)^k$$. Sau 3 bước: $$1 \to -0.8 \to 0.64 \to -0.512$$ (vượt đáy liên tục nhưng biên độ vẫn thu hẹp về $$0$$).
4. **$$t = 0.55$$ (quá lớn, $$t > 2/L$$):** $$x_k = (-1.2)^k$$. Sau 3 bước: $$1 \to -1.2 \to 1.44 \to -1.728 \to \dots$$ (bùng nổ ra vô cực!).
   **Bài học thực hành:** Trong thực tế không biết chính xác $$L$$, hãy bắt đầu với $$t$$ nhỏ theo thang log ($$10^{-4}, 10^{-3}, 10^{-2}, \dots$$) và theo dõi đường cong loss ngay trong 10 bước đầu!

---

Cách đơn giản nhất để chọn kích thước bước trong gradient descent là giữ nguyên một giá trị cố định cho mọi lần lặp: $$t_k = t$$ với $$k = 1, 2, 3, ...$$. Tuy nhiên, tốc độ và khả năng hội tụ của thuật toán phụ thuộc rất lớn vào việc lựa chọn $$t$$.

Ví dụ, hình dưới đây minh họa gradient descent áp dụng cho hàm $$f(x) = (10 x_1^2 + x_2^2) / 2$$ với ba kích thước bước khác nhau:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_02_01_gradientdescent4.png" alt="gradientdescent4" width="100%" height="100%">
  <figcaption style="text-align: center;">[Hình 1] Các trường hợp lựa chọn kích thước bước [3]</figcaption>
</p>
</figure>

* Trong trường hợp A, kích thước bước $$t$$ quá lớn, khiến thuật toán phân kỳ sau 8 bước và không thể tiến tới điểm cực tiểu.
* Trong trường hợp B, kích thước bước $$t$$ quá nhỏ, khiến tốc độ hội tụ rất chậm và chưa đạt được điểm cực tiểu ngay cả sau 100 bước.
* Trong trường hợp C, kích thước bước có độ lớn phù hợp, giúp thuật toán hội tụ trong khoảng 40 bước. (Cách xác định khoảng giá trị phù hợp này sẽ được phân tích ở các mục sau trong chương.)

### Kích thước bước: ổn định, quá lớn, quá nhỏ (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/gd-step-sizes_vi.mp4"></video>
</div>

Trên mặt hàm có đường đồng mức kéo dài, bước quá lớn gây dao động zig-zag hoặc phân kỳ, còn bước quá nhỏ khiến thuật toán tiến rất chậm. Backtracking line search và exact line search giúp tự động chọn kích thước bước phù hợp.

### Tự tay thử: kích thước bước

<div class="opx-explainer" data-opx="gd" data-lang="vi"></div>

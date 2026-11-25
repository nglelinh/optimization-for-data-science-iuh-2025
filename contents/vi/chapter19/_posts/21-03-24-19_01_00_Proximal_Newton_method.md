---
layout: post
title: '19-01 Phương pháp Newton proximal'
chapter: '19'
order: 2
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Nếu ví proximal gradient descent như việc đặt một cái bát hình tròn đều $$\frac{1}{2t}\|y - x\|_2^2$$ lên bề mặt hàm trơn $$g$$ để tìm đáy cục bộ, thì khi thung lũng của $$g$$ bị kéo dãn thành một khe hẹp hình elip, chiếc bát tròn buộc phải co thật nhỏ mới nằm gọn được bên trong — khiến bước đi trở nên li ti. Phương pháp Newton proximal thay chiếc bát tròn ấy bằng một **chiếc bát elip** khớp đúng với độ cong thực $$\nabla^2 g(x)$$ theo mọi phương, đồng thời giữ nguyên cấu trúc không trơn của $$h$$.

## Kiến thức cần nhớ: Ba viên gạch mở đường cho Newton proximal

Phần 19-01 dẫn dắt người học qua ba bước nâng cấp liên tiếp cực kỳ mạch lạc:

- **Ôn tập Proximal Gradient (19-01-01):** Nhận diện bài toán tổng hợp $$f = g + h$$ dưới góc nhìn cực tiểu hóa mô hình bậc hai đẳng hướng $$\hat{g}_t(y) + h(y)$$.
- **Thay độ cong vô hướng bằng Hessian thực (19-01-02):** Đổi $$\frac{1}{t}I$$ thành $$H = \nabla^2 g(x)$$ để định nghĩa hướng Newton proximal $$v^{(k)}$$ thông qua một bài toán con lồi bậc hai có điều chuẩn.
- **Chuẩn hóa bằng ánh xạ proximal có tỉ lệ (19-01-03):** Đóng gói toàn bộ phép cập nhật vào toán tử $$\operatorname{prox}_H(x - H^{-1}\nabla g(x))$$ và kiểm chứng hai tính chất nền tảng: tính duy nhất của nghiệm và tính không giãn trong chuẩn $$H$$.

### Giải thích: Hình tròn vs. Elip trong bài toán con 2 chiều

Xét hàm tổng hợp 2 chiều $$g(x_1, x_2) = \frac{1}{2}(x_1^2 + 10x_2^2) - x_1 - 10x_2$$ và $$h(x) = |x_1| + |x_2|$$. Độ cong dọc trục $$x_2$$ lớn gấp 10 lần trục $$x_1$$ ($$H = \operatorname{diag}(1, 10)$$, số điều kiện $$\kappa = 10$$). Tại điểm $$x = (2, 2)^T$$, ta có $$\nabla g(x) = (1, 10)^T$$:

1. **Với Proximal Gradient:** Để hội tụ ổn định, bước học phải thỏa mãn $$t \le \frac{1}{L} = \frac{1}{10} = 0.1$$.
   - Theo trục $$x_2$$: $$x_2^+ = S_{0.1}(2 - 0.1 \times 10) = S_{0.1}(1) = 0.9$$ (tiến sát nghiệm tối ưu $$x_2^\star = 0.9$$ ngay!).
   - Nhưng theo trục $$x_1$$: $$x_1^+ = S_{0.1}(2 - 0.1 \times 1) = S_{0.1}(1.9) = 1.8$$ (còn cách rất xa nghiệm tối ưu $$x_1^\star = 0$$!).
2. **Với Proximal Newton:** Ma trận $$H = \operatorname{diag}(1, 10)$$ tự động cấp bước $$1/1 = 1$$ cho trục $$x_1$$ và bước $$1/10 = 0.1$$ cho trục $$x_2$$:
   - $$x_1^+ = S_1(2 - 1 \times 1) = S_1(1) = 0 = x_1^\star$$.
   - $$x_2^+ = S_{0.1}(2 - 0.1 \times 10) = S_{0.1}(1) = 0.9 = x_2^\star$$.
   Cả hai tọa độ đều chạm đích chính xác ngay ở vòng lặp đầu tiên!

---

Trong phần này, chúng ta ôn lại **phương pháp hạ gradient lân cận (proximal gradient descent)** và xem **phương pháp Newton proximal** được mở rộng tự nhiên từ đó như thế nào.

Chúng ta cũng tìm hiểu định nghĩa của **phương pháp Newton proximal** và **ánh xạ proximal có tỉ lệ (scaled proximal map)** — toán tử kế thừa những tính chất quan trọng như tính duy nhất và tính không giãn (non-expansiveness) của ánh xạ proximal thông thường.

### Newton gần kề so với gradient gần kề (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/prox-newton_vi.mp4"></video>
</div>

Gradient gần kề chỉ dùng kích thước bước vô hướng; Newton gần kề cực tiểu hóa mô hình bậc hai sử dụng ma trận Hessian thực cộng thêm $$\lambda\|x\|_1$$, nhờ đó cần ít bước lặp hơn đáng kể.

### Tự tay thử: gradient gần kề so với Newton gần kề

<div class="opx-explainer" data-opx="pn" data-lang="vi"></div>

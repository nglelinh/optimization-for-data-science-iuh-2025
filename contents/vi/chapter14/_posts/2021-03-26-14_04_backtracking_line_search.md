---
layout: post
title: 14-04 Tìm kiếm đường backtracking
chapter: '14'
order: 10
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Như ta đã chứng kiến ở mục 14-02, phương pháp Newton thuần túy giống như một chiếc xe đua Công thức 1 không có phanh: trên đường thẳng gần đích nó đạt tốc độ không tưởng, nhưng chỉ cần vào cua khi còn xa đích là nó có thể lao thẳng ra khỏi đường đua và phân kỳ.

Giải pháp cực kỳ gọn gàng để biến "xe đua mất phanh" thành thuật toán hội tụ toàn cục chính là **tìm kiếm đường backtracking (backtracking line search)** — tạo nên **phương pháp Newton có giảm chấn (damped Newton method)**. Thay vì nhắm mắt nhảy luôn một bước đầy đủ $$t = 1$$, ta thử $$t = 1$$ trước; nếu hàm mục tiêu chưa giảm đủ sâu theo điều kiện Armijo, ta thu ngắn bước đi theo hệ số $$\beta \in (0, 1)$$ cho đến khi bước đi an toàn. Điểm tuyệt vời là khi đã vào gần nghiệm, bước $$t = 1$$ tự động thỏa mãn ngay từ lần thử đầu tiên nên tốc độ hội tụ bậc hai vẫn được bảo toàn nguyên vẹn!

## Bản đồ kiến thức nền: Cơ chế hoạt động của Newton có giảm chấn

- **Điều kiện giảm đủ Armijo cho Newton:** Với hướng Newton $$v = -(\nabla^2 f(x))^{-1}\nabla f(x)$$ và đạo hàm theo hướng $$\nabla f(x)^T v = -\lambda(x)^2$$, bước $$t$$ được chấp nhận khi:
  $$f(x + tv) \le f(x) - \alpha t \lambda(x)^2, \qquad \alpha \in (0, 0.5).$$
- **Tại sao luôn thử $$t = 1$$ đầu tiên:** Khác với Gradient Descent (nơi bước $$t = 1$$ thường quá lớn), bước Newton đã tự co giãn đúng tỷ lệ nhờ $$(\nabla^2 f)^{-1}$$. Thử $$t = 1$$ trước đảm bảo thuật toán tự động chuyển sang Newton thuần túy ngay khi vào pha hội tụ bậc hai.
- **Hai tham số $$\alpha$$ và $$\beta$$:** Trong thực hành, $$\alpha \in [0.01, 0.3]$$ (mức giảm tối thiểu yêu cầu so với đường tiếp tuyến) và $$\beta \in [0.1, 0.8]$$ (tỷ lệ thu bước mỗi lần thất bại, phổ biến nhất là $$\beta = 0.5$$).

### Khung giải thích (nên đọc chậm): Chạy tay một vòng backtracking trên hàm $$f(x) = \sqrt{1 + x^2}$$ để cứu bước Newton phân kỳ

Nhớ lại ở mục 14-02, với $$f(x) = \sqrt{1 + x^2}$$ tại điểm khởi tạo $$x = 1.2$$, bước Newton thuần túy nhảy sang $$-1.728$$ và **phân kỳ**! Giờ hãy lắp thêm backtracking với $$\alpha = 0.25$$ và $$\beta = 0.5$$:

1. **Tính giá trị tại $$x = 1.2$$:**
   - $$f(1.2) = \sqrt{1 + 1.44} = \sqrt{2.44} \approx 1.5620$$.
   - $$f'(1.2) = \frac{1.2}{1.5620} \approx 0.7682$$, $$f''(1.2) = \frac{1}{(1.5620)^3} \approx 0.2624$$.
   - Hướng Newton: $$v = -\frac{f'(1.2)}{f''(1.2)} = -1.2(2.44) = -2.928$$.
   - $$\lambda(1.2)^2 = -f'(1.2)v \approx 0.7682 \times 2.928 \approx 2.2494$$.
2. **Thử $$t = 1$$:**
   - Điểm mới: $$x + v = 1.2 - 2.928 = -1.728 \implies f(-1.728) = \sqrt{1 + 2.986} \approx 1.9965$$.
   - Ngưỡng Armijo: $$1.5620 - 0.25(1)(2.2494) = 0.9997$$. Vì $$1.9965 > 0.9997$$ (thậm chí tăng!), **từ chối $$t = 1$$** và giảm $$t \leftarrow 0.5$$.
3. **Thử $$t = 0.5$$:**
   - Điểm mới: $$x + 0.5v = 1.2 - 1.464 = -0.264 \implies f(-0.264) = \sqrt{1 + 0.0697} \approx 1.0343$$.
   - Ngưỡng Armijo: $$1.5620 - 0.25(0.5)(2.2494) \approx 1.2808$$.
   - Vì $$1.0343 \le 1.2808$$, **chấp nhận $$t = 0.5$$!**
4. **Kết quả kỳ diệu:** Điểm mới $$x^{(1)} = -0.264$$ đã rơi gọn vào vùng hội tụ bậc hai ($$\vert x \vert < 1$$), nên từ vòng lặp tiếp theo trở đi, $$t = 1$$ sẽ luôn được chấp nhận và hội tụ về $$0$$ trong chớp mắt!

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Đến đây, chúng ta mới xét phương pháp Newton thuần túy. Vì phương pháp này không đảm bảo hội tụ toàn cục, ta kết hợp thêm tìm kiếm đường backtracking để thu được phương pháp Newton có giảm chấn (damped Newton method).

## Phương pháp Newton có giảm chấn
Phương pháp Newton thuần túy lặp lại công thức cập nhật sau với $$t = 1$$:

>\begin{align}
>x^{+} = x -t(\nabla^{2}f(x))^{-1}\nabla f(x).
>\end{align}

Phương pháp Newton có giảm chấn sử dụng tìm kiếm đường backtracking: nếu giá trị hàm tại điểm cập nhật lớn hơn cận trên từ xấp xỉ tuyến tính có hệ số $$\alpha$$ (điều kiện giảm đủ Armijo), ta thu nhỏ kích thước bước $$t$$:

>$$
>\begin{align}
>&\text{với các tham số }0<\alpha \leq \frac{1}{2}, 0<\beta<1, \\
>&\text{trong khi } f(x+tv)>f(x)+\alpha t \nabla f(x)^{T}v\\
>&\text{thu nhỏ }t=\beta t
>\end{align}
>$$

Ở đây, $$v=-(\nabla^{2}f(x))^{-1}\nabla f(x)$$ và $$\nabla f(x)^{T}v = -\lambda^{2}(x)$$.

## Ví dụ: hồi quy logistic
Xét bài toán hồi quy logistic với $$n = 500$$ và $$p = 100$$ để so sánh tốc độ hội tụ giữa gradient descent và phương pháp Newton kết hợp tìm kiếm đường backtracking.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/2.jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hồi quy logistic [3]</figcaption>
</p>
</figure>

Phương pháp Newton hội tụ nhanh hơn đáng kể so với gradient descent. Mục tiếp theo sẽ phân tích lý thuyết tốc độ hội tụ này.
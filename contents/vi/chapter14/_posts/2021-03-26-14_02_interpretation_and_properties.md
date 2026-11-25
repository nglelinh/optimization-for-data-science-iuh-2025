---
layout: post
title: 14-02 Giải thích và Tính chất
chapter: '14'
order: 5
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Một thuật toán chỉ thực sự đáng tin khi ta hiểu rõ **bản chất, điểm mạnh và ranh giới sụp đổ** của nó. Trước khi gắn thêm các cơ chế bảo vệ như backtracking line search, mục 14-02 dừng lại để soi chiếu phương pháp Newton dưới ba góc độ nền tảng: mối quan hệ lịch sử với bài toán **tìm nghiệm phương trình**, đặc quyền **bất biến affine**, và tính **hội tụ cục bộ** cực nhanh nhưng cũng cực kỳ đỏng đảnh khi đứng quá xa nghiệm.

Nắm rõ bộ ba tính chất này sẽ giúp bạn giải thích ngay lập tức vì sao phương pháp Newton không cần chuẩn hóa dữ liệu (feature scaling) như Gradient Descent, nhưng lại có thể phân kỳ nổ tung nếu thiếu cơ chế giảm chấn.

## Bản đồ kiến thức nền: Ba đặc tính cốt lõi định danh phương pháp Newton

- **Cầu nối tìm nghiệm ↔ tối ưu hóa:** Tìm cực tiểu của hàm trơn lồi $$f(x)$$ chính là tìm nghiệm của hệ phương trình $$\nabla f(x) = 0$$. Áp dụng Newton–Raphson cổ điển cho hàm vectơ $$F(x) = \nabla f(x)$$ sinh ra đúng bước Newton tối ưu hóa!
- **Tính bất biến affine (Affine Invariance):** Nếu đổi biến $$x = Ay$$ (với $$A$$ khả nghịch), dãy điểm Newton sinh ra trong không gian $$y$$ khi nhân ngược lại với $$A$$ sẽ trùng khít từng điểm với dãy Newton trong không gian $$x$$.
- **Hội tụ cục bộ bậc hai — con dao hai lưỡi:** Trong một bán kính đủ nhỏ quanh $$x^\star$$, sai số giảm bình phương sau mỗi bước ($$\|x^+ - x^\star\| \le C\|x - x^\star\|^2$$). Nhưng bên ngoài bán kính đó, bước Newton thuần túy không hề có bảo chứng hội tụ và có thể nhảy ra vô cực.

### Khung giải thích (nên đọc chậm): Quan sát cả hai mặt — siêu nhanh gần nghiệm và phân kỳ xa nghiệm

Xét hàm 1 chiều $$f(x) = \sqrt{1 + x^2}$$ (hàm lồi chặt, đáy duy nhất tại $$x^\star = 0$$). Ta tính đạo hàm:
$$f'(x) = \frac{x}{\sqrt{1 + x^2}}, \qquad f''(x) = \frac{1}{(1 + x^2)^{3/2}}.$$
Bước cập nhật Newton thuần túy rút gọn cực đẹp:
$$x^+ = x - \frac{f'(x)}{f''(x)} = x - x(1 + x^2) = -x^3.$$

Hãy thử hai điểm khởi tạo khác nhau:
1. **Khởi tạo gần nghiệm ($$x^{(0)} = 0.5$$):**
   - $$x^{(1)} = -(0.5)^3 = -0.125$$.
   - $$x^{(2)} = -(-0.125)^3 \approx +0.00195$$.
   - $$x^{(3)} \approx -7.45 \times 10^{-9}$$.
   Tốc độ hội tụ thậm chí là **bậc ba** — chỉ 3 bước đã chính xác tới 8 chữ số thập phân!
2. **Khởi tạo hơi xa nghiệm ($$x^{(0)} = 1.2$$):**
   - $$x^{(1)} = -(1.2)^3 = -1.728$$.
   - $$x^{(2)} = -(-1.728)^3 \approx +5.16$$.
   - $$x^{(3)} \approx -137.4$$ — nổ tung ra vô cực!
   Ranh giới hội tụ cục bộ ở đây là $$\vert x^{(0)} \vert < 1$$; tại $$\vert x^{(0)} \vert = 1$$, thuật toán dao động mãi mãi giữa $$1$$ và $$-1$$.

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trong mục này, trước khi khảo sát các tính chất của phương pháp Newton, chúng ta tìm hiểu cách áp dụng phương pháp này cho bài toán tìm nghiệm.

Tiếp theo, chúng ta sẽ phân tích hai tính chất quan trọng của phương pháp Newton: tính bất biến affine và hội tụ cục bộ.
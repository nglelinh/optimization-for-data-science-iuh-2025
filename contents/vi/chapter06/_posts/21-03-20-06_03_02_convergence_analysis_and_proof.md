---
layout: post
title: 06-03-02 Phân Tích Hội Tụ & Chứng Minh
chapter: '06'
order: 11
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Rất nhiều sinh viên toán và khoa học máy tính lần đầu đọc chứng minh tốc độ hội tụ $$O(1/k)$$ của Gradient Descent thường thắc mắc: *tại sao chứng minh lại đột nhiên khai triển hiệu khoảng cách $$\|x^{(i)} - x^\star\|_2^2 - \|x^{(i+1)} - x^\star\|_2^2$$ rồi cộng dồn từ $$i=0$$ đến $$k-1$$?*

Bí mật nằm ở kỹ thuật **hàm thế năng (Lyapunov / Potential Function)** — một trong những công cụ đẹp nhất của giải tích thuật toán. Mỗi bước GD đổi một phần khoảng cách bình phương tới nghiệm $$\|x^{(i)} - x^\star\|_2^2$$ để lấy mức giảm sai số hàm mục tiêu $$f(x^{(i+1)}) - f^\star$$. Khi cộng dồn $$k$$ bước lại, các số hạng trung gian tự triệt tiêu sạch sẽ (telescoping sum), để lại ngay cận trên gọn gàng $$\frac{\|x^{(0)} - x^\star\|_2^2}{2tk}$$!

## Kiến thức cần nhớ: Ba mắt xích trong chứng minh tốc độ hội tụ $$O(1/k)$$

Chứng minh kinh điển này chỉ dựa trên đúng ba bất đẳng thức ghép nối nhau như bánh răng:

- **Mắt xích 1 — Cận trên bậc hai (Bổ đề giảm):** Với $$t \le 1/L$$, mỗi bước thỏa $$f(x^+) \le f(x) - \frac{t}{2}\|\nabla f(x)\|_2^2$$.
- **Mắt xích 2 — Cận dưới lồi tại nghiệm $$x^\star$$:** Vì $$f$$ lồi, $$f(x) \le f(x^\star) + \nabla f(x)^T(x - x^\star)$$. Thay vào Mắt xích 1 rồi hoàn thành bình phương theo $$x - t\nabla f(x) - x^\star = x^+ - x^\star$$ thu ngay:
  $$f(x^+) - f^\star \le \frac{1}{2t}\left(\|x - x^\star\|_2^2 - \|x^+ - x^\star\|_2^2\right).$$
- **Mắt xích 3 — Tổng lồng nhau & Tính đơn điệu giảm của $$f(x^{(i)})$$:** Cộng bất đẳng thức trên từ $$i = 0$$ đến $$k - 1$$ cho $$\sum_{i=1}^k (f(x^{(i)}) - f^\star) \le \frac{1}{2t}\|x^{(0)} - x^\star\|_2^2$$. Vì $$f(x^{(k)})$$ nhỏ nhất trong cả dãy, ta chia cả hai vế cho $$k$$ và thu được ngay:
  $$f(x^{(k)}) - f^\star \le \frac{\|x^{(0)} - x^\star\|_2^2}{2tk}.$$

### Giải thích: Kiểm chứng từng mắt xích của chứng minh bằng số cụ thể

Xét $$f(x) = \frac{1}{2} x^2$$ ($$L = 1,\; x^\star = 0,\; f^\star = 0$$), bước $$t = 0.5 \le 1/L$$, xuất phát từ $$x^{(0)} = 2$$:

1. **Quỹ đạo 3 bước đầu:**
   - $$x^{(0)} = 2,\; f = 2,\; \|x^{(0)} - x^\star\|^2 = 4$$.
   - $$x^{(1)} = 1,\; f = 0.5,\; \|x^{(1)} - x^\star\|^2 = 1$$.
   - $$x^{(2)} = 0.5,\; f = 0.125,\; \|x^{(2)} - x^\star\|^2 = 0.25$$.
   - $$x^{(3)} = 0.25,\; f = 0.03125,\; \|x^{(3)} - x^\star\|^2 = 0.0625$$.
2. **Kiểm tra Mắt xích 2 tại bước $$i = 0 \to 1$$:**
   - Vế trái: $$f(x^{(1)}) - f^\star = 0.5$$.
   - Vế phải: $$\frac{1}{2(0.5)}(4 - 1) = 3$$. Quả nhiên $$0.5 \le 3$$!
3. **Kiểm tra Tổng lồng nhau tại $$k = 3$$:**
   - Tổng sai số 3 bước: $$0.5 + 0.125 + 0.03125 = 0.65625$$.
   - Vế phải telescoping: $$\frac{1}{2(0.5)}(4 - 0.0625) = 3.9375 \le 4$$.
   - Cận cuối cùng tại $$k = 3$$: $$f(x^{(3)}) - f^\star = 0.03125 \le \frac{4}{2(0.5)(3)} = 1.3333$$.
   **Nhận xét:** Cận $$O(1/k)$$ là cận *trường hợp xấu nhất* cho mọi hàm lồi $$L$$-trơn; vì $$f(x) = \frac{1}{2}x^2$$ còn lồi mạnh nên thực tế nó hội tụ nhanh hơn cận $$O(1/k)$$ rất nhiều!

---

Giả sử $$f$$ lồi, khả vi với $$dom(f) = \mathbb{R}^n$$ và $$\nabla f$$ liên tục Lipschitz với hằng số $$L > 0$$:

>$$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2 \quad \text{với mọi } x, y$$

Tham khảo: [[Wikipedia: Lipschitz continuity](https://en.wikipedia.org/wiki/Lipschitz_continuity)]

## Định lý Hội tụ

Thuật toán **gradient descent** với kích thước bước cố định $$t \le 1/L$$ thỏa mãn:
>$$
\begin{align}
f(x^{(k)}) - f^* \le \frac{ \| x^{(0)} - x^* \|^2_2 }{2tk}
\end{align}
$$

Với kích thước bước cố định, tốc độ hội tụ là $$O(1/k)$$. Do đó, để đạt sai số $$f(x^{(k)}) - f^* \le \epsilon$$, thuật toán cần $$O(1/\epsilon)$$ vòng lặp.

## Chứng minh (Bổ đề giảm)

Vì $$f$$ lồi và $$\nabla f$$ liên tục Lipschitz với hằng số $$L$$, hàm $$f$$ thỏa mãn cận trên bậc hai (xem [06-03-01]({% multilang_post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %})):

> $$
\begin{align}
f(y) \le f(x) + \nabla f(x)^T (y-x) + \frac{L}{2} \| y - x \|^2_2 \quad \forall x, y
\end{align}
$$

Với bước cập nhật gradient descent $$x^+ = x - t \nabla f(x)$$, thay $$y = x^+$$ vào bất đẳng thức trên, ta được:

>$$
\begin{align}
f(x^+) & \le f(x) - t \left( 1 - \frac{Lt}{2} \right)\| \nabla f(x) \|^2_2 \\
& \le f(x) - \frac{t}{2} \| \nabla f(x) \|^2_2 \quad \text{nếu } t \le 1/L
\end{align}
$$

Do đó $$f(x^+) < f(x)$$ mỗi khi $$\nabla f(x) \neq 0$$, cho thấy giá trị hàm mục tiêu giảm nghiêm ngặt qua từng bước lặp và tiến tới hội tụ.

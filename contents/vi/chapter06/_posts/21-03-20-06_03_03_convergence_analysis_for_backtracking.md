---
layout: post
title: 06-03-03 Convergence analysis for backtracking
chapter: '06'
order: 12
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

Ở bài trước ta đã chứng minh Gradient Descent bước cố định $$t \le 1/L$$ đạt tốc độ hội tụ $$O(1/k)$$, nhưng ta phải biết trước hằng số $$L$$. Vậy nếu ta dùng **Backtracking Line Search** (tự động chọn bước $$t_k$$ khác nhau ở mỗi vòng lặp mà không hề biết $$L$$), liệu tốc độ hội tụ $$O(1/k)$$ có bị suy giảm hay không?

Câu trả lời là một trong những tin vui lớn nhất của tối ưu hóa thực hành: **Backtracking Line Search giữ nguyên trọn vẹn tốc độ hội tụ $$O(1/k)$$**, chỉ trả thêm một hệ số hằng nhỏ cỡ $$1/\beta$$ (ví dụ gấp đôi khi $$\beta = 0.5$$) — trong khi đổi lại bạn **không bao giờ phải ước lượng $$L$$ bằng tay** và thường chạy nhanh hơn bước cố định rất nhiều trên vùng phẳng!

## Bản đồ kiến thức nền: Vì sao Backtracking luôn có cận dưới cho bước $$t_k$$?

Ba trụ cột sau giải thích gọn gàng chứng minh hội tụ của Backtracking Line Search:

- **Chặn dưới kích thước bước $$t_{\min}$$:** Khi $$\alpha \le 0.5$$, mọi bước $$t \le 1/L$$ đều tự động thỏa điều kiện Armijo $$f(x - tg) \le f(x) - \frac{t}{2}\|g\|_2^2$$. Do Backtracking chỉ nhân thêm $$\beta$$ mỗi lần thử thất bại, nên bước cuối cùng được chấp nhận chắc chắn thỏa:
  $$t_k \ge \min\left(1,\; \frac{\beta}{L}\right) = t_{\min}.$$
- **Chứng minh tương tự bước cố định:** Vì mỗi bước đều thỏa $$f(x^+) \le f(x) - \frac{t_k}{2}\|\nabla f(x)\|_2^2$$ (khi chọn $$\alpha = 0.5$$) và $$t_k \ge t_{\min}$$, ta thay $$t$$ bằng $$t_{\min}$$ trong chuỗi tổng lồng nhau và thu ngay:
  $$f(x^{(k)}) - f^\star \le \frac{\|x^{(0)} - x^\star\|_2^2}{2 t_{\min} k}.$$
- **Ưu thế ẩn của độ cong địa phương:** Cận lý thuyết dùng $$L$$ toàn cục, nhưng thực tế tại những vùng hàm có độ cong địa phương $$L_{\text{loc}} \ll L$$, Backtracking chấp nhận bước $$t_k \approx 1/L_{\text{loc}} \gg 1/L$$ — giúp chạy nhanh vượt trội so với bước cố định $$1/L$$!

### Khung giải thích (nên đọc chậm): Tính cận dưới $$t_{\min}$$ và so sánh cận sai số với bước cố định

Giả sử một bài toán hồi quy có hằng số trơn thật (nhưng ta không biết) là $$L = 20$$, và khoảng cách ban đầu $$\|x^{(0)} - x^\star\|_2 = 2$$. Ta dùng Backtracking với $$t_0 = 1,\; \alpha = 0.5,\; \beta = 0.5$$:

1. **Bước 1 — Tính cận dưới bước chấp nhận $$t_{\min}$$:**
   $$t_{\min} = \min\left(1,\; \frac{\beta}{L}\right) = \min\left(1,\; \frac{0.5}{20}\right) = 0.025.$$
   Điều này có nghĩa là trong quá trình co bước $$1 \to 0.5 \to 0.25 \to 0.125 \to 0.0625 \to 0.03125$$, vòng lặp `while` **chắc chắn dừng chậm nhất ở $$t = 0.03125$$** (chỉ tối đa 5 phép thử, vì $$0.03125 \le 1/20 = 0.05$$ đã thỏa Armijo!).
2. **Bước 2 — So sánh cận sai số tại $$k = 100$$:**
   - Bước cố định biết trước $$L$$ ($$t = 1/L = 0.05$$):
     $$f(x^{(100)}) - f^\star \le \frac{2^2}{2(0.05)(100)} = \frac{4}{10} = 0.4.$$
   - Backtracking không cần biết $$L$$ ($$t_{\min} = 0.025$$):
     $$f(x^{(100)}) - f^\star \le \frac{2^2}{2(0.025)(100)} = \frac{4}{5} = 0.8.$$
3. **Kết luận:** Không cần biết trước $$L = 20$$, Backtracking chỉ trả tối đa hệ số $$2\times$$ trong trường hợp xấu nhất — một mức giá quá hời cho sự an toàn và khả năng tự thích ứng!

---

Giả sử $$f$$ lồi, khả vi với $$dom(f) = \mathbb{R}^n$$ và $$\nabla f$$ liên tục Lipschitz với hằng số $$L > 0$$:
>$$ \| \nabla f(x) - \nabla f(y) \|_2 \le L \| x - y \|_2 \quad \text{với mọi } x, y$$

Tham khảo: [[Wikipedia: Lipschitz continuity](https://en.wikipedia.org/wiki/Lipschitz_continuity)]

## Định lý Hội tụ

Thuật toán **gradient descent** kết hợp tìm kiếm đường lùi (backtracking line search) thỏa mãn:
> $$ \begin{align}
f(x^{(k)}) - f^* \le \frac{\| x^{(0)} - x^* \|_2^2}{2 t_{min} k}, \quad t_{min} = \min \{ 1, \beta/L \}
\end{align} $$

Tốc độ hội tụ của tìm kiếm đường lùi có cùng bậc $$O(1/k)$$ như trường hợp kích thước bước cố định, trong đó $$t$$ được thay bởi $$t_{min}$$. Nếu $$\beta$$ không quá nhỏ thì cận hội tụ tương đương với kích thước bước cố định ($$\beta/L$$ so với $$1/L$$), trong khi không cần biết trước hằng số $$L$$.

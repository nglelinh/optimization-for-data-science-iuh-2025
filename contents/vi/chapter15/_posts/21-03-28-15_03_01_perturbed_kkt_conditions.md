---
layout: post
title: '15-03-01 Điều kiện KKT nhiễu (Perturbed KKT conditions)'
chapter: "15"
order: 8
categories:
- chapter16
lang: vi
---

Trong hệ điều kiện KKT của bài toán gốc, điều kiện khó chịu nhất về mặt tính toán chính là **điều kiện bù yếu (complementary slackness)**: $$u_i h_i(x) = 0$$. Vì tích bằng $$0$$ buộc *hoặc* $$u_i = 0$$ *hoặc* $$h_i(x) = 0$$, phương trình này có dạng góc vuông chữ L gãy khúc (tổ hợp rời rạc: phải đoán xem ràng buộc nào đang tích cực!).

Cái đẹp thiên tài của hàm chắn logarit nằm ở chỗ nó **làm tròn góc vuông chữ L đó thành một đường cong hypebol mượt mà**: $$-u_i h_i(x) = \frac{1}{t}$$! Hệ phương trình mới gọi là **điều kiện KKT nhiễu (perturbed KKT conditions)**. Khi $$t$$ tăng dần tới $$+\infty$$, đường cong hypebol ép sát vào hai trục tọa độ và tiến mượt mà về đúng góc vuông KKT gốc — đây cũng chính là cầu nối trực tiếp sang phương pháp điểm trong nguyên thủy – đối ngẫu ở Chương 17!

## Kiến thức cần nhớ: So sánh trực diện KKT gốc và KKT nhiễu

- **Bốn phương trình của KKT gốc:** (1) Dừng: $$\nabla f(x) + \sum u_i \nabla h_i(x) + A^T v = 0$$; (2) Khả thi nguyên thủy: $$h_i(x) \le 0, Ax = b$$; (3) Khả thi đối ngẫu: $$u_i \ge 0$$; (4) Bù yếu: $$u_i h_i(x) = 0$$.
- **Biến đổi từ phương trình dừng của bài toán chắn:** Chia phương trình $$t\nabla f(x) - \sum \frac{1}{h_i(x)}\nabla h_i(x) + A^T w = 0$$ cho $$t$$ và đặt:
  $$u_i = -\frac{1}{t h_i(x)}, \qquad v = \frac{w}{t}.$$
- **Sự khác biệt duy nhất nằm ở điều kiện thứ (4):** Cả ba điều kiện đầu đều khớp nguyên bản (thậm chí chặt hơn: $$h_i(x) < 0$$ và $$u_i > 0$$), chỉ duy nhất điều kiện bù yếu bị nhiễu đúng một lượng $$1/t$$: $$-u_i h_i(x) = \frac{1}{t}$$.

### Giải thích: Quan sát đường hypebol $$-u h(x) = 1/t$$ ép sát góc vuông KKT

Xét bài toán $$\min_{x \in \mathbb{R}} \frac{1}{2}(x - 2)^2$$ với ràng buộc $$h(x) = x - 1 \le 0$$ (nghiệm KKT gốc: $$x^* = 1, h(x^*) = 0, u^* = 1$$).

1. **Viết hệ KKT nhiễu ứng với tham số $$t > 0$$:**
   - Điều kiện dừng: $$(x - 2) + u(1) = 0 \implies u = 2 - x$$.
   - Bù yếu nhiễu: $$-u(x - 1) = \frac{1}{t} \iff (2 - x)(1 - x) = \frac{1}{t}$$ (với $$x < 1, u > 0$$).
2. **Giải cụ thể tại hai mốc $$t = 1$$ và $$t = 100$$:**
   - **Tại $$t = 1$$:** $$(2-x)(1-x) = 1 \iff x^2 - 3x + 1 = 0 \implies x^*(1) = \frac{3 - \sqrt{5}}{2} \approx 0.382$$, $$u^*(1) = 2 - 0.382 = 1.618$$.
     Kiểm tra tích bù yếu nhiễu: $$-u^*(1) h(x^*(1)) = 1.618 \times (1 - 0.382) = 1.618 \times 0.618 = 1.000 = \frac{1}{1}$$.
   - **Tại $$t = 100$$:** $$(2-x)(1-x) = 0.01 \implies x^*(100) \approx 0.9901$$, $$u^*(100) \approx 1.0099$$.
     Kiểm tra tích bù yếu nhiễu: $$-u^*(100) h(x^*(100)) = 1.0099 \times 0.0099 \approx 0.0100 = \frac{1}{100}$$.
   Cả cặp $$(x^*(t), u^*(t))$$ cùng trượt mượt mà trên đường hypebol tới đúng nghiệm KKT $$(1, 1)$$!

---

So sánh điều kiện KKT của bài toán chắn và bài toán ban đầu cho thấy mối liên hệ chặt chẽ giữa hai bài toán.

## Điều kiện KKT của bài toán chắn
Số hạng thứ hai trong phương trình dừng của bài toán chắn chính là gradient của hàm chắn logarit:
>
$$\begin{align}
t \nabla f(x^*(t)) - \sum_{i=1}^{m} \frac{1}{h_i(x^*(t))} \nabla h_i(x^*(t)) + A^Tw = 0  \\\ 
 Ax^*(t) = b, \quad h_i(x^*(t)) \lt 0, \quad i = 1, \cdots , m \\\
\end{align}$$

## Điều kiện KKT của bài toán ban đầu
Trong điều kiện KKT của bài toán gốc, điều kiện độ lệch bù (complementary slackness) đòi hỏi $$h_i(x^*) \cdot u_i^* = 0$$, nhưng trong thực tế ta khó xác định trước ràng buộc nào đạt dấu bằng trên biên:
>
$$\begin{align}
\nabla f(x^*) + \sum_{i=1}^{m} u_i^* \nabla h_i(x^*) + A^Tv^* = 0 \\\ 
Ax^* = b, \quad h_i(x^*) \le 0, \quad u_i^* \ge 0,   \\\ 
h_i(x^*) \cdot u_i^* = 0,  \quad i = 1, \cdots , m \\\
\end{align}$$

## Viết lại điều kiện KKT của bài toán chắn
Để thấy rõ mối quan hệ giữa hai hệ điều kiện, ta định nghĩa các biến đối ngẫu $$u_i(t)$$ và $$v$$ như sau:
>
$$\begin{align}
u_i(t) = - \frac{1}{t h_i(x^*(t))}, \quad v = \frac{1}{t}w
\end{align}$$

Chia cả hai vế của phương trình dừng trong bài toán chắn cho $$t$$ và thay $$u_i(t)$$, $$v$$ vào, ta thu được hệ điều kiện tương đương:

>
$$\begin{align}
& \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)) + A^Tv = 0  \\\ 
& Ax^*(t) = b, \quad u_i(t) \cdot   h_i(x^*(t)) = - \frac{1}{t}, \quad h_i(x^*(t)) \lt 0, \quad u_i(t) \gt 0 , \quad i = 1, \cdots , m \\\
\end{align}$$

Hệ này gần như trùng khớp với điều kiện KKT của bài toán gốc, ngoại trừ điều kiện độ lệch bù bị nhiễu thành $$u_i(t) \cdot h_i(x^*(t)) = - \frac{1}{t}$$. Khi $$t \to \infty$$, vế phải tiến về $$0$$, khôi phục đúng điều kiện $$h_i(x^*) \cdot u_i^* = 0$$ của bài toán ban đầu.

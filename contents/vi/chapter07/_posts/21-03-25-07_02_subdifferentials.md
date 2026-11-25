---
layout: post
title: 07-02 Vi phân dưới (Sub-differentials)
chapter: '07'
order: 3
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
lesson_type: required
---

Nếu mỗi subgradient $$g$$ là một "mặt phẳng đỡ" riêng lẻ, thì việc gom tất cả các mặt phẳng đỡ hợp lệ tại cùng một điểm $$x$$ lại thành một tập hợp duy nhất sinh ra khái niệm **Vi phân dưới (Subdifferential)** $$\partial f(x)$$. Thay vì tư duy theo một vector đơn lẻ như đạo hàm cổ điển, ta chuyển sang làm việc với một **ánh xạ đa trị** (set-valued map): mỗi điểm $$x$$ ứng với một tập lồi đóng $$\partial f(x) \subseteq \mathbb{R}^n$$.

Điều kỳ diệu là dù hàm $$f$$ không hề trơn (như đa diện hay hàm chỉ thị tập lồi), tập $$\partial f(x)$$ lại luôn sở hữu những tính chất hình học cực kỳ ngăn nắp: luôn **lồi**, luôn **đóng**, và ở mọi điểm trong của miền xác định luôn **khác rỗng và bị chặn**!

## Bản đồ kiến thức nền: Bốn tính chất vàng của Vi phân dưới $$\partial f(x)$$

Hiểu rõ cấu trúc tập hợp của $$\partial f(x)$$ giúp bạn xử lý mượt mà các định lý tối ưu và phép tính ở phần sau:

- **Tính Lồi và Đóng (Closed & Convex Set):** Tập $$\partial f(x) = \bigcap_{y \in \mathbb{R}^n} \{g \in \mathbb{R}^n : g^T(y - x) \le f(y) - f(x)\}$$ là giao của vô hạn nửa không gian đóng! Vì giao của các tập lồi đóng luôn là tập lồi đóng, $$\partial f(x)$$ luôn lồi và đóng — kể cả khi $$f$$ không lồi!
- **Tính Khác rỗng trên Phần trong Miền xác định:** Nếu $$f$$ lồi và $$x \in \operatorname{int}(\operatorname{dom} f)$$, thì $$\partial f(x) \neq \emptyset$$ và bị chặn (nhờ định lý siêu phẳng hỗ trợ áp dụng lên tập trên đồ thị $$\operatorname{epi}(f)$$!).
- **Tiêu chuẩn Khả vi tương đương:** Hàm lồi $$f$$ khả vi tại $$x$$ khi và chỉ khi $$\partial f(x)$$ chỉ gồm **đúng một phần tử duy nhất** (singleton): $$\partial f(x) = \{\nabla f(x)\}$$.
- **Trực giác Hình học ở 2D/3D:** Tại điểm gãy của $$f(x_1, x_2) = |x_1| + |x_2|$$ ở gốc tọa độ $$(0,0)$$, $$\partial f(0,0)$$ là cả **hình vuông đặc** $$[-1, 1] \times [-1, 1]$$; còn tại điểm trên cạnh $$(2, 0)$$, $$\partial f(2,0) = \{1\} \times [-1, 1]$$ là một **đoạn thẳng đứng**!

### Khung giải thích (nên đọc chậm): Xác định chính xác hình dạng tập $$\partial f(x)$$ tại 3 vị trí của $$f(x_1, x_2) = |x_1| + 2|x_2|$$

1. **Tại điểm trơn $$x^{(1)} = (3, -1)$$:** Cả hai tọa độ đều khác 0.
   $$\partial f(3, -1) = \{(+1,\; -2)\} \quad (\text{1 điểm duy nhất!}).$$
2. **Tại điểm nằm trên cạnh gãy $$x^{(2)} = (3, 0)$$:** $$x_1 > 0$$ (trơn theo $$x_1$$), $$x_2 = 0$$ (gãy theo $$x_2$$).
   - Thành phần 1 cố định: $$g_1 = +1$$.
   - Thành phần 2 chạy tự do trên đoạn $$2 \cdot [-1, 1] = [-2, 2]$$.
   $$\partial f(3, 0) = \{(1, g_2) : -2 \le g_2 \le 2\} \quad (\text{đoạn thẳng lồi đóng}).$$
3. **Tại đỉnh nhọn $$x^{(3)} = (0, 0)$$:** Cả hai tọa độ đều bằng 0.
   $$\partial f(0, 0) = [-1, 1] \times [-2, 2] \quad (\text{hình chữ nhật đặc lồi đóng}).$$
   Kiểm tra: $$(0, 0) \in [-1, 1] \times [-2, 2] \implies (0, 0)$$ là nghiệm tối ưu toàn cục!

---

Vi phân dưới (subdifferential) $$\partial f(x)$$ của một hàm lồi $$f$$ tại điểm $$x$$ là tập hợp tất cả các gradient dưới của $$f$$ tại $$x$$:

>
\begin{equation}
\partial f(x) = \{g \in \mathbb{R}^n | \text{g là gradient dưới của f tại x} \}
\end{equation}

Vi phân dưới có các tính chất cơ bản sau:

- $$\partial f(x)$$ luôn là một tập lồi đóng, bất kể $$f$$ có lồi hay không.
- Nếu $$f$$ lồi, $$\partial f(x)$$ luôn khác rỗng (chứa ít nhất một phần tử); nếu $$f$$ không lồi, $$\partial f(x)$$ có thể rỗng.
- Nếu $$f$$ lồi và khả vi tại $$x$$, thì $$\partial f(x) = \{\nabla f(x)\}$$.
- Ngược lại, nếu $$\partial f(x) = \{g\}$$ (chỉ gồm một phần tử duy nhất), thì $$f$$ khả vi tại $$x$$ và $$\nabla f(x) = g$$.

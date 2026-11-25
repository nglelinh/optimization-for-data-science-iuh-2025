---
layout: post
title: 07-03-01 Điều kiện tối ưu gradient dưới
chapter: '07'
order: 7
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
lesson_type: required
---

Rất ít định lý trong toàn bộ lịch sử toán học vừa có **chứng minh ngắn đúng 2 dòng**, vừa sở hữu sức mạnh bao quát từ bài toán tìm trung vị đến huấn luyện mạng nơ-ron và máy vector hỗ trợ. **Điều kiện tối ưu gradient dưới** — phát biểu rằng $$x^\star$$ là cực tiểu toàn cục của $$f$$ **khi và chỉ khi** $$0 \in \partial f(x^\star)$$ — chính là một kiệt tác như thế!

Một chi tiết cực kỳ thú vị mà nhiều người đọc lướt hay bỏ qua: chứng minh của bổ đề này **thậm chí không cần dùng đến giả thiết $$f$$ là hàm lồi**! Tính lồi chỉ đóng vai trò đảm bảo rằng tập $$\partial f(x)$$ thực sự tồn tại (khác rỗng) để ta có thể tìm thấy vector $$0$$ bên trong nó.

## Bản đồ kiến thức nền: Ba điểm tinh tế của Điều kiện $$0 \in \partial f(x^\star)$$

Để vận dụng bổ đề này không bao giờ sai sót, hãy nắm chắc ba điểm sau:

- **Sự tương đương logic 2 chiều tuyệt đối:**
  $$x^\star \in \arg\min_x f(x) \iff f(y) \ge f(x^\star) \; \forall y \iff f(y) \ge f(x^\star) + 0^T(y - x^\star) \; \forall y \iff 0 \in \partial f(x^\star).$$
  Không có bất kỳ xấp xỉ hay điều kiện bậc hai nào cần kiểm tra thêm — đây là chứng chỉ **tối ưu toàn cục**!
- **Tác dụng của Tính Lồi:** Với hàm phi lồi, có thể tồn tại cực tiểu địa phương mà $$\partial f(x) = \emptyset$$ (không có mặt phẳng nào đỡ được toàn bộ đồ thị phía dưới). Tính lồi đảm bảo mọi cực tiểu địa phương đều là toàn cục và có mặt phẳng đỡ ngang ($$g = 0$$)!
- **Tổng quát hóa trực tiếp phương trình Fermat:** Khi $$f$$ khả vi, $$\partial f(x^\star) = \{\nabla f(x^\star)\}$$, nên $$0 \in \partial f(x^\star)$$ lập tức trở về $$\nabla f(x^\star) = 0$$.

### Khung giải thích (nên đọc chậm): Kiểm chứng $$0 \in \partial f(x^\star)$$ để tìm cực tiểu toàn cục của hàm bậc hai + trị tuyệt đối

Xét bài toán $$f(x) = \frac{1}{2}(x - 5)^2 + 2|x - 1|$$ trên $$\mathbb{R}$$. Ta tìm điểm $$x^\star$$ thỏa $$0 \in \partial f(x^\star)$$:

1. **Tính $$\partial f(x) = (x - 5) + 2\partial|x - 1|$$ theo 3 trường hợp:**
   - Nếu $$x > 1$$: $$\partial f(x) = \{x - 5 + 2\} = \{x - 3\}$$. Cho $$0 \in \{x - 3\} \implies x^\star = 3$$ (thỏa mãn điều kiện $$3 > 1$$!).
   - Nếu $$x = 1$$: $$\partial f(1) = (1 - 5) + [-2, 2] = [-6, -2]$$. Không chứa $$0$$!
   - Nếu $$x < 1$$: $$\partial f(x) = \{x - 5 - 2\} = \{x - 7\}$$. Cho $$x - 7 = 0 \implies x = 7$$ (mâu thuẫn $$x < 1$$!).
2. **Thử tăng hệ số phạt từ $$2$$ lên $$5$$: $$f_2(x) = \frac{1}{2}(x - 5)^2 + 5|x - 1|$$:**
   - Tại $$x = 1$$: $$\partial f_2(1) = (1 - 5) + [-5, 5] = [-9, +1]$$ — **CHỨA $$0$$**!
   - Vậy ngay khi lực kéo của $$|x - 1|$$ vượt ngưỡng $$4$$, nghiệm tối ưu bị "hút dính" ngay tại điểm gãy khúc $$x^\star = 1$$!

---

### Bổ đề

Với bất kỳ hàm $$f$$ nào, điều kiện $$x^*$$ là điểm cực tiểu toàn cục của $$f$$ tương đương với việc vector $$0$$ là một gradient dưới của $$f$$ tại $$x^*$$:

> $$
\begin{equation}
f(x^*) = \min_x f(x) \Longleftrightarrow 0 \in \partial f(x^*)
\end{equation}
$$

### Chứng minh
>
$$
\begin{align}
&f(x^*) = \min_x f(x)\\
\Longleftrightarrow &f(y) \geq f(x^*) \text{ với mọi } y\\
\Longleftrightarrow &f(y) \geq f(x^*) + 0^T(y-x^*)\\
\Longleftrightarrow &0 \in \partial f(x^*)
\end{align}
$$

Lưu ý rằng chứng minh trên không sử dụng giả thiết lồi của $$f$$, vì vậy điều kiện tối ưu này đúng ngay cả với các hàm không lồi.

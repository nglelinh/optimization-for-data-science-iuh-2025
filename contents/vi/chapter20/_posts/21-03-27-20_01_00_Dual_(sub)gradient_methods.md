---
layout: post
title: '20-01 Các phương pháp dual (sub)gradient'
chapter: '20'
order: 2
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Ở ví dụ đơn giản trong bài mở đầu, ta dễ dàng viết được công thức tường minh cho hàm liên hợp $$f^*$$. Nhưng trong thực tế, phần lớn hàm $$f$$ phức tạp không hề có công thức dạng đóng cho $$f^*$$! Điều kỳ diệu của **phương pháp (dưới) gradient đối ngẫu** là ta **không bao giờ cần viết tường minh $$f^*$$**: nhờ định lý bao hàm thức liên hợp $$x \in \partial f^*(-A^T u) \iff x \in \arg\min_z (f(z) + u^T A z)$$, chỉ cần giải bài toán cực tiểu hóa theo $$x$$ với $$u$$ cố định, ta lập tức có ngay một dưới gradient của hàm đối ngẫu — chính là phần dư ràng buộc $$Ax - b$$!

## Kiến thức cần nhớ: Ba trụ cột vận hành phương pháp Dual (Sub)gradient

Hiểu ba ý tưởng sau sẽ giúp bạn thấy công thức lặp $$x^{(k)}, u^{(k)}$$ hoàn toàn tự nhiên như hơi thở:

- **Đẳng thức dưới vi phân liên hợp (Danskin's Theorem):** Với $$g(u) = \inf_x (f(x) + u^T(Ax - b))$$, mỗi nghiệm $$x^+ \in \arg\min_x (f(x) + u^T Ax)$$ tự động cung cấp một dưới gradient (hoặc gradient nếu $$x^+$$ duy nhất) của $$g$$ tại $$u$$ là $$Ax^+ - b \in \partial g(u)$$.
- **Quy tắc cập nhật Dual Ascent (tăng theo phần dư ràng buộc):** Vì ta đang **cực đại hóa** hàm lõm $$g(u)$$, ta cộng thêm bước đi theo hướng gradient: $$u^{(k)} = u^{(k-1)} + t_k(Ax^{(k)} - b)$$. Nếu $$Ax^{(k)} > b$$, nhân tử $$u$$ tăng lên để "phạt" mạnh hơn ở bước sau; nếu $$Ax^{(k)} < b$$, $$u$$ giảm xuống!
- **Xử lý ràng buộc bất đẳng thức $$Ax \le b$$:** Khi ràng buộc là bất đẳng thức, biến đối ngẫu phải giữ không âm $$u \ge 0$$, nên bước cập nhật đối ngẫu chỉ cần thêm phép chiếu đơn giản lên góc phần tư không âm: $$u^{(k)} = (u^{(k-1)} + t_k(Ax^{(k)} - b))_+$$.

### Giải thích: Chạy tay 2 vòng lặp Dual Gradient Ascent và quan sát phần dư thu hẹp

Xét bài toán tối ưu lồi 1 biến có ràng buộc đẳng thức:

$$\min_{x \in \mathbb{R}} \; \frac{1}{2}x^2 \qquad \text{với điều kiện} \qquad x = 2 \quad (A = 1, b = 2).$$

Nghiệm tối ưu dễ thấy là $$x^\star = 2, u^\star = -2$$. Chạy thuật toán Dual Gradient Ascent với khởi tạo $$u^{(0)} = 0$$ và bước học cố định $$t = 0.5$$:

1. **Vòng lặp $$k = 1$$:**
   - **Bước gốc:** $$x^{(1)} = \arg\min_x \left(\frac{1}{2}x^2 + u^{(0)} x\right) = \arg\min_x \frac{1}{2}x^2 = 0$$.
   - **Phần dư ràng buộc (gradient đối ngẫu):** $$r^{(1)} = x^{(1)} - 2 = 0 - 2 = -2$$.
   - **Bước đối ngẫu:** $$u^{(1)} = u^{(0)} + 0.5(-2) = 0 - 1 = -1$$.
2. **Vòng lặp $$k = 2$$:**
   - **Bước gốc:** $$x^{(2)} = \arg\min_x \left(\frac{1}{2}x^2 - 1 \cdot x\right) = 1$$.
   - **Phần dư ràng buộc:** $$r^{(2)} = x^{(2)} - 2 = 1 - 2 = -1$$ (sai số ràng buộc giảm đúng một nửa!).
   - **Bước đối ngẫu:** $$u^{(2)} = -1 + 0.5(-1) = -1.5$$.
3. **Quan sát quy luật hội tụ:** Ở mỗi bước, sai số $$|x^{(k)} - 2|$$ và $$|u^{(k)} - (-2)|$$ đều giảm đúng theo cấp số nhân $$0.5^k$$! Nếu chọn bước học $$t = 1$$ (đúng bằng hằng số lồi mạnh $$d = 1$$ chia cho $$\|A\|_2^2 = 1$$), ta nhảy thẳng từ $$u^{(0)} = 0$$ tới $$u^{(1)} = -2 = u^\star$$ và $$x^{(2)} = 2 = x^\star$$ ngay tức thì!

---

Ngay cả khi không thể tìm được biểu thức dạng đóng cho hàm liên hợp (và do đó cho hàm mục tiêu đối ngẫu), ta vẫn có thể áp dụng phương pháp gradient hoặc dưới vi phân (subgradient) trực tiếp trên bài toán đối ngẫu.

Xét bài toán tối ưu có ràng buộc đẳng thức:
>\begin{equation}
\min_x f(x) \text{ subject to } Ax = b
\end{equation}

Bài toán đối ngẫu tương ứng — viết qua hàm liên hợp $$f^{\ast}$$ của $$f$$ — có dạng:
>\begin{equation}
\max_u -f^{\ast}(-A^T u) - b^T u
\end{equation}

Đặt $$g(u) = -f^{\ast}(-A^Tu) - b^Tu$$. Khi đó, dưới vi phân của $$g(u)$$ là:
>\begin{equation}
\partial g(u) = A \partial f^{\ast}(-A^Tu) - b
\end{equation}

Lấy một phần tử $$x \in \partial f^{\ast}(-A^Tu)$$, theo tính chất hàm liên hợp ở bài trước, ta có thể biểu diễn phần tử thuộc $$\partial g(u)$$ như sau:

>\begin{equation}
Ax - b \in \partial g(u) \quad \text{với} \quad x \in \arg\min_z f(z) + u^T A z
\end{equation}

## Phương pháp dual subgradient
**Phương pháp dual subgradient** cực đại hóa hàm mục tiêu đối ngẫu $$g(u)$$. Bắt đầu từ điểm khởi tạo $$u^{(0)}$$, thuật toán lặp các bước sau với $$k = 1, 2, 3, \dots$$:
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)} - b) 
> \end{alignat}
> $$

trong đó dãy độ dài bước $$t_k$$ ($$k = 1, 2, 3, \dots$$) được chọn theo các quy tắc chuẩn của phương pháp subgradient.

#### Trường hợp $$f$$ lồi chặt
Nếu $$f$$ lồi chặt thì $$f^{\ast}$$ khả vi, và thuật toán trở thành **tăng gradient đối ngẫu (dual gradient ascent)** với các bước lặp ($$k = 1, 2, 3, \dots$$):
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)}-b) 
> \end{alignat}
> $$

Khác biệt so với dạng tổng quát là nghiệm $$x^{(k)}$$ là duy nhất (dùng ký hiệu "$$=$$" thay cho "$$\in$$"). Khi giải bài toán con tìm $$x^{(k)}$$, ta có thể áp dụng các kỹ thuật tăng tốc hoặc proximal gradient như thông thường.

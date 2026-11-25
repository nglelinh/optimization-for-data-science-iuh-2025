---
layout: post
title: '20-01-01 Phân tích hội tụ'
chapter: '20'
order: 3
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Một trong những định lý đối xứng đẹp nhất trong toàn bộ giải tích lồi — xứng đáng được đóng khung treo tường — là sự **đối ngẫu giữa tính lồi mạnh và độ trơn Lipschitz**: hàm gốc $$f$$ càng "cong nhọn" (lồi mạnh với tham số $$d$$), thì hàm liên hợp $$f^*$$ càng "mềm mượt" (có gradient liên tục Lipschitz với hằng số $$1/d$$), và ngược lại! Định lý này không chỉ là vẻ đẹp thuần túy mà còn cho ta công thức bước học chính xác $$t \le d / \|A\|_2^2$$ để phương pháp tăng gradient đối ngẫu hội tụ an toàn.

## Bản đồ kiến thức nền: Ba trụ cột của phân tích hội tụ phương pháp đối ngẫu

Để đọc hiểu phần chứng minh và hệ quả thực tiễn trong bài học này, hãy nắm chắc ba mối liên hệ sau:

- **Đối ngẫu hình học (Cong ở gốc $$\iff$$ Trơn ở đối ngẫu):** Nếu $$f$$ lồi mạnh với tham số $$d > 0$$, đáy của $$f(x) - u^T x$$ là duy nhất và không bao giờ phẳng lì, nên điểm cực tiểu $$x_u = \nabla f^*(u)$$ biến thiên liên tục Lipschitz theo $$u$$ với độ nhạy tối đa $$1/d$$.
- **Chuyển đổi hằng số Lipschitz qua ma trận ràng buộc $$A$$:** Với hàm đối ngẫu $$g(u) = -f^*(-A^T u) - b^T u$$, áp dụng quy tắc dây chuyền cho $$\nabla g(u) = A\nabla f^*(-A^T u) - b$$ cho thấy $$\nabla g$$ liên tục Lipschitz với hằng số $$L_g = \frac{\|A\|_2^2}{d}$$ (trong đó $$\|A\|_2 = \sigma_{\max}(A)$$ là giá trị kỳ dị lớn nhất của $$A$$).
- **Hệ quả trực tiếp cho chọn bước học và tốc độ hội tụ:** Nhờ độ trơn $$L_g$$, Dual Gradient Ascent với bước học hằng số $$t \le \frac{1}{L_g} = \frac{d}{\|A\|_2^2}$$ đảm bảo hội tụ với tốc độ $$O(1/k)$$ (và có thể gia tốc lên $$O(1/k^2)$$ bằng Nesterov!). Ngược lại, nếu $$f$$ **không** lồi mạnh ($$d = 0$$), $$g$$ có thể không khả vi và buộc phải dùng bước học giảm dần chậm chạp $$O(1/\sqrt{k})$$.

### Khung giải thích (nên đọc chậm): Kiểm chứng bằng số cặp hằng số $$(d, 1/d)$$ và ngưỡng bước học ổn định

Xét bài toán tối ưu 1 biến:

$$\min_{x \in \mathbb{R}} \; f(x) = \frac{d}{2}x^2 \quad (d = 4) \qquad \text{với điều kiện} \qquad 2x = 6 \quad (A = 2, \; b = 6).$$

1. **Kiểm tra cặp tính chất đối ngẫu:**
   - Hàm gốc $$f(x) = 2x^2$$ có $$f''(x) = 4$$, nên lồi mạnh với tham số $$d = 4$$.
   - Hàm liên hợp là $$f^*(y) = \sup_x (yx - 2x^2) = \frac{y^2}{8}$$, có đạo hàm $$\nabla f^*(y) = \frac{y}{4}$$.
   - Với mọi $$y_1, y_2$$: $$|\nabla f^*(y_1) - \nabla f^*(y_2)| = \frac{1}{4}|y_1 - y_2|$$ — hằng số Lipschitz đúng bằng $$\frac{1}{d} = \frac{1}{4}$$!
2. **Tính hằng số Lipschitz của hàm đối ngẫu $$g(u)$$ và ngưỡng bước học:**
   - Với $$A = 2$$, ta có $$\|A\|_2^2 = 4$$, suy ra $$L_g = \frac{\|A\|_2^2}{d} = \frac{4}{4} = 1$$.
   - Công thức lý thuyết bảo đảm Dual Gradient Ascent hội tụ với mọi $$t \in (0, 2/L_g) = (0, 2)$$, và bước học chuẩn là $$t = 1/L_g = 1$$.
3. **Thử nghiệm so sánh hai bước học từ $$u^{(0)} = 0$$ (nghiệm thực $$x^\star = 3, u^\star = -6$$):**
   - Với $$t = 1$$ (đúng chuẩn $$1/L_g$$): $$x^{(1)} = 0 \implies u^{(1)} = 0 + 1(0 - 6) = -6 = u^\star \implies x^{(2)} = 3 = x^\star$$ (**hội tụ sau 1 bước!**).
   - Với $$t = 2.5 > 2/L_g$$ (vượt ngưỡng ổn định): $$u^{(1)} = -15 \implies x^{(2)} = 7.5 \implies u^{(2)} = -15 + 2.5(15 - 6) = +7.5$$ — **dao động phân kỳ ngày càng lớn!**

---

## Tính đối ngẫu giữa gradient Lipschitz và tính lồi mạnh
Giả sử $$f$$ là hàm lồi đóng. Khi đó, mối tương đương sau luôn đúng:
> $$f \text{ lồi mạnh với tham số } d \Longleftrightarrow \nabla f^{\ast} \text{ liên tục Lipschitz với tham số } 1/d.$$

### Chứng minh
Ta chứng minh chiều "$$\Rightarrow$$". Nếu hàm $$g$$ lồi mạnh với tham số $$d$$ và đạt cực tiểu tại $$x$$ thì:
>\begin{equation}
g(y) \geq g(x) + \frac{d}{2}\lVert y-x \rVert_2^2, \quad \forall y
\end{equation}

Gọi $$x_u = \nabla f^{\ast}(u)$$ là điểm cực tiểu của $$x \mapsto f(x) - u^T x$$, và $$x_v = \nabla f^{\ast}(v)$$ là điểm cực tiểu của $$x \mapsto f(x) - v^T x$$. Áp dụng bất đẳng thức trên cho hai hàm này, ta có:
> $$
> \begin{alignat}{1}
> f(x_v) - u^Tx_v \geq f(x_u) - u^T x_u + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 \\
> f(x_u) - v^Tx_u \geq f(x_v) - v^T x_v + \frac{d}{2} \lVert x_u - x_v \rVert_2^2 
> \end{alignat}
> $$

Cộng hai bất đẳng thức theo vế:
>\begin{equation}
f(x_v) - u^Tx_v + f(x_u) - v^Tx_u \geq f(x_u) - u^T x_u +  f(x_v) - v^T x_v + d \lVert x_u - x_v \rVert_2^2.  
\end{equation}

Rút gọn và áp dụng bất đẳng thức Cauchy–Schwarz:
> $$
> \begin{align}
> d \lVert x_u - x_v \rVert_2^2 & \leq - u^Tx_v - v^Tx_u + u^T x_u + v^T x_v \\\\
> & = (u-v)^T(x_u - x_v) \\\\
> & \leq \lVert u-v \rVert_2 \lVert x_u - x_v \rVert_2
> \end{align}
> $$

Chia hai vế cho $$d \lVert x_u - x_v \rVert_2$$ (khi $$x_u \neq x_v$$), ta thu được:

> $$\lVert x_u - x_v \rVert_2 \leq \frac{1}{d} \lVert u-v \rVert_2$$

chứng tỏ $$\nabla f^{\ast}$$ liên tục Lipschitz với hằng số $$1/d$$.

## Đảm bảo hội tụ
Kết hợp tính chất trên với kết quả hội tụ của gradient descent, ta thu được các đảm bảo hội tụ cho phương pháp tăng gradient đối ngẫu (dual gradient ascent):

* Nếu $$f$$ lồi mạnh với tham số $$d$$, thì dual gradient ascent với độ dài bước $$t_k = d$$ ($$k = 1, 2, 3, \dots$$) hội tụ với tốc độ $$O(1/\epsilon)$$.
* Nếu $$f$$ vừa lồi mạnh với tham số $$d$$ vừa có $$\nabla f$$ liên tục Lipschitz với tham số $$L$$, thì dual gradient ascent với độ dài bước $$t_k = 2/(1/d + 1/L)$$ ($$k = 1, 2, 3, \dots$$) hội tụ tuyến tính với tốc độ $$O(\log(1/\epsilon))$$.

(Các công thức độ dài bước trên giả sử $$\lVert A \rVert_2 \le 1$$; tổng quát, gradient đối ngẫu liên tục Lipschitz với hằng số $$\lVert A \rVert_2^2 / d$$ nên độ dài bước cần được nhân thêm hệ số $$1/\lVert A \rVert_2^2$$.)

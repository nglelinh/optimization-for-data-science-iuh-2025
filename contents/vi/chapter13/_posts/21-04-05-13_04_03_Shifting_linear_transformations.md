---
layout: post
title: 13-04-03 Dịch chuyển biến đổi tuyến tính
chapter: '13'
order: 8
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Trong rất nhiều bài toán thực tế — từ lọc nhiễu ảnh *Total Variation* (phạt $$\|Dx\|_1$$ với ma trận sai phân $$D$$), đến *Fused Lasso* hay hồi quy có ràng buộc tuyến tính — khó khăn lớn nhất nằm ở chỗ hàm không trơn $$g$$ lại bọc lấy một phép biến đổi tuyến tính $$Ax$$. Ta biết rõ cách xử lý $$g(z)$$ khi đứng một mình, nhưng khi bị "dính" với ma trận $$A$$ bên trong $$g(Ax)$$, toán tử gần kề (proximal operator) không còn công thức đóng nữa!

Bài học ngắn nhưng cực kỳ đắt giá này chỉ ra một "phép hoán đổi vị trí" kỳ diệu nhờ đối ngẫu: khi lập bài toán đối ngẫu của $$\min_x f(x) + g(Ax)$$, ma trận $$A$$ nhảy sang vế bên kia dưới dạng ma trận chuyển vị $$A^T$$ nằm trong $$f^*(-A^T u)$$, còn $$g^*(u)$$ hoàn toàn tự do không dính ma trận nào! Nếu $$f^*$$ là hàm trơn (như hàm bậc hai), ta đã đẩy được ma trận $$A$$ ra khỏi hàm không trơn sang hàm trơn dễ tính đạo hàm.

## Bản đồ kiến thức nền: Nghệ thuật đẩy ma trận chuyển vị sang vế dễ hơn

- **Biến đổi tương đương $$z = Ax$$:** Tách toán tử tuyến tính $$A$$ ra khỏi hàm $$g$$ bằng một ràng buộc đẳng thức $$Ax - z = 0$$, sau đó nhân với biến đối ngẫu $$u$$ trong hàm Lagrange.
- **Tính chất liên hợp của ma trận chuyển vị:** Trong biểu thức $$u^T(Ax - z) = (A^T u)^T x - u^T z$$, ma trận $$A$$ tự động chuyển từ tác động lên $$x$$ sang dạng $$A^T$$ tác động lên biến đối ngẫu $$u$$.
- **Lợi ích thuật toán thực chiến:** Khi $$f$$ lồi mạnh (nên $$f^*$$ khả vi Lipschitz) còn $$g$$ là chuẩn không trơn (như $$\|Dx\|_1$$), bài toán đối ngẫu $$\min_u f^*(-A^T u) + g^*(u)$$ trở thành bài toán tối ưu hàm trơn trên tập hộp đơn giản — giải cực nhanh bằng FISTA hay Projected Gradient Descent!

### Khung giải thích (nên đọc chậm): Dịch chuyển ma trận sai phân trong bài toán làm mịn 1D (Fused Signal)

Xét tín hiệu 2 điểm $$y = (0, 4)^T$$ và bài toán làm mịn:

$$\min_{x \in \mathbb{R}^2} \underbrace{\frac{1}{2}\|x - y\|_2^2}_{f(x)} + \underbrace{\vert x_2 - x_1 \vert}_{g(Ax)},$$

trong đó ma trận sai phân $$A = \begin{bmatrix} -1 & 1 \end{bmatrix}$$ ($$Ax = x_2 - x_1$$) và $$g(z) = \vert z \vert$$.

1. **Tính hai hàm liên hợp:**
   - $$f^*(w) = \frac{1}{2}\|w\|_2^2 + y^T w$$ (vì $$f(x) = \frac{1}{2}\|x - y\|_2^2$$).
   - $$g^*(u) = I_{[-1, 1]}(u)$$ với $$u \in \mathbb{R}$$.
2. **Áp dụng công thức dịch chuyển biến đổi tuyến tính:**
   Bài toán đối ngẫu là $$\max_u -f^*(-A^T u) - g^*(u)$$, tương đương cực tiểu hóa theo biến vô hướng $$u \in [-1, 1]$$:
   $$\min_{\vert u \vert \le 1} \frac{1}{2}\|A^T u\|_2^2 - y^T (A^T u).$$
   Ta tính cụ thể: $$A^T u = (-u, u)^T$$, nên $$\|A^T u\|_2^2 = 2u^2$$ và $$y^T(A^T u) = 0(-u) + 4(u) = 4u$$.
   Vậy bài toán đối ngẫu thu gọn thành bài toán 1 biến cực dễ:
   $$\min_{-1 \le u \le 1} \bigl(u^2 - 4u\bigr).$$
3. **Giải đối ngẫu và khôi phục $$x^\star$$:**
   - Parabol $$u^2 - 4u$$ có đỉnh tại $$u = 2$$, bị chặn bởi $$[-1, 1]$$ nên đạt cực tiểu tại $$u^\star = 1$$.
   - Khôi phục từ điều kiện dừng $$x^\star - y = -A^T u^\star$$:
     $$x^\star = y - A^T u^\star = \begin{bmatrix} 0 \\ 4 \end{bmatrix} - \begin{bmatrix} -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \end{bmatrix}.$$
   - Kiểm tra giá trị: nguyên thủy $$f(x^\star) + g(Ax^\star) = \frac{1}{2}(1^2 + (-1)^2) + \vert 3 - 1 \vert = 1 + 2 = 3$$; đối ngẫu $$-((1)^2 - 4(1)) = 3$$. Hai bên bằng nhau tuyệt đối!

---

Kỹ thuật lập bài toán đối ngẫu cho phép dịch chuyển phép biến đổi tuyến tính từ một thành phần này sang thành phần khác của hàm mục tiêu.

Xét bài toán sau:

> $$ \min_x f(x) + g(Ax)$$

Ta viết lại bài toán ở dạng tương đương bằng cách đặt $$z = Ax$$:

> $$\min_{x,z} f(x) + g(z) \text{ với điều kiện } Ax = z$$

Từ đó tính hàm đối ngẫu Lagrange:

> $$g(u) = \min_{x,z} \left(f(x) + g(z) + u^T(z - Ax)\right)$$
> $$\qquad  = -\max_{x} \left((A^T u)^T x - f(x)\right) - \max_{z} \left((-u)^T z - g(z)\right)$$
> $$\qquad = -f^* (A^T u) - g^* (-u) $$

Vậy bài toán đối ngẫu là:

> $$\max_u -f^*(A^Tu) - g^*(-u)$$

#### Ví dụ

Với một chuẩn $$\| \cdot \|$$ và chuẩn đối ngẫu tương ứng $$\| \cdot \|_{*}$$, xét cặp bài toán:

> $$ \min_x f(x) + \| Ax \|$$
> 
> $$ \max_u -f^*(A^Tu) \text{ với điều kiện } \| u \|_{*} \leq 1$$

Bài toán thứ nhất là bài toán nguyên thủy, còn bài toán thứ hai là bài toán đối ngẫu tương ứng, trong đó ma trận $$A$$ đã được chuyển sang tác động lên đối số của $$f^*$$ dưới dạng $$A^T u$$.

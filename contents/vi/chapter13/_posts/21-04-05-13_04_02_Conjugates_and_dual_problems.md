---
layout: post
title: 13-04-02 Hàm liên hợp và bài toán đối ngẫu
chapter: '13'
order: 7
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

Nếu từng phải tính hàm đối ngẫu bằng tay nhiều lần, bạn sẽ nhận ra một mô-típ lặp đi lặp lại đến kỳ lạ: gần như lần nào ta cũng viết ra biểu thức $$\min_x (f(x) - u^T x)$$, và lần nào nó cũng biến thành $$-f^*(u)$$. Đây không phải sự trùng hợp ngẫu nhiên, mà là cấu trúc cốt lõi nối liền **đối ngẫu Lagrange** với **đối ngẫu Fenchel**.

Thay vì mỗi lần gặp bài toán tổng hai hàm $$\min_x f(x) + g(x)$$ lại phải đạo hàm từng bước dài dòng, hàm liên hợp cho ta một "công thức rút gọn siêu tốc": tách biến $$x = z$$, đưa nhân tử $$u$$ vào, và chỉ sau hai dòng đại số, bài toán đối ngẫu hiện ra cực kỳ đối xứng: $$\max_u -f^*(u) - g^*(-u)$$.

## Bản đồ kiến thức nền: Chiếc cầu giữa hàm liên hợp và bài toán đối ngẫu

- **Đồng nhất thức nền tảng:** $$\min_x \{f(x) - u^T x\} = -\max_x \{u^T x - f(x)\} = -f^*(u)$$. Bất cứ khi nào hàm mục tiêu cộng thêm một số hạng tuyến tính, cực tiểu hóa nó chính là tính âm của hàm liên hợp.
- **Tách biến cho tổng hai hàm:** Bài toán $$\min_x f(x) + g(x)$$ được viết thành $$\min_{x=z} f(x) + g(z)$$. Nhân tử đối ngẫu $$u$$ buộc hai biến $$x, z$$ có cùng độ dốc ngược dấu ($$u$$ và $$-u$$), dẫn thẳng tới bài toán đối ngẫu Fenchel $$\max_u -f^*(u) - g^*(-u)$$.
- **Mở rộng cho các hàm phạt chuẩn và hàm chỉ thị:** Khi $$g(x)$$ là hàm chỉ thị $$I_C(x)$$ của một tập lồi $$C$$, liên hợp $$g^*(v)$$ chính là **hàm tựa (support function)** $$\max_{x \in C} v^T x$$; khi $$g(x) = \|x\|$$, liên hợp là hàm chỉ thị của quả cầu chuẩn đối ngẫu.

### Khung giải thích (nên đọc chậm): Suy dẫn đối ngẫu tức thì cho bài toán tổng hai hàm 1 chiều

Xét bài toán không ràng buộc:

$$\min_{x \in \mathbb{R}} \underbrace{\frac{1}{2}(x - 3)^2}_{f(x)} + \underbrace{2\vert x \vert}_{g(x)}.$$

1. **Tính nhanh hai hàm liên hợp:**
   - Với $$f(x) = \frac{1}{2}(x - 3)^2$$: cực đại của $$ux - \frac{1}{2}(x-3)^2$$ đạt tại $$x - 3 = u \implies x = u + 3$$. Thay vào ta được:
     $$f^*(u) = u(u+3) - \frac{1}{2}u^2 = \frac{1}{2}u^2 + 3u.$$
   - Với $$g(x) = 2\vert x \vert$$: tương tự hàm giá trị tuyệt đối có hệ số $$2$$, ta có $$g^*(w) = 0$$ nếu $$\vert w \vert \le 2$$ và $$+\infty$$ nếu $$\vert w \vert > 2$$.
2. **Áp dụng công thức đối ngẫu $$\max_u -f^*(u) - g^*(-u)$$:**
   Điều kiện $$g^*(-u) < \infty$$ tương đương $$\vert -u \vert \le 2 \iff -2 \le u \le 2$$. Bài toán đối ngẫu trở thành:
   $$\max_{-2 \le u \le 2} \left(-\frac{1}{2}u^2 - 3u\right).$$
3. **Giải bài toán đối ngẫu:** Parabol $$-\frac{1}{2}u^2 - 3u$$ có đỉnh tự do tại $$u = -3$$, nằm ngoài đoạn $$[-2, 2]$$, nên trên $$[-2, 2]$$ nó đạt cực đại tại biên trái $$u^\star = -2$$.
   - Giá trị đối ngẫu tối ưu: $$-\frac{1}{2}(-2)^2 - 3(-2) = -2 + 6 = 4$$.
4. **Khôi phục nghiệm nguyên thủy:** Từ điều kiện đạt cực đại trong $$f^*(u^\star)$$, ta có $$x^\star = u^\star + 3 = -2 + 3 = 1$$.
   - Kiểm tra giá trị nguyên thủy: $$f(1) + g(1) = \frac{1}{2}(1-3)^2 + 2\vert 1\vert = 2 + 2 = 4$$ — khớp tuyệt đối!

---

Hàm liên hợp thường xuất hiện trực tiếp khi suy dẫn bài toán đối ngẫu từ bài toán cực tiểu hóa hàm Lagrangian, thông qua hệ thức:

> $$-f^{*}(u) = \min_x (f(x) - u^Tx)$$

Chẳng hạn, xét bài toán tổng hai hàm không ràng buộc:

> $$ \min_x  f(x) + g(x)$$

Ta đưa thêm biến phụ và ràng buộc đẳng thức để viết lại bài toán tương đương:

> $$ \min_{x,z} f(x) + g(z) \text{ với điều kiện } x = z $$

Hàm đối ngẫu Lagrange tương ứng là:

> $$g(u) = \min_{x,z} \left(f(x) + g(z) + u^T(z - x)\right) = -f^{*}(u) - g^{*}(-u)$$

Do đó, bài toán đối ngẫu của bài toán gốc là:

> $$ \max_u -f^{*}(u) - g^{*}(-u)$$

#### Ví dụ

* **Hàm chỉ thị:** Đối ngẫu của $$\min_x f(x) + I_C(x)$$ là:
> $$ \max_u -f^{*}(u) - I^{*}_C(-u)$$
> 
> trong đó $$I^{*}_C$$ là hàm hỗ trợ của tập $$C$$.

* **Hàm chuẩn:** Đối ngẫu của $$\min_x f(x) + \lVert x \rVert$$ là:

> $$ \max_u -f^{*}(u) \text{ với điều kiện } \lVert u \rVert_{*} \le 1$$, trong đó $$\lVert \cdot \rVert_{*}$$ là chuẩn đối ngẫu của $$\lVert \cdot \rVert$$.

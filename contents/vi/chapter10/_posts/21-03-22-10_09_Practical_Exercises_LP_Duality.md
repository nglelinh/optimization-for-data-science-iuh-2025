---
layout: post
title: "10-09 Bài Tập Thực Hành - Tính Đối Ngẫu trong Quy Hoạch Tuyến Tính"
chapter: "10"
order: 10
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter10
lesson_type: required
redirect_from:
  - /contents/vi/chapter10/10_07_Practical_Exercises_LP_Duality/
---

Biết viết bài toán đối ngẫu trên giấy mới chỉ là bước khởi động; sức mạnh thực sự của đối ngẫu LP nằm ở việc **dùng nó để giải nhanh bài toán, phân tích độ nhạy kinh tế và kiểm định tính tối ưu** trong thực hành. Bộ bài tập thực hành Chương 10 dưới đây tuyển chọn những bài toán kinh điển nhất từ Boyd & Vandenberghe, Bertsimas & Tsitsiklis và Dantzig — trải dài từ lập kế hoạch sản xuất, tối ưu danh mục đầu tư, đến chứng minh tối ưu bằng điều kiện bù.

Điểm đặc biệt giúp bạn giải nhanh bộ bài tập này là kỹ năng **đọc nghiệm đối ngẫu từ nghiệm gốc bằng điều kiện bù (Complementary Slackness)** mà không cần chạy lại thuật toán đơn hình từ đầu. Khung tính tay dưới đây minh họa trọn vẹn kỹ thuật cực kỳ hữu ích ấy chỉ trong vài dòng!

## Bản đồ kiến thức nền: Bốn kỹ năng thực chiến cần dùng trong bộ bài tập thực hành

- **Chuyển đổi dạng hỗn hợp sang bài toán đối ngẫu không sai dấu:** Thành thạo viết bảng đối chiếu giữa 3 loại ràng buộc gốc ($$\le, =, \ge$$) và 3 loại miền biến gốc ($$\ge 0, \text{tự do}, \le 0$$) sang bài toán đối ngẫu.
- **Kiểm định tối ưu bằng chứng chỉ cặp Primal–Dual:** Để chứng minh $$x^*$$ là tối ưu, chỉ cần tìm một điểm đối ngẫu khả thi $$u^*$$ sao cho $$c^T x^* = b^T u^*$$ — phương pháp ngắn gọn và thuyết phục tuyệt đối.
- **Khai thác hệ phương trình điều kiện bù (Complementary Slackness):** Tại nghiệm tối ưu, $$u_i^*(a_i^T x^* - b_i) = 0$$ và $$x_j^*(c_j - (A^T u^*)_j) = 0$$. Khi biết các biến gốc dương và ràng buộc gốc chặt, hệ bất đẳng thức đối ngẫu thu gọn thành một **hệ phương trình tuyến tính** giải ra ngay $$u^*$$!
- **Phân tích độ nhạy (Sensitivity Analysis):** Dùng nghiệm đối ngẫu $$u^*$$ để trả lời các câu hỏi kinh doanh như *"Nên mua thêm bao nhiêu nguyên liệu với giá tối đa bao nhiêu?"* hay *"Nên mở thêm sản phẩm mới không?"*

### Khung giải thích (nên đọc chậm): Dùng điều kiện bù để tìm nhanh giá bóng $$u^*$$ từ nghiệm gốc

Giả sử trong bài toán lập kế hoạch sản xuất:
$$\max_{x_1, x_2 \ge 0} \; 5x_1 + 4x_2 \quad \text{s.t.} \quad \begin{cases} x_1 + x_2 \le 6 & (\text{nguyên liệu A, giá bóng } u_1 \ge 0) \\ 2x_1 + x_2 \le 10 & (\text{giờ máy B, giá bóng } u_2 \ge 0) \\ x_2 \le 5 & (\text{hạn mức thị trường, giá bóng } u_3 \ge 0) \end{cases}$$
Bạn đã tìm ra nghiệm gốc tối ưu là $$x^* = (4, 2)$$ với lợi nhuận $$5(4) + 4(2) = 28$$. Hãy tìm nhanh $$u^* = (u_1^*, u_2^*, u_3^*)$$ mà không cần giải lại LP đối ngẫu!

1. **Kiểm tra độ chặt của các ràng buộc gốc tại $$x^* = (4, 2)$$:**
   - Ràng buộc 1: $$4 + 2 = 6$$ (**chặt**).
   - Ràng buộc 2: $$2(4) + 2 = 10$$ (**chặt**).
   - Ràng buộc 3: $$x_2^* = 2 < 5$$ (**lỏng**, dư 3 đơn vị) $$\implies$$ theo điều kiện bù, chắc chắn $$u_3^* = 0$$!
2. **Dùng điều kiện bù cho các biến gốc dương ($$x_1^* = 4 > 0, x_2^* = 2 > 0$$):**
   Hai ràng buộc đối ngẫu tương ứng phải trở thành **đẳng thức**:
   $$\begin{cases} u_1^* + 2u_2^* = 5 \\ u_1^* + u_2^* + u_3^* = 4 \end{cases}$$
   Thay $$u_3^* = 0$$ vào hệ, trừ vế theo vế ta được ngay: $$u_2^* = 1$$ và $$u_1^* = 3$$ (cả hai đều $$\ge 0$$!).
3. **Kiểm chứng đối ngẫu mạnh:**
   Giá trị hàm mục tiêu đối ngẫu: $$6 u_1^* + 10 u_2^* + 5 u_3^* = 6(3) + 10(1) + 5(0) = 28 = p^*$$!
   Ý nghĩa kinh tế đọc ngay ra được: mỗi đơn vị nguyên liệu A tăng thêm mang lại $$3$$ đơn vị lợi nhuận, mỗi giờ máy B thêm mang lại $$1$$ đơn vị, còn tăng hạn mức thị trường $$x_2 \le 5$$ chẳng tăng thêm đồng nào ($$u_3^* = 0$$)!

Các bài tập dưới đây được tham khảo từ Boyd & Vandenberghe (2004), Bertsimas & Tsitsiklis (1997) và Dantzig (1963), giúp rèn luyện các kỹ năng xây dựng và vận dụng tính đối ngẫu trong quy hoạch tuyến tính (LP).

---

## Phần I: Xây dựng bài toán đối ngẫu

### Bài tập 1: Các dạng LP cơ bản (Boyd & Vandenberghe, Ex. 5.1)

Với các bài toán LP sau, hãy lập bài toán đối ngẫu và nêu ý nghĩa của các biến đối ngẫu.

**a) Dạng chuẩn:**

$$
\begin{align}
\min_{x} \quad & 3x_1 + 5x_2 + 2x_3 \\
\text{s.t.} \quad & x_1 + 2x_2 + x_3 = 4 \\
& 2x_1 + x_2 + 3x_3 = 5 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**b) Dạng bất đẳng thức:**

$$
\begin{align}
\min_{x} \quad & 2x_1 + 4x_2 \\
\text{s.t.} \quad & x_1 + x_2 \geq 3 \\
& 2x_1 + x_2 \geq 5 \\
& x_1, x_2 \geq 0
\end{align}
$$

**c) Dạng hỗn hợp:**

$$
\begin{align}
\min_{x} \quad & x_1 + 2x_2 + 3x_3 \\
\text{s.t.} \quad & x_1 + x_2 = 2 \\
& x_2 + x_3 \leq 3 \\
& x_1 + x_3 \geq 1 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bài a) Dạng chuẩn:**

**Quy tắc:** Với bài toán cực tiểu hóa có ràng buộc đẳng thức và biến không âm ($$x \geq 0$$):
- Mỗi ràng buộc đẳng thức ứng với một biến đối ngẫu không ràng buộc dấu.
- Mỗi biến gốc không âm ứng với một ràng buộc đối ngẫu dạng $$\leq$$.

**Bài toán đối ngẫu:**

$$
\begin{align}
\max_{u} \quad & 4u_1 + 5u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 3 \\
& 2u_1 + u_2 \leq 5 \\
& u_1 + 3u_2 \leq 2 \\
& u_1, u_2 \in \mathbb{R}
\end{align}
$$

**Giải thích:**
- $$u_1, u_2$$ là giá bóng (shadow prices) của ràng buộc thứ nhất và thứ hai, cho biết mức thay đổi biên của giá trị tối ưu khi vế phải tăng thêm một đơn vị.
- Hai biến đối ngẫu không ràng buộc dấu vì các ràng buộc gốc là đẳng thức.
- Mỗi biến của bài toán gốc tạo ra một ràng buộc tương ứng trong bài toán đối ngẫu.

---

**Bài b) Dạng bất đẳng thức:**

**Quy tắc:** Với bài toán cực tiểu hóa có ràng buộc $$\geq$$ và biến $$x \geq 0$$:
- Mỗi ràng buộc $$\geq$$ ứng với một biến đối ngẫu $$\geq 0$$.
- Mỗi biến $$x_i \geq 0$$ ứng với một ràng buộc đối ngẫu $$\leq$$.

**Bài toán đối ngẫu:**

$$
\begin{align}
\max_{u} \quad & 3u_1 + 5u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 2 \\
& u_1 + u_2 \leq 4 \\
& u_1, u_2 \geq 0
\end{align}
$$

---

**Bài c) Dạng hỗn hợp:**

**Phân tích:**
- Ràng buộc 1 ($$=$$): biến đối ngẫu $$u_1 \in \mathbb{R}$$.
- Ràng buộc 2 ($$\leq$$): biến đối ngẫu $$u_2 \leq 0$$.
- Ràng buộc 3 ($$\geq$$): biến đối ngẫu $$u_3 \geq 0$$.

**Bài toán đối ngẫu:**

$$
\begin{align}
\max_{u} \quad & 2u_1 + 3u_2 + u_3 \\
\text{s.t.} \quad & u_1 + u_3 \leq 1 \\
& u_1 + u_2 \leq 2 \\
& u_2 + u_3 \leq 3 \\
& u_1 \in \mathbb{R}, \quad u_2 \leq 0, \quad u_3 \geq 0
\end{align}
$$

</details>

---

### Bài tập 2: Lập kế hoạch sản xuất (Boyd & Vandenberghe, Ex. 5.2)

Một xí nghiệp sản xuất 2 sản phẩm A và B với các thông số sau:

| Sản phẩm | Lợi nhuận (nghìn đồng) | Lao động (giờ) | Máy móc (giờ) |
|----------|------------------------|----------------|---------------|
| A        | 40                     | 2              | 1             |
| B        | 30                     | 1              | 2             |

Nguồn lực hiện có: 100 giờ lao động và 80 giờ máy móc.

**Yêu cầu:**
a) Lập bài toán LP cực đại hóa lợi nhuận.
b) Xây dựng bài toán đối ngẫu.
c) Giải thích ý nghĩa kinh tế của các biến đối ngẫu.
d) Nếu có thêm 1 giờ lao động, lợi nhuận tăng thêm tối đa bao nhiêu?

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Bài toán gốc:**

Đặt $$x_1, x_2$$ lần lượt là số lượng sản phẩm A và B cần sản xuất:

$$
\begin{align}
\max_{x} \quad & 40x_1 + 30x_2 \\
\text{s.t.} \quad & 2x_1 + x_2 \leq 100 \quad \text{(Lao động)} \\
& x_1 + 2x_2 \leq 80 \quad \text{(Máy móc)} \\
& x_1, x_2 \geq 0
\end{align}
$$

**b) Bài toán đối ngẫu:**

Chuyển về dạng cực tiểu hóa $$\min -40x_1 - 30x_2$$ rồi lập đối ngẫu, ta thu được:

$$
\begin{align}
\min_{u} \quad & 100u_1 + 80u_2 \\
\text{s.t.} \quad & 2u_1 + u_2 \geq 40 \\
& u_1 + 2u_2 \geq 30 \\
& u_1, u_2 \geq 0
\end{align}
$$

**c) Ý nghĩa kinh tế:**

- $$u_1$$: **Giá bóng của lao động** — mức tăng lợi nhuận biên khi có thêm 1 giờ lao động.
- $$u_2$$: **Giá bóng của máy móc** — mức tăng lợi nhuận biên khi có thêm 1 giờ máy móc.

Các ràng buộc đối ngẫu có nghĩa là tổng giá trị nguồn lực dùng để sản xuất mỗi đơn vị sản phẩm A ($$2u_1 + u_2$$) phải lớn hơn hoặc bằng lợi nhuận của sản phẩm A (40), và tương tự cho sản phẩm B ($$u_1 + 2u_2 \geq 30$$).

**d) Mức tăng lợi nhuận khi có thêm 1 giờ lao động:**

Giải hệ hai ràng buộc đối ngẫu chặt $$2u_1 + u_2 = 40$$ và $$u_1 + 2u_2 = 30$$, ta được $$u_1^* = 50/3 \approx 16.67$$ và $$u_2^* = 20/3 \approx 6.67$$ nghìn đồng/giờ. Kiểm tra lại: nghiệm gốc $$x^* = (40, 20)$$ cho giá trị $$40 \cdot 40 + 30 \cdot 20 = 2200$$, bằng giá trị đối ngẫu $$100 \cdot \frac{50}{3} + 80 \cdot \frac{20}{3} = 2200$$ ✓.

Do đó, thêm 1 giờ lao động giúp lợi nhuận tăng tối đa $$50/3 \approx 16.67$$ nghìn đồng.

</details>

---

### Bài tập 3: Tối ưu danh mục đầu tư (Boyd & Vandenberghe, Ex. 5.3)

Một nhà đầu tư có 1000 triệu đồng muốn phân bổ vào 3 loại tài sản với các thông số sau:

| Tài sản | Lợi nhuận (%) | Rủi ro (độ lệch chuẩn) |
|---------|---------------|-------------------------|
| Cổ phiếu| 15            | 20                      |
| Trái phiếu| 8           | 5                       |
| Tiền mặt| 3             | 0                       |

Yêu cầu: lợi nhuận đạt ít nhất 10% và tổng rủi ro không vượt quá 12%.

**Yêu cầu:**
a) Lập bài toán LP cực tiểu hóa rủi ro.
b) Xây dựng bài toán đối ngẫu.
c) Giải thích ý nghĩa của các biến đối ngẫu.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Bài toán gốc:**

Đặt $$x_1, x_2, x_3$$ là tỷ trọng đầu tư vào cổ phiếu, trái phiếu và tiền mặt:

$$
\begin{align}
\min_{x} \quad & 20x_1 + 5x_2 \\
\text{s.t.} \quad & x_1 + x_2 + x_3 = 1 \quad \text{(Tổng vốn)} \\
& 15x_1 + 8x_2 + 3x_3 \geq 10 \quad \text{(Lợi nhuận)} \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**b) Bài toán đối ngẫu:**

$$
\begin{align}
\max_{u} \quad & u_1 + 10u_2 \\
\text{s.t.} \quad & u_1 + 15u_2 \leq 20 \\
& u_1 + 8u_2 \leq 5 \\
& u_1 + 3u_2 \leq 0 \\
& u_1 \in \mathbb{R}, \quad u_2 \geq 0
\end{align}
$$

**c) Ý nghĩa và nghiệm:**

- $$u_1$$: giá trị biên của ràng buộc tổng vốn (độ nhạy của rủi ro tối ưu khi thay đổi vế phải ràng buộc tổng tỷ trọng).
- $$u_2$$: giá trị biên của ràng buộc lợi nhuận, phản ánh sự đánh đổi giữa yêu cầu lợi nhuận và mức rủi ro.

**Nghiệm:** Danh mục tối ưu chỉ phân bổ vào cổ phiếu và trái phiếu: $$15x_1 + 8(1 - x_1) = 10 \Rightarrow x_1 = 2/7$$, nên $$x^* = (2/7, 5/7, 0)$$ với mức rủi ro $$20(2/7) + 5(5/7) = 65/7 \approx 9.29\% \leq 12\%$$ ✓ (ràng buộc trần rủi ro 12% không chặt). Nghiệm đối ngẫu là $$u_1^* = -85/7$$, $$u_2^* = 15/7 \approx 2.14$$ (giá trị đối ngẫu $$-85/7 + 150/7 = 65/7$$ ✓), cho thấy khi tăng yêu cầu lợi nhuận thêm 1 điểm phần trăm, rủi ro tối ưu tăng khoảng 2,14 điểm phần trăm.

</details>

---

## Phần II: Tính đối ngẫu yếu và đối ngẫu mạnh

### Bài tập 4: Đối ngẫu yếu (Boyd & Vandenberghe, Ex. 5.5)

Cho bài toán:

$$
\begin{align}
\text{(P)} \quad \min_{x} \quad & 2x_1 + 3x_2 \\
\text{s.t.} \quad & x_1 + x_2 \geq 4 \\
& 2x_1 + x_2 \geq 6 \\
& x_1, x_2 \geq 0
\end{align}
$$

**a)** Xây dựng bài toán đối ngẫu (D).
**b)** Cho $$x = (3, 1)$$. Kiểm tra tính khả thi của $$x$$ và tìm một nghiệm khả thi $$u$$ của (D).
**c)** Kiểm chứng bất đẳng thức đối ngẫu yếu $$c^T x \geq b^T u$$.
**d)** Chứng minh $$x^* = (4, 0)$$ là nghiệm tối ưu.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Bài toán đối ngẫu:**

$$
\begin{align}
\text{(D)} \quad \max_{u} \quad & 4u_1 + 6u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 2 \\
& u_1 + u_2 \leq 3 \\
& u_1, u_2 \geq 0
\end{align}
$$

**b) Kiểm tra $$x = (3, 1)$$:**

Tính khả thi gốc:
- $$3 + 1 = 4 \geq 4$$ ✓
- $$2(3) + 1 = 7 \geq 6$$ ✓
- $$x \geq 0$$ ✓

Giá trị mục tiêu gốc: $$f(x) = 2(3) + 3(1) = 9$$.

Chọn nghiệm đối ngẫu khả thi $$u = (0, 1)$$:
- $$0 + 2(1) = 2 \leq 2$$ ✓
- $$0 + 1 = 1 \leq 3$$ ✓
- Giá trị mục tiêu đối ngẫu: $$g(u) = 4(0) + 6(1) = 6$$.

**c) Kiểm chứng đối ngẫu yếu:**

$$
c^Tx = 9 \geq 6 = b^Tu
$$

Bất đẳng thức đối ngẫu yếu được thỏa mãn ✓.

**d) Chứng minh $$x^* = (4, 0)$$ tối ưu:**

Kiểm tra tính khả thi gốc:
- $$4 + 0 = 4 \geq 4$$ ✓ (ràng buộc chặt)
- $$2(4) + 0 = 8 \geq 6$$ ✓ (ràng buộc lỏng, độ dư bằng 2)

Giá trị mục tiêu gốc: $$f(x^*) = 2(4) + 3(0) = 8$$.

Tìm $$u^*$$ theo điều kiện bù: vì ràng buộc gốc thứ hai lỏng nên $$u_2^* = 0$$; vì $$x_1^* > 0$$ nên ràng buộc đối ngẫu thứ nhất chặt: $$u_1^* + 2u_2^* = 2 \Rightarrow u_1^* = 2$$.

Kiểm tra tính khả thi đối ngẫu: $$u_1^* + u_2^* = 2 \leq 3$$ ✓ (lỏng, khớp với $$x_2^* = 0$$). Giá trị mục tiêu đối ngẫu: $$g(u^*) = 4(2) + 6(0) = 8 = f(x^*)$$ ✓.

**Kết luận:** Theo đối ngẫu yếu, mọi $$x$$ khả thi đều thỏa $$f(x) \geq g(u^*) = 8$$, do đó $$x^* = (4, 0)$$ là nghiệm tối ưu. Lưu ý rằng điểm $$(2, 2)$$ khả thi nhưng cho $$f = 10 > 8$$, còn $$x = (3, 1)$$ cho $$f = 9$$.

</details>

---

### Bài tập 5: Đối ngẫu mạnh (Boyd & Vandenberghe, Ex. 5.6)

Cho bài toán:

$$
\begin{align}
\text{(P)} \quad \min_{x} \quad & x_1 + 2x_2 + x_3 \\
\text{s.t.} \quad & x_1 + x_2 = 3 \\
& x_2 + x_3 = 2 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**a)** Tìm nghiệm tối ưu bằng phương pháp đại số.
**b)** Xây dựng và giải bài toán đối ngẫu.
**c)** Tính khoảng cách đối ngẫu.
**d)** Giải thích vì sao tính đối ngẫu mạnh đúng trong trường hợp này.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Giải bài toán gốc:**

Từ hai ràng buộc đẳng thức, ta có $$x_1 = 3 - x_2$$ và $$x_3 = 2 - x_2$$. Thế vào hàm mục tiêu:

$$
f = (3 - x_2) + 2x_2 + (2 - x_2) = 5
$$

Hàm mục tiêu có giá trị không đổi bằng $$5$$ trên toàn bộ tập khả thi, nên giá trị tối ưu là $$f^* = 5$$. Điều kiện không âm của các biến cho $$0 \leq x_2 \leq 2$$; chẳng hạn $$x^* = (2, 1, 1)$$ là một nghiệm tối ưu.

**b) Bài toán đối ngẫu:**

$$
\begin{align}
\max_{u} \quad & 3u_1 + 2u_2 \\
\text{s.t.} \quad & u_1 \leq 1 \\
& u_1 + u_2 \leq 2 \\
& u_2 \leq 1 \\
& u_1, u_2 \in \mathbb{R}
\end{align}
$$

Để cực đại hóa $$3u_1 + 2u_2$$, chọn $$u_1 = 1$$ và $$u_2 = 1$$. Kiểm tra các ràng buộc: $$1 \leq 1$$ ✓, $$1 + 1 = 2 \leq 2$$ ✓, $$1 \leq 1$$ ✓. Giá trị tối ưu đối ngẫu: $$g^* = 3(1) + 2(1) = 5$$.

**c) Khoảng cách đối ngẫu:**

$$
\text{Gap} = f^* - g^* = 5 - 5 = 0
$$

Tính đối ngẫu mạnh được thỏa mãn ✓.

**d) Giải thích:**

Đối với quy hoạch tuyến tính, tính đối ngẫu mạnh luôn đúng khi một trong hai bài toán có nghiệm tối ưu hữu hạn (khi đó bài toán còn lại cũng có nghiệm tối ưu với cùng giá trị mục tiêu):
- Nếu bài toán gốc không bị chặn thì bài toán đối ngẫu vô nghiệm (và ngược lại).
- Ngoại lệ duy nhất là trường hợp cả hai bài toán đều vô nghiệm.

Với LP khả thi, các ràng buộc đều là hàm affine nên điều kiện Slater dạng mở rộng tự động thỏa mãn.

</details>

---

## Phần III: Điều kiện bù (Complementary Slackness)

### Bài tập 6: Áp dụng điều kiện bù (Bertsimas & Tsitsiklis, Ex. 4.3)

Cho bài toán gốc và ba cặp nghiệm thử:

$$
\begin{align}
\text{(P)} \quad \min_{x} \quad & 3x_1 + 2x_2 \\
\text{s.t.} \quad & x_1 + x_2 \geq 4 \\
& 2x_1 + x_2 \geq 6 \\
& x_1, x_2 \geq 0
\end{align}
$$

**Các cặp nghiệm:**
1. $$x = (2, 2)$$, $$u = (1, 1)$$
2. $$x = (3, 1)$$, $$u = (0, 3/2)$$
3. $$x = (0, 6)$$, $$u = (0, 2)$$

**Yêu cầu:** Kiểm tra cặp nghiệm nào tối ưu bằng điều kiện bù.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bài toán đối ngẫu:**

$$
\begin{align}
\max_{u} \quad & 4u_1 + 6u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 3 \\
& u_1 + u_2 \leq 2 \\
& u_1, u_2 \geq 0
\end{align}
$$

**Hệ điều kiện bù:**
1. $$u_1 \cdot [x_1 + x_2 - 4] = 0$$
2. $$u_2 \cdot [2x_1 + x_2 - 6] = 0$$
3. $$x_1 \cdot [u_1 + 2u_2 - 3] = 0$$
4. $$x_2 \cdot [u_1 + u_2 - 2] = 0$$

---

**Cặp 1: $$x = (2,2)$$, $$u = (1,1)$$**

Tính khả thi gốc:
- $$2 + 2 = 4 \geq 4$$ ✓ (chặt)
- $$4 + 2 = 6 \geq 6$$ ✓ (chặt)

Tính khả thi đối ngẫu:
- $$1 + 2 = 3 \leq 3$$ ✓ (chặt)
- $$1 + 1 = 2 \leq 2$$ ✓ (chặt)

Điều kiện bù:
1. $$1 \cdot 0 = 0$$ ✓
2. $$1 \cdot 0 = 0$$ ✓
3. $$2 \cdot 0 = 0$$ ✓
4. $$2 \cdot 0 = 0$$ ✓

**Kết luận:** Cặp 1 là cặp nghiệm tối ưu ✓. Giá trị mục tiêu: $$f = 3(2) + 2(2) = 10 = 4(1) + 6(1) = g$$ ✓.

---

**Cặp 2: $$x = (3,1)$$, $$u = (0, 3/2)$$**

- Khả thi gốc: $$3 + 1 = 4$$ ✓, $$6 + 1 = 7 > 6$$ (độ dư bằng 1).
- Khả thi đối ngẫu: $$0 + 3 = 3$$ ✓, $$0 + 3/2 = 3/2 \leq 2$$ ✓.
- Điều kiện bù thứ 2: $$u_2 \cdot [7 - 6] = (3/2)(1) = 3/2 \neq 0$$ ✗.

**Kết luận:** Không tối ưu.

---

**Cặp 3: $$x = (0,6)$$, $$u = (0,2)$$**

- Kiểm tra khả thi đối ngẫu: $$0 + 2(2) = 4 \not\leq 3$$ ✗.

**Kết luận:** Nghiệm đối ngẫu không khả thi, nên cặp 3 không tối ưu.

</details>

---

### Bài tập 7: Giá bóng (Bertsimas & Tsitsiklis, Ex. 4.7)

Xét lại bài toán sản xuất ở Bài tập 2 với hàm mục tiêu $$\max 40x_1 + 30x_2$$ và nghiệm tối ưu $$x^* = (40, 20)$$, tại đó hai ràng buộc đều chặt:
- Lao động: $$2(40) + 20 = 100$$
- Máy móc: $$40 + 2(20) = 80$$

**a)** Tính giá bóng của từng nguồn lực.
**b)** Nếu có thể mua thêm 1 giờ lao động với giá 12 nghìn đồng, có nên mua không?
**c)** Phân tích độ nhạy khi quỹ lao động tăng lên 105 giờ.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Tính giá bóng:**

Vì cả hai biến gốc đều dương và cả hai ràng buộc đều chặt, theo điều kiện bù ta có hệ:

$$
\begin{cases}
2u_1 + u_2 = 40 \\
u_1 + 2u_2 = 30
\end{cases}
$$

Giải hệ phương trình:
- Từ phương trình (1): $$u_2 = 40 - 2u_1$$.
- Thế vào phương trình (2): $$u_1 + 2(40 - 2u_1) = 30 \Rightarrow -3u_1 = -50 \Rightarrow u_1^* = 50/3 \approx 16.67$$.
- Suy ra $$u_2^* = 40 - 2(50/3) = 20/3 \approx 6.67$$.

**Giá bóng:**
- Lao động: $$u_1^* = 50/3 \approx 16.67$$ nghìn đồng/giờ.
- Máy móc: $$u_2^* = 20/3 \approx 6.67$$ nghìn đồng/giờ.

**b) Quyết định mua thêm lao động:**

Giá mua là 12 nghìn đồng/giờ, thấp hơn giá trị biên $$u_1^* \approx 16.67$$ nghìn đồng/giờ. Vì $$12 < 16.67$$, doanh nghiệp **nên mua** (lợi nhuận ròng tăng thêm khoảng 4,67 nghìn đồng/giờ).

**c) Phân tích độ nhạy:**

Khi tăng thêm 5 giờ lao động (từ 100 lên 105 giờ, vẫn nằm trong khoảng ổn định cơ sở tối ưu):

$$
\Delta f = u_1^* \times 5 = \frac{50}{3} \times 5 = \frac{250}{3} \approx 83.33 \text{ nghìn đồng}
$$

Lợi nhuận hiện tại là $$40(40) + 30(20) = 2200$$ nghìn đồng, nên lợi nhuận mới đạt khoảng $$2283.33$$ nghìn đồng.

*(Lưu ý: Giá bóng chỉ có hiệu lực trong khoảng độ nhạy mà tập ràng buộc chặt không đổi.)*

</details>

---

## Phần IV: Luồng cực đại và lát cắt cực tiểu

### Bài tập 8: Bài toán luồng cực đại (Bertsimas & Tsitsiklis, Ex. 7.2)

Cho mạng có hướng với dung lượng các cung như sau:

```
    s --10--> a --8--> t
    |        / \       ^
    8      5    3     10
    |    /        \    |
    v  /            \  |
    b ---------------> c
          10
```

**a)** Viết bài toán luồng cực đại dưới dạng LP.
**b)** Tìm một luồng khả thi.
**c)** Tìm một lát cắt và tính dung lượng của nó.
**d)** Kiểm chứng bất đẳng thức: giá trị luồng $$\leq$$ dung lượng lát cắt.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Bài toán LP luồng cực đại:**

Đặt $$f_{ij}$$ là luồng trên cung $$(i, j)$$:

$$
\begin{align}
\max \quad & f_{sa} + f_{sb} \\
\text{s.t.} \quad & f_{sa} - f_{ab} - f_{at} - f_{ac} = 0 \quad \text{(nút a)} \\
& f_{sb} + f_{ab} - f_{bc} = 0 \quad \text{(nút b)} \\
& f_{ac} + f_{bc} - f_{ct} = 0 \quad \text{(nút c)} \\
& 0 \leq f_{sa} \leq 10, \quad 0 \leq f_{sb} \leq 8 \\
& 0 \leq f_{at} \leq 8, \quad 0 \leq f_{ab} \leq 5 \\
& 0 \leq f_{ac} \leq 3, \quad 0 \leq f_{bc} \leq 10 \\
& 0 \leq f_{ct} \leq 10
\end{align}
$$

**b) Luồng khả thi:**

Xét luồng:
- $$f_{sa} = 10$$, $$f_{sb} = 8$$
- $$f_{at} = 8$$, $$f_{ab} = 0$$, $$f_{ac} = 2$$
- $$f_{bc} = 8$$, $$f_{ct} = 10$$

Kiểm tra điều kiện bảo toàn luồng tại các nút trung gian:
- Nút $$a$$: $$10 - 0 - 8 - 2 = 0$$ ✓
- Nút $$b$$: $$8 + 0 - 8 = 0$$ ✓
- Nút $$c$$: $$2 + 8 - 10 = 0$$ ✓

Giá trị luồng: $$|f| = 10 + 8 = 18$$.

**c) Lát cắt:**

Xét lát cắt $$S = \{s\}$$, $$T = \{a, b, c, t\}$$. Các cung đi từ $$S$$ sang $$T$$ gồm:
- $$(s, a)$$ có dung lượng 10
- $$(s, b)$$ có dung lượng 8

Dung lượng lát cắt: $$C(S, T) = 10 + 8 = 18$$.

**d) Kiểm chứng:**

Ta có giá trị luồng bằng $$18$$, đúng bằng dung lượng lát cắt $$C(S, T) = 18$$. Theo định lý luồng cực đại – lát cắt cực tiểu, đây đồng thời là luồng cực đại và lát cắt cực tiểu ✓.

</details>

---

## Phần V: Trò chơi ma trận

### Bài tập 9: Trò chơi tổng bằng không (Dantzig, Ex. 8.1)

Cho ma trận chi trả (tính theo phần thưởng của người chơi hàng):

$$
P = \begin{bmatrix}
3 & -1 & 2 \\
1 & 4 & -2 \\
0 & 2 & 3
\end{bmatrix}
$$

**a)** Kiểm tra xem trò chơi có điểm cân bằng Nash thuần túy hay không.
**b)** Viết bài toán LP tìm chiến lược hỗn hợp tối ưu cho người chơi hàng.
**c)** Viết bài toán LP đối ngẫu cho người chơi cột.
**d)** Giải thích giá trị của trò chơi.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Kiểm tra cân bằng Nash thuần túy:**

Giá trị nhỏ nhất của từng hàng:
- Hàng 1: $$\min\{3, -1, 2\} = -1$$
- Hàng 2: $$\min\{1, 4, -2\} = -2$$
- Hàng 3: $$\min\{0, 2, 3\} = 0$$

Suy ra $$\text{Maxmin} = \max\{-1, -2, 0\} = 0$$ (hàng 3).

Giá trị lớn nhất của từng cột:
- Cột 1: $$\max\{3, 1, 0\} = 3$$
- Cột 2: $$\max\{-1, 4, 2\} = 4$$
- Cột 3: $$\max\{2, -2, 3\} = 3$$

Suy ra $$\text{Minmax} = \min\{3, 4, 3\} = 3$$.

Vì $$\text{Maxmin} \neq \text{Minmax}$$, trò chơi **không có điểm cân bằng Nash thuần túy**.

**b) Bài toán LP cho người chơi hàng:**

Cực đại hóa mức thưởng đảm bảo $$v$$:

$$
\begin{align}
\max_{x, v} \quad & v \\
\text{s.t.} \quad & 3x_1 + x_2 + 0x_3 \geq v \\
& -x_1 + 4x_2 + 2x_3 \geq v \\
& 2x_1 - 2x_2 + 3x_3 \geq v \\
& x_1 + x_2 + x_3 = 1 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**c) Bài toán LP cho người chơi cột:**

Cực tiểu hóa mức lỗ tối đa $$u$$:

$$
\begin{align}
\min_{y, u} \quad & u \\
\text{s.t.} \quad & 3y_1 - y_2 + 2y_3 \leq u \\
& y_1 + 4y_2 - 2y_3 \leq u \\
& 0y_1 + 2y_2 + 3y_3 \leq u \\
& y_1 + y_2 + y_3 = 1 \\
& y_1, y_2, y_3 \geq 0
\end{align}
$$

**d) Giá trị trò chơi:**

Theo định lý minimax của von Neumann:

$$
v^* = \max_x \min_y x^T P y = \min_y \max_x x^T P y
$$

Giá trị $$v^*$$ là mức chi trả tại cân bằng Nash trong chiến lược hỗn hợp.

**Thử nghiệm với chiến lược đều** $$x = y = (1/3, 1/3, 1/3)$$: chi trả kỳ vọng ứng với ba cột lần lượt là $$(1/3)(3 + 1 + 0) = 4/3$$, $$(1/3)(-1 + 4 + 2) = 5/3$$ và $$(1/3)(2 - 2 + 3) = 1$$. Giá trị nhỏ nhất là $$1$$, nên $$v^* \geq 1$$.

**Nghiệm tối ưu (giải LP):** $$x^* = (3/8, 1/4, 3/8)$$, $$y^* = (17/40, 7/20, 9/40)$$, giá trị trò chơi $$v^* = 11/8 = 1.375$$. Kiểm tra: với $$x^*$$, chi trả kỳ vọng theo từng cột đều bằng $$\frac{11}{8}$$ (cột 1: $$\frac{9}{8} + \frac{2}{8}$$; cột 2: $$-\frac{3}{8} + \frac{8}{8} + \frac{6}{8}$$; cột 3: $$\frac{6}{8} - \frac{4}{8} + \frac{9}{8}$$). Ta thấy $$\text{Maxmin} = 0 < v^* = 1.375 < \text{Minmax} = 3$$.

</details>

---

## Phần VI: Bài tập nâng cao từ Boyd & Vandenberghe

### Bài tập 10: Quy hoạch tuyến tính bền vững (Robust LP – Boyd & Vandenberghe, Ex. 5.11)

Xét bài toán LP có hệ số bất định:

$$
\begin{align}
\min_{x} \quad & c^T x \\
\text{s.t.} \quad & a_i^T x \leq b_i, \quad i = 1, \ldots, m \\
& x \geq 0
\end{align}
$$

trong đó mỗi vector $$a_i$$ biến thiên trong ellipsoid $$\{a_i + P_i u : \|u\| \leq 1\}$$.

**Yêu cầu:**
a) Viết dạng tương đương của bài toán bền vững (robust).
b) Chỉ ra đây là một bài toán quy hoạch nón bậc hai (SOCP), không còn là LP thuần túy.
c) Nhận xét về bài toán đối ngẫu.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Dạng tương đương bền vững:**

Ràng buộc bền vững đòi hỏi:

$$
(a_i + P_i u)^T x \leq b_i, \quad \forall \|u\| \leq 1
$$

Điều này tương đương với:

$$
a_i^T x + \max_{\|u\| \leq 1} u^T P_i^T x \leq b_i
$$

Theo bất đẳng thức Cauchy–Schwarz:

$$
\max_{\|u\| \leq 1} u^T P_i^T x = \|P_i^T x\|
$$

Do đó, ràng buộc bền vững trở thành:

$$
a_i^T x + \|P_i^T x\| \leq b_i
$$

**b) Đây là bài toán SOCP:**

Bài toán tương đương có dạng quy hoạch nón bậc hai (Second-Order Cone Program – SOCP):

$$
\begin{align}
\min_{x} \quad & c^T x \\
\text{s.t.} \quad & a_i^T x + \|P_i^T x\| \leq b_i, \quad i = 1, \ldots, m \\
& x \geq 0
\end{align}
$$

Khi $$P_i = 0$$ (không có bất định), bài toán quay về LP thông thường.

**c) Bài toán đối ngẫu:**

Bài toán đối ngẫu được xây dựng theo lý thuyết đối ngẫu của SOCP (có chứa ràng buộc chuẩn Euclide của các biến đối ngẫu) chứ không còn là một LP thuần túy.

</details>

---

### Bài tập 11: Tâm Chebyshev (Boyd & Vandenberghe, Ex. 8.5)

Tìm tâm $$x_c$$ và bán kính $$r$$ lớn nhất sao cho hình cầu Euclide $$\{x : \|x - x_c\| \leq r\}$$ nằm trọn trong đa diện $$\{x : a_i^T x \leq b_i, i = 1, \ldots, m\}$$.

**Yêu cầu:**
a) Lập bài toán tối ưu.
b) Chứng minh đây là một bài toán LP.
c) Giải cho một đa diện cụ thể.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Lập bài toán tối ưu:**

Điều kiện để hình cầu nằm trong đa diện là:

$$
a_i^T x \leq b_i, \quad \forall x : \|x - x_c\| \leq r
$$

Điều này tương đương với:

$$
\max_{\|x - x_c\| \leq r} a_i^T x \leq b_i
$$

$$
a_i^T x_c + r\|a_i\| \leq b_i
$$

Vậy bài toán tìm tâm Chebyshev là:

$$
\begin{align}
\max_{x_c, r} \quad & r \\
\text{s.t.} \quad & a_i^T x_c + r\|a_i\| \leq b_i, \quad i = 1, \ldots, m
\end{align}
$$

**b) Chứng minh là bài toán LP:**

Vì các chuẩn $$\|a_i\|$$ là hằng số đã biết, cả hàm mục tiêu lẫn các ràng buộc đều tuyến tính theo biến $$(x_c, r)$$, nên đây là một bài toán LP.

**c) Ví dụ cụ thể:**

Xét đa diện xác định bởi bốn bất đẳng thức:
- $$x_1 + x_2 \leq 4$$
- $$x_1 - x_2 \leq 2$$
- $$-x_1 + x_2 \leq 2$$
- $$-x_1 - x_2 \leq 2$$

Bài toán LP tương ứng (với $$\|a_i\| = \sqrt{2}$$ cho cả bốn ràng buộc):

$$
\begin{align}
\max \quad & r \\
\text{s.t.} \quad & x_{c1} + x_{c2} + r\sqrt{2} \leq 4 \\
& x_{c1} - x_{c2} + r\sqrt{2} \leq 2 \\
& -x_{c1} + x_{c2} + r\sqrt{2} \leq 2 \\
& -x_{c1} - x_{c2} + r\sqrt{2} \leq 2
\end{align}
$$

Giải bài toán ta thu được $$r\sqrt{2} = 2$$, tức $$r = \sqrt{2} \approx 1.414$$, với tâm $$x_c = (t, t)$$ với $$0 \leq t \leq 1$$ (ví dụ $$x_c = (0, 0)$$); nghiệm không duy nhất vì ràng buộc thứ nhất không chặt. Kiểm tra tại $$x_c = (0, 0)$$: vế trái của 4 ràng buộc đều bằng $$2$$, thỏa mãn $$\leq 4, 2, 2, 2$$ ✓ (ba ràng buộc cuối chặt).

</details>

---

### Bài tập 12: Phân bổ tài nguyên

Một công ty sản xuất 3 sản phẩm A, B, C với các thông số:

| Sản phẩm | Lợi nhuận | Lao động | Máy | Nguyên liệu |
|----------|-----------|----------|-----|-------------|
| A        | 5         | 2        | 1   | 3           |
| B        | 4         | 1        | 2   | 2           |
| C        | 6         | 3        | 2   | 1           |

Nguồn lực hiện có: 100 giờ lao động, 80 giờ máy và 90 kg nguyên liệu. Biết rằng tại phương án tối ưu, cả ba sản phẩm đều được sản xuất và cả ba nguồn lực đều dùng hết.

**a)** Lập bài toán LP gốc và bài toán đối ngẫu.
**b)** Tìm phương án sản xuất tối ưu và giá bóng của từng nguồn lực.
**c)** Có nên mua thêm 10 giờ lao động (giá 1,5 triệu/giờ) hay 10 kg nguyên liệu (giá 1 triệu/kg) không?

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Bài toán LP gốc:**

$$
\begin{align}
\max_{x} \quad & 5x_1 + 4x_2 + 6x_3 \\
\text{s.t.} \quad & 2x_1 + x_2 + 3x_3 \leq 100 \\
& x_1 + 2x_2 + 2x_3 \leq 80 \\
& 3x_1 + 2x_2 + x_3 \leq 90 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**Bài toán đối ngẫu:**

$$
\begin{align}
\min_{u} \quad & 100u_1 + 80u_2 + 90u_3 \\
\text{s.t.} \quad & 2u_1 + u_2 + 3u_3 \geq 5 \\
& u_1 + 2u_2 + 2u_3 \geq 4 \\
& 3u_1 + 2u_2 + u_3 \geq 6 \\
& u_1, u_2, u_3 \geq 0
\end{align}
$$

**b) Phương án tối ưu và giá bóng:**

Vì cả ba ràng buộc nguồn lực đều chặt, $$x^*$$ là nghiệm của hệ $$Ax = b$$:

$$
x^* = \left(\tfrac{160}{11}, \tfrac{150}{11}, \tfrac{210}{11}\right) \approx (14{,}55;\ 13{,}64;\ 19{,}09), \qquad 5x_1 + 4x_2 + 6x_3 = \tfrac{2660}{11} \approx 241{,}82
$$

Kiểm tra ràng buộc lao động: $$2 \cdot 160 + 150 + 3 \cdot 210 = 1100$$, chia cho 11 được 100 ✓.

Vì $$x_1, x_2, x_3 > 0$$, theo điều kiện bù cả ba ràng buộc đối ngẫu đều chặt:

$$
\begin{cases}
2u_1 + u_2 + 3u_3 = 5 \\
u_1 + 2u_2 + 2u_3 = 4 \\
3u_1 + 2u_2 + u_3 = 6
\end{cases}
\quad\Longrightarrow\quad
u^* = \left(\tfrac{14}{11}, \tfrac{9}{11}, \tfrac{6}{11}\right) \approx (1{,}27;\ 0{,}82;\ 0{,}55)
$$

Kiểm tra: $$100u_1 + 80u_2 + 90u_3 = \tfrac{1400 + 720 + 540}{11} = \tfrac{2660}{11}$$, khớp với giá trị tối ưu bài toán gốc ✓ (đối ngẫu mạnh). Mọi $$u_i \ge 0$$ nên $$u^*$$ khả thi.

Ý nghĩa: thêm 1 giờ lao động tăng lợi nhuận khoảng 1,27; thêm 1 giờ máy tăng khoảng 0,82; thêm 1 kg nguyên liệu tăng khoảng 0,55.

**c) Quyết định mua thêm nguồn lực:**

Giá bóng chỉ còn đúng khi cơ sở tối ưu không thay đổi. Với $$A^{-1} = \tfrac{1}{11}\begin{pmatrix} 2 & -5 & 4 \\ -5 & 7 & 1 \\ 4 & 1 & -3 \end{pmatrix}$$:
- Thêm 10 giờ lao động: $$x = A^{-1}(110, 80, 90) = \left(\tfrac{180}{11}, \tfrac{100}{11}, \tfrac{250}{11}\right) > 0$$, cơ sở giữ nguyên.
- Thêm 10 kg nguyên liệu: $$x = A^{-1}(100, 80, 100) = \left(\tfrac{200}{11}, \tfrac{160}{11}, \tfrac{180}{11}\right) > 0$$, cơ sở giữ nguyên.

**Phương án 1 (lao động):** lợi nhuận tăng $$10 \cdot \tfrac{14}{11} \approx 12{,}7$$ triệu, chi phí 15 triệu → **lỗ khoảng 2,3 triệu**.

**Phương án 2 (nguyên liệu):** lợi nhuận tăng $$10 \cdot \tfrac{6}{11} \approx 5{,}5$$ triệu, chi phí 10 triệu → **lỗ khoảng 4,5 triệu**.

**Kết luận:** Giá mua của cả hai nguồn lực đều cao hơn giá bóng tương ứng, nên không nên mua thêm. Nếu bắt buộc phải chọn một trong hai, phương án 1 lỗ ít hơn.

</details>

---

## Tổng kết và chiến lược giải bài tập

### Xây dựng bài toán đối ngẫu
- Xác định rõ dạng bài toán gốc (cực tiểu hay cực đại, loại ràng buộc và dấu biến).
- Áp dụng quy tắc tương ứng gốc – đối ngẫu: số biến đối ngẫu bằng số ràng buộc gốc, và số ràng buộc đối ngẫu bằng số biến gốc.

### Kiểm tra tính tối ưu
- Kiểm tra tính khả thi của cả nghiệm gốc và nghiệm đối ngẫu.
- Kiểm tra điều kiện bù: $$u_i(a_i^T x - b_i) = 0$$.
- Đối chiếu giá trị mục tiêu: $$f^* = g^*$$ (đối ngẫu mạnh).

### Giá bóng (Shadow price)
- Biểu thị giá trị biên của từng nguồn lực.
- Chỉ chính xác trong khoảng độ nhạy mà cơ sở tối ưu không đổi.
- Ràng buộc lỏng (độ dư dương) có giá bóng bằng 0.

### Luồng cực đại – lát cắt cực tiểu
- Kiểm tra điều kiện bảo toàn luồng tại mọi nút trung gian.
- Luôn có giá trị luồng $$\leq$$ dung lượng lát cắt (đối ngẫu yếu).
- Khi dấu bằng xảy ra, cả luồng và lát cắt đều tối ưu (đối ngẫu mạnh).

### Trò chơi ma trận
- Kiểm tra điểm yên ngựa (cân bằng Nash thuần túy) trước.
- Nếu không có, lập bài toán LP để tìm chiến lược hỗn hợp tối ưu.
- Theo định lý minimax của von Neumann: $$\max_x \min_y = \min_y \max_x$$.

---

## Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 5: Duality.

2. **Bertsimas, D., & Tsitsiklis, J. N.** (1997). *Introduction to Linear Optimization*. Athena Scientific. Chapters 4, 7.

3. **Dantzig, G. B.** (1963). *Linear Programming and Extensions*. Princeton University Press. Chapters 5-8.

4. **Luenberger, D. G., & Ye, Y.** (2008). *Linear and Nonlinear Programming* (3rd ed.). Springer.

5. **Vanderbei, R. J.** (2020). *Linear Programming: Foundations and Extensions* (5th ed.). Springer.

---

**Ghi chú:** Các bài tập trên được sắp xếp từ cơ bản đến nâng cao theo các giáo trình chuẩn về quy hoạch tuyến tính và tối ưu lồi.

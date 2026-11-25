---
layout: post
title: "10-06 Tính Chất Đối Ngẫu Kép - Dual của Dual là Primal"
chapter: "10"
order: 7
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter10
redirect_from:
  - /contents/vi/chapter10/10_08_Dual_of_Dual_Property/
---

Trong toán học, có những phép biến đổi "hai lần thì trở về chính mình" — gọi là **phép đối hợp (involution)** — giống như phép lấy đối xứng qua gương, phép nghịch đảo $$1/(1/x) = x$$ hay phép chuyển vị ma trận $$(A^T)^T = A$$. Trong quy hoạch tuyến tính, phép lấy bài toán đối ngẫu cũng sở hữu vẻ đẹp đối xứng tuyệt đối đó: **đối ngẫu của bài toán đối ngẫu chính là bài toán gốc (Dual of Dual = Primal)**!

Tại sao tính chất này lại quan trọng chứ không chỉ là một trò đố đại số? Bởi vì nó biến mọi định lý một chiều thành định lý hai chiều đối xứng hoàn toàn! Chẳng hạn, khi bạn biết "Primal khả thi và bị chặn $$\implies$$ Dual có nghiệm", nhờ tính đối hợp bạn suy ra ngay chiều ngược lại mà không cần chứng minh thêm dòng nào. Và trong thuật toán thực hành (như Dual Simplex), nếu bài toán gốc có ít biến nhưng cả triệu ràng buộc, ta chỉ việc giải bài toán đối ngẫu có ít ràng buộc rồi chuyển ngược về nghiệm gốc mà không lo mất thông tin.

## Kiến thức cần nhớ: Ba trụ cột của tính chất đối ngẫu kép trong LP

- **Chuẩn hóa bài toán đối ngẫu về dạng cực tiểu:** Bài toán đối ngẫu sinh ra ở dạng $$\max$$ với ràng buộc $$\le$$ hoặc $$=$$. Để áp dụng lại đúng cùng một quy tắc lấy đối ngẫu, ta đổi $$\max f \leftrightarrow -\min(-f)$$ và đổi chiều mọi ràng buộc $$\ge$$ sang $$\le$$ bằng cách nhân $$-1$$.
- **Phép chuyển vị kép và bảo toàn dấu biến:** Ma trận ràng buộc bị chuyển vị hai lần $$(A^T)^T = A$$ nên cấu trúc hệ số quay lại y nguyên; biến đối ngẫu không âm $$v \ge 0$$ tạo ra ràng buộc bất đẳng thức, rồi bất đẳng thức ấy lại sinh ra biến không âm (hoặc biến tự do tạo ràng buộc đẳng thức rồi đẳng thức lại tạo biến tự do).
- **Đối xứng toàn diện trong bảng phân loại 4 trạng thái LP:** Nhờ tính đối hợp, cặp Primal–Dual chỉ có thể rơi vào 4 tổ hợp hợp lệ: (1) Cả hai tối ưu với $$p^* = d^*$$; (2) Primal không bị chặn và Dual vô nghiệm; (3) Dual không bị chặn và Primal vô nghiệm; (4) Cả hai đều vô nghiệm. (Không bao giờ có chuyện một bên tối ưu hữu hạn mà bên kia vô nghiệm!)

### Giải thích: Thực hiện tay hai lần lấy đối ngẫu trên một LP 2 biến

Xét bài toán gốc **(P)**:
$$\min_{x_1, x_2} \; 2x_1 + 3x_2 \quad \text{s.t.} \quad x_1 + x_2 \ge 4, \quad x_1 \ge 0, \; x_2 \ge 0.$$

1. **Lần 1 — Lấy đối ngẫu của (P) để thu được (D):**
   Nhân ràng buộc $$x_1 + x_2 \ge 4$$ với $$u \ge 0$$ để chặn dưới $$2x_1 + 3x_2$$:
   **(D):** $$\max_u \; 4u \quad \text{s.t.} \quad u \le 2, \quad u \le 3, \quad u \ge 0.$$
2. **Đưa (D) về dạng cực tiểu hóa chuẩn để chuẩn bị lấy đối ngẫu lần 2:**
   $$\min_u \; -4u \quad \text{s.t.} \quad \begin{cases} -u \ge -2 & (\text{biến đối ngẫu } y_1 \ge 0) \\ -u \ge -3 & (\text{biến đối ngẫu } y_2 \ge 0) \\ u \ge 0. \end{cases}$$
3. **Lần 2 — Lấy đối ngẫu của (D) để thu được (DD):**
   Nhân hai ràng buộc với $$y_1, y_2 \ge 0$$ sao cho tổ hợp tuyến tính $$-(y_1 + y_2)u \le -4u$$ (vì $$u \ge 0$$, điều này tương đương $$-y_1 - y_2 \le -4 \iff y_1 + y_2 \ge 4$$):
   - Hàm mục tiêu (vế phải của tổ hợp): $$\max_{y_1, y_2 \ge 0} \; (-2y_1 - 3y_2)$$.
   - Đổi dấu về dạng cực tiểu hóa (nhớ rằng ta đã đảo dấu mục tiêu từ $$\max 4u$$ sang $$\min -4u$$ ở bước 2):
     **(DD):** $$\min_{y_1, y_2 \ge 0} \; 2y_1 + 3y_2 \quad \text{s.t.} \quad y_1 + y_2 \ge 4!$$
   Đổi tên biến $$(y_1, y_2) \to (x_1, x_2)$$, ta thu lại **chính xác 100% bài toán gốc (P)** ban đầu!

Trong quy hoạch tuyến tính (LP), một tính chất cơ bản của phép lấy đối ngẫu là: **đối ngẫu của bài toán đối ngẫu chính là bài toán gốc (primal)**. Tính chất này được gọi là **tính đối hợp (involution)** của phép đối ngẫu, hay thường gọi ngắn gọn là tính chất **dual của dual là primal**.

Tính chất này thể hiện sự đối xứng giữa bài toán gốc và bài toán đối ngẫu trong LP, có vai trò quan trọng trong cả phân tích lý thuyết lẫn thiết kế thuật toán.

---

## Nhắc lại dạng chuẩn của bài toán quy hoạch tuyến tính gốc

Xét một bài toán quy hoạch tuyến tính ở dạng gốc:

$$
\begin{align}
\text{minimize} \quad & c^T x \label{eq:primal-obj} \\
\text{subject to} \quad & A x \geq b, \label{eq:primal-ineq} \\
& x \geq 0, \label{eq:primal-nonneg}
\end{align}
$$

trong đó:

- $$x \in \mathbb{R}^n$$ là vector biến quyết định,
- $$c \in \mathbb{R}^n$$ là vector hệ số hàm mục tiêu,
- $$A \in \mathbb{R}^{m \times n}$$ là ma trận ràng buộc,
- $$b \in \mathbb{R}^m$$ là vector vế phải.

**Lưu ý:** Một bài toán LP có thể được viết dưới nhiều dạng khác nhau (cực đại hóa, ràng buộc đẳng thức, biến tự do...), nhưng luôn có thể quy về dạng trên mà không làm mất tính tổng quát.

### Ví dụ minh họa

Xét bài toán:

$$
\begin{align}
\text{minimize} \quad & 2x_1 + 3x_2 \\
\text{subject to} \quad & x_1 + x_2 \geq 4, \\
& 2x_1 + x_2 \geq 5, \\
& x_1, x_2 \geq 0.
\end{align}
$$

Ở đây:
- $$c = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$$
- $$A = \begin{bmatrix} 1 & 1 \\ 2 & 1 \end{bmatrix}$$
- $$b = \begin{bmatrix} 4 \\ 5 \end{bmatrix}$$

---

## Xây dựng bài toán đối ngẫu

Bài toán đối ngẫu được lập từ bài toán gốc nhằm cung cấp cận dưới cho giá trị tối ưu cũng như thông tin về độ nhạy và điều kiện tối ưu. Với bài toán gốc ở trên, bài toán đối ngẫu tương ứng là:

$$
\begin{align}
\text{maximize} \quad & b^T y \label{eq:dual-obj} \\
\text{subject to} \quad & A^T y \leq c, \label{eq:dual-ineq} \\
& y \geq 0, \label{eq:dual-nonneg}
\end{align}
$$

trong đó $$y \in \mathbb{R}^m$$ là vector biến đối ngẫu.

### Ý nghĩa

- Bài toán đối ngẫu cũng là một bài toán quy hoạch tuyến tính.
- Theo **đối ngẫu yếu** (weak duality), giá trị mục tiêu của mọi nghiệm đối ngẫu khả thi đều là cận dưới của giá trị tối ưu bài toán gốc.
- Khi **đối ngẫu mạnh** (strong duality) thỏa mãn (luôn đúng với LP nếu ít nhất một trong hai bài toán khả thi), giá trị tối ưu của hai bài toán bằng nhau.

### Ví dụ (tiếp theo)

Bài toán đối ngẫu của ví dụ trên là:

$$
\begin{align}
\text{maximize} \quad & 4y_1 + 5y_2 \\
\text{subject to} \quad & y_1 + 2y_2 \leq 2, \\
& y_1 + y_2 \leq 3, \\
& y_1, y_2 \geq 0.
\end{align}
$$

---

## Xây dựng đối ngẫu của bài toán đối ngẫu

Bây giờ, ta coi bài toán đối ngẫu vừa lập như một bài toán gốc mới và áp dụng quy tắc lấy đối ngẫu thêm một lần nữa.

### Bước 1: Đưa bài toán đối ngẫu về dạng cực tiểu hóa

Đổi dấu hàm mục tiêu và nhân hai vế ràng buộc với $$-1$$ để chuyển về dạng chuẩn cực tiểu hóa với ràng buộc $$\geq$$:

$$
\begin{align}
\text{minimize} \quad & -b^T y \\
\text{subject to} \quad & -A^T y \geq -c, \\
& y \geq 0.
\end{align}
$$

### Bước 2: Áp dụng quy tắc lấy đối ngẫu

Áp dụng quy tắc đối ngẫu cho bài toán vừa biến đổi:

- Biến đối ngẫu mới: $$z \in \mathbb{R}^n$$ (cùng số chiều với $$x$$ trong bài toán gốc).
- Hàm mục tiêu mới: cực đại hóa $$(-c)^T z$$, tương đương với cực tiểu hóa $$c^T z$$ sau khi đổi dấu lại.
- Ràng buộc mới: ma trận ràng buộc là $$(-A^T)^T = -A$$, nên ràng buộc là $$-A z \leq -b$$, tương đương với $$A z \geq b$$.
- Điều kiện dấu: $$z \geq 0$$.

### Bước 3: Kết quả

Đối ngẫu của bài toán đối ngẫu là:

$$
\begin{align}
\text{minimize} \quad & c^T z \\
\text{subject to} \quad & A z \geq b, \\
& z \geq 0.
\end{align}
$$

Đây chính là bài toán gốc ban đầu (chỉ khác tên biến $$z$$ thay cho $$x$$).

### Ví dụ (tiếp theo)

Xuất phát từ bài toán đối ngẫu của ví dụ trên:

$$
\text{maximize } 4y_1 + 5y_2 \text{ s.t. } y_1 + 2y_2 \leq 2, \; y_1 + y_2 \leq 3, \; y_1, y_2 \geq 0
$$

Đưa về dạng cực tiểu hóa:

$$
\text{minimize } -4y_1 - 5y_2 \text{ s.t. } -y_1 - 2y_2 \geq -2, \; -y_1 - y_2 \geq -3, \; y_1, y_2 \geq 0
$$

Lấy đối ngẫu (với biến $$z_1, z_2$$), ta được bài toán cực đại hóa $$-2z_1 - 3z_2$$, tức cực tiểu hóa $$2z_1 + 3z_2$$:

$$
\begin{align}
\text{minimize} \quad & 2z_1 + 3z_2 \\
\text{subject to} \quad & z_1 + z_2 \geq 4, \\
& 2z_1 + z_2 \geq 5, \\
& z_1, z_2 \geq 0.
\end{align}
$$

Kết quả quay trở về đúng bài toán gốc ban đầu.

---

## Giải thích toán học

Tính chất đối ngẫu kép bắt nguồn từ tính đối xứng của hàm Lagrangian trong LP.

### 1. Hàm Lagrangian

Hàm Lagrangian của bài toán gốc là:

$$
\mathcal{L}(x, y) = c^T x - y^T (A x - b),
$$

trong đó $$y \geq 0$$ là vector nhân tử Lagrange cho các ràng buộc bất đẳng thức.

### 2. Quan hệ gốc – đối ngẫu

- **Bài toán gốc:** $$\min_{x \geq 0} \sup_{y \geq 0} \mathcal{L}(x, y)$$
- **Bài toán đối ngẫu:** $$\max_{y \geq 0} \inf_{x \geq 0} \mathcal{L}(x, y)$$

Với hàm song tuyến tính (lồi theo $$x$$, lõm theo $$y$$) như Lagrangian của LP, ta có quan hệ min-max:

$$
\min_x \max_y \mathcal{L}(x, y) = \max_y \min_x \mathcal{L}(x, y)
$$

Mỗi lần lấy đối ngẫu tương ứng với một lần hoán đổi vai trò giữa cực tiểu hóa và cực đại hóa; áp dụng hai lần sẽ đưa bài toán về đúng vị trí ban đầu.

### 3. Góc nhìn ma trận

Phép lấy đối ngẫu thực hiện ba thao tác:
- Chuyển vị ma trận ràng buộc: $$A \to A^T$$.
- Đổi chiều bất đẳng thức: $$\geq$$ thành $$\leq$$ (và ngược lại).
- Hoán đổi vai trò giữa $$b$$ và $$c$$.

Khi áp dụng liên tiếp hai lần, $$(A^T)^T = A$$, chiều bất đẳng thức quay về như cũ và cặp $$(b, c)$$ trở lại đúng thứ tự ban đầu.

### 4. Minh họa hình học

Có thể hình dung phép lấy đối ngẫu tương tự như phép lấy đối xứng qua một mặt phẳng: áp dụng một lần cho ảnh đối xứng, áp dụng lần thứ hai quay về đúng điểm xuất phát. Trong toán học, phép biến đổi mà áp dụng hai lần trở về chính nó được gọi là một **phép đối hợp (involution)**.

---

## Ví dụ chi tiết: Bài toán sản xuất

### Bài toán gốc (P)

Một công ty sản xuất hai sản phẩm A và B với lợi nhuận lần lượt là 3 triệu và 5 triệu cho mỗi đơn vị, dưới hai ràng buộc nguồn lực:
- Nguyên liệu: sản phẩm A cần 2 kg/đơn vị, sản phẩm B cần 1 kg/đơn vị; tổng nguồn cung là 8 kg.
- Thời gian: sản phẩm A cần 1 giờ/đơn vị, sản phẩm B cần 2 giờ/đơn vị; tổng quỹ thời gian là 10 giờ.

Bài toán tìm số lượng sản phẩm $$x_1, x_2$$ để cực đại hóa lợi nhuận:

$$
\begin{align}
\text{maximize} \quad & 3x_1 + 5x_2 \\
\text{subject to} \quad & 2x_1 + x_2 \leq 8, \\
& x_1 + 2x_2 \leq 10, \\
& x_1, x_2 \geq 0.
\end{align}
$$

Chuyển về dạng chuẩn cực tiểu hóa:

$$
\begin{align}
\text{minimize} \quad & -3x_1 - 5x_2 \\
\text{subject to} \quad & -2x_1 - x_2 \geq -8, \\
& -x_1 - 2x_2 \geq -10, \\
& x_1, x_2 \geq 0.
\end{align}
$$

### Bài toán đối ngẫu (D)

Về mặt kinh tế, bài toán đối ngẫu tìm **giá bóng (shadow price)** của từng nguồn lực sao cho tổng giá trị nguồn lực là nhỏ nhất, đồng thời tổng giá trị nguồn lực tiêu hao cho mỗi đơn vị sản phẩm không thấp hơn lợi nhuận của sản phẩm đó. Vì (P) là bài toán cực đại hóa với ràng buộc $$\leq$$, bài toán đối ngẫu (D) là bài toán cực tiểu hóa với ràng buộc $$\geq$$:

$$
\begin{align}
\text{minimize} \quad & 8y_1 + 10y_2 \\
\text{subject to} \quad & 2y_1 + y_2 \geq 3, \\
& y_1 + 2y_2 \geq 5, \\
& y_1, y_2 \geq 0.
\end{align}
$$

### Đối ngẫu của bài toán đối ngẫu (DD)

Bài toán (D) đã ở dạng chuẩn (cực tiểu hóa, ràng buộc $$\geq$$, biến không âm) với vector mục tiêu $$(8, 10)$$, ma trận ràng buộc $$\begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$ và vế phải $$(3, 5)$$. Áp dụng quy tắc lấy đối ngẫu với biến mới $$z_1, z_2$$, ta thu được:

$$
\begin{align}
\text{maximize} \quad & 3z_1 + 5z_2 \\
\text{subject to} \quad & 2z_1 + z_2 \leq 8, \\
& z_1 + 2z_2 \leq 10, \\
& z_1, z_2 \geq 0.
\end{align}
$$

Kết quả trùng khớp hoàn toàn với bài toán gốc (P).

**Kiểm tra bằng số:** Bài toán (P) đạt tối ưu tại $$(x_1, x_2) = (2, 4)$$ với lợi nhuận $$3 \cdot 2 + 5 \cdot 4 = 26$$. Bài toán (D) đạt tối ưu tại $$(y_1, y_2) = (\tfrac{1}{3}, \tfrac{7}{3})$$ với giá trị mục tiêu $$8 \cdot \tfrac{1}{3} + 10 \cdot \tfrac{7}{3} = 26$$. Hai giá trị bằng nhau, phù hợp với tính đối ngẫu mạnh.

---

## Mở rộng: Tối ưu lồi tổng quát

Tính chất đối ngẫu kép luôn đúng đối với quy hoạch tuyến tính. Tuy nhiên, trong tối ưu lồi tổng quát, tính chất này chỉ đúng khi thỏa mãn thêm các điều kiện nhất định:
- Bài toán gốc là lồi (và đóng).
- Thỏa mãn điều kiện Slater (hoặc một điều kiện chuẩn hóa ràng buộc tương đương).
- Tính đối ngẫu mạnh được bảo đảm.
- Tính chất này nói chung **không đúng** cho các bài toán không lồi.

Để tìm hiểu chi tiết hơn, xem **Chương 11, Bài 11-07**: "Dual của Dual trong Tối Ưu Convex Tổng Quát", trong đó trình bày các điều kiện cần thiết, so sánh giữa LP và tối ưu lồi tổng quát, ví dụ khi đối ngẫu kép không quay về bài toán gốc và ứng dụng trong thiết kế thuật toán.

---

## Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L. (2004).** *Convex Optimization.* Cambridge University Press.
   - Chapter 5: Duality (đặc biệt Section 5.2 về LP duality)

2. **Bertsimas, D., & Tsitsiklis, J. N. (1997).** *Introduction to Linear Optimization.* Athena Scientific.
   - Chapter 4: Duality Theory

3. **Nesterov, Y. (2018).** *Lectures on Convex Optimization.* Springer.
   - Chapter 3: Duality in Convex Optimization

4. **Dantzig, G. B. (1963).** *Linear Programming and Extensions.* Princeton University Press.
   - Foundational work on LP duality

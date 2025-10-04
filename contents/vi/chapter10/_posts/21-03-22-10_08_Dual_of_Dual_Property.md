---
layout: post
title: "10-08 Tính Chất Đối Ngẫu Kép - Dual của Dual là Primal"
chapter: "10"
order: 9
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter10
---

Trong quy hoạch tuyến tính (Linear Programming), một tính chất toán học đẹp và quan trọng là: **đối ngẫu của bài toán đối ngẫu chính là bài toán gốc (primal)**. Tính chất này được gọi là **"involution" của đối ngẫu** hay **"định lý dual của dual"**.

Đây là một tính chất cơ bản thể hiện tính đối xứng hoàn hảo trong lý thuyết đối ngẫu của LP, và nó có ý nghĩa sâu sắc trong cả lý thuyết lẫn ứng dụng.

---

## Nhắc Lại Dạng Chuẩn của Linear Program (Bài Toán Primal)**

Một bài toán quy hoạch tuyến tính ở dạng primal thường được viết như sau:

$$
\begin{align}
\text{minimize} \quad & c^T x \label{eq:primal-obj} \\
\text{subject to} \quad & A x \geq b, \label{eq:primal-ineq} \\
& x \geq 0, \label{eq:primal-nonneg}
\end{align}
$$

trong đó:

- $$x \in \mathbb{R}^n$$ là vector biến quyết định
- $c \in \mathbb{R}^n$$ là vector hệ số hàm mục tiêu
- $$A \in \mathbb{R}^{m \times n}$$ là ma trận ràng buộc
- $$b \in \mathbb{R}^m$$ là vector vế phải

**Lưu ý:** LP có thể được viết dưới nhiều dạng khác nhau (maximization, equality constraints, v.v.), nhưng chúng ta luôn có thể chuyển đổi về dạng chuẩn này mà không làm mất tính tổng quát.

### **Ví dụ Minh Họa:**

Xét bài toán đơn giản:

$$
\begin{align}
\text{minimize} \quad & 2x_1 + 3x_2 \\
\text{subject to} \quad & x_1 + x_2 \geq 4, \\
& 2x_1 + x_2 \geq 5, \\
& x_1, x_2 \geq 0.
\end{align}
$$

Ở đây:
- $c = \begin{bmatrix} 2 \\ 3 \end{bmatrix}$
- $A = \begin{bmatrix} 1 & 1 \\ 2 & 1 \end{bmatrix}$
- $b = \begin{bmatrix} 4 \\ 5 \end{bmatrix}$

---

## Xây Dựng Bài Toán Đối Ngẫu (Dual Problem)**

Bài toán đối ngẫu được xây dựng từ bài toán primal để cung cấp các chặn và thông tin về tính tối ưu (ví dụ: phân tích độ nhạy, điều kiện tối ưu).

Đối với bài toán primal ở trên, bài toán dual được định nghĩa như sau:

$$
\begin{align}
\text{maximize} \quad & b^T y \label{eq:dual-obj} \\
\text{subject to} \quad & A^T y \leq c, \label{eq:dual-ineq} \\
& y \geq 0, \label{eq:dual-nonneg}
\end{align}
$$

trong đó $y \in \mathbb{R}^m$ là vector biến đối ngẫu.

### **Ý Nghĩa:**

- Bài toán dual cũng là một LP
- Theo **đối ngẫu yếu** (weak duality): giá trị tối ưu của dual cung cấp chặn dưới cho giá trị tối ưu của primal
- Nếu **đối ngẫu mạnh** (strong duality) thỏa mãn (luôn đúng với LP khả thi dưới điều kiện nhẹ như điều kiện Slater), thì giá trị tối ưu của hai bài toán bằng nhau

### **Ví Dụ (Tiếp Theo):**

Dual của bài toán trên là:

$$
\begin{align}
\text{maximize} \quad & 4y_1 + 5y_2 \\
\text{subject to} \quad & y_1 + 2y_2 \leq 2, \\
& y_1 + y_2 \leq 3, \\
& y_1, y_2 \geq 0.
\end{align}
$$

---

## **Bước 3: Xây Dựng Dual của Dual**

Bây giờ, chúng ta sẽ coi bài toán dual vừa xây dựng như một bài toán primal mới, và áp dụng quy tắc đối ngẫu lần nữa.

### **Bước 3.1: Chuyển Dual Về Dạng "Primal-Like"**

Để thuận tiện cho việc áp dụng quy tắc đối ngẫu, ta chuyển bài toán maximization thành minimization bằng cách đổi dấu hàm mục tiêu:

$$
\begin{align}
\text{minimize} \quad & -b^T y \\
\text{subject to} \quad & -A^T y \geq -c, \\
& y \geq 0.
\end{align}
$$

### **Bước 3.2: Áp Dụng Quy Tắc Đối Ngẫu**

Áp dụng quy tắc đối ngẫu cho bài toán này:

- Biến đối ngẫu mới: $z \in \mathbb{R}^n$ (có cùng số chiều với $x$ trong bài toán primal gốc)
- Hàm mục tiêu mới: maximize $(-c)^T z$ (tương đương minimize $c^T z$)
- Ràng buộc mới: từ $-A^T y \geq -c$ và quy tắc đối ngẫu, ta có:
  - Ma trận ràng buộc của dual mới là $(-A^T)^T = -A$
  - Ràng buộc trở thành: $-A z \leq -b$
  - Đơn giản hóa: $A z \geq b$
- Điều kiện không âm: $z \geq 0$

### **Bước 3.3: Kết Quả**

Dual của dual là:

$$
\begin{align}
\text{minimize} \quad & c^T z \\
\text{subject to} \quad & A z \geq b, \\
& z \geq 0.
\end{align}
$$

**Đây chính xác là bài toán primal ban đầu!** (với $z$ chỉ là cách đặt tên khác cho $x$)

### **Ví Dụ (Tiếp Theo):**

Dual của dual cho bài toán ví dụ:

Từ dual:
$$
\text{maximize } 4y_1 + 5y_2 \text{ s.t. } y_1 + 2y_2 \leq 2, \; y_1 + y_2 \leq 3, \; y_1, y_2 \geq 0
$$

Chuyển về dạng minimize:
$$
\text{minimize } -4y_1 - 5y_2 \text{ s.t. } -y_1 - 2y_2 \geq -2, \; -y_1 - y_2 \geq -3, \; y_1, y_2 \geq 0
$$

Dual của nó (với biến $z_1, z_2$):
$$
\begin{align}
\text{minimize} \quad & 2z_1 + 3z_2 \\
\text{subject to} \quad & z_1 + z_2 \geq 4, \\
& 2z_1 + z_2 \geq 5, \\
& z_1, z_2 \geq 0.
\end{align}
$$

**Đúng là bài toán primal ban đầu!**

---

## **Bước 4: Tại Sao Tính Chất Này Đúng? (Giải Thích Toán Học)**

Tính chất này xuất phát từ **tính đối xứng trong công thức Lagrangian** của LP.

### **4.1. Hàm Lagrangian**

Hàm Lagrangian cho bài toán primal là:

$$
\mathcal{L}(x, y) = c^T x - y^T (A x - b),
$$

trong đó $y \geq 0$ là các nhân tử Lagrange cho các bất đẳng thức.

### **4.2. Quan Hệ Primal-Dual**

- **Bài toán primal**: $\min_x \sup_{y \geq 0} \mathcal{L}(x, y)$
- **Bài toán dual**: $\max_{y \geq 0} \inf_{x \geq 0} \mathcal{L}(x, y)$

Định lý min-max (cho hàm convex-concave như Lagrangian tuyến tính này) có tính chất đối xứng:

$$
\min_x \max_y \mathcal{L}(x, y) = \max_y \min_x \mathcal{L}(x, y)
$$

Khi áp dụng đối ngẫu hai lần, ta đổi chỗ min và max hai lần, quay lại vị trí ban đầu.

### **4.3. Góc Nhìn Ma Trận**

Quá trình đối ngẫu hóa bao gồm:
- Chuyển vị ma trận: $A \to A^T$
- Đổi chiều bất đẳng thức: $\geq$ thành $\leq$ (hoặc ngược lại)
- Hoán đổi vai trò của $b$ và $c$

Khi áp dụng hai lần:
- $(A^T)^T = A$ (chuyển vị hai lần trả về ma trận gốc)
- Đổi chiều hai lần trả về chiều ban đầu
- Hoán đổi $(b, c)$ hai lần trả về $(b, c)$

**Kết luận:** Cấu trúc toán học quay về ban đầu!

### **4.4. Minh Họa Hình Học**

Hãy tưởng tượng một phép biến đổi hình học (như phép đối xứng qua một mặt phẳng):
- Áp dụng một lần: ta được ảnh đối xứng
- Áp dụng hai lần: ta quay về vị trí ban đầu

Tính chất "dual của dual là primal" tương tự như vậy - đây là một **involution** (phép biến đổi mà khi áp dụng hai lần sẽ cho kết quả ban đầu).

---

## **Ví Dụ Chi Tiết: Bài Toán Sản Xuất**

### **Bài Toán Primal (P)**

Một công ty sản xuất hai sản phẩm A và B. Lợi nhuận từ mỗi đơn vị A là 3 triệu, từ B là 5 triệu. Có hai nguồn lực giới hạn:
- Nguyên liệu: A cần 2 kg/đơn vị, B cần 1 kg/đơn vị, tổng cộng có 8 kg
- Thời gian: A cần 1 giờ/đơn vị, B cần 2 giờ/đơn vị, tổng cộng có 10 giờ

Tìm số lượng sản phẩm để maximize lợi nhuận.

**Công thức:**

$$
\begin{align}
\text{maximize} \quad & 3x_1 + 5x_2 \\
\text{subject to} \quad & 2x_1 + x_2 \leq 8, \\
& x_1 + 2x_2 \leq 10, \\
& x_1, x_2 \geq 0.
\end{align}
$$

Chuyển về dạng chuẩn (minimize):

$$
\begin{align}
\text{minimize} \quad & -3x_1 - 5x_2 \\
\text{subject to} \quad & -2x_1 - x_2 \geq -8, \\
& -x_1 - 2x_2 \geq -10, \\
& x_1, x_2 \geq 0.
\end{align}
$$

### **Bài Toán Dual (D)**

Dual có ý nghĩa kinh tế: tìm giá của nguồn lực sao cho minimize tổng chi phí, nhưng vẫn đảm bảo chi phí nguồn lực cho mỗi sản phẩm không nhỏ hơn lợi nhuận.

$$
\begin{align}
\text{maximize} \quad & 8y_1 + 10y_2 \\
\text{subject to} \quad & 2y_1 + y_2 \leq 3, \\
& y_1 + 2y_2 \leq 5, \\
& y_1, y_2 \geq 0.
\end{align}
$$

### **Dual của Dual (DD)**

Chuyển dual về dạng minimize:

$$
\begin{align}
\text{minimize} \quad & -8y_1 - 10y_2 \\
\text{subject to} \quad & -2y_1 - y_2 \geq -3, \\
& -y_1 - 2y_2 \geq -5, \\
& y_1, y_2 \geq 0.
\end{align}
$$

Dual của nó (với biến $z_1, z_2$):

$$
\begin{align}
\text{maximize} \quad & 3z_1 + 5z_2 \\
\text{subject to} \quad & 2z_1 + z_2 \leq 8, \\
& z_1 + 2z_2 \leq 10, \\
& z_1, z_2 \geq 0.
\end{align}
$$

**Đây chính xác là bài toán primal (P) ban đầu!**

---

## **Mở Rộng: Tối Ưu Convex Tổng Quát**

Tính chất "dual của dual là primal" đã được chứng minh cho Linear Programming. Vậy tính chất này có còn đúng với bài toán tối ưu convex tổng quát không?

**Kết quả:** Tính chất này **có điều kiện** đối với convex optimization:
- Cần thỏa mãn điều kiện Slater
- Cần strong duality
- **Không đúng** cho bài toán non-convex

**Để tìm hiểu chi tiết**, xem **Chương 11, Bài 11-09**: "Dual của Dual trong Tối Ưu Convex Tổng Quát" - nơi chúng ta phân tích sâu về:
- Điều kiện cần thiết cho tính chất này
- So sánh LP vs Convex Optimization
- Ví dụ khi dual của dual ≠ primal
- Ứng dụng trong thiết kế thuật toán

---

## **Tài Liệu Tham Khảo**

1. **Boyd, S., & Vandenberghe, L. (2004).** *Convex Optimization.* Cambridge University Press.
   - Chapter 5: Duality (đặc biệt Section 5.2 về LP duality)

2. **Bertsimas, D., & Tsitsiklis, J. N. (1997).** *Introduction to Linear Optimization.* Athena Scientific.
   - Chapter 4: Duality Theory

3. **Nesterov, Y. (2018).** *Lectures on Convex Optimization.* Springer.
   - Chapter 3: Duality in Convex Optimization

4. **Dantzig, G. B. (1963).** *Linear Programming and Extensions.* Princeton University Press.
   - Foundational work on LP duality


---
layout: post
title: 05-10 Bài Tập Thực Hành - Các Bài Toán Chuẩn
chapter: '05'
order: 16
owner: GitHub Copilot
lang: vi
categories:
- chapter05
lesson_type: required
redirect_from:
  - /contents/vi/chapter05/05_08_Practical_Exercises_Canonical_Problems/
---

Trên giấy, các bài toán chuẩn LP, QP, QCQP, SOCP, SDP trông giống những khuôn mẫu toán học trừu tượng. Nhưng ngay khi bạn bước vào bộ bài tập thực hành này — từ bài toán lập thực đơn dinh dưỡng tối ưu chi phí (Diet Problem), bài toán phân bổ danh mục đầu tư Markowitz, cho đến thiết kế tối ưu bền vững bằng SOCP — bạn sẽ thấy mỗi lớp bài toán chuẩn chính là một "vũ khí chuyên dụng" giải quyết trực tiếp bài toán thật của thế giới công nghiệp.

Mục tiêu của buổi thực hành này không chỉ là bấm chạy ra con số cuối cùng, mà là rèn kỹ năng **chuyển dịch hai chiều**: từ mô tả bằng lời sang công thức toán học chuẩn, và từ nghiệm số quay ngược lại diễn giải ý nghĩa kinh tế/kỹ thuật của từng biến và ràng buộc tích cực.

## Kiến thức cần nhớ: Bốn kỹ năng thực chiến khi mô hình hóa bài toán chuẩn

Khi tự tay giải các bài tập trong bộ này (bằng tay hoặc bằng CVXPY/Python), hãy kiểm tra bốn tiêu chí sau:

- **Định nghĩa biến quyết định & Đơn vị rõ ràng:** Mọi sai sót mô hình hóa thường bắt nguồn từ việc trộn lẫn đơn vị (ví dụ lợi nhuận theo % năm nhưng rủi ro theo phương sai ngày, hoặc quên điều kiện không âm $$x \ge 0$$).
- **Chọn đúng lớp chuẩn & Kiểm tra ma trận $$Q \succeq 0$$:** Trước khi nạp ma trận hiệp phương sai $$\Sigma$$ vào QP, luôn kiểm tra tính đối xứng và trị riêng không âm (tránh lỗi số học nhỏ như $$\lambda_{\min} = -10^{-16}$$).
- **Kỹ thuật Epigraph & Biến phụ để tuyến tính hóa:** Biết cách chuyển $$\min \|x\|_1$$ thành $$\min \mathbf{1}^T t \text{ s.t. } -t \le x \le t$$ (LP) và chuyển ràng buộc bất định ellipsoid thành chuẩn $$\ell_2$$ (SOCP).
- **Hậu kiểm nghiệm (Sanity Check):** Luôn kiểm tra lại ba thứ sau khi giải: (1) nghiệm có thỏa mọi ràng buộc với dung sai $$10^{-6}$$ không? (2) ràng buộc nào tích cực? (3) kết quả có hợp lý về mặt vật lý/kinh tế không?

### Giải thích: Giải tay một bài toán Khẩu phần ăn (Diet Problem) 2 thực phẩm

Một người cần ít nhất $$10$$ đơn vị protein và $$12$$ đơn vị vitamin mỗi ngày từ 2 loại thực phẩm:
- Thực phẩm A: giá $$2$$ USD/phần, chứa $$2$$ protein và $$1$$ vitamin.
- Thực phẩm B: giá $$3$$ USD/phần, chứa $$1$$ protein và $$3$$ vitamin.

1. **Bước 1 — Lập mô hình LP:** Gọi $$x_1, x_2 \ge 0$$ là số phần A và B.
   $$\min_{x_1, x_2 \ge 0} \; 2x_1 + 3x_2 \quad \text{s.t.} \quad \begin{cases} 2x_1 + x_2 \ge 10 \\ x_1 + 3x_2 \ge 12 \end{cases}$$
2. **Bước 2 — Xác định các đỉnh của vùng khả thi (không bị chặn phía trên):**
   - Giao $$2x_1 + x_2 = 10$$ và $$x_1 = 0$$: $$(0, 10)$$ — kiểm tra $$0 + 30 = 30 \ge 12$$ (khả thi), chi phí $$= 30$$ USD.
   - Giao $$x_1 + 3x_2 = 12$$ và $$x_2 = 0$$: $$(12, 0)$$ — kiểm tra $$24 + 0 = 24 \ge 10$$ (khả thi), chi phí $$= 24$$ USD.
   - Giao hai đường thẳng $$2x_1 + x_2 = 10$$ và $$x_1 + 3x_2 = 12$$:
     Nhân phương trình 2 với 2: $$2x_1 + 6x_2 = 24$$. Trừ phương trình 1: $$5x_2 = 14 \implies x_2^\star = 2.8$$, suy ra $$x_1^\star = 12 - 3(2.8) = 3.6$$.
3. **Bước 3 — Tính chi phí tối ưu và hậu kiểm:**
   - Chi phí tại $$(3.6, 2.8)$$: $$2(3.6) + 3(2.8) = 7.2 + 8.4 = 15.6$$ USD (thấp hơn hẳn 24 USD và 30 USD!).
   - Hậu kiểm dinh dưỡng: Protein $$= 2(3.6) + 2.8 = 10$$ (đạt đúng ngưỡng), Vitamin $$= 3.6 + 3(2.8) = 12$$ (đạt đúng ngưỡng). Cả hai ràng buộc đều tích cực!

---

# Bài Tập Thực Hành - Các Bài Toán Chuẩn

Các bài tập dưới đây được tham khảo từ Boyd & Vandenberghe (2004) và Ben-Tal & Nemirovski (2001).

---

## 📝 **Phần I: Quy hoạch Tuyến tính (LP)**

### **Bài tập 1: Bài toán Khẩu phần ăn (Diet Problem)**

Một người cần lập kế hoạch dinh dưỡng với 3 loại thực phẩm:
- Thực phẩm 1: 2 đơn vị protein, 1 đơn vị tinh bột (carbs), giá 3 USD.
- Thực phẩm 2: 1 đơn vị protein, 2 đơn vị carbs, giá 2 USD.
- Thực phẩm 3: 1 đơn vị protein, 1 đơn vị carbs, giá 1.5 USD.

Yêu cầu tối thiểu mỗi ngày: 5 đơn vị protein và 6 đơn vị carbs.

**Yêu cầu:**  
a) Phát biểu bài toán LP cực tiểu hóa chi phí.  
b) Tìm nghiệm tối ưu.  
c) Giải thích ý nghĩa của các biến đối ngẫu (giá bóng – shadow prices).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Mô hình hóa bài toán:**

Đặt $$x_i$$ là lượng thực phẩm thứ $$i$$ ($$i = 1, 2, 3$$):

$$
\begin{align}
\min_{x} \quad & 3x_1 + 2x_2 + 1.5x_3 \\
\text{s.t.} \quad & 2x_1 + x_2 + x_3 \geq 5 \quad \text{(protein)} \\
& x_1 + 2x_2 + x_3 \geq 6 \quad \text{(carbs)} \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**Viết dưới dạng bất đẳng thức $$\leq$$:**

$$
\begin{align}
\min_{x} \quad & 3x_1 + 2x_2 + 1.5x_3 \\
\text{s.t.} \quad & -2x_1 - x_2 - x_3 \leq -5 \\
& -x_1 - 2x_2 - x_3 \leq -6 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

---

**b) Tìm nghiệm tối ưu:**

Thực phẩm 3 có đơn giá thấp nhất trên mỗi đơn vị dinh dưỡng, nên nghiệm tối ưu ưu tiên sử dụng nhiều thực phẩm 3. Xét đỉnh $$x = (0, 1, 4)$$ (cả hai ràng buộc đều chặt và $$x_1 = 0$$):

$$\text{Protein: } 0 + 1 + 4 = 5 \text{ ✓}, \qquad \text{Carbs: } 0 + 2 + 4 = 6 \text{ ✓}$$

Chi phí: $$3 \cdot 0 + 2 \cdot 1 + 1.5 \cdot 4 = 8$$ USD.

Tính tối ưu được xác nhận bằng bài toán đối ngẫu ở phần c): tồn tại nghiệm đối ngẫu khả thi $$\lambda$$ có giá trị mục tiêu bằng 8.

**Nghiệm tối ưu:** $$x^* = (0, 1, 4)$$, chi phí tối thiểu = 8 USD.

(Lưu ý: đỉnh $$x_3 = 0$$ cho $$x = \left(\frac{4}{3}, \frac{7}{3}, 0\right)$$ cũng khả thi nhưng có chi phí $$\frac{26}{3} \approx 8.67 > 8$$ nên không tối ưu.)

---

**c) Biến đối ngẫu (Giá bóng – Shadow prices):**

Bài toán đối ngẫu:

$$
\max_{\lambda} \quad 5\lambda_1 + 6\lambda_2 \quad \text{s.t.} \quad A^T\lambda \leq c, \; \lambda \geq 0
$$

cụ thể là $$2\lambda_1 + \lambda_2 \leq 3$$, $$\lambda_1 + 2\lambda_2 \leq 2$$, và $$\lambda_1 + \lambda_2 \leq 1.5$$.

Xét $$\lambda^* = \left(1, \frac{1}{2}\right)$$ (suy ra từ điều kiện bù lỏng vì $$x_2^*, x_3^* > 0$$ nên ràng buộc đối ngẫu thứ 2 và thứ 3 phải chặt): ràng buộc thứ nhất cho $$2 + 0.5 = 2.5 < 3$$ (không chặt, khớp với $$x_1^* = 0$$), và giá trị đối ngẫu $$5(1) + 6(0.5) = 8$$ bằng đúng giá trị gốc, xác nhận nghiệm tối ưu theo đối ngẫu mạnh.

**Ý nghĩa kinh tế:**
- $$\lambda_1^* = 1$$: tăng yêu cầu protein thêm 1 đơn vị làm chi phí tối thiểu tăng thêm 1 USD.
- $$\lambda_2^* = \frac{1}{2}$$: tăng yêu cầu carbs thêm 1 đơn vị làm chi phí tối thiểu tăng thêm 0.5 USD.

Trong cấu trúc giá này, chi phí cận biên của protein cao gấp đôi carbs.

</details>

---

## 📝 **Phần II: Quy hoạch Bậc hai (QP)**

### **Bài tập 2: Tối ưu hóa Danh mục Đầu tư**

Xét đầu tư vào 2 tài sản với:
- Lợi suất kỳ vọng: $$\mu = (0.12, 0.10)^T$$
- Ma trận hiệp phương sai: $$\Sigma = \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{bmatrix}$$

**Yêu cầu:**  
a) Viết bài toán cực tiểu hóa rủi ro với lợi suất mục tiêu $$r = 0.11$$.  
b) Tìm danh mục tối ưu.  
c) Xác định biên hiệu quả (efficient frontier).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Mô hình hóa bài toán:**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2} x^T \Sigma x \\
\text{s.t.} \quad & \mu^T x = r \\
& \mathbf{1}^T x = 1 \\
& x \geq 0
\end{align}
$$

Với $$r = 0.11$$:

$$
\begin{align}
\min_{x} \quad & \frac{1}{2}(0.04x_1^2 + 0.02x_1x_2 + 0.09x_2^2) \\
\text{s.t.} \quad & 0.12x_1 + 0.10x_2 = 0.11 \\
& x_1 + x_2 = 1 \\
& x_1, x_2 \geq 0
\end{align}
$$

---

**b) Tìm nghiệm:**

Từ hệ hai phương trình ràng buộc $$x_1 + x_2 = 1$$ và $$0.12x_1 + 0.10x_2 = 0.11$$:

$$0.12x_1 + 0.10(1-x_1) = 0.11 \Rightarrow 0.02x_1 = 0.01 \Rightarrow x_1 = 0.5, \quad x_2 = 0.5$$

**Nghiệm:** $$x^* = (0.5, 0.5)^T$$.

**Kiểm tra tính khả thi:** $$0.5 + 0.5 = 1$$ ✓, $$0.12(0.5) + 0.10(0.5) = 0.11$$ ✓.

**Phương sai (rủi ro):**

$$\sigma^2 = x^{*T} \Sigma x^* = \begin{bmatrix} 0.5 & 0.5 \end{bmatrix} \begin{bmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{bmatrix} \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix} = \begin{bmatrix} 0.5 & 0.5 \end{bmatrix} \begin{bmatrix} 0.025 \\ 0.05 \end{bmatrix} = 0.0375$$

**Độ lệch chuẩn:** $$\sigma = \sqrt{0.0375} \approx 0.194 = 19.4\%$$.

---

**c) Biên hiệu quả (Efficient frontier):**

Cho $$r$$ chạy từ $$\min(\mu_i) = 0.10$$ đến $$\max(\mu_i) = 0.12$$:

| Lợi suất $$r$$ | $$x_1$$ | $$x_2$$ | Độ lệch chuẩn $$\sigma$$ |
|----------------|---------|---------|--------------------------|
| 0.10 | 0 | 1 | 0.300 |
| 0.105 | 0.25 | 0.75 | 0.238 |
| 0.11 | 0.5 | 0.5 | 0.194 |
| 0.1145 | 0.727 | 0.273 | 0.178 (rủi ro nhỏ nhất) |
| 0.115 | 0.75 | 0.25 | 0.179 |
| 0.12 | 1 | 0 | 0.200 |

**Kết luận:** Danh mục có rủi ro nhỏ nhất đạt tại $$x_1 = 0.08/0.11 \approx 0.727$$ (tương ứng $$r \approx 0.1145$$). Chỉ nhánh $$r \geq 0.1145$$ là **biên hiệu quả** (với cùng mức rủi ro, lợi suất cao hơn); các điểm ứng với $$r < 0.1145$$ đều bị trội (dominated).

</details>

---

## 📝 **Phần III: QCQP và SOCP**

### **Bài tập 3: Bình phương tối thiểu bền vững (SOCP)**

Cho dữ liệu $$A \in \mathbb{R}^{m \times n}$$, $$b \in \mathbb{R}^m$$. Thay cho bình phương tối thiểu thông thường, xét phiên bản bền vững:

$$
\min_{x} \quad \|Ax - b\|_2 + \gamma \|x\|_2
$$

với $$\gamma > 0$$ là tham số chính quy hóa.

**Yêu cầu:**  
a) Viết bài toán dưới dạng SOCP.  
b) Với $$A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 2 & 0 \end{bmatrix}$$, $$b = \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix}$$, $$\gamma = 0.1$$, tìm nghiệm.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Biểu diễn dạng SOCP:**

Đưa thêm hai biến phụ $$t_1, t_2$$ thỏa mãn:
- $$\|Ax - b\|_2 \leq t_1$$
- $$\|x\|_2 \leq t_2$$

Bài toán trở thành:

$$
\begin{align}
\min_{x, t_1, t_2} \quad & t_1 + \gamma t_2 \\
\text{s.t.} \quad & \|Ax - b\|_2 \leq t_1 \\
& \|x\|_2 \leq t_2
\end{align}
$$

Đây là một bài toán **SOCP** với 2 ràng buộc nón bậc hai, khớp với dạng chuẩn tổng quát:

$$
\begin{align}
\min \quad & c^T y \\
\text{s.t.} \quad & \|A_i y + b_i\|_2 \leq c_i^T y + d_i, \quad i = 1, \ldots, k
\end{align}
$$

---

**b) Giải số:**

Dữ liệu:

$$A = \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 2 & 0 \end{bmatrix}, \quad b = \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix}, \quad \gamma = 0.1$$

**Gradient (khi $$Ax \neq b$$ và $$x \neq 0$$):**

$$\nabla f(x) = \frac{A^T(Ax-b)}{\|Ax-b\|_2} + \gamma \frac{x}{\|x\|_2}$$

(Hàm mục tiêu không trơn tại $$x = 0$$ và $$Ax = b$$, đồng thời phương trình $$\nabla f(x) = 0$$ là phi tuyến.)

**Cách 1: Xấp xỉ bằng hồi quy Ridge có nghiệm dạng đóng:**

Xét bài toán lân cận $$\min \|Ax-b\|_2^2 + \gamma^2\|x\|_2^2$$:

$$x_{\text{ridge}} = (A^TA + \gamma^2 I)^{-1} A^T b$$

Tính toán:

$$A^TA = \begin{bmatrix} 1 & 1 & 2 \\ 1 & -1 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 1 & -1 \\ 2 & 0 \end{bmatrix} = \begin{bmatrix} 6 & 0 \\ 0 & 2 \end{bmatrix}$$

$$A^TA + 0.01I = \begin{bmatrix} 6.01 & 0 \\ 0 & 2.01 \end{bmatrix}, \qquad A^Tb = \begin{bmatrix} 1 & 1 & 2 \\ 1 & -1 & 0 \end{bmatrix} \begin{bmatrix} 2 \\ 0 \\ 3 \end{bmatrix} = \begin{bmatrix} 8 \\ 2 \end{bmatrix}$$

Suy ra $$x_{\text{ridge}} = \left(\frac{8}{6.01}, \frac{2}{2.01}\right)^T \approx (1.331, 0.995)^T$$, với giá trị hàm mục tiêu gốc $$f(x_{\text{ridge}}) \approx 0.744$$.

**Cách 2: Nghiệm số của bài toán SOCP gốc** (giải trực tiếp $$\min \|Ax-b\|_2 + 0.1\|x\|_2$$):

$$x^* \approx (1.326, 0.983)^T, \qquad f(x^*) \approx 0.743$$

(Hai nghiệm rất gần nhau nhưng không trùng khớp hoàn toàn vì bài toán gốc dùng chuẩn $$\ell_2$$ thay vì bình phương chuẩn.)

</details>

---

## 📝 **Phần IV: Quy hoạch Nửa xác định (SDP)**

### **Bài tập 4: Hoàn thiện Ma trận (Matrix Completion)**

Cho ma trận đối xứng $$M \in \mathbb{R}^{3 \times 3}$$ bị khuyết một số phần tử, biết:

$$M_{11} = 4, \quad M_{12} = 2, \quad M_{22} = 5, \quad M_{23} = 1$$

Tìm ma trận nửa xác định dương $$X$$ hoàn chỉnh có vết (trace) nhỏ nhất.

**Yêu cầu:**  
a) Viết bài toán SDP.  
b) Tìm nghiệm tối ưu.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Biểu diễn dạng SDP:**

$$
\begin{align}
\min_{X} \quad & \text{tr}(X) \\
\text{s.t.} \quad & X_{11} = 4 \\
& X_{12} = X_{21} = 2 \\
& X_{22} = 5 \\
& X_{23} = X_{32} = 1 \\
& X \succeq 0 \\
& X = X^T
\end{align}
$$

Cấu trúc ma trận $$X$$:

$$X = \begin{bmatrix} 4 & 2 & x_{13} \\ 2 & 5 & 1 \\ x_{13} & 1 & x_{33} \end{bmatrix}$$

---

**b) Giải bài toán:**

**Điều kiện nửa xác định dương (PSD):** tất cả các định thức con chính đều không âm.

- **Định thức con chính cấp 1:** $$4 > 0$$ ✓.
- **Định thức con chính cấp 2:**
$$\begin{vmatrix} 4 & 2 \\ 2 & 5 \end{vmatrix} = 20 - 4 = 16 > 0 \text{ ✓}$$
- **Định thức cấp 3:**
$$\det(X) = 4(5x_{33} - 1) - 2(2x_{33} - x_{13}) + x_{13}(2 - 5x_{13})$$
$$= 20x_{33} - 4 - 4x_{33} + 2x_{13} + 2x_{13} - 5x_{13}^2 = 16x_{33} - 5x_{13}^2 + 4x_{13} - 4$$

Điều kiện $$\det(X) \geq 0$$ tương đương với:
$$x_{33} \geq \frac{5x_{13}^2 - 4x_{13} + 4}{16}$$

(Do hai định thức con chính dẫn đầu cấp 1 và cấp 2 đều dương chặt, điều kiện $$\det(X) \geq 0$$ cũng đủ đảm bảo $$X \succeq 0$$.)

**Cực tiểu hóa $$\text{tr}(X) = 4 + 5 + x_{33} = 9 + x_{33}$$:**

Bài toán quy về tìm giá trị nhỏ nhất của vế phải theo $$x_{13}$$:

$$\frac{d}{dx_{13}}\left(\frac{5x_{13}^2 - 4x_{13} + 4}{16}\right) = \frac{10x_{13} - 4}{16} = 0 \Rightarrow x_{13}^* = 0.4$$

Thay ngược lại để tính $$x_{33}^*$$:

$$x_{33}^{\min} = \frac{5(0.4)^2 - 4(0.4) + 4}{16} = \frac{0.8 - 1.6 + 4}{16} = \frac{3.2}{16} = 0.2$$

**Nghiệm tối ưu:**

$$X^* = \begin{bmatrix} 4 & 2 & 0.4 \\ 2 & 5 & 1 \\ 0.4 & 1 & 0.2 \end{bmatrix}, \quad \text{tr}(X^*) = 9.2$$

**Kiểm tra:** $$\det(X^*) = 16(0.2) - 5(0.16) + 1.6 - 4 = 0$$ (ma trận suy biến hạng 2 và nửa xác định dương ✓).

</details>

---

## 📝 **Phần V: Tổng hợp**

### **Bài tập 5: Nhận diện dạng bài toán chuẩn phù hợp**

Với mỗi bài toán sau, xác định lớp bài toán chuẩn phù hợp nhất (LP, QP, QCQP, SOCP hay SDP):

**a)** $$\min c^T x$$ s.t. $$Ax = b$$, $$\|x\|_\infty \leq 1$$

**b)** $$\min \|Ax - b\|_1$$

**c)** $$\min x^TQx$$ s.t. $$\|Ax - b\|_2 \leq \delta$$ (với $$Q \succeq 0$$)

**d)** $$\min \text{tr}(X)$$ s.t. $$X \succeq yy^T$$, $$X \succeq 0$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) $$\min c^Tx$$ s.t. $$Ax = b$$, $$\|x\|_\infty \leq 1$$:**

Ràng buộc $$\|x\|_\infty \leq 1 \Leftrightarrow -1 \leq x_i \leq 1$$ là hệ các bất đẳng thức tuyến tính.

→ **Quy hoạch tuyến tính (LP)**.

---

**b) $$\min \|Ax - b\|_1$$:**

Đặt $$r = Ax - b$$, ta có $$\|Ax - b\|_1 = \sum_i |r_i|$$. Đưa thêm biến phụ $$t_i \geq |r_i|$$:

$$
\begin{align}
\min_{x, t} \quad & \sum_i t_i \\
\text{s.t.} \quad & -t_i \leq (Ax - b)_i \leq t_i
\end{align}
$$

→ **Quy hoạch tuyến tính (LP)**.

---

**c) $$\min x^TQx$$ s.t. $$\|Ax - b\|_2 \leq \delta$$ (với $$Q \succeq 0$$):**

- Hàm mục tiêu bậc hai lồi (có thể đưa về ràng buộc nón bậc hai bằng biến phụ epigraph).
- Ràng buộc chuẩn $$\ell_2$$ là ràng buộc nón bậc hai.

→ **Quy hoạch nón bậc hai (SOCP)** (hoặc **QCQP** nếu bình phương hai vế ràng buộc thành $$\|Ax-b\|_2^2 \leq \delta^2$$).

---

**d) $$\min \text{tr}(X)$$ s.t. $$X \succeq yy^T$$, $$X \succeq 0$$:**

- Hàm mục tiêu tuyến tính theo ma trận $$X$$.
- Ràng buộc $$X - yy^T \succeq 0$$ là ràng buộc nửa xác định dương (và kéo theo $$X \succeq 0$$).

→ **Quy hoạch nửa xác định (SDP)**.

</details>

---

## 💡 **Tổng kết**

### **Hệ phân cấp các bài toán tối ưu hóa lồi:**

$$
\text{LP} \subset \text{QP} \subset \text{QCQP} \subset \text{SOCP} \subset \text{SDP}
$$

| Lớp bài toán | Hàm mục tiêu | Ràng buộc | Ví dụ tiêu biểu |
|--------------|--------------|-----------|-----------------|
| **LP** | Tuyến tính | Tuyến tính | Bài toán khẩu phần ăn, vận tải |
| **QP** | Bậc hai lồi | Tuyến tính | Danh mục đầu tư, bình phương tối thiểu |
| **QCQP** | Bậc hai lồi | Bậc hai lồi | Tối ưu hóa bền vững bậc hai |
| **SOCP** | Tuyến tính | Nón bậc hai ($$\ell_2$$) | Bình phương tối thiểu bền vững, thiết kế ăng-ten |
| **SDP** | Tuyến tính | Nón ma trận PSD | Hoàn thiện ma trận, nới lỏng tổ hợp |

### **Nguyên tắc lựa chọn mô hình:**
- **LP:** khi hàm mục tiêu và mọi ràng buộc đều tuyến tính.
- **QP:** tối ưu hóa rủi ro bậc hai, bình phương tối thiểu có chính quy hóa $$\ell_2$$.
- **SOCP:** tối ưu hóa bền vững dạng ellipsoid và các ràng buộc chuẩn $$\ell_2$$.
- **SDP:** bài toán có biến ma trận nửa xác định dương hoặc nới lỏng bài toán tổ hợp.

---

## 📚 **Tài liệu tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 4.

2. **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM.

3. **Lobo, M. S., et al.** (1998). "Applications of Second-Order Cone Programming". *Linear Algebra and Applications*.

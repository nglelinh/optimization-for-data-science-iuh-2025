---
layout: post
title: 06-11 Bài Tập Thực Hành - Thuật toán Tối ưu
chapter: '06'
order: 23
owner: GitHub Copilot
lang: vi
categories:
- chapter06
lesson_type: required
redirect_from:
  - /contents/vi/chapter06/06_10_Practical_Exercises_Optimization_Algorithms/
---

Đọc định lý rằng Heavy Ball (Momentum) tăng tốc từ $$\kappa$$ xuống $$\sqrt{\kappa}$$ hay Backtracking tự thích ứng bước luôn thú vị, nhưng chỉ khi bạn tự tay viết vòng lặp tính số, vẽ đường cong log-sai số $$\log(f(x^{(k)}) - f^\star)$$ và chứng kiến đường thẳng dốc đứng của hội tụ tuyến tính cắt mặt đường cong thoải của hội tụ $$O(1/k)$$, trực giác thuật toán mới thực sự ngấm vào máu!

Bộ bài tập thực hành này tập trung vào các kỹ năng định lượng cốt lõi của Chương 06: phân tích tốc độ hội tụ thực nghiệm, so sánh trực tiếp Gradient Descent vs. Heavy Ball Momentum trên ma trận điều kiện xấu, cài đặt Backtracking Line Search và đánh giá nhiễu của SGD.

## Bản đồ kiến thức nền: Bốn thói quen vàng khi thực nghiệm thuật toán tối ưu

Trước khi giải bài tập trên giấy hoặc viết mã Python mô phỏng, hãy ghi nhớ bốn quy chuẩn thực nghiệm sau:

- **Luôn vẽ sai số trên thang bán logarit (`semilogy`):** Trên biểu đồ $$\log_{10}(f(x^{(k)}) - f^\star)$$ theo số vòng lặp $$k$$, **hội tụ tuyến tính $$O(c^k)$$ hiện ra thành một đường thẳng** có độ dốc $$\log_{10}(c)$$, còn hội tụ $$O(1/k)$$ hiện ra thành một đường cong phẳng dần rất dễ phân biệt bằng mắt!
- **Kiểm tra gradient bằng sai phân hữu hạn (Gradient Checking):** Trước khi đổ lỗi cho thuật toán không hội tụ, luôn kiểm tra công thức $$\nabla f(x)$$ của bạn bằng $$\frac{f(x + \varepsilon e_i) - f(x - \varepsilon e_i)}{2\varepsilon}$$ ($$\varepsilon = 10^{-6}$$); 80% lỗi thuật toán trong thực tế đến từ tính sai gradient!
- **So sánh công bằng theo số phép tính gradient (Oracle Calls):** Khi so sánh Batch GD, Backtracking và SGD, đừng chỉ đếm số vòng lặp `k` — hãy đếm tổng số lượt duyệt dữ liệu (epochs) hoặc số lần đánh giá hàm/gradient!
- **Kiểm soát chỉ số điều kiện $$\kappa$$ khi tạo bài test:** Để thấy rõ sự khác biệt giữa GD và Momentum, hãy thử nghiệm trên ma trận $$Q$$ có $$\kappa \in \{10, 100, 1000\}$$ (vì tại $$\kappa = 1$$ cả hai đều hội tụ sau đúng 1 bước!).

### Khung giải thích (nên đọc chậm): Tính trước độ dốc đường `semilogy` để đối chiếu với kết quả chạy code

Giả sử bạn chạy bài tập so sánh GD và Momentum trên bài toán bậc hai có $$m = 1,\; L = 100$$ ($$\kappa = 100$$) với bước tối ưu:

1. **Dự đoán lý thuyết cho GD ($$t^\star = \frac{2}{101} \approx 0.0198$$):**
   - Hệ số co khoảng cách: $$\rho_{\text{GD}} = \frac{100 - 1}{100 + 1} = \frac{99}{101} \approx 0.9802$$.
   - Hệ số co sai số hàm: $$\rho_{\text{GD}}^2 \approx 0.9608$$.
   - Số bước để sai số hàm giảm **10 lần** (1 bậc trên thang `log10`):
     $$k_{10\times}^{\text{GD}} = \frac{\ln 10}{-\ln(0.9608)} \approx \frac{2.3026}{0.0400} \approx 58 \text{ bước!}$$
2. **Dự đoán lý thuyết cho Heavy Ball Momentum ($$\alpha^\star = \frac{4}{121},\; \beta^\star = \frac{81}{121}$$):**
   - Hệ số co khoảng cách: $$\rho_{\text{HB}} = \frac{\sqrt{100} - 1}{\sqrt{100} + 1} = \frac{9}{11} \approx 0.8182$$.
   - Hệ số co sai số hàm: $$\rho_{\text{HB}}^2 \approx 0.6694$$.
   - Số bước để sai số hàm giảm **10 lần**:
     $$k_{10\times}^{\text{HB}} = \frac{\ln 10}{-\ln(0.6694)} \approx \frac{2.3026}{0.4013} \approx 6 \text{ bước!}$$
3. **Kiểm chứng:** Khi chạy code vẽ `semilogy`, nếu bạn thấy Momentum cần khoảng 60 bước để giảm sai số xuống $$10^{-10}$$ còn GD cần gần 580 bước (chênh đúng ~10 lần $$= \sqrt{\kappa}$$!), bạn biết chắc chắn code của mình đã chính xác 100%!

---

# Bài tập Thực hành — Thuật toán Tối ưu hóa

Các bài tập dưới đây được tham khảo từ Boyd & Vandenberghe (2004) và Nocedal & Wright (2006).

---

## 📝 **Phần I: Gradient Descent**

### **Bài tập 1: Phân tích Tốc độ Hội tụ**

Cho hàm số $$f(x) = \frac{1}{2}x^TQx$$ với $$Q = \text{diag}(1, 4, 10)$$.

**Yêu cầu:**  
a) Tính gradient $$\nabla f(x)$$.  
b) Với kích thước bước $$t = \frac{2}{m + L}$$ (trong đó $$m = \lambda_{\min}(Q)$$, $$L = \lambda_{\max}(Q)$$), tính hệ số hội tụ.  
c) Xuất phát từ $$x^{(0)} = (1, 1, 1)^T$$, tính $$x^{(1)}$$ và $$x^{(2)}$$.  
d) Ước lượng số vòng lặp cần thiết để đạt $$\|x^{(k)}\| < 10^{-6}$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Gradient:**

$$\nabla f(x) = Qx = \begin{bmatrix} x_1 \\ 4x_2 \\ 10x_3 \end{bmatrix}$$

---

**b) Hệ số hội tụ:**

$$m = 1, \quad L = 10$$

$$t = \frac{2}{1 + 10} = \frac{2}{11}$$

**Đánh giá tốc độ hội tụ:**

$$\|x^{(k+1)} - x^*\| \leq \left(\frac{L - m}{L + m}\right) \|x^{(k)} - x^*\|$$

$$= \frac{10 - 1}{10 + 1} \|x^{(k)} - x^*\| = \frac{9}{11} \|x^{(k)} - x^*\|$$

Thuật toán đạt **hội tụ tuyến tính** với hệ số co $$\frac{9}{11} \approx 0.818$$.

---

**c) Các bước lặp đầu tiên:**

$$x^{(0)} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}, \quad \nabla f(x^{(0)}) = \begin{bmatrix} 1 \\ 4 \\ 10 \end{bmatrix}$$

$$x^{(1)} = x^{(0)} - t \nabla f(x^{(0)}) = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - \frac{2}{11} \begin{bmatrix} 1 \\ 4 \\ 10 \end{bmatrix} = \begin{bmatrix} 1 - \frac{2}{11} \\ 1 - \frac{8}{11} \\ 1 - \frac{20}{11} \end{bmatrix} = \begin{bmatrix} \frac{9}{11} \\ \frac{3}{11} \\ -\frac{9}{11} \end{bmatrix}$$

$$\nabla f(x^{(1)}) = \begin{bmatrix} \frac{9}{11} \\ \frac{12}{11} \\ -\frac{90}{11} \end{bmatrix}$$

$$x^{(2)} = x^{(1)} - \frac{2}{11} \nabla f(x^{(1)}) = \begin{bmatrix} \frac{9}{11} - \frac{18}{121} \\ \frac{3}{11} - \frac{24}{121} \\ -\frac{9}{11} + \frac{180}{121} \end{bmatrix} = \begin{bmatrix} \frac{81}{121} \\ \frac{9}{121} \\ \frac{81}{121} \end{bmatrix}$$

---

**d) Số vòng lặp ước lượng:**

$$\|x^{(k)}\| \leq \left(\frac{9}{11}\right)^k \|x^{(0)}\|, \quad \|x^{(0)}\| = \sqrt{3}$$

Cần thỏa mãn: $$\left(\frac{9}{11}\right)^k \sqrt{3} < 10^{-6}$$

$$k > \frac{\ln(10^{-6}/\sqrt{3})}{\ln(9/11)} = \frac{\ln(10^{-6}) - 0.5\ln(3)}{\ln(9/11)} \approx \frac{-13.816 - 0.549}{-0.201} \approx 71.6$$

Do đó cần khoảng **72 vòng lặp**.

</details>

---

## 📝 **Phần II: Các Phương pháp Momentum**

### **Bài tập 2: So sánh Heavy Ball và Gradient Descent**

Cho hàm $$f(x) = x_1^2 + 9x_2^2$$ (điều kiện xấu với chỉ số điều kiện $$\kappa = 9$$).

**Yêu cầu:**  
a) So sánh các bước lặp đầu của GD và Heavy Ball xuất phát từ $$x^{(0)} = (3, 1)^T$$.  
b) Tính hệ số momentum tối ưu $$\beta$$.  
c) So sánh tốc độ hội tụ của hai phương pháp.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Gradient Descent:**

$$\nabla f(x) = \begin{bmatrix} 2x_1 \\ 18x_2 \end{bmatrix}$$

Kích thước bước tối ưu: $$t = \frac{2}{2 + 18} = 0.1$$.

$$x^{(1)} = (3, 1) - 0.1(6, 18) = (2.4, -0.8)$$

$$x^{(2)} = (2.4, -0.8) - 0.1(4.8, -14.4) = (1.92, 0.64)$$

**Nhận xét:** Quỹ đạo dao động đổi dấu liên tục theo trục $$x_2$$ và tiến chậm về $$(0, 0)$$.

---

**Phương pháp Heavy Ball:**

$$x^{(k+1)} = x^{(k)} - t\nabla f(x^{(k)}) + \beta(x^{(k)} - x^{(k-1)})$$

**Hệ số momentum tối ưu $$\beta$$:**

$$\beta = \left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^2 = \left(\frac{3 - 1}{3 + 1}\right)^2 = \left(\frac{1}{2}\right)^2 = 0.25$$

---

**b) Minh họa bước lặp Heavy Ball (với cùng $$t = 0.1$$):**

$$x^{(1)} = (2.4, -0.8), \quad x^{(2)} = (1.92, 0.64)$$ (ở các bước khởi đầu chưa tích lũy momentum)

$$x^{(3)} = (1.92, 0.64) - 0.1(3.84, 11.52) + 0.25\big((1.92, 0.64) - (2.4, -0.8)\big)$$

$$= (1.92, 0.64) - (0.384, 1.152) + 0.25(-0.48, 1.44)$$

$$= (1.92, 0.64) - (0.384, 1.152) + (-0.12, 0.36) = (1.416, -0.152)$$

---

**c) So sánh tốc độ hội tụ:**

- **GD:** $$\left(\frac{\kappa - 1}{\kappa + 1}\right)^k = \left(\frac{8}{10}\right)^k = 0.8^k$$
- **Heavy Ball (với bộ tham số tối ưu):** $$\left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^{k} = 0.5^k$$

Ở mỗi vòng lặp, Heavy Ball co sai số theo hệ số $$0.5$$ so với $$0.8$$ của GD, tức số vòng lặp cần thiết giảm khoảng $$\frac{\ln 0.5}{\ln 0.8} \approx 3.1$$ lần.

</details>

---

## 📝 **Phần III: Tăng tốc Nesterov**

### **Bài tập 3: So sánh Nesterov và Gradient Descent Chuẩn**

Cho $$f(x) = \frac{1}{2}\|Ax - b\|^2$$ với $$A = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$$ và $$b = (2, 1)^T$$.

**Yêu cầu:**  
a) Tìm nghiệm chính xác $$x^*$$.  
b) Viết công thức và tính các bước đầu của phương pháp Nesterov.  
c) So sánh kết quả với GD sau 5 vòng lặp.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Nghiệm chính xác:**

$$\nabla f(x) = A^T(Ax - b) = 0 \Leftrightarrow A^TAx = A^Tb$$

$$\begin{bmatrix} 4 & 0 \\ 0 & 1 \end{bmatrix} x = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \end{bmatrix} \Rightarrow x^* = (1, 1)^T$$

---

**b) Phương pháp Nesterov:**

$$
\begin{align}
y^{(k)} &= x^{(k)} + \frac{k-1}{k+2}(x^{(k)} - x^{(k-1)}) \\
x^{(k+1)} &= y^{(k)} - t\nabla f(y^{(k)})
\end{align}
$$

Với $$L = \lambda_{\max}(A^TA) = 4$$, chọn $$t = \frac{1}{L} = 0.25$$.

Xuất phát từ $$x^{(0)} = (0, 0)$$ và $$x^{(1)} = (0, 0)$$:
- Tại $$k=1$$: $$y^{(1)} = (0, 0)$$, $$\nabla f(y^{(1)}) = A^T(A(0,0) - (2,1)) = -A^Tb = (-4, -1)$$, nên $$x^{(2)} = (0, 0) - 0.25(-4, -1) = (1, 0.25)$$.
- Tại $$k=2$$: $$y^{(2)} = (1, 0.25) + \frac{1}{4}\big((1, 0.25) - (0, 0)\big) = (1.25, 0.3125)$$.

(Tiếp tục tương tự cho các bước tiếp theo.)

---

**c) So sánh sau 5 vòng lặp:**

| Phương pháp | $$x$$ sau 5 vòng lặp | $$\|x^{(5)} - x^*\|$$ |
|-------------|----------------------|-----------------------|
| GD | $$(1, 0.763)$$ | $$0.237$$ |
| Nesterov | $$(1, 0.944)$$ | $$0.056$$ |

Sai số của phương pháp Nesterov nhỏ hơn khoảng 4 lần so với GD (với GD, sai số ở tọa độ thứ hai bằng $$0.75^5 \approx 0.237$$).

</details>

---

## 📝 **Phần IV: Gradient Gần kề (Proximal Gradient)**

### **Bài tập 4: Bài toán LASSO với Toán tử Ngưỡng mềm**

Cho bài toán LASSO: $$\min_x \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$

với $$A = I$$, $$b = (2, -1, 0.5)^T$$ và $$\lambda = 1$$.

**Yêu cầu:**  
a) Viết quy tắc cập nhật gradient gần kề.  
b) Xác định toán tử ngưỡng mềm (soft-thresholding operator).  
c) Thực hiện lặp xuất phát từ $$x^{(0)} = 0$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Quy tắc gradient gần kề:**

Đặt $$f(x) = \frac{1}{2}\|x - b\|^2$$ (phần trơn) và $$g(x) = \lambda\|x\|_1$$ (phần không trơn):

$$x^{(k+1)} = \text{prox}_{tg}\big(x^{(k)} - t\nabla f(x^{(k)})\big) = \text{prox}_{t\lambda\|\cdot\|_1}\big(x^{(k)} - t(x^{(k)} - b)\big)$$

Với $$t = 1$$:

$$x^{(k+1)} = \text{prox}_{\lambda\|\cdot\|_1}(b)$$

---

**b) Toán tử ngưỡng mềm (Soft-thresholding):**

$$\text{prox}_{\lambda\|\cdot\|_1}(y) = S_\lambda(y)$$

trong đó theo từng thành phần:

$$S_\lambda(y_i) = \begin{cases}
y_i - \lambda & \text{nếu } y_i > \lambda \\
0 & \text{nếu } |y_i| \leq \lambda \\
y_i + \lambda & \text{nếu } y_i < -\lambda
\end{cases}$$

---

**c) Kết quả lặp:**

Với $$x^{(0)} = (0, 0, 0)$$, $$b = (2, -1, 0.5)$$ và $$\lambda = 1$$:

$$x^{(1)} = S_1(b) = \big(S_1(2), S_1(-1), S_1(0.5)\big) = (2 - 1, 0, 0) = (1, 0, 0)$$

Do $$A = I$$, thuật toán hội tụ chỉ sau đúng **1 bước**, cho nghiệm tối ưu $$x^* = (1, 0, 0)^T$$:
- $$b_1 = 2 > \lambda$$ được co về $$1$$.
- $$|b_2| = 1 = \lambda$$ được đưa về $$0$$.
- $$|b_3| = 0.5 < \lambda$$ được đưa về $$0$$.

</details>

---

## 📝 **Phần V: Hạ Tọa độ (Coordinate Descent)**

### **Bài tập 5: Hạ Tọa độ cho Bài toán Toàn phương**

$$\min_x \quad x_1^2 + 2x_2^2 + x_1x_2 - 3x_1 - 4x_2$$

**Yêu cầu:**  
a) Cực tiểu hóa theo $$x_1$$ khi cố định $$x_2$$.  
b) Cực tiểu hóa theo $$x_2$$ khi cố định $$x_1$$.  
c) Lặp từ $$(0, 0)$$ và đối chiếu với nghiệm chính xác.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Cực tiểu hóa theo $$x_1$$:**

$$f(x_1, x_2) = x_1^2 + x_1x_2 - 3x_1 + (2x_2^2 - 4x_2)$$

$$\frac{\partial f}{\partial x_1} = 2x_1 + x_2 - 3 = 0 \Rightarrow x_1^* = \frac{3 - x_2}{2}$$

---

**b) Cực tiểu hóa theo $$x_2$$:**

$$\frac{\partial f}{\partial x_2} = 4x_2 + x_1 - 4 = 0 \Rightarrow x_2^* = \frac{4 - x_1}{4}$$

---

**c) Các bước hạ tọa độ:**

**Bước 0:** $$(x_1, x_2) = (0, 0)$$

**Bước 1:**
- Cố định $$x_2 = 0$$: $$x_1 = \frac{3 - 0}{2} = 1.5$$
- Cố định $$x_1 = 1.5$$: $$x_2 = \frac{4 - 1.5}{4} = 0.625$$

**Bước 2:**
- Cố định $$x_2 = 0.625$$: $$x_1 = \frac{3 - 0.625}{2} = 1.1875$$
- Cố định $$x_1 = 1.1875$$: $$x_2 = \frac{4 - 1.1875}{4} \approx 0.703$$

**Bước 3:**
- $$x_1 \approx 1.148$$, $$x_2 \approx 0.713$$

Dãy lặp tiến dần về $$x^* \approx (1.143, 0.714)$$.

**Nghiệm chính xác (giải hệ phương trình đồng thời):**

$$
\begin{cases}
2x_1 + x_2 = 3 \\
x_1 + 4x_2 = 4
\end{cases}
\Rightarrow x^* = \left(\frac{8}{7}, \frac{5}{7}\right) \approx (1.143, 0.714)$$

</details>

---

## 💡 **Tổng kết**

### **So sánh Các Thuật toán**

| Phương pháp | Tốc độ hội tụ | Chi phí mỗi vòng lặp | Phù hợp nhất với |
|-------------|---------------|----------------------|------------------|
| GD | $$O(1/k)$$ | $$O(n)$$ | Bài toán có chỉ số điều kiện tốt |
| Heavy Ball | $$O(\rho^k)$$, $$\rho < 1$$ | $$O(n)$$ | Bài toán bậc hai / lồi mạnh điều kiện xấu |
| Nesterov | $$O(1/k^2)$$ | $$O(n)$$ | Bài toán lồi trơn cần hội tụ nhanh |
| Proximal GD | $$O(1/k)$$ | $$O(n)$$ + phép chiếu/prox | Bài toán hợp (phần trơn + phần không trơn) |
| Coordinate Descent | Tùy cấu trúc | $$O(n/m)$$ | Bài toán quy mô lớn, tách biến được |

### **Gợi ý Lựa chọn Phương pháp**
- **GD:** Bài toán đơn giản, chỉ số điều kiện nhỏ.
- **Momentum (Heavy Ball):** Hàm bậc hai hoặc lồi mạnh có điều kiện xấu.
- **Nesterov:** Cần tăng tốc hội tụ trên hàm lồi trơn.
- **Proximal GD:** Bài toán có số hạng điều chuẩn không trơn (chuẩn $$\ell_1$$, chuẩn hạt nhân...).
- **Coordinate Descent:** Số chiều rất lớn và bước tối ưu theo từng tọa độ tính nhanh.

---

## 📚 **Tài liệu Tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 9.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization*. Springer. Chapters 2-3.

3. **Nesterov, Y.** (2004). *Introductory Lectures on Convex Optimization*. Springer.

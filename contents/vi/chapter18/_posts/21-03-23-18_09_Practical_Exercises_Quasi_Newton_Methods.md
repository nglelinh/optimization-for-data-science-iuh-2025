---
layout: post
title: 18-09 Bài Tập Thực Hành - Quasi-Newton Methods
chapter: '18'
order: 10
owner: GitHub Copilot
lang: vi
categories:
- chapter18
lesson_type: required
redirect_from:
  - /contents/vi/chapter18/18_08_Practical_Exercises_Quasi_Newton_Methods/
---

Để thực sự tin tưởng các công thức cập nhật ma trận phức tạp như SR1, DFP, BFGS hay vòng lặp hai chiều L-BFGS, không gì thay thế được việc tự tay tính thử từng ma trận $$2 \times 2$$, kiểm chứng phương trình secant bằng phép nhân trực tiếp và đối chiếu số vòng lặp của chúng trên các hàm kiểm chuẩn khét tiếng như thung lũng cong Rosenbrock. Bộ bài tập thực hành này giúp bạn biến các ký hiệu $$B_k, H_k, s_k, y_k$$ thành kỹ năng tính toán và lập trình sắc bén.

## Bản đồ kiến thức nền: Bốn nguyên tắc kiểm tra chéo khi làm bài tập Quasi-Newton

Trước khi giải từng bài tập tính tay và viết mã bên dưới, hãy giữ sẵn bốn phép kiểm chứng nhanh này như một "bộ công cụ gỡ lỗi":

- **Kiểm tra dấu điều kiện độ cong trước mọi phép cập nhật:** Luôn tính $$y_k^T s_k$$ đầu tiên. Nếu $$y_k^T s_k \le 0$$, cập nhật BFGS/DFP không còn đảm bảo tính xác định dương và bạn cần kiểm tra lại hướng bước đi hoặc điều kiện Wolfe.
- **Kiểm chứng phương trình secant ngay sau khi tính $$B_{k+1}$$ hoặc $$H_{k+1}$$:** Phép nhân $$B_{k+1} s_k$$ **bắt buộc** phải ra đúng $$y_k$$ (và $$H_{k+1} y_k = s_k$$). Nếu lệch dù chỉ ở một phần tử, chắc chắn đã có lỗi dấu hoặc lỗi hệ số $$\rho = 1/(y_k^T s_k)$$.
- **Kiểm tra tính đối xứng và trị riêng dương:** Với ma trận $$2 \times 2$$ dạng $$\begin{bmatrix} a & b \\ b & c \end{bmatrix}$$, kiểm tra nhanh $$a > 0$$ và $$ac - b^2 > 0$$ là đủ khẳng định ma trận xác định dương.
- **Đối chiếu L-BFGS với BFGS đầy đủ:** Khi lập trình L-BFGS, đặt lịch sử $$m$$ lớn hơn số vòng lặp chạy thử (và dùng cùng khởi tạo $$H_0 = I$$, tắt tỉ lệ động $$\gamma_k$$) thì hướng bước đi của L-BFGS phải trùng khớp tuyệt đối với BFGS đầy đủ tới sai số máy $$10^{-14}$$.

### Khung giải thích (nên đọc chậm): Thử kiểm tra nhanh tính tương thích giữa $$B_1$$ và $$H_1$$ trên một ví dụ nhỏ

Giả sử trên hàm $$f(x_1, x_2) = 2x_1^2 + x_2^2$$, bạn đi từ $$x^0 = (1, 2)^T$$ tới $$x^1 = (0.5, 1)^T$$ với $$H_0 = I$$:

1. **Tính cặp $$(s, y)$$:**
   - $$s = x^1 - x^0 = (-0.5, \; -1)^T$$.
   - $$\nabla f(x^0) = (4, 4)^T$$, $$\nabla f(x^1) = (2, 2)^T \implies y = (-2, \; -2)^T$$.
2. **Kiểm tra điều kiện độ cong:** $$y^T s = (-2)(-0.5) + (-2)(-1) = 1 + 2 = 3 > 0 \implies \rho = \frac{1}{3}$$.
3. **Tính $$B_1^{\text{BFGS}}$$:** Với $$B_0 = I$$, $$s^T B_0 s = 0.25 + 1 = 1.25$$:
   $$B_1 = I - \frac{1}{1.25}\begin{bmatrix} 0.25 & 0.5 \\ 0.5 & 1 \end{bmatrix} + \frac{1}{3}\begin{bmatrix} 4 & 4 \\ 4 & 4 \end{bmatrix} = \begin{bmatrix} 0.8 & -0.4 \\ -0.4 & 0.2 \end{bmatrix} + \begin{bmatrix} 4/3 & 4/3 \\ 4/3 & 4/3 \end{bmatrix} \approx \begin{bmatrix} 2.1333 & 0.9333 \\ 0.9333 & 1.5333 \end{bmatrix}.$$
4. **Kiểm chứng chéo secant:**
   $$B_1 s = \begin{bmatrix} 2.1333(-0.5) + 0.9333(-1) \\ 0.9333(-0.5) + 1.5333(-1) \end{bmatrix} = \begin{bmatrix} -2.0000 \\ -2.0000 \end{bmatrix} = y, \qquad \det(B_1) \approx 2.40 > 0.$$
   Mọi phép kiểm tra đều khớp hoàn hảo — bạn đã sẵn sàng chinh phục trọn bộ bài tập thực hành của Chương 18!

---

# Bài Tập Thực Hành - Phương pháp Quasi-Newton

Các bài tập được tham khảo từ Nocedal & Wright (2006).

---

## 📝 **Bài tập 1: Cập nhật BFGS**

Cho hàm mục tiêu $$f(x) = x_1^2 + 4x_2^2$$, $$x^{(k)} = (2, 1)$$, $$x^{(k+1)} = (1.6, 0.7)$$.

**Yêu cầu:**  
a) Tính $$s^{(k)} = x^{(k+1)} - x^{(k)}$$ và $$y^{(k)} = \nabla f(x^{(k+1)}) - \nabla f(x^{(k)})$$.  
b) Áp dụng công thức cập nhật BFGS cho xấp xỉ nghịch đảo Hessian: $$H_{k+1} = \left(I - \rho s y^T\right) H_k \left(I - \rho y s^T\right) + \rho s s^T$$, với $$\rho = \frac{1}{y^Ts}$$ và khởi tạo $$H_0 = I$$.  
c) Kiểm chứng phương trình secant $$H_{k+1}y = s$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tính $$s$$ và $$y$$:**

$$s = (1.6, 0.7) - (2, 1) = (-0.4, -0.3)$$

$$\nabla f(x) = (2x_1, 8x_2)$$

$$\nabla f(x^{(k)}) = (4, 8)$$, $$\nabla f(x^{(k+1)}) = (3.2, 5.6)$$

$$y = (3.2, 5.6) - (4, 8) = (-0.8, -2.4)$$

---

**b) Cập nhật BFGS (khởi tạo $$H_0 = I$$):**

$$y^Ts = (-0.8)(-0.4) + (-2.4)(-0.3) = 0.32 + 0.72 = 1.04$$, suy ra $$\rho = 1/1.04 \approx 0.9615$$.

$$I - \rho s y^T = \begin{bmatrix} 0.692 & -0.923 \\ -0.231 & 0.308 \end{bmatrix}$$

$$H_1 = (I - \rho s y^T)(I - \rho y s^T) + \rho s s^T$$

$$\approx \begin{bmatrix} 1.331 & -0.444 \\ -0.444 & 0.148 \end{bmatrix} + \begin{bmatrix} 0.154 & 0.115 \\ 0.115 & 0.087 \end{bmatrix} \approx \begin{bmatrix} 1.485 & -0.328 \\ -0.328 & 0.234 \end{bmatrix}$$

---

**c) Kiểm chứng điều kiện secant:**

$$H_1 y = \begin{bmatrix} 1.485 & -0.328 \\ -0.328 & 0.234 \end{bmatrix} \begin{bmatrix} -0.8 \\ -2.4 \end{bmatrix} \approx \begin{bmatrix} -0.4 \\ -0.3 \end{bmatrix} = s$$ ✓

</details>

---

## 📝 **Bài tập 2: So sánh SR1 và BFGS**

Xét công thức cập nhật SR1: $$H_{k+1} = H_k + \frac{(s - H_k y)(s - H_k y)^T}{(s - H_k y)^T y}$$.

**Yêu cầu:**  
a) So sánh độ ổn định của SR1 với BFGS.  
b) Khi nào cập nhật SR1 thất bại?  
c) Tính ma trận cập nhật SR1 cho dữ liệu từ Bài tập 1.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Độ ổn định:**

- **BFGS:** Luôn bảo toàn tính xác định dương khi điều kiện độ cong $$y^Ts > 0$$ được thỏa mãn.
- **SR1:** Có thể tạo ra ma trận suy biến (singular) hoặc không xác định (indefinite).

**b) SR1 gặp sự cố khi:**

$$(s - H_k y)^T y \approx 0$$, gây hiện tượng chia cho số gần $$0$$.

**Quy tắc bảo vệ:** Bỏ qua bước cập nhật nếu $$|(s - H_k y)^T y| < \epsilon \|s - H_k y\| \|y\|$$ (hoặc theo ngưỡng $$\epsilon \|s\| \|y\|$$).

---

**c) Tính cập nhật SR1:**

$$s - H_0 y = (-0.4, -0.3) - (-0.8, -2.4) = (0.4, 2.1)$$

$$(s - H_0 y)^T y = 0.4(-0.8) + 2.1(-2.4) = -0.32 - 5.04 = -5.36$$

$$H_1^{\text{SR1}} = I + \frac{1}{-5.36}\begin{bmatrix} 0.16 & 0.84 \\ 0.84 & 4.41 \end{bmatrix}$$

$$\approx \begin{bmatrix} 0.970 & -0.157 \\ -0.157 & 0.177 \end{bmatrix}$$

Ma trận này thỏa mãn phương trình secant $$H_1 y = s$$. Trong ví dụ cụ thể này, $$H_1^{\text{SR1}}$$ vẫn xác định dương (định thức xấp xỉ $$0.147 > 0$$), nhưng tổng quát SR1 **không** đảm bảo tính xác định dương vì mẫu số có thể âm hoặc tiến gần $$0$$.

</details>

---

## 📝 **Bài tập 3: L-BFGS cho bài toán quy mô lớn**

L-BFGS chỉ lưu trữ $$m$$ cặp $$(s, y)$$ gần nhất thay vì toàn bộ ma trận $$H_k$$ kích thước $$n \times n$$.

**Yêu cầu:**  
a) Trình bày thuật toán đệ quy hai vòng (two-loop recursion).  
b) Viết tường minh cách tính $$H_k \nabla f$$ với $$m = 2$$ cặp lưu trữ.  
c) Ước lượng bộ nhớ cần thiết khi $$n = 10^6$$ và $$m = 10$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Thuật toán đệ quy hai vòng:**

```
q = ∇f(x_k)
for i = k-1, ..., k-m:
    α_i = ρ_i s_i^T q
    q = q - α_i y_i
r = H_0 q  (often H_0 = γI)
for i = k-m, ..., k-1:
    β = ρ_i y_i^T r
    r = r + s_i(α_i - β)
return r = H_k ∇f
```

---

**b) Minh họa với $$m = 2$$:**

Giả sử lưu hai cặp $$\{(s_1, y_1), (s_2, y_2)\}$$ với $$\rho_i = \frac{1}{y_i^T s_i}$$.

**Vòng lặp 1 (ngược):**

$$\alpha_2 = \rho_2 s_2^T \nabla f$$, $$q_1 = \nabla f - \alpha_2 y_2$$

$$\alpha_1 = \rho_1 s_1^T q_1$$, $$q_0 = q_1 - \alpha_1 y_1$$

**Khởi tạo:** $$r_0 = \gamma q_0$$

**Vòng lặp 2 (xuôi):**

$$\beta_1 = \rho_1 y_1^T r_0$$, $$r_1 = r_0 + s_1(\alpha_1 - \beta_1)$$

$$\beta_2 = \rho_2 y_2^T r_1$$, $$r_2 = r_1 + s_2(\alpha_2 - \beta_2)$$

Hướng giảm thu được: $$d = -r_2$$.

---

**c) Ước lượng bộ nhớ (dùng số thực 64-bit / 8 byte):**

- **BFGS đầy đủ:** $$n^2 = 10^{12}$$ phần tử $$\approx$$ **8 TB**.
- **L-BFGS:** $$2mn = 2 \cdot 10 \cdot 10^6 = 2 \times 10^7$$ phần tử $$\approx$$ **160 MB**.

Mức giảm bộ nhớ đạt **$$50{,}000\times$$**.

</details>

---

## 📝 **Bài tập 4: Tốc độ hội tụ**

**Yêu cầu:**  
a) Phương pháp Newton: $$\|x^{(k+1)} - x^*\| \leq C\|x^{(k)} - x^*\|^2$$ (hội tụ bậc hai).  
b) Phương pháp BFGS: tốc độ hội tụ tương ứng thuộc loại nào?  
c) So sánh số vòng lặp ước lượng giữa GD, BFGS và Newton.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Phương pháp Newton:**

Hội tụ **bậc hai** ($$p = 2$$), với hằng số $$C \approx \frac{1}{2} \|\nabla^2 f(x^*)^{-1}\| \|\nabla^3 f(x^*)\|$$.

Số vòng lặp cần thiết trong vùng hội tụ cục bộ tỉ lệ với $$\log\log(1/\epsilon)$$.

---

**b) Phương pháp BFGS:**

Hội tụ **siêu tuyến tính** (nhanh hơn hội tụ tuyến tính nhưng chậm hơn hội tụ bậc hai), nghĩa là:

$$\lim_{k \to \infty} \frac{\|x^{(k+1)} - x^*\|}{\|x^{(k)} - x^*\|} = 0$$

---

**c) So sánh số vòng lặp minh họa (để đạt độ chính xác $$10^{-10}$$):**

| Phương pháp | Tốc độ hội tụ | Số vòng lặp ước lượng |
|--------|------|------------|
| GD | Tuyến tính ($$0.9^k$$) | ~230 |
| BFGS | Siêu tuyến tính | ~15 |
| Newton | Bậc hai | ~5 |

BFGS đạt sự cân bằng tốt giữa chi phí mỗi vòng lặp và tốc độ hội tụ.

</details>

---

## 📝 **Bài tập 5: Các chi tiết cài đặt thực tế**

**Yêu cầu:**  
a) Khi nào nên bỏ qua bước cập nhật BFGS?  
b) Cách chọn hệ số co giãn cho ma trận khởi đầu $$H_0$$.  
c) Yêu cầu đối với thuật toán tìm kiếm theo đường thẳng (line search).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bỏ qua bước cập nhật khi:**

$$y^Ts \leq \epsilon_s \|s\|^2$$ (vi phạm điều kiện độ cong).

**Lý do:** Đảm bảo ma trận xấp xỉ luôn xác định dương và tránh mất ổn định số học.

---

**b) Xấp xỉ Hessian khởi đầu:**

$$H_0 = \gamma I$$ với $$\gamma = \frac{y_{k-1}^T s_{k-1}}{y_{k-1}^T y_{k-1}}$$.

Hệ số co giãn thích nghi này phản ánh tỷ lệ độ cong cục bộ từ bước lặp gần nhất.

---

**c) Yêu cầu tìm kiếm theo đường thẳng:**

Sử dụng **điều kiện Wolfe mạnh (Strong Wolfe conditions)**:

1. $$f(x + \alpha d) \leq f(x) + c_1 \alpha \nabla f^T d$$ (điều kiện giảm đủ)
2. $$|\nabla f(x + \alpha d)^T d| \leq c_2 |\nabla f^T d|$$ (điều kiện độ cong)

Thường chọn $$c_1 = 10^{-4}$$ và $$c_2 = 0.9$$. Điều kiện này đảm bảo $$y^Ts > 0$$.

</details>

---

## 💡 **Tổng kết**

| Phương pháp | Bộ nhớ | Tốc độ hội tụ | Phù hợp với |
|--------|---------|------|----------|
| Newton | $$O(n^2)$$ | Bậc hai | Bài toán kích thước nhỏ ($$n$$ nhỏ) |
| BFGS | $$O(n^2)$$ | Siêu tuyến tính | Bài toán kích thước trung bình |
| L-BFGS | $$O(mn)$$ | Siêu tuyến tính | Bài toán quy mô lớn ($$n$$ lớn) |
| SR1 | $$O(n^2)$$ | Siêu tuyến tính | Chấp nhận Hessian không xác định dương |

---

## 📚 **Tài liệu tham khảo**

1. Nocedal, J., & Wright, S. J. (2006). *Numerical Optimization*. Springer. Chapter 6.
2. Liu, D. C., & Nocedal, J. (1989). "On the Limited Memory BFGS Method".

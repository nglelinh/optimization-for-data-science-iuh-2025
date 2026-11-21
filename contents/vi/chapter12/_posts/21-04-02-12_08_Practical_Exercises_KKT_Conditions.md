---
layout: post
title: 12-8 Bài Tập Thực Hành - Điều Kiện KKT
chapter: '12'
order: 9
owner: GitHub Copilot
lang: vi
categories:
- chapter12
lesson_type: required
---

# Bài Tập Thực Hành - Điều Kiện KKT (Karush-Kuhn-Tucker)

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004), Nocedal & Wright (2006), và Bertsekas (1999).

---

## 📝 **Phần I: Kiểm chứng Điều kiện KKT**

### **Bài tập 1: Bài toán cơ bản (Boyd & Vandenberghe, Ex. 5.1)**

Cho bài toán:

$$
\begin{align}
\min_{x} \quad & x_1^2 + x_2^2 \\
\text{s.t.} \quad & x_1 + x_2 = 1 \\
& x_1 \geq 0
\end{align}
$$

Kiểm tra hai nghiệm ứng viên:
1. $$x^{(1)} = (0.5, 0.5)$$, $$\nu = 1$$, $$\lambda = 0$$
2. $$x^{(2)} = (0, 1)$$, $$\nu = 2$$, $$\lambda = 2$$

**Yêu cầu:** Viết điều kiện KKT, kiểm tra từng điều kiện, xác định nghiệm tối ưu.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Lagrangian:** $$L(x,\nu,\lambda) = x_1^2 + x_2^2 - \nu(x_1+x_2-1) + \lambda(-x_1)$$ (ràng buộc bất đẳng thức viết dạng $$g(x)=-x_1 \leq 0$$)

**Bốn điều kiện KKT:**

1. **Stationarity:** $$2x_1 - \nu - \lambda = 0$$, $$2x_2 - \nu = 0$$
2. **Primal Feasibility:** $$x_1 + x_2 = 1$$, $$x_1 \geq 0$$
3. **Dual Feasibility:** $$\lambda \geq 0$$
4. **Complementary Slackness:** $$\lambda \cdot (-x_1) = 0$$

**Kiểm tra $$x^{(1)} = (0.5,0.5)$$, $$\nu=1$$, $$\lambda=0$$:**
- Stationarity: $$2(0.5)-1-0=0$$ ✓, $$2(0.5)-1=0$$ ✓
- Primal Feasibility: $$0.5+0.5=1$$ ✓, $$0.5 \geq 0$$ ✓
- Dual Feasibility: $$0 \geq 0$$ ✓
- Comp. Slackness: $$0 \cdot (-0.5)=0$$ ✓

**Thỏa mãn!** Giá trị: $$f^{(1)} = 0.5$$

**Kiểm tra $$x^{(2)} = (0,1)$$, $$\nu=2$$, $$\lambda=2$$:**
- Stationarity: $$0-2-2=-4 \neq 0$$ ✗ (thành phần thứ hai: $$2-2=0$$ ✓)
- Primal Feasibility: $$0+1=1$$ ✓, $$0 \geq 0$$ ✓
- Dual Feasibility: $$2 \geq 0$$ ✓
- Comp. Slackness: $$2 \cdot 0=0$$ ✓

**Không thỏa mãn!** Thực tế, với $$x^{(2)}$$ thì $$\nu=2x_2=2$$ và $$\lambda = 2x_1-\nu = -2 < 0$$: không có multiplier hợp lệ nào, nên $$(0,1)$$ không phải điểm KKT. (Giá trị $$f^{(2)} = 1 > f^{(1)}$$ cũng phù hợp.)

**Kết luận:** Chỉ $$x^* = (0.5,0.5)$$ là điểm KKT.

**Giải thích:** Bài toán lồi nên KKT đủ cho global optimum, do đó $$x^* = (0.5,0.5)$$ là nghiệm tối ưu duy nhất.

</details>

---

### **Bài tập 2: QP đơn giản (Nocedal & Wright, Ex. 12.1)**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2}(x_1^2 + x_2^2) \\
\text{s.t.} \quad & x_1 + x_2 = 1 \\
& x_1, x_2 \geq 0
\end{align}
$$

**Yêu cầu:** Giải bằng phương pháp active set.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**3 trường hợp active set** (với $$L = \frac{1}{2}\|x\|^2 - \nu(x_1+x_2-1) - \lambda_1x_1 - \lambda_2x_2$$, stationarity: $$x_i = \nu + \lambda_i$$):

**TH1:** Không có ràng buộc $$\geq 0$$ active ($$\lambda_1=\lambda_2=0$$)

Từ stationarity: $$x_1=\nu$$, $$x_2=\nu$$  
Từ $$x_1+x_2=1$$: $$2\nu=1 \Rightarrow \nu=0.5$$

→ $$x=(0.5, 0.5)$$, $$f=0.25$$, feasible ✓

**TH2:** $$x_1=0$$ active

$$x_2=1$$, stationarity cho $$x_2$$: $$\nu=1$$  
Stationarity cho $$x_1$$: $$\lambda_1 = x_1 - \nu = -1 < 0$$ ✗

→ $$x=(0,1)$$ khả thi nhưng **vi phạm dual feasibility**, không phải điểm KKT ($$f=0.5$$)

**TH3:** $$x_2=0$$ active

→ tương tự, $$\lambda_2 = -1 < 0$$ ✗, $$x=(1,0)$$ ($$f=0.5$$) không phải điểm KKT

**Nghiệm tối ưu:** $$x^*=(0.5,0.5)$$ với $$f^*=0.25$$

</details>

---

## 📝 **Phần II: Ứng dụng Portfolio Optimization**

### **Bài tập 3: Markowitz Mean-Variance**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2} x^T \Sigma x \\
\text{s.t.} \quad & \mu^T x \geq r_{\min} \\
& \mathbf{1}^T x = 1 \\
& x \geq 0
\end{align}
$$

Với $$n=3$$:

$$
\Sigma = \begin{bmatrix} 0.04 & 0.01 & 0 \\ 0.01 & 0.09 & 0.02 \\ 0 & 0.02 & 0.16 \end{bmatrix}, \quad
\mu = \begin{bmatrix} 0.10 \\ 0.15 \\ 0.08 \end{bmatrix}, \quad
r_{\min} = 0.12
$$

**Yêu cầu:** Thử giả thiết $$x_3=0$$ (chỉ đầu tư vào tài sản 1, 2): tìm $$x_1, x_2$$ và các dual variables, rồi kiểm tra các điều kiện KKT.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Giả sử:** $$x_3=0$$ ($$\nu_{2,3} > 0$$), $$x_1,x_2>0$$, ràng buộc return chặt ($$\lambda>0$$)

**Ràng buộc:**
$$
\begin{cases}
x_1 + x_2 = 1 \\
0.10x_1 + 0.15x_2 = 0.12
\end{cases}
$$

Từ phương trình 2: $$0.10x_1 + 0.15x_2 = 0.12$$  
Thế $$x_1 = 1-x_2$$:

$$
0.10(1-x_2) + 0.15x_2 = 0.12 \\
0.10 + 0.05x_2 = 0.12 \\
x_2 = 0.4
$$

→ $$x_1 = 0.6$$

**Nghiệm:** $$x^* = (0.6, 0.4, 0)^T$$

**Kiểm tra dual variables từ stationarity** (với $$L = \frac{1}{2}x^T\Sigma x - \lambda(\mu^Tx - r_{\min}) - \nu_1(\mathbf{1}^Tx-1) - \nu_2^Tx$$, nên $$\Sigma x = \lambda\mu + \nu_1\mathbf{1} + \nu_2$$):

$$\Sigma x^* = \begin{bmatrix} 0.028 \\ 0.042 \\ 0.008 \end{bmatrix}$$

Với $$\nu_{2,1}=\nu_{2,2}=0$$:

$$
\begin{cases}
0.028 = 0.10\lambda + \nu_1 \\
0.042 = 0.15\lambda + \nu_1
\end{cases}
$$

Trừ: $$0.014 = 0.05\lambda \Rightarrow \lambda = 0.28$$  
→ $$\nu_1 = 0.028 - 0.028 = 0$$

Từ phương trình 3:
$$\nu_{2,3} = 0.008 - 0.08(0.28) - 0 = -0.0144 < 0$$ ✗

**Kết luận:** Dual feasibility ($$\nu_2 \geq 0$$) bị vi phạm, nên giả thiết $$x_3=0$$ **sai**: tài sản 3 (ít tương quan với tài sản 1) vẫn nên được đầu tư một lượng nhỏ nhờ hiệu ứng đa dạng hóa.

**Giải lại với cả 3 tài sản active** ($$x_i>0$$, ràng buộc return chặt): giải hệ $$\Sigma x = \lambda\mu + \nu_1\mathbf{1}$$, $$\mu^Tx=0.12$$, $$\mathbf{1}^Tx=1$$ cho

$$x^* \approx (0.522,\ 0.422,\ 0.056)^T, \quad \lambda^* \approx 0.385, \quad \nu_1^* \approx -0.0134$$

Kiểm tra thành phần 3: $$(\Sigma x^*)_3 \approx 0.0174 = 0.08(0.385) - 0.0134$$ ✓. Phương sai $$\frac{1}{2}x^{*T}\Sigma x^* \approx 0.0164$$ ($$\sigma \approx 0.181$$), thấp hơn $$0.0168$$ ($$\sigma \approx 0.183$$) của $$(0.6, 0.4, 0)$$.

**Ý nghĩa:**
- $$\lambda^*\approx 0.385$$: Shadow price của ràng buộc return (tăng $$r_{\min}$$ thêm $$0.001$$ → $$\frac{1}{2}x^T\Sigma x$$ tăng khoảng $$0.000385$$)
- $$x_3^* \approx 0.056 > 0$$: Tài sản 3 có return thấp nhưng giúp giảm rủi ro nhờ đa dạng hóa

</details>

---

## 📝 **Phần III: Support Vector Machines**

### **Bài tập 4: SVM Hard-Margin (Boyd & Vandenberghe, Ex. 8.6)**

**Dữ liệu:**
- Lớp +1: $$(1,2)$$, $$(2,3)$$, $$(3,3)$$
- Lớp -1: $$(1,1)$$, $$(2,1)$$, $$(3,2)$$

**Primal:**

$$
\begin{align}
\min_{w,b} \quad & \frac{1}{2}\|w\|^2 \\
\text{s.t.} \quad & y_i(w^Tx_i + b) \geq 1, \quad i=1,\ldots,6
\end{align}
$$

**Dual:**

$$
\begin{align}
\max_{\alpha} \quad & \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i\alpha_j y_iy_j x_i^Tx_j \\
\text{s.t.} \quad & \sum_i \alpha_i y_i = 0 \\
& \alpha_i \geq 0
\end{align}
$$

**Yêu cầu:** Xác định support vectors và hyperplane.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Quan sát hình học:** Hai lớp tách được tuyến tính. Support vectors là các điểm nằm trên biên margin.

**Nghiệm (giải bằng solver QP, rồi kiểm tra lại bằng KKT):**
- Support vectors: $$x_1=(1,2)$$ (lớp +1), $$x_3=(3,3)$$ (lớp +1), $$x_6=(3,2)$$ (lớp -1)
- $$\alpha_1^* = 0.5$$, $$\alpha_3^* = 2$$, $$\alpha_6^* = 2.5$$
- Các $$\alpha$$ khác = 0

Kiểm tra: $$\sum_i \alpha_i y_i = 0.5 + 2 - 2.5 = 0$$ ✓

**Tính $$w^*$$:**

$$
w^* = \sum_i \alpha_i^* y_i x_i = 0.5(1,2) + 2(3,3) - 2.5(3,2)
$$

$$
= (0.5,1.0) + (6,6) - (7.5,5) = (-1, 2)
$$

**Tính $$b^*$$ từ SV $$x_1$$:**

$$y_1(w^{*T}x_1 + b^*) = 1$$

$$1 \cdot ((-1)(1) + (2)(2) + b^*) = 1$$

$$3 + b^* = 1 \Rightarrow b^* = -2$$

**Decision boundary:** $$-x_1 + 2x_2 - 2 = 0$$ hay $$x_2 = \frac{x_1+2}{2}$$

**Kiểm tra margin:** $$y_i(w^{*T}x_i+b^*) = 1, 2, 1, 1, 2, 1$$ cho 6 điểm (đều $$\geq 1$$, bằng 1 tại các SV) ✓. Độ rộng margin: $$\frac{2}{\|w^*\|} = \frac{2}{\sqrt{5}} \approx 0.894$$.

</details>

---

## 📝 **Phần IV: Water-Filling Algorithm**

### **Bài tập 5: Power Allocation (Boyd & Vandenberghe, Ex. 5.7)**

$$
\begin{align}
\max_{p} \quad & \sum_{i=1}^n \log(1 + p_i/\sigma_i^2) \\
\text{s.t.} \quad & \sum_i p_i \leq P_{\text{total}} \\
& p_i \geq 0
\end{align}
$$

Với $$n=4$$, $$\sigma^2=(1,2,3,4)$$, $$P_{\text{total}}=10$$.

**Yêu cầu:** Suy ra công thức water-filling và tính nghiệm.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Điều kiện KKT (chuyển về min):**

Lagrangian: $$L = -\sum \log(1+p_i/\sigma_i^2) + \lambda(\sum p_i - P) - \sum \mu_i p_i$$

Stationarity: $$\frac{\partial L}{\partial p_i} = -\frac{1}{\sigma_i^2 + p_i} + \lambda - \mu_i = 0$$

**Phân tích:**

- Nếu $$p_i > 0$$: $$\mu_i=0 \Rightarrow \frac{1}{\sigma_i^2+p_i}=\lambda \Rightarrow p_i = \frac{1}{\lambda}-\sigma_i^2$$
- Nếu $$p_i = 0$$: $$\mu_i \geq 0 \Rightarrow \sigma_i^2 \geq \frac{1}{\lambda}$$

**Công thức water-filling:**

$$
\boxed{p_i^* = \max\left(0, \frac{1}{\lambda^*} - \sigma_i^2\right)}
$$

với $$\lambda^*$$ sao cho $$\sum p_i^* = P_{\text{total}}$$.

---

**Tính nghiệm:**

Giả sử tất cả kênh active:

$$
\sum_{i=1}^4 \left(\frac{1}{\lambda}-\sigma_i^2\right) = 10
$$

$$
\frac{4}{\lambda} - (1+2+3+4) = 10
$$

$$
\frac{4}{\lambda} = 20 \Rightarrow \lambda = 0.2
$$

**Water level:** $$\frac{1}{\lambda} = 5$$

**Công suất:**
- $$p_1 = 5-1 = 4$$ ✓
- $$p_2 = 5-2 = 3$$ ✓
- $$p_3 = 5-3 = 2$$ ✓
- $$p_4 = 5-4 = 1$$ ✓

**Tổng:** $$4+3+2+1=10$$ ✓

**Nghiệm:** $$p^* = (4,3,2,1)$$

**Giải thích Water Level:**

```
Water level = 5
|     |     |     |
|  4  |  3  |  2  |  1  |  ← Công suất
+-----+-----+-----+-----+
|  1  |  2  |  3  |  4  |  ← Noise floor
+-----+-----+-----+-----+
  p₁    p₂    p₃    p₄
```

Kênh tốt (noise thấp) nhận nhiều công suất hơn!

**Capacity:** 

$$C = \sum \log_2(1+p_i^*/\sigma_i^2) \approx 4.70 \text{ bits/s/Hz}$$

</details>

---

## 📝 **Phần V: Bài tập Nâng cao**

### **Bài tập 6: Constrained Least Squares (Bertsekas, Ex. 3.2.2)**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2}\|Ax-b\|^2 \\
\text{s.t.} \quad & Cx = d \\
& x \geq 0
\end{align}
$$

Với:

$$
A = \begin{bmatrix} 1&1\\1&-1\\2&0 \end{bmatrix}, \quad
b = \begin{bmatrix} 2\\0\\3 \end{bmatrix}, \quad
C = [1\ 1], \quad
d = 2
$$

**Yêu cầu:** Giải bằng KKT.

<details>
<summary><strong>💡 Lời giải</strong></summary>

$$\nabla f(x) = A^TAx - A^Tb$$

$$
A^TA = \begin{bmatrix} 6&0\\0&2 \end{bmatrix}, \quad
A^Tb = \begin{bmatrix} 8\\2 \end{bmatrix}
$$

**KKT system (không có $$x \geq 0$$):**

$$
\begin{bmatrix} 6&0&-1\\0&2&-1\\1&1&0 \end{bmatrix}
\begin{bmatrix} x_1\\x_2\\\nu \end{bmatrix} =
\begin{bmatrix} 8\\2\\2 \end{bmatrix}
$$

Giải:
- Từ (3): $$x_1+x_2=2$$
- Từ (1), (2): $$x_1=\frac{8+\nu}{6}$$, $$x_2=\frac{2+\nu}{2}$$, thế vào (3): $$14+4\nu=12 \Rightarrow \nu=-0.5$$
- $$x_1=1.25$$, $$x_2=0.75$$

**Kiểm tra $$x \geq 0$$:** $$x_1=1.25>0$$, $$x_2=0.75>0$$ ✓

**Kiểm tra $$\lambda$$:**

$$\lambda = A^TAx - A^Tb - C^T\nu = \begin{bmatrix} 7.5-8+0.5\\1.5-2+0.5 \end{bmatrix} = \begin{bmatrix} 0\\0 \end{bmatrix} \geq 0$$ ✓

**Nghiệm:** $$x^*=(1.25, 0.75)^T$$, $$Ax^*-b=(0,0.5,-0.5)^T$$, $$f^*=\frac{1}{2}(0.25+0.25)=0.25$$

</details>

---

### **Bài tập 7: Penalty Method (Nocedal & Wright, Ex. 17.1)**

$$
\begin{align}
\min_{x} \quad & x_1 + x_2 \\
\text{s.t.} \quad & x_1^2 + x_2^2 = 1
\end{align}
$$

**Penalty:** $$\min \phi(x;\mu) = x_1+x_2 + \frac{\mu}{2}(x_1^2+x_2^2-1)^2$$

**Yêu cầu:** Giải bằng KKT, tính nghiệm penalty với $$\mu=1,10,100$$, phân tích hội tụ.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Giải bằng KKT:**

Lagrangian: $$L = x_1+x_2 - \nu(x_1^2+x_2^2-1)$$

Stationarity: $$1-2\nu x_1=0$$, $$1-2\nu x_2=0$$ → $$x_1=x_2=\frac{1}{2\nu}$$

Feasibility: $$\frac{1}{4\nu^2}+\frac{1}{4\nu^2}=1 \Rightarrow \nu = \pm\frac{1}{\sqrt{2}}$$

**Hai nghiệm KKT:**
1. $$x=(1/\sqrt{2}, 1/\sqrt{2})$$, $$f=\sqrt{2}$$
2. $$x=(-1/\sqrt{2}, -1/\sqrt{2})$$, $$f=-\sqrt{2}$$

**Tối ưu (min):** $$x^* = (-1/\sqrt{2}, -1/\sqrt{2})$$

---

**Penalty method:**

FOC: $$1 + 2\mu x_i(x_1^2+x_2^2-1)=0$$

Với $$x_1=x_2=x$$: $$1 + 2\mu x(2x^2-1)=0$$ hay $$4\mu x^3 - 2\mu x + 1=0$$

**Nghiệm số** (lấy nghiệm thực âm của phương trình bậc ba, có $$\phi$$ nhỏ nhất; với $$\mu$$ lớn phương trình còn nghiệm dương ứng với một cực tiểu địa phương gần điểm KKT cực đại, có $$\phi$$ lớn hơn):
- $$\mu=1$$: $$x \approx -0.885$$ ($$x_1^2+x_2^2-1 \approx 0.57$$, vi phạm ràng buộc khá nhiều)
- $$\mu=10$$: $$x \approx -0.731$$ ($$x_1^2+x_2^2-1 \approx 0.07$$)
- $$\mu=100$$: $$x \approx -0.710$$ ($$x_1^2+x_2^2-1 \approx 0.007$$) $$\to -1/\sqrt{2} \approx -0.7071$$

**Hội tụ:** Khi $$\mu \to \infty$$, nghiệm penalty hội tụ đến nghiệm KKT (từ phía **ngoài** tập khả thi, vì $$x_1^2+x_2^2>1$$)!

**Mối liên hệ:** $$\nu \approx -\mu(x_1^2+x_2^2-1)$$ (với quy ước $$L = f - \nu h$$; ví dụ $$\mu=100$$: $$\nu \approx -100 \cdot 0.007 \approx -0.7 \approx -1/\sqrt{2}$$ ✓)

</details>

---

## 💡 **Tổng kết Chiến lược**

### **Kiểm chứng KKT:**
- Kiểm tra **4 điều kiện** riêng biệt
- KKT **cần** cho local optimum (với CQ), **đủ** cho global optimum (bài toán lồi)

### **Giải bằng KKT:**
- **Active set strategy:** Thử các trường hợp active set
- Giải hệ KKT từ stationarity + active constraints
- Kiểm tra feasibility và so sánh objective

### **Complementary Slackness:**
- $$\lambda_i > 0 \Rightarrow$$ ràng buộc $$i$$ active
- **Shadow price:** $$\lambda_i^*$$ = giá trị biên của ràng buộc $$i$$

### **Bài toán lồi:**
- KKT đủ → một KKT point là global optimal
- Strong duality: $$f^*=g^*$$

---

## 📚 **Tài liệu Tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 5.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization* (2nd ed.). Springer. Chapters 12, 16-17.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming* (2nd ed.). Athena Scientific. Chapter 3.

4. **Luenberger, D. G., & Ye, Y.** (2008). *Linear and Nonlinear Programming* (3rd ed.). Springer. Chapter 10.

5. **Bazaraa, M. S., Sherali, H. D., & Shetty, C. M.** (2006). *Nonlinear Programming: Theory and Algorithms* (3rd ed.). Wiley.


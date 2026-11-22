---
layout: post
title: 12-09 Bài Tập Thực Hành - Điều Kiện KKT
chapter: '12'
order: 10
owner: GitHub Copilot
lang: vi
categories:
- chapter12
lesson_type: required
redirect_from:
  - /contents/vi/chapter12/12_08_Practical_Exercises_KKT_Conditions/
---

# Bài tập thực hành - Điều kiện KKT (Karush–Kuhn–Tucker)

Các bài tập dưới đây được tham khảo từ Boyd & Vandenberghe (2004), Nocedal & Wright (2006) và Bertsekas (1999).

---

## 📝 **Phần I: Kiểm chứng điều kiện KKT**

### **Bài tập 1: Bài toán cơ bản (Boyd & Vandenberghe, Ex. 5.1)**

Xét bài toán tối ưu:

$$
\begin{align}
\min_{x} \quad & x_1^2 + x_2^2 \\
\text{s.t.} \quad & x_1 + x_2 = 1 \\
& x_1 \geq 0
\end{align}
$$

Kiểm tra hai điểm ứng viên sau:
1. $$x^{(1)} = (0.5, 0.5)$$, $$\nu = 1$$, $$\lambda = 0$$
2. $$x^{(2)} = (0, 1)$$, $$\nu = 2$$, $$\lambda = 2$$

**Yêu cầu:** Viết hệ điều kiện KKT, kiểm tra từng điều kiện cho hai điểm trên và xác định nghiệm tối ưu.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Hàm Lagrangian:** $$L(x,\nu,\lambda) = x_1^2 + x_2^2 - \nu(x_1+x_2-1) + \lambda(-x_1)$$ (viết ràng buộc bất đẳng thức dưới dạng chuẩn $$g(x)=-x_1 \leq 0$$).

**Bốn điều kiện KKT:**

1. **Điều kiện dừng (Stationarity):** $$2x_1 - \nu - \lambda = 0$$, $$2x_2 - \nu = 0$$
2. **Tính khả thi nguyên thủy (Primal feasibility):** $$x_1 + x_2 = 1$$, $$x_1 \geq 0$$
3. **Tính khả thi đối ngẫu (Dual feasibility):** $$\lambda \geq 0$$
4. **Điều kiện bù yếu (Complementary slackness):** $$\lambda \cdot (-x_1) = 0$$

**Kiểm tra $$x^{(1)} = (0.5,0.5)$$, $$\nu=1$$, $$\lambda=0$$:**
- Điều kiện dừng: $$2(0.5)-1-0=0$$ ✓, $$2(0.5)-1=0$$ ✓
- Khả thi nguyên thủy: $$0.5+0.5=1$$ ✓, $$0.5 \geq 0$$ ✓
- Khả thi đối ngẫu: $$0 \geq 0$$ ✓
- Bù yếu: $$0 \cdot (-0.5)=0$$ ✓

Điểm này **thỏa mãn** toàn bộ điều kiện KKT, với giá trị mục tiêu $$f^{(1)} = 0.5$$.

**Kiểm tra $$x^{(2)} = (0,1)$$, $$\nu=2$$, $$\lambda=2$$:**
- Điều kiện dừng: $$0-2-2=-4 \neq 0$$ ✗ (thành phần thứ hai: $$2-2=0$$ ✓)
- Khả thi nguyên thủy: $$0+1=1$$ ✓, $$0 \geq 0$$ ✓
- Khả thi đối ngẫu: $$2 \geq 0$$ ✓
- Bù yếu: $$2 \cdot 0=0$$ ✓

Điểm này **không thỏa mãn** điều kiện dừng. Thực tế, tại $$x^{(2)}$$ ta buộc phải có $$\nu=2x_2=2$$ và $$\lambda = 2x_1-\nu = -2 < 0$$, nên không tồn tại nhân tử đối ngẫu hợp lệ nào; do đó $$(0,1)$$ không phải là điểm KKT (giá trị mục tiêu $$f^{(2)} = 1 > f^{(1)}$$ cũng phản ánh điều này).

**Kết luận:** Chỉ có $$x^* = (0.5,0.5)$$ là điểm KKT. Vì bài toán là bài toán lồi nên điều kiện KKT là điều kiện đủ cho cực tiểu toàn cục; do đó $$x^* = (0.5,0.5)$$ là nghiệm tối ưu duy nhất.

</details>

---

### **Bài tập 2: Quy hoạch bậc hai đơn giản (Nocedal & Wright, Ex. 12.1)**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2}(x_1^2 + x_2^2) \\
\text{s.t.} \quad & x_1 + x_2 = 1 \\
& x_1, x_2 \geq 0
\end{align}
$$

**Yêu cầu:** Giải bài toán bằng phương pháp tập ràng buộc tích cực (active set).

<details>
<summary><strong>💡 Lời giải</strong></summary>

Với hàm Lagrangian $$L = \frac{1}{2}\|x\|^2 - \nu(x_1+x_2-1) - \lambda_1x_1 - \lambda_2x_2$$, điều kiện dừng cho $$x_i = \nu + \lambda_i$$ ($$i=1,2$$). Ta xét 3 trường hợp của tập ràng buộc tích cực:

**Trường hợp 1:** Không có ràng buộc bất đẳng thức nào tích cực ($$\lambda_1=\lambda_2=0$$).

Từ điều kiện dừng: $$x_1=\nu$$, $$x_2=\nu$$.  
Thay vào $$x_1+x_2=1$$: $$2\nu=1 \Rightarrow \nu=0.5$$.

Thu được $$x=(0.5, 0.5)$$, $$f=0.25$$, thỏa mãn toàn bộ điều kiện khả thi và KKT ✓.

**Trường hợp 2:** Ràng buộc $$x_1=0$$ tích cực ($$\lambda_2=0$$).

Khi đó $$x_2=1$$; từ điều kiện dừng cho $$x_2$$ suy ra $$\nu=1$$.  
Từ điều kiện dừng cho $$x_1$$ suy ra $$\lambda_1 = x_1 - \nu = -1 < 0$$ ✗.

Điểm $$x=(0,1)$$ khả thi nguyên thủy nhưng **vi phạm tính khả thi đối ngẫu**, nên không phải điểm KKT ($$f=0.5$$).

**Trường hợp 3:** Ràng buộc $$x_2=0$$ tích cực ($$\lambda_1=0$$).

Tương tự, ta có $$\lambda_2 = -1 < 0$$ ✗, nên $$x=(1,0)$$ ($$f=0.5$$) không phải điểm KKT.

**Nghiệm tối ưu:** $$x^*=(0.5,0.5)$$ với giá trị tối ưu $$f^*=0.25$$.

</details>

---

## 📝 **Phần II: Ứng dụng tối ưu hóa danh mục đầu tư**

### **Bài tập 3: Mô hình Markowitz Mean–Variance**

$$
\begin{align}
\min_{x} \quad & \frac{1}{2} x^T \Sigma x \\
\text{s.t.} \quad & \mu^T x \geq r_{\min} \\
& \mathbf{1}^T x = 1 \\
& x \geq 0
\end{align}
$$

Cho $$n=3$$ với:

$$
\Sigma = \begin{bmatrix} 0.04 & 0.01 & 0 \\ 0.01 & 0.09 & 0.02 \\ 0 & 0.02 & 0.16 \end{bmatrix}, \quad
\mu = \begin{bmatrix} 0.10 \\ 0.15 \\ 0.08 \end{bmatrix}, \quad
r_{\min} = 0.12
$$

**Yêu cầu:** Thử giả thiết $$x_3=0$$ (chỉ phân bổ vốn vào tài sản 1 và 2): tìm $$x_1, x_2$$ cùng các biến đối ngẫu tương ứng, sau đó kiểm tra các điều kiện KKT.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Giả thiết thử:** $$x_3=0$$ ($$\nu_{2,3} > 0$$), $$x_1,x_2>0$$, và ràng buộc lợi suất kỳ vọng đang chặt ($$\lambda>0$$).

**Hệ ràng buộc:**
$$
\begin{cases}
x_1 + x_2 = 1 \\
0.10x_1 + 0.15x_2 = 0.12
\end{cases}
$$

Thế $$x_1 = 1-x_2$$ vào phương trình thứ hai:

$$
0.10(1-x_2) + 0.15x_2 = 0.12 \\
0.10 + 0.05x_2 = 0.12 \\
x_2 = 0.4
$$

Suy ra $$x_1 = 0.6$$, tức điểm ứng viên là $$x^* = (0.6, 0.4, 0)^T$$.

**Kiểm tra biến đối ngẫu từ điều kiện dừng:** Với hàm Lagrangian $$L = \frac{1}{2}x^T\Sigma x - \lambda(\mu^Tx - r_{\min}) - \nu_1(\mathbf{1}^Tx-1) - \nu_2^Tx$$, điều kiện dừng cho $$\Sigma x = \lambda\mu + \nu_1\mathbf{1} + \nu_2$$.

Tính tích ma trận–vector:

$$\Sigma x^* = \begin{bmatrix} 0.028 \\ 0.042 \\ 0.008 \end{bmatrix}$$

Vì $$x_1, x_2 > 0$$ nên $$\nu_{2,1}=\nu_{2,2}=0$$, ta có hệ:

$$
\begin{cases}
0.028 = 0.10\lambda + \nu_1 \\
0.042 = 0.15\lambda + \nu_1
\end{cases}
$$

Trừ hai phương trình: $$0.014 = 0.05\lambda \Rightarrow \lambda = 0.28$$, suy ra $$\nu_1 = 0.028 - 0.028 = 0$$.

Từ phương trình thứ ba:
$$\nu_{2,3} = 0.008 - 0.08(0.28) - 0 = -0.0144 < 0$$ ✗

**Kết luận:** Tính khả thi đối ngẫu ($$\nu_2 \geq 0$$) bị vi phạm, nên giả thiết $$x_3=0$$ **không đúng**: tài sản 3 (ít tương quan với tài sản 1) vẫn nên được phân bổ một tỷ trọng nhỏ nhờ hiệu ứng đa dạng hóa rủi ro.

**Giải lại khi cả 3 tài sản đều có tỷ trọng dương** ($$x_i>0$$, ràng buộc lợi suất đang chặt): giải hệ $$\Sigma x = \lambda\mu + \nu_1\mathbf{1}$$, $$\mu^Tx=0.12$$, $$\mathbf{1}^Tx=1$$ thu được:

$$x^* \approx (0.522,\ 0.422,\ 0.056)^T, \quad \lambda^* \approx 0.385, \quad \nu_1^* \approx -0.0134$$

Kiểm tra thành phần thứ ba: $$(\Sigma x^*)_3 \approx 0.0174 = 0.08(0.385) - 0.0134$$ ✓. Giá trị hàm mục tiêu $$\frac{1}{2}x^{*T}\Sigma x^* \approx 0.0164$$ (tương ứng độ lệch chuẩn $$\sigma \approx 0.181$$), thấp hơn mức $$0.0168$$ ($$\sigma \approx 0.183$$) của danh mục $$(0.6, 0.4, 0)$$.

**Ý nghĩa kinh tế:**
- $$\lambda^*\approx 0.385$$ là giá bóng (shadow price) của ràng buộc lợi suất: nếu tăng $$r_{\min}$$ thêm $$0.001$$ thì giá trị $$\frac{1}{2}x^T\Sigma x$$ tăng xấp xỉ $$0.000385$$.
- $$x_3^* \approx 0.056 > 0$$ cho thấy dù tài sản 3 có lợi suất kỳ vọng thấp hơn, nó vẫn giúp giảm phương sai danh mục nhờ đa dạng hóa.

</details>

---

## 📝 **Phần III: Máy vector hỗ trợ (Support Vector Machines)**

### **Bài tập 4: Hard-Margin SVM (Boyd & Vandenberghe, Ex. 8.6)**

**Dữ liệu:**
- Lớp $$+1$$: $$(1,2)$$, $$(2,3)$$, $$(3,3)$$
- Lớp $$-1$$: $$(1,1)$$, $$(2,1)$$, $$(3,2)$$

**Bài toán nguyên thủy (Primal):**

$$
\begin{align}
\min_{w,b} \quad & \frac{1}{2}\|w\|^2 \\
\text{s.t.} \quad & y_i(w^Tx_i + b) \geq 1, \quad i=1,\ldots,6
\end{align}
$$

**Bài toán đối ngẫu (Dual):**

$$
\begin{align}
\max_{\alpha} \quad & \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i\alpha_j y_iy_j x_i^Tx_j \\
\text{s.t.} \quad & \sum_i \alpha_i y_i = 0 \\
& \alpha_i \geq 0
\end{align}
$$

**Yêu cầu:** Xác định các vector hỗ trợ và siêu phẳng phân cách tối ưu.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Quan sát hình học:** Hai lớp dữ liệu tách được tuyến tính; các vector hỗ trợ là những điểm nằm đúng trên biên của lề.

**Nghiệm đối ngẫu (giải bằng bộ giải QP rồi kiểm chứng lại bằng KKT):**
- Các vector hỗ trợ có $$\alpha_i^* > 0$$: $$x_1=(1,2)$$ (lớp $$+1$$), $$x_3=(3,3)$$ (lớp $$+1$$), $$x_6=(3,2)$$ (lớp $$-1$$)
- $$\alpha_1^* = 0.5$$, $$\alpha_3^* = 2$$, $$\alpha_6^* = 2.5$$; các $$\alpha_i^*$$ còn lại bằng $$0$$

Kiểm tra ràng buộc cân bằng: $$\sum_i \alpha_i y_i = 0.5 + 2 - 2.5 = 0$$ ✓.

**Tính $$w^*$$:**

$$
w^* = \sum_i \alpha_i^* y_i x_i = 0.5(1,2) + 2(3,3) - 2.5(3,2)
$$

$$
= (0.5,1.0) + (6,6) - (7.5,5) = (-1, 2)
$$

**Tính $$b^*$$ từ vector hỗ trợ $$x_1$$:**

$$y_1(w^{*T}x_1 + b^*) = 1$$

$$1 \cdot ((-1)(1) + (2)(2) + b^*) = 1$$

$$3 + b^* = 1 \Rightarrow b^* = -2$$

**Siêu phẳng phân cách:** $$-x_1 + 2x_2 - 2 = 0$$, hay $$x_2 = \frac{x_1+2}{2}$$.

**Kiểm tra lề:** Giá trị $$y_i(w^{*T}x_i+b^*)$$ lần lượt bằng $$1, 2, 1, 1, 2, 1$$ cho 6 điểm (đều $$\geq 1$$ và bằng $$1$$ tại các vector hỗ trợ) ✓. Độ rộng lề là $$\frac{2}{\|w^*\|} = \frac{2}{\sqrt{5}} \approx 0.894$$.

</details>

---

## 📝 **Phần IV: Thuật toán Water-Filling**

### **Bài tập 5: Phân bổ công suất (Boyd & Vandenberghe, Ex. 5.7)**

$$
\begin{align}
\max_{p} \quad & \sum_{i=1}^n \log(1 + p_i/\sigma_i^2) \\
\text{s.t.} \quad & \sum_i p_i \leq P_{\text{total}} \\
& p_i \geq 0
\end{align}
$$

Cho $$n=4$$, $$\sigma^2=(1,2,3,4)$$ và $$P_{\text{total}}=10$$.

**Yêu cầu:** Suy ra công thức water-filling từ điều kiện KKT và tính nghiệm cụ thể.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Điều kiện KKT (đưa về bài toán cực tiểu hóa):**

Hàm Lagrangian: $$L = -\sum \log(1+p_i/\sigma_i^2) + \lambda(\sum p_i - P) - \sum \mu_i p_i$$

Điều kiện dừng: $$\frac{\partial L}{\partial p_i} = -\frac{1}{\sigma_i^2 + p_i} + \lambda - \mu_i = 0$$

**Phân tích hai trường hợp:**

- Nếu $$p_i > 0$$: theo điều kiện bù yếu $$\mu_i=0 \Rightarrow \frac{1}{\sigma_i^2+p_i}=\lambda \Rightarrow p_i = \frac{1}{\lambda}-\sigma_i^2$$.
- Nếu $$p_i = 0$$: vì $$\mu_i \geq 0$$ nên $$\sigma_i^2 \geq \frac{1}{\lambda}$$.

**Công thức water-filling:**

$$
\boxed{p_i^* = \max\left(0, \frac{1}{\lambda^*} - \sigma_i^2\right)}
$$

trong đó $$\lambda^*$$ được xác định sao cho $$\sum p_i^* = P_{\text{total}}$$.

---

**Tính nghiệm số:**

Giả sử cả 4 kênh đều được cấp công suất dương:

$$
\sum_{i=1}^4 \left(\frac{1}{\lambda}-\sigma_i^2\right) = 10
$$

$$
\frac{4}{\lambda} - (1+2+3+4) = 10
$$

$$
\frac{4}{\lambda} = 20 \Rightarrow \lambda = 0.2
$$

**Mực nước (water level):** $$\frac{1}{\lambda} = 5$$.

**Công suất phân bổ cho từng kênh:**
- $$p_1 = 5-1 = 4$$ ✓
- $$p_2 = 5-2 = 3$$ ✓
- $$p_3 = 5-3 = 2$$ ✓
- $$p_4 = 5-4 = 1$$ ✓

Kiểm tra tổng công suất: $$4+3+2+1=10$$ ✓. Vậy nghiệm tối ưu là $$p^* = (4,3,2,1)$$.

**Minh họa mực nước:**

```
Water level = 5
|     |     |     |
|  4  |  3  |  2  |  1  |  ← Công suất
+-----+-----+-----+-----+
|  1  |  2  |  3  |  4  |  ← Mức nhiễu nền
+-----+-----+-----+-----+
  p₁    p₂    p₃    p₄
```

Kênh có mức nhiễu nền thấp hơn (chất lượng tốt hơn) nhận được nhiều công suất hơn.

**Tổng dung lượng kênh:**

$$C = \sum \log_2(1+p_i^*/\sigma_i^2) \approx 4.70 \text{ bits/s/Hz}$$

</details>

---

## 📝 **Phần V: Bài tập nâng cao**

### **Bài tập 6: Bình phương tối thiểu có ràng buộc (Bertsekas, Ex. 3.2.2)**

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

**Yêu cầu:** Giải bài toán bằng điều kiện KKT.

<details>
<summary><strong>💡 Lời giải</strong></summary>

Ta có $$\nabla f(x) = A^TAx - A^Tb$$, với:

$$
A^TA = \begin{bmatrix} 6&0\\0&2 \end{bmatrix}, \quad
A^Tb = \begin{bmatrix} 8\\2 \end{bmatrix}
$$

**Giải thử hệ KKT khi bỏ qua ràng buộc $$x \geq 0$$ (tức giả sử $$\lambda = 0$$):**

$$
\begin{bmatrix} 6&0&-1\\0&2&-1\\1&1&0 \end{bmatrix}
\begin{bmatrix} x_1\\x_2\\\nu \end{bmatrix} =
\begin{bmatrix} 8\\2\\2 \end{bmatrix}
$$

Giải hệ phương trình:
- Từ phương trình (3): $$x_1+x_2=2$$.
- Từ phương trình (1) và (2): $$x_1=\frac{8+\nu}{6}$$, $$x_2=\frac{2+\nu}{2}$$; thế vào (3) được $$14+4\nu=12 \Rightarrow \nu=-0.5$$.
- Suy ra $$x_1=1.25$$, $$x_2=0.75$$.

**Kiểm tra tính khả thi $$x \geq 0$$:** $$x_1=1.25>0$$, $$x_2=0.75>0$$ ✓.

**Kiểm tra nhân tử $$\lambda$$:**

$$\lambda = A^TAx - A^Tb - C^T\nu = \begin{bmatrix} 7.5-8+0.5\\1.5-2+0.5 \end{bmatrix} = \begin{bmatrix} 0\\0 \end{bmatrix} \geq 0$$ ✓

**Nghiệm tối ưu:** $$x^*=(1.25, 0.75)^T$$, phần dư $$Ax^*-b=(0,0.5,-0.5)^T$$ và giá trị tối ưu $$f^*=\frac{1}{2}(0.25+0.25)=0.25$$.

</details>

---

### **Bài tập 7: Phương pháp hàm phạt (Nocedal & Wright, Ex. 17.1)**

$$
\begin{align}
\min_{x} \quad & x_1 + x_2 \\
\text{s.t.} \quad & x_1^2 + x_2^2 = 1
\end{align}
$$

**Bài toán phạt:** $$\min \phi(x;\mu) = x_1+x_2 + \frac{\mu}{2}(x_1^2+x_2^2-1)^2$$

**Yêu cầu:** Giải bài toán gốc bằng KKT, tính nghiệm của bài toán phạt với $$\mu=1,10,100$$ và phân tích sự hội tụ.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Giải bài toán gốc bằng KKT:**

Hàm Lagrangian: $$L = x_1+x_2 - \nu(x_1^2+x_2^2-1)$$

Điều kiện dừng: $$1-2\nu x_1=0$$, $$1-2\nu x_2=0 \Rightarrow x_1=x_2=\frac{1}{2\nu}$$

Thế vào ràng buộc khả thi: $$\frac{1}{4\nu^2}+\frac{1}{4\nu^2}=1 \Rightarrow \nu = \pm\frac{1}{\sqrt{2}}$$

**Hai điểm KKT:**
1. $$x=(1/\sqrt{2}, 1/\sqrt{2})$$, giá trị mục tiêu $$f=\sqrt{2}$$ (cực đại)
2. $$x=(-1/\sqrt{2}, -1/\sqrt{2})$$, giá trị mục tiêu $$f=-\sqrt{2}$$ (cực tiểu)

**Nghiệm cực tiểu tối ưu:** $$x^* = (-1/\sqrt{2}, -1/\sqrt{2})$$.

---

**Giải bằng phương pháp hàm phạt:**

Điều kiện bậc nhất: $$1 + 2\mu x_i(x_1^2+x_2^2-1)=0$$ ($$i=1,2$$).

Với tính đối xứng $$x_1=x_2=x$$: $$1 + 2\mu x(2x^2-1)=0$$, tức $$4\mu x^3 - 2\mu x + 1=0$$.

**Nghiệm số** (chọn nghiệm thực âm của phương trình bậc ba cho giá trị $$\phi$$ nhỏ nhất; khi $$\mu$$ lớn, phương trình còn nghiệm dương tương ứng với cực tiểu địa phương gần điểm cực đại, có giá trị $$\phi$$ lớn hơn):
- $$\mu=1$$: $$x \approx -0.885$$ ($$x_1^2+x_2^2-1 \approx 0.57$$, vi phạm ràng buộc còn lớn)
- $$\mu=10$$: $$x \approx -0.731$$ ($$x_1^2+x_2^2-1 \approx 0.07$$)
- $$\mu=100$$: $$x \approx -0.710$$ ($$x_1^2+x_2^2-1 \approx 0.007$$) $$\to -1/\sqrt{2} \approx -0.7071$$

**Nhận xét về hội tụ:** Khi $$\mu \to \infty$$, nghiệm của bài toán phạt hội tụ về nghiệm KKT từ phía **ngoài** miền khả thi (vì $$x_1^2+x_2^2>1$$).

**Liên hệ với nhân tử Lagrange:** Với quy ước $$L = f - \nu h$$, ta có $$\nu \approx -\mu(x_1^2+x_2^2-1)$$ (chẳng hạn tại $$\mu=100$$, $$\nu \approx -100 \cdot 0.007 \approx -0.7 \approx -1/\sqrt{2}$$ ✓).

</details>

---

## 💡 **Tổng kết chiến lược giải bài tập**

### **Kiểm chứng điều kiện KKT**
- Kiểm tra riêng rẽ đủ **4 điều kiện** (dừng, khả thi nguyên thủy, khả thi đối ngẫu, bù yếu).
- KKT là điều kiện **cần** cho cực tiểu địa phương (khi thỏa điều kiện chuẩn ràng buộc) và là điều kiện **đủ** cho cực tiểu toàn cục đối với bài toán lồi.

### **Giải bài toán bằng KKT**
- **Chiến lược tập tích cực (active set):** Chia trường hợp dựa trên các ràng buộc bất đẳng thức đang chặt.
- Giải hệ phương trình thu được từ điều kiện dừng và các ràng buộc tích cực.
- Kiểm tra tính khả thi nguyên thủy, đối ngẫu và so sánh giá trị mục tiêu (nếu bài toán không lồi).

### **Điều kiện bù yếu**
- Nếu $$\lambda_i > 0$$ thì ràng buộc thứ $$i$$ chắc chắn đang chặt (tích cực).
- **Giá bóng (shadow price):** Nhân tử $$\lambda_i^*$$ cho biết tốc độ thay đổi biên của giá trị tối ưu khi nới lỏng ràng buộc thứ $$i$$.

### **Bài toán lồi**
- Điều kiện KKT là điều kiện đủ: mọi điểm KKT đều là nghiệm tối ưu toàn cục.
- Khi thỏa tính đối ngẫu mạnh: $$f^* = g^*$$.

---

## 📚 **Tài liệu tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 5.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization* (2nd ed.). Springer. Chapters 12, 16-17.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming* (2nd ed.). Athena Scientific. Chapter 3.

4. **Luenberger, D. G., & Ye, Y.** (2008). *Linear and Nonlinear Programming* (3rd ed.). Springer. Chapter 10.

5. **Bazaraa, M. S., Sherali, H. D., & Shetty, C. M.** (2006). *Nonlinear Programming: Theory and Algorithms* (3rd ed.). Wiley.

---
layout: post
title: 09-11 Bài Tập Thực Hành - Proximal Gradient
chapter: '09'
order: 13
owner: GitHub Copilot
lang: vi
categories:
- chapter09
lesson_type: required
---

# Bài Tập Thực Hành - Proximal Gradient

Các bài tập được tham khảo từ Parikh & Boyd (2014) và Beck & Teboulle (2009).

---

## 📝 **Bài tập 1: Bài toán LASSO với toán tử ngưỡng mềm**

Cho bài toán LASSO: $$\min \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$ với $$A = I$$, $$b = (2, -1, 0.5)^T$$, $$\lambda = 1$$.

**a)** Viết toán tử gần kề (proximal operator).  
**b)** Áp dụng toán tử ngưỡng mềm (soft-thresholding).  
**c)** Thực hiện bước lặp xuất phát từ $$x^{(0)} = 0$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Toán tử gần kề:**

$$\text{prox}_{t\lambda\|\cdot\|_1}(y) = S_{t\lambda}(y)$$

**Toán tử ngưỡng mềm:**

$$S_{\tau}(y_i) = \begin{cases}
y_i - \tau & \text{nếu } y_i > \tau \\
0 & \text{nếu } |y_i| \leq \tau \\
y_i + \tau & \text{nếu } y_i < -\tau
\end{cases}$$

**Với $$A = I$$ (hằng số Lipschitz $$L = 1$$, chọn kích thước bước $$t = 1$$):**

$$x^{(1)} = S_1(b) = (1, 0, 0)^T$$

Thuật toán hội tụ chỉ sau 1 bước.

</details>

---

## 📝 **Bài tập 2: Hoàn thiện ma trận (Matrix Completion)**

Cực tiểu hóa $$\|X\|_*$$ với ràng buộc $$X_{ij} = M_{ij}$$ tại các vị trí quan sát được.

**a)** Viết bước lặp gradient gần kề cho phiên bản chính quy hóa với $$f(X) = \frac{1}{2}\|P_\Omega(X - M)\|_F^2$$.  
**b)** Tính toán tử gần kề của chuẩn hạt nhân (nuclear norm).  
**c)** Áp dụng ngưỡng mềm theo phân tích SVD.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Toán tử gần kề của chuẩn hạt nhân:**

$$\text{prox}_{t\|\cdot\|_*}(Y) = U S_t(\Sigma) V^T$$

trong đó $$Y = U\Sigma V^T$$ là phân tích SVD của $$Y$$ và $$S_t(\sigma_i) = \max(\sigma_i - t, 0)$$.

**Công thức cập nhật:**

$$X^{(k+1)} = \text{prox}_{t\|\cdot\|_*}(X^{(k)} - t\nabla f(X^{(k)}))$$

với $$\nabla f(X) = P_\Omega(X - M)$$.

</details>

---

## 📝 **Bài tập 3: Gradient gần kề tăng tốc (FISTA)**

Cho bài toán tổng hợp $$f(x) + g(x)$$ với $$f$$ trơn và $$g$$ không trơn.

**a)** Viết công thức cập nhật của FISTA.  
**b)** So sánh tốc độ hội tụ với phương pháp gradient gần kề tiêu chuẩn.  
**c)** Nêu cách áp dụng cho bài toán LASSO.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Công thức cập nhật FISTA:**

$$
\begin{align}
y^{(k)} &= x^{(k)} + \frac{k-1}{k+2}(x^{(k)} - x^{(k-1)}) \\
x^{(k+1)} &= \text{prox}_{tg}(y^{(k)} - t\nabla f(y^{(k)}))
\end{align}
$$

**So sánh tốc độ hội tụ:**
- Gradient gần kề tiêu chuẩn: $$O(1/k)$$ (cần $$O(1/\epsilon)$$ bước để đạt sai số $$\epsilon$$).
- FISTA: $$O(1/k^2)$$ (chỉ cần $$O(1/\sqrt{\epsilon})$$ bước để đạt sai số $$\epsilon$$).

Với bài toán LASSO, ta thay $$\nabla f(y) = A^T(Ay - b)$$ và $$\text{prox}_{tg}$$ bằng toán tử ngưỡng mềm $$S_{t\lambda}$$.

</details>

---

## 📝 **Bài tập 4: Tính các toán tử gần kề cơ bản**

Tính toán tử gần kề cho các hàm sau:

**a)** $$g(x) = \|x\|_2$$  
**b)** $$g(x) = I_C(x)$$ (hàm chỉ thị của tập lồi đóng $$C$$)  
**c)** $$g(x) = \frac{1}{2}x^TQx$$ (với $$Q$$ đối xứng nửa xác định dương)

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Chuẩn $$\ell_2$$:**

$$\text{prox}_{t\|\cdot\|_2}(y) = \begin{cases}
\left(1 - \frac{t}{\|y\|}\right)y & \text{nếu } \|y\| > t \\
0 & \text{trường hợp khác}
\end{cases}$$

**b) Hàm chỉ thị:**

$$\text{prox}_{tI_C}(y) = \Pi_C(y)$$ (phép chiếu Euclid lên tập $$C$$).

**c) Hàm bậc hai:**

$$\text{prox}_{tg}(y) = (I + tQ)^{-1}y$$

</details>

---

## 📝 **Bài tập 5: Gradient gần kề đối ngẫu**

Cho bài toán $$\min c^Tx$$ với ràng buộc $$Ax = b, x \geq 0$$.

**a)** Viết bài toán đối ngẫu.  
**b)** Áp dụng phương pháp gradient gần kề cho bài toán đối ngẫu.  
**c)** Khôi phục nghiệm bài toán gốc.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**Bài toán đối ngẫu:**

$$\max_\nu \quad g(\nu) = b^T\nu$$

với ràng buộc $$A^T\nu \leq c$$.

**Bước cập nhật gradient gần kề (có chiếu) trên bài toán đối ngẫu:**

$$\nu^{(k+1)} = \Pi_{\{A^T\nu \leq c\}}(\nu^{(k)} + t b)$$

**Khôi phục nghiệm gốc:**

$$x^{(k)} = \arg\min_x L(x, \nu^{(k)})$$

</details>

---

## 💡 **Tổng kết**

| Phương pháp | Tốc độ hội tụ | Đặc điểm chính |
|-------------|---------------|----------------|
| Gradient gần kề | $$O(1/k)$$ | Xử lý trực tiếp thành phần không trơn $$g$$ |
| FISTA | $$O(1/k^2)$$ | Tăng tốc bằng động lượng Nesterov |
| Gradient gần kề đối ngẫu | $$O(1/k)$$ | Xử lý ràng buộc qua bài toán đối ngẫu |

### **Một số toán tử gần kề thường gặp:**

| Hàm số | Toán tử gần kề |
|--------|----------------|
| $$\|\cdot\|_1$$ | Ngưỡng mềm (Soft-thresholding) |
| $$\|\cdot\|_2$$ | Ngưỡng mềm theo khối (Block soft-thresholding) |
| $$\|\cdot\|_*$$ | Ngưỡng mềm trên giá trị kỳ dị (SVD soft-thresholding) |
| $$I_C$$ | Phép chiếu $$\Pi_C$$ |
| Hàm bậc hai | Nghịch đảo ma trận $$(I + tQ)^{-1}$$ |

---

## 📚 **Tài liệu Tham khảo**

1. Parikh, N., & Boyd, S. (2014). "Proximal Algorithms". Foundations and Trends.
2. Beck, A., & Teboulle, M. (2009). "A Fast Iterative Shrinkage-Thresholding Algorithm" (FISTA).
3. Combettes, P. L., & Pesquet, J.-C. (2011). "Proximal Splitting Methods".

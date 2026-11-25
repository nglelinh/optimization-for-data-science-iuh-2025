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

Sức mạnh thực sự của phương pháp gradient gần kề nằm ở "từ điển toán tử gần kề": chỉ cần biết cách tính $$\operatorname{prox}_{t h}(v)$$ cho một hàm không trơn mới — dù là chuẩn $$\ell_1$$, chuẩn hạt nhân ma trận, chuẩn $$\ell_2$$ không bình phương (Group Lasso), hay hàm chỉ thị của đơn hình xác suất — là bạn lập tức có ngay một bộ giải tốc độ $$O(1/k^2)$$ bằng FISTA!

Năm bài tập thực hành dưới đây đưa bạn đi qua trọn bộ kỹ năng triển khai đó: từ lập trình ISTA và FISTA cho Lasso, giải bài toán hoàn thiện ma trận bằng SVD, tự tay suy ra các công thức prox cơ bản (bao gồm đồng nhất thức Moreau tuyệt đẹp!), cho đến kết hợp gradient gần kề với bài toán đối ngẫu.

## Bản đồ kiến thức nền: Bốn công cụ giải tích cần thiết cho bộ bài tập thực hành

- **Điều kiện tối ưu của bài toán con prox:** Điểm $$u = \operatorname{prox}_{t h}(v)$$ được đặc trưng duy nhất bởi quan hệ bao hàm dưới vi phân:
  $$0 \in \frac{1}{t}(u - v) + \partial h(u) \;\Longleftrightarrow\; \frac{v - u}{t} \in \partial h(u).$$
  Đây là công cụ nhanh nhất để tự chứng minh mọi công thức prox đóng.
- **Định lý phân rã Moreau (Moreau Decomposition):** Với mọi hàm lồi đóng chính quy $$h$$ và hàm liên hợp lồi $$h^*$$ của nó:
  $$v = \operatorname{prox}_h(v) + \operatorname{prox}_{h^*}(v).$$
  Định lý này giống như phép phân tích trực giao $$v = P_S(v) + P_{S^\perp}(v)$$ tổng quát hóa sang hàm lồi! Nhờ nó, nếu bạn biết phép chiếu lên quả cầu $$\ell_\infty$$ (prox của $$h^* = I_{B_\infty}$$), bạn suy ngay ra co ngưỡng mềm (prox của $$h = \|\cdot\|_1$$) bằng một phép trừ duy nhất!
- **Quy tắc biến đổi affine và tách biến (Separable Sum Rule):** Nếu $$h(x) = \sum_{j=1}^n h_j(x_j)$$, toán tử prox tách độc lập theo từng tọa độ $$j$$. Với chuẩn $$\ell_2$$ không bình phương $$\lambda\|x\|_2$$ (không tách biến), ta vẫn có công thức đóng gọi là *co ngưỡng khối* (block soft-thresholding): $$\left(1 - \frac{t\lambda}{\|v\|_2}\right)_+ v$$.
- **Tiêu chuẩn dừng thực hành:** Thay vì chỉ dừng theo số vòng lặp, ta thường kiểm tra chuẩn độ dốc tổng quát $$\|G_t(x^{(k)})\|_2 = \frac{1}{t}\|x^{(k)} - x^{(k+1)}\|_2 \le \text{tol}$$ hoặc khoảng cách đối ngẫu (duality gap).

### Khung giải thích (nên đọc chậm): Kiểm chứng tay định lý phân rã Moreau cho $$h(x) = |x|$$

Với $$h(x) = |x|$$ trên $$\mathbb{R}$$, hàm liên hợp lồi là hàm chỉ thị đoạn $$[-1, 1]$$:
$$h^*(y) = \sup_x (xy - |x|) = I_{[-1, 1]}(y) = \begin{cases} 0 & \text{nếu } |y| \le 1, \\ +\infty & \text{nếu } |y| > 1. \end{cases}$$
Do đó $$\operatorname{prox}_h(v) = S_1(v)$$ (co ngưỡng mềm ngưỡng $$1$$) và $$\operatorname{prox}_{h^*}(v) = P_{[-1, 1]}(v) = \operatorname{clip}(v, -1, 1)$$.

1. **Kiểm thử với $$v = 2.7$$ (ngoài đoạn $$[-1, 1]$$):**
   - $$\operatorname{prox}_h(2.7) = S_1(2.7) = 2.7 - 1 = 1.7$$.
   - $$\operatorname{prox}_{h^*}(2.7) = \operatorname{clip}(2.7, -1, 1) = 1.0$$.
   - Cộng lại: $$1.7 + 1.0 = 2.7 = v$$!
2. **Kiểm thử với $$v = -0.6$$ (trong đoạn $$[-1, 1]$$):**
   - $$\operatorname{prox}_h(-0.6) = S_1(-0.6) = 0$$.
   - $$\operatorname{prox}_{h^*}(-0.6) = \operatorname{clip}(-0.6, -1, 1) = -0.6$$.
   - Cộng lại: $$0 + (-0.6) = -0.6 = v$$!
3. **Ứng dụng ngay cho Bài tập 4:** Tương tự, với $$h(x) = \|x\|_2$$, hàm liên hợp là $$I_{B_2(1)}$$, nên chỉ cần trừ đi hình chiếu lên quả cầu đơn vị $$\ell_2$$ là bạn có ngay công thức $$\operatorname{prox}_{\|\cdot\|_2}(v) = v - P_{B_2(1)}(v) = \left(1 - \frac{1}{\|v\|_2}\right)_+ v$$ mà không cần giải đạo hàm phức tạp!

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

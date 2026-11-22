---
layout: post
title: 19-09 Bài Tập Thực Hành - Proximal Newton Methods
chapter: '19'
order: 13
owner: GitHub Copilot
lang: vi
categories:
- chapter19
lesson_type: required
redirect_from:
  - /contents/vi/chapter19/19_08_Practical_Exercises_Proximal_Newton_Methods/
---

# Bài Tập Thực Hành - Phương pháp Proximal Newton

Các bài tập được tham khảo từ Lee et al. (2014) và Rakotomamonjy et al. (2016).

---

## 📝 **Bài tập 1: Bước Proximal Newton**

Cho hàm mục tiêu tổng hợp $$f(x) + g(x)$$ với $$f(x) = x^2$$ và $$g(x) = |x|$$.

**Yêu cầu:**  
a) Viết bài toán con của phương pháp Proximal Newton.  
b) Giải bài toán con tại $$x^{(k)} = 2$$.  
c) So sánh kết quả với phương pháp proximal gradient descent.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bài toán con Proximal Newton:**

$$x^{(k+1)} = \arg\min_x \left\{ f(x^{(k)}) + \nabla f(x^{(k)})^T(x - x^{(k)}) + \frac{1}{2}(x - x^{(k)})^T \nabla^2 f(x^{(k)})(x - x^{(k)}) + g(x) \right\}$$

$$= \arg\min_x \left\{ \frac{H_k}{2}(x - x^{(k)})^2 + \nabla f(x^{(k)})(x - x^{(k)}) + g(x) \right\}$$

---

**b) Giải tại $$x^{(k)} = 2$$:**

Ta có $$\nabla f(2) = 4$$ và $$\nabla^2 f(2) = 2$$, nên bài toán con là:

$$\min_x \left\{ (x - 2)^2 + 4(x - 2) + |x| \right\}$$

$$= \min_x \left\{ x^2 - 4x + 4 + 4x - 8 + |x| \right\}$$

$$= \min_x \left\{ x^2 - 4 + |x| \right\}$$

- **Trường hợp 1 ($$x \geq 0$$):** $$\min_{x \ge 0} (x^2 + x - 4)$$; điểm dừng $$x = -0.5$$ nằm ngoài miền $$x \ge 0$$ nên đạt cực tiểu tại biên $$x = 0$$.
- **Trường hợp 2 ($$x < 0$$):** $$\min_{x < 0} (x^2 - x - 4)$$; điểm dừng $$x = 0.5$$ nằm ngoài miền $$x < 0$$ nên hàm giảm dần về biên $$x = 0$$.
- **Kiểm tra tại biên $$x = 0$$:** giá trị hàm mục tiêu bằng $$-4$$.

**Nghiệm tối ưu:** $$x^{(1)} = 0$$.

---

**c) So sánh với Proximal Gradient Descent:**

$$x^{(k+1)} = \text{prox}_{t|\cdot|}(x^{(k)} - t\nabla f(x^{(k)})) = S_t(2 - 4t)$$

Với độ dài bước $$t = 0.5$$ (bằng $$1/H_k$$): $$S_{0.5}(0) = 0$$.

Trong bài toán bậc hai 1 chiều đơn giản này, hai phương pháp cho cùng kết quả vì Hessian là hằng số $$H_k = 2$$.

</details>

---

## 📝 **Bài tập 2: Proximal Newton cho LASSO**

Xét bài toán:

$$\min \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$

**Yêu cầu:**  
a) Xác định tập biến hoạt động (active set) và không hoạt động (inactive set).  
b) Viết bước Newton trên tập biến hoạt động.  
c) Xử lý trường hợp biến đổi dấu trong quá trình cập nhật.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tập hoạt động:**

$$\mathcal{A} = \{i : x_i \neq 0\}, \qquad \mathcal{I} = \{i : x_i = 0\}$$

**Điều kiện KKT trên $$\mathcal{A}$$:** $$\nabla f(x)_{\mathcal{A}} + \lambda \cdot \text{sign}(x_{\mathcal{A}}) = 0$$.

---

**b) Bước Newton trên $$\mathcal{A}$$:**

Xét bài toán thu gọn trên tập hoạt động:

$$\min_{x_{\mathcal{A}}} \frac{1}{2}\|A_{\mathcal{A}}x_{\mathcal{A}} - b\|^2 + \lambda\|x_{\mathcal{A}}\|_1$$

Khi cố định dấu $$\text{sign}(x_{\mathcal{A}})$$, hệ phương trình Newton là:

$$\nabla^2 f_{\mathcal{A}} \Delta x_{\mathcal{A}} = -\nabla f_{\mathcal{A}} - \lambda \cdot \text{sign}(x_{\mathcal{A}})$$

$$\Delta x_{\mathcal{A}} = -(A_{\mathcal{A}}^T A_{\mathcal{A}})^{-1}\big(A_{\mathcal{A}}^T(A_{\mathcal{A}}x_{\mathcal{A}} - b) + \lambda \cdot \text{sign}(x_{\mathcal{A}})\big)$$

---

**c) Xử lý khi biến đổi dấu:**

Nếu một thành phần đổi dấu ($$x_i^{\text{new}} \cdot x_i^{\text{old}} < 0$$), ta cắt ngắn độ dài bước để dừng trước (hoặc tại) điểm $$0$$:

$$\alpha_{\max} = \min_{\{i \in \mathcal{A} \,:\, x_i^{\text{old}} \Delta x_i < 0\}} \frac{-x_i^{\text{old}}}{\Delta x_i}$$

**Cập nhật an toàn:** $$x^{(k+1)} = x^{(k)} + \min(1, 0.99\alpha_{\max}) \Delta x$$ (hoặc đặt tọa độ chạm $$0$$ về đúng $$0$$ và cập nhật lại tập hoạt động).

</details>

---

## 📝 **Bài tập 3: Phương pháp Newton bán trơn (Semismooth Newton)**

Xét điều kiện tối ưu dạng bao hàm: $$F(x) = \nabla f(x) + \partial g(x) \ni 0$$.

**Yêu cầu:**  
a) Nêu khái niệm ma trận Jacobi tổng quát (generalized Jacobian).  
b) Minh họa với $$g(x) = \|x\|_1$$.  
c) Nêu điều kiện để phương pháp đạt hội tụ siêu tuyến tính.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Ma trận Jacobi tổng quát:**

$$\partial F(x) = \nabla^2 f(x) + \partial^2 g(x)$$

trong đó $$\partial^2 g$$ ký hiệu đạo hàm bậc hai dạng ánh xạ đa trị (trong cài đặt thực tế thường áp dụng trực tiếp cho phương trình điểm bất động không trơn $$x - \text{prox}_g(x - \nabla f(x)) = 0$$).

---

**b) Với $$g(x) = \|x\|_1$$:**

$$\partial g(x)_i = \begin{cases}
\text{sign}(x_i) & \text{if } x_i \neq 0 \\
[-1, 1] & \text{if } x_i = 0
\end{cases}$$

$$\partial^2 g(x)_i = \begin{cases}
0 & \text{if } x_i \neq 0 \\
\{0\} \cup \{\infty \cdot \text{sign}\} & \text{if } x_i = 0
\end{cases}$$

**Hướng Newton:** Chọn một phần tử đại diện $$V_x \in \partial F(x)$$ và giải hệ tuyến tính tương ứng.

---

**c) Tốc độ hội tụ:**

Nếu ánh xạ $$F$$ thỏa mãn tính chất bán trơn (semismooth):

$$\|F(x + d) - F(x) - V_x d\| = o(\|d\|)$$

với $$V_x \in \partial F(x)$$ (và $$V_x$$ khả nghịch đều quanh nghiệm), thì phương pháp Newton bán trơn đạt **hội tụ siêu tuyến tính cục bộ** tương tự phương pháp Newton trơn.

</details>

---

## 📝 **Bài tập 4: Đường điều chuẩn (Regularization Path)**

Theo dõi quỹ đạo nghiệm $$x^*(\lambda)$$ khi tham số điều chuẩn $$\lambda$$ thay đổi.

**Yêu cầu:**  
a) Tính đạo hàm dọc đường điều chuẩn $$\frac{dx^*}{d\lambda}$$.  
b) Dự báo nghiệm mới khi thay đổi $$\lambda \to \lambda + \Delta\lambda$$.  
c) Áp dụng vào kỹ thuật khởi động ấm (warm-start).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Đạo hàm hàm ẩn:**

Từ điều kiện KKT: $$\nabla f(x^*) + \lambda v^* = 0$$ với $$v^* \in \partial g(x^*)$$.

Lấy đạo hàm hai vế theo $$\lambda$$:

$$\nabla^2 f(x^*) \frac{dx^*}{d\lambda} + v^* + \lambda \frac{dv^*}{d\lambda} = 0$$

Trên tập hoạt động (nơi $$v^*$$ không đổi cục bộ, chẳng hạn $$v_i^* = \text{sign}(x_i^*)$$ với phạt $$\ell_1$$ nên $$\frac{dv^*}{d\lambda} = 0$$):

$$\frac{dx^*}{d\lambda} = -(\nabla^2 f)^{-1} v^*$$

---

**b) Dự báo nghiệm mới:**

$$x^*(\lambda + \Delta\lambda) \approx x^*(\lambda) + \frac{dx^*}{d\lambda} \Delta\lambda = x^*(\lambda) - (\nabla^2 f)^{-1} v^* \Delta\lambda$$

---

**c) Khởi động ấm (Warm-start):**

Sử dụng giá trị dự báo trên làm điểm khởi tạo cho bài toán tại $$\lambda + \Delta\lambda$$ giúp giảm đáng kể số vòng lặp Newton cần thiết.

</details>

---

## 📝 **Bài tập 5: Điều chuẩn thích nghi (Adaptive Regularization)**

Điều chỉnh tham số điều chuẩn $$\mu$$ trong vòng lặp để đảm bảo tính ổn định.

**Yêu cầu:**  
a) Viết bài toán con kiểu Levenberg–Marquardt với ma trận $$\nabla^2 f + \mu I$$.  
b) Nêu quy tắc cập nhật $$\mu$$ dựa trên tỷ số giảm thực tế trên giảm dự báo.  
c) So sánh với việc dùng Hessian cố định không điều chuẩn.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bài toán con có điều chuẩn:**

$$\min_d \left\{ \frac{1}{2}d^T(\nabla^2 f + \mu I)d + \nabla f^T d + g(x + d) \right\}$$

Tham số $$\mu > 0$$ đủ lớn đảm bảo ma trận bậc hai xác định dương.

---

**b) Quy tắc kiểu miền tin cậy (Trust region):**

Tính tỷ số giảm:

$$\rho = \frac{\text{mức giảm thực tế}}{\text{mức giảm dự báo}}$$

- Nếu $$\rho > 0.75$$: giảm $$\mu$$ (tiến gần hơn tới bước Newton đầy đủ).
- Nếu $$\rho < 0.25$$: tăng $$\mu$$ (thận trọng hơn, tiến gần về bước proximal gradient).

---

**c) Lợi ích so với Hessian cố định:**

- **Hessian cố định:** Có thể không hội tụ hoặc bài toán con không bị chặn nếu $$\nabla^2 f$$ không xác định dương.
- **Điều chuẩn thích nghi $$\mu$$:** Đảm bảo luôn thu được hướng giảm và ổn định trên các bài toán có số điều kiện xấu.

</details>

---

## 💡 **Tổng kết**

| Phương pháp | Đặc điểm chính | Phù hợp với |
|--------|-------------|----------|
| Proximal Newton | Mô hình bậc hai + toán tử prox | Phạt $$\ell_1$$, thưa theo nhóm (group sparsity) |
| Tập hoạt động (Active set) | Cố định dấu, giải Newton trơn trên biến khác 0 | Đường điều chuẩn LASSO |
| Newton bán trơn (Semismooth) | Dùng ma trận Jacobi tổng quát | Hệ phương trình tối ưu không trơn |
| Điều chuẩn thích nghi | Dùng $$\nabla^2 f + \mu I$$ | Bài toán có số điều kiện xấu |

---

## 📚 **Tài liệu tham khảo**

1. Lee, J. D., et al. (2014). "Proximal Newton-type methods". *NeurIPS*.
2. Rakotomamonjy, A., et al. (2016). "Efficient Proximal Newton". *ICML*.

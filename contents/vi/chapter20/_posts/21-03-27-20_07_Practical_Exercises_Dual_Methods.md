---
layout: post
title: 20-07 Bài Tập Thực Hành - Dual Methods
chapter: '20'
order: 15
owner: GitHub Copilot
lang: vi
categories:
- chapter20
lesson_type: required
redirect_from:
  - /contents/vi/chapter20/20_06_Practical_Exercises_Dual_Methods/
---

Để làm chủ hoàn toàn nhóm phương pháp đối ngẫu — từ phân rã song song (Dual Decomposition), hàm Lagrange tăng cường (Augmented Lagrangian) cho đến ADMM — không có cách nào hiệu quả hơn việc tự tay viết hàm Lagrange, tách các khối biến, tính phần dư ràng buộc và chạy thử một vài vòng lặp để tận mắt thấy nhân tử Lagrange tự điều chỉnh như thế nào. Bộ bài tập thực hành dưới đây tổng hợp các dạng bài kinh điển từ Bertsekas (1999) và Boyd et al. (2011).

## Bản đồ kiến thức nền: Bốn quy tắc kiểm chứng khi giải bài tập Chương 20

Trước khi bước vào từng bài tập bên dưới, hãy giữ sẵn bốn nguyên tắc kiểm tra nhanh để không bao giờ bị nhầm dấu nhân tử:

- **Thống nhất dấu hàm Lagrange ngay từ dòng đầu:** Với ràng buộc $$Ax = b$$, nếu viết $$L(x, \nu) = f(x) + \nu^T(Ax - b)$$ thì bước cập nhật tăng đối ngẫu luôn mang dấu **cộng**: $$\nu^{(k+1)} = \nu^{(k)} + t_k(Ax^{(k+1)} - b)$$. Nếu viết dấu trừ $$-\nu^T(Ax - b)$$ thì bước cập nhật phải đổi thành dấu trừ!
- **Kiểm tra điều kiện tồn tại cực tiểu của bước gốc:** Khi làm bài tập Dual Decomposition, luôn kiểm tra xem $$f_i(x_i) + \nu^T A_i x_i$$ có lồi chặt để có nghiệm hữu hạn duy nhất không; nếu không, đó chính là dấu hiệu cần chuyển sang Augmented Lagrangian!
- **Kiểm chứng điểm yên ngựa tại nghiệm tìm được:** Thay $$(x^\star, \nu^\star)$$ vào cả phương trình dừng $$\nabla_x L(x^\star, \nu^\star) = 0$$ lẫn ràng buộc $$Ax^\star = b$$, đồng thời kiểm tra $$f(x^\star) = g(\nu^\star)$$.
- **So sánh độ nhạy tham số $$\rho$$:** Trong các bài tập lập trình Augmented Lagrangian và ADMM, thử chạy với $$\rho \in \{0.1, 1, 10\}$$ và vẽ biểu đồ $$\|r^{(k)}\|_2$$ cùng $$\|s^{(k)}\|_2$$ theo số vòng lặp để cảm nhận trực tiếp sự đánh đổi giữa phần dư gốc và phần dư đối ngẫu.

### Khung giải thích (nên đọc chậm): Khởi động bằng phép kiểm tra điểm yên ngựa và dấu nhân tử Lagrange

Xét bài toán nhỏ $$\min_{x_1, x_2} x_1^2 + x_2^2$$ với ràng buộc $$x_1 + 2x_2 = 5$$:

1. **Viết hàm Lagrange đúng quy ước dấu cộng:**
   $$L(x_1, x_2, \nu) = x_1^2 + x_2^2 + \nu(x_1 + 2x_2 - 5) = (x_1^2 + \nu x_1) + (x_2^2 + 2\nu x_2) - 5\nu.$$
2. **Tách hai bài toán con theo $$\nu$$ cố định:**
   - $$x_1(\nu) = \arg\min_{x_1} (x_1^2 + \nu x_1) = -\frac{\nu}{2}$$.
   - $$x_2(\nu) = \arg\min_{x_2} (x_2^2 + 2\nu x_2) = -\nu$$.
3. **Tìm $$\nu^\star$$ để thỏa mãn ràng buộc $$x_1(\nu) + 2x_2(\nu) = 5$$:**
   $$-\frac{\nu}{2} + 2(-\nu) = 5 \iff -\frac{5}{2}\nu = 5 \implies \nu^\star = -2.$$
4. **Kiểm chứng chéo:** Thay $$\nu^\star = -2$$ ta được $$x_1^\star = 1, x_2^\star = 2$$, thỏa mãn $$1 + 2(2) = 5$$. Giá trị gốc $$f(1, 2) = 1^2 + 2^2 = 5$$; giá trị đối ngẫu $$g(-2) = L(1, 2, -2) = 5 + (-2)(0) = 5$$ — khớp tuyệt đối! Giờ bạn đã sẵn sàng giải trọn bộ bài tập Chương 20.

---

# Bài Tập Thực Hành - Các phương pháp đối ngẫu

Các bài tập được tham khảo từ Bertsekas (1999) và Boyd et al. (2011).

---

## 📝 **Bài tập 1: Phân rã đối ngẫu (Dual Decomposition)**

Xét bài toán cực tiểu hóa $$\sum_{i=1}^N f_i(x_i)$$ với ràng buộc $$\sum_{i=1}^N x_i = c$$.

**Yêu cầu:**  
a) Viết hàm Lagrange và hàm đối ngẫu.  
b) Phân rã thành $$N$$ bài toán con độc lập.  
c) Viết công thức cập nhật biến đối ngẫu $$\nu$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Hàm Lagrange và hàm đối ngẫu:**

$$L(x, \nu) = \sum_i f_i(x_i) + \nu\left(\sum_i x_i - c\right) = \sum_i [f_i(x_i) + \nu x_i] - \nu c$$

$$g(\nu) = \sum_i \min_{x_i} [f_i(x_i) + \nu x_i] - \nu c$$

**b) Phân rã:** Với $$\nu$$ cố định, ta giải song song $$N$$ bài toán con độc lập:

$$x_i^{(k)} = \arg\min_{x_i} [f_i(x_i) + \nu^{(k)} x_i], \quad i = 1, \dots, N$$

**c) Cập nhật biến đối ngẫu:**

$$\nu^{(k+1)} = \nu^{(k)} + \alpha\left(\sum_i x_i^{(k)} - c\right)$$

</details>

---

## 📝 **Bài tập 2: Hàm Lagrange tăng cường (Augmented Lagrangian)**

Xét bài toán $$\min f(x)$$ với ràng buộc $$Ax = b$$.

**Yêu cầu:**  
a) Viết hàm Lagrange tăng cường $$L_\rho(x, \nu)$$.  
b) So sánh ưu điểm so với hàm Lagrange tiêu chuẩn.  
c) Viết các bước lặp của phương pháp nhân tử (ALM).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Hàm Lagrange tăng cường:**

$$L_\rho(x, \nu) = f(x) + \nu^T(Ax - b) + \frac{\rho}{2}\|Ax - b\|^2$$

**b) So sánh ưu điểm:**

- **Hàm Lagrange tiêu chuẩn:** Hàm đối ngẫu $$g(\nu)$$ có thể không khả vi (khi $$f$$ không lồi chặt).
- **Hàm Lagrange tăng cường:** Tạo ra bài toán đối ngẫu trơn hơn và có số điều kiện tốt hơn, giúp hội tụ ổn định dưới các giả thiết nhẹ hơn.

**c) Các bước lặp của ALM:**

1. $$x^{(k+1)} = \arg\min_x L_\rho(x, \nu^{(k)})$$
2. $$\nu^{(k+1)} = \nu^{(k)} + \rho(Ax^{(k+1)} - b)$$

</details>

---

## 📝 **Bài tập 3: Phương pháp nhân tử (Method of Multipliers)**

Áp dụng ALM cho bài toán $$\min x_1^2 + x_2^2$$ thỏa mãn $$x_1 + x_2 = 1$$.

**Yêu cầu:**  
a) Thiết lập hàm Lagrange tăng cường.  
b) Thực hiện các bước lặp đầu tiên từ $$\nu^{(0)} = 0$$ với $$\rho = 1$$.  
c) Nêu giá trị hội tụ của $$(x^{(k)}, \nu^{(k)})$$.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Hàm Lagrange tăng cường ($$\rho = 1$$):**

$$L_\rho(x, \nu) = x_1^2 + x_2^2 + \nu(x_1 + x_2 - 1) + \frac{1}{2}(x_1 + x_2 - 1)^2$$

**b) Bước cực tiểu hóa theo $$x$$:**

Từ điều kiện dừng $$\nabla_x L_\rho = 0$$:

$$\nabla_x L_\rho = \big(2x_1 + \nu + (x_1 + x_2 - 1),\ 2x_2 + \nu + (x_1 + x_2 - 1)\big) = 0$$

$$3x_1 + x_2 = 1 - \nu, \qquad x_1 + 3x_2 = 1 - \nu$$

Suy ra nghiệm: $$x_1 = x_2 = \frac{1-\nu}{4}$$.

- **Vòng lặp 0:** Với $$\nu^{(0)} = 0$$ $$\Rightarrow$$ $$x^{(1)} = (0.25, 0.25)$$. Phần dư: $$0.5 - 1 = -0.5$$. Cập nhật: $$\nu^{(1)} = 0 + 1(-0.5) = -0.5$$.
- **Vòng lặp 1:** Với $$\nu^{(1)} = -0.5$$ $$\Rightarrow$$ $$x^{(2)} = (0.375, 0.375)$$. Phần dư: $$0.75 - 1 = -0.25$$. Cập nhật: $$\nu^{(2)} = -0.5 + 1(-0.25) = -0.75$$.

**c) Hội tụ:** Dãy lặp hội tụ nhanh về nghiệm tối ưu $$x^* = (0.5, 0.5)$$ và nhân tử tối ưu $$\nu^* = -1$$.

</details>

---

## 📝 **Bài tập 4: So sánh Dual Gradient và Dual Newton**

Xét bài toán cực đại hóa hàm đối ngẫu $$g(\nu)$$ bằng phương pháp tăng gradient và phương pháp Newton.

**Yêu cầu:**  
a) Viết cập nhật Dual Gradient: $$\nu^{(k+1)} = \nu^{(k)} + \alpha \nabla g(\nu^{(k)})$$.  
b) Viết công thức Hessian $$\nabla^2 g(\nu)$$ cho cập nhật Dual Newton: $$\nu^{(k+1)} = \nu^{(k)} - (\nabla^2 g(\nu^{(k)}))^{-1} \nabla g(\nu^{(k)})$$.  
c) So sánh sự đánh đổi giữa hai phương pháp.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Dual Gradient:**

$$\nabla g(\nu) = Ax^*(\nu) - b$$

$$\nu^{(k+1)} = \nu^{(k)} + \alpha(Ax^{(k)} - b)$$

Tốc độ hội tụ là tuyến tính (khi $$g$$ trơn và lõm mạnh) hoặc dưới tuyến tính như phương pháp subgradient nếu $$g$$ không trơn.

**b) Dual Newton:**

Lấy đạo hàm theo $$\nu$$ của $$\nabla g(\nu) = Ax^*(\nu) - b$$ (kết hợp vi phân ẩn của điều kiện dừng $$\nabla f(x^*) + A^T\nu = 0$$ cho $$\frac{\partial x^*}{\partial \nu} = -(\nabla^2 f(x^*))^{-1} A^T$$):

$$\nabla^2 g(\nu) = A \frac{\partial x^*(\nu)}{\partial \nu} = -A (\nabla^2 f(x^*))^{-1} A^T$$

Phương pháp đạt **hội tụ bậc hai cục bộ** nếu $$g$$ trơn (khả vi hai lần) và lõm mạnh.

**c) Đánh đổi:**

- **Dual Gradient:** Chi phí mỗi vòng lặp thấp, nhưng cần nhiều vòng lặp hơn.
- **Dual Newton:** Chi phí mỗi vòng lặp cao (phải tính và giải hệ với ma trận Hessian đối ngẫu), nhưng hội tụ rất nhanh gần nghiệm.

</details>

---

## 📝 **Bài tập 5: Tối ưu đồng thuận (Consensus Optimization)**

Cho $$N$$ tác tử cùng cực tiểu hóa $$\sum_{i=1}^N f_i(x_i)$$ với ràng buộc đồng thuận $$x_1 = x_2 = \cdots = x_N$$.

**Yêu cầu:**  
a) Thiết lập phân rã đối ngẫu trên đồ thị kết nối.  
b) Viết quy tắc cập nhật phân tán.  
c) Nêu đặc điểm truyền thông của thuật toán.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Hàm Lagrange và hàm đối ngẫu:**

$$L(x, \nu) = \sum_{i=1}^N f_i(x_i) + \sum_{i<j} \nu_{ij}(x_i - x_j) = \sum_{i=1}^N \left[ f_i(x_i) + \left(\sum_{j>i} \nu_{ij} - \sum_{j<i} \nu_{ji}\right) x_i \right]$$

$$g(\nu) = \sum_{i=1}^N \min_{x_i} \left[ f_i(x_i) + \left(\sum_{j>i} \nu_{ij} - \sum_{j<i} \nu_{ji}\right) x_i \right]$$

**b) Quy tắc cập nhật phân tán:**

Mỗi tác tử $$i$$ cập nhật độc lập:

$$x_i^{(k+1)} = \arg\min_{x_i} \left[ f_i(x_i) + \left(\sum_{j>i} \nu_{ij}^{(k)} - \sum_{j<i} \nu_{ji}^{(k)}\right) x_i \right]$$

Sau đó, với mỗi cặp tác tử kết nối $$(i, j)$$ ($$i < j$$), cập nhật nhân tử trên cạnh:

$$\nu_{ij}^{(k+1)} = \nu_{ij}^{(k)} + \rho(x_i^{(k+1)} - x_j^{(k+1)})$$

**c) Truyền thông:**

Mỗi tác tử chỉ cần trao đổi biến $$x_i$$ với các nút láng giềng trực tiếp trên đồ thị mà không cần máy chủ trung tâm, tạo thành sơ đồ đồng thuận phân tán.

</details>

---

## 💡 **Tổng kết**

| Phương pháp | Ý tưởng chính | Tốc độ hội tụ tiêu biểu |
|--------|----------|-------------|
| Phân rã đối ngẫu (Dual decomposition) | Tách thành các bài toán con song song | Dưới tuyến tính (nếu không lồi chặt) |
| Hàm Lagrange tăng cường (ALM) | Thêm số hạng phạt bậc hai | Tuyến tính / siêu tuyến tính |
| Dual gradient | Phương pháp bậc nhất trên bài toán đối ngẫu | $$O(1/k)$$ (tuyến tính nếu lồi mạnh và trơn) |
| Dual Newton | Phương pháp bậc hai trên bài toán đối ngẫu | Bậc hai cục bộ |

---

## 📚 **Tài liệu tham khảo**

1. Bertsekas, D. P. (1999). *Nonlinear Programming*. Athena Scientific.
2. Boyd, S., et al. (2011). "Distributed Optimization and Statistical Learning via ADMM".

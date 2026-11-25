---
layout: post
title: 21-08 Bài Tập Thực Hành - ADMM Applications
chapter: '21'
order: 9
owner: GitHub Copilot
lang: vi
categories:
- chapter21
lesson_type: required
redirect_from:
  - /contents/vi/chapter21/21_07_Practical_Exercises_ADMM_Applications/
---

Cài đặt thành công một bộ giải ADMM cho Lasso, Group Lasso hay Consensus ADMM chỉ trong vài chục dòng Python là một trải nghiệm cực kỳ "đã tay": bạn sẽ thấy một bộ khung vỏn vẹn 3 dòng lặp có thể giải quyết trơn tru hàng loạt bài toán tối ưu lồi tưởng chừng rất khác nhau. Bộ bài tập thực hành này — lấy cảm hứng từ cẩm nang kinh điển của Boyd và cộng sự (2011) — giúp bạn tự tay viết mã, kiểm tra tiêu chuẩn dừng gốc–đối ngẫu và thử nghiệm độ nhạy của tham số $$\rho$$.

## Bản đồ kiến thức nền: Bốn mẹo thực hành giúp code ADMM chạy chuẩn và nhanh

Trước khi bắt tay giải và lập trình các bài tập bên dưới, hãy bỏ túi bốn kinh nghiệm thực chiến sau:

- **Luôn dùng dạng chuẩn hóa (Scaled Form) khi lập trình:** Chỉ lưu một biến đối ngẫu $$u$$ (tức $$w = u_{\text{raw}}/\rho$$) giúp code ngắn gọn hơn và giảm hẳn nguy cơ nhân thiếu hoặc nhân thừa hệ số $$\rho$$.
- **Đặt phân tích Cholesky ra ngoài vòng lặp `for`:** Với Lasso và bài toán bậc hai, tính `L = cholesky(A.T @ A + rho * I)` đúng một lần trước vòng lặp, bên trong chỉ gọi `cho_solve` để tiết kiệm thời gian tính toán theo cấp số nhân.
- **Theo dõi đồng thời cả hai phần dư dừng:** Tính $$\|r^{(k)}\|_2 = \|x^{(k)} - z^{(k)}\|_2$$ và $$\|s^{(k)}\|_2 = \rho\|z^{(k)} - z^{(k-1)}\|_2$$ ở cuối mỗi vòng lặp; tuyệt đối không chỉ nhìn riêng vào $$r^{(k)}$$ kẻo dừng quá sớm (như ta đã thấy ở bài 21-02!).
- **Thử cập nhật $$\rho$$ thích nghi (Residual Balancing):** Nếu $$\|r^{(k)}\|_2 > 10\|s^{(k)}\|_2$$, nhân đôi $$\rho \leftarrow 2\rho$$ và chia đôi biến chuẩn hóa $$w \leftarrow w / 2$$; ngược lại nếu $$\|s^{(k)}\|_2 > 10\|r^{(k)}\|_2$$, chia đôi $$\rho \leftarrow \rho/2$$ và nhân đôi $$w \leftarrow 2w$$ để hai phần dư cân bằng và hội tụ nhanh hơn nhiều!

### Khung giải thích (nên đọc chậm): Chạy nháp 1 vòng Lasso ADMM với ma trận trực giao $$2 \times 2$$

Trước khi viết code cho Bài tập 1, hãy tự tính tay 1 vòng lặp Lasso ADMM cho $$A = I_2$$, $$b = (2, \; -0.5)^T$$, $$\lambda = 1$$, $$\rho = 1$$, khởi tạo $$z^{(0)} = (0, 0)^T, u^{(0)} = (0, 0)^T$$:

1. **Tiền phân tích ma trận hệ thống:** $$A^T A + \rho I = I_2 + I_2 = 2 I_2 \implies (A^T A + \rho I)^{-1} = 0.5 I_2$$.
2. **Bước $$x^{(1)}$$:**
   $$x^{(1)} = 0.5\left(A^T b + \rho(z^{(0)} - u^{(0)})\right) = 0.5\begin{bmatrix} 2 \\ -0.5 \end{bmatrix} = \begin{bmatrix} 1.0 \\ -0.25 \end{bmatrix}.$$
3. **Bước $$z^{(1)}$$ (ngưỡng mềm với $$\lambda/\rho = 1$$):**
   $$z^{(1)} = S_1(x^{(1)} + u^{(0)}) = S_1\begin{bmatrix} 1.0 \\ -0.25 \end{bmatrix} = \begin{bmatrix} 0.0 \\ 0.0 \end{bmatrix}.$$
4. **Bước $$u^{(1)}$$ và hai phần dư:**
   - $$u^{(1)} = u^{(0)} + x^{(1)} - z^{(1)} = (1.0, \; -0.25)^T$$.
   - Phần dư gốc $$\|r^{(1)}\|_2 = \sqrt{1^2 + 0.25^2} \approx 1.031$$; phần dư đối ngẫu $$\|s^{(1)}\|_2 = 0$$.
   Ở vòng 2, $$x^{(2)} = 0.5(b - u^{(1)}) = (0.5, -0.125)^T$$, $$x^{(2)} + u^{(1)} = (1.5, -0.375)^T \implies z^{(2)} = (0.5, 0.0)^T$$, tiến thẳng về nghiệm chính xác $$x^\star = S_1(2, -0.5) = (1.0, \; 0.0)^T$$!

---

# Bài Tập Thực Hành - Ứng dụng của ADMM

Các bài tập dưới đây được tham khảo từ Boyd và cộng sự (2011).

---

## 📝 **Bài tập 1: Cơ bản về ADMM**

Xét bài toán $$\min f(x) + g(z)$$ với ràng buộc $$Ax + Bz = c$$.

**Yêu cầu:**  
a) Viết các bước cập nhật của ADMM dạng chuẩn hóa (scaled ADMM).  
b) Áp dụng cho bài toán Lasso: $$\min \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$.  
c) Chạy thử vài vòng lặp với một ví dụ nhỏ.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) ADMM dạng chuẩn hóa:**

$$x^{(k+1)} = \arg\min_x \left[ f(x) + \frac{\rho}{2}\|Ax + Bz^{(k)} - c + u^{(k)}\|^2 \right]$$

$$z^{(k+1)} = \arg\min_z \left[ g(z) + \frac{\rho}{2}\|Ax^{(k+1)} + Bz - c + u^{(k)}\|^2 \right]$$

$$u^{(k+1)} = u^{(k)} + Ax^{(k+1)} + Bz^{(k+1)} - c$$

**b) Áp dụng cho Lasso** với ràng buộc tách biến $$x - z = 0$$:

$$x^{(k+1)} = (A^TA + \rho I)^{-1}(A^Tb + \rho(z^{(k)} - u^{(k)}))$$

$$z^{(k+1)} = S_{\lambda/\rho}(x^{(k+1)} + u^{(k)})$$

$$u^{(k+1)} = u^{(k)} + x^{(k+1)} - z^{(k+1)}$$

</details>

---

## 📝 **Bài tập 2: ADMM đồng thuận (Consensus ADMM)**

Cho $$N$$ hàm mục tiêu: $$\min \sum_{i=1}^N f_i(x)$$.

**Yêu cầu:**  
a) Viết lại bài toán dưới dạng đồng thuận với các biến cục bộ $$x_i$$.  
b) Suy ra bước cập nhật biến toàn cục.  
c) Mô tả cách triển khai phân tán.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Dạng đồng thuận:**

$$\min \sum_i f_i(x_i)$$ với ràng buộc $$x_i = z \, \forall i$$

**b) Các bước ADMM:**

$$x_i^{(k+1)} = \arg\min_{x_i} \left[ f_i(x_i) + \frac{\rho}{2}\|x_i - z^{(k)} + u_i^{(k)}\|^2 \right]$$

$$z^{(k+1)} = \frac{1}{N}\sum_i (x_i^{(k+1)} + u_i^{(k)})$$

$$u_i^{(k+1)} = u_i^{(k)} + x_i^{(k+1)} - z^{(k+1)}$$

**c) Triển khai phân tán:** Mỗi nút tính toán cập nhật độc lập biến cục bộ $$x_i$$, sau đó nút điều phối lấy trung bình để cập nhật biến toàn cục $$z$$.

</details>

---

## 📝 **Bài tập 3: Khử nhiễu biến phân toàn phần (Total Variation Denoising)**

Xét bài toán:

$$\min \frac{1}{2}\|x - b\|^2 + \lambda \|Dx\|_1$$

với $$D$$ là toán tử sai phân.

**Yêu cầu:**  
a) Thiết lập công thức ADMM.  
b) Viết bước cập nhật $$x$$ (thành phần trơn).  
c) Viết bước cập nhật $$z$$ (co ngưỡng mềm).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tách biến:** Đặt $$z = Dx$$, bài toán trở thành:

$$\min_{x,z} \frac{1}{2}\|x - b\|^2 + \lambda\|z\|_1$$ với ràng buộc $$Dx - z = 0$$

**b) Bước cập nhật $$x$$:**

$$x^{(k+1)} = (I + \rho D^TD)^{-1}(b + \rho D^T(z^{(k)} - u^{(k)}))$$

(Giải hệ phương trình tuyến tính, thường có cấu trúc dải nên tính toán nhanh.)

**c) Bước cập nhật $$z$$:**

$$z^{(k+1)} = S_{\lambda/\rho}(Dx^{(k+1)} + u^{(k)})$$

</details>

---

## 📝 **Bài tập 4: Phân rã ma trận**

Xét bài toán $$\min \|L\|_* + \lambda\|S\|_1$$ với ràng buộc $$L + S = M$$.

**Yêu cầu:**  
a) Viết bước cập nhật $$L$$ (co ngưỡng giá trị kỳ dị qua SVD).  
b) Viết bước cập nhật $$S$$ (co ngưỡng mềm theo phần tử).  
c) Nêu ứng dụng trong PCA bền vững (robust PCA).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bước cập nhật $$L$$:**

$$L^{(k+1)} = \arg\min_L \left[ \|L\|_* + \frac{\rho}{2}\|L + S^{(k)} - M + U^{(k)}\|_F^2 \right]$$

$$= \mathcal{S}_{1/\rho}(M - S^{(k)} - U^{(k)})$$

với $$\mathcal{S}_\tau(X) = U \text{diag}(\max(\sigma_i - \tau, 0)) V^T$$.

**b) Bước cập nhật $$S$$:**

$$S^{(k+1)} = S_{\lambda/\rho}(M - L^{(k+1)} - U^{(k)})$$

**c) Ứng dụng PCA bền vững:** Phân rã ma trận quan sát $$M = L + S$$ thành thành phần hạng thấp $$L$$ và thành phần thưa $$S$$ (nhiễu ngoại lai).

</details>

---

## 📝 **Bài tập 5: Hội tụ và điều chỉnh tham số**

**Yêu cầu:**  
a) Cách chọn tham số $$\rho$$.  
b) Tiêu chí dừng thuật toán.  
c) Quy tắc điều chỉnh $$\rho$$ thích nghi.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Chọn $$\rho$$:**

*Quy tắc kinh nghiệm:* Chọn $$\rho \sim 1.0$$ đối với dữ liệu đã chuẩn hóa.

*Nguyên tắc cân bằng:* Điều chỉnh sao cho phần dư gốc và phần dư đối ngẫu giảm cân đối với nhau.

**b) Tiêu chí dừng:**

$$\epsilon_{\text{pri}} = \sqrt{n}\epsilon_{\text{abs}} + \epsilon_{\text{rel}}\max(\|Ax\|, \|Bz\|, \|c\|)$$

$$\epsilon_{\text{dual}} = \sqrt{n}\epsilon_{\text{abs}} + \epsilon_{\text{rel}}\|A^T\nu\|$$

Dừng thuật toán khi $$\|r\| < \epsilon_{\text{pri}}$$ và $$\|s\| < \epsilon_{\text{dual}}$$.

**c) Điều chỉnh $$\rho$$ thích nghi:**

```
if ||r|| > μ ||s||:
    ρ = τ_incr * ρ
elif ||s|| > μ ||r||:
    ρ = ρ / τ_decr
```

thường chọn $$\mu = 10$$ và $$\tau = 2$$.

</details>

---

## 💡 **Tổng kết**

**Một số ứng dụng tiêu biểu của ADMM:**

| Bài toán | $$f(x)$$ | $$g(z)$$ | Ứng dụng |
|----------|----------|----------|----------|
| Lasso | $$\frac{1}{2}\|Ax-b\|^2$$ | $$\lambda\|z\|_1$$ | Hồi quy thưa |
| Biến phân toàn phần (TV) | $$\frac{1}{2}\|x-b\|^2$$ | $$\lambda\|z\|_1$$ | Khử nhiễu ảnh |
| Robust PCA | $$\|L\|_*$$ | $$\lambda\|S\|_1$$ | Loại bỏ nhiễu ngoại lai |
| Đồng thuận | $$\sum f_i(x_i)$$ | $$0$$ | Tối ưu phân tán |

---

## 📚 **Tài liệu Tham khảo**

1. Boyd, S., et al. (2011). "Distributed Optimization via ADMM". *Foundations and Trends*.

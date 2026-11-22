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

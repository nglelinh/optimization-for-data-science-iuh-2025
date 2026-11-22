---
layout: post
title: "08-11 Bài Tập Thực Hành - Phương pháp Subgradient"
chapter: "08"
order: 19
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter08
lesson_type: required
redirect_from:
  - /contents/vi/chapter08/08_10_Practical_Exercises_Subgradient_Methods/
---

# Bài Tập Thực Hành - Phương pháp Subgradient

Các bài tập được tham khảo từ Boyd et al. (2003) và Nesterov (2009).

---

## **Bài tập 1: Phương pháp Subgradient đối ngẫu cho bài toán Quy hoạch tuyến tính (LP)**

Cho bài toán LP: $$\min c^Tx$$ với ràng buộc $$Ax = b$$, $$x \geq 0$$, trong đó $$c = (1,2)^T$$, $$A = [1,1]$$, $$b = 3$$.

**a)** Viết bài toán đối ngẫu.  
**b)** Tính subgradient của hàm đối ngẫu.  
**c)** Thực hiện các bước lặp subgradient đối ngẫu.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**Hàm Lagrangian:** $$L(x,\nu) = c^Tx + \nu(b - Ax)$$, suy ra $$g(\nu) = 3\nu + \inf_{x \geq 0}(c - A^T\nu)^Tx$$, hữu hạn khi $$A^T\nu \leq c$$.

**Bài toán đối ngẫu:** $$\max 3\nu$$ với ràng buộc $$\nu \leq 1$$.

**Subgradient:** $$g'(\nu) = b - Ax^*(\nu) = 3$$ (với $$x^*=0$$ khi $$\nu \le 1$$).

**Nghiệm tối ưu:** $$\nu^* = 1$$ (giá trị đối ngẫu bằng $$3$$, trùng với giá trị gốc tại $$x = (3, 0)$$).

Áp dụng bước tăng gradient có chiếu lên miền $$\nu \leq 1$$ với $$\alpha = 0.1$$ xuất phát từ $$\nu^{(0)} = 0$$, ta thu được dãy $$0.3, 0.6, 0.9, 1$$, hội tụ đến $$\nu^* = 1$$ sau 4 bước.

</details>

---

## **Bài tập 2: Phương pháp Subgradient ngẫu nhiên**

Cho bài toán $$\min \frac{1}{n}\sum_i \max(0, 1 - y_i w^T x_i)$$ với 3 điểm dữ liệu.

**a)** Viết công thức cập nhật ngẫu nhiên.  
**b)** So sánh với phương pháp batch.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

Phương pháp ngẫu nhiên chọn một mẫu dữ liệu $$i$$ ở mỗi bước lặp và cập nhật:

$$w^{(k+1)} = w^{(k)} - \alpha_k g_i$$

với $$g_i = -y_i x_i$$ nếu mẫu $$i$$ vi phạm lề ($$1 - y_i w^T x_i > 0$$), và $$g_i = 0$$ nếu không vi phạm.

**Ưu điểm:** Chi phí mỗi bước lặp thấp hơn nhiều so với phương pháp batch, đồng thời vẫn tạo được tiến triển nhanh trong giai đoạn đầu khi tập dữ liệu lớn.

</details>

---

## **Bài tập 3: Trung bình Polyak–Ruppert**

Cho $$f(x) = \max\{2x, -x+3\}$$.

**a)** Tìm nghiệm tối ưu $$x^*$$.  
**b)** So sánh dãy điểm lặp $$x^{(k)}$$ với dãy trung bình $$\bar{x}^{(k)}$$.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**Nghiệm tối ưu:** $$x^* = 1$$ (giao điểm của hai đường thẳng $$2x$$ và $$-x+3$$).

**Trung bình các bước lặp:** $$\bar{x}^{(k)} = \frac{1}{k}\sum_{i=1}^k x^{(i)}$$.

Việc lấy trung bình giúp làm mượt dao động quanh điểm gấp khúc và cải thiện sự ổn định khi tiến gần $$x^*$$.

</details>

---

## **Bài tập 4: Mirror Descent trên tập đơn hình (Simplex)**

Cho $$f(x) = c^Tx$$ trên tập đơn hình $$\Delta_3$$.

**a)** Sử dụng ánh xạ gương entropy $$\psi(x) = \sum x_i \log x_i$$.  
**b)** Suy ra công thức cập nhật.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**Công thức cập nhật:**

$$x_i^{(k+1)} \propto x_i^{(k)} e^{-\alpha c_i}$$

Sau đó chuẩn hóa để đảm bảo $$\sum x_i = 1$$.

**Ưu điểm:** Phù hợp tự nhiên với cấu trúc hình học của tập đơn hình, giúp duy trì nghiệm nằm trong miền ràng buộc một cách trực tiếp.

</details>

---

## **Bài tập 5: Phương pháp mặt phẳng cắt (Cutting Plane Method)**

Cho $$f(x) = \max\{x^2, (x-2)^2\}$$.

**a)** Xây dựng các mặt phẳng cắt $$\ell_k(x) = f(x^{(k)}) + g^{(k)}(x - x^{(k)})$$.  
**b)** Cực tiểu hóa hàm cận dưới $$\hat{f}(x) = \max_k \ell_k(x)$$.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

Xuất phát từ $$x^{(0)} = 0$$:

$$\ell_0(x) = 4 - 4x$$

Tại $$x^{(1)} = 1$$:

$$\ell_1(x) = 1 + 2(x-1) = 2x - 1$$

Cực tiểu hóa $$\max\{4-4x, 2x-1\}$$ cho điểm tiếp theo $$x^{(2)} = \frac{5}{6}$$.

Lặp lại quá trình bổ sung mặt phẳng cắt cho đến khi khoảng cách giữa cận trên và cận dưới đạt ngưỡng cho phép.

</details>

---

## **Tổng kết**

| Phương pháp | Tốc độ hội tụ | Phù hợp nhất cho |
|-------------|---------------|------------------|
| Subgradient đối ngẫu | $$O(1/\sqrt{k})$$ | Quy hoạch tuyến tính, bài toán lồi |
| Subgradient ngẫu nhiên | $$O(1/\sqrt{k})$$ | Học máy quy mô lớn |
| Trung bình hóa | $$O(1/\sqrt{k})$$ | Giảm dao động quanh nghiệm |
| Mirror Descent | $$O(1/\sqrt{k})$$ | Miền ràng buộc có hình học đặc thù |
| Bundle / Mặt phẳng cắt | $$O(1/k)$$ | Hàm không trơn, số biến nhỏ |

---

## **Tài liệu Tham khảo**

1. Boyd, S., et al. (2003). "Subgradient Methods". Stanford.
2. Nesterov, Y. (2009). "Primal-dual subgradient methods".
3. Beck, A., & Teboulle, M. (2003). "Mirror descent".

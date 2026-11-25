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

Lý thuyết tối ưu chỉ thực sự thấm vào tay nghề khi bạn tự viết vòng lặp, nhìn thấy đường cong loss nhảy lên nhảy xuống trên màn hình, rồi tự tay thuần hóa nó bằng các kỹ thuật thực hành. Trong khi các bài giảng trước tập trung vào công thức cập nhật cơ bản, năm bài tập thực hành dưới đây đưa bạn đi thẳng vào "xưởng cơ khí" của tối ưu không trơn: từ subgradient đối ngẫu cho quy hoạch tuyến tính, trung bình hóa Polyak–Ruppert, Mirror Descent trên đơn hình xác suất cho tới phương pháp mặt phẳng cắt (Cutting Plane).

Mỗi bài tập đều đại diện cho một hướng nâng cấp quan trọng của phương pháp subgradient cổ điển. Nếu bạn từng thắc mắc làm sao một thuật toán chỉ có tốc độ $$O(1/\epsilon^2)$$ lại có thể được cải tiến mạnh mẽ trong thực tế bằng kỹ thuật lấy trung bình hay thay đổi hình học không gian, loạt bài thực hành này chính là câu trả lời sống động nhất.

## Bản đồ kiến thức nền: Bốn kỹ thuật mở rộng xuất hiện trong bộ bài tập thực hành

- **Subgradient đối ngẫu cho bài toán có ràng buộc (Dual Subgradient):** Khi bài toán gốc có ràng buộc tuyến tính $$Ax = b$$, hàm đối ngẫu $$g(\lambda) = \inf_{x \ge 0} (c^T x + \lambda^T(Ax - b))$$ là hàm lõm không trơn; subgradient của $$-g(\lambda)$$ chính là phần dư vi phạm ràng buộc $$b - Ax(\lambda)$$!
- **Trung bình hóa Polyak–Ruppert (Iterate Averaging):** Thay vì lấy điểm lặp cuối $$x^{(k)}$$ vốn dễ dao động quanh đáy chữ V, ta lấy trung bình $$\bar{x}^{(k)} = \frac{1}{k}\sum_{i=1}^k x^{(i)}$$ (hoặc trung bình có trọng số bước $$\alpha_i$$). Nhờ tính lồi (bất đẳng thức Jensen), $$f(\bar{x}^{(k)}) \le \frac{1}{k}\sum f(x^{(i)})$$, triệt tiêu đáng kể dao động răng cưa!
- **Mirror Descent và hình học đơn hình xác suất:** Trên đơn hình $$\Delta_n = \{x \ge 0 : \sum x_i = 1\}$$, dùng hàm tạo entropy $$\psi(x) = \sum x_i \ln x_i$$ biến bước cập nhật thành quy tắc nhân trọng số (Exponentiated Gradient) $$x_i^{(k+1)} \propto x_i^{(k)} e^{-t_k g_i^{(k)}}$$, tránh hẳn phép chiếu đắt đỏ và tăng tốc mạnh theo số chiều $$n$$.
- **Phương pháp mặt phẳng cắt (Cutting Plane / Kelley's Method):** Thay vì quên sạch các subgradient cũ sau mỗi bước, ta tích lũy chúng thành một hàm xấp xỉ tuyến tính từng khúc $$\hat{f}_k(x) = \max_{1 \le i \le k} \{f(x^{(i)}) + g^{(i)T}(x - x^{(i)})\}$$ — đây là tiền thân trực tiếp của phương pháp bó (bundle methods).

### Khung giải thích (nên đọc chậm): Tính tay sức mạnh của trung bình hóa Polyak–Ruppert trên hàm $$f(x) = |x|$$

Quay lại kịch bản dao động bất tận của $$f(x) = |x|$$ với bước cố định $$t = 1$$ từ $$x^{(0)} = 0.5$$:

1. **Quỹ đạo thô $$x^{(k)}$$ bị kẹt dao động:**
   - $$x^{(0)} = +0.5 \implies f(x^{(0)}) = 0.5$$
   - $$x^{(1)} = 0.5 - 1(1) = -0.5 \implies f(x^{(1)}) = 0.5$$
   - $$x^{(2)} = -0.5 - 1(-1) = +0.5 \implies f(x^{(2)}) = 0.5$$
   - $$x^{(3)} = -0.5 \implies f(x^{(3)}) = 0.5$$
   Nếu chỉ nhìn điểm cuối $$x^{(k)}$$ hay thậm chí $$f_{\text{best}}^{(k)}$$, sai số không bao giờ nhỏ hơn $$0.5$$!
2. **Áp dụng trung bình hóa Polyak–Ruppert $$\bar{x}^{(k)} = \frac{1}{k}\sum_{i=0}^{k-1} x^{(i)}$$:**
   - Sau $$k = 2$$ điểm ($$x^{(0)}, x^{(1)}$$): $$\bar{x}^{(2)} = \frac{0.5 + (-0.5)}{2} = 0.0 = x^* \implies f(\bar{x}^{(2)}) = 0!$$
   - Sau $$k = 3$$ điểm: $$\bar{x}^{(3)} = \frac{0.5 - 0.5 + 0.5}{3} = 0.167 \implies f(\bar{x}^{(3)}) = 0.167 < 0.5$$.
   - Sau $$k = 4$$ điểm: $$\bar{x}^{(4)} = 0.0 \implies f(\bar{x}^{(4)}) = 0$$!
3. **Trực giác cốt lõi:** Bất đẳng thức Jensen đảm bảo điểm trung bình của một đám mây dao động quanh đáy luôn nằm sâu hơn hẳn từng điểm đơn lẻ — một mẹo lập trình chỉ tốn 2 dòng code nhưng mang lại khác biệt rõ rệt khi làm các bài tập thực hành dưới đây.

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

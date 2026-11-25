---
layout: post
title: 07-10 Bài Tập Thực Hành - Tối ưu Subgradient
chapter: '07'
order: 14
owner: GitHub Copilot
lang: vi
categories:
- chapter07
lesson_type: required
redirect_from:
  - /contents/vi/chapter07/07_09_Practical_Exercises_Subgradient_Optimization/
---

Khi lý thuyết Subgradient chuyển hóa thành thuật toán lặp $$x^{(k+1)} = x^{(k)} - t_k g^{(k)}$$ (với $$g^{(k)} \in \partial f(x^{(k)})$$), ta bước vào một lãnh địa có luật chơi khác hẳn Gradient Descent ở Chương 06: không thể dùng Backtracking Line Search (vì $$-g^{(k)}$$ chưa chắc là hướng giảm!), không thể dùng bước cố định để hội tụ chính xác về $$f^\star$$, và tốc độ hội tụ chậm hơn đáng kể — chỉ đạt $$O(1/\sqrt{k})$$ thay vì $$O(1/k)$$!

Bộ bài tập thực hành này giúp bạn trực tiếp chạm tay vào cả hai mặt của Chương 07: tính chuẩn xác subgradient của các hàm không trơn phổ biến (chuẩn $$\ell_1, \ell_2, \ell_\infty$$, hàm cực đại, hinge loss) và tự tay phân tích, cài đặt **Phương pháp Subgradient** với các lịch bước giảm dần chuẩn xác!

## Kiến thức cần nhớ: Bốn quy tắc thực chiến cho Phương pháp Subgradient

Khi giải các bài tập thực hành tính subgradient và chạy thuật toán Subgradient Method, hãy nắm chắc bốn nguyên tắc sau:

- **Tính chất Lipschitz của hàm (không phải gradient!) $$|f(x) - f(y)| \le G\|x - y\|_2$$:** Điều kiện tương đương là mọi subgradient đều bị chặn chuẩn $$\|g\|_2 \le G \; \forall g \in \partial f(x)$$. (Ví dụ với $$f(x) = \|x\|_1$$ trên $$\mathbb{R}^n$$, $$\|g\|_2 \le \sqrt{n} \implies G = \sqrt{n}$$.)
- **Theo dõi $$f_{\text{best}}^{(k)} = \min_{i=0,\dots,k} f(x^{(i)})$$:** Vì phương pháp Subgradient **không giảm đơn điệu** ($$f(x^{(k+1)})$$ có thể lớn hơn $$f(x^{(k)})$$), ta luôn phải lưu kỷ lục tốt nhất trong suốt quá trình chạy!
- **Lựa chọn kích thước bước $$t_k$$:**
  - **Bước cố định $$t_k = t$$:** Chỉ hội tụ vào lân cận $$f^\star + \frac{G^2 t}{2}$$.
  - **Bước giảm dần không cộng dồn bình phương** ($$\sum t_k = \infty,\; \sum t_k^2 < \infty$$, ví dụ $$t_k = \frac{c}{k}$$ hoặc $$\frac{c}{\sqrt{k}}$$): Đảm bảo $$f_{\text{best}}^{(k)} \to f^\star$$, với tốc độ tối ưu $$O\left(\frac{GR}{\sqrt{k}}\right)$$ khi chọn $$t_k = \frac{R}{G\sqrt{k}}$$ (trong đó $$R = \|x^{(0)} - x^\star\|_2$$)!
  - **Bước Polyak (khi biết trước $$f^\star$$):** $$t_k = \frac{f(x^{(k)}) - f^\star}{\|g^{(k)}\|_2^2}$$ — cực kỳ hiệu quả cho bài toán tìm điểm giao các tập lồi (nơi ta biết trước $$f^\star = 0$$)!
- **Độ phức tạp $$O(1/\epsilon^2)$$:** Để đạt độ chính xác $$\epsilon$$, phương pháp Subgradient cần cỡ $$\frac{G^2 R^2}{\epsilon^2}$$ vòng lặp (ví dụ $$\epsilon = 10^{-3}$$ cần tới ~$$10^6$$ bước — đó là động lực để sang các chương sau ta học Phương pháp Proximal!).

### Giải thích: Chạy tay 3 bước Phương pháp Subgradient với bước Polyak và bước $$1/\sqrt{k}$$

Xét hàm không trơn $$f(x) = |x - 2|$$ ($$G = 1,\; x^\star = 2,\; f^\star = 0$$), xuất phát từ $$x^{(0)} = 0$$ ($$R = 2$$):

1. **Dùng lịch bước chuẩn $$t_k = \frac{R}{G\sqrt{k+1}} = \frac{2}{\sqrt{k+1}}$$:**
   - **Bước $$k = 0$$:** $$x^{(0)} = 0 \implies g^{(0)} = -1$$, $$t_0 = 2$$.
     $$x^{(1)} = 0 - 2(-1) = 2 \implies f(2) = 0$$ (may mắn chạm đúng đích!).
   - Thử xuất phát từ $$x^{(0)} = -1$$ ($$R = 3$$, dùng lịch $$t_k = \frac{1}{\sqrt{k+1}}$$):
     - $$k = 0$$: $$x^{(0)} = -1,\; g^{(0)} = -1,\; t_0 = 1 \implies x^{(1)} = 0,\; f = 2$$.
     - $$k = 1$$: $$x^{(1)} = 0,\; g^{(1)} = -1,\; t_1 \approx 0.707 \implies x^{(2)} \approx 0.707,\; f \approx 1.293$$.
     - $$k = 2$$: $$x^{(2)} \approx 0.707,\; g^{(2)} = -1,\; t_2 \approx 0.577 \implies x^{(3)} \approx 1.284,\; f \approx 0.716$$.
2. **Dùng bước Polyak $$t_k = \frac{f(x^{(k)}) - f^\star}{\|g^{(k)}\|_2^2}$$ từ $$x^{(0)} = -1$$ (biết $$f^\star = 0$$):**
   - $$k = 0$$: $$f(-1) = 3,\; g^{(0)} = -1 \implies t_0 = \frac{3 - 0}{(-1)^2} = 3$$.
   - Cập nhật: $$x^{(1)} = -1 - 3(-1) = 2 \implies f(2) = 0$$ — chạm đúng cực tiểu toàn cục sau **đúng 1 bước**!

---

# Bài Tập Thực Hành - Tối ưu Subgradient (Subgradient Optimization)

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004) và Shor (1985).

---

## 📝 **Phần I: Tính Subgradient**

### **Bài tập 1: Subgradient của hàm không khả vi**

Tính vi phân dưới (tập các subgradient) của các hàm sau tại điểm cho trước:

**a)** $$f(x) = |x|$$ tại $$x = 0$$

**b)** $$f(x) = \max\{x_1, x_2\}$$ tại $$x = (1, 1)^T$$

**c)** $$f(x) = \|x\|_1$$ tại $$x = (0, 0)^T$$

**d)** $$f(x) = \max\{x_1 + x_2, 2x_1 - x_2\}$$ tại $$x = (1, 0)^T$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) $$f(x) = |x|$$ tại $$x = 0$$:**

**Định nghĩa:** $$g \in \partial f(0)$$ khi và chỉ khi

$$f(y) \geq f(0) + g(y - 0)$$ $$\forall y$$

$$|y| \geq 0 + gy \quad \forall y$$

- Với $$y > 0$$: $$y \geq gy$$ suy ra $$g \leq 1$$.
- Với $$y < 0$$: $$-y \geq gy$$ suy ra $$g \geq -1$$.

Do đó: $$\partial f(0) = [-1, 1]$$.

**Ý nghĩa hình học:** Tập hợp hệ số góc của tất cả các đường thẳng tựa đi qua đồ thị tại $$x = 0$$.

---

**b) $$f(x) = \max\{x_1, x_2\}$$ tại $$x = (1, 1)$$:**

Ta có $$f(1, 1) = 1$$ (cả hai thành phần đều đạt giá trị lớn nhất).

**Tập hoạt động (active set):** $$I = \{1, 2\}$$.

$$\partial f(x) = \text{conv}\{\nabla f_i(x) : i \in I\}$$

$$= \text{conv}\{(1, 0), (0, 1)\}$$

$$= \{(\lambda, 1-\lambda) : 0 \leq \lambda \leq 1\}$$

**Ý nghĩa hình học:** Đoạn thẳng nối hai điểm $$(1, 0)$$ và $$(0, 1)$$.

---

**c) $$f(x) = \|x\|_1 = |x_1| + |x_2|$$ tại $$x = (0, 0)$$:**

$$\partial f(0) = \partial |x_1| \times \partial |x_2|$$

$$= [-1, 1] \times [-1, 1]$$

$$= \{(g_1, g_2) : |g_1| \leq 1, |g_2| \leq 1\}$$

**Ý nghĩa hình học:** Hình vuông $$[-1, 1]^2$$.

---

**d) $$f(x) = \max\{x_1 + x_2, 2x_1 - x_2\}$$ tại $$x = (1, 0)$$:**

$$f_1(1, 0) = 1 + 0 = 1$$

$$f_2(1, 0) = 2 - 0 = 2$$

$$\Rightarrow f(1, 0) = 2$$ (chỉ có $$f_2$$ đạt giá trị lớn nhất).

$$\nabla f_2 = (2, -1)$$

$$\partial f(1, 0) = \{(2, -1)\}$$ (chỉ gồm một phần tử vì chỉ có một hàm thành phần hoạt động).

</details>

---

## 📝 **Phần II: Phương pháp Subgradient**

### **Bài tập 2: Phân tích hội tụ**

Cho $$f(x) = |x - 2| + |x + 1|$$.

**Yêu cầu:**  
a) Tìm tập điểm cực tiểu $$x^*$$.  
b) Với kích thước bước $$\alpha_k = \frac{1}{\sqrt{k}}$$, viết công thức lặp xuất phát từ $$x^{(0)} = 5$$.  
c) Tính $$x^{(1)}, x^{(2)}, x^{(3)}$$.  
d) Ước lượng tốc độ hội tụ.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tìm $$x^*$$:**

$$f(x) = |x - 2| + |x + 1|$$

**Xét theo từng khoảng:**
- Với $$x < -1$$: $$f(x) = -(x-2) - (x+1) = -2x + 1$$ (hàm giảm).
- Với $$-1 \leq x \leq 2$$: $$f(x) = -(x-2) + (x+1) = 3$$ (hàm hằng).
- Với $$x > 2$$: $$f(x) = (x-2) + (x+1) = 2x - 1$$ (hàm tăng).

Do đó $$f^* = 3$$ và tập điểm cực tiểu là $$x^* \in [-1, 2]$$.

---

**b) Công thức lặp của phương pháp subgradient:**

$$x^{(k+1)} = x^{(k)} - \alpha_k g^{(k)}$$

với $$g^{(k)} \in \partial f(x^{(k)})$$.

---

**c) Tính các bước lặp đầu tiên:**

Tại $$x^{(0)} = 5 > 2$$:

$$\partial f(5) = \{\text{sign}(5-2)\} + \{\text{sign}(5+1)\} = \{1\} + \{1\} = \{2\}$$

$$g^{(0)} = 2$$

$$\alpha_0 = \frac{1}{\sqrt{1}} = 1$$

$$x^{(1)} = 5 - 1 \cdot 2 = 3$$

---

Tại $$x^{(1)} = 3 > 2$$:

$$g^{(1)} = 2$$

$$\alpha_1 = \frac{1}{\sqrt{2}} \approx 0.707$$

$$x^{(2)} = 3 - 0.707 \cdot 2 = 1.586$$

---

Tại $$x^{(2)} = 1.586 \in [-1, 2]$$ (đã nằm trong miền tối ưu):

$$\partial f(1.586) = \{\text{sign}(1.586 - 2) + \text{sign}(1.586 + 1)\} = \{-1 + 1\} = \{0\}$$ (trên khoảng $$(-1, 2)$$, $$f$$ là hàm hằng nên khả vi với đạo hàm bằng 0).

$$g^{(2)} = 0 \Rightarrow x^{(3)} = x^{(2)} = 1.586$$ (thuật toán đã hội tụ đến tập nghiệm tối ưu).

---

**d) Tốc độ hội tụ:**

Với $$\alpha_i = \frac{1}{\sqrt{i}}$$, từ bất đẳng thức cơ bản ta có:

$$f(x_{\text{best}}^{(k)}) - f^* \leq \frac{R^2 + G^2 \sum_{i=1}^k \alpha_i^2}{2\sum_{i=1}^k \alpha_i}$$

$$\sum_{i=1}^k \frac{1}{\sqrt{i}} \approx 2\sqrt{k}$$

$$\sum_{i=1}^k \frac{1}{i} \approx \log k$$

$$\Rightarrow f(x_{\text{best}}^{(k)}) - f^* = O\left(\frac{\log k}{\sqrt{k}}\right)$$

(Nếu chọn kích thước bước cố định theo tổng số bước $$k$$ dạng $$\alpha = \frac{R}{G\sqrt{k}}$$, cận sẽ bỏ được thừa số $$\log k$$ và đạt $$O(1/\sqrt{k})$$.)

Đây là **hội tụ dưới tuyến tính (sublinear)**, chậm hơn so với gradient descent trên hàm trơn.

</details>

---

## 📝 **Phần III: Các quy tắc chọn kích thước bước**

### **Bài tập 3: So sánh các chiến lược kích thước bước**

Cho $$f(x) = \max\{x_1, x_2, -x_1 - x_2 + 1\}$$.

**Yêu cầu:**  
a) Tìm nghiệm tối ưu $$x^*$$.  
b) So sánh 3 quy tắc kích thước bước:
   - Cố định: $$\alpha_k = 0.1$$
   - Giảm dần: $$\alpha_k = \frac{1}{k}$$
   - Tổng bình phương hội tụ: $$\alpha_k = \frac{1}{k^{0.6}}$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tìm nghiệm tối ưu:**

$$f(x) = \max\{x_1, x_2, 1 - x_1 - x_2\}$$

**Các đường giao nhau của ba hàm thành phần:**
- $$x_1 = x_2$$
- $$x_1 = 1 - x_1 - x_2 \iff 2x_1 + x_2 = 1$$
- $$x_2 = 1 - x_1 - x_2 \iff x_1 + 2x_2 = 1$$

Giải hệ $$x_1 = x_2$$ và $$2x_1 + x_2 = 1$$:

$$3x_1 = 1 \Rightarrow x_1 = \frac{1}{3}$$

Suy ra $$x^* = \left(\frac{1}{3}, \frac{1}{3}\right)$$ và $$f^* = \frac{1}{3}$$.

---

**b) So sánh các quy tắc kích thước bước:**

**Xuất phát từ $$x^{(0)} = (1, 1)$$:**

Ta có $$f_1 = 1$$, $$f_2 = 1$$, $$f_3 = -1$$ nên giá trị lớn nhất đạt tại cả $$f_1$$ và $$f_2$$:

$$\partial f(1, 1) = \text{conv}\{(1, 0), (0, 1)\}$$

Chọn trung điểm $$g = (0.5, 0.5)$$.

---

**Kích thước bước cố định $$\alpha_k = 0.1$$:**

$$x^{(1)} = (1, 1) - 0.1(0.5, 0.5) = (0.95, 0.95)$$

$$x^{(2)} = (0.90, 0.90)$$

$$x^{(3)} = (0.85, 0.85)$$

...

**Nhận xét:** Thuật toán hội tụ đến một lân cận của $$x^*$$ (bán kính cỡ $$O(\alpha)$$), nhưng không đạt tới nghiệm chính xác.

---

**Kích thước bước giảm dần $$\alpha_k = \frac{1}{k}$$:**

$$x^{(1)} = (1, 1) - 1 \cdot (0.5, 0.5) = (0.5, 0.5)$$

$$x^{(2)} = (0.5, 0.5) - 0.5 \cdot (0.5, 0.5) = (0.25, 0.25)$$ (với $$g^{(1)} = (0.5, 0.5)$$)

Tại $$(0.25, 0.25)$$, thành phần $$f_3 = 0.5$$ đạt giá trị lớn nhất nên $$g^{(2)} = (-1, -1)$$, suy ra $$x^{(3)} = (0.25, 0.25) + \frac{1}{3}(1, 1) \approx (0.583, 0.583)$$ (điểm lặp dao động quanh $$x^*$$ với biên độ giảm dần).

...

**Nhận xét:** Hội tụ đến $$x^*$$ nhưng rất chậm (cận $$O(1/\log k)$$ vì $$\sum_{i \le k} 1/i \approx \log k$$).

---

**Kích thước bước tổng bình phương hội tụ $$\alpha_k = \frac{1}{k^{0.6}}$$:**

$$\sum \alpha_k = \sum \frac{1}{k^{0.6}} = \infty$$ ✓

$$\sum \alpha_k^2 = \sum \frac{1}{k^{1.2}} < \infty$$ ✓

**Nhận xét:** Hội tụ đến $$x^*$$ với cận $$O(1/k^{0.4})$$ (vì $$\sum_{i \le k} \alpha_i \sim k^{0.4}$$), nhanh hơn quy tắc $$\alpha_k = 1/k$$ nhưng vẫn là tốc độ hội tụ dưới tuyến tính.

</details>

---

## 📝 **Phần IV: Kích thước bước Polyak**

### **Bài tập 4: Kích thước bước Polyak cho bài toán cực tiểu hóa $$\ell_1$$**

$$\min_{x} \|x\|_1 \quad \text{s.t.} \quad Ax = b$$

với $$A = [1, 2, 3]$$, $$b = 6$$.

**Yêu cầu:**  
a) Viết hàm Lagrangian.  
b) Tìm hàm đối ngẫu.  
c) Cực đại hóa hàm đối ngẫu bằng phương pháp subgradient với kích thước bước Polyak.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Hàm Lagrangian:**

$$L(x, \nu) = \|x\|_1 + \nu^T(Ax - b)$$

$$= \sum_i (|x_i| + \nu a_i x_i) - \nu b$$

---

**b) Hàm đối ngẫu:**

$$g(\nu) = \inf_x L(x, \nu)$$

$$= \inf_x \sum_i (|x_i| + \nu a_i x_i) - \nu b$$

Cực tiểu hóa độc lập theo từng biến $$x_i$$:

$$\inf_{x_i} (|x_i| + \nu a_i x_i) = \begin{cases}
0 & \text{nếu } |\nu a_i| \leq 1 \\
-\infty & \text{trường hợp khác}
\end{cases}$$

$$g(\nu) = \begin{cases}
-\nu b & \text{nếu } |\nu a_i| \leq 1 \, \forall i \\
-\infty & \text{trường hợp khác}
\end{cases}$$

Với $$A = [1, 2, 3]$$:

$$|\nu| \leq 1, \quad |2\nu| \leq 1, \quad |3\nu| \leq 1$$

$$\Rightarrow |\nu| \leq \frac{1}{3}$$

Do đó $$g(\nu) = -6\nu$$ với $$|\nu| \leq \frac{1}{3}$$.

---

**c) Cực đại hóa bài toán đối ngẫu:**

$$\max_{\nu} \quad -6\nu \quad \text{s.t.} \quad -\frac{1}{3} \leq \nu \leq \frac{1}{3}$$

Ta thấy ngay $$\nu^* = -\frac{1}{3}$$ và $$g^* = 2$$.

**Subgradient của $$g(\nu) = -6\nu$$:** $$s = -6$$ (vì đây là bài toán cực đại hóa hàm lõm $$g$$, ta áp dụng bước tăng subgradient).

**Kích thước bước Polyak** (khi đã biết $$g^* = 2$$):

$$\alpha_k = \frac{g^* - g(\nu^{(k)})}{\|s^{(k)}\|^2}, \qquad \nu^{(k+1)} = \Pi_{[-1/3,\,1/3]}\left(\nu^{(k)} + \alpha_k s^{(k)}\right)$$

Xuất phát từ $$\nu^{(0)} = 0$$ (có $$g(0) = 0$$):

$$\alpha_0 = \frac{2 - 0}{36} = \frac{1}{18}$$

$$\nu^{(1)} = 0 + \frac{1}{18} \cdot (-6) = -\frac{1}{3}$$ ✓ (thuộc miền xác định).

Thuật toán hội tụ chỉ sau 1 bước: $$g(-1/3) = 2 = g^*$$, tương ứng với nghiệm gốc $$x^* = (0, 0, 2)$$ có $$\|x^*\|_1 = 2$$.

</details>

---

## 📝 **Phần V: Phương pháp Subgradient có chiếu**

### **Bài tập 5: Subgradient có chiếu cho bài toán tối ưu có ràng buộc**

$$\min_{x} \|x - c\|_1 \quad \text{s.t.} \quad \|x\|_2 \leq R$$

với $$c = (2, 3)^T$$, $$R = 2$$.

**Yêu cầu:**  
a) Viết công thức cập nhật của phương pháp subgradient có chiếu.  
b) Thực hiện các bước lặp xuất phát từ $$x^{(0)} = (0, 0)$$.  
c) Tìm nghiệm chính xác của bài toán.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Phương pháp subgradient có chiếu:**

$$x^{(k+1)} = \Pi_C\left(x^{(k)} - \alpha_k g^{(k)}\right)$$

với $$C = \{x : \|x\|_2 \leq R\}$$ và $$g^{(k)} \in \partial f(x^{(k)})$$.

**Phép chiếu lên hình cầu $$\ell_2$$:**

$$\Pi_C(y) = \begin{cases}
y & \text{nếu } \|y\| \leq R \\
R \frac{y}{\|y\|} & \text{nếu } \|y\| > R
\end{cases}$$

---

**b) Các bước lặp:**

Tại $$x^{(0)} = (0, 0)$$:

$$\partial f(0, 0) = \partial \|(0, 0) - (2, 3)\|_1 = \partial(|{-2}| + |{-3}|)$$

Subgradient: $$g = \text{sign}(x - c) = (-1, -1)$$.

Chọn $$\alpha_0 = 1$$:

$$\tilde{x}^{(1)} = (0, 0) - 1 \cdot (-1, -1) = (1, 1)$$

Vì $$\|\tilde{x}^{(1)}\| = \sqrt{2} < 2$$ nên điểm nằm trong $$C$$, không cần chiếu:

$$x^{(1)} = (1, 1)$$

---

Ở bước tiếp theo:

$$g^{(1)} = \text{sign}((1, 1) - (2, 3)) = (-1, -1)$$

$$\tilde{x}^{(2)} = (1, 1) + (1, 1) = (2, 2)$$

Vì $$\|\tilde{x}^{(2)}\| = 2\sqrt{2} > 2$$, ta chiếu lên biên của hình cầu $$C$$:

$$x^{(2)} = 2 \cdot \frac{(2, 2)}{2\sqrt{2}} = \frac{2}{\sqrt{2}}(1, 1) = (\sqrt{2}, \sqrt{2})$$

---

**c) Nghiệm chính xác:**

Ta cần cực tiểu hóa $$\|x - c\|_1$$ trên tập $$\|x\|_2 \leq 2$$.

**Nghiệm không ràng buộc:** $$x = c = (2, 3)$$, nhưng $$\|c\|_2 = \sqrt{13} > 2$$ nên không khả thi.

**Nghiệm có ràng buộc:** Vì $$c$$ nằm ngoài hình cầu, nghiệm tối ưu nằm trên biên $$\|x\|_2 = 2$$. (Lưu ý rằng phép chiếu $$c$$ lên hình cầu chỉ tối ưu cho khoảng cách $$\ell_2$$, không tối ưu cho chuẩn $$\ell_1$$.) Trên biên trong miền $$x_1 < 2$$, $$x_2 < 3$$:

$$f(x) = (2 - x_1) + (3 - x_2) = 5 - (x_1 + x_2)$$

Do đó bài toán tương đương với $$\max\; (x_1 + x_2)$$ trên đường tròn $$x_1^2 + x_2^2 = 4$$, đạt cực đại tại $$x_1 = x_2 = \sqrt{2}$$:

$$x^* = (\sqrt{2}, \sqrt{2}) \approx (1.414, 1.414)$$

**Giá trị hàm mục tiêu:** $$f(x^*) = 5 - 2\sqrt{2} \approx 2.172$$ (trong khi điểm chiếu $$\frac{2}{\sqrt{13}}(2,3)$$ cho giá trị $$2.227$$, lớn hơn). Điểm này trùng khớp với kết quả $$x^{(2)}$$ thu được ở câu b.

</details>

---

## 💡 **Tổng kết**

### **So sánh Gradient Descent và Phương pháp Subgradient:**

| Tiêu chí | Gradient Descent | Phương pháp Subgradient |
|----------|------------------|-------------------------|
| **Phạm vi áp dụng** | Hàm trơn $$f$$ | Hàm lồi không trơn $$f$$ |
| **Tốc độ hội tụ** | Tuyến tính ($$O(\rho^k)$$, khi lồi mạnh) | Dưới tuyến tính ($$O(1/\sqrt{k})$$) |
| **Kích thước bước** | Cố định hoặc tìm kiếm đường thẳng | Giảm dần hoặc bước Polyak |
| **Tính giảm đơn điệu** | Luôn giảm (với bước phù hợp) | Có thể tăng ở một số bước |
| **Ứng dụng điển hình** | Hàm khả vi trơn | Phạt $$\ell_1$$, hàm max, bài toán có ràng buộc |

### **Các quy tắc chọn kích thước bước:**

1. **Bước cố định $$\alpha$$:** Hội tụ đến lân cận của nghiệm tối ưu.
2. **Bước giảm dần $$\frac{1}{k}$$:** Hội tụ chính xác nhưng rất chậm (cận $$O(1/\log k)$$).
3. **Tổng bình phương hội tụ $$\frac{1}{k^{0.6}}$$:** Hội tụ chính xác với cận $$O(1/k^{0.4})$$, nhanh hơn $$\frac{1}{k}$$.
4. **Bước Polyak:** Hội tụ nhanh khi biết trước $$f^*$$.

### **Khi nào nên dùng phương pháp Subgradient:**
- Hàm mục tiêu không khả vi (chứa chuẩn $$\ell_1$$, hàm $$\max$$).
- Cần chi phí tính toán mỗi bước lặp thấp và đơn giản.
- Có thể chấp nhận tốc độ hội tụ chậm hơn.
- Xử lý ràng buộc thông qua phép chiếu.

---

## 📚 **Tài liệu Tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Section 3.1.

2. **Shor, N. Z.** (1985). *Minimization Methods for Non-Differentiable Functions*. Springer.

3. **Polyak, B. T.** (1987). *Introduction to Optimization*. Optimization Software.

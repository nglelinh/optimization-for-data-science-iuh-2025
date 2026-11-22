---
layout: post
title: 22-06 Bài Tập Thực Hành - Conditional Gradient (Frank-Wolfe)
chapter: '22'
order: 7
owner: GitHub Copilot
lang: vi
categories:
- chapter22
lesson_type: required
redirect_from:
  - /contents/vi/chapter22/22_05_Practical_Exercises_Conditional_Gradient/
---

# Bài Tập Thực Hành - Phương pháp Gradient có điều kiện (Frank-Wolfe)

Các bài tập dưới đây được tham khảo từ Jaggi (2013) và Lacoste-Julien & Jaggi (2015).

---

## 📝 **Bài tập 1: Frank-Wolfe cơ bản**

Xét bài toán $$\min_{x \in C} f(x)$$ với $$f(x) = \frac{1}{2}\|x\|^2$$ và $$C = \{x : \|x\|_1 \leq 1\}$$.

**Yêu cầu:**  
a) Viết bộ giải cực tiểu tuyến tính (Linear Minimization Oracle — LMO).  
b) Thực hiện vài vòng lặp xuất phát từ $$x^{(0)} = 0$$.  
c) Nêu tốc độ hội tụ.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Bộ giải cực tiểu tuyến tính (LMO):**

$$s^{(k)} = \arg\min_{s \in C} \langle \nabla f(x^{(k)}), s \rangle = \arg\min_{\|s\|_1 \leq 1} \langle x^{(k)}, s \rangle$$

Nghiệm tối ưu là $$s = -\text{sign}(x_i^{(k)}) e_i$$ với $$i = \arg\max_j |x_j^{(k)}|$$.

**b) Các bước lặp:**

$$d^{(k)} = s^{(k)} - x^{(k)}$$

$$\gamma^{(k)} = \frac{2}{k+2}$$ (kích thước bước mặc định với chỉ số $$k = 0, 1, 2, \ldots$$)

$$x^{(k+1)} = x^{(k)} + \gamma^{(k)} d^{(k)} = (1 - \gamma^{(k)})x^{(k)} + \gamma^{(k)} s^{(k)}$$

*Vòng 0:* $$x^{(0)} = 0$$, $$\nabla f(x^{(0)}) = 0$$, chọn tùy ý một đỉnh $$s^{(0)}$$ (ví dụ $$e_1$$):

$$x^{(1)} = \frac{2}{2}e_1 = e_1$$

*Vòng 1:* $$\nabla f(e_1) = e_1$$, suy ra $$s^{(1)} = -e_1$$:

$$x^{(2)} = \frac{1}{3}e_1 + \frac{2}{3}(-e_1) = -\frac{1}{3}e_1$$

**c) Tốc độ hội tụ:**

$$f(x^{(k)}) - f^* \leq \frac{2C_f}{k+2}$$

trong đó $$C_f$$ là hằng số độ cong (curvature constant) của $$f$$ trên $$C$$ (thỏa mãn $$C_f \leq L \cdot \text{diam}(C)^2$$ với $$L$$ là hằng số Lipschitz của $$\nabla f$$).

Thuật toán đạt tốc độ hội tụ **$$O(1/k)$$**.

</details>

---

## 📝 **Bài tập 2: Không cần phép chiếu (Projection-Free)**

So sánh Frank-Wolfe với Projected Gradient Descent trên hình cầu $$\ell_1$$.

**Yêu cầu:**  
a) Độ phức tạp của phép chiếu $$\Pi_{\ell_1}(y)$$.  
b) Độ phức tạp của LMO.  
c) Khi nào Frank-Wolfe có lợi thế hơn?

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Phép chiếu lên hình cầu $$\ell_1$$:**

$$\Pi_{\|\cdot\|_1 \leq 1}(y) = \arg\min_{\|x\|_1 \leq 1} \|x - y\|^2$$

Thuật toán sử dụng co ngưỡng mềm với ngưỡng chọn thích nghi, có độ phức tạp $$O(n \log n)$$ nếu dùng sắp xếp (hoặc $$O(n)$$ kỳ vọng với thuật toán chọn trung vị).

**b) Bộ giải cực tiểu tuyến tính (LMO):**

$$s = \arg\min_{\|s\|_1 \leq 1} \langle g, s \rangle = -\text{sign}(g_{\max}) e_{\max}$$

Độ phức tạp: $$O(n)$$ (chỉ cần tìm phần tử có trị tuyệt đối lớn nhất).

**c) Ưu điểm của Frank-Wolfe:**

* **Với số chiều $$n$$ lớn:** Chi phí $$O(n)$$ của LMO nhẹ hơn đáng kể so với sắp xếp $$O(n \log n)$$.
* **Điểm lặp thưa:** Mỗi $$x^{(k)}$$ là tổ hợp lồi của tối đa $$k+1$$ nguyên tử.
* **Không cần tinh chỉnh bước:** Kích thước bước mặc định $$\gamma = \frac{2}{k+2}$$ đảm bảo hội tụ.

</details>

---

## 📝 **Bài tập 3: Tìm kiếm đường thẳng (Line Search)**

Thay kích thước bước mặc định $$\gamma = \frac{2}{k+2}$$ bằng tìm kiếm đường thẳng chính xác (exact line search).

**Yêu cầu:**  
a) Phát biểu công thức $$\gamma^* = \arg\min_{\gamma \in [0,1]} f(x + \gamma d)$$.  
b) Tính nghiệm đóng cho hàm bậc hai $$f(x) = \frac{1}{2}x^TQx - b^Tx$$ (với $$Q \succ 0$$).  
c) So sánh hội tụ.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tìm kiếm đường thẳng chính xác:**

$$\gamma^{(k)} = \arg\min_{\gamma \in [0,1]} f(x^{(k)} + \gamma d^{(k)})$$

**b) Trường hợp hàm bậc hai:**

$$f(x + \gamma d) = \frac{1}{2}(x + \gamma d)^TQ(x + \gamma d) - b^T(x + \gamma d)$$

Đặt đạo hàm theo $$\gamma$$ bằng 0:

$$\frac{d}{d\gamma}f(x + \gamma d) = d^TQ(x + \gamma d) - b^Td = 0$$

$$\gamma^* = \frac{b^Td - x^TQd}{d^TQd} = \frac{-\nabla f(x)^T d}{d^TQd}$$

Sau đó cắt ngưỡng (clip) $$\gamma^*$$ vào đoạn $$[0, 1]$$.

**c) So sánh hội tụ:**

* **Bước mặc định $$\gamma = 2/(k+2)$$:** tốc độ $$O(1/k)$$.
* **Tìm kiếm đường thẳng chính xác:** vẫn giữ bậc $$O(1/k)$$ nhưng có hằng số tốt hơn.
* **Thực nghiệm:** Thường hội tụ nhanh hơn rõ rệt trong thực tế.

</details>

---

## 📝 **Bài tập 4: Frank-Wolfe với bước rời xa (Away-Step Frank-Wolfe)**

Bổ sung bước rời xa (away step) nhằm khắc phục tốc độ hội tụ chậm gần biên.

**Yêu cầu:**  
a) Xác định tập hoạt động $$\mathcal{S}^{(k)}$$.  
b) Viết hướng rời xa $$d_A = x - v_A$$.  
c) Nêu quy tắc chọn giữa bước Frank-Wolfe và bước rời xa.

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Tập hoạt động:**

$$x^{(k)} = \sum_{v \in \mathcal{S}^{(k)}} \alpha_v v$$ với $$\alpha_v > 0$$ và $$\sum_{v \in \mathcal{S}^{(k)}} \alpha_v = 1$$

(tập các đỉnh có trọng số dương trong biểu diễn tổ hợp lồi của $$x^{(k)}$$).

**b) Đỉnh rời xa và hướng rời xa:**

$$v_A = \arg\max_{v \in \mathcal{S}^{(k)}} \langle \nabla f(x^{(k)}), v \rangle$$

$$d_A = x^{(k)} - v_A$$

**c) Quy tắc chọn bước:**

$$g_{\text{FW}} = \langle \nabla f(x^{(k)}), s - x^{(k)} \rangle$$

$$g_{\text{away}} = \langle \nabla f(x^{(k)}), x^{(k)} - v_A \rangle$$

Nếu $$g_{\text{FW}} \leq g_{\text{away}}$$: chọn bước Frank-Wolfe với $$\gamma_{\max} = 1$$.  
Ngược lại: chọn bước rời xa với $$\gamma_{\max} = \frac{\alpha_{v_A}}{1 - \alpha_{v_A}}$$ (để đảm bảo trọng số của $$v_A$$ sau cập nhật không âm).

**Kết quả:** Loại bỏ được các đỉnh thừa trong tập hoạt động và cải thiện tốc độ hội tụ (đạt hội tụ tuyến tính khi $$f$$ lồi mạnh trên đa diện).

</details>

---

## 📝 **Bài tập 5: Các ứng dụng tiêu biểu**

**Yêu cầu:** Nêu LMO và ưu thế của Frank-Wolfe trên:  
a) Hình cầu chuẩn hạt nhân (nuclear norm ball): $$\|X\|_* \leq \tau$$.  
b) Đa diện ghép cặp (matching polytope).  
c) Mô hình đồ thị xác suất (probabilistic graphical models).

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Hình cầu chuẩn hạt nhân:**

*LMO:* $$S = \arg\min_{\|S\|_* \leq \tau} \langle G, S \rangle = -\tau u_1 v_1^T$$

với $$(u_1, v_1)$$ là cặp vector kỳ dị hàng đầu của $$G$$.

*Độ phức tạp:* Chi phí tìm cặp vector kỳ dị hàng đầu $$O(mn)$$ (mỗi phép nhân ma trận–vector) thấp hơn nhiều so với phân rã SVD đầy đủ $$O(m^2n)$$ cần cho phép chiếu (giả sử $$m \leq n$$).

**b) Đa diện ghép cặp:**

*LMO:* Quy về bài toán ghép cặp hoàn hảo có trọng số nhỏ nhất (minimum weight perfect matching).

*Độ phức tạp:* $$O(n^3)$$ bằng thuật toán Hungary, trong khi phép chiếu lên đa diện này khó thực hiện trực tiếp.

**c) Mô hình đồ thị xác suất:**

*LMO:* Tương đương với bài toán suy luận MAP.

*Ưu điểm:* Thuật toán vẫn làm việc được ngay cả khi bộ giải LMO chỉ tính gần đúng.

</details>

---

## 💡 **Tổng kết**

**Ưu điểm của Frank-Wolfe:**

| Khía cạnh | Lợi ích |
|-----------|---------|
| **Không cần phép chiếu** | LMO tốn $$O(n)$$ thay vì phép chiếu $$O(n \log n)$$ |
| **Điểm lặp thưa** | Tự động tạo nghiệm thưa nhờ tổ hợp lồi của ít đỉnh |
| **Kích thước bước đơn giản** | Quy tắc $$\gamma = 2/(k+2)$$ không cần tinh chỉnh |
| **Ràng buộc có cấu trúc** | LMO dễ tính hơn nhiều so với phép chiếu |

**Hạn chế:**

* Tốc độ hội tụ $$O(1/k)$$ chậm hơn các phương pháp có gia tốc.
* Phiên bản cơ bản không tự tận dụng được tính lồi mạnh.
* Có thể dao động zíc-zắc khi nghiệm nằm trên biên.

**Khi nào nên dùng:**

* Phép chiếu lên tập ràng buộc tốn kém.
* Cần nghiệm có cấu trúc thưa (tổ hợp ít nguyên tử).
* Ràng buộc có cấu trúc tổ hợp hoặc ma trận (chuẩn hạt nhân, đa diện ghép cặp).

---

## 📚 **Tài liệu Tham khảo**

1. Jaggi, M. (2013). "Revisiting Frank-Wolfe: Projection-Free Sparse Convex Optimization". *ICML*.
2. Lacoste-Julien, S., & Jaggi, M. (2015). "On the Global Linear Convergence of Frank-Wolfe". *NeurIPS*.

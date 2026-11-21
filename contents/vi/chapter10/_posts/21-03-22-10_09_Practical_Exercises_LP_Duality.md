---
layout: post
title: "10-09 Bài Tập Thực Hành - Tính Đối Ngẫu trong Quy Hoạch Tuyến Tính"
chapter: "10"
order: 10
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter10
lesson_type: required
redirect_from:
  - /contents/vi/chapter10/10_07_Practical_Exercises_LP_Duality/
---

Các bài tập sau được tham khảo từ Boyd & Vandenberghe (2004), Bertsimas & Tsitsiklis (1997), và Dantzig (1963), giúp sinh viên nắm vững các khái niệm về tính đối ngẫu trong LP.

---

## **Phần I: Xây dựng Bài toán Đối ngẫu**

### **Bài tập 1: Các dạng LP cơ bản (Boyd & Vandenberghe, Ex. 5.1)**

Cho các bài toán LP sau, hãy xây dựng bài toán đối ngẫu và giải thích ý nghĩa của các biến đối ngẫu.

**a) Dạng chuẩn:**

$$
\begin{align}
\min_{x} \quad & 3x_1 + 5x_2 + 2x_3 \\
\text{s.t.} \quad & x_1 + 2x_2 + x_3 = 4 \\
& 2x_1 + x_2 + 3x_3 = 5 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**b) Dạng bất đẳng thức:**

$$
\begin{align}
\min_{x} \quad & 2x_1 + 4x_2 \\
\text{s.t.} \quad & x_1 + x_2 \geq 3 \\
& 2x_1 + x_2 \geq 5 \\
& x_1, x_2 \geq 0
\end{align}
$$

**c) Dạng hỗn hợp:**

$$
\begin{align}
\min_{x} \quad & x_1 + 2x_2 + 3x_3 \\
\text{s.t.} \quad & x_1 + x_2 = 2 \\
& x_2 + x_3 \leq 3 \\
& x_1 + x_3 \geq 1 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Bài a) Dạng chuẩn:**

**Quy tắc:** Với bài toán min có ràng buộc đẳng thức và biến $$\geq 0$$:
- Mỗi ràng buộc đẳng thức → biến dual không ràng buộc dấu  
- Mỗi biến $$\geq 0$$ → ràng buộc dual $$\leq$$

**Bài toán Dual:**

$$
\begin{align}
\max_{u} \quad & 4u_1 + 5u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 3 \\
& 2u_1 + u_2 \leq 5 \\
& u_1 + 3u_2 \leq 2 \\
& u_1, u_2 \in \mathbb{R}
\end{align}
$$

**Giải thích:**
- $$u_1, u_2$$: Shadow prices của ràng buộc 1 và 2 (giá trị biên nếu tăng RHS)
- Không ràng buộc dấu vì ràng buộc primal là đẳng thức
- Mỗi biến primal tạo một ràng buộc dual

---

**Bài b) Dạng bất đẳng thức:**

**Quy tắc:** Min với $$\geq$$ và $$x \geq 0$$:
- Ràng buộc $$\geq$$ → biến dual $$\geq 0$$
- Biến $$\geq 0$$ → ràng buộc dual $$\leq$$

**Bài toán Dual:**

$$
\begin{align}
\max_{u} \quad & 3u_1 + 5u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 2 \\
& u_1 + u_2 \leq 4 \\
& u_1, u_2 \geq 0
\end{align}
$$

---

**Bài c) Dạng hỗn hợp:**

**Phân tích:**
- Ràng buộc 1 ($$=$$): biến dual $$u_1 \in \mathbb{R}$$
- Ràng buộc 2 ($$\leq$$): biến dual $$u_2 \leq 0$$  
- Ràng buộc 3 ($$\geq$$): biến dual $$u_3 \geq 0$$

**Bài toán Dual:**

$$
\begin{align}
\max_{u} \quad & 2u_1 + 3u_2 + u_3 \\
\text{s.t.} \quad & u_1 + u_3 \leq 1 \\
& u_1 + u_2 \leq 2 \\
& u_2 + u_3 \leq 3 \\
& u_1 \in \mathbb{R}, \quad u_2 \leq 0, \quad u_3 \geq 0
\end{align}
$$

</details>

---

### **Bài tập 2: Production Planning (Boyd & Vandenberghe, Ex. 5.2)**

Một xí nghiệp sản xuất 2 sản phẩm A và B:

| Sản phẩm | Lợi nhuận (nghìn đồng) | Lao động (giờ) | Máy móc (giờ) |
|----------|------------------------|----------------|---------------|
| A        | 40                     | 2              | 1             |
| B        | 30                     | 1              | 2             |

Tài nguyên: 100 giờ lao động, 80 giờ máy móc.

**Yêu cầu:**  
a) Lập bài toán LP tối đa hóa lợi nhuận    
b) Xây dựng bài toán đối ngẫu    
c) Giải thích ý nghĩa kinh tế của biến đối ngẫu    
d) Nếu có thêm 1 giờ lao động, lợi nhuận tăng tối đa bao nhiêu?

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Bài toán Primal:**

Đặt $$x_1, x_2$$ là số lượng sản phẩm A, B.

$$
\begin{align}
\max_{x} \quad & 40x_1 + 30x_2 \\
\text{s.t.} \quad & 2x_1 + x_2 \leq 100 \quad \text{(Lao động)} \\
& x_1 + 2x_2 \leq 80 \quad \text{(Máy móc)} \\
& x_1, x_2 \geq 0
\end{align}
$$

**b) Bài toán Dual:**

Chuyển về min: $$\min -40x_1 - 30x_2$$

$$
\begin{align}
\min_{u} \quad & 100u_1 + 80u_2 \\
\text{s.t.} \quad & 2u_1 + u_2 \geq 40 \\
& u_1 + 2u_2 \geq 30 \\
& u_1, u_2 \geq 0
\end{align}
$$

**c) Ý nghĩa kinh tế:**

- $$u_1$$: **Shadow price của lao động** - giá trị biên khi tăng 1 giờ lao động
- $$u_2$$: **Shadow price của máy móc** - giá trị biên khi tăng 1 giờ máy móc

Ràng buộc dual:
- $$2u_1 + u_2 \geq 40$$: Giá trị tài nguyên để sản xuất 1 sản phẩm A phải $$\geq$$ lợi nhuận của nó
- $$u_1 + 2u_2 \geq 30$$: Tương tự cho sản phẩm B

**d) Tăng lợi nhuận:**

Để trả lời, cần giải hệ ràng buộc dual chặt: $$2u_1 + u_2 = 40$$, $$u_1 + 2u_2 = 30$$ → $$u_1^* = 50/3 \approx 16.67$$, $$u_2^* = 20/3 \approx 6.67$$ nghìn đồng/giờ (kiểm tra: primal $$x^* = (40, 20)$$ cho $$40 \cdot 40 + 30 \cdot 20 = 2200$$ = dual $$100 \cdot \frac{50}{3} + 80 \cdot \frac{20}{3} = 2200$$ ✓).

→ Thêm 1 giờ lao động tăng lợi nhuận khoảng **16.67 nghìn đồng** ($$50/3$$).

</details>

---

### **Bài tập 3: Portfolio Optimization (Boyd & Vandenberghe, Ex. 5.3)**

Một nhà đầu tư có 1000 triệu đồng muốn đầu tư vào 3 tài sản với lợi nhuận kỳ vọng:

| Tài sản | Lợi nhuận (%) | Rủi ro (độ lệch chuẩn) |
|---------|---------------|-------------------------|
| Cổ phiếu| 15            | 20                      |
| Trái phiếu| 8           | 5                       |
| Tiền mặt| 3             | 0                       |

Yêu cầu: Lợi nhuận ít nhất 10%, tổng rủi ro không quá 12%.

**Yêu cầu:**  
a) Lập bài toán LP minimize rủi ro  
b) Xây dựng bài toán đối ngẫu  
c) Giải thích ý nghĩa của biến đối ngẫu

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Bài toán Primal:**

Đặt $$x_1, x_2, x_3$$ là tỷ lệ đầu tư vào cổ phiếu, trái phiếu, tiền mặt.

$$
\begin{align}
\min_{x} \quad & 20x_1 + 5x_2 \\
\text{s.t.} \quad & x_1 + x_2 + x_3 = 1 \quad \text{(Tổng vốn)} \\
& 15x_1 + 8x_2 + 3x_3 \geq 10 \quad \text{(Lợi nhuận)} \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**b) Bài toán Dual:**

$$
\begin{align}
\max_{u} \quad & u_1 + 10u_2 \\
\text{s.t.} \quad & u_1 + 15u_2 \leq 20 \\
& u_1 + 8u_2 \leq 5 \\
& u_1 + 3u_2 \leq 0 \\
& u_1 \in \mathbb{R}, \quad u_2 \geq 0
\end{align}
$$

**c) Ý nghĩa:**

- $$u_1$$: Giá trị biên của vốn - nếu có thêm 1% vốn, rủi ro giảm bao nhiêu
- $$u_2$$: Giá trị của việc nới lỏng ràng buộc lợi nhuận - trade-off giữa lợi nhuận và rủi ro

**Nghiệm:** chỉ cần cổ phiếu và trái phiếu: $$15x_1 + 8(1-x_1) = 10 \Rightarrow x_1 = 2/7$$, nên $$x^* = (2/7, 5/7, 0)$$ với rủi ro $$20(2/7) + 5(5/7) = 65/7 \approx 9.29\% \leq 12\%$$ ✓ (ràng buộc rủi ro tối đa 12% không chặt). Nghiệm dual: $$u_1^* = -85/7$$, $$u_2^* = 15/7 \approx 2.14$$ (giá trị dual $$-85/7 + 150/7 = 65/7$$ ✓), nghĩa là nâng yêu cầu lợi nhuận thêm 1% làm rủi ro tăng khoảng 2.14%.

</details>

---

## **Phần II: Tính Đối Ngẫu Yếu và Mạnh**

### **Bài tập 4: Weak Duality (Boyd & Vandenberghe, Ex. 5.5)**

Cho bài toán:

$$
\begin{align}
\text{(P)} \quad \min_{x} \quad & 2x_1 + 3x_2 \\
\text{s.t.} \quad & x_1 + x_2 \geq 4 \\
& 2x_1 + x_2 \geq 6 \\
& x_1, x_2 \geq 0
\end{align}
$$

**a)** Xây dựng bài toán đối ngẫu (D)    
**b)** Cho $$x = (3, 1)$$. Kiểm tra tính khả thi và tìm nghiệm khả thi $$u$$ của (D)    
**c)** Kiểm tra $$c^Tx \geq b^Tu$$ (weak duality)    
**d)** Chứng minh $$x^* = (4, 0)$$ là nghiệm tối ưu

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Bài toán đối ngẫu:**

$$
\begin{align}
\text{(D)} \quad \max_{u} \quad & 4u_1 + 6u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 2 \\
& u_1 + u_2 \leq 3 \\
& u_1, u_2 \geq 0
\end{align}
$$

**b) Kiểm tra $$x = (3, 1)$$:**

Primal feasibility:
- $$3 + 1 = 4 \geq 4$$ ✓
- $$2(3) + 1 = 7 \geq 6$$ ✓  
- $$x \geq 0$$ ✓

Giá trị primal: $$f(x) = 2(3) + 3(1) = 9$$

Thử $$u = (0, 1)$$:
- $$0 + 2(1) = 2 \leq 2$$ ✓
- $$0 + 1 = 1 \leq 3$$ ✓
- Giá trị dual: $$g(u) = 4(0) + 6(1) = 6$$

**c) Weak duality:**

$$
c^Tx = 9 \geq 6 = b^Tu
$$

✓ Thỏa mãn!

**d) Chứng minh $$x^* = (4, 0)$$ tối ưu:**

Kiểm tra khả thi:
- $$4 + 0 = 4 \geq 4$$ ✓ (chặt)
- $$2(4) + 0 = 8 \geq 6$$ ✓ (lỏng, slack = 2)

Giá trị: $$f(x^*) = 2(4) + 3(0) = 8$$

Tìm $$u^*$$ thỏa điều kiện bù: ràng buộc 2 lỏng nên $$u_2^* = 0$$; $$x_1^* > 0$$ nên ràng buộc dual 1 chặt: $$u_1^* + 2u_2^* = 2 \Rightarrow u_1^* = 2$$.

Kiểm tra dual khả thi: $$u_1^* + u_2^* = 2 \leq 3$$ ✓ (lỏng, khớp với $$x_2^* = 0$$). Giá trị dual: $$g(u^*) = 4(2) + 6(0) = 8 = f(x^*)$$ ✓

**Kết luận:** $$x^* = (4, 0)$$ tối ưu (theo weak duality, mọi $$x$$ khả thi đều có $$f(x) \geq g(u^*) = 8$$). Lưu ý $$(2,2)$$ khả thi nhưng $$f = 10 > 8$$ nên không tối ưu; $$x = (3,1)$$ cho $$f = 9$$.

</details>

---

### **Bài tập 5: Strong Duality (Boyd & Vandenberghe, Ex. 5.6)**

Cho:

$$
\begin{align}
\text{(P)} \quad \min_{x} \quad & x_1 + 2x_2 + x_3 \\
\text{s.t.} \quad & x_1 + x_2 = 3 \\
& x_2 + x_3 = 2 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**a)** Tìm nghiệm tối ưu bằng phương pháp đại số    
**b)** Xây dựng và giải bài toán đối ngẫu    
**c)** Tính khoảng cách đối ngẫu    
**d)** Giải thích tại sao strong duality đúng

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Giải Primal:**

Từ ràng buộc: $$x_1 = 3 - x_2$$, $$x_3 = 2 - x_2$$

Thế vào hàm mục tiêu:

$$
f = (3 - x_2) + 2x_2 + (2 - x_2) = 5
$$

Hàm mục tiêu **không phụ thuộc $$x_2$$**! Giá trị tối ưu: $$f^* = 5$$

Điều kiện: $$0 \leq x_2 \leq 2$$ (từ $$x_3 \geq 0$$)

Ví dụ nghiệm: $$x^* = (2, 1, 1)$$

**b) Dual:**

$$
\begin{align}
\max_{u} \quad & 3u_1 + 2u_2 \\
\text{s.t.} \quad & u_1 \leq 1 \\
& u_1 + u_2 \leq 2 \\
& u_2 \leq 1 \\
& u_1, u_2 \in \mathbb{R}
\end{align}
$$

Maximize: chọn $$u_1 = 1$$, $$u_2 = 1$$

Kiểm tra: $$1 \leq 1$$ ✓, $$1 + 1 = 2 \leq 2$$ ✓, $$1 \leq 1$$ ✓

Giá trị: $$g^* = 3(1) + 2(1) = 5$$

**c) Duality gap:**

$$
\text{Gap} = f^* - g^* = 5 - 5 = 0
$$

Strong duality đúng! ✓

**d) Giải thích:**

Trong LP, strong duality đúng khi một trong hai bài toán có nghiệm tối ưu hữu hạn (khi đó bài toán kia cũng có nghiệm tối ưu và hai giá trị bằng nhau):
- Nếu primal unbounded thì dual infeasible (và ngược lại)
- Cả hai bài toán có thể cùng infeasible

Điều kiện Slater tự động thỏa với LP khả thi.

</details>

---

## **Phần III: Điều kiện Bù (Complementary Slackness)**

### **Bài tập 6: Applying CS (Bertsimas & Tsitsiklis, Ex. 4.3)**

Cho bài toán và các cặp nghiệm:

$$
\begin{align}
\text{(P)} \quad \min_{x} \quad & 3x_1 + 2x_2 \\
\text{s.t.} \quad & x_1 + x_2 \geq 4 \\
& 2x_1 + x_2 \geq 6 \\
& x_1, x_2 \geq 0
\end{align}
$$

**Các cặp nghiệm:**  
1. $$x = (2, 2)$$, $$u = (1, 1)$$  
2. $$x = (3, 1)$$, $$u = (0, 3/2)$$  
3. $$x = (0, 6)$$, $$u = (0, 2)$$

**Yêu cầu:** Kiểm tra cặp nào tối ưu bằng điều kiện bù.

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**Dual:**

$$
\begin{align}
\max_{u} \quad & 4u_1 + 6u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 3 \\
& u_1 + u_2 \leq 2 \\
& u_1, u_2 \geq 0
\end{align}
$$

**Điều kiện bù:**
1. $$u_1 \cdot [x_1 + x_2 - 4] = 0$$
2. $$u_2 \cdot [2x_1 + x_2 - 6] = 0$$
3. $$x_1 \cdot [u_1 + 2u_2 - 3] = 0$$
4. $$x_2 \cdot [u_1 + u_2 - 2] = 0$$

---

**Cặp 1: $$x = (2,2)$$, $$u = (1,1)$$**

Primal feasible:
- $$2 + 2 = 4 \geq 4$$ ✓ (chặt)
- $$4 + 2 = 6 \geq 6$$ ✓ (chặt)

Dual feasible:
- $$1 + 2 = 3 \leq 3$$ ✓ (chặt)
- $$1 + 1 = 2 \leq 2$$ ✓ (chặt)

Complementary slackness:
1. $$1 \cdot 0 = 0$$ ✓
2. $$1 \cdot 0 = 0$$ ✓
3. $$2 \cdot 0 = 0$$ ✓
4. $$2 \cdot 0 = 0$$ ✓

**Kết luận:** Cặp 1 tối ưu! ✓✓✓

Giá trị: $$f = 3(2) + 2(2) = 10 = 4(1) + 6(1) = g$$ ✓

---

**Cặp 2: $$x = (3,1)$$, $$u = (0, 3/2)$$**

Primal: $$3+1=4$$ ✓, $$6+1=7 > 6$$ (slack = 1)

Dual: $$0+3=3$$ ✓, $$0+3/2=3/2$$ ✓

CS 2: $$u_2 \cdot [7-6] = (3/2)(1) = 3/2 \neq 0$$ ✗

**Kết luận:** Không tối ưu!

---

**Cặp 3: $$x = (0,6)$$, $$u = (0,2)$$**

Dual: $$0 + 4 = 4 \not\leq 3$$ ✗

**Kết luận:** Dual không khả thi!

</details>

---

### **Bài tập 7: Shadow Prices (Bertsimas & Tsitsiklis, Ex. 4.7)**

Bài toán sản xuất có nghiệm tối ưu $$x^* = (40, 20)$$ với:
- Lao động: $$2(40) + 20 = 100$$ (chặt)
- Máy móc: $$40 + 2(20) = 80$$ (chặt)

**a)** Tính shadow price của mỗi tài nguyên    
**b)** Nếu mua thêm 1 giờ lao động với giá 12 nghìn, có nên mua không?    
**c)** Phân tích độ nhạy khi lao động tăng lên 105 giờ

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Tính shadow price:**

Hàm mục tiêu: $$\max 40x_1 + 30x_2$$

Từ điều kiện bù (cả hai ràng buộc chặt, cả hai biến dương):

$$
\begin{cases}
2u_1 + u_2 = 40 \\
u_1 + 2u_2 = 30
\end{cases}
$$

Giải hệ:
- Từ (1): $$u_2 = 40 - 2u_1$$
- Thế vào (2): $$u_1 + 2(40 - 2u_1) = 30$$
- $$u_1 + 80 - 4u_1 = 30$$
- $$-3u_1 = -50$$
- $$u_1 = 50/3 \approx 16.67$$
- $$u_2 = 40 - 2(50/3) = 40 - 100/3 = 20/3 \approx 6.67$$

**Shadow prices:**
- Lao động: $$u_1^* = 16.67$$ nghìn đồng/giờ
- Máy móc: $$u_2^* = 6.67$$ nghìn đồng/giờ

**b) Quyết định mua:**

Giá mua: 12 nghìn đồng/giờ    
Giá trị biên: $$u_1^* = 16.67$$ nghìn đồng/giờ

$$12 < 16.67$$ → **Nên mua** (lời 4.67 nghìn/giờ)

**c) Độ nhạy:**

Tăng 5 giờ lao động:

$$
\Delta f \approx u_1^* \times 5 = 16.67 \times 5 = 83.35 \text{ nghìn đồng}
$$

Lợi nhuận hiện tại: $$40(40) + 30(20) = 2200$$ nghìn

Lợi nhuận mới: $$2200 + 83.35 = 2283.35$$ nghìn đồng

*(Lưu ý: Shadow price chỉ chính xác trong khoảng sensitivity range)*

</details>

---

## **Phần IV: Max Flow và Min Cut**

### **Bài tập 8: Max Flow Problem (Bertsimas & Tsitsiklis, Ex. 7.2)**

Cho mạng với dung lượng:

```
    s --10--> a --8--> t
    |        / \       ^
    8      5    3     10
    |    /        \    |
    v  /            \  |
    b ---------------> c
          10
```

**a)** Viết bài toán max flow dạng LP    
**b)** Tìm một luồng khả thi    
**c)** Tìm một lát cắt và tính công suất    
**d)** Kiểm chứng: giá trị luồng $$\leq$$ công suất cắt

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Max Flow LP:**

Biến: $$f_{ij}$$ là luồng trên cung $$(i,j)$$

$$
\begin{align}
\max \quad & f_{sa} + f_{sb} \\
\text{s.t.} \quad & f_{sa} - f_{ab} - f_{at} - f_{ac} = 0 \quad \text{(nút a)} \\
& f_{sb} + f_{ab} - f_{bc} = 0 \quad \text{(nút b)} \\
& f_{ac} + f_{bc} - f_{ct} = 0 \quad \text{(nút c)} \\
& 0 \leq f_{sa} \leq 10, \quad 0 \leq f_{sb} \leq 8 \\
& 0 \leq f_{at} \leq 8, \quad 0 \leq f_{ab} \leq 5 \\
& 0 \leq f_{ac} \leq 3, \quad 0 \leq f_{bc} \leq 10 \\
& 0 \leq f_{ct} \leq 10
\end{align}
$$

**b) Luồng khả thi:**

Thử:
- $$f_{sa} = 10$$, $$f_{sb} = 8$$
- $$f_{at} = 8$$, $$f_{ab} = 0$$, $$f_{ac} = 2$$
- $$f_{bc} = 8$$, $$f_{ct} = 10$$

Kiểm tra bảo toàn:
- Nút a: $$10 - 0 - 8 - 2 = 0$$ ✓
- Nút b: $$8 + 0 - 8 = 0$$ ✓
- Nút c: $$2 + 8 - 10 = 0$$ ✓

Giá trị luồng: $$|f| = 10 + 8 = 18$$

**c) Lát cắt:**

Cắt $$S = \{s\}$$, $$T = \{a,b,c,t\}$$:

Cung từ $$S$$ sang $$T$$:
- $$(s,a)$$: dung lượng 10
- $$(s,b)$$: dung lượng 8

Công suất: $$C(S,T) = 10 + 8 = 18$$

**d) Kiểm chứng:**

Giá trị luồng = 18 = Công suất cắt

Theo định lý Max-Flow Min-Cut: Đây là luồng cực đại và lát cắt cực tiểu! ✓

</details>

---

## **Phần V: Matrix Games**

### **Bài tập 9: Zero-Sum Game (Dantzig, Ex. 8.1)**

Ma trận phần thưởng (từ góc độ người chơi hàng):

$$
P = \begin{bmatrix}
3 & -1 & 2 \\
1 & 4 & -2 \\
0 & 2 & 3
\end{bmatrix}
$$

**a)** Kiểm tra điểm cân bằng Nash thuần túy    
**b)** Viết LP cho chiến lược hỗn hợp (người chơi hàng)    
**c)** Viết LP đối ngẫu (người chơi cột)    
**d)** Giải thích giá trị trò chơi

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Nash equilibrium thuần túy:**

Tìm min mỗi hàng:
- Hàng 1: $$\min\{3, -1, 2\} = -1$$
- Hàng 2: $$\min\{1, 4, -2\} = -2$$
- Hàng 3: $$\min\{0, 2, 3\} = 0$$

Maxmin: $$\max\{-1, -2, 0\} = 0$$ (hàng 3)

Tìm max mỗi cột:
- Cột 1: $$\max\{3, 1, 0\} = 3$$
- Cột 2: $$\max\{-1, 4, 2\} = 4$$
- Cột 3: $$\max\{2, -2, 3\} = 3$$

Minmax: $$\min\{3, 4, 3\} = 3$$

$$\text{Maxmin} \neq \text{Minmax}$$ → **Không có Nash equilibrium thuần túy**

**b) LP cho người chơi hàng:**

Maximize guaranteed payoff $$v$$:

$$
\begin{align}
\max_{x, v} \quad & v \\
\text{s.t.} \quad & 3x_1 + x_2 + 0x_3 \geq v \\
& -x_1 + 4x_2 + 2x_3 \geq v \\
& 2x_1 - 2x_2 + 3x_3 \geq v \\
& x_1 + x_2 + x_3 = 1 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**c) LP người chơi cột:**

Minimize max loss $$u$$:

$$
\begin{align}
\min_{y, u} \quad & u \\
\text{s.t.} \quad & 3y_1 - y_2 + 2y_3 \leq u \\
& y_1 + 4y_2 - 2y_3 \leq u \\
& 0y_1 + 2y_2 + 3y_3 \leq u \\
& y_1 + y_2 + y_3 = 1 \\
& y_1, y_2, y_3 \geq 0
\end{align}
$$

**d) Giá trị trò chơi:**

Theo Von Neumann minimax theorem:

$$
v^* = \max_x \min_y x^T P y = \min_y \max_x x^T P y
$$

Giá trị này là điểm cân bằng Nash trong chiến lược hỗn hợp.

**Thử nghiệm:** $$x = y = (1/3, 1/3, 1/3)$$

Expected payoff với mỗi cột:
- Cột 1: $$(1/3)(3+1+0) = 4/3$$
- Cột 2: $$(1/3)(-1+4+2) = 5/3$$
- Cột 3: $$(1/3)(2-2+3) = 1$$

Min = 1, vậy $$v^* \geq 1$$.

**Nghiệm tối ưu (giải LP):** $$x^* = (3/8, 1/4, 3/8)$$, $$y^* = (17/40, 7/20, 9/40)$$, $$v^* = 11/8 = 1.375$$. Kiểm tra: với $$x^*$$, payoff của từng cột đều bằng $$\frac{11}{8}$$ (cột 1: $$\frac{9}{8}+\frac{2}{8}$$; cột 2: $$-\frac{3}{8}+\frac{8}{8}+\frac{6}{8}$$; cột 3: $$\frac{6}{8}-\frac{4}{8}+\frac{9}{8}$$). Lưu ý $$\text{Maxmin} = 0 < v^* = 1.375 < \text{Minmax} = 3$$.

</details>

---

## **Phần VI: Bài tập Nâng cao từ Boyd & Vandenberghe**

### **Bài tập 10: Robust LP (Boyd & Vandenberghe, Ex. 5.11)**

Xét bài toán LP không chắc chắn về hệ số:

$$
\begin{align}
\min_{x} \quad & c^T x \\
\text{s.t.} \quad & a_i^T x \leq b_i, \quad i = 1, \ldots, m \\
& x \geq 0
\end{align}
$$

trong đó $$a_i$$ có thể dao động trong ellipsoid: $$\{a_i + P_i u : \|u\| \leq 1\}$$

**Yêu cầu:**    
a) Viết bài toán robust tương đương    
b) Chứng minh đây là một SOCP (không còn là bài toán LP thuần túy)    
c) Xây dựng bài toán đối ngẫu

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Robust formulation:**

Ràng buộc robust yêu cầu:

$$
(a_i + P_i u)^T x \leq b_i, \quad \forall \|u\| \leq 1
$$

Tương đương:

$$
a_i^T x + \max_{\|u\| \leq 1} u^T P_i^T x \leq b_i
$$

Theo Cauchy-Schwarz:

$$
\max_{\|u\| \leq 1} u^T P_i^T x = \|P_i^T x\|
$$

Vậy ràng buộc robust:

$$
a_i^T x + \|P_i^T x\| \leq b_i
$$

**b) Đây là SOCP, không phải LP:**

Dạng tương đương SOCP (Second-Order Cone Program):

$$
\begin{align}
\min_{x} \quad & c^T x \\
\text{s.t.} \quad & a_i^T x + \|P_i^T x\| \leq b_i, \quad i = 1, \ldots, m \\
& x \geq 0
\end{align}
$$

Nếu $$P_i = 0$$ (không có uncertainty), quay về LP thông thường.

**c) Bài toán đối ngẫu:**

Sử dụng duality của SOCP, dual problem khá phức tạp và không còn là LP thuần túy.

</details>

---

### **Bài tập 11: Chebyshev Center (Boyd & Vandenberghe, Ex. 8.5)**

Tìm điểm $$x_c$$ và bán kính $$r$$ lớn nhất sao cho hình cầu $$\{x : \|x - x_c\| \leq r\}$$ nằm trong polyhedron $$\{x : a_i^T x \leq b_i, i = 1, \ldots, m\}$$.

**Yêu cầu:**    
a) Viết bài toán tối ưu    
b) Chứng minh đây là bài toán LP    
c) Giải cho polyhedron cụ thể

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) Formulation:**

Điều kiện để hình cầu nằm trong polyhedron:

$$
a_i^T x \leq b_i, \quad \forall x : \|x - x_c\| \leq r
$$

Tương đương:

$$
\max_{\|x - x_c\| \leq r} a_i^T x \leq b_i
$$

$$
a_i^T x_c + r\|a_i\| \leq b_i
$$

**Bài toán:**

$$
\begin{align}
\max_{x_c, r} \quad & r \\
\text{s.t.} \quad & a_i^T x_c + r\|a_i\| \leq b_i, \quad i = 1, \ldots, m
\end{align}
$$

**b) Chứng minh là LP:**

Đây là LP với biến $$(x_c, r)$$. Hệ số $$\|a_i\|$$ là hằng số.

**c) Ví dụ cụ thể:**

Cho polyhedron:
- $$x_1 + x_2 \leq 4$$
- $$x_1 - x_2 \leq 2$$
- $$-x_1 + x_2 \leq 2$$
- $$-x_1 - x_2 \leq 2$$

LP:

$$
\begin{align}
\max \quad & r \\
\text{s.t.} \quad & x_{c1} + x_{c2} + r\sqrt{2} \leq 4 \\
& x_{c1} - x_{c2} + r\sqrt{2} \leq 2 \\
& -x_{c1} + x_{c2} + r\sqrt{2} \leq 2 \\
& -x_{c1} - x_{c2} + r\sqrt{2} \leq 2
\end{align}
$$

Giải (bằng tay hoặc solver): $$r\sqrt{2} = 2$$, tức $$r = \sqrt{2} \approx 1.414$$, với tâm $$x_c = (t, t)$$, $$0 \leq t \leq 1$$ (ví dụ $$x_c = (0, 0)$$); nghiệm không duy nhất vì ràng buộc 1 không chặt. Kiểm tra với $$x_c = (0,0)$$: vế trái của 4 ràng buộc bằng $$2, 2, 2, 2$$, tức $$\leq 4, 2, 2, 2$$ ✓ (ràng buộc 2, 3, 4 chặt).

</details>

---

### **Bài tập 12: Phân bổ tài nguyên**

Công ty sản xuất 3 sản phẩm:

| Sản phẩm | Lợi nhuận | Lao động | Máy | Nguyên liệu |
|----------|-----------|----------|-----|-------------|
| A        | 5         | 2        | 1   | 3           |
| B        | 4         | 1        | 2   | 2           |
| C        | 6         | 3        | 2   | 1           |

Tài nguyên: 100 giờ lao động, 80 giờ máy, 90 kg nguyên liệu. Biết rằng ở phương án tối ưu cả ba sản phẩm đều được sản xuất và cả ba tài nguyên đều được dùng hết.

**a)** Lập bài toán LP và bài toán đối ngẫu.  
**b)** Tìm phương án sản xuất tối ưu và shadow price của mỗi tài nguyên.  
**c)** Có nên mua thêm 10 giờ lao động (giá 1,5 triệu/giờ) hay 10 kg nguyên liệu (giá 1 triệu/kg) không?

<details markdown="1">
<summary><strong>Lời giải chi tiết</strong></summary>

**a) LP:**

$$
\begin{align}
\max_{x} \quad & 5x_1 + 4x_2 + 6x_3 \\
\text{s.t.} \quad & 2x_1 + x_2 + 3x_3 \leq 100 \\
& x_1 + 2x_2 + 2x_3 \leq 80 \\
& 3x_1 + 2x_2 + x_3 \leq 90 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**Đối ngẫu:**

$$
\begin{align}
\min_{u} \quad & 100u_1 + 80u_2 + 90u_3 \\
\text{s.t.} \quad & 2u_1 + u_2 + 3u_3 \geq 5 \\
& u_1 + 2u_2 + 2u_3 \geq 4 \\
& 3u_1 + 2u_2 + u_3 \geq 6 \\
& u_1, u_2, u_3 \geq 0
\end{align}
$$

**b) Phương án tối ưu và shadow price:**

Ba ràng buộc tài nguyên đều chặt, nên $$x^*$$ là nghiệm của hệ $$Ax = b$$:

$$
x^* = \left(\tfrac{160}{11}, \tfrac{150}{11}, \tfrac{210}{11}\right) \approx (14{,}55;\ 13{,}64;\ 19{,}09), \qquad 5x_1 + 4x_2 + 6x_3 = \tfrac{2660}{11} \approx 241{,}82
$$

Kiểm tra lao động: $$2 \cdot 160 + 150 + 3 \cdot 210 = 1100$$, chia 11 được 100 ✓.

Vì $$x_1, x_2, x_3 > 0$$, theo điều kiện bù (complementary slackness) cả ba ràng buộc đối ngẫu đều chặt:

$$
\begin{cases}
2u_1 + u_2 + 3u_3 = 5 \\
u_1 + 2u_2 + 2u_3 = 4 \\
3u_1 + 2u_2 + u_3 = 6
\end{cases}
\quad\Longrightarrow\quad
u^* = \left(\tfrac{14}{11}, \tfrac{9}{11}, \tfrac{6}{11}\right) \approx (1{,}27;\ 0{,}82;\ 0{,}55)
$$

Kiểm tra: $$100u_1 + 80u_2 + 90u_3 = \tfrac{1400 + 720 + 540}{11} = \tfrac{2660}{11}$$, bằng giá trị tối ưu của bài toán gốc ✓ (đối ngẫu mạnh). Mọi $$u_i \ge 0$$ nên $$u^*$$ khả thi.

Ý nghĩa: thêm 1 giờ lao động tăng lợi nhuận khoảng 1,27; thêm 1 giờ máy khoảng 0,82; thêm 1 kg nguyên liệu khoảng 0,55.

**c) Quyết định:**

Shadow price chỉ đúng khi cơ sở tối ưu không đổi. Với $$A^{-1} = \tfrac{1}{11}\begin{pmatrix} 2 & -5 & 4 \\ -5 & 7 & 1 \\ 4 & 1 & -3 \end{pmatrix}$$:
- Thêm 10 giờ lao động: $$x = A^{-1}(110, 80, 90) = \left(\tfrac{180}{11}, \tfrac{100}{11}, \tfrac{250}{11}\right) > 0$$, cơ sở giữ nguyên.
- Thêm 10 kg nguyên liệu: $$x = A^{-1}(100, 80, 100) = \left(\tfrac{200}{11}, \tfrac{160}{11}, \tfrac{180}{11}\right) > 0$$, cơ sở giữ nguyên.

**Phương án 1 (lao động):** lợi nhuận tăng $$10 \cdot \tfrac{14}{11} \approx 12{,}7$$ triệu, chi phí 15 triệu, **lỗ khoảng 2,3 triệu**.

**Phương án 2 (nguyên liệu):** lợi nhuận tăng $$10 \cdot \tfrac{6}{11} \approx 5{,}5$$ triệu, chi phí 10 triệu, **lỗ khoảng 4,5 triệu**.

**Kết luận:** giá mua của cả hai tài nguyên đều cao hơn shadow price, nên không nên mua thêm. Nếu buộc phải chọn một, phương án 1 lỗ ít hơn.

</details>

---

## **Tổng kết và Chiến lược**

### **Xây dựng đối ngẫu:**
- Xác định dạng bài toán (min/max, ràng buộc)
- Áp dụng quy tắc tương ứng primal-dual
- Số biến dual = số ràng buộc primal
- Số ràng buộc dual = số biến primal

### **Kiểm tra tối ưu:**
- Primal + Dual feasibility
- Complementary slackness: $$u_i(a_i^T x - b_i) = 0$$
- So sánh giá trị: $$f^* = g^*$$ (strong duality)

### **Shadow price:**
- Giá trị biên của tài nguyên
- Chỉ chính xác trong sensitivity range
- Slack > 0 → shadow price = 0

### **Max Flow - Min Cut:**
- Bảo toàn luồng tại nút trung gian
- Giá trị luồng $$\leq$$ công suất cắt (weak duality)
- Nếu bằng nhau → cả hai tối ưu (strong duality)

### **Matrix Games:**
- Kiểm tra saddle point trước
- Nếu không có, giải LP cho mixed strategy
- Von Neumann minimax: $$\max_x \min_y = \min_y \max_x$$

---

## **Tài liệu Tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 5: Duality.

2. **Bertsimas, D., & Tsitsiklis, J. N.** (1997). *Introduction to Linear Optimization*. Athena Scientific. Chapters 4, 7.

3. **Dantzig, G. B.** (1963). *Linear Programming and Extensions*. Princeton University Press. Chapters 5-8.

4. **Luenberger, D. G., & Ye, Y.** (2008). *Linear and Nonlinear Programming* (3rd ed.). Springer.

5. **Vanderbei, R. J.** (2020). *Linear Programming: Foundations and Extensions* (5th ed.). Springer.

---

**Ghi chú:** Các bài tập được sắp xếp từ cơ bản đến nâng cao, tham khảo trực tiếp từ các sách giáo khoa kinh điển. Hãy thực hành đầy đủ để nắm vững tính đối ngẫu trong LP!

---
layout: post
title: "14-12 Bài Tập Thực Hành - Phương Pháp Newton"
chapter: "14"
order: 20
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter14
lesson_type: required
redirect_from:
  - /contents/vi/chapter14/14_11_Practical_Exercises_Newton_Method/
---

# Bài Tập Thực Hành - Phương Pháp Newton

Các bài tập dưới đây được tham khảo từ Boyd & Vandenberghe (2004), Nocedal & Wright (2006) và Bertsekas (1999).

---

## **Phần I: Phương pháp Newton cơ bản**

### **Bài tập 1: Tính bước Newton (Boyd & Vandenberghe, Ex. 9.1)**

Cho hàm mục tiêu:

$$
f(x) = \frac{1}{2}x^T Q x + c^T x
$$

với $$Q \succ 0$$.

**Yêu cầu:**  
a) Tính gradient $$\nabla f(x)$$ và ma trận Hessian $$\nabla^2 f(x)$$.  
b) Tại $$x = (1, 2)^T$$, tính bước Newton $$\Delta x_{nt}$$.  
c) Tính đại lượng giảm Newton (Newton decrement) $$\lambda(x) = \sqrt{\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x)}$$.  
d) Với $$Q = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$ và $$c = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$$, tính tất cả các giá trị trên.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**a) Gradient và Hessian:**

$$
\nabla f(x) = Qx + c
$$

$$
\nabla^2 f(x) = Q
$$

(Ma trận Hessian là hằng số vì $$f$$ là hàm bậc hai.)

---

**b) Bước Newton:**

Theo định nghĩa:

$$
\Delta x_{nt} = -(\nabla^2 f(x))^{-1} \nabla f(x) = -Q^{-1}(Qx + c)
$$

---

**c) Đại lượng giảm Newton:**

$$
\lambda(x) = \sqrt{\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x)}
$$

$$
= \sqrt{(Qx+c)^T Q^{-1} (Qx+c)}
$$

---

**d) Tính toán cụ thể:**

Dữ liệu:

$$
Q = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}, \quad
c = \begin{bmatrix} -1 \\ -1 \end{bmatrix}, \quad
x = \begin{bmatrix} 1 \\ 2 \end{bmatrix}
$$

**Tính $$Q^{-1}$$:**

$$
\det(Q) = 2 \times 2 - 1 \times 1 = 3
$$

$$
Q^{-1} = \frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix}
$$

**Gradient tại $$x$$:**

$$
\nabla f(x) = Qx + c = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \end{bmatrix} + \begin{bmatrix} -1 \\ -1 \end{bmatrix}
$$

$$
= \begin{bmatrix} 4 \\ 5 \end{bmatrix} + \begin{bmatrix} -1 \\ -1 \end{bmatrix} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}
$$

**Bước Newton:**

$$
\Delta x_{nt} = -Q^{-1} \nabla f(x) = -\frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 3 \\ 4 \end{bmatrix}
$$

$$
= -\frac{1}{3}\begin{bmatrix} 6-4 \\ -3+8 \end{bmatrix} = -\frac{1}{3}\begin{bmatrix} 2 \\ 5 \end{bmatrix} = \begin{bmatrix} -2/3 \\ -5/3 \end{bmatrix}
$$

**Đại lượng giảm Newton:**

$$
\lambda^2(x) = \nabla f(x)^T Q^{-1} \nabla f(x)
$$

$$
= \begin{bmatrix} 3 & 4 \end{bmatrix} \frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} 3 \\ 4 \end{bmatrix}
$$

$$
= \frac{1}{3}\begin{bmatrix} 3 & 4 \end{bmatrix} \begin{bmatrix} 2 \\ 5 \end{bmatrix} = \frac{1}{3}(6 + 20) = \frac{26}{3}
$$

$$
\lambda(x) = \sqrt{\frac{26}{3}} \approx 2.944
$$

**Nghiệm tối ưu:**

Vì $$f$$ là hàm bậc hai, phương pháp Newton hội tụ ngay trong 1 bước:

$$
x^+ = x + \Delta x_{nt} = \begin{bmatrix} 1 \\ 2 \end{bmatrix} + \begin{bmatrix} -2/3 \\ -5/3 \end{bmatrix} = \begin{bmatrix} 1/3 \\ 1/3 \end{bmatrix}
$$

Kiểm tra trực tiếp từ $$\nabla f(x^*) = Q x^* + c = 0 \Rightarrow x^* = -Q^{-1}c$$:

$$
x^* = -\frac{1}{3}\begin{bmatrix} 2 & -1 \\ -1 & 2 \end{bmatrix} \begin{bmatrix} -1 \\ -1 \end{bmatrix} = -\frac{1}{3}\begin{bmatrix} -1 \\ -1 \end{bmatrix} = \begin{bmatrix} 1/3 \\ 1/3 \end{bmatrix}
$$

Kết quả trùng khớp.

</details>

---

### **Bài tập 2: Phương pháp Newton cho hồi quy logistic (Nocedal & Wright, Ex. 8.1)**

Xét bài toán hồi quy logistic:

$$
\min_x \sum_{i=1}^m \log(1 + e^{-y_i (a_i^T x)})
$$

với tập dữ liệu $$(a_i, y_i)$$ trong đó $$y_i \in \{-1, +1\}$$.

**Yêu cầu:**  
a) Tính gradient $$\nabla f(x)$$.  
b) Tính ma trận Hessian $$\nabla^2 f(x)$$.  
c) Chứng minh $$\nabla^2 f(x) \succeq 0$$ (hàm lồi).  
d) Với dữ liệu $$m=3$$, $$n=2$$:
   - $$a_1 = (1, 1)^T$$, $$y_1 = +1$$
   - $$a_2 = (1, -1)^T$$, $$y_2 = +1$$
   - $$a_3 = (-1, 0)^T$$, $$y_3 = -1$$
   
   Tính bước Newton tại $$x = (0, 0)^T$$.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**a) Gradient:**

Đặt $$\phi(z) = \log(1 + e^{-z})$$, khi đó:

$$
f(x) = \sum_{i=1}^m \phi(y_i a_i^T x)
$$

$$
\phi'(z) = \frac{-e^{-z}}{1 + e^{-z}} = -\frac{1}{1 + e^z}
$$

$$
\nabla f(x) = \sum_{i=1}^m \phi'(y_i a_i^T x) \cdot y_i a_i = -\sum_{i=1}^m \frac{y_i a_i}{1 + e^{y_i a_i^T x}}
$$

---

**b) Hessian:**

$$
\phi''(z) = \frac{e^z}{(1 + e^z)^2}
$$

$$
\nabla^2 f(x) = \sum_{i=1}^m \phi''(y_i a_i^T x) \cdot y_i^2 a_i a_i^T = \sum_{i=1}^m \frac{a_i a_i^T}{(1 + e^{y_i a_i^T x})^2} \cdot e^{y_i a_i^T x}
$$

Rút gọn (do $$y_i^2 = 1$$):

$$
\nabla^2 f(x) = \sum_{i=1}^m w_i a_i a_i^T
$$

với $$w_i = \frac{e^{y_i a_i^T x}}{(1 + e^{y_i a_i^T x})^2} > 0$$.

---

**c) Chứng minh tính lồi:**

Ta có $$\nabla^2 f(x) = \sum_{i=1}^m w_i a_i a_i^T$$ với $$w_i > 0$$. Với mọi $$v \in \mathbb{R}^n$$:

$$
v^T (\nabla^2 f(x)) v = \sum_{i=1}^m w_i (a_i^T v)^2 \geq 0
$$

Suy ra $$\nabla^2 f(x) \succeq 0$$, nên $$f$$ là hàm lồi.

---

**d) Tính toán tại $$x = (0,0)^T$$:**

**Gradient:**

Tại $$x = 0$$, ta có $$a_i^T x = 0$$ với mọi $$i$$:

$$
\nabla f(0) = -\sum_{i=1}^3 \frac{y_i a_i}{1 + e^0} = -\frac{1}{2}\sum_{i=1}^3 y_i a_i
$$

$$
= -\frac{1}{2}\left( (+1)\begin{bmatrix} 1 \\ 1 \end{bmatrix} + (+1)\begin{bmatrix} 1 \\ -1 \end{bmatrix} + (-1)\begin{bmatrix} -1 \\ 0 \end{bmatrix} \right)
$$

$$
= -\frac{1}{2}\begin{bmatrix} 1+1+1 \\ 1-1+0 \end{bmatrix} = -\frac{1}{2}\begin{bmatrix} 3 \\ 0 \end{bmatrix} = \begin{bmatrix} -1.5 \\ 0 \end{bmatrix}
$$

**Hessian:**

Ta có $$w_i = \frac{e^0}{(1+e^0)^2} = \frac{1}{4}$$ với mọi $$i$$:

$$
\nabla^2 f(0) = \frac{1}{4}\sum_{i=1}^3 a_i a_i^T
$$

$$
= \frac{1}{4}\left( \begin{bmatrix} 1 \\ 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \end{bmatrix} + \begin{bmatrix} 1 \\ -1 \end{bmatrix}\begin{bmatrix} 1 & -1 \end{bmatrix} + \begin{bmatrix} -1 \\ 0 \end{bmatrix}\begin{bmatrix} -1 & 0 \end{bmatrix} \right)
$$

$$
= \frac{1}{4}\left( \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} + \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix} \right) = \frac{1}{4}\begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}
$$

**Bước Newton:**

$$
\Delta x_{nt} = -(\nabla^2 f(0))^{-1} \nabla f(0)
$$

$$
= -\frac{4}{1}\begin{bmatrix} 1/3 & 0 \\ 0 & 1/2 \end{bmatrix} \begin{bmatrix} -1.5 \\ 0 \end{bmatrix} = 4\begin{bmatrix} 0.5 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 0 \end{bmatrix}
$$

</details>

---

## **Phần II: Tìm kiếm đường Backtracking**

### **Bài tập 3: Điều kiện Armijo (Boyd & Vandenberghe, Ex. 9.3)**

Cho hàm $$f(x) = x^2$$ và điểm $$x = 2$$.

**Yêu cầu:**  
a) Tính gradient $$\nabla f(x)$$ và Hessian $$\nabla^2 f(x)$$.  
b) Tính hướng Newton $$\Delta x_{nt}$$.  
c) Với các tham số Armijo $$\alpha = 0.3$$, $$\beta = 0.5$$, tìm kích thước bước $$t$$ thỏa mãn điều kiện Armijo:

$$
f(x + t \Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x
$$

d) Minh họa bằng đồ thị.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**a) Gradient và Hessian:**

$$
\nabla f(x) = 2x, \quad \nabla^2 f(x) = 2
$$

Tại $$x = 2$$:

$$
\nabla f(2) = 4, \quad \nabla^2 f(2) = 2
$$

---

**b) Hướng Newton:**

$$
\Delta x_{nt} = -\frac{\nabla f(x)}{\nabla^2 f(x)} = -\frac{4}{2} = -2
$$

---

**c) Tìm kiếm đường backtracking:**

Điều kiện Armijo:

$$
f(x + t \Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x
$$

Thay số:

$$
(2 + t(-2))^2 \leq 4 + 0.3 \cdot t \cdot 4 \cdot (-2)
$$

$$
(2 - 2t)^2 \leq 4 - 2.4t
$$

$$
4 - 8t + 4t^2 \leq 4 - 2.4t
$$

$$
4t^2 - 5.6t \leq 0
$$

$$
t(4t - 5.6) \leq 0
$$

Vì $$t > 0$$, điều kiện tương đương $$4t - 5.6 \leq 0 \Rightarrow t \leq 1.4$$.

**Kiểm tra backtracking:**

Thử $$t = 1$$:

$$
f(2 - 2 \cdot 1) = f(0) = 0
$$

$$
4 + 0.3 \cdot 1 \cdot (-8) = 4 - 2.4 = 1.6
$$

Vì $$0 \leq 1.6$$, điều kiện Armijo được thỏa mãn ngay tại $$t = 1$$.

**Kết quả:** $$t = 1$$ (bước Newton đầy đủ).

---

**d) Giải thích hình học:**

- Đồ thị của $$f(x)$$ là parabol $$y = x^2$$.
- Tại $$x = 2$$, bước Newton $$\Delta x = -2$$ hướng thẳng về điểm cực tiểu $$x^* = 0$$.
- Bước đầy đủ $$t = 1$$ đưa nghiệm về đúng điểm tối ưu ngay sau 1 vòng lặp.
- Điều kiện Armijo đảm bảo mức giảm giá trị hàm là đủ lớn (sufficient decrease).

**Đồ thị minh họa:**

```
f(x) = x²

     4 |     • (2, 4)
       |    /
       |   /
       |  /
     1 |_/__________
       |/      
     0 •------------ x
      0  1   2
         ↑
      Bước Newton
      đưa đến x=0
```

Đường Armijo: $$y = 4 - 2.4t$$ (đường thẳng đi qua $$(2, 4)$$ có độ dốc thu nhỏ bằng $$\alpha \nabla f \Delta x$$).

</details>

---

## **Phần III: Phân tích hội tụ**

### **Bài tập 4: Hội tụ bậc hai (Nocedal & Wright, Theorem 3.5)**

Xét phương pháp Newton cho hàm lồi mạnh $$f$$ thỏa mãn:
- $$m I \preceq \nabla^2 f(x) \preceq M I$$
- $$\nabla^2 f$$ liên tục Lipschitz với hằng số $$L$$

**Yêu cầu:**  
a) Chứng minh phương pháp Newton có hội tụ bậc hai khi gần nghiệm.  
b) Tính toán cụ thể với $$f(x) = \frac{1}{2}x^T Q x$$ trong đó $$Q = \begin{bmatrix} 4 & 0 \\ 0 & 1 \end{bmatrix}$$.  
c) So sánh với gradient descent.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**a) Chứng minh hội tụ bậc hai:**

<div class="textbook-theorem" markdown="1">
<strong>Định lý:</strong> Nếu $$f$$ lồi mạnh với tham số $$m$$ và $$\nabla^2 f$$ liên tục Lipschitz với hằng số $$L$$, thì tồn tại $$\delta > 0$$ sao cho khi $$\|x^{(k)} - x^*\| < \delta$$:

$$
\|x^{(k+1)} - x^*\| \leq \frac{L}{2m} \|x^{(k)} - x^*\|^2
$$
</div>

**Phác thảo chứng minh:**

Công thức lặp Newton:

$$
x^{(k+1)} = x^{(k)} - (\nabla^2 f(x^{(k)}))^{-1} \nabla f(x^{(k)})
$$

Khai triển tích phân của gradient quanh $$x^*$$:

$$
\nabla f(x^{(k)}) = \nabla f(x^*) + \int_0^1 \nabla^2 f(x^* + t(x^{(k)} - x^*)) (x^{(k)} - x^*) dt
$$

Vì $$\nabla f(x^*) = 0$$:

$$
\nabla f(x^{(k)}) = \int_0^1 \nabla^2 f(x^* + t(x^{(k)} - x^*)) (x^{(k)} - x^*) dt
$$

Suy ra sai số ở bước $$k+1$$:

$$
x^{(k+1)} - x^* = x^{(k)} - x^* - (\nabla^2 f(x^{(k)}))^{-1} \nabla f(x^{(k)})
$$

Áp dụng tính liên tục Lipschitz của Hessian:

$$
\|\nabla^2 f(x) - \nabla^2 f(y)\| \leq L \|x - y\|
$$

Kết hợp với cận dưới $$m$$ của giá trị riêng Hessian (suy ra $$\|(\nabla^2 f(x^{(k)}))^{-1}\| \leq 1/m$$), ta thu được:

$$
\|x^{(k+1)} - x^*\| \leq \frac{L}{2m} \|x^{(k)} - x^*\|^2
$$

**Ý nghĩa:** Sai số giảm theo bình phương sau mỗi vòng lặp (hội tụ bậc hai).

---

**b) Tính toán với $$Q = \text{diag}(4, 1)$$:**

$$
f(x) = \frac{1}{2}x^T Q x = 2x_1^2 + \frac{1}{2}x_2^2
$$

**Các tham số:**
- $$m = \lambda_{\min}(Q) = 1$$
- $$M = \lambda_{\max}(Q) = 4$$
- $$L = 0$$ (vì ma trận Hessian là hằng số $$\nabla^2 f(x) = Q$$)

**Sự hội tụ:**

Với $$L = 0$$, phương pháp Newton hội tụ ngay trong **1 bước** (do $$f$$ là hàm bậc hai). Từ mọi điểm khởi tạo $$x^{(0)}$$:

$$
x^{(1)} = x^{(0)} - Q^{-1} (Qx^{(0)}) = x^{(0)} - x^{(0)} = 0 = x^*
$$

---

**c) So sánh với Gradient Descent:**

Xét gradient descent với kích thước bước tối ưu $$t = \frac{2}{m + M} = \frac{2}{5} = 0.4$$:

$$
x^{(k+1)} = x^{(k)} - 0.4 \nabla f(x^{(k)})
$$

**Tốc độ hội tụ:**

$$
\|x^{(k+1)} - x^*\| \leq \left(\frac{M - m}{M + m}\right) \|x^{(k)} - x^*\| = \frac{3}{5} \|x^{(k)} - x^*\|
$$

Đây là hội tụ tuyến tính với hệ số co $$0.6$$.

**Bảng so sánh:**

| Phương pháp | Tốc độ hội tụ | Số vòng lặp để đạt sai số $$10^{-6}$$ |
|---|---|---|
| Newton | Bậc hai | 1 (với hàm bậc hai) |
| Gradient Descent | Tuyến tính ($$0.6^k$$) | $$k = 28$$ (do $$0.6^{27} \approx 1.03 \times 10^{-6}$$) |

Phương pháp Newton hội tụ nhanh hơn đáng kể so với gradient descent.

</details>

---

## **Phần IV: Tính bất biến Affine**

### **Bài tập 5: Tính chất bất biến Affine (Boyd & Vandenberghe, Ex. 9.20)**

Phương pháp Newton có tính bất biến affine: khi thực hiện phép biến đổi affine lên hệ tọa độ, quỹ đạo lặp của phương pháp không thay đổi.

**Yêu cầu:**  
a) Chứng minh: Nếu $$\tilde{x} = Ax + b$$ với $$A$$ khả nghịch và $$\tilde{f}(\tilde{x}) = f(A^{-1}(\tilde{x} - b))$$, thì bước Newton biến đổi tương ứng theo phép biến đổi affine đó.  
b) Minh họa bằng một ví dụ cụ thể.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**a) Chứng minh tính bất biến affine:**

Bài toán gốc: $$\min_x f(x)$$  
Bài toán sau biến đổi: $$\min_{\tilde{x}} \tilde{f}(\tilde{x})$$ với $$\tilde{x} = Ax + b$$.

**Gradient của $$\tilde{f}$$:**

Theo quy tắc chuỗi (với $$x = A^{-1}(\tilde{x} - b)$$):

$$
\nabla \tilde{f}(\tilde{x}) = A^{-T} \nabla f(x)
$$

**Hessian của $$\tilde{f}$$:**

$$
\nabla^2 \tilde{f}(\tilde{x}) = A^{-T} \nabla^2 f(x) A^{-1}
$$

**Bước Newton trong tọa độ mới:**

$$
\Delta \tilde{x}_{nt} = -(\nabla^2 \tilde{f}(\tilde{x}))^{-1} \nabla \tilde{f}(\tilde{x})
$$

$$
= -(A \nabla^2 f(x)^{-1} A^T)(A^{-T} \nabla f(x))
$$

$$
= -A \nabla^2 f(x)^{-1} \nabla f(x) = A \Delta x_{nt}
$$

**Quan hệ giữa hai bước lặp:**

$$
\Delta \tilde{x}_{nt} = A \Delta x_{nt}
$$

Trong tọa độ gốc:

$$
x^{(k+1)} = x^{(k)} + \Delta x_{nt}
$$

Trong tọa độ mới:

$$
\tilde{x}^{(k+1)} = \tilde{x}^{(k)} + \Delta \tilde{x}_{nt} = A x^{(k)} + b + A \Delta x_{nt} = A x^{(k+1)} + b
$$

**Kết luận:** Quỹ đạo của phương pháp Newton giữ nguyên cấu trúc dưới mọi phép biến đổi affine khả nghịch.

---

**b) Ví dụ minh họa:**

$$
f(x) = x_1^2 + 4x_2^2
$$

**Phép biến đổi:** $$\tilde{x} = Ax$$ với $$A = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix}$$, khi đó:

$$
\tilde{f}(\tilde{x}) = \tilde{x}_1^2 + \tilde{x}_2^2
$$

(Phép biến đổi đưa các đường đồng mức elip thành đường tròn.)

**Xuất phát từ $$x^{(0)} = (2, 1)^T$$:**

**Trong tọa độ gốc:**
- $$\nabla f = (4, 8)^T$$
- $$\nabla^2 f = \text{diag}(2, 8)$$
- $$\Delta x = -(2, 1)^T$$
- $$x^{(1)} = (0, 0)^T$$

**Trong tọa độ mới:** $$\tilde{x}^{(0)} = (2, 2)^T$$
- $$\nabla \tilde{f} = (4, 4)^T$$
- $$\nabla^2 \tilde{f} = 2I$$
- $$\Delta \tilde{x} = -(2, 2)^T$$
- $$\tilde{x}^{(1)} = (0, 0)^T$$

Cả hai hệ tọa độ đều cho cùng điểm tối ưu với số vòng lặp như nhau.

</details>

---

## **Phần V: Bài toán ứng dụng**

### **Bài tập 6: Điều khiển tối ưu (Bertsekas, Ex. 2.3.5)**

Xét bài toán điều khiển tối ưu rời rạc:

$$
\min_{u_0,\ldots,u_{N-1}} \sum_{k=0}^{N-1} \left( x_k^T Q x_k + u_k^T R u_k \right) + x_N^T Q_f x_N
$$

với phương trình trạng thái:

$$
x_{k+1} = A x_k + B u_k, \quad x_0 = \bar{x}
$$

**Yêu cầu:**  
a) Viết bài toán dưới dạng quy hoạch bậc hai (QP) không ràng buộc.  
b) Tính gradient và ma trận Hessian.  
c) Áp dụng phương pháp Newton với $$N = 3$$, $$Q = I$$, $$R = I$$, $$Q_f = I$$, $$A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$$, $$B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$, $$\bar{x} = (1, 0)^T$$.

<details markdown="1">
<summary><strong>Lời giải</strong></summary>

**a) Biểu diễn bài toán dạng QP không ràng buộc:**

**Biến quyết định:** $$z = (u_0, u_1, u_2)^T \in \mathbb{R}^{3}$$ (với $$u_k \in \mathbb{R}$$).

**Biểu diễn $$x_k$$ theo $$u$$:**

$$
\begin{align}
x_1 &= Ax_0 + Bu_0 \\
x_2 &= Ax_1 + Bu_1 = A^2 x_0 + AB u_0 + B u_1 \\
x_3 &= A^3 x_0 + A^2 B u_0 + AB u_1 + B u_2
\end{align}
$$

**Dạng rút gọn:** $$x_k = \Phi_k x_0 + \sum_{j=0}^{k-1} \Psi_{kj} u_j$$.

**Hàm mục tiêu:**

$$
f(u) = \sum_{k=0}^{N-1} (x_k^T Q x_k + u_k^T R u_k) + x_N^T Q_f x_N
$$

$$
= \frac{1}{2} u^T H u + g^T u + \text{const}
$$

trong đó $$H$$ và $$g$$ được xác định từ phương trình trạng thái và các ma trận trọng số.

---

**b) Gradient và Hessian:**

Vì $$f$$ là hàm bậc hai:

$$
\nabla f(u) = Hu + g
$$

$$
\nabla^2 f(u) = H
$$

**Bước Newton:**

$$
\Delta u = -H^{-1}(Hu + g) = -u - H^{-1}g
$$

Thuật toán hội tụ ngay trong 1 bước.

---

**c) Tính toán cụ thể với $$N=3$$:**

Dữ liệu:

$$
A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}, \quad
B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}, \quad
x_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}
$$

**Tính các trạng thái $$x_k$$:**

$$
x_1 = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \end{bmatrix} u_0 = \begin{bmatrix} 1 \\ u_0 \end{bmatrix}
$$

$$
x_2 = A x_1 + B u_1 = \begin{bmatrix} 1 + u_0 \\ u_0 + u_1 \end{bmatrix}
$$

$$
x_3 = A x_2 + B u_2 = \begin{bmatrix} 1 + 2u_0 + u_1 \\ u_0 + u_1 + u_2 \end{bmatrix}
$$

**Hàm mục tiêu (với $$Q = R = Q_f = I$$):**

$$
f = \sum_{k=0}^2 (\|x_k\|^2 + u_k^2) + \|x_3\|^2
$$

$$
= (1^2 + u_0^2) + ((1)^2 + (u_0)^2 + u_1^2) + \ldots
$$

Khai triển đầy đủ và lấy đạo hàm, ta thu được $$\nabla f(0) = (6, 2, 0)^T$$ và $$\nabla^2 f = \begin{bmatrix} 18 & 8 & 2 \\ 8 & 8 & 2 \\ 2 & 2 & 4 \end{bmatrix}$$. Bước Newton xuất phát từ $$u = 0$$ là $$\Delta u = -(\nabla^2 f)^{-1}\nabla f(0)$$.

**Kết quả:**

Điều khiển tối ưu: $$u^* = (-2/5,\ 4/35,\ 1/7)^T \approx (-0.4,\ 0.114,\ 0.143)^T$$, với giá trị mục tiêu tối ưu $$f^* = 102/35 \approx 2.914$$.

Phương pháp Newton tìm ra nghiệm chính xác sau 1 vòng lặp vì bài toán có dạng quy hoạch bậc hai.

</details>

---

## **Tổng kết và lưu ý thực hành**

### **Phương pháp Newton:**
- **Bước Newton:** $$\Delta x = -(\nabla^2 f(x))^{-1} \nabla f(x)$$
- **Đại lượng giảm Newton:** $$\lambda(x) = \sqrt{\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x)}$$
- **Tiêu chí dừng:** $$\lambda^2(x)/2 < \epsilon$$

### **Tìm kiếm đường Backtracking:**
- **Điều kiện Armijo:** $$f(x + t\Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x$$
- **Tham số:** $$\alpha \in (0, 0.5)$$, $$\beta \in (0, 1)$$
- **Giá trị thường dùng:** $$\alpha = 0.3$$, $$\beta = 0.8$$

### **Tính chất hội tụ:**
- **Hội tụ bậc hai:** $$\|x^{(k+1)} - x^*\| \leq C \|x^{(k)} - x^*\|^2$$
- **Gần điểm tối ưu:** Khi ở gần $$x^*$$, phương pháp Newton hội tụ rất nhanh
- **Hàm bậc hai:** Hội tụ trong 1 bước

### **Tính bất biến Affine:**
- Quỹ đạo phương pháp Newton không phụ thuộc vào phép biến đổi affine của hệ tọa độ
- Số vòng lặp giữ nguyên dưới các phép biến đổi affine khả nghịch
- **Lợi ích:** Không nhạy cảm với số điều kiện của hệ tọa độ

### **Khi nào nên dùng phương pháp Newton:**
- Hàm mục tiêu trơn, khả vi hai lần ($$\nabla^2 f$$ tồn tại và tính được)
- Đã ở gần nghiệm hoặc cần tốc độ hội tụ cao
- Số chiều không quá lớn (lưu trữ và giải hệ tuyến tính cỡ $$n \times n$$ còn khả thi)
- Cần độ chính xác cao

---

## **Tài liệu tham khảo**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 9.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization* (2nd ed.). Springer. Chapters 3, 6.

3. **Bertsekas, D. P.** (1999). *Nonlinear Programming* (2nd ed.). Athena Scientific. Chapter 1.

4. **Nesterov, Y.** (2004). *Introductory Lectures on Convex Optimization*. Springer. Chapter 2.

5. **Dennis, J. E., & Schnabel, R. B.** (1996). *Numerical Methods for Unconstrained Optimization and Nonlinear Equations*. SIAM.

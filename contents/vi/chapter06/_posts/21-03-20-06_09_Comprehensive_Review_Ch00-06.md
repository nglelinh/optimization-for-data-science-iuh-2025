---
layout: post
title: 06-09 Ôn tập tổng hợp - Nền tảng Tối ưu hóa Lồi (Chương 00-06)
chapter: '06'
order: 17
owner: GitHub Copilot
lang: vi
categories:
- chapter06
lesson_type: review
---

<script>
window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]'], ['$$', '$$']],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};
</script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# 📚 Ôn tập tổng hợp: Nền tảng Tối ưu hóa Lồi

Đây là bài ôn tập tổng hợp các khái niệm cốt lõi từ chương 00 đến chương 06, được sắp xếp theo logic xây dựng kiến thức từ nền tảng toán học đến các thuật toán thực tế.

---

## 🏗️ **PHẦN I: NỀN TẢNG TOÁN HỌC (Chương 00)**

### 🔢 **1. Giải tích cơ bản**

#### **Đạo hàm và Gradient**
- **Đạo hàm:** $$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$
- **Đạo hàm riêng:** $$\frac{\partial f}{\partial x_i}$$ - đạo hàm theo $$x_i$$ khi các biến khác cố định
- **Gradient:** $$\nabla f = \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix}$$ - vector chỉ hướng tăng dốc nhất

#### **Đạo hàm có hướng và Chuỗi Taylor**
- **Đạo hàm có hướng:** $$D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u} = \|\nabla f\| \cos \theta$$
- **Chuỗi Taylor bậc 1:** $$f(\mathbf{x}) \approx f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T (\mathbf{x} - \mathbf{x}_0)$$
- **Chuỗi Taylor bậc 2:** $$f(\mathbf{x}) \approx f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T (\mathbf{x} - \mathbf{x}_0) + \frac{1}{2} (\mathbf{x} - \mathbf{x}_0)^T \nabla^2 f(\mathbf{x}_0) (\mathbf{x} - \mathbf{x}_0)$$

### 📐 **2. Đại số tuyến tính**

#### **Vector và Phép toán**
- **Tích vô hướng:** $$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos \theta$$
- **Chuẩn vector:**
  - L2 (Euclid): $$\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2}$$
  - L1 (Manhattan): $$\|\mathbf{x}\|_1 = \sum_{i=1}^n \lvert x_i \rvert$$
  - L∞ (Max): $$\|\mathbf{x}\|_\infty = \max_i \lvert x_i \rvert$$

#### **Ma trận và Eigenvalue**
- **Phép nhân ma trận:** $$(AB)_{ij} = \sum_{k} A_{ik} B_{kj}$$
- **Eigenvalue/eigenvector:** $$A\mathbf{v} = \lambda \mathbf{v}$$ với $$\mathbf{v} \neq \mathbf{0}$$
- **Ma trận xác định dương:** $$A \succ 0 \Leftrightarrow \mathbf{x}^T A \mathbf{x} > 0, \forall \mathbf{x} \neq 0$$

### 📊 **3. Lý thuyết tập hợp**

#### **Tập hợp cơ bản**
- **Tập mở:** Mọi điểm đều có lân cận nằm trong tập
- **Tập đóng:** Chứa tất cả điểm biên
- **Tập compact:** Đóng và bị chặn trong $$\mathbb{R}^n$$

#### **Tính liên tục**
- **Liên tục:** $$\lim_{x \to x_0} f(x) = f(x_0)$$
- **Liên tục đều:** $$\forall \epsilon > 0, \exists \delta > 0$$ sao cho $$\lvert x-y \rvert < \delta \Rightarrow \lvert f(x)-f(y) \rvert < \epsilon$$

---

## 🎯 **PHẦN II: KHÁI NIỆM TỐI ƯU HÓA (Chương 01)**

### 🔍 **4. Bài toán tối ưu hóa tổng quát**

#### **Dạng chuẩn**
$$\begin{align} 
&\min_{x\in D}\ &&f(x) \\
&\text{với điều kiện} && g_i(x) \le 0,\ i = 1, ..., m \\
&&& h_j(x) = 0,\ j = 1,\ ..., r
\end{align}$$

**Các thành phần:**
- $$x \in \mathbb{R}^n$$: biến tối ưu hóa
- $$f(x)$$: hàm mục tiêu
- $$g_i(x) \le 0$$: ràng buộc bất đẳng thức
- $$h_j(x) = 0$$: ràng buộc đẳng thức
- $$x^*$$: nghiệm tối ưu

### 🌟 **5. Tối ưu hóa lồi - Tính chất vàng**

#### **Định nghĩa bài toán lồi**
Bài toán tối ưu hóa là lồi khi:
- Hàm mục tiêu $$f$$ là lồi
- Các hàm ràng buộc bất đẳng thức $$g_i$$ là lồi
- Các hàm ràng buộc đẳng thức $$h_j$$ là affine

#### **Tính chất quan trọng**
> **Mọi cực tiểu địa phương của bài toán tối ưu hóa lồi đều là cực tiểu toàn cục**

Điều này làm cho tối ưu hóa lồi trở nên đáng tin cậy và hiệu quả!

---

## 🔵 **PHẦN III: TẬP LỒI (Chương 02)**

### 📏 **6. Từ Affine đến Lồi**

#### **Tập Affine**
- **Định nghĩa:** $$\theta x_1 + (1-\theta)x_2 \in C$$ với mọi $$\theta \in \mathbb{R}$$
- **Tổ hợp affine:** $$\sum_{i=1}^k \theta_i x_i$$ với $$\sum_{i=1}^k \theta_i = 1$$
- **Ý nghĩa:** Đường thẳng qua hai điểm

#### **Tập Lồi**
- **Định nghĩa:** $$\theta x_1 + (1-\theta)x_2 \in C$$ với mọi $$0 \le \theta \le 1$$
- **Tổ hợp lồi:** $$\sum_{i=1}^k \theta_i x_i$$ với $$\sum_{i=1}^k \theta_i = 1, \theta_i \ge 0$$
- **Ý nghĩa:** Đoạn thẳng nối hai điểm

#### **Hình Nón Lồi**
- **Định nghĩa:** Vừa là nón vừa là lồi
- **Tổ hợp nón:** $$\sum_{i=1}^k \theta_i x_i$$ với $$\theta_i \ge 0$$
- **Ý nghĩa:** Tia từ gốc qua điểm

### 🏗️ **7. Các tập lồi quan trọng**

#### **Tập hợp cơ bản**
- **Siêu phẳng:** $$\{x \mid a^T x = b\}$$ - affine và lồi
- **Nửa không gian:** $$\{x \mid a^T x \le b\}$$ - lồi
- **Hình cầu Euclidean:** $$\{x \mid \lVert x - x_c \rVert_2 \le r\}$$ - lồi
- **Ellipsoid:** $$\{x \mid (x-x_c)^T P^{-1} (x-x_c) \le 1\}$$ với $$P \succ 0$$ - lồi

#### **Phép toán bảo toàn tính lồi**
- **Giao:** Giao của các tập lồi là lồi
- **Tổ hợp affine:** $$\alpha C + \beta D$$ lồi nếu $$C, D$$ lồi
- **Ảnh affine:** $$f(C) = \{Ax + b \mid x \in C\}$$ lồi nếu $$C$$ lồi

---

## 📈 **PHẦN IV: HÀM LỒI (Chương 03)**

### 🔍 **8. Định nghĩa và đặc trưng**

#### **Hàm lồi**
$$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$$
với mọi $$x, y \in \text{dom}(f), 0 \le \theta \le 1$$

#### **Các loại hàm lồi**
- **Lồi chặt:** Bất đẳng thức nghiêm ngặt với $$x \neq y, 0 < \theta < 1$$
- **Lồi mạnh:** $$f - \frac{m}{2}\lVert x \rVert_2^2$$ lồi với $$m > 0$$
- **Hàm lõm:** $$f$$ lõm ⟺ $$-f$$ lồi

### 🎯 **9. Đặc trưng hàm lồi**

#### **Đặc trưng epigraph**
$$f$$ lồi ⟺ $$\text{epi}(f) = \{(x,t) \mid f(x) \le t\}$$ là tập lồi

#### **Đặc trưng bậc nhất (hàm khả vi)**
$$f$$ lồi ⟺ $$f(y) \ge f(x) + \nabla f(x)^T (y-x)$$ với mọi $$x,y$$

#### **Đặc trưng bậc hai (hàm khả vi hai lần)**
$$f$$ lồi ⟺ $$\nabla^2 f(x) \succeq 0$$ với mọi $$x$$

### ⭐ **10. Hàm liên hợp**

#### **Định nghĩa**
$$f^*(y) = \sup_{x \in \text{dom}(f)} \{y^T x - f(x)\}$$

#### **Tính chất quan trọng**
- $$f^*$$ luôn lồi (dù $$f$$ có lồi hay không)
- **Bất đẳng thức Fenchel:** $$f(x) + f^*(y) \ge x^T y$$
- **Fenchel biconjugate:** Nếu $$f$$ đóng và lồi: $$f^{**} = f$$

---

## 🏆 **PHẦN V: CƠ BẢN TỐI ƯU HÓA LỒI (Chương 04)**

### ✅ **11. Điều kiện tối ưu**

#### **Điều kiện bậc nhất (không ràng buộc)**
$$\nabla f(x^*) = 0$$

#### **Điều kiện bậc nhất (có ràng buộc)**
Với bài toán $$\min_x f(x)$$ s.t. $$x \in C$$:
$$\nabla f(x^*)^T (y - x^*) \ge 0 \quad \forall y \in C$$

#### **Điều kiện bậc hai**
- **Điều kiện cần:** $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succeq 0$$
- **Điều kiện đủ:** $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succ 0$$

### 🔄 **12. Kỹ thuật biến đổi bài toán**

#### **Biến phụ (Slack Variables)**
$$g_i(x) \le 0 \quad \Rightarrow \quad g_i(x) + s_i = 0, \quad s_i \ge 0$$

#### **Làm giản (Relaxation)**
Thay thế tập khả thi $$C$$ bằng siêu tập $$\tilde{C} \supseteq C$$

#### **Loại bỏ ràng buộc đẳng thức**
Nếu $$Ax = b$$ có nghiệm: $$x = x_0 + Fz$$ với $$Ax_0 = b$$ và $$AF = 0$$

---

## 📊 **PHẦN VI: CÁC BÀI TOÁN KINH ĐIỂN (Chương 05)**

### 🎯 **13. Phân cấp bài toán tối ưu**

```
LP ⊆ QP ⊆ QCQP ⊆ SDP
    ⊆ SOCP ⊆
```

#### **Linear Programming (LP)**
$$\begin{align}
&\min_{x} &&c^T x \\
&\text{s.t.} &&Ax = b \\
&&&x \succeq 0
\end{align}$$

**Đặc điểm:**
- Hàm mục tiêu và ràng buộc đều affine
- Nghiệm tối ưu tại đỉnh của đa diện
- Giải bằng thuật toán Simplex

#### **Quadratic Programming (QP)**
$$\begin{align}
&\min_{x} &&\frac{1}{2}x^T P x + q^T x \\
&\text{s.t.} &&Gx \preceq h \\
&&&Ax = b
\end{align}$$

**Điều kiện lồi:** $$P \succeq 0$$

### 🎯 **14. Bình phương tối thiểu**

#### **Bài toán cơ bản**
$$\min_{x} \lVert Ax - b \rVert_2^2$$

#### **Nghiệm dạng đóng (Normal Equation)**
$$x^* = (A^T A)^{-1} A^T b$$

#### **Hồi quy tuyến tính**
- **Một biến:** $$m = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$$, $$c = \bar{y} - m\bar{x}$$
- **Nhiều biến:** $$\beta^* = (X^T X)^{-1} X^T y$$

---

## ⚡ **PHẦN VII: GRADIENT DESCENT (Chương 06)**

### 🎯 **15. Thuật toán cơ bản**

#### **Quy tắc cập nhật**
$$x^{(k)} = x^{(k-1)} - t \nabla f(x^{(k-1)})$$

#### **Giải thích**
- Gradient $$\nabla f(x)$$ chỉ hướng tăng dốc nhất
- Gradient âm $$-\nabla f(x)$$ chỉ hướng giảm dốc nhất
- Tại cực tiểu: $$\nabla f(x^*) = 0$$

### 📏 **16. Lựa chọn kích thước bước**

#### **Kích thước bước cố định**
$$t = \text{const} > 0$$

#### **Backtracking line search**
**Điều kiện Armijo:** $$f(x + t\Delta x) \le f(x) + \alpha t \nabla f(x)^T \Delta x$$

#### **Exact line search**
$$t^* = \arg\min_{t > 0} f(x + t\Delta x)$$

### 📊 **17. Phân tích hội tụ**

#### **Điều kiện Lipschitz**
$$\lVert \nabla f(x) - \nabla f(y) \rVert_2 \le L \lVert x - y \rVert_2$$

#### **Hội tụ cho hàm lồi**
$$f(x^{(k)}) - f^* \le \frac{\lVert x^{(0)} - x^* \rVert_2^2}{2tk}$$
**Tốc độ:** $$O(1/k)$$ - sublinear

#### **Hội tụ cho hàm lồi mạnh**
$$f(x^{(k)}) - f^* \le \left(1 - \frac{2m}{m + L}\right)^k \left(f(x^{(0)}) - f^*\right)$$
**Tốc độ:** $$O(\rho^k)$$ với $$\rho < 1$$ - linear

### 🎲 **18. Stochastic Gradient Descent**

#### **Bài toán tổng**
$$\min_x f(x) = \min_x \sum_{i=1}^m f_i(x)$$

#### **Batch vs SGD**
- **Batch GD:** $$x^{(k)} = x^{(k-1)} - t_k \sum_{i=1}^m \nabla f_i(x^{(k-1)})$$ - Chi phí $$O(m)$$
- **SGD:** $$x^{(k)} = x^{(k-1)} - t_k \nabla f_{i_k}(x^{(k-1)})$$ - Chi phí $$O(1)$$

#### **Mini-batch SGD**
$$x^{(k)} = x^{(k-1)} - t_k \frac{1}{b} \sum_{i \in \mathcal{B}_k} \nabla f_i(x^{(k-1)})$$

### ⚡ **19. Momentum và các kỹ thuật nâng cao**

#### **Classical Momentum**
$$\begin{align}
v^{(k)} &= \beta v^{(k-1)} + \nabla f(x^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align}$$

#### **Adaptive Methods**
- **AdaGrad:** Điều chỉnh learning rate theo lịch sử gradient
- **RMSprop:** Exponential moving average
- **Adam:** Kết hợp momentum và adaptive learning rate

---

## 🔗 **PHẦN VIII: KẾT NỐI VÀ TỔNG HỢP**

### 🌟 **20. Mối liên hệ giữa các khái niệm**

#### **Chuỗi logic xây dựng**
```
Nền tảng toán học (Ch 00)
    ↓
Khái niệm tối ưu hóa (Ch 01)
    ↓
Tập lồi (Ch 02) → Hàm lồi (Ch 03)
    ↓
Điều kiện tối ưu (Ch 04)
    ↓
Bài toán cụ thể (Ch 05) → Thuật toán (Ch 06)
```

#### **Kết nối quan trọng**
- **Gradient** (Ch 00) → **Điều kiện tối ưu bậc nhất** (Ch 04) → **Gradient descent** (Ch 06)
- **Tập lồi** (Ch 02) + **Hàm lồi** (Ch 03) → **Bài toán lồi** (Ch 01,04,05)
- **Chuỗi Taylor** (Ch 00) → **Giải thích gradient descent** (Ch 06)
- **Eigenvalue** (Ch 00) → **Ma trận xác định dương** (Ch 03) → **Hessian** (Ch 04)

### 🎯 **21. Ứng dụng thống nhất**

#### **Machine Learning Pipeline**
1. **Formulation:** Chuyển bài toán ML thành tối ưu hóa (Ch 01, 05)
2. **Analysis:** Kiểm tra tính lồi (Ch 02, 03)
3. **Optimality:** Áp dụng điều kiện tối ưu (Ch 04)
4. **Algorithm:** Sử dụng gradient descent (Ch 06)

#### **Ví dụ: Linear Regression**
- **Bài toán:** $$\min_w \lVert Xw - y \rVert_2^2$$ (Ch 05 - Least Squares)
- **Tính lồi:** Hàm mục tiêu là lồi (Ch 03)
- **Điều kiện tối ưu:** $$\nabla f(w^*) = 2X^T(Xw^* - y) = 0$$ (Ch 04)
- **Nghiệm:** $$w^* = (X^TX)^{-1}X^Ty$$ (Ch 05)
- **Thuật toán:** Gradient descent với $$\nabla f(w) = 2X^T(Xw - y)$$ (Ch 06)

### 🔄 **22. So sánh và lựa chọn phương pháp**

| Bài toán | Phương pháp | Ưu điểm | Nhược điểm |
|----------|-------------|---------|------------|
| **LP** | Simplex | Chính xác, hiệu quả | Chỉ cho LP |
| **QP** | Active Set | Chính xác | Phức tạp |
| **Least Squares** | Normal Equation | Nghiệm đóng | $$O(n^3)$$ |
| **General Convex** | Gradient Descent | Đơn giản, tổng quát | Chậm |
| **Large Scale** | SGD | Nhanh, scalable | Nhiễu |

### 💡 **23. Nguyên tắc thiết kế thuật toán**

#### **Từ lý thuyết đến thực hành**
1. **Phân tích bài toán:** Tính lồi, điều kiện tối ưu
2. **Chọn thuật toán:** Dựa trên cấu trúc bài toán
3. **Tối ưu tham số:** Learning rate, stopping criteria
4. **Đánh giá hiệu suất:** Convergence rate, computational cost

#### **Trade-offs quan trọng**
- **Accuracy vs Speed:** Exact methods vs Gradient methods
- **Memory vs Computation:** Batch vs SGD
- **Simplicity vs Performance:** Basic GD vs Advanced optimizers

---

## 🎓 **PHẦN IX: TỔNG KẾT VÀ HƯỚNG PHÁT TRIỂN**

### 🌟 **24. Những điểm mấu chốt**

#### **Tại sao tối ưu hóa lồi quan trọng?**
1. **Đảm bảo tối ưu toàn cục:** Không có local minima "giả"
2. **Thuật toán hiệu quả:** Polynomial time algorithms
3. **Lý thuyết chặt chẽ:** Convergence guarantees
4. **Ứng dụng rộng rãi:** ML, signal processing, finance, engineering

#### **Gradient descent - Trái tim của ML**
- **Backpropagation** = Gradient descent + Chain rule
- **Deep learning** = SGD + Momentum + Adaptive methods
- **Modern optimizers** = Sophisticated variants of gradient descent

### 🚀 **25. Hướng phát triển tiếp theo**

#### **Chương 07+: Mở rộng lý thuyết**
- **Subgradient:** Non-smooth optimization
- **Proximal methods:** Composite optimization
- **Duality:** Lagrangian và KKT conditions
- **Interior point methods:** Polynomial-time algorithms

#### **Ứng dụng hiện đại**
- **Deep learning:** Neural networks, transformers
- **Reinforcement learning:** Policy optimization
- **Distributed optimization:** Federated learning
- **Quantum optimization:** Quantum algorithms

### 🎯 **26. Lời khuyên học tập**

#### **Cách tiếp cận hiệu quả**
1. **Nắm vững nền tảng:** Toán học cơ bản là chìa khóa
2. **Kết nối khái niệm:** Hiểu mối liên hệ giữa các chương
3. **Thực hành tính toán:** Làm bài tập và implement algorithms
4. **Ứng dụng thực tế:** Áp dụng vào bài toán ML/AI

#### **Debugging và troubleshooting**
- **Kiểm tra tính lồi:** Đảm bảo bài toán well-posed
- **Verify gradients:** Numerical vs analytical gradients
- **Monitor convergence:** Loss curves, gradient norms
- **Tune hyperparameters:** Learning rate, batch size

---

## 💡 **KẾT LUẬN**

Hành trình từ chương 00 đến 06 đã đưa chúng ta qua:

🔢 **Nền tảng toán học** → 🎯 **Khái niệm tối ưu hóa** → 🔵 **Tập lồi** → 📈 **Hàm lồi** → 🏆 **Điều kiện tối ưu** → 📊 **Bài toán cụ thể** → ⚡ **Thuật toán thực tế**

Đây không chỉ là kiến thức lý thuyết mà là **nền tảng của AI và machine learning hiện đại**. Mỗi khái niệm đều có vai trò quan trọng trong việc hiểu và phát triển các thuật toán tối ưu hóa tiên tiến.

**Tối ưu hóa lồi** là cầu nối giữa toán học thuần túy và ứng dụng thực tế, giúp chúng ta giải quyết các bài toán phức tạp một cách hiệu quả và đáng tin cậy.

---

*"Optimization is the engine of machine learning, and convex optimization is its most reliable and well-understood component."*

<style>
/* Custom styling for comprehensive review */
.MathJax {
    vertical-align: baseline !important;
}

h2 {
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
    padding-bottom: 10px;
}

h3 {
    color: #34495e;
    margin-top: 25px;
}

h4 {
    color: #7f8c8d;
    margin-top: 20px;
}

blockquote {
    background-color: #f8f9fa;
    border-left: 4px solid #3498db;
    padding: 15px;
    margin: 20px 0;
    font-style: italic;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
}

table th, table td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}

table th {
    background-color: #f2f2f2;
    font-weight: bold;
}

.highlight-box {
    background-color: #e8f4fd;
    border: 1px solid #bee5eb;
    border-radius: 5px;
    padding: 15px;
    margin: 15px 0;
}

.formula-box {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
    text-align: center;
}

code {
    background-color: #f1f1f1;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: monospace;
}

pre {
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 5px;
    padding: 15px;
    overflow-x: auto;
}
</style>

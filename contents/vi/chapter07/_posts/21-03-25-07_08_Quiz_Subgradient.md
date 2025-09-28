---
layout: post
title: 07-08 Bài tập trắc nghiệm - Subgradient
chapter: '07'
order: 16
owner: GitHub Copilot
lang: vi
categories:
- chapter07
lesson_type: quiz
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### 📐 **Gradient Dưới (Subgradient)**

#### **Định nghĩa**
Đối với hàm lồi $$f: \mathbb{R}^n \to \mathbb{R}$$, gradient dưới tại $$x$$ là vector $$g \in \mathbb{R}^n$$ thỏa mãn:

$$f(y) \ge f(x) + g^T(y - x), \quad \forall y$$

**Ý nghĩa hình học:**
- $$g$$ định nghĩa một siêu phẳng hỗ trợ (supporting hyperplane) của $$f$$ tại $$x$$
- Siêu phẳng này nằm dưới đồ thị hàm số tại mọi điểm
- Tổng quát hóa khái niệm gradient cho hàm không khả vi

#### **Tính chất cơ bản**
- **Tồn tại:** Gradient dưới luôn tồn tại cho hàm lồi
- **Duy nhất:** Nếu $$f$$ khả vi tại $$x$$, thì $$g = \nabla f(x)$$ là gradient dưới duy nhất
- **Không lồi:** Với hàm không lồi, gradient dưới có thể không tồn tại

### 📊 **Các Ví Dụ Quan Trọng**

#### **1. Hàm giá trị tuyệt đối: $$f(x) = \lvert x \rvert$$**
$$\partial f(x) = \begin{cases}
\{-1\} & \text{nếu } x < 0 \\
[-1, 1] & \text{nếu } x = 0 \\
\{1\} & \text{nếu } x > 0
\end{cases}$$

#### **2. Chuẩn L1: $$f(x) = \lVert x \rVert_1 = \sum_{i=1}^n \lvert x_i \rvert$$**
$$(\partial f(x))_i = \begin{cases}
\{\text{sign}(x_i)\} & \text{nếu } x_i \neq 0 \\
[-1, 1] & \text{nếu } x_i = 0
\end{cases}$$

#### **3. Chuẩn L2: $$f(x) = \lVert x \rVert_2$$**
$$\partial f(x) = \begin{cases}
\left\{\frac{x}{\lVert x \rVert_2}\right\} & \text{nếu } x \neq 0 \\
\{g : \lVert g \rVert_2 \le 1\} & \text{nếu } x = 0
\end{cases}$$

#### **4. Hàm max: $$f(x) = \max\{f_1(x), f_2(x)\}$$**
$$\partial f(x) = \begin{cases}
\{\nabla f_1(x)\} & \text{nếu } f_1(x) > f_2(x) \\
\{\nabla f_2(x)\} & \text{nếu } f_1(x) < f_2(x) \\
\text{conv}\{\nabla f_1(x), \nabla f_2(x)\} & \text{nếu } f_1(x) = f_2(x)
\end{cases}$$

### 🔍 **Vi Phân Dưới (Subdifferential)**

#### **Định nghĩa**
Vi phân dưới $$\partial f(x)$$ là tập hợp tất cả gradient dưới tại $$x$$:

$$\partial f(x) = \{g \in \mathbb{R}^n : g \text{ là gradient dưới của } f \text{ tại } x\}$$

#### **Tính chất quan trọng**
- **Tập lồi đóng:** $$\partial f(x)$$ luôn là tập lồi đóng
- **Không rỗng:** Nếu $$f$$ lồi, thì $$\partial f(x) \neq \emptyset$$
- **Duy nhất:** Nếu $$f$$ khả vi tại $$x$$, thì $$\partial f(x) = \{\nabla f(x)\}$$
- **Khả vi:** Nếu $$\partial f(x) = \{g\}$$, thì $$f$$ khả vi tại $$x$$ và $$\nabla f(x) = g$$

### 🎯 **Điều Kiện Tối Ưu Gradient Dưới**

#### **Định lý cơ bản**
$$x^* \text{ là cực tiểu toàn cục của } f \quad \Longleftrightarrow \quad 0 \in \partial f(x^*)$$

#### **Chứng minh**
$$\begin{align}
f(x^*) = \min_x f(x) &\Longleftrightarrow f(y) \ge f(x^*) \text{ với mọi } y \\
&\Longleftrightarrow f(y) \ge f(x^*) + 0^T(y - x^*) \\
&\Longleftrightarrow 0 \in \partial f(x^*)
\end{align}$$

**Lưu ý quan trọng:** Điều kiện này đúng cho cả hàm không lồi!

### 🔗 **Kết Nối với Điều Kiện Tối Ưu Bậc Một**

#### **Bài toán có ràng buộc**
$$\min_{x \in C} f(x)$$

#### **Điều kiện tối ưu bậc một**
Nếu $$f$$ lồi và khả vi:
$$x^* \text{ tối ưu} \Longleftrightarrow \nabla f(x^*)^T(y - x^*) \ge 0, \quad \forall y \in C$$

#### **Suy dẫn từ gradient dưới**
$$\begin{align}
\min_{x \in C} f(x) &\Longleftrightarrow \min_x [f(x) + I_C(x)] \\
&\Longleftrightarrow 0 \in \partial[f(x^*) + I_C(x^*)] \\
&\Longleftrightarrow 0 \in \{\nabla f(x^*)\} + \mathcal{N}_C(x^*) \\
&\Longleftrightarrow -\nabla f(x^*) \in \mathcal{N}_C(x^*) \\
&\Longleftrightarrow \nabla f(x^*)^T(y - x^*) \ge 0, \quad \forall y \in C
\end{align}$$

### 📏 **Quy Tắc Tính Toán Gradient Dưới**

#### **1. Tổ hợp tuyến tính**
$$\partial(\alpha f + \beta g)(x) = \alpha \partial f(x) + \beta \partial g(x)$$
với $$\alpha, \beta \ge 0$$

#### **2. Hàm max**
$$\partial \max\{f_1, \ldots, f_m\}(x) = \text{conv}\{\partial f_i(x) : i \in I(x)\}$$
với $$I(x) = \{i : f_i(x) = \max_j f_j(x)\}$$

#### **3. Hàm hợp thành**
Nếu $$h(x) = f(Ax + b)$$:
$$\partial h(x) = A^T \partial f(Ax + b)$$

#### **4. Hàm chỉ thị**
$$\partial I_C(x) = \begin{cases}
\mathcal{N}_C(x) & \text{nếu } x \in C \\
\emptyset & \text{nếu } x \notin C
\end{cases}$$

với $$\mathcal{N}_C(x)$$ là nón pháp tuyến của $$C$$ tại $$x$$

### 🎲 **Ứng Dụng Thực Tế**

#### **1. LASSO Regression**
$$\min_\beta \frac{1}{2}\lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$$

**Điều kiện tối ưu:**
$$0 \in X^T(X\beta^* - y) + \lambda \partial \lVert \beta^* \rVert_1$$

#### **2. Soft-thresholding**
Nghiệm của $$\min_x \frac{1}{2}(x - a)^2 + \lambda \lvert x \rvert$$:

$$x^* = \text{soft}(a, \lambda) = \begin{cases}
a - \lambda & \text{nếu } a > \lambda \\
0 & \text{nếu } \lvert a \rvert \le \lambda \\
a + \lambda & \text{nếu } a < -\lambda
\end{cases}$$

#### **3. Khoảng cách đến tập lồi**
$$\min_x \frac{1}{2}\lVert x - a \rVert_2^2 + I_C(x)$$

**Nghiệm:** $$x^* = P_C(a)$$ (phép chiếu của $$a$$ lên $$C$$)

### 🔄 **So Sánh Gradient vs Subgradient**

| Khía cạnh | Gradient | Subgradient |
|-----------|----------|-------------|
| **Điều kiện** | Hàm khả vi | Hàm lồi |
| **Duy nhất** | Có | Không (có thể là tập) |
| **Tồn tại** | Không luôn | Luôn (với hàm lồi) |
| **Tính toán** | Đạo hàm | Quy tắc subdifferential |
| **Ứng dụng** | Smooth optimization | Non-smooth optimization |

### 🛠️ **Kỹ Thuật Tính Toán**

#### **Bước 1: Xác định tính khả vi**
- Nếu $$f$$ khả vi tại $$x$$: $$\partial f(x) = \{\nabla f(x)\}$$
- Nếu không khả vi: sử dụng quy tắc tính toán

#### **Bước 2: Phân tích cấu trúc**
- Tổ hợp tuyến tính của hàm lồi
- Hàm max/min
- Hàm hợp thành
- Hàm chỉ thị

#### **Bước 3: Áp dụng quy tắc**
- Sử dụng các quy tắc tính toán subdifferential
- Kết hợp các kết quả từng phần

### ⚡ **Thuật Toán Subgradient Method**

#### **Quy tắc cập nhật**
$$x^{(k+1)} = x^{(k)} - t_k g^{(k)}$$
với $$g^{(k)} \in \partial f(x^{(k)})$$

#### **Lựa chọn step size**
- **Cố định:** $$t_k = t > 0$$
- **Giảm dần:** $$t_k \to 0$$, $$\sum t_k = \infty$$
- **Square summable:** $$\sum t_k^2 < \infty$$

#### **Hội tụ**
- Không đảm bảo giảm monotonic
- Hội tụ về giá trị tối ưu (không nhất thiết về điểm tối ưu)
- Tốc độ hội tụ: $$O(1/\sqrt{k})$$

### 🎯 **Ví Dụ Minh Họa**

#### **Bài toán:** $$\min_x \lvert x - 2 \rvert + \lvert x + 1 \rvert$$

**Bước 1:** Tính subdifferential
$$\partial f(x) = \partial \lvert x - 2 \rvert + \partial \lvert x + 1 \rvert$$

**Bước 2:** Phân tích từng khoảng
- $$x < -1$$: $$\partial f(x) = \{-1 - 1\} = \{-2\}$$
- $$-1 < x < 2$$: $$\partial f(x) = \{-1 + 1\} = \{0\}$$
- $$x > 2$$: $$\partial f(x) = \{1 + 1\} = \{2\}$$

**Bước 3:** Điều kiện tối ưu
$$0 \in \partial f(x^*) \Rightarrow x^* \in [-1, 2]$$

### 💡 **Mẹo Thực Hành**

#### **Nhận biết hàm không khả vi:**
- Hàm chứa $$\lvert \cdot \rvert$$, $$\max\{\cdot\}$$, $$\min\{\cdot\}$$
- Hàm chỉ thị $$I_C(\cdot)$$
- Chuẩn $$\lVert \cdot \rVert_1$$, $$\lVert \cdot \rVert_\infty$$

#### **Tính toán hiệu quả:**
- Sử dụng quy tắc tổ hợp tuyến tính
- Phân tích theo từng thành phần
- Áp dụng tính chất hình học

#### **Kiểm tra kết quả:**
- Xác minh điều kiện subdifferential
- Kiểm tra tính lồi của tập kết quả
- So sánh với trường hợp khả vi (nếu có)

---

💡 **Mẹo:** Subgradient mở rộng khái niệm gradient cho hàm không khả vi, là công cụ mạnh mẽ trong tối ưu hóa lồi và machine learning với regularization!

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

<style>
/* Sửa lỗi alignment cho MathJax inline math */
.MathJax {
    vertical-align: baseline !important;
}

mjx-container[jax="CHTML"][display="false"] {
    vertical-align: baseline !important;
    display: inline !important;
}

/* Đảm bảo các label trong quiz có alignment tốt */
.options label {
    display: flex;
    align-items: center;
    margin: 8px 0;
    padding: 8px;
    border-radius: 4px;
    transition: background-color 0.2s;
}

.options label:hover {
    background-color: #f0f0f0;
}

.options input[type="radio"] {
    margin-right: 8px;
    flex-shrink: 0;
}

/* Styling cho quiz container */
#quiz-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.question {
    background: #f8f9fa;
    border-left: 4px solid #007bff;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.question h3 {
    color: #2c3e50;
    margin-bottom: 15px;
}

.explanation {
    background: #e8f5e8;
    border: 1px solid #28a745;
    padding: 15px;
    margin-top: 15px;
    border-radius: 6px;
}

.quiz-controls {
    text-align: center;
    margin: 30px 0;
}

.quiz-controls button {
    background: #007bff;
    color: white;
    border: none;
    padding: 12px 24px;
    margin: 0 10px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
}

.quiz-controls button:hover {
    background: #0056b3;
}

.quiz-controls button:disabled {
    background: #6c757d;
    cursor: not-allowed;
}

.progress-bar {
    width: 100%;
    height: 8px;
    background: #e9ecef;
    border-radius: 4px;
    margin: 20px 0;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #007bff, #28a745);
    transition: width 0.3s ease;
}

.score-display {
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: #2c3e50;
    margin: 20px 0;
}

.options label.selected {
    background-color: #e3f2fd;
    border: 2px solid #2196f3;
}

.final-score {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    margin: 30px 0;
}
</style>

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về gradient dưới (subgradient), subdifferential, các tính chất hình học và điều kiện tối ưu trong tối ưu hóa lồi.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🧮 Quiz: Subgradient và Subdifferential</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">25</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Định nghĩa subgradient -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Gradient dưới (subgradient) của hàm lồi \\(f\\) tại điểm \\(x\\) là vector \\(g\\) thỏa mãn:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \\(f(y) \leq f(x) + g^T(y-x)\\) với mọi \\(y\\)</label>
                <label><input type="radio" name="q1" value="b"> B) \\(f(y) \geq f(x) + g^T(y-x)\\) với mọi \\(y\\)</label>
                <label><input type="radio" name="q1" value="c"> C) \\(f(y) = f(x) + g^T(y-x)\\) với mọi \\(y\\)</label>
                <label><input type="radio" name="q1" value="d"> D) \\(\nabla f(x) = g\\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$f(y) \geq f(x) + g^T(y-x)$$ với mọi $$y$$</strong><br>
                Đây là định nghĩa chính xác của subgradient: hàm luôn nằm trên siêu phẳng tuyến tính được định nghĩa bởi subgradient.
            </div>
        </div>

        <!-- Câu hỏi 2: Subdifferential -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Subdifferential \\(\partial f(x)\\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Tập hợp tất cả các gradient tại \\(x\\)</label>
                <label><input type="radio" name="q2" value="b"> B) Tập hợp tất cả các subgradient tại \\(x\\)</label>
                <label><input type="radio" name="q2" value="c"> C) Vector gradient duy nhất tại \\(x\\)</label>
                <label><input type="radio" name="q2" value="d"> D) Đạo hàm bậc hai tại \\(x\\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tập hợp tất cả các subgradient tại $$x$$</strong><br>
                Subdifferential $$\partial f(x)$$ là tập hợp tất cả các vector $$g$$ thỏa mãn điều kiện subgradient.
            </div>
        </div>

        <!-- Câu hỏi 3: Subgradient của |x| -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Subgradient của hàm \\(f(x) = |x|\\) tại \\(x = 0\\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \\(\{0\}\\)</label>
                <label><input type="radio" name="q3" value="b"> B) \\(\{1, -1\}\\)</label>
                <label><input type="radio" name="q3" value="c"> C) \\([-1, 1]\\)</label>
                <label><input type="radio" name="q3" value="d"> D) \\(\mathbb{R}\\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$[-1, 1]$$</strong><br>
                Tại $$x = 0$$, hàm $$|x|$$ không khả vi và subdifferential là đoạn $$[-1, 1]$$ vì $$|y| \geq g \cdot y$$ với mọi $$y$$ khi $$g \in [-1, 1]$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Subgradient khi hàm khả vi -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Nếu hàm lồi \\(f\\) khả vi tại \\(x\\), thì \\(\partial f(x)\\) bằng:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) \\(\{\nabla f(x)\}\\)</label>
                <label><input type="radio" name="q4" value="b"> B) \\(\emptyset\\)</label>
                <label><input type="radio" name="q4" value="c"> C) \\(\mathbb{R}^n\\)</label>
                <label><input type="radio" name="q4" value="d"> D) Tập hợp vô hạn các vector</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\{\nabla f(x)\}$$</strong><br>
                Khi hàm lồi khả vi tại một điểm, subdifferential chỉ chứa một phần tử duy nhất là gradient.
            </div>
        </div>

        <!-- Câu hỏi 5: Điều kiện tối ưu -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Điều kiện cần và đủ để \\(x^*\\) là điểm cực tiểu toàn cục của hàm lồi \\(f\\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \\(\nabla f(x^*) = 0\\)</label>
                <label><input type="radio" name="q5" value="b"> B) \\(0 \in \partial f(x^*)\\)</label>
                <label><input type="radio" name="q5" value="c"> C) \\(f(x^*) = 0\\)</label>
                <label><input type="radio" name="q5" value="d"> D) \\(\partial f(x^*) = \mathbb{R}^n\\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$0 \in \partial f(x^*)$$</strong><br>
                Điều kiện tối ưu subgradient: $$x^*$$ là cực tiểu toàn cục khi và chỉ khi $$0$$ thuộc subdifferential tại $$x^*$$.
            </div>
        </div>

        <!-- Câu hỏi 6: Tính chất subdifferential -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Subdifferential \(\partial f(x)\) của hàm lồi luôn là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) Tập hợp rỗng</label>
                <label><input type="radio" name="q6" value="b"> B) Tập hợp đóng và lồi</label>
                <label><input type="radio" name="q6" value="c"> C) Tập hợp mở</label>
                <label><input type="radio" name="q6" value="d"> D) Chỉ chứa một phần tử</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tập hợp đóng và lồi</strong><br>
                Subdifferential của hàm lồi luôn là tập hợp đóng, lồi và compact (nếu hàm hữu hạn tại điểm đó).
            </div>
        </div>

        <!-- Câu hỏi 7: Subgradient của max function -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Cho \(f(x) = \max\{x_1, x_2\}\) tại điểm \(x = (2, 2)\). Subdifferential \(\partial f(x)\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(\{(1, 0), (0, 1)\}\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(\text{conv}\{(1, 0), (0, 1)\}\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(\{(1, 1)\}\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(\{(0, 0)\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) \(\text{conv}\{(1, 0), (0, 1)\}\)</strong><br>
                Tại điểm có nhiều thành phần đạt maximum, subdifferential là bao lồi của các gradient của các thành phần active.
            </div>
        </div>

        <!-- Câu hỏi 8: Quy tắc tổng -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Nếu \(f\) và \(g\) là hai hàm lồi, thì \(\partial(f + g)(x)\) bằng:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\partial f(x) + \partial g(x)\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(\partial f(x) \cup \partial g(x)\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(\partial f(x) \cap \partial g(x)\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(\max\{\partial f(x), \partial g(x)\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) \(\partial f(x) + \partial g(x)\)</strong><br>
                Quy tắc tổng: subdifferential của tổng bằng tổng Minkowski của các subdifferential.
            </div>
        </div>

        <!-- Câu hỏi 9: Subgradient của norm -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Subdifferential của hàm \(f(x) = \|x\|_2\) tại \(x \neq 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\{x/\|x\|_2\}\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\{u : \|u\|_2 \leq 1\}\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\{0\}\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\mathbb{R}^n\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) \(\{x/\|x\|_2\}\)</strong><br>
                Khi \(x \neq 0\), norm Euclidean khả vi và gradient là \(x/\|x\|_2\).
            </div>
        </div>

        <!-- Câu hỏi 10: Subgradient tại gốc -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Subdifferential của hàm \(f(x) = \|x\|_2\) tại \(x = 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(\{0\}\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(\{u : \|u\|_2 \leq 1\}\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(\{u : \|u\|_2 = 1\}\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(\mathbb{R}^n\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) \(\{u : \|u\|_2 \leq 1\}\)</strong><br>
                Tại gốc, subdifferential của norm Euclidean là đơn vị ball đóng.
            </div>
        </div>

        <!-- Câu hỏi 11: Quy tắc chain rule -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Cho \(f(x) = g(Ax + b)\) với \(g\) lồi và \(A\) là ma trận. Khi đó \(\partial f(x)\) bằng:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(A^T \partial g(Ax + b)\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(A \partial g(Ax + b)\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(\partial g(Ax + b) A^T\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(\partial g(Ax + b)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) \(A^T \partial g(Ax + b)\)</strong><br>
                Chain rule cho subdifferential: \(\partial f(x) = A^T \partial g(Ax + b)\).
            </div>
        </div>

        <!-- Câu hỏi 12: Hàm chỉ thị -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Subdifferential của hàm chỉ thị \(I_C(x)\) của tập lồi \(C\) tại \(x \in C\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) \(\{0\}\)</label>
                <label><input type="radio" name="q12" value="b"> B) Nón pháp tuyến \(N_C(x)\)</label>
                <label><input type="radio" name="q12" value="c"> C) Nón tiếp tuyến \(T_C(x)\)</label>
                <label><input type="radio" name="q12" value="d"> D) \(\mathbb{R}^n\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Nón pháp tuyến \(N_C(x)\)</strong><br>
                Subdifferential của hàm chỉ thị bằng nón pháp tuyến của tập lồi tại điểm đó.
            </div>
        </div>

        <!-- Câu hỏi 13: Tính đơn điệu -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Toán tử subdifferential \(\partial f\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Đơn điệu</label>
                <label><input type="radio" name="q13" value="b"> B) Không đơn điệu</label>
                <label><input type="radio" name="q13" value="c"> C) Tuyến tính</label>
                <label><input type="radio" name="q13" value="d"> D) Liên tục</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Đơn điệu</strong><br>
                Subdifferential của hàm lồi là toán tử đơn điệu: \((g_1 - g_2)^T(x_1 - x_2) \geq 0\) với \(g_i \in \partial f(x_i)\).
            </div>
        </div>

        <!-- Câu hỏi 14: Subgradient của hàm tuyến tính -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Subdifferential của hàm tuyến tính \(f(x) = c^T x\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(\{c\}\)</label>
                <label><input type="radio" name="q14" value="b"> B) \(\{0\}\)</label>
                <label><input type="radio" name="q14" value="c"> C) \(\mathbb{R}^n\)</label>
                <label><input type="radio" name="q14" value="d"> D) \(\{tc : t \geq 0\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) \(\{c\}\)</strong><br>
                Hàm tuyến tính khả vi mọi nơi với gradient không đổi bằng \(c\).
            </div>
        </div>

        <!-- Câu hỏi 15: Subgradient của hàm bậc hai -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Cho \(f(x) = \frac{1}{2}x^T Q x + c^T x\) với \(Q \succeq 0\). Subdifferential \(\partial f(x)\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(\{Qx + c\}\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(\{Qx\}\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(\{c\}\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(\{x\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) \(\{Qx + c\}\)</strong><br>
                Hàm bậc hai lồi khả vi với gradient \(\nabla f(x) = Qx + c\).
            </div>
        </div>

        <!-- Câu hỏi 16: Điều kiện tối ưu có ràng buộc -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Cho bài toán \(\min f(x)\) s.t. \(x \in C\). Điều kiện tối ưu là:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(0 \in \partial f(x^*)\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(-\partial f(x^*) \cap N_C(x^*) \neq \emptyset\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(\nabla f(x^*) = 0\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(x^* \in C\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) \(-\partial f(x^*) \cap N_C(x^*) \neq \emptyset\)</strong><br>
                Điều kiện tối ưu subgradient có ràng buộc: tồn tại subgradient âm thuộc nón pháp tuyến.
            </div>
        </div>

        <!-- Câu hỏi 17: Subgradient của hàm lồi từng phần -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Cho \(f(x) = \max\{f_1(x), f_2(x)\}\) với \(f_1, f_2\) lồi và khả vi. Tại điểm \(x\) mà \(f_1(x) > f_2(x)\):</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(\partial f(x) = \{\nabla f_1(x)\}\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(\partial f(x) = \{\nabla f_2(x)\}\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(\partial f(x) = \text{conv}\{\nabla f_1(x), \nabla f_2(x)\}\)</label>
                <label><input type="radio" name="q17" value="d"> D) \(\partial f(x) = \emptyset\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) \(\partial f(x) = \{\nabla f_1(x)\}\)</strong><br>
                Khi chỉ có một hàm đạt maximum, subdifferential chỉ chứa gradient của hàm đó.
            </div>
        </div>

        <!-- Câu hỏi 18: Tính liên tục -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Subdifferential \(\partial f(x)\) của hàm lồi \(f\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Liên tục trên</label>
                <label><input type="radio" name="q18" value="b"> B) Nửa liên tục trên</label>
                <label><input type="radio" name="q18" value="c"> C) Liên tục dưới</label>
                <label><input type="radio" name="q18" value="d"> D) Không liên tục</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Nửa liên tục trên</strong><br>
                Subdifferential là ánh xạ đa trị nửa liên tục trên (upper semicontinuous).
            </div>
        </div>

        <!-- Câu hỏi 19: Subgradient của hàm khoảng cách -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Cho \(f(x) = d_C(x) = \inf_{y \in C} \|x - y\|_2\) với \(C\) lồi đóng. Khi \(x \notin C\):</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(\partial f(x) = \{(x - P_C(x))/\|x - P_C(x)\|_2\}\)</label>
                <label><input type="radio" name="q19" value="b"> B) \(\partial f(x) = \{0\}\)</label>
                <label><input type="radio" name="q19" value="c"> C) \(\partial f(x) = N_C(x)\)</label>
                <label><input type="radio" name="q19" value="d"> D) \(\partial f(x) = \{x\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) \(\partial f(x) = \{(x - P_C(x))/\|x - P_C(x)\|_2\}\)</strong><br>
                Subgradient của hàm khoảng cách là vector đơn vị từ phép chiếu đến điểm gốc.
            </div>
        </div>

        <!-- Câu hỏi 20: Subgradient của hàm support -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Hàm support \(\sigma_C(x) = \sup_{y \in C} y^T x\) của tập lồi compact \(C\) có subdifferential:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) \(\partial \sigma_C(x) = \arg\max_{y \in C} y^T x\)</label>
                <label><input type="radio" name="q20" value="b"> B) \(\partial \sigma_C(x) = C\)</label>
                <label><input type="radio" name="q20" value="c"> C) \(\partial \sigma_C(x) = \{x\}\)</label>
                <label><input type="radio" name="q20" value="d"> D) \(\partial \sigma_C(x) = \{0\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) \(\partial \sigma_C(x) = \arg\max_{y \in C} y^T x\)</strong><br>
                Subdifferential của hàm support là tập các điểm đạt maximum trong định nghĩa supremum.
            </div>
        </div>

        <!-- Câu hỏi 21: Ứng dụng trong machine learning -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Trong SVM, hàm hinge loss \(f(t) = \max\{0, 1-t\}\) có subdifferential tại \(t = 1\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) \(\{0\}\)</label>
                <label><input type="radio" name="q21" value="b"> B) \(\{-1\}\)</label>
                <label><input type="radio" name="q21" value="c"> C) \([-1, 0]\)</label>
                <label><input type="radio" name="q21" value="d"> D) \([0, 1]\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) \([-1, 0]\)</strong><br>
                Tại điểm kink \(t = 1\), subdifferential là đoạn nối giữa đạo hàm trái (-1) và đạo hàm phải (0).
            </div>
        </div>

        <!-- Câu hỏi 22: Subgradient của norm L1 -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Subdifferential của \(f(x) = \|x\|_1\) tại \(x\) với \(x_i \neq 0\) cho thành phần thứ \(i\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) \(\text{sign}(x_i)\)</label>
                <label><input type="radio" name="q22" value="b"> B) \([-1, 1]\)</label>
                <label><input type="radio" name="q22" value="c"> C) \(x_i\)</label>
                <label><input type="radio" name="q22" value="d"> D) \(|x_i|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) \(\text{sign}(x_i)\)</strong><br>
                Khi \(x_i \neq 0\), thành phần thứ \(i\) của subdifferential là \(\text{sign}(x_i)\).
            </div>
        </div>

        <!-- Câu hỏi 23: Subgradient tại điểm không khả vi -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Nếu hàm lồi \(f\) không khả vi tại \(x\), thì \(\partial f(x)\):</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Là tập hợp rỗng</label>
                <label><input type="radio" name="q23" value="b"> B) Chứa nhiều hơn một phần tử</label>
                <label><input type="radio" name="q23" value="c"> C) Chỉ chứa vector không</label>
                <label><input type="radio" name="q23" value="d"> D) Không xác định</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Chứa nhiều hơn một phần tử</strong><br>
                Tại điểm không khả vi, subdifferential chứa nhiều subgradient, phản ánh sự "góc cạnh" của hàm.
            </div>
        </div>

        <!-- Câu hỏi 24: Ứng dụng trong tối ưu hóa -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Trong thuật toán subgradient method, hướng cập nhật được chọn là:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Gradient \(\nabla f(x)\)</label>
                <label><input type="radio" name="q24" value="b"> B) Bất kỳ subgradient \(g \in \partial f(x)\)</label>
                <label><input type="radio" name="q24" value="c"> C) Vector ngẫu nhiên</label>
                <label><input type="radio" name="q24" value="d"> D) Hướng Newton</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Bất kỳ subgradient \(g \in \partial f(x)\)</strong><br>
                Subgradient method sử dụng bất kỳ subgradient nào tại điểm hiện tại để cập nhật.
            </div>
        </div>

        <!-- Câu hỏi 25: Tính chất hình học -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Về mặt hình học, subgradient \(g \in \partial f(x)\) định nghĩa:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Siêu phẳng tiếp xúc với đồ thị hàm</label>
                <label><input type="radio" name="q25" value="b"> B) Siêu phẳng nằm dưới đồ thị hàm</label>
                <label><input type="radio" name="q25" value="c"> C) Siêu phẳng cắt đồ thị hàm</label>
                <label><input type="radio" name="q25" value="d"> D) Siêu phẳng vuông góc với đồ thị hàm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Siêu phẳng nằm dưới đồ thị hàm</strong><br>
                Subgradient định nghĩa siêu phẳng support: \(f(y) \geq f(x) + g^T(y-x)\) - đồ thị hàm nằm trên siêu phẳng này.
            </div>
        </div>

    </div>

    <div class="quiz-controls">
        <button onclick="previousQuestion()" id="prev-btn" disabled>← Câu trước</button>
        <button onclick="nextQuestion()" id="next-btn">Câu tiếp →</button>
        <button onclick="submitQuiz()" id="submit-btn" style="display: none;">Nộp bài</button>
        <button onclick="resetQuiz()" id="reset-btn" style="display: none;">Làm lại</button>
    </div>

    <div id="final-result" style="display: none;" class="final-score">
        <h2>🎉 Hoàn thành Quiz!</h2>
        <p>Điểm số của bạn: <span id="final-score-text"></span></p>
        <p id="performance-message"></p>
    </div>
</div>

<script>
let currentQuestion = 1;
const totalQuestions = 25;
let userAnswers = {};
let quizSubmitted = false;

// Đáp án đúng
const correctAnswers = {
    q1: 'b', q2: 'b', q3: 'c', q4: 'a', q5: 'b',
    q6: 'b', q7: 'b', q8: 'a', q9: 'a', q10: 'b',
    q11: 'a', q12: 'b', q13: 'a', q14: 'a', q15: 'a',
    q16: 'b', q17: 'a', q18: 'b', q19: 'a', q20: 'a',
    q21: 'c', q22: 'a', q23: 'b', q24: 'b', q25: 'b'
};

function showQuestion(n) {
    // Ẩn tất cả câu hỏi
    for (let i = 1; i <= totalQuestions; i++) {
        document.getElementById(`q${i}`).style.display = 'none';
    }
    
    // Hiển thị câu hỏi hiện tại
    document.getElementById(`q${n}`).style.display = 'block';
    
    // Cập nhật progress bar
    const progress = (n / totalQuestions) * 100;
    document.getElementById('progress-fill').style.width = progress + '%';
    
    // Cập nhật số câu hỏi
    document.getElementById('current-q').textContent = n;
    
    // Cập nhật nút điều hướng
    document.getElementById('prev-btn').disabled = (n === 1);
    document.getElementById('next-btn').style.display = (n === totalQuestions) ? 'none' : 'inline-block';
    document.getElementById('submit-btn').style.display = (n === totalQuestions) ? 'inline-block' : 'none';
    
    currentQuestion = n;
    
    // Re-render MathJax cho câu hỏi hiện tại
    if (window.MathJax) {
        MathJax.typesetPromise([document.getElementById(`q${n}`)]).then(() => {
            // MathJax rendering complete
        });
    }
}

function nextQuestion() {
    if (currentQuestion < totalQuestions) {
        showQuestion(currentQuestion + 1);
    }
}

function previousQuestion() {
    if (currentQuestion > 1) {
        showQuestion(currentQuestion - 1);
    }
}

function saveAnswer(questionId, answer) {
    userAnswers[questionId] = answer;
    
    // Highlight selected option
    const questionDiv = document.getElementById(questionId);
    const labels = questionDiv.querySelectorAll('.options label');
    labels.forEach(label => {
        label.classList.remove('selected');
        const input = label.querySelector('input[type="radio"]');
        if (input.checked) {
            label.classList.add('selected');
        }
    });
}

function calculateScore() {
    let correct = 0;
    for (let q in correctAnswers) {
        if (userAnswers[q] === correctAnswers[q]) {
            correct++;
        }
    }
    return correct;
}

function submitQuiz() {
    quizSubmitted = true;
    const score = calculateScore();
    const percentage = Math.round((score / totalQuestions) * 100);
    
    // Hiển thị tất cả giải thích
    for (let i = 1; i <= totalQuestions; i++) {
        const explanation = document.querySelector(`#q${i} .explanation`);
        explanation.style.display = 'block';
        
        // Highlight đáp án đúng và sai
        const questionDiv = document.getElementById(`q${i}`);
        const labels = questionDiv.querySelectorAll('.options label');
        labels.forEach(label => {
            const input = label.querySelector('input[type="radio"]');
            const value = input.value;
            
            if (value === correctAnswers[`q${i}`]) {
                label.style.backgroundColor = '#d4edda';
                label.style.border = '2px solid #28a745';
            } else if (value === userAnswers[`q${i}`] && value !== correctAnswers[`q${i}`]) {
                label.style.backgroundColor = '#f8d7da';
                label.style.border = '2px solid #dc3545';
            }
        });
    }
    
    // Hiển thị kết quả cuối
    document.getElementById('final-result').style.display = 'block';
    document.getElementById('final-score-text').textContent = `${score}/${totalQuestions} (${percentage}%)`;
    
    let message = '';
    if (percentage >= 90) {
        message = '🌟 Xuất sắc! Bạn đã nắm vững kiến thức về subgradient!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu khá tốt về subgradient và subdifferential.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại một số khái niệm về điều kiện tối ưu.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Hãy ôn lại định nghĩa và tính chất cơ bản.';
    } else {
        message = '📖 Hãy học lại từ đầu các khái niệm về subgradient nhé!';
    }
    
    document.getElementById('performance-message').textContent = message;
    
    // Ẩn nút submit, hiện nút reset
    document.getElementById('submit-btn').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'inline-block';
    
    // Re-render MathJax cho tất cả nội dung
    if (window.MathJax) {
        MathJax.typesetPromise().then(() => {
            // MathJax rendering complete
        });
    }
    
    // Cuộn đến kết quả
    document.getElementById('final-result').scrollIntoView({ behavior: 'smooth' });
}

function resetQuiz() {
    // Reset trạng thái
    currentQuestion = 1;
    userAnswers = {};
    quizSubmitted = false;
    
    // Ẩn tất cả giải thích
    document.querySelectorAll('.explanation').forEach(exp => {
        exp.style.display = 'none';
    });
    
    // Reset style của labels
    document.querySelectorAll('.options label').forEach(label => {
        label.style.backgroundColor = '';
        label.style.border = '';
        label.classList.remove('selected');
    });
    
    // Uncheck tất cả radio buttons
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.checked = false;
    });
    
    document.querySelectorAll('.options label').forEach(label => {
        label.classList.remove('selected');
    });
    
    // Hiển thị câu hỏi đầu tiên
    showQuestion(1);
    
    // Cuộn lên đầu
    document.getElementById('quiz-header').scrollIntoView({ behavior: 'smooth' });
    
    // Ẩn kết quả cuối và reset button
    document.getElementById('final-result').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'none';
}

// Khởi tạo bài tập khi trang được tải
document.addEventListener('DOMContentLoaded', function() {
    showQuestion(1);
    
    // Thêm event listener cho tất cả radio button
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.addEventListener('change', function() {
            const questionId = this.name;
            const answer = this.value;
            saveAnswer(questionId, answer);
        });
    });
    
    // Render MathJax sau khi DOM được tải
    if (window.MathJax) {
        MathJax.typesetPromise().then(() => {
            // MathJax rendering complete
        });
    }
});

// Xử lý phím tắt
document.addEventListener('keydown', function(event) {
    if (quizSubmitted) return;
    
    switch(event.key) {
        case 'ArrowLeft':
            if (currentQuestion > 1) previousQuestion();
            break;
        case 'ArrowRight':
            if (currentQuestion < totalQuestions) nextQuestion();
            break;
        case 'Enter':
            if (currentQuestion === totalQuestions) submitQuiz();
            break;
    }
});
</script>
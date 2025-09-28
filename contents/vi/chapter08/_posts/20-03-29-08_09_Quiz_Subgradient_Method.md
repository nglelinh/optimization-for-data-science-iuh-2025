---
layout: post
title: 08-09 Bài tập trắc nghiệm - Phương Pháp Subgradient
chapter: '08'
order: 17
owner: GitHub Copilot
lang: vi
categories:
- chapter08
lesson_type: quiz
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Phương Pháp Subgradient**

#### **Định nghĩa thuật toán**
Phương pháp subgradient là mở rộng của gradient descent cho hàm lồi không khả vi:

$$x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}, \quad k = 1, 2, 3, \ldots$$

với $$g^{(k-1)} \in \partial f(x^{(k-1)})$$ là một subgradient của $$f$$ tại $$x^{(k-1)}$$

#### **Khác biệt quan trọng với Gradient Descent**
- **Không đảm bảo descent:** Giá trị hàm số có thể tăng ở một số bước
- **Theo dõi best value:** $$f(x_{\text{best}}^{(k)}) = \min_{i=0,\ldots,k} f(x^{(i)})$$
- **Step size cố định:** Không thể sử dụng line search như gradient descent

### 📏 **Lựa Chọn Kích Thước Bước**

#### **1. Kích thước bước cố định**
$$t_k = t > 0, \quad \forall k$$

**Đặc điểm:**
- Đơn giản để implement
- Hội tụ đến lân cận của nghiệm tối ưu
- Không đạt được nghiệm chính xác

#### **2. Kích thước bước giảm dần**
Thỏa mãn điều kiện:
$$\sum_{k=1}^{\infty} t_k = \infty, \quad \sum_{k=1}^{\infty} t_k^2 < \infty$$

**Ví dụ phổ biến:**
- $$t_k = \frac{1}{k}$$ (chuỗi điều hòa)
- $$t_k = \frac{1}{\sqrt{k}}$$
- $$t_k = \frac{a}{b + k}$$ với $$a, b > 0$$

**Đặc điểm:**
- Hội tụ chính xác đến nghiệm tối ưu
- Tốc độ hội tụ chậm hơn kích thước bước cố định ban đầu

#### **3. Polyak step sizes**
$$t_k = \frac{f(x^{(k)}) - f^*}{\lVert g^{(k)} \rVert_2^2}$$

**Yêu cầu:** Biết giá trị tối ưu $$f^*$$
**Ưu điểm:** Hội tụ nhanh hơn khi biết $$f^*$$

### 📊 **Phân Tích Hội Tụ**

#### **Giả định cơ bản**
- $$f$$ là hàm lồi với $$\text{dom}(f) = \mathbb{R}^n$$
- $$f$$ thỏa mãn điều kiện Lipschitz:
  $$|f(x) - f(y)| \le G \lVert x - y \rVert_2, \quad \forall x, y$$
- Subgradients bị chặn: $$\lVert g \rVert_2 \le G$$ với $$g \in \partial f(x)$$

#### **Định lý hội tụ cho kích thước bước cố định**
$$\lim_{k \to \infty} f(x_{\text{best}}^{(k)}) \le f^* + \frac{G^2 t}{2}$$

**Ý nghĩa:**
- Hội tụ đến lân cận của nghiệm tối ưu
- Sai số cuối cùng tỷ lệ với kích thước bước $$t$$
- Trade-off: $$t$$ nhỏ → sai số nhỏ nhưng hội tụ chậm

#### **Định lý hội tụ cho kích thước bước giảm dần**
$$\lim_{k \to \infty} f(x_{\text{best}}^{(k)}) = f^*$$

**Ý nghĩa:**
- Hội tụ chính xác đến nghiệm tối ưu
- Tốc độ hội tụ: $$O(1/\sqrt{k})$$ (sublinear)

#### **Chứng minh cơ bản**
Từ bất đẳng thức cơ bản:
$$f_{\text{best}}^{(k)} - f^* \le \frac{R^2 + G^2 \sum_{i=1}^k t_i^2}{2 \sum_{i=1}^k t_i}$$

với $$R = \lVert x^{(0)} - x^* \rVert_2$$

### 🎯 **Ứng Dụng Thực Tế**

#### **1. LASSO Regression**
$$\min_\beta \frac{1}{2} \lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$$

**Subgradient:**
$$\partial f(\beta) = X^T(X\beta - y) + \lambda \partial \lVert \beta \rVert_1$$

#### **2. Regularized Logistic Regression**
$$\min_\beta \sum_{i=1}^n \left[-y_i x_i^T \beta + \log(1 + \exp(x_i^T \beta))\right] + \lambda \lVert \beta \rVert_1$$

**So sánh:**
- **Ridge (L2):** Khả vi → Gradient descent
- **LASSO (L1):** Không khả vi → Subgradient method

#### **3. Support Vector Machine**
$$\min_w \frac{1}{2} \lVert w \rVert_2^2 + C \sum_{i=1}^n \max(0, 1 - y_i w^T x_i)$$

**Hinge loss:** $$\max(0, 1 - z)$$ không khả vi tại $$z = 1$$

### 🔄 **Stochastic Subgradient Method**

#### **Bài toán tổng**
$$\min_x f(x) = \min_x \sum_{i=1}^m f_i(x)$$

#### **Stochastic update**
$$x^{(k)} = x^{(k-1)} - t_k g_i^{(k-1)}$$

với $$g_i^{(k-1)} \in \partial f_i(x^{(k-1)})$$ và $$i$$ được chọn ngẫu nhiên

#### **Ưu điểm**
- Chi phí tính toán: $$O(1)$$ thay vì $$O(m)$$
- Phù hợp với big data
- Có thể thoát khỏi saddle points

#### **Nhược điểm**
- Nhiễu cao hơn batch method
- Cần tuning learning rate cẩn thận
- Hội tụ chậm hơn gần nghiệm tối ưu

### 📈 **Projected Subgradient Method**

#### **Bài toán có ràng buộc**
$$\min_{x \in C} f(x)$$

với $$C$$ là tập lồi đóng

#### **Thuật toán**
$$x^{(k)} = P_C(x^{(k-1)} - t_k g^{(k-1)})$$

với $$P_C(\cdot)$$ là phép chiếu lên tập $$C$$

#### **Ví dụ: Intersection of Sets**
$$\min_x \frac{1}{2} \lVert x \rVert_2^2 \quad \text{s.t.} \quad x \in \bigcap_{i=1}^m C_i$$

**Thuật toán:**
1. Chọn tập $$C_i$$ vi phạm nhất
2. Chiếu lên $$C_i$$: $$x^{(k)} = P_{C_i}(x^{(k-1)})$$

### 🔄 **So Sánh Các Phương Pháp**

| Phương pháp | Điều kiện | Tốc độ hội tụ | Ứng dụng |
|-------------|-----------|---------------|----------|
| **Gradient Descent** | Hàm khả vi | $$O(1/k)$$ hoặc linear | Smooth optimization |
| **Subgradient** | Hàm lồi | $$O(1/\sqrt{k})$$ | Non-smooth optimization |
| **SGD** | Hàm khả vi | $$O(1/\sqrt{k})$$ | Large-scale problems |
| **Stochastic Subgradient** | Hàm lồi | $$O(1/\sqrt{k})$$ | Large-scale non-smooth |

### 🛠️ **Kỹ Thuật Thực Hành**

#### **Chọn step size**
1. **Fixed step size:** Thử $$t = 0.01, 0.1, 1$$ và chọn tốt nhất
2. **Diminishing:** Sử dụng $$t_k = \frac{1}{\sqrt{k}}$$ hoặc $$t_k = \frac{1}{k}$$
3. **Polyak:** Nếu biết $$f^*$$, sử dụng công thức Polyak

#### **Monitoring convergence**
- Theo dõi $$f(x_{\text{best}}^{(k)})$$ thay vì $$f(x^{(k)})$$
- Vẽ đồ thị convergence để kiểm tra
- Sử dụng moving average để làm mượt

#### **Debugging**
- Kiểm tra tính đúng đắn của subgradient
- Verify Lipschitz constant $$G$$
- Thử nhiều step size khác nhau
- So sánh với gradient descent (nếu hàm khả vi)

### ⚡ **Cải Tiến Subgradient Method**

#### **1. Averaging**
$$\bar{x}^{(k)} = \frac{1}{k} \sum_{i=1}^k x^{(i)}$$

**Ưu điểm:** Giảm nhiễu, cải thiện convergence rate

#### **2. Momentum**
$$x^{(k)} = x^{(k-1)} - t_k g^{(k-1)} + \beta(x^{(k-1)} - x^{(k-2)})$$

**Ưu điểm:** Tăng tốc hội tụ, giảm oscillation

#### **3. Adaptive step sizes**
- **AdaGrad for subgradients**
- **RMSprop variants**
- **Adam-like methods**

### 🎯 **Ví Dụ Minh Họa**

#### **Bài toán:** $$\min_x |x - 2| + |x + 1|$$

**Bước 1:** Tính subgradient
$$\partial f(x) = \partial |x - 2| + \partial |x + 1|$$

**Bước 2:** Subgradient method với $$t_k = 0.1$$
- Bắt đầu từ $$x^{(0)} = 5$$
- $$g^{(0)} = 1 + 1 = 2$$
- $$x^{(1)} = 5 - 0.1 \times 2 = 4.8$$
- Tiếp tục cho đến hội tụ

**Kết quả:** Hội tụ đến $$x^* \in [-1, 2]$$

### 💡 **Mẹo Thực Hành**

#### **Khi nào sử dụng Subgradient Method:**
- Hàm mục tiêu không khả vi (chứa $$\lvert \cdot \rvert$$, $$\max\{\cdot\}$$)
- Regularization với L1 norm
- Constraint optimization với indicator functions
- Large-scale problems với stochastic variants

#### **Khi nào KHÔNG sử dụng:**
- Hàm khả vi (dùng gradient descent)
- Cần convergence nhanh (dùng Newton methods)
- Hàm không lồi (không đảm bảo global optimum)

#### **Best practices:**
- Luôn theo dõi $$f_{\text{best}}^{(k)}$$
- Thử nhiều step size strategies
- Sử dụng averaging để giảm nhiễu
- Kết hợp với projection cho constrained problems

---

💡 **Mẹo:** Subgradient method là công cụ mạnh mẽ cho non-smooth optimization, đặc biệt quan trọng trong machine learning với regularization và robust optimization!

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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về phương pháp subgradient, lựa chọn kích thước bước, phân tích hội tụ, projected subgradient method và stochastic subgradient method.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: Phương Pháp Subgradient</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Định nghĩa subgradient method -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Công thức cập nhật của phương pháp subgradient là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(x^{(k)} = x^{(k-1)} + t_k \cdot g^{(k-1)}\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(x^{(k)} = x^{(k-1)} - t_k \cdot \nabla f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(x^{(k)} = x^{(k-1)} - g^{(k-1)}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}$$</strong><br>
                Phương pháp subgradient thay thế gradient bằng subgradient $$g^{(k-1)} \in \partial f(x^{(k-1)})$$ với step size $$t_k$$.
            </div>
        </div>

        <!-- Câu hỏi 2: Tính chất descent -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Khác với gradient descent, phương pháp subgradient:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Luôn giảm giá trị hàm số ở mỗi bước</label>
                <label><input type="radio" name="q2" value="b"> B) Không luôn đảm bảo giảm giá trị hàm số ở mỗi bước</label>
                <label><input type="radio" name="q2" value="c"> C) Chỉ áp dụng cho hàm khả vi</label>
                <label><input type="radio" name="q2" value="d"> D) Hội tụ nhanh hơn gradient descent</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Không luôn đảm bảo giảm giá trị hàm số ở mỗi bước</strong><br>
                Vì vậy phương pháp này không được gọi là "descent" subgradient và cần theo dõi giá trị tốt nhất $$f(x_{best}^{(k)})$$.
            </div>
        </div>

        <!-- Câu hỏi 3: Best value tracking -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Trong subgradient method, \(f(x_{best}^{(k)})\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(f(x^{(k)})\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\min_{i=0,...,k} f(x^{(i)})\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(\max_{i=0,...,k} f(x^{(i)})\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(\frac{1}{k+1} \sum_{i=0}^k f(x^{(i)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\min_{i=0,...,k} f(x^{(i)})$$</strong><br>
                Đây là giá trị nhỏ nhất của hàm $$f$$ thu được trong $$k$$ lần lặp của phương pháp subgradient.
            </div>
        </div>

        <!-- Câu hỏi 4: Fixed step size -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Với kích thước bước cố định \(t_k = t\), phương pháp subgradient:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Hội tụ đến nghiệm tối ưu chính xác</label>
                <label><input type="radio" name="q4" value="b"> B) Hội tụ đến một lân cận của nghiệm tối ưu</label>
                <label><input type="radio" name="q4" value="c"> C) Không hội tụ</label>
                <label><input type="radio" name="q4" value="d"> D) Chỉ hội tụ cho hàm khả vi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Hội tụ đến một lân cận của nghiệm tối ưu</strong><br>
                Với step size cố định, thuật toán không hội tụ chính xác mà chỉ đến gần nghiệm tối ưu trong một lân cận.
            </div>
        </div>

        <!-- Câu hỏi 5: Diminishing step size conditions -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Điều kiện cho kích thước bước giảm dần để đảm bảo hội tụ là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(\sum_{k=1}^{\infty} t_k < \infty\) và \(\sum_{k=1}^{\infty} t_k^2 < \infty\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(\sum_{k=1}^{\infty} t_k = \infty\) và \(\sum_{k=1}^{\infty} t_k^2 < \infty\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(\sum_{k=1}^{\infty} t_k = \infty\) và \(\sum_{k=1}^{\infty} t_k^2 = \infty\)</label>
                <label><input type="radio" name="q5" value="d"> D) \(t_k = \text{constant}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\sum_{k=1}^{\infty} t_k = \infty$$ và $$\sum_{k=1}^{\infty} t_k^2 < \infty$$</strong><br>
                Điều kiện Robbins-Monro: tổng vô hạn để đảm bảo tiến bộ, tổng bình phương hữu hạn để kiểm soát nhiễu.
            </div>
        </div>

        <!-- Câu hỏi 6: Ví dụ step size -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Kích thước bước \(t_k = \frac{1}{k}\) thỏa mãn điều kiện hội tụ vì:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(\sum_{k=1}^{\infty} \frac{1}{k} = \infty\) (chuỗi điều hòa) và \(\sum_{k=1}^{\infty} \frac{1}{k^2} < \infty\) (bài toán Basel)</label>
                <label><input type="radio" name="q6" value="b"> B) Cả hai tổng đều hữu hạn</label>
                <label><input type="radio" name="q6" value="c"> C) Cả hai tổng đều vô hạn</label>
                <label><input type="radio" name="q6" value="d"> D) Không thỏa mãn điều kiện</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\sum_{k=1}^{\infty} \frac{1}{k} = \infty$$ (chuỗi điều hòa) và $$\sum_{k=1}^{\infty} \frac{1}{k^2} < \infty$$ (bài toán Basel)</strong><br>
                Đây là ví dụ cổ điển của step size thỏa mãn điều kiện Robbins-Monro.
            </div>
        </div>

        <!-- Câu hỏi 7: Convergence rate -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Tốc độ hội tụ của subgradient method với diminishing step size là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(O(1/k)\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(O(1/\sqrt{k})\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(O(e^{-k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$O(1/\sqrt{k})$$</strong><br>
                Subgradient method có tốc độ hội tụ $$O(1/\sqrt{k})$$, chậm hơn gradient descent $$O(1/k)$$.
            </div>
        </div>

        <!-- Câu hỏi 8: Basic inequality -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Bất đẳng thức cơ bản trong phân tích subgradient method là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\|x^{(k)} - x^*\|^2 \leq \|x^{(k-1)} - x^*\|^2 - 2t_k(f(x^{(k-1)}) - f^*) + t_k^2\|g^{(k-1)}\|^2\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(\|x^{(k)} - x^*\|^2 \geq \|x^{(k-1)} - x^*\|^2\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(f(x^{(k)}) \leq f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(\|g^{(k)}\| \leq \|g^{(k-1)}\|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\|x^{(k)} - x^*\|^2 \leq \|x^{(k-1)} - x^*\|^2 - 2t_k(f(x^{(k-1)}) - f^*) + t_k^2\|g^{(k-1)}\|^2$$</strong><br>
                Đây là bất đẳng thức cơ bản dùng để phân tích hội tụ, cân bằng giữa tiến bộ và nhiễu.
            </div>
        </div>

        <!-- Câu hỏi 9: Polyak step size -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Polyak step size được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(t_k = \frac{1}{k}\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(t_k = \frac{f(x^{(k-1)}) - f^*}{\|g^{(k-1)}\|^2}\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(t_k = \text{constant}\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(t_k = \frac{1}{\|g^{(k-1)}\|}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$t_k = \frac{f(x^{(k-1)}) - f^*}{\|g^{(k-1)}\|^2}$$</strong><br>
                Polyak step size yêu cầu biết giá trị tối ưu $$f^*$$ và thường cho kết quả tốt trong thực tế.
            </div>
        </div>

        <!-- Câu hỏi 10: Projected subgradient method -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Projected subgradient method cho bài toán có ràng buộc \(\min_{x \in C} f(x)\) có công thức:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(x^{(k)} = x^{(k-1)} - t_k g^{(k-1)}\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(x^{(k)} = P_C(x^{(k-1)} - t_k g^{(k-1)})\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(x^{(k)} = x^{(k-1)} - t_k P_C(g^{(k-1)})\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(x^{(k)} = P_C(x^{(k-1)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$x^{(k)} = P_C(x^{(k-1)} - t_k g^{(k-1)})$$</strong><br>
                Projected subgradient method thực hiện bước subgradient rồi chiếu kết quả về tập ràng buộc $$C$$.
            </div>
        </div>

        <!-- Câu hỏi 11: Stochastic subgradient -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Stochastic subgradient method cho bài toán \(\min \sum_{i=1}^m f_i(x)\) có công thức:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(x^{(k)} = x^{(k-1)} - t_k \sum_{i=1}^m g_i^{(k-1)}\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(x^{(k)} = x^{(k-1)} - t_k g_{i_k}^{(k-1)}\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(x^{(k)} = x^{(k-1)} - t_k \frac{1}{m} \sum_{i=1}^m g_i^{(k-1)}\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(x^{(k)} = x^{(k-1)} - g_{i_k}^{(k-1)}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$x^{(k)} = x^{(k-1)} - t_k g_{i_k}^{(k-1)}$$</strong><br>
                Stochastic version chỉ sử dụng subgradient của một hàm $$f_{i_k}$$ được chọn tại mỗi iteration.
            </div>
        </div>

        <!-- Câu hỏi 12: Advantage of stochastic -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Ưu điểm chính của stochastic subgradient method là:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Hội tụ nhanh hơn batch method</label>
                <label><input type="radio" name="q12" value="b"> B) Chi phí tính toán thấp hơn mỗi iteration</label>
                <label><input type="radio" name="q12" value="c"> C) Luôn giảm giá trị hàm số</label>
                <label><input type="radio" name="q12" value="d"> D) Không cần step size</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Chi phí tính toán thấp hơn mỗi iteration</strong><br>
                Stochastic method chỉ cần tính subgradient của một hàm thay vì tổng tất cả, giảm đáng kể chi phí tính toán.
            </div>
        </div>

        <!-- Câu hỏi 13: Convergence comparison -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: So với gradient descent, subgradient method:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Hội tụ nhanh hơn</label>
                <label><input type="radio" name="q13" value="b"> B) Hội tụ chậm hơn</label>
                <label><input type="radio" name="q13" value="c"> C) Có cùng tốc độ hội tụ</label>
                <label><input type="radio" name="q13" value="d"> D) Không hội tụ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Hội tụ chậm hơn</strong><br>
                Subgradient method có tốc độ $$O(1/\sqrt{k})$$ so với $$O(1/k)$$ của gradient descent, nhưng áp dụng được cho hàm không khả vi.
            </div>
        </div>

        <!-- Câu hỏi 14: When to use subgradient -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Subgradient method được sử dụng khi:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Hàm mục tiêu khả vi mọi nơi</label>
                <label><input type="radio" name="q14" value="b"> B) Hàm mục tiêu lồi nhưng có thể không khả vi</label>
                <label><input type="radio" name="q14" value="c"> C) Hàm mục tiêu không lồi</label>
                <label><input type="radio" name="q14" value="d"> D) Chỉ cho bài toán không ràng buộc</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Hàm mục tiêu lồi nhưng có thể không khả vi</strong><br>
                Subgradient method được thiết kế đặc biệt cho các hàm lồi không khả vi như norm L1, max function.
            </div>
        </div>

        <!-- Câu hỏi 15: Step size adaptation -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Khác với gradient descent, step size trong subgradient method:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Có thể sử dụng backtracking line search</label>
                <label><input type="radio" name="q15" value="b"> B) Phải được thiết lập trước, không thích ứng</label>
                <label><input type="radio" name="q15" value="c"> C) Luôn bằng 1</label>
                <label><input type="radio" name="q15" value="d"> D) Tự động tối ưu</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Phải được thiết lập trước, không thích ứng</strong><br>
                Subgradient method không thể sử dụng line search vì không đảm bảo descent direction.
            </div>
        </div>

        <!-- Câu hỏi 16: Subgradient bound -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Trong phân tích hội tụ, thường giả sử subgradient bị chặn:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(\|g^{(k)}\| \leq G\) với \(G > 0\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(\|g^{(k)}\| = 1\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(\|g^{(k)}\| \to 0\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(\|g^{(k)}\|\) không bị chặn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\|g^{(k)}\| \leq G$$ với $$G > 0$$</strong><br>
                Giả sử subgradient bị chặn là cần thiết để đảm bảo hội tụ và ước lượng tốc độ hội tụ.
            </div>
        </div>

        <!-- Câu hỏi 17: Intersection of sets -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Để tìm giao của các tập lồi \(C_1 \cap C_2 \cap ... \cap C_m\), ta có thể sử dụng:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Gradient descent</label>
                <label><input type="radio" name="q17" value="b"> B) Projected subgradient method với hàm chỉ thị</label>
                <label><input type="radio" name="q17" value="c"> C) Newton method</label>
                <label><input type="radio" name="q17" value="d"> D) Không thể giải được</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Projected subgradient method với hàm chỉ thị</strong><br>
                Có thể tối ưu hóa tổng các hàm chỉ thị $$\sum I_{C_i}(x)$$ để tìm giao của các tập.
            </div>
        </div>

        <!-- Câu hỏi 18: Regularized problems -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Subgradient method thích hợp cho bài toán regularized như:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) \(\min f(x) + \lambda \|x\|_2^2\)</label>
                <label><input type="radio" name="q18" value="b"> B) \(\min f(x) + \lambda \|x\|_1\)</label>
                <label><input type="radio" name="q18" value="c"> C) \(\min f(x) + \lambda x^T x\)</label>
                <label><input type="radio" name="q18" value="d"> D) Tất cả các trường hợp trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\min f(x) + \lambda \|x\|_1$$</strong><br>
                L1 regularization tạo ra hàm không khả vi, phù hợp với subgradient method. L2 regularization vẫn khả vi.
            </div>
        </div>

        <!-- Câu hỏi 19: Batch vs stochastic -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Trong stochastic subgradient method, việc chọn index \(i_k\):</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Phải hoàn toàn ngẫu nhiên</label>
                <label><input type="radio" name="q19" value="b"> B) Có thể tuần hoàn hoặc ngẫu nhiên</label>
                <label><input type="radio" name="q19" value="c"> C) Phải theo thứ tự tăng dần</label>
                <label><input type="radio" name="q19" value="d"> D) Không ảnh hưởng đến hội tụ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Có thể tuần hoàn hoặc ngẫu nhiên</strong><br>
                Cả hai cách chọn tuần hoàn và ngẫu nhiên đều có thể đảm bảo hội tụ với điều kiện thích hợp.
            </div>
        </div>

        <!-- Câu hỏi 20: Practical considerations -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Trong thực tế, để cải thiện hiệu suất của subgradient method, ta có thể:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Sử dụng averaging của các iterate</label>
                <label><input type="radio" name="q20" value="b"> B) Kết hợp với momentum</label>
                <label><input type="radio" name="q20" value="c"> C) Sử dụng adaptive step size</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các phương pháp trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các phương pháp trên</strong><br>
                Averaging, momentum, và adaptive step size đều là các kỹ thuật được sử dụng để cải thiện subgradient method.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Subgradient method có tốc độ hội tụ:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$O(1/k)$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$O(1/\sqrt{k})$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$O(1/k^2)$$</label>
                <label><input type="radio" name="q21" value="d"> D) Tuyến tính</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$O(1/\sqrt{k})$$</strong><br>
                Subgradient method có tốc độ hội tụ $$O(1/\sqrt{k})$$ cho hàm lồi không trơn.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Kích thước bước trong subgradient method thường chọn:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Cố định nhỏ</label>
                <label><input type="radio" name="q22" value="b"> B) Giảm dần theo $$1/\sqrt{k}$$</label>
                <label><input type="radio" name="q22" value="c"> C) Tăng dần</label>
                <label><input type="radio" name="q22" value="d"> D) Ngẫu nhiên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Giảm dần theo $$1/\sqrt{k}$$</strong><br>
                Kích thước bước thường chọn $$t_k = \frac{c}{\sqrt{k}}$$ để đảm bảo hội tụ.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Với hàm $$f(x) = |x|$$, từ $$x_0 = 2$$, một bước subgradient với $$t = 0.5$$ cho:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$x_1 = 1.5$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$x_1 = 2.5$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$x_1 = 1$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$x_1 = 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x_1 = 1.5$$</strong><br>
                Tại $$x_0 = 2$$: subgradient là $$g = 1$$. $$x_1 = 2 - 0.5 \cdot 1 = 1.5$$.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Subgradient method khác gradient descent ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Không cần hàm khả vi</label>
                <label><input type="radio" name="q24" value="b"> B) Hội tụ chậm hơn</label>
                <label><input type="radio" name="q24" value="c"> C) Có thể dao động</label>
                <label><input type="radio" name="q24" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Subgradient method áp dụng cho hàm không trơn, hội tụ chậm hơn và có thể dao động quanh nghiệm.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Điều kiện dừng trong subgradient method thường dựa vào:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$\|g_k\| < \epsilon$$</label>
                <label><input type="radio" name="q25" value="b"> B) Số lần lặp tối đa</label>
                <label><input type="radio" name="q25" value="c"> C) Giá trị hàm mục tiêu</label>
                <label><input type="radio" name="q25" value="d"> D) B và C</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) B và C</strong><br>
                Do subgradient có thể không bằng 0 tại nghiệm, thường dùng số lần lặp hoặc giá trị hàm để dừng.
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
    q1: 'b', q2: 'b', q3: 'b', q4: 'b', q5: 'b',
    q6: 'a', q7: 'c', q8: 'a', q9: 'b', q10: 'b',
    q11: 'b', q12: 'b', q13: 'b', q14: 'b', q15: 'b',
    q16: 'a', q17: 'b', q18: 'b', q19: 'b', q20: 'd'
,
    q21: 'b', q22: 'b', q23: 'a', q24: 'd', q25: 'd'};

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
        message = '🌟 Xuất sắc! Bạn đã nắm vững subgradient method!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu khá tốt về thuật toán và phân tích hội tụ.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại step size choices và stochastic methods.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Hãy ôn lại các khái niệm cơ bản về subgradient.';
    } else {
        message = '📖 Hãy học lại từ đầu về subgradient method nhé!';
    }
    
    document.getElementById('performance-message').textContent = message;
    
    // Ẩn nút submit, hiện nút reset
    document.getElementById('submit-btn').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'inline-block';
    
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
        MathJax.typesetPromise();
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

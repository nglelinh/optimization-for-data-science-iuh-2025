---
layout: post
title: 11-06 Bài tập trắc nghiệm - Tính Đối Ngẫu trong Chương Trình Tổng Quát
chapter: '11'
order: 7
owner: GitHub Copilot
lang: vi
categories:
- chapter11
lesson_type: quiz
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Tính Đối Ngẫu Tổng Quát (General Duality)**

#### **Bài toán tối ưu tổng quát**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad l_j(x) = 0$$

với:
- $$f(x)$$: hàm mục tiêu (không nhất thiết lồi)
- $$h_i(x) \le 0$$: ràng buộc bất đẳng thức ($$i = 1,\ldots,m$$)
- $$l_j(x) = 0$$: ràng buộc đẳng thức ($$j = 1,\ldots,r$$)

#### **Mở rộng từ LP Duality**
- **LP Duality (Chương 10):** Chỉ áp dụng cho linear programs
- **General Duality (Chương 11):** Áp dụng cho **mọi** bài toán tối ưu
- **Công cụ chính:** Lagrangian function thay vì linear combination

### 📏 **Hàm Lagrangian**

#### **Định nghĩa**
$$L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x)$$

với:
- $$u \in \mathbb{R}^m, u \ge 0$$: dual variables cho inequality constraints
- $$v \in \mathbb{R}^r$$: dual variables cho equality constraints (không ràng buộc dấu)

#### **Tính chất cơ bản**
Với mọi $$x$$ khả thi và mọi $$u \ge 0, v$$:
$$L(x,u,v) = f(x) + \sum_{i=1}^m u_i \underbrace{h_i(x)}_{\le 0} + \sum_{j=1}^r v_j \underbrace{l_j(x)}_{= 0} \le f(x)$$

**Ý nghĩa:** Lagrangian cung cấp **lower bound** cho $$f(x)$$ tại mọi feasible point.

#### **Geometric interpretation**
- **Primal problem:** Tìm minimum trực tiếp trong feasible region
- **Lagrangian:** "Penalty method" - thêm penalty cho constraint violations
- **Dual variables:** "Prices" cho việc vi phạm constraints

### 🎯 **Hàm Đối Ngẫu Lagrange (Lagrange Dual Function)**

#### **Định nghĩa**
$$g(u,v) = \min_x L(x,u,v) = \min_x \left\{ f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x) \right\}$$

#### **Tính chất quan trọng**
1. **Lower bound:** $$g(u,v) \le f^*$$ với mọi $$u \ge 0, v$$ (weak duality)
2. **Concavity:** $$g(u,v)$$ là hàm **lõm** theo $$(u,v)$$
3. **Không phụ thuộc convexity:** $$g$$ lõm ngay cả khi $$f$$ không lồi

#### **Chứng minh concavity**
$$g(u,v) = \min_x L(x,u,v) = -\max_x \{-L(x,u,v)\}$$

Vì $$-L(x,u,v)$$ là **convex** theo $$(u,v)$$ (linear), nên $$\max_x$$ của convex functions là convex, do đó $$g(u,v)$$ là concave.

### 📊 **Bài Toán Đối Ngẫu Lagrange**

#### **Định nghĩa**
$$\max_{u,v} g(u,v) \quad \text{s.t.} \quad u \ge 0$$

**Mục tiêu:** Tìm **best lower bound** cho $$f^*$$

#### **Tính chất đặc biệt**
1. **Luôn là convex problem:** Maximize concave function over convex set
2. **Không phụ thuộc primal:** Dual luôn convex ngay cả khi primal non-convex
3. **Computational advantage:** Có thể dễ giải hơn primal

#### **Weak Duality**
**Luôn đúng:** $$g^* \le f^*$$ (dual optimal ≤ primal optimal)

**Duality gap:** $$f^* - g^* \ge 0$$

### 🔄 **Ví Dụ: Quadratic Programming**

#### **Bài toán**
$$\min_x \frac{1}{2}x^T Q x + c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

#### **Trường hợp 1: $$Q \succ 0$$ (positive definite)**

**Lagrangian:**
$$L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^T x + v^T(Ax - b)$$

**Tối ưu hóa theo $$x$$:**
$$\nabla_x L = Qx + c - u + A^T v = 0$$
$$\Rightarrow x^* = Q^{-1}(u - c - A^T v)$$

**Dual function:**
$$g(u,v) = -\frac{1}{2}(c - u + A^T v)^T Q^{-1}(c - u + A^T v) - b^T v$$

#### **Trường hợp 2: $$Q \succeq 0$$ (positive semidefinite)**

**Dual function:**
$$g(u,v) = \begin{cases}
-\frac{1}{2}(c - u + A^T v)^T Q^+(c - u + A^T v) - b^T v & \text{if } c - u + A^T v \perp \text{null}(Q) \\
-\infty & \text{otherwise}
\end{cases}$$

với $$Q^+$$ là Moore-Penrose pseudoinverse.

### 💪 **Strong Duality**

#### **Định nghĩa**
**Strong duality xảy ra khi:** $$f^* = g^*$$ (duality gap = 0)

#### **Slater's Condition**
**Điều kiện đủ cho strong duality:**

Nếu bài toán primal là **convex** và tồn tại $$x$$ **strictly feasible**:
$$h_i(x) < 0 \quad \forall i, \quad l_j(x) = 0 \quad \forall j$$

**Lưu ý:** Strict inequality không cần thiết cho affine constraints.

#### **Ý nghĩa của Strong Duality**
- **Perfect correspondence:** Primal và dual có cùng optimal value
- **Computational:** Có thể giải dual thay vì primal
- **Theoretical:** Enables KKT conditions (Chương 12)

### 🎯 **Ví Dụ: Support Vector Machine (SVM)**

#### **Primal problem**
$$\min_{\beta,\beta_0,\xi} \frac{1}{2}\|\beta\|_2^2 + C\sum_{i=1}^n \xi_i$$
$$\text{s.t.} \quad \xi_i \ge 0, \quad y_i(x_i^T\beta + \beta_0) \ge 1 - \xi_i$$

#### **Lagrangian**
$$L(\beta,\beta_0,\xi,v,w) = \frac{1}{2}\|\beta\|_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i + \sum_{i=1}^n w_i(1 - \xi_i - y_i(x_i^T\beta + \beta_0))$$

#### **Dual problem** (sau khi eliminate primal variables)
$$\max_w -\frac{1}{2}w^T \tilde{X}\tilde{X}^T w + \mathbf{1}^T w$$
$$\text{s.t.} \quad 0 \le w \le C\mathbf{1}, \quad w^T y = 0$$

với $$\tilde{X} = \text{diag}(y)X$$

**Strong duality:** Slater's condition thỏa mãn → $$f^* = g^*$$

### 📐 **Duality Gap**

#### **Định nghĩa**
Cho $$x$$ khả thi primal và $$(u,v)$$ khả thi dual:
$$\text{Duality gap} = f(x) - g(u,v)$$

#### **Tính chất**
1. **Upper bound cho suboptimality:** $$f(x) - f^* \le f(x) - g(u,v)$$
2. **Stopping criterion:** Nếu $$f(x) - g(u,v) \le \epsilon$$ thì $$f(x) - f^* \le \epsilon$$
3. **Optimality test:** $$f(x) - g(u,v) = 0 \Leftrightarrow x, (u,v)$$ optimal

#### **Ứng dụng trong algorithms**
- **Primal-dual methods:** Simultaneously update primal và dual variables
- **Convergence monitoring:** Track duality gap thay vì objective values
- **Early stopping:** Stop khi duality gap đủ nhỏ

### 🔄 **So Sánh LP Duality vs General Duality**

| **Aspect** | **LP Duality (Ch 10)** | **General Duality (Ch 11)** |
|------------|------------------------|------------------------------|
| **Scope** | Linear programs only | Any optimization problem |
| **Method** | Linear combination of constraints | Lagrangian function |
| **Dual convexity** | Always convex (LP) | Always convex (concave $$g$$) |
| **Strong duality** | If one feasible → strong duality | Slater's condition needed |
| **Applications** | LP, network flows, games | SVM, QP, general constrained |

### 🛠️ **Kỹ Thuật Thực Hành**

#### **Xây dựng dual problem:**
1. **Write Lagrangian:** $$L(x,u,v) = f(x) + u^T h(x) + v^T l(x)$$
2. **Minimize over $$x$$:** $$g(u,v) = \min_x L(x,u,v)$$
3. **Solve optimization:** $$\nabla_x L = 0$$ (nếu unconstrained)
4. **Substitute back:** Get $$g(u,v)$$ explicitly
5. **Maximize $$g$$:** Subject to $$u \ge 0$$

#### **Kiểm tra strong duality:**
1. **Verify convexity:** Primal problem convex?
2. **Check Slater's condition:** Strictly feasible point exists?
3. **Special cases:** LP, QP với $$Q \succ 0$$, etc.

#### **Computational strategies:**
- **Dual easier:** Khi dual có fewer variables hoặc simpler structure
- **Primal-dual methods:** Update both simultaneously
- **Duality gap monitoring:** For convergence assessment

### 💡 **Ví Dụ Minh Họa**

#### **Bài toán đơn giản:**
$$\min_x x^2 \quad \text{s.t.} \quad x \ge 1$$

**Lagrangian:**
$$L(x,u) = x^2 - u(x - 1) = x^2 - ux + u$$

**Minimize over $$x$$:**
$$\frac{\partial L}{\partial x} = 2x - u = 0 \Rightarrow x = \frac{u}{2}$$

**Dual function:**
$$g(u) = L\left(\frac{u}{2}, u\right) = \frac{u^2}{4} - u \cdot \frac{u}{2} + u = -\frac{u^2}{4} + u$$

**Dual problem:**
$$\max_u -\frac{u^2}{4} + u \quad \text{s.t.} \quad u \ge 0$$

**Solution:** $$u^* = 2$$, $$g^* = 1$$, $$x^* = 1$$, $$f^* = 1$$

**Strong duality:** $$f^* = g^* = 1$$ ✓

### 🎯 **Kết Nối Với Các Chương**

#### **Từ chương trước:**
- **Chương 10:** LP duality như special case
- **Chương 09:** Proximal gradient cho composite problems
- **Chương 05:** QP như canonical problem

#### **Tầm quan trọng của General Duality:**
- **Theoretical foundation:** Cho modern optimization theory
- **KKT conditions:** Optimality conditions (Chương 12)
- **Algorithms:** Primal-dual methods, interior point
- **Machine learning:** SVM, neural networks, regularization

#### **Hướng phát triển:**
- **Chương 12:** KKT conditions và complementary slackness
- **Advanced topics:** Robust optimization, semidefinite programming
- **Applications:** Deep learning, reinforcement learning

### 🌟 **Ý Nghĩa Lý Thuyết**

#### **Duality như universal principle:**
- **Mọi optimization problem** có dual perspective
- **Dual luôn convex** ngay cả khi primal non-convex
- **Provides bounds** và **optimality conditions**
- **Enables algorithms** không thể có với primal alone

#### **Geometric interpretation:**
- **Primal:** Direct search trong feasible region
- **Dual:** Indirect approach qua "supporting hyperplanes"
- **Strong duality:** Perfect geometric correspondence

#### **Computational significance:**
- **Alternative solution path:** Dual có thể easier than primal
- **Parallel computation:** Primal-dual methods
- **Convergence monitoring:** Duality gap như stopping criterion

### 💡 **Mẹo Thực Hành**

#### **Khi nào sử dụng duality:**
1. **Primal khó giải:** Many variables, complex constraints
2. **Dual structure simpler:** Fewer dual variables
3. **Bounds needed:** Duality gap cho convergence assessment
4. **Theoretical analysis:** Optimality conditions, sensitivity

#### **Common pitfalls:**
- **Forget constraint qualifications:** Slater's condition
- **Wrong sign conventions:** $$u \ge 0$$ cho $$h(x) \le 0$$
- **Non-convex primal:** Strong duality không guaranteed
- **Computational issues:** Dual có thể numerically unstable

#### **Debugging strategies:**
- **Verify weak duality:** $$g^* \le f^*$$ luôn đúng
- **Check Slater's condition:** For strong duality
- **Compare với known results:** LP, QP special cases
- **Numerical verification:** Small examples

### 🔬 **Advanced Topics**

#### **Fenchel duality:**
- **Conjugate functions:** Alternative duality framework
- **Applications:** Convex analysis, variational problems

#### **Conic duality:**
- **Semidefinite programming:** Matrix optimization
- **Second-order cone programming:** Robust optimization

#### **Stochastic duality:**
- **Robust optimization:** Worst-case analysis
- **Chance constraints:** Probabilistic optimization

---

💡 **Mẹo:** General Duality là **paradigm shift** từ "giải bài toán trực tiếp" sang "tìm best bound và exploit structure". Đây là foundation cho toàn bộ modern optimization theory!

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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về tính đối ngẫu trong quy hoạch tổng quát, bao gồm Lagrangian, dual function, strong duality, Slater condition và KKT conditions.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🎯 Quiz: Tính Đối Ngẫu trong Chương Trình Tổng Quát</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Lagrangian definition -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Cho bài toán \(\min f(x)\) s.t. \(h_i(x) \leq 0, l_j(x) = 0\). Lagrangian được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(L(x,u,v) = f(x) - \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(L(x,u,v) = f(x) + \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(L(x,u,v) = f(x) - \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)$$</strong><br>
                Lagrangian kết hợp objective function với penalty terms cho constraints, với $$u_i \geq 0$$ cho inequality constraints.
            </div>
        </div>

        <!-- Câu hỏi 2: Dual variables constraints -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Trong Lagrangian, dual variables phải thỏa mãn:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(u \geq 0, v\) không ràng buộc</label>
                <label><input type="radio" name="q2" value="b"> B) \(u\) không ràng buộc, \(v \geq 0\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(u \geq 0, v \geq 0\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(u\) và \(v\) đều không ràng buộc</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$u \geq 0, v$$ không ràng buộc</strong><br>
                Dual variables $$u_i$$ cho inequality constraints phải non-negative, $$v_j$$ cho equality constraints không có ràng buộc dấu.
            </div>
        </div>

        <!-- Câu hỏi 3: Lagrange dual function -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Lagrange dual function \(g(u,v)\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(g(u,v) = \max_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(g(u,v) = \min_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(g(u,v) = L(x^*,u,v)\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(g(u,v) = \nabla_x L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$g(u,v) = \min_x L(x,u,v)$$</strong><br>
                Dual function là infimum của Lagrangian over primal variables $$x$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Weak duality -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Weak duality theorem phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) \(g(u,v) \geq f^*\) với mọi \(u \geq 0, v\)</label>
                <label><input type="radio" name="q4" value="b"> B) \(g(u,v) \leq f^*\) với mọi \(u \geq 0, v\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(g(u,v) = f^*\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(g(u,v) > f^*\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$g(u,v) \leq f^*$$ với mọi $$u \geq 0, v$$</strong><br>
                Dual function cung cấp lower bound cho primal optimal value: $$g^* \leq f^*$$.
            </div>
        </div>

        <!-- Câu hỏi 5: Dual problem -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Lagrange dual problem là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(\min_{u \geq 0, v} g(u,v)\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(\max_{u \geq 0, v} g(u,v)\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(\min_{u, v \geq 0} g(u,v)\)</label>
                <label><input type="radio" name="q5" value="d"> D) \(\max_{u, v} g(u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\max_{u \geq 0, v} g(u,v)$$</strong><br>
                Dual problem tối đa hóa dual function để tìm best lower bound cho primal problem.
            </div>
        </div>

        <!-- Câu hỏi 6: Strong duality -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Strong duality xảy ra khi:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(f^* > g^*\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(f^* = g^*\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(f^* < g^*\)</label>
                <label><input type="radio" name="q6" value="d"> D) Duality gap > 0</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$f^* = g^*$$</strong><br>
                Strong duality có nghĩa là không có duality gap: primal và dual optimal values bằng nhau.
            </div>
        </div>

        <!-- Câu hỏi 7: Slater condition -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Slater condition yêu cầu:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Tồn tại \(x\) sao cho \(h_i(x) \leq 0, l_j(x) = 0\)</label>
                <label><input type="radio" name="q7" value="b"> B) Tồn tại \(x\) sao cho \(h_i(x) < 0, l_j(x) = 0\) (strictly feasible)</label>
                <label><input type="radio" name="q7" value="c"> C) Tồn tại \(x\) sao cho \(h_i(x) = 0, l_j(x) = 0\)</label>
                <label><input type="radio" name="q7" value="d"> D) Tất cả constraints đều active</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tồn tại $$x$$ sao cho $$h_i(x) < 0, l_j(x) = 0$$ (strictly feasible)</strong><br>
                Slater condition yêu cầu tồn tại điểm strictly feasible (interior point) để đảm bảo strong duality.
            </div>
        </div>

        <!-- Câu hỏi 8: Duality gap -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Duality gap được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(g^* - f^*\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(f^* - g^*\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(|f^* - g^*|\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(f^* + g^*\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$f^* - g^*$$</strong><br>
                Duality gap là hiệu số giữa primal và dual optimal values, luôn non-negative do weak duality.
            </div>
        </div>

        <!-- Câu hỏi 9: KKT stationarity -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: KKT stationarity condition là:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\nabla f(x^*) + \sum u_i^* \nabla h_i(x^*) + \sum v_j^* \nabla l_j(x^*) = 0\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\nabla f(x^*) = 0\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(u_i^* h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(h_i(x^*) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\nabla f(x^*) + \sum u_i^* \nabla h_i(x^*) + \sum v_j^* \nabla l_j(x^*) = 0$$</strong><br>
                Stationarity: gradient của Lagrangian theo $$x$$ bằng 0 tại optimal point.
            </div>
        </div>

        <!-- Câu hỏi 10: KKT complementary slackness -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: KKT complementary slackness condition là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(u_i^* \geq 0\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(h_i(x^*) \leq 0\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(u_i^* h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(l_j(x^*) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$u_i^* h_i(x^*) = 0$$</strong><br>
                Complementary slackness: nếu constraint không active thì dual variable = 0, nếu dual variable > 0 thì constraint active.
            </div>
        </div>

        <!-- Câu hỏi 11: KKT conditions sufficiency -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: KKT conditions là điều kiện đủ cho optimality khi:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Bài toán là convex</label>
                <label><input type="radio" name="q11" value="b"> B) Bài toán là non-convex</label>
                <label><input type="radio" name="q11" value="c"> C) Luôn luôn</label>
                <label><input type="radio" name="q11" value="d"> D) Không bao giờ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Bài toán là convex</strong><br>
                KKT conditions là necessary cho mọi bài toán (với constraint qualification), nhưng chỉ sufficient khi bài toán convex.
            </div>
        </div>

        <!-- Câu hỏi 12: Dual function properties -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Dual function \(g(u,v)\) có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Luôn concave</label>
                <label><input type="radio" name="q12" value="b"> B) Luôn convex</label>
                <label><input type="radio" name="q12" value="c"> C) Có thể không concave hoặc convex</label>
                <label><input type="radio" name="q12" value="d"> D) Luôn linear</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn concave</strong><br>
                Dual function luôn concave vì là pointwise minimum của linear functions trong $$(u,v)$$.
            </div>
        </div>

        <!-- Câu hỏi 13: Constraint qualification -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Constraint qualification cần thiết để:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Đảm bảo KKT conditions là necessary</label>
                <label><input type="radio" name="q13" value="b"> B) Đảm bảo strong duality</label>
                <label><input type="radio" name="q13" value="c"> C) Đảm bảo convexity</label>
                <label><input type="radio" name="q13" value="d"> D) Đảm bảo uniqueness</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Đảm bảo KKT conditions là necessary</strong><br>
                Constraint qualification (như LICQ, MFCQ) đảm bảo KKT conditions là necessary conditions cho local optimality.
            </div>
        </div>

        <!-- Câu hỏi 14: SVM dual problem -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Trong SVM, dual problem có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Quadratic programming với linear constraints</label>
                <label><input type="radio" name="q14" value="b"> B) Linear programming</label>
                <label><input type="radio" name="q14" value="c"> C) Nonlinear programming</label>
                <label><input type="radio" name="q14" value="d"> D) Integer programming</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Quadratic programming với linear constraints</strong><br>
                SVM dual là QP problem: maximize quadratic objective subject to linear constraints và box constraints.
            </div>
        </div>

        <!-- Câu hỏi 15: Lagrangian saddle point -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Tại optimal point, Lagrangian có tính chất saddle point:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(L(x^*,u,v) \leq L(x^*,u^*,v^*) \leq L(x,u^*,v^*)\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(L(x^*,u,v) \geq L(x^*,u^*,v^*) \geq L(x,u^*,v^*)\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(L(x^*,u^*,v^*) = 0\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(L(x,u,v)\) là constant</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$L(x^*,u,v) \leq L(x^*,u^*,v^*) \leq L(x,u^*,v^*)$$</strong><br>
                Saddle point property: Lagrangian minimized over $$x$$ và maximized over $$(u,v)$$ tại optimal point.
            </div>
        </div>

        <!-- Câu hỏi 16: Convex optimization duality -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Trong convex optimization, nếu Slater condition thỏa mãn thì:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Weak duality holds</label>
                <label><input type="radio" name="q16" value="b"> B) Strong duality holds</label>
                <label><input type="radio" name="q16" value="c"> C) KKT conditions sufficient</label>
                <label><input type="radio" name="q16" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Với convex problem và Slater condition: weak duality luôn có, strong duality holds, KKT necessary và sufficient.
            </div>
        </div>

        <!-- Câu hỏi 17: Dual optimal solution -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Nếu \(x^*\) là primal optimal và \((u^*,v^*)\) là dual optimal với strong duality, thì:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(f(x^*) = g(u^*,v^*)\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(f(x^*) > g(u^*,v^*)\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(f(x^*) < g(u^*,v^*)\)</label>
                <label><input type="radio" name="q17" value="d"> D) Không thể xác định</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f(x^*) = g(u^*,v^*)$$</strong><br>
                Strong duality có nghĩa là primal và dual optimal values bằng nhau.
            </div>
        </div>

        <!-- Câu hỏi 18: Lagrangian relaxation -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Lagrangian relaxation được sử dụng để:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Tìm upper bound cho minimization problem</label>
                <label><input type="radio" name="q18" value="b"> B) Tìm lower bound cho minimization problem</label>
                <label><input type="radio" name="q18" value="c"> C) Giải chính xác bài toán gốc</label>
                <label><input type="radio" name="q18" value="d"> D) Chuyển đổi sang maximization</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tìm lower bound cho minimization problem</strong><br>
                Lagrangian relaxation "relax" constraints và cung cấp lower bound thông qua dual function.
            </div>
        </div>

        <!-- Câu hỏi 19: Geometric interpretation -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Về mặt hình học, duality gap bằng 0 có nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Feasible set rỗng</label>
                <label><input type="radio" name="q19" value="b"> B) Supporting hyperplane tách hoàn hảo epigraph và feasible set</label>
                <label><input type="radio" name="q19" value="c"> C) Bài toán unbounded</label>
                <label><input type="radio" name="q19" value="d"> D) Constraints redundant</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Supporting hyperplane tách hoàn hảo epigraph và feasible set</strong><br>
                Strong duality tương ứng với việc tồn tại supporting hyperplane tách epigraph của objective và feasible region.
            </div>
        </div>

        <!-- Câu hỏi 20: Applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Lagrangian duality có ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Machine learning (SVM, neural networks)</label>
                <label><input type="radio" name="q20" value="b"> B) Economics (utility maximization)</label>
                <label><input type="radio" name="q20" value="c"> C) Engineering (optimal control, signal processing)</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các lĩnh vực trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lĩnh vực trên</strong><br>
                Lagrangian duality là công cụ fundamental trong optimization với ứng dụng rộng rãi trong ML, economics, engineering và nhiều lĩnh vực khác.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Hàm đối ngẫu Lagrange $$g(\lambda, \nu)$$ được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$\inf_x L(x, \lambda, \nu)$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$\sup_x L(x, \lambda, \nu)$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$\nabla_x L(x, \lambda, \nu)$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$L(x^*, \lambda, \nu)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\inf_x L(x, \lambda, \nu)$$</strong><br>
                Hàm đối ngẫu Lagrange: $$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Đối ngẫu yếu khẳng định:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$g(\lambda, \nu) \leq p^*$$ với $$\lambda \geq 0$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$g(\lambda, \nu) \geq p^*$$ với $$\lambda \geq 0$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$g(\lambda, \nu) = p^*$$</label>
                <label><input type="radio" name="q22" value="d"> D) Không có mối quan hệ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$g(\lambda, \nu) \leq p^*$$ với $$\lambda \geq 0$$</strong><br>
                Đối ngẫu yếu: giá trị dual luôn là cận dưới của giá trị primal.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Duality gap bằng 0 khi:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Đối ngẫu mạnh thỏa mãn</label>
                <label><input type="radio" name="q23" value="b"> B) Bài toán lồi</label>
                <label><input type="radio" name="q23" value="c"> C) Slater condition thỏa mãn</label>
                <label><input type="radio" name="q23" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Duality gap = 0 khi có đối ngẫu mạnh, thường xảy ra với bài toán lồi và Slater condition.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Slater condition yêu cầu:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Tồn tại $$x$$ khả thi với $$g_i(x) < 0$$ (strict)</label>
                <label><input type="radio" name="q24" value="b"> B) Tồn tại $$x$$ với $$g_i(x) \leq 0$$</label>
                <label><input type="radio" name="q24" value="c"> C) Hàm mục tiêu lồi</label>
                <label><input type="radio" name="q24" value="d"> D) Ràng buộc tuyến tính</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tồn tại $$x$$ khả thi với $$g_i(x) < 0$$ (strict)</strong><br>
                Slater condition: tồn tại điểm strictly feasible $$x$$ với $$g_i(x) < 0$$ cho tất cả $$i$$.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Bài toán dual của $$\min f(x)$$ với $$g(x) \leq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$\max g(\lambda)$$ với $$\lambda \geq 0$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$\min g(\lambda)$$ với $$\lambda \geq 0$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$\max g(\lambda)$$ với $$\lambda \leq 0$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$\sup g(\lambda)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max g(\lambda)$$ với $$\lambda \geq 0$$</strong><br>
                Bài toán dual: $$\max_{\lambda \geq 0} g(\lambda)$$ với $$g(\lambda) = \inf_x L(x,\lambda)$$.
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
    q1: 'a', q2: 'a', q3: 'b', q4: 'b', q5: 'b',
    q6: 'b', q7: 'b', q8: 'b', q9: 'a', q10: 'c',
    q11: 'a', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'd', q17: 'a', q18: 'b', q19: 'b', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'd', q24: 'a', q25: 'a'};

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
        message = '🌟 Xuất sắc! Bạn đã thành thạo Lagrangian duality theory!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về KKT conditions và strong duality.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại Slater condition và complementary slackness.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại Lagrangian và dual function.';
    } else {
        message = '📖 Hãy học lại từ đầu về general duality theory nhé!';
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

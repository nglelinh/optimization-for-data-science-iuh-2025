---
layout: post
title: 12-07 Bài tập trắc nghiệm - Điều Kiện KKT
chapter: '12'
order: 8
owner: GitHub Copilot
lang: vi
categories:
- chapter12
lesson_type: quiz
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Điều Kiện Karush-Kuhn-Tucker (KKT)**

#### **Bài toán tối ưu tổng quát**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad l_j(x) = 0$$

với $$i = 1,\ldots,m$$ và $$j = 1,\ldots,r$$

#### **Bốn điều kiện KKT**
Cho nghiệm $$x^*, \lambda^*, \nu^*$$:

1. **Stationarity (Tính dừng):**
   $$0 \in \partial \left( f(x^*) + \sum_{i=1}^m \lambda_i^* h_i(x^*) + \sum_{j=1}^r \nu_j^* l_j(x^*) \right)$$

2. **Complementary Slackness (Bù yếu):**
   $$\lambda_i^* \cdot h_i(x^*) = 0 \quad \forall i$$

3. **Primal Feasibility (Tính khả thi nguyên thủy):**
   $$h_i(x^*) \le 0, \quad l_j(x^*) = 0 \quad \forall i,j$$

4. **Dual Feasibility (Tính khả thi đối ngẫu):**
   $$\lambda_i^* \ge 0 \quad \forall i$$

#### **Ý nghĩa các điều kiện**
- **Stationarity:** Gradient của Lagrangian bằng 0
- **Complementary slackness:** Hoặc constraint active ($$h_i = 0$$) hoặc dual variable = 0 ($$\lambda_i = 0$$)
- **Primal feasibility:** Thỏa mãn tất cả constraints của bài toán gốc
- **Dual feasibility:** Dual variables cho inequality constraints phải non-negative

### 📊 **Tính Đủ và Tính Cần Thiết**

#### **Tính đủ (Sufficiency)**
**Nếu** $$x^*, \lambda^*, \nu^*$$ thỏa mãn KKT conditions và bài toán **convex**, **thì** chúng là optimal solutions.

**Chứng minh:**
$$g(\lambda^*, \nu^*) = \min_x L(x, \lambda^*, \nu^*) = L(x^*, \lambda^*, \nu^*) = f(x^*)$$

Do đó: $$g(\lambda^*, \nu^*) = f(x^*)$$ ⟹ duality gap = 0 ⟹ optimal

#### **Tính cần thiết (Necessity)**
**Nếu** $$x^*, \lambda^*, \nu^*$$ là optimal solutions với **strong duality**, **thì** chúng thỏa mãn KKT conditions.

**Điều kiện:** Strong duality (ví dụ: Slater's condition)

#### **Tổng hợp**
Cho convex problems với strong duality:
$$x^*, \lambda^*, \nu^* \text{ optimal} \Leftrightarrow x^*, \lambda^*, \nu^* \text{ satisfy KKT}$$

### 🔄 **Ví Dụ: Quadratic Programming với Equality Constraints**

#### **Bài toán**
$$\min_x \frac{1}{2}x^T P x + q^T x + r \quad \text{s.t.} \quad Ax = b$$

với $$P \in \mathbb{S}_+^n$$ (positive semidefinite)

#### **KKT conditions**
- **Stationarity:** $$Px^* + q + A^T \nu^* = 0$$
- **Primal feasibility:** $$Ax^* = b$$
- **Complementary slackness:** Không có (no inequality constraints)
- **Dual feasibility:** Không có (no inequality constraints)

#### **Hệ Ma Trận KKT**
$$\begin{bmatrix} P & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x^* \\ \nu^* \end{bmatrix} = \begin{bmatrix} -q \\ b \end{bmatrix}$$

**Ý nghĩa:** Đây chính là **Newton step** cho constrained optimization!

### 🌊 **Ví Dụ: Water-Filling Algorithm**

#### **Bài toán**
$$\min_x -\sum_{i=1}^n \log(\alpha_i + x_i) \quad \text{s.t.} \quad x \succeq 0, \quad \mathbf{1}^T x = 1$$

với $$\alpha_i > 0$$

#### **KKT conditions**
- **Stationarity:** $$-\frac{1}{\alpha_i + x_i^*} - \lambda_i^* + \nu^* = 0$$
- **Complementary slackness:** $$\lambda_i^* x_i^* = 0$$
- **Primal feasibility:** $$x^* \succeq 0, \mathbf{1}^T x^* = 1$$
- **Dual feasibility:** $$\lambda^* \succeq 0$$

#### **Analytical solution**
$$x_i^* = \max\left\{0, \frac{1}{\nu^*} - \alpha_i\right\}$$

với $$\nu^*$$ được xác định từ: $$\sum_{i=1}^n \max\left\{0, \frac{1}{\nu^*} - \alpha_i\right\} = 1$$

#### **Water-filling interpretation**
- $$\alpha_i$$: "Ground level" của channel $$i$$
- $$\frac{1}{\nu^*}$$: "Water level" chung
- $$x_i^*$$: "Water depth" trong channel $$i$$
- **Thuật toán:** Đổ nước cho đến khi tổng volume = 1

### 🎯 **Ví Dụ: Support Vector Machine (SVM)**

#### **Primal problem**
$$\min_{\beta,\beta_0,\xi} \frac{1}{2}\|\beta\|_2^2 + C\sum_{i=1}^n \xi_i$$
$$\text{s.t.} \quad \xi_i \ge 0, \quad y_i(x_i^T\beta + \beta_0) \ge 1 - \xi_i$$

#### **KKT conditions**
- **Stationarity:**
  - $$\beta^* = \sum_{i=1}^n w_i^* y_i x_i$$
  - $$\sum_{i=1}^n w_i^* y_i = 0$$
  - $$w^* = C\mathbf{1} - v^*$$

- **Complementary slackness:**
  - $$v_i^* \xi_i^* = 0$$
  - $$w_i^* (1 - \xi_i^* - y_i(x_i^T\beta^* + \beta_0^*)) = 0$$

#### **Support vectors**
**Điểm $$i$$ là support vector** ⟺ $$w_i^* > 0$$

**Hai loại support vectors:**
- **On margin:** $$\xi_i^* = 0$$, $$w_i^* \in (0, C]$$
- **Inside margin:** $$\xi_i^* > 0$$, $$w_i^* = C$$

#### **Practical implications**
- **Sparsity:** Chỉ support vectors có $$w_i^* > 0$$
- **Efficiency:** Có thể filter non-support points trước khi optimize
- **Interpretation:** KKT conditions giải thích structure của SVM solution

### 🔄 **Constrained Form vs Lagrangian Form**

#### **Constrained form (C)**
$$\min_x f(x) \quad \text{s.t.} \quad h(x) \le t$$

#### **Lagrangian form (L)**
$$\min_x f(x) + \lambda h(x)$$

#### **Equivalence conditions**
**Khi nào (C) và (L) equivalent?**

1. **(C) → (L):** Nếu (C) thỏa mãn Slater + strong duality, tồn tại $$\lambda^* \ge 0$$ sao cho solution của (C) cũng là solution của (L)

2. **(L) → (C):** Nếu $$x^*$$ solve (L) và KKT conditions hold, thì $$x^*$$ cũng solve (C) với $$t = h(x^*)$$

#### **Perfect equivalence**
**Khi:** $$h(x) \ge 0$$ (như norm), $$t = 0$$, $$\lambda = \infty$$

**Kết quả:** Cả hai đều enforce $$h(x) = 0$$

### 🛠️ **Kỹ Thuật Thực Hành**

#### **Kiểm tra KKT conditions:**
1. **Verify stationarity:** $$\nabla_x L(x^*, \lambda^*, \nu^*) = 0$$
2. **Check complementary slackness:** $$\lambda_i^* h_i(x^*) = 0 \quad \forall i$$
3. **Verify feasibility:** Primal và dual constraints
4. **Confirm optimality:** Nếu convex + KKT ⟹ optimal

#### **Analytical solution strategy:**
1. **Write KKT conditions** cho specific problem
2. **Use complementary slackness** để identify active constraints
3. **Solve system of equations** từ stationarity + feasibility
4. **Verify solution** thỏa mãn tất cả KKT conditions

#### **Computational applications:**
- **Active set methods:** Identify active constraints iteratively
- **Interior point methods:** Follow central path satisfying KKT
- **Primal-dual methods:** Update primal và dual simultaneously

### 💡 **Ví Dụ Minh Họa**

#### **Bài toán đơn giản:**
$$\min_x x^2 + y^2 \quad \text{s.t.} \quad x + y = 1, \quad x \ge 0$$

**KKT conditions:**
- **Stationarity:** $$2x^* - \lambda^* + \nu^* = 0$$, $$2y^* + \nu^* = 0$$
- **Complementary slackness:** $$\lambda^* x^* = 0$$
- **Primal feasibility:** $$x^* + y^* = 1$$, $$x^* \ge 0$$
- **Dual feasibility:** $$\lambda^* \ge 0$$

**Case analysis:**
- **Case 1:** $$x^* > 0$$ ⟹ $$\lambda^* = 0$$ ⟹ $$x^* = y^* = 1/2$$
- **Case 2:** $$x^* = 0$$ ⟹ $$y^* = 1$$ ⟹ $$\lambda^* = 2$$

**Optimal solution:** $$x^* = 1/2, y^* = 1/2$$ (Case 1 gives smaller objective)

### 🎯 **Kết Nối Với Các Chương**

#### **Từ chương trước:**
- **Chương 11:** General duality theory - KKT là direct consequence
- **Chương 10:** LP duality - KKT generalizes optimality conditions
- **Chương 04:** First-order optimality conditions - KKT extends to constrained

#### **Tầm quan trọng của KKT:**
- **Optimality characterization:** Necessary và sufficient conditions
- **Algorithm design:** Active set, interior point, SQP methods
- **Theoretical analysis:** Sensitivity, perturbation theory
- **Machine learning:** SVM, regularization, constrained learning

#### **Hướng phát triển:**
- **Second-order conditions:** Bordered Hessian, LICQ, MFCQ
- **Nonlinear programming:** SQP, trust region methods
- **Variational inequalities:** Complementarity problems
- **Optimal control:** Pontryagin maximum principle

### 🌟 **Ý Nghĩa Lý Thuyết**

#### **KKT như universal optimality conditions:**
- **Unifies:** Unconstrained ($$\nabla f = 0$$) và constrained optimization
- **Characterizes:** Exactly when point is optimal
- **Enables:** Systematic algorithm design
- **Connects:** Primal và dual perspectives

#### **Geometric interpretation:**
- **Stationarity:** Gradient orthogonal to feasible directions
- **Complementary slackness:** Either constraint active hoặc multiplier zero
- **Feasibility:** Point lies in feasible region
- **Non-negativity:** Consistent với constraint directions

#### **Computational significance:**
- **Algorithm foundation:** Most constrained optimization algorithms
- **Convergence criteria:** KKT residual như stopping condition
- **Sensitivity analysis:** Dual variables như shadow prices
- **Problem structure:** Active set identification

### 💡 **Mẹo Thực Hành**

#### **Khi nào sử dụng KKT:**
1. **Analytical solutions:** Small problems với closed-form solutions
2. **Algorithm design:** Foundation cho numerical methods
3. **Optimality verification:** Check if candidate point optimal
4. **Sensitivity analysis:** Understand parameter changes

#### **Common pitfalls:**
- **Forget constraint qualifications:** LICQ, MFCQ for necessity
- **Wrong complementary slackness:** $$\lambda_i h_i = 0$$, not $$\lambda_i = 0$$ or $$h_i = 0$$
- **Non-convex problems:** KKT necessary but not sufficient
- **Numerical issues:** KKT matrix có thể ill-conditioned

#### **Debugging strategies:**
- **Check each condition separately:** Stationarity, slackness, feasibility
- **Verify constraint qualifications:** For necessity
- **Use geometric intuition:** Gradient orthogonality
- **Compare với known solutions:** Simple test cases

### 🔬 **Advanced Topics**

#### **Constraint qualifications:**
- **LICQ:** Linear Independence Constraint Qualification
- **MFCQ:** Mangasarian-Fromovitz Constraint Qualification
- **CPLD:** Constant Positive Linear Dependence
- **Applications:** When KKT conditions are necessary

#### **Second-order conditions:**
- **SOSC:** Second-Order Sufficient Conditions
- **Bordered Hessian:** For equality-constrained problems
- **Critical cone:** Directions of potential descent
- **Applications:** Algorithm convergence rates

#### **Variational inequalities:**
- **Complementarity problems:** Generalize KKT conditions
- **Nash equilibria:** Game theory applications
- **Contact mechanics:** Engineering applications

### 📈 **Ứng Dụng Thực Tế**

#### **Machine Learning:**
- **SVM:** Dual formulation và support vector identification
- **Regularization:** L1, L2 penalties via constrained formulation
- **Neural networks:** Constrained training, fairness constraints

#### **Engineering:**
- **Optimal control:** Pontryagin maximum principle
- **Signal processing:** Filter design, beamforming
- **Structural optimization:** Weight minimization với stress constraints

#### **Economics và Finance:**
- **Portfolio optimization:** Risk-return tradeoffs
- **Mechanism design:** Incentive compatibility
- **Resource allocation:** Utility maximization

#### **Operations Research:**
- **Production planning:** Capacity constraints
- **Supply chain:** Inventory optimization
- **Transportation:** Network flow problems

---

💡 **Mẹo:** KKT conditions là **crown jewel** của optimization theory - chúng provide exact characterization của optimality cho constrained problems và là foundation cho hầu hết modern optimization algorithms!

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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về điều kiện Karush-Kuhn-Tucker (KKT), bao gồm các ví dụ thực tế như SVM, water-filling algorithm, quadratic programming và L1 penalized problems.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>⚖️ Quiz: Điều Kiện KKT</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: KKT conditions components -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Điều kiện KKT bao gồm những thành phần nào?</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Chỉ stationarity và complementary slackness</label>
                <label><input type="radio" name="q1" value="b"> B) Stationarity, complementary slackness, primal feasibility, dual feasibility</label>
                <label><input type="radio" name="q1" value="c"> C) Chỉ primal và dual feasibility</label>
                <label><input type="radio" name="q1" value="d"> D) Chỉ stationarity</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Stationarity, complementary slackness, primal feasibility, dual feasibility</strong><br>
                KKT conditions gồm 4 thành phần: (1) Stationarity, (2) Complementary slackness, (3) Primal feasibility, (4) Dual feasibility.
            </div>
        </div>

        <!-- Câu hỏi 2: Stationarity condition -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Stationarity condition trong KKT có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\nabla f(x^*) = 0\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\nabla f(x^*) + \sum \lambda_i \nabla h_i(x^*) + \sum \nu_j \nabla l_j(x^*) = 0\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\lambda_i h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(h_i(x^*) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\nabla f(x^*) + \sum \lambda_i \nabla h_i(x^*) + \sum \nu_j \nabla l_j(x^*) = 0$$</strong><br>
                Stationarity: gradient của Lagrangian theo $$x$$ bằng 0, tức là gradient của objective cân bằng với tổ hợp tuyến tính của gradients của constraints.
            </div>
        </div>

        <!-- Câu hỏi 3: Complementary slackness -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Complementary slackness condition phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(\lambda_i h_i(x^*) = 0\) với mọi \(i\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\lambda_i = 0\) hoặc \(h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q3" value="c"> C) Nếu \(h_i(x^*) < 0\) thì \(\lambda_i = 0\)</label>
                <label><input type="radio" name="q3" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Complementary slackness có thể phát biểu theo nhiều cách tương đương: $$\lambda_i h_i(x^*) = 0$$, hoặc $$\lambda_i = 0$$ hoặc $$h_i(x^*) = 0$$, hoặc inactive constraints có dual variable = 0.
            </div>
        </div>

        <!-- Câu hỏi 4: KKT sufficiency -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: KKT conditions là điều kiện đủ cho global optimality khi:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Bài toán là convex</label>
                <label><input type="radio" name="q4" value="b"> B) Bài toán là non-convex</label>
                <label><input type="radio" name="q4" value="c"> C) Luôn luôn</label>
                <label><input type="radio" name="q4" value="d"> D) Không bao giờ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Bài toán là convex</strong><br>
                KKT conditions là necessary (với constraint qualification) cho mọi bài toán, nhưng chỉ sufficient cho global optimality khi bài toán convex.
            </div>
        </div>

        <!-- Câu hỏi 5: Active constraints -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Constraint \(h_i(x) \leq 0\) được gọi là active tại \(x^*\) khi:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(h_i(x^*) < 0\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(\lambda_i > 0\)</label>
                <label><input type="radio" name="q5" value="d"> D) \(\lambda_i = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$h_i(x^*) = 0$$</strong><br>
                Constraint active có nghĩa là nó được thỏa mãn với dấu bằng tại optimal point.
            </div>
        </div>

        <!-- Câu hỏi 6: Quadratic programming KKT -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Trong quadratic programming \(\min \frac{1}{2}x^T Q x + c^T x\) s.t. \(Ax = b\), stationarity condition là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(Qx^* + c = 0\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(Qx^* + c + A^T \nu^* = 0\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(Ax^* = b\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\nu^* = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$Qx^* + c + A^T \nu^* = 0$$</strong><br>
                Stationarity: $$\nabla f(x^*) + A^T \nu^* = Qx^* + c + A^T \nu^* = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 7: Water-filling problem -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Trong water-filling algorithm, bài toán tối ưu có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(\max \sum \log(\alpha_i + x_i)\) s.t. \(\sum x_i = P, x_i \geq 0\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(\min \sum \log(\alpha_i + x_i)\) s.t. \(\sum x_i = P, x_i \geq 0\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(\max \sum x_i^2\) s.t. \(\sum x_i = P\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(\min \sum x_i^2\) s.t. \(\sum x_i = P\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max \sum \log(\alpha_i + x_i)$$ s.t. $$\sum x_i = P, x_i \geq 0$$</strong><br>
                Water-filling maximizes sum of log capacities subject to total power constraint và non-negativity.
            </div>
        </div>

        <!-- Câu hỏi 8: Water-filling solution -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Nghiệm của water-filling algorithm có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(x_i^* = \max(0, \mu - \alpha_i)\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(x_i^* = \max(0, \alpha_i - \mu)\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(x_i^* = \mu - \alpha_i\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(x_i^* = \alpha_i + \mu\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x_i^* = \max(0, \mu - \alpha_i)$$</strong><br>
                Water-filling solution: allocate power $$\mu - \alpha_i$$ to channel $$i$$ if $$\mu > \alpha_i$$, otherwise allocate 0.
            </div>
        </div>

        <!-- Câu hỏi 9: SVM primal problem -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: SVM primal problem có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\min \frac{1}{2}\|w\|^2\) s.t. \(y_i(w^T x_i + b) \geq 1\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\max \frac{1}{2}\|w\|^2\) s.t. \(y_i(w^T x_i + b) \geq 1\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\min \sum \alpha_i\) s.t. \(\sum \alpha_i y_i = 0\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\max \sum \alpha_i\) s.t. \(\sum \alpha_i y_i = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min \frac{1}{2}\|w\|^2$$ s.t. $$y_i(w^T x_i + b) \geq 1$$</strong><br>
                SVM primal: minimize margin width subject to classification constraints.
            </div>
        </div>

        <!-- Câu hỏi 10: SVM dual problem -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: SVM dual problem có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(\min \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(\max \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(\min \frac{1}{2}\|w\|^2 + C\sum \xi_i\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(\max \frac{1}{2}\|w\|^2\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\max \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j$$</strong><br>
                SVM dual maximizes linear term minus quadratic term subject to constraints $$\sum \alpha_i y_i = 0, \alpha_i \geq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 11: Support vectors -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Support vectors trong SVM là những điểm có:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(\alpha_i = 0\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(\alpha_i > 0\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(y_i(w^T x_i + b) > 1\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(y_i(w^T x_i + b) < 1\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\alpha_i > 0$$</strong><br>
                Support vectors có dual variables $$\alpha_i > 0$$ và nằm trên margin boundary: $$y_i(w^T x_i + b) = 1$$.
            </div>
        </div>

        <!-- Câu hỏi 12: LICQ condition -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Linear Independence Constraint Qualification (LICQ) yêu cầu:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Tất cả constraints đều active</label>
                <label><input type="radio" name="q12" value="b"> B) Gradients của active constraints độc lập tuyến tính</label>
                <label><input type="radio" name="q12" value="c"> C) Tất cả constraints đều inactive</label>
                <label><input type="radio" name="q12" value="d"> D) Objective function khả vi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Gradients của active constraints độc lập tuyến tính</strong><br>
                LICQ đảm bảo gradients của active constraints tại optimal point độc lập tuyến tính, guarantee KKT necessity.
            </div>
        </div>

        <!-- Câu hỏi 13: L1 penalized problem -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Trong L1 penalized problem \(\min f(x) + \lambda\|x\|_1\), điều kiện KKT cho thành phần \(x_i\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(\frac{\partial f}{\partial x_i} + \lambda \text{sign}(x_i) = 0\) nếu \(x_i \neq 0\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(\frac{\partial f}{\partial x_i} + \lambda = 0\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(\frac{\partial f}{\partial x_i} = 0\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(x_i = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\frac{\partial f}{\partial x_i} + \lambda \text{sign}(x_i) = 0$$ nếu $$x_i \neq 0$$</strong><br>
                Khi $$x_i \neq 0$$, subgradient của $$|x_i|$$ là $$\text{sign}(x_i)$$. Khi $$x_i = 0$$, subgradient là $$[-1,1]$$.
            </div>
        </div>

        <!-- Câu hỏi 14: Uniqueness in L1 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Trong L1 regularization, nghiệm duy nhất khi:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(f\) là strictly convex</label>
                <label><input type="radio" name="q14" value="b"> B) \(\lambda\) đủ lớn</label>
                <label><input type="radio" name="q14" value="c"> C) Active set được xác định duy nhất</label>
                <label><input type="radio" name="q14" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f$$ là strictly convex</strong><br>
                Strict convexity của $$f$$ đảm bảo uniqueness của nghiệm, ngay cả khi L1 term không strictly convex.
            </div>
        </div>

        <!-- Câu hỏi 15: KKT matrix system -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Hệ phương trình KKT cho equality constrained QP có thể viết dưới dạng ma trận:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(\begin{bmatrix} Q & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(\begin{bmatrix} Q & A \\ A^T & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(Qx = -c\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(Ax = b\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\begin{bmatrix} Q & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}$$</strong><br>
                KKT system kết hợp stationarity $$Qx + c + A^T\nu = 0$$ và feasibility $$Ax = b$$.
            </div>
        </div>

        <!-- Câu hỏi 16: Constraint qualification -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Constraint qualification cần thiết để:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Đảm bảo KKT conditions sufficient</label>
                <label><input type="radio" name="q16" value="b"> B) Đảm bảo KKT conditions necessary</label>
                <label><input type="radio" name="q16" value="c"> C) Đảm bảo strong duality</label>
                <label><input type="radio" name="q16" value="d"> D) Đảm bảo convexity</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Đảm bảo KKT conditions necessary</strong><br>
                Constraint qualification (LICQ, MFCQ, etc.) đảm bảo KKT conditions là necessary cho local optimality.
            </div>
        </div>

        <!-- Câu hỏi 17: Second-order conditions -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Second-order sufficient condition yêu cầu Hessian của Lagrangian:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Positive definite trên toàn không gian</label>
                <label><input type="radio" name="q17" value="b"> B) Positive definite trên tangent space của active constraints</label>
                <label><input type="radio" name="q17" value="c"> C) Negative definite</label>
                <label><input type="radio" name="q17" value="d"> D) Singular</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Positive definite trên tangent space của active constraints</strong><br>
                SOSC: Hessian của Lagrangian positive definite trên tangent space, đảm bảo local minimum.
            </div>
        </div>

        <!-- Câu hỏi 18: Penalty method connection -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Mối liên hệ giữa KKT multipliers và penalty methods:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) KKT multipliers là giới hạn của penalty parameters</label>
                <label><input type="radio" name="q18" value="b"> B) Penalty parameters là giới hạn của KKT multipliers</label>
                <label><input type="radio" name="q18" value="c"> C) Không có mối liên hệ</label>
                <label><input type="radio" name="q18" value="d"> D) Chúng luôn bằng nhau</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) KKT multipliers là giới hạn của penalty parameters</strong><br>
                Khi penalty parameter $$\to \infty$$, nghiệm của penalized problem hội tụ và multipliers hội tụ đến KKT multipliers.
            </div>
        </div>

        <!-- Câu hỏi 19: Sensitivity analysis -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: KKT multipliers cung cấp thông tin về:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Sensitivity của optimal value đối với thay đổi constraints</label>
                <label><input type="radio" name="q19" value="b"> B) Tốc độ hội tụ của algorithm</label>
                <label><input type="radio" name="q19" value="c"> C) Condition number của problem</label>
                <label><input type="radio" name="q19" value="d"> D) Số lượng iterations cần thiết</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Sensitivity của optimal value đối với thay đổi constraints</strong><br>
                KKT multipliers là shadow prices: cho biết optimal value thay đổi bao nhiêu khi constraint bounds thay đổi.
            </div>
        </div>

        <!-- Câu hỏi 20: Practical applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: KKT conditions được ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Machine learning (SVM, neural networks)</label>
                <label><input type="radio" name="q20" value="b"> B) Signal processing (water-filling, beamforming)</label>
                <label><input type="radio" name="q20" value="c"> C) Economics (utility maximization, portfolio optimization)</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các lĩnh vực trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lĩnh vực trên</strong><br>
                KKT conditions là công cụ fundamental trong constrained optimization với ứng dụng rộng rãi trong ML, signal processing, economics và nhiều lĩnh vực khác.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Điều kiện KKT bao gồm:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Stationarity, primal feasibility, dual feasibility, complementary slackness</label>
                <label><input type="radio" name="q21" value="b"> B) Chỉ stationarity</label>
                <label><input type="radio" name="q21" value="c"> C) Chỉ feasibility</label>
                <label><input type="radio" name="q21" value="d"> D) Chỉ complementary slackness</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Stationarity, primal feasibility, dual feasibility, complementary slackness</strong><br>
                KKT gồm 4 điều kiện: $$\nabla f + \sum \lambda_i \nabla g_i + \sum \nu_j \nabla h_j = 0$$, $$g_i(x) \leq 0$$, $$\lambda_i \geq 0$$, $$\lambda_i g_i(x) = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Điều kiện complementary slackness có nghĩa:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$\lambda_i g_i(x) = 0$$ cho mọi $$i$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$\lambda_i + g_i(x) = 0$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$\lambda_i = g_i(x)$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$\lambda_i \cdot g_i(x) = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\lambda_i g_i(x) = 0$$ cho mọi $$i$$</strong><br>
                Complementary slackness: hoặc $$\lambda_i = 0$$ hoặc $$g_i(x) = 0$$ (ràng buộc tích cực).
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Cho bài toán $$\min x^2$$ với $$x \geq 1$$. Điều kiện KKT tại nghiệm $$x^* = 1$$:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$2x - \lambda = 0, \lambda \geq 0, \lambda(1-x) = 0$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$2x = 0$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$x = 1$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$\lambda = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$2x - \lambda = 0, \lambda \geq 0, \lambda(1-x) = 0$$</strong><br>
                Stationarity: $$2x - \lambda = 0$$. Tại $$x^* = 1$$: $$\lambda = 2$$, thỏa mãn complementary slackness.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: LICQ (Linear Independence Constraint Qualification) yêu cầu:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Gradient của các ràng buộc tích cực độc lập tuyến tính</label>
                <label><input type="radio" name="q24" value="b"> B) Tất cả ràng buộc tuyến tính</label>
                <label><input type="radio" name="q24" value="c"> C) Hàm mục tiêu tuyến tính</label>
                <label><input type="radio" name="q24" value="d"> D) Ma trận Hessian khả nghịch</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Gradient của các ràng buộc tích cực độc lập tuyến tính</strong><br>
                LICQ: các gradient $$\nabla g_i(x^*), \nabla h_j(x^*)$$ của ràng buộc tích cực phải độc lập tuyến tính.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Trong bài toán QP với KKT, ma trận hệ phương trình có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$\begin{pmatrix} H & A^T \\ A & 0 \end{pmatrix}$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$\begin{pmatrix} H & 0 \\ 0 & A \end{pmatrix}$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$H + A^T A$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$H - A^T A$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\begin{pmatrix} H & A^T \\ A & 0 \end{pmatrix}$$</strong><br>
                Hệ KKT cho QP có dạng ma trận khối với Hessian $$H$$ và ma trận ràng buộc $$A$$.
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
    q1: 'b', q2: 'b', q3: 'd', q4: 'a', q5: 'b',
    q6: 'b', q7: 'a', q8: 'a', q9: 'a', q10: 'b',
    q11: 'b', q12: 'b', q13: 'a', q14: 'a', q15: 'a',
    q16: 'b', q17: 'b', q18: 'a', q19: 'a', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'a'};

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
        message = '🌟 Xuất sắc! Bạn đã thành thạo KKT conditions và applications!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về optimality conditions và practical examples.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại complementary slackness và constraint qualification.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại KKT conditions và stationarity.';
    } else {
        message = '📖 Hãy học lại từ đầu về KKT theory nhé!';
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

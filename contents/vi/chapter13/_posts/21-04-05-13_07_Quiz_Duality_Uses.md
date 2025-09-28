---
layout: post
title: 13-07 Bài tập trắc nghiệm - Ứng Dụng và Tương Ứng của Tính Đối Ngẫu
chapter: '13'
order: 8
owner: GitHub Copilot
lang: vi
categories:
- chapter13
lesson_type: quiz
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Ứng Dụng Của Đối Ngẫu (Duality Uses)**

#### **Hai ứng dụng chính của duality**

**1. Duality Gap như Stopping Criterion:**
- **Duality gap:** $$f(x) - g(u,v)$$ với $$x$$ primal feasible, $$(u,v)$$ dual feasible
- **Upper bound cho suboptimality:** $$f(x) - f^* \le f(x) - g(u,v)$$
- **Optimality test:** Nếu duality gap = 0 thì $$x$$ optimal
- **Practical stopping:** Stop algorithm khi duality gap $$< \epsilon$$

**2. Solving Primal via Dual:**
Khi có dual optimal $$u^*, v^*$$ và strong duality:
$$x^* = \arg\min_x L(x, u^*, v^*) = \arg\min_x \left\{ f(x) + \sum u_i^* h_i(x) + \sum v_j^* l_j(x) \right\}$$

**Ưu điểm:** Dual có thể easier to solve than primal

### 🔄 **Giải Primal Thông Qua Dual**

#### **Separable problems**
**Bài toán:** $$\min_x \sum_{i=1}^n f_i(x_i) \quad \text{s.t.} \quad a^T x = b$$

**Dual function:**
$$g(v) = bv - \sum_{i=1}^n f_i^*(a_i v)$$

**Dual problem:** $$\max_v bv - \sum_{i=1}^n f_i^*(a_i v)$$

**Recovery primal solution:**
Khi có $$v^*$$, solve: $$\nabla f_i(x_i^*) = a_i v^*$$ cho mỗi $$i$$

**Ưu điểm:**
- **Scalar optimization:** Dual chỉ có 1 biến $$v$$
- **Parallel computation:** Mỗi $$f_i^*$$ tính độc lập
- **Closed-form:** Nhiều $$f_i^*$$ có analytical form

### 📏 **Dual Norms (Chuẩn Đối Ngẫu)**

#### **Định nghĩa**
Cho norm $$\lVert x \rVert$$, **dual norm** $$\lVert x \rVert_*$$ được định nghĩa:
$$\lVert z \rVert_* = \max_{\lVert x \rVert \le 1} z^T x$$

#### **Tính chất cơ bản**
- **Generalized Cauchy-Schwarz:** $$\lvert z^T x \rvert \le \lVert z \rVert_* \lVert x \rVert$$
- **Double dual:** $$\lVert x \rVert_{**} = \lVert x \rVert$$
- **Always a norm:** $$\lVert \cdot \rVert_*$$ luôn là norm ngay cả khi $$\lVert \cdot \rVert$$ không convex

#### **Ví dụ quan trọng**
- **$$\ell_p$$ norms:** $$(\lVert x \rVert_p)_* = \lVert x \rVert_q$$ với $$\frac{1}{p} + \frac{1}{q} = 1$$
  - $$(\lVert x \rVert_1)_* = \lVert x \rVert_\infty$$
  - $$(\lVert x \rVert_2)_* = \lVert x \rVert_2$$
  - $$(\lVert x \rVert_\infty)_* = \lVert x \rVert_1$$
- **Matrix norms:** $$(\lVert X \rVert_{tr})_* = \lVert X \rVert_{op} = \sigma_1(X)$$ (largest singular value)

#### **Dual norm characterization**
**Bài toán:** $$\min_y \lVert y \rVert \quad \text{s.t.} \quad y = x$$

**Dual problem:** $$\max_{\lVert u \rVert_* \le 1} u^T x$$

**Kết quả:** $$\lVert x \rVert = \max_{\lVert u \rVert_* \le 1} u^T x$$

### 🎯 **Ví Dụ: LASSO Dual**

#### **Primal LASSO**
$$\min_\beta \frac{1}{2}\lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$$

#### **Reformulation**
$$\min_{\beta,z} \frac{1}{2}\lVert y - z \rVert_2^2 + \lambda \lVert \beta \rVert_1 \quad \text{s.t.} \quad z = X\beta$$

#### **Dual derivation**
**Lagrangian:**
$$L(\beta,z,u) = \frac{1}{2}\lVert y - z \rVert_2^2 + \lambda \lVert \beta \rVert_1 + u^T(z - X\beta)$$

**Dual function:**
$$g(u) = \frac{1}{2}\lVert y \rVert_2^2 - \frac{1}{2}\lVert y - u \rVert_2^2 - I_{\{\lVert X^T v \rVert_\infty \le \lambda\}}(u)$$

#### **LASSO dual problem**
$$\min_u \lVert y - u \rVert_2^2 \quad \text{s.t.} \quad \lVert X^T u \rVert_\infty \le \lambda$$

#### **Primal-dual relationship**
- **Strong duality:** Slater's condition satisfied
- **Primal recovery:** $$X\beta^* = y - u^*$$
- **Residual interpretation:** $$u^*$$ là dual residual

### 🔗 **Conjugate Functions và Dual Problems**

#### **Conjugate function**
$$f^*(u) = \sup_x \{u^T x - f(x)\}$$

**Equivalent:** $$-f^*(u) = \min_x \{f(x) - u^T x\}$$

#### **Composite problems**
**Bài toán:** $$\min_x f(x) + g(x)$$

**Equivalent constrained form:**
$$\min_{x,z} f(x) + g(z) \quad \text{s.t.} \quad x = z$$

**Dual function:**
$$g(u) = \min_{x,z} f(x) + g(z) + u^T(z - x) = -f^*(u) - g^*(-u)$$

**Dual problem:** $$\max_u -f^*(u) - g^*(-u)$$

#### **Ví dụ ứng dụng**

**1. Indicator function:**
$$\min_x f(x) + I_C(x) \Rightarrow \max_u -f^*(u) - I_C^*(-u)$$

với $$I_C^*$$ là support function của $$C$$

**2. Norm regularization:**
$$\min_x f(x) + \lVert x \rVert \Rightarrow \max_{\lVert u \rVert_* \le 1} -f^*(u)$$

### 🔺 **Dual Cones (Nón Đối Ngẫu)**

#### **Định nghĩa**
Cho cone $$K \subseteq \mathbb{R}^n$$, **dual cone** $$K^*$$ là:
$$K^* = \{y : y^T x \ge 0 \quad \forall x \in K\}$$

#### **Tính chất**
- **Always convex:** $$K^*$$ luôn convex ngay cả khi $$K$$ không convex
- **Double dual:** Nếu $$K$$ closed convex cone thì $$K^{**} = K$$
- **Geometric interpretation:** $$y \in K^* \Leftrightarrow$$ halfspace $$\{x : y^T x \ge 0\}$$ contains $$K$$

#### **Ví dụ quan trọng**

**1. Linear subspace:**
- **$$V$$ subspace:** $$V^* = V^\perp$$ (orthogonal complement)
- **Row space:** $$(row(A))^* = null(A)$$

**2. Norm cones:**
- **Norm cone:** $$K = \{(x,t) : \lVert x \rVert \le t\}$$
- **Dual:** $$K^* = \{(y,s) : \lVert y \rVert_* \le s\}$$

**3. Positive semidefinite cone:**
- **Self-dual:** $$(\mathbb{S}_+^n)^* = \mathbb{S}_+^n$$
- **Verification:** $$Y \succeq 0 \Leftrightarrow tr(YX) \ge 0 \quad \forall X \succeq 0$$

### 🎯 **Conic Programming Duality**

#### **Primal conic problem**
$$\min_x f(x) \quad \text{s.t.} \quad Ax \in K$$

#### **Dual conic problem**
$$\max_u -f^*(A^T u) \quad \text{s.t.} \quad u \in K^*$$

**Derivation:** Sử dụng support function $$I_K^*(y) = \max_{z \in K} z^T y$$

#### **Ví dụ: Second-Order Cone Programming (SOCP)**
**Primal:** $$\min c^T x \quad \text{s.t.} \quad \lVert A_i x + b_i \rVert_2 \le c_i^T x + d_i$$

**Equivalent conic form:** $$Ax \in K$$ với $$K$$ là product của second-order cones

**Dual:** $$\max -b^T u \quad \text{s.t.} \quad A^T u = c, \quad u \in K^*$$

### 🛠️ **Kỹ Thuật Thực Hành**

#### **Khi nào sử dụng duality:**
1. **Dual easier:** Fewer variables, simpler structure
2. **Bounds needed:** Duality gap cho convergence monitoring
3. **Sensitivity analysis:** Dual variables như shadow prices
4. **Parallel computation:** Separable problems

#### **Computational strategies:**
- **Primal-dual methods:** Update both simultaneously
- **Dual decomposition:** Exploit separable structure
- **Augmented Lagrangian:** Improve convergence
- **Barrier methods:** Interior point approaches

#### **Common applications:**
- **Machine learning:** SVM, regularized regression, matrix completion
- **Signal processing:** Compressed sensing, image denoising
- **Network optimization:** Flow problems, resource allocation
- **Finance:** Portfolio optimization, risk management

### 💡 **Ví Dụ Minh Họa**

#### **Simple norm minimization:**
**Problem:** $$\min_x \lVert x \rVert_2 \quad \text{s.t.} \quad Ax = b$$

**Dual:** $$\max_{A^T u = 0} -b^T u$$

**Interpretation:** Find $$u \perp row(A)$$ maximizing $$-b^T u$$

**Solution:** $$u^* = -A^+ b$$ (pseudoinverse)

#### **$$\ell_1$$ minimization:**
**Problem:** $$\min_x \lVert x \rVert_1 \quad \text{s.t.} \quad Ax = b$$

**Dual:** $$\max_{\lVert A^T u \rVert_\infty \le 1} b^T u$$

**Geometric interpretation:** Find $$u$$ trong dual feasible set maximizing $$b^T u$$

### 🎯 **Kết Nối Với Các Chương**

#### **Từ chương trước:**
- **Chương 12:** KKT conditions - dual variables interpretation
- **Chương 11:** General duality theory - foundation
- **Chương 10:** LP duality - special case

#### **Tầm quan trọng của Duality Uses:**
- **Computational efficiency:** Solve easier dual instead of primal
- **Algorithm design:** Primal-dual methods, decomposition
- **Theoretical insights:** Optimality conditions, sensitivity
- **Practical applications:** Machine learning, signal processing

#### **Hướng phát triển:**
- **Interior point methods:** Barrier function approaches
- **Decomposition methods:** ADMM, dual decomposition
- **Stochastic optimization:** Online dual methods
- **Robust optimization:** Worst-case analysis

### 🌟 **Ý Nghĩa Lý Thuyết**

#### **Duality như computational tool:**
- **Alternative solution path:** Dual có thể easier than primal
- **Parallel computation:** Separable structure exploitation
- **Convergence monitoring:** Duality gap như stopping criterion
- **Sensitivity analysis:** Dual variables interpretation

#### **Geometric insights:**
- **Dual norms:** Characterize unit balls của different norms
- **Dual cones:** Geometric duality trong cone programming
- **Support functions:** Convex analysis foundation
- **Conjugate functions:** Legendre-Fenchel transform

#### **Algorithmic implications:**
- **Primal-dual methods:** Simultaneous updates
- **Decomposition:** Exploit problem structure
- **Interior point:** Barrier function approaches
- **Augmented Lagrangian:** Penalty method improvements

### 💡 **Mẹo Thực Hành**

#### **Choosing primal vs dual:**
1. **Variable count:** Fewer variables often easier
2. **Constraint structure:** Simple constraints preferred
3. **Separability:** Dual exploits separable structure
4. **Computational resources:** Parallel vs sequential

#### **Implementation tips:**
- **Numerical stability:** Check condition numbers
- **Convergence monitoring:** Use duality gap
- **Warm starting:** Initialize với previous solutions
- **Regularization:** Add small regularization for stability

#### **Common pitfalls:**
- **Constraint qualifications:** Ensure strong duality
- **Numerical precision:** Duality gap sensitivity
- **Infeasibility:** Handle primal/dual infeasible cases
- **Scaling:** Proper problem scaling important

### 🔬 **Advanced Topics**

#### **Fenchel duality:**
- **General framework:** Conjugate function approach
- **Minimax theorems:** Saddle point theory
- **Variational problems:** Calculus of variations
- **Optimal transport:** Kantorovich duality

#### **Conic duality:**
- **Semidefinite programming:** Matrix optimization
- **Second-order cone programming:** Robust optimization
- **Exponential cone:** Entropy optimization
- **Power cone:** Geometric programming

#### **Algorithmic developments:**
- **First-order methods:** Accelerated gradient, FISTA
- **Primal-dual algorithms:** ADMM, Chambolle-Pock
- **Interior point methods:** Polynomial-time algorithms
- **Stochastic methods:** Online optimization

### 📈 **Ứng Dụng Thực Tế**

#### **Machine Learning:**
- **SVM:** Dual formulation enables kernel trick
- **LASSO:** Dual provides geometric insights
- **Matrix completion:** Nuclear norm dual
- **Deep learning:** Regularization via duality

#### **Signal Processing:**
- **Compressed sensing:** $$\ell_1$$ minimization dual
- **Image denoising:** Total variation dual
- **Filter design:** Frequency domain duality
- **Beamforming:** Array processing applications

#### **Operations Research:**
- **Network flows:** Max-flow min-cut duality
- **Resource allocation:** Shadow price interpretation
- **Production planning:** Capacity constraint duals
- **Transportation:** Assignment problem duality

#### **Finance:**
- **Portfolio optimization:** Risk-return duality
- **Option pricing:** Risk-neutral measure duality
- **Risk management:** Coherent risk measure duality
- **Algorithmic trading:** Execution cost optimization

### 🔮 **Future Directions**

#### **Emerging applications:**
- **Quantum optimization:** Quantum duality theory
- **Distributed optimization:** Consensus và duality
- **Robust optimization:** Distributionally robust duality
- **Online learning:** Regret minimization duality

#### **Computational advances:**
- **GPU acceleration:** Parallel dual methods
- **Quantum computing:** Quantum optimization algorithms
- **Approximate methods:** Inexact dual solutions
- **Adaptive algorithms:** Problem-specific dual methods

### 💎 **Key Insights**

#### **Duality transformations:**
1. **Problem reformulation:** Convert hard primal to easy dual
2. **Geometric interpretation:** Dual norms, cones provide insights
3. **Computational efficiency:** Exploit separable structure
4. **Theoretical understanding:** Optimality, sensitivity analysis

#### **Practical impact:**
- **Algorithm design:** Foundation cho modern optimization
- **Software implementation:** Dual methods trong solvers
- **Real-world problems:** Enable solution của large-scale problems
- **Interdisciplinary applications:** Across science và engineering

### 🌟 **Legacy của chương 13:**

- **Computational revolution:** Duality enables efficient algorithms
- **Theoretical unification:** Connects diverse optimization areas
- **Practical impact:** Solves real-world problems efficiently
- **Educational value:** Bridges theory và applications
- **Scientific influence:** Foundation cho modern optimization

---

💡 **Thông điệp cuối cùng:** Duality không chỉ là mathematical curiosity - nó là **powerful computational tool** enabling efficient solution của complex optimization problems across science, engineering, và machine learning!

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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về các ứng dụng và tương ứng của duality, bao gồm conjugate functions, dual norms, LASSO dual, dual cones và các khái niệm advanced duality.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: Ứng Dụng và Tương Ứng của Tính Đối Ngẫu</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Conjugate function definition -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Conjugate function $$f^*(y)$$ được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) $$f^*(y) = \max_x (y^T x - f(x))$$</label>
                <label><input type="radio" name="q1" value="b"> B) $$f^*(y) = \min_x (y^T x - f(x))$$</label>
                <label><input type="radio" name="q1" value="c"> C) $$f^*(y) = \max_x (y^T x + f(x))$$</label>
                <label><input type="radio" name="q1" value="d"> D) $$f^*(y) = f(y)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \max_x (y^T x - f(x))$$</strong><br>
                Conjugate function (Legendre-Fenchel transform) là supremum của linear function $$y^T x$$ trừ đi $$f(x)$$.
            </div>
        </div>

        <!-- Câu hỏi 2: Conjugate properties -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Conjugate function $$f^*$$ có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Luôn convex</label>
                <label><input type="radio" name="q2" value="b"> B) Luôn concave</label>
                <label><input type="radio" name="q2" value="c"> C) Có cùng tính lồi với $$f$$</label>
                <label><input type="radio" name="q2" value="d"> D) Không xác định được</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn convex</strong><br>
                Conjugate function luôn convex vì là supremum của các affine functions, bất kể $$f$$ có convex hay không.
            </div>
        </div>

        <!-- Câu hỏi 3: Double conjugate -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Nếu $$f$$ là convex và lower semicontinuous, thì $$f^{**}$$ bằng:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$f$$</label>
                <label><input type="radio" name="q3" value="b"> B) $$-f$$</label>
                <label><input type="radio" name="q3" value="c"> C) $$f^*$$</label>
                <label><input type="radio" name="q3" value="d"> D) $$0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f$$</strong><br>
                Fenchel-Moreau theorem: nếu $$f$$ convex và lower semicontinuous thì $$f^{**} = f$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Dual norm definition -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Dual norm $$\lVert x \rVert_*$$ được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$\lVert x \rVert_* = \max_{\lVert z \rVert \leq 1} z^T x$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$\lVert x \rVert_* = \min_{\lVert z \rVert \leq 1} z^T x$$</label>
                <label><input type="radio" name="q4" value="c"> C) $$\lVert x \rVert_* = \max_{\lVert z \rVert = 1} z^T x$$</label>
                <label><input type="radio" name="q4" value="d"> D) $$\lVert x \rVert_* = \lVert x \rVert$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\|x\|_* = \max_{\|z\| \leq 1} z^T x$$</strong><br>
                Dual norm là maximum inner product với vectors trong unit ball của primal norm.
            </div>
        </div>

        <!-- Câu hỏi 5: Lp dual norm -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Dual norm của $$\ell_p$$ norm là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) $$\ell_p$$ norm</label>
                <label><input type="radio" name="q5" value="b"> B) $$\ell_q$$ norm với $$1/p + 1/q = 1$$</label>
                <label><input type="radio" name="q5" value="c"> C) \(\ell_\infty\) norm</label>
                <label><input type="radio" name="q5" value="d"> D) \(\ell_1\) norm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\ell_q$$ norm với $$1/p + 1/q = 1$$</strong><br>
                Hölder conjugate: dual của $$\ell_p$$ là $$\ell_q$$ với $$1/p + 1/q = 1$$. Đặc biệt: dual của $$\ell_1$$ là $$\ell_\infty$$.
            </div>
        </div>

        <!-- Câu hỏi 6: Holder inequality -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Hölder inequality có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(|x^T y| \leq \|x\|_p \|y\|_q\) với \(1/p + 1/q = 1\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(|x^T y| \leq \|x\|_p \|y\|_p\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(|x^T y| \geq \|x\|_p \|y\|_q\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\|x + y\|_p \leq \|x\|_p + \|y\|_p\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$|x^T y| \leq \|x\|_p \|y\|_q$$ với $$1/p + 1/q = 1$$</strong><br>
                Hölder inequality là generalization của Cauchy-Schwarz, liên hệ dual norms với inner product.
            </div>
        </div>

        <!-- Câu hỏi 7: Nuclear norm dual -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Dual norm của nuclear norm (trace norm) là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Frobenius norm</label>
                <label><input type="radio" name="q7" value="b"> B) Operator norm (spectral norm)</label>
                <label><input type="radio" name="q7" value="c"> C) Nuclear norm</label>
                <label><input type="radio" name="q7" value="d"> D) \(\ell_1\) norm của singular values</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Operator norm (spectral norm)</strong><br>
                Dual của nuclear norm $$\|X\|_* = \sum \sigma_i$$ là operator norm $$\|X\|_{op} = \sigma_1$$ (largest singular value).
            </div>
        </div>

        <!-- Câu hỏi 8: LASSO dual problem -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: LASSO dual problem có constraint:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\|A^T u\|_\infty \leq \lambda\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(\|A^T u\|_1 \leq \lambda\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(\|A^T u\|_2 \leq \lambda\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(\|u\|_2 \leq \lambda\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\|A^T u\|_\infty \leq \lambda$$</strong><br>
                LASSO dual constraint: $$\|A^T u\|_\infty \leq \lambda$$ vì dual của $$\ell_1$$ norm là $$\ell_\infty$$ norm.
            </div>
        </div>

        <!-- Câu hỏi 9: Conjugate of quadratic -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Conjugate của \(f(x) = \frac{1}{2}x^T Q x\) với \(Q \succ 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(f^*(y) = \frac{1}{2}y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(f^*(y) = \frac{1}{2}y^T Q y\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(f^*(y) = y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(f^*(y) = \frac{1}{2}y^T Q^{-2} y\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \frac{1}{2}y^T Q^{-1} y$$</strong><br>
                Conjugate của quadratic form với $$Q \succ 0$$ là quadratic form với $$Q^{-1}$$.
            </div>
        </div>

        <!-- Câu hỏi 10: Conjugate of indicator -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Conjugate của indicator function \(I_C(x)\) của tập lồi \(C\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(I_C^*(y) = \sup_{x \in C} y^T x\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(I_C^*(y) = \inf_{x \in C} y^T x\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(I_C^*(y) = I_C(y)\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(I_C^*(y) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$I_C^*(y) = \sup_{x \in C} y^T x$$</strong><br>
                Conjugate của indicator function là support function của tập $$C$$.
            </div>
        </div>

        <!-- Câu hỏi 11: Dual cone definition -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Dual cone \(K^*\) của cone \(K\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(K^* = \{y : y^T x \geq 0 \text{ với mọi } x \in K\}\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(K^* = \{y : y^T x \leq 0 \text{ với mọi } x \in K\}\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(K^* = \{y : y^T x = 0 \text{ với mọi } x \in K\}\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(K^* = K\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$K^* = \{y : y^T x \geq 0 \text{ với mọi } x \in K\}$$</strong><br>
                Dual cone gồm các vector tạo góc không tù với mọi vector trong cone gốc.
            </div>
        </div>

        <!-- Câu hỏi 12: Self-dual cone -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Cone nào sau đây là self-dual?</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Positive orthant \(\mathbb{R}_+^n\)</label>
                <label><input type="radio" name="q12" value="b"> B) Second-order cone (Lorentz cone)</label>
                <label><input type="radio" name="q12" value="c"> C) Positive semidefinite cone</label>
                <label><input type="radio" name="q12" value="d"> D) Tất cả các cone trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các cone trên</strong><br>
                Positive orthant, second-order cone và PSD cone đều là self-dual: $$K^* = K$$.
            </div>
        </div>

        <!-- Câu hỏi 13: Conjugate of norm -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Conjugate của norm \(\|x\|\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(f^*(y) = I_{\{\|y\|_* \leq 1\}}(y)\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(f^*(y) = \|y\|_*\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(f^*(y) = \|y\|\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(f^*(y) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = I_{\{\|y\|_* \leq 1\}}(y)$$</strong><br>
                Conjugate của norm là indicator function của dual norm unit ball.
            </div>
        </div>

        <!-- Câu hỏi 14: Fenchel duality -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Fenchel duality theorem áp dụng cho bài toán \(\min f(x) + g(Ax)\):</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(\min f(x) + g(Ax) = \max -f^*(-A^T y) - g^*(y)\)</label>
                <label><input type="radio" name="q14" value="b"> B) \(\min f(x) + g(Ax) = \max f^*(A^T y) + g^*(y)\)</label>
                <label><input type="radio" name="q14" value="c"> C) \(\min f(x) + g(Ax) = \min f^*(x) + g^*(Ax)\)</label>
                <label><input type="radio" name="q14" value="d"> D) Không có mối liên hệ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min f(x) + g(Ax) = \max -f^*(-A^T y) - g^*(y)$$</strong><br>
                Fenchel duality kết nối primal problem với dual problem thông qua conjugate functions.
            </div>
        </div>

        <!-- Câu hỏi 15: Legendre transform -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Legendre transform được sử dụng khi:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(f\) là convex và differentiable</label>
                <label><input type="radio" name="q15" value="b"> B) \(f\) là concave</label>
                <label><input type="radio" name="q15" value="c"> C) \(f\) là linear</label>
                <label><input type="radio" name="q15" value="d"> D) \(f\) là non-convex</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f$$ là convex và differentiable</strong><br>
                Legendre transform là trường hợp đặc biệt của conjugate function khi $$f$$ convex và differentiable.
            </div>
        </div>

        <!-- Câu hỏi 16: Moreau envelope -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Moreau envelope \(M_\lambda f(x)\) liên quan đến:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Proximal operator</label>
                <label><input type="radio" name="q16" value="b"> B) Conjugate function</label>
                <label><input type="radio" name="q16" value="c"> C) Smoothing của \(f\)</label>
                <label><input type="radio" name="q16" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Moreau envelope kết nối proximal operator, conjugate function và cung cấp smooth approximation của $$f$$.
            </div>
        </div>

        <!-- Câu hỏi 17: Convex conjugate inequality -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Fenchel-Young inequality phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(f(x) + f^*(y) \geq x^T y\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(f(x) + f^*(y) \leq x^T y\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(f(x) + f^*(y) = x^T y\)</label>
                <label><input type="radio" name="q17" value="d"> D) \(f(x) - f^*(y) \geq x^T y\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f(x) + f^*(y) \geq x^T y$$</strong><br>
                Fenchel-Young inequality: $$f(x) + f^*(y) \geq x^T y$$ với equality khi $$y \in \partial f(x)$$.
            </div>
        </div>

        <!-- Câu hỏi 18: Dual problem solving -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Khi nào nên giải dual problem thay vì primal?</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Khi dual có ít variables hơn</label>
                <label><input type="radio" name="q18" value="b"> B) Khi dual có structure đơn giản hơn</label>
                <label><input type="radio" name="q18" value="c"> C) Khi có strong duality</label>
                <label><input type="radio" name="q18" value="d"> D) Tất cả các trường hợp trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các trường hợp trên</strong><br>
                Giải dual có lợi khi: fewer variables, simpler structure, hoặc computational advantages, với điều kiện có strong duality.
            </div>
        </div>

        <!-- Câu hỏi 19: Conjugate of max -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Conjugate của \(f(x) = \max\{f_1(x), f_2(x)\}\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(f^*(y) = \max\{f_1^*(y), f_2^*(y)\}\)</label>
                <label><input type="radio" name="q19" value="b"> B) \(f^*(y) = \min\{f_1^*(y), f_2^*(y)\}\)</label>
                <label><input type="radio" name="q19" value="c"> C) \(f^*(y) = f_1^*(y) + f_2^*(y)\)</label>
                <label><input type="radio" name="q19" value="d"> D) \(f^*(y) = \inf\{\lambda_1 f_1^*(y) + \lambda_2 f_2^*(y) : \lambda_1 + \lambda_2 = 1, \lambda_i \geq 0\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) $$f^*(y) = \inf\{\lambda_1 f_1^*(y) + \lambda_2 f_2^*(y) : \lambda_1 + \lambda_2 = 1, \lambda_i \geq 0\}$$</strong><br>
                Conjugate của max là infimal convolution của conjugates (under regularity conditions).
            </div>
        </div>

        <!-- Câu hỏi 20: Applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Conjugate duality được ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Machine learning (regularization, kernel methods)</label>
                <label><input type="radio" name="q20" value="b"> B) Signal processing (compressed sensing, denoising)</label>
                <label><input type="radio" name="q20" value="c"> C) Economics (utility theory, market equilibrium)</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các lĩnh vực trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lĩnh vực trên</strong><br>
                Conjugate duality có ứng dụng rộng rãi: ML (regularization), signal processing (sparsity), economics (utility maximization), và nhiều lĩnh vực khác.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Sensitivity analysis trong tối ưu hóa nghiên cứu:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Thay đổi nghiệm khi tham số thay đổi</label>
                <label><input type="radio" name="q21" value="b"> B) Độ nhạy của thuật toán</label>
                <label><input type="radio" name="q21" value="c"> C) Tốc độ hội tụ</label>
                <label><input type="radio" name="q21" value="d"> D) Độ chính xác số</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Thay đổi nghiệm khi tham số thay đổi</strong><br>
                Sensitivity analysis phân tích cách nghiệm tối ưu thay đổi khi các tham số bài toán thay đổi.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Trong LP, shadow price của ràng buộc $$i$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Giá trị của dual variable $$y_i^*$$</label>
                <label><input type="radio" name="q22" value="b"> B) Giá trị của primal variable</label>
                <label><input type="radio" name="q22" value="c"> C) Hệ số trong hàm mục tiêu</label>
                <label><input type="radio" name="q22" value="d"> D) Slack variable</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Giá trị của dual variable $$y_i^*$$</strong><br>
                Shadow price = dual variable, cho biết mức tăng giá trị tối ưu khi nới lỏng ràng buộc một đơn vị.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Envelope theorem trong tối ưu hóa cho biết:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$\frac{\partial f^*(\theta)}{\partial \theta} = \frac{\partial L}{\partial \theta}$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$\frac{\partial f^*}{\partial x} = 0$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$\frac{\partial^2 f^*}{\partial \theta^2} = 0$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$f^*(\theta) = \text{const}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\frac{\partial f^*(\theta)}{\partial \theta} = \frac{\partial L}{\partial \theta}$$</strong><br>
                Envelope theorem: đạo hàm của giá trị tối ưu theo tham số bằng đạo hàm riêng của Lagrangian.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Parametric programming nghiên cứu bài toán:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$\min f(x,\theta)$$ với $$g(x,\theta) \leq 0$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$\min f(x)$$ với $$g(x) \leq \theta$$</label>
                <label><input type="radio" name="q24" value="c"> C) Cả A và B</label>
                <label><input type="radio" name="q24" value="d"> D) Không có tham số</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Cả A và B</strong><br>
                Parametric programming xem xét bài toán tối ưu với tham số trong hàm mục tiêu và/hoặc ràng buộc.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Trong portfolio optimization, khi risk aversion tăng:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Chọn portfolio ít rủi ro hơn</label>
                <label><input type="radio" name="q25" value="b"> B) Chọn portfolio rủi ro hơn</label>
                <label><input type="radio" name="q25" value="c"> C) Không thay đổi</label>
                <label><input type="radio" name="q25" value="d"> D) Tối đa hóa return</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Chọn portfolio ít rủi ro hơn</strong><br>
                Risk aversion cao dẫn đến việc chọn portfolio có phương sai (rủi ro) thấp hơn.
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
    q1: 'a', q2: 'a', q3: 'a', q4: 'a', q5: 'b',
    q6: 'a', q7: 'b', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'd', q13: 'a', q14: 'a', q15: 'a',
    q16: 'd', q17: 'a', q18: 'd', q19: 'd', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'c', q25: 'a'};

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
        message = '🌟 Xuất sắc! Bạn đã thành thạo advanced duality theory!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về conjugate functions và dual norms.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại conjugate properties và Fenchel duality.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại conjugate functions và dual cones.';
    } else {
        message = '📖 Hãy học lại từ đầu về advanced duality concepts nhé!';
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

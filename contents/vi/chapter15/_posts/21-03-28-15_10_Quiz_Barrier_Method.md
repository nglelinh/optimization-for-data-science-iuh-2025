---
layout: post
title: 15-09 Bài tập trắc nghiệm - Phương Pháp Rào Cản
chapter: '15'
order: 18
owner: GitHub Copilot
lang: vi
categories:
- chapter15
lesson_type: quiz
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Barrier Method (Phương Pháp Rào Cản)**

#### **Bài toán inequality constrained**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad Ax = b$$

với $$i = 1,\ldots,m$$

#### **Vấn đề với boundary optimization**
- **Binding vs non-binding constraints:** Khó phân biệt constraints nào active
- **Boundary computation:** $$O(m^2)$$ complexity cho active set methods
- **Non-differentiable:** Indicator function không khả vi

#### **Interior method philosophy**
**Ý tưởng:** Solve từ **interior** của feasible region thay vì boundary
- **Avoid boundary:** Không cần xác định active constraints
- **Smooth approximation:** Sử dụng differentiable barrier functions
- **Newton applicable:** Enable Newton method cho constrained problems

### 🚧 **Logarithmic Barrier Function**

#### **Indicator function approximation**
**Original:** $$I_C(x) = \begin{cases} 0 & \text{if } x \in C \\ \infty & \text{otherwise} \end{cases}$$

**Barrier approximation:** $$\phi(x) = -\sum_{i=1}^m \log(-h_i(x))$$

#### **Properties của log barrier**
- **Domain:** $$\{x : h_i(x) < 0 \quad \forall i\}$$ (strictly feasible)
- **Smooth:** Twice differentiable trong interior
- **Barrier effect:** $$\phi(x) \to \infty$$ khi $$x$$ approaches boundary
- **Self-concordant:** (khi $$h_i$$ affine hoặc convex quadratic) Enables elegant Newton analysis

#### **Barrier problem formulation**
**Original problem:** $$\min f(x)$$ s.t. $$h_i(x) \le 0, Ax = b$$

**Barrier approximation:**
$$\min_x tf(x) + \phi(x) \quad \text{s.t.} \quad Ax = b$$

với $$t > 0$$ là **barrier parameter**

#### **Interpretation**
- **Large $$t$$:** Emphasize original objective $$f(x)$$
- **Small $$t$$:** Emphasize staying interior (large barrier effect)
- **$$t \to \infty$$:** Barrier problem → original problem

### 🛤️ **Central Path**

#### **Definition**
**Central path:** $$\{x^*(t) : t > 0\}$$ với $$x^*(t) = \arg\min_x \{tf(x) + \phi(x) : Ax = b\}$$

#### **Properties**
- **Smooth curve:** Forms continuous path trong $$\mathbb{R}^n$$
- **Convergence:** $$x^*(t) \to x^*$$ as $$t \to \infty$$
- **Interior:** All points strictly feasible
- **Unique:** Each $$t$$ gives unique $$x^*(t)$$ (under strict convexity)

#### **Geometric interpretation**
- **Path from interior to boundary:** Gradually approach optimal solution
- **Balance:** Trade-off giữa objective và barrier terms
- **Smooth transition:** Continuous movement toward optimum

### 📊 **Điều Kiện KKT và Giải Thích**

#### **Barrier problem KKT**
Cho barrier problem $$\min tf(x) + \phi(x)$$ s.t. $$Ax = b$$:

**Stationarity:** $$t\nabla f(x^*(t)) + \nabla \phi(x^*(t)) + A^T \nu^*(t) = 0$$

**Feasibility:** $$Ax^*(t) = b$$

#### **Original problem KKT**
Cho original problem $$\min f(x)$$ s.t. $$h_i(x) \le 0, Ax = b$$:

**Stationarity:** $$\nabla f(x^*) + \sum_{i=1}^m \lambda_i^* \nabla h_i(x^*) + A^T \nu^* = 0$$

**Complementary slackness:** $$\lambda_i^* h_i(x^*) = 0$$

**Dual feasibility:** $$\lambda_i^* \ge 0$$

**Primal feasibility:** $$h_i(x^*) \le 0, Ax^* = b$$

#### **Connection**
**Key insight:** $$\nabla \phi(x) = -\sum_{i=1}^m \frac{1}{h_i(x)} \nabla h_i(x)$$

**Perturbed KKT:** $$\lambda_i^*(t) = -\frac{1}{th_i(x^*(t))}$$

**Interpretation:** Barrier method gives **perturbed KKT conditions**

### 📈 **Suboptimality Gap**

#### **Duality gap for barrier problem**
**Theorem:** $$f(x^*(t)) - f^* \le \frac{m}{t}$$

**Proof sketch:**
1. Construct dual feasible point từ barrier solution
2. Use weak duality: $$f(x^*(t)) - f^* \le \text{duality gap}$$
3. Duality gap = $$\frac{m}{t}$$

#### **Practical implication**
- **Accuracy control:** Choose $$t = \frac{m}{\epsilon}$$ for $$\epsilon$$-optimal solution
- **Trade-off:** Larger $$t$$ → better approximation but harder subproblem
- **Stopping criterion:** $$\frac{m}{t} < \epsilon$$

### 🔄 **Barrier Method Algorithms**

#### **Barrier Method v.0 (Naive)**
**Algorithm:**
1. Choose $$t = \frac{m}{\epsilon}$$
2. Solve barrier problem $$\min tf(x) + \phi(x)$$ s.t. $$Ax = b$$
3. Return $$x^*(t)$$

**Problems:**
- **Large $$t$$:** Very difficult subproblem
- **Poor conditioning:** Hessian becomes ill-conditioned
- **Slow convergence:** Many Newton iterations needed

#### **Barrier Method v.1 (Path-following)**
**Algorithm:**
1. Choose $$t^{(0)} > 0$$, set $$k = 0$$
2. Solve barrier problem at $$t^{(0)}$$ to get $$x^{(0)}$$
3. **While** $$\frac{m}{t^{(k)}} > \epsilon$$:
   - Choose $$t^{(k+1)} > t^{(k)}$$ (typically $$t^{(k+1)} = \mu t^{(k)}$$)
   - **Warm start:** Initialize Newton với $$x^{(k)}$$
   - Solve barrier problem at $$t^{(k+1)}$$ to get $$x^{(k+1)}$$
   - $$k \leftarrow k + 1$$

#### **Key components**
- **Centering steps:** Solve barrier problem (outer iterations)
- **Newton steps:** Within each centering step (inner iterations)
- **Warm start:** Use previous solution as initialization
- **Parameter update:** $$t^{(k+1)} = \mu t^{(k)}$$ với $$\mu > 1$$

### ⚖️ **Parameter Selection Trade-offs**

#### **Choice of $$\mu$$ (update factor)**
- **$$\mu$$ too small:** Many outer iterations (more centering steps)
- **$$\mu$$ too large:** Many inner iterations (Newton steps per centering)
- **Typical choice:** $$\mu = 10$$ to $$50$$

#### **Choice of $$t^{(0)}$$ (initial parameter)**
- **$$t^{(0)}$$ too small:** Many outer iterations
- **$$t^{(0)}$$ too large:** Difficult first centering step
- **Practical:** Start với moderate value, algorithm is robust

#### **Robustness**
**Good news:** Barrier method performance is **robust** to parameter choices
- **Wide range:** Many $$(\mu, t^{(0)})$$ combinations work well
- **Problem-dependent:** Optimal values vary with problem size
- **Practical guidance:** Default values usually sufficient

### 📊 **Convergence Analysis**

#### **Convergence theorem**
**Assumption:** Centering steps solved exactly

**Result:** After $$k$$ outer iterations:
$$f(x^{(k)}) - f^* \le \frac{m}{\mu^k t^{(0)}}$$

#### **Iteration complexity**
**To achieve $$\epsilon$$-optimal solution:**
$$\text{Outer iterations} = \frac{\log(m/(t^{(0)}\epsilon))}{\log \mu} + 1$$

**Convergence rate:** $$O(\log(1/\epsilon))$$ - **linear convergence**

#### **Comparison với other methods**
- **Newton method:** $$O(\log\log(1/\epsilon))$$ - quadratic convergence
- **Gradient descent:** $$O(1/\epsilon)$$ - sublinear convergence
- **Barrier method:** $$O(\log(1/\epsilon))$$ - linear convergence

**Lưu ý:** Hội tụ tuyến tính là **rất tốt** đối với các bài toán có ràng buộc!

### 🎯 **Feasibility Methods**

#### **Problem: Finding strictly feasible starting point**
**Need:** $$x$$ such that $$h_i(x) < 0 \quad \forall i, \quad Ax = b$$

#### **Phase I: Maximum infeasibility**
$$\min_{x,s} s \quad \text{s.t.} \quad h_i(x) \le s, \quad Ax = b$$

**Goal:** Find $$s < 0$$ (strictly feasible point exists)

**Advantage:** Single slack variable

#### **Phase I: Individual infeasibilities**
$$\min_{x,s} \mathbf{1}^T s \quad \text{s.t.} \quad h_i(x) \le s_i, \quad Ax = b, \quad s \succeq 0$$

**Goal:** Optimal $$s^* = 0$$ ⟺ bài toán gốc feasible

**Advantage:** Identify which constraints are problematic

#### **Implementation**
- **Use barrier method:** For Phase I problems too
- **Lower accuracy:** Don't need high precision for feasibility
- **Infeasibility detection:** Trong Phase I cơ bản, nếu optimal $$s^* > 0$$ thì original problem infeasible; nếu $$s^* \ge 0$$ thì không có strictly feasible point

### 🛠️ **Implementation Details**

#### **Newton method for barrier problems**
**Gradient:** $$\nabla (tf + \phi) = t\nabla f - \sum_{i=1}^m \frac{1}{h_i(x)} \nabla h_i$$

**Hessian:** $$\nabla^2 (tf + \phi) = t\nabla^2 f + \sum_{i=1}^m \frac{1}{h_i^2(x)} \nabla h_i \nabla h_i^T - \sum_{i=1}^m \frac{1}{h_i(x)} \nabla^2 h_i$$

#### **Numerical considerations**
- **Stay strictly feasible:** Ensure $$h_i(x) < 0$$ throughout
- **Line search:** Backtracking to maintain feasibility
- **Conditioning:** Hessian becomes ill-conditioned as $$t$$ increases
- **Stopping criteria:** Use duality gap $$\frac{m}{t}$$

### 💡 **Ví Dụ: Linear Programming**

#### **LP problem**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

#### **Barrier formulation**
$$\min tc^T x - \sum_{i=1}^n \log x_i \quad \text{s.t.} \quad Ax = b$$

#### **Central path**
**KKT conditions:** $$tc + A^T \nu - X^{-1} e = 0, \quad Ax = b$$

với $$X = \text{diag}(x)$$, $$e = (1,\ldots,1)^T$$

**Interpretation:** $$x_i \lambda_i = \frac{1}{t}$$ (perturbed complementary slackness)

### 🎯 **Kết Nối Với Các Chương**

#### **Từ chương trước:**
- **Chương 14:** Newton method - foundation cho barrier method
- **Chương 12:** KKT conditions - perturbed KKT interpretation
- **Chương 11:** General duality - duality gap analysis

#### **Tầm quan trọng của Barrier Method:**
- **Interior point revolution:** Polynomial-time algorithms cho LP
- **Constrained optimization:** Practical method cho inequality constraints
- **Self-concordance:** Elegant theoretical framework
- **Real-world impact:** Standard in optimization software

#### **Hướng phát triển:**
- **Primal-dual methods:** Simultaneous primal-dual updates
- **Homogeneous methods:** Handle infeasible problems
- **Semidefinite programming:** Extension to matrix constraints
- **Large-scale applications:** Sparse matrix techniques

### 🌟 **Ý Nghĩa Lý Thuyết**

#### **Interior point paradigm:**
- **Avoid combinatorial complexity:** No active set identification
- **Polynomial-time:** $$O(n^3 \log(1/\epsilon))$$ for LP
- **Smooth approximation:** Differentiable barrier functions
- **Path-following:** Systematic approach to boundary

#### **Theoretical elegance:**
- **Self-concordance:** Affine-invariant analysis
- **Central path:** Geometric interpretation của optimization
- **Duality connection:** Perturbed KKT conditions
- **Convergence guarantees:** Rigorous complexity analysis

#### **Practical impact:**
- **Software revolution:** CPLEX, Gurobi use interior point
- **Large-scale problems:** Handle millions of variables
- **Robust performance:** Works across diverse problem classes
- **Warm start capability:** Efficient reoptimization

### 💡 **Mẹo Thực Hành**

#### **When to use barrier methods:**
1. **Many inequality constraints:** More efficient than active set
2. **Large-scale problems:** Polynomial-time complexity
3. **High accuracy needed:** Linear convergence to high precision
4. **Smooth problems:** Twice differentiable objectives và constraints

#### **Implementation tips:**
- **Maintain strict feasibility:** Never let $$h_i(x) \ge 0$$
- **Use warm starts:** Previous solution as initialization
- **Monitor conditioning:** Watch Hessian condition number
- **Adaptive parameters:** Adjust $$\mu$$ based on performance
- **Feasibility phase:** Always check for strictly feasible starting point

#### **Common pitfalls:**
- **Infeasible start:** Must begin with strictly feasible point
- **Poor conditioning:** Large $$t$$ makes Hessian ill-conditioned
- **Boundary approach:** Don't let iterates get too close to boundary
- **Parameter choice:** Extreme $$\mu$$ values can hurt performance

### 🔬 **Advanced Topics**

#### **Primal-dual interior point:**
- **Simultaneous updates:** Update both primal và dual variables
- **Predictor-corrector:** Mehrotra's algorithm
- **Homogeneous methods:** Handle infeasible problems
- **Higher-order methods:** Beyond Newton steps

#### **Extensions:**
- **Semidefinite programming:** Matrix inequality constraints
- **Second-order cone programming:** Conic constraints
- **Robust optimization:** Uncertainty sets
- **Stochastic programming:** Probabilistic constraints

#### **Large-scale techniques:**
- **Sparse linear algebra:** Exploit problem structure
- **Iterative methods:** CG for Newton systems
- **Preconditioning:** Improve conditioning
- **Parallel computation:** Distributed implementations

### 📈 **Ứng Dụng Thực Tế**

#### **Linear và Quadratic Programming:**
- **Portfolio optimization:** Risk-return trade-offs
- **Production planning:** Resource allocation
- **Network flows:** Transportation problems
- **Machine learning:** SVM training

#### **Engineering Design:**
- **Structural optimization:** Weight minimization
- **Control systems:** Optimal control
- **Signal processing:** Filter design
- **Image processing:** Reconstruction problems

#### **Finance và Economics:**
- **Risk management:** Value-at-Risk optimization
- **Algorithmic trading:** Execution strategies
- **Auction design:** Mechanism optimization
- **Market equilibrium:** Economic modeling

#### **Machine Learning:**
- **Regularized regression:** L1, L2 penalties
- **Neural network training:** Constrained optimization
- **Kernel methods:** SVM và variants
- **Matrix completion:** Low-rank optimization

### 🔮 **Future Directions**

#### **Algorithmic developments:**
- **Quantum interior point:** Quantum optimization algorithms
- **Distributed methods:** Parallel barrier methods
- **Online algorithms:** Streaming optimization
- **Adaptive methods:** Problem-specific adaptations

#### **Application areas:**
- **Deep learning:** Constrained neural network training
- **Autonomous systems:** Real-time optimization
- **Smart grids:** Energy optimization
- **Bioinformatics:** Computational biology problems

### 💎 **Key Insights**

#### **Barrier method contributions:**
1. **Interior approach:** Avoid boundary complexity
2. **Polynomial-time:** Theoretical breakthrough cho LP
3. **Practical efficiency:** Handle large-scale problems
4. **Smooth approximation:** Enable Newton methods

#### **Practical impact:**
- **Software standard:** Foundation của modern solvers
- **Industrial applications:** Optimization across industries
- **Research foundation:** Basis cho advanced methods
- **Educational value:** Elegant theory-practice connection

### 🌟 **Legacy của chương 15:**

- **Algorithmic revolution:** Interior point methods
- **Theoretical breakthrough:** Polynomial-time linear programming
- **Practical impact:** Large-scale optimization capability
- **Software influence:** Standard in commercial solvers
- **Educational significance:** Beautiful theory-practice synthesis

---

💡 **Thông điệp cuối cùng:** Barrier Method không chỉ là clever approximation technique - nó là **paradigm shift** từ boundary-based sang interior-based optimization, enabling polynomial-time algorithms và practical solution của large-scale constrained problems!

---


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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về Barrier method, bao gồm interior point methods, log barrier function, central path, convergence analysis và feasibility methods.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🚧 Quiz: Phương Pháp Rào Cản & Điểm Trong</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Barrier method concept -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Barrier method giải quyết inequality constraints bằng cách:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Chuyển thành equality constraints</label>
                <label><input type="radio" name="q1" value="b"> B) Thêm barrier function vào objective</label>
                <label><input type="radio" name="q1" value="c"> C) Loại bỏ constraints</label>
                <label><input type="radio" name="q1" value="d"> D) Sử dụng penalty method</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Thêm barrier function vào objective</strong><br>
                Barrier method thêm barrier function để "đẩy" solution vào interior của feasible region, tránh vi phạm constraints.
            </div>
        </div>

        <!-- Câu hỏi 2: Log barrier function -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Log barrier function cho constraint \(g_i(x) \leq 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(-\log(-g_i(x))\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\log(g_i(x))\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(-\log(g_i(x))\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\log(-g_i(x))\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$-\log(-g_i(x))$$</strong><br>
                Log barrier function $$-\log(-g_i(x))$$ đảm bảo $$g_i(x) < 0$$ và tăng đến $$+\infty$$ khi approach boundary.
            </div>
        </div>

        <!-- Câu hỏi 3: Barrier problem -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Barrier problem có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(\min tf(x) + \phi(x)\) subject to \(Ax = b\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\min f(x) + t\phi(x)\) subject to \(Ax = b\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(\min f(x) - t\phi(x)\) subject to \(Ax = b\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(\min f(x)\) subject to \(Ax = b, g(x) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min tf(x) + \phi(x)$$ subject to $$Ax = b$$</strong><br>
                Barrier problem có parameter $$t > 0$$, khi $$t \to \infty$$ thì solution approach original problem.
            </div>
        </div>

        <!-- Câu hỏi 4: Central path -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Central path là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Tập hợp \(\{x^*(t) | t > 0\}\) với \(x^*(t)\) là solution của barrier problem</label>
                <label><input type="radio" name="q4" value="b"> B) Đường thẳng từ starting point đến optimal</label>
                <label><input type="radio" name="q4" value="c"> C) Center của feasible region</label>
                <label><input type="radio" name="q4" value="d"> D) Gradient descent path</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tập hợp $$\{x^*(t) | t > 0\}$$ với $$x^*(t)$$ là solution của barrier problem</strong><br>
                Central path là trajectory của optimal solutions khi parameter $$t$$ thay đổi từ 0 đến $$\infty$$.
            </div>
        </div>

        <!-- Câu hỏi 5: Central path properties -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Khi \(t \to \infty\), central path:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Hội tụ về optimal solution của original problem</label>
                <label><input type="radio" name="q5" value="b"> B) Diverge</label>
                <label><input type="radio" name="q5" value="c"> C) Oscillate</label>
                <label><input type="radio" name="q5" value="d"> D) Approach boundary</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Hội tụ về optimal solution của original problem</strong><br>
                Khi $$t \to \infty$$, barrier term $$\phi(x)$$ trở nên negligible, solution approach original optimal $$x^*$$.
            </div>
        </div>

        <!-- Câu hỏi 6: KKT conditions for barrier -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: KKT conditions cho barrier problem tại \(x^*(t)\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(t\nabla f(x) + \sum \frac{1}{-g_i(x)} \nabla g_i(x) + A^T\nu = 0\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(\nabla f(x) + \sum \lambda_i \nabla g_i(x) + A^T\nu = 0\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(t\nabla f(x) = 0\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\nabla f(x) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$t\nabla f(x) + \sum \frac{1}{-g_i(x)} \nabla g_i(x) + A^T\nu = 0$$</strong><br>
                Gradient của barrier objective: $$t\nabla f(x) + \nabla \phi(x) + A^T\nu = 0$$ với $$\nabla \phi(x) = \sum \frac{1}{-g_i(x)} \nabla g_i(x)$$.
            </div>
        </div>

        <!-- Câu hỏi 7: Dual variables interpretation -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Dual variables trong barrier method có quan hệ:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(\lambda_i^*(t) = \frac{1}{t(-g_i(x^*(t)))}\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(\lambda_i^*(t) = t(-g_i(x^*(t)))\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(\lambda_i^*(t) = -g_i(x^*(t))\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(\lambda_i^*(t) = \frac{1}{-g_i(x^*(t))}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\lambda_i^*(t) = \frac{1}{t(-g_i(x^*(t)))}$$</strong><br>
                Dual variables từ barrier method: $$\lambda_i^*(t) = \frac{1}{t(-g_i(x^*(t)))}$$, approach true dual khi $$t \to \infty$$.
            </div>
        </div>

        <!-- Câu hỏi 8: Duality gap -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Duality gap trong barrier method là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\frac{m}{t}\) với \(m\) là số inequality constraints</label>
                <label><input type="radio" name="q8" value="b"> B) \(\frac{1}{t}\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(mt\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(t\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\frac{m}{t}$$ với $$m$$ là số inequality constraints</strong><br>
                Duality gap $$\eta = f(x^*(t)) - g(\lambda^*(t), \nu^*(t)) = \frac{m}{t}$$, giảm khi tăng $$t$$.
            </div>
        </div>

        <!-- Câu hỏi 9: Barrier method algorithm -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Barrier method algorithm:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Tăng \(t\) theo sequence, solve barrier problem mỗi \(t\)</label>
                <label><input type="radio" name="q9" value="b"> B) Giảm \(t\) theo sequence</label>
                <label><input type="radio" name="q9" value="c"> C) Giữ \(t\) cố định</label>
                <label><input type="radio" name="q9" value="d"> D) Random \(t\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tăng $$t$$ theo sequence, solve barrier problem mỗi $$t$$</strong><br>
                Algorithm: start với $$t^{(0)}$$, solve barrier problem, update $$t^{(k+1)} = \mu t^{(k)}$$ với $$\mu > 1$$.
            </div>
        </div>

        <!-- Câu hỏi 10: Centering step -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Centering step trong barrier method là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Giải barrier problem cho \(t\) cố định bằng Newton method</label>
                <label><input type="radio" name="q10" value="b"> B) Tìm center của feasible region</label>
                <label><input type="radio" name="q10" value="c"> C) Update parameter \(t\)</label>
                <label><input type="radio" name="q10" value="d"> D) Check feasibility</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Giải barrier problem cho $$t$$ cố định bằng Newton method</strong><br>
                Centering step solve $$\min tf(x) + \phi(x)$$ subject to $$Ax = b$$ để tìm $$x^*(t)$$ trên central path.
            </div>
        </div>

        <!-- Câu hỏi 11: Self-concordance of log barrier -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Với \(g_i\) affine, log barrier function \(-\log(-g_i(x))\) có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Self-concordant</label>
                <label><input type="radio" name="q11" value="b"> B) Convex</label>
                <label><input type="radio" name="q11" value="c"> C) Smooth</label>
                <label><input type="radio" name="q11" value="d"> D) Tất cả các tính chất trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các tính chất trên</strong><br>
                Với $$g_i$$ affine, log barrier function vừa convex, smooth, vừa self-concordant, làm cho Newton method có convergence guarantees. (Với $$g_i$$ lồi tổng quát, barrier vẫn convex và smooth nhưng không nhất thiết self-concordant.)
            </div>
        </div>

        <!-- Câu hỏi 12: Feasibility methods -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Phase I problem để tìm feasible starting point:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) \(\min s\) subject to \(g_i(x) \leq s, Ax = b\)</label>
                <label><input type="radio" name="q12" value="b"> B) \(\min \|g(x)\|\)</label>
                <label><input type="radio" name="q12" value="c"> C) \(\min f(x)\)</label>
                <label><input type="radio" name="q12" value="d"> D) \(\min \|x\|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min s$$ subject to $$g_i(x) \leq s, Ax = b$$</strong><br>
                Phase I tìm feasible point bằng cách minimize slack variable $$s$$. Nếu optimal $$s^* < 0$$ thì có strictly feasible point; nếu $$s^* > 0$$ thì bài toán infeasible.
            </div>
        </div>

        <!-- Câu hỏi 13: Convergence rate -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Số outer iterations của barrier method để đạt accuracy \(\epsilon\):</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(O(\log(1/\epsilon))\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(O(1/\epsilon)\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(O(\sqrt{1/\epsilon})\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(O(1/\epsilon^2)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$O(\log(1/\epsilon))$$</strong><br>
                Với update rule $$t^{(k+1)} = \mu t^{(k)}$$, cần $$O(\log(1/\epsilon))$$ outer iterations để reduce duality gap.
            </div>
        </div>

        <!-- Câu hỏi 14: Newton decrement in barrier -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Newton decrement trong barrier method được dùng để:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Stopping criterion cho centering step</label>
                <label><input type="radio" name="q14" value="b"> B) Update parameter \(t\)</label>
                <label><input type="radio" name="q14" value="c"> C) Check feasibility</label>
                <label><input type="radio" name="q14" value="d"> D) Compute duality gap</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Stopping criterion cho centering step</strong><br>
                Newton decrement $$\lambda(x) \leq \eta$$ là stopping criterion để đảm bảo $$x$$ đủ gần central path trước khi update $$t$$.
            </div>
        </div>

        <!-- Câu hỏi 15: Primal-dual methods -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Primal-dual interior point methods khác barrier method ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Update cả primal và dual variables simultaneously</label>
                <label><input type="radio" name="q15" value="b"> B) Không cần central path</label>
                <label><input type="radio" name="q15" value="c"> C) Chỉ dùng cho linear programs</label>
                <label><input type="radio" name="q15" value="d"> D) Không cần Newton method</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Update cả primal và dual variables simultaneously</strong><br>
                Primal-dual methods update $$(x, \lambda, \nu)$$ cùng lúc thay vì chỉ solve cho $$x$$ như barrier method.
            </div>
        </div>

        <!-- Câu hỏi 16: Barrier parameter update -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Typical choice cho barrier parameter update:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(t^{(k+1)} = \mu t^{(k)}\) với \(\mu = 10\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(t^{(k+1)} = t^{(k)} + 1\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(t^{(k+1)} = 2t^{(k)}\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(t^{(k+1)} = t^{(k)}^2\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$t^{(k+1)} = \mu t^{(k)}$$ với $$\mu = 10$$</strong><br>
                Thường chọn $$\mu = 10$$ để balance giữa số outer iterations và computational cost mỗi centering step.
            </div>
        </div>

        <!-- Câu hỏi 17: Barrier method advantages -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Ưu điểm của barrier method:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Polynomial-time complexity</label>
                <label><input type="radio" name="q17" value="b"> B) Warm-start capability</label>
                <label><input type="radio" name="q17" value="c"> C) Handle inequality constraints naturally</label>
                <label><input type="radio" name="q17" value="d"> D) Tất cả các ưu điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ưu điểm trên</strong><br>
                Barrier method có polynomial complexity, support warm-start, và handle inequality constraints một cách tự nhiên.
            </div>
        </div>

        <!-- Câu hỏi 18: Linear programming barrier -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Cho LP: \(\min c^Tx\) s.t. \(Ax = b, x \geq 0\). Barrier function là:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) \(-\sum_{i=1}^n \log x_i\)</label>
                <label><input type="radio" name="q18" value="b"> B) \(\sum_{i=1}^n \log x_i\)</label>
                <label><input type="radio" name="q18" value="c"> C) \(-\sum_{i=1}^n x_i\)</label>
                <label><input type="radio" name="q18" value="d"> D) \(\sum_{i=1}^n x_i^2\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$-\sum_{i=1}^n \log x_i$$</strong><br>
                Cho constraints $$x_i \geq 0$$, log barrier function là $$-\sum_{i=1}^n \log x_i$$ để enforce $$x_i > 0$$.
            </div>
        </div>

        <!-- Câu hỏi 19: Barrier method vs penalty method -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Barrier method khác penalty method ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Barrier giữ solution trong feasible region</label>
                <label><input type="radio" name="q19" value="b"> B) Penalty cho phép vi phạm constraints</label>
                <label><input type="radio" name="q19" value="c"> C) Barrier cần feasible starting point</label>
                <label><input type="radio" name="q19" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Barrier method maintain feasibility, cần feasible start, khác với penalty method cho phép constraint violations.
            </div>
        </div>

        <!-- Câu hỏi 20: Applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Interior point methods được ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Linear programming solvers</label>
                <label><input type="radio" name="q20" value="b"> B) Semidefinite programming</label>
                <label><input type="radio" name="q20" value="c"> C) Convex optimization packages</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các ứng dụng trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ứng dụng trên</strong><br>
                Interior point methods là foundation của modern optimization solvers: CPLEX, Gurobi, CVX, MOSEK.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Barrier method biến đổi bài toán có ràng buộc thành:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Chuỗi bài toán không ràng buộc</label>
                <label><input type="radio" name="q21" value="b"> B) Bài toán tuyến tính</label>
                <label><input type="radio" name="q21" value="c"> C) Bài toán QP</label>
                <label><input type="radio" name="q21" value="d"> D) Bài toán SDP</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Chuỗi bài toán không ràng buộc</strong><br>
                Barrier method: $$\min t f(x) + \phi(x)$$ (tương đương $$\min f(x) + \frac{1}{t}\phi(x)$$) với $$\phi$$ là barrier function, $$t \to \infty$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Logarithmic barrier cho ràng buộc $$g_i(x) \leq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$-\sum \log(-g_i(x))$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$\sum \log(g_i(x))$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$\sum g_i(x)^2$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$\sum |g_i(x)|$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$-\sum \log(-g_i(x))$$</strong><br>
                Log barrier: $$\phi(x) = -\sum_{i=1}^m \log(-g_i(x))$$ với $$g_i(x) < 0$$.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Central path trong barrier method là:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Tập nghiệm của $$t\nabla f + \nabla \phi + A^T\nu = 0$$</label>
                <label><input type="radio" name="q23" value="b"> B) Đường thẳng qua nghiệm</label>
                <label><input type="radio" name="q23" value="c"> C) Biên của miền khả thi</label>
                <label><input type="radio" name="q23" value="d"> D) Đường gradient descent</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tập nghiệm của $$t\nabla f + \nabla \phi + A^T\nu = 0$$</strong><br>
                Central path: $$x^*(t)$$ thỏa mãn $$t\nabla f(x) + \nabla \phi(x) + A^T\nu = 0$$, $$Ax = b$$ với tham số $$t > 0$$.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Khi $$t \to \infty$$ trong barrier method:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Nghiệm tiến đến nghiệm tối ưu gốc</label>
                <label><input type="radio" name="q24" value="b"> B) Nghiệm phân kỳ</label>
                <label><input type="radio" name="q24" value="c"> C) Barrier function bằng 0</label>
                <label><input type="radio" name="q24" value="d"> D) Không có ý nghĩa</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Nghiệm tiến đến nghiệm tối ưu gốc</strong><br>
                Khi $$t \to \infty$$, nghiệm của bài toán barrier tiến đến nghiệm của bài toán gốc.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Cho ràng buộc $$x > 0$$, barrier function $$-\log x$$ có gradient:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$-1/x$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$1/x$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$-x$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$\log x$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$-1/x$$</strong><br>
                $$\frac{d}{dx}(-\log x) = -\frac{1}{x}$$.
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
    q1: 'b', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'd', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'a', q17: 'd', q18: 'a', q19: 'd', q20: 'd'
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
        message = '🌟 Xuất sắc! Bạn đã thành thạo barrier method và interior point optimization!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về central path và convergence analysis.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại log barrier function và duality gap.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại barrier problem và KKT conditions.';
    } else {
        message = '📖 Hãy học lại từ đầu về interior point methods nhé!';
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
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        MathJax.startup.promise.then(() => MathJax.typesetPromise());
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

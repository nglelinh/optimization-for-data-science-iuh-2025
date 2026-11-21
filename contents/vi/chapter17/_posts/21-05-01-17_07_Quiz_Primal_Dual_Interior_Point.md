---
layout: post
title: 17-07 Bài tập trắc nghiệm - Phương Pháp Điểm Trong Nguyên Thủy-Đối Ngẫu
chapter: '17'
order: 11
owner: GitHub Copilot
lang: vi
categories:
- chapter17
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter17/17_06_Quiz_Primal_Dual_Interior_Point/
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Primal-Dual Interior Point Method**

#### **Motivation và so sánh với Barrier Method**
**Barrier Method limitations:**
- **Multiple Newton steps:** Centering steps require many iterations
- **Must stay feasible:** Always maintain $$h_i(x) < 0$$
- **Sequential approach:** Solve sequence of barrier problems
- **Less efficient:** Many outer iterations needed

**Primal-Dual advantages:**
- **Single Newton step:** One Newton step per iteration
- **Infeasible start OK:** Can start from infeasible points (không cần $$Ax^0 = b$$; trong dạng này vẫn cần $$h(x^0) < 0, u^0 > 0$$)
- **Simultaneous updates:** Update primal và dual variables together
- **More efficient:** Generally superior performance

### 🎯 **Central Path Equations Revisited**

#### **Original KKT conditions**
$$\begin{align}
\nabla f(x) + \nabla h(x)u + A^T v &= 0 \\
Uh(x) &= 0 \\
Ax &= b \\
u \ge 0, \quad -h(x) &\ge 0
\end{align}$$

#### **Perturbed KKT conditions (Central Path)**
$$\begin{align}
\nabla f(x) + \nabla h(x)u + A^T v &= 0 \\
Uh(x) + \tau\mathbf{1} &= 0 \\
Ax - b &= 0 \\
u > 0, \quad -h(x) &> 0
\end{align}$$

#### **Key differences:**
- **Complementary slackness:** $$Uh(x) = 0$$ vs $$Uh(x) = -\tau\mathbf{1}$$
- **Feasibility:** $$\ge 0$$ vs $$> 0$$ (strict interior)
- **Parameter:** $$\tau = 1/t$$ controls perturbation level

#### **Duality gap property**
**Important fact:** Solution $$(x(\tau), u(\tau), v(\tau))$$ has duality gap:
$$f(x(\tau)) - \min_x L(x, u(\tau), v(\tau)) = m\tau = \frac{m}{t}$$

### 🔄 **Newton Step for Central Path**

#### **Residual function definition**
$$r(x,u,v) = \begin{bmatrix}
\nabla f(x) + \nabla h(x)u + A^T v \\
Uh(x) + \tau\mathbf{1} \\
Ax - b
\end{bmatrix}$$

#### **Newton system**
$$\begin{bmatrix}
\nabla^2 f(x) + \sum u_i \nabla^2 h_i(x) & \nabla h(x) & A^T \\
U \nabla h(x)^T & H(x) & 0 \\
A & 0 & 0
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta u \\
\Delta v
\end{bmatrix} = -r(x,u,v)$$

với $$H(x) = \text{diag}(h(x))$$, $$U = \text{diag}(u)$$

#### **Solution interpretation**
- $$(\Delta x, \Delta u, \Delta v)$$: Newton direction
- **Simultaneous update:** Both primal ($$x$$) và dual ($$u,v$$) variables
- **Root finding:** Solve $$r(x,u,v) = 0$$ using Newton method

### 📊 **Residuals và Surrogate Duality Gap**

#### **Three types of residuals**
1. **Dual residual:** $$r_{\text{dual}} = \nabla f(x) + \nabla h(x)u + A^T v$$
2. **Central residual:** $$r_{\text{cent}} = Uh(x) + \tau\mathbf{1}$$
3. **Primal residual:** $$r_{\text{prim}} = Ax - b$$

#### **Residual interpretations**
- **$$r_{\text{dual}} = 0$$:** Dual feasibility ($$u,v$$ in domain of $$g$$)
- **$$r_{\text{prim}} = 0$$:** Primal feasibility
- **$$r_{\text{cent}} = 0$$:** Complementary slackness with perturbation $$\tau$$

#### **Surrogate duality gap**
**Definition:** $$-h(x)^T u$$ for $$h(x) \le 0, u \ge 0$$

**Properties:**
- **If feasible:** Surrogate gap = true duality gap = $$m\tau$$
- **Parameter relationship:** $$t = -\frac{m}{h(x)^T u}$$
- **Central path condition:** $$r(x,u,v) = 0$$ for $$\tau = -\frac{h(x)^T u}{m}$$

### 🔄 **Primal-Dual Algorithm**

#### **Parameter definitions**
- $$\tau(x,u) = -\frac{h(x)^T u}{m}$$ (current perturbation)
- $$\sigma \in (0,1)$$ (centering parameter, $$\sigma = 1/\mu$$)
- $$\tau = \sigma \tau(x^k, u^k)$$ (target perturbation)

#### **Algorithm steps**
1. **Choose parameters:** $$\sigma \in (0,1)$$
2. **Initialize:** $$(x^0, u^0, v^0)$$ với $$h(x^0) < 0, u^0 > 0$$
3. **Main loop:** For $$k = 0, 1, 2, \ldots$$
   - **Compute Newton step:** Solve for $$(\Delta x, \Delta u, \Delta v)$$
   - **Backtracking line search:** Find step size $$\theta_k$$
   - **Update:** $$(x^{k+1}, u^{k+1}, v^{k+1}) = (x^k, u^k, v^k) + \theta_k(\Delta x, \Delta u, \Delta v)$$
4. **Termination:** Stop when $$-h(x)^T u \le \epsilon$$ và $$\lVert r_{\text{prim}} \rVert^2 + \lVert r_{\text{dual}} \rVert^2 \le \epsilon^2$$

### 🎯 **Multi-Stage Backtracking Line Search**

#### **Stage 1: Dual feasibility ($$u > 0$$)**
$$\theta_{\max} = \min\left\{1, \min\left\{-\frac{u_i}{\Delta u_i} : \Delta u_i < 0\right\}\right\}$$

**Goal:** Ensure $$u + \theta \Delta u \ge 0$$

#### **Stage 2: Primal feasibility ($$h(x) < 0$$)**
- Start với $$\theta = 0.99\theta_{\max}$$
- Update $$\theta = \beta\theta$$ until $$h_i(x^+) < 0$$ for all $$i$$

**Goal:** Ensure $$h(x + \theta \Delta x) < 0$$

#### **Stage 3: Residual reduction**
Update $$\theta = \beta\theta$$ until:
$$\|r(x^+, u^+, v^+)\| \le (1 - \alpha\theta)\|r(x, u, v)\|$$

**Goal:** Sufficient decrease in residual norm

#### **Parameters**
- $$\alpha, \beta \in (0,1)$$ (typical: $$\alpha = 0.01, \beta = 0.5$$)
- **Multi-objective:** Maintain feasibility + reduce residuals

### 📈 **Linear Programming Special Case**

#### **Primal LP**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

#### **Dual LP**
$$\max b^T y \quad \text{s.t.} \quad A^T y + s = c, \quad s \ge 0$$

#### **Central path conditions**
$$\begin{align}
A^T y + s &= c \\
Ax &= b \\
XS\mathbf{1} &= \tau\mathbf{1} \\
x, s &> 0
\end{align}$$

với $$X = \text{diag}(x)$$, $$S = \text{diag}(s)$$

#### **Newton system for LP**
$$\begin{bmatrix}
0 & A^T & I \\
A & 0 & 0 \\
S & 0 & X
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta y \\
\Delta s
\end{bmatrix} = -\begin{bmatrix}
A^T y + s - c \\
Ax - b \\
XS\mathbf{1} - \tau\mathbf{1}
\end{bmatrix}$$

#### **Relationship to barrier methods**
- **Primal barrier:** $$x = \tau S^{-1}\mathbf{1}$$
- **Dual barrier:** $$s = \tau X^{-1}\mathbf{1}$$
- **Primal-dual:** Simultaneous updates of both

### 📊 **Semidefinite Programming (SDP)**

#### **Primal SDP**
$$\min C \bullet X \quad \text{s.t.} \quad \mathcal{A}(X) = b, \quad X \succeq 0$$

#### **Dual SDP**
$$\max b^T y \quad \text{s.t.} \quad \mathcal{A}^*(y) + S = C, \quad S \succeq 0$$

#### **Central path conditions**
$$\begin{align}
\mathcal{A}^*(y) + S &= C \\
\mathcal{A}(X) &= b \\
XS &= \tau I \\
X, S &\succ 0
\end{align}$$

#### **Newton system for SDP**
$$\begin{bmatrix}
0 & \mathcal{A}^* & I \\
\mathcal{A} & 0 & 0 \\
S & 0 & X
\end{bmatrix}
\begin{bmatrix}
\Delta X \\
\Delta y \\
\Delta S
\end{bmatrix} = -\begin{bmatrix}
\mathcal{A}^*(y) + S - C \\
\mathcal{A}(X) - b \\
XS - \tau I
\end{bmatrix}$$

#### **Matrix operations**
- $$X \bullet S = \text{tr}(XS)$$ (trace inner product)
- $$XS = \tau I$$ (matrix complementary slackness)
- $$\mathcal{A}: \mathbb{S}^n \to \mathbb{R}^m$$ (linear map)

### 🔄 **Comparison: Barrier vs Primal-Dual**

| **Aspect** | **Barrier Method** | **Primal-Dual Method** |
|------------|-------------------|------------------------|
| **Newton steps** | Multiple per centering | Single per iteration |
| **Feasibility** | Must maintain | Can start infeasible |
| **Variables** | Primal only | Primal + dual simultaneous |
| **Convergence** | Linear | Often superlinear |
| **Efficiency** | Good | Generally superior |
| **Intuition** | Clear (central path) | Less intuitive |

### 🎯 **Performance Analysis**

#### **Theoretical advantages**
- **Polynomial-time:** $$O(\sqrt{n}\log(1/\epsilon))$$ iterations, tổng $$O(n^{3.5} \log(1/\epsilon))$$ complexity
- **Superlinear convergence:** Under appropriate conditions
- **Robust performance:** Works across problem classes
- **Infeasible start:** No need for Phase I (chỉ cần điểm trong strict interior của ràng buộc bất đẳng thức)

#### **Practical benefits**
- **Fewer iterations:** Compared to barrier method
- **Higher accuracy:** Can achieve very high precision
- **Warm starts:** Efficient reoptimization
- **Large-scale capability:** Handle millions of variables

#### **Experimental results (LP example)**
- **Standard LP:** $$n = 50, m = 100$$
- **Primal-dual:** Fixed $$\mu = 10$$, fast convergence
- **Barrier:** Various $$\mu$$ values, more iterations needed
- **Accuracy:** Primal-dual achieves higher precision

### 🛠️ **Implementation Considerations**

#### **Linear system solution**
- **Sparse factorization:** Exploit problem structure
- **Iterative methods:** For very large problems
- **Numerical stability:** Monitor condition numbers
- **Regularization:** Handle near-singular systems

#### **Step size selection**
- **Conservative factors:** 0.99 for feasibility margin
- **Adaptive parameters:** Adjust $$\alpha, \beta$$ based on performance
- **Feasibility monitoring:** Ensure strict interior maintenance
- **Convergence tracking:** Monitor residual norms

#### **Stopping criteria**
- **Duality gap:** $$-h(x)^T u \le \epsilon$$
- **Feasibility:** $$\lVert r_{\text{prim}} \rVert^2 + \lVert r_{\text{dual}} \rVert^2 \le \epsilon^2$$
- **Relative criteria:** Scale by problem data
- **Multiple conditions:** All must be satisfied

### 🎯 **Kết Nối Với Các Chương**

#### **From previous chapters:**
- **Chương 15:** Barrier method foundation
- **Chương 16:** Duality theory, perturbed KKT
- **Chương 14:** Newton method for root finding
- **Chương 12:** KKT conditions framework

#### **Advanced connections:**
- **Central path:** Geometric interpretation of optimization
- **Perturbed optimality:** Bridge between exact và approximate
- **Simultaneous updates:** Primal-dual variable coordination
- **Polynomial-time algorithms:** Theoretical complexity guarantees

#### **Practical applications:**
- **Commercial solvers:** CPLEX, Gurobi, Mosek
- **Large-scale optimization:** Industrial applications
- **Machine learning:** SVM, regularized regression
- **Engineering design:** Control, signal processing

### 🌟 **Ý Nghĩa Lý Thuyết**

#### **Algorithmic innovation:**
- **Primal-dual paradigm:** Simultaneous variable updates
- **Infeasible start capability:** No Phase I required
- **Superlinear convergence:** Beyond linear rates
- **Unified framework:** Works for LP, QP, SDP

#### **Theoretical elegance:**
- **Central path following:** Smooth trajectory to optimality
- **Perturbed KKT:** Systematic perturbation approach
- **Polynomial-time guarantee:** Worst-case complexity bounds
- **Self-dual structure:** Exploits problem symmetry

#### **Practical impact:**
- **Software revolution:** Foundation of modern solvers
- **Industrial applications:** Large-scale optimization capability
- **Research foundation:** Basis for advanced methods
- **Educational value:** Beautiful theory-practice connection

### 💡 **Mẹo Thực Hành**

#### **When to use primal-dual methods:**
1. **Large-scale problems:** More efficient than barrier methods
2. **High accuracy needed:** Can achieve very high precision
3. **Infeasible start:** When feasible starting point hard to find
4. **Warm starts:** Efficient reoptimization scenarios

#### **Parameter selection:**
- **$$\sigma$$:** Thường từ 0.1 đến 0.9 (0.1 để tiến nhanh, 0.9 để ổn định)
- **$$\alpha, \beta$$:** Standard values 0.01, 0.5 work well
- **$$\epsilon$$:** Problem-dependent tolerance
- **Feasibility margin:** 0.99 factor for numerical stability

#### **Implementation tips:**
- **Sparse linear algebra:** Essential for large problems
- **Numerical conditioning:** Monitor và regularize if needed
- **Convergence monitoring:** Track multiple criteria
- **Warm starts:** Use previous solutions as initialization

#### **Common pitfalls:**
- **Poor conditioning:** Large problems may have numerical issues
- **Step size too aggressive:** Can lead to infeasibility
- **Inadequate stopping criteria:** May terminate prematurely
- **Memory requirements:** Large Newton systems need careful handling

### 🔬 **Advanced Topics**

#### **Mehrotra's predictor-corrector:**
- **Predictor step:** Estimate progress along central path
- **Corrector step:** Adjust for better centering
- **Adaptive $$\sigma$$:** Dynamic centering parameter
- **Superior performance:** State-of-the-art implementation

#### **Homogeneous methods:**
- **Infeasibility detection:** Distinguish infeasible from unbounded
- **Unified treatment:** Handle all problem types
- **Theoretical completeness:** Covers all cases
- **Practical robustness:** More reliable than standard methods

#### **Higher-order methods:**
- **Beyond Newton:** Higher-order corrections
- **Faster convergence:** Potential for cubic convergence
- **Computational trade-offs:** More work per iteration
- **Research frontier:** Active area of development

### 📈 **Ứng Dụng Thực Tế**

#### **Linear và Quadratic Programming:**
- **Portfolio optimization:** Large-scale mean-variance models
- **Network flows:** Transportation và communication
- **Production planning:** Resource allocation problems
- **Machine learning:** SVM training, regularized regression

#### **Semidefinite Programming:**
- **Control theory:** LMI-based controller design
- **Combinatorial optimization:** SDP relaxations
- **Machine learning:** Kernel methods, matrix completion
- **Signal processing:** Beamforming, robust filtering

#### **Engineering Applications:**
- **Structural optimization:** Truss design, topology optimization
- **Circuit design:** Analog circuit sizing
- **Power systems:** Optimal power flow
- **Robotics:** Motion planning, control

#### **Finance và Economics:**
- **Risk management:** Value-at-Risk optimization
- **Algorithmic trading:** Execution optimization
- **Market design:** Auction mechanisms
- **Insurance:** Portfolio optimization

### 🔮 **Future Directions**

#### **Algorithmic developments:**
- **Distributed methods:** Parallel primal-dual algorithms
- **Online algorithms:** Streaming optimization
- **Stochastic methods:** Uncertainty handling
- **Quantum algorithms:** Quantum optimization

#### **Application areas:**
- **Deep learning:** Neural network training
- **Autonomous systems:** Real-time optimization
- **Smart grids:** Energy system optimization
- **Bioinformatics:** Computational biology

#### **Theoretical advances:**
- **Non-convex extensions:** Beyond convex optimization
- **Robust optimization:** Worst-case analysis
- **Multi-objective:** Pareto optimization
- **Dynamic optimization:** Time-varying problems

### 💎 **Key Insights**

#### **Primal-dual advantages:**
1. **Simultaneous updates:** Both primal và dual variables
2. **Infeasible start:** No Phase I required
3. **Superior efficiency:** Fewer iterations than barrier methods
4. **High accuracy:** Can achieve very high precision

#### **Algorithmic elegance:**
- **Newton framework:** Root finding for perturbed KKT
- **Multi-stage line search:** Systematic feasibility maintenance
- **Residual minimization:** Clear optimization objective
- **Polynomial-time guarantee:** Theoretical complexity bounds

#### **Practical power:**
- **Commercial software:** Foundation of modern solvers
- **Large-scale capability:** Handle millions of variables
- **Robust performance:** Works across diverse problems
- **Industrial impact:** Enables complex optimization applications

### 🌟 **Legacy của chương 17:**

- **Algorithmic breakthrough:** Primal-dual interior point revolution
- **Theoretical completeness:** Unified framework for convex optimization
- **Practical impact:** Foundation of commercial optimization software
- **Industrial transformation:** Large-scale optimization capability
- **Educational significance:** Beautiful synthesis of theory và practice

### 🎯 **Takeaway messages:**

1. **Primal-dual is superior:** More efficient than pure barrier methods
2. **Simultaneous updates:** Key to algorithmic efficiency
3. **Infeasible start OK:** No need for feasible initialization
4. **Polynomial-time guarantee:** Theoretical và practical efficiency
5. **Commercial foundation:** Basis of modern optimization software

### 💫 **Philosophical impact:**

Chương 17 **completes interior point revolution**:
- **From primal-only to primal-dual:** Simultaneous variable updates
- **From feasible to infeasible start:** Greater algorithmic flexibility
- **From barrier to direct approach:** More efficient path following
- **From academic to commercial:** Industrial optimization software
- **From theory to practice:** Complete optimization framework

### 🔮 **Synthesis:**

Primal-Dual Interior Point Method represents **culmination** của interior point approach:
- **Theoretical elegance:** Perturbed KKT conditions framework
- **Algorithmic efficiency:** Simultaneous primal-dual updates
- **Practical power:** Foundation of commercial software
- **Industrial impact:** Large-scale optimization capability
- **Educational value:** Beautiful theory-practice synthesis

### 💡 **Final insight:**

Chương 17 demonstrates that **optimization theory can be both beautiful và practical**. From perturbed KKT conditions đến Newton systems, từ central path following đến multi-stage line search, từ theoretical polynomial-time guarantees đến commercial software implementations - **primal-dual interior point methods represent perfect marriage** của mathematical elegance với computational efficiency.

**Primal-Dual = Simultaneous optimization of dual perspectives!**

---

💡 **Thông điệp cuối cùng:** Primal-Dual Interior Point Method không chỉ là algorithmic improvement - nó là **completion của interior point revolution**, enabling both theoretical understanding và practical solution của large-scale optimization problems across science, engineering, finance, và technology!

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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về Primal-Dual Interior Point Method, bao gồm primal-dual algorithms, central path equations, semidefinite programming và advanced interior point concepts.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>⚡ Quiz: Primal-Dual Interior Point Method</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Primal-dual vs barrier method -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Primal-dual interior point method khác barrier method ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Update cả primal và dual variables simultaneously</label>
                <label><input type="radio" name="q1" value="b"> B) Chỉ cần one Newton step per iteration</label>
                <label><input type="radio" name="q1" value="c"> C) Không cần feasible starting point</label>
                <label><input type="radio" name="q1" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Primal-dual methods update cả primal và dual, thường chỉ cần 1 Newton step, và có thể start từ infeasible points.
            </div>
        </div>

        <!-- Câu hỏi 2: Central path equations -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Central path equations cho inequality constraints $$g_i(x) \leq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) $$\nabla f(x) + \sum \lambda_i \nabla g_i(x) = 0, \lambda_i g_i(x) = -\frac{1}{t}$$</label>
                <label><input type="radio" name="q2" value="b"> B) $$\nabla f(x) + \sum \lambda_i \nabla g_i(x) = 0, \lambda_i g_i(x) = 0$$</label>
                <label><input type="radio" name="q2" value="c"> C) $$\nabla f(x) = 0, g_i(x) = 0$$</label>
                <label><input type="radio" name="q2" value="d"> D) $$\lambda_i = \frac{1}{t}, g_i(x) = -1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\nabla f(x) + \sum \lambda_i \nabla g_i(x) = 0, \lambda_i g_i(x) = -\frac{1}{t}$$</strong><br>
                Central path equations: stationarity condition và modified complementary slackness với parameter $$t$$.
            </div>
        </div>

        <!-- Câu hỏi 3: Newton system -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Newton system trong primal-dual method solve cho:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$(\Delta x, \Delta \lambda, \Delta \nu)$$ - directions cho cả primal và dual</label>
                <label><input type="radio" name="q3" value="b"> B) Chỉ $$\Delta x$$ - primal direction</label>
                <label><input type="radio" name="q3" value="c"> C) Chỉ $$\Delta \lambda$$ - dual direction</label>
                <label><input type="radio" name="q3" value="d"> D) Parameter $$t$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$(\Delta x, \Delta \lambda, \Delta \nu)$$ - directions cho cả primal và dual</strong><br>
                Newton system solve simultaneously cho primal direction $$\Delta x$$ và dual directions $$\Delta \lambda, \Delta \nu$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Surrogate duality gap -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Surrogate duality gap trong primal-dual method là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$\eta = -\sum_{i=1}^m \lambda_i g_i(x)$$</label>
                <label><input type="radio" name="q4" value="b"> B) \(\eta = f(x) - g(\lambda, \nu)\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(\eta = \|\nabla f(x)\|\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(\eta = \sum_{i=1}^m |\lambda_i|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\eta = -\sum_{i=1}^m \lambda_i g_i(x)$$</strong><br>
                Surrogate duality gap estimate duality gap từ current primal-dual point, không cần compute dual function.
            </div>
        </div>

        <!-- Câu hỏi 5: Residuals -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Residuals trong primal-dual method gồm:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Dual residual, primal residual, centrality residual</label>
                <label><input type="radio" name="q5" value="b"> B) Chỉ dual residual</label>
                <label><input type="radio" name="q5" value="c"> C) Chỉ primal residual</label>
                <label><input type="radio" name="q5" value="d"> D) Chỉ centrality residual</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Dual residual, primal residual, centrality residual</strong><br>
                Ba residuals: dual (stationarity), primal (feasibility), centrality (complementary slackness).
            </div>
        </div>

        <!-- Câu hỏi 6: Predictor-corrector -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Predictor-corrector method trong primal-dual:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) Predictor step giảm duality gap, corrector step improve centrality</label>
                <label><input type="radio" name="q6" value="b"> B) Predictor step tăng feasibility, corrector step giảm gap</label>
                <label><input type="radio" name="q6" value="c"> C) Chỉ có predictor step</label>
                <label><input type="radio" name="q6" value="d"> D) Chỉ có corrector step</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Predictor step giảm duality gap, corrector step improve centrality</strong><br>
                Predictor-corrector: predictor step approach optimal, corrector step maintain central path proximity.
            </div>
        </div>

        <!-- Câu hỏi 7: Mehrotra's algorithm -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Mehrotra's predictor-corrector algorithm là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Practical primal-dual algorithm với adaptive centering</label>
                <label><input type="radio" name="q7" value="b"> B) Pure Newton method</label>
                <label><input type="radio" name="q7" value="c"> C) Barrier method variant</label>
                <label><input type="radio" name="q7" value="d"> D) First-order method</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Practical primal-dual algorithm với adaptive centering</strong><br>
                Mehrotra's algorithm là widely used primal-dual method với adaptive centering parameter selection.
            </div>
        </div>

        <!-- Câu hỏi 8: Infeasible start -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Primal-dual method có thể start từ infeasible point bằng cách:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Backtracking line search đảm bảo progress toward feasibility</label>
                <label><input type="radio" name="q8" value="b"> B) Ignore feasibility constraints</label>
                <label><input type="radio" name="q8" value="c"> C) Project lên feasible region</label>
                <label><input type="radio" name="q8" value="d"> D) Không thể start từ infeasible point</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Backtracking line search đảm bảo progress toward feasibility</strong><br>
                Infeasible-start primal-dual methods sử dụng line search để maintain progress toward feasibility và optimality.
            </div>
        </div>

        <!-- Câu hỏi 9: SDP primal problem -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Semidefinite Programming (SDP) primal problem có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\min C \bullet X\) s.t. \(A_i \bullet X = b_i, X \succeq 0\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\min c^T x\) s.t. \(Ax = b, x \geq 0\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\min \frac{1}{2}x^T Q x\) s.t. \(Ax \leq b\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\min f(x)\) s.t. \(g_i(x) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min C \bullet X$$ s.t. $$A_i \bullet X = b_i, X \succeq 0$$</strong><br>
                SDP: minimize linear function của matrix variable với linear equality constraints và positive semidefinite constraint.
            </div>
        </div>

        <!-- Câu hỏi 10: SDP dual -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: SDP dual problem có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(\max b^T y\) s.t. \(\sum y_i A_i + S = C, S \succeq 0\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(\min b^T y\) s.t. \(A^T y \leq c\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(\max c^T z\) s.t. \(A^T z = b\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(\min \|y\|^2\) s.t. \(Ay = b\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max b^T y$$ s.t. $$\sum y_i A_i + S = C, S \succeq 0$$</strong><br>
                SDP dual: maximize linear function với dual matrix variable $$S \succeq 0$$ và linear constraint.
            </div>
        </div>

        <!-- Câu hỏi 11: SDP complementary slackness -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Complementary slackness trong SDP là:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(X \bullet S = 0\) (tức \(\text{tr}(XS) = 0\))</label>
                <label><input type="radio" name="q11" value="b"> B) \(X \bullet S = 1\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(X + S = 0\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(\|X - S\| = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$X \bullet S = 0$$ (tức $$\text{tr}(XS) = 0$$)</strong><br>
                SDP complementary slackness: inner product (trace) của primal và dual matrix variables bằng 0. (Với $$X, S \succeq 0$$, điều này tương đương với $$XS = 0$$.)
            </div>
        </div>

        <!-- Câu hỏi 12: Central path for SDP -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Central path condition cho SDP là:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) \(XS = \frac{1}{t}I\)</label>
                <label><input type="radio" name="q12" value="b"> B) \(X \bullet S = \frac{n}{t}\)</label>
                <label><input type="radio" name="q12" value="c"> C) \(XS = 0\)</label>
                <label><input type="radio" name="q12" value="d"> D) \(X = S\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$XS = \frac{1}{t}I$$</strong><br>
                SDP central path: matrix product $$XS = \frac{1}{t}I$$ thay vì scalar complementary slackness.
            </div>
        </div>

        <!-- Câu hỏi 13: Newton direction for SDP -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Newton direction trong SDP primal-dual method solve:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Linearized system cho \((\Delta X, \Delta y, \Delta S)\)</label>
                <label><input type="radio" name="q13" value="b"> B) Chỉ cho \(\Delta X\)</label>
                <label><input type="radio" name="q13" value="c"> C) Chỉ cho \(\Delta S\)</label>
                <label><input type="radio" name="q13" value="d"> D) Eigenvalue decomposition</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Linearized system cho $$(\Delta X, \Delta y, \Delta S)$$</strong><br>
                SDP Newton system solve simultaneously cho primal matrix $$\Delta X$$, dual vector $$\Delta y$$, và dual matrix $$\Delta S$$.
            </div>
        </div>

        <!-- Câu hỏi 14: Polynomial complexity -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Primal-dual interior point methods có complexity:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Polynomial-time trong worst case</label>
                <label><input type="radio" name="q14" value="b"> B) Exponential-time</label>
                <label><input type="radio" name="q14" value="c"> C) NP-hard</label>
                <label><input type="radio" name="q14" value="d"> D) Không có theoretical guarantees</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Polynomial-time trong worst case</strong><br>
                Interior point methods có polynomial-time complexity, breakthrough trong optimization theory.
            </div>
        </div>

        <!-- Câu hỏi 15: Warm start -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Warm start trong primal-dual methods có nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Start từ solution của similar problem</label>
                <label><input type="radio" name="q15" value="b"> B) Start từ origin</label>
                <label><input type="radio" name="q15" value="c"> C) Start từ random point</label>
                <label><input type="radio" name="q15" value="d"> D) Start từ boundary</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Start từ solution của similar problem</strong><br>
                Warm start sử dụng solution từ previous/similar problem làm starting point, rất hiệu quả trong practice.
            </div>
        </div>

        <!-- Câu hỏi 16: Homogeneous self-dual -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Homogeneous self-dual formulation có ưu điểm:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Detect infeasibility và unboundedness</label>
                <label><input type="radio" name="q16" value="b"> B) Không cần feasible starting point</label>
                <label><input type="radio" name="q16" value="c"> C) Unified treatment của different cases</label>
                <label><input type="radio" name="q16" value="d"> D) Tất cả các ưu điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ưu điểm trên</strong><br>
                Homogeneous self-dual formulation handle tất cả cases (optimal, infeasible, unbounded) trong unified framework.
            </div>
        </div>

        <!-- Câu hỏi 17: Centering parameter -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Centering parameter \(\sigma\) trong primal-dual method:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Control balance giữa centrality và progress toward optimality</label>
                <label><input type="radio" name="q17" value="b"> B) Luôn bằng 0</label>
                <label><input type="radio" name="q17" value="c"> C) Luôn bằng 1</label>
                <label><input type="radio" name="q17" value="d"> D) Không ảnh hưởng đến algorithm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Control balance giữa centrality và progress toward optimality</strong><br>
                Centering parameter $$\sigma \in [0,1]$$: $$\sigma = 0$$ (pure affine), $$\sigma = 1$$ (pure centering).
            </div>
        </div>

        <!-- Câu hỏi 18: Linear programming special case -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Cho LP, primal-dual method có đặc điểm:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Newton system trở thành linear system đơn giản</label>
                <label><input type="radio" name="q18" value="b"> B) Complementary slackness: \(x_i s_i = \frac{1}{t}\)</label>
                <label><input type="radio" name="q18" value="c"> C) Highly efficient implementation</label>
                <label><input type="radio" name="q18" value="d"> D) Tất cả các đặc điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các đặc điểm trên</strong><br>
                LP là special case với structure đơn giản, leading to highly efficient primal-dual algorithms.
            </div>
        </div>

        <!-- Câu hỏi 19: Convergence rate -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Primal-dual interior point methods có convergence rate:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Superlinear under nondegeneracy conditions</label>
                <label><input type="radio" name="q19" value="b"> B) Luôn linear</label>
                <label><input type="radio" name="q19" value="c"> C) Luôn quadratic</label>
                <label><input type="radio" name="q19" value="d"> D) Sublinear</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Superlinear under nondegeneracy conditions</strong><br>
                Primal-dual methods có superlinear convergence under appropriate nondegeneracy assumptions.
            </div>
        </div>

        <!-- Câu hỏi 20: Modern applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Primal-dual interior point methods được sử dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Commercial optimization solvers</label>
                <label><input type="radio" name="q20" value="b"> B) Large-scale linear và semidefinite programming</label>
                <label><input type="radio" name="q20" value="c"> C) Machine learning optimization</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các ứng dụng trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ứng dụng trên</strong><br>
                Primal-dual methods là backbone của modern optimization: CPLEX, Gurobi, MOSEK, và many ML applications.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Primal-dual interior point method kết hợp:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Barrier method + Newton method</label>
                <label><input type="radio" name="q21" value="b"> B) Gradient descent + momentum</label>
                <label><input type="radio" name="q21" value="c"> C) Simplex + dual simplex</label>
                <label><input type="radio" name="q21" value="d"> D) SGD + Adam</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Barrier method + Newton method</strong><br>
                Primal-dual IPM sử dụng barrier function và Newton method để giải đồng thời primal và dual.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Trong primal-dual IPM, hệ phương trình Newton rút gọn (sau khi khử \(\Delta \lambda\)) có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Ma trận khối đối xứng</label>
                <label><input type="radio" name="q22" value="b"> B) Ma trận tam giác</label>
                <label><input type="radio" name="q22" value="c"> C) Ma trận đường chéo</label>
                <label><input type="radio" name="q22" value="d"> D) Ma trận đơn vị</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Ma trận khối đối xứng</strong><br>
                Sau khi khử $$\Delta \lambda$$, hệ KKT trong IPM trở thành ma trận khối đối xứng (augmented system) với cấu trúc đặc biệt; hệ Newton đầy đủ ban đầu nói chung không đối xứng.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Predictor-corrector approach trong IPM:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Dự đoán hướng + hiệu chỉnh centrality</label>
                <label><input type="radio" name="q23" value="b"> B) Chỉ dự đoán</label>
                <label><input type="radio" name="q23" value="c"> C) Chỉ hiệu chỉnh</label>
                <label><input type="radio" name="q23" value="d"> D) Không liên quan</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Dự đoán hướng + hiệu chỉnh centrality</strong><br>
                Predictor step tìm hướng giảm duality gap, corrector step cải thiện centrality.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Complexity của IPM cho LP là:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$O(n^{3.5} \log(1/\epsilon))$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$O(2^n)$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$O(n!)$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$O(n \log n)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$O(n^{3.5} \log(1/\epsilon))$$</strong><br>
                IPM có complexity polynomial: $$O(\sqrt{n}\log(1/\epsilon))$$ iterations, mỗi iteration $$O(n^3)$$, tổng $$O(n^{3.5} \log(1/\epsilon))$$ cho LP.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Mehrotra's algorithm là:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Predictor-corrector IPM thực tế</label>
                <label><input type="radio" name="q25" value="b"> B) Simplex method</label>
                <label><input type="radio" name="q25" value="c"> C) Gradient descent</label>
                <label><input type="radio" name="q25" value="d"> D) Branch and bound</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Predictor-corrector IPM thực tế</strong><br>
                Mehrotra's algorithm là implementation thực tế phổ biến nhất của primal-dual IPM.
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
    q1: 'd', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'd', q17: 'a', q18: 'd', q19: 'a', q20: 'd'
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
        message = '🌟 Xuất sắc! Bạn đã thành thạo primal-dual interior point methods!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về central path và SDP.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại Newton systems và residuals.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại primal-dual algorithms và complementary slackness.';
    } else {
        message = '📖 Hãy học lại từ đầu về primal-dual methods nhé!';
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

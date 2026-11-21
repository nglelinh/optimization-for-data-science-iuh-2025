---
layout: post
title: '17-06 Multiple-Choice Quiz - Primal-Dual Interior Point Method'
chapter: '17'
order: 10
owner: GitHub Copilot
lang: en
categories:
- chapter17
lesson_type: quiz
---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### ⚡ **Primal-Dual Interior Point Method**

#### **Motivation and comparison with the Barrier Method**
**Barrier Method limitations:**
- **Multiple Newton steps:** Centering steps require many iterations
- **Must stay feasible:** Always maintain $$h_i(x) < 0$$
- **Sequential approach:** Solve sequence of barrier problems
- **Less efficient:** Many outer iterations needed

**Primal-Dual advantages:**
- **Single Newton step:** One Newton step per iteration
- **Infeasible start OK:** Can start from infeasible points ($$Ax^0 = b$$ is not required; in this form we still need $$h(x^0) < 0, u^0 > 0$$)
- **Simultaneous updates:** Update primal and dual variables together
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

with $$H(x) = \text{diag}(h(x))$$, $$U = \text{diag}(u)$$

#### **Solution interpretation**
- $$(\Delta x, \Delta u, \Delta v)$$: Newton direction
- **Simultaneous update:** Both primal ($$x$$) and dual ($$u,v$$) variables
- **Root finding:** Solve $$r(x,u,v) = 0$$ using Newton method

### 📊 **Residuals and the Surrogate Duality Gap**

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
2. **Initialize:** $$(x^0, u^0, v^0)$$ with $$h(x^0) < 0, u^0 > 0$$
3. **Main loop:** For $$k = 0, 1, 2, \ldots$$
   - **Compute Newton step:** Solve for $$(\Delta x, \Delta u, \Delta v)$$
   - **Backtracking line search:** Find step size $$\theta_k$$
   - **Update:** $$(x^{k+1}, u^{k+1}, v^{k+1}) = (x^k, u^k, v^k) + \theta_k(\Delta x, \Delta u, \Delta v)$$
4. **Termination:** Stop when $$-h(x)^T u \le \epsilon$$ and $$\lVert r_{\text{prim}} \rVert^2 + \lVert r_{\text{dual}} \rVert^2 \le \epsilon^2$$

### 🎯 **Multi-Stage Backtracking Line Search**

#### **Stage 1: Dual feasibility ($$u > 0$$)**
$$\theta_{\max} = \min\left\{1, \min\left\{-\frac{u_i}{\Delta u_i} : \Delta u_i < 0\right\}\right\}$$

**Goal:** Ensure $$u + \theta \Delta u \ge 0$$

#### **Stage 2: Primal feasibility ($$h(x) < 0$$)**
- Start with $$\theta = 0.99\theta_{\max}$$
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

with $$X = \text{diag}(x)$$, $$S = \text{diag}(s)$$

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
- **Polynomial-time:** $$O(\sqrt{n}\log(1/\epsilon))$$ iterations, $$O(n^{3.5} \log(1/\epsilon))$$ total complexity
- **Superlinear convergence:** Under appropriate conditions
- **Robust performance:** Works across problem classes
- **Infeasible start:** No need for Phase I (only a point in the strict interior of the inequality constraints is needed)

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

### 🎯 **Connections to Other Chapters**

#### **From previous chapters:**
- **Chapter 15:** Barrier method foundation
- **Chapter 16:** Duality theory, perturbed KKT
- **Chapter 14:** Newton's method for root finding
- **Chapter 12:** KKT conditions framework

#### **Advanced connections:**
- **Central path:** Geometric interpretation of optimization
- **Perturbed optimality:** Bridge between exact and approximate
- **Simultaneous updates:** Primal-dual variable coordination
- **Polynomial-time algorithms:** Theoretical complexity guarantees

#### **Practical applications:**
- **Commercial solvers:** CPLEX, Gurobi, Mosek
- **Large-scale optimization:** Industrial applications
- **Machine learning:** SVM, regularized regression
- **Engineering design:** Control, signal processing

### 🌟 **Theoretical Significance**

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

### 💡 **Practical Tips**

#### **When to use primal-dual methods:**
1. **Large-scale problems:** More efficient than barrier methods
2. **High accuracy needed:** Can achieve very high precision
3. **Infeasible start:** When feasible starting point hard to find
4. **Warm starts:** Efficient reoptimization scenarios

#### **Parameter selection:**
- **$$\sigma$$:** Usually from 0.1 to 0.9 (0.1 for fast progress, 0.9 for stability)
- **$$\alpha, \beta$$:** Standard values 0.01, 0.5 work well
- **$$\epsilon$$:** Problem-dependent tolerance
- **Feasibility margin:** 0.99 factor for numerical stability

#### **Implementation tips:**
- **Sparse linear algebra:** Essential for large problems
- **Numerical conditioning:** Monitor and regularize if needed
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

### 📈 **Real-World Applications**

#### **Linear and Quadratic Programming:**
- **Portfolio optimization:** Large-scale mean-variance models
- **Network flows:** Transportation and communication
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

#### **Finance and Economics:**
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
1. **Simultaneous updates:** Both primal and dual variables
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

### 🌟 **Legacy of Chapter 17:**

- **Algorithmic breakthrough:** Primal-dual interior point revolution
- **Theoretical completeness:** Unified framework for convex optimization
- **Practical impact:** Foundation of commercial optimization software
- **Industrial transformation:** Large-scale optimization capability
- **Educational significance:** Beautiful synthesis of theory and practice

### 🎯 **Takeaway messages:**

1. **Primal-dual is superior:** More efficient than pure barrier methods
2. **Simultaneous updates:** Key to algorithmic efficiency
3. **Infeasible start OK:** No need for feasible initialization
4. **Polynomial-time guarantee:** Theoretical and practical efficiency
5. **Commercial foundation:** Basis of modern optimization software

### 💫 **Philosophical impact:**

Chapter 17 **completes the interior point revolution**:
- **From primal-only to primal-dual:** Simultaneous variable updates
- **From feasible to infeasible start:** Greater algorithmic flexibility
- **From barrier to direct approach:** More efficient path following
- **From academic to commercial:** Industrial optimization software
- **From theory to practice:** Complete optimization framework

### 🔮 **Synthesis:**

The Primal-Dual Interior Point Method represents the **culmination** of the interior point approach:
- **Theoretical elegance:** Perturbed KKT conditions framework
- **Algorithmic efficiency:** Simultaneous primal-dual updates
- **Practical power:** Foundation of commercial software
- **Industrial impact:** Large-scale optimization capability
- **Educational value:** Beautiful theory-practice synthesis

### 💡 **Final insight:**

Chapter 17 demonstrates that **optimization theory can be both beautiful and practical**. From perturbed KKT conditions to Newton systems, from central path following to multi-stage line search, from theoretical polynomial-time guarantees to commercial software implementations - **primal-dual interior point methods represent a perfect marriage** of mathematical elegance with computational efficiency.

**Primal-Dual = Simultaneous optimization of dual perspectives!**

---

💡 **Final message:** The Primal-Dual Interior Point Method is not just an algorithmic improvement - it is the **completion of the interior point revolution**, enabling both theoretical understanding and the practical solution of large-scale optimization problems across science, engineering, finance, and technology!

---


<style>
/* Fix alignment for MathJax inline math */
.MathJax {
    vertical-align: baseline !important;
}

mjx-container[jax="CHTML"][display="false"] {
    vertical-align: baseline !important;
    display: inline !important;
}

/* Make sure labels in the quiz are well aligned */
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

This multiple-choice quiz tests your understanding of the Primal-Dual Interior Point Method, including primal-dual algorithms, central path equations, semidefinite programming and advanced interior point concepts.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>⚡ Quiz: Primal-Dual Interior Point Method</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1 -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: The primal-dual interior point method differs from the barrier method in that it:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Updates both primal and dual variables simultaneously</label>
                <label><input type="radio" name="q1" value="b"> B) Needs only one Newton step per iteration</label>
                <label><input type="radio" name="q1" value="c"> C) Does not need a feasible starting point</label>
                <label><input type="radio" name="q1" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                Primal-dual methods update both primal and dual variables, usually need only 1 Newton step, and can start from infeasible points.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The central path equations for inequality constraints $$g_i(x) \leq 0$$ are:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) $$\nabla f(x) + \sum \lambda_i \nabla g_i(x) = 0, \lambda_i g_i(x) = -\frac{1}{t}$$</label>
                <label><input type="radio" name="q2" value="b"> B) $$\nabla f(x) + \sum \lambda_i \nabla g_i(x) = 0, \lambda_i g_i(x) = 0$$</label>
                <label><input type="radio" name="q2" value="c"> C) $$\nabla f(x) = 0, g_i(x) = 0$$</label>
                <label><input type="radio" name="q2" value="d"> D) $$\lambda_i = \frac{1}{t}, g_i(x) = -1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\nabla f(x) + \sum \lambda_i \nabla g_i(x) = 0, \lambda_i g_i(x) = -\frac{1}{t}$$</strong><br>
                Central path equations: the stationarity condition and the modified complementary slackness with parameter $$t$$.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: The Newton system in the primal-dual method solves for:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$(\Delta x, \Delta \lambda, \Delta \nu)$$ - directions for both primal and dual</label>
                <label><input type="radio" name="q3" value="b"> B) Only $$\Delta x$$ - the primal direction</label>
                <label><input type="radio" name="q3" value="c"> C) Only $$\Delta \lambda$$ - the dual direction</label>
                <label><input type="radio" name="q3" value="d"> D) Parameter $$t$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$(\Delta x, \Delta \lambda, \Delta \nu)$$ - directions for both primal and dual</strong><br>
                The Newton system solves simultaneously for the primal direction $$\Delta x$$ and the dual directions $$\Delta \lambda, \Delta \nu$$.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The surrogate duality gap in the primal-dual method is:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$\eta = -\sum_{i=1}^m \lambda_i g_i(x)$$</label>
                <label><input type="radio" name="q4" value="b"> B) \(\eta = f(x) - g(\lambda, \nu)\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(\eta = \|\nabla f(x)\|\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(\eta = \sum_{i=1}^m |\lambda_i|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\eta = -\sum_{i=1}^m \lambda_i g_i(x)$$</strong><br>
                The surrogate duality gap estimates the duality gap from the current primal-dual point, without computing the dual function.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The residuals in the primal-dual method consist of:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Dual residual, primal residual, centrality residual</label>
                <label><input type="radio" name="q5" value="b"> B) Only the dual residual</label>
                <label><input type="radio" name="q5" value="c"> C) Only the primal residual</label>
                <label><input type="radio" name="q5" value="d"> D) Only the centrality residual</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Dual residual, primal residual, centrality residual</strong><br>
                Ba residuals: dual (stationarity), primal (feasibility), centrality (complementary slackness).
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: The predictor-corrector method in primal-dual IPM:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) The predictor step reduces the duality gap, the corrector step improves centrality</label>
                <label><input type="radio" name="q6" value="b"> B) The predictor step increases feasibility, the corrector step reduces the gap</label>
                <label><input type="radio" name="q6" value="c"> C) Only a predictor step</label>
                <label><input type="radio" name="q6" value="d"> D) Only a corrector step</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The predictor step reduces the duality gap, the corrector step improves centrality</strong><br>
                Predictor-corrector: predictor step approach optimal, corrector step maintain central path proximity.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: Mehrotra's predictor-corrector algorithm is:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) A practical primal-dual algorithm with adaptive centering</label>
                <label><input type="radio" name="q7" value="b"> B) Pure Newton method</label>
                <label><input type="radio" name="q7" value="c"> C) Barrier method variant</label>
                <label><input type="radio" name="q7" value="d"> D) First-order method</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) A practical primal-dual algorithm with adaptive centering</strong><br>
                Mehrotra's algorithm is a widely used primal-dual method with adaptive selection of the centering parameter.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The primal-dual method can start from an infeasible point by:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) A backtracking line search that ensures progress toward feasibility</label>
                <label><input type="radio" name="q8" value="b"> B) Ignore feasibility constraints</label>
                <label><input type="radio" name="q8" value="c"> C) Projecting onto the feasible region</label>
                <label><input type="radio" name="q8" value="d"> D) It cannot start from an infeasible point</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) A backtracking line search that ensures progress toward feasibility</strong><br>
                Infeasible-start primal-dual methods use a line search to maintain progress toward feasibility and optimality.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The Semidefinite Programming (SDP) primal problem has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\min C \bullet X\) s.t. \(A_i \bullet X = b_i, X \succeq 0\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\min c^T x\) s.t. \(Ax = b, x \geq 0\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\min \frac{1}{2}x^T Q x\) s.t. \(Ax \leq b\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\min f(x)\) s.t. \(g_i(x) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\min C \bullet X$$ s.t. $$A_i \bullet X = b_i, X \succeq 0$$</strong><br>
                SDP: minimize a linear function of a matrix variable subject to linear equality constraints and a positive semidefinite constraint.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The SDP dual problem has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(\max b^T y\) s.t. \(\sum y_i A_i + S = C, S \succeq 0\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(\min b^T y\) s.t. \(A^T y \leq c\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(\max c^T z\) s.t. \(A^T z = b\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(\min \|y\|^2\) s.t. \(Ay = b\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max b^T y$$ s.t. $$\sum y_i A_i + S = C, S \succeq 0$$</strong><br>
                SDP dual: maximize a linear function with a dual matrix variable $$S \succeq 0$$ and a linear constraint.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: Complementary slackness in SDP is:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(X \bullet S = 0\) (i.e. \(\text{tr}(XS) = 0\))</label>
                <label><input type="radio" name="q11" value="b"> B) \(X \bullet S = 1\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(X + S = 0\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(\|X - S\| = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$X \bullet S = 0$$ (i.e. $$\text{tr}(XS) = 0$$)</strong><br>
                SDP complementary slackness: the inner product (trace) of the primal and dual matrix variables is 0. (For $$X, S \succeq 0$$, this is equivalent to $$XS = 0$$.)
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The central path condition for SDP is:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) \(XS = \frac{1}{t}I\)</label>
                <label><input type="radio" name="q12" value="b"> B) \(X \bullet S = \frac{n}{t}\)</label>
                <label><input type="radio" name="q12" value="c"> C) \(XS = 0\)</label>
                <label><input type="radio" name="q12" value="d"> D) \(X = S\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$XS = \frac{1}{t}I$$</strong><br>
                SDP central path: the matrix product $$XS = \frac{1}{t}I$$ instead of scalar complementary slackness.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The Newton direction in the SDP primal-dual method solves:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) A linearized system for \((\Delta X, \Delta y, \Delta S)\)</label>
                <label><input type="radio" name="q13" value="b"> B) Only for \(\Delta X\)</label>
                <label><input type="radio" name="q13" value="c"> C) Only for \(\Delta S\)</label>
                <label><input type="radio" name="q13" value="d"> D) Eigenvalue decomposition</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) A linearized system for $$(\Delta X, \Delta y, \Delta S)$$</strong><br>
                The SDP Newton system solves simultaneously for the primal matrix $$\Delta X$$, the dual vector $$\Delta y$$, and the dual matrix $$\Delta S$$.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: Primal-dual interior point methods have complexity:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Polynomial-time in the worst case</label>
                <label><input type="radio" name="q14" value="b"> B) Exponential-time</label>
                <label><input type="radio" name="q14" value="c"> C) NP-hard</label>
                <label><input type="radio" name="q14" value="d"> D) No theoretical guarantees</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Polynomial-time in the worst case</strong><br>
                Interior point methods have polynomial-time complexity, a breakthrough in optimization theory.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: A warm start in primal-dual methods means:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Starting from the solution of a similar problem</label>
                <label><input type="radio" name="q15" value="b"> B) Starting from the origin</label>
                <label><input type="radio" name="q15" value="c"> C) Starting from a random point</label>
                <label><input type="radio" name="q15" value="d"> D) Starting from the boundary</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Starting from the solution of a similar problem</strong><br>
                A warm start uses the solution of a previous/similar problem as the starting point, which is very effective in practice.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: The homogeneous self-dual formulation has the advantages:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Detects infeasibility and unboundedness</label>
                <label><input type="radio" name="q16" value="b"> B) Does not need a feasible starting point</label>
                <label><input type="radio" name="q16" value="c"> C) Unified treatment of the different cases</label>
                <label><input type="radio" name="q16" value="d"> D) All of the above advantages</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above advantages</strong><br>
                The homogeneous self-dual formulation handles all cases (optimal, infeasible, unbounded) in a unified framework.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: The centering parameter \(\sigma\) in the primal-dual method:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Controls the balance between centrality and progress toward optimality</label>
                <label><input type="radio" name="q17" value="b"> B) Is always 0</label>
                <label><input type="radio" name="q17" value="c"> C) Is always 1</label>
                <label><input type="radio" name="q17" value="d"> D) Does not affect the algorithm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Controls the balance between centrality and progress toward optimality</strong><br>
                Centering parameter $$\sigma \in [0,1]$$: $$\sigma = 0$$ (pure affine), $$\sigma = 1$$ (pure centering).
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: For LP, the primal-dual method has the characteristics:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) The Newton system becomes a simple linear system</label>
                <label><input type="radio" name="q18" value="b"> B) Complementary slackness: \(x_i s_i = \frac{1}{t}\)</label>
                <label><input type="radio" name="q18" value="c"> C) Highly efficient implementation</label>
                <label><input type="radio" name="q18" value="d"> D) All of the above characteristics</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above characteristics</strong><br>
                LP is a special case with a simple structure, leading to highly efficient primal-dual algorithms.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: Primal-dual interior point methods have convergence rate:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Superlinear under nondegeneracy conditions</label>
                <label><input type="radio" name="q19" value="b"> B) Always linear</label>
                <label><input type="radio" name="q19" value="c"> C) Always quadratic</label>
                <label><input type="radio" name="q19" value="d"> D) Sublinear</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Superlinear under nondegeneracy conditions</strong><br>
                Primal-dual methods have superlinear convergence under appropriate nondegeneracy assumptions.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: Primal-dual interior point methods are used in:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Commercial optimization solvers</label>
                <label><input type="radio" name="q20" value="b"> B) Large-scale linear and semidefinite programming</label>
                <label><input type="radio" name="q20" value="c"> C) Machine learning optimization</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above applications</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above applications</strong><br>
                Primal-dual methods are the backbone of modern optimization: CPLEX, Gurobi, MOSEK, and many ML applications.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: The primal-dual interior point method combines:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Barrier method + Newton method</label>
                <label><input type="radio" name="q21" value="b"> B) Gradient descent + momentum</label>
                <label><input type="radio" name="q21" value="c"> C) Simplex + dual simplex</label>
                <label><input type="radio" name="q21" value="d"> D) SGD + Adam</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Barrier method + Newton method</strong><br>
                Primal-dual IPM uses a barrier function and Newton's method to solve the primal and dual simultaneously.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: In primal-dual IPM, the reduced Newton system (after eliminating \(\Delta \lambda\)) has the form of a:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Symmetric block matrix</label>
                <label><input type="radio" name="q22" value="b"> B) Triangular matrix</label>
                <label><input type="radio" name="q22" value="c"> C) Diagonal matrix</label>
                <label><input type="radio" name="q22" value="d"> D) Identity matrix</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Symmetric block matrix</strong><br>
                After eliminating $$\Delta \lambda$$, the KKT system in IPM becomes a symmetric block matrix (augmented system) with special structure; the original full Newton system is generally not symmetric.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: The predictor-corrector approach in IPM:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Predicts a direction + corrects centrality</label>
                <label><input type="radio" name="q23" value="b"> B) Only predicts</label>
                <label><input type="radio" name="q23" value="c"> C) Only corrects</label>
                <label><input type="radio" name="q23" value="d"> D) Is unrelated</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Predicts a direction + corrects centrality</strong><br>
                The predictor step finds a direction that reduces the duality gap, the corrector step improves centrality.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The complexity of IPM for LP is:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$O(n^{3.5} \log(1/\epsilon))$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$O(2^n)$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$O(n!)$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$O(n \log n)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$O(n^{3.5} \log(1/\epsilon))$$</strong><br>
                IPM has polynomial complexity: $$O(\sqrt{n}\log(1/\epsilon))$$ iterations, each costing $$O(n^3)$$, for a total of $$O(n^{3.5} \log(1/\epsilon))$$ for LP.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: Mehrotra's algorithm is:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) A practical predictor-corrector IPM</label>
                <label><input type="radio" name="q25" value="b"> B) Simplex method</label>
                <label><input type="radio" name="q25" value="c"> C) Gradient descent</label>
                <label><input type="radio" name="q25" value="d"> D) Branch and bound</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) A practical predictor-corrector IPM</strong><br>
                Mehrotra's algorithm is the most popular practical implementation of primal-dual IPM.
            </div>
        </div>

    </div>

    <div class="quiz-controls">
        <button onclick="previousQuestion()" id="prev-btn" disabled>← Previous</button>
        <button onclick="nextQuestion()" id="next-btn">Next →</button>
        <button onclick="submitQuiz()" id="submit-btn" style="display: none;">Submit</button>
        <button onclick="resetQuiz()" id="reset-btn" style="display: none;">Try again</button>
    </div>

    <div id="final-result" style="display: none;" class="final-score">
        <h2>🎉 Quiz Complete!</h2>
        <p>Your score: <span id="final-score-text"></span></p>
        <p id="performance-message"></p>
    </div>
</div>

<script>
let currentQuestion = 1;
const totalQuestions = 25;
let userAnswers = {};
let quizSubmitted = false;

// Correct answers
const correctAnswers = {
    q1: 'd', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'd', q17: 'a', q18: 'd', q19: 'a', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'a'};

function showQuestion(n) {
    // Hide all questions
    for (let i = 1; i <= totalQuestions; i++) {
        document.getElementById(`q${i}`).style.display = 'none';
    }
    
    // Show the current question
    document.getElementById(`q${n}`).style.display = 'block';
    
    // Update the progress bar
    const progress = (n / totalQuestions) * 100;
    document.getElementById('progress-fill').style.width = progress + '%';
    
    // Update the question number
    document.getElementById('current-q').textContent = n;
    
    // Update the navigation buttons
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
    
    // Show all explanations
    for (let i = 1; i <= totalQuestions; i++) {
        const explanation = document.querySelector(`#q${i} .explanation`);
        explanation.style.display = 'block';
        
        // Highlight correct and incorrect answers
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
    
    // Show the final result
    document.getElementById('final-result').style.display = 'block';
    document.getElementById('final-score-text').textContent = `${score}/${totalQuestions} (${percentage}%)`;
    
    let message = '';
    if (percentage >= 90) {
        message = '🌟 Excellent! You have mastered primal-dual interior point methods!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand the central path and SDP well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review Newton systems and residuals.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review primal-dual algorithms and complementary slackness.';
    } else {
        message = '📖 Study primal-dual methods again from the beginning!';
    }
    
    document.getElementById('performance-message').textContent = message;
    
    // Hide the submit button, show the reset button
    document.getElementById('submit-btn').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'inline-block';
    
    // Scroll to the results
    document.getElementById('final-result').scrollIntoView({ behavior: 'smooth' });
}

function resetQuiz() {
    // Reset state
    currentQuestion = 1;
    userAnswers = {};
    quizSubmitted = false;
    
    // Hide all explanations
    document.querySelectorAll('.explanation').forEach(exp => {
        exp.style.display = 'none';
    });
    
    // Reset label styles
    document.querySelectorAll('.options label').forEach(label => {
        label.style.backgroundColor = '';
        label.style.border = '';
        label.classList.remove('selected');
    });
    
    // Uncheck all radio buttons
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.checked = false;
    });
    
    document.querySelectorAll('.options label').forEach(label => {
        label.classList.remove('selected');
    });
    
    // Show the first question
    showQuestion(1);
    
    // Scroll to the top
    document.getElementById('quiz-header').scrollIntoView({ behavior: 'smooth' });
    
    // Hide the final result and the reset button
    document.getElementById('final-result').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'none';
}

// Initialize the exercise when the page loads
document.addEventListener('DOMContentLoaded', function() {
    showQuestion(1);
    
    // Add event listeners to all radio buttons
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.addEventListener('change', function() {
            const questionId = this.name;
            const answer = this.value;
            saveAnswer(questionId, answer);
        });
    });
    
    // Render MathJax after the DOM has loaded
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        MathJax.startup.promise.then(() => MathJax.typesetPromise());
    }
});

// Handle keyboard shortcuts
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

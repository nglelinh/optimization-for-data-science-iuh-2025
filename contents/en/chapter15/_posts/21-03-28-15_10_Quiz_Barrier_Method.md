---
layout: post
title: '15-10 Multiple-Choice Quiz - Barrier Method'
chapter: '15'
order: 16
owner: GitHub Copilot
lang: en
categories:
- chapter15
lesson_type: quiz
redirect_from:
  - /contents/en/chapter15/15_09_Quiz_Barrier_Method/
---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### ⚡ **The Barrier Method**

#### **The inequality-constrained problem**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad Ax = b$$

with $$i = 1,\ldots,m$$

#### **Problems with boundary optimization**
- **Binding vs non-binding constraints:** Hard to tell which constraints are active
- **Boundary computation:** $$O(m^2)$$ complexity for active set methods
- **Non-differentiable:** The indicator function is not differentiable

#### **Interior method philosophy**
**Idea:** Solve from the **interior** of the feasible region instead of the boundary
- **Avoid boundary:** No need to identify the active constraints
- **Smooth approximation:** Use differentiable barrier functions
- **Newton applicable:** Enables Newton's method for constrained problems

### 🚧 **Logarithmic Barrier Function**

#### **Indicator function approximation**
**Original:** $$I_C(x) = \begin{cases} 0 & \text{if } x \in C \\ \infty & \text{otherwise} \end{cases}$$

**Barrier approximation:** $$\phi(x) = -\sum_{i=1}^m \log(-h_i(x))$$

#### **Properties of the log barrier**
- **Domain:** $$\{x : h_i(x) < 0 \quad \forall i\}$$ (strictly feasible)
- **Smooth:** Twice differentiable in the interior
- **Barrier effect:** $$\phi(x) \to \infty$$ as $$x$$ approaches the boundary
- **Self-concordant:** (when $$h_i$$ is affine or convex quadratic) Enables elegant Newton analysis

#### **Barrier problem formulation**
**Original problem:** $$\min f(x)$$ s.t. $$h_i(x) \le 0, Ax = b$$

**Barrier approximation:**
$$\min_x tf(x) + \phi(x) \quad \text{s.t.} \quad Ax = b$$

with $$t > 0$$ the **barrier parameter**

#### **Interpretation**
- **Large $$t$$:** Emphasize original objective $$f(x)$$
- **Small $$t$$:** Emphasize staying interior (large barrier effect)
- **$$t \to \infty$$:** Barrier problem → original problem

### 🛤️ **Central Path**

#### **Definition**
**Central path:** $$\{x^*(t) : t > 0\}$$ with $$x^*(t) = \arg\min_x \{tf(x) + \phi(x) : Ax = b\}$$

#### **Properties**
- **Smooth curve:** Forms a continuous path in $$\mathbb{R}^n$$
- **Convergence:** $$x^*(t) \to x^*$$ as $$t \to \infty$$
- **Interior:** All points strictly feasible
- **Unique:** Each $$t$$ gives unique $$x^*(t)$$ (under strict convexity)

#### **Geometric interpretation**
- **Path from interior to boundary:** Gradually approach optimal solution
- **Balance:** Trade-off between the objective and barrier terms
- **Smooth transition:** Continuous movement toward optimum

### 📊 **KKT Conditions and Interpretation**

#### **Barrier problem KKT**
For the barrier problem $$\min tf(x) + \phi(x)$$ s.t. $$Ax = b$$:

**Stationarity:** $$t\nabla f(x^*(t)) + \nabla \phi(x^*(t)) + A^T \nu^*(t) = 0$$

**Feasibility:** $$Ax^*(t) = b$$

#### **Original problem KKT**
For the original problem $$\min f(x)$$ s.t. $$h_i(x) \le 0, Ax = b$$:

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
1. Construct a dual feasible point from the barrier solution
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
   - **Warm start:** Initialize Newton with $$x^{(k)}$$
   - Solve barrier problem at $$t^{(k+1)}$$ to get $$x^{(k+1)}$$
   - $$k \leftarrow k + 1$$

#### **Key components**
- **Centering steps:** Solve barrier problem (outer iterations)
- **Newton steps:** Within each centering step (inner iterations)
- **Warm start:** Use previous solution as initialization
- **Parameter update:** $$t^{(k+1)} = \mu t^{(k)}$$ with $$\mu > 1$$

### ⚖️ **Parameter Selection Trade-offs**

#### **Choice of $$\mu$$ (update factor)**
- **$$\mu$$ too small:** Many outer iterations (more centering steps)
- **$$\mu$$ too large:** Many inner iterations (Newton steps per centering)
- **Typical choice:** $$\mu = 10$$ to $$50$$

#### **Choice of $$t^{(0)}$$ (initial parameter)**
- **$$t^{(0)}$$ too small:** Many outer iterations
- **$$t^{(0)}$$ too large:** Difficult first centering step
- **Practical:** Start with a moderate value; the algorithm is robust

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

#### **Comparison with other methods**
- **Newton method:** $$O(\log\log(1/\epsilon))$$ - quadratic convergence
- **Gradient descent:** $$O(1/\epsilon)$$ - sublinear convergence
- **Barrier method:** $$O(\log(1/\epsilon))$$ - linear convergence

**Note:** Linear convergence is **very good** for constrained problems!

### 🎯 **Feasibility Methods**

#### **Problem: Finding strictly feasible starting point**
**Need:** $$x$$ such that $$h_i(x) < 0 \quad \forall i, \quad Ax = b$$

#### **Phase I: Maximum infeasibility**
$$\min_{x,s} s \quad \text{s.t.} \quad h_i(x) \le s, \quad Ax = b$$

**Goal:** Find $$s < 0$$ (strictly feasible point exists)

**Advantage:** Single slack variable

#### **Phase I: Individual infeasibilities**
$$\min_{x,s} \mathbf{1}^T s \quad \text{s.t.} \quad h_i(x) \le s_i, \quad Ax = b, \quad s \succeq 0$$

**Goal:** Optimal $$s^* = 0$$ ⟺ the original problem is feasible

**Advantage:** Identify which constraints are problematic

#### **Implementation**
- **Use barrier method:** For Phase I problems too
- **Lower accuracy:** Don't need high precision for feasibility
- **Infeasibility detection:** In the basic Phase I, if the optimal $$s^* > 0$$ then the original problem is infeasible; if $$s^* \ge 0$$ there is no strictly feasible point

### 🛠️ **Implementation Details**

#### **Newton method for barrier problems**
**Gradient:** $$\nabla (tf + \phi) = t\nabla f - \sum_{i=1}^m \frac{1}{h_i(x)} \nabla h_i$$

**Hessian:** $$\nabla^2 (tf + \phi) = t\nabla^2 f + \sum_{i=1}^m \frac{1}{h_i^2(x)} \nabla h_i \nabla h_i^T - \sum_{i=1}^m \frac{1}{h_i(x)} \nabla^2 h_i$$

#### **Numerical considerations**
- **Stay strictly feasible:** Ensure $$h_i(x) < 0$$ throughout
- **Line search:** Backtracking to maintain feasibility
- **Conditioning:** Hessian becomes ill-conditioned as $$t$$ increases
- **Stopping criteria:** Use duality gap $$\frac{m}{t}$$

### 💡 **Example: Linear Programming**

#### **LP problem**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

#### **Barrier formulation**
$$\min tc^T x - \sum_{i=1}^n \log x_i \quad \text{s.t.} \quad Ax = b$$

#### **Central path**
**KKT conditions:** $$tc + A^T \nu - X^{-1} e = 0, \quad Ax = b$$

with $$X = \text{diag}(x)$$, $$e = (1,\ldots,1)^T$$

**Interpretation:** $$x_i \lambda_i = \frac{1}{t}$$ (perturbed complementary slackness)

### 🎯 **Connections to Other Chapters**

#### **From the previous chapter:**
- **Chapter 14:** Newton's method - the foundation of the barrier method
- **Chapter 12:** KKT conditions - perturbed KKT interpretation
- **Chapter 11:** General duality - duality gap analysis

#### **Importance of the Barrier Method:**
- **Interior point revolution:** Polynomial-time algorithms for LP
- **Constrained optimization:** A practical method for inequality constraints
- **Self-concordance:** Elegant theoretical framework
- **Real-world impact:** Standard in optimization software

#### **Looking ahead:**
- **Primal-dual methods:** Simultaneous primal-dual updates
- **Homogeneous methods:** Handle infeasible problems
- **Semidefinite programming:** Extension to matrix constraints
- **Large-scale applications:** Sparse matrix techniques

### 🌟 **Theoretical Significance**

#### **Interior point paradigm:**
- **Avoid combinatorial complexity:** No active set identification
- **Polynomial-time:** $$O(n^3 \log(1/\epsilon))$$ for LP
- **Smooth approximation:** Differentiable barrier functions
- **Path-following:** Systematic approach to boundary

#### **Theoretical elegance:**
- **Self-concordance:** Affine-invariant analysis
- **Central path:** Geometric interpretation of optimization
- **Duality connection:** Perturbed KKT conditions
- **Convergence guarantees:** Rigorous complexity analysis

#### **Practical impact:**
- **Software revolution:** CPLEX, Gurobi use interior point
- **Large-scale problems:** Handle millions of variables
- **Robust performance:** Works across diverse problem classes
- **Warm start capability:** Efficient reoptimization

### 💡 **Practical Tips**

#### **When to use barrier methods:**
1. **Many inequality constraints:** More efficient than active set
2. **Large-scale problems:** Polynomial-time complexity
3. **High accuracy needed:** Linear convergence to high precision
4. **Smooth problems:** Twice differentiable objectives and constraints

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
- **Simultaneous updates:** Update both primal and dual variables
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

### 📈 **Real-World Applications**

#### **Linear and Quadratic Programming:**
- **Portfolio optimization:** Risk-return trade-offs
- **Production planning:** Resource allocation
- **Network flows:** Transportation problems
- **Machine learning:** SVM training

#### **Engineering Design:**
- **Structural optimization:** Weight minimization
- **Control systems:** Optimal control
- **Signal processing:** Filter design
- **Image processing:** Reconstruction problems

#### **Finance and Economics:**
- **Risk management:** Value-at-Risk optimization
- **Algorithmic trading:** Execution strategies
- **Auction design:** Mechanism optimization
- **Market equilibrium:** Economic modeling

#### **Machine Learning:**
- **Regularized regression:** L1, L2 penalties
- **Neural network training:** Constrained optimization
- **Kernel methods:** SVM and variants
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
2. **Polynomial-time:** A theoretical breakthrough for LP
3. **Practical efficiency:** Handle large-scale problems
4. **Smooth approximation:** Enable Newton methods

#### **Practical impact:**
- **Software standard:** Foundation of modern solvers
- **Industrial applications:** Optimization across industries
- **Research foundation:** Basis for advanced methods
- **Educational value:** Elegant theory-practice connection

### 🌟 **Legacy of Chapter 15:**

- **Algorithmic revolution:** Interior point methods
- **Theoretical breakthrough:** Polynomial-time linear programming
- **Practical impact:** Large-scale optimization capability
- **Software influence:** Standard in commercial solvers
- **Educational significance:** Beautiful theory-practice synthesis

---

💡 **Final message:** The barrier method is not just a clever approximation technique - it is a **paradigm shift** from boundary-based to interior-based optimization, enabling polynomial-time algorithms and the practical solution of large-scale constrained problems!

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

This multiple-choice quiz tests your understanding of the barrier method, including interior point methods, the log barrier function, the central path, convergence analysis and feasibility methods.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🚧 Quiz: Barrier & Interior Point Methods</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1 -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: The barrier method handles inequality constraints by:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Converting them into equality constraints</label>
                <label><input type="radio" name="q1" value="b"> B) Adding a barrier function to the objective</label>
                <label><input type="radio" name="q1" value="c"> C) Removing the constraints</label>
                <label><input type="radio" name="q1" value="d"> D) Using a penalty method</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Adding a barrier function to the objective</strong><br>
                The barrier method adds a barrier function that "pushes" the solution into the interior of the feasible region, avoiding constraint violations.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The log barrier function for the constraint \(g_i(x) \leq 0\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(-\log(-g_i(x))\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\log(g_i(x))\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(-\log(g_i(x))\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\log(-g_i(x))\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$-\log(-g_i(x))$$</strong><br>
                The log barrier function $$-\log(-g_i(x))$$ ensures $$g_i(x) < 0$$ and grows to $$+\infty$$ as the boundary is approached.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: The barrier problem has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(\min tf(x) + \phi(x)\) subject to \(Ax = b\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\min f(x) + t\phi(x)\) subject to \(Ax = b\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(\min f(x) - t\phi(x)\) subject to \(Ax = b\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(\min f(x)\) subject to \(Ax = b, g(x) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\min tf(x) + \phi(x)$$ subject to $$Ax = b$$</strong><br>
                The barrier problem has a parameter $$t > 0$$; as $$t \to \infty$$ the solution approaches that of the original problem.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The central path is:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) The set \(\{x^*(t) | t > 0\}\) where \(x^*(t)\) is the solution of the barrier problem</label>
                <label><input type="radio" name="q4" value="b"> B) A straight line from the starting point to the optimum</label>
                <label><input type="radio" name="q4" value="c"> C) The center of the feasible region</label>
                <label><input type="radio" name="q4" value="d"> D) Gradient descent path</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The set $$\{x^*(t) | t > 0\}$$ where $$x^*(t)$$ is the solution of the barrier problem</strong><br>
                The central path is the trajectory of the optimal solutions as the parameter $$t$$ goes from 0 to $$\infty$$.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: As \(t \to \infty\), the central path:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Converges to the optimal solution of the original problem</label>
                <label><input type="radio" name="q5" value="b"> B) Diverge</label>
                <label><input type="radio" name="q5" value="c"> C) Oscillate</label>
                <label><input type="radio" name="q5" value="d"> D) Approach boundary</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Converges to the optimal solution of the original problem</strong><br>
                As $$t \to \infty$$, the barrier term $$\phi(x)$$ becomes negligible and the solution approaches the original optimum $$x^*$$.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: The KKT conditions for the barrier problem at \(x^*(t)\) are:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(t\nabla f(x) + \sum \frac{1}{-g_i(x)} \nabla g_i(x) + A^T\nu = 0\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(\nabla f(x) + \sum \lambda_i \nabla g_i(x) + A^T\nu = 0\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(t\nabla f(x) = 0\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\nabla f(x) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$t\nabla f(x) + \sum \frac{1}{-g_i(x)} \nabla g_i(x) + A^T\nu = 0$$</strong><br>
                Gradient of the barrier objective: $$t\nabla f(x) + \nabla \phi(x) + A^T\nu = 0$$ with $$\nabla \phi(x) = \sum \frac{1}{-g_i(x)} \nabla g_i(x)$$.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: The dual variables in the barrier method satisfy:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(\lambda_i^*(t) = \frac{1}{t(-g_i(x^*(t)))}\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(\lambda_i^*(t) = t(-g_i(x^*(t)))\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(\lambda_i^*(t) = -g_i(x^*(t))\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(\lambda_i^*(t) = \frac{1}{-g_i(x^*(t))}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\lambda_i^*(t) = \frac{1}{t(-g_i(x^*(t)))}$$</strong><br>
                Dual variables from the barrier method: $$\lambda_i^*(t) = \frac{1}{t(-g_i(x^*(t)))}$$, approaching the true dual as $$t \to \infty$$.
            </div>
        </div>

        <!-- Question 8: Duality gap -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The duality gap in the barrier method is:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\frac{m}{t}\) where \(m\) is the number of inequality constraints</label>
                <label><input type="radio" name="q8" value="b"> B) \(\frac{1}{t}\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(mt\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(t\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\frac{m}{t}$$ where $$m$$ is the number of inequality constraints</strong><br>
                Duality gap $$\eta = f(x^*(t)) - g(\lambda^*(t), \nu^*(t)) = \frac{m}{t}$$, decreasing as $$t$$ increases.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: Barrier method algorithm:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Increase \(t\) along a sequence, solving the barrier problem for each \(t\)</label>
                <label><input type="radio" name="q9" value="b"> B) Decrease \(t\) along a sequence</label>
                <label><input type="radio" name="q9" value="c"> C) Keep \(t\) fixed</label>
                <label><input type="radio" name="q9" value="d"> D) Random \(t\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Increase $$t$$ along a sequence, solving the barrier problem for each $$t$$</strong><br>
                Algorithm: start with $$t^{(0)}$$, solve the barrier problem, update $$t^{(k+1)} = \mu t^{(k)}$$ with $$\mu > 1$$.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The centering step in the barrier method is:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Solving the barrier problem for fixed \(t\) with Newton's method</label>
                <label><input type="radio" name="q10" value="b"> B) Finding the center of the feasible region</label>
                <label><input type="radio" name="q10" value="c"> C) Update parameter \(t\)</label>
                <label><input type="radio" name="q10" value="d"> D) Check feasibility</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Solving the barrier problem for fixed $$t$$ with Newton's method</strong><br>
                The centering step solves $$\min tf(x) + \phi(x)$$ subject to $$Ax = b$$ to find $$x^*(t)$$ on the central path.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: For affine \(g_i\), the log barrier function \(-\log(-g_i(x))\) has the property of being:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Self-concordant</label>
                <label><input type="radio" name="q11" value="b"> B) Convex</label>
                <label><input type="radio" name="q11" value="c"> C) Smooth</label>
                <label><input type="radio" name="q11" value="d"> D) All of the above properties</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above properties</strong><br>
                For affine $$g_i$$, the log barrier function is convex, smooth and self-concordant, which gives Newton's method convergence guarantees. (For general convex $$g_i$$, the barrier is still convex and smooth but not necessarily self-concordant.)
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The Phase I problem for finding a feasible starting point:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) \(\min s\) subject to \(g_i(x) \leq s, Ax = b\)</label>
                <label><input type="radio" name="q12" value="b"> B) \(\min \|g(x)\|\)</label>
                <label><input type="radio" name="q12" value="c"> C) \(\min f(x)\)</label>
                <label><input type="radio" name="q12" value="d"> D) \(\min \|x\|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\min s$$ subject to $$g_i(x) \leq s, Ax = b$$</strong><br>
                Phase I finds a feasible point by minimizing the slack variable $$s$$. If the optimal $$s^* < 0$$ there is a strictly feasible point; if $$s^* > 0$$ the problem is infeasible.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The number of outer iterations of the barrier method to reach accuracy \(\epsilon\):</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(O(\log(1/\epsilon))\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(O(1/\epsilon)\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(O(\sqrt{1/\epsilon})\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(O(1/\epsilon^2)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$O(\log(1/\epsilon))$$</strong><br>
                With the update rule $$t^{(k+1)} = \mu t^{(k)}$$, $$O(\log(1/\epsilon))$$ outer iterations are needed to reduce the duality gap.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: The Newton decrement in the barrier method is used as:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) The stopping criterion for the centering step</label>
                <label><input type="radio" name="q14" value="b"> B) Update parameter \(t\)</label>
                <label><input type="radio" name="q14" value="c"> C) Check feasibility</label>
                <label><input type="radio" name="q14" value="d"> D) Compute duality gap</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The stopping criterion for the centering step</strong><br>
                The Newton decrement $$\lambda(x) \leq \eta$$ is the stopping criterion that ensures $$x$$ is close enough to the central path before updating $$t$$.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: Primal-dual interior point methods differ from the barrier method in that they:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Update both primal and dual variables simultaneously</label>
                <label><input type="radio" name="q15" value="b"> B) Do not need the central path</label>
                <label><input type="radio" name="q15" value="c"> C) Only apply to linear programs</label>
                <label><input type="radio" name="q15" value="d"> D) Do not need Newton's method</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Update both primal and dual variables simultaneously</strong><br>
                Primal-dual methods update $$(x, \lambda, \nu)$$ together instead of solving only for $$x$$ as the barrier method does.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: The typical choice for the barrier parameter update:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(t^{(k+1)} = \mu t^{(k)}\) with \(\mu = 10\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(t^{(k+1)} = t^{(k)} + 1\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(t^{(k+1)} = 2t^{(k)}\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(t^{(k+1)} = t^{(k)}^2\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$t^{(k+1)} = \mu t^{(k)}$$ with $$\mu = 10$$</strong><br>
                $$\mu = 10$$ is usually chosen to balance the number of outer iterations against the computational cost of each centering step.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: Advantages of the barrier method:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Polynomial-time complexity</label>
                <label><input type="radio" name="q17" value="b"> B) Warm-start capability</label>
                <label><input type="radio" name="q17" value="c"> C) Handle inequality constraints naturally</label>
                <label><input type="radio" name="q17" value="d"> D) All of the above advantages</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above advantages</strong><br>
                The barrier method has polynomial complexity, supports warm starts, and handles inequality constraints naturally.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: Given the LP: \(\min c^Tx\) s.t. \(Ax = b, x \geq 0\). The barrier function is:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) \(-\sum_{i=1}^n \log x_i\)</label>
                <label><input type="radio" name="q18" value="b"> B) \(\sum_{i=1}^n \log x_i\)</label>
                <label><input type="radio" name="q18" value="c"> C) \(-\sum_{i=1}^n x_i\)</label>
                <label><input type="radio" name="q18" value="d"> D) \(\sum_{i=1}^n x_i^2\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$-\sum_{i=1}^n \log x_i$$</strong><br>
                For the constraints $$x_i \geq 0$$, the log barrier function is $$-\sum_{i=1}^n \log x_i$$, which enforces $$x_i > 0$$.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: The barrier method differs from the penalty method in that:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) The barrier keeps the solution in the feasible region</label>
                <label><input type="radio" name="q19" value="b"> B) The penalty allows constraint violations</label>
                <label><input type="radio" name="q19" value="c"> C) The barrier needs a feasible starting point</label>
                <label><input type="radio" name="q19" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                The barrier method maintains feasibility and needs a feasible start, unlike the penalty method, which allows constraint violations.
            </div>
        </div>

        <!-- Question 20: Applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: Interior point methods are applied in:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Linear programming solvers</label>
                <label><input type="radio" name="q20" value="b"> B) Semidefinite programming</label>
                <label><input type="radio" name="q20" value="c"> C) Convex optimization packages</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above applications</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above applications</strong><br>
                Interior point methods are the foundation of modern optimization solvers: CPLEX, Gurobi, CVX, MOSEK.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: The barrier method transforms a constrained problem into:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) A sequence of unconstrained problems</label>
                <label><input type="radio" name="q21" value="b"> B) A linear problem</label>
                <label><input type="radio" name="q21" value="c"> C) A QP problem</label>
                <label><input type="radio" name="q21" value="d"> D) An SDP problem</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) A sequence of unconstrained problems</strong><br>
                Barrier method: $$\min t f(x) + \phi(x)$$ (equivalently $$\min f(x) + \frac{1}{t}\phi(x)$$) with $$\phi$$ the barrier function, $$t \to \infty$$.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The logarithmic barrier for the constraints $$g_i(x) \leq 0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$-\sum \log(-g_i(x))$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$\sum \log(g_i(x))$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$\sum g_i(x)^2$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$\sum |g_i(x)|$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$-\sum \log(-g_i(x))$$</strong><br>
                Log barrier: $$\phi(x) = -\sum_{i=1}^m \log(-g_i(x))$$ with $$g_i(x) < 0$$.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: The central path in the barrier method is:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) The set of solutions of $$t\nabla f + \nabla \phi + A^T\nu = 0$$</label>
                <label><input type="radio" name="q23" value="b"> B) A straight line through the solution</label>
                <label><input type="radio" name="q23" value="c"> C) The boundary of the feasible region</label>
                <label><input type="radio" name="q23" value="d"> D) The gradient descent path</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The set of solutions of $$t\nabla f + \nabla \phi + A^T\nu = 0$$</strong><br>
                Central path: $$x^*(t)$$ satisfies $$t\nabla f(x) + \nabla \phi(x) + A^T\nu = 0$$, $$Ax = b$$ for the parameter $$t > 0$$.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: As $$t \to \infty$$ in the barrier method:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) The solution approaches the original optimal solution</label>
                <label><input type="radio" name="q24" value="b"> B) The solution diverges</label>
                <label><input type="radio" name="q24" value="c"> C) The barrier function equals 0</label>
                <label><input type="radio" name="q24" value="d"> D) It has no meaning</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The solution approaches the original optimal solution</strong><br>
                As $$t \to \infty$$, the solution of the barrier problem approaches the solution of the original problem.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: For the constraint $$x > 0$$, the barrier function $$-\log x$$ has gradient:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$-1/x$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$1/x$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$-x$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$\log x$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$-1/x$$</strong><br>
                $$\frac{d}{dx}(-\log x) = -\frac{1}{x}$$.
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
    q1: 'b', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'd', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'a', q17: 'd', q18: 'a', q19: 'd', q20: 'd'
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
        message = '🌟 Excellent! You have mastered the barrier method and interior point optimization!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand the central path and convergence analysis well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review the log barrier function and the duality gap.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review the barrier problem and the KKT conditions.';
    } else {
        message = '📖 Study interior point methods again from the beginning!';
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

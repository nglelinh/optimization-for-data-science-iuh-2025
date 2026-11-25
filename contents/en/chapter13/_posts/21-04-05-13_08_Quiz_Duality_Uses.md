---
layout: post
title: '13-08 Multiple-Choice Quiz - Uses and Correspondences of Duality'
chapter: '13'
order: 12
owner: GitHub Copilot
lang: en
categories:
- chapter13
lesson_type: quiz
redirect_from:
  - /contents/en/chapter13/13_07_Quiz_Duality_Uses/
---

Before clicking through the multiple-choice questions below, pause and notice why duality questions are favorite traps on graduate qualifying exams: a single missing minus sign in $$f^*(y) = \max_x (y^T x - f(x))$$, a swapped primal/dual norm pair, or forgetting that an equivalent dual transformation can change the optimal value will flip an answer from right to wrong. Use the concept map and warm-up calculation below to sharpen your reflexes before starting the quiz.

## Background Knowledge Map: High-Yield Quiz Checkpoints

- **Pillar 1 — Duality Gap & Stopping Criteria:** Remember $$f(x) - f^\star \le f(x) - g(u,v)$$ requires $$x$$ primal feasible and $$(u,v)$$ dual feasible; zero gap certifies optimality under strong duality.
- **Pillar 2 — Dual Norm & Conjugate Pairings:** Memorize the exact pairs: $$\ell_1 \leftrightarrow \ell_\infty$$, $$\ell_2 \leftrightarrow \ell_2$$, trace norm $$\leftrightarrow$$ operator norm; norm $$\leftrightarrow$$ indicator of dual-norm unit ball; indicator $$\leftrightarrow$$ support function.
- **Pillar 3 — Splitting & Linear Transformations:** For $$\min_x f(x) + g(Ax)$$, the dual is $$\max_u -f^*(A^T u) - g^*(-u)$$. Watch the transpose $$A^T$$ and the minus sign on $$-u$$!
- **Pillar 4 — Dual Cones & Self-Duality:** $$K^* = \{y : y^T x \ge 0\ \forall x \in K\}$$ is always convex and closed; $$\mathbb{R}^n_+$$, $$\mathcal{Q}^n$$, and $$\mathbb{S}^n_+$$ are self-dual, and $$K^{**} = K$$ holds for closed convex cones.

### Step-by-Step Worked Example (Read Slowly): Rapid 4-Check Diagnostic Before the Quiz

Test yourself on four classic exam micro-calculations before taking the quiz:

1. **Duality gap check:** If primal feasible $$x$$ has $$f(x) = 14.2$$ and dual feasible $$(u,v)$$ has $$g(u,v) = 13.7$$, what is the tightest guaranteed bound on $$f(x) - f^\star$$?
   - Answer: $$f(x) - f^\star \le 14.2 - 13.7 = 0.5$$ (and $$f^\star \in [13.7, 14.2]$$).
2. **Dual norm check:** For $$y = (-2, 5, -1)^T$$, compute $$(\|y\|_1)_*$$ and $$(\|y\|_\infty)_*$$.
   - $$(\|y\|_1)_* = \|y\|_\infty = 5$$; $$(\|y\|_\infty)_* = \|y\|_1 = 2 + 5 + 1 = 8$$.
3. **Conjugate check:** For $$f(x) = \frac{1}{2}ax^2 + bx + c$$ ($$a > 0$$), compute $$f^*(y)$$.
   - Set $$\frac{d}{dx}(yx - \frac{1}{2}ax^2 - bx - c) = y - ax - b = 0 \implies x^\star = \frac{y-b}{a}$.
   - Substituting back: $$f^*(y) = \frac{(y-b)^2}{2a} - c$$.
4. **Dual cone check:** Is $$y = (-1, 3)^T$$ in the dual of the first quadrant $$K = \mathbb{R}^2_+$$?
   - Test with $$x = (1, 0)^T \in K$$: $$y^T x = -1 < 0$$. So $$y \notin (\mathbb{R}^2_+)^* = \mathbb{R}^2_+$$.

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### ⚡ **Uses of Duality**

#### **Two main uses of duality**

**1. The Duality Gap as a Stopping Criterion:**
- **Duality gap:** $$f(x) - g(u,v)$$ with $$x$$ primal feasible, $$(u,v)$$ dual feasible
- **Upper bound on suboptimality:** $$f(x) - f^* \le f(x) - g(u,v)$$
- **Optimality test:** If the duality gap = 0 then $$x$$ is optimal
- **Practical stopping:** Stop the algorithm when the duality gap is $$< \epsilon$$

**2. Solving Primal via Dual:**
Given a dual optimal $$u^*, v^*$$ and strong duality:
$$x^* = \arg\min_x L(x, u^*, v^*) = \arg\min_x \left\{ f(x) + \sum u_i^* h_i(x) + \sum v_j^* l_j(x) \right\}$$

**Advantage:** The dual may be easier to solve than the primal

### 🔄 **Solving the Primal via the Dual**

#### **Separable problems**
**Problem:** $$\min_x \sum_{i=1}^n f_i(x_i) \quad \text{s.t.} \quad a^T x = b$$

**Dual function:**
$$g(v) = bv - \sum_{i=1}^n f_i^*(a_i v)$$

**Dual problem:** $$\max_v bv - \sum_{i=1}^n f_i^*(a_i v)$$

**Recovery primal solution:**
Once $$v^*$$ is known, solve: $$\nabla f_i(x_i^*) = a_i v^*$$ for each $$i$$

**Advantages:**
- **Scalar optimization:** The dual has only 1 variable $$v$$
- **Parallel computation:** Each $$f_i^*$$ is computed independently
- **Closed-form:** Many $$f_i^*$$ have an analytical form

### 📏 **Dual Norms**

#### **Definition**
Given a norm $$\lVert x \rVert$$, the **dual norm** $$\lVert x \rVert_*$$ is defined as:
$$\lVert z \rVert_* = \max_{\lVert x \rVert \le 1} z^T x$$

#### **Basic properties**
- **Generalized Cauchy-Schwarz:** $$\lvert z^T x \rvert \le \lVert z \rVert_* \lVert x \rVert$$
- **Double dual:** $$\lVert x \rVert_{**} = \lVert x \rVert$$
- **Always a norm:** $$\lVert \cdot \rVert_*$$ is always a norm (a supremum of linear functions, hence always convex)

#### **Important examples**
- **$$\ell_p$$ norms:** $$(\lVert x \rVert_p)_* = \lVert x \rVert_q$$ with $$\frac{1}{p} + \frac{1}{q} = 1$$
  - $$(\lVert x \rVert_1)_* = \lVert x \rVert_\infty$$
  - $$(\lVert x \rVert_2)_* = \lVert x \rVert_2$$
  - $$(\lVert x \rVert_\infty)_* = \lVert x \rVert_1$$
- **Matrix norms:** $$(\lVert X \rVert_{tr})_* = \lVert X \rVert_{op} = \sigma_1(X)$$ (largest singular value)

#### **Dual norm characterization**
**Problem:** $$\min_y \lVert y \rVert \quad \text{s.t.} \quad y = x$$

**Dual problem:** $$\max_{\lVert u \rVert_* \le 1} u^T x$$

**Result:** $$\lVert x \rVert = \max_{\lVert u \rVert_* \le 1} u^T x$$

### 🎯 **Example: The LASSO Dual**

#### **Primal LASSO**
$$\min_\beta \frac{1}{2}\lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$$

#### **Reformulation**
$$\min_{\beta,z} \frac{1}{2}\lVert y - z \rVert_2^2 + \lambda \lVert \beta \rVert_1 \quad \text{s.t.} \quad z = X\beta$$

#### **Dual derivation**
**Lagrangian:**
$$L(\beta,z,u) = \frac{1}{2}\lVert y - z \rVert_2^2 + \lambda \lVert \beta \rVert_1 + u^T(z - X\beta)$$

**Dual function:**
$$g(u) = \frac{1}{2}\lVert y \rVert_2^2 - \frac{1}{2}\lVert y - u \rVert_2^2 - I_{\{\lVert X^T u \rVert_\infty \le \lambda\}}(u)$$

#### **LASSO dual problem**
$$\min_u \lVert y - u \rVert_2^2 \quad \text{s.t.} \quad \lVert X^T u \rVert_\infty \le \lambda$$

#### **Primal-dual relationship**
- **Strong duality:** Slater's condition satisfied
- **Primal recovery:** $$X\beta^* = y - u^*$$
- **Residual interpretation:** $$u^*$$ is the dual residual

### 🔗 **Conjugate Functions and Dual Problems**

#### **Conjugate function**
$$f^*(u) = \sup_x \{u^T x - f(x)\}$$

**Equivalent:** $$-f^*(u) = \min_x \{f(x) - u^T x\}$$

#### **Composite problems**
**Problem:** $$\min_x f(x) + g(x)$$

**Equivalent constrained form:**
$$\min_{x,z} f(x) + g(z) \quad \text{s.t.} \quad x = z$$

**Dual function:**
$$g(u) = \min_{x,z} f(x) + g(z) + u^T(z - x) = -f^*(u) - g^*(-u)$$

**Dual problem:** $$\max_u -f^*(u) - g^*(-u)$$

#### **Application examples**

**1. Indicator function:**
$$\min_x f(x) + I_C(x) \Rightarrow \max_u -f^*(u) - I_C^*(-u)$$

where $$I_C^*$$ is the support function of $$C$$

**2. Norm regularization:**
$$\min_x f(x) + \lVert x \rVert \Rightarrow \max_{\lVert u \rVert_* \le 1} -f^*(u)$$

### 🔺 **Dual Cones**

#### **Definition**
Given a cone $$K \subseteq \mathbb{R}^n$$, the **dual cone** $$K^*$$ is:
$$K^* = \{y : y^T x \ge 0 \quad \forall x \in K\}$$

#### **Properties**
- **Always convex:** $$K^*$$ is always convex even when $$K$$ is not convex
- **Double dual:** If $$K$$ is a closed convex cone then $$K^{**} = K$$
- **Geometric interpretation:** $$y \in K^* \Leftrightarrow$$ halfspace $$\{x : y^T x \ge 0\}$$ contains $$K$$

#### **Important examples**

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

**Derivation:** Using the support function $$I_K^*(y) = \max_{z \in K} z^T y$$

#### **Example: Second-Order Cone Programming (SOCP)**
**Primal:** $$\min c^T x \quad \text{s.t.} \quad \lVert A_i x + b_i \rVert_2 \le c_i^T x + d_i$$

**Equivalent conic form:** $$Ax + b \in K$$ (stacking $$(A_i x + b_i, c_i^T x + d_i)$$) with $$K$$ a product of second-order cones

**Dual:** $$\max -b^T u \quad \text{s.t.} \quad A^T u = c, \quad u \in K^*$$

### 🛠️ **Practical Techniques**

#### **When to use duality:**
1. **Dual easier:** Fewer variables, simpler structure
2. **Bounds needed:** Duality gap for convergence monitoring
3. **Sensitivity analysis:** Dual variables as shadow prices
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

### 💡 **Illustrative Examples**

#### **Simple norm minimization:**
**Problem:** $$\min_x \lVert x \rVert_2 \quad \text{s.t.} \quad Ax = b$$

**Dual:** $$\max_{A^T u = 0} -b^T u$$

**Interpretation:** Find $$u \perp row(A)$$ maximizing $$-b^T u$$

**Solution:** $$u^* = -A^+ b$$ (pseudoinverse)

#### **$$\ell_1$$ minimization:**
**Problem:** $$\min_x \lVert x \rVert_1 \quad \text{s.t.} \quad Ax = b$$

**Dual:** $$\max_{\lVert A^T u \rVert_\infty \le 1} b^T u$$

**Geometric interpretation:** Find $$u$$ in the dual feasible set maximizing $$b^T u$$

### 🎯 **Connections to Other Chapters**

#### **From the previous chapter:**
- **Chapter 12:** KKT conditions - interpretation of dual variables
- **Chapter 11:** General duality theory - the foundation
- **Chapter 10:** LP duality - a special case

#### **Importance of Duality Uses:**
- **Computational efficiency:** Solve easier dual instead of primal
- **Algorithm design:** Primal-dual methods, decomposition
- **Theoretical insights:** Optimality conditions, sensitivity
- **Practical applications:** Machine learning, signal processing

#### **Looking ahead:**
- **Interior point methods:** Barrier function approaches
- **Decomposition methods:** ADMM, dual decomposition
- **Stochastic optimization:** Online dual methods
- **Robust optimization:** Worst-case analysis

### 🌟 **Theoretical Significance**

#### **Duality as a computational tool:**
- **Alternative solution path:** The dual can be easier than the primal
- **Parallel computation:** Separable structure exploitation
- **Convergence monitoring:** The duality gap as a stopping criterion
- **Sensitivity analysis:** Dual variables interpretation

#### **Geometric insights:**
- **Dual norms:** Characterize the unit balls of different norms
- **Dual cones:** Geometric duality in cone programming
- **Support functions:** Convex analysis foundation
- **Conjugate functions:** Legendre-Fenchel transform

#### **Algorithmic implications:**
- **Primal-dual methods:** Simultaneous updates
- **Decomposition:** Exploit problem structure
- **Interior point:** Barrier function approaches
- **Augmented Lagrangian:** Penalty method improvements

### 💡 **Practical Tips**

#### **Choosing primal vs dual:**
1. **Variable count:** Fewer variables often easier
2. **Constraint structure:** Simple constraints preferred
3. **Separability:** Dual exploits separable structure
4. **Computational resources:** Parallel vs sequential

#### **Implementation tips:**
- **Numerical stability:** Check condition numbers
- **Convergence monitoring:** Use duality gap
- **Warm starting:** Initialize with previous solutions
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

### 📈 **Real-World Applications**

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
- **Distributed optimization:** Consensus and duality
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
- **Algorithm design:** Foundation for modern optimization
- **Software implementation:** Dual methods in solvers
- **Real-world problems:** Enable the solution of large-scale problems
- **Interdisciplinary applications:** Across science and engineering

### 🌟 **Legacy of Chapter 13:**

- **Computational revolution:** Duality enables efficient algorithms
- **Theoretical unification:** Connects diverse optimization areas
- **Practical impact:** Solves real-world problems efficiently
- **Educational value:** Bridges theory and applications
- **Scientific influence:** Foundation for modern optimization

---

💡 **Final message:** Duality is not just a mathematical curiosity - it is a **powerful computational tool** enabling the efficient solution of complex optimization problems across science, engineering, and machine learning!

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

This multiple-choice quiz tests your understanding of the uses and correspondences of duality, including conjugate functions, dual norms, the LASSO dual, dual cones and advanced duality concepts.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: Uses and Correspondences of Duality</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1 -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: The conjugate function $$f^*(y)$$ is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) $$f^*(y) = \max_x (y^T x - f(x))$$</label>
                <label><input type="radio" name="q1" value="b"> B) $$f^*(y) = \min_x (y^T x - f(x))$$</label>
                <label><input type="radio" name="q1" value="c"> C) $$f^*(y) = \max_x (y^T x + f(x))$$</label>
                <label><input type="radio" name="q1" value="d"> D) $$f^*(y) = f(y)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f^*(y) = \max_x (y^T x - f(x))$$</strong><br>
                The conjugate function (Legendre-Fenchel transform) is the supremum of the linear function $$y^T x$$ minus $$f(x)$$.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The conjugate function $$f^*$$ has the property of being:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Always convex</label>
                <label><input type="radio" name="q2" value="b"> B) Always concave</label>
                <label><input type="radio" name="q2" value="c"> C) Of the same convexity as $$f$$</label>
                <label><input type="radio" name="q2" value="d"> D) Undeterminable</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Always convex</strong><br>
                The conjugate function is always convex because it is a supremum of affine functions, whether or not $$f$$ is convex.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: If $$f$$ is convex and lower semicontinuous, then $$f^{**}$$ equals:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$f$$</label>
                <label><input type="radio" name="q3" value="b"> B) $$-f$$</label>
                <label><input type="radio" name="q3" value="c"> C) $$f^*$$</label>
                <label><input type="radio" name="q3" value="d"> D) $$0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f$$</strong><br>
                Fenchel-Moreau theorem: if $$f$$ is convex and lower semicontinuous then $$f^{**} = f$$.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The dual norm $$\lVert x \rVert_*$$ is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$\lVert x \rVert_* = \max_{\lVert z \rVert \leq 1} z^T x$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$\lVert x \rVert_* = \min_{\lVert z \rVert \leq 1} z^T x$$</label>
                <label><input type="radio" name="q4" value="c"> C) $$\lVert x \rVert_* = \max_{\lVert z \rVert = 1} z^T x$$</label>
                <label><input type="radio" name="q4" value="d"> D) $$\lVert x \rVert_* = \lVert x \rVert$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\|x\|_* = \max_{\|z\| \leq 1} z^T x$$</strong><br>
                The dual norm is the maximum inner product with vectors in the unit ball of the primal norm.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The dual norm of the $$\ell_p$$ norm is:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) $$\ell_p$$ norm</label>
                <label><input type="radio" name="q5" value="b"> B) $$\ell_q$$ norm with $$1/p + 1/q = 1$$</label>
                <label><input type="radio" name="q5" value="c"> C) \(\ell_\infty\) norm</label>
                <label><input type="radio" name="q5" value="d"> D) \(\ell_1\) norm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\ell_q$$ norm with $$1/p + 1/q = 1$$</strong><br>
                Hölder conjugate: the dual of $$\ell_p$$ is $$\ell_q$$ with $$1/p + 1/q = 1$$. In particular: the dual of $$\ell_1$$ is $$\ell_\infty$$.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: Hölder's inequality has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(|x^T y| \leq \|x\|_p \|y\|_q\) with \(1/p + 1/q = 1\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(|x^T y| \leq \|x\|_p \|y\|_p\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(|x^T y| \geq \|x\|_p \|y\|_q\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\|x + y\|_p \leq \|x\|_p + \|y\|_p\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$|x^T y| \leq \|x\|_p \|y\|_q$$ with $$1/p + 1/q = 1$$</strong><br>
                Hölder's inequality generalizes Cauchy-Schwarz, relating dual norms to the inner product.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: The dual norm of the nuclear norm (trace norm) is:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Frobenius norm</label>
                <label><input type="radio" name="q7" value="b"> B) Operator norm (spectral norm)</label>
                <label><input type="radio" name="q7" value="c"> C) Nuclear norm</label>
                <label><input type="radio" name="q7" value="d"> D) \(\ell_1\) norm of the singular values</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Operator norm (spectral norm)</strong><br>
                The dual of the nuclear norm $$\|X\|_* = \sum \sigma_i$$ is the operator norm $$\|X\|_{op} = \sigma_1$$ (largest singular value).
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The LASSO dual problem has the constraint:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\|A^T u\|_\infty \leq \lambda\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(\|A^T u\|_1 \leq \lambda\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(\|A^T u\|_2 \leq \lambda\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(\|u\|_2 \leq \lambda\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\|A^T u\|_\infty \leq \lambda$$</strong><br>
                LASSO dual constraint: $$\|A^T u\|_\infty \leq \lambda$$ because the dual of the $$\ell_1$$ norm is the $$\ell_\infty$$ norm.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The conjugate of \(f(x) = \frac{1}{2}x^T Q x\) with \(Q \succ 0\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(f^*(y) = \frac{1}{2}y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(f^*(y) = \frac{1}{2}y^T Q y\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(f^*(y) = y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(f^*(y) = \frac{1}{2}y^T Q^{-2} y\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f^*(y) = \frac{1}{2}y^T Q^{-1} y$$</strong><br>
                The conjugate of a quadratic form with $$Q \succ 0$$ is the quadratic form with $$Q^{-1}$$.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The conjugate of the indicator function \(I_C(x)\) of a convex set \(C\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(I_C^*(y) = \sup_{x \in C} y^T x\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(I_C^*(y) = \inf_{x \in C} y^T x\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(I_C^*(y) = I_C(y)\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(I_C^*(y) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$I_C^*(y) = \sup_{x \in C} y^T x$$</strong><br>
                The conjugate of an indicator function is the support function of the set $$C$$.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: The dual cone \(K^*\) of a cone \(K\) is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(K^* = \{y : y^T x \geq 0 \text{ for all } x \in K\}\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(K^* = \{y : y^T x \leq 0 \text{ for all } x \in K\}\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(K^* = \{y : y^T x = 0 \text{ for all } x \in K\}\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(K^* = K\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$K^* = \{y : y^T x \geq 0 \text{ for all } x \in K\}$$</strong><br>
                The dual cone consists of the vectors that make a non-obtuse angle with every vector in the original cone.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: Which of the following cones is self-dual?</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Positive orthant \(\mathbb{R}_+^n\)</label>
                <label><input type="radio" name="q12" value="b"> B) Second-order cone (Lorentz cone)</label>
                <label><input type="radio" name="q12" value="c"> C) Positive semidefinite cone</label>
                <label><input type="radio" name="q12" value="d"> D) All of the cones above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the cones above</strong><br>
                The positive orthant, the second-order cone and the PSD cone are all self-dual: $$K^* = K$$.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The conjugate of a norm \(\|x\|\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(f^*(y) = I_{\{\|y\|_* \leq 1\}}(y)\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(f^*(y) = \|y\|_*\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(f^*(y) = \|y\|\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(f^*(y) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f^*(y) = I_{\{\|y\|_* \leq 1\}}(y)$$</strong><br>
                The conjugate of a norm is the indicator function of the dual-norm unit ball.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: The Fenchel duality theorem for the problem \(\min f(x) + g(Ax)\):</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(\min f(x) + g(Ax) = \max -f^*(-A^T y) - g^*(y)\)</label>
                <label><input type="radio" name="q14" value="b"> B) \(\min f(x) + g(Ax) = \max f^*(A^T y) + g^*(y)\)</label>
                <label><input type="radio" name="q14" value="c"> C) \(\min f(x) + g(Ax) = \min f^*(x) + g^*(Ax)\)</label>
                <label><input type="radio" name="q14" value="d"> D) There is no relation</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\min f(x) + g(Ax) = \max -f^*(-A^T y) - g^*(y)$$</strong><br>
                Fenchel duality connects the primal problem with the dual problem through conjugate functions.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: The Legendre transform is used when:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(f\) is convex and differentiable</label>
                <label><input type="radio" name="q15" value="b"> B) \(f\) is concave</label>
                <label><input type="radio" name="q15" value="c"> C) \(f\) is linear</label>
                <label><input type="radio" name="q15" value="d"> D) \(f\) is non-convex</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f$$ is convex and differentiable</strong><br>
                The Legendre transform is the special case of the conjugate function when $$f$$ is convex and differentiable.
            </div>
        </div>

        <!-- Question 16: Moreau envelope -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: The Moreau envelope \(M_\lambda f(x)\) is related to:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Proximal operator</label>
                <label><input type="radio" name="q16" value="b"> B) Conjugate function</label>
                <label><input type="radio" name="q16" value="c"> C) Smoothing of \(f\)</label>
                <label><input type="radio" name="q16" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                The Moreau envelope connects the proximal operator and the conjugate function, and provides a smooth approximation of $$f$$.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: The Fenchel-Young inequality states that:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(f(x) + f^*(y) \geq x^T y\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(f(x) + f^*(y) \leq x^T y\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(f(x) + f^*(y) = x^T y\)</label>
                <label><input type="radio" name="q17" value="d"> D) \(f(x) - f^*(y) \geq x^T y\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f(x) + f^*(y) \geq x^T y$$</strong><br>
                Fenchel-Young inequality: $$f(x) + f^*(y) \geq x^T y$$ with equality when $$y \in \partial f(x)$$.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: When should we solve the dual problem instead of the primal?</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) When the dual has fewer variables</label>
                <label><input type="radio" name="q18" value="b"> B) When the dual has a simpler structure</label>
                <label><input type="radio" name="q18" value="c"> C) When strong duality holds</label>
                <label><input type="radio" name="q18" value="d"> D) All of the above cases</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above cases</strong><br>
                Solving the dual is advantageous when it has fewer variables, a simpler structure, or computational advantages, provided strong duality holds.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: The conjugate of \(f(x) = \max\{f_1(x), f_2(x)\}\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(f^*(y) = \max\{f_1^*(y), f_2^*(y)\}\)</label>
                <label><input type="radio" name="q19" value="b"> B) \(f^*(y) = \min\{f_1^*(y), f_2^*(y)\}\)</label>
                <label><input type="radio" name="q19" value="c"> C) \(f^*(y) = f_1^*(y) + f_2^*(y)\)</label>
                <label><input type="radio" name="q19" value="d"> D) \(f^*(y) = \inf\{\lambda_1 f_1^*(y_1/\lambda_1) + \lambda_2 f_2^*(y_2/\lambda_2) : y_1 + y_2 = y,\ \lambda_1 + \lambda_2 = 1, \lambda_i \geq 0\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) $$f^*(y) = \inf\{\lambda_1 f_1^*(y_1/\lambda_1) + \lambda_2 f_2^*(y_2/\lambda_2) : y_1 + y_2 = y,\ \lambda_1 + \lambda_2 = 1, \lambda_i \geq 0\}$$</strong><br>
                For closed convex $$f_1, f_2$$: the conjugate of the max is the convex hull of $$\min\{f_1^*, f_2^*\}$$, which is exactly formula D (using perspectives). Answer B is only $$\min\{f_1^*, f_2^*\}$$, which is generally not convex and so cannot be a conjugate. Example: $$\max\{x, -x\} = |x|$$ has conjugate $$I_{[-1,1]}$$, whereas $$\min\{I_{\{1\}}, I_{\{-1\}}\} = I_{\{-1,1\}}$$.
            </div>
        </div>

        <!-- Question 20: Applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: Conjugate duality is applied in:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Machine learning (regularization, kernel methods)</label>
                <label><input type="radio" name="q20" value="b"> B) Signal processing (compressed sensing, denoising)</label>
                <label><input type="radio" name="q20" value="c"> C) Economics (utility theory, market equilibrium)</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above fields</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above fields</strong><br>
                Conjugate duality has wide applications: ML (regularization), signal processing (sparsity), economics (utility maximization), and many other fields.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: Sensitivity analysis in optimization studies:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) How the solution changes when parameters change</label>
                <label><input type="radio" name="q21" value="b"> B) The sensitivity of the algorithm</label>
                <label><input type="radio" name="q21" value="c"> C) The convergence rate</label>
                <label><input type="radio" name="q21" value="d"> D) Numerical accuracy</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) How the solution changes when parameters change</strong><br>
                Sensitivity analysis studies how the optimal solution changes when the problem parameters change.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: In LP, the shadow price of constraint $$i$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) The value of the dual variable $$y_i^*$$</label>
                <label><input type="radio" name="q22" value="b"> B) The value of a primal variable</label>
                <label><input type="radio" name="q22" value="c"> C) A coefficient in the objective function</label>
                <label><input type="radio" name="q22" value="d"> D) Slack variable</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The value of the dual variable $$y_i^*$$</strong><br>
                Shadow price = dual variable; it tells how much the optimal value increases when the constraint is relaxed by one unit.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: The envelope theorem in optimization states that:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$\frac{\partial f^*(\theta)}{\partial \theta} = \frac{\partial L}{\partial \theta}$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$\frac{\partial f^*}{\partial x} = 0$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$\frac{\partial^2 f^*}{\partial \theta^2} = 0$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$f^*(\theta) = \text{const}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\frac{\partial f^*(\theta)}{\partial \theta} = \frac{\partial L}{\partial \theta}$$</strong><br>
                Envelope theorem: the derivative of the optimal value with respect to a parameter equals the partial derivative of the Lagrangian.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: Parametric programming studies problems of the form:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$\min f(x,\theta)$$ subject to $$g(x,\theta) \leq 0$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$\min f(x)$$ subject to $$g(x) \leq \theta$$</label>
                <label><input type="radio" name="q24" value="c"> C) Both A and B</label>
                <label><input type="radio" name="q24" value="d"> D) No parameters</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Both A and B</strong><br>
                Parametric programming considers optimization problems with parameters in the objective and/or the constraints.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: In portfolio optimization, when risk aversion increases:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) A less risky portfolio is chosen</label>
                <label><input type="radio" name="q25" value="b"> B) A riskier portfolio is chosen</label>
                <label><input type="radio" name="q25" value="c"> C) Nothing changes</label>
                <label><input type="radio" name="q25" value="d"> D) Return is maximized</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) A less risky portfolio is chosen</strong><br>
                Higher risk aversion leads to choosing a portfolio with lower variance (risk).
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
    q1: 'a', q2: 'a', q3: 'a', q4: 'a', q5: 'b',
    q6: 'a', q7: 'b', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'd', q13: 'a', q14: 'a', q15: 'a',
    q16: 'd', q17: 'a', q18: 'd', q19: 'd', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'c', q25: 'a'};

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
        message = '🌟 Excellent! You have mastered advanced duality theory!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand conjugate functions and dual norms well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review the conjugate properties and Fenchel duality.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review conjugate functions and dual cones.';
    } else {
        message = '📖 Study the advanced duality concepts again from the beginning!';
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

---
layout: post
title: '12-08 Multiple-Choice Quiz - KKT Conditions'
chapter: '12'
order: 9
owner: GitHub Copilot
lang: en
categories:
- chapter12
lesson_type: quiz
redirect_from:
  - /contents/en/chapter12/12_07_Quiz_KKT_Conditions/
---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### ⚡ **The Karush-Kuhn-Tucker (KKT) Conditions**

#### **General optimization problem**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad l_j(x) = 0$$

with $$i = 1,\ldots,m$$ and $$j = 1,\ldots,r$$

#### **The four KKT conditions**
Given $$x^*, \lambda^*, \nu^*$$:

1. **Stationarity:**
   $$0 \in \partial \left( f(x^*) + \sum_{i=1}^m \lambda_i^* h_i(x^*) + \sum_{j=1}^r \nu_j^* l_j(x^*) \right)$$

2. **Complementary Slackness:**
   $$\lambda_i^* \cdot h_i(x^*) = 0 \quad \forall i$$

3. **Primal Feasibility:**
   $$h_i(x^*) \le 0, \quad l_j(x^*) = 0 \quad \forall i,j$$

4. **Dual Feasibility:**
   $$\lambda_i^* \ge 0 \quad \forall i$$

#### **Meaning of the conditions**
- **Stationarity:** The gradient of the Lagrangian is 0
- **Complementary slackness:** Either the constraint is active ($$h_i = 0$$) or the dual variable is 0 ($$\lambda_i = 0$$)
- **Primal feasibility:** All constraints of the original problem are satisfied
- **Dual feasibility:** Dual variables for inequality constraints must be non-negative

### 📊 **Sufficiency and Necessity**

#### **Sufficiency**
**If** $$x^*, \lambda^*, \nu^*$$ satisfy the KKT conditions and the problem is **convex**, **then** they are optimal solutions.

**Proof:**
$$g(\lambda^*, \nu^*) = \min_x L(x, \lambda^*, \nu^*) = L(x^*, \lambda^*, \nu^*) = f(x^*)$$

Hence: $$g(\lambda^*, \nu^*) = f(x^*)$$ ⟹ duality gap = 0 ⟹ optimal

#### **Necessity**
**If** $$x^*, \lambda^*, \nu^*$$ are optimal solutions with **strong duality**, **then** they satisfy the KKT conditions.

**Condition:** Strong duality (e.g. Slater's condition)

#### **Summary**
For convex problems with strong duality:
$$x^*, \lambda^*, \nu^* \text{ optimal} \Leftrightarrow x^*, \lambda^*, \nu^* \text{ satisfy KKT}$$

### 🔄 **Example: Quadratic Programming with Equality Constraints**

#### **Problem**
$$\min_x \frac{1}{2}x^T P x + q^T x + r \quad \text{s.t.} \quad Ax = b$$

with $$P \in \mathbb{S}_+^n$$ (positive semidefinite)

#### **KKT conditions**
- **Stationarity:** $$Px^* + q + A^T \nu^* = 0$$
- **Primal feasibility:** $$Ax^* = b$$
- **Complementary slackness:** None (no inequality constraints)
- **Dual feasibility:** None (no inequality constraints)

#### **The KKT Matrix System**
$$\begin{bmatrix} P & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x^* \\ \nu^* \end{bmatrix} = \begin{bmatrix} -q \\ b \end{bmatrix}$$

**Meaning:** This is exactly the **Newton step** for constrained optimization!

### 🌊 **Example: The Water-Filling Algorithm**

#### **Problem**
$$\min_x -\sum_{i=1}^n \log(\alpha_i + x_i) \quad \text{s.t.} \quad x \succeq 0, \quad \mathbf{1}^T x = 1$$

with $$\alpha_i > 0$$

#### **KKT conditions**
- **Stationarity:** $$-\frac{1}{\alpha_i + x_i^*} - \lambda_i^* + \nu^* = 0$$
- **Complementary slackness:** $$\lambda_i^* x_i^* = 0$$
- **Primal feasibility:** $$x^* \succeq 0, \mathbf{1}^T x^* = 1$$
- **Dual feasibility:** $$\lambda^* \succeq 0$$

#### **Analytical solution**
$$x_i^* = \max\left\{0, \frac{1}{\nu^*} - \alpha_i\right\}$$

with $$\nu^*$$ determined by: $$\sum_{i=1}^n \max\left\{0, \frac{1}{\nu^*} - \alpha_i\right\} = 1$$

#### **Water-filling interpretation**
- $$\alpha_i$$: "Ground level" of channel $$i$$
- $$\frac{1}{\nu^*}$$: "Water level" chung
- $$x_i^*$$: "Water depth" in channel $$i$$
- **Algorithm:** Pour water until the total volume = 1

### 🎯 **Example: Support Vector Machine (SVM)**

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
**Point $$i$$ is a support vector** ⟺ $$w_i^* > 0$$

**Two types of support vectors:**
- **On margin:** $$\xi_i^* = 0$$, $$w_i^* \in (0, C]$$
- **Inside margin:** $$\xi_i^* > 0$$, $$w_i^* = C$$

#### **Practical implications**
- **Sparsity:** Only support vectors have $$w_i^* > 0$$
- **Efficiency:** Non-support points can be filtered out before optimizing
- **Interpretation:** The KKT conditions explain the structure of the SVM solution

### 🔄 **Constrained Form vs Lagrangian Form**

#### **Constrained form (C)**
$$\min_x f(x) \quad \text{s.t.} \quad h(x) \le t$$

#### **Lagrangian form (L)**
$$\min_x f(x) + \lambda h(x)$$

#### **Equivalence conditions**
**When are (C) and (L) equivalent?**

1. **(C) → (L):** If (C) satisfies Slater + strong duality, there exists $$\lambda^* \ge 0$$ such that a solution of (C) is also a solution of (L)

2. **(L) → (C):** If $$x^*$$ solves (L) and the KKT conditions hold, then $$x^*$$ also solves (C) with $$t = h(x^*)$$

#### **Perfect equivalence**
**When:** $$h(x) \ge 0$$ (like a norm), $$t = 0$$, $$\lambda = \infty$$

**Result:** Both enforce $$h(x) = 0$$

### 🛠️ **Practical Techniques**

#### **Checking the KKT conditions:**
1. **Verify stationarity:** $$\nabla_x L(x^*, \lambda^*, \nu^*) = 0$$
2. **Check complementary slackness:** $$\lambda_i^* h_i(x^*) = 0 \quad \forall i$$
3. **Verify feasibility:** Primal and dual constraints
4. **Confirm optimality:** If convex + KKT ⟹ optimal

#### **Analytical solution strategy:**
1. **Write the KKT conditions** for the specific problem
2. **Use complementary slackness** to identify the active constraints
3. **Solve the system of equations** from stationarity + feasibility
4. **Verify that the solution** satisfies all KKT conditions

#### **Computational applications:**
- **Active set methods:** Identify active constraints iteratively
- **Interior point methods:** Follow central path satisfying KKT
- **Primal-dual methods:** Update primal and dual simultaneously

### 💡 **Illustrative Examples**

#### **Simple problem:**
$$\min_x x^2 + y^2 \quad \text{s.t.} \quad x + y = 1, \quad x \ge 0$$

**KKT conditions:**
- **Stationarity:** $$2x^* - \lambda^* + \nu^* = 0$$, $$2y^* + \nu^* = 0$$
- **Complementary slackness:** $$\lambda^* x^* = 0$$
- **Primal feasibility:** $$x^* + y^* = 1$$, $$x^* \ge 0$$
- **Dual feasibility:** $$\lambda^* \ge 0$$

**Case analysis:**
- **Case 1:** $$x^* > 0$$ ⟹ $$\lambda^* = 0$$ ⟹ $$x^* = y^* = 1/2$$
- **Case 2:** $$x^* = 0$$ ⟹ $$y^* = 1$$ ⟹ $$\nu^* = -2$$ ⟹ $$\lambda^* = -2 < 0$$ (violates dual feasibility, rejected)

**Optimal solution:** $$x^* = 1/2, y^* = 1/2$$, $$\nu^* = -1$$, $$\lambda^* = 0$$ (only Case 1 satisfies KKT)

### 🎯 **Connections to Other Chapters**

#### **From the previous chapter:**
- **Chapter 11:** General duality theory - KKT is a direct consequence
- **Chapter 10:** LP duality - KKT generalizes the optimality conditions
- **Chapter 04:** First-order optimality conditions - KKT extends them to constrained problems

#### **Importance of KKT:**
- **Optimality characterization:** Necessary and sufficient conditions
- **Algorithm design:** Active set, interior point, SQP methods
- **Theoretical analysis:** Sensitivity, perturbation theory
- **Machine learning:** SVM, regularization, constrained learning

#### **Looking ahead:**
- **Second-order conditions:** Bordered Hessian, LICQ, MFCQ
- **Nonlinear programming:** SQP, trust region methods
- **Variational inequalities:** Complementarity problems
- **Optimal control:** Pontryagin maximum principle

### 🌟 **Theoretical Significance**

#### **KKT as universal optimality conditions:**
- **Unifies:** Unconstrained ($$\nabla f = 0$$) and constrained optimization
- **Characterizes:** Exactly when point is optimal
- **Enables:** Systematic algorithm design
- **Connects:** Primal and dual perspectives

#### **Geometric interpretation:**
- **Stationarity:** Gradient orthogonal to feasible directions
- **Complementary slackness:** Either the constraint is active or the multiplier is zero
- **Feasibility:** Point lies in feasible region
- **Non-negativity:** Consistent with the constraint directions

#### **Computational significance:**
- **Algorithm foundation:** Most constrained optimization algorithms
- **Convergence criteria:** KKT residual as a stopping condition
- **Sensitivity analysis:** Dual variables as shadow prices
- **Problem structure:** Active set identification

### 💡 **Practical Tips**

#### **When to use KKT:**
1. **Analytical solutions:** Small problems with closed-form solutions
2. **Algorithm design:** Foundation for numerical methods
3. **Optimality verification:** Check if candidate point optimal
4. **Sensitivity analysis:** Understand parameter changes

#### **Common pitfalls:**
- **Forget constraint qualifications:** LICQ, MFCQ for necessity
- **Wrong complementary slackness:** $$\lambda_i h_i = 0$$ only means that at least one of the two is 0; an active constraint can still have $$\lambda_i = 0$$
- **Non-convex problems:** KKT necessary but not sufficient
- **Numerical issues:** The KKT matrix can be ill-conditioned

#### **Debugging strategies:**
- **Check each condition separately:** Stationarity, slackness, feasibility
- **Verify constraint qualifications:** For necessity
- **Use geometric intuition:** Gradient orthogonality
- **Compare with known solutions:** Simple test cases

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

### 📈 **Real-World Applications**

#### **Machine Learning:**
- **SVM:** Dual formulation and support vector identification
- **Regularization:** L1, L2 penalties via constrained formulation
- **Neural networks:** Constrained training, fairness constraints

#### **Engineering:**
- **Optimal control:** Pontryagin maximum principle
- **Signal processing:** Filter design, beamforming
- **Structural optimization:** Weight minimization with stress constraints

#### **Economics and Finance:**
- **Portfolio optimization:** Risk-return tradeoffs
- **Mechanism design:** Incentive compatibility
- **Resource allocation:** Utility maximization

#### **Operations Research:**
- **Production planning:** Capacity constraints
- **Supply chain:** Inventory optimization
- **Transportation:** Network flow problems

---

💡 **Tip:** The KKT conditions are the **crown jewel** of optimization theory - they provide an exact characterization of optimality for constrained problems and are the foundation of most modern optimization algorithms!

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

This multiple-choice quiz tests your understanding of the Karush-Kuhn-Tucker (KKT) conditions, including practical examples such as SVM, the water-filling algorithm, quadratic programming and L1-penalized problems.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>⚖️ Quiz: KKT Conditions</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1 -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: Which components make up the KKT conditions?</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Only stationarity and complementary slackness</label>
                <label><input type="radio" name="q1" value="b"> B) Stationarity, complementary slackness, primal feasibility, dual feasibility</label>
                <label><input type="radio" name="q1" value="c"> C) Only primal and dual feasibility</label>
                <label><input type="radio" name="q1" value="d"> D) Only stationarity</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Stationarity, complementary slackness, primal feasibility, dual feasibility</strong><br>
                The KKT conditions have 4 components: (1) Stationarity, (2) Complementary slackness, (3) Primal feasibility, (4) Dual feasibility.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The stationarity condition in KKT has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\nabla f(x^*) = 0\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\nabla f(x^*) + \sum \lambda_i \nabla h_i(x^*) + \sum \nu_j \nabla l_j(x^*) = 0\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\lambda_i h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(h_i(x^*) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\nabla f(x^*) + \sum \lambda_i \nabla h_i(x^*) + \sum \nu_j \nabla l_j(x^*) = 0$$</strong><br>
                Stationarity: the gradient of the Lagrangian with respect to $$x$$ is 0, i.e. the gradient of the objective is balanced by a linear combination of the gradients of the constraints.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: The complementary slackness condition states that:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(\lambda_i h_i(x^*) = 0\) for all \(i\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\lambda_i = 0\) or \(h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q3" value="c"> C) If \(h_i(x^*) < 0\) then \(\lambda_i = 0\)</label>
                <label><input type="radio" name="q3" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                Complementary slackness can be stated in several equivalent ways: $$\lambda_i h_i(x^*) = 0$$, or $$\lambda_i = 0$$ or $$h_i(x^*) = 0$$, or inactive constraints have dual variable = 0.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The KKT conditions are sufficient for global optimality when:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) The problem is convex</label>
                <label><input type="radio" name="q4" value="b"> B) The problem is non-convex</label>
                <label><input type="radio" name="q4" value="c"> C) Always</label>
                <label><input type="radio" name="q4" value="d"> D) Never</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The problem is convex</strong><br>
                The KKT conditions are necessary (under a constraint qualification) for every problem, but sufficient for global optimality only when the problem is convex.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: A constraint \(h_i(x) \leq 0\) is called active at \(x^*\) when:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(h_i(x^*) < 0\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(\lambda_i > 0\)</label>
                <label><input type="radio" name="q5" value="d"> D) \(\lambda_i = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$h_i(x^*) = 0$$</strong><br>
                An active constraint is one that holds with equality at the optimal point.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: In quadratic programming \(\min \frac{1}{2}x^T Q x + c^T x\) s.t. \(Ax = b\), the stationarity condition is:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(Qx^* + c = 0\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(Qx^* + c + A^T \nu^* = 0\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(Ax^* = b\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\nu^* = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$Qx^* + c + A^T \nu^* = 0$$</strong><br>
                Stationarity: $$\nabla f(x^*) + A^T \nu^* = Qx^* + c + A^T \nu^* = 0$$.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: In the water-filling algorithm, the optimization problem has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(\max \sum \log(\alpha_i + x_i)\) s.t. \(\sum x_i = P, x_i \geq 0\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(\min \sum \log(\alpha_i + x_i)\) s.t. \(\sum x_i = P, x_i \geq 0\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(\max \sum x_i^2\) s.t. \(\sum x_i = P\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(\min \sum x_i^2\) s.t. \(\sum x_i = P\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max \sum \log(\alpha_i + x_i)$$ s.t. $$\sum x_i = P, x_i \geq 0$$</strong><br>
                Water-filling maximizes the sum of log capacities subject to a total power constraint and non-negativity.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The solution of the water-filling algorithm has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(x_i^* = \max(0, \mu - \alpha_i)\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(x_i^* = \max(0, \alpha_i - \mu)\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(x_i^* = \mu - \alpha_i\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(x_i^* = \alpha_i + \mu\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$x_i^* = \max(0, \mu - \alpha_i)$$</strong><br>
                Water-filling solution: allocate power $$\mu - \alpha_i$$ to channel $$i$$ if $$\mu > \alpha_i$$, otherwise allocate 0.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The SVM primal problem has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\min \frac{1}{2}\|w\|^2\) s.t. \(y_i(w^T x_i + b) \geq 1\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\max \frac{1}{2}\|w\|^2\) s.t. \(y_i(w^T x_i + b) \geq 1\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\min \sum \alpha_i\) s.t. \(\sum \alpha_i y_i = 0\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\max \sum \alpha_i\) s.t. \(\sum \alpha_i y_i = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\min \frac{1}{2}\|w\|^2$$ s.t. $$y_i(w^T x_i + b) \geq 1$$</strong><br>
                SVM primal: minimize $$\frac{1}{2}\|w\|^2$$, i.e. maximize the margin $$2/\|w\|$$, subject to classification constraints.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The SVM dual problem has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(\min \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(\max \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(\min \frac{1}{2}\|w\|^2 + C\sum \xi_i\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(\max \frac{1}{2}\|w\|^2\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\max \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j$$</strong><br>
                SVM dual maximizes linear term minus quadratic term subject to constraints $$\sum \alpha_i y_i = 0, \alpha_i \geq 0$$.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: Support vectors in SVM are the points with:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(\alpha_i = 0\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(\alpha_i > 0\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(y_i(w^T x_i + b) > 1\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(y_i(w^T x_i + b) < 1\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\alpha_i > 0$$</strong><br>
                Support vectors have dual variables $$\alpha_i > 0$$ and lie on the margin boundary: $$y_i(w^T x_i + b) = 1$$.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The Linear Independence Constraint Qualification (LICQ) requires:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) All constraints to be active</label>
                <label><input type="radio" name="q12" value="b"> B) The gradients of the active constraints to be linearly independent</label>
                <label><input type="radio" name="q12" value="c"> C) All constraints to be inactive</label>
                <label><input type="radio" name="q12" value="d"> D) The objective function to be differentiable</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The gradients of the active constraints to be linearly independent</strong><br>
                LICQ ensures that the gradients of the active constraints at the optimal point are linearly independent, which guarantees KKT necessity.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: In the L1-penalized problem \(\min f(x) + \lambda\|x\|_1\), the KKT condition for the component \(x_i\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(\frac{\partial f}{\partial x_i} + \lambda \text{sign}(x_i) = 0\) if \(x_i \neq 0\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(\frac{\partial f}{\partial x_i} + \lambda = 0\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(\frac{\partial f}{\partial x_i} = 0\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(x_i = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\frac{\partial f}{\partial x_i} + \lambda \text{sign}(x_i) = 0$$ if $$x_i \neq 0$$</strong><br>
                When $$x_i \neq 0$$, the subgradient of $$|x_i|$$ is $$\text{sign}(x_i)$$. When $$x_i = 0$$, the subdifferential is $$[-1,1]$$.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: In L1 regularization, the solution is unique when:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(f\) is strictly convex</label>
                <label><input type="radio" name="q14" value="b"> B) \(\lambda > 0\) is arbitrary</label>
                <label><input type="radio" name="q14" value="c"> C) The active set is uniquely determined</label>
                <label><input type="radio" name="q14" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f$$ is strictly convex</strong><br>
                Strict convexity of $$f$$ guarantees uniqueness of the solution, even though the L1 term is not strictly convex.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: The KKT system for an equality-constrained QP can be written in matrix form as:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(\begin{bmatrix} Q & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(\begin{bmatrix} Q & A \\ A^T & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(Qx = -c\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(Ax = b\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{bmatrix} Q & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}$$</strong><br>
                The KKT system combines stationarity $$Qx + c + A^T\nu = 0$$ and feasibility $$Ax = b$$.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: A constraint qualification is needed to:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Guarantee that the KKT conditions are sufficient</label>
                <label><input type="radio" name="q16" value="b"> B) Guarantee that the KKT conditions are necessary</label>
                <label><input type="radio" name="q16" value="c"> C) Guarantee that the objective is differentiable</label>
                <label><input type="radio" name="q16" value="d"> D) Guarantee convexity</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Guarantee that the KKT conditions are necessary</strong><br>
                A constraint qualification (LICQ, MFCQ, etc.) guarantees that the KKT conditions are necessary for local optimality.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: The second-order sufficient condition requires the Hessian of the Lagrangian to be:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Positive definite on the whole space</label>
                <label><input type="radio" name="q17" value="b"> B) Positive definite on the tangent space of the active constraints</label>
                <label><input type="radio" name="q17" value="c"> C) Negative definite</label>
                <label><input type="radio" name="q17" value="d"> D) Singular</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Positive definite on the tangent space of the active constraints</strong><br>
                The SOSC: the Hessian of the Lagrangian is positive definite on the tangent space, which guarantees a local minimum.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: The relation between KKT multipliers and penalty methods:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) The multiplier estimates of the penalty method converge to the KKT multipliers</label>
                <label><input type="radio" name="q18" value="b"> B) Penalty parameters are limits of KKT multipliers</label>
                <label><input type="radio" name="q18" value="c"> C) There is no relation</label>
                <label><input type="radio" name="q18" value="d"> D) They are always equal</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The multiplier estimates of the penalty method converge to the KKT multipliers</strong><br>
                As the penalty parameter $$\to \infty$$, the solution of the penalized problem converges and the multiplier estimates converge to the KKT multipliers.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: KKT multipliers provide information about:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) The sensitivity of the optimal value to changes in the constraints</label>
                <label><input type="radio" name="q19" value="b"> B) The convergence rate of the algorithm</label>
                <label><input type="radio" name="q19" value="c"> C) The condition number of the problem</label>
                <label><input type="radio" name="q19" value="d"> D) The number of iterations needed</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The sensitivity of the optimal value to changes in the constraints</strong><br>
                KKT multipliers are shadow prices: they tell how much the optimal value changes when the constraint bounds change.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: KKT conditions are applied in:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Machine learning (SVM, neural networks)</label>
                <label><input type="radio" name="q20" value="b"> B) Signal processing (water-filling, beamforming)</label>
                <label><input type="radio" name="q20" value="c"> C) Economics (utility maximization, portfolio optimization)</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above fields</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above fields</strong><br>
                The KKT conditions are a fundamental tool in constrained optimization with wide applications in ML, signal processing, economics and many other fields.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: The KKT conditions consist of:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Stationarity, primal feasibility, dual feasibility, complementary slackness</label>
                <label><input type="radio" name="q21" value="b"> B) Only stationarity</label>
                <label><input type="radio" name="q21" value="c"> C) Only feasibility</label>
                <label><input type="radio" name="q21" value="d"> D) Only complementary slackness</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Stationarity, primal feasibility, dual feasibility, complementary slackness</strong><br>
                KKT consists of 4 conditions: $$\nabla f + \sum \lambda_i \nabla g_i + \sum \nu_j \nabla h_j = 0$$, $$g_i(x) \leq 0$$, $$\lambda_i \geq 0$$, $$\lambda_i g_i(x) = 0$$.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The complementary slackness condition means:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$\lambda_i g_i(x) = 0$$ for all $$i$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$\lambda_i + g_i(x) = 0$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$\lambda_i = g_i(x)$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$\lambda_i \cdot g_i(x) = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\lambda_i g_i(x) = 0$$ for all $$i$$</strong><br>
                Complementary slackness: either $$\lambda_i = 0$$ or $$g_i(x) = 0$$ (active constraint).
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: Given the problem $$\min x^2$$ subject to $$x \geq 1$$. The KKT conditions at the solution $$x^* = 1$$:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$2x - \lambda = 0, \lambda \geq 0, \lambda(1-x) = 0$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$2x = 0$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$x = 1$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$\lambda = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$2x - \lambda = 0, \lambda \geq 0, \lambda(1-x) = 0$$</strong><br>
                Stationarity: $$2x - \lambda = 0$$. At $$x^* = 1$$: $$\lambda = 2$$, which satisfies complementary slackness.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: LICQ (Linear Independence Constraint Qualification) requires:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) The gradients of the active constraints to be linearly independent</label>
                <label><input type="radio" name="q24" value="b"> B) All constraints to be linear</label>
                <label><input type="radio" name="q24" value="c"> C) The objective function to be linear</label>
                <label><input type="radio" name="q24" value="d"> D) The Hessian matrix to be invertible</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The gradients of the active constraints to be linearly independent</strong><br>
                LICQ: the gradients $$\nabla g_i(x^*), \nabla h_j(x^*)$$ of the active constraints must be linearly independent.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: In a QP with KKT, the matrix of the system of equations has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$\begin{pmatrix} H & A^T \\ A & 0 \end{pmatrix}$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$\begin{pmatrix} H & 0 \\ 0 & A \end{pmatrix}$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$H + A^T A$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$H - A^T A$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{pmatrix} H & A^T \\ A & 0 \end{pmatrix}$$</strong><br>
                The KKT system for a QP has a block-matrix form with the Hessian $$H$$ and the constraint matrix $$A$$.
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
    q1: 'b', q2: 'b', q3: 'd', q4: 'a', q5: 'b',
    q6: 'b', q7: 'a', q8: 'a', q9: 'a', q10: 'b',
    q11: 'b', q12: 'b', q13: 'a', q14: 'a', q15: 'a',
    q16: 'b', q17: 'b', q18: 'a', q19: 'a', q20: 'd'
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
        message = '🌟 Excellent! You have mastered the KKT conditions and their applications!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand the optimality conditions and the practical examples well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review complementary slackness and constraint qualifications.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review the KKT conditions and stationarity.';
    } else {
        message = '📖 Study KKT theory again from the beginning!';
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

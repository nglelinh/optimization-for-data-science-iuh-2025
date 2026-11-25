---
layout: post
title: '11-09 Multiple-Choice Quiz - Duality in General Programs'
chapter: '11'
order: 10
owner: GitHub Copilot
lang: en
categories:
- chapter11
lesson_type: quiz
redirect_from:
  - /contents/en/chapter11/11_06_Quiz_General_Duality/
---

Before starting the Chapter 11 multiple-choice quiz, pause to separate the *always-true* laws of Lagrangian duality from the *conditional* ones. The single most common exam mistake is thinking that $$g(u, v)$$ is only concave when the primal is convex (false—$$g$$ is *always* concave!), or thinking convexity alone guarantees strong duality (false—you also need a constraint qualification like Slater's condition!). Use the four diagnostic pillars and rapid warm-up below to calibrate your intuition.

## Key ideas: Chapter 11 Mastery Checklist

- **Pillar 1 — Universal Laws (No Convexity Needed):** For *any* optimization problem, (i) $$L(x, u, v)$$ is affine in $$(u, v)$$, (ii) $$g(u, v) = \inf_x L(x, u, v)$$ is concave, (iii) the dual problem $$\max_{u \ge 0, v} g(u, v)$$ is convex, and (iv) weak duality $$g^\star \le f^\star$$ holds.
- **Pillar 2 — Strong Duality & Slater's Condition:** Strong duality ($$g^\star = f^\star$$) is guaranteed for convex problems admitting a strictly feasible point $$x$$ ($$h_i(x) < 0$$ for non-affine inequalities, $$h_k(x) \le 0$$ for affine inequalities, $$l_j(x) = 0$$).
- **Pillar 3 — Duality Gap & Certification:** For any feasible $$x$$ and $$(u, v)$$ with $$u \ge 0$$, $$f(x) - f^\star \le f(x) - g(u, v)$$. Zero duality gap proves both $$x$$ and $$(u, v)$$ are globally optimal.
- **Pillar 4 — Double Duality & Perturbation:** The dual of the dual recovers the primal when the problem is closed and convex; for nonconvex problems it yields the convex envelope (biconjugate), explaining why a strict duality gap $$f^\star - g^\star > 0$$ can persist.

### Worked example: Quick 3-Part Diagnostic on a Constrained Exponential Problem

Consider $$\min_{x \in \mathbb{R}} e^x$$ subject to $$x \ge 0$$ (i.e., $$-x \le 0$$).

1. **Compute the Lagrangian and dual function:**
   - $$L(x, u) = e^x - u x$$ for $$u \ge 0$$.
   - Minimize over $$x \in \mathbb{R}$$:
     - If $$u = 0$$: $$\inf_x e^x = 0$$ (approached as $$x \to -\infty$$).
     - If $$u > 0$$: set $$e^x - u = 0 \implies x = \ln u$$, giving $$g(u) = u - u \ln u$$.
   - Verify concavity of $$g(u) = u - u\ln u$$: $$g''(u) = -1/u < 0$$ on $$u > 0$$!
2. **Solve the dual problem $$\max_{u \ge 0} (u - u\ln u)$$:**
   - Set $$g'(u) = 1 - (\ln u + 1) = -\ln u = 0 \implies u^\star = 1$$.
   - Dual optimal value: $$g^\star = 1 - 1\ln(1) = 1$$.
3. **Verify Slater's condition and strong duality:**
   - Primal is convex and $$x = 1$$ satisfies $$-1 < 0$$ (Slater holds!).
   - Primal minimum is at $$x^\star = 0$$ with $$f^\star = e^0 = 1 = g^\star$$ (zero gap!).

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### ⚡ **General Duality**

#### **General optimization problem**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad l_j(x) = 0$$

where:
- $$f(x)$$: the objective function (not necessarily convex)
- $$h_i(x) \le 0$$: inequality constraints ($$i = 1,\ldots,m$$)
- $$l_j(x) = 0$$: equality constraints ($$j = 1,\ldots,r$$)

#### **Extending LP Duality**
- **LP Duality (Chapter 10):** Applies only to linear programs
- **General Duality (Chapter 11):** Applies to **any** optimization problem
- **Main tool:** The Lagrangian function instead of a linear combination

### 📏 **The Lagrangian Function**

#### **Definition**
$$L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x)$$

where:
- $$u \in \mathbb{R}^m, u \ge 0$$: dual variables for the inequality constraints
- $$v \in \mathbb{R}^r$$: dual variables for the equality constraints (no sign constraint)

#### **Basic properties**
For every feasible $$x$$ and every $$u \ge 0, v$$:
$$L(x,u,v) = f(x) + \sum_{i=1}^m u_i \underbrace{h_i(x)}_{\le 0} + \sum_{j=1}^r v_j \underbrace{l_j(x)}_{= 0} \le f(x)$$

**Meaning:** The Lagrangian provides a **lower bound** on $$f(x)$$ at every feasible point.

#### **Geometric interpretation**
- **Primal problem:** Find the minimum directly in the feasible region
- **Lagrangian:** "Penalty method" - adds a penalty for constraint violations
- **Dual variables:** "Prices" for violating the constraints

### 🎯 **The Lagrange Dual Function**

#### **Definition**
$$g(u,v) = \min_x L(x,u,v) = \min_x \left\{ f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x) \right\}$$

#### **Important properties**
1. **Lower bound:** $$g(u,v) \le f^*$$ for all $$u \ge 0, v$$ (weak duality)
2. **Concavity:** $$g(u,v)$$ is a **concave** function of $$(u,v)$$
3. **Independent of convexity:** $$g$$ is concave even when $$f$$ is not convex

#### **Proof of concavity**
$$g(u,v) = \min_x L(x,u,v) = -\max_x \{-L(x,u,v)\}$$

Since $$-L(x,u,v)$$ is **convex** in $$(u,v)$$ (linear), and the $$\max_x$$ of convex functions is convex, $$g(u,v)$$ is concave.

### 📊 **The Lagrange Dual Problem**

#### **Definition**
$$\max_{u,v} g(u,v) \quad \text{s.t.} \quad u \ge 0$$

**Goal:** Find the **best lower bound** on $$f^*$$

#### **Special properties**
1. **Always a convex problem:** Maximize a concave function over a convex set
2. **Independent of the primal:** The dual is always convex even when the primal is non-convex
3. **Computational advantage:** May be easier to solve than the primal

#### **Weak Duality**
**Always true:** $$g^* \le f^*$$ (dual optimal ≤ primal optimal)

**Duality gap:** $$f^* - g^* \ge 0$$

### 🔄 **Example: Quadratic Programming**

#### **Problem**
$$\min_x \frac{1}{2}x^T Q x + c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

#### **Case 1: $$Q \succ 0$$ (positive definite)**

**Lagrangian:**
$$L(x,u,v) = \frac{1}{2}x^T Q x + c^T x - u^T x + v^T(Ax - b)$$

**Minimizing over $$x$$:**
$$\nabla_x L = Qx + c - u + A^T v = 0$$
$$\Rightarrow x^* = Q^{-1}(u - c - A^T v)$$

**Dual function:**
$$g(u,v) = -\frac{1}{2}(c - u + A^T v)^T Q^{-1}(c - u + A^T v) - b^T v$$

#### **Case 2: $$Q \succeq 0$$ (positive semidefinite)**

**Dual function:**
$$g(u,v) = \begin{cases}
-\frac{1}{2}(c - u + A^T v)^T Q^+(c - u + A^T v) - b^T v & \text{if } c - u + A^T v \perp \text{null}(Q) \\
-\infty & \text{otherwise}
\end{cases}$$

where $$Q^+$$ is the Moore-Penrose pseudoinverse.

### 💪 **Strong Duality**

#### **Definition**
**Strong duality holds when:** $$f^* = g^*$$ (duality gap = 0)

#### **Slater's Condition**
**Sufficient condition for strong duality:**

If the primal problem is **convex** and there exists a **strictly feasible** $$x$$:
$$h_i(x) < 0 \quad \forall i, \quad l_j(x) = 0 \quad \forall j$$

**Note:** Strict inequality is not needed for affine constraints.

#### **Meaning of Strong Duality**
- **Perfect correspondence:** The primal and dual have the same optimal value
- **Computational:** We can solve the dual instead of the primal
- **Theoretical:** Enables the KKT conditions (Chapter 12)

### 🎯 **Example: Support Vector Machine (SVM)**

#### **Primal problem**
$$\min_{\beta,\beta_0,\xi} \frac{1}{2}\|\beta\|_2^2 + C\sum_{i=1}^n \xi_i$$
$$\text{s.t.} \quad \xi_i \ge 0, \quad y_i(x_i^T\beta + \beta_0) \ge 1 - \xi_i$$

#### **Lagrangian**
$$L(\beta,\beta_0,\xi,v,w) = \frac{1}{2}\|\beta\|_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i + \sum_{i=1}^n w_i(1 - \xi_i - y_i(x_i^T\beta + \beta_0))$$

#### **Dual problem** (after eliminating the primal variables)
$$\max_w -\frac{1}{2}w^T \tilde{X}\tilde{X}^T w + \mathbf{1}^T w$$
$$\text{s.t.} \quad 0 \le w \le C\mathbf{1}, \quad w^T y = 0$$

with $$\tilde{X} = \text{diag}(y)X$$

**Strong duality:** Slater's condition holds → $$f^* = g^*$$

### 📐 **Duality Gap**

#### **Definition**
Given a primal feasible $$x$$ and a dual feasible $$(u,v)$$:
$$\text{Duality gap} = f(x) - g(u,v)$$

#### **Properties**
1. **Upper bound on suboptimality:** $$f(x) - f^* \le f(x) - g(u,v)$$
2. **Stopping criterion:** If $$f(x) - g(u,v) \le \epsilon$$ then $$f(x) - f^* \le \epsilon$$
3. **Optimality test:** $$f(x) - g(u,v) = 0 \Leftrightarrow x, (u,v)$$ optimal

#### **Use in algorithms**
- **Primal-dual methods:** Simultaneously update the primal and dual variables
- **Convergence monitoring:** Track the duality gap instead of objective values
- **Early stopping:** Stop when the duality gap is small enough

### 🔄 **Comparing LP Duality and General Duality**

| **Aspect** | **LP Duality (Ch 10)** | **General Duality (Ch 11)** |
|------------|------------------------|------------------------------|
| **Scope** | Linear programs only | Any optimization problem |
| **Method** | Linear combination of constraints | Lagrangian function |
| **Dual convexity** | Always convex (LP) | Always convex (concave $$g$$) |
| **Strong duality** | If one feasible → strong duality | Slater's condition needed |
| **Applications** | LP, network flows, games | SVM, QP, general constrained |

### 🛠️ **Practical Techniques**

#### **Constructing the dual problem:**
1. **Write Lagrangian:** $$L(x,u,v) = f(x) + u^T h(x) + v^T l(x)$$
2. **Minimize over $$x$$:** $$g(u,v) = \min_x L(x,u,v)$$
3. **Solve the optimization:** $$\nabla_x L = 0$$ (if unconstrained)
4. **Substitute back:** Get $$g(u,v)$$ explicitly
5. **Maximize $$g$$:** Subject to $$u \ge 0$$

#### **Checking strong duality:**
1. **Verify convexity:** Primal problem convex?
2. **Check Slater's condition:** Strictly feasible point exists?
3. **Special cases:** LP, QP with $$Q \succ 0$$, etc.

#### **Computational strategies:**
- **Dual easier:** When the dual has fewer variables or a simpler structure
- **Primal-dual methods:** Update both simultaneously
- **Duality gap monitoring:** For convergence assessment

### 💡 **Illustrative Examples**

#### **Simple problem:**
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

### 🎯 **Connections to Other Chapters**

#### **From the previous chapter:**
- **Chapter 10:** LP duality as a special case
- **Chapter 09:** Proximal gradient for composite problems
- **Chapter 05:** QP as a canonical problem

#### **Importance of General Duality:**
- **Theoretical foundation:** For modern optimization theory
- **KKT conditions:** Optimality conditions (Chapter 12)
- **Algorithms:** Primal-dual methods, interior point
- **Machine learning:** SVM, neural networks, regularization

#### **Looking ahead:**
- **Chapter 12:** KKT conditions and complementary slackness
- **Advanced topics:** Robust optimization, semidefinite programming
- **Applications:** Deep learning, reinforcement learning

### 🌟 **Theoretical Significance**

#### **Duality as a universal principle:**
- **Every optimization problem** has a dual perspective
- **The dual is always convex** even when the primal is non-convex
- **Provides bounds** and **optimality conditions**
- **Enables algorithms** that are impossible with the primal alone

#### **Geometric interpretation:**
- **Primal:** Direct search in the feasible region
- **Dual:** Indirect approach qua "supporting hyperplanes"
- **Strong duality:** Perfect geometric correspondence

#### **Computational significance:**
- **Alternative solution path:** The dual can be easier than the primal
- **Parallel computation:** Primal-dual methods
- **Convergence monitoring:** The duality gap as a stopping criterion

### 💡 **Practical Tips**

#### **When to use duality:**
1. **Primal hard to solve:** Many variables, complex constraints
2. **Dual structure simpler:** Fewer dual variables
3. **Bounds needed:** Duality gap for convergence assessment
4. **Theoretical analysis:** Optimality conditions, sensitivity

#### **Common pitfalls:**
- **Forget constraint qualifications:** Slater's condition
- **Wrong sign conventions:** $$u \ge 0$$ for $$h(x) \le 0$$
- **Non-convex primal:** Strong duality is not guaranteed
- **Computational issues:** The dual may be numerically unstable

#### **Debugging strategies:**
- **Verify weak duality:** $$g^* \le f^*$$ always holds
- **Check Slater's condition:** For strong duality
- **Compare with known results:** LP, QP special cases
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

💡 **Tip:** General duality is a **paradigm shift** from "solving the problem directly" to "finding the best bound and exploiting structure". It is the foundation of all of modern optimization theory!

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

This multiple-choice quiz tests your understanding of duality for general programs, including the Lagrangian, the dual function, strong duality, the Slater condition and the KKT conditions.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🎯 Quiz: Duality in General Programs</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1: Lagrangian definition -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: Given the problem \(\min f(x)\) s.t. \(h_i(x) \leq 0, l_j(x) = 0\). The Lagrangian is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(L(x,u,v) = f(x) - \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(L(x,u,v) = f(x) + \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(L(x,u,v) = f(x) - \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)$$</strong><br>
                The Lagrangian combines the objective function with penalty terms for the constraints, with $$u_i \geq 0$$ for the inequality constraints.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: In the Lagrangian, the dual variables must satisfy:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(u \geq 0, v\) unconstrained</label>
                <label><input type="radio" name="q2" value="b"> B) \(u\) unconstrained, \(v \geq 0\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(u \geq 0, v \geq 0\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(u\) and \(v\) both unconstrained</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$u \geq 0, v$$ unconstrained</strong><br>
                The dual variables $$u_i$$ for inequality constraints must be non-negative; $$v_j$$ for equality constraints have no sign constraint.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: The Lagrange dual function \(g(u,v)\) is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(g(u,v) = \max_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(g(u,v) = \min_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(g(u,v) = L(x^*,u,v)\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(g(u,v) = \nabla_x L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$g(u,v) = \min_x L(x,u,v)$$</strong><br>
                The dual function is the infimum of the Lagrangian over the primal variables $$x$$.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The weak duality theorem states that:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) \(g(u,v) \geq f^*\) for all \(u \geq 0, v\)</label>
                <label><input type="radio" name="q4" value="b"> B) \(g(u,v) \leq f^*\) for all \(u \geq 0, v\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(g(u,v) = f^*\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(g(u,v) > f^*\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$g(u,v) \leq f^*$$ for all $$u \geq 0, v$$</strong><br>
                The dual function provides a lower bound on the primal optimal value: $$g^* \leq f^*$$.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The Lagrange dual problem is:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(\min_{u \geq 0, v} g(u,v)\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(\max_{u \geq 0, v} g(u,v)\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(\min_{u, v \geq 0} g(u,v)\)</label>
                <label><input type="radio" name="q5" value="d"> D) \(\max_{u, v} g(u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\max_{u \geq 0, v} g(u,v)$$</strong><br>
                The dual problem maximizes the dual function to find the best lower bound for the primal problem.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: Strong duality holds when:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(f^* > g^*\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(f^* = g^*\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(f^* < g^*\)</label>
                <label><input type="radio" name="q6" value="d"> D) Duality gap > 0</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$f^* = g^*$$</strong><br>
                Strong duality means there is no duality gap: the primal and dual optimal values are equal.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: The Slater condition requires:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) There exists \(x\) such that \(h_i(x) \leq 0, l_j(x) = 0\)</label>
                <label><input type="radio" name="q7" value="b"> B) There exists \(x\) such that \(h_i(x) < 0, l_j(x) = 0\) (strictly feasible)</label>
                <label><input type="radio" name="q7" value="c"> C) There exists \(x\) such that \(h_i(x) = 0, l_j(x) = 0\)</label>
                <label><input type="radio" name="q7" value="d"> D) All constraints are active</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) There exists $$x$$ such that $$h_i(x) < 0, l_j(x) = 0$$ (strictly feasible)</strong><br>
                The Slater condition requires a strictly feasible (interior) point in order to guarantee strong duality.
            </div>
        </div>

        <!-- Question 8: Duality gap -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The duality gap is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(g^* - f^*\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(f^* - g^*\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(|f^* - g^*|\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(f^* + g^*\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$f^* - g^*$$</strong><br>
                The duality gap is the difference between the primal and dual optimal values, always non-negative by weak duality.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The KKT stationarity condition is:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\nabla f(x^*) + \sum u_i^* \nabla h_i(x^*) + \sum v_j^* \nabla l_j(x^*) = 0\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\nabla f(x^*) = 0\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(u_i^* h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(h_i(x^*) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\nabla f(x^*) + \sum u_i^* \nabla h_i(x^*) + \sum v_j^* \nabla l_j(x^*) = 0$$</strong><br>
                Stationarity: the gradient of the Lagrangian with respect to $$x$$ is 0 at the optimal point.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The KKT complementary slackness condition is:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(u_i^* \geq 0\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(h_i(x^*) \leq 0\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(u_i^* h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(l_j(x^*) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) $$u_i^* h_i(x^*) = 0$$</strong><br>
                Complementary slackness: if a constraint is not active then its dual variable = 0; if a dual variable > 0 then its constraint is active.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: The KKT conditions are sufficient for optimality when:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) The problem is convex</label>
                <label><input type="radio" name="q11" value="b"> B) The problem is non-convex</label>
                <label><input type="radio" name="q11" value="c"> C) Always</label>
                <label><input type="radio" name="q11" value="d"> D) Never</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The problem is convex</strong><br>
                The KKT conditions are necessary for every problem (under a constraint qualification), but only sufficient when the problem is convex.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The dual function \(g(u,v)\) has the property of being:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Always concave</label>
                <label><input type="radio" name="q12" value="b"> B) Always convex</label>
                <label><input type="radio" name="q12" value="c"> C) Possibly neither concave nor convex</label>
                <label><input type="radio" name="q12" value="d"> D) Always linear</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Always concave</strong><br>
                The dual function is always concave because it is a pointwise minimum of linear functions of $$(u,v)$$.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: A constraint qualification is needed to:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Guarantee that the KKT conditions are necessary</label>
                <label><input type="radio" name="q13" value="b"> B) Guarantee that the dual function is concave</label>
                <label><input type="radio" name="q13" value="c"> C) Guarantee convexity</label>
                <label><input type="radio" name="q13" value="d"> D) Guarantee uniqueness</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Guarantee that the KKT conditions are necessary</strong><br>
                A constraint qualification (such as LICQ, MFCQ) guarantees that the KKT conditions are necessary conditions for local optimality.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: In SVM, the dual problem has the form of:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Quadratic programming with linear constraints</label>
                <label><input type="radio" name="q14" value="b"> B) Linear programming</label>
                <label><input type="radio" name="q14" value="c"> C) Nonlinear programming</label>
                <label><input type="radio" name="q14" value="d"> D) Integer programming</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Quadratic programming with linear constraints</strong><br>
                The SVM dual is a QP: maximize a quadratic objective subject to linear constraints and box constraints.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: At the optimal point, the Lagrangian has the saddle-point property:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(L(x^*,u,v) \leq L(x^*,u^*,v^*) \leq L(x,u^*,v^*)\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(L(x^*,u,v) \geq L(x^*,u^*,v^*) \geq L(x,u^*,v^*)\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(L(x^*,u^*,v^*) = 0\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(L(x,u,v)\) is constant</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$L(x^*,u,v) \leq L(x^*,u^*,v^*) \leq L(x,u^*,v^*)$$</strong><br>
                Saddle-point property: the Lagrangian is minimized over $$x$$ and maximized over $$(u,v)$$ at the optimal point.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: In convex optimization, if the Slater condition holds then:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Weak duality holds</label>
                <label><input type="radio" name="q16" value="b"> B) Strong duality holds</label>
                <label><input type="radio" name="q16" value="c"> C) KKT conditions sufficient</label>
                <label><input type="radio" name="q16" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                For a convex problem with the Slater condition: weak duality always holds, strong duality holds, and KKT is necessary and sufficient.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: If \(x^*\) is primal optimal and \((u^*,v^*)\) is dual optimal with strong duality, then:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(f(x^*) = g(u^*,v^*)\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(f(x^*) > g(u^*,v^*)\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(f(x^*) < g(u^*,v^*)\)</label>
                <label><input type="radio" name="q17" value="d"> D) It cannot be determined</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f(x^*) = g(u^*,v^*)$$</strong><br>
                Strong duality means that the primal and dual optimal values are equal.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: Lagrangian relaxation is used to:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Find an upper bound for a minimization problem</label>
                <label><input type="radio" name="q18" value="b"> B) Find a lower bound for a minimization problem</label>
                <label><input type="radio" name="q18" value="c"> C) Solve the original problem exactly</label>
                <label><input type="radio" name="q18" value="d"> D) Convert to a maximization problem</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Find a lower bound for a minimization problem</strong><br>
                Lagrangian relaxation "relaxes" the constraints and provides a lower bound through the dual function.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: Geometrically, a zero duality gap means:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) The feasible set is empty</label>
                <label><input type="radio" name="q19" value="b"> B) A supporting hyperplane perfectly separates the epigraph and the feasible set</label>
                <label><input type="radio" name="q19" value="c"> C) The problem is unbounded</label>
                <label><input type="radio" name="q19" value="d"> D) Constraints redundant</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) A supporting hyperplane perfectly separates the epigraph and the feasible set</strong><br>
                Strong duality corresponds to the existence of a supporting hyperplane separating the epigraph of the objective and the feasible region.
            </div>
        </div>

        <!-- Question 20: Applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: Lagrangian duality has applications in:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Machine learning (SVM, neural networks)</label>
                <label><input type="radio" name="q20" value="b"> B) Economics (utility maximization)</label>
                <label><input type="radio" name="q20" value="c"> C) Engineering (optimal control, signal processing)</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above fields</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above fields</strong><br>
                Lagrangian duality is a fundamental tool in optimization with wide applications in ML, economics, engineering and many other fields.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: The Lagrange dual function $$g(\lambda, \nu)$$ is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$\inf_x L(x, \lambda, \nu)$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$\sup_x L(x, \lambda, \nu)$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$\nabla_x L(x, \lambda, \nu)$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$L(x^*, \lambda, \nu)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\inf_x L(x, \lambda, \nu)$$</strong><br>
                Lagrange dual function: $$g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$$.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: Weak duality states that:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$g(\lambda, \nu) \leq p^*$$ for $$\lambda \geq 0$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$g(\lambda, \nu) \geq p^*$$ for $$\lambda \geq 0$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$g(\lambda, \nu) = p^*$$</label>
                <label><input type="radio" name="q22" value="d"> D) There is no relationship</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$g(\lambda, \nu) \leq p^*$$ for $$\lambda \geq 0$$</strong><br>
                Weak duality: the dual value is always a lower bound on the primal value.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: The duality gap is zero when:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Strong duality holds</label>
                <label><input type="radio" name="q23" value="b"> B) The problem is convex and satisfies the Slater condition</label>
                <label><input type="radio" name="q23" value="c"> C) The problem is a feasible LP</label>
                <label><input type="radio" name="q23" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                A zero duality gap is exactly strong duality; convexity + the Slater condition is a sufficient condition; a feasible LP always has strong duality. Note: convexity alone is not enough.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The Slater condition requires:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) There exists a feasible $$x$$ with $$g_i(x) < 0$$ (strict)</label>
                <label><input type="radio" name="q24" value="b"> B) There exists $$x$$ with $$g_i(x) \leq 0$$</label>
                <label><input type="radio" name="q24" value="c"> C) The objective function is convex</label>
                <label><input type="radio" name="q24" value="d"> D) The constraints are linear</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) There exists a feasible $$x$$ with $$g_i(x) < 0$$ (strict)</strong><br>
                Slater condition: there exists a strictly feasible point $$x$$ with $$g_i(x) < 0$$ for all $$i$$.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: The dual problem of $$\min f(x)$$ subject to $$h(x) \leq 0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$\max g(\lambda)$$ subject to $$\lambda \geq 0$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$\min g(\lambda)$$ subject to $$\lambda \geq 0$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$\max g(\lambda)$$ subject to $$\lambda \leq 0$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$\sup g(\lambda)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max g(\lambda)$$ subject to $$\lambda \geq 0$$</strong><br>
                Dual problem: $$\max_{\lambda \geq 0} g(\lambda)$$ with $$g(\lambda) = \inf_x L(x,\lambda)$$.
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
    q1: 'a', q2: 'a', q3: 'b', q4: 'b', q5: 'b',
    q6: 'b', q7: 'b', q8: 'b', q9: 'a', q10: 'c',
    q11: 'a', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'd', q17: 'a', q18: 'b', q19: 'b', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'd', q24: 'a', q25: 'a'};

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
        message = '🌟 Excellent! You have mastered Lagrangian duality theory!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand the KKT conditions and strong duality well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review the Slater condition and complementary slackness.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review the Lagrangian and the dual function.';
    } else {
        message = '📖 Study general duality theory again from the beginning!';
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

---
layout: post
title: '16-04 Multiple-Choice Quiz - Duality Revisited'
chapter: '16'
order: 5
owner: GitHub Copilot
lang: en
categories:
- chapter16
lesson_type: quiz
---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### ⚡ **Duality Revisited**

#### **Lagrangian formulation of the primal-dual pair**
**The primal problem:**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad l_j(x) = 0$$

**Lagrangian:**
$$L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x)$$

#### **Primal-dual reformulation**
**Primal (reformulated):**
$$\min_x \max_{u \ge 0, v} L(x,u,v)$$

**Dual (reformulated):**
$$\max_{u \ge 0, v} \min_x L(x,u,v)$$

#### **Indicator function interpretation**
- **Primal:** $$\max_{u,v}$$ acts as an indicator function for constraint violations
- **Dual:** $$\min_x$$ provides domain relaxation
- **Equivalence:** Reformulated problems equivalent to original under feasibility

### 🔄 **Weak and Strong Duality (Refined)**

#### **Weak Duality Theorem**
**Always true:** $$p \ge d$$ (primal optimal ≥ dual optimal)

**Proof:** From minimax inequality
$$\min_x \max_{u \ge 0, v} L(x,u,v) \ge \max_{u \ge 0, v} \min_x L(x,u,v)$$

#### **Strong Duality (Refined Slater's Condition)**
**Condition:** For a domain $$D$$, assume $$f, h_1,\ldots,h_p$$ are convex and $$h_{p+1},\ldots,h_m, l_1,\ldots,l_r$$ are affine.

**If exists $$\hat{x} \in \text{relint}(D)$$ such that:**
- $$h_i(\hat{x}) < 0, \quad i = 1,\ldots,p$$ (strict inequality for non-affine)
- $$h_i(\hat{x}) \le 0, \quad i = p+1,\ldots,m$$ (weak inequality for affine)
- $$l_j(\hat{x}) = 0, \quad j = 1,\ldots,r$$ (equality constraints)

**Then:** $$p = d$$ (strong duality holds)

### 📊 **Duality Examples Revisited**

#### **1. Linear Programming Duality**

**Primal (Standard Form):**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

**Lagrangian approach:**
$$L(x,s,y) = c^T x - s^T x + (b - Ax)^T y$$

**Stationarity condition:** $$\nabla_x L = c - s - A^T y = 0$$
$$\Rightarrow c = A^T y + s$$

**Dual:**
$$\max b^T y \quad \text{s.t.} \quad A^T y + s = c, \quad s \ge 0$$

#### **2. Quadratic Programming Duality**

**Primal:**
$$\min \frac{1}{2}x^T Q x + c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

with $$Q$$ symmetric positive semidefinite

**Lagrangian:**
$$L(x,s,y) = \frac{1}{2}x^T Q x + c^T x - s^T x + (b - Ax)^T y$$

**Stationarity:** $$Qx + c - s - A^T y = 0$$
$$\Rightarrow Qx = A^T y + s - c$$

**Dual:**
$$\max b^T y - \frac{1}{2}x^T Q x \quad \text{s.t.} \quad Qx = A^T y + s - c, \quad s \ge 0$$

**Key insight:** The dual of a QP is also a QP!

#### **3. Barrier Method Duality**

**LP Barrier Primal:**
$$\min c^T x - \tau \sum_{i=1}^n \log(x_i) \quad \text{s.t.} \quad Ax = b$$

**Lagrangian:**
$$L(x,y) = c^T x - \tau \sum_{i=1}^n \log(x_i) + (b - Ax)^T y$$

**Optimal $$x$$:** $$x_i = \frac{\tau}{s_i}$$ with $$s = c - A^T y$$

**LP Barrier Dual:**
$$\max b^T y + \tau \sum_{i=1}^n \log(s_i) \quad \text{s.t.} \quad A^T y + s = c$$ (ignoring the constant $$n\tau(1 - \log\tau)$$)

**Beautiful result:** The barrier dual = the dual of the barrier problem!

### 🎯 **Optimality Conditions Comparison**

#### **Original Problem KKT**
$$\begin{align}
l_j(x^*) &= 0 \quad \forall j \\
u_i^*, -h_i(x^*) &\ge 0 \quad \forall i \\
u_i^* h_i(x^*) &= 0 \quad \forall i \\
\nabla f(x^*) + \sum u_i^* \nabla h_i(x^*) + \sum v_j^* \nabla l_j(x^*) &= 0
\end{align}$$

#### **Barrier Problem KKT (Perturbed)**
$$\begin{align}
l_j(x^*(t)) &= 0 \quad \forall j \\
u_i(t), -h_i(x^*(t)) &> 0 \quad \forall i \\
u_i(t) h_i(x^*(t)) &= -\tau \quad \forall i \\
\nabla f(x^*(t)) + \sum u_i(t) \nabla h_i(x^*(t)) + \sum \hat{v}_j^* \nabla l_j(x^*(t)) &= 0
\end{align}$$

with $$\tau = \frac{1}{t}$$, $$u_i(t) = -\frac{1}{t h_i(x^*(t))}$$, $$\hat{v} = \frac{1}{t}v$$

#### **Key differences:**
- **Complementary slackness:** $$= 0$$ vs $$= -\tau$$
- **Feasibility:** $$\ge 0$$ vs $$> 0$$ (strict)
- **Interpretation:** Exact vs perturbed KKT conditions

### 📈 **Linear Programming Special Case**

#### **Primal-Dual Optimality Conditions**
$$\begin{align}
A^T y^* + s^* &= c \\
Ax^* &= b \\
X S \mathbf{1} &= 0 \\
x^*, s^* &\ge 0
\end{align}$$

with $$X = \text{diag}(x^*)$$, $$S = \text{diag}(s^*)$$

#### **Barrier Problem Conditions**
$$\begin{align}
A^T y^* + s^* &= c \\
Ax^* &= b \\
X S \mathbf{1} &= \tau \mathbf{1} \\
x^*, s^* &> 0
\end{align}$$

#### **Algorithm implications:**
- **Simplex (primal):** Maintains conditions 2, 3 and $$x \ge 0$$; gradually satisfies 1 with $$s \ge 0$$ (dual feasibility)
- **Interior Point:** Maintain condition 4; gradually satisfy 1,2,3
- **Central path:** $$XS\mathbf{1} = \tau\mathbf{1}$$ defines path to optimality

### 🔗 **Fenchel Duality**

#### **Composite problem form**
**Primal:** $$\min_x f(x) + g(Ax)$$

**Reformulated:** $$\min_{x,z} f(x) + g(z) \quad \text{s.t.} \quad Ax = z$$

#### **Conjugate function approach**
**Lagrangian:**
$$L(x,z,v) = f(x) + g(z) + v^T(z - Ax)$$

**Dual function:**
$$\begin{align}
g(v) &= \min_{x,z} L(x,z,v) \\
&= \min_x [f(x) - (A^T v)^T x] + \min_z [g(z) + v^T z] \\
&= -f^*(A^T v) - g^*(-v)
\end{align}$$

#### **Fenchel Dual**
$$\max_v -f^*(A^T v) - g^*(-v)$$

#### **Beautiful property**
**Symmetry:** The dual of the dual = the primal (if $$f,g$$ are convex and closed)

### 🎯 **Conic Programming Applications**

#### **Standard Conic Program**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \in K$$

#### **Fenchel reformulation**
- $$f(x) = c^T x + I_K(x)$$
- $$g(z) = I_{\{b\}}(z)$$
- $$\min f(x) + g(Ax)$$

#### **Conic Dual**
$$\max b^T y \quad \text{s.t.} \quad A^T y + s = c, \quad s \in K^*$$

**Key insight:** Dual cone $$K^*$$ appears naturally!

#### **Strong duality conditions:**
- **Primal strictly feasible** OR **dual strictly feasible** (and a finite optimal value) ⟹ strong duality
- **Both strictly feasible** ⟹ strong duality + optimal solutions exist

### 📊 **Semidefinite Programming (SDP)**

#### **Primal SDP**
$$\min \text{tr}(CX) \quad \text{s.t.} \quad \text{tr}(A_i X) = b_i, \quad X \succeq 0$$

#### **Dual SDP**
$$\max b^T y \quad \text{s.t.} \quad \sum y_i A_i + S = C, \quad S \succeq 0$$

#### **Self-dual cone property**
$$(\mathbb{S}_+^n)^* = \mathbb{S}_+^n$$

**Interpretation:** Positive semidefinite cone is self-dual

#### **SDP Barrier Problems**

**Primal Barrier:**
$$\min \text{tr}(CX) - \tau \log(\det(X)) \quad \text{s.t.} \quad \text{tr}(A_i X) = b_i$$

**Dual Barrier:**
$$\max b^T y + \tau \log(\det(S)) \quad \text{s.t.} \quad \sum y_i A_i + S = C$$

**Note:** Unlike LP, SDP doesn't always have strong duality!

### 🛠️ **Practical Implications**

#### **Algorithm design insights:**
1. **Primal-dual methods:** Update both primal and dual variables
2. **Barrier methods:** Perturbed KKT conditions guide algorithms
3. **Self-duality:** Exploit symmetric structure (SDP)
4. **Central path:** Smooth path from interior to boundary

#### **Computational advantages:**
- **Dual easier:** Sometimes dual has better structure
- **Bounds:** Dual provides lower bounds for primal
- **Warm starts:** Use dual information for initialization
- **Stopping criteria:** Duality gap for convergence

### 🔄 **Connections Between Formulations**

#### **Lagrangian ↔ Fenchel**
- **Lagrangian:** General constrained problems
- **Fenchel:** Composite function problems
- **Connection:** Both use conjugate functions
- **Advantage:** Fenchel more natural for some problems

#### **Barrier ↔ Original**
- **Original KKT:** Exact optimality conditions
- **Barrier KKT:** Perturbed optimality conditions
- **Connection:** $$\tau \to 0$$ recovers original
- **Advantage:** Barrier enables interior point methods

#### **Primal ↔ Dual**
- **Primal:** Direct problem formulation
- **Dual:** Alternative perspective via bounds
- **Connection:** Strong duality bridges them
- **Advantage:** Choose easier formulation

### 💡 **Key Theoretical Insights**

#### **1. Duality universality**
**Every optimization problem** has dual perspective:
- **Lagrangian dual:** For constrained problems
- **Fenchel dual:** For composite problems
- **Conic dual:** For conic programs
- **Barrier dual:** For interior point methods

#### **2. Geometric interpretation**
- **Primal:** Direct search in the feasible region
- **Dual:** Supporting hyperplane approach
- **Central path:** Smooth trajectory through interior
- **Strong duality:** Perfect geometric correspondence

#### **3. Algorithmic implications**
- **Simplex:** Vertex-hopping on boundary
- **Interior point:** Path-following through interior
- **Primal-dual:** Simultaneous primal-dual updates
- **Barrier methods:** Perturbed optimality conditions

### 🎯 **Connections to Other Chapters**

#### **From previous chapters:**
- **Chapter 10:** LP duality foundation
- **Chapter 11:** General Lagrangian duality
- **Chapter 12:** KKT conditions
- **Chapter 15:** Barrier methods and the central path

#### **Advanced connections:**
- **Conjugate functions:** Fenchel duality framework
- **Conic programming:** Generalization to cones
- **Self-duality:** Special structure exploitation
- **Perturbed KKT:** Bridge between exact and approximate

#### **Future applications:**
- **Primal-dual algorithms:** Simultaneous updates
- **Interior point methods:** Polynomial-time algorithms
- **Semidefinite programming:** Matrix optimization
- **Robust optimization:** Worst-case analysis

### 🌟 **Theoretical Significance**

#### **Duality as universal principle:**
- **Every problem has dual:** Alternative formulation always exists
- **Geometric correspondence:** Primal-dual relationship
- **Algorithmic flexibility:** Choose best formulation
- **Theoretical elegance:** Unified framework

#### **Practical significance:**
- **Algorithm design:** Primal-dual methods
- **Computational efficiency:** Exploit structure
- **Sensitivity analysis:** Dual variables as shadow prices
- **Convergence analysis:** Duality gap monitoring

#### **Mathematical beauty:**
- **Symmetry:** The dual of the dual = the primal
- **Self-duality:** Some cones are self-dual
- **Conjugate functions:** Elegant mathematical framework
- **Central path:** Smooth geometric trajectory

### 💡 **Practical Tips**

#### **When to use different duality formulations:**
1. **Lagrangian:** General constrained problems
2. **Fenchel:** Composite functions, regularization
3. **Conic:** Problems with cone constraints
4. **Barrier:** Interior point algorithms

#### **Algorithm selection:**
- **Primal easier:** Direct primal methods
- **Dual easier:** Dual methods or primal-dual
- **Both complex:** Barrier methods with the central path
- **Large-scale:** Interior point methods

#### **Implementation considerations:**
- **Strong duality:** Check Slater's condition
- **Numerical stability:** Monitor condition numbers
- **Convergence:** Use duality gap
- **Warm starts:** Exploit dual information

### 🔬 **Advanced Topics**

#### **Robust duality:**
- **Uncertain problems:** Worst-case duality
- **Distributionally robust:** Ambiguous distributions
- **Chance constraints:** Probabilistic duality

#### **Algorithmic developments:**
- **Primal-dual interior point:** Mehrotra's algorithm
- **Homogeneous methods:** Handle infeasibility
- **Higher-order methods:** Beyond Newton steps
- **Distributed algorithms:** Parallel computation

#### **Modern applications:**
- **Machine learning:** SVM, regularization, neural networks
- **Finance:** Portfolio optimization, risk management
- **Engineering:** Control, signal processing, design
- **Operations research:** Logistics, scheduling, planning

### 📈 **Real-World Applications**

#### **Linear and Conic Programming:**
- **Portfolio optimization:** Mean-variance models
- **Network flows:** Transportation, communication
- **Production planning:** Resource allocation
- **Facility location:** Optimal placement

#### **Semidefinite Programming:**
- **Control theory:** LMI-based design
- **Combinatorial optimization:** SDP relaxations
- **Machine learning:** Kernel methods, matrix completion
- **Signal processing:** Beamforming, filter design

#### **Interior Point Methods:**
- **Large-scale LP:** Commercial solvers (CPLEX, Gurobi)
- **Quadratic programming:** Portfolio optimization
- **Nonlinear programming:** General constrained problems
- **Convex optimization:** Modern optimization software

### 🔮 **Future Directions**

#### **Theoretical developments:**
- **Non-convex duality:** Extensions beyond convexity
- **Stochastic duality:** Random optimization problems
- **Dynamic duality:** Time-varying problems
- **Quantum duality:** Quantum optimization

#### **Algorithmic innovations:**
- **Adaptive methods:** Problem-specific algorithms
- **Parallel algorithms:** Distributed computation
- **Online methods:** Streaming optimization
- **Approximation algorithms:** Near-optimal solutions

#### **Application domains:**
- **Deep learning:** Neural network optimization
- **Autonomous systems:** Real-time optimization
- **Smart grids:** Energy optimization
- **Bioinformatics:** Computational biology

### 💎 **Key Insights**

#### **Duality transformations:**
1. **Lagrangian:** Constraint incorporation via multipliers
2. **Fenchel:** Conjugate function perspective
3. **Barrier:** Interior point approximation
4. **Conic:** Cone-based generalization

#### **Algorithmic implications:**
- **Primal methods:** Direct feasible region search
- **Dual methods:** Bound-based approaches
- **Primal-dual:** Simultaneous optimization
- **Interior point:** Smooth path following

#### **Theoretical elegance:**
- **Weak duality:** Universal lower bounds
- **Strong duality:** Perfect correspondence
- **Self-duality:** Symmetric structures
- **Central path:** Geometric optimization trajectory

### 🌟 **Legacy of Chapter 16:**

- **Unified duality theory:** Multiple perspectives on same problems
- **Algorithmic flexibility:** Choose best formulation approach
- **Theoretical completeness:** Comprehensive duality framework
- **Practical impact:** Foundation for modern optimization software
- **Educational value:** Deep understanding of optimization structure

### 🎯 **Takeaway messages:**

1. **Duality is universal:** Every problem has dual perspective
2. **Multiple formulations:** Lagrangian, Fenchel, conic, barrier
3. **Algorithmic choice:** Select best approach for problem structure
4. **Geometric insight:** Primal-dual correspondence
5. **Practical power:** Enables efficient algorithms and software

### 💫 **Philosophical impact:**

Chapter 16 **unifies duality theory**:
- **From specific to general:** LP duality → universal duality
- **From single to multiple:** One formulation → many perspectives
- **From theoretical to practical:** Mathematical elegance → algorithmic power
- **From simple to sophisticated:** Basic concepts → advanced applications
- **From academic to industrial:** Research ideas → commercial software

### 🔮 **Synthesis:**

Duality revisited shows that **optimization has multiple faces**:
- **Primal face:** Direct problem solving
- **Dual face:** Bound-based approaches
- **Barrier face:** Interior approximation
- **Conjugate face:** Function transformation
- **Conic face:** Geometric generalization

Each face reveals different aspects of the same underlying mathematical structure, enabling **flexible algorithm design** and **deep theoretical understanding**. This multiplicity of perspectives is what makes modern optimization both **theoretically elegant** and **practically powerful**.

### 💡 **Final insight:**

Chapter 16 demonstrates that **duality is not just a mathematical curiosity** - it is a **fundamental organizing principle** of optimization theory. From simple LP duality to sophisticated Fenchel duality, from exact KKT conditions to perturbed barrier conditions, from primal algorithms to primal-dual methods - **duality provides a unified framework** that connects theory with practice, algorithms with applications, mathematics with engineering.

**Duality = Multiple perspectives on same optimization reality!**

---

💡 **Final message:** Duality Revisited does not just review previous concepts - it **synthesizes multiple duality perspectives** into a unified framework, showing how Lagrangian, Fenchel, conic, and barrier dualities are all **different faces of the same fundamental principle**!

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

This multiple-choice quiz tests your understanding of Duality Revisited, including Lagrangian duality theory, optimality conditions, Fenchel duality and advanced duality concepts.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: Duality Revisited & Advanced Theory</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1: Lagrangian definition -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: The Lagrangian for a problem with constraints \(h_i(x) \leq 0\) and \(l_j(x) = 0\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(L(x,u,v) = f(x) - \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(L(x,u,v) = f(x) + \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(L(x,u,v) = f(x) - \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)$$</strong><br>
                Standard-form Lagrangian with dual variables $$u_i \geq 0$$ for the inequality constraints and free $$v_j$$ for the equality constraints.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The primal problem can be rewritten as:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\min_x \max_{u \geq 0, v} L(x,u,v)\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\max_x \min_{u \geq 0, v} L(x,u,v)\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\min_x \min_{u \geq 0, v} L(x,u,v)\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\max_x \max_{u \geq 0, v} L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\min_x \max_{u \geq 0, v} L(x,u,v)$$</strong><br>
                Primal problem: minimize over $$x$$, maximizing the Lagrangian over the dual variables to enforce the constraints.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: The corresponding dual problem is:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(\max_{u \geq 0, v} \min_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\min_{u \geq 0, v} \max_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(\max_{u \geq 0, v} \max_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(\min_{u \geq 0, v} \min_x L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max_{u \geq 0, v} \min_x L(x,u,v)$$</strong><br>
                Dual problem: maximize over dual variables, minimize Lagrangian over primal variables.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The dual function \(g(u,v)\) is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) \(g(u,v) = \inf_x L(x,u,v)\)</label>
                <label><input type="radio" name="q4" value="b"> B) \(g(u,v) = \sup_x L(x,u,v)\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(g(u,v) = L(x^*,u,v)\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(g(u,v) = \nabla_x L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$g(u,v) = \inf_x L(x,u,v)$$</strong><br>
                The dual function is the infimum of the Lagrangian over the primal variables, always concave in the dual variables.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: Strong duality holds when:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(p^* = d^*\) (primal optimal = dual optimal)</label>
                <label><input type="radio" name="q5" value="b"> B) \(p^* > d^*\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(p^* < d^*\)</label>
                <label><input type="radio" name="q5" value="d"> D) Duality gap = ∞</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$p^* = d^*$$ (primal optimal = dual optimal)</strong><br>
                Strong duality: there is no duality gap; the primal and dual optimal values are equal.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: The KKT stationarity condition is:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(\nabla_x L(x^*,u^*,v^*) = 0\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(h_i(x^*) \leq 0\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(u_i^* \geq 0\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(u_i^* h_i(x^*) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\nabla_x L(x^*,u^*,v^*) = 0$$</strong><br>
                Stationarity: the gradient of the Lagrangian with respect to the primal variables is 0 at the optimal point.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: The complementary slackness condition is:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(u_i^* h_i(x^*) = 0\) for all \(i\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(u_i^* + h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(u_i^* h_i(x^*) \geq 0\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(u_i^* = h_i(x^*)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$u_i^* h_i(x^*) = 0$$ for all $$i$$</strong><br>
                Complementary slackness: the dual variable is 0 if the constraint is not active, or the constraint is active if the dual variable > 0.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The Fenchel conjugate of a function \(f\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(f^*(y) = \sup_x (y^T x - f(x))\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(f^*(y) = \inf_x (y^T x - f(x))\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(f^*(y) = \sup_x (y^T x + f(x))\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(f^*(y) = f(y)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f^*(y) = \sup_x (y^T x - f(x))$$</strong><br>
                Fenchel conjugate (Legendre transform): the supremum of a linear function minus the original function.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: Fenchel duality for the problem \(\min_x f(x) + g(Ax)\) has the dual:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\max_v -f^*(A^T v) - g^*(-v)\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\min_v f^*(A^T v) + g^*(v)\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\max_v f^*(A^T v) - g^*(v)\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\min_v -f^*(A^T v) + g^*(-v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max_v -f^*(A^T v) - g^*(-v)$$</strong><br>
                The Fenchel dual uses the conjugate functions of both $$f$$ and $$g$$ with appropriate transformations.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The biconjugate \(f^{**}\) of a convex function \(f\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(f^{**} = f\) (if \(f\) is convex and lower semicontinuous)</label>
                <label><input type="radio" name="q10" value="b"> B) \(f^{**} = -f\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(f^{**} = f^2\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(f^{**} = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f^{**} = f$$ (if $$f$$ is convex and lower semicontinuous)</strong><br>
                Fenchel-Moreau theorem: the biconjugate of a convex lower semicontinuous function is the function itself.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: \((x^*, u^*, v^*)\) is a saddle point of the Lagrangian if:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(L(x^*, u, v) \leq L(x^*, u^*, v^*) \leq L(x, u^*, v^*)\) for all feasible \((x,u,v)\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(L(x^*, u^*, v^*) = 0\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(\nabla L(x^*, u^*, v^*) = 0\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(L(x, u, v) = L(x^*, u^*, v^*)\) for all \((x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$L(x^*, u, v) \leq L(x^*, u^*, v^*) \leq L(x, u^*, v^*)$$ for all feasible $$(x,u,v)$$</strong><br>
                Saddle point: a minimum in the primal variables, a maximum in the dual variables.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: For a convex problem, the Slater condition guarantees:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Strong duality holds</label>
                <label><input type="radio" name="q12" value="b"> B) Weak duality holds</label>
                <label><input type="radio" name="q12" value="c"> C) No duality gap</label>
                <label><input type="radio" name="q12" value="d"> D) Both A and C</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) Both A and C</strong><br>
                The Slater condition (strict feasibility) guarantees strong duality, i.e. no duality gap.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The dual of the LP \(\min c^T x\) s.t. \(Ax = b, x \geq 0\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(\max b^T y\) s.t. \(A^T y \leq c\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(\min b^T y\) s.t. \(A^T y \geq c\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(\max c^T y\) s.t. \(A^T y = b\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(\min A^T y\) s.t. \(b^T y \leq c\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max b^T y$$ s.t. $$A^T y \leq c$$</strong><br>
                Standard LP dual: maximize with free dual variables $$y$$, constraint $$A^T y \leq c$$.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: The dual of the QP \(\min \frac{1}{2}x^T Q x + c^T x\) s.t. \(Ax \leq b\) with \(Q \succ 0\):</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(\max -\frac{1}{2}(A^T u + c)^T Q^{-1} (A^T u + c) - b^T u\) s.t. \(u \geq 0\)</label>
                <label><input type="radio" name="q14" value="b"> B) \(\min \frac{1}{2}u^T Q u - b^T u\) s.t. \(u \geq 0\)</label>
                <label><input type="radio" name="q14" value="c"> C) \(\max b^T u\) s.t. \(A^T u = c\)</label>
                <label><input type="radio" name="q14" value="d"> D) \(\min c^T u + b^T u\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max -\frac{1}{2}(A^T u + c)^T Q^{-1} (A^T u + c) - b^T u$$ s.t. $$u \geq 0$$</strong><br>
                The QP dual is derived from the Lagrangian by eliminating the primal variables using the stationarity condition.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: The conjugate of \(f(x) = \frac{1}{2}x^T Q x\) with \(Q \succ 0\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(f^*(y) = \frac{1}{2}y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(f^*(y) = \frac{1}{2}y^T Q y\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(f^*(y) = y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(f^*(y) = -\frac{1}{2}y^T Q^{-1} y\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f^*(y) = \frac{1}{2}y^T Q^{-1} y$$</strong><br>
                Conjugate of a quadratic form: replace $$Q$$ with $$Q^{-1}$$, keeping the coefficient $$\frac{1}{2}$$.
            </div>
        </div>

        <!-- Question 16: Moreau envelope -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: The Moreau envelope of a function \(f\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(M_\lambda f(x) = \inf_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(M_\lambda f(x) = f(x) + \lambda\|x\|^2\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(M_\lambda f(x) = \lambda f(x)\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(M_\lambda f(x) = f(\lambda x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$M_\lambda f(x) = \inf_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)$$</strong><br>
                Moreau envelope: a smooth approximation of the function obtained by adding a quadratic regularization.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: How is the proximal operator related to the Moreau envelope?</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(\text{prox}_{\lambda f}(x) = \arg\min_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(\text{prox}_{\lambda f}(x) = \nabla M_\lambda f(x)\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(\text{prox}_{\lambda f}(x) = M_\lambda f(x)\)</label>
                <label><input type="radio" name="q17" value="d"> D) \(\text{prox}_{\lambda f}(x) = x - \lambda \nabla f(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\text{prox}_{\lambda f}(x) = \arg\min_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)$$</strong><br>
                The proximal operator is the argmin of the expression in the definition of the Moreau envelope.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: In SVM, the dual problem has the advantages:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) The kernel trick can be applied</label>
                <label><input type="radio" name="q18" value="b"> B) The number of variables depends on the number of data points</label>
                <label><input type="radio" name="q18" value="c"> C) Quadratic programming with box constraints</label>
                <label><input type="radio" name="q18" value="d"> D) All of the above advantages</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above advantages</strong><br>
                The SVM dual allows the kernel trick, has a simpler structure, and is efficient for high-dimensional features.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: The weak duality theorem states that:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(d^* \leq p^*\) always holds</label>
                <label><input type="radio" name="q19" value="b"> B) \(d^* \geq p^*\) always holds</label>
                <label><input type="radio" name="q19" value="c"> C) \(d^* = p^*\) always holds</label>
                <label><input type="radio" name="q19" value="d"> D) There is no relation between \(d^*\) and \(p^*\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$d^* \leq p^*$$ always holds</strong><br>
                Weak duality: the dual optimum is always a lower bound on the primal optimum, independent of convexity.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: Duality theory is applied in:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Sensitivity analysis</label>
                <label><input type="radio" name="q20" value="b"> B) Algorithm design (dual methods)</label>
                <label><input type="radio" name="q20" value="c"> C) Theoretical analysis and bounds</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above applications</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above applications</strong><br>
                Duality theory has wide applications: sensitivity analysis, dual algorithms, theoretical bounds, economic interpretation.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: In duality revisited, strong duality holds when:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Duality gap = 0</label>
                <label><input type="radio" name="q21" value="b"> B) Primal infeasible</label>
                <label><input type="radio" name="q21" value="c"> C) Dual infeasible</label>
                <label><input type="radio" name="q21" value="d"> D) Both primal and dual are unbounded</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Duality gap = 0</strong><br>
                Strong duality: $$p^* = d^*$$ (the duality gap is 0).
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The Fenchel conjugate of $$f(x) = \frac{1}{2}x^2$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$f^*(y) = \frac{1}{2}y^2$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$f^*(y) = y^2$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$f^*(y) = \frac{1}{4}y^2$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$f^*(y) = 2y^2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f^*(y) = \frac{1}{2}y^2$$</strong><br>
                The Fenchel conjugate of $$\frac{1}{2}x^2$$ is $$\frac{1}{2}y^2$$.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: The bidual theorem states that:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$f^{**} = f$$ if $$f$$ is convex and closed</label>
                <label><input type="radio" name="q23" value="b"> B) $$f^{**} = -f$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$f^{**} = f^2$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$f^{**}$$ does not exist</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f^{**} = f$$ if $$f$$ is convex and closed</strong><br>
                For a closed convex function, the conjugate of the conjugate returns the original function.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The Moreau decomposition states that:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$x = \text{prox}_f(x) + \text{prox}_{f^*}(x)$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$x = \text{prox}_f(x) - \text{prox}_{f^*}(x)$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$x = \text{prox}_f(x) \cdot \text{prox}_{f^*}(x)$$</label>
                <label><input type="radio" name="q24" value="d"> D) There is no formula</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$x = \text{prox}_f(x) + \text{prox}_{f^*}(x)$$</strong><br>
                Moreau decomposition: every point can be decomposed as the sum of two proximal mappings.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: The Legendre transform is related to:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Fenchel conjugate</label>
                <label><input type="radio" name="q25" value="b"> B) Gradient</label>
                <label><input type="radio" name="q25" value="c"> C) Hessian</label>
                <label><input type="radio" name="q25" value="d"> D) Eigenvalue</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Fenchel conjugate</strong><br>
                The Legendre transform is a special case of the Fenchel conjugate for strictly convex functions.
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
    q1: 'a', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'd', q13: 'a', q14: 'a', q15: 'a',
    q16: 'a', q17: 'a', q18: 'd', q19: 'a', q20: 'd'
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
        message = '🌟 Excellent! You have mastered duality theory and advanced concepts!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand Lagrangian and Fenchel duality well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review the KKT conditions and conjugate functions.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review strong duality and optimality conditions.';
    } else {
        message = '📖 Study duality theory again from the beginning!';
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

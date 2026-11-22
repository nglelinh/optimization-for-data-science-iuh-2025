---
layout: post
title: 16-05 Bài tập trắc nghiệm - Tính Đối Ngẫu Tái Xét
chapter: '16'
order: 6
owner: GitHub Copilot
lang: vi
categories:
- chapter16
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter16/16_04_Quiz_Duality_Revisited/
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Duality Revisited - Nhìn Lại Tính Đối Ngẫu**

#### **Lagrangian formulation của primal-dual**
**Bài toán nguyên thủy:**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad l_j(x) = 0$$

**Lagrangian:**
$$L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x)$$

#### **Primal-dual reformulation**
**Primal (reformulated):**
$$\min_x \max_{u \ge 0, v} L(x,u,v)$$

**Dual (reformulated):**
$$\max_{u \ge 0, v} \min_x L(x,u,v)$$

#### **Indicator function interpretation**
- **Primal:** $$\max_{u,v}$$ acts như indicator function cho constraint violations
- **Dual:** $$\min_x$$ provides domain relaxation
- **Equivalence:** Reformulated problems equivalent to original under feasibility

### 🔄 **Weak và Strong Duality (Refined)**

#### **Weak Duality Theorem**
**Always true:** $$p \ge d$$ (primal optimal ≥ dual optimal)

<div class="textbook-proof" markdown="1">
**Proof:** From minimax inequality
$$\min_x \max_{u \ge 0, v} L(x,u,v) \ge \max_{u \ge 0, v} \min_x L(x,u,v)$$
</div>

#### **Strong Duality (Refined Slater's Condition)**
**Condition:** For domain $$D$$, assume $$f, h_1,\ldots,h_p$$ convex và $$h_{p+1},\ldots,h_m, l_1,\ldots,l_r$$ affine.

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

với $$Q$$ symmetric positive semidefinite

**Lagrangian:**
$$L(x,s,y) = \frac{1}{2}x^T Q x + c^T x - s^T x + (b - Ax)^T y$$

**Stationarity:** $$Qx + c - s - A^T y = 0$$
$$\Rightarrow Qx = A^T y + s - c$$

**Dual:**
$$\max b^T y - \frac{1}{2}x^T Q x \quad \text{s.t.} \quad Qx = A^T y + s - c, \quad s \ge 0$$

**Key insight:** Dual của QP cũng là QP!

#### **3. Barrier Method Duality**

**LP Barrier Primal:**
$$\min c^T x - \tau \sum_{i=1}^n \log(x_i) \quad \text{s.t.} \quad Ax = b$$

**Lagrangian:**
$$L(x,y) = c^T x - \tau \sum_{i=1}^n \log(x_i) + (b - Ax)^T y$$

**Optimal $$x$$:** $$x_i = \frac{\tau}{s_i}$$ với $$s = c - A^T y$$

**LP Barrier Dual:**
$$\max b^T y + \tau \sum_{i=1}^n \log(s_i) \quad \text{s.t.} \quad A^T y + s = c$$ (bỏ qua hằng số $$n\tau(1 - \log\tau)$$)

**Beautiful result:** Barrier dual = Dual của barrier!

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

với $$\tau = \frac{1}{t}$$, $$u_i(t) = -\frac{1}{t h_i(x^*(t))}$$, $$\hat{v} = \frac{1}{t}v$$

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

với $$X = \text{diag}(x^*)$$, $$S = \text{diag}(s^*)$$

#### **Barrier Problem Conditions**
$$\begin{align}
A^T y^* + s^* &= c \\
Ax^* &= b \\
X S \mathbf{1} &= \tau \mathbf{1} \\
x^*, s^* &> 0
\end{align}$$

#### **Algorithm implications:**
- **Simplex (primal):** Maintain conditions 2, 3 và $$x \ge 0$$; gradually satisfy 1 với $$s \ge 0$$ (dual feasibility)
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
**Symmetry:** Dual của dual = primal (if $$f,g$$ convex và closed)

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
- **Primal strictly feasible** OR **dual strictly feasible** (và giá trị tối ưu hữu hạn) ⟹ strong duality
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
1. **Primal-dual methods:** Update both primal và dual variables
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
- **Primal:** Direct search trong feasible region
- **Dual:** Supporting hyperplane approach
- **Central path:** Smooth trajectory through interior
- **Strong duality:** Perfect geometric correspondence

#### **3. Algorithmic implications**
- **Simplex:** Vertex-hopping on boundary
- **Interior point:** Path-following through interior
- **Primal-dual:** Simultaneous primal-dual updates
- **Barrier methods:** Perturbed optimality conditions

### 🎯 **Kết Nối Với Các Chương**

#### **From previous chapters:**
- **Chương 10:** LP duality foundation
- **Chương 11:** General Lagrangian duality
- **Chương 12:** KKT conditions
- **Chương 15:** Barrier methods và central path

#### **Advanced connections:**
- **Conjugate functions:** Fenchel duality framework
- **Conic programming:** Generalization to cones
- **Self-duality:** Special structure exploitation
- **Perturbed KKT:** Bridge between exact và approximate

#### **Future applications:**
- **Primal-dual algorithms:** Simultaneous updates
- **Interior point methods:** Polynomial-time algorithms
- **Semidefinite programming:** Matrix optimization
- **Robust optimization:** Worst-case analysis

### 🌟 **Ý Nghĩa Lý Thuyết**

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
- **Symmetry:** Dual của dual = primal
- **Self-duality:** Some cones are self-dual
- **Conjugate functions:** Elegant mathematical framework
- **Central path:** Smooth geometric trajectory

### 💡 **Mẹo Thực Hành**

#### **When to use different duality formulations:**
1. **Lagrangian:** General constrained problems
2. **Fenchel:** Composite functions, regularization
3. **Conic:** Problems with cone constraints
4. **Barrier:** Interior point algorithms

#### **Algorithm selection:**
- **Primal easier:** Direct primal methods
- **Dual easier:** Dual methods or primal-dual
- **Both complex:** Barrier methods với central path
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

### 📈 **Ứng Dụng Thực Tế**

#### **Linear và Conic Programming:**
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

### 🌟 **Legacy của chương 16:**

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
5. **Practical power:** Enables efficient algorithms và software

### 💫 **Philosophical impact:**

Chương 16 **unifies duality theory**:
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

Each face reveals different aspects của same underlying mathematical structure, enabling **flexible algorithm design** và **deep theoretical understanding**. This multiplicity of perspectives is what makes modern optimization both **theoretically elegant** và **practically powerful**.

### 💡 **Final insight:**

Chương 16 demonstrates that **duality is not just mathematical curiosity** - it's **fundamental organizing principle** của optimization theory. From simple LP duality đến sophisticated Fenchel duality, từ exact KKT conditions đến perturbed barrier conditions, từ primal algorithms đến primal-dual methods - **duality provides unified framework** that connects theory với practice, algorithms với applications, mathematics với engineering.

**Duality = Multiple perspectives on same optimization reality!**

---

💡 **Thông điệp cuối cùng:** Duality Revisited không chỉ review previous concepts - nó **synthesizes multiple duality perspectives** into unified framework, showing how Lagrangian, Fenchel, conic, và barrier dualities are all **different faces of same fundamental principle**!

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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về Duality Revisited, bao gồm Lagrangian duality theory, optimality conditions, Fenchel duality và advanced duality concepts.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: Tính Đối Ngẫu Tái Xét & Lý Thuyết Nâng Cao</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Lagrangian definition -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Lagrangian cho bài toán có constraints \(h_i(x) \leq 0\) và \(l_j(x) = 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(L(x,u,v) = f(x) - \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(L(x,u,v) = f(x) + \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(L(x,u,v) = f(x) - \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)$$</strong><br>
                Lagrangian standard form với dual variables $$u_i \geq 0$$ cho inequality constraints và $$v_j$$ free cho equality constraints.
            </div>
        </div>

        <!-- Câu hỏi 2: Primal problem reformulation -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Bài toán primal có thể viết lại thành:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\min_x \max_{u \geq 0, v} L(x,u,v)\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\max_x \min_{u \geq 0, v} L(x,u,v)\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\min_x \min_{u \geq 0, v} L(x,u,v)\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\max_x \max_{u \geq 0, v} L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min_x \max_{u \geq 0, v} L(x,u,v)$$</strong><br>
                Primal problem: minimize over $$x$$, maximize Lagrangian over dual variables để enforce constraints.
            </div>
        </div>

        <!-- Câu hỏi 3: Dual problem -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Bài toán dual tương ứng là:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(\max_{u \geq 0, v} \min_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\min_{u \geq 0, v} \max_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(\max_{u \geq 0, v} \max_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(\min_{u \geq 0, v} \min_x L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max_{u \geq 0, v} \min_x L(x,u,v)$$</strong><br>
                Dual problem: maximize over dual variables, minimize Lagrangian over primal variables.
            </div>
        </div>

        <!-- Câu hỏi 4: Dual function -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Dual function \(g(u,v)\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) \(g(u,v) = \inf_x L(x,u,v)\)</label>
                <label><input type="radio" name="q4" value="b"> B) \(g(u,v) = \sup_x L(x,u,v)\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(g(u,v) = L(x^*,u,v)\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(g(u,v) = \nabla_x L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$g(u,v) = \inf_x L(x,u,v)$$</strong><br>
                Dual function là infimum của Lagrangian over primal variables, luôn concave trong dual variables.
            </div>
        </div>

        <!-- Câu hỏi 5: Strong duality condition -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Strong duality xảy ra khi:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(p^* = d^*\) (primal optimal = dual optimal)</label>
                <label><input type="radio" name="q5" value="b"> B) \(p^* > d^*\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(p^* < d^*\)</label>
                <label><input type="radio" name="q5" value="d"> D) Duality gap = ∞</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$p^* = d^*$$ (primal optimal = dual optimal)</strong><br>
                Strong duality: không có duality gap, primal và dual optimal values bằng nhau.
            </div>
        </div>

        <!-- Câu hỏi 6: KKT stationarity -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: KKT stationarity condition là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(\nabla_x L(x^*,u^*,v^*) = 0\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(h_i(x^*) \leq 0\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(u_i^* \geq 0\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(u_i^* h_i(x^*) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\nabla_x L(x^*,u^*,v^*) = 0$$</strong><br>
                Stationarity: gradient của Lagrangian theo primal variables bằng 0 tại optimal point.
            </div>
        </div>

        <!-- Câu hỏi 7: Complementary slackness -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Complementary slackness condition là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(u_i^* h_i(x^*) = 0\) for all \(i\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(u_i^* + h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(u_i^* h_i(x^*) \geq 0\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(u_i^* = h_i(x^*)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$u_i^* h_i(x^*) = 0$$ for all $$i$$</strong><br>
                Complementary slackness: dual variable bằng 0 nếu constraint không active, hoặc constraint active nếu dual variable > 0.
            </div>
        </div>

        <!-- Câu hỏi 8: Fenchel conjugate -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Fenchel conjugate của hàm \(f\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(f^*(y) = \sup_x (y^T x - f(x))\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(f^*(y) = \inf_x (y^T x - f(x))\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(f^*(y) = \sup_x (y^T x + f(x))\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(f^*(y) = f(y)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \sup_x (y^T x - f(x))$$</strong><br>
                Fenchel conjugate (Legendre transform): supremum của linear function trừ original function.
            </div>
        </div>

        <!-- Câu hỏi 9: Fenchel duality -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Fenchel duality cho bài toán \(\min_x f(x) + g(Ax)\) có dual:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\max_v -f^*(A^T v) - g^*(-v)\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\min_v f^*(A^T v) + g^*(v)\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\max_v f^*(A^T v) - g^*(v)\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\min_v -f^*(A^T v) + g^*(-v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max_v -f^*(A^T v) - g^*(-v)$$</strong><br>
                Fenchel dual sử dụng conjugate functions của cả $$f$$ và $$g$$ với appropriate transformations.
            </div>
        </div>

        <!-- Câu hỏi 10: Biconjugate -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Biconjugate \(f^{**}\) của hàm convex \(f\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(f^{**} = f\) (nếu \(f\) convex và lower semicontinuous)</label>
                <label><input type="radio" name="q10" value="b"> B) \(f^{**} = -f\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(f^{**} = f^2\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(f^{**} = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^{**} = f$$ (nếu $$f$$ convex và lower semicontinuous)</strong><br>
                Fenchel-Moreau theorem: biconjugate của convex lower semicontinuous function là chính nó.
            </div>
        </div>

        <!-- Câu hỏi 11: Saddle point -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: \((x^*, u^*, v^*)\) là saddle point của Lagrangian nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(L(x^*, u, v) \leq L(x^*, u^*, v^*) \leq L(x, u^*, v^*)\) for all feasible \((x,u,v)\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(L(x^*, u^*, v^*) = 0\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(\nabla L(x^*, u^*, v^*) = 0\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(L(x, u, v) = L(x^*, u^*, v^*)\) for all \((x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$L(x^*, u, v) \leq L(x^*, u^*, v^*) \leq L(x, u^*, v^*)$$ for all feasible $$(x,u,v)$$</strong><br>
                Saddle point: minimum theo primal variables, maximum theo dual variables.
            </div>
        </div>

        <!-- Câu hỏi 12: Slater condition -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Với bài toán lồi, Slater condition đảm bảo:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Strong duality holds</label>
                <label><input type="radio" name="q12" value="b"> B) Weak duality holds</label>
                <label><input type="radio" name="q12" value="c"> C) No duality gap</label>
                <label><input type="radio" name="q12" value="d"> D) Cả A và C</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Cả A và C</strong><br>
                Slater condition (strict feasibility) đảm bảo strong duality, tức là no duality gap.
            </div>
        </div>

        <!-- Câu hỏi 13: Linear programming dual -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Dual của LP \(\min c^T x\) s.t. \(Ax = b, x \geq 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(\max b^T y\) s.t. \(A^T y \leq c\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(\min b^T y\) s.t. \(A^T y \geq c\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(\max c^T y\) s.t. \(A^T y = b\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(\min A^T y\) s.t. \(b^T y \leq c\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max b^T y$$ s.t. $$A^T y \leq c$$</strong><br>
                Standard LP dual: maximize với dual variables $$y$$ free, constraint $$A^T y \leq c$$.
            </div>
        </div>

        <!-- Câu hỏi 14: Quadratic programming dual -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Dual của QP \(\min \frac{1}{2}x^T Q x + c^T x\) s.t. \(Ax \leq b\) với \(Q \succ 0\):</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(\max -\frac{1}{2}(A^T u + c)^T Q^{-1} (A^T u + c) - b^T u\) s.t. \(u \geq 0\)</label>
                <label><input type="radio" name="q14" value="b"> B) \(\min \frac{1}{2}u^T Q u - b^T u\) s.t. \(u \geq 0\)</label>
                <label><input type="radio" name="q14" value="c"> C) \(\max b^T u\) s.t. \(A^T u = c\)</label>
                <label><input type="radio" name="q14" value="d"> D) \(\min c^T u + b^T u\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max -\frac{1}{2}(A^T u + c)^T Q^{-1} (A^T u + c) - b^T u$$ s.t. $$u \geq 0$$</strong><br>
                QP dual được derive từ Lagrangian, eliminate primal variables bằng stationarity condition.
            </div>
        </div>

        <!-- Câu hỏi 15: Conjugate of quadratic -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Conjugate của \(f(x) = \frac{1}{2}x^T Q x\) với \(Q \succ 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(f^*(y) = \frac{1}{2}y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(f^*(y) = \frac{1}{2}y^T Q y\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(f^*(y) = y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(f^*(y) = -\frac{1}{2}y^T Q^{-1} y\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \frac{1}{2}y^T Q^{-1} y$$</strong><br>
                Conjugate của quadratic form: thay $$Q$$ bằng $$Q^{-1}$$, giữ nguyên coefficient $$\frac{1}{2}$$.
            </div>
        </div>

        <!-- Câu hỏi 16: Moreau envelope -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Moreau envelope của hàm \(f\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(M_\lambda f(x) = \inf_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(M_\lambda f(x) = f(x) + \lambda\|x\|^2\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(M_\lambda f(x) = \lambda f(x)\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(M_\lambda f(x) = f(\lambda x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$M_\lambda f(x) = \inf_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)$$</strong><br>
                Moreau envelope: smooth approximation của function bằng cách thêm quadratic regularization.
            </div>
        </div>

        <!-- Câu hỏi 17: Proximal operator -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Proximal operator liên quan đến Moreau envelope như thế nào?</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(\text{prox}_{\lambda f}(x) = \arg\min_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(\text{prox}_{\lambda f}(x) = \nabla M_\lambda f(x)\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(\text{prox}_{\lambda f}(x) = M_\lambda f(x)\)</label>
                <label><input type="radio" name="q17" value="d"> D) \(\text{prox}_{\lambda f}(x) = x - \lambda \nabla f(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\text{prox}_{\lambda f}(x) = \arg\min_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)$$</strong><br>
                Proximal operator là argmin của expression trong Moreau envelope definition.
            </div>
        </div>

        <!-- Câu hỏi 18: Duality in SVM -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Trong SVM, dual problem có ưu điểm:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Kernel trick có thể áp dụng</label>
                <label><input type="radio" name="q18" value="b"> B) Số variables phụ thuộc vào số data points</label>
                <label><input type="radio" name="q18" value="c"> C) Quadratic programming với box constraints</label>
                <label><input type="radio" name="q18" value="d"> D) Tất cả các ưu điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ưu điểm trên</strong><br>
                SVM dual cho phép kernel trick, có structure đơn giản hơn, và efficient cho high-dimensional features.
            </div>
        </div>

        <!-- Câu hỏi 19: Weak duality theorem -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Weak duality theorem nói rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(d^* \leq p^*\) luôn đúng</label>
                <label><input type="radio" name="q19" value="b"> B) \(d^* \geq p^*\) luôn đúng</label>
                <label><input type="radio" name="q19" value="c"> C) \(d^* = p^*\) luôn đúng</label>
                <label><input type="radio" name="q19" value="d"> D) Không có quan hệ giữa \(d^*\) và \(p^*\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$d^* \leq p^*$$ luôn đúng</strong><br>
                Weak duality: dual optimal luôn là lower bound của primal optimal, independent of convexity.
            </div>
        </div>

        <!-- Câu hỏi 20: Applications of duality -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Duality theory được ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Sensitivity analysis</label>
                <label><input type="radio" name="q20" value="b"> B) Algorithm design (dual methods)</label>
                <label><input type="radio" name="q20" value="c"> C) Theoretical analysis và bounds</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các ứng dụng trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ứng dụng trên</strong><br>
                Duality theory có ứng dụng rộng rãi: sensitivity analysis, dual algorithms, theoretical bounds, economic interpretation.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Trong duality revisited, strong duality xảy ra khi:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Duality gap = 0</label>
                <label><input type="radio" name="q21" value="b"> B) Primal infeasible</label>
                <label><input type="radio" name="q21" value="c"> C) Dual infeasible</label>
                <label><input type="radio" name="q21" value="d"> D) Cả primal và dual unbounded</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Duality gap = 0</strong><br>
                Strong duality: $$p^* = d^*$$ (duality gap bằng 0).
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Fenchel conjugate của hàm $$f(x) = \frac{1}{2}x^2$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$f^*(y) = \frac{1}{2}y^2$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$f^*(y) = y^2$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$f^*(y) = \frac{1}{4}y^2$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$f^*(y) = 2y^2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \frac{1}{2}y^2$$</strong><br>
                Fenchel conjugate của $$\frac{1}{2}x^2$$ là $$\frac{1}{2}y^2$$.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Bidual theorem khẳng định:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$f^{**} = f$$ nếu $$f$$ lồi và đóng</label>
                <label><input type="radio" name="q23" value="b"> B) $$f^{**} = -f$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$f^{**} = f^2$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$f^{**}$$ không tồn tại</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^{**} = f$$ nếu $$f$$ lồi và đóng</strong><br>
                Với hàm lồi đóng, conjugate của conjugate trả về hàm gốc.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Moreau decomposition cho biết:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$x = \text{prox}_f(x) + \text{prox}_{f^*}(x)$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$x = \text{prox}_f(x) - \text{prox}_{f^*}(x)$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$x = \text{prox}_f(x) \cdot \text{prox}_{f^*}(x)$$</label>
                <label><input type="radio" name="q24" value="d"> D) Không có công thức</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x = \text{prox}_f(x) + \text{prox}_{f^*}(x)$$</strong><br>
                Moreau decomposition: mọi điểm có thể phân tích thành tổng của hai proximal projection.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Legendre transform liên quan đến:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Fenchel conjugate</label>
                <label><input type="radio" name="q25" value="b"> B) Gradient</label>
                <label><input type="radio" name="q25" value="c"> C) Hessian</label>
                <label><input type="radio" name="q25" value="d"> D) Eigenvalue</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Fenchel conjugate</strong><br>
                Legendre transform là trường hợp đặc biệt của Fenchel conjugate cho hàm strictly convex.
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
    q1: 'a', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'd', q13: 'a', q14: 'a', q15: 'a',
    q16: 'a', q17: 'a', q18: 'd', q19: 'a', q20: 'd'
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
        message = '🌟 Xuất sắc! Bạn đã thành thạo duality theory và advanced concepts!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về Lagrangian và Fenchel duality.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại KKT conditions và conjugate functions.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại strong duality và optimality conditions.';
    } else {
        message = '📖 Hãy học lại từ đầu về duality theory nhé!';
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

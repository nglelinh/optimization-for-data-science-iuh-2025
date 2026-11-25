---
layout: post
title: '10-08 Multiple-Choice Quiz - Duality in Linear Programming'
chapter: "10"
order: 9
owner: "GitHub Copilot"
lang: en
categories:
  - chapter10
lesson_type: quiz
redirect_from:
  - /contents/en/chapter10/10_06_Quiz_LP_Duality/
---

Before you jump into the Chapter 10 multiple-choice quiz, run a quick mental check on the sign rules and structural theorems of LP duality. Most quiz mistakes come from flipping a sign on $$Gx \le h$$ vs. $$Gx \ge h$$, forgetting that an unbounded primal forces an infeasible dual (while an infeasible primal can have *either* an unbounded or infeasible dual!), or losing track of how max-flow and matrix games dualize. Use the four pillars and quick dual-check below to lock everything in place.

## Key ideas: Chapter 10 Quiz Readiness Pillars

- **Pillar 1 — Mechanical Dualization Dictionary:** For a minimization primal: $$=$$ constraint $$\leftrightarrow$$ free dual variable; $$\le$$ constraint $$\leftrightarrow$$ $$u \ge 0$$ (in $$-h^\top u$$) or $$y \le 0$$ (in $$h^\top y$$); free primal variable $$\leftrightarrow$$ equality dual constraint; $$x \ge 0$$ $$\leftrightarrow$$ inequality dual constraint.
- **Pillar 2 — Weak, Strong, and Infeasibility Outcomes:** Weak duality ($$d^\star \le p^\star$$) *always* holds. Strong duality ($$d^\star = p^\star$$) holds whenever either primal or dual is feasible and bounded. Remember the one-way trap: primal infeasible does *not* automatically imply dual unbounded (both can be infeasible!).
- **Pillar 3 — Complementary Slackness Preview:** At any optimal pair $$(x^\star, u^\star)$$, every strictly slack primal inequality ($$(Gx^\star)_i < h_i$$) must have zero dual price ($$u_i^\star = 0$$), and every strictly positive dual variable ($$u_i^\star > 0$$) forces its primal constraint to be tight.
- **Pillar 4 — Canonical Applications:** Max-flow dualizes to min-cut (via node potentials $$b_i$$ and edge weights $$a_{ij}$$); zero-sum matrix games dualize player $$J$$'s minimax LP into player $$R$$'s maximin LP (proving von Neumann's theorem).

### Worked example: Spot-Checking a Primal–Dual Pair for Optimality

Primal $$(P)$$: $$\min 5x_1 + 4x_2$$ s.t. $$x_1 + x_2 \ge 3$$, $$2x_1 + x_2 \ge 4$$, $$x_1, x_2 \ge 0$$.
Dual $$(D)$$: $$\max 3y_1 + 4y_2$$ s.t. $$y_1 + 2y_2 \le 5$$, $$y_1 + y_2 \le 4$$, $$y_1, y_2 \ge 0$$.
Someone proposes $$x = (1, 2)^\top$$ and $$y = (3, 1)^\top$$. Are they optimal?

1. **Check primal feasibility of $$x = (1, 2)^\top$$:**
   - $$1 + 2 = 3 \ge 3$$ (tight!), $$2(1) + 2 = 4 \ge 4$$ (tight!), $$x \ge 0$$. Feasible!
   - Primal objective: $$5(1) + 4(2) = 13$$.
2. **Check dual feasibility of $$y = (3, 1)^\top$$:**
   - $$3 + 2(1) = 5 \le 5$$ (tight!), $$3 + 1 = 4 \le 4$$ (tight!), $$y \ge 0$$. Feasible!
   - Dual objective: $$3(3) + 4(1) = 13$$.
3. **Conclude by Weak Duality:** Since $$x$$ is primal feasible, $$y$$ is dual feasible, and $$c^\top x = 13 = b^\top y$$, **both** $$x = (1, 2)^\top$$ and $$y = (3, 1)^\top$$ are certified globally optimal—zero simplex pivots required!

## Theory Review

Before starting the exercises, review the key concepts of this chapter:

### **Duality in Linear Programming (LP Duality)**

#### **Basic idea**
LP duality arises from looking for a **lower bound** on the optimal value of the primal problem.

**Principle:** If the objective can be written as a **linear combination** of the constraints, we obtain a lower bound.

#### **From simple examples to the general case**

**Example 1:** The constraint contains the objective
$$\min_{x,y} x + y \quad \text{s.t.} \quad x + y \ge 2, \quad x,y \ge 0$$

**Obvious lower bound:** $$B = 2$$

**Example 2:** Writing the objective as a linear combination
$$\min_{x,y} x + 3y \quad \text{s.t.} \quad x + y \ge 2, \quad x,y \ge 0$$

**Linear combination:**
$$1 \cdot (x + y) + 0 \cdot x + 2 \cdot y = x + 3y \ge 2$$

**Lower bound:** $$B = 2$$

### 📏 **Constructing the Dual Problem**

#### **General primal problem**
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b, \quad Gx \le h$$

#### **Method for constructing the dual**
1. **Define dual variables:** $$u$$ (for equality constraints), $$v \ge 0$$ (for inequality constraints)
2. **Form a linear combination:** $$u^T(Ax - b) + v^T(Gx - h) \le 0$$
3. **Rearrange to isolate the objective:** $$(-A^T u - G^T v)^T x \ge -b^T u - h^T v$$
4. **Matching condition:** $$c = -A^T u - G^T v$$

#### **The dual problem**
$$\max_{u,v} -b^T u - h^T v \quad \text{s.t.} \quad c = -A^T u - G^T v, \quad v \ge 0$$

### 🔄 **Primal-Dual Conversion Rules**

| **Primal** | **Dual** |
|------------|----------|
| $$\min$$ | $$\max$$ |
| $$Ax = b$$ | $$u$$ unconstrained |
| $$Gx \le h$$ | $$v \ge 0$$ |
| $$x \ge 0$$ | Inequality constraint in the dual |
| $$x$$ unconstrained | Equality constraint in the dual |

#### **Conversion example**
**Primal:**
$$\min_{x,y} px + qy \quad \text{s.t.} \quad x \ge 0, \quad y \le 1, \quad 3x + y = 2$$

**Dual:**
$$\max_{a,b,c} 2c - b \quad \text{s.t.} \quad a + 3c = p, \quad -b + c = q, \quad a,b \ge 0$$

### 🌊 **Example: Max Flow - Min Cut**

#### **The Max Flow problem**
Find the maximum flow from the source $$s$$ to the sink $$t$$ in a directed graph.

$$\max \sum_{(s,j) \in E} f_{sj} \quad \text{s.t.} \begin{cases}
f_{ij} \ge 0, \quad f_{ij} \le c_{ij} & \forall (i,j) \in E \\
\sum_{(i,k) \in E} f_{ik} = \sum_{(k,j) \in E} f_{kj} & \forall k \in V \setminus \{s,t\}
\end{cases}$$

#### **The Min Cut problem**
Find a cut of minimum capacity separating $$s$$ and $$t$$.

$$\min \sum_{(i,j) \in E} b_{ij} c_{ij} \quad \text{s.t.} \begin{cases}
b_{ij} \ge x_i - x_j & \forall (i,j) \in E \\
x_i, b_{ij} \in \{0,1\} & \forall i,j \\
x_s = 1, x_t = 0
\end{cases}$$

#### **Dual relationship**
**Dual of Max Flow = LP relaxation of Min Cut**

$$\text{Max Flow Value} \le \text{Dual LP} = \text{LP Relaxed Min Cut} \le \text{Min Cut Capacity}$$

**Max-Flow Min-Cut theorem:** All three values are equal!

### **Lagrangian Approach**

#### **The Lagrangian**
For the general optimization problem:
$$\min_x f(x) \quad \text{s.t.} \quad Ax = b, \quad Gx \le h$$

**Lagrangian function:**
$$L(x,u,v) = f(x) + u^T(Ax - b) + v^T(Gx - h)$$

#### **Dual function**
$$g(u,v) = \min_x L(x,u,v)$$

**Property:** $$g(u,v) \le f^*$$ for all $$v \ge 0$$ (weak duality)

#### **The Lagrangian dual problem**
$$\max_{u,v} g(u,v) \quad \text{s.t.} \quad v \ge 0$$

#### **For LP:**
$$g(u,v) = \min_x (c + A^T u + G^T v)^T x - b^T u - h^T v$$

$$= \begin{cases}
-b^T u - h^T v & \text{if } c + A^T u + G^T v = 0 \\
-\infty & \text{otherwise}
\end{cases}$$

**Result:** The same as the classical LP dual!

### 🎮 **Matrix Games**

#### **Game setup**
- **Two players:** J (rows) and R (columns)
- **Payout matrix:** $$P$$ (J pays R)
- **Mixed strategies:** $$x$$ (J), $$y$$ (R)
- **Expected payout:** $$x^T P y$$

#### **J's perspective (minimizer)**
R gets to know J's strategy in advance, so J wants to minimize the worst-case expected payout:
$$\min_x \max_{i=1,\ldots,n} (P^T x)_i \quad \text{s.t.} \quad x \ge 0, \quad \mathbf{1}^T x = 1$$

**Reformulation:**
$$\min_{x,t} t \quad \text{s.t.} \quad x \ge 0, \quad \mathbf{1}^T x = 1, \quad P^T x \preceq t \mathbf{1}$$

#### **R's perspective (maximizer)**
J gets to know R's strategy in advance, so R wants to maximize the worst-case expected payout:
$$\max_y \min_{j=1,\ldots,m} (Py)_j \quad \text{s.t.} \quad y \ge 0, \quad \mathbf{1}^T y = 1$$

**Reformulation:**
$$\max_{y,v} v \quad \text{s.t.} \quad y \ge 0, \quad \mathbf{1}^T y = 1, \quad Py \succeq v \mathbf{1}$$

#### **Von Neumann's Minimax Theorem**
The two problems above are **primal-dual** to each other and have the same optimal value:
$$\min_x \max_y x^T P y = \max_y \min_x x^T P y$$

**Reason:** $$x^T P y$$ is bilinear (convex in $$x$$, concave in $$y$$) and the simplices are compact and convex; moreover this is a pair of dual LPs, so strong duality always holds.

### **Weak vs Strong Duality**

#### **Weak Duality**
**Always true:** Dual value ≤ Primal value
$$\max_{u,v} g(u,v) \le \min_x f(x)$$

**Duality gap:** $$f^* - g^* \ge 0$$

#### **Strong Duality**
**Special condition:** Dual value = Primal value
$$\max_{u,v} g(u,v) = \min_x f(x)$$

**Duality gap:** $$f^* - g^* = 0$$

#### **When Strong Duality holds in LP:**
- **Slater's condition:** A strictly feasible point exists
- **For LP:** If either the primal or the dual is feasible, strong duality holds
- **Exception:** Both primal and dual are infeasible

### 🔄 **Standard Forms of LP**

#### **Standard form**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

**Dual:**
$$\max b^T u \quad \text{s.t.} \quad A^T u \le c$$

#### **Inequality form**
$$\min c^T x \quad \text{s.t.} \quad Ax \le b$$

**Dual:**
$$\max -b^T u \quad \text{s.t.} \quad A^T u = -c, \quad u \ge 0$$

#### **General form**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad Gx \le h$$

**Dual:**
$$\max -b^T u - h^T v \quad \text{s.t.} \quad -A^T u - G^T v = c, \quad v \ge 0$$

### 🛠️ **Practical Techniques**

#### **Building the dual from the primal:**
1. **Identify the problem type:** Min or max, equality or inequality constraints
2. **Apply the conversion rules:** Following the primal-dual table
3. **Check correctness:** Weak duality must hold
4. **Find strong duality conditions:** Slater's condition or feasibility

#### **Economic interpretation:**
- **Primal variables:** Production decisions, resource allocation
- **Dual variables:** Shadow prices, marginal values of the constraints
- **Duality gap:** The difference between the upper and lower bounds

#### **Practical applications:**
- **Network flows:** Internet routing, transportation
- **Game theory:** Strategic decision making, auction design
- **Economics:** Market equilibrium, resource allocation
- **Machine learning:** SVM dual formulation

### **Illustrative Example**

#### **Simple problem:**
**Primal:**
$$\min 2x_1 + 3x_2 \quad \text{s.t.} \quad x_1 + x_2 \ge 1, \quad x_1, x_2 \ge 0$$

**Dual:**
$$\max u \quad \text{s.t.} \quad u \le 2, \quad u \le 3, \quad u \ge 0$$

**Solution:**
- **Primal optimal:** $$x_1^* = 1, x_2^* = 0$$, $$f^* = 2$$
- **Dual optimal:** $$u^* = 2$$, $$g^* = 2$$
- **Strong duality:** $$f^* = g^* = 2$$

#### **Complementary slackness:**
- $$x_1^* > 0 \Rightarrow u^* = 2$$ (tight)
- $$x_2^* = 0 \Rightarrow u^* \le 3$$ (slack OK)
- $$u^* > 0 \Rightarrow x_1^* + x_2^* = 1$$ (primal constraint tight)

### **Connections to Other Chapters**

#### **From the previous chapter:**
- **Chapter 05:** LP as a canonical problem
- **Chapter 04:** Optimality conditions
- **Chapter 03:** Convex functions and their properties

#### **Importance of LP Duality:**
- **Theoretical foundation:** For general duality (Chapter 11)
- **Computational:** Dual simplex, interior point methods
- **Economic interpretation:** Shadow prices, sensitivity analysis
- **Machine learning:** SVM, robust optimization

#### **Looking ahead:**
- **Chapter 11:** General duality theory
- **Chapter 12:** KKT conditions
- **Applications:** Constrained optimization, game theory

### **Theoretical Significance**

#### **Duality as an analysis tool:**
- **Bounds:** Upper and lower bounds on the optimal value
- **Sensitivity:** Effect of changes in the constraints
- **Optimality:** Necessary and sufficient conditions for an optimal solution
- **Algorithms:** Dual-based methods (dual simplex, etc.)

#### **Geometric interpretation:**
- **Primal:** Find a point in the feasible region
- **Dual:** Find a hyperplane supporting the optimal value
- **Strong duality:** Hyperplane touches feasible region

#### **Economic interpretation:**
- **Primal:** Direct resource allocation
- **Dual:** Price-based market mechanism
- **Equilibrium:** Primal-dual optimal solutions

### **Practical Tips**

#### **Recognizing when to use duality:**
1. **Primal is hard to solve:** The dual may be simpler
2. **Sensitivity analysis:** Dual variables give shadow prices
3. **Bounds:** The dual provides bounds for the primal
4. **Algorithm design:** Primal-dual methods

#### **Common mistakes:**
- **Wrong conversion rules:** Mixing up min/max, ≤/≥
- **Forgetting non-negativity conditions:** On dual variables
- **Not checking feasibility:** Of both primal and dual
- **Misinterpretation:** Dual variables are not primal variables

#### **Debugging tips:**
- **Verify weak duality:** $$g^* \le f^*$$ always holds
- **Check complementary slackness:** At the optimal solutions
- **Geometric intuition:** Visualize in 2D when possible
- **Economic meaning:** Dual variables as prices

---

💡 **Tip:** LP duality is the foundation of all duality theory in optimization. Understanding LP duality well will help you master the more advanced duality concepts!

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

This multiple-choice quiz tests your understanding of duality in linear programming (LP duality), weak/strong duality, complementary slackness, the max flow-min cut theorem and matrix games.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: Duality in Linear Programming</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1 -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: Given the primal LP: $$\min c^T x$$ s.t. $$Ax = b, Gx \leq h$$. The dual problem has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) $$\max -b^T u - h^T v$$ s.t. $$-A^T u - G^T v = c, v \geq 0$$</label>
                <label><input type="radio" name="q1" value="b"> B) $$\min -b^T u - h^T v$$ s.t. $$-A^T u - G^T v = c, v \geq 0$$</label>
                <label><input type="radio" name="q1" value="c"> C) $$\max -b^T u - h^T v$$ s.t. $$-A^T u - G^T v = c, v \leq 0$$</label>
                <label><input type="radio" name="q1" value="d"> D) $$\max c^T x$$ s.t. $$Ax \geq b, Gx = h$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max -b^T u - h^T v$$ s.t. $$-A^T u - G^T v = c, v \geq 0$$</strong><br>
                The dual of a minimization problem is a maximization problem. The dual variable $$u$$ for the equality constraints has no sign constraint, and $$v$$ for the inequality constraints must be non-negative. From the Lagrangian $$L = c^Tx + u^T(Ax-b) + v^T(Gx-h)$$, the minimum over $$x$$ is finite if and only if $$c + A^Tu + G^Tv = 0$$, in which case $$g(u,v) = -b^Tu - h^Tv$$.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The weak duality theorem states that:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) The primal optimal value equals the dual optimal value</label>
                <label><input type="radio" name="q2" value="b"> B) The primal optimal value is always greater than or equal to the dual optimal value</label>
                <label><input type="radio" name="q2" value="c"> C) The primal optimal value is always less than the dual optimal value</label>
                <label><input type="radio" name="q2" value="d"> D) The primal and dual cannot both have optimal solutions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The primal optimal value is always greater than or equal to the dual optimal value</strong><br>
                Weak duality: $$p^* \geq d^*$$, where $$p^*$$ is the primal (minimization) optimal value and $$d^*$$ is the dual (maximization) optimal value.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: Strong duality holds when:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$p^* < d^*$$</label>
                <label><input type="radio" name="q3" value="b"> B) $$p^* = d^*$$</label>
                <label><input type="radio" name="q3" value="c"> C) $$p^* > d^*$$</label>
                <label><input type="radio" name="q3" value="d"> D) The primal has no solution</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$p^* = d^*$$</strong><br>
                Strong duality means there is no duality gap: the primal optimal value equals the dual optimal value.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: For the LP pair $$\min c^T x$$ s.t. $$Ax \geq b, x \geq 0$$ and $$\max b^T y$$ s.t. $$A^T y \leq c, y \geq 0$$, complementary slackness states that:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$x_i > 0 \Rightarrow (A^T y)_i = c_i$$ and $$y_j > 0 \Rightarrow (Ax)_j = b_j$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$x_i = 0$$ and $$y_j = 0$$ for all $$i, j$$</label>
                <label><input type="radio" name="q4" value="c"> C) The primal and dual are both feasible</label>
                <label><input type="radio" name="q4" value="d"> D) $$Ax \geq b$$ and $$x \geq 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$x_i > 0 \Rightarrow (A^T y)_i = c_i$$ and $$y_j > 0 \Rightarrow (Ax)_j = b_j$$</strong><br>
                Complementary slackness: if a primal variable is positive then the corresponding dual constraint is tight; if a dual variable is positive then the corresponding primal constraint is tight.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The duality gap is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) $$d^* - p^*$$</label>
                <label><input type="radio" name="q5" value="b"> B) $$p^* - d^*$$</label>
                <label><input type="radio" name="q5" value="c"> C) $$p^* + d^*$$</label>
                <label><input type="radio" name="q5" value="d"> D) $$|p^* - d^*|$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$p^* - d^*$$</strong><br>
                The duality gap is the difference between the primal and dual optimal values. By weak duality, this gap is always non-negative.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: Given an LP in standard form: $$\min c^T x$$ s.t. $$Ax = b, x \geq 0$$. The dual problem is:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) $$\max b^T y$$ s.t. $$A^T y \leq c$$</label>
                <label><input type="radio" name="q6" value="b"> B) $$\max b^T y$$ s.t. $$A^T y = c$$</label>
                <label><input type="radio" name="q6" value="c"> C) $$\min b^T y$$ s.t. $$A^T y \geq c$$</label>
                <label><input type="radio" name="q6" value="d"> D) $$\max b^T y$$ s.t. $$A^T y \geq c$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max b^T y$$ s.t. $$A^T y \leq c$$</strong><br>
                Dual of the standard-form LP: the dual variable $$y$$ has no sign constraint because the primal has equality constraints.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: In the max flow problem, the goal is to:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Minimize the total capacity of the edges</label>
                <label><input type="radio" name="q7" value="b"> B) Maximize the flow from source to sink</label>
                <label><input type="radio" name="q7" value="c"> C) Minimize the number of edges in a path</label>
                <label><input type="radio" name="q7" value="d"> D) Maximize the number of vertices visited</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Maximize the flow from source to sink</strong><br>
                The max flow problem finds the largest flow that can be sent from the source node to the sink node through the network.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The min cut problem finds:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) A set of edges with minimum total capacity that disconnects the source from the sink</label>
                <label><input type="radio" name="q8" value="b"> B) The shortest path from source to sink</label>
                <label><input type="radio" name="q8" value="c"> C) The minimum number of edges connecting all vertices</label>
                <label><input type="radio" name="q8" value="d"> D) The minimum spanning tree of the graph</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) A set of edges with minimum total capacity that disconnects the source from the sink</strong><br>
                Min cut finds a partition of the vertices into two sets such that the total capacity of the edges between them is minimal.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The max flow-min cut theorem states that:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) The max flow value equals the capacity of the min cut</label>
                <label><input type="radio" name="q9" value="b"> B) Max flow is always less than min cut</label>
                <label><input type="radio" name="q9" value="c"> C) Min cut is always less than max flow</label>
                <label><input type="radio" name="q9" value="d"> D) Max flow and min cut are unrelated</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The max flow value equals the capacity of the min cut</strong><br>
                This is a classic example of strong duality: the max flow problem and the min cut problem are duals of each other.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: In a matrix game with payout matrix $$P$$, player J wants to:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Maximize the expected payout</label>
                <label><input type="radio" name="q10" value="b"> B) Minimize the maximum loss (minimax)</label>
                <label><input type="radio" name="q10" value="c"> C) Maximize the minimum gain</label>
                <label><input type="radio" name="q10" value="d"> D) Minimize the expected payout</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Minimize the maximum loss (minimax)</strong><br>
                Player J (row player) wants to minimize the maximum possible loss, i.e. find a mixed strategy that minimizes the worst-case payout.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: If the primal LP has an empty feasible region, then the dual LP:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Also has an empty feasible region</label>
                <label><input type="radio" name="q11" value="b"> B) May be unbounded or infeasible</label>
                <label><input type="radio" name="q11" value="c"> C) Always has an optimal solution</label>
                <label><input type="radio" name="q11" value="d"> D) Is always unbounded</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) May be unbounded or infeasible</strong><br>
                When the primal is infeasible, the dual may be unbounded (if the dual is feasible) or also infeasible.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: In economics, dual variables are usually interpreted as:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Shadow prices</label>
                <label><input type="radio" name="q12" value="b"> B) Production quantities</label>
                <label><input type="radio" name="q12" value="c"> C) Market demands</label>
                <label><input type="radio" name="q12" value="d"> D) Cost coefficients</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Shadow prices</strong><br>
                Dual variables represent the marginal value of resources, i.e. the value gained by increasing a resource constraint by one unit.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The dual of the dual problem is:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) A completely different problem</label>
                <label><input type="radio" name="q13" value="b"> B) The original primal problem</label>
                <label><input type="radio" name="q13" value="c"> C) It does not exist</label>
                <label><input type="radio" name="q13" value="d"> D) Equal to the dual problem</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The original primal problem</strong><br>
                Symmetry property: the dual of the dual is the original primal problem (possibly after a change of form).
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: For strong duality in LP, the required condition is:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Both the primal and the dual have optimal solutions</label>
                <label><input type="radio" name="q14" value="b"> B) The primal or dual has an interior point (Slater condition)</label>
                <label><input type="radio" name="q14" value="c"> C) The feasible region is bounded</label>
                <label><input type="radio" name="q14" value="d"> D) No condition is needed, LP always has strong duality</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) No condition is needed, LP always has strong duality</strong><br>
                Linear programs always satisfy strong duality (unless both are infeasible) thanks to the special nature of linear constraints.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: Primal-dual algorithms solve LPs by:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Solving only the primal problem</label>
                <label><input type="radio" name="q15" value="b"> B) Solving only the dual problem</label>
                <label><input type="radio" name="q15" value="c"> C) Updating both the primal and dual variables simultaneously</label>
                <label><input type="radio" name="q15" value="d"> D) Solving the primal and then the dual sequentially</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Updating both the primal and dual variables simultaneously</strong><br>
                Primal-dual methods maintain and update both primal and dual solutions, using duality to guide convergence.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: The dual optimal solution provides information about:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) The sensitivity of the objective value to changes in the constraints</label>
                <label><input type="radio" name="q16" value="b"> B) The number of iterations needed</label>
                <label><input type="radio" name="q16" value="c"> C) The complexity of the algorithm</label>
                <label><input type="radio" name="q16" value="d"> D) The condition number of the matrix</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The sensitivity of the objective value to changes in the constraints</strong><br>
                Dual variables tell how much the objective value changes when the right-hand side of the constraints changes.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: A Nash equilibrium in a matrix game corresponds to:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Primal optimal solution</label>
                <label><input type="radio" name="q17" value="b"> B) Dual optimal solution</label>
                <label><input type="radio" name="q17" value="c"> C) A pair of primal-dual optimal solutions</label>
                <label><input type="radio" name="q17" value="d"> D) Any feasible solution</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) A pair of primal-dual optimal solutions</strong><br>
                Nash equilibrium mixed strategies correspond to the optimal solutions of a primal-dual pair of LP problems.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: If the primal LP is unbounded below, then the dual LP:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Is also unbounded</label>
                <label><input type="radio" name="q18" value="b"> B) Infeasible</label>
                <label><input type="radio" name="q18" value="c"> C) Has an optimal solution</label>
                <label><input type="radio" name="q18" value="d"> D) Bounded</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Infeasible</strong><br>
                If the primal (minimization) is unbounded below, then the dual (maximization) must be infeasible by weak duality.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: In the max flow problem, the flow conservation constraint requires:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Total flow into each node equals total flow out (except source/sink)</label>
                <label><input type="radio" name="q19" value="b"> B) The flow on each edge does not exceed its capacity</label>
                <label><input type="radio" name="q19" value="c"> C) The flow must be non-negative</label>
                <label><input type="radio" name="q19" value="d"> D) All of the above conditions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Total flow into each node equals total flow out (except source/sink)</strong><br>
                Flow conservation: $$\sum_{i} f_{ij} = \sum_{k} f_{jk}$$ at each intermediate node $$j$$.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: LP duality has applications in:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Economics (resource allocation)</label>
                <label><input type="radio" name="q20" value="b"> B) Network flows and transportation</label>
                <label><input type="radio" name="q20" value="c"> C) Game theory and decision making</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above fields</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above fields</strong><br>
                LP duality has wide applications: economics (shadow prices), networks (max flow-min cut), game theory (minimax), and many other fields.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: The dual of the LP $$\min c^T x$$ subject to $$Ax \geq b, x \geq 0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$\max b^T y$$ subject to $$A^T y \leq c, y \geq 0$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$\max b^T y$$ subject to $$A^T y \geq c, y \geq 0$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$\min b^T y$$ subject to $$A^T y \leq c, y \geq 0$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$\max c^T y$$ subject to $$A^T y \leq b, y \geq 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max b^T y$$ subject to $$A^T y \leq c, y \geq 0$$</strong><br>
                The dual of this LP has the form $$\max b^T y$$ subject to $$A^T y \leq c, y \geq 0$$.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The strong duality theorem in LP states:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$c^T x^* = b^T y^*$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$c^T x^* \leq b^T y^*$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$c^T x^* \geq b^T y^*$$</label>
                <label><input type="radio" name="q22" value="d"> D) There is no relationship</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$c^T x^* = b^T y^*$$</strong><br>
                When both the primal and dual have optimal solutions, their optimal values are equal.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: Complementary slackness in LP: if $$x_i > 0$$ then:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) The corresponding dual constraint is active</label>
                <label><input type="radio" name="q23" value="b"> B) The corresponding dual constraint is inactive</label>
                <label><input type="radio" name="q23" value="c"> C) $$y_i = 0$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$y_i > 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The corresponding dual constraint is active</strong><br>
                Complementary slackness: if $$x_i > 0$$ then the dual constraint $$\sum_j a_{ji}y_j = c_i$$ must be active.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The duality gap in LP equals:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$c^T x - b^T y$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$b^T y - c^T x$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$|c^T x - b^T y|$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$\max\{c^T x, b^T y\}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$c^T x - b^T y$$</strong><br>
                Duality gap = primal value - dual value = $$c^T x - b^T y \geq 0$$.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: Given the LP: $$\min 2x_1 + 3x_2$$ subject to $$x_1 + x_2 \geq 1, x_1, x_2 \geq 0$$. The dual problem is:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$\max y$$ subject to $$y \leq 2, y \leq 3, y \geq 0$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$\max y$$ subject to $$y \geq 2, y \geq 3, y \geq 0$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$\min y$$ subject to $$y \leq 2, y \leq 3, y \geq 0$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$\max 2y + 3y$$ subject to $$y \geq 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\max y$$ subject to $$y \leq 2, y \leq 3, y \geq 0$$</strong><br>
                Dual: $$\max y$$ subject to $$y \leq 2$$ (from $$x_1 \geq 0$$), $$y \leq 3$$ (from $$x_2 \geq 0$$), $$y \geq 0$$.
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
    q1: 'a', q2: 'b', q3: 'b', q4: 'a', q5: 'b',
    q6: 'a', q7: 'b', q8: 'a', q9: 'a', q10: 'b',
    q11: 'b', q12: 'a', q13: 'b', q14: 'd', q15: 'c',
    q16: 'a', q17: 'c', q18: 'b', q19: 'a', q20: 'd'
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
        message = '🌟 Excellent! You have mastered LP duality theory!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand primal-dual relationships well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review complementary slackness and the applications.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review weak/strong duality and the formulations.';
    } else {
        message = '📖 Study LP duality again from the beginning!';
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

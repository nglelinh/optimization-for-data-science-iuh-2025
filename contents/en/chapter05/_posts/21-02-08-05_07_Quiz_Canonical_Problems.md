---
layout: post
title: '05-07 Multiple-Choice Quiz - Canonical Optimization Problems'
chapter: '05'
order: 11
owner: GitHub Copilot
lang: en
categories:
- chapter05
lesson_type: quiz
---

This multiple-choice quiz tests your understanding of the canonical optimization problems, including linear programming, quadratic programming, least squares and linear regression.

---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### 📊 **Linear Programming (LP)**

**General form:**
$$\begin{align}
&\min_{x} &&c^T x + d \\
&\text{s.t.} &&Gx \preceq h \\
&&&Ax = b
\end{align}$$

**Standard form:**
$$\begin{align}
&\min_{x} &&c^T x \\
&\text{s.t.} &&Ax = b \\
&&&x \succeq 0
\end{align}$$

**Main features:**
- The objective and constraints are all **affine** (linear)
- The feasible set is a **polyhedron**
- If an optimal solution exists (and the polyhedron has a vertex), there is always an optimal solution at a **vertex** of the polyhedron
- Can be solved efficiently by the **Simplex algorithm**

**Converting to standard form:**
1. Add slack variables: $$g_i(x) \le 0 \Rightarrow g_i(x) + s_i = 0, s_i \ge 0$$
2. Split variables: $$x = x^+ - x^-$$ with $$x^+, x^- \ge 0$$

### 📈 **Quadratic Programming (QP)**

**General form:**
$$\begin{align}
&\min_{x} &&\frac{1}{2}x^T P x + q^T x + r \\
&\text{s.t.} &&Gx \preceq h \\
&&&Ax = b
\end{align}$$

**Convexity condition:** $$P \in \mathbb{S}_+^n$$ (positive semidefinite matrix)

**Checking $$P \succeq 0$$:**
- All eigenvalues $$\lambda_i \ge 0$$
- $$v^T P v \ge 0$$ for all $$v$$
- For a $$2 \times 2$$ matrix: $$a \ge 0, c \ge 0, ac \ge b^2$$

**Example applications:**
- **Portfolio optimization:** $$\max \mu^T x - \frac{\gamma}{2}x^T P x$$
- **SVM:** $$\min \frac{1}{2}\lVert \beta \rVert_2^2 + C\sum \xi_i$$
- **Ridge regression:** $$\min \lVert Ax - b \rVert_2^2 + \lambda \lVert x \rVert_2^2$$

### 🎯 **Least Squares**

**Basic problem:**
$$\min_{x} \lVert Ax - b \rVert_2^2 = \min_{x} \sum_{i=1}^m (a_i^T x - b_i)^2$$

**Closed-form solution (Normal Equation):**
$$x^* = (A^T A)^{-1} A^T b$$

**Condition for a unique solution:** $$A^T A$$ invertible ($$A$$ has full column rank)

**Simple linear regression:**
- Model: $$y = mx + c$$
- Solution: $$m = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$$, $$c = \bar{y} - m\bar{x}$$

**Multiple linear regression:**
- Model: $$y = X\beta$$
- Solution: $$\beta^* = (X^T X)^{-1} X^T y$$

### 🔢 **Other Canonical Problems**

**QCQP (Quadratically Constrained QP):**
$$\begin{align}
&\min &&\frac{1}{2}x^T P_0 x + q_0^T x \\
&\text{s.t.} &&\frac{1}{2}x^T P_i x + q_i^T x + r_i \le 0, \quad i = 1,\ldots,m
\end{align}$$

**SOCP (Second-Order Cone Programming):**
$$\begin{align}
&\min &&f^T x \\
&\text{s.t.} &&\lVert A_i x + b_i \rVert_2 \le c_i^T x + d_i, \quad i = 1,\ldots,m
\end{align}$$

**SDP (Semidefinite Programming):**
$$\begin{align}
&\min &&\text{tr}(CX) \\
&\text{s.t.} &&\text{tr}(A_i X) = b_i, \quad i = 1,\ldots,m \\
&&&X \succeq 0
\end{align}$$

### 🏗️ **Relations Between the Problems**

```
LP ⊆ QP ⊆ QCQP ⊆ SDP
    ⊆ SOCP ⊆
```

**Explanation:**
- **LP → QP:** Set $$P = 0$$ in the QP
- **QP → QCQP:** Linear constraints are a special case of quadratic constraints
- **SOCP → SDP:** Second-order cones can be represented by positive semidefinite (LMI) constraints
- **QCQP → SDP:** (Convex) QCQPs can be written as SDPs using the Schur complement

### 🛠️ **Solution Algorithms**

**Linear Programming:**
- **Simplex Method:** Move from vertex to vertex
- **Interior Point Methods:** Travel through the interior of the feasible set
- **Dual Simplex:** Start from a dual feasible solution

**Quadratic Programming:**
- **Active Set Methods:** Identify the active constraints
- **Interior Point Methods:** Extended from LP
- **Gradient Projection:** Project the gradient step onto the feasible set

**Least Squares:**
- **Normal Equation:** Direct solution $$x^* = (A^T A)^{-1} A^T b$$
- **QR Decomposition:** More numerically stable
- **SVD:** Handles singular matrices
- **Gradient Descent:** For large problems

### 📋 **Real-World Applications**

**Linear Programming:**
- Production and distribution optimization
- Diet planning
- Portfolio management
- Staff scheduling

**Quadratic Programming:**
- Markowitz portfolio optimization
- Support Vector Machines
- Model Predictive Control
- Image denoising

**Least Squares:**
- Linear and nonlinear regression
- Curve fitting and interpolation
- Signal processing
- Computer vision

### 🔍 **Recognizing the Problem Type**

**Checklist:**
- [ ] Linear objective? → **LP**
- [ ] Quadratic objective, linear constraints? → **QP**
- [ ] Quadratic constraints? → **QCQP**
- [ ] Norm constraints? → **SOCP**
- [ ] Matrix constraints? → **SDP**
- [ ] No constraints, squared objective? → **Least Squares**

### ⚡ **Computational Complexity**

| Problem | Complexity | Notes |
|----------|-------------|---------|
| **LP** | Polynomial (interior point); Simplex fast in practice | Simplex: good on average |
| **QP** | Polynomial | Interior point methods |
| **Least Squares** | $$O(n^3)$$ | Normal equation |
| **SOCP** | Polynomial | Similar to SDP |
| **SDP** | Polynomial | Slower than LP, QP |

---

💡 **Tip:** Always start with the simplest problem class that solves your problem. LP is faster than QP, and QP is faster than SDP!

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Multiple-Choice Quiz: Canonical Optimization Problems</h2>
        <p>Choose the best answer for each question. The quiz focuses on the basic concepts and practical applications of LP, QP and least squares.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Question 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Question 1 -->
        <div class="question" id="q1">
            <h3>Question 1: Which of the following characterizes linear programming (LP)?</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) The objective and constraints are all linear functions</label>
                <label><input type="radio" name="q1" value="b"> B) The objective is quadratic, the constraints are linear</label>
                <label><input type="radio" name="q1" value="c"> C) The objective is linear, the constraints are nonlinear</label>
                <label><input type="radio" name="q1" value="d"> D) Both the objective and constraints are nonlinear</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The objective and constraints are all linear functions</strong><br>
                Linear programming is defined by a linear objective with all constraints linear (affine).
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The standard form of an LP has:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Maximization, inequality constraints, free variables</label>
                <label><input type="radio" name="q2" value="b"> B) Minimization, equality constraints, nonnegative variables</label>
                <label><input type="radio" name="q2" value="c"> C) Maximization, equality constraints, nonnegative variables</label>
                <label><input type="radio" name="q2" value="d"> D) Minimization, inequality constraints, free variables</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Minimization, equality constraints, nonnegative variables</strong><br>
                Standard-form LP: minimize $$c^T x$$ subject to $$Ax = b$$, $$x \geq 0$$.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: Slack variables are used to:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Turn equality constraints into inequalities</label>
                <label><input type="radio" name="q3" value="b"> B) Turn inequality constraints into equalities</label>
                <label><input type="radio" name="q3" value="c"> C) Increase the number of variables</label>
                <label><input type="radio" name="q3" value="d"> D) Reduce the computational complexity</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Turn inequality constraints into equalities</strong><br>
                A slack variable turns $$Gx \leq h$$ into $$Gx + s = h$$ with $$s \geq 0$$.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The fundamental theorem of linear programming states that:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) The optimal solution is always unique</label>
                <label><input type="radio" name="q4" value="b"> B) If the LP has an optimal solution and the feasible region has a vertex, then there is always an optimal solution at a vertex</label>
                <label><input type="radio" name="q4" value="c"> C) The feasible region is always bounded</label>
                <label><input type="radio" name="q4" value="d"> D) The objective always has a global minimum</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) If the LP has an optimal solution and the feasible region has a vertex, then there is always an optimal solution at a vertex</strong><br>
                This is the basis of the Simplex algorithm: an optimal solution of an LP can always be found at a vertex.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The Simplex algorithm works by:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Searching randomly in the feasible region</label>
                <label><input type="radio" name="q5" value="b"> B) Moving from vertex to vertex to improve the objective</label>
                <label><input type="radio" name="q5" value="c"> C) Using gradient descent</label>
                <label><input type="radio" name="q5" value="d"> D) Bisecting the feasible region</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Moving from vertex to vertex to improve the objective</strong><br>
                Simplex starts at a vertex and moves to an adjacent vertex that improves the objective value.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: A quadratic program (QP) has an objective of the form:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) $$c^T x$$</label>
                <label><input type="radio" name="q6" value="b"> B) $$\frac{1}{2}x^T P x + q^T x + r$$</label>
                <label><input type="radio" name="q6" value="c"> C) $$\|Ax - b\|_2$$</label>
                <label><input type="radio" name="q6" value="d"> D) $$x^T A x^T$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\frac{1}{2}x^T P x + q^T x + r$$</strong><br>
                A QP has a convex quadratic objective with matrix $$P \in \mathbb{S}_+^n$$.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: In a QP, the matrix $$P$$ must satisfy:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) $$P$$ is symmetric</label>
                <label><input type="radio" name="q7" value="b"> B) $$P$$ is positive semidefinite</label>
                <label><input type="radio" name="q7" value="c"> C) $$P$$ is invertible</label>
                <label><input type="radio" name="q7" value="d"> D) $$P$$ is diagonal</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$P$$ is positive semidefinite</strong><br>
                The condition $$P \in \mathbb{S}_+^n$$ guarantees that the objective is convex.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: LP is a special case of QP when:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) $$P = I$$ (identity matrix)</label>
                <label><input type="radio" name="q8" value="b"> B) $$P = 0$$ (zero matrix)</label>
                <label><input type="radio" name="q8" value="c"> C) $$q = 0$$</label>
                <label><input type="radio" name="q8" value="d"> D) $$r = 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$P = 0$$ (zero matrix)</strong><br>
                When $$P = 0$$, the QP objective becomes $$q^T x + r$$, which is exactly an LP.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The linear least-squares problem has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) minimize $$\|Ax - b\|_1$$</label>
                <label><input type="radio" name="q9" value="b"> B) minimize $$\|Ax - b\|_2^2$$</label>
                <label><input type="radio" name="q9" value="c"> C) minimize $$\|Ax - b\|_\infty$$</label>
                <label><input type="radio" name="q9" value="d"> D) minimize $$x^T A x$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) minimize $$\|Ax - b\|_2^2$$</strong><br>
                The least-squares problem minimizes the sum of squared errors.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The solution of the least-squares problem is given by:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) $$x^* = A^{-1}b$$</label>
                <label><input type="radio" name="q10" value="b"> B) $$x^* = (A^T A)^{-1} A^T b$$</label>
                <label><input type="radio" name="q10" value="c"> C) $$x^* = A^T (AA^T)^{-1} b$$</label>
                <label><input type="radio" name="q10" value="d"> D) $$x^* = A^T b$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$x^* = (A^T A)^{-1} A^T b$$</strong><br>
                This is the closed-form solution of the normal equation $$A^T A x = A^T b$$ (when $$A$$ has full column rank).
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: In linear regression $$y = mx + c$$, the slope $$m$$ is computed as:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) $$\frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$$</label>
                <label><input type="radio" name="q11" value="b"> B) $$\frac{\sum (y_i - \bar{y})^2}{\sum (x_i - \bar{x})^2}$$</label>
                <label><input type="radio" name="q11" value="c"> C) $$\bar{y} - m\bar{x}$$</label>
                <label><input type="radio" name="q11" value="d"> D) $$\frac{\sum x_i y_i}{\sum x_i^2}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$$</strong><br>
                This is the standard formula for the slope in simple linear regression.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The Gauss-Markov assumptions do NOT include:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) The errors have zero mean</label>
                <label><input type="radio" name="q12" value="b"> B) The errors are uncorrelated</label>
                <label><input type="radio" name="q12" value="c"> C) Constant variance (homoscedasticity)</label>
                <label><input type="radio" name="q12" value="d"> D) Uniformly distributed errors</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) Uniformly distributed errors</strong><br>
                The Gauss-Markov assumptions only require errors with zero mean, no correlation and constant variance; they assume no particular distribution (normality is not needed, let alone uniformity). The normality assumption is only added for inference (tests, confidence intervals) or to make OLS coincide with MLE.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: Maximum likelihood estimation (MLE) in linear regression is equivalent to:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Maximizing the log-likelihood</label>
                <label><input type="radio" name="q13" value="b"> B) Minimizing the sum of squared errors</label>
                <label><input type="radio" name="q13" value="c"> C) Both A and B</label>
                <label><input type="radio" name="q13" value="d"> D) Maximizing R²</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Both A and B</strong><br>
                Under the Gaussian assumption, maximizing the log-likelihood is equivalent to minimizing the MSE.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: The diet problem is an example of:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Linear programming</label>
                <label><input type="radio" name="q14" value="b"> B) Quadratic programming</label>
                <label><input type="radio" name="q14" value="c"> C) Least squares</label>
                <label><input type="radio" name="q14" value="d"> D) Nonlinear programming</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Linear programming</strong><br>
                The diet problem has a linear objective and linear constraints.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: Portfolio optimization is an example of:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Linear programming</label>
                <label><input type="radio" name="q15" value="b"> B) Quadratic programming</label>
                <label><input type="radio" name="q15" value="c"> C) Least squares</label>
                <label><input type="radio" name="q15" value="d"> D) Integer programming</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Quadratic programming</strong><br>
                Portfolio optimization balances return (linear) and risk (quadratic).
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: The feasible region of an LP is called:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Ellipsoid</label>
                <label><input type="radio" name="q16" value="b"> B) A polytope (if bounded)</label>
                <label><input type="radio" name="q16" value="c"> C) Simplex</label>
                <label><input type="radio" name="q16" value="d"> D) Hyperplane</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) A polytope (if bounded)</strong><br>
                The feasible region of an LP is an intersection of halfspaces, forming a polytope if it is bounded.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: The optimality condition for the least-squares problem is:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) $$Ax = b$$</label>
                <label><input type="radio" name="q17" value="b"> B) $$A^T A x = A^T b$$</label>
                <label><input type="radio" name="q17" value="c"> C) $$A^T x = b$$</label>
                <label><input type="radio" name="q17" value="d"> D) $$x = 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$A^T A x = A^T b$$</strong><br>
                This is the normal equation, the necessary and sufficient condition for the least-squares problem.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: The coefficient of determination R² measures:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) The mean error</label>
                <label><input type="radio" name="q18" value="b"> B) The proportion of variance explained by the model</label>
                <label><input type="radio" name="q18" value="c"> C) The standard deviation</label>
                <label><input type="radio" name="q18" value="d"> D) The correlation coefficient</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The proportion of variance explained by the model</strong><br>
                R² = 1 - (SSres/SStot) tells what percentage of the variation in the data the model explains.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: The complexity of the Simplex algorithm is:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Polynomial</label>
                <label><input type="radio" name="q19" value="b"> B) Exponential in the worst case but efficient in practice</label>
                <label><input type="radio" name="q19" value="c"> C) Logarithmic</label>
                <label><input type="radio" name="q19" value="d"> D) Constant</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Exponential in the worst case but efficient in practice</strong><br>
                Simplex has exponential worst-case complexity (e.g. Klee-Minty), but in practice the number of iterations is usually only about 2-3 times the number of constraints.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: BLUE in linear regression stands for:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Best Linear Unbiased Estimator</label>
                <label><input type="radio" name="q20" value="b"> B) Basic Linear Uniform Estimation</label>
                <label><input type="radio" name="q20" value="c"> C) Bayesian Linear Update Equation</label>
                <label><input type="radio" name="q20" value="d"> D) Bounded Linear Uncertainty Estimate</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Best Linear Unbiased Estimator</strong><br>
                Under the Gauss-Markov assumptions, OLS gives the best linear unbiased estimator.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: The standard form of an LP is:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$\min c^T x$$ subject to $$Ax = b, x \geq 0$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$\min c^T x$$ subject to $$Ax \leq b$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$\max c^T x$$ subject to $$Ax \leq b$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$\min c^T x$$ subject to $$Ax \geq b$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\min c^T x$$ subject to $$Ax = b, x \geq 0$$</strong><br>
                The standard form of an LP is minimization with equality constraints and nonnegativity constraints.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: In an SOCP, the cone constraint has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$\|Ax + b\|_2 \leq c^T x + d$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$\|Ax + b\|_1 \leq c^T x + d$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$\|Ax + b\|_\infty \leq c^T x + d$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$(Ax + b)^2 \leq c^T x + d$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\|Ax + b\|_2 \leq c^T x + d$$</strong><br>
                SOCP uses second-order cone constraints with the Euclidean (L2) norm.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: An SDP has the constraint:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Positive semidefinite matrix</label>
                <label><input type="radio" name="q23" value="b"> B) Symmetric matrix</label>
                <label><input type="radio" name="q23" value="c"> C) Triangular matrix</label>
                <label><input type="radio" name="q23" value="d"> D) Diagonal matrix</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Positive semidefinite matrix</strong><br>
                An SDP constrains a matrix to be positive semidefinite: $$X \succeq 0$$.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: A resource allocation problem with 3 projects and a budget of 100 can be modeled as:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) LP</label>
                <label><input type="radio" name="q24" value="b"> B) QP</label>
                <label><input type="radio" name="q24" value="c"> C) SOCP</label>
                <label><input type="radio" name="q24" value="d"> D) SDP</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) LP</strong><br>
                A linear resource allocation problem is usually modeled by Linear Programming.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: In portfolio optimization, the objective is usually to:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Minimize risk (variance)</label>
                <label><input type="radio" name="q25" value="b"> B) Maximize return</label>
                <label><input type="radio" name="q25" value="c"> C) Balance risk and return</label>
                <label><input type="radio" name="q25" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above cases</strong><br>
                Portfolio optimization can minimize risk, maximize return, or balance both (the Markowitz model).
            </div>
        </div>

    </div>

    <div id="quiz-navigation">
        <button id="prev-btn" onclick="previousQuestion()" disabled>Previous</button>
        <button id="next-btn" onclick="nextQuestion()">Next</button>
        <button id="submit-btn" onclick="submitQuiz()" style="display: none;">Submit</button>
    </div>

    <div id="quiz-results" style="display: none;">
        <h3>Exercise Results</h3>
        <div id="score-display"></div>
        <div id="detailed-results"></div>
        <button onclick="restartQuiz()">Try again</button>
    </div>
</div>

<style>
#quiz-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

#quiz-header {
    text-align: center;
    margin-bottom: 30px;
}

#progress-bar {
    width: 100%;
    height: 10px;
    background-color: #e0e0e0;
    border-radius: 5px;
    margin: 20px 0;
    overflow: hidden;
}

#progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #FF6B35, #F7931E);
    width: 5%;
    transition: width 0.3s ease;
}

.question {
    background: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.question h3 {
    color: #333;
    margin-bottom: 20px;
    font-size: 1.1em;
    line-height: 1.4;
}

.options {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.options label {
    display: flex;
    align-items: flex-start;
    padding: 12px;
    background: white;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 1em;
    line-height: 1.4;
}

.options label:hover {
    border-color: #FF6B35;
    background-color: #fff5f0;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #FF6B35;
    background-color: #ffe5d6;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #fff5f0;
    border-left: 4px solid #FF6B35;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #D2691E;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #FF6B35;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #E55A2B;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #fff5f0;
    border-radius: 8px;
    border: 2px solid #FF6B35;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #D2691E;
}

#detailed-results {
    text-align: left;
    margin: 20px 0;
    max-height: 400px;
    overflow-y: auto;
}

.result-item {
    padding: 10px;
    margin: 5px 0;
    border-radius: 4px;
    border-left: 4px solid;
}

.result-item.correct {
    background-color: #e8f5e8;
    border-left-color: #4CAF50;
}

.result-item.incorrect {
    background-color: #ffebee;
    border-left-color: #f44336;
}

@media (max-width: 600px) {
    #quiz-container {
        padding: 10px;
    }
    
    .question {
        padding: 15px;
    }
    
    #quiz-navigation {
        flex-direction: column;
        gap: 10px;
    }
    
    #quiz-navigation button {
        width: 100%;
    }
}
</style>

<script>
let currentQuestion = 1;
const totalQuestions = 25;
let userAnswers = {};
let quizSubmitted = false;

// Correct answer for each question
const correctAnswers = {
    q1: 'a', q2: 'b', q3: 'b', q4: 'b', q5: 'b',
    q6: 'b', q7: 'b', q8: 'b', q9: 'b', q10: 'b',
    q11: 'a', q12: 'd', q13: 'c', q14: 'a', q15: 'b',
    q16: 'b', q17: 'b', q18: 'b', q19: 'b', q20: 'a'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'd'};

/**
 * Update the progress bar and show the current question
 */
function updateProgress() {
    const progressFill = document.getElementById('progress-fill');
    const progressText = document.getElementById('progress-text');
    
    const percentage = (currentQuestion / totalQuestions) * 100;
    progressFill.style.width = percentage + '%';
    progressText.textContent = `Question ${currentQuestion}/${totalQuestions}`;
}

/**
 * Show a question by its number
 */
function showQuestion(questionNum) {
    // Hide all questions
    for (let i = 1; i <= totalQuestions; i++) {
        document.getElementById(`q${i}`).style.display = 'none';
    }
    
    // Show the current question
    document.getElementById(`q${questionNum}`).style.display = 'block';
    
    // Update the state of the navigation buttons
    document.getElementById('prev-btn').disabled = (questionNum === 1);
    document.getElementById('next-btn').style.display = (questionNum === totalQuestions) ? 'none' : 'inline-block';
    document.getElementById('submit-btn').style.display = (questionNum === totalQuestions) ? 'inline-block' : 'none';
    
    updateProgress();
}

/**
 * Go to the next question
 */
function nextQuestion() {
    if (currentQuestion < totalQuestions) {
        currentQuestion++;
        showQuestion(currentQuestion);
    }
}

/**
 * Go back to the previous question
 */
function previousQuestion() {
    if (currentQuestion > 1) {
        currentQuestion--;
        showQuestion(currentQuestion);
    }
}

/**
 * Store the user's answer
 */
function saveAnswer(questionId, answer) {
    userAnswers[questionId] = answer;
    
    // Update the UI to show the selected answer
    const labels = document.querySelectorAll(`#${questionId} .options label`);
    labels.forEach(label => {
        label.classList.remove('selected');
        if (label.querySelector('input').value === answer) {
            label.classList.add('selected');
        }
    });
}

/**
 * Submit and show the results
 */
function submitQuiz() {
    if (quizSubmitted) return;
    
    quizSubmitted = true;
    let correctCount = 0;
    let detailedResults = '';
    
    // Compute the score and build the detailed report
    for (let i = 1; i <= totalQuestions; i++) {
        const questionId = `q${i}`;
        const userAnswer = userAnswers[questionId];
        const correctAnswer = correctAnswers[questionId];
        const isCorrect = userAnswer === correctAnswer;
        
        if (isCorrect) correctCount++;
        
        // Show explanations for all questions
        const explanation = document.querySelector(`#${questionId} .explanation`);
        if (explanation) {
            explanation.style.display = 'block';
        }
        
        // Build the detailed report
        detailedResults += `
            <div class="result-item ${isCorrect ? 'correct' : 'incorrect'}">
                <strong>Question ${i}:</strong> ${isCorrect ? 'Correct' : 'Incorrect'}
                ${!isCorrect ? `<br><small>Your answer: ${userAnswer || 'Not answered'} | Correct answer: ${correctAnswer}</small>` : ''}
            </div>
        `;
    }
    
    // Show the results
    const scorePercentage = Math.round((correctCount / totalQuestions) * 100);
    document.getElementById('score-display').innerHTML = `
        <div>Score: ${correctCount}/${totalQuestions} (${scorePercentage}%)</div>
        <div style="margin-top: 10px; font-size: 0.9em;">
            ${scorePercentage >= 80 ? '🎉 Excellent! You have mastered the canonical optimization problems!' :
              scorePercentage >= 60 ? '👍 Pretty good! Review a few concepts about LP and QP.' :
              scorePercentage >= 40 ? '📚 You need more review of the Simplex algorithm and least squares.' : '💪 Reread the theory of the basic optimization problems!'}
        </div>
    `;
    
    document.getElementById('detailed-results').innerHTML = detailedResults;
    document.getElementById('quiz-results').style.display = 'block';
    document.getElementById('quiz-navigation').style.display = 'none';
    
    // Scroll to the results
    document.getElementById('quiz-results').scrollIntoView({ behavior: 'smooth' });
}

/**
 * Restart the exercise
 */
function restartQuiz() {
    currentQuestion = 1;
    userAnswers = {};
    quizSubmitted = false;
    
    // Hide the results and show the navigation again
    document.getElementById('quiz-results').style.display = 'none';
    document.getElementById('quiz-navigation').style.display = 'flex';
    
    // Hide all explanations
    document.querySelectorAll('.explanation').forEach(exp => {
        exp.style.display = 'none';
    });
    
    // Clear all selections
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

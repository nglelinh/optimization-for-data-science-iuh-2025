---
layout: post
title: '04-09 Multiple-Choice Quiz - Convex Optimization Basics'
chapter: '04'
order: 10
owner: GitHub Copilot
lang: en
categories:
- chapter04
lesson_type: quiz
---

This multiple-choice quiz tests your understanding of the basic concepts of convex optimization, including terminology, optimality conditions and transformation techniques.

---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### 🎯 **The Convex Optimization Problem**

**Standard form:**
$$\begin{aligned}
&\min_{x \in D} &&f(x) \\
&\text{subject to} &&g_i(x) \le 0, \quad i = 1, \ldots, m \\
&&&h_j(x) = 0, \quad j = 1, \ldots, r
\end{aligned}$$

**Convexity conditions:**
- $$f, g_i$$ are convex functions
- $$h_j$$ are affine functions: $$h_j(x) = a_j^T x + b_j$$
- $$D = \text{dom}(f) \cap \bigcap_{i=1}^m \text{dom}(g_i) \cap \bigcap_{j=1}^r \text{dom}(h_j)$$

### 📝 **Basic Terminology**

**Key concepts:**
- **Objective function:** $$f(x)$$ - the function to minimize
- **Inequality constraints:** $$g_i(x) \le 0$$
- **Equality constraints:** $$h_j(x) = 0$$
- **Feasible point:** $$x$$ satisfying all the constraints
- **Optimal value:** $$f^* = \min\{f(x) \mid x \text{ feasible}\}$$
- **Optimal solution:** $$x^*$$ feasible with $$f(x^*) = f^*$$
- **$$\epsilon$$-suboptimal:** $$x$$ feasible with $$f(x) \le f^* + \epsilon$$
- **Active constraint:** $$g_i(x^*) = 0$$ at the optimal solution

**Feasible set:**
$$S = \{x \in D \mid g_i(x) \le 0, h_j(x) = 0\}$$

### 🔵 **Properties of the Solution Set**

**Property 1:** The solution set $$X_{\text{opt}}$$ of a convex problem is convex

**Proof:** If $$x, y \in X_{\text{opt}}$$ and $$0 \le \theta \le 1$$:
- $$\theta x + (1-\theta)y$$ is feasible (by convexity of the feasible set)
- $$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y) = f^*$$

**Property 2:** If $$f$$ is strictly convex then the solution (if it exists) is unique

### ✅ **Optimality Conditions**

**First-order condition (differentiable functions):**
For the problem $$\min_x f(x)$$ s.t. $$x \in C$$:
$$\nabla f(x^*)^T (y - x^*) \ge 0 \quad \forall y \in C$$

**Unconstrained case:** $$C = \mathbb{R}^n$$
$$\nabla f(x^*) = 0$$

**Second-order conditions (twice-differentiable functions):**
- **Necessary condition:** $$\nabla f(x^*) = 0$$ and $$\nabla^2 f(x^*) \succeq 0$$
- **Sufficient condition:** $$\nabla f(x^*) = 0$$ and $$\nabla^2 f(x^*) \succ 0$$

**Meaning of the Hessian:**
- $$\nabla^2 f(x^*) \succ 0$$: strict local minimum
- $$\nabla^2 f(x^*) \prec 0$$: strict local maximum
- $$\nabla^2 f(x^*)$$ indefinite: saddle point

### 🔄 **Slack Variables**

**Purpose:** Turn inequality constraints into equalities

**Transformation:**
$$g_i(x) \le 0 \quad \Rightarrow \quad g_i(x) + s_i = 0, \quad s_i \ge 0$$

**Original problem:**
$$\begin{aligned}
&\min_x &&f(x) \\
&\text{s.t.} &&g_i(x) \le 0
\end{aligned}$$

**With slack variables:**
$$\begin{aligned}
&\min_{x,s} &&f(x) \\
&\text{s.t.} &&g_i(x) + s_i = 0 \\
&&&s_i \ge 0
\end{aligned}$$

**Meaning:**
- $$s_i > 0$$: constraint $$i$$ is inactive
- $$s_i = 0$$: constraint $$i$$ is active (tight)

**Note:** Convexity is preserved only when $$g_i(x)$$ is affine

### 🔧 **Relaxation**

**Definition:** Replace the feasible set $$C$$ with a superset $$\tilde{C} \supseteq C$$

**Original problem:** $$\min_x f(x)$$ s.t. $$x \in C$$
**Relaxed problem:** $$\min_x f(x)$$ s.t. $$x \in \tilde{C}$$

**Property:** Optimal value of the relaxed problem $$\le$$ original optimal value

**Important example:** Relaxing equality constraints
$$h_j(x) = 0 \quad \Rightarrow \quad h_j(x) \le 0$$

**Application:** Turn a non-convex problem into a convex one (when $$h_j$$ is convex but not affine)

### 🎲 **Other Transformation Techniques**

**Eliminating equality constraints:**
If $$Ax = b$$ is solvable, we can parametrize:
$$x = x_0 + Fz$$ with $$Ax_0 = b$$ and $$\text{range}(F) = \text{null}(A)$$

**Change of variables:**
- Change variables to simplify the problem
- Convexity is preserved under affine transformations

**Decomposition:**
- Split a large problem into smaller subproblems
- Exploit the special structure of the problem

### 📊 **Comparison of Techniques**

| Technique | Purpose | Advantages | Disadvantages |
|----------|----------|---------|------------|
| **Slack variables** | Inequality → equality | Simplifies algorithms | More variables |
| **Relaxation** | Enlarge the feasible set | Non-convex → convex | The solution may be inexact |
| **Eliminating constraints** | Fewer constraints | Lower problem dimension | Requires special analysis |

### 🔍 **Recognizing Convex Problems**

**Checklist:**
- [ ] Is the objective $$f$$ convex?
- [ ] Are the inequality constraints $$g_i$$ convex?
- [ ] Are the equality constraints $$h_j$$ affine?
- [ ] Is the domain $$D$$ convex?

**If all ✓ → Convex optimization problem**

---

💡 **Tip:** In convex optimization every local minimum is a global minimum. This makes solving problems reliable and efficient!

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Multiple-Choice Quiz: Convex Optimization Basics</h2>
        <p>Choose the best answer for each question. The quiz focuses on basic and practical concepts of convex optimization.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Question 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Question 1 -->
        <div class="question" id="q1">
            <h3>Question 1: In a convex optimization problem, the equality constraint functions $$h_j(x) = 0$$ must be:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Convex functions</label>
                <label><input type="radio" name="q1" value="b"> B) Concave functions</label>
                <label><input type="radio" name="q1" value="c"> C) Affine functions</label>
                <label><input type="radio" name="q1" value="d"> D) Arbitrary functions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Affine function</strong><br>
                In a convex optimization problem, the equality constraint functions $$h_j(x) = 0$$ must be affine to guarantee that the feasible set is convex.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: A point $$x$$ is called feasible if:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) $$x \in D$$ and $$g_i(x) \leq 0$$ for all $$i$$</label>
                <label><input type="radio" name="q2" value="b"> B) $$x \in D$$, $$g_i(x) \leq 0$$ for all $$i$$, and $$h_j(x) = 0$$ for all $$j$$</label>
                <label><input type="radio" name="q2" value="c"> C) Only $$f(x)$$ needs to be defined</label>
                <label><input type="radio" name="q2" value="d"> D) $$x$$ is an optimal solution</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$x \in D$$, $$g_i(x) \leq 0$$ for all $$i$$, and $$h_j(x) = 0$$ for all $$j$$</strong><br>
                A feasible point must satisfy all the conditions: it lies in the domain and satisfies all the constraints.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: A constraint $$g_i(x) \leq 0$$ is called "active" at $$x$$ when:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$g_i(x) < 0$$</label>
                <label><input type="radio" name="q3" value="b"> B) $$g_i(x) = 0$$</label>
                <label><input type="radio" name="q3" value="c"> C) $$g_i(x) > 0$$</label>
                <label><input type="radio" name="q3" value="d"> D) $$g_i(x) \leq -1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$g_i(x) = 0$$</strong><br>
                An active constraint is satisfied with equality, i.e. $$g_i(x) = 0$$.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: A point $$x$$ is called $$\epsilon$$-suboptimal if:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$f(x) = f^* + \epsilon$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$f(x) \leq f^* + \epsilon$$</label>
                <label><input type="radio" name="q4" value="c"> C) $$f(x) \geq f^* - \epsilon$$</label>
                <label><input type="radio" name="q4" value="d"> D) $$|f(x) - f^*| \leq \epsilon$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$f(x) \leq f^* + \epsilon$$</strong><br>
                An $$\epsilon$$-suboptimal point has an objective value no larger than the optimal value plus $$\epsilon$$.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The solution set $$X_{opt}$$ of a convex optimization problem:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Is always convex</label>
                <label><input type="radio" name="q5" value="b"> B) May be non-convex</label>
                <label><input type="radio" name="q5" value="c"> C) Always contains exactly one point</label>
                <label><input type="radio" name="q5" value="d"> D) Is always empty</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Is always convex</strong><br>
                The solution set of a convex optimization problem is always convex; this is an important property.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: A convex optimization problem has a unique solution when:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) The objective $$f$$ is convex</label>
                <label><input type="radio" name="q6" value="b"> B) The objective $$f$$ is strictly convex</label>
                <label><input type="radio" name="q6" value="c"> C) The feasible set is bounded</label>
                <label><input type="radio" name="q6" value="d"> D) There are equality constraints</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The objective $$f$$ is strictly convex</strong><br>
                When the objective is strictly convex, the optimal solution (if it exists) is unique because the graph has no flat segments.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: For the problem $$\min_x f(x)$$ s.t. $$x \in C$$, the first-order optimality condition is:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) $$\nabla f(x) = 0$$</label>
                <label><input type="radio" name="q7" value="b"> B) $$\nabla f(x)^T(y-x) \geq 0$$ for all $$y \in C$$</label>
                <label><input type="radio" name="q7" value="c"> C) $$\nabla f(x)^T(y-x) \leq 0$$ for all $$y \in C$$</label>
                <label><input type="radio" name="q7" value="d"> D) $$f(x) \leq f(y)$$ for all $$y \in C$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\nabla f(x)^T(y-x) \geq 0$$ for all $$y \in C$$</strong><br>
                The first-order optimality condition requires that no feasible direction is a descent direction: $$-\nabla f(x)$$ must not point into the feasible set.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: For the unconstrained problem $$\min_x f(x)$$ ($$C = \mathbb{R}^n$$), the optimality condition is:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) $$\nabla f(x) = 0$$</label>
                <label><input type="radio" name="q8" value="b"> B) $$\nabla^2 f(x) \succ 0$$</label>
                <label><input type="radio" name="q8" value="c"> C) $$f(x) = 0$$</label>
                <label><input type="radio" name="q8" value="d"> D) $$x = 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\nabla f(x) = 0$$</strong><br>
                For an unconstrained problem, the first-order optimality condition becomes $$\nabla f(x) = 0$$.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The Hessian matrix $$\nabla^2 f(x)$$ gives information about:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) The slope of the function</label>
                <label><input type="radio" name="q9" value="b"> B) The curvature of the function</label>
                <label><input type="radio" name="q9" value="c"> C) The value of the function</label>
                <label><input type="radio" name="q9" value="d"> D) The domain of the function</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The curvature of the function</strong><br>
                The Hessian contains the second derivatives and gives information about the curvature of the function at a point.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: A sufficient condition for a strict local minimum is:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) $$\nabla f(x) = 0$$ and $$\nabla^2 f(x) \succeq 0$$</label>
                <label><input type="radio" name="q10" value="b"> B) $$\nabla f(x) = 0$$ and $$\nabla^2 f(x) \succ 0$$</label>
                <label><input type="radio" name="q10" value="c"> C) Only $$\nabla f(x) = 0$$</label>
                <label><input type="radio" name="q10" value="d"> D) $$\nabla^2 f(x) \prec 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\nabla f(x) = 0$$ and $$\nabla^2 f(x) \succ 0$$</strong><br>
                The sufficient condition for a strict local minimum requires a zero gradient and a positive definite Hessian.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: Slack variables $$s_i$$ are introduced in order to:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Turn inequality constraints into equalities</label>
                <label><input type="radio" name="q11" value="b"> B) Turn equality constraints into inequalities</label>
                <label><input type="radio" name="q11" value="c"> C) Increase the number of variables</label>
                <label><input type="radio" name="q11" value="d"> D) Reduce the computational complexity</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Turn inequality constraints into equalities</strong><br>
                Slack variables are used to transform $$g_i(x) \leq 0$$ into $$g_i(x) + s_i = 0$$ with $$s_i \geq 0$$.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: When $$s_i > 0$$ at the optimal solution, this means:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) The constraint $$g_i(x) \leq 0$$ is active</label>
                <label><input type="radio" name="q12" value="b"> B) The constraint $$g_i(x) \leq 0$$ is inactive</label>
                <label><input type="radio" name="q12" value="c"> C) The problem is infeasible</label>
                <label><input type="radio" name="q12" value="d"> D) The solution is not optimal</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The constraint $$g_i(x) \leq 0$$ is inactive</strong><br>
                When $$s_i > 0$$, we have $$g_i(x) = -s_i < 0$$, so the constraint is inactive (there is "slack").
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The slack-variable transformation preserves convexity when:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) $$g_i(x)$$ is any convex function</label>
                <label><input type="radio" name="q13" value="b"> B) $$g_i(x)$$ is an affine function</label>
                <label><input type="radio" name="q13" value="c"> C) $$g_i(x)$$ is a concave function</label>
                <label><input type="radio" name="q13" value="d"> D) It always preserves convexity</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$g_i(x)$$ is an affine function</strong><br>
                The slack-variable transformation preserves convexity only when $$g_i(x)$$ is affine. For nonlinear functions it can destroy convexity.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: Relaxation changes the set $$C$$ into $$\tilde{C}$$ such that:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) $$\tilde{C} \subseteq C$$</label>
                <label><input type="radio" name="q14" value="b"> B) $$\tilde{C} \supseteq C$$</label>
                <label><input type="radio" name="q14" value="c"> C) $$\tilde{C} = C$$</label>
                <label><input type="radio" name="q14" value="d"> D) $$\tilde{C} \cap C = \emptyset$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\tilde{C} \supseteq C$$</strong><br>
                Relaxation enlarges the feasible set, i.e. $$\tilde{C}$$ contains $$C$$ as a subset.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: After relaxation, the optimal value $$\tilde{f}^*$$ compared with the original value $$f^*$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) $$\tilde{f}^* \geq f^*$$</label>
                <label><input type="radio" name="q15" value="b"> B) $$\tilde{f}^* \leq f^*$$</label>
                <label><input type="radio" name="q15" value="c"> C) $$\tilde{f}^* = f^*$$</label>
                <label><input type="radio" name="q15" value="d"> D) There is no fixed relationship</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\tilde{f}^* \leq f^*$$</strong><br>
                Since we optimize over a larger set, the relaxed optimal value cannot be larger than the original one.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: Relaxing the equality constraint $$h_j(x) = 0$$ gives:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) $$h_j(x) \geq 0$$</label>
                <label><input type="radio" name="q16" value="b"> B) $$h_j(x) \leq 0$$</label>
                <label><input type="radio" name="q16" value="c"> C) $$|h_j(x)| \leq \epsilon$$</label>
                <label><input type="radio" name="q16" value="d"> D) Remove the constraint</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$h_j(x) \leq 0$$</strong><br>
                When $$h_j(x)$$ is convex but not affine, $$h_j(x) = 0$$ can be relaxed to $$h_j(x) \leq 0$$.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: The feasible set of a convex optimization problem:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Is always convex</label>
                <label><input type="radio" name="q17" value="b"> B) May be non-convex</label>
                <label><input type="radio" name="q17" value="c"> C) Is always bounded</label>
                <label><input type="radio" name="q17" value="d"> D) Is always nonempty</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Is always convex</strong><br>
                In a convex optimization problem, the feasible set is always convex because the constraints are convex and affine.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: In linear programming, a bounded feasible set is called:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Polyhedron</label>
                <label><input type="radio" name="q18" value="b"> B) Polytope</label>
                <label><input type="radio" name="q18" value="c"> C) Simplex</label>
                <label><input type="radio" name="q18" value="d"> D) Ellipsoid</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Polytope</strong><br>
                A polytope is a bounded feasible set in linear programming, whereas a polyhedron may be unbounded.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: In linear programming, if an optimal solution exists, it can be found at:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Any point of the feasible set</label>
                <label><input type="radio" name="q19" value="b"> B) The center of the feasible set</label>
                <label><input type="radio" name="q19" value="c"> C) One of the vertices of the feasible set</label>
                <label><input type="radio" name="q19" value="d"> D) The boundary of the feasible set</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) One of the vertices of the feasible set</strong><br>
                This is the basis of the Simplex algorithm: an optimal solution of an LP can always be found at a vertex.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: The main advantage of convex optimization problems is:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) They always have a unique solution</label>
                <label><input type="radio" name="q20" value="b"> B) Every local minimum is a global minimum</label>
                <label><input type="radio" name="q20" value="c"> C) They are faster to compute</label>
                <label><input type="radio" name="q20" value="d"> D) No optimality conditions are needed</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Every local minimum is a global minimum</strong><br>
                This is the most important property of convex optimization; it guarantees we do not get "stuck" at a local minimum.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: In a convex optimization problem, the KKT conditions are:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Sufficient for optimality, and also necessary when Slater's condition holds</label>
                <label><input type="radio" name="q21" value="b"> B) Only necessary</label>
                <label><input type="radio" name="q21" value="c"> C) Only sufficient</label>
                <label><input type="radio" name="q21" value="d"> D) Irrelevant</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Sufficient for optimality, and also necessary when Slater's condition holds</strong><br>
                For a convex optimization problem, the KKT conditions are always sufficient for global optimality; they are also necessary under a constraint qualification such as Slater's condition (then strong duality holds). Without Slater, an optimal solution may fail to satisfy KKT (e.g. $$\min x$$ subject to $$x^2 \leq 0$$).
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The solution of the problem $$\min x^2 + y^2$$ subject to $$x + y \geq 1$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$x = 0.5, y = 0.5$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$x = 1, y = 0$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$x = 0, y = 1$$</label>
                <label><input type="radio" name="q22" value="d"> D) No solution</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$x = 0.5, y = 0.5$$</strong><br>
                Using the Lagrange method with the active constraint $$x + y = 1$$, we get $$x = y = 0.5$$.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: The Lagrangian of the problem $$\min f(x)$$ subject to $$g(x) \leq 0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$L(x,\lambda) = f(x) + \lambda g(x)$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$L(x,\lambda) = f(x) - \lambda g(x)$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$L(x,\lambda) = f(x) + \lambda^2 g(x)$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$L(x,\lambda) = f(x) \cdot \lambda g(x)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$L(x,\lambda) = f(x) + \lambda g(x)$$</strong><br>
                The standard Lagrangian has the form $$L(x,\lambda) = f(x) + \lambda g(x)$$ with $$\lambda \geq 0$$.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The complementary slackness condition in KKT is:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$\lambda_i g_i(x) = 0$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$\lambda_i + g_i(x) = 0$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$\lambda_i - g_i(x) = 0$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$\lambda_i \cdot g_i(x) = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\lambda_i g_i(x) = 0$$</strong><br>
                Complementary slackness $$\lambda_i g_i(x) = 0$$ ensures that either the constraint is inactive or the Lagrange multiplier is zero.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: In the QP $$\min \frac{1}{2}x^T P x + q^T x$$, the matrix $$P$$ must be:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Positive semidefinite</label>
                <label><input type="radio" name="q25" value="b"> B) Positive definite</label>
                <label><input type="radio" name="q25" value="c"> C) Symmetric</label>
                <label><input type="radio" name="q25" value="d"> D) Both A and C</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) Both A and C</strong><br>
                For the QP to be convex, the matrix $$P$$ must be positive semidefinite and symmetric.
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
    background: linear-gradient(90deg, #E91E63, #9C27B0);
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
    border-color: #E91E63;
    background-color: #fce4ec;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #E91E63;
    background-color: #f8bbd9;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #fce4ec;
    border-left: 4px solid #E91E63;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #AD1457;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #E91E63;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #C2185B;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #fce4ec;
    border-radius: 8px;
    border: 2px solid #E91E63;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #AD1457;
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
    q1: 'c', q2: 'b', q3: 'b', q4: 'b', q5: 'a',
    q6: 'b', q7: 'b', q8: 'a', q9: 'b', q10: 'b',
    q11: 'a', q12: 'b', q13: 'b', q14: 'b', q15: 'b',
    q16: 'b', q17: 'a', q18: 'b', q19: 'c', q20: 'b'
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
            ${scorePercentage >= 80 ? '🎉 Excellent! You have mastered the basics of convex optimization!' :
              scorePercentage >= 60 ? '👍 Pretty good! Review a few basic concepts.' :
              scorePercentage >= 40 ? '📚 You need more review of terminology and optimality conditions.' : '💪 Reread the basic theory of convex optimization!'}
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

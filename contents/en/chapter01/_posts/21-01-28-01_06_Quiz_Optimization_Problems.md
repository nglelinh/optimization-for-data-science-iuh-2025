---
layout: post
title: '01-06 Multiple-Choice Quiz - Optimization Problems'
chapter: '01'
order: 7
owner: GitHub Copilot
lang: en
categories:
- chapter01
lesson_type: quiz
redirect_from:
  - /contents/en/chapter01/01_05_Quiz_Optimization_Problems/
---

This multiple-choice quiz tests your understanding of the basic concepts of optimization problems and convex optimization.

---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### 🎯 **The General Optimization Problem**

**Standard form:**
$$\begin{align*} 
&\min_{x\in D}\ &&f(x) \\
&\text{subject to} && g_i(x) \le 0,\ i = 1, ..., m \\
&&& h_j(x) = 0,\ j = 1,\ ..., r
\end{align*}$$

**Components:**
- $$x \in \mathbb{R}^n$$: optimization variable (decision variable)
- $$f(x)$$: objective function or cost function
- $$g_i(x) \le 0$$: inequality constraints
- $$h_j(x) = 0$$: equality constraints
- $$x^*$$: optimal solution

**Feasible region:**
$$D = \text{dom}(f) \cap \bigcap_{i=1}^m \text{dom}(g_i) \cap \bigcap_{j=1}^r \text{dom}(h_j)$$

### 🔵 **Convex Sets**

<div class="textbook-definition" markdown="1">
**Definition:**
A set $$C$$ is convex if for all $$x_1, x_2 \in C$$ and $$0 \le \theta \le 1$$:
$$\theta x_1 + (1-\theta)x_2 \in C$$
</div>

**Line segment:** $$x = \theta x_1 + (1 - \theta) x_2$$ with $$0 \le \theta \le 1$$

**Convex combination:**
$$x = \sum_{i=1}^k \theta_i x_i$$ with $$\sum_{i=1}^k \theta_i = 1, \theta_i \ge 0$$

### 📈 **Convex Functions**

<div class="textbook-definition" markdown="1">
**Definition:**
A function $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ is convex if:
1. $$\text{dom}(f)$$ is a convex set
2. $$f(\theta x + (1 - \theta)y) \le \theta f(x) + (1-\theta)f(y)$$
   for all $$x, y \in \text{dom}(f), 0 \le \theta \le 1$$
</div>

**Epigraph:**
$$\text{epi } f = \{(x, t) \in \mathbb{R}^{n+1} \mid x \in \text{dom } f, f(x) \le t\}$$

**Key property:** $$f$$ convex ⟺ $$\text{epi } f$$ is a convex set

### 🏆 **Convex Optimization Problems**

<div class="textbook-definition" markdown="1">
**Definition:**
An optimization problem is convex when:
- The objective function $$f$$ is convex
- The inequality constraint functions $$g_i$$ are convex
- The equality constraint functions $$h_j$$ are affine: $$h_j(x) = a_j^T x + b_j$$
</div>

**The golden property:**
> Every local minimum of a convex optimization problem is a global minimum

**Affine function:** $$f(x) = Ax + b$$ (linear + constant)

### 🔄 **Concave vs Convex Functions**

**Concave function:** $$f$$ concave ⟺ $$-f$$ convex
$$f(\theta x + (1 - \theta)y) \ge \theta f(x) + (1-\theta)f(y)$$

**Conversion:** Maximizing a concave function $$f$$ = Minimizing the convex function $$-f$$

### 🎯 **Course Goals**

1. **Recognize:** When is a problem a convex optimization problem?
2. **Formulate:** Turn real-world situations into convex optimization problems
3. **Choose:** The most suitable algorithm for each specific problem

### 🛠️ **Main Algorithms**

- **Gradient Descent:** First-order method
- **Newton Method:** Second-order method
- **Proximal Gradient:** For non-differentiable functions
- **ADMM:** For problems with special structure
- **Coordinate Descent:** Optimize one variable at a time

---

💡 **Tip:** Convex optimization has a wonderful property - there are no "spurious" local minima; every local solution is global!

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Multiple-Choice Quiz: Optimization Problems</h2>
        <p>Choose the best answer for each question. You will see your results as soon as you finish.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Question 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Question 1 -->
        <div class="question" id="q1">
            <h3>Question 1: In the standard form of an optimization problem, $$f(x)$$ is called:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Constraint function</label>
                <label><input type="radio" name="q1" value="b"> B) Objective function</label>
                <label><input type="radio" name="q1" value="c"> C) Optimization variable</label>
                <label><input type="radio" name="q1" value="d"> D) Feasible region</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Objective function</strong><br>
                In the optimization problem $$\min_{x\in D} f(x)$$, the function $$f(x)$$ is the objective function (or cost function) that we want to minimize.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: Consider the problem $$\min \log(x)$$. The constraint $$x > 0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) An explicit constraint</label>
                <label><input type="radio" name="q2" value="b"> B) An implicit constraint</label>
                <label><input type="radio" name="q2" value="c"> C) An equality constraint</label>
                <label><input type="radio" name="q2" value="d"> D) Not a constraint</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) An implicit constraint</strong><br>
                The constraint $$x > 0$$ comes from the domain of $$\log(x)$$ and is not stated directly in the problem, so it is called an implicit constraint.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: A set $$C$$ is called convex if:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) For all $$x_1, x_2 \in C$$ and $$0 \leq \theta \leq 1$$, we have $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q3" value="b"> B) The set $$C$$ is a disk</label>
                <label><input type="radio" name="q3" value="c"> C) The set $$C$$ has no holes</label>
                <label><input type="radio" name="q3" value="d"> D) The set $$C$$ is closed</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) For all $$x_1, x_2 \in C$$ and $$0 \leq \theta \leq 1$$, we have $$\theta x_1 + (1-\theta)x_2 \in C$$</strong><br>
                Definition of a convex set: the line segment joining any two points of the set lies entirely in the set.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: A function $$f$$ is convex if:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$f(\theta x + (1-\theta)y) \geq \theta f(x) + (1-\theta)f(y)$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$</label>
                <label><input type="radio" name="q4" value="c"> C) $$f(\theta x + (1-\theta)y) = \theta f(x) + (1-\theta)f(y)$$</label>
                <label><input type="radio" name="q4" value="d"> D) $$f$$ is a linear function</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$</strong><br>
                Definition of a convex function: the line segment joining any two points on the graph lies above the graph of the function.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: If $$f$$ is a concave function, then $$-f$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Concave</label>
                <label><input type="radio" name="q5" value="b"> B) Convex</label>
                <label><input type="radio" name="q5" value="c"> C) Linear</label>
                <label><input type="radio" name="q5" value="d"> D) Cannot be determined</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Convex</strong><br>
                By definition, $$f$$ is concave if and only if $$-f$$ is convex. This is how maximizing a concave function is turned into minimizing a convex function.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: The epigraph of a function $$f$$ is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) $$\{(x,t) : x \in \text{dom } f, f(x) \geq t\}$$</label>
                <label><input type="radio" name="q6" value="b"> B) $$\{(x,t) : x \in \text{dom } f, f(x) \leq t\}$$</label>
                <label><input type="radio" name="q6" value="c"> C) $$\{(x,t) : x \in \text{dom } f, f(x) = t\}$$</label>
                <label><input type="radio" name="q6" value="d"> D) $$\{x : x \in \text{dom } f\}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\{(x,t) : x \in \text{dom } f, f(x) \leq t\}$$</strong><br>
                The epigraph is the set of points lying above the graph of the function. "Epi" means "above".
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: A function $$f$$ is convex if and only if:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) The domain of $$f$$ is a convex set</label>
                <label><input type="radio" name="q7" value="b"> B) The epigraph of $$f$$ is a convex set</label>
                <label><input type="radio" name="q7" value="c"> C) The graph of $$f$$ is a convex set</label>
                <label><input type="radio" name="q7" value="d"> D) The hypograph of $$f$$ is a convex set</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The epigraph of $$f$$ is a convex set</strong><br>
                This is the key link between convex functions and convex sets: convex function ⟺ convex epigraph.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: For a convex function, a local optimum:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Is always a global optimum</label>
                <label><input type="radio" name="q8" value="b"> B) May not be a global optimum</label>
                <label><input type="radio" name="q8" value="c"> C) Does not exist</label>
                <label><input type="radio" name="q8" value="d"> D) Is always the unique point</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Is always a global optimum</strong><br>
                This is an important property of convex functions: every local optimum is a global optimum, which makes finding solutions easier.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: A convex combination of the points $$x_1, x_2, ..., x_k$$ has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) $$\sum_{i=1}^k \theta_i x_i$$ with $$\theta_i \geq 0$$</label>
                <label><input type="radio" name="q9" value="b"> B) $$\sum_{i=1}^k \theta_i x_i$$ with $$\sum_{i=1}^k \theta_i = 1$$</label>
                <label><input type="radio" name="q9" value="c"> C) $$\sum_{i=1}^k \theta_i x_i$$ with $$\theta_i \geq 0$$ and $$\sum_{i=1}^k \theta_i = 1$$</label>
                <label><input type="radio" name="q9" value="d"> D) $$\sum_{i=1}^k x_i$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) $$\sum_{i=1}^k \theta_i x_i$$ with $$\theta_i \geq 0$$ and $$\sum_{i=1}^k \theta_i = 1$$</strong><br>
                A convex combination requires nonnegative coefficients summing to 1, producing a "weighted average" of the points.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: In a convex optimization problem, the equality constraint functions $$h_j(x) = 0$$ must be:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Convex</label>
                <label><input type="radio" name="q10" value="b"> B) Concave</label>
                <label><input type="radio" name="q10" value="c"> C) Affine functions</label>
                <label><input type="radio" name="q10" value="d"> D) Arbitrary functions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Affine function</strong><br>
                In a convex optimization problem, the equality constraints must be affine: $$h_j(x) = a_j^T x + b_j$$.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: An affine function has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) $$e^{a^T x} + b$$</label>
                <label><input type="radio" name="q11" value="b"> B) $$ax^2 + bx + c$$</label>
                <label><input type="radio" name="q11" value="c"> C) $$a^T x + b$$</label>
                <label><input type="radio" name="q11" value="d"> D) $$\|x\|^2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) $$a^T x + b$$</strong><br>
                An affine function is a linear function plus a constant, with general form $$a^T x + b$$ in several dimensions.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: Which of the following sets is convex?</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) A disk</label>
                <label><input type="radio" name="q12" value="b"> B) A square</label>
                <label><input type="radio" name="q12" value="c"> C) A halfspace</label>
                <label><input type="radio" name="q12" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                A disk, a square and a halfspace are all examples of convex sets, because the segment joining any two points of the set lies entirely in the set.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: Which of the following functions is convex?</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) $$f(x) = x^2$$</label>
                <label><input type="radio" name="q13" value="b"> B) $$f(x) = |x|$$</label>
                <label><input type="radio" name="q13" value="c"> C) $$f(x) = e^x$$</label>
                <label><input type="radio" name="q13" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                $$x^2$$ (parabola), $$|x|$$ (absolute value), and $$e^x$$ (exponential) are all basic examples of convex functions.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: In machine learning, which of the following problems is usually solved by convex optimization?</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Training a neural network</label>
                <label><input type="radio" name="q14" value="b"> B) Linear regression</label>
                <label><input type="radio" name="q14" value="c"> C) Feature selection via the Lasso ($$\ell_1$$ penalty)</label>
                <label><input type="radio" name="q14" value="d"> D) Both B and C</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) Both B and C</strong><br>
                Linear regression and feature selection via the Lasso (a convex relaxation of subset selection) lead to convex optimization problems. Training a neural network is usually a non-convex problem.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: The feasible region of an optimization problem is:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) The set of all variables</label>
                <label><input type="radio" name="q15" value="b"> B) The set of points satisfying all the constraints</label>
                <label><input type="radio" name="q15" value="c"> C) The domain of the objective function</label>
                <label><input type="radio" name="q15" value="d"> D) The set of optimal solutions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The set of points satisfying all the constraints</strong><br>
                The feasible region is the set of all points $$x$$ satisfying the constraints $$g_i(x) \leq 0$$ and $$h_j(x) = 0$$.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: Who developed the Simplex algorithm, and in what year?</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) George Dantzig, 1947</label>
                <label><input type="radio" name="q16" value="b"> B) John von Neumann, 1944</label>
                <label><input type="radio" name="q16" value="c"> C) Leonid Kantorovich, 1939</label>
                <label><input type="radio" name="q16" value="d"> D) Narendra Karmarkar, 1984</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) George Dantzig, 1947</strong><br>
                George Dantzig developed the Simplex algorithm in 1947, revolutionizing practical optimization.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: In total variation denoising, the term $$\sum_{(i,j) \in E} |\theta_i - \theta_j|$$ serves to:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Increase the noise</label>
                <label><input type="radio" name="q17" value="b"> B) Smooth the image</label>
                <label><input type="radio" name="q17" value="c"> C) Increase the contrast</label>
                <label><input type="radio" name="q17" value="d"> D) Reduce the image size</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Smooth the image</strong><br>
                The total variation penalty encourages small changes between neighboring pixels, which smooths the image.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: In a convex optimization problem, the inequality constraint functions $$g_i(x) \leq 0$$ must be:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Convex</label>
                <label><input type="radio" name="q18" value="b"> B) Concave</label>
                <label><input type="radio" name="q18" value="c"> C) Linear</label>
                <label><input type="radio" name="q18" value="d"> D) Arbitrary functions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Convex</strong><br>
                In a convex optimization problem, the inequality constraint functions $$g_i(x) \leq 0$$ must be convex to guarantee that the feasible region is a convex set.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: The main advantage of convex optimization problems over non-convex ones is:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) They have more solutions</label>
                <label><input type="radio" name="q19" value="b"> B) There are no local minima (other than global minima)</label>
                <label><input type="radio" name="q19" value="c"> C) They are faster to compute</label>
                <label><input type="radio" name="q19" value="d"> D) They have wider applications</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) There are no local minima (other than global minima)</strong><br>
                The main advantage of convex optimization is that every local minimum is a global minimum, which avoids getting "stuck" at a local minimum.
            </div>
        </div>

        <!-- Question 20: Real-world applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: Which of the following is NOT a main application of convex optimization?</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Signal processing</label>
                <label><input type="radio" name="q20" value="b"> B) Circuit design</label>
                <label><input type="radio" name="q20" value="c"> C) Video games</label>
                <label><input type="radio" name="q20" value="d"> D) Finance</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Video games</strong><br>
                Although optimization can be used in video games, signal processing, circuit design and finance are the main and more traditional applications of convex optimization.
            </div>
        </div>

        <!-- Question 21 -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: Consider minimizing $$f(x) = x^2 + 4x + 3$$. The optimal value is:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$-1$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$0$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$3$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$-2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$-1$$</strong><br>
                $$f'(x) = 2x + 4 = 0 \Rightarrow x = -2$$<br>
                $$f(-2) = (-2)^2 + 4(-2) + 3 = 4 - 8 + 3 = -1$$
            </div>
        </div>

        <!-- Question 22 -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: Is the function $$f(x) = |x|$$ convex?</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Yes, because $$f''(x) \geq 0$$ everywhere</label>
                <label><input type="radio" name="q22" value="b"> B) Yes, by the definition of a convex function</label>
                <label><input type="radio" name="q22" value="c"> C) No, because it is not differentiable at $$x = 0$$</label>
                <label><input type="radio" name="q22" value="d"> D) No, because the graph has a sharp corner</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Yes, by the definition of a convex function</strong><br>
                The function $$|x|$$ satisfies $$|tx + (1-t)y| \leq t|x| + (1-t)|y|$$ for all $$t \in [0,1]$$. Non-differentiability at one point does not affect convexity.
            </div>
        </div>

        <!-- Question 23 -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: In a budget allocation problem with $$x_1 + x_2 + x_3 = 100$$ and $$x_i \geq 0$$, how many constraints are there?</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) 1 equality constraint, 3 inequality constraints</label>
                <label><input type="radio" name="q23" value="b"> B) 4 equality constraints</label>
                <label><input type="radio" name="q23" value="c"> C) 3 inequality constraints</label>
                <label><input type="radio" name="q23" value="d"> D) 1 equality constraint</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) 1 equality constraint, 3 inequality constraints</strong><br>
                There is 1 equality constraint $$x_1 + x_2 + x_3 = 100$$ and 3 inequality constraints $$x_1 \geq 0, x_2 \geq 0, x_3 \geq 0$$.
            </div>
        </div>

        <!-- Question 24 -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The feasible region of the problem $$\min x^2 + y^2$$ subject to $$x + y = 1, x \geq 0, y \geq 0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) The line segment from $$(0,1)$$ to $$(1,0)$$</label>
                <label><input type="radio" name="q24" value="b"> B) The triangle with vertices $$(0,0), (0,1), (1,0)$$</label>
                <label><input type="radio" name="q24" value="c"> C) The unit circle</label>
                <label><input type="radio" name="q24" value="d"> D) The whole plane</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The line segment from $$(0,1)$$ to $$(1,0)$$</strong><br>
                The constraint $$x + y = 1$$ gives a line; combined with $$x \geq 0, y \geq 0$$ we get a line segment in the first quadrant.
            </div>
        </div>

        <!-- Question 25 -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: The solution of the problem $$\min x^2 + y^2$$ subject to $$x + y = 1$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$x = 0.5, y = 0.5$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$x = 1, y = 0$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$x = 0, y = 1$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$x = 1, y = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$x = 0.5, y = 0.5$$</strong><br>
                Use the Lagrange method or substitute $$y = 1-x$$ into the objective:<br>
                $$\min x^2 + (1-x)^2 = 2x^2 - 2x + 1$$<br>
                $$\frac{d}{dx}(2x^2 - 2x + 1) = 4x - 2 = 0 \Rightarrow x = 0.5, y = 0.5$$
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
    background-color: #ffe8e0;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #e8f4fd;
    border-left: 4px solid #2196F3;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #1976D2;
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
    background: #e55a2b;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #f0f8f0;
    border-radius: 8px;
    border: 2px solid #FF6B35;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #d84315;
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
    q1: 'b', q2: 'b', q3: 'a', q4: 'b', q5: 'b',
    q6: 'b', q7: 'b', q8: 'a', q9: 'c', q10: 'c',
    q11: 'c', q12: 'd', q13: 'd', q14: 'd', q15: 'b',
    q16: 'a', q17: 'b', q18: 'a', q19: 'b', q20: 'c',
    q21: 'a', q22: 'b', q23: 'a', q24: 'a', q25: 'a'
};

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
            ${scorePercentage >= 80 ? '🎉 Excellent! You have mastered the basic concepts!' :
              scorePercentage >= 60 ? '👍 Pretty good! Review a few concepts.' :
              scorePercentage >= 40 ? '📚 You need more review of convex optimization.' : '💪 Reread the theory and try again!'}
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

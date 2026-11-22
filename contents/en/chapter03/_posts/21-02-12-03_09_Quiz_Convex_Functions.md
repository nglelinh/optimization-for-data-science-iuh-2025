---
layout: post
title: '03-09 Multiple-Choice Quiz - Convex Functions'
chapter: '03'
order: 17
owner: GitHub Copilot
lang: en
categories:
- chapter03
lesson_type: quiz
redirect_from:
  - /contents/en/chapter03/03_08_Quiz_Convex_Functions/
---

This multiple-choice quiz tests your understanding of convex functions, their basic properties, convexity-preserving operations and conjugate functions.

---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### 📈 **Definition of Convex Functions**

**Convex function:**
A function $$f: \mathbb{R}^n \to \mathbb{R}$$ is convex if:
1. $$\text{dom}(f)$$ is a convex set
2. $$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$$
   for all $$x, y \in \text{dom}(f), 0 \le \theta \le 1$$

**Types of convex functions:**
- **Strictly convex:** $$f(\theta x + (1-\theta)y) < \theta f(x) + (1-\theta)f(y)$$ for $$x \neq y, 0 < \theta < 1$$
- **Strongly convex:** $$f - \frac{m}{2}\lVert x \rVert_2^2$$ is convex for some $$m > 0$$
- **Concave function:** $$f$$ is concave ⟺ $$-f$$ is convex

**Relation:** Strongly convex ⟹ Strictly convex ⟹ Convex

### 🔢 **Important Examples**

**Functions of one variable:**
- Exponential: $$e^{ax}$$ is convex for every $$a \in \mathbb{R}$$
- Power: $$x^a$$ is convex on $$\mathbb{R}_+$$ when $$a \ge 1$$ or $$a \le 0$$
- Power: $$x^a$$ is concave on $$\mathbb{R}_+$$ when $$0 \le a \le 1$$

**Functions of several variables:**
- Affine function: $$a^T x + b$$ is both convex and concave
- Quadratic function: $$\frac{1}{2}x^T P x + q^T x + r$$ is convex when $$P \succeq 0$$
- Norms: $$\lVert x \rVert_p$$ is convex for every $$p \ge 1$$
- Squared loss: $$\lVert Ax - b \rVert_2^2$$ is always convex

**Special functions:**
- Indicator function: $$I_C(x) = \begin{cases} 0 & x \in C \\ +\infty & x \notin C \end{cases}$$ is convex if $$C$$ is convex
- Support function: $$I_C^*(x) = \max_{y \in C} x^T y$$ is always convex
- Max function: $$\max\{f_1(x), \ldots, f_m(x)\}$$ is convex if the $$f_i$$ are convex

### 🔍 **Characterizing Properties**

**Epigraph characterization:**
$$f$$ convex ⟺ $$\text{epi}(f) = \{(x,t) \mid x \in \text{dom}(f), f(x) \le t\}$$ is a convex set

**Sublevel sets:**
If $$f$$ is convex then $$\{x \mid f(x) \le \alpha\}$$ is convex for every $$\alpha$$

**First-order characterization (differentiable functions):**
$$f$$ is convex ⟺ $$f(y) \ge f(x) + \nabla f(x)^T (y-x)$$ for all $$x,y$$
(The function lies above its tangent lines)

**Second-order characterization (twice-differentiable functions):**
$$f$$ convex ⟺ $$\nabla^2 f(x) \succeq 0$$ for all $$x$$ (positive semidefinite Hessian, with $$\text{dom}(f)$$ convex)

### 🔄 **Operations that Preserve Convexity**

**Linear combination:**
- $$\alpha f$$ is convex if $$f$$ is convex and $$\alpha \ge 0$$
- $$f_1 + f_2$$ is convex if $$f_1, f_2$$ are convex
- $$\sum_{i=1}^m \alpha_i f_i$$ is convex if the $$f_i$$ are convex and $$\alpha_i \ge 0$$

**Affine composition:**
$$f(Ax + b)$$ is convex if $$f$$ is convex

**General composition:** $$h(g(x))$$ is convex if:
- $$g$$ is convex, $$h$$ is convex and nondecreasing
- $$g$$ is concave, $$h$$ is convex and nonincreasing

**Pointwise maximum:**
- $$\max\{f_1(x), f_2(x)\}$$ is convex if $$f_1, f_2$$ are convex
- $$\sup_{y \in A} f(x,y)$$ is convex in $$x$$ if $$f(x,y)$$ is convex in $$x$$ for every $$y$$

**Perspective transformation:**
$$g(x,t) = tf(\frac{x}{t})$$ is convex if $$f$$ is convex, for $$t > 0$$

### ⭐ **Conjugate Functions**

<div class="textbook-definition" markdown="1">
**Definition:**
$$f^*(y) = \sup_{x \in \text{dom}(f)} \{y^T x - f(x)\}$$
</div>

**Key properties:**
- $$f^*$$ is always convex (whether or not $$f$$ is convex)
- Fenchel's inequality: $$f(x) + f^*(y) \ge x^T y$$
- If $$f$$ is closed and convex: $$f^{**} = f$$

**Examples:**
- $$f(x) = \frac{1}{2}x^T Q x \Rightarrow f^*(y) = \frac{1}{2}y^T Q^{-1} y$$ ($$Q \succ 0$$)
- $$f(x) = \lvert x \rvert \Rightarrow f^*(y) = \begin{cases} 0 & \lvert y \rvert \le 1 \\ +\infty & \lvert y \rvert > 1 \end{cases}$$
- $$f(x) = e^x \Rightarrow f^*(y) = \begin{cases} y \log y - y & y > 0 \\ 0 & y = 0 \\ +\infty & y < 0 \end{cases}$$

### 📊 **Jensen's Inequality**

**General form:**
If $$f$$ is convex and $$\sum_{i=1}^n w_i = 1, w_i \ge 0$$:
$$f\left(\sum_{i=1}^n w_i x_i\right) \le \sum_{i=1}^n w_i f(x_i)$$

**Probabilistic form:**
If $$X$$ is a random variable: $$f(E[X]) \le E[f(X)]$$

---

💡 **Tip:** Convex functions "curve upward" - the chord joining any 2 points on the graph always lies above the graph. This makes optimization much easier!

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Multiple-Choice Quiz: Convex Functions</h2>
        <p>Choose the best answer for each question. The quiz focuses on the basic concepts of convex functions and related operations.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Question 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Question 1 -->
        <div class="question" id="q1">
            <h3>Question 1: A function $$f: \mathbb{R}^n \to \mathbb{R}$$ is convex if:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) The domain is a convex set and $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$</label>
                <label><input type="radio" name="q1" value="b"> B) Only $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$ is needed</label>
                <label><input type="radio" name="q1" value="c"> C) The domain is a convex set and the function is differentiable</label>
                <label><input type="radio" name="q1" value="d"> D) The function is continuous on its domain</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The domain is a convex set and $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$</strong><br>
                The definition of a convex function requires both conditions: the domain must be a convex set and Jensen's inequality must hold for $$0 \leq \theta \leq 1$$.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: How does a strictly convex function differ from a convex function?</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) It uses the strict inequality $$<$$ instead of $$\leq$$</label>
                <label><input type="radio" name="q2" value="b"> B) It only applies for $$0 < \theta < 1$$ and $$x \neq y$$</label>
                <label><input type="radio" name="q2" value="c"> C) Both A and B are correct</label>
                <label><input type="radio" name="q2" value="d"> D) There is no difference</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Both A and B are correct</strong><br>
                A strictly convex function requires $$f(\theta x + (1-\theta)y) < \theta f(x) + (1-\theta)f(y)$$ for $$0 < \theta < 1$$ and $$x \neq y$$.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: The relation between the types of convex functions is:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Strongly convex ⇒ Strictly convex ⇒ Convex</label>
                <label><input type="radio" name="q3" value="b"> B) Convex ⇒ Strictly convex ⇒ Strongly convex</label>
                <label><input type="radio" name="q3" value="c"> C) Strictly convex ⇒ Strongly convex ⇒ Convex</label>
                <label><input type="radio" name="q3" value="d"> D) They are all equivalent</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Strongly convex ⇒ Strictly convex ⇒ Convex</strong><br>
                This is the order from strongest to weakest: strong convexity is the strongest condition, then strict convexity, and finally convexity.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The affine function $$f(x) = a^T x + b$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Convex only</label>
                <label><input type="radio" name="q4" value="b"> B) Concave only</label>
                <label><input type="radio" name="q4" value="c"> C) Both convex and concave</label>
                <label><input type="radio" name="q4" value="d"> D) Neither convex nor concave</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Both convex and concave</strong><br>
                An affine function satisfies $$f(\theta x + (1-\theta)y) = \theta f(x) + (1-\theta)f(y)$$ (with equality), so it is both convex and concave.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The function $$f(x) = e^{ax}$$ with $$a \in \mathbb{R}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Convex for every $$a$$</label>
                <label><input type="radio" name="q5" value="b"> B) Convex only when $$a > 0$$</label>
                <label><input type="radio" name="q5" value="c"> C) Concave for every $$a$$</label>
                <label><input type="radio" name="q5" value="d"> D) Depends on the sign of $$a$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Convex for every $$a$$</strong><br>
                The exponential $$e^{ax}$$ is convex for every real value of $$a$$, including negative, zero and positive $$a$$.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: On $$\mathbb{R}_+$$, the function $$f(x) = x^a$$ is convex when:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) $$a \geq 1$$ or $$a \leq 0$$</label>
                <label><input type="radio" name="q6" value="b"> B) $$0 \leq a \leq 1$$</label>
                <label><input type="radio" name="q6" value="c"> C) $$a > 0$$</label>
                <label><input type="radio" name="q6" value="d"> D) For every $$a$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$a \geq 1$$ or $$a \leq 0$$</strong><br>
                The function $$x^a$$ is convex on $$\mathbb{R}_+$$ when $$a \geq 1$$ or $$a \leq 0$$, and concave when $$0 \leq a \leq 1$$.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: The quadratic function $$f(x) = \frac{1}{2}x^T P x + q^T x + r$$ is convex when:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) $$P$$ is positive definite</label>
                <label><input type="radio" name="q7" value="b"> B) $$P$$ is positive semidefinite</label>
                <label><input type="radio" name="q7" value="c"> C) $$P$$ is symmetric</label>
                <label><input type="radio" name="q7" value="d"> D) $$P$$ is invertible</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$P$$ is positive semidefinite</strong><br>
                A quadratic function is convex when its Hessian $$P$$ is positive semidefinite ($$P \succeq 0$$).
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: All norms on $$\mathbb{R}^n$$ are:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Convex</label>
                <label><input type="radio" name="q8" value="b"> B) Concave</label>
                <label><input type="radio" name="q8" value="c"> C) Both convex and concave</label>
                <label><input type="radio" name="q8" value="d"> D) Depends on the type of norm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Convex</strong><br>
                By definition, every norm satisfies the triangle inequality (and homogeneity), which implies convexity.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: If $$f_1, f_2, ..., f_n$$ are convex functions, then $$\sum_{i=1}^n \alpha_i f_i$$ is convex when:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) $$\alpha_i \geq 0$$ for all $$i$$</label>
                <label><input type="radio" name="q9" value="b"> B) $$\sum_{i=1}^n \alpha_i = 1$$</label>
                <label><input type="radio" name="q9" value="c"> C) $$\alpha_i > 0$$ for all $$i$$</label>
                <label><input type="radio" name="q9" value="d"> D) For all $$\alpha_i \in \mathbb{R}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\alpha_i \geq 0$$ for all $$i$$</strong><br>
                A nonnegative weighted sum of convex functions is still convex. The condition $$\sum \alpha_i = 1$$ is not needed.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: If $$f$$ is a convex function, then $$g(x) = f(Ax + b)$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Always convex</label>
                <label><input type="radio" name="q10" value="b"> B) Convex only if $$A$$ is invertible</label>
                <label><input type="radio" name="q10" value="c"> C) Convex only if $$A$$ is square</label>
                <label><input type="radio" name="q10" value="d"> D) Not necessarily convex</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Always convex</strong><br>
                Composition of a convex function with an affine map always preserves convexity, whatever the properties of $$A$$.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: Let $$g$$ be convex and $$h$$ convex and nondecreasing. The function $$f(x) = h(g(x))$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Convex</label>
                <label><input type="radio" name="q11" value="b"> B) Concave</label>
                <label><input type="radio" name="q11" value="c"> C) Cannot be determined</label>
                <label><input type="radio" name="q11" value="d"> D) Both convex and concave</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Convex</strong><br>
                When $$g$$ is convex and $$h$$ is convex and nondecreasing, the composition $$h(g(x))$$ is convex.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: If $$f_1, f_2$$ are convex functions, then $$f(x) = \max\{f_1(x), f_2(x)\}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Convex</label>
                <label><input type="radio" name="q12" value="b"> B) Concave</label>
                <label><input type="radio" name="q12" value="c"> C) Neither convex nor concave</label>
                <label><input type="radio" name="q12" value="d"> D) Depends on $$f_1, f_2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Convex</strong><br>
                The pointwise maximum of convex functions is always convex. This is an important convexity-preserving property.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The conjugate function $$f^*(y) = \sup_x \{y^T x - f(x)\}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Always convex, whether or not $$f$$ is convex</label>
                <label><input type="radio" name="q13" value="b"> B) Convex only if $$f$$ is convex</label>
                <label><input type="radio" name="q13" value="c"> C) Has the same convexity as $$f$$</label>
                <label><input type="radio" name="q13" value="d"> D) Always concave</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Always convex, whether or not $$f$$ is convex</strong><br>
                The conjugate is always convex because it is a supremum of functions $$y^T x - f(x)$$ that are affine in $$y$$.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: Fenchel's inequality states that:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) $$f(x) + f^*(y) \geq x^T y$$</label>
                <label><input type="radio" name="q14" value="b"> B) $$f(x) + f^*(y) \leq x^T y$$</label>
                <label><input type="radio" name="q14" value="c"> C) $$f(x) \cdot f^*(y) \geq x^T y$$</label>
                <label><input type="radio" name="q14" value="d"> D) $$f(x) = f^*(y) + x^T y$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f(x) + f^*(y) \geq x^T y$$</strong><br>
                Fenchel's inequality is a basic inequality in the theory of conjugate functions.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: For a closed convex function $$f$$, the biconjugate $$f^{**}$$ satisfies:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) $$f^{**} = f$$</label>
                <label><input type="radio" name="q15" value="b"> B) $$f^{**} \leq f$$</label>
                <label><input type="radio" name="q15" value="c"> C) $$f^{**} \geq f$$</label>
                <label><input type="radio" name="q15" value="d"> D) There is no fixed relationship</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$f^{**} = f$$</strong><br>
                For a closed convex function, the biconjugate equals the original function. This is the Fenchel-Moreau theorem.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: The conjugate of $$f(x) = |x|$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) The indicator function of $$[-1,1]$$</label>
                <label><input type="radio" name="q16" value="b"> B) $$|y|$$</label>
                <label><input type="radio" name="q16" value="c"> C) $$y^2/2$$</label>
                <label><input type="radio" name="q16" value="d"> D) $$\log|y|$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The indicator function of $$[-1,1]$$</strong><br>
                The conjugate of $$|x|$$ is $$f^*(y) = 0$$ if $$|y| \leq 1$$ and $$+\infty$$ if $$|y| > 1$$.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: The indicator function $$I_C(x)$$ of a convex set $$C$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Convex</label>
                <label><input type="radio" name="q17" value="b"> B) Concave</label>
                <label><input type="radio" name="q17" value="c"> C) Neither convex nor concave</label>
                <label><input type="radio" name="q17" value="d"> D) Depends on the set $$C$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Convex</strong><br>
                The indicator function of a convex set is always convex: $$I_C(x) = 0$$ if $$x \in C$$, $$+\infty$$ if $$x \notin C$$.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: The support function $$S_C(x) = \max_{y \in C} x^T y$$ of a set $$C$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Convex whether or not $$C$$ is convex</label>
                <label><input type="radio" name="q18" value="b"> B) Convex only if $$C$$ is convex</label>
                <label><input type="radio" name="q18" value="c"> C) Concave whether or not $$C$$ is convex</label>
                <label><input type="radio" name="q18" value="d"> D) Has the same convexity as $$C$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Convex whether or not $$C$$ is convex</strong><br>
                The support function is always convex because it is a supremum of the linear functions $$x^T y$$.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: The function $$f(x) = \|Ax - b\|_2^2$$ for an arbitrary matrix $$A$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Always convex</label>
                <label><input type="radio" name="q19" value="b"> B) Convex only if $$A$$ is square</label>
                <label><input type="radio" name="q19" value="c"> C) Convex only if $$A$$ is invertible</label>
                <label><input type="radio" name="q19" value="d"> D) Not necessarily convex</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Always convex</strong><br>
                Since $$A^T A$$ is positive semidefinite for every matrix $$A$$, $$\|Ax - b\|_2^2$$ is always convex.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: Why is recognizing convex functions important in optimization?</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Every local minimum is a global minimum</label>
                <label><input type="radio" name="q20" value="b"> B) There are many efficient algorithms</label>
                <label><input type="radio" name="q20" value="c"> C) Duality theory applies</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above reasons</strong><br>
                Convex functions have many good properties: local minimum = global minimum, efficient algorithms exist, and duality theory is strong.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: Consider $$f(x) = e^x$$. Is this function convex?</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Yes, because $$f''(x) = e^x > 0$$</label>
                <label><input type="radio" name="q21" value="b"> B) No, because it grows too fast</label>
                <label><input type="radio" name="q21" value="c"> C) Convex only on $$(0, \infty)$$</label>
                <label><input type="radio" name="q21" value="d"> D) Cannot be determined</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Yes, because $$f''(x) = e^x > 0$$</strong><br>
                $$f'(x) = e^x$$, $$f''(x) = e^x > 0$$ for all $$x$$, so the function is convex on all of $$\mathbb{R}$$.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: Is the function $$g(x) = \max\{x, 0\}$$ (ReLU) convex?</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Yes, by the definition of a convex function</label>
                <label><input type="radio" name="q22" value="b"> B) No, because it is not differentiable at $$x = 0$$</label>
                <label><input type="radio" name="q22" value="c"> C) Convex only on $$[0, \infty)$$</label>
                <label><input type="radio" name="q22" value="d"> D) No, because it has a sharp corner</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Yes, by the definition of a convex function</strong><br>
                The ReLU function satisfies the definition of a convex function. Non-differentiability at one point does not affect convexity.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: Let $$f(x,y) = x^2 + y^2$$. The Hessian matrix of $$f$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$\begin{pmatrix} 2x & 0 \\ 0 & 2y \end{pmatrix}$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$\begin{pmatrix} x & y \\ y & x \end{pmatrix}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$</strong><br>
                $$\frac{\partial^2 f}{\partial x^2} = 2$$, $$\frac{\partial^2 f}{\partial y^2} = 2$$, $$\frac{\partial^2 f}{\partial x \partial y} = 0$$
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The sum of two convex functions $$f$$ and $$g$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Always convex</label>
                <label><input type="radio" name="q24" value="b"> B) May or may not be convex</label>
                <label><input type="radio" name="q24" value="c"> C) Always concave</label>
                <label><input type="radio" name="q24" value="d"> D) Depends on the domain</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Always convex</strong><br>
                The sum of two convex functions is always convex. This is one of the convexity-preserving operations.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: What property does $$h(x) = |x|^p$$ with $$p \geq 1$$ have?</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Convex on $$\mathbb{R}$$</label>
                <label><input type="radio" name="q25" value="b"> B) Concave on $$\mathbb{R}$$</label>
                <label><input type="radio" name="q25" value="c"> C) Convex only when $$p = 2$$</label>
                <label><input type="radio" name="q25" value="d"> D) Neither convex nor concave</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Convex on $$\mathbb{R}$$</strong><br>
                For $$p \geq 1$$, the function $$|x|^p$$ is convex on all of $$\mathbb{R}$$. This is an important example of a convex function.
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
    background: linear-gradient(90deg, #00BCD4, #009688);
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
    border-color: #00BCD4;
    background-color: #e0f2f1;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #00BCD4;
    background-color: #b2dfdb;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #e0f2f1;
    border-left: 4px solid #00BCD4;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #00695C;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #00BCD4;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #00ACC1;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #e0f2f1;
    border-radius: 8px;
    border: 2px solid #00BCD4;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #00695C;
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
    q1: 'a', q2: 'c', q3: 'a', q4: 'c', q5: 'a',
    q6: 'a', q7: 'b', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'a', q17: 'a', q18: 'a', q19: 'a', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'a'};

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
            ${scorePercentage >= 80 ? '🎉 Excellent! You have mastered the theory of convex functions!' :
              scorePercentage >= 60 ? '👍 Pretty good! Review a few concepts about convex functions.' :
              scorePercentage >= 40 ? '📚 You need more review of the definitions and properties of convex functions.' : '💪 Reread the theory of convex functions and their operations!'}
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

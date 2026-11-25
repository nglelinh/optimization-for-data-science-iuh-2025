---
layout: post
title: '07-09 Multiple-Choice Quiz - Subgradient'
chapter: '07'
order: 13
owner: GitHub Copilot
lang: en
categories:
- chapter07
lesson_type: quiz
redirect_from:
  - /contents/en/chapter07/07_08_Quiz_Subgradient/
---

Working with sets of slopes instead of single numbers requires a subtle shift in intuition: addition becomes Minkowski set addition, gradients become convex hulls of active branches, and $$f'(x^\star) = 0$$ becomes set membership $$0 \in \partial f(x^\star)$$. This Chapter 07 quiz tests your fluency across subgradient definitions, normal cones, calculus rules, Lasso optimality, soft-thresholding, and distance-function subgradients.

## Key ideas: Chapter 07 Assessment Pillars

1. **Definition & Existence**: Checking $$f(y) \ge f(x) + g^T(y - x)$$ globally, knowing $$\partial f(x)$$ is always closed and convex, and recognizing when $$\partial f(x) = \{\nabla f(x)\}$$ vs. an interval or ball.
2. **Subgradient Calculus**: Applying positive scaling ($$a > 0$$), Minkowski addition, affine composition ($$A^T \partial f(Ax + b)$$), and the active-set convex-hull rule for pointwise maxima.
3. **Indicator Functions & Normal Cones**: Translating constrained problems into $$f + I_C$$ using $$\partial I_C(x) = N_C(x)$$ and verifying $$-\nabla f(x^\star) \in N_C(x^\star)$$.
4. **Universal Optimality & Canonical Examples**: Testing $$0 \in \partial f(x^\star)$$ to solve Lasso correlation conditions, soft-thresholding $$S_\lambda(y)$$, and Euclidean distance gradients $$(x - P_C(x))/\|x - P_C(x)\|_2$$.

### Worked example: Pre-Quiz Subdifferential Check on $$\|x\|_\infty$$

**Warm-Up Question**: Compute $$\partial f(x)$$ for $$f(x_1, x_2) = \|x\|_\infty = \max\{|x_1|, |x_2|\}$$ at the point $$x = (2, -2)$$.

1. **Rewrite as a pointwise maximum of 4 linear functions**:
   $$f(x) = \max\{x_1,\; -x_1,\; x_2,\; -x_2\}.$$
2. **Identify the active branches at $$x = (2, -2)$$**:
   - $$x_1 = 2$$ (active! gradient $$(1, 0)$$),
   - $$-x_1 = -2$$ (inactive),
   - $$x_2 = -2$$ (inactive),
   - $$-x_2 = 2$$ (active! gradient $$(0, -1)$$).
3. **Take the convex hull of active gradients**:
   $$\partial f(2, -2) = \operatorname{conv}\!\left\{\begin{bmatrix} 1 \\ 0 \end{bmatrix},\; \begin{bmatrix} 0 \\ -1 \end{bmatrix}\right\} = \left\{\begin{bmatrix} \theta \\ -(1 - \theta) \end{bmatrix} : 0 \le \theta \le 1\right\}.$$
   Notice every vector $$g \in \partial f(2, -2)$$ satisfies $$\|g\|_1 = \theta + (1 - \theta) = 1$$ (the dual norm of $$\|\cdot\|_\infty$$!) and $$g^T x = 2\theta + 2(1 - \theta) = 2 = \|x\|_\infty$$!

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### 📐 **Subgradients**

#### **Definition**
For a convex function $$f: \mathbb{R}^n \to \mathbb{R}$$, a subgradient at $$x$$ is a vector $$g \in \mathbb{R}^n$$ satisfying:

$$f(y) \ge f(x) + g^T(y - x), \quad \forall y$$

**Geometric meaning:**
- $$g$$ defines a supporting hyperplane of $$f$$ at $$x$$
- This hyperplane lies below the graph of the function at every point
- It generalizes the gradient to non-differentiable functions

#### **Basic properties**
- **Existence:** A subgradient always exists for a convex function
- **Uniqueness:** If $$f$$ is differentiable at $$x$$, then $$g = \nabla f(x)$$ is the unique subgradient
- **Non-convex:** For non-convex functions, a subgradient may not exist

### 📊 **Important Examples**

#### **1. Absolute value: $$f(x) = \lvert x \rvert$$**
$$\partial f(x) = \begin{cases}
\{-1\} & \text{if } x < 0 \\
[-1, 1] & \text{if } x = 0 \\
\{1\} & \text{if } x > 0
\end{cases}$$

#### **2. L1 norm: $$f(x) = \lVert x \rVert_1 = \sum_{i=1}^n \lvert x_i \rvert$$**
$$(\partial f(x))_i = \begin{cases}
\{\text{sign}(x_i)\} & \text{if } x_i \neq 0 \\
[-1, 1] & \text{if } x_i = 0
\end{cases}$$

#### **3. L2 norm: $$f(x) = \lVert x \rVert_2$$**
$$\partial f(x) = \begin{cases}
\left\{\frac{x}{\lVert x \rVert_2}\right\} & \text{if } x \neq 0 \\
\{g : \lVert g \rVert_2 \le 1\} & \text{if } x = 0
\end{cases}$$

#### **4. Max function: $$f(x) = \max\{f_1(x), f_2(x)\}$$**
$$\partial f(x) = \begin{cases}
\{\nabla f_1(x)\} & \text{if } f_1(x) > f_2(x) \\
\{\nabla f_2(x)\} & \text{if } f_1(x) < f_2(x) \\
\text{conv}\{\nabla f_1(x), \nabla f_2(x)\} & \text{if } f_1(x) = f_2(x)
\end{cases}$$

### 🔍 **The Subdifferential**

#### **Definition**
The subdifferential $$\partial f(x)$$ is the set of all subgradients at $$x$$:

$$\partial f(x) = \{g \in \mathbb{R}^n : g \text{ is a subgradient of } f \text{ at } x\}$$

#### **Important properties**
- **Closed convex set:** $$\partial f(x)$$ is always a closed convex set
- **Nonempty:** If $$f$$ is convex, then $$\partial f(x) \neq \emptyset$$
- **Uniqueness:** If $$f$$ is differentiable at $$x$$, then $$\partial f(x) = \{\nabla f(x)\}$$
- **Differentiability:** If $$\partial f(x) = \{g\}$$, then $$f$$ is differentiable at $$x$$ and $$\nabla f(x) = g$$

### 🎯 **Subgradient Optimality Condition**

#### **Fundamental theorem**
$$x^* \text{ is a global minimizer of } f \quad \Longleftrightarrow \quad 0 \in \partial f(x^*)$$

#### **Proof**
$$\begin{align}
f(x^*) = \min_x f(x) &\Longleftrightarrow f(y) \ge f(x^*) \text{ for all } y \\
&\Longleftrightarrow f(y) \ge f(x^*) + 0^T(y - x^*) \\
&\Longleftrightarrow 0 \in \partial f(x^*)
\end{align}$$

**Important note:** This condition holds even for non-convex functions!

### 🔗 **Connection with the First-Order Optimality Condition**

#### **Constrained problem**
$$\min_{x \in C} f(x)$$

#### **First-order optimality condition**
If $$f$$ is convex and differentiable:
$$x^* \text{ optimal} \Longleftrightarrow \nabla f(x^*)^T(y - x^*) \ge 0, \quad \forall y \in C$$

#### **Derivation from subgradients**
$$\begin{align}
\min_{x \in C} f(x) &\Longleftrightarrow \min_x [f(x) + I_C(x)] \\
&\Longleftrightarrow 0 \in \partial[f(x^*) + I_C(x^*)] \\
&\Longleftrightarrow 0 \in \{\nabla f(x^*)\} + \mathcal{N}_C(x^*) \\
&\Longleftrightarrow -\nabla f(x^*) \in \mathcal{N}_C(x^*) \\
&\Longleftrightarrow \nabla f(x^*)^T(y - x^*) \ge 0, \quad \forall y \in C
\end{align}$$

### 📏 **Subgradient Calculus Rules**

#### **1. Linear combinations**
$$\partial(\alpha f + \beta g)(x) = \alpha \partial f(x) + \beta \partial g(x)$$
with $$\alpha, \beta \ge 0$$

#### **2. Max functions**
$$\partial \max\{f_1, \ldots, f_m\}(x) = \text{conv}\{\partial f_i(x) : i \in I(x)\}$$
with $$I(x) = \{i : f_i(x) = \max_j f_j(x)\}$$

#### **3. Composition**
If $$h(x) = f(Ax + b)$$:
$$\partial h(x) = A^T \partial f(Ax + b)$$

#### **4. Indicator functions**
$$\partial I_C(x) = \begin{cases}
\mathcal{N}_C(x) & \text{if } x \in C \\
\emptyset & \text{if } x \notin C
\end{cases}$$

where $$\mathcal{N}_C(x)$$ is the normal cone of $$C$$ at $$x$$

### 🎲 **Practical Applications**

#### **1. LASSO Regression**
$$\min_\beta \frac{1}{2}\lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$$

**Optimality conditions:**
$$0 \in X^T(X\beta^* - y) + \lambda \partial \lVert \beta^* \rVert_1$$

#### **2. Soft-thresholding**
The solution of $$\min_x \frac{1}{2}(x - a)^2 + \lambda \lvert x \rvert$$:

$$x^* = \text{soft}(a, \lambda) = \begin{cases}
a - \lambda & \text{if } a > \lambda \\
0 & \text{if } \lvert a \rvert \le \lambda \\
a + \lambda & \text{if } a < -\lambda
\end{cases}$$

#### **3. Distance to a convex set**
$$\min_x \frac{1}{2}\lVert x - a \rVert_2^2 + I_C(x)$$

**Solution:** $$x^* = P_C(a)$$ (the projection of $$a$$ onto $$C$$)

### 🔄 **Gradient vs Subgradient**

| Aspect | Gradient | Subgradient |
|-----------|----------|-------------|
| **Condition** | Differentiable function | Convex function |
| **Unique** | Yes | No (may be a set) |
| **Existence** | Not always | Always (for convex functions) |
| **Computation** | Derivatives | Subdifferential rules |
| **Application** | Smooth optimization | Non-smooth optimization |

### 🛠️ **Computation Techniques**

#### **Step 1: Check differentiability**
- If $$f$$ is differentiable at $$x$$: $$\partial f(x) = \{\nabla f(x)\}$$
- If not differentiable: use the calculus rules

#### **Step 2: Analyze the structure**
- Linear combinations of convex functions
- Max/min functions
- Compositions
- Indicator functions

#### **Step 3: Apply the rules**
- Use the subdifferential calculus rules
- Combine the partial results

### ⚡ **The Subgradient Method**

#### **Update rule**
$$x^{(k+1)} = x^{(k)} - t_k g^{(k)}$$
with $$g^{(k)} \in \partial f(x^{(k)})$$

#### **Choosing the step size**
- **Fixed:** $$t_k = t > 0$$
- **Diminishing:** $$t_k \to 0$$, $$\sum t_k = \infty$$
- **Square summable:** $$\sum t_k^2 < \infty$$

#### **Convergence**
- Monotonic decrease is not guaranteed
- Converges to the optimal value (not necessarily to an optimal point)
- Convergence rate: $$O(1/\sqrt{k})$$

### 🎯 **Illustrative Examples**

#### **Problem:** $$\min_x \lvert x - 2 \rvert + \lvert x + 1 \rvert$$

**Step 1:** Compute the subdifferential
$$\partial f(x) = \partial \lvert x - 2 \rvert + \partial \lvert x + 1 \rvert$$

**Step 2:** Analyze each interval
- $$x < -1$$: $$\partial f(x) = \{-1 - 1\} = \{-2\}$$
- $$-1 < x < 2$$: $$\partial f(x) = \{-1 + 1\} = \{0\}$$
- $$x > 2$$: $$\partial f(x) = \{1 + 1\} = \{2\}$$

**Step 3:** Optimality condition
$$0 \in \partial f(x^*) \Rightarrow x^* \in [-1, 2]$$

### 💡 **Practical Tips**

#### **Recognizing non-differentiable functions:**
- Functions containing $$\lvert \cdot \rvert$$, $$\max\{\cdot\}$$, $$\min\{\cdot\}$$
- Indicator functions $$I_C(\cdot)$$
- The norms $$\lVert \cdot \rVert_1$$, $$\lVert \cdot \rVert_\infty$$

#### **Efficient computation:**
- Use the linear-combination rule
- Analyze component by component
- Apply geometric properties

#### **Checking results:**
- Verify the subdifferential condition
- Check that the resulting set is convex
- Compare with the differentiable case (if applicable)

---

💡 **Tip:** Subgradients extend the gradient to non-differentiable functions; they are a powerful tool in convex optimization and in machine learning with regularization!

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

This multiple-choice quiz tests your understanding of subgradients, subdifferentials, their geometric properties and optimality conditions in convex optimization.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🧮 Quiz: Subgradients and Subdifferentials</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">25</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1 -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: A subgradient of a convex function \\(f\\) at a point \\(x\\) is a vector \\(g\\) satisfying:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \\(f(y) \leq f(x) + g^T(y-x)\\) for all \\(y\\)</label>
                <label><input type="radio" name="q1" value="b"> B) \\(f(y) \geq f(x) + g^T(y-x)\\) for all \\(y\\)</label>
                <label><input type="radio" name="q1" value="c"> C) \\(f(y) = f(x) + g^T(y-x)\\) for all \\(y\\)</label>
                <label><input type="radio" name="q1" value="d"> D) \\(\nabla f(x) = g\\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$f(y) \geq f(x) + g^T(y-x)$$ for all $$y$$</strong><br>
                This is the exact definition of a subgradient: the function always lies above the affine function defined by the subgradient.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The subdifferential \\(\partial f(x)\\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) The set of all gradients at \\(x\\)</label>
                <label><input type="radio" name="q2" value="b"> B) The set of all subgradients at \\(x\\)</label>
                <label><input type="radio" name="q2" value="c"> C) The unique gradient vector at \\(x\\)</label>
                <label><input type="radio" name="q2" value="d"> D) The second derivative at \\(x\\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The set of all subgradients at $$x$$</strong><br>
                The subdifferential $$\partial f(x)$$ is the set of all vectors $$g$$ satisfying the subgradient condition.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: The subgradients of \\(f(x) = |x|\\) at \\(x = 0\\) are:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \\(\{0\}\\)</label>
                <label><input type="radio" name="q3" value="b"> B) \\(\{1, -1\}\\)</label>
                <label><input type="radio" name="q3" value="c"> C) \\([-1, 1]\\)</label>
                <label><input type="radio" name="q3" value="d"> D) \\(\mathbb{R}\\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) $$[-1, 1]$$</strong><br>
                At $$x = 0$$, $$|x|$$ is not differentiable and the subdifferential is the interval $$[-1, 1]$$, because $$|y| \geq g \cdot y$$ for all $$y$$ when $$g \in [-1, 1]$$.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: If a convex function \\(f\\) is differentiable at \\(x\\), then \\(\partial f(x)\\) equals:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) \\(\{\nabla f(x)\}\\)</label>
                <label><input type="radio" name="q4" value="b"> B) \\(\emptyset\\)</label>
                <label><input type="radio" name="q4" value="c"> C) \\(\mathbb{R}^n\\)</label>
                <label><input type="radio" name="q4" value="d"> D) An infinite set of vectors</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\{\nabla f(x)\}$$</strong><br>
                When a convex function is differentiable at a point, its subdifferential contains a single element: the gradient.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: A necessary and sufficient condition for \\(x^*\\) to be a global minimizer of a convex function \\(f\\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \\(\nabla f(x^*) = 0\\)</label>
                <label><input type="radio" name="q5" value="b"> B) \\(0 \in \partial f(x^*)\\)</label>
                <label><input type="radio" name="q5" value="c"> C) \\(f(x^*) = 0\\)</label>
                <label><input type="radio" name="q5" value="d"> D) \\(\partial f(x^*) = \mathbb{R}^n\\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$0 \in \partial f(x^*)$$</strong><br>
                Subgradient optimality condition: $$x^*$$ is a global minimizer if and only if $$0$$ belongs to the subdifferential at $$x^*$$.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: The subdifferential \(\partial f(x)\) of a convex function is always:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) The empty set</label>
                <label><input type="radio" name="q6" value="b"> B) A closed convex set</label>
                <label><input type="radio" name="q6" value="c"> C) An open set</label>
                <label><input type="radio" name="q6" value="d"> D) A single element</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) A closed convex set</strong><br>
                The subdifferential of a convex function is always closed and convex, and it is also compact and nonempty (if $$x$$ lies in the interior of $$\text{dom} f$$).
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: Let \(f(x) = \max\{x_1, x_2\}\) at the point \(x = (2, 2)\). The subdifferential \(\partial f(x)\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(\{(1, 0), (0, 1)\}\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(\text{conv}\{(1, 0), (0, 1)\}\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(\{(1, 1)\}\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(\{(0, 0)\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) \(\text{conv}\{(1, 0), (0, 1)\}\)</strong><br>
                At a point where several components attain the maximum, the subdifferential is the convex hull of the gradients of the active components.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: If \(f\) and \(g\) are two convex functions, then \(\partial(f + g)(x)\) equals:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\partial f(x) + \partial g(x)\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(\partial f(x) \cup \partial g(x)\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(\partial f(x) \cap \partial g(x)\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(\max\{\partial f(x), \partial g(x)\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) \(\partial f(x) + \partial g(x)\)</strong><br>
                Sum rule: the subdifferential of a sum is the Minkowski sum of the subdifferentials (valid, for example, when $$\text{relint}\,\text{dom} f \cap \text{relint}\,\text{dom} g \neq \emptyset$$, e.g. when both functions are finite on all of $$\mathbb{R}^n$$).
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The subdifferential of \(f(x) = \|x\|_2\) at \(x \neq 0\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\{x/\|x\|_2\}\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\{u : \|u\|_2 \leq 1\}\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\{0\}\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\mathbb{R}^n\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) \(\{x/\|x\|_2\}\)</strong><br>
                When \(x \neq 0\), the Euclidean norm is differentiable with gradient \(x/\|x\|_2\).
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The subdifferential of \(f(x) = \|x\|_2\) at \(x = 0\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(\{0\}\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(\{u : \|u\|_2 \leq 1\}\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(\{u : \|u\|_2 = 1\}\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(\mathbb{R}^n\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) \(\{u : \|u\|_2 \leq 1\}\)</strong><br>
                At the origin, the subdifferential of the Euclidean norm is the closed unit ball.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: Let \(f(x) = g(Ax + b)\) with \(g\) convex and \(A\) a matrix. Then \(\partial f(x)\) equals:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(A^T \partial g(Ax + b)\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(A \partial g(Ax + b)\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(\partial g(Ax + b) A^T\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(\partial g(Ax + b)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) \(A^T \partial g(Ax + b)\)</strong><br>
                Chain rule for subdifferentials: \(\partial f(x) = A^T \partial g(Ax + b)\).
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The subdifferential of the indicator function \(I_C(x)\) of a convex set \(C\) at \(x \in C\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) \(\{0\}\)</label>
                <label><input type="radio" name="q12" value="b"> B) The normal cone \(N_C(x)\)</label>
                <label><input type="radio" name="q12" value="c"> C) The tangent cone \(T_C(x)\)</label>
                <label><input type="radio" name="q12" value="d"> D) \(\mathbb{R}^n\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The normal cone \(N_C(x)\)</strong><br>
                The subdifferential of the indicator function equals the normal cone of the convex set at that point.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The subdifferential operator \(\partial f\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Monotone</label>
                <label><input type="radio" name="q13" value="b"> B) Not monotone</label>
                <label><input type="radio" name="q13" value="c"> C) Linear</label>
                <label><input type="radio" name="q13" value="d"> D) Continuous</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Monotone</strong><br>
                The subdifferential of a convex function is a monotone operator: \((g_1 - g_2)^T(x_1 - x_2) \geq 0\) for \(g_i \in \partial f(x_i)\).
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: The subdifferential of the linear function \(f(x) = c^T x\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(\{c\}\)</label>
                <label><input type="radio" name="q14" value="b"> B) \(\{0\}\)</label>
                <label><input type="radio" name="q14" value="c"> C) \(\mathbb{R}^n\)</label>
                <label><input type="radio" name="q14" value="d"> D) \(\{tc : t \geq 0\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) \(\{c\}\)</strong><br>
                A linear function is differentiable everywhere with constant gradient \(c\).
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: Let \(f(x) = \frac{1}{2}x^T Q x + c^T x\) with \(Q \succeq 0\). The subdifferential \(\partial f(x)\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(\{Qx + c\}\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(\{Qx\}\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(\{c\}\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(\{x\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) \(\{Qx + c\}\)</strong><br>
                A convex quadratic is differentiable with gradient \(\nabla f(x) = Qx + c\).
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: Consider the problem \(\min f(x)\) s.t. \(x \in C\). The optimality condition is:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(0 \in \partial f(x^*)\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(-\partial f(x^*) \cap N_C(x^*) \neq \emptyset\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(\nabla f(x^*) = 0\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(x^* \in C\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) \(-\partial f(x^*) \cap N_C(x^*) \neq \emptyset\)</strong><br>
                Constrained subgradient optimality condition: the negative of some subgradient lies in the normal cone.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: Let \(f(x) = \max\{f_1(x), f_2(x)\}\) with \(f_1, f_2\) convex and differentiable. At a point \(x\) where \(f_1(x) > f_2(x)\):</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(\partial f(x) = \{\nabla f_1(x)\}\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(\partial f(x) = \{\nabla f_2(x)\}\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(\partial f(x) = \text{conv}\{\nabla f_1(x), \nabla f_2(x)\}\)</label>
                <label><input type="radio" name="q17" value="d"> D) \(\partial f(x) = \emptyset\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) \(\partial f(x) = \{\nabla f_1(x)\}\)</strong><br>
                When only one function attains the maximum, the subdifferential contains only the gradient of that function.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: The subdifferential \(\partial f(x)\) of a convex function \(f\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Upper continuous</label>
                <label><input type="radio" name="q18" value="b"> B) Upper semicontinuous</label>
                <label><input type="radio" name="q18" value="c"> C) Lower continuous</label>
                <label><input type="radio" name="q18" value="d"> D) Discontinuous</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Upper semicontinuous</strong><br>
                The subdifferential is an upper semicontinuous set-valued map.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: Let \(f(x) = d_C(x) = \inf_{y \in C} \|x - y\|_2\) with \(C\) closed and convex. When \(x \notin C\):</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(\partial f(x) = \{(x - P_C(x))/\|x - P_C(x)\|_2\}\)</label>
                <label><input type="radio" name="q19" value="b"> B) \(\partial f(x) = \{0\}\)</label>
                <label><input type="radio" name="q19" value="c"> C) \(\partial f(x) = N_C(x)\)</label>
                <label><input type="radio" name="q19" value="d"> D) \(\partial f(x) = \{x\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) \(\partial f(x) = \{(x - P_C(x))/\|x - P_C(x)\|_2\}\)</strong><br>
                The subgradient of the distance function is the unit vector pointing from the projection to the point.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: The support function \(\sigma_C(x) = \sup_{y \in C} y^T x\) of a compact convex set \(C\) has subdifferential:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) \(\partial \sigma_C(x) = \arg\max_{y \in C} y^T x\)</label>
                <label><input type="radio" name="q20" value="b"> B) \(\partial \sigma_C(x) = C\)</label>
                <label><input type="radio" name="q20" value="c"> C) \(\partial \sigma_C(x) = \{x\}\)</label>
                <label><input type="radio" name="q20" value="d"> D) \(\partial \sigma_C(x) = \{0\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) \(\partial \sigma_C(x) = \arg\max_{y \in C} y^T x\)</strong><br>
                The subdifferential of the support function is the set of points attaining the maximum in the supremum.
            </div>
        </div>

        <!-- Question 21 -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: In SVM, the hinge loss \(f(t) = \max\{0, 1-t\}\) has subdifferential at \(t = 1\):</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) \(\{0\}\)</label>
                <label><input type="radio" name="q21" value="b"> B) \(\{-1\}\)</label>
                <label><input type="radio" name="q21" value="c"> C) \([-1, 0]\)</label>
                <label><input type="radio" name="q21" value="d"> D) \([0, 1]\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) \([-1, 0]\)</strong><br>
                At the kink \(t = 1\), the subdifferential is the interval between the left derivative (-1) and the right derivative (0).
            </div>
        </div>

        <!-- Question 22 -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The subdifferential of \(f(x) = \|x\|_1\) at \(x\) with \(x_i \neq 0\), for the \(i\)-th component, is:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) \(\text{sign}(x_i)\)</label>
                <label><input type="radio" name="q22" value="b"> B) \([-1, 1]\)</label>
                <label><input type="radio" name="q22" value="c"> C) \(x_i\)</label>
                <label><input type="radio" name="q22" value="d"> D) \(|x_i|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) \(\text{sign}(x_i)\)</strong><br>
                When \(x_i \neq 0\), the \(i\)-th component of the subdifferential is \(\text{sign}(x_i)\).
            </div>
        </div>

        <!-- Question 23 -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: If a convex function \(f\) is not differentiable at \(x\), then \(\partial f(x)\):</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Is the empty set</label>
                <label><input type="radio" name="q23" value="b"> B) Contains more than one element</label>
                <label><input type="radio" name="q23" value="c"> C) Contains only the zero vector</label>
                <label><input type="radio" name="q23" value="d"> D) Is undefined</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Contains more than one element</strong><br>
                At a point of non-differentiability, the subdifferential contains several subgradients, reflecting the "kink" of the function.
            </div>
        </div>

        <!-- Question 24 -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: In the subgradient method, the update direction is chosen as:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Gradient \(\nabla f(x)\)</label>
                <label><input type="radio" name="q24" value="b"> B) The negative of any subgradient: \(-g\) with \(g \in \partial f(x)\)</label>
                <label><input type="radio" name="q24" value="c"> C) A random vector</label>
                <label><input type="radio" name="q24" value="d"> D) The Newton direction</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The negative of any subgradient: \(-g\) with \(g \in \partial f(x)\)</strong><br>
                The subgradient method picks any subgradient $$g$$ at the current point and updates $$x^{+} = x - t g$$. Note that $$-g$$ is not necessarily a descent direction.
            </div>
        </div>

        <!-- Question 25 -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: Geometrically, a subgradient \(g \in \partial f(x)\) defines:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) A hyperplane lying above the graph of the function</label>
                <label><input type="radio" name="q25" value="b"> B) A hyperplane lying below the graph of the function</label>
                <label><input type="radio" name="q25" value="c"> C) A hyperplane cutting the graph of the function</label>
                <label><input type="radio" name="q25" value="d"> D) A hyperplane perpendicular to the graph of the function</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) A hyperplane lying below the graph of the function</strong><br>
                A subgradient defines a supporting hyperplane: \(f(y) \geq f(x) + g^T(y-x)\) - the graph of the function lies above this hyperplane.
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
    q1: 'b', q2: 'b', q3: 'c', q4: 'a', q5: 'b',
    q6: 'b', q7: 'b', q8: 'a', q9: 'a', q10: 'b',
    q11: 'a', q12: 'b', q13: 'a', q14: 'a', q15: 'a',
    q16: 'b', q17: 'a', q18: 'b', q19: 'a', q20: 'a',
    q21: 'c', q22: 'a', q23: 'b', q24: 'b', q25: 'b'
};

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
    
    // Re-render MathJax for the current question
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        MathJax.startup.promise.then(() => MathJax.typesetPromise([document.getElementById(`q${n}`)])).then(() => {
            // MathJax rendering complete
        });
    }
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
        message = '🌟 Excellent! You have mastered subgradients!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand subgradients and subdifferentials quite well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review a few concepts about optimality conditions.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review the definitions and basic properties.';
    } else {
        message = '📖 Study the concepts of subgradients again from the beginning!';
    }
    
    document.getElementById('performance-message').textContent = message;
    
    // Hide the submit button, show the reset button
    document.getElementById('submit-btn').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'inline-block';
    
    // Re-render MathJax for all content
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        MathJax.startup.promise.then(() => MathJax.typesetPromise()).then(() => {
            // MathJax rendering complete
        });
    }
    
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
        MathJax.startup.promise.then(() => MathJax.typesetPromise()).then(() => {
            // MathJax rendering complete
        });
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
---
layout: post
title: '08-09 Multiple-Choice Quiz - Subgradient Method'
chapter: '08'
order: 17
owner: GitHub Copilot
lang: en
categories:
- chapter08
lesson_type: quiz
---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### ⚡ **The Subgradient Method**

#### **Algorithm definition**
The subgradient method extends gradient descent to non-differentiable convex functions:

$$x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}, \quad k = 1, 2, 3, \ldots$$

where $$g^{(k-1)} \in \partial f(x^{(k-1)})$$ is a subgradient of $$f$$ at $$x^{(k-1)}$$

#### **Key differences from Gradient Descent**
- **No guaranteed descent:** The function value may increase at some steps
- **Track the best value:** $$f(x_{\text{best}}^{(k)}) = \min_{i=0,\ldots,k} f(x^{(i)})$$
- **Pre-set step sizes:** Line search cannot be used as in gradient descent

### 📏 **Choosing the Step Size**

#### **1. Fixed step size**
$$t_k = t > 0, \quad \forall k$$

**Characteristics:**
- Simple to implement
- Converges to a neighborhood of the optimal value
- Does not reach the exact solution

#### **2. Diminishing step sizes**
Satisfying the conditions:
$$\sum_{k=1}^{\infty} t_k = \infty, \quad \sum_{k=1}^{\infty} t_k^2 < \infty$$

**Common examples:**
- $$t_k = \frac{1}{k}$$ (harmonic series)
- $$t_k = \frac{1}{\sqrt{k}}$$
- $$t_k = \frac{a}{b + k}$$ with $$a, b > 0$$

**Characteristics:**
- Converges exactly to the optimal value ($$f_{\text{best}}^{(k)} \to f^*$$)
- Slower initial convergence than a fixed step size

#### **3. Polyak step sizes**
$$t_k = \frac{f(x^{(k)}) - f^*}{\lVert g^{(k)} \rVert_2^2}$$

**Requirement:** The optimal value $$f^*$$ must be known
**Advantage:** Faster convergence when $$f^*$$ is known

### 📊 **Convergence Analysis**

#### **Basic assumptions**
- $$f$$ is convex with $$\text{dom}(f) = \mathbb{R}^n$$
- $$f$$ satisfies the Lipschitz condition:
  $$|f(x) - f(y)| \le G \lVert x - y \rVert_2, \quad \forall x, y$$
- Bounded subgradients: $$\lVert g \rVert_2 \le G$$ for $$g \in \partial f(x)$$

#### **Convergence theorem for a fixed step size**
$$\lim_{k \to \infty} f(x_{\text{best}}^{(k)}) \le f^* + \frac{G^2 t}{2}$$

**Meaning:**
- Converges to a neighborhood of the optimal value
- The final error is proportional to the step size $$t$$
- Trade-off: small $$t$$ → small error but slow convergence

#### **Convergence theorem for diminishing step sizes**
$$\lim_{k \to \infty} f(x_{\text{best}}^{(k)}) = f^*$$

**Meaning:**
- Converges exactly to the optimal value ($$f_{\text{best}}^{(k)} \to f^*$$)
- Convergence rate: $$O(1/\sqrt{k})$$ (sublinear)

#### **Basic proof**
From the basic inequality:
$$f_{\text{best}}^{(k)} - f^* \le \frac{R^2 + G^2 \sum_{i=1}^k t_i^2}{2 \sum_{i=1}^k t_i}$$

with $$R = \lVert x^{(0)} - x^* \rVert_2$$

### 🎯 **Practical Applications**

#### **1. LASSO Regression**
$$\min_\beta \frac{1}{2} \lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$$

**Subgradient:**
$$\partial f(\beta) = X^T(X\beta - y) + \lambda \partial \lVert \beta \rVert_1$$

#### **2. Regularized Logistic Regression**
$$\min_\beta \sum_{i=1}^n \left[-y_i x_i^T \beta + \log(1 + \exp(x_i^T \beta))\right] + \lambda \lVert \beta \rVert_1$$

**Comparison:**
- **Ridge (L2):** Differentiable → Gradient descent
- **LASSO (L1):** Non-differentiable → Subgradient method

#### **3. Support Vector Machine**
$$\min_w \frac{1}{2} \lVert w \rVert_2^2 + C \sum_{i=1}^n \max(0, 1 - y_i w^T x_i)$$

**Hinge loss:** $$\max(0, 1 - z)$$ is not differentiable at $$z = 1$$

### 🔄 **Stochastic Subgradient Method**

#### **Sum problem**
$$\min_x f(x) = \min_x \sum_{i=1}^m f_i(x)$$

#### **Stochastic update**
$$x^{(k)} = x^{(k-1)} - t_k g_i^{(k-1)}$$

with $$g_i^{(k-1)} \in \partial f_i(x^{(k-1)})$$ and $$i$$ chosen at random

#### **Advantages**
- Computational cost: $$O(1)$$ instead of $$O(m)$$
- Suited to big data
- Can escape saddle points

#### **Disadvantages**
- Noisier than the batch method
- Requires careful learning-rate tuning
- Slower convergence near the optimum

### 📈 **Projected Subgradient Method**

#### **Constrained problem**
$$\min_{x \in C} f(x)$$

with $$C$$ a closed convex set

#### **Algorithm**
$$x^{(k)} = P_C(x^{(k-1)} - t_k g^{(k-1)})$$

with $$P_C(\cdot)$$ the projection onto $$C$$

#### **Example: Intersection of Sets**
$$\min_x \frac{1}{2} \lVert x \rVert_2^2 \quad \text{s.t.} \quad x \in \bigcap_{i=1}^m C_i$$

**Algorithm:**
1. Choose the most violated set $$C_i$$
2. Project onto $$C_i$$: $$x^{(k)} = P_{C_i}(x^{(k-1)})$$

### 🔄 **Comparing the Methods**

| Method | Condition | Convergence rate | Applications |
|-------------|-----------|---------------|----------|
| **Gradient Descent** | Differentiable functions | $$O(1/k)$$ or linear | Smooth optimization |
| **Subgradient** | Convex functions | $$O(1/\sqrt{k})$$ | Non-smooth optimization |
| **SGD** | Differentiable functions | $$O(1/\sqrt{k})$$ | Large-scale problems |
| **Stochastic Subgradient** | Convex functions | $$O(1/\sqrt{k})$$ | Large-scale non-smooth |

### 🛠️ **Practical Techniques**

#### **Choosing the step size**
1. **Fixed step size:** Try $$t = 0.01, 0.1, 1$$ and pick the best
2. **Diminishing:** Use $$t_k = \frac{1}{\sqrt{k}}$$ or $$t_k = \frac{1}{k}$$
3. **Polyak:** If $$f^*$$ is known, use the Polyak formula

#### **Monitoring convergence**
- Track $$f(x_{\text{best}}^{(k)})$$ instead of $$f(x^{(k)})$$
- Plot the convergence to check it
- Use a moving average for smoothing

#### **Debugging**
- Check that the subgradient is correct
- Verify Lipschitz constant $$G$$
- Try several step sizes
- Compare with gradient descent (if the function is differentiable)

### ⚡ **Improvements to the Subgradient Method**

#### **1. Averaging**
$$\bar{x}^{(k)} = \frac{1}{k} \sum_{i=1}^k x^{(i)}$$

**Advantages:** Reduces noise, improves the convergence rate

#### **2. Momentum**
$$x^{(k)} = x^{(k-1)} - t_k g^{(k-1)} + \beta(x^{(k-1)} - x^{(k-2)})$$

**Advantages:** Accelerates convergence, reduces oscillation

#### **3. Adaptive step sizes**
- **AdaGrad for subgradients**
- **RMSprop variants**
- **Adam-like methods**

### 🎯 **Illustrative Examples**

#### **Problem:** $$\min_x |x - 2| + |x + 1|$$

**Step 1:** Compute a subgradient
$$\partial f(x) = \partial |x - 2| + \partial |x + 1|$$

**Step 2:** Subgradient method with $$t_k = 0.1$$
- Start from $$x^{(0)} = 5$$
- $$g^{(0)} = 1 + 1 = 2$$
- $$x^{(1)} = 5 - 0.1 \times 2 = 4.8$$
- Continue until convergence

**Result:** Converges to $$x^* \in [-1, 2]$$

### 💡 **Practical Tips**

#### **When to use the Subgradient Method:**
- Non-differentiable objectives (containing $$\lvert \cdot \rvert$$, $$\max\{\cdot\}$$)
- Regularization with the L1 norm
- Constrained optimization with indicator functions
- Large-scale problems with stochastic variants

#### **When NOT to use it:**
- Differentiable functions (use gradient descent)
- When fast convergence is needed (use Newton methods)
- Non-convex functions (no global optimum guarantee)

#### **Best practices:**
- Always track $$f_{\text{best}}^{(k)}$$
- Try several step-size strategies
- Use averaging to reduce noise
- Combine with projection for constrained problems

---

💡 **Tip:** The subgradient method is a powerful tool for non-smooth optimization, especially important in machine learning with regularization and in robust optimization!

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

This multiple-choice quiz tests your understanding of the subgradient method, step-size choice, convergence analysis, the projected subgradient method and the stochastic subgradient method.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: The Subgradient Method</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1 -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: The update formula of the subgradient method is:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(x^{(k)} = x^{(k-1)} + t_k \cdot g^{(k-1)}\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(x^{(k)} = x^{(k-1)} - t_k \cdot \nabla f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(x^{(k)} = x^{(k-1)} - g^{(k-1)}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$x^{(k)} = x^{(k-1)} - t_k \cdot g^{(k-1)}$$</strong><br>
                The subgradient method replaces the gradient with a subgradient $$g^{(k-1)} \in \partial f(x^{(k-1)})$$ with step size $$t_k$$.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: Unlike gradient descent, the subgradient method:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Always decreases the function value at every step</label>
                <label><input type="radio" name="q2" value="b"> B) Does not always guarantee a decrease of the function value at every step</label>
                <label><input type="radio" name="q2" value="c"> C) Only applies to differentiable functions</label>
                <label><input type="radio" name="q2" value="d"> D) Converges faster than gradient descent</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Does not always guarantee a decrease of the function value at every step</strong><br>
                That is why this method is not called subgradient "descent", and we need to track the best value $$f(x_{best}^{(k)})$$.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: In the subgradient method, \(f(x_{best}^{(k)})\) is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(f(x^{(k)})\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\min_{i=0,...,k} f(x^{(i)})\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(\max_{i=0,...,k} f(x^{(i)})\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(\frac{1}{k+1} \sum_{i=0}^k f(x^{(i)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\min_{i=0,...,k} f(x^{(i)})$$</strong><br>
                This is the smallest value of $$f$$ obtained over $$k$$ iterations of the subgradient method.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: With a fixed step size \(t_k = t\), the subgradient method:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Converges to the exact optimal solution</label>
                <label><input type="radio" name="q4" value="b"> B) Converges to a neighborhood of the optimal value</label>
                <label><input type="radio" name="q4" value="c"> C) Does not converge</label>
                <label><input type="radio" name="q4" value="d"> D) Converges only for differentiable functions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Converges to a neighborhood of the optimal value</strong><br>
                With a fixed step size the algorithm does not converge exactly: $$\lim_{k\to\infty} f(x_{best}^{(k)}) \leq f^* + \frac{G^2 t}{2}$$, i.e. it only gets within a neighborhood of the optimal value proportional to $$t$$.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: A condition on diminishing step sizes that guarantees convergence is:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(\sum_{k=1}^{\infty} t_k < \infty\) and \(\sum_{k=1}^{\infty} t_k^2 < \infty\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(\sum_{k=1}^{\infty} t_k = \infty\) and \(\sum_{k=1}^{\infty} t_k^2 < \infty\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(\sum_{k=1}^{\infty} t_k = \infty\) and \(\sum_{k=1}^{\infty} t_k^2 = \infty\)</label>
                <label><input type="radio" name="q5" value="d"> D) \(t_k = \text{constant}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\sum_{k=1}^{\infty} t_k = \infty$$ and $$\sum_{k=1}^{\infty} t_k^2 < \infty$$</strong><br>
                The Robbins-Monro condition: an infinite sum guarantees progress, a finite sum of squares controls the noise.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: The step size \(t_k = \frac{1}{k}\) satisfies the convergence condition because:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(\sum_{k=1}^{\infty} \frac{1}{k} = \infty\) (harmonic series) and \(\sum_{k=1}^{\infty} \frac{1}{k^2} < \infty\) (Basel problem)</label>
                <label><input type="radio" name="q6" value="b"> B) Both sums are finite</label>
                <label><input type="radio" name="q6" value="c"> C) Both sums are infinite</label>
                <label><input type="radio" name="q6" value="d"> D) It does not satisfy the condition</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\sum_{k=1}^{\infty} \frac{1}{k} = \infty$$ (harmonic series) and $$\sum_{k=1}^{\infty} \frac{1}{k^2} < \infty$$ (Basel problem)</strong><br>
                This is the classic example of a step size satisfying the Robbins-Monro condition.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: The convergence rate of the subgradient method with diminishing step sizes is:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(O(1/k)\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(O(1/\sqrt{k})\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(O(e^{-k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) $$O(1/\sqrt{k})$$</strong><br>
                The subgradient method converges at the rate $$O(1/\sqrt{k})$$, slower than gradient descent's $$O(1/k)$$.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The basic inequality in the analysis of the subgradient method is:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\|x^{(k)} - x^*\|^2 \leq \|x^{(k-1)} - x^*\|^2 - 2t_k(f(x^{(k-1)}) - f^*) + t_k^2\|g^{(k-1)}\|^2\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(\|x^{(k)} - x^*\|^2 \geq \|x^{(k-1)} - x^*\|^2\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(f(x^{(k)}) \leq f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(\|g^{(k)}\| \leq \|g^{(k-1)}\|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\|x^{(k)} - x^*\|^2 \leq \|x^{(k-1)} - x^*\|^2 - 2t_k(f(x^{(k-1)}) - f^*) + t_k^2\|g^{(k-1)}\|^2$$</strong><br>
                This is the basic inequality used in the convergence analysis, balancing progress against noise.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The Polyak step size is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(t_k = \frac{1}{k}\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(t_k = \frac{f(x^{(k-1)}) - f^*}{\|g^{(k-1)}\|^2}\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(t_k = \text{constant}\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(t_k = \frac{1}{\|g^{(k-1)}\|}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$t_k = \frac{f(x^{(k-1)}) - f^*}{\|g^{(k-1)}\|^2}$$</strong><br>
                The Polyak step size requires knowing the optimal value $$f^*$$ and usually performs well in practice.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The projected subgradient method for the constrained problem \(\min_{x \in C} f(x)\) has the formula:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(x^{(k)} = x^{(k-1)} - t_k g^{(k-1)}\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(x^{(k)} = P_C(x^{(k-1)} - t_k g^{(k-1)})\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(x^{(k)} = x^{(k-1)} - t_k P_C(g^{(k-1)})\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(x^{(k)} = P_C(x^{(k-1)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$x^{(k)} = P_C(x^{(k-1)} - t_k g^{(k-1)})$$</strong><br>
                The projected subgradient method takes a subgradient step and then projects the result onto the constraint set $$C$$.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: The stochastic subgradient method for the problem \(\min \sum_{i=1}^m f_i(x)\) has the formula:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(x^{(k)} = x^{(k-1)} - t_k \sum_{i=1}^m g_i^{(k-1)}\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(x^{(k)} = x^{(k-1)} - t_k g_{i_k}^{(k-1)}\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(x^{(k)} = x^{(k-1)} - t_k \frac{1}{m} \sum_{i=1}^m g_i^{(k-1)}\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(x^{(k)} = x^{(k-1)} - g_{i_k}^{(k-1)}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$x^{(k)} = x^{(k-1)} - t_k g_{i_k}^{(k-1)}$$</strong><br>
                The stochastic version only uses the subgradient of one function $$f_{i_k}$$ chosen at each iteration.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The main advantage of the stochastic subgradient method is:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Faster convergence than the batch method</label>
                <label><input type="radio" name="q12" value="b"> B) Lower computational cost per iteration</label>
                <label><input type="radio" name="q12" value="c"> C) It always decreases the function value</label>
                <label><input type="radio" name="q12" value="d"> D) No step size is needed</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Lower computational cost per iteration</strong><br>
                The stochastic method only needs the subgradient of one function instead of the whole sum, greatly reducing the computational cost.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: Compared with gradient descent, the subgradient method:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Converges faster</label>
                <label><input type="radio" name="q13" value="b"> B) Converges more slowly</label>
                <label><input type="radio" name="q13" value="c"> C) Has the same convergence rate</label>
                <label><input type="radio" name="q13" value="d"> D) Does not converge</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Converges more slowly</strong><br>
                The subgradient method has rate $$O(1/\sqrt{k})$$ compared with $$O(1/k)$$ for gradient descent, but it applies to non-differentiable functions.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: The subgradient method is used when:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) The objective is differentiable everywhere</label>
                <label><input type="radio" name="q14" value="b"> B) The objective is convex but possibly non-differentiable</label>
                <label><input type="radio" name="q14" value="c"> C) The objective is non-convex</label>
                <label><input type="radio" name="q14" value="d"> D) Only for unconstrained problems</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The objective is convex but possibly non-differentiable</strong><br>
                The subgradient method is designed specifically for non-differentiable convex functions such as the L1 norm and max functions.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: Unlike gradient descent, the step size in the subgradient method:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Can use backtracking line search</label>
                <label><input type="radio" name="q15" value="b"> B) Must be set in advance, not adaptively</label>
                <label><input type="radio" name="q15" value="c"> C) Is always equal to 1</label>
                <label><input type="radio" name="q15" value="d"> D) Is automatically optimal</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Must be set in advance, not adaptively</strong><br>
                The subgradient method cannot use line search because the direction is not guaranteed to be a descent direction.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: In the convergence analysis, the subgradients are usually assumed to be bounded:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(\|g^{(k)}\| \leq G\) with \(G > 0\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(\|g^{(k)}\| = 1\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(\|g^{(k)}\| \to 0\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(\|g^{(k)}\|\) is unbounded</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\|g^{(k)}\| \leq G$$ with $$G > 0$$</strong><br>
                The bounded-subgradient assumption is needed to guarantee convergence and to estimate the convergence rate.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: To find a point in the intersection of convex sets \(C_1 \cap C_2 \cap ... \cap C_m\), we can use:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Gradient descent</label>
                <label><input type="radio" name="q17" value="b"> B) The subgradient method on $$f(x) = \max_i d_{C_i}(x)$$ (which leads to alternating projections)</label>
                <label><input type="radio" name="q17" value="c"> C) Newton method</label>
                <label><input type="radio" name="q17" value="d"> D) It cannot be solved</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The subgradient method on $$f(x) = \max_i d_{C_i}(x)$$ (which leads to alternating projections)</strong><br>
                Minimize $$f(x) = \max_i d_{C_i}(x)$$ (with $$f^* = 0$$ when the intersection is nonempty). The subgradient of $$d_{C_i}$$ is $$(x - P_{C_i}(x))/d_{C_i}(x)$$; with the Polyak step size, each step projects $$x$$ onto the farthest set, i.e. the alternating projections algorithm.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: The subgradient method is well suited to regularized problems such as:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) \(\min f(x) + \lambda \|x\|_2^2\)</label>
                <label><input type="radio" name="q18" value="b"> B) \(\min f(x) + \lambda \|x\|_1\)</label>
                <label><input type="radio" name="q18" value="c"> C) \(\min f(x) + \lambda x^T x\)</label>
                <label><input type="radio" name="q18" value="d"> D) All of the above cases</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\min f(x) + \lambda \|x\|_1$$</strong><br>
                L1 regularization makes the function non-differentiable, which suits the subgradient method. L2 regularization remains differentiable.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: In the stochastic subgradient method, the choice of the index \(i_k\):</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Must be completely random</label>
                <label><input type="radio" name="q19" value="b"> B) Can be cyclic or random</label>
                <label><input type="radio" name="q19" value="c"> C) Must be in increasing order</label>
                <label><input type="radio" name="q19" value="d"> D) Does not affect convergence</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Can be cyclic or random</strong><br>
                Both cyclic and random choices can guarantee convergence under suitable conditions.
            </div>
        </div>

        <!-- Question 20: Practical considerations -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: In practice, to improve the performance of the subgradient method, we can:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Average the iterates</label>
                <label><input type="radio" name="q20" value="b"> B) Combine it with momentum</label>
                <label><input type="radio" name="q20" value="c"> C) Use adaptive step sizes</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above methods</strong><br>
                Averaging, momentum and adaptive step sizes are all techniques used to improve the subgradient method.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: The subgradient method has convergence rate:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$O(1/k)$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$O(1/\sqrt{k})$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$O(1/k^2)$$</label>
                <label><input type="radio" name="q21" value="d"> D) Linear</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$O(1/\sqrt{k})$$</strong><br>
                The subgradient method has convergence rate $$O(1/\sqrt{k})$$ for non-smooth convex functions.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The step size in the subgradient method is usually chosen:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Fixed and small</label>
                <label><input type="radio" name="q22" value="b"> B) Diminishing like $$1/\sqrt{k}$$</label>
                <label><input type="radio" name="q22" value="c"> C) Increasing</label>
                <label><input type="radio" name="q22" value="d"> D) Random</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Diminishing like $$1/\sqrt{k}$$</strong><br>
                The step size is usually chosen as $$t_k = \frac{c}{\sqrt{k}}$$ to guarantee convergence.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: For $$f(x) = |x|$$, starting from $$x_0 = 2$$, one subgradient step with $$t = 0.5$$ gives:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$x_1 = 1.5$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$x_1 = 2.5$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$x_1 = 1$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$x_1 = 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$x_1 = 1.5$$</strong><br>
                At $$x_0 = 2$$: the subgradient is $$g = 1$$. $$x_1 = 2 - 0.5 \cdot 1 = 1.5$$.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The subgradient method differs from gradient descent in that it:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Does not require a differentiable function</label>
                <label><input type="radio" name="q24" value="b"> B) Converges more slowly</label>
                <label><input type="radio" name="q24" value="c"> C) Can oscillate</label>
                <label><input type="radio" name="q24" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                The subgradient method applies to non-smooth functions, converges more slowly and can oscillate around the solution.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: The stopping criterion of the subgradient method is usually based on:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$\|g_k\| < \epsilon$$</label>
                <label><input type="radio" name="q25" value="b"> B) The maximum number of iterations</label>
                <label><input type="radio" name="q25" value="c"> C) The objective value</label>
                <label><input type="radio" name="q25" value="d"> D) B and C</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) B and C</strong><br>
                Since a subgradient need not be 0 at the solution, the number of iterations or the function value is usually used to stop.
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
    q1: 'b', q2: 'b', q3: 'b', q4: 'b', q5: 'b',
    q6: 'a', q7: 'c', q8: 'a', q9: 'b', q10: 'b',
    q11: 'b', q12: 'b', q13: 'b', q14: 'b', q15: 'b',
    q16: 'a', q17: 'b', q18: 'b', q19: 'b', q20: 'd'
,
    q21: 'b', q22: 'b', q23: 'a', q24: 'd', q25: 'd'};

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
        message = '🌟 Excellent! You have mastered the subgradient method!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand the algorithm and its convergence analysis quite well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review the step-size choices and stochastic methods.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review the basic concepts of subgradients.';
    } else {
        message = '📖 Study the subgradient method again from the beginning!';
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

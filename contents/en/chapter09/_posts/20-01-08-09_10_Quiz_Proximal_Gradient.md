---
layout: post
title: '09-10 Multiple-Choice Quiz - Proximal Gradient Method'
chapter: '09'
order: 12
owner: GitHub Copilot
lang: en
categories:
- chapter09
lesson_type: quiz
---

Before tackling the Chapter 09 multiple-choice quiz, take a moment to check your mental model of composite optimization. Most errors on proximal gradient exams come from mixing up the smooth part $$g$$ and the nonsmooth part $$h$$—forgetting that $$L$$ belongs *only* to $$\nabla g$$, misplacing the step size $$t$$ inside the soft-thresholding parameter $$\lambda t$$, or confusing the $$O(1/\varepsilon)$$ proximal rate with the $$O(1/\sqrt{\varepsilon})$$ accelerated rate. Review the four core pillars and quick warm-up check below before starting the questions.

## Key ideas: Chapter 09 Diagnostic Checklist

- **Pillar 1 — Composite Structure & Prox Definition:** For $$f = g + h$$, $$\operatorname{prox}_{t h}(y) = \arg\min_z \{\frac{1}{2t}\|z - y\|_2^2 + h(z)\}$$ uses *only* $$h$$; the smooth gradient $$\nabla g$$ enters only through the proposal $$y = x - t\nabla g(x)$$.
- **Pillar 2 — Iconic Proximal Operators:** Know the big three cold: $$h = 0 \implies \text{identity}$$; $$h = I_C \implies P_C$$ (Euclidean projection); $$h = \lambda \|\cdot\|_1 \implies S_{\lambda t}$$ (coordinatewise soft-thresholding); and $$h = \lambda \|\cdot\|_* \implies \text{SVT}$$ (singular value soft-thresholding).
- **Pillar 3 — Complexity Hierarchy:** Black-box subgradient: $$O(1/\varepsilon^2)$$; Proximal gradient (ISTA): $$O(1/\varepsilon)$$ with $$t \le 1/L$$; Accelerated proximal gradient (FISTA): $$O(1/\sqrt{\varepsilon})$$ with momentum extrapolation.
- **Pillar 4 — Practical Caveats:** Proximal gradient is monotonic for $$t \le 1/L$$, whereas FISTA is non-monotonic (Nesterov ripples) and benefits from adaptive restarting or MFISTA when $$f$$ is ill-conditioned or locally strongly convex.

### Worked example: Rapid 3-Operator Proximal Warm-Up

Let $$y = (3, -1, 0.4)^\top$$ and step size $$t = 0.5$$. Evaluate $$\operatorname{prox}_{t h}(y)$$ for three different choices of $$h$$:

1. **$$h(x) = 2\|x\|_1$$ (Lasso regularizer):**
   - Effective threshold is $$\lambda t = 2 \cdot 0.5 = 1.0$$.
   - Coordinate 1: $$3 - 1.0 = 2.0$$.
   - Coordinate 2: $$|-1| \le 1.0 \implies 0$$.
   - Coordinate 3: $$|0.4| \le 1.0 \implies 0$$.
   - Result: $$\operatorname{prox}_{t h}(y) = (2, 0, 0)^\top$$.
2. **$$h(x) = I_{\mathbb{R}_+^3}(x)$$ (Nonnegativity constraint $$x \ge 0$$):**
   - Projection clips negative entries to $$0$$: $$\operatorname{prox}_{t h}(y) = (3, 0, 0.4)^\top$$.
3. **$$h(x) = \frac{\mu}{2}\|x\|_2^2$$ with $$\mu = 2$$ (Ridge / $$\ell_2^2$$ penalty):**
   - Minimizing $$\frac{1}{2t}\|z - y\|_2^2 + \frac{\mu}{2}\|z\|_2^2$$ sets $$\frac{1}{t}(z - y) + \mu z = 0 \implies z = \frac{1}{1 + \mu t} y$$.
   - With $$\mu t = 2 \cdot 0.5 = 1$$, $$\operatorname{prox}_{t h}(y) = \frac{1}{2} y = (1.5, -0.5, 0.2)^\top$$ (pure multiplicative shrinkage—notice ridge shrinks uniformly without creating exact zeros!).

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### ⚡ **The Proximal Gradient Method**

#### **The composite problem**
Consider an objective that can be decomposed as:
$$f(x) = g(x) + h(x)$$

where:
- $$g(x)$$: convex, differentiable, $$\text{dom}(g) = \mathbb{R}^n$$
- $$h(x)$$: convex, possibly non-differentiable

#### **Main idea**
- **Approximate $$g$$:** Use a second-order Taylor expansion with Hessian $$\frac{1}{t}I$$
- **Keep $$h$$ as is:** Do not approximate the non-differentiable part
- **Optimize the combination:** Find the minimizer of the approximation + $$h$$

#### **Basic algorithm**
$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}))$$

with the **proximal mapping:**
$$\text{prox}_t(x) = \underset{z}{\arg\min} \left\{ \frac{1}{2t} \lVert x - z \rVert_2^2 + h(z) \right\}$$

#### **Intuitive explanation**
1. **Gradient step:** $$x - t\nabla g(x)$$ (gradient descent on $$g$$)
2. **Proximal correction:** Find a point close to the gradient step that also makes $$h$$ small
3. **Trade-off:** Balance between "close to the gradient step" and "small $$h$$"

### 📏 **The Proximal Mapping**

#### **Definition**
$$\text{prox}_t(x) = \underset{z}{\arg\min} \left\{ \frac{1}{2t} \lVert x - z \rVert_2^2 + h(z) \right\}$$

#### **Important properties**
- **Depends only on $$h$$:** Not on $$g$$
- **Often computable in closed form:** For many important functions $$h$$
- **Single-valued:** Unique solution (by strict convexity)
- **Non-expansive:** $$\lVert \text{prox}_t(x) - \text{prox}_t(y) \rVert \le \lVert x - y \rVert$$

#### **Important examples**

**1. L1 norm (LASSO):**
$$h(x) = \lambda \lVert x \rVert_1 \Rightarrow \text{prox}_t(x) = S_{\lambda t}(x)$$

**Soft-thresholding operator:**
$$[S_{\lambda t}(x)]_i = \begin{cases}
x_i - \lambda t & \text{if } x_i > \lambda t \\
0 & \text{if } |x_i| \le \lambda t \\
x_i + \lambda t & \text{if } x_i < -\lambda t
\end{cases}$$

**2. Indicator function (Projection):**
$$h(x) = I_C(x) \Rightarrow \text{prox}_t(x) = P_C(x)$$

**3. L2 norm:**
$$h(x) = \lambda \lVert x \rVert_2 \Rightarrow \text{prox}_t(x) = \max\left\{0, 1 - \frac{\lambda t}{\lVert x \rVert_2}\right\} x$$

### 📊 **Convergence Analysis**

#### **Assumptions**
- $$g$$ convex and differentiable with $$\nabla g$$ Lipschitz continuous (constant $$L$$)
- $$h$$ convex, with $$\text{prox}_t$$ computable

#### **Convergence theorem**
With step size $$t \le 1/L$$:
$$f(x^{(k)}) - f^* \le \frac{\lVert x^{(0)} - x^* \rVert_2^2}{2tk}$$

**Meaning:**
- **Convergence rate:** $$O(1/k)$$ (same as gradient descent)
- **Step-size condition:** $$t \le 1/L$$ (same as gradient descent)
- **Performance:** Equivalent to gradient descent in number of iterations

#### **Backtracking line search**
**Condition:**
$$g(x - tG_t(x)) > g(x) - t\nabla g(x)^T G_t(x) + \frac{t}{2} \lVert G_t(x) \rVert_2^2$$

with $$G_t(x) = \frac{x - \text{prox}_t(x - t\nabla g(x))}{t}$$

**Note:** The condition is checked only on $$g$$, not on $$f$$

### 🎯 **Example: ISTA (Iterative Soft-Thresholding Algorithm)**

#### **The LASSO problem**
$$\min_\beta \frac{1}{2} \lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$$

**Decomposition:**
- $$g(\beta) = \frac{1}{2} \lVert y - X\beta \rVert_2^2$$ (differentiable)
- $$h(\beta) = \lambda \lVert \beta \rVert_1$$ (non-differentiable)

#### **Gradient of $$g$$**
$$\nabla g(\beta) = -X^T(y - X\beta) = X^T(X\beta - y)$$

#### **ISTA update**
$$\beta^{(k)} = S_{\lambda t}(\beta^{(k-1)} + tX^T(y - X\beta^{(k-1)}))$$

**Advantages:** Simple, and much more efficient than the subgradient method

### 🎯 **Example: Matrix Completion**

#### **Problem**
$$\min_B \frac{1}{2} \sum_{(i,j) \in \Omega} (Y_{ij} - B_{ij})^2 + \lambda \lVert B \rVert_{tr}$$

**Decomposition:**
- $$g(B) = \frac{1}{2} \lVert P_\Omega(Y) - P_\Omega(B) \rVert_F^2$$ (differentiable)
- $$h(B) = \lambda \lVert B \rVert_{tr}$$ (trace norm, non-differentiable)

#### **Projection operator**
$$[P_\Omega(B)]_{ij} = \begin{cases}
B_{ij} & \text{if } (i,j) \in \Omega \\
0 & \text{otherwise}
\end{cases}$$

#### **Gradient of $$g$$**
$$\nabla g(B) = -(P_\Omega(Y) - P_\Omega(B))$$

#### **Proximal mapping for the trace norm**
$$\text{prox}_t(B) = S_{\lambda t}(B)$$ (matrix soft-thresholding)

If $$B = U\Sigma V^T$$ (SVD), then:
$$S_{\lambda t}(B) = U\Sigma_{\lambda t} V^T$$

with $$(\Sigma_{\lambda t})_{ii} = \max\{\Sigma_{ii} - \lambda t, 0\}$$

#### **Soft-Impute Algorithm**
$$B^{(k)} = S_{\lambda}(P_\Omega(Y) + P_\Omega^\perp(B^{(k-1)}))$$

### 🔄 **Special Cases**

Proximal gradient is a **general method** that includes:

#### **1. Gradient Descent**
$$h = 0 \Rightarrow \text{prox}_t(x) = x$$
$$x^{(k)} = x^{(k-1)} - t\nabla g(x^{(k-1)})$$

#### **2. Projected Gradient Descent**
$$h = I_C \Rightarrow \text{prox}_t(x) = P_C(x)$$
$$x^{(k)} = P_C(x^{(k-1)} - t\nabla g(x^{(k-1)}))$$

#### **3. Proximal Minimization Algorithm (PMA)**
$$g = 0 \Rightarrow x^{(k)} = \text{prox}_t(x^{(k-1)})$$

### ⚡ **Accelerated Proximal Gradient (FISTA)**

#### **Idea**
Add **momentum** to accelerate convergence from $$O(1/k)$$ to $$O(1/k^2)$$

#### **Algorithm**
$$v = x^{(k-1)} + \frac{k-2}{k+1}(x^{(k-1)} - x^{(k-2)})$$
$$x^{(k)} = \text{prox}_{t_k}(v - t_k \nabla g(v))$$

#### **Momentum weight**
$$\frac{k-2}{k+1} \to 1$$ as $$k \to \infty$$

#### **Characteristics**
- **Convergence rate:** $$O(1/k^2)$$ - optimal for first-order methods
- **Not monotonic:** May increase temporarily ("Nesterov ripples")
- **Highly effective:** Especially good for problems with a large condition number

#### **FISTA for LASSO**
A significant improvement over ISTA and the subgradient method

### 🔄 **Comparing the Methods**

| Method | Condition | Convergence rate | Applications |
|-------------|-----------|---------------|----------|
| **Gradient Descent** | $$f$$ differentiable | $$O(1/k)$$ | Smooth optimization |
| **Subgradient** | $$f$$ convex | $$O(1/\sqrt{k})$$ | Non-smooth |
| **Proximal Gradient** | $$f = g + h$$, $$g$$ smooth | $$O(1/k)$$ | Composite problems |
| **Accelerated Proximal** | $$f = g + h$$, $$g$$ smooth | $$O(1/k^2)$$ | Fast composite |

### 🛠️ **Practical Techniques**

#### **When to use Proximal Gradient:**
- **Composite functions:** $$f = g + h$$ with $$g$$ smooth, $$h$$ non-smooth
- **Regularization problems:** LASSO, elastic net, group LASSO
- **Constrained optimization:** Projected gradient descent
- **Matrix problems:** Matrix completion, robust PCA
- **Sparse optimization:** Feature selection, compressed sensing

#### **Implementation requirements:**
1. **Compute $$\nabla g$$:** The gradient of the smooth part must be computable
2. **Compute $$\text{prox}_t$$:** A closed-form formula or an efficient solver is needed
3. **Lipschitz constant $$L$$:** To choose a suitable step size

#### **Debugging and tuning:**
- **Check the proximal mapping:** Verify its correctness
- **Step size selection:** Fixed ($$t = 1/L$$) or backtracking
- **Convergence monitoring:** Track $$f(x^{(k)})$$
- **Acceleration:** Try FISTA if speed-up is needed

### 📈 **Real-World Applications**

#### **1. Machine Learning**
- **LASSO Regression:** Feature selection
- **Elastic Net:** Combines L1 and L2 regularization
- **Group LASSO:** Structured sparsity
- **Sparse Logistic Regression:** Classification with feature selection

#### **2. Signal Processing**
- **Compressed Sensing:** Recovering sparse signals
- **Image Denoising:** Total variation regularization
- **Matrix Completion:** Collaborative filtering, recommender systems

#### **3. Computer Vision**
- **Image Segmentation:** Total variation methods
- **Optical Flow:** Regularized motion estimation
- **Structure from Motion:** Bundle adjustment with sparsity

#### **4. Statistics**
- **Variable Selection:** High-dimensional regression
- **Robust Statistics:** Huber loss, quantile regression
- **Graphical Models:** Sparse precision matrix estimation

### 💡 **Illustrative Examples**

#### **Problem:** $$\min_x \frac{1}{2}(x-2)^2 + |x|$$

**Decomposition:**
- $$g(x) = \frac{1}{2}(x-2)^2$$, $$\nabla g(x) = x-2$$
- $$h(x) = |x|$$

**Proximal mapping:**
$$\text{prox}_t(x) = S_t(x) = \begin{cases}
x - t & \text{if } x > t \\
0 & \text{if } |x| \le t \\
x + t & \text{if } x < -t
\end{cases}$$

**Proximal gradient step:**
1. Gradient step: $$x - t(x-2) = (1-t)x + 2t$$
2. Soft-thresholding: $$\text{prox}_t((1-t)x + 2t)$$

### 🎯 **Connections to Other Chapters**

#### **From the previous chapter:**
- **Chapter 08:** The subgradient method for non-smooth functions
- **Chapter 07:** Subgradients and subdifferentials
- **Chapter 06:** Gradient descent for smooth functions

#### **Advantages of Proximal Gradient:**
- **Faster than subgradient:** $$O(1/k)$$ vs $$O(1/\sqrt{k})$$
- **More general than gradient descent:** Handles non-smooth components
- **Can be accelerated:** FISTA achieves $$O(1/k^2)$$

#### **Looking ahead:**
- **ADMM:** Alternating Direction Method of Multipliers
- **Primal-dual methods:** Handle constrained problems
- **Stochastic variants:** Mini-batch and online versions

### 🌟 **Theoretical Significance**

#### **The proximal operator as a "generalized gradient":**
- **Gradient:** $$\nabla f(x)$$ for smooth functions
- **Subgradient:** $$\partial f(x)$$ for non-smooth functions
- **Proximal operator:** $$\text{prox}_t$$ for composite functions

#### **Moreau envelope:**
$$f_t(x) = \min_z \left\{ f(z) + \frac{1}{2t}\lVert x - z \rVert^2 \right\}$$

**Property:** $$f_t$$ is smooth with $$\nabla f_t(x) = \frac{x - \text{prox}_t(x)}{t}$$

#### **Connection to variational analysis:**
- Proximal gradient ↔ Forward-backward splitting
- Acceleration ↔ Inertial methods
- Convergence rates ↔ Complexity theory

### 💡 **Practical Tips**

#### **Choosing a method:**
1. **Smooth function:** Gradient descent
2. **Non-smooth function:** Subgradient method
3. **Composite function with a computable prox:** Proximal gradient
4. **Need acceleration:** FISTA
5. **Constrained:** Projected gradient descent

#### **Implementation tips:**
- **Vectorization:** Exploit parallel computation
- **Warm start:** Use the previous solution as initialization
- **Adaptive step size:** Backtracking line search
- **Early stopping:** Monitoring convergence criteria

#### **Common pitfalls:**
- **Wrong proximal mapping:** Check the formula carefully
- **Step size too large:** May fail to converge
- **Not checking the Lipschitz constant:** Affects convergence
- **Forgetting to normalize data:** Affects numerical stability

---

💡 **Tip:** The proximal gradient method is the perfect bridge between smooth and non-smooth optimization, and is especially powerful for machine learning with regularization!

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

This multiple-choice quiz tests your understanding of the proximal gradient method, proximal operators, composite optimization and acceleration methods such as FISTA.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🎯 Quiz: The Proximal Gradient Method</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1 -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: The proximal gradient method applies to problems of the form:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(\min f(x)\) with \(f\) differentiable</label>
                <label><input type="radio" name="q1" value="b"> B) \(\min f(x) = g(x) + h(x)\) with \(g\) differentiable, \(h\) convex</label>
                <label><input type="radio" name="q1" value="c"> C) \(\min f(x)\) with \(f\) non-convex</label>
                <label><input type="radio" name="q1" value="d"> D) \(\min f(x)\) with linear constraints</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\min f(x) = g(x) + h(x)$$ with $$g$$ differentiable, $$h$$ convex</strong><br>
                The proximal gradient method is designed for composite optimization with $$g$$ differentiable and $$h$$ possibly non-differentiable.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The proximal operator of a function \(h\) is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\text{prox}_h(v) = \arg\min_x \{h(x) + \frac{1}{2}\|x - v\|^2\}\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\text{prox}_h(v) = \arg\min_x \{h(x) - \frac{1}{2}\|x - v\|^2\}\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\text{prox}_h(v) = \arg\min_x \{h(x) + \|x - v\|\}\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\text{prox}_h(v) = v - \nabla h(v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\text{prox}_h(v) = \arg\min_x \{h(x) + \frac{1}{2}\|x - v\|^2\}$$</strong><br>
                The proximal operator balances minimizing $$h(x)$$ against keeping $$x$$ close to $$v$$.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: The update formula of the proximal gradient method is:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(x^{(k+1)} = x^{(k)} - t \nabla g(x^{(k)})\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(x^{(k+1)} = \text{prox}_{th}(x^{(k)} - t \nabla g(x^{(k)}))\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(x^{(k+1)} = \text{prox}_{tg}(x^{(k)} - t \nabla h(x^{(k)}))\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(x^{(k+1)} = x^{(k)} - t(\nabla g(x^{(k)}) + \nabla h(x^{(k)}))\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$x^{(k+1)} = \text{prox}_{th}(x^{(k)} - t \nabla g(x^{(k)}))$$</strong><br>
                Take a gradient step on $$g$$, then apply the proximal operator of $$h$$.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The proximal operator of \(h(x) = \lambda\|x\|_1\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) \(\text{prox}_{\lambda\|\cdot\|_1}(v) = v - \lambda\)</label>
                <label><input type="radio" name="q4" value="b"> B) \(\text{prox}_{\lambda\|\cdot\|_1}(v) = \text{sign}(v) \max(|v| - \lambda, 0)\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(\text{prox}_{\lambda\|\cdot\|_1}(v) = \frac{v}{1 + \lambda}\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(\text{prox}_{\lambda\|\cdot\|_1}(v) = v\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\text{prox}_{\lambda\|\cdot\|_1}(v) = \text{sign}(v) \max(|v| - \lambda, 0)$$</strong><br>
                This is the soft-thresholding operator, which shrinks each component toward 0 by $$\lambda$$.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The proximal operator of \(h(x) = \frac{\lambda}{2}\|x\|_2^2\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = \frac{v}{1 + \lambda}\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = v - \lambda v\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = v\)</label>
                <label><input type="radio" name="q5" value="d"> D) \(\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = \frac{v}{1 + \lambda}$$</strong><br>
                The proximal operator of a quadratic function is a shrinkage with factor $$\frac{1}{1 + \lambda}$$.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: The convergence rate of the proximal gradient method is:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(O(1/k)\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(O(1/\sqrt{k})\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(O(e^{-k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$O(1/k)$$</strong><br>
                The proximal gradient method converges at rate $$O(1/k)$$, like gradient descent for convex functions.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: The proximal gradient method is appropriate when:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Both \(g\) and \(h\) are differentiable</label>
                <label><input type="radio" name="q7" value="b"> B) \(g\) is differentiable and the proximal operator of \(h\) is easy to compute</label>
                <label><input type="radio" name="q7" value="c"> C) Neither \(g\) nor \(h\) is differentiable</label>
                <label><input type="radio" name="q7" value="d"> D) The objective is non-convex</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$g$$ is differentiable and the proximal operator of $$h$$ is easy to compute</strong><br>
                The method is effective when the gradient of $$g$$ and the proximal operator of $$h$$ can be computed easily.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: FISTA (Fast Iterative Shrinkage-Thresholding Algorithm) is:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) A slow version of proximal gradient</label>
                <label><input type="radio" name="q8" value="b"> B) An accelerated version of proximal gradient with momentum</label>
                <label><input type="radio" name="q8" value="c"> C) An algorithm for non-convex problems</label>
                <label><input type="radio" name="q8" value="d"> D) An algorithm only for L1 regularization</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) An accelerated version of proximal gradient with momentum</strong><br>
                FISTA uses momentum to achieve the convergence rate $$O(1/k^2)$$ instead of $$O(1/k)$$.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The convergence rate of FISTA is:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(O(1/k)\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(O(1/\sqrt{k})\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(O(e^{-k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$O(1/k^2)$$</strong><br>
                FISTA achieves the optimal rate $$O(1/k^2)$$ for first-order methods on convex functions.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: In FISTA, the momentum parameter \(t_k\) is updated by the formula:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(t_{k+1} = \frac{1 + \sqrt{1 + 4t_k^2}}{2}\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(t_{k+1} = t_k + 1\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(t_{k+1} = 0.9 t_k\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(t_{k+1} = 1\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$t_{k+1} = \frac{1 + \sqrt{1 + 4t_k^2}}{2}$$</strong><br>
                This is the special formula in FISTA that guarantees the optimal convergence rate.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: The proximal operator has the property of:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Not increasing distances (non-expansive, for convex $$h$$)</label>
                <label><input type="radio" name="q11" value="b"> B) Increasing distances</label>
                <label><input type="radio" name="q11" value="c"> C) Being discontinuous</label>
                <label><input type="radio" name="q11" value="d"> D) Applying only to differentiable functions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Not increasing distances (non-expansive, for convex $$h$$)</strong><br>
                $$\|\text{prox}_h(u) - \text{prox}_h(v)\| \leq \|u - v\|$$ for all $$u, v$$; this is an important property for the convergence analysis.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The Lasso problem \(\min \frac{1}{2}\|Ax - b\|_2^2 + \lambda\|x\|_1\) can be solved with:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Gradient descent</label>
                <label><input type="radio" name="q12" value="b"> B) Proximal gradient with \(g(x) = \frac{1}{2}\|Ax - b\|_2^2\), \(h(x) = \lambda\|x\|_1\)</label>
                <label><input type="radio" name="q12" value="c"> C) Newton method</label>
                <label><input type="radio" name="q12" value="d"> D) It cannot be solved</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Proximal gradient with $$g(x) = \frac{1}{2}\|Ax - b\|_2^2$$, $$h(x) = \lambda\|x\|_1$$</strong><br>
                Lasso is the textbook example of composite optimization with $$g$$ differentiable and $$h$$ non-differentiable.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: In matrix completion, the proximal operator of the nuclear norm performs:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Hard thresholding of the singular values</label>
                <label><input type="radio" name="q13" value="b"> B) Soft thresholding of the singular values</label>
                <label><input type="radio" name="q13" value="c"> C) No change to the matrix</label>
                <label><input type="radio" name="q13" value="d"> D) Setting all entries to 0</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Soft thresholding of the singular values</strong><br>
                The proximal operator of the nuclear norm $$\|X\|_*$$ computes an SVD and soft-thresholds the singular values.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: Can backtracking line search be used in the proximal gradient method?</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) No, because the function is not differentiable</label>
                <label><input type="radio" name="q14" value="b"> B) Yes, based on a sufficient-decrease condition for the composite function</label>
                <label><input type="radio" name="q14" value="c"> C) Only when \(h = 0\)</label>
                <label><input type="radio" name="q14" value="d"> D) Only for FISTA</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Yes, based on a sufficient-decrease condition for the composite function</strong><br>
                Backtracking can be used with the condition $$f(x^+) \leq Q_t(x^+, x)$$, where $$Q_t$$ is the quadratic upper bound.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: The proximal operator of the indicator function \(I_C(x)\) of a convex set \(C\) is:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(\text{prox}_{I_C}(v) = v\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(\text{prox}_{I_C}(v) = P_C(v)\) (projection onto \(C\))</label>
                <label><input type="radio" name="q15" value="c"> C) \(\text{prox}_{I_C}(v) = 0\)</label>
                <label><input type="radio" name="q15" value="d"> D) It does not exist</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\text{prox}_{I_C}(v) = P_C(v)$$ (projection onto $$C$$)</strong><br>
                The proximal operator of an indicator function is exactly the projection onto the constraint set.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: The composite gradient mapping \(G_t(x)\) is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(G_t(x) = \nabla g(x)\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(G_t(x) = \frac{1}{t}(x - \text{prox}_{th}(x - t\nabla g(x)))\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(G_t(x) = \text{prox}_{th}(x)\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(G_t(x) = x - t\nabla g(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$G_t(x) = \frac{1}{t}(x - \text{prox}_{th}(x - t\nabla g(x)))$$</strong><br>
                The composite gradient mapping generalizes the gradient to composite functions and is used in stopping criteria.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: Is acceleration (such as FISTA) always beneficial?</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Always beneficial</label>
                <label><input type="radio" name="q17" value="b"> B) No, it can slow convergence in some cases</label>
                <label><input type="radio" name="q17" value="c"> C) Only beneficial for quadratic functions</label>
                <label><input type="radio" name="q17" value="d"> D) Only beneficial for L1 regularization</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) No, it can slow convergence in some cases</strong><br>
                Acceleration can cause oscillation and slow convergence, especially for poorly conditioned functions or in the early phase.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: Compared with the subgradient method, the proximal gradient method is:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Slower</label>
                <label><input type="radio" name="q18" value="b"> B) Faster and more stable</label>
                <label><input type="radio" name="q18" value="c"> C) Applying only to differentiable functions</label>
                <label><input type="radio" name="q18" value="d"> D) Has the same convergence rate</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Faster and more stable</strong><br>
                Proximal gradient has rate $$O(1/k)$$ versus $$O(1/\sqrt{k})$$ for subgradient, and oscillates less.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: When \(g\) is strongly convex, the proximal gradient method converges at rate:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(O(1/k)\)</label>
                <label><input type="radio" name="q19" value="b"> B) \(O(\rho^k)\) with \(\rho < 1\) (linear)</label>
                <label><input type="radio" name="q19" value="c"> C) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q19" value="d"> D) \(O(1/\sqrt{k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$O(\rho^k)$$ with $$\rho < 1$$ (linear)</strong><br>
                Strong convexity of $$g$$ guarantees a linear (geometric) convergence rate for the proximal gradient method.
            </div>
        </div>

        <!-- Question 20: Practical considerations -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: In practice, to apply the proximal gradient method effectively, we need:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) The proximal operator of \(h\) to have a closed-form solution</label>
                <label><input type="radio" name="q20" value="b"> B) \(g\) to have a Lipschitz gradient</label>
                <label><input type="radio" name="q20" value="c"> C) A suitable step size</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above conditions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above conditions</strong><br>
                To be effective, we need an easily computed proximal operator, a Lipschitz gradient for $$g$$, and a suitable step size.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: The proximal operator of $$f(x) = \lambda|x|$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$\text{prox}_f(x) = \text{sign}(x)\max\{|x|-\lambda, 0\}$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$\text{prox}_f(x) = x - \lambda$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$\text{prox}_f(x) = \lambda x$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$\text{prox}_f(x) = |x|$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\text{prox}_f(x) = \text{sign}(x)\max\{|x|-\lambda, 0\}$$</strong><br>
                This is the soft-thresholding operator, one of the most important proximal operators.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The proximal gradient method combines:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Gradient descent + proximal operator</label>
                <label><input type="radio" name="q22" value="b"> B) Newton method + gradient</label>
                <label><input type="radio" name="q22" value="c"> C) SGD + momentum</label>
                <label><input type="radio" name="q22" value="d"> D) Line search + Hessian</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Gradient descent + proximal operator</strong><br>
                Proximal gradient method: $$x^{(k+1)} = \text{prox}_{th}(x^{(k)} - t\nabla g(x^{(k)}))$$.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: FISTA is an algorithm that:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Accelerates proximal gradient</label>
                <label><input type="radio" name="q23" value="b"> B) Is an improved Newton method</label>
                <label><input type="radio" name="q23" value="c"> C) Stochastic gradient descent</label>
                <label><input type="radio" name="q23" value="d"> D) Interior point method</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Accelerates proximal gradient</strong><br>
                FISTA (Fast Iterative Shrinkage-Thresholding Algorithm) is the accelerated version of proximal gradient.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The LASSO problem has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_2$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$\min \|Ax-b\|_1 + \lambda\|x\|_2$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$\min \|Ax-b\|_\infty + \lambda\|x\|_1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$$</strong><br>
                LASSO uses L1 regularization: $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$$.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: For $$\text{prox}_{\lambda|\cdot|}(2)$$ with $$\lambda = 0.5$$, the result is:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$1.5$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$2$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$1$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$0.5$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$1.5$$</strong><br>
                $$\text{prox}_{0.5|\cdot|}(2) = \text{sign}(2)\max\{|2|-0.5, 0\} = 1 \cdot 1.5 = 1.5$$.
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
    q1: 'b', q2: 'a', q3: 'b', q4: 'b', q5: 'a',
    q6: 'b', q7: 'b', q8: 'b', q9: 'a', q10: 'a',
    q11: 'a', q12: 'b', q13: 'b', q14: 'b', q15: 'b',
    q16: 'b', q17: 'b', q18: 'b', q19: 'b', q20: 'd'
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
        message = '🌟 Excellent! You have mastered the proximal gradient method!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand proximal operators and FISTA well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review proximal operators and acceleration.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review composite optimization and proximal operators.';
    } else {
        message = '📖 Study the proximal gradient method again from the beginning!';
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

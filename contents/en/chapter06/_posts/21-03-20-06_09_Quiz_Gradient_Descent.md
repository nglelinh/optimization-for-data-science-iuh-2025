---
layout: post
title: '06-08 Multiple-Choice Quiz - Gradient Descent'
chapter: '06'
order: 16
owner: GitHub Copilot
lang: en
categories:
- chapter06
lesson_type: quiz
---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### 🎯 **Basic Gradient Descent**

**Optimization problem:**
$$\min_x f(x), \quad f \text{ differentiable and } \text{dom}(f) = \mathbb{R}^n$$

**Update rule:**
$$x^{(k)} = x^{(k-1)} - t \nabla f(x^{(k-1)}), \quad k = 1, 2, 3, \ldots$$

**Pseudocode:**
1. **Given a starting point** $$x \in \text{dom}(f)$$
2. **Repeat:**
   - Determine the descent direction: $$\Delta x = -\nabla f(x)$$
   - Line search: choose a step size $$t > 0$$
   - Update: $$x = x + t \Delta x$$
3. **Until** the stopping criterion is satisfied

**Geometric interpretation:**
- The gradient $$\nabla f(x)$$ points in the direction of steepest ascent
- The negative gradient $$-\nabla f(x)$$ points in the direction of steepest descent
- At a minimum: $$\nabla f(x^*) = 0$$

### 📏 **Choosing the Step Size**

#### **1. Fixed step size**
$$t = \text{const} > 0$$

**Advantages:** Simple, fast to compute
**Disadvantages:** Hard to choose a suitable value

#### **2. Backtracking line search**
**Armijo condition:**
$$f(x + t\Delta x) \le f(x) + \alpha t \nabla f(x)^T \Delta x$$

**Algorithm:**
- Start with $$t = t_0$$
- If the Armijo condition is not satisfied: $$t := \beta t$$ (with $$0 < \beta < 1$$)
- Repeat until it is satisfied

**Common parameters:** $$\alpha = 0.01 \div 0.3$$, $$\beta = 0.1 \div 0.8$$

#### **3. Exact line search**
$$t^* = \arg\min_{t > 0} f(x + t\Delta x)$$

**Advantages:** Theoretically optimal
**Disadvantages:** Computationally expensive

### 📊 **Convergence Analysis**

#### **Lipschitz condition**
The gradient $$\nabla f$$ is Lipschitz continuous with constant $$L > 0$$:
$$\lVert \nabla f(x) - \nabla f(y) \rVert_2 \le L \lVert x - y \rVert_2$$

#### **Convergence theorem for convex functions**
With a fixed step size $$t \le \frac{1}{L}$$:
$$f(x^{(k)}) - f^* \le \frac{\lVert x^{(0)} - x^* \rVert_2^2}{2tk}$$

**Convergence rate:** $$O(1/k)$$ - sublinear convergence

#### **Convergence theorem for strongly convex functions**
If $$f$$ is strongly convex with parameter $$m > 0$$:
$$f(x^{(k)}) - f^* \le \left(1 - \frac{m}{L}\right)^k \left(f(x^{(0)}) - f^*\right) \quad (t = 1/L)$$

**Convergence rate:** $$O(\rho^k)$$ with $$\rho < 1$$ - linear convergence

#### **Condition number**
$$\kappa = \frac{L}{m}$$ - the ratio of the Lipschitz constant to the strong convexity parameter

- Small $$\kappa$$: fast convergence
- Large $$\kappa$$: slow convergence (ill-conditioned)

### 🎲 **Stochastic Gradient Descent (SGD)**

#### **Sum problem**
$$\min_x f(x) = \min_x \sum_{i=1}^m f_i(x)$$

#### **Batch Gradient Descent**
$$x^{(k)} = x^{(k-1)} - t_k \sum_{i=1}^m \nabla f_i(x^{(k-1)})$$

**Cost:** $$O(m)$$ gradient evaluations per iteration

#### **Stochastic Gradient Descent**
$$x^{(k)} = x^{(k-1)} - t_k \nabla f_{i_k}(x^{(k-1)})$$

**Cost:** $$O(1)$$ gradient evaluations per iteration

#### **Index selection strategies**
- **Cyclic rule:** $$i_k = 1, 2, \ldots, m, 1, 2, \ldots$$
- **Randomized rule:** $$i_k$$ chosen at random from $$\{1, 2, \ldots, m\}$$

#### **Mini-batch SGD**
$$x^{(k)} = x^{(k-1)} - t_k \frac{1}{b} \sum_{i \in \mathcal{B}_k} \nabla f_i(x^{(k-1)})$$

With $$\mathcal{B}_k$$ a mini-batch of size $$b$$

### ⚡ **Gradient Descent with Momentum**

#### **Classical Momentum**
$$\begin{align}
v^{(k)} &= \beta v^{(k-1)} + \nabla f(x^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align}$$

#### **Nesterov Accelerated Gradient**
$$\begin{align}
v^{(k)} &= \beta v^{(k-1)} + \nabla f(x^{(k-1)} - t\beta v^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align}$$

**Common parameter:** $$\beta = 0.9$$

**Advantages:**
- Accelerates convergence
- Dampens local oscillations
- Reduces the effect of noise

### 🔄 **Comparing the Methods**

| Method | Speed/iteration | Memory | Convergence | Use case |
|-------------|----------------|--------|--------|----------|
| **Batch GD** | Slow | High | Stable | Small datasets |
| **SGD** | Fast | Low | Noisy | Large datasets |
| **Mini-batch** | Medium | Medium | Balanced | Practice |
| **Momentum** | Fast | Low | Accelerated | Deep learning |

### 🛠️ **Practical Techniques**

#### **Learning Rate Scheduling**
- **Step decay:** $$t_k = t_0 \cdot \gamma^{\lfloor k/s \rfloor}$$
- **Exponential decay:** $$t_k = t_0 \cdot e^{-\lambda k}$$
- **Polynomial decay:** $$t_k = t_0 \cdot (1 + \lambda k)^{-p}$$

#### **Adaptive Methods**
- **AdaGrad:** Adapts the learning rate based on the gradient history
- **RMSprop:** Improves AdaGrad with an exponential moving average
- **Adam:** Combines momentum with an adaptive learning rate

#### **Regularization**
- **L1 regularization:** $$f(x) + \lambda \lVert x \rVert_1$$
- **L2 regularization:** $$f(x) + \frac{\lambda}{2} \lVert x \rVert_2^2$$
- **Dropout:** Randomization in neural networks

### 📈 **Real-World Applications**

#### **Machine Learning**
- **Linear regression:** $$\min_w \lVert Xw - y \rVert_2^2$$
- **Logistic regression:** $$\min_w \sum_i \log(1 + e^{-y_i w^T x_i})$$
- **Neural networks:** Backpropagation + SGD

#### **Deep Learning**
- **Convolutional Neural Networks (CNNs)**
- **Recurrent Neural Networks (RNNs)**
- **Transformer models**

#### **Optimization Problems**
- **Portfolio optimization**
- **Signal processing**
- **Computer vision**

### 🔍 **Stopping Criteria**

#### **Gradient-based**
$$\lVert \nabla f(x^{(k)}) \rVert_2 < \epsilon$$

#### **Function value-based**
$$|f(x^{(k)}) - f(x^{(k-1)})| < \epsilon$$

#### **Parameter-based**
$$\lVert x^{(k)} - x^{(k-1)} \rVert_2 < \epsilon$$

#### **Maximum iterations**
$$k > k_{\max}$$

### ⚠️ **Challenges and Solutions**

#### **Common problems:**
- **Vanishing/exploding gradients:** Gradients that are too small or too large
- **Saddle points:** Saddle points in high-dimensional spaces
- **Local minima:** Local minima (for non-convex functions)
- **Ill-conditioning:** Large condition number

#### **Solutions:**
- **Gradient clipping:** Limit the gradient magnitude
- **Batch normalization:** Normalize the input of each layer
- **Residual connections:** Skip connections in deep networks
- **Preconditioning:** Transform the optimization space

### 💡 **Practical Tips**

#### **Choosing the learning rate:**
1. Start with $$t = 0.01$$
2. Increase/decrease by powers of 10
3. Watch the loss curve
4. Use learning rate scheduling

#### **Debugging:**
- Check the gradient implementation
- Visualize loss curve
- Monitor gradient norms
- Use validation set

#### **Speeding up:**
- Use mini-batches instead of the full batch
- Parallel/distributed training
- GPU acceleration
- Mixed precision training

---

💡 **Tip:** Gradient descent is the foundation of modern machine learning. Understanding its variants and optimization techniques will help you train models more effectively!

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
</style>

This multiple-choice quiz tests your understanding of the gradient descent algorithm and its variants, including step-size selection, convergence analysis, SGD and momentum.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Multiple-Choice Quiz: Gradient Descent</h2>
        <p>Choose the best answer for each question. The quiz focuses on the basic concepts and practical applications of gradient descent.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Question 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Question 1 -->
        <div class="question" id="q1">
            <h3>Question 1: The basic update rule of gradient descent is:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(x^{(k)} = x^{(k-1)} + t \nabla f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(x^{(k)} = x^{(k-1)} - t \nabla f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(x^{(k)} = x^{(k-1)} - t \nabla^2 f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(x^{(k)} = x^{(k-1)} + t f(x^{(k-1)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$x^{(k)} = x^{(k-1)} - t \nabla f(x^{(k-1)})$$</strong><br>
                Gradient descent moves in the direction opposite to the gradient to decrease the objective value.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The descent direction in gradient descent is:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\Delta x = \nabla f(x)\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\Delta x = -\nabla f(x)\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\Delta x = \nabla^2 f(x)\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\Delta x = f(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\Delta x = -\nabla f(x)$$</strong><br>
                The descent direction is the negative gradient, the direction of fastest decrease of the function.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: If the step size $$t$$ is too large, gradient descent may:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Converge faster</label>
                <label><input type="radio" name="q3" value="b"> B) Overshoot the minimum and diverge</label>
                <label><input type="radio" name="q3" value="c"> C) Stop immediately</label>
                <label><input type="radio" name="q3" value="d"> D) Find the exact solution</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Overshoot the minimum and diverge</strong><br>
                A step size that is too large can make the algorithm oscillate or diverge away from the optimal solution.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: If the step size $$t$$ is too small, gradient descent will:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Converge very slowly</label>
                <label><input type="radio" name="q4" value="b"> B) Diverge</label>
                <label><input type="radio" name="q4" value="c"> C) Oscillate</label>
                <label><input type="radio" name="q4" value="d"> D) Stop immediately</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Converge very slowly</strong><br>
                A step size that is too small makes the algorithm update very slowly, needing many iterations to converge.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: Backtracking line search works by:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Gradually increasing the step size</label>
                <label><input type="radio" name="q5" value="b"> B) Starting with a large step size and gradually decreasing it</label>
                <label><input type="radio" name="q5" value="c"> C) Using a fixed step size</label>
                <label><input type="radio" name="q5" value="d"> D) Computing second derivatives</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Starting with a large step size and gradually decreasing it</strong><br>
                Backtracking starts with a large step and shrinks it until sufficient decrease is achieved (the Armijo condition).
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: The Armijo condition in backtracking requires:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(f(x + t\Delta x) \leq f(x)\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(f(x + t\Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(f(x + t\Delta x) = f(x)\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\nabla f(x + t\Delta x) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$f(x + t\Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x$$</strong><br>
                The Armijo condition guarantees sufficient decrease with parameter $$\alpha \in (0, 0.5)$$.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: Exact line search finds the step size by:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Using a fixed formula</label>
                <label><input type="radio" name="q7" value="b"> B) Minimizing \(f(x - t \nabla f(x))\) over \(t\)</label>
                <label><input type="radio" name="q7" value="c"> C) Choosing at random</label>
                <label><input type="radio" name="q7" value="d"> D) Using second derivatives</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Minimizing $$f(x - t \nabla f(x))$$ over $$t$$</strong><br>
                Exact line search finds the optimal step size by solving a one-dimensional optimization problem.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The Lipschitz condition on the gradient means:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\|\nabla f(x) - \nabla f(y)\| \leq L \|x - y\|\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(\|f(x) - f(y)\| \leq L \|x - y\|\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(\nabla f(x) = L\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(f(x) \leq L\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\|\nabla f(x) - \nabla f(y)\| \leq L \|x - y\|$$</strong><br>
                The Lipschitz condition ensures the gradient does not change too fast, which is important for convergence analysis.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: For a convex function with Lipschitz gradient, gradient descent converges at the rate:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(O(1/k)\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(O(\log k)\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(O(e^{-k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$O(1/k)$$</strong><br>
                Gradient descent has a sublinear convergence rate $$O(1/k)$$ for convex functions with Lipschitz gradient.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: Stochastic Gradient Descent (SGD) differs from Batch GD in that:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) SGD uses all the data in each update</label>
                <label><input type="radio" name="q10" value="b"> B) SGD uses only one data sample in each update</label>
                <label><input type="radio" name="q10" value="c"> C) SGD does not use gradients</label>
                <label><input type="radio" name="q10" value="d"> D) SGD always converges faster</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) SGD uses only one data sample in each update</strong><br>
                SGD updates the parameters using the gradient of a single sample instead of the whole dataset.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: The main advantage of SGD over Batch GD is:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Higher accuracy</label>
                <label><input type="radio" name="q11" value="b"> B) Lower computational cost per update</label>
                <label><input type="radio" name="q11" value="c"> C) It always converges to the optimal solution</label>
                <label><input type="radio" name="q11" value="d"> D) No need to tune the learning rate</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Lower computational cost per update</strong><br>
                SGD costs O(1) per update compared with O(m) for Batch GD, which is very efficient for big data.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: Mini-batch Gradient Descent is a combination of:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) SGD and Newton's method</label>
                <label><input type="radio" name="q12" value="b"> B) Batch GD and SGD</label>
                <label><input type="radio" name="q12" value="c"> C) Gradient descent and momentum</label>
                <label><input type="radio" name="q12" value="d"> D) Line search and a fixed step</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Batch GD and SGD</strong><br>
                Mini-batch uses a small subset of the data (typically 32-256 samples) to balance efficiency and stability.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The update rule of Gradient Descent with momentum is:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(v^{(k)} = \beta v^{(k-1)} + \nabla f(x^{(k-1)})\), \(x^{(k)} = x^{(k-1)} + t v^{(k)}\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)})\), \(x^{(k)} = x^{(k-1)} - t v^{(k)}\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(x^{(k)} = x^{(k-1)} - t \beta \nabla f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(x^{(k)} = \beta x^{(k-1)} - t \nabla f(x^{(k-1)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)})$$, $$x^{(k)} = x^{(k-1)} - t v^{(k)}$$</strong><br>
                Momentum accumulates a velocity as an exponentially weighted moving average of the gradients. (The classical form $$v^{(k)} = \beta v^{(k-1)} + \nabla f(x^{(k-1)})$$, $$x^{(k)} = x^{(k-1)} - t v^{(k)}$$ is also correct and only rescales $$t$$; option A is wrong because it moves along $$+v$$, which increases the objective.)
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: The momentum coefficient $$\beta$$ is usually chosen in the range:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) [0.1, 0.3]</label>
                <label><input type="radio" name="q14" value="b"> B) [0.5, 0.7]</label>
                <label><input type="radio" name="q14" value="c"> C) [0.9, 0.99]</label>
                <label><input type="radio" name="q14" value="d"> D) [1.0, 1.5]</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) [0.9, 0.99]</strong><br>
                The momentum coefficient is usually chosen large (0.9 or 0.99) to keep a long "memory" of previous gradients.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: Momentum helps gradient descent to:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Reduce oscillations and accelerate convergence</label>
                <label><input type="radio" name="q15" value="b"> B) Improve numerical accuracy</label>
                <label><input type="radio" name="q15" value="c"> C) Reduce memory usage</label>
                <label><input type="radio" name="q15" value="d"> D) Eliminate local minima completely</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Reduce oscillations and accelerate convergence</strong><br>
                Momentum smooths the optimization process, reduces oscillations and accelerates progress along consistent directions.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: Nesterov Accelerated Gradient (NAG) differs from ordinary momentum in that:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) It uses a different momentum coefficient</label>
                <label><input type="radio" name="q16" value="b"> B) It computes the gradient at a "look-ahead" position</label>
                <label><input type="radio" name="q16" value="c"> C) It does not use momentum</label>
                <label><input type="radio" name="q16" value="d"> D) It only applies to convex functions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) It computes the gradient at a "look-ahead" position</strong><br>
                NAG computes the gradient at $$x^{(k-1)} - t\beta v^{(k-1)}$$ instead of $$x^{(k-1)}$$, allowing it to "look ahead" in the direction of motion.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: Gradient descent is NOT used directly in:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Training neural networks</label>
                <label><input type="radio" name="q17" value="b"> B) Linear regression</label>
                <label><input type="radio" name="q17" value="c"> C) Logistic regression</label>
                <label><input type="radio" name="q17" value="d"> D) Integer programming</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) Integer programming</strong><br>
                Integer programming is a discrete optimization problem; gradient descent cannot be used because there is no gradient.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: A common stopping criterion for gradient descent is:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) \(\|\nabla f(x)\| < \epsilon\)</label>
                <label><input type="radio" name="q18" value="b"> B) \(f(x) = 0\)</label>
                <label><input type="radio" name="q18" value="c"> C) \(x = 0\)</label>
                <label><input type="radio" name="q18" value="d"> D) \(t = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\|\nabla f(x)\| < \epsilon$$</strong><br>
                The algorithm stops when the gradient norm falls below a threshold $$\epsilon$$, indicating it is close to a minimum.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: For a strongly convex function, gradient descent converges at the rate:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(O(1/k)\)</label>
                <label><input type="radio" name="q19" value="b"> B) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q19" value="c"> C) \(O(\rho^k)\) with \(\rho < 1\) (linear)</label>
                <label><input type="radio" name="q19" value="d"> D) \(O(\log k)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) $$O(\rho^k)$$ with $$\rho < 1$$ (linear)</strong><br>
                Strong convexity lets gradient descent achieve a linear (geometric) convergence rate, which is much faster.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: Backpropagation in neural networks is essentially:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) A new optimization algorithm</label>
                <label><input type="radio" name="q20" value="b"> B) An efficient way to compute gradients for gradient descent</label>
                <label><input type="radio" name="q20" value="c"> C) A replacement for gradient descent</label>
                <label><input type="radio" name="q20" value="d"> D) Only applicable to linear functions</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) An efficient way to compute gradients for gradient descent</strong><br>
                Backpropagation uses the chain rule to compute gradients efficiently in neural networks; gradient descent then uses them to update the weights.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: In gradient descent, what does a step size $$t = 0.01$$ mean?</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Move 1% in the gradient direction</label>
                <label><input type="radio" name="q21" value="b"> B) Move in the direction $$-\nabla f$$ by a step equal to 0.01 times the gradient (length $$0.01\lVert\nabla f\rVert$$)</label>
                <label><input type="radio" name="q21" value="c"> C) Divide the gradient by 100</label>
                <label><input type="radio" name="q21" value="d"> D) The maximum number of iterations</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Move in the direction $$-\nabla f$$ by a step equal to 0.01 times the gradient (length $$0.01\lVert\nabla f\rVert$$)</strong><br>
                The step size $$t$$ scales the move along $$-\nabla f$$: $$x^{(k+1)} = x^{(k)} - t\nabla f(x^{(k)})$$.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The Armijo condition in line search checks:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Sufficient decrease of the objective</label>
                <label><input type="radio" name="q22" value="b"> B) The slope of the gradient</label>
                <label><input type="radio" name="q22" value="c"> C) Convexity of the function</label>
                <label><input type="radio" name="q22" value="d"> D) Convergence of the algorithm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Sufficient decrease of the objective</strong><br>
                The Armijo condition ensures $$f(x + t\Delta x) \leq f(x) + c_1 t \nabla f(x)^T \Delta x$$ with $$c_1 \in (0,1)$$.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: SGD differs from GD in that it:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Uses the whole dataset</label>
                <label><input type="radio" name="q23" value="b"> B) Uses a random sample</label>
                <label><input type="radio" name="q23" value="c"> C) Has a fixed step size</label>
                <label><input type="radio" name="q23" value="d"> D) Always converges faster</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Uses a random sample</strong><br>
                Stochastic Gradient Descent uses a random sample (or mini-batch) instead of the whole dataset.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: Momentum in gradient descent helps to:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Accelerate convergence</label>
                <label><input type="radio" name="q24" value="b"> B) Escape local minima</label>
                <label><input type="radio" name="q24" value="c"> C) Reduce oscillations</label>
                <label><input type="radio" name="q24" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above reasons</strong><br>
                Momentum helps accelerate convergence, reduce oscillations and can escape some small local minima.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: For $$f(x) = x^2$$, gradient descent from $$x_0 = 4$$ with $$t = 0.1$$ gives $$x_1 = ?$$</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$3.2$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$4.8$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$3.6$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$2.4$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$3.2$$</strong><br>
                $$\nabla f(4) = 2 \cdot 4 = 8$$. $$x_1 = 4 - 0.1 \cdot 8 = 4 - 0.8 = 3.2$$.
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
    background: linear-gradient(90deg, #2196F3, #00BCD4);
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
    border-color: #2196F3;
    background-color: #e3f2fd;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #2196F3;
    background-color: #bbdefb;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #e3f2fd;
    border-left: 4px solid #2196F3;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #1565C0;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #2196F3;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #1976D2;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #e3f2fd;
    border-radius: 8px;
    border: 2px solid #2196F3;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #1565C0;
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
    q1: 'b', q2: 'b', q3: 'b', q4: 'a', q5: 'b',
    q6: 'b', q7: 'b', q8: 'a', q9: 'b', q10: 'b',
    q11: 'b', q12: 'b', q13: 'b', q14: 'c', q15: 'a',
    q16: 'b', q17: 'd', q18: 'a', q19: 'c', q20: 'b'
,
    q21: 'b', q22: 'a', q23: 'b', q24: 'd', q25: 'a'};

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
    
    // Re-render MathJax for the newly displayed question
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        MathJax.startup.promise.then(() => MathJax.typesetPromise([document.getElementById(`q${questionNum}`)]));
    }
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
            ${scorePercentage >= 80 ? '🎉 Excellent! You have mastered gradient descent and its variants!' :
              scorePercentage >= 60 ? '👍 Pretty good! Review a few concepts about SGD and momentum.' :
              scorePercentage >= 40 ? '📚 You need more review of the gradient descent algorithm.' : '💪 Reread the theory of gradient descent from the beginning!'}
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

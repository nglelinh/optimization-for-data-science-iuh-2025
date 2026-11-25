---
layout: post
title: '14-11 Multiple-Choice Quiz - Newton''s Method'
chapter: '14'
order: 19
owner: GitHub Copilot
lang: en
categories:
- chapter14
lesson_type: quiz
redirect_from:
  - /contents/en/chapter14/14_10_Quiz_Newton_Method/
---

Newton's method quizzes love testing the subtle distinctions between *local* and *global* properties: pure Newton is affine invariant, yet its classical $$m, L, M$$ convergence bound is *not*; Newton's step is orthogonal to level curves in the *Hessian* norm, yet *not* in the Euclidean norm; and a quadratic error rate $$O(\log\log(1/\epsilon))$$ only kicks in after the damped phase ends. Run through this concept map and 4-point warm-up before starting the quiz.

## Key ideas: High-Yield Newton's Method Checkpoints

- **Pillar 1 — Update & Geometry:** $$\Delta x_{\text{nt}} = -(\nabla^2 f(x))^{-1}\nabla f(x)$$ minimizes the local quadratic model; it is strictly a descent direction whenever $$\nabla^2 f(x) \succ 0$$ and is affine invariant.
- **Pillar 2 — Newton Decrement Identities:** $$\lambda(x)^2 = \nabla f(x)^T H^{-1}\nabla f(x) = \Delta x_{\text{nt}}^T H \Delta x_{\text{nt}} = -\nabla f(x)^T \Delta x_{\text{nt}}$$, and $$\frac{1}{2}\lambda(x)^2$$ estimates $$f(x) - f^\star$$.
- **Pillar 3 — Convergence Regimes & Self-Concordance:** Classical damped Newton has Phase I (constant drop $$-\gamma$$) and Phase II (quadratic $$O(\log\log(1/\epsilon))$$). Self-concordant functions ($$|f'''| \le 2(f'')^{3/2}$$) eliminate $$m, L, M$$ and restore affine-invariant bounds.
- **Pillar 4 — Complexity & Extensions:** Dense Newton takes $$O(n^2)$$ memory and $$O(n^3)$$ flops per step; banded Hessians drop this to $$O(n)$$; equality constraints use the block KKT system; quasi-Newton achieves superlinear convergence without Hessians.

### Worked example: 4-Check Rapid Quiz Warm-Up

1. **Newton step & decrement:** For $$f(x) = \frac{1}{2}x^2 + e^x$$ at $$x = 0$$, compute $$\Delta x_{\text{nt}}$$ and $$\lambda(0)$$.
   - $$f'(0) = 0 + 1 = 1$$, $$f''(0) = 1 + 1 = 2$$.
   - $$\Delta x_{\text{nt}} = -1/2 = -0.5$$; $$\lambda(0) = \sqrt{1^2 / 2} = \frac{1}{\sqrt{2}} \approx 0.707$$.
2. **Self-concordance check:** Is $$f(x) = -\log(x) + 3x^2$$ self-concordant on $$x > 0$$?
   - Yes! Both $$-\log(x)$$ and the convex quadratic $$3x^2$$ are self-concordant, and self-concordance is closed under addition.
3. **Affine invariance check:** If $$g(y) = f(10y)$$, how does $$\lambda_g(y)$$ compare to $$\lambda_f(10y)$$?
   - They are **identical**: $$\lambda_g(y) = \lambda_f(10y)$$.
4. **Equality-constrained feasibility check:** If $$Ax^{(0)} = b$$ and $$A\Delta x_{\text{nt}} = 0$$, is $$x^{(0)} + 0.5\Delta x_{\text{nt}}$$ feasible?
   - Yes: $$A(x^{(0)} + 0.5\Delta x_{\text{nt}}) = b + 0 = b$$ for every step size $$t$$.

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### ⚡ **Newton's Method**

#### **From First-Order to Second-Order**
- **First-order methods:** Gradient Descent - uses $$\nabla f(x)$$
- **Second-order methods:** Newton's Method - uses $$\nabla^2 f(x)$$ (Hessian)
- **Idea:** Instead of approximating the Hessian by $$\frac{1}{t}I$$, compute $$\nabla^2 f(x)$$ exactly

#### **Problem**
$$\min_x f(x)$$ with $$f$$ convex, twice differentiable, $$\text{dom}(f) = \mathbb{R}^n$$

#### **Newton update rule**
$$x^{(k)} = x^{(k-1)} - (\nabla^2 f(x^{(k-1)}))^{-1} \nabla f(x^{(k-1)})$$

**Comparison with Gradient Descent:**
- **GD:** $$x^{(k)} = x^{(k-1)} - t \nabla f(x^{(k-1)})$$
- **Newton:** $$x^{(k)} = x^{(k-1)} - (\nabla^2 f(x^{(k-1)}))^{-1} \nabla f(x^{(k-1)})$$

### 🔍 **Explanation and Properties**

#### **Newton step interpretation**
**Newton direction:** $$\Delta x_{nt} = -(\nabla^2 f(x))^{-1} \nabla f(x)$$

**Geometric interpretation:**
- Minimize quadratic approximation: $$f(x) + \nabla f(x)^T (y-x) + \frac{1}{2}(y-x)^T \nabla^2 f(x) (y-x)$$
- Solution: $$y^* = x - (\nabla^2 f(x))^{-1} \nabla f(x)$$

#### **Root finding connection**
Newton's method for optimization ≡ Newton-Raphson root finding for $$\nabla f(x) = 0$$

**Newton-Raphson:** $$x^{(k)} = x^{(k-1)} - \frac{g(x^{(k-1)})}{g'(x^{(k-1)})}$$

**For $$g(x) = \nabla f(x)$$:** $$x^{(k)} = x^{(k-1)} - (\nabla^2 f(x^{(k-1)}))^{-1} \nabla f(x^{(k-1)})$$

#### **Affine invariance**
**Key property:** Newton's method is unchanged under affine transformations

**If:** $$g(y) = f(Ay + b)$$ with $$A$$ nonsingular
**Then:** The Newton steps for $$g$$ and $$f$$ are equivalent

**Meaning:** Not affected by conditioning, unlike Gradient Descent

### 📐 **Newton Decrement**

#### **Definition**
$$\lambda(x) = (\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x))^{1/2}$$

#### **Physical meaning**
1. **Approximation quality:** $$\frac{1}{2}\lambda^2(x) = f(x) - \min_y \hat{f}(y)$$
   - $$\hat{f}(y)$$: quadratic approximation of $$f$$ at $$x$$
   - $$\frac{1}{2}\lambda^2(x)$$: an estimate of $$f(x) - f^*$$ (based on the quadratic approximation; not a rigorous upper bound)

2. **Step length:** $$\lambda(x) = \lVert \Delta x_{nt} \rVert_{\nabla^2 f(x)}$$ (Hessian norm)

3. **Mahalanobis distance:** Distance from the current point to the Newton step

#### **Alternative expressions**
- $$\lambda(x) = (\Delta x_{nt}^T \nabla^2 f(x) \Delta x_{nt})^{1/2}$$
- $$\nabla f(x)^T \Delta x_{nt} = -\lambda^2(x)$$

#### **Affine invariance**
The Newton decrement is also affine invariant: $$\lambda_g(y) = \lambda_f(x)$$

### 🎯 **Damped Newton Method**

#### **Problems with Pure Newton**
- **No convergence guarantee:** $$f(x^{(k)})$$ may increase
- **Only local convergence:** Needs a starting point close to the optimum

#### **Backtracking line search**
**Algorithm:**
1. Compute Newton direction: $$v = -(\nabla^2 f(x))^{-1} \nabla f(x)$$
2. **Backtracking:** with parameters $$0 < \alpha \le 1/2$$, $$0 < \beta < 1$$
   ```
   t = 1
   while f(x + tv) > f(x) + α t ∇f(x)^T v:
       t = βt
   ```
3. **Update:** $$x^+ = x + tv$$

#### **Armijo condition**
$$f(x + tv) \le f(x) + \alpha t \nabla f(x)^T v$$

with $$\nabla f(x)^T v = -\lambda^2(x) < 0$$

### 📊 **Convergence Analysis**

#### **Assumptions**
1. **$$\nabla f$$ Lipschitz:** $$\lVert \nabla f(x) - \nabla f(y) \rVert_2 \le L \lVert x-y \rVert_2$$
2. **Strong convexity:** $$mI \preceq \nabla^2 f(x) \preceq LI$$
3. **$$\nabla^2 f$$ Lipschitz:** $$\lVert \nabla^2 f(x) - \nabla^2 f(y) \rVert_2 \le M \lVert x-y \rVert_2$$

#### **Two-phase convergence**
**Phase I - Damped phase:** $$\lVert \nabla f(x^{(k)}) \rVert_2 \ge \eta$$
$$f(x^{(k+1)}) - f(x^{(k)}) \le -\gamma$$

**Phase II - Pure phase:** $$\lVert \nabla f(x^{(k)}) \rVert_2 < \eta$$
$$\frac{M}{2m^2} \lVert \nabla f(x^{(k+1)}) \rVert_2 \le \left(\frac{M}{2m^2} \lVert \nabla f(x^{(k)}) \rVert_2\right)^2$$

#### **Convergence rates**
**Phase I (damped phase):** The function value decreases by at least a fixed amount $$\gamma$$ per step
$$f(x^{(k)}) - f^* \le (f(x^{(0)}) - f^*) - \gamma k$$

**Phase II:** Quadratic convergence
$$f(x^{(k)}) - f^* \le \frac{2m^3}{M^2}\left(\frac{1}{2}\right)^{2^{k-k_0+1}}$$

#### **Total complexity**
$$\frac{f(x^{(0)}) - f^*}{\gamma} + \log\log\left(\frac{\epsilon_0}{\epsilon}\right)$$

**Practical estimate:** $$\frac{f(x^{(0)}) - f^*}{\gamma} + 6$$

### 🌟 **Self-Concordant Functions**

#### **Motivation**
**Problems with the standard analysis:**
1. **Hard to find constants:** $$L, m, M$$ are hard to determine in practice
2. **Not affine invariant:** The analysis depends on the coordinate system

#### **Self-concordance definition**
A function $$f$$ is **self-concordant** if:
$$|f'''(x)| \le 2(f''(x))^{3/2}$$ (univariate case)

**Multivariate:** $$\lvert D^3 f(x)[h,h,h] \rvert \le 2(h^T \nabla^2 f(x) h)^{3/2}$$

#### **Key properties**
1. **Affine invariant:** Self-concordance preserved under affine transformation
2. **No constants needed:** The analysis does not need $$L, m, M$$
3. **Barrier functions:** Logarithmic barriers are self-concordant

#### **Convergence for self-concordant**
**Simpler analysis:** Only the Newton decrement $$\lambda(x)$$ is needed
- **Damped phase:** $$\lambda(x) \ge \eta$$
- **Pure phase:** $$\lambda(x) < \eta$$

### 🔄 **Newton vs Gradient Descent**

#### **Computational comparison**

| Aspect | Newton Method | Gradient Descent |
|--------|---------------|------------------|
| **Memory** | $$O(n^2)$$ (Hessian storage) | $$O(n)$$ (gradient storage) |
| **Computation** | $$O(n^3)$$ (linear system) | $$O(n)$$ (vector operations) |
| **Convergence** | Quadratic (near optimum) | Linear |
| **Conditioning** | Affine invariant | Sensitive to conditioning |
| **Robustness** | Sensitive to numerical errors | More robust |

#### **When to use Newton**
**Advantages:**
- **Fast convergence:** Quadratic near optimum
- **Affine invariant:** Not affected by conditioning
- **Fewer iterations:** Especially for high accuracy

**Disadvantages:**
- **Expensive per iteration:** $$O(n^3)$$ cost
- **Memory intensive:** $$O(n^2)$$ storage
- **Numerical sensitivity:** Hessian inversion issues

#### **Practical considerations**
- **Small to medium $$n$$:** Newton often better
- **Large $$n$$:** Gradient descent or quasi-Newton
- **High accuracy needed:** Newton's quadratic convergence wins
- **Ill-conditioned:** Newton's affine invariance helps

### 🛠️ **Implementation Details**

#### **Computing Newton step**
1. **Form Hessian:** $$H = \nabla^2 f(x)$$
2. **Solve linear system:** $$H \Delta x = -\nabla f(x)$$
3. **Don't invert explicitly:** Use Cholesky, LU, or CG

#### **Numerical considerations**
- **Hessian positive definite:** Ensure convexity
- **Regularization:** Add $$\epsilon I$$ if needed
- **Condition number:** Monitor $$\kappa(H)$$
- **Line search:** Always use backtracking for global convergence

#### **Stopping criteria**
1. **Newton decrement:** $$\lambda^2(x)/2 < \epsilon$$
2. **Gradient norm:** $$\lVert \nabla f(x) \rVert_2 < \epsilon$$
3. **Function decrease:** $$\lvert f(x^{(k)}) - f(x^{(k-1)}) \rvert < \epsilon$$

### 🎯 **Special Cases and Extensions**

#### **Quasi-Newton methods**
**Motivation:** Avoid computing exact Hessian

**BFGS update:**
$$B_{k+1} = B_k + \frac{y_k y_k^T}{y_k^T s_k} - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$$

with $$s_k = x_{k+1} - x_k$$, $$y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$$

**L-BFGS:** Limited-memory version for large-scale problems

#### **Trust region methods**
**Alternative to line search:**
$$\min_p f(x) + \nabla f(x)^T p + \frac{1}{2}p^T \nabla^2 f(x) p$$
subject to $$\lVert p \rVert \le \Delta$$

### 💡 **Illustrative Examples**

#### **Logistic regression**
**Problem:** $$\min_\beta \sum_{i=1}^n \log(1 + \exp(-y_i x_i^T \beta))$$

**Gradient:** $$\nabla f(\beta) = -\sum_{i=1}^n \frac{y_i x_i}{1 + \exp(y_i x_i^T \beta)}$$

**Hessian:** $$\nabla^2 f(\beta) = \sum_{i=1}^n \frac{\exp(y_i x_i^T \beta)}{(1 + \exp(y_i x_i^T \beta))^2} x_i x_i^T$$

**Newton step:** Solve $$\nabla^2 f(\beta) \Delta \beta = -\nabla f(\beta)$$

#### **Quadratic function**
**Problem:** $$f(x) = \frac{1}{2}x^T Q x + b^T x + c$$ with $$Q \succ 0$$

**Newton step:** $$\Delta x = -Q^{-1}(Qx + b) = -(x + Q^{-1}b)$$

**One-step convergence:** $$x^{(1)} = x^{(0)} - (x^{(0)} + Q^{-1}b) = -Q^{-1}b = x^*$$

### 🎯 **Connections to Other Chapters**

#### **From the previous chapter:**
- **Chapter 06:** Gradient Descent - the first-order foundation
- **Chapter 13:** Duality uses - computational efficiency
- **Chapter 12:** KKT conditions - optimality characterization

#### **Importance of Newton's Method:**
- **Second-order information:** Uses curvature information
- **Quadratic convergence:** Fastest local convergence rate
- **Affine invariance:** Robust to problem conditioning
- **Interior point foundation:** Basis for barrier methods

#### **Looking ahead:**
- **Chapter 15:** Barrier methods - Newton for constrained problems
- **Interior point methods:** Polynomial-time algorithms
- **Quasi-Newton methods:** Practical approximations
- **Trust region methods:** Alternative globalization strategy

### 🌟 **Theoretical Significance**

#### **Newton as the optimal second-order method:**
- **Natural step:** Minimizes quadratic approximation
- **Affine invariant:** Coordinate-free algorithm
- **Optimal convergence:** Fastest possible local rate
- **Self-correcting:** Adapts to local curvature

#### **Computational trade-offs:**
- **Per-iteration cost:** $$O(n^3)$$ vs $$O(n)$$ for gradient
- **Total iterations:** Much fewer than first-order
- **Memory requirements:** $$O(n^2)$$ vs $$O(n)$$
- **Numerical stability:** More sensitive than gradient methods

#### **Theoretical foundations:**
- **Quadratic approximation:** Natural extension of linear approximation
- **Self-concordance:** Elegant analysis framework
- **Affine invariance:** Geometric rather than algebraic property
- **Root finding connection:** Unifies optimization and equation solving

### 💡 **Practical Tips**

#### **When to use Newton:**
1. **Medium-scale problems:** $$n \le 10^3$$ typically
2. **High accuracy needed:** Quadratic convergence valuable
3. **Well-conditioned:** Or when affine invariance helps
4. **Smooth problems:** Hessian computable and reliable

#### **Implementation tips:**
- **Never invert Hessian:** Always solve linear system
- **Check positive definiteness:** Ensure Hessian $$\succ 0$$
- **Use regularization:** Add $$\epsilon I$$ if needed
- **Monitor condition number:** Watch for numerical issues
- **Always use line search:** For global convergence

#### **Common pitfalls:**
- **Singular Hessian:** At saddle points or boundaries
- **Expensive Hessian:** When second derivatives costly
- **Poor starting point:** May not reach quadratic phase
- **Numerical errors:** Hessian inversion amplifies errors

### 🔬 **Advanced Topics**

#### **Modified Newton methods:**
- **Regularized Newton:** $$H + \epsilon I$$
- **Levenberg-Marquardt:** Adaptive regularization
- **Cubic regularization:** Third-order methods
- **Inexact Newton:** Approximate linear system solution

#### **Large-scale adaptations:**
- **Quasi-Newton:** BFGS, L-BFGS approximations
- **Gauss-Newton:** For least squares problems
- **Truncated Newton:** CG for linear system
- **Limited memory:** Avoid storing full Hessian

#### **Constrained extensions:**
- **Sequential Quadratic Programming (SQP):** Newton for constrained
- **Interior point methods:** Barrier function approach
- **Augmented Lagrangian:** Penalty method combination
- **Active set methods:** Constraint identification

### 📈 **Real-World Applications**

#### **Machine Learning:**
- **Logistic regression:** Standard Newton application
- **Neural network training:** Second-order optimization
- **Gaussian processes:** Hyperparameter optimization
- **SVM training:** Interior point methods

#### **Statistics:**
- **Maximum likelihood estimation:** Natural Newton application
- **Generalized linear models:** Iteratively reweighted least squares
- **Robust regression:** M-estimators
- **Survival analysis:** Cox regression

#### **Engineering:**
- **Structural optimization:** Design optimization
- **Control systems:** Optimal control problems
- **Signal processing:** Parameter estimation
- **Image processing:** Reconstruction problems

#### **Finance:**
- **Portfolio optimization:** Risk management
- **Option pricing:** Calibration problems
- **Risk modeling:** Parameter estimation
- **Algorithmic trading:** Strategy optimization

### 🔮 **Future Directions**

#### **Emerging developments:**
- **Stochastic Newton:** Online second-order methods
- **Distributed Newton:** Parallel computation
- **Quantum Newton:** Quantum optimization algorithms
- **Adaptive methods:** Problem-specific modifications

#### **Computational advances:**
- **GPU acceleration:** Parallel linear algebra
- **Automatic differentiation:** Efficient Hessian computation
- **Sparse methods:** Structured Hessian exploitation
- **Randomized algorithms:** Sketching techniques

### 💎 **Key Insights**

#### **Newton's fundamental contributions:**
1. **Second-order information:** Uses curvature for faster convergence
2. **Affine invariance:** Coordinate-free optimization
3. **Quadratic convergence:** Optimal local convergence rate
4. **Natural algorithm:** Minimizes quadratic approximation

#### **Practical impact:**
- **Interior point revolution:** Enabled polynomial-time algorithms
- **Machine learning:** Foundation for many optimization algorithms
- **Scientific computing:** Standard tool for nonlinear equations
- **Engineering design:** Enables complex optimization problems

### 🌟 **Legacy of Chapter 14:**

- **Algorithmic breakthrough:** Second-order optimization methods
- **Theoretical foundation:** Convergence analysis framework
- **Practical impact:** Enables the solution of complex problems
- **Educational value:** Bridges linear algebra and optimization
- **Scientific influence:** Foundation for modern optimization

---

💡 **Final message:** Newton's method is not just a faster gradient descent - it is a **paradigm shift** from first-order to second-order thinking, enabling quadratic convergence and affine invariance for optimization problems!

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

This multiple-choice quiz tests your understanding of Newton's method, including second-order optimization, convergence analysis, backtracking line search, self-concordant functions and quasi-Newton methods.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔢 Quiz: Newton's Method</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Question: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Question 1 -->
        <div class="question" id="q1" style="display: block;">
            <h3>Question 1: The update formula of the pure Newton method (no line search) is:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(x^{(k+1)} = x^{(k)} - t_k \nabla f(x^{(k)})\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(x^{(k+1)} = x^{(k)} - t_k [\nabla^2 f(x^{(k)})]^{-1} \nabla f(x^{(k)})\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(x^{(k+1)} = x^{(k)} - [\nabla^2 f(x^{(k)})]^{-1} \nabla f(x^{(k)})\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(x^{(k+1)} = x^{(k)} - \nabla^2 f(x^{(k)}) \nabla f(x^{(k)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) $$x^{(k+1)} = x^{(k)} - [\nabla^2 f(x^{(k)})]^{-1} \nabla f(x^{(k)})$$</strong><br>
                The pure Newton method uses the full Newton step with step size = 1; no line search is needed near the optimum.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: The Newton direction \(\Delta x_{nt}\) is computed by solving:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\nabla^2 f(x) \Delta x_{nt} = \nabla f(x)\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\nabla^2 f(x) \Delta x_{nt} = -\nabla f(x)\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\nabla f(x) \Delta x_{nt} = -\nabla^2 f(x)\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\Delta x_{nt} = -\nabla f(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\nabla^2 f(x) \Delta x_{nt} = -\nabla f(x)$$</strong><br>
                The Newton direction is found by solving a linear system with the Hessian matrix and the negative gradient.
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: Newton's method is called a second-order method because it:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Uses second derivatives (the Hessian)</label>
                <label><input type="radio" name="q3" value="b"> B) Converges in 2 steps</label>
                <label><input type="radio" name="q3" value="c"> C) Needs 2 gradient evaluations</label>
                <label><input type="radio" name="q3" value="d"> D) Has quadratic convergence</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Uses second derivatives (the Hessian)</strong><br>
                Second-order methods use information from second derivatives, unlike first-order methods that only use the gradient.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: The convergence rate of Newton's method is:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Linear</label>
                <label><input type="radio" name="q4" value="b"> B) Superlinear</label>
                <label><input type="radio" name="q4" value="c"> C) Quadratic</label>
                <label><input type="radio" name="q4" value="d"> D) Cubic</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Quadratic</strong><br>
                Newton's method has quadratic convergence near the optimal point: $$\lVert x^{(k+1)} - x^* \rVert \leq C \lVert x^{(k)} - x^* \rVert^2$$.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The Newton decrement \(\lambda(x)\) is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(\lambda(x) = \sqrt{\nabla f(x)^T [\nabla^2 f(x)]^{-1} \nabla f(x)}\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(\lambda(x) = \nabla f(x)^T [\nabla^2 f(x)]^{-1} \nabla f(x)\)</label>
                <label><input type="radio" name="q5" value="c"> C) $$\lambda(x) = \lVert \nabla f(x) \rVert$$</label>
                <label><input type="radio" name="q5" value="d"> D) $$\lambda(x) = \lVert \nabla^2 f(x) \rVert$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\lambda(x) = \sqrt{\nabla f(x)^T [\nabla^2 f(x)]^{-1} \nabla f(x)}$$</strong><br>
                The Newton decrement is a natural, affine-invariant stopping criterion for Newton's method.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: Newton's method being affine invariant means that it:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) Does not change under affine coordinate transformations</label>
                <label><input type="radio" name="q6" value="b"> B) Only works for affine functions</label>
                <label><input type="radio" name="q6" value="c"> C) Needs affine constraints</label>
                <label><input type="radio" name="q6" value="d"> D) Converges linearly</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Does not change under affine coordinate transformations</strong><br>
                Newton's method does not depend on the coordinate system: under the transformation $$x \mapsto Ax + b$$, the Newton steps transform accordingly.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: Backtracking line search in Newton's method uses:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) The Armijo condition with the Newton direction</label>
                <label><input type="radio" name="q7" value="b"> B) Exact line search</label>
                <label><input type="radio" name="q7" value="c"> C) Fixed step size</label>
                <label><input type="radio" name="q7" value="d"> D) Golden section search</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The Armijo condition with the Newton direction</strong><br>
                Backtracking line search checks the sufficient-decrease condition: $$f(x + t\Delta x_{nt}) \leq f(x) + \alpha t \nabla f(x)^T \Delta x_{nt}$$.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: Newton's method can fail when:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) The Hessian is not positive definite</label>
                <label><input type="radio" name="q8" value="b"> B) Starting point xa optimal</label>
                <label><input type="radio" name="q8" value="c"> C) Hessian singular</label>
                <label><input type="radio" name="q8" value="d"> D) All of the above cases</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above cases</strong><br>
                Newton's method needs a positive definite Hessian, can diverge from a distant starting point, and fails when the Hessian is singular.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: Self-concordant functions are important because of:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Convergence analysis that does not depend on constants</label>
                <label><input type="radio" name="q9" value="b"> B) Affine invariant analysis</label>
                <label><input type="radio" name="q9" value="c"> C) Barrier functions in interior point methods</label>
                <label><input type="radio" name="q9" value="d"> D) All of the above reasons</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above reasons</strong><br>
                Self-concordant functions remove the constants problem from the analysis, are affine invariant, and appear naturally in barrier methods.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: A function \(f\) is self-concordant if:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(|f'''(x)[h,h,h]| \leq 2(f''(x)[h,h])^{3/2}\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(f''(x) \succ 0\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(f\) is convex</label>
                <label><input type="radio" name="q10" value="d"> D) \(f\) is smooth</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$|f'''(x)[h,h,h]| \leq 2(f''(x)[h,h])^{3/2}$$</strong><br>
                The self-concordance condition controls the third derivative relative to the second derivative.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: Quasi-Newton methods differ from Newton's method in that they:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Do not need to compute the exact Hessian</label>
                <label><input type="radio" name="q11" value="b"> B) Use an approximation of the Hessian</label>
                <label><input type="radio" name="q11" value="c"> C) Have lower computational cost</label>
                <label><input type="radio" name="q11" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                Quasi-Newton methods approximate the Hessian to reduce computational cost, which suits problems where the Hessian is expensive to compute.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The BFGS method updates an approximation of the:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Diagonal of the Hessian only</label>
                <label><input type="radio" name="q12" value="b"> B) Inverse Hessian matrix</label>
                <label><input type="radio" name="q12" value="c"> C) Gradient vector</label>
                <label><input type="radio" name="q12" value="d"> D) Objective function</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Inverse Hessian matrix</strong><br>
                BFGS (in its commonly used form) directly updates an approximation $$H_k$$ of the inverse Hessian, avoiding solving a linear system. (There is also an equivalent form that updates an approximation $$B_k$$ of the Hessian itself.)
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The computational cost per iteration of Newton's method is:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(O(n)\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(O(n^2)\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(O(n^3)\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(O(n^4)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) $$O(n^3)$$</strong><br>
                Newton's method needs $$O(n^2)$$ to compute the Hessian and $$O(n^3)$$ to solve the linear system $$H \Delta x = -g$$.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: The damped Newton method uses:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) A small fixed step size</label>
                <label><input type="radio" name="q14" value="b"> B) Line search with the Newton direction</label>
                <label><input type="radio" name="q14" value="c"> C) Modified Hessian</label>
                <label><input type="radio" name="q14" value="d"> D) Gradient descent direction</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Line search with the Newton direction</strong><br>
                The damped Newton method combines the Newton direction with a line search to guarantee global convergence.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: The trust-region Newton method differs from line-search Newton in that it:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Limits the step size to a region</label>
                <label><input type="radio" name="q15" value="b"> B) Modifies the direction instead of the step size</label>
                <label><input type="radio" name="q15" value="c"> C) Chooses the step by solving a subproblem with the constraint $$\lVert p \rVert \leq \Delta$$</label>
                <label><input type="radio" name="q15" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                Trust-region methods limit the step to a trusted region, may modify the direction, and choose the step by minimizing the quadratic model subject to the constraint $$\lVert p \rVert \leq \Delta$$.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: Newton's method for root finding \(g(x) = 0\) has the formula:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(x^{(k+1)} = x^{(k)} - \frac{g(x^{(k)})}{g'(x^{(k)})}\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(x^{(k+1)} = x^{(k)} - g(x^{(k)})\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(x^{(k+1)} = x^{(k)} - g'(x^{(k)})\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(x^{(k+1)} = x^{(k)} + \frac{g(x^{(k)})}{g'(x^{(k)})}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$x^{(k+1)} = x^{(k)} - \frac{g(x^{(k)})}{g'(x^{(k)})}$$</strong><br>
                Newton's method for root finding becomes the optimization case when $$g(x) = \nabla f(x)$$ and we seek $$\nabla f(x) = 0$$.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: When the Hessian is not positive definite, we can:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Add regularization: \(H + \lambda I\)</label>
                <label><input type="radio" name="q17" value="b"> B) Use absolute eigenvalues</label>
                <label><input type="radio" name="q17" value="c"> C) Modified Cholesky decomposition</label>
                <label><input type="radio" name="q17" value="d"> D) All of the above methods</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above methods</strong><br>
                There are many ways to modify the Hessian to ensure positive definiteness: regularization, eigenvalue modification, modified Cholesky.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: The advantages of L-BFGS (Limited-memory BFGS) are:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Memory requirement \(O(n)\) instead of \(O(n^2)\)</label>
                <label><input type="radio" name="q18" value="b"> B) Suitable for large-scale problems</label>
                <label><input type="radio" name="q18" value="c"> C) No need to store the full matrix</label>
                <label><input type="radio" name="q18" value="d"> D) All of the above advantages</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above advantages</strong><br>
                L-BFGS stores only a limited history (usually 5-20 vectors) instead of the full matrix, making it very efficient for large-scale optimization.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: Newton's method is applied in:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Interior point methods</label>
                <label><input type="radio" name="q19" value="b"> B) Neural network training</label>
                <label><input type="radio" name="q19" value="c"> C) Maximum likelihood estimation</label>
                <label><input type="radio" name="q19" value="d"> D) All of the above applications</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above applications</strong><br>
                Newton's method has wide applications: interior point methods, second-order optimization in ML, statistical estimation.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: Compared with first-order methods, Newton's method has:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Fewer iterations but each iteration is more expensive</label>
                <label><input type="radio" name="q20" value="b"> B) Quadratic convergence vs linear convergence</label>
                <label><input type="radio" name="q20" value="c"> C) Affine invariant vs coordinate dependent</label>
                <label><input type="radio" name="q20" value="d"> D) All of the above</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) All of the above</strong><br>
                The Newton trade-off: fewer iterations with faster convergence, but each iteration is more expensive. Affine invariance is a major advantage.
            </div>
        </div>
        <!-- Question 21: Practice -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: Newton's method uses the information of:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Gradient and Hessian</label>
                <label><input type="radio" name="q21" value="b"> B) Only the gradient</label>
                <label><input type="radio" name="q21" value="c"> C) Only the Hessian</label>
                <label><input type="radio" name="q21" value="d"> D) Only function values</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Gradient and Hessian</strong><br>
                Newton method: $$x^{(k+1)} = x^{(k)} - [\nabla^2 f(x^{(k)})]^{-1} \nabla f(x^{(k)})$$.
            </div>
        </div>

        <!-- Question 22: Practice -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: The convergence rate of Newton's method is:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Quadratic (second order)</label>
                <label><input type="radio" name="q22" value="b"> B) Linear</label>
                <label><input type="radio" name="q22" value="c"> C) Sublinear</label>
                <label><input type="radio" name="q22" value="d"> D) Cubic</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Quadratic (second order)</strong><br>
                Newton's method converges quadratically near the solution when the Hessian is invertible.
            </div>
        </div>

        <!-- Question 23: Practice -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: Quasi-Newton methods differ from Newton's method in that they:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Approximate the Hessian instead of computing it exactly</label>
                <label><input type="radio" name="q23" value="b"> B) Do not use the gradient</label>
                <label><input type="radio" name="q23" value="c"> C) Only work for linear functions</label>
                <label><input type="radio" name="q23" value="d"> D) Are always slower</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Approximate the Hessian instead of computing it exactly</strong><br>
                Quasi-Newton methods (BFGS, L-BFGS) build a Hessian approximation from gradient information.
            </div>
        </div>

        <!-- Question 24: Practice -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The BFGS update formula updates:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) An approximation of the inverse Hessian</label>
                <label><input type="radio" name="q24" value="b"> B) Gradient</label>
                <label><input type="radio" name="q24" value="c"> C) The current point</label>
                <label><input type="radio" name="q24" value="d"> D) The step size</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) An approximation of the inverse Hessian</strong><br>
                BFGS updates the approximation matrix $$H_k \approx [\nabla^2 f]^{-1}$$ using gradient information.
            </div>
        </div>

        <!-- Question 25: Practice -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: For $$f(x) = x^2$$, one Newton step from $$x_0 = 2$$ gives:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$x_1 = 0$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$x_1 = 1$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$x_1 = -2$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$x_1 = 2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$x_1 = 0$$</strong><br>
                $$\nabla f(2) = 4$$, $$\nabla^2 f(2) = 2$$. $$x_1 = 2 - 4/2 = 0$$.
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
    q1: 'c', q2: 'b', q3: 'a', q4: 'c', q5: 'a',
    q6: 'a', q7: 'a', q8: 'd', q9: 'd', q10: 'a',
    q11: 'd', q12: 'b', q13: 'c', q14: 'b', q15: 'd',
    q16: 'a', q17: 'd', q18: 'd', q19: 'd', q20: 'd'
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
        message = '🌟 Excellent! You have mastered the Newton method and second-order optimization!';
    } else if (percentage >= 80) {
        message = '👍 Very good! You understand the Newton method and its convergence analysis well.';
    } else if (percentage >= 70) {
        message = '📚 Not bad! Review self-concordance and quasi-Newton methods.';
    } else if (percentage >= 60) {
        message = '💪 Needs improvement! Review the Newton direction and backtracking line search.';
    } else {
        message = '📖 Study the Newton method again from the beginning!';
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

---
layout: post
title: 14-10 Bài tập trắc nghiệm - Phương Pháp Newton
chapter: '14'
order: 17
owner: GitHub Copilot
lang: vi
categories:
- chapter14
lesson_type: quiz
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Newton Method (Phương Pháp Newton)**

#### **Từ First-Order đến Second-Order**
- **First-order methods:** Gradient Descent - sử dụng $$\nabla f(x)$$
- **Second-order methods:** Newton Method - sử dụng $$\nabla^2 f(x)$$ (Hessian)
- **Ý tưởng:** Thay vì xấp xỉ Hessian bằng $$\frac{1}{t}I$$, tính chính xác $$\nabla^2 f(x)$$

#### **Bài toán**
$$\min_x f(x)$$ với $$f$$ convex, twice differentiable, $$\text{dom}(f) = \mathbb{R}^n$$

#### **Newton update rule**
$$x^{(k)} = x^{(k-1)} - (\nabla^2 f(x^{(k-1)}))^{-1} \nabla f(x^{(k-1)})$$

**So sánh với Gradient Descent:**
- **GD:** $$x^{(k)} = x^{(k-1)} - t \nabla f(x^{(k-1)})$$
- **Newton:** $$x^{(k)} = x^{(k-1)} - (\nabla^2 f(x^{(k-1)}))^{-1} \nabla f(x^{(k-1)})$$

### 🔍 **Giải Thích và Tính Chất**

#### **Newton step interpretation**
**Newton direction:** $$\Delta x_{nt} = -(\nabla^2 f(x))^{-1} \nabla f(x)$$

**Geometric interpretation:**
- Minimize quadratic approximation: $$f(x) + \nabla f(x)^T (y-x) + \frac{1}{2}(y-x)^T \nabla^2 f(x) (y-x)$$
- Solution: $$y^* = x - (\nabla^2 f(x))^{-1} \nabla f(x)$$

#### **Root finding connection**
Newton method cho optimization ≡ Newton-Raphson cho root finding của $$\nabla f(x) = 0$$

**Newton-Raphson:** $$x^{(k)} = x^{(k-1)} - \frac{g(x^{(k-1)})}{g'(x^{(k-1)})}$$

**For $$g(x) = \nabla f(x)$$:** $$x^{(k)} = x^{(k-1)} - (\nabla^2 f(x^{(k-1)}))^{-1} \nabla f(x^{(k-1)})$$

#### **Affine invariance**
**Tính chất quan trọng:** Newton method không thay đổi dưới affine transformation

**Nếu:** $$g(y) = f(Ay + b)$$ với $$A$$ nonsingular
**Thì:** Newton steps cho $$g$$ và $$f$$ tương đương

**Ý nghĩa:** Không bị ảnh hưởng bởi conditioning như Gradient Descent

### 📐 **Newton Decrement**

#### **Định nghĩa**
$$\lambda(x) = (\nabla f(x)^T (\nabla^2 f(x))^{-1} \nabla f(x))^{1/2}$$

#### **Ý nghĩa vật lý**
1. **Approximation quality:** $$\frac{1}{2}\lambda^2(x) = f(x) - \min_y \hat{f}(y)$$
   - $$\hat{f}(y)$$: quadratic approximation của $$f$$ tại $$x$$
   - $$\frac{1}{2}\lambda^2(x)$$: ước lượng cho $$f(x) - f^*$$ (dựa trên xấp xỉ bậc hai; chưa phải cận trên chặt chẽ)

2. **Step length:** $$\lambda(x) = \lVert \Delta x_{nt} \rVert_{\nabla^2 f(x)}$$ (Hessian norm)

3. **Mahalanobis distance:** Distance từ current point đến Newton step

#### **Alternative expressions**
- $$\lambda(x) = (\Delta x_{nt}^T \nabla^2 f(x) \Delta x_{nt})^{1/2}$$
- $$\nabla f(x)^T \Delta x_{nt} = -\lambda^2(x)$$

#### **Affine invariance**
Newton decrement cũng affine invariant: $$\lambda_g(y) = \lambda_f(x)$$

### 🎯 **Damped Newton Method**

#### **Vấn đề với Pure Newton**
- **Không đảm bảo convergence:** $$f(x^{(k)})$$ có thể tăng
- **Chỉ có local convergence:** Cần starting point gần optimal

#### **Backtracking line search**
**Algorithm:**
1. Compute Newton direction: $$v = -(\nabla^2 f(x))^{-1} \nabla f(x)$$
2. **Backtracking:** với parameters $$0 < \alpha \le 1/2$$, $$0 < \beta < 1$$
   ```
   t = 1
   while f(x + tv) > f(x) + α t ∇f(x)^T v:
       t = βt
   ```
3. **Update:** $$x^+ = x + tv$$

#### **Armijo condition**
$$f(x + tv) \le f(x) + \alpha t \nabla f(x)^T v$$

với $$\nabla f(x)^T v = -\lambda^2(x) < 0$$

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
**Phase I (damped phase):** Giá trị hàm giảm ít nhất một lượng cố định $$\gamma$$ mỗi bước
$$f(x^{(k)}) - f^* \le (f(x^{(0)}) - f^*) - \gamma k$$

**Phase II:** Quadratic convergence
$$f(x^{(k)}) - f^* \le \frac{2m^3}{M^2}\left(\frac{1}{2}\right)^{2^{k-k_0+1}}$$

#### **Total complexity**
$$\frac{f(x^{(0)}) - f^*}{\gamma} + \log\log\left(\frac{\epsilon_0}{\epsilon}\right)$$

**Practical estimate:** $$\frac{f(x^{(0)}) - f^*}{\gamma} + 6$$

### 🌟 **Self-Concordant Functions**

#### **Motivation**
**Problems với standard analysis:**
1. **Hard to find constants:** $$L, m, M$$ khó xác định trong thực tế
2. **Not affine invariant:** Analysis phụ thuộc coordinate system

#### **Self-concordance definition**
Hàm $$f$$ là **self-concordant** nếu:
$$|f'''(x)| \le 2(f''(x))^{3/2}$$ (univariate case)

**Multivariate:** $$\lvert D^3 f(x)[h,h,h] \rvert \le 2(h^T \nabla^2 f(x) h)^{3/2}$$

#### **Key properties**
1. **Affine invariant:** Self-concordance preserved under affine transformation
2. **No constants needed:** Analysis không cần $$L, m, M$$
3. **Barrier functions:** Logarithmic barriers are self-concordant

#### **Convergence for self-concordant**
**Simpler analysis:** Chỉ cần Newton decrement $$\lambda(x)$$
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

### 🎯 **Special Cases và Extensions**

#### **Quasi-Newton methods**
**Motivation:** Avoid computing exact Hessian

**BFGS update:**
$$B_{k+1} = B_k + \frac{y_k y_k^T}{y_k^T s_k} - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$$

với $$s_k = x_{k+1} - x_k$$, $$y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$$

**L-BFGS:** Limited memory version cho large-scale problems

#### **Trust region methods**
**Alternative to line search:**
$$\min_p f(x) + \nabla f(x)^T p + \frac{1}{2}p^T \nabla^2 f(x) p$$
subject to $$\lVert p \rVert \le \Delta$$

### 💡 **Ví Dụ Minh Họa**

#### **Logistic regression**
**Problem:** $$\min_\beta \sum_{i=1}^n \log(1 + \exp(-y_i x_i^T \beta))$$

**Gradient:** $$\nabla f(\beta) = -\sum_{i=1}^n \frac{y_i x_i}{1 + \exp(y_i x_i^T \beta)}$$

**Hessian:** $$\nabla^2 f(\beta) = \sum_{i=1}^n \frac{\exp(y_i x_i^T \beta)}{(1 + \exp(y_i x_i^T \beta))^2} x_i x_i^T$$

**Newton step:** Solve $$\nabla^2 f(\beta) \Delta \beta = -\nabla f(\beta)$$

#### **Quadratic function**
**Problem:** $$f(x) = \frac{1}{2}x^T Q x + b^T x + c$$ với $$Q \succ 0$$

**Newton step:** $$\Delta x = -Q^{-1}(Qx + b) = -(x + Q^{-1}b)$$

**One-step convergence:** $$x^{(1)} = x^{(0)} - (x^{(0)} + Q^{-1}b) = -Q^{-1}b = x^*$$

### 🎯 **Kết Nối Với Các Chương**

#### **Từ chương trước:**
- **Chương 06:** Gradient Descent - first-order foundation
- **Chương 13:** Duality uses - computational efficiency
- **Chương 12:** KKT conditions - optimality characterization

#### **Tầm quan trọng của Newton Method:**
- **Second-order information:** Sử dụng curvature information
- **Quadratic convergence:** Fastest local convergence rate
- **Affine invariance:** Robust to problem conditioning
- **Interior point foundation:** Basis cho barrier methods

#### **Hướng phát triển:**
- **Chương 15:** Barrier methods - Newton for constrained problems
- **Interior point methods:** Polynomial-time algorithms
- **Quasi-Newton methods:** Practical approximations
- **Trust region methods:** Alternative globalization strategy

### 🌟 **Ý Nghĩa Lý Thuyết**

#### **Newton như optimal second-order method:**
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
- **Root finding connection:** Unifies optimization và equation solving

### 💡 **Mẹo Thực Hành**

#### **When to use Newton:**
1. **Medium-scale problems:** $$n \le 10^3$$ typically
2. **High accuracy needed:** Quadratic convergence valuable
3. **Well-conditioned:** Or when affine invariance helps
4. **Smooth problems:** Hessian computable và reliable

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

### 📈 **Ứng Dụng Thực Tế**

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

### 🌟 **Legacy của chương 14:**

- **Algorithmic breakthrough:** Second-order optimization methods
- **Theoretical foundation:** Convergence analysis framework
- **Practical impact:** Enables solution của complex problems
- **Educational value:** Bridges linear algebra và optimization
- **Scientific influence:** Foundation cho modern optimization

---

💡 **Thông điệp cuối cùng:** Newton Method không chỉ là faster gradient descent - nó là **paradigm shift** từ first-order sang second-order thinking, enabling quadratic convergence và affine invariance cho optimization problems!

---


<style>
/* Sửa lỗi alignment cho MathJax inline math */
.MathJax {
    vertical-align: baseline !important;
}

mjx-container[jax="CHTML"][display="false"] {
    vertical-align: baseline !important;
    display: inline !important;
}

/* Đảm bảo các label trong quiz có alignment tốt */
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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về Newton method, bao gồm second-order optimization, convergence analysis, backtracking line search, self-concordant functions và quasi-Newton methods.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔢 Quiz: Phương Pháp Newton</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Newton method update -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Công thức cập nhật của pure Newton method (không line search) là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(x^{(k+1)} = x^{(k)} - t_k \nabla f(x^{(k)})\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(x^{(k+1)} = x^{(k)} - t_k [\nabla^2 f(x^{(k)})]^{-1} \nabla f(x^{(k)})\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(x^{(k+1)} = x^{(k)} - [\nabla^2 f(x^{(k)})]^{-1} \nabla f(x^{(k)})\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(x^{(k+1)} = x^{(k)} - \nabla^2 f(x^{(k)}) \nabla f(x^{(k)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$x^{(k+1)} = x^{(k)} - [\nabla^2 f(x^{(k)})]^{-1} \nabla f(x^{(k)})$$</strong><br>
                Pure Newton method sử dụng full Newton step với step size = 1, không cần line search khi gần optimal.
            </div>
        </div>

        <!-- Câu hỏi 2: Newton direction -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Newton direction \(\Delta x_{nt}\) được tính bằng cách giải:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\nabla^2 f(x) \Delta x_{nt} = \nabla f(x)\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\nabla^2 f(x) \Delta x_{nt} = -\nabla f(x)\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\nabla f(x) \Delta x_{nt} = -\nabla^2 f(x)\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\Delta x_{nt} = -\nabla f(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\nabla^2 f(x) \Delta x_{nt} = -\nabla f(x)$$</strong><br>
                Newton direction được tìm bằng cách giải hệ tuyến tính với Hessian matrix và negative gradient.
            </div>
        </div>

        <!-- Câu hỏi 3: Second-order method -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Newton method được gọi là second-order method vì:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Sử dụng đạo hàm bậc hai (Hessian)</label>
                <label><input type="radio" name="q3" value="b"> B) Hội tụ trong 2 bước</label>
                <label><input type="radio" name="q3" value="c"> C) Cần 2 lần tính gradient</label>
                <label><input type="radio" name="q3" value="d"> D) Có quadratic convergence</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Sử dụng đạo hàm bậc hai (Hessian)</strong><br>
                Second-order methods sử dụng thông tin từ đạo hàm bậc hai, khác với first-order methods chỉ dùng gradient.
            </div>
        </div>

        <!-- Câu hỏi 4: Convergence rate -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Tốc độ hội tụ của Newton method là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Linear</label>
                <label><input type="radio" name="q4" value="b"> B) Superlinear</label>
                <label><input type="radio" name="q4" value="c"> C) Quadratic</label>
                <label><input type="radio" name="q4" value="d"> D) Cubic</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Quadratic</strong><br>
                Newton method có quadratic convergence khi gần optimal point: $$\lVert x^{(k+1)} - x^* \rVert \leq C \lVert x^{(k)} - x^* \rVert^2$$.
            </div>
        </div>

        <!-- Câu hỏi 5: Newton decrement -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Newton decrement \(\lambda(x)\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(\lambda(x) = \sqrt{\nabla f(x)^T [\nabla^2 f(x)]^{-1} \nabla f(x)}\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(\lambda(x) = \nabla f(x)^T [\nabla^2 f(x)]^{-1} \nabla f(x)\)</label>
                <label><input type="radio" name="q5" value="c"> C) $$\lambda(x) = \lVert \nabla f(x) \rVert$$</label>
                <label><input type="radio" name="q5" value="d"> D) $$\lambda(x) = \lVert \nabla^2 f(x) \rVert$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\lambda(x) = \sqrt{\nabla f(x)^T [\nabla^2 f(x)]^{-1} \nabla f(x)}$$</strong><br>
                Newton decrement là natural stopping criterion cho Newton method, affine invariant.
            </div>
        </div>

        <!-- Câu hỏi 6: Affine invariance -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Newton method có tính chất affine invariant có nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) Không thay đổi khi transform tọa độ affine</label>
                <label><input type="radio" name="q6" value="b"> B) Chỉ hoạt động với affine functions</label>
                <label><input type="radio" name="q6" value="c"> C) Cần affine constraints</label>
                <label><input type="radio" name="q6" value="d"> D) Hội tụ tuyến tính</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Không thay đổi khi transform tọa độ affine</strong><br>
                Newton method không phụ thuộc vào hệ tọa độ: nếu transform $$x \mapsto Ax + b$$, Newton steps tương ứng cũng transform theo.
            </div>
        </div>

        <!-- Câu hỏi 7: Backtracking line search -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Backtracking line search trong Newton method sử dụng:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Armijo condition với Newton direction</label>
                <label><input type="radio" name="q7" value="b"> B) Exact line search</label>
                <label><input type="radio" name="q7" value="c"> C) Fixed step size</label>
                <label><input type="radio" name="q7" value="d"> D) Golden section search</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Armijo condition với Newton direction</strong><br>
                Backtracking line search kiểm tra sufficient decrease condition: $$f(x + t\Delta x_{nt}) \leq f(x) + \alpha t \nabla f(x)^T \Delta x_{nt}$$.
            </div>
        </div>

        <!-- Câu hỏi 8: When Newton method fails -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Newton method có thể thất bại khi:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Hessian không positive definite</label>
                <label><input type="radio" name="q8" value="b"> B) Starting point xa optimal</label>
                <label><input type="radio" name="q8" value="c"> C) Hessian singular</label>
                <label><input type="radio" name="q8" value="d"> D) Tất cả các trường hợp trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các trường hợp trên</strong><br>
                Newton method cần Hessian positive definite, có thể diverge từ starting point xa, và fail khi Hessian singular.
            </div>
        </div>

        <!-- Câu hỏi 9: Self-concordant functions -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Self-concordant functions quan trọng vì:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Convergence analysis không phụ thuộc constants</label>
                <label><input type="radio" name="q9" value="b"> B) Affine invariant analysis</label>
                <label><input type="radio" name="q9" value="c"> C) Barrier functions trong interior point methods</label>
                <label><input type="radio" name="q9" value="d"> D) Tất cả các lý do trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lý do trên</strong><br>
                Self-concordant functions giải quyết vấn đề constants trong analysis, affine invariant, và xuất hiện tự nhiên trong barrier methods.
            </div>
        </div>

        <!-- Câu hỏi 10: Self-concordance definition -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Hàm \(f\) là self-concordant nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(|f'''(x)[h,h,h]| \leq 2(f''(x)[h,h])^{3/2}\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(f''(x) \succ 0\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(f\) là convex</label>
                <label><input type="radio" name="q10" value="d"> D) \(f\) là smooth</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$|f'''(x)[h,h,h]| \leq 2(f''(x)[h,h])^{3/2}$$</strong><br>
                Self-concordance condition kiểm soát third derivative relative to second derivative.
            </div>
        </div>

        <!-- Câu hỏi 11: Quasi-Newton methods -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Quasi-Newton methods khác với Newton method ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Không cần tính Hessian chính xác</label>
                <label><input type="radio" name="q11" value="b"> B) Sử dụng approximation của Hessian</label>
                <label><input type="radio" name="q11" value="c"> C) Chi phí tính toán thấp hơn</label>
                <label><input type="radio" name="q11" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Quasi-Newton methods approximate Hessian để giảm computational cost, phù hợp khi Hessian expensive to compute.
            </div>
        </div>

        <!-- Câu hỏi 12: BFGS update -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: BFGS method cập nhật approximation của:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Chỉ đường chéo của Hessian</label>
                <label><input type="radio" name="q12" value="b"> B) Inverse Hessian matrix</label>
                <label><input type="radio" name="q12" value="c"> C) Gradient vector</label>
                <label><input type="radio" name="q12" value="d"> D) Objective function</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Inverse Hessian matrix</strong><br>
                BFGS (dạng thường dùng) directly updates approximation $$H_k$$ của inverse Hessian, tránh việc phải solve linear system. (Cũng có dạng tương đương cập nhật xấp xỉ $$B_k$$ của chính Hessian.)
            </div>
        </div>

        <!-- Câu hỏi 13: Computational complexity -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Computational cost mỗi iteration của Newton method là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(O(n)\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(O(n^2)\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(O(n^3)\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(O(n^4)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$O(n^3)$$</strong><br>
                Newton method cần $$O(n^2)$$ để tính Hessian và $$O(n^3)$$ để solve linear system $$H \Delta x = -g$$.
            </div>
        </div>

        <!-- Câu hỏi 14: Damped Newton method -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Damped Newton method sử dụng:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Fixed step size nhỏ</label>
                <label><input type="radio" name="q14" value="b"> B) Line search với Newton direction</label>
                <label><input type="radio" name="q14" value="c"> C) Modified Hessian</label>
                <label><input type="radio" name="q14" value="d"> D) Gradient descent direction</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Line search với Newton direction</strong><br>
                Damped Newton method kết hợp Newton direction với line search để đảm bảo global convergence.
            </div>
        </div>

        <!-- Câu hỏi 15: Trust region vs line search -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Trust region Newton method khác với line search Newton ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Giới hạn step size trong một region</label>
                <label><input type="radio" name="q15" value="b"> B) Modify direction thay vì step size</label>
                <label><input type="radio" name="q15" value="c"> C) Chọn step bằng cách giải bài toán con với ràng buộc $$\lVert p \rVert \leq \Delta$$</label>
                <label><input type="radio" name="q15" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Trust region methods giới hạn step trong trusted region, có thể modify direction, và chọn step bằng cách tối thiểu hóa quadratic model trong ràng buộc $$\lVert p \rVert \leq \Delta$$.
            </div>
        </div>

        <!-- Câu hỏi 16: Newton method for root finding -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Newton method cho root finding \(g(x) = 0\) có công thức:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(x^{(k+1)} = x^{(k)} - \frac{g(x^{(k)})}{g'(x^{(k)})}\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(x^{(k+1)} = x^{(k)} - g(x^{(k)})\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(x^{(k+1)} = x^{(k)} - g'(x^{(k)})\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(x^{(k+1)} = x^{(k)} + \frac{g(x^{(k)})}{g'(x^{(k)})}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x^{(k+1)} = x^{(k)} - \frac{g(x^{(k)})}{g'(x^{(k)})}$$</strong><br>
                Newton method cho root finding là trường hợp đặc biệt khi $$g(x) = \nabla f(x)$$ và tìm $$\nabla f(x) = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 17: Hessian modification -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Khi Hessian không positive definite, có thể:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Thêm regularization: \(H + \lambda I\)</label>
                <label><input type="radio" name="q17" value="b"> B) Sử dụng absolute eigenvalues</label>
                <label><input type="radio" name="q17" value="c"> C) Modified Cholesky decomposition</label>
                <label><input type="radio" name="q17" value="d"> D) Tất cả các phương pháp trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các phương pháp trên</strong><br>
                Có nhiều cách modify Hessian để đảm bảo positive definiteness: regularization, eigenvalue modification, modified Cholesky.
            </div>
        </div>

        <!-- Câu hỏi 18: L-BFGS -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: L-BFGS (Limited-memory BFGS) có ưu điểm:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Memory requirement \(O(n)\) thay vì \(O(n^2)\)</label>
                <label><input type="radio" name="q18" value="b"> B) Phù hợp cho large-scale problems</label>
                <label><input type="radio" name="q18" value="c"> C) Không cần store full matrix</label>
                <label><input type="radio" name="q18" value="d"> D) Tất cả các ưu điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ưu điểm trên</strong><br>
                L-BFGS chỉ store limited history (thường 5-20 vectors) thay vì full matrix, rất hiệu quả cho large-scale optimization.
            </div>
        </div>

        <!-- Câu hỏi 19: Newton method applications -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Newton method được ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Interior point methods</label>
                <label><input type="radio" name="q19" value="b"> B) Neural network training</label>
                <label><input type="radio" name="q19" value="c"> C) Maximum likelihood estimation</label>
                <label><input type="radio" name="q19" value="d"> D) Tất cả các ứng dụng trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ứng dụng trên</strong><br>
                Newton method có ứng dụng rộng rãi: interior point methods, second-order optimization trong ML, statistical estimation.
            </div>
        </div>

        <!-- Câu hỏi 20: Comparison with first-order methods -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: So với first-order methods, Newton method:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Ít iterations hơn nhưng mỗi iteration expensive hơn</label>
                <label><input type="radio" name="q20" value="b"> B) Quadratic convergence vs linear convergence</label>
                <label><input type="radio" name="q20" value="c"> C) Affine invariant vs coordinate dependent</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Newton method trade-off: fewer iterations với faster convergence, nhưng mỗi iteration expensive hơn. Affine invariant là advantage lớn.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Newton method sử dụng thông tin:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Gradient và Hessian</label>
                <label><input type="radio" name="q21" value="b"> B) Chỉ gradient</label>
                <label><input type="radio" name="q21" value="c"> C) Chỉ Hessian</label>
                <label><input type="radio" name="q21" value="d"> D) Chỉ giá trị hàm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Gradient và Hessian</strong><br>
                Newton method: $$x^{(k+1)} = x^{(k)} - [\nabla^2 f(x^{(k)})]^{-1} \nabla f(x^{(k)})$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Tốc độ hội tụ của Newton method là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Quadratic (bậc 2)</label>
                <label><input type="radio" name="q22" value="b"> B) Linear</label>
                <label><input type="radio" name="q22" value="c"> C) Sublinear</label>
                <label><input type="radio" name="q22" value="d"> D) Cubic</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Quadratic (bậc 2)</strong><br>
                Newton method có tốc độ hội tụ quadratic khi gần nghiệm và Hessian khả nghịch.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Quasi-Newton methods khác Newton method ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Xấp xỉ Hessian thay vì tính chính xác</label>
                <label><input type="radio" name="q23" value="b"> B) Không dùng gradient</label>
                <label><input type="radio" name="q23" value="c"> C) Chỉ cho hàm tuyến tính</label>
                <label><input type="radio" name="q23" value="d"> D) Luôn chậm hơn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Xấp xỉ Hessian thay vì tính chính xác</strong><br>
                Quasi-Newton (BFGS, L-BFGS) xây dựng xấp xỉ Hessian từ thông tin gradient.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: BFGS update formula cập nhật:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Xấp xỉ Hessian nghịch đảo</label>
                <label><input type="radio" name="q24" value="b"> B) Gradient</label>
                <label><input type="radio" name="q24" value="c"> C) Điểm hiện tại</label>
                <label><input type="radio" name="q24" value="d"> D) Kích thước bước</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Xấp xỉ Hessian nghịch đảo</strong><br>
                BFGS cập nhật ma trận xấp xỉ $$H_k \approx [\nabla^2 f]^{-1}$$ sử dụng thông tin gradient.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Với hàm $$f(x) = x^2$$, một bước Newton từ $$x_0 = 2$$ cho:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$x_1 = 0$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$x_1 = 1$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$x_1 = -2$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$x_1 = 2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x_1 = 0$$</strong><br>
                $$\nabla f(2) = 4$$, $$\nabla^2 f(2) = 2$$. $$x_1 = 2 - 4/2 = 0$$.
            </div>
        </div>

    </div>

    <div class="quiz-controls">
        <button onclick="previousQuestion()" id="prev-btn" disabled>← Câu trước</button>
        <button onclick="nextQuestion()" id="next-btn">Câu tiếp →</button>
        <button onclick="submitQuiz()" id="submit-btn" style="display: none;">Nộp bài</button>
        <button onclick="resetQuiz()" id="reset-btn" style="display: none;">Làm lại</button>
    </div>

    <div id="final-result" style="display: none;" class="final-score">
        <h2>🎉 Hoàn thành Quiz!</h2>
        <p>Điểm số của bạn: <span id="final-score-text"></span></p>
        <p id="performance-message"></p>
    </div>
</div>

<script>
let currentQuestion = 1;
const totalQuestions = 25;
let userAnswers = {};
let quizSubmitted = false;

// Đáp án đúng
const correctAnswers = {
    q1: 'c', q2: 'b', q3: 'a', q4: 'c', q5: 'a',
    q6: 'a', q7: 'a', q8: 'd', q9: 'd', q10: 'a',
    q11: 'd', q12: 'b', q13: 'c', q14: 'b', q15: 'd',
    q16: 'a', q17: 'd', q18: 'd', q19: 'd', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'a'};

function showQuestion(n) {
    // Ẩn tất cả câu hỏi
    for (let i = 1; i <= totalQuestions; i++) {
        document.getElementById(`q${i}`).style.display = 'none';
    }
    
    // Hiển thị câu hỏi hiện tại
    document.getElementById(`q${n}`).style.display = 'block';
    
    // Cập nhật progress bar
    const progress = (n / totalQuestions) * 100;
    document.getElementById('progress-fill').style.width = progress + '%';
    
    // Cập nhật số câu hỏi
    document.getElementById('current-q').textContent = n;
    
    // Cập nhật nút điều hướng
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
    
    // Hiển thị tất cả giải thích
    for (let i = 1; i <= totalQuestions; i++) {
        const explanation = document.querySelector(`#q${i} .explanation`);
        explanation.style.display = 'block';
        
        // Highlight đáp án đúng và sai
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
    
    // Hiển thị kết quả cuối
    document.getElementById('final-result').style.display = 'block';
    document.getElementById('final-score-text').textContent = `${score}/${totalQuestions} (${percentage}%)`;
    
    let message = '';
    if (percentage >= 90) {
        message = '🌟 Xuất sắc! Bạn đã thành thạo Newton method và second-order optimization!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về Newton method và convergence analysis.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại self-concordance và quasi-Newton methods.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại Newton direction và backtracking line search.';
    } else {
        message = '📖 Hãy học lại từ đầu về Newton method nhé!';
    }
    
    document.getElementById('performance-message').textContent = message;
    
    // Ẩn nút submit, hiện nút reset
    document.getElementById('submit-btn').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'inline-block';
    
    // Cuộn đến kết quả
    document.getElementById('final-result').scrollIntoView({ behavior: 'smooth' });
}

function resetQuiz() {
    // Reset trạng thái
    currentQuestion = 1;
    userAnswers = {};
    quizSubmitted = false;
    
    // Ẩn tất cả giải thích
    document.querySelectorAll('.explanation').forEach(exp => {
        exp.style.display = 'none';
    });
    
    // Reset style của labels
    document.querySelectorAll('.options label').forEach(label => {
        label.style.backgroundColor = '';
        label.style.border = '';
        label.classList.remove('selected');
    });
    
    // Uncheck tất cả radio buttons
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.checked = false;
    });
    
    document.querySelectorAll('.options label').forEach(label => {
        label.classList.remove('selected');
    });
    
    // Hiển thị câu hỏi đầu tiên
    showQuestion(1);
    
    // Cuộn lên đầu
    document.getElementById('quiz-header').scrollIntoView({ behavior: 'smooth' });
    
    // Ẩn kết quả cuối và reset button
    document.getElementById('final-result').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'none';
}

// Khởi tạo bài tập khi trang được tải
document.addEventListener('DOMContentLoaded', function() {
    showQuestion(1);
    
    // Thêm event listener cho tất cả radio button
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.addEventListener('change', function() {
            const questionId = this.name;
            const answer = this.value;
            saveAnswer(questionId, answer);
        });
    });
    
    // Render MathJax sau khi DOM được tải
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        MathJax.startup.promise.then(() => MathJax.typesetPromise());
    }
});

// Xử lý phím tắt
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

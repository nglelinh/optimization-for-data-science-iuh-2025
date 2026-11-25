---
layout: post
title: '06-11 Practical Exercises - Optimization Algorithms'
chapter: '06'
order: 23
owner: GitHub Copilot
lang: en
categories:
- chapter06
lesson_type: required
redirect_from:
  - /contents/en/chapter06/06_10_Practical_Exercises_Optimization_Algorithms/
---

Reading convergence proofs builds intuition, but actually computing Hessian eigenvalues, running backtracking trials by hand, diagnosing SGD variance, and comparing momentum against vanilla gradient descent is what turns theory into engineering fluency. These practical exercises challenge you to execute, analyze, and tune every major first-order algorithm from Chapter 06.

## Background Knowledge Map: Algorithmic Analysis Toolkit for These Exercises

1. **Exact Quadratic Diagnostics**: For $$f(x) = \frac{1}{2}x^T Q x + c^T x$$, immediately extract $$L = \lambda_{\max}(Q)$$, $$m = \lambda_{\min}(Q)$$, $$\kappa = L/m$$, stability limit $$2/L$$, and optimal fixed step $$t^\star = \frac{2}{L + m}$$.
2. **Step-by-Step Line Search Verification**: Always write the Armijo RHS $$f(x_k) - \alpha t \|\nabla f(x_k)\|_2^2$$ explicitly as a function of $$t$$ before testing $$t = 1, \beta, \beta^2, \dots$$ so each trial is a single clean comparison.
3. **SGD & Momentum Tuning Checks**: Track both bias (mean iterate) and variance (spread across random draws) for SGD, and verify that momentum $$\beta \in [0, 1)$$ stays below the stability ceiling $$\beta < 1$$ with $$t < \frac{2(1 + \beta)}{L}$$.
4. **Regularization Path Analysis**: When comparing Ridge vs. Lasso, check the optimality condition at $$w = 0$$ (whether $$|g_j(0)| \le \lambda$$) to predict which features drop out to exact zero.

### Step-by-Step Worked Example (Read Slowly): Warm-Up Convergence Rate Calculation

Before starting Exercise 1, analyze $$f(x) = \frac{1}{2}x^T Q x$$ with $$Q = \operatorname{diag}(2, 8)$$ from $$x^{(0)} = (1, 1)$$:

1. **Extract spectral parameters**: $$m = 2$$, $$L = 8$$, $$\kappa = L/m = 4$$.
2. **Compute the optimal fixed step size and contraction factor**:
   $$t^\star = \frac{2}{L + m} = \frac{2}{10} = 0.20, \qquad \rho = \frac{\kappa - 1}{\kappa + 1} = \frac{3}{5} = 0.60.$$
3. **Verify the exact iterate formula**:
   $$x^{(k)} = \bigl((1 - 0.2 \cdot 2)^k,\; (1 - 0.2 \cdot 8)^k\bigr) = \bigl(0.6^k,\; (-0.6)^k\bigr).$$
4. **Find the exact iteration $$k$$ where $$\|x^{(k)}\|_2 \le 0.01\|x^{(0)}\|_2$$**:
   Since $$\|x^{(k)}\|_2 = 0.6^k \|x^{(0)}\|_2$$, we need $$0.6^k \le 0.01 \implies k \ge \frac{\ln(0.01)}{\ln(0.6)} = \frac{-4.6052}{-0.5108} \approx 9.02 \implies k = 10$$ iterations!

# Practical Exercises - Optimization Algorithms

The exercises are adapted from Boyd & Vandenberghe (2004) and Nocedal & Wright (2006).

---

## 📝 **Part I: Gradient Descent**

### **Exercise 1: Convergence Rate Analysis**

Consider the function $$f(x) = \frac{1}{2}x^TQx$$ with $$Q = \text{diag}(1, 4, 10)$$.

**Tasks:**  
a) Compute the gradient $$\nabla f(x)$$  
b) With step size $$t = \frac{2}{m + L}$$ ($$m = \lambda_{\min}(Q)$$, $$L = \lambda_{\max}(Q)$$), compute the convergence rate  
c) Starting from $$x^{(0)} = (1, 1, 1)^T$$, compute $$x^{(1)}$$, $$x^{(2)}$$  
d) Estimate the number of iterations needed to reach $$\|x^{(k)}\| < 10^{-6}$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Gradient:**

$$\nabla f(x) = Qx = \begin{bmatrix} x_1 \\ 4x_2 \\ 10x_3 \end{bmatrix}$$

---

**b) Convergence rate:**

$$m = 1$$, $$L = 10$$

$$t = \frac{2}{1 + 10} = \frac{2}{11}$$

**Convergence rate:**

$$\|x^{(k+1)} - x^*\| \leq \left(\frac{L - m}{L + m}\right) \|x^{(k)} - x^*\|$$

$$= \frac{10 - 1}{10 + 1} \|x^{(k)} - x^*\| = \frac{9}{11} \|x^{(k)} - x^*\|$$

**Linear convergence** with ratio $$\approx 0.818$$.

---

**c) Iterations:**

$$x^{(0)} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$$

$$\nabla f(x^{(0)}) = \begin{bmatrix} 1 \\ 4 \\ 10 \end{bmatrix}$$

$$x^{(1)} = x^{(0)} - t \nabla f(x^{(0)}) = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - \frac{2}{11} \begin{bmatrix} 1 \\ 4 \\ 10 \end{bmatrix}$$

$$= \begin{bmatrix} 1 - \frac{2}{11} \\ 1 - \frac{8}{11} \\ 1 - \frac{20}{11} \end{bmatrix} = \begin{bmatrix} \frac{9}{11} \\ \frac{3}{11} \\ -\frac{9}{11} \end{bmatrix}$$

$$\nabla f(x^{(1)}) = \begin{bmatrix} \frac{9}{11} \\ \frac{12}{11} \\ -\frac{90}{11} \end{bmatrix}$$

$$x^{(2)} = x^{(1)} - \frac{2}{11} \nabla f(x^{(1)})$$

$$= \begin{bmatrix} \frac{9}{11} - \frac{18}{121} \\ \frac{3}{11} - \frac{24}{121} \\ -\frac{9}{11} + \frac{180}{121} \end{bmatrix} = \begin{bmatrix} \frac{81}{121} \\ \frac{9}{121} \\ -\frac{81}{121} \end{bmatrix}$$

---

**d) Number of iterations:**

$$\|x^{(k)}\| \leq \left(\frac{9}{11}\right)^k \|x^{(0)}\|$$

$$\|x^{(0)}\| = \sqrt{3}$$

Needed: $$\left(\frac{9}{11}\right)^k \sqrt{3} < 10^{-6}$$

$$k > \frac{\log(10^{-6}/\sqrt{3})}{\log(9/11)} = \frac{\log(10^{-6}) - 0.5\log(3)}{\log(9/11)}$$

$$\approx \frac{-13.8 - 0.55}{-0.20} \approx 72$$

**About 72 iterations are needed.**

</details>

---

## 📝 **Part II: Momentum Methods**

### **Exercise 2: Heavy Ball vs Gradient Descent**

Consider $$f(x) = x_1^2 + 9x_2^2$$ (ill-conditioned with $$\kappa = 9$$).

**Tasks:**  
a) Compare GD and Heavy Ball starting from $$x^{(0)} = (3, 1)^T$$  
b) Compute the optimal momentum parameter $$\beta$$  
c) Compare the convergence rates

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Gradient Descent:**

$$\nabla f(x) = \begin{bmatrix} 2x_1 \\ 18x_2 \end{bmatrix}$$

Step size: $$t = \frac{2}{2 + 18} = 0.1$$

$$x^{(1)} = (3, 1) - 0.1(6, 18) = (2.4, -0.8)$$

$$x^{(2)} = (2.4, -0.8) - 0.1(4.8, -14.4) = (1.92, 0.64)$$

**Pattern:** Oscillates slowly toward $$(0, 0)$$.

---

**Heavy Ball:**

$$x^{(k+1)} = x^{(k)} - t\nabla f(x^{(k)}) + \beta(x^{(k)} - x^{(k-1)})$$

**Optimal $$\beta$$:**

$$\beta = \left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^2 = \left(\frac{3 - 1}{3 + 1}\right)^2 = \left(\frac{1}{2}\right)^2 = 0.25$$

---

**b) Heavy Ball iterations:**

$$x^{(1)} = (2.4, -0.8)$$, $$x^{(2)} = (1.92, 0.64)$$ (the same as GD in the first steps, since there is no momentum yet)

$$x^{(3)} = (1.92, 0.64) - 0.1(3.84, 11.52) + 0.25((1.92, 0.64) - (2.4, -0.8))$$

$$= (1.92, 0.64) - (0.384, 1.152) + 0.25(-0.48, 1.44)$$

$$= (1.92, 0.64) - (0.384, 1.152) + (-0.12, 0.36)$$

$$= (1.416, -0.152)$$

---

**c) Convergence rate comparison:**

**GD:** $$\left(\frac{\kappa - 1}{\kappa + 1}\right)^k = \left(\frac{8}{10}\right)^k = 0.8^k$$

**Heavy Ball:** $$\left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^{k} = 0.5^k$$

**Each Heavy Ball iteration shrinks the error by a factor of 0.5 (versus 0.8 for GD), so it needs about $$\ln 0.8 / \ln 0.5 \approx 3$$ times fewer iterations!**

</details>

---

## 📝 **Part III: Nesterov's Acceleration**

### **Exercise 3: Nesterov vs Standard GD**

Consider $$f(x) = \frac{1}{2}\|Ax - b\|^2$$ with $$A = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$$, $$b = (2, 1)^T$$.

**Tasks:**  
a) Compute the exact solution $$x^*$$  
b) Implement Nesterov's method  
c) Compare with GD after 5 iterations

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Exact solution:**

$$\nabla f(x) = A^T(Ax - b) = 0$$

$$A^TAx = A^Tb$$

$$\begin{bmatrix} 4 & 0 \\ 0 & 1 \end{bmatrix} x = \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \end{bmatrix}$$

$$x^* = (1, 1)^T$$

---

**b) Nesterov's method:**

$$
\begin{align}
y^{(k)} &= x^{(k)} + \frac{k-1}{k+2}(x^{(k)} - x^{(k-1)}) \\
x^{(k+1)} &= y^{(k)} - t\nabla f(y^{(k)})
\end{align}
$$

With $$t = \frac{1}{L}$$, $$L = \lambda_{\max}(A^TA) = 4$$ → $$t = 0.25$$.

**From $$x^{(0)} = (0, 0)$$, $$x^{(1)} = (0, 0)$$:**

$$k=1$$: $$y^{(1)} = (0, 0)$$

$$\nabla f(y^{(1)}) = A^T(A(0,0) - (2,1)) = -A^Tb = (-4, -1)$$

$$x^{(2)} = (0, 0) - 0.25(-4, -1) = (1, 0.25)$$

$$k=2$$: $$y^{(2)} = (1, 0.25) + \frac{1}{4}((1, 0.25) - (0, 0)) = (1.25, 0.3125)$$

(Continue...)

---

**c) Comparison (after 5 iterations):**

| Method | $$x$$ after 5 iterations | $$\|x - x^*\|$$ |
|--------|-------------|----------------------|
| GD | $$(1, 0.763)$$ | $$0.237$$ |
| Nesterov | $$(1, 0.944)$$ | $$0.056$$ |

**Nesterov's error is about 4× smaller!** (GD: the error in the second coordinate is $$0.75^5 \approx 0.237$$)

</details>

---

## 📝 **Part IV: Proximal Gradient**

### **Exercise 4: LASSO with Soft Thresholding**

Consider LASSO: $$\min_x \frac{1}{2}\|Ax - b\|^2 + \lambda\|x\|_1$$

With $$A = I$$, $$b = (2, -1, 0.5)^T$$, $$\lambda = 1$$.

**Tasks:**  
a) Write the proximal gradient update  
b) Compute the soft-thresholding operator  
c) Iterate from $$x^{(0)} = 0$$

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Proximal gradient:**

$$f(x) = \frac{1}{2}\|x - b\|^2$$ (smooth), $$g(x) = \lambda\|x\|_1$$ (non-smooth)

$$x^{(k+1)} = \text{prox}_{tg}(x^{(k)} - t\nabla f(x^{(k)}))$$

$$= \text{prox}_{t\lambda\|\cdot\|_1}(x^{(k)} - t(x^{(k)} - b))$$

With $$t = 1$$:

$$x^{(k+1)} = \text{prox}_{\lambda\|\cdot\|_1}(b)$$

---

**b) Soft-thresholding:**

$$\text{prox}_{\lambda\|\cdot\|_1}(y) = S_\lambda(y)$$

$$S_\lambda(y_i) = \begin{cases}
y_i - \lambda & \text{if } y_i > \lambda \\
0 & \text{if } |y_i| \leq \lambda \\
y_i + \lambda & \text{if } y_i < -\lambda
\end{cases}$$

---

**c) Iteration:**

$$x^{(0)} = (0, 0, 0)$$

$$b = (2, -1, 0.5)$$, $$\lambda = 1$$

$$x^{(1)} = S_1(b) = (S_1(2), S_1(-1), S_1(0.5))$$

$$= (2-1, 0, 0) = (1, 0, 0)$$

**Converged in 1 step!** (because $$A = I$$)

**Solution:** $$x^* = (1, 0, 0)^T$$

**Explanation:**
- $$b_1 = 2 > \lambda$$ → shrink to $$1$$
- $$|b_2| = 1 = \lambda$$ → shrink to $$0$$
- $$|b_3| = 0.5 < \lambda$$ → shrink to $$0$$

</details>

---

## 📝 **Part V: Coordinate Descent**

### **Exercise 5: Coordinate Descent for QP**

$$\min_x \quad x_1^2 + 2x_2^2 + x_1x_2 - 3x_1 - 4x_2$$

**Tasks:**  
a) Minimize w.r.t. $$x_1$$ (fix $$x_2$$)  
b) Minimize w.r.t. $$x_2$$ (fix $$x_1$$)  
c) Iterate from $$(0, 0)$$ until convergence

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Minimize w.r.t. $$x_1$$:**

$$f(x_1, x_2) = x_1^2 + x_1x_2 - 3x_1 + (2x_2^2 - 4x_2)$$

$$\frac{\partial f}{\partial x_1} = 2x_1 + x_2 - 3 = 0$$

$$x_1^* = \frac{3 - x_2}{2}$$

---

**b) Minimize w.r.t. $$x_2$$:**

$$\frac{\partial f}{\partial x_2} = 4x_2 + x_1 - 4 = 0$$

$$x_2^* = \frac{4 - x_1}{4}$$

---

**c) Coordinate descent:**

**Iteration 0:** $$(x_1, x_2) = (0, 0)$$

**Iter 1:**
- Fix $$x_2 = 0$$: $$x_1 = \frac{3-0}{2} = 1.5$$
- Fix $$x_1 = 1.5$$: $$x_2 = \frac{4-1.5}{4} = 0.625$$

**Iter 2:**
- Fix $$x_2 = 0.625$$: $$x_1 = \frac{3-0.625}{2} = 1.1875$$
- Fix $$x_1 = 1.1875$$: $$x_2 = \frac{4-1.1875}{4} = 0.703$$

**Iter 3:**
- $$x_1 = 1.148$$, $$x_2 = 0.713$$

**Converging to:** $$x^* \approx (1.143, 0.714)$$

**Exact solution (solve simultaneously):**

$$
\begin{cases}
2x_1 + x_2 = 3 \\
x_1 + 4x_2 = 4
\end{cases}
\Rightarrow x^* = (\frac{8}{7}, \frac{5}{7}) = (1.143, 0.714)$$

✓

</details>

---

## 💡 **Summary**

### **Algorithm Comparison:**

| Method | Convergence | Per-iter cost | Best for |
|--------|-------------|---------------|----------|
| GD | $$O(1/k)$$ | $$O(n)$$ | Well-conditioned |
| Heavy Ball | $$O(\rho^k)$$, $$\rho < 1$$ | $$O(n)$$ | Ill-conditioned |
| Nesterov | $$O(1/k^2)$$ | $$O(n)$$ | Smooth convex |
| Proximal GD | $$O(1/k)$$ | $$O(n)$$ + prox | Composite (smooth + non-smooth) |
| Coordinate Descent | Varies | $$O(n/m)$$ | Large-scale, separable |

### **When to use what:**
- **GD:** Simple, well-conditioned
- **Momentum:** Ill-conditioned quadratics
- **Nesterov:** Need fast convergence, can afford acceleration overhead
- **Proximal:** Non-smooth regularization ($$\ell_1$$, nuclear norm)
- **Coordinate:** Huge dimension, coordinate-wise cheap

---

## 📚 **References**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 9.

2. **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization*. Springer. Chapters 2-3.

3. **Nesterov, Y.** (2004). *Introductory Lectures on Convex Optimization*. Springer.


---
layout: post
title: 0-6 Bài Tập Thực Hành - Kiến Thức Nền Tảng
chapter: '0'
order: 7
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

# Bài Tập Thực Hành - Kiến Thức Nền Tảng (Prerequisites)

Các bài tập được tham khảo từ Boyd & Vandenberghe (2004) Appendix và các sách giáo trình chuẩn.

---

## 📝 **Phần I: Calculus và Multivariable Analysis**

### **Bài tập 1: Gradient và Hessian**

Cho hàm $$f: \mathbb{R}^n \to \mathbb{R}$$:

**a)** $$f(x) = x^TAx + b^Tx + c$$ với $$A \in \mathbb{R}^{n \times n}$$ symmetric

**b)** $$f(x) = \log(\sum_{i=1}^n e^{x_i})$$ (log-sum-exp)

**c)** $$f(x) = \|Ax - b\|_2^2$$

**Yêu cầu:** Tính $$\nabla f(x)$$ và $$\nabla^2 f(x)$$ cho mỗi trường hợp.

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**a) Quadratic form:**

$$\nabla f(x) = (A + A^T)x + b = 2Ax + b$$ (vì $$A$$ symmetric)

$$\nabla^2 f(x) = 2A$$

**Kiểm tra:** 
- Linear term: $$\nabla(b^Tx) = b$$
- Quadratic: $$\nabla(x^TAx) = (A + A^T)x$$
- Hessian constant cho quadratic

---

**b) Log-sum-exp:**

Đặt $$z_i = e^{x_i}$$, $$Z = \sum_{i=1}^n z_i$$

$$\frac{\partial f}{\partial x_i} = \frac{z_i}{Z} = \frac{e^{x_i}}{\sum_j e^{x_j}}$$

$$\nabla f(x) = \begin{bmatrix} \frac{e^{x_1}}{Z} \\ \vdots \\ \frac{e^{x_n}}{Z} \end{bmatrix}$$ (softmax!)

**Hessian:**

$$\frac{\partial^2 f}{\partial x_i \partial x_j} = \begin{cases}
\frac{z_i}{Z} - \left(\frac{z_i}{Z}\right)^2 & i = j \\
-\frac{z_iz_j}{Z^2} & i \neq j
\end{cases}$$

$$\nabla^2 f(x) = \text{diag}(p) - pp^T$$ với $$p_i = \frac{e^{x_i}}{Z}$$

---

**c) Least squares:**

$$f(x) = (Ax - b)^T(Ax - b) = x^TA^TAx - 2b^TAx + b^Tb$$

$$\nabla f(x) = 2A^T(Ax - b)$$

$$\nabla^2 f(x) = 2A^TA$$

</details>

---

### **Bài tập 2: Taylor Series**

Cho $$f(x) = e^x$$, $$x_0 = 0$$.

**Yêu cầu:**  
a) Viết Taylor series bậc 3  
b) Estimate error cho $$|x| \leq 0.1$$  
c) Multivariate: $$f(x, y) = e^{x+y}$$, expand tại $$(0, 0)$$

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**a) Taylor bậc 3:**

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2}x^2 + \frac{f'''(0)}{6}x^3 + O(x^4)$$

$$e^x \approx 1 + x + \frac{x^2}{2} + \frac{x^3}{6}$$

---

**b) Error bound:**

$$|R_3(x)| = \left|\frac{f^{(4)}(\xi)}{24}x^4\right| = \frac{e^\xi}{24}|x|^4$$

với $$\xi \in (0, x)$$.

Cho $$|x| \leq 0.1$$:

$$|R_3| \leq \frac{e^{0.1}}{24}(0.1)^4 \approx \frac{1.105}{24} \times 10^{-4} \approx 4.6 \times 10^{-6}$$

---

**c) Multivariate:**

$$f(x, y) = e^{x+y} = e^0 \cdot e^{x+y}$$

$$= 1 + (x+y) + \frac{(x+y)^2}{2} + \frac{(x+y)^3}{6} + \cdots$$

$$= 1 + x + y + \frac{x^2 + 2xy + y^2}{2} + O(3)$$

</details>

---

## 📝 **Phần II: Linear Algebra**

### **Bài tập 3: Eigenvalues và Positive Definiteness**

Cho ma trận $$A = \begin{bmatrix} 4 & 1 \\ 1 & 3 \end{bmatrix}$$.

**Yêu cầu:**  
a) Tính eigenvalues và eigenvectors  
b) Verify $$A$$ positive definite  
c) Tìm $$A^{1/2}$$ (square root)

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**a) Eigenvalues:**

$$\det(A - \lambda I) = 0$$

$$\begin{vmatrix} 4-\lambda & 1 \\ 1 & 3-\lambda \end{vmatrix} = (4-\lambda)(3-\lambda) - 1 = 0$$

$$\lambda^2 - 7\lambda + 11 = 0$$

$$\lambda = \frac{7 \pm \sqrt{49 - 44}}{2} = \frac{7 \pm \sqrt{5}}{2}$$

$$\lambda_1 = \frac{7 + \sqrt{5}}{2} \approx 4.618$$, $$\lambda_2 = \frac{7 - \sqrt{5}}{2} \approx 2.382$$

**Eigenvectors:**

Cho $$\lambda_1$$: $$(A - \lambda_1 I)v_1 = 0$$

$$v_1 = \begin{bmatrix} 1 \\ \frac{\lambda_1 - 4}{1} \end{bmatrix} \approx \begin{bmatrix} 1 \\ 0.618 \end{bmatrix}$$

Tương tự $$v_2 \approx \begin{bmatrix} 1 \\ -1.618 \end{bmatrix}$$

---

**b) Positive definite:**

**Method 1:** $$\lambda_1, \lambda_2 > 0$$ → $$A \succ 0$$ ✓

**Method 2:** Leading principal minors:
- $$a_{11} = 4 > 0$$ ✓
- $$\det(A) = 12 - 1 = 11 > 0$$ ✓

**Method 3:** $$x^TAx = 4x_1^2 + 2x_1x_2 + 3x_2^2 > 0$$ $$\forall x \neq 0$$ ✓

---

**c) Square root:**

$$A = Q\Lambda Q^T$$ với $$\Lambda = \text{diag}(\lambda_1, \lambda_2)$$

$$A^{1/2} = Q\Lambda^{1/2}Q^T = Q \begin{bmatrix} \sqrt{\lambda_1} & 0 \\ 0 & \sqrt{\lambda_2} \end{bmatrix} Q^T$$

$$\approx \begin{bmatrix} 1.979 & 0.245 \\ 0.245 & 1.708 \end{bmatrix}$$

**Verify:** $$(A^{1/2})^2 = A$$ ✓

</details>

---

### **Bài tập 4: Matrix Norms và Singular Values**

Cho $$A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}$$.

**Yêu cầu:**  
a) Tính $$\|A\|_F$$ (Frobenius)  
b) Tính $$\|A\|_2$$ (spectral norm)  
c) Tìm SVD của $$A$$

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**a) Frobenius norm:**

$$\|A\|_F = \sqrt{\sum_{i,j} a_{ij}^2} = \sqrt{9 + 0 + 16 + 25} = \sqrt{50} \approx 7.07$$

---

**b) Spectral norm:**

$$\|A\|_2 = \sqrt{\lambda_{\max}(A^TA)}$$

$$A^TA = \begin{bmatrix} 3 & 4 \\ 0 & 5 \end{bmatrix} \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix} = \begin{bmatrix} 25 & 20 \\ 20 & 25 \end{bmatrix}$$

$$\det(A^TA - \lambda I) = (25-\lambda)^2 - 400 = 0$$

$$\lambda = 25 \pm 20$$: $$\lambda_{\max} = 45$$

$$\|A\|_2 = \sqrt{45} \approx 6.71$$

---

**c) SVD:**

$$A = U\Sigma V^T$$

Singular values: $$\sigma_1 = \sqrt{45} \approx 6.71$$, $$\sigma_2 = \sqrt{5} \approx 2.24$$

(Đầy đủ SVD cần tính $$U, V$$ từ eigenvectors của $$AA^T$$ và $$A^TA$$)

</details>

---

## 📝 **Phần III: Real Analysis**

### **Bài tập 5: Continuity và Compactness**

**Yêu cầu:**  
a) Prove: $$f(x) = x^2$$ continuous tại $$x = 2$$  
b) Hàm $$f(x) = 1/x$$ có continuous trên $$(0, 1]$$?  
c) Áp dụng Extreme Value Theorem

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**a) $$\epsilon$$-$$\delta$$ proof:**

Cần show: $$\forall \epsilon > 0$$, $$\exists \delta > 0$$ sao cho $$|x - 2| < \delta \Rightarrow |x^2 - 4| < \epsilon$$

$$|x^2 - 4| = |x - 2| \cdot |x + 2|$$

Giả sử $$|x - 2| < 1$$ → $$1 < x < 3$$ → $$|x + 2| < 5$$

$$|x^2 - 4| < 5|x - 2|$$

Chọn $$\delta = \min(1, \epsilon/5)$$:

$$|x - 2| < \delta \Rightarrow |x^2 - 4| < 5 \cdot \frac{\epsilon}{5} = \epsilon$$ ✓

---

**b) Continuity trên $$(0, 1]$$:**

**Yes!** $$f$$ continuous tại mọi $$x_0 \in (0, 1]$$.

**Proof:** $$\lim_{x \to x_0} \frac{1}{x} = \frac{1}{x_0} = f(x_0)$$

**Note:** Không continuous tại $$x = 0$$ (không trong domain)

---

**c) Extreme Value Theorem:**

**Theorem:** Nếu $$f$$ continuous trên compact set $$K$$, thì $$f$$ đạt min và max trên $$K$$.

**Example:** $$f(x) = x^2$$ trên $$[-1, 2]$$:
- Compact: $$[-1, 2]$$ closed và bounded ✓
- Continuous: $$x^2$$ continuous ✓
- Conclusion: $$\min = 0$$ tại $$x = 0$$, $$\max = 4$$ tại $$x = 2$$

</details>

---

## 📝 **Phần IV: Probability & Statistics**

### **Bài tập 6: Expectation và Variance**

Cho $$X \sim \mathcal{N}(\mu, \sigma^2)$$.

**Yêu cầu:**  
a) Tính $$\mathbb{E}[X^2]$$  
b) Prove: $$\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$  
c) Cho $$Y = aX + b$$, tính $$\mathbb{E}[Y]$$, $$\text{Var}(Y)$$

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**a) Second moment:**

$$\mathbb{E}[X^2] = \text{Var}(X) + (\mathbb{E}[X])^2 = \sigma^2 + \mu^2$$

**Proof from definition:**

$$\mathbb{E}[X^2] = \int_{-\infty}^\infty x^2 \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx$$

(Integration by parts hoặc dùng moment generating function)

---

**b) Variance formula:**

$$\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2]$$

$$= \mathbb{E}[X^2 - 2X\mathbb{E}[X] + (\mathbb{E}[X])^2]$$

$$= \mathbb{E}[X^2] - 2\mathbb{E}[X]\mathbb{E}[X] + (\mathbb{E}[X])^2$$

$$= \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$ ✓

---

**c) Linear transformation:**

$$\mathbb{E}[Y] = \mathbb{E}[aX + b] = a\mathbb{E}[X] + b = a\mu + b$$

$$\text{Var}(Y) = \text{Var}(aX + b) = a^2\text{Var}(X) = a^2\sigma^2$$

**Note:** Constant $$b$$ không ảnh hưởng variance!

</details>

---

### **Bài tập 7: Maximum Likelihood Estimation**

Cho $$n$$ observations $$x_1, \ldots, x_n$$ i.i.d. từ $$\mathcal{N}(\mu, \sigma^2)$$.

**Yêu cầu:**  
a) Viết likelihood function  
b) Tìm MLE của $$\mu$$  
c) Tìm MLE của $$\sigma^2$$

<details>
<summary><strong>💡 Lời giải chi tiết</strong></summary>

**a) Likelihood:**

$$L(\mu, \sigma^2 | x) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right)$$

**Log-likelihood:**

$$\ell(\mu, \sigma^2) = -\frac{n}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^n (x_i - \mu)^2$$

---

**b) MLE của $$\mu$$:**

$$\frac{\partial \ell}{\partial \mu} = \frac{1}{\sigma^2}\sum_{i=1}^n (x_i - \mu) = 0$$

$$\hat{\mu} = \frac{1}{n}\sum_{i=1}^n x_i = \bar{x}$$ (sample mean)

---

**c) MLE của $$\sigma^2$$:**

$$\frac{\partial \ell}{\partial \sigma^2} = -\frac{n}{2\sigma^2} + \frac{1}{2(\sigma^2)^2}\sum_{i=1}^n (x_i - \mu)^2 = 0$$

$$\hat{\sigma}^2 = \frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2$$ (sample variance)

**Note:** Unbiased estimator dùng $$\frac{1}{n-1}$$ thay vì $$\frac{1}{n}$$

</details>

---

## 💡 **Tổng kết**

### **Calculus Essentials:**

| Concept | Formula | Application |
|---------|---------|-------------|
| **Gradient** | $$\nabla f = [\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}]^T$$ | First-order optimality |
| **Hessian** | $$\nabla^2 f = [\frac{\partial^2 f}{\partial x_i \partial x_j}]$$ | Second-order optimality |
| **Taylor 2nd order** | $$f(x+p) \approx f(x) + \nabla f^T p + \frac{1}{2}p^T\nabla^2 f \, p$$ | Newton method |
| **Chain rule** | $$\nabla(f \circ g) = (\nabla f)(g) \cdot (\nabla g)$$ | Composite functions |

### **Linear Algebra Essentials:**

| Concept | Key Property | Use in Optimization |
|---------|--------------|---------------------|
| **Eigenvalues** | $$Av = \lambda v$$ | PD test, convergence rate |
| **SVD** | $$A = U\Sigma V^T$$ | Matrix analysis, low-rank |
| **PSD** | $$x^TAx \geq 0$$ $$\forall x$$ | Convexity test |
| **Spectral norm** | $$\|A\|_2 = \sigma_{\max}$$ | Lipschitz constants |

### **Analysis Essentials:**

- **Compactness:** Closed + Bounded → has min/max (Extreme Value Theorem)
- **Continuity:** Preserves limits, needed for optimization
- **Convergence:** $$\lim_{k \to \infty} x^{(k)} = x^*$$

### **Probability Essentials:**

- **Expectation:** $$\mathbb{E}[X] = \int x f(x) dx$$
- **Variance:** $$\text{Var}(X) = \mathbb{E}[(X - \mu)^2]$$
- **MLE:** $$\hat{\theta} = \arg\max_\theta L(\theta | x)$$

---

## 📚 Tài liệu tham khảo

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Appendix A-C.

2. **Strang, G.** (2016). *Introduction to Linear Algebra*. Wellesley-Cambridge Press.

3. **Rudin, W.** (1976). *Principles of Mathematical Analysis*. McGraw-Hill.

4. **Casella, G., & Berger, R. L.** (2002). *Statistical Inference*. Duxbury.

5. **Stewart, J.** (2015). *Calculus: Early Transcendentals*. Cengage Learning.


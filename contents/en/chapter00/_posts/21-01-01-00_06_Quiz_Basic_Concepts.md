---
layout: post
title: '00-06 Multiple-Choice Quiz - Basic Concepts'
chapter: '00'
order: 19
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: quiz
redirect_from:
  - /contents/en/chapter00/00_05_Quiz_Basic_Concepts/
---

This multiple-choice quiz tests your understanding of the basic concepts of calculus and linear algebra that form the foundation of optimization.

---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### 🔢 **Basic Calculus**

**Derivatives and partial derivatives:**
- Derivative: $$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$
- Partial derivative: $$\frac{\partial f}{\partial x_i}$$ - the derivative with respect to $$x_i$$ when the other variables are held fixed

**Gradient and directional derivative:**
- Gradient: $$\nabla f = \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix}$$ - the vector pointing in the direction of steepest ascent
- Directional derivative: $$D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u} = \|\nabla f\| \cos \theta$$

**Taylor series:**
- First order: $$f(\mathbf{x}) \approx f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T (\mathbf{x} - \mathbf{x}_0)$$
- Second order: $$f(\mathbf{x}) \approx f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T (\mathbf{x} - \mathbf{x}_0) + \frac{1}{2} (\mathbf{x} - \mathbf{x}_0)^T \nabla^2 f(\mathbf{x}_0) (\mathbf{x} - \mathbf{x}_0)$$

### 📐 **Linear Algebra**

**Vectors and vector spaces:**
- Vector: an ordered list of numbers $$\mathbf{v} = \begin{pmatrix} v_1 \\ \vdots \\ v_n \end{pmatrix}$$
- The space $$\mathbb{R}^n$$: the set of all vectors with $$n$$ components

**Vector operations:**
- Vector addition: $$\mathbf{u} + \mathbf{v} = \begin{pmatrix} u_1 + v_1 \\ \vdots \\ u_n + v_n \end{pmatrix}$$
- Scalar multiplication: $$c\mathbf{v} = \begin{pmatrix} cv_1 \\ \vdots \\ cv_n \end{pmatrix}$$
- Dot product: $$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos \theta$$

**Vector norms:**
- L2 (Euclidean) norm: $$\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2}$$
- L1 (Manhattan) norm: $$\|\mathbf{x}\|_1 = \sum_{i=1}^n \lvert x_i \rvert$$
- L∞ (Max) norm: $$\|\mathbf{x}\|_\infty = \max_i \lvert x_i \rvert$$

**Matrices:**
- Matrix multiplication: $$(AB)_{ij} = \sum_{k} A_{ik} B_{kj}$$
- Inverse matrix: $$AA^{-1} = I$$ (if it exists)
- Determinant: $$\det(A)$$ - measures the "volume" scaling of the linear map

**Eigenvalues and eigenvectors:**
- $$A\mathbf{v} = \lambda \mathbf{v}$$ with $$\mathbf{v} \neq \mathbf{0}$$
- $$\lambda$$: eigenvalue, $$\mathbf{v}$$: the corresponding eigenvector

### 📊 **Set Theory and Real Analysis**

**Basic sets:**
- Open set: every point has a neighborhood contained in the set
- Closed set: contains all of its boundary points
- Compact set: closed and bounded in $$\mathbb{R}^n$$

**Continuity:**
- Function continuous at $$x_0$$: $$\lim_{x \to x_0} f(x) = f(x_0)$$
- Uniformly continuous: $$\forall \epsilon > 0, \exists \delta > 0$$ such that $$\lvert x-y \rvert < \delta \Rightarrow \lvert f(x)-f(y) \rvert < \epsilon$$

### 🎲 **Basic Probability**

**Basic concepts:**
- Probability: $$P(A) \in [0,1]$$, $$P(\Omega) = 1$$
- Random variable: a function from the sample space to the real numbers
- Expectation: $$E[X] = \int x f(x) dx$$ (continuous) or $$E[X] = \sum x P(X=x)$$ (discrete)

**Common distributions:**
- Normal: $$X \sim N(\mu, \sigma^2)$$
- Uniform: $$X \sim U(a,b)$$
- Bernoulli: $$X \sim \text{Ber}(p)$$

---

💡 **Tip:** These concepts are the foundation of optimization. The gradient points in the direction of fastest increase, the Hessian matrix describes curvature, and the Taylor series gives local approximations of a function.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Multiple-Choice Quiz: Basic Concepts</h2>
        <p>Choose the best answer for each question. You will see your results as soon as you finish.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Question 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Question 1 -->
        <div class="question" id="q1">
            <h3>Question 1: The derivative of $$f(x) = x^3 + 2x^2 - 5x + 1$$ at $$x = 1$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) $$4$$</label>
                <label><input type="radio" name="q1" value="b"> B) $$2$$</label>
                <label><input type="radio" name="q1" value="c"> C) $$-1$$</label>
                <label><input type="radio" name="q1" value="d"> D) $$6$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$2$$</strong><br>
                $$f'(x) = 3x^2 + 4x - 5$$<br>
                $$f'(1) = 3(1)^2 + 4(1) - 5 = 3 + 4 - 5 = 2$$
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: Let $$f(x,y) = x^2y + 3xy^2$$. The partial derivative $$\frac{\partial f}{\partial x}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) $$2xy + 3y^2$$</label>
                <label><input type="radio" name="q2" value="b"> B) $$x^2 + 6xy$$</label>
                <label><input type="radio" name="q2" value="c"> C) $$2xy + 6xy$$</label>
                <label><input type="radio" name="q2" value="d"> D) $$x^2 + 3y^2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$2xy + 3y^2$$</strong><br>
                When taking the partial derivative with respect to $$x$$, we treat $$y$$ as a constant:<br>
                $$\frac{\partial f}{\partial x} = \frac{\partial}{\partial x}(x^2y + 3xy^2) = 2xy + 3y^2$$
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: The gradient of $$f(x,y) = x^2 + 2xy + y^2$$ at the point $$(1,1)$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$\begin{pmatrix} 4 \\ 4 \end{pmatrix}$$</label>
                <label><input type="radio" name="q3" value="b"> B) $$\begin{pmatrix} 2 \\ 2 \end{pmatrix}$$</label>
                <label><input type="radio" name="q3" value="c"> C) $$\begin{pmatrix} 3 \\ 3 \end{pmatrix}$$</label>
                <label><input type="radio" name="q3" value="d"> D) $$\begin{pmatrix} 1 \\ 1 \end{pmatrix}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{pmatrix} 4 \\ 4 \end{pmatrix}$$</strong><br>
                $$\frac{\partial f}{\partial x} = 2x + 2y$$, $$\frac{\partial f}{\partial y} = 2x + 2y$$<br>
                At $$(1,1)$$: $$\nabla f(1,1) = \begin{pmatrix} 2(1) + 2(1) \\ 2(1) + 2(1) \end{pmatrix} = \begin{pmatrix} 4 \\ 4 \end{pmatrix}$$
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: Given the gradient $$\nabla f = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$ and the unit vector $$\mathbf{u} = \begin{pmatrix} 0.6 \\ 0.8 \end{pmatrix}$$, the directional derivative $$D_{\mathbf{u}}f$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$5$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$4.8$$</label>
                <label><input type="radio" name="q4" value="c"> C) $$3.2$$</label>
                <label><input type="radio" name="q4" value="d"> D) $$7$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$5$$</strong><br>
                $$D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u} = 3(0.6) + 4(0.8) = 1.8 + 3.2 = 5$$
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: The direction of steepest ascent of a function is always:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) The direction of the gradient vector</label>
                <label><input type="radio" name="q5" value="b"> B) The direction opposite to the gradient vector</label>
                <label><input type="radio" name="q5" value="c"> C) A direction perpendicular to the gradient vector</label>
                <label><input type="radio" name="q5" value="d"> D) The direction of the x-axis</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The direction of the gradient vector</strong><br>
                The gradient always points in the direction of steepest ascent of the function. This is a fundamental property of the gradient.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: Let $$\mathbf{u} = \begin{pmatrix} 2 \\ -1 \\ 3 \end{pmatrix}$$ and $$\mathbf{v} = \begin{pmatrix} 1 \\ 4 \\ -2 \end{pmatrix}$$. The vector $$\mathbf{u} + \mathbf{v}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) $$\begin{pmatrix} 3 \\ 3 \\ 1 \end{pmatrix}$$</label>
                <label><input type="radio" name="q6" value="b"> B) $$\begin{pmatrix} 1 \\ -5 \\ 5 \end{pmatrix}$$</label>
                <label><input type="radio" name="q6" value="c"> C) $$\begin{pmatrix} 2 \\ 4 \\ -6 \end{pmatrix}$$</label>
                <label><input type="radio" name="q6" value="d"> D) $$\begin{pmatrix} 3 \\ -3 \\ 1 \end{pmatrix}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{pmatrix} 3 \\ 3 \\ 1 \end{pmatrix}$$</strong><br>
                $$\mathbf{u} + \mathbf{v} = \begin{pmatrix} 2+1 \\ -1+4 \\ 3+(-2) \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \\ 1 \end{pmatrix}$$
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: The dot product of $$\mathbf{a} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$$ and $$\mathbf{b} = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) $$32$$</label>
                <label><input type="radio" name="q7" value="b"> B) $$14$$</label>
                <label><input type="radio" name="q7" value="c"> C) $$18$$</label>
                <label><input type="radio" name="q7" value="d"> D) $$24$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$32$$</strong><br>
                $$\mathbf{a} \cdot \mathbf{b} = 1 \cdot 4 + 2 \cdot 5 + 3 \cdot 6 = 4 + 10 + 18 = 32$$
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The Euclidean norm of the vector $$\mathbf{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) $$5$$</label>
                <label><input type="radio" name="q8" value="b"> B) $$7$$</label>
                <label><input type="radio" name="q8" value="c"> C) $$25$$</label>
                <label><input type="radio" name="q8" value="d"> D) $$\sqrt{7}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$5$$</strong><br>
                $$\|\mathbf{v}\|_2 = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: Two vectors $$\mathbf{u}$$ and $$\mathbf{v}$$ are called orthogonal when:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) $$\mathbf{u} \cdot \mathbf{v} = 0$$</label>
                <label><input type="radio" name="q9" value="b"> B) $$\mathbf{u} \cdot \mathbf{v} = 1$$</label>
                <label><input type="radio" name="q9" value="c"> C) $$\|\mathbf{u}\| = \|\mathbf{v}\|$$</label>
                <label><input type="radio" name="q9" value="d"> D) $$\mathbf{u} + \mathbf{v} = \mathbf{0}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\mathbf{u} \cdot \mathbf{v} = 0$$</strong><br>
                Two vectors are orthogonal (perpendicular) if and only if their dot product is 0.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: The product of the two matrices $$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) $$\begin{pmatrix} 4 & 6 \\ 10 & 12 \end{pmatrix}$$</label>
                <label><input type="radio" name="q10" value="b"> B) $$\begin{pmatrix} 2 & 4 \\ 10 & 14 \end{pmatrix}$$</label>
                <label><input type="radio" name="q10" value="c"> C) $$\begin{pmatrix} 2 & 0 \\ 3 & 12 \end{pmatrix}$$</label>
                <label><input type="radio" name="q10" value="d"> D) $$\begin{pmatrix} 3 & 2 \\ 4 & 7 \end{pmatrix}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{pmatrix} 4 & 6 \\ 10 & 12 \end{pmatrix}$$</strong><br>
                Entry $$(1,1)$$: $$1 \cdot 2 + 2 \cdot 1 = 4$$<br>
                Entry $$(1,2)$$: $$1 \cdot 0 + 2 \cdot 3 = 6$$<br>
                Entry $$(2,1)$$: $$3 \cdot 2 + 4 \cdot 1 = 10$$<br>
                Entry $$(2,2)$$: $$3 \cdot 0 + 4 \cdot 3 = 12$$
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: The $$2 \times 2$$ identity matrix is:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) $$\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$</label>
                <label><input type="radio" name="q11" value="b"> B) $$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$</label>
                <label><input type="radio" name="q11" value="c"> C) $$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$$</label>
                <label><input type="radio" name="q11" value="d"> D) $$\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$</strong><br>
                The identity matrix has ones on the main diagonal and zeros everywhere else.
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The transpose of the matrix $$\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) $$\begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$</label>
                <label><input type="radio" name="q12" value="b"> B) $$\begin{pmatrix} 6 & 5 & 4 \\ 3 & 2 & 1 \end{pmatrix}$$</label>
                <label><input type="radio" name="q12" value="c"> C) $$\begin{pmatrix} 4 & 1 \\ 5 & 2 \\ 6 & 3 \end{pmatrix}$$</label>
                <label><input type="radio" name="q12" value="d"> D) $$\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$</strong><br>
                The transpose of a matrix is formed by swapping its rows and columns.
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The determinant of the matrix $$\begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) $$10$$</label>
                <label><input type="radio" name="q13" value="b"> B) $$14$$</label>
                <label><input type="radio" name="q13" value="c"> C) $$2$$</label>
                <label><input type="radio" name="q13" value="d"> D) $$12$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$10$$</strong><br>
                $$\det\begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} = 3 \cdot 4 - 1 \cdot 2 = 12 - 2 = 10$$
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: The two vectors $$\mathbf{v}_1 = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$ and $$\mathbf{v}_2 = \begin{pmatrix} 2 \\ 4 \end{pmatrix}$$ are:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Linearly independent</label>
                <label><input type="radio" name="q14" value="b"> B) Linearly dependent</label>
                <label><input type="radio" name="q14" value="c"> C) Orthogonal</label>
                <label><input type="radio" name="q14" value="d"> D) Cannot be determined</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Linearly dependent</strong><br>
                $$\mathbf{v}_2 = 2\mathbf{v}_1$$, so the two vectors are linearly dependent.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: The Manhattan (L1) norm of the vector $$\mathbf{v} = \begin{pmatrix} -2 \\ 3 \\ -1 \end{pmatrix}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) $$6$$</label>
                <label><input type="radio" name="q15" value="b"> B) $$0$$</label>
                <label><input type="radio" name="q15" value="c"> C) $$4$$</label>
                <label><input type="radio" name="q15" value="d"> D) $$\sqrt{14}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$6$$</strong><br>
                $$\|\mathbf{v}\|_1 = |-2| + |3| + |-1| = 2 + 3 + 1 = 6$$
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: Let $$z = x^2 + y^2$$ with $$x = 2t$$ and $$y = 3t$$. The derivative $$\frac{dz}{dt}$$ at $$t = 1$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) $$26$$</label>
                <label><input type="radio" name="q16" value="b"> B) $$13$$</label>
                <label><input type="radio" name="q16" value="c"> C) $$10$$</label>
                <label><input type="radio" name="q16" value="d"> D) $$5$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$26$$</strong><br>
                $$\frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt} = 2x \cdot 2 + 2y \cdot 3$$<br>
                At $$t = 1$$: $$x = 2, y = 3$$, so $$\frac{dz}{dt} = 2(2)(2) + 2(3)(3) = 8 + 18 = 26$$
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: A critical point of a function is a point where:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) The gradient equals the zero vector</label>
                <label><input type="radio" name="q17" value="b"> B) The function attains its maximum value</label>
                <label><input type="radio" name="q17" value="c"> C) The function attains its minimum value</label>
                <label><input type="radio" name="q17" value="d"> D) The function is undefined</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) The gradient equals the zero vector</strong><br>
                A critical point is a point where the gradient of the function is the zero vector, i.e. $$\nabla f = \mathbf{0}$$.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: The inverse of the matrix $$\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) $$\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$$</label>
                <label><input type="radio" name="q18" value="b"> B) $$\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$$</label>
                <label><input type="radio" name="q18" value="c"> C) $$\begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$$</label>
                <label><input type="radio" name="q18" value="d"> D) $$\begin{pmatrix} 0.5 & 0.5 \\ 0.5 & 1 \end{pmatrix}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$$</strong><br>
                $$\det(A) = 2 \cdot 1 - 1 \cdot 1 = 1$$<br>
                $$A^{-1} = \frac{1}{1}\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$$
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: The (nonzero) gradient of a function at a point is always:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Perpendicular to the level curve at that point</label>
                <label><input type="radio" name="q19" value="b"> B) Parallel to the level curve at that point</label>
                <label><input type="radio" name="q19" value="c"> C) At a 45° angle to the level curve</label>
                <label><input type="radio" name="q19" value="d"> D) Unrelated to the level curve</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Perpendicular to the level curve at that point</strong><br>
                The gradient is always perpendicular to the level curve, because the level curve is the set of points with the same function value.
            </div>
        </div>

        <!-- Question 20 -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: In the gradient descent algorithm, we move in the direction:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Opposite to the gradient</label>
                <label><input type="radio" name="q20" value="b"> B) Along the gradient</label>
                <label><input type="radio" name="q20" value="c"> C) Perpendicular to the gradient</label>
                <label><input type="radio" name="q20" value="d"> D) A random direction</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Opposite to the gradient</strong><br>
                Gradient descent moves in the direction $$-\nabla f$$ to find a minimum of the function.
            </div>
        </div>

        <!-- Question 21 -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: The second derivative of $$f(x) = 3x^4 - 2x^3 + x^2 - 5x + 1$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$36x^2 - 12x + 2$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$12x^3 - 6x^2 + 2x - 5$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$36x^2 - 12x + 1$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$12x^2 - 6x + 2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$36x^2 - 12x + 2$$</strong><br>
                $$f'(x) = 12x^3 - 6x^2 + 2x - 5$$<br>
                $$f''(x) = 36x^2 - 12x + 2$$
            </div>
        </div>

        <!-- Question 22 -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: Let $$f(x,y) = x^2 + 2xy + 3y^2$$. The Hessian matrix at the point $$(1,1)$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$\begin{pmatrix} 2 & 2 \\ 2 & 6 \end{pmatrix}$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$\begin{pmatrix} 2 & 1 \\ 1 & 6 \end{pmatrix}$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$\begin{pmatrix} 4 & 4 \\ 4 & 8 \end{pmatrix}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\begin{pmatrix} 2 & 2 \\ 2 & 6 \end{pmatrix}$$</strong><br>
                $$\frac{\partial^2 f}{\partial x^2} = 2$$, $$\frac{\partial^2 f}{\partial y^2} = 6$$, $$\frac{\partial^2 f}{\partial x \partial y} = 2$$<br>
                In this case the Hessian matrix does not depend on the particular point.
            </div>
        </div>

        <!-- Question 23 -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: The distance from the point $$A(1,2)$$ to the point $$B(4,6)$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$5$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$7$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$25$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$3$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$5$$</strong><br>
                Distance = $$\sqrt{(4-1)^2 + (6-2)^2} = \sqrt{9 + 16} = \sqrt{25} = 5$$
            </div>
        </div>

        <!-- Question 24 -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: The eigenvalues of the matrix $$A = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$$ are:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$\lambda_1 = 3, \lambda_2 = 2$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$\lambda_1 = 3, \lambda_2 = 1$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$\lambda_1 = 1, \lambda_2 = 5$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$\lambda_1 = 0, \lambda_2 = 5$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\lambda_1 = 3, \lambda_2 = 2$$</strong><br>
                For an upper triangular matrix, the eigenvalues are exactly the entries on the main diagonal.
            </div>
        </div>

        <!-- Question 25 -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: The minimizer of $$f(x) = x^2 - 4x + 5$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$x = 2$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$x = -2$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$x = 4$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$x = 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$x = 2$$</strong><br>
                $$f'(x) = 2x - 4 = 0 \Rightarrow x = 2$$<br>
                $$f''(x) = 2 > 0$$, so $$x = 2$$ is a minimizer.
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
    background: linear-gradient(90deg, #4CAF50, #45a049);
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
    align-items: center;
    padding: 12px;
    background: white;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 1em;
}

.options label:hover {
    border-color: #4CAF50;
    background-color: #f0f8f0;
}

.options input[type="radio"] {
    margin-right: 12px;
    transform: scale(1.2);
}

.options label.selected {
    border-color: #4CAF50;
    background-color: #e8f5e8;
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
    background: #4CAF50;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #45a049;
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
    border: 2px solid #4CAF50;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #2E7D32;
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
    q1: 'b', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'a', q13: 'a', q14: 'b', q15: 'a',
    q16: 'a', q17: 'a', q18: 'a', q19: 'a', q20: 'a',
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'a'
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
            ${scorePercentage >= 80 ? '🎉 Excellent!' :
              scorePercentage >= 60 ? '👍 Pretty good!' :
              scorePercentage >= 40 ? '📚 Needs more review' : '💪 Keep trying!'}
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

---
layout: post
title: '05-02-04 Logistic Regression'
chapter: '05'
order: 8
owner: GitHub Copilot
categories:
- chapter05
lang: en
lesson_type: required
---

Try predicting whether a tumor is malignant ($$y = 1$$) or benign ($$y = 0$$) using linear regression and two disasters strike immediately: predictions shoot past $$0$$ and $$1$$ into meaningless probabilities like $$-0.4$$ or $$1.7$$, and a single confident outlier drags the entire decision boundary off course. Logistic regression fixes both by passing the linear score $$w^T x$$ through the sigmoid function—and miraculously, the resulting cross-entropy loss is still a smooth, globally convex optimization problem!

## Key ideas: Convexity Behind Logistic Regression

1. **Log-Odds and the Sigmoid Link**: Modeling the log-odds as linear, $$\ln\frac{p}{1 - p} = w^T x$$, maps any real score $$z = w^T x \in \mathbb{R}$$ smoothly into a calibrated probability $$p = \sigma(z) = \frac{1}{1 + e^{-z}} \in (0, 1)$$.
2. **Convexity of Binary Cross-Entropy**: For labels $$y_i \in \{0, 1\}$$, the negative log-likelihood is
   $$J(w) = \sum_{i=1}^m \Bigl[\ln\bigl(1 + e^{w^T x_i}\bigr) - y_i (w^T x_i)\Bigr].$$
   Its Hessian is $$\nabla^2 J(w) = X^T D X$$ where $$D = \operatorname{diag}\bigl(p_i(1 - p_i)\bigr) \succ 0$$, proving $$J(w)$$ is **globally convex** (and strictly convex whenever $$X$$ has full column rank).
3. **No Closed-Form Solution, Fast Iterative Solvers**: Unlike linear least squares, $$\nabla J(w) = X^T(p - y) = 0$$ is nonlinear in $$w$$ and cannot be inverted in one shot. Because $$J(w)$$ is smooth and convex, Gradient Descent, L-BFGS, and Newton's Method (Iteratively Reweighted Least Squares, IRLS) converge rapidly to the unique global minimum.
4. **Linear Separability Requires Regularization**: If two classes are perfectly separable by a hyperplane, pushing $$\|w\|_2 \to \infty$$ drives $$J(w) \to 0$$ with no finite minimizer. Adding $$\frac{\lambda}{2}\|w\|_2^2$$ makes the objective strongly convex and guarantees a finite, well-behaved maximum-margin-like separator.

### Worked example: Computing Gradient, Hessian, and One Newton Step

Consider 1D logistic regression without intercept ($$z_i = w x_i$$) on two points: $$(x_1, y_1) = (1, 1)$$ and $$(x_2, y_2) = (-1, 0)$$, with L2 regularization $$\frac{1}{2}w^2$$ ($$\lambda = 1$$):
$$J(w) = \ln(1 + e^{w}) - w + \ln(1 + e^{-w}) + \frac{1}{2}w^2.$$
Start at $$w_0 = 0$$.

1. **Compute predicted probabilities at $$w_0 = 0$$**:
   $$p_1 = \sigma(0) = 0.5, \qquad p_2 = \sigma(0) = 0.5.$$
2. **Compute the first derivative (gradient) at $$w_0 = 0$$**:
   $$J'(w) = x_1(p_1 - y_1) + x_2(p_2 - y_2) + w = 1(0.5 - 1) + (-1)(0.5 - 0) + 0 = -0.5 - 0.5 = -1.$$
   Since $$J'(0) = -1 < 0$$, increasing $$w$$ reduces the loss.
3. **Compute the second derivative (Hessian) at $$w_0 = 0$$**:
   $$J''(w) = x_1^2 p_1(1 - p_1) + x_2^2 p_2(1 - p_2) + 1 = 1(0.25) + 1(0.25) + 1 = 1.5 > 0.$$
   (Strictly positive, confirming strict convexity!)
4. **Take one Newton step**:
   $$w_1 = w_0 - \frac{J'(w_0)}{J''(w_0)} = 0 - \frac{-1}{1.5} = \frac{2}{3} \approx 0.6667.$$
   Check the drop in loss: $$J(0) = 2\ln 2 \approx 1.3863$$, while at $$w_1 = 2/3$$, $$\ln(1 + e^{2/3}) - \frac{2}{3} + \ln(1 + e^{-2/3}) + \frac{2}{9} = 2\ln(1 + e^{-2/3}) + \frac{2}{9} \approx 2(0.4144) + 0.2222 = 1.0510$$—nearly at the global minimum in a single step!

# Logistic Regression

Logistic regression is one of the most important applications of convex optimization in machine learning, and is widely used for binary classification problems.

## 🎯 The Binary Classification Problem

Unlike linear regression, which predicts a continuous value, **binary classification** predicts the probability that a sample belongs to one of two classes.

**Real-world examples:**
- **Medicine**: Predicting whether a patient has a disease (0: healthy, 1: sick)
- **Marketing**: Whether a customer buys a product (0: does not buy, 1: buys)
- **Finance**: Whether an email is spam (0: not spam, 1: spam)
- **Technology**: Whether a transaction is fraudulent (0: legitimate, 1: fraudulent)

**Training data:**
- $$\{(\mathbf{x}_i, y_i)\}_{i=1}^n$$ with $$\mathbf{x}_i \in \mathbb{R}^p$$, $$y_i \in \{0, 1\}$$
- $$\mathbf{x}_i$$: feature vector
- $$y_i$$: class label

## 📊 From Linear Regression to Logistic Regression

### The Problem with Linear Regression for Classification

If we apply linear regression directly: $$\hat{y} = \mathbf{w}^T \mathbf{x} + b$$

**The problem:**
- $$\hat{y}$$ can take any value: $$(-\infty, +\infty)$$
- But a probability must lie in $$[0, 1]$$
- This does not match the probabilistic nature of classification

### The Sigmoid Function - An Important Bridge

**The sigmoid function:**
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

**Important properties:**
- **Range**: $$\sigma(z) \in (0, 1)$$ $$\forall z \in \mathbb{R}$$
- **Monotonically increasing**: $$\sigma'(z) > 0$$ $$\forall z$$
- **Symmetry**: $$\sigma(-z) = 1 - \sigma(z)$$
- **Limits**: $$\lim_{z \to -\infty} \sigma(z) = 0$$, $$\lim_{z \to +\infty} \sigma(z) = 1$$

**A special derivative:**
$$\sigma'(z) = \sigma(z)(1 - \sigma(z))$$


### The Logistic Regression Model

**Predicted probability:**
$$P(y = 1 | \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x}) = \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}}}$$

$$P(y = 0 | \mathbf{x}) = 1 - P(y = 1 | \mathbf{x}) = \frac{e^{-\mathbf{w}^T \mathbf{x}}}{1 + e^{-\mathbf{w}^T \mathbf{x}}}$$

**Decision rule:**
$$\hat{y} = \begin{cases}
1 & \text{if } P(y = 1 | \mathbf{x}) \geq 0.5 \\
0 & \text{if } P(y = 1 | \mathbf{x}) < 0.5
\end{cases}$$

## 🧮 The Cross-Entropy Loss

In logistic regression, we use the **Cross-Entropy Loss** to measure the difference between predictions and reality:

$$J(\mathbf{w}) = -\sum_{i=1}^n \left[ y_i \log p_i + (1-y_i) \log (1-p_i) \right]$$

where $$p_i = \sigma(\mathbf{w}^T \mathbf{x}_i)$$ is the predicted probability.

**Important characteristics:**
- **Heavy penalty for wrong predictions:** The more wrong the prediction, the larger and unbounded the loss
- **Smooth and convex:** Guarantees efficient optimization
- **Probabilistic:** Matches the probabilistic nature of the problem

## 🔍 Proof of Convexity

### Theorem: The logistic loss function is convex

<div class="textbook-proof" markdown="1">
**Proof:**
</div>

**Step 1:** Show that $$-\log \sigma(z)$$ is convex

$$-\log \sigma(z) = -\log \frac{1}{1 + e^{-z}} = \log(1 + e^{-z})$$

Second derivative:
$$\frac{d^2}{dz^2} \log(1 + e^{-z}) = \frac{e^{-z}}{(1 + e^{-z})^2} = \sigma(z)(1 - \sigma(z)) > 0$$

⟹ $$-\log \sigma(z)$$ is convex in $$z$$

**Step 2:** Show that $$-\log(1 - \sigma(z))$$ is convex

$$-\log(1 - \sigma(z)) = -\log \frac{e^{-z}}{1 + e^{-z}} = z + \log(1 + e^{-z})$$

Second derivative:
$$\frac{d^2}{dz^2} [z + \log(1 + e^{-z})] = \frac{e^{-z}}{(1 + e^{-z})^2} > 0$$

⟹ $$-\log(1 - \sigma(z))$$ is convex in $$z$$

**Step 3:** Conclusion

Since $$z = \mathbf{w}^T \mathbf{x}_i$$ is affine in $$\mathbf{w}$$, and a sum of convex functions is convex:

$$J(\mathbf{w}) = \sum_{i=1}^n \left[ -y_i \log \sigma(\mathbf{w}^T \mathbf{x}_i) - (1-y_i) \log (1 - \sigma(\mathbf{w}^T \mathbf{x}_i)) \right]$$

is a **convex function** of $$\mathbf{w}$$.

## 📈 The Gradient of the Loss Function

**Gradient:**
$$\nabla_{\mathbf{w}} J(\mathbf{w}) = \sum_{i=1}^n (\sigma(\mathbf{w}^T \mathbf{x}_i) - y_i) \mathbf{x}_i = \mathbf{X}^T (\boldsymbol{\sigma} - \mathbf{y})$$

with:
- $$\mathbf{X} \in \mathbb{R}^{n \times p}$$: the feature matrix
- $$\boldsymbol{\sigma} = [\sigma(\mathbf{w}^T \mathbf{x}_1), ..., \sigma(\mathbf{w}^T \mathbf{x}_n)]^T$$
- $$\mathbf{y} = [y_1, ..., y_n]^T$$

**Hessian:**
$$\nabla^2_{\mathbf{w}} J(\mathbf{w}) = \mathbf{X}^T \mathbf{S} \mathbf{X}$$

with $$\mathbf{S} = \text{diag}(\sigma(\mathbf{w}^T \mathbf{x}_i)(1 - \sigma(\mathbf{w}^T \mathbf{x}_i)))$$

Since the diagonal entries of $$\mathbf{S}$$ are positive, we have $$\nabla^2_{\mathbf{w}} J(\mathbf{w}) = \mathbf{X}^T \mathbf{S} \mathbf{X} \succeq 0$$ ⟹ **convex function**.

### 🎯 The Significance of Convexity

**Why does convexity matter?**

1. **Guarantees a global optimum:**
   - Every **local minimum is a global minimum** (the set of optimal solutions is convex)
   - There are no "false" local minima as in neural networks
   - Optimization algorithms head toward a global optimum

2. **Gradient descent works efficiently:**
   - **Converges** to the optimal solution (with a suitable learning rate, when an optimal solution exists; for perfectly linearly separable data the optimum lies at infinity and $$\|\mathbf{w}\|$$ keeps growing)
   - **Does not get stuck** at local minima
   - **Simple and stable** - no complicated techniques are needed

3. **Powerful optimization theory:**
   - We can prove **convergence rates**
   - We can **estimate the error**
   - There are clear **stopping criteria**

### 🚀 From Convexity to Gradient Descent

**Since the logistic loss is convex and differentiable**, we can use **Gradient Descent** with confidence:

**The basic algorithm:**
$$\mathbf{w}^{(k+1)} = \mathbf{w}^{(k)} - \alpha \nabla J(\mathbf{w}^{(k)})$$

with the gradient:
$$\nabla J(\mathbf{w}) = \mathbf{X}^T (\boldsymbol{\sigma} - \mathbf{y})$$

**Convergence guarantee:**
- Choose a suitable learning rate $$\alpha$$ → **converges**
- No need to worry about local minima
- The behavior of the algorithm is predictable

**Connection with Chapter 6:**
In **Chapter 6 - Gradient Descent**, we will study in detail:
- How to choose the optimal learning rate
- Convergence rate analysis
- Variants such as Stochastic Gradient Descent
- **Logistic Regression will be the main example** illustrating these concepts!

## 🔄 Comparison with Linear Regression

| Aspect | Linear Regression | Logistic Regression |
|-----------|-------------------|---------------------|
| **Problem** | Regression | Classification |
| **Output** | Continuous value | Probability $$\in [0,1]$$ |
| **Activation function** | Identity: $$f(z) = z$$ | Sigmoid: $$\sigma(z) = \frac{1}{1+e^{-z}}$$ |
| **Loss function** | MSE: $$\frac{1}{2n}\sum(y_i - \hat{y}_i)^2$$ | Cross-entropy: $$-\sum[y_i \log p_i + (1-y_i)\log(1-p_i)]$$ |
| **Closed-form solution** | Yes (if $$\mathbf{X}^T\mathbf{X}$$ is invertible): $$\mathbf{w}^* = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$ | None |
| **Algorithm** | Normal equation or GD | Gradient Descent |
| **Convexity** | Convex (quadratic) | Convex |

## 💡 Illustrative Example: Spam Email Prediction

**Problem:** Classify spam emails based on the number of suspicious keywords.

**Data:**
- $$x$$: the number of spam keywords in the email
- $$y$$: 1 if spam, 0 if not spam

**Model:**
$$P(\text{spam} | x) = \sigma(w_0 + w_1 x) = \frac{1}{1 + e^{-(w_0 + w_1 x)}}$$

**Interpretation:**
- If $$w_1 > 0$$: the more spam keywords, the higher the probability of spam
- Decision point: $$x^* = -\frac{w_0}{w_1}$$ (when $$P = 0.5$$)

## 🎛️ Interactive Visualization

<div id="logistic-regression-demo" style="margin: 20px 0;">
    <div style="display: flex; gap: 20px; margin-bottom: 20px;">
        <div style="flex: 1;">
            <h4>🎚️ Parameter Controls</h4>
            <div style="margin: 10px 0;">
                <label for="w0-slider">Bias (w₀): <span id="w0-value">0</span></label>
                <input type="range" id="w0-slider" min="-5" max="5" step="0.1" value="0" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <label for="w1-slider">Weight (w₁): <span id="w1-value">1</span></label>
                <input type="range" id="w1-slider" min="-3" max="3" step="0.1" value="1" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <button id="add-data-btn" style="padding: 8px 16px; margin: 5px;">Add Data</button>
                <button id="clear-data-btn" style="padding: 8px 16px; margin: 5px;">Clear Data</button>
                <button id="fit-model-btn" style="padding: 8px 16px; margin: 5px;">Fit Model</button>
            </div>
        </div>
        <div style="flex: 1;">
            <h4>📊 Model Information</h4>
            <div id="model-info">
                <p><strong>Equation:</strong> P(y=1|x) = σ(<span id="equation">0 + 1·x</span>)</p>
                <p><strong>Decision point:</strong> x = <span id="decision-boundary">0</span></p>
                <p><strong>Loss:</strong> <span id="current-loss">-</span></p>
                <p><strong>Accuracy:</strong> <span id="accuracy">-</span></p>
            </div>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
            <h4>📈 Sigmoid Function</h4>
            <canvas id="sigmoid-canvas" width="400" height="300" style="border: 1px solid #ccc;"></canvas>
        </div>
        <div style="flex: 1;">
            <h4>🎯 Classification Results</h4>
            <canvas id="classification-canvas" width="400" height="300" style="border: 1px solid #ccc;"></canvas>
        </div>
    </div>
    
    <div style="margin-top: 20px;">
        <h4>📉 Loss Function Visualization</h4>
        <canvas id="loss-canvas" width="800" height="300" style="border: 1px solid #ccc;"></canvas>
    </div>
</div>

<script>
class LogisticRegressionDemo {
    constructor() {
        this.w0 = 0;
        this.w1 = 1;
        this.dataPoints = [];
        this.isAddingData = false;
        
        this.initializeCanvases();
        this.setupEventListeners();
        this.generateSampleData();
        this.updateVisualization();
    }
    
    initializeCanvases() {
        this.sigmoidCanvas = document.getElementById('sigmoid-canvas');
        this.sigmoidCtx = this.sigmoidCanvas.getContext('2d');
        
        this.classificationCanvas = document.getElementById('classification-canvas');
        this.classificationCtx = this.classificationCanvas.getContext('2d');
        
        this.lossCanvas = document.getElementById('loss-canvas');
        this.lossCtx = this.lossCanvas.getContext('2d');
    }
    
    setupEventListeners() {
        const w0Slider = document.getElementById('w0-slider');
        const w1Slider = document.getElementById('w1-slider');
        const addDataBtn = document.getElementById('add-data-btn');
        const clearDataBtn = document.getElementById('clear-data-btn');
        const fitModelBtn = document.getElementById('fit-model-btn');
        
        w0Slider.addEventListener('input', (e) => {
            this.w0 = parseFloat(e.target.value);
            document.getElementById('w0-value').textContent = this.w0.toFixed(1);
            this.updateVisualization();
        });
        
        w1Slider.addEventListener('input', (e) => {
            this.w1 = parseFloat(e.target.value);
            document.getElementById('w1-value').textContent = this.w1.toFixed(1);
            this.updateVisualization();
        });
        
        addDataBtn.addEventListener('click', () => {
            this.isAddingData = !this.isAddingData;
            addDataBtn.textContent = this.isAddingData ? 'Stop Adding' : 'Add Data';
            addDataBtn.style.backgroundColor = this.isAddingData ? '#ff6b6b' : '';
        });
        
        clearDataBtn.addEventListener('click', () => {
            this.dataPoints = [];
            this.updateVisualization();
        });
        
        fitModelBtn.addEventListener('click', () => {
            this.fitModel();
        });
        
        // Click to add data points
        this.classificationCanvas.addEventListener('click', (e) => {
            if (this.isAddingData) {
                const rect = this.classificationCanvas.getBoundingClientRect();
                const x = (e.clientX - rect.left - 50) / 300 * 10 - 5; // Scale to [-5, 5]
                const y = e.clientY - rect.top > 150 ? 0 : 1; // Top half = class 1, bottom = class 0
                this.dataPoints.push({x, y});
                this.updateVisualization();
            }
        });
    }
    
    generateSampleData() {
        // Generate some sample data
        const sampleData = [
            {x: -3, y: 0}, {x: -2.5, y: 0}, {x: -2, y: 0}, {x: -1.5, y: 0},
            {x: -1, y: 0}, {x: -0.5, y: 0}, {x: 0, y: 0}, {x: 0.5, y: 1},
            {x: 1, y: 1}, {x: 1.5, y: 1}, {x: 2, y: 1}, {x: 2.5, y: 1}, {x: 3, y: 1}
        ];
        
        // Add some noise
        this.dataPoints = sampleData.map(point => ({
            x: point.x + (Math.random() - 0.5) * 0.5,
            y: Math.random() < 0.1 ? 1 - point.y : point.y // 10% label noise
        }));
    }
    
    sigmoid(z) {
        return 1 / (1 + Math.exp(-z));
    }
    
    predict(x) {
        return this.sigmoid(this.w0 + this.w1 * x);
    }
    
    calculateLoss() {
        if (this.dataPoints.length === 0) return 0;
        
        let loss = 0;
        for (const point of this.dataPoints) {
            const p = this.predict(point.x);
            const epsilon = 1e-15; // Prevent log(0)
            const clampedP = Math.max(epsilon, Math.min(1 - epsilon, p));
            loss += -point.y * Math.log(clampedP) - (1 - point.y) * Math.log(1 - clampedP);
        }
        return loss / this.dataPoints.length;
    }
    
    calculateAccuracy() {
        if (this.dataPoints.length === 0) return 0;
        
        let correct = 0;
        for (const point of this.dataPoints) {
            const prediction = this.predict(point.x) >= 0.5 ? 1 : 0;
            if (prediction === point.y) correct++;
        }
        return correct / this.dataPoints.length;
    }
    
    fitModel() {
        if (this.dataPoints.length === 0) return;
        
        // Simple gradient descent
        const learningRate = 0.1;
        const iterations = 1000;
        
        for (let iter = 0; iter < iterations; iter++) {
            let gradW0 = 0, gradW1 = 0;
            
            for (const point of this.dataPoints) {
                const p = this.predict(point.x);
                const error = p - point.y;
                gradW0 += error;
                gradW1 += error * point.x;
            }
            
            gradW0 /= this.dataPoints.length;
            gradW1 /= this.dataPoints.length;
            
            this.w0 -= learningRate * gradW0;
            this.w1 -= learningRate * gradW1;
        }
        
        // Update sliders
        document.getElementById('w0-slider').value = this.w0;
        document.getElementById('w1-slider').value = this.w1;
        document.getElementById('w0-value').textContent = this.w0.toFixed(1);
        document.getElementById('w1-value').textContent = this.w1.toFixed(1);
        
        this.updateVisualization();
    }
    
    drawSigmoid() {
        const ctx = this.sigmoidCtx;
        const canvas = this.sigmoidCanvas;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(canvas.width - 20, canvas.height - 50);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(50, 20);
        ctx.lineTo(50, canvas.height - 50);
        ctx.stroke();
        
        // Draw sigmoid curve
        ctx.strokeStyle = '#2196F3';
        ctx.lineWidth = 2;
        ctx.beginPath();
        
        for (let i = 0; i <= 300; i++) {
            const x = (i / 300) * 10 - 5; // x from -5 to 5
            const z = this.w0 + this.w1 * x;
            const y = this.sigmoid(z);
            
            const canvasX = 50 + (x + 5) / 10 * 300;
            const canvasY = canvas.height - 50 - y * 200;
            
            if (i === 0) {
                ctx.moveTo(canvasX, canvasY);
            } else {
                ctx.lineTo(canvasX, canvasY);
            }
        }
        ctx.stroke();
        
        // Draw decision boundary
        if (this.w1 !== 0) {
            const decisionX = -this.w0 / this.w1;
            if (decisionX >= -5 && decisionX <= 5) {
                const canvasX = 50 + (decisionX + 5) / 10 * 300;
                ctx.strokeStyle = '#ff6b6b';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(canvasX, 20);
                ctx.lineTo(canvasX, canvas.height - 50);
                ctx.stroke();
                ctx.setLineDash([]);
            }
        }
        
        // Labels
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('P(y=1|x)', 10, 30);
        ctx.fillText('x', canvas.width - 15, canvas.height - 30);
        ctx.fillText('0', 45, canvas.height - 30);
        ctx.fillText('1', 45, 25);
        ctx.fillText('0.5', 35, canvas.height - 150);
    }
    
    drawClassification() {
        const ctx = this.classificationCtx;
        const canvas = this.classificationCanvas;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw background regions
        ctx.fillStyle = 'rgba(255, 107, 107, 0.1)'; // Red for class 0
        ctx.fillRect(50, canvas.height/2, 300, canvas.height/2 - 50);
        
        ctx.fillStyle = 'rgba(76, 175, 80, 0.1)'; // Green for class 1
        ctx.fillRect(50, 20, 300, canvas.height/2 - 20);
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(350, canvas.height - 50);
        ctx.stroke();
        
        // Y-axis (class separator)
        ctx.beginPath();
        ctx.moveTo(50, canvas.height/2);
        ctx.lineTo(350, canvas.height/2);
        ctx.stroke();
        
        // Draw data points
        for (const point of this.dataPoints) {
            const canvasX = 50 + (point.x + 5) / 10 * 300;
            const canvasY = point.y === 1 ? canvas.height/4 : 3*canvas.height/4;
            
            ctx.fillStyle = point.y === 1 ? '#4CAF50' : '#f44336';
            ctx.beginPath();
            ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
            ctx.fill();
        }
        
        // Draw decision boundary
        if (this.w1 !== 0) {
            const decisionX = -this.w0 / this.w1;
            if (decisionX >= -5 && decisionX <= 5) {
                const canvasX = 50 + (decisionX + 5) / 10 * 300;
                ctx.strokeStyle = '#2196F3';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(canvasX, 20);
                ctx.lineTo(canvasX, canvas.height - 50);
                ctx.stroke();
            }
        }
        
        // Labels
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('Class 1', 10, 40);
        ctx.fillText('Class 0', 10, canvas.height - 60);
        ctx.fillText('x', 360, canvas.height - 30);
    }
    
    drawLoss() {
        const ctx = this.lossCtx;
        const canvas = this.lossCanvas;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        if (this.dataPoints.length === 0) return;
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(canvas.width - 20, canvas.height - 50);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(50, 20);
        ctx.lineTo(50, canvas.height - 50);
        ctx.stroke();
        
        // Calculate loss surface
        const originalW0 = this.w0;
        const originalW1 = this.w1;
        
        const w0Range = [-3, 3];
        const w1Range = [-2, 2];
        const resolution = 50;
        
        let minLoss = Infinity;
        let maxLoss = -Infinity;
        const lossData = [];
        
        for (let i = 0; i <= resolution; i++) {
            lossData[i] = [];
            for (let j = 0; j <= resolution; j++) {
                this.w0 = w0Range[0] + (w0Range[1] - w0Range[0]) * i / resolution;
                this.w1 = w1Range[0] + (w1Range[1] - w1Range[0]) * j / resolution;
                const loss = this.calculateLoss();
                lossData[i][j] = loss;
                minLoss = Math.min(minLoss, loss);
                maxLoss = Math.max(maxLoss, loss);
            }
        }
        
        // Draw contour lines
        const numContours = 10;
        for (let c = 0; c < numContours; c++) {
            const level = minLoss + (maxLoss - minLoss) * c / numContours;
            ctx.strokeStyle = `hsl(${240 - c * 20}, 70%, 60%)`;
            ctx.lineWidth = 1;
            
            // Simple contour drawing (could be improved)
            for (let i = 0; i < resolution; i++) {
                for (let j = 0; j < resolution; j++) {
                    if (Math.abs(lossData[i][j] - level) < (maxLoss - minLoss) / numContours / 2) {
                        const x = 50 + i / resolution * (canvas.width - 70);
                        const y = canvas.height - 50 - j / resolution * (canvas.height - 70);
                        ctx.fillRect(x, y, 2, 2);
                    }
                }
            }
        }
        
        // Mark current position
        this.w0 = originalW0;
        this.w1 = originalW1;
        
        const currentX = 50 + (this.w0 - w0Range[0]) / (w0Range[1] - w0Range[0]) * (canvas.width - 70);
        const currentY = canvas.height - 50 - (this.w1 - w1Range[0]) / (w1Range[1] - w1Range[0]) * (canvas.height - 70);
        
        ctx.fillStyle = '#ff6b6b';
        ctx.beginPath();
        ctx.arc(currentX, currentY, 6, 0, 2 * Math.PI);
        ctx.fill();
        
        // Labels
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('w₁', 10, canvas.height - 30);
        ctx.fillText('w₀', canvas.width - 20, canvas.height - 30);
    }
    
    updateVisualization() {
        this.drawSigmoid();
        this.drawClassification();
        this.drawLoss();
        
        // Update info panel
        const equation = `${this.w0.toFixed(1)} + ${this.w1.toFixed(1)}·x`;
        document.getElementById('equation').textContent = equation;
        
        const decisionBoundary = this.w1 !== 0 ? (-this.w0 / this.w1).toFixed(2) : '∞';
        document.getElementById('decision-boundary').textContent = decisionBoundary;
        
        const loss = this.calculateLoss();
        document.getElementById('current-loss').textContent = loss.toFixed(3);
        
        const accuracy = this.calculateAccuracy();
        document.getElementById('accuracy').textContent = (accuracy * 100).toFixed(1) + '%';
    }
}

// Initialize demo when page loads
document.addEventListener('DOMContentLoaded', () => {
    new LogisticRegressionDemo();
});
</script>

<style>
#logistic-regression-demo {
    font-family: Arial, sans-serif;
    max-width: 1000px;
    margin: 0 auto;
}

#logistic-regression-demo canvas {
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

#logistic-regression-demo input[type="range"] {
    width: 100%;
    margin: 5px 0;
}

#logistic-regression-demo button {
    background-color: #2196F3;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

#logistic-regression-demo button:hover {
    background-color: #1976D2;
}

#model-info {
    background-color: #f5f5f5;
    padding: 15px;
    border-radius: 4px;
    font-size: 14px;
}

#model-info p {
    margin: 5px 0;
}
</style>


---

💡 **Practice exercise:** Try changing the parameters in the visualization above to understand better how logistic regression works!

---

## 📖 Further Reading: Alternative Link Functions to the Sigmoid

*This section is for those who want to learn more about why the sigmoid function is chosen, why the cross-entropy loss is used, and the alternatives in generalized linear models.*

## 🧮 Why Is Cross-Entropy the Loss Function?

### 🎯 Goal: Find the Best Weights

**Core question:** How do we find the weights $$\mathbf{w}$$ so that the model predicts as accurately as possible?

**Idea:** Choose $$\mathbf{w}$$ so that **the probability of observing the actual data is highest**.

### 🔍 From Probability to Cross-Entropy

#### **Step 1: Modeling the probability**

For each data sample $$(\mathbf{x}_i, y_i)$$, the model predicts:
- If $$y_i = 1$$: the probability is $$p_i = \sigma(\mathbf{w}^T \mathbf{x}_i)$$
- If $$y_i = 0$$: the probability is $$1 - p_i = 1 - \sigma(\mathbf{w}^T \mathbf{x}_i)$$

#### **Step 2: Likelihood**

**Question:** With the current weights $$\mathbf{w}$$, how likely is it to observe all of the data?

**Answer:** Multiply the probabilities of all the samples:
$$\text{Likelihood} = p_1^{y_1} \cdot (1-p_1)^{1-y_1} \times p_2^{y_2} \cdot (1-p_2)^{1-y_2} \times \ldots$$

#### **Step 3: The Maximum Likelihood Principle**

**Principle:** Choose $$\mathbf{w}$$ to **maximize the likelihood** = choose $$\mathbf{w}$$ so that the observed data is as likely as possible.

**A practical problem:** The likelihood is a product of many small numbers → hard to compute and numerically unstable.

#### **Step 4: Log-Likelihood**

**Solution:** Take the logarithm to turn the product into a sum:
$$\log(\text{Likelihood}) = \sum_{i=1}^n \left[ y_i \log p_i + (1-y_i) \log (1-p_i) \right]$$

**Benefits:**
- More numerically stable
- Maximizing the log-likelihood = maximizing the likelihood

#### **Step 5: Cross-Entropy Loss**

**Final conversion:** Maximizing = minimizing the negative

$$J(\mathbf{w}) = -\log(\text{Likelihood}) = -\sum_{i=1}^n \left[ y_i \log p_i + (1-y_i) \log (1-p_i) \right]$$

**This is exactly the Cross-Entropy Loss!**

### 💡 Why Is Cross-Entropy "Reasonable"?

#### **1. Heavy penalty for wrong predictions**

**Illustrative example:**
- **Case 1:** $$y = 1$$ (actual), $$p = 0.9$$ (predicted)
  - Loss = $$-1 \times \log(0.9) = 0.105$$ (low - good!)

- **Case 2:** $$y = 1$$ (actual), $$p = 0.1$$ (predicted)  
  - Loss = $$-1 \times \log(0.1) = 2.303$$ (high - bad!)

**Conclusion:** The more wrong the prediction, the larger the loss, and it is **unbounded** (it grows roughly linearly in the size of the error as $$p \to 0$$).

#### **2. It encourages confident predictions**

Cross-entropy "rewards" confident and correct predictions:
- $$p = 0.99$$ when $$y = 1$$ → very low loss
- $$p = 0.51$$ when $$y = 1$$ → the loss is still high (even though it is correct)

#### **3. Smooth and differentiable**

Unlike accuracy (0-1 loss), cross-entropy is:
- **Smooth**: has derivatives everywhere
- **Convex**: guarantees a global optimum
- **Informative gradient**: the gradient is large when the prediction is wrong

### 🔄 Comparison with Other Losses

| Loss Function | Formula | Advantages | Disadvantages |
|---------------|-----------|---------|------------|
| **Cross-Entropy** | $$-[y\log p + (1-y)\log(1-p)]$$ | Smooth, convex, principled | Sensitive to outliers |
| **Mean Squared Error** | $$(y - p)^2$$ | Simple, familiar | Not probabilistic |
| **0-1 Loss** | $$\mathbf{1}[y \neq \text{round}(p)]$$ | Direct accuracy | Non-differentiable |

### 🎯 Conclusion on Cross-Entropy

**Cross-Entropy is not an arbitrary choice** - it arises naturally from:

1. **The Maximum Likelihood principle** - the best way to fit a probabilistic model
2. **Good mathematical properties** - convex, smooth, differentiable  
3. **Practical meaning** - heavily penalizes wrong predictions, encourages confidence

**This is why cross-entropy is the "gold standard" for classification problems!**

## 🤔 Why Choose the Sigmoid Function?

### 1. **Mathematical Requirements for an Activation Function**

To convert from $$\mathbb{R}$$ to a probability in $$[0,1]$$, we need a function $$g: \mathbb{R} \to [0,1]$$ satisfying:

**Mandatory requirements:**
- ✅ **Monotonic**: $$g'(z) > 0$$ (preserves ordering)
- ✅ **Bounded**: $$g(z) \in [0,1]$$ (a valid probability)
- ✅ **Smooth**: differentiable, so we can compute gradients
- ✅ **Asymptotic**: $$\lim_{z \to -\infty} g(z) = 0$$, $$\lim_{z \to +\infty} g(z) = 1$$

**Desirable requirements:**
- 🎯 **Simple derivative**: the derivative is easy to compute
- 🎯 **Probabilistic interpretation**: it has a probabilistic meaning
- 🎯 **Symmetric**: $$g(-z) = 1 - g(z)$$

### 2. **The Origin in Odds and Logit**

**Odds:**
$$\text{Odds} = \frac{P(y=1|x)}{P(y=0|x)} = \frac{P(y=1|x)}{1-P(y=1|x)}$$

**Log-odds (Logit):**
$$\text{logit}(p) = \log\left(\frac{p}{1-p}\right)$$

**A linear model for the log-odds:**
$$\log\left(\frac{P(y=1|x)}{1-P(y=1|x)}\right) = \mathbf{w}^T \mathbf{x}$$

**Solving back for P:**
$$\frac{P(y=1|x)}{1-P(y=1|x)} = e^{\mathbf{w}^T \mathbf{x}}$$

$$P(y=1|x) = (1-P(y=1|x)) \cdot e^{\mathbf{w}^T \mathbf{x}}$$

$$P(y=1|x) = e^{\mathbf{w}^T \mathbf{x}} - P(y=1|x) \cdot e^{\mathbf{w}^T \mathbf{x}}$$

$$P(y=1|x)(1 + e^{\mathbf{w}^T \mathbf{x}}) = e^{\mathbf{w}^T \mathbf{x}}$$

$$P(y=1|x) = \frac{e^{\mathbf{w}^T \mathbf{x}}}{1 + e^{\mathbf{w}^T \mathbf{x}}} = \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}}} = \sigma(\mathbf{w}^T \mathbf{x})$$

⟹ **The sigmoid arises naturally from the linear log-odds model!**

### 3. **Special Advantages of the Sigmoid**

#### **a) An Elegant Derivative**
$$\sigma'(z) = \sigma(z)(1 - \sigma(z))$$

**Benefits:**
- No need to recompute $$e^{-z}$$
- Efficient gradient descent
- Simple backpropagation

#### **b) Symmetry**
$$\sigma(-z) = 1 - \sigma(z)$$

**Meaning:** If $$P(y=1|x) = 0.7$$ then $$P(y=1|-x) = 0.3$$ (for the model without a bias term)

#### **c) A Natural Probabilistic Interpretation**
- $$z = 0 \Rightarrow P = 0.5$$ (no bias)
- $$z > 0 \Rightarrow P > 0.5$$ (leans toward class 1)
- $$z < 0 \Rightarrow P < 0.5$$ (leans toward class 0)

### 🔄 Why Do We Need Alternative Functions?

Although the sigmoid is the most popular choice, in some special cases other link functions can be more suitable:

- **Data with different tail behavior**
- **Rare events or imbalanced data**
- **Special modeling requirements**
- **Different theoretical assumptions**

### 1. **Tanh Function**

$$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} = \frac{e^{2z} - 1}{e^{2z} + 1}$$

**Relationship with the Sigmoid:**
$$\tanh(z) = 2\sigma(2z) - 1$$

**Properties:**
- ✅ **Range**: $$(-1, 1)$$
- ✅ **Symmetric about the origin**: $$\tanh(-z) = -\tanh(z)$$
- ✅ **Derivative**: $$\tanh'(z) = 1 - \tanh^2(z)$$

**Conversion to a probability:** $$p = \frac{\tanh(z) + 1}{2}$$

**Applications:** Neural networks (hidden layers), when outputs centered around 0 are needed

### 2. **Probit Function (Inverse Normal CDF)**

$$\Phi^{-1}(p) = z \Leftrightarrow p = \Phi(z) = \int_{-\infty}^z \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt$$

**Properties:**
- ✅ **Range**: $$(0, 1)$$
- ✅ **Symmetric**: $$\Phi(-z) = 1 - \Phi(z)$$
- ❌ **No closed form**: requires numerical integration

**Comparison with the Sigmoid:**
- **Sigmoid**: exponentially decaying tails $$\sim e^{-|z|}$$
- **Probit**: Gaussian decaying tails $$\sim e^{-z^2/2}$$ (faster)

**Applications:** 
- Econometrics (probit regression)
- When the data has a nearly Gaussian distribution
- Threshold models

### 3. **Gumbel (Log-log) Function**

$$F(z) = e^{-e^{-z}}$$

**Properties:**
- ✅ **Range**: $$(0, 1)$$
- ❌ **Not symmetric**: Right-skewed
- **The CDF of the Gumbel distribution**

**Applications:**
- Extreme value theory
- Survival analysis
- Modeling maximum values

### 4. **Complementary Log-log**

$$F(z) = 1 - e^{-e^z}$$

**Properties:**
- ✅ **Range**: $$(0, 1)$$
- ❌ **Not symmetric**: Left-skewed
- **The complement of the Gumbel**

**Applications:**
- **Rare events modeling** (y=1 is rare)
- Survival analysis (hazard modeling)
- Time-to-event data
- Poisson regression with binary outcomes

### 5. **Cauchit Function**

$$F(z) = \frac{1}{2} + \frac{1}{\pi} \arctan(z)$$

**Properties:**
- ✅ **Range**: $$(0, 1)$$
- ✅ **Symmetric**: $$F(-z) = 1 - F(z)$$
- **Heavy tails**: slower decay than sigmoid/probit

**Applications:**
- Robust regression (outlier-resistant)
- Heavy-tailed error distributions
- Financial modeling

## 📊 Interactive Comparison Tool

<div id="link-functions-comparison" style="margin: 20px 0;">
    <div style="margin-bottom: 20px;">
        <h4>🎛️ Display Controls</h4>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <label><input type="checkbox" id="show-sigmoid" checked> Sigmoid</label>
            <label><input type="checkbox" id="show-tanh" checked> Tanh (scaled)</label>
            <label><input type="checkbox" id="show-probit" checked> Probit</label>
            <label><input type="checkbox" id="show-gumbel"> Gumbel</label>
            <label><input type="checkbox" id="show-cauchit"> Cauchit</label>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
            <h4>📈 Link Functions Comparison</h4>
            <canvas id="link-functions-canvas" width="500" height="400" style="border: 1px solid #ccc;"></canvas>
        </div>
        <div style="flex: 1;">
            <h4>📊 Properties Comparison</h4>
            <div id="properties-table" style="font-size: 14px;">
                <table style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr style="background-color: #f0f0f0;">
                            <th style="border: 1px solid #ccc; padding: 8px;">Function</th>
                            <th style="border: 1px solid #ccc; padding: 8px;">Symmetric</th>
                            <th style="border: 1px solid #ccc; padding: 8px;">Tail Behavior</th>
                            <th style="border: 1px solid #ccc; padding: 8px;">Computation</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Sigmoid</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">✅ Yes</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Exponential</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">⚡ Fast</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Tanh</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">✅ Yes</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Exponential</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">⚡ Fast</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Probit</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">✅ Yes</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Gaussian</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">🐌 Slow</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Gumbel</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">❌ No</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Right-skewed</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">⚡ Fast</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Cauchit</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">✅ Yes</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Heavy tails</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">⚡ Fast</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<script>
class LinkFunctionsComparison {
    constructor() {
        this.canvas = document.getElementById('link-functions-canvas');
        if (!this.canvas) return;
        this.ctx = this.canvas.getContext('2d');
        this.setupEventListeners();
        this.draw();
    }
    
    setupEventListeners() {
        const checkboxes = ['sigmoid', 'tanh', 'probit', 'gumbel', 'cauchit'];
        checkboxes.forEach(name => {
            const checkbox = document.getElementById(`show-${name}`);
            if (checkbox) {
                checkbox.addEventListener('change', () => {
                    this.draw();
                });
            }
        });
    }
    
    sigmoid(z) {
        return 1 / (1 + Math.exp(-z));
    }
    
    tanh_scaled(z) {
        return (Math.tanh(z) + 1) / 2; // Scale tanh from [-1,1] to [0,1]
    }
    
    // Approximation of probit function (inverse normal CDF)
    probit(z) {
        // Using rational approximation for normal CDF
        const a1 = 0.254829592;
        const a2 = -0.284496736;
        const a3 = 1.421413741;
        const a4 = -1.453152027;
        const a5 = 1.061405429;
        const p = 0.3275911;
        
        const sign = z < 0 ? -1 : 1;
        z = Math.abs(z) / Math.sqrt(2);
        
        const t = 1.0 / (1.0 + p * z);
        const y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-z * z);
        
        return 0.5 * (1.0 + sign * y);
    }
    
    gumbel(z) {
        return Math.exp(-Math.exp(-z));
    }
    
    cauchit(z) {
        return 0.5 + Math.atan(z) / Math.PI;
    }
    
    draw() {
        const ctx = this.ctx;
        const canvas = this.canvas;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(canvas.width - 20, canvas.height - 50);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(50, 20);
        ctx.lineTo(50, canvas.height - 50);
        ctx.stroke();
        
        // Grid lines
        ctx.strokeStyle = '#f0f0f0';
        ctx.lineWidth = 0.5;
        
        // Horizontal grid lines
        for (let i = 1; i <= 4; i++) {
            const y = 20 + (canvas.height - 70) * i / 5;
            ctx.beginPath();
            ctx.moveTo(50, y);
            ctx.lineTo(canvas.width - 20, y);
            ctx.stroke();
        }
        
        // Vertical grid lines
        for (let i = 1; i <= 9; i++) {
            const x = 50 + (canvas.width - 70) * i / 10;
            ctx.beginPath();
            ctx.moveTo(x, 20);
            ctx.lineTo(x, canvas.height - 50);
            ctx.stroke();
        }
        
        // Draw functions
        const functions = [
            { name: 'sigmoid', func: this.sigmoid, color: '#2196F3', label: 'Sigmoid' },
            { name: 'tanh', func: this.tanh_scaled, color: '#4CAF50', label: 'Tanh (scaled)' },
            { name: 'probit', func: this.probit, color: '#FF9800', label: 'Probit' },
            { name: 'gumbel', func: this.gumbel, color: '#9C27B0', label: 'Gumbel' },
            { name: 'cauchit', func: this.cauchit, color: '#F44336', label: 'Cauchit' }
        ];
        
        functions.forEach(({name, func, color, label}) => {
            const checkbox = document.getElementById(`show-${name}`);
            if (checkbox && checkbox.checked) {
                ctx.strokeStyle = color;
                ctx.lineWidth = 2;
                ctx.beginPath();
                
                for (let i = 0; i <= 400; i++) {
                    const z = (i / 400) * 10 - 5; // z from -5 to 5
                    let y;
                    
                    try {
                        y = func.call(this, z);
                        if (isNaN(y) || !isFinite(y)) continue;
                    } catch (e) {
                        continue;
                    }
                    
                    const canvasX = 50 + (z + 5) / 10 * (canvas.width - 70);
                    const canvasY = canvas.height - 50 - y * (canvas.height - 70);
                    
                    if (i === 0) {
                        ctx.moveTo(canvasX, canvasY);
                    } else {
                        ctx.lineTo(canvasX, canvasY);
                    }
                }
                ctx.stroke();
            }
        });
        
        // Draw legend
        let legendY = 30;
        functions.forEach(({name, color, label}) => {
            const checkbox = document.getElementById(`show-${name}`);
            if (checkbox && checkbox.checked) {
                ctx.strokeStyle = color;
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(canvas.width - 150, legendY);
                ctx.lineTo(canvas.width - 120, legendY);
                ctx.stroke();
                
                ctx.fillStyle = '#333';
                ctx.font = '12px Arial';
                ctx.fillText(label, canvas.width - 115, legendY + 4);
                
                legendY += 20;
            }
        });
        
        // Labels
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('z', canvas.width - 15, canvas.height - 30);
        ctx.fillText('P(y=1|z)', 10, 15);
        
        // Axis labels
        ctx.fillText('-5', 45, canvas.height - 30);
        ctx.fillText('0', 245, canvas.height - 30);
        ctx.fillText('5', 445, canvas.height - 30);
        ctx.fillText('0', 35, canvas.height - 45);
        ctx.fillText('0.5', 30, canvas.height/2 + 5);
        ctx.fillText('1', 35, 25);
    }
}

// Initialize comparison when page loads
document.addEventListener('DOMContentLoaded', () => {
    new LinkFunctionsComparison();
});
</script>

## 🎯 Guide to Choosing a Link Function

### **Sigmoid (Logistic)** - The Default Choice ⭐
**Use when:**
- A standard binary classification problem
- High computational speed is needed
- You want to interpret odds ratios
- The data is balanced, with no extreme outliers

### **Probit** - For Gaussian Data
**Use when:**
- The data has a nearly Gaussian distribution
- You need to model threshold effects
- You care about exact tail behavior
- You have computation time to spare (slower than the sigmoid)

### **Complementary Log-log** - For Rare Events
**Use when:**
- Modeling rare events (y=1 is rare)
- Survival analysis
- Time-to-event data
- Asymmetric data distribution

### **Cauchit** - For Heavy-tailed Data
**Use when:**
- The data has many outliers
- Heavy-tailed distributions
- Robust modeling is needed

## 💡 Conclusion on Link Functions

### **Why Is the Sigmoid Still the Best Choice?**

1. **🧮 Elegant Mathematics:**
   - Simple derivative: $$\sigma'(z) = \sigma(z)(1-\sigma(z))$$
   - Fast computation, numerically stable
   - No lookup tables or integrals needed

2. **📊 A Natural Probabilistic Meaning:**
   - Arises from the log-odds model
   - Intuitive interpretation (odds ratio)
   - Symmetric around 0.5

3. **⚡ Computational Efficiency:**
   - Only one division and one exponential
   - Efficient gradient descent
   - Suitable for big data

4. **🔄 Guaranteed Convexity:**
   - Cross-entropy with the sigmoid is always convex
   - Global optimum guaranteed
   - Algorithms converge stably

**Recommendation:** Start with the sigmoid, and switch to another link function only when there is a specific reason and after comparing performance experimentally.

## 🔢 Extension: Softmax Regression (Multi-class Classification)

*Logistic Regression can only handle 2 classes. So how do we classify more than two classes?*

### 🎯 From Binary to Multi-class

**The multi-class classification problem:**
- **Input**: $$\mathbf{x} \in \mathbb{R}^p$$
- **Output**: $$y \in \{1, 2, 3, ..., K\}$$ (K classes)
- **Goal**: Predict the probability of each class

**Real-world examples:**
- **Digit recognition**: 0, 1, 2, ..., 9 (10 classes)
- **Email classification**: spam, promotion, social, primary (4 classes)
- **Disease diagnosis**: healthy, cold, sore throat, COVID (4 classes)

### 🧮 The Softmax Function

**Extension of the Sigmoid:**
- **Sigmoid**: $$\sigma(z) = \frac{e^z}{1 + e^z}$$ (2 classes)
- **Softmax**: $$\text{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}$$ (K classes)

**Properties of Softmax:**
- ✅ **Sums to 1**: $$\sum_{i=1}^K \text{softmax}(\mathbf{z})_i = 1$$
- ✅ **Always positive**: $$\text{softmax}(\mathbf{z})_i > 0$$ $$\forall i$$
- ✅ **Monotonic**: The class with larger $$z_i$$ → higher probability
- ✅ **Smooth**: differentiable everywhere

### 🏗️ The Softmax Regression Model

**Model parameters:**
- $$\mathbf{W} \in \mathbb{R}^{p \times K}$$: the weight matrix
- $$\mathbf{b} \in \mathbb{R}^K$$: the bias vector

**Forward pass:**
$$\mathbf{z} = \mathbf{W}^T \mathbf{x} + \mathbf{b}$$

$$P(y = k | \mathbf{x}) = \frac{e^{z_k}}{\sum_{j=1}^K e^{z_j}}$$

**Prediction:**
$$\hat{y} = \arg\max_k P(y = k | \mathbf{x})$$

### 📊 Cross-Entropy Loss for Multi-class

**One-hot encoding:**
- $$y = 2$$ (class 2) → $$\mathbf{y} = [0, 1, 0, 0]$$ (if K=4)

**Multi-class Cross-Entropy:**
$$J(\mathbf{W}) = -\sum_{i=1}^n \sum_{k=1}^K y_{i,k} \log p_{i,k}$$

with:
- $$y_{i,k}$$: the one-hot encoding of sample $$i$$
- $$p_{i,k} = P(y = k | \mathbf{x}_i)$$: the predicted probability

**Properties:**
- **A natural extension** of binary cross-entropy
- **Still convex** → gradient descent works well
- **Heavily penalizes wrong predictions** as in the binary case

### 🔄 Comparison: Binary vs Multi-class

| Aspect | Binary Logistic | Softmax Regression |
|-----------|-----------------|-------------------|
| **Number of classes** | 2 | K ≥ 2 |
| **Activation** | Sigmoid | Softmax |
| **Parameters** | $$\mathbf{w} \in \mathbb{R}^p$$ | $$\mathbf{W} \in \mathbb{R}^{p \times K}$$ |
| **Output** | 1 probability | K probabilities |
| **Loss** | Binary cross-entropy | Multi-class cross-entropy |
| **Gradient** | $$\mathbf{X}^T(\boldsymbol{\sigma} - \mathbf{y})$$ | $$\mathbf{X}^T(\mathbf{P} - \mathbf{Y})$$ |

### 🎛️ Interactive Softmax Demo

<div id="softmax-demo" style="margin: 20px 0;">
    <div style="display: flex; gap: 20px; margin-bottom: 20px;">
        <div style="flex: 1;">
            <h4>🎚️ Logit Controls</h4>
            <div style="margin: 10px 0;">
                <label for="z1-slider">z₁ (Class 1): <span id="z1-value">1.0</span></label>
                <input type="range" id="z1-slider" min="-3" max="3" step="0.1" value="1.0" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <label for="z2-slider">z₂ (Class 2): <span id="z2-value">0.5</span></label>
                <input type="range" id="z2-slider" min="-3" max="3" step="0.1" value="0.5" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <label for="z3-slider">z₃ (Class 3): <span id="z3-value">-0.5</span></label>
                <input type="range" id="z3-slider" min="-3" max="3" step="0.1" value="-0.5" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <label for="z4-slider">z₄ (Class 4): <span id="z4-value">-1.0</span></label>
                <input type="range" id="z4-slider" min="-3" max="3" step="0.1" value="-1.0" style="width: 100%;">
            </div>
        </div>
        <div style="flex: 1;">
            <h4>📊 Softmax Probabilities</h4>
            <div id="probabilities-display" style="font-family: monospace; font-size: 14px;">
                <div>Class 1: <span id="p1">0.000</span></div>
                <div>Class 2: <span id="p2">0.000</span></div>
                <div>Class 3: <span id="p3">0.000</span></div>
                <div>Class 4: <span id="p4">0.000</span></div>
                <hr>
                <div><strong>Sum: <span id="sum">1.000</span></strong></div>
                <div><strong>Predicted: Class <span id="predicted">1</span></strong></div>
            </div>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
            <h4>📈 Probability Bars</h4>
            <canvas id="prob-bars-canvas" width="400" height="300" style="border: 1px solid #ccc;"></canvas>
        </div>
        <div style="flex: 1;">
            <h4>🥧 Probability Pie Chart</h4>
            <canvas id="prob-pie-canvas" width="400" height="300" style="border: 1px solid #ccc;"></canvas>
        </div>
    </div>
</div>

<script>
class SoftmaxDemo {
    constructor() {
        this.z = [1.0, 0.5, -0.5, -1.0];
        this.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'];
        this.setupEventListeners();
        this.updateDisplay();
    }
    
    setupEventListeners() {
        for (let i = 1; i <= 4; i++) {
            const slider = document.getElementById(`z${i}-slider`);
            if (slider) {
                slider.addEventListener('input', (e) => {
                    this.z[i-1] = parseFloat(e.target.value);
                    document.getElementById(`z${i}-value`).textContent = this.z[i-1].toFixed(1);
                    this.updateDisplay();
                });
            }
        }
    }
    
    softmax(z) {
        const maxZ = Math.max(...z);
        const expZ = z.map(zi => Math.exp(zi - maxZ)); // Numerical stability
        const sumExpZ = expZ.reduce((sum, exp) => sum + exp, 0);
        return expZ.map(exp => exp / sumExpZ);
    }
    
    updateDisplay() {
        const probs = this.softmax(this.z);
        const sum = probs.reduce((s, p) => s + p, 0);
        const predicted = probs.indexOf(Math.max(...probs)) + 1;
        
        // Update probability display
        for (let i = 1; i <= 4; i++) {
            const elem = document.getElementById(`p${i}`);
            if (elem) {
                elem.textContent = probs[i-1].toFixed(3);
                elem.style.color = this.colors[i-1];
                elem.style.fontWeight = predicted === i ? 'bold' : 'normal';
            }
        }
        
        const sumElem = document.getElementById('sum');
        if (sumElem) sumElem.textContent = sum.toFixed(3);
        
        const predElem = document.getElementById('predicted');
        if (predElem) {
            predElem.textContent = predicted;
            predElem.style.color = this.colors[predicted-1];
        }
        
        this.drawBars(probs);
        this.drawPie(probs);
    }
    
    drawBars(probs) {
        const canvas = document.getElementById('prob-bars-canvas');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const barWidth = 60;
        const maxHeight = 200;
        const startX = 50;
        const startY = canvas.height - 50;
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(30, 30);
        ctx.lineTo(30, startY);
        ctx.lineTo(canvas.width - 20, startY);
        ctx.stroke();
        
        // Draw bars
        for (let i = 0; i < 4; i++) {
            const x = startX + i * (barWidth + 20);
            const height = probs[i] * maxHeight;
            
            ctx.fillStyle = this.colors[i];
            ctx.fillRect(x, startY - height, barWidth, height);
            
            // Labels
            ctx.fillStyle = '#333';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`Class ${i+1}`, x + barWidth/2, startY + 20);
            ctx.fillText(probs[i].toFixed(3), x + barWidth/2, startY - height - 5);
        }
        
        // Y-axis labels
        ctx.textAlign = 'right';
        ctx.fillText('0.0', 25, startY + 5);
        ctx.fillText('0.5', 25, startY - maxHeight/2 + 5);
        ctx.fillText('1.0', 25, startY - maxHeight + 5);
    }
    
    drawPie(probs) {
        const canvas = document.getElementById('prob-pie-canvas');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = 100;
        
        let currentAngle = -Math.PI / 2; // Start from top
        
        for (let i = 0; i < 4; i++) {
            const sliceAngle = probs[i] * 2 * Math.PI;
            
            // Draw slice
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle);
            ctx.closePath();
            ctx.fillStyle = this.colors[i];
            ctx.fill();
            ctx.strokeStyle = '#fff';
            ctx.lineWidth = 2;
            ctx.stroke();
            
            // Draw label
            if (probs[i] > 0.05) { // Only show label if slice is big enough
                const labelAngle = currentAngle + sliceAngle / 2;
                const labelX = centerX + Math.cos(labelAngle) * radius * 0.7;
                const labelY = centerY + Math.sin(labelAngle) * radius * 0.7;
                
                ctx.fillStyle = '#fff';
                ctx.font = 'bold 12px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(`${i+1}`, labelX, labelY + 4);
            }
            
            currentAngle += sliceAngle;
        }
        
        // Legend
        for (let i = 0; i < 4; i++) {
            const legendY = 20 + i * 20;
            ctx.fillStyle = this.colors[i];
            ctx.fillRect(20, legendY, 15, 15);
            ctx.fillStyle = '#333';
            ctx.font = '12px Arial';
            ctx.textAlign = 'left';
            ctx.fillText(`Class ${i+1}: ${(probs[i] * 100).toFixed(1)}%`, 40, legendY + 12);
        }
    }
}

// Initialize demo when page loads
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('softmax-demo')) {
        new SoftmaxDemo();
    }
});
</script>

<style>
#softmax-demo {
    font-family: Arial, sans-serif;
    max-width: 1000px;
    margin: 0 auto;
}

#softmax-demo canvas {
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

#softmax-demo input[type="range"] {
    width: 100%;
    margin: 5px 0;
}

#probabilities-display {
    background-color: #f5f5f5;
    padding: 15px;
    border-radius: 4px;
    line-height: 1.6;
}

#probabilities-display div {
    margin: 5px 0;
}
</style>

### 🎯 Real-World Applications of Softmax

#### **1. Computer Vision**
- **Image Classification**: ImageNet (1000 classes)
- **Object Detection**: COCO dataset (80 classes)
- **Medical Imaging**: X-ray and MRI classification

#### **2. Natural Language Processing**
- **Sentiment Analysis**: positive, negative, neutral
- **Language Detection**: English, Vietnamese, Chinese, ...
- **Text Classification**: news categories, spam detection

#### **3. Recommendation Systems**
- **Content Categories**: movies, music, books
- **User Preferences**: age groups, interests
- **Product Classification**: electronics, fashion, food

### 🔄 Connection with Deep Learning

**Softmax is an important building block:**
- The **output layer** of neural networks
- **Attention mechanisms** in Transformers
- **Policy networks** in Reinforcement Learning

**From Logistic → Softmax → Neural Networks:**
1. **Logistic Regression**: Linear + Sigmoid
2. **Softmax Regression**: Linear + Softmax  
3. **Neural Networks**: Multiple layers + Softmax

### 💡 Summary of Softmax Regression

**Advantages:**
- ✅ **A natural extension** of binary classification
- ✅ **Meaningful probabilistic output**
- ✅ **Convex optimization** → reliable
- ✅ **Efficient training** with gradient descent

**Disadvantages:**
- ❌ **Linear decision boundaries** (like logistic)
- ❌ **Assumes linear separability**
- ❌ **May struggle** with complex patterns

**When to use:**
- Multi-class classification problems
- When probabilistic outputs are needed
- A baseline model before trying complex methods
- When interpretability matters

**Softmax Regression is the perfect stepping stone** between simple logistic regression and complex neural networks!

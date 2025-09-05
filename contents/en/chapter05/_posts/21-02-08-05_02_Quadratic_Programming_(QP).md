---
layout: post
title: 05-02 Quadratic Programming (QP)
chapter: '05'
order: 3
owner: Hooncheol Shin
categories:
- chapter05
lang: en
lesson_type: required
---

A *Quadratic Program* (QP) is a convex optimization problem where the objective function is a convex quadratic and all constraint functions are affine. The general quadratic program is formulated as:

### Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&\frac{1}{2}x^T P x + q^T x + r \\
>    &\text{subject to } &&Gx \preceq h \\
>    & &&Ax = b,\\
>    & \text{where } &&P \in \mathbb{S}_{+}^n, G \in \mathbb{R}^{m \times n}, \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align}
>$$

* The constant $$+ r$$ in the objective function does not affect the optimization process or result and can be omitted.
* If $$P \in \mathbb{S}_{+}^n$$ is not satisfied, the problem is not convex.
* Even if not explicitly stated, QP assumes $$P \in \mathbb{S}_{+}^n$$.
* The above problem seeks the minimizer $$x^*$$ of the convex quadratic function $$\frac{1}{2}x^T P x + q^T x + r$$ over a polyhedral feasible set.

### Understanding $$\mathbb{S}_{+}^n$$ (Positive Semidefinite Cone)

The notation $$\mathbb{S}_{+}^n$$ represents the **positive semidefinite cone**, which is a fundamental concept in convex optimization:

**Definition:**
>$$\mathbb{S}_{+}^n = \{ X \in \mathbb{S}^n : X \succeq 0 \}$$

where:
* $$\mathbb{S}^n$$ is the set of all $$n \times n$$ **symmetric matrices**
* $$X \succeq 0$$ means matrix $$X$$ is **positive semidefinite**

**Key Properties:**
1. **Positive semidefinite condition**: A matrix $$P$$ is positive semidefinite if:
   - All eigenvalues of $$P$$ are non-negative ($$\lambda_i \geq 0$$)
   - For any vector $$v$$, we have $$v^T P v \geq 0$$

2. **Convex cone property**: $$\mathbb{S}_{+}^n$$ is a convex cone because if $$\theta_1, \theta_2 \geq 0$$ and $$A, B \in \mathbb{S}_{+}^n$$, then $$\theta_1 A + \theta_2 B \in \mathbb{S}_{+}^n$$

**Example for $$n=2$$:**
For a $$2 \times 2$$ matrix $$P = \begin{bmatrix} a & b \\ b & c \end{bmatrix}$$, the condition $$P \in \mathbb{S}_{+}^2$$ requires:
* $$a \geq 0$$ (diagonal elements non-negative)
* $$c \geq 0$$ (diagonal elements non-negative)
* $$ac \geq b^2$$ (determinant non-negative)

**Why is this important for QP?**
* The condition $$P \in \mathbb{S}_{+}^n$$ ensures that the quadratic function $$(1/2)x^T P x + q^T x + r$$ is **convex**
* Without this condition, the problem may have multiple local minima and would not be a convex optimization problem
* This guarantees that any local minimum is also a global minimum

### Understanding $$Gx \preceq h$$ (Component-wise Inequality)

The notation $$Gx \preceq h$$ represents **component-wise inequality constraints**, which is a compact way to write multiple linear inequality constraints:

**Definition:**
>$$Gx \preceq h \quad \Leftrightarrow \quad (Gx)_i \leq h_i \text{ for all } i = 1, 2, \ldots, m$$

where:
* $$G \in \mathbb{R}^{m \times n}$$ is the constraint matrix
* $$x \in \mathbb{R}^n$$ is the decision variable vector
* $$h \in \mathbb{R}^m$$ is the right-hand side vector
* $$m$$ is the number of inequality constraints

**Expanded Form:**
The single matrix inequality $$Gx \preceq h$$ is equivalent to the system:
>$$
>\begin{align}
>g_1^T x &\leq h_1 \\
>g_2^T x &\leq h_2 \\
>&\vdots \\
>g_m^T x &\leq h_m
>\end{align}
>$$

where $$g_i^T$$ is the $$i$$-th row of matrix $$G$$.

**Example:**
Consider $$G = \begin{bmatrix} 1 & 2 \\ -1 & 3 \\ 0 & -1 \end{bmatrix}$$, $$x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$, and $$h = \begin{bmatrix} 5 \\ 2 \\ -1 \end{bmatrix}$$

Then $$Gx \preceq h$$ means:
>$$
>\begin{align}
>x_1 + 2x_2 &\leq 5 \\
>-x_1 + 3x_2 &\leq 2 \\
>-x_2 &\leq -1 \quad (\text{i.e., } x_2 \geq 1)
>\end{align}
>$$

**Geometric Interpretation:**
* Each inequality $$g_i^T x \leq h_i$$ defines a **half-space** in $$\mathbb{R}^n$$
* The feasible region is the **intersection** of all these half-spaces
* This intersection forms a **polyhedron** (or polytope if bounded)
* The constraint $$Gx \preceq h$$ defines the **polyhedral feasible set** for the QP

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_02_geometric_interpretation_of_QP.png" alt="[Fig 1] Geometric interpretation of QP [1]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Geometric interpretation of QP [1]</figcaption>
</p>
</figure>

## QP in Standard form
The standard form of a quadratic program is:

### Standard form QP
>$$
>\begin{align}
>    &\text{minimize}_{x} &&\frac{1}{2}x^T P x + q^T x + r \\
>    &\text{subject to } &&A x = b \\
>    & &&x \succeq 0.
>\end{align}
>$$

Any general quadratic program can be converted to standard form using the following steps:

### Converting QPs to standard form
**Step 1.** Use slack variables $$s$$ to convert inequality constraints into equality constraints:
> $$
> \begin{align}
>     &\text{minimize}_{x, s} &&\frac{1}{2}x^T P x + q^T x + r \\
>     &\text{subject to } &&Gx + s = h \\
>     & &&Ax = b,\\
>     & &&s \succeq 0.
> \end{align}
> $$

**Step 2.** Replace $$x$$ with two nonnegative variables:
$$x = x^{+} - x^{-}$$, where $$x^{+}, x^{-} \succeq 0.$$

> $$
> \begin{align}
>     &\text{minimize}_{x^{+}, x^{-}, s} &&\frac{1}{2}(x^{+} - x^{-})^T P (x^{+} - x^{-}) + q^T x^{+} - q^T x^{-} + r\\
>     &\text{subject to } &&Gx^{+} - Gx^{-} + s = h \\
>     & &&Ax^{+} - Ax^{-} = b,\\
>     & &&s \succeq 0\\
>     & &&x^{+} \succeq 0, \quad x^{-} \succeq 0.
> \end{align}
> $$

**Step 3.** Define $$\tilde{x}$$, $$\tilde{q}$$, $$\tilde{b}$$, $$\tilde{A}$$, $$\tilde{P}$$:

> $$
> \tilde{x} =
> \begin{bmatrix}
> x^{+} \\\\
> x^{-} \\\\
> s
> \end{bmatrix},
> \tilde{q} =
> \begin{bmatrix}
> q \\\\
> -q \\\\
> 0
> \end{bmatrix},
> \tilde{b} =
> \begin{bmatrix}
> h \\\\
> b
> \end{bmatrix},
> \tilde{A} =
> \begin{bmatrix}
> G & -G & I \\\\
> A & -A & O
> \end{bmatrix},
> \tilde{P} =
> \begin{bmatrix}
>  P & -P & O \\\\
> -P &  P & O \\\\
>  O &  O & O \\\\
> \end{bmatrix}
> $$

**Step 4.** Substitute the expressions from Step 2 into the formulations with 
$$\tilde{x}, \tilde{q}, \tilde{b}, \tilde{A}, \tilde{P}$$:

>$$
>\begin{align}
>    &\text{minimize}_{\tilde{x}} &&\frac{1}{2}\tilde{x}^T \tilde{P} \tilde{x} + \tilde{q}^T \tilde{x} + r \\
>    &\text{subject to } &&\tilde{A} \tilde{x} = \tilde{b} \\
>    & &&\tilde{x} \succeq 0.
>\end{align}
>$$

## LP and equivalent QP
If the quadratic term is removed from the objective function of a quadratic program, it takes the form of a linear program. Thus, LP is a special case of QP, denoted as LP $$ \subseteq $$ QP.

### Recall: General LP
>$$
>\begin{align}
>    &\text{minimize}_{x} &&c^T x + d \\
>    &\text{subject to } &&Gx \preceq h \\
>    & &&Ax = b,\\
>    & \text{where } &&G \in \mathbb{R}^{m \times n} \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align}
>$$

### Example 1) Portfolio optimization
This problem involves appropriately trading off performance and risk in creating a financial portfolio. 

>$$
>\begin{align}
>    &\text{maximize}_{x} &&\mu^T x - \frac{\gamma}{2}x^T P x \\
>    &\text{subject to } &&\mathbf{1}^Tx = 1 \\
>    & &&x \succeq 0.
>\end{align}
>$$

* $$\mu$$: expected assets' returns.
* $$P$$: covariance matrix of assets' returns.
* $$\gamma$$: risk aversion (hyper-parameter).
* $$x$$: portfolio holdings (percentages).



### Example 2)  Support vector machines

Support Vector Machines (hereafter SVM) are an example of a quadratic program. Below is C-SVM, a variant of SVM. A detailed explanation of SVM is beyond the scope of this chapter and will therefore be omitted

>$$
>\begin{align}
>    &\text{minimize}_{\beta, \beta_0, \xi} &&\frac{1}{2} \| \beta \|_2^2 + C \sum_{i=1}^{n} \xi_i \\
>    &\text{subject to } &&\xi_i \geq 0, \quad i = 1, \ldots, n \\
>    & &&y_i (x_i^T \beta + \beta_0) \geq 1 - \xi_i, \quad i = 1, \ldots, n,\\
>    & \text{given} && y \in \{-1, 1\}^n, \quad X \in \mathbb{R}^{n \times p} \text{ having rows } x_1, \ldots, x_n.
>\end{align}
>$$

### Example 3)  Least-squares in regression
The problem of minimizing the following convex quadratic function corresponds to an (unconstrained) QP:
> $$\| Ax - b \|_2^2 = x^T A^TA x - 2b^TAx + b^Tb$$


## Least-Squares Problems

A least-squares problem is an optimization problem without constraints where we minimize the sum of squared errors:

>$$\text{minimize}_{x} \quad f_0(x) = \|Ax - b\|_2^2 = \sum_{i=1}^{k} (a_i^T x - b_i)^2$$

where:
* $$A \in \mathbb{R}^{k \times n}$$ is a matrix with $$k \geq n$$
* $$a_i^T$$ are the rows of $$A$$
* $$x \in \mathbb{R}^n$$ is the variable we want to find
* $$b \in \mathbb{R}^k$$ is the target vector

**Goal:** Find $$x$$ to minimize the sum of squared residuals.

### Example: Linear Regression

Finding the best-fit line $$y = mx + c$$ through data points. We minimize the sum of squared vertical distances from points to the line.

**Goal:** Find $$m, c$$.

<div id="linear-regression-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f9f9f9;">
    <h4 style="text-align: center; color: #333;">Interactive Linear Regression Demonstration</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <!-- Canvas for visualization -->
        <div style="flex: 1; min-width: 400px;">
            <canvas id="regressionCanvas" width="400" height="300" style="border: 1px solid #ccc; background: white; cursor: crosshair;"></canvas>
            <p style="font-size: 12px; color: #666; margin-top: 5px;">
                <strong>Instructions:</strong> Click on the canvas to add data points. The red line shows the best-fit line.
            </p>
        </div>
        
        <!-- Controls and information -->
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Regression Parameters</h5>
                <div id="regression-params" style="font-family: monospace; font-size: 14px; line-height: 1.6;">
                    <div><strong>Slope (m):</strong> <span id="slope-value">0.000</span></div>
                    <div><strong>Intercept (c):</strong> <span id="intercept-value">0.000</span></div>
                    <div><strong>R² Score:</strong> <span id="r2-value">N/A</span></div>
                    <div><strong>MSE:</strong> <span id="mse-value">N/A</span></div>
                </div>
                
                <div style="margin-top: 15px;">
                    <h5 style="color: #444;">Equation</h5>
                    <div id="equation" style="font-family: monospace; font-size: 16px; background: #f0f0f0; padding: 8px; border-radius: 4px;">
                        y = 0.000x + 0.000
                    </div>
                </div>
                
                <div style="margin-top: 15px;">
                    <button onclick="clearPoints()" style="background: #ff6b6b; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin-right: 10px;">Clear Points</button>
                    <button onclick="addRandomPoints()" style="background: #4ecdc4; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Add Random Points</button>
                </div>
            </div>
            
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-top: 15px;">
                <h5 style="margin-top: 0; color: #444;">Mathematical Formulation</h5>
                <div style="font-size: 13px; line-height: 1.5;">
                    <p><strong>Objective:</strong> Minimize sum of squared residuals</p>
                    <div style="background: #f8f8f8; padding: 8px; border-radius: 4px; font-family: monospace;">
                        S(m,c) = Σ(yᵢ - mxᵢ - c)²
                    </div>
                    <p style="margin-top: 10px;"><strong>Solution:</strong></p>
                    <div style="background: #f8f8f8; padding: 8px; border-radius: 4px; font-family: monospace; font-size: 11px;">
                        m = Σ(xᵢ-x̄)(yᵢ-ȳ) / Σ(xᵢ-x̄)²<br>
                        c = ȳ - mx̄
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// Linear Regression Interactive Demo
class LinearRegressionDemo {
    constructor() {
        this.canvas = document.getElementById('regressionCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.points = [];
        this.slope = 0;
        this.intercept = 0;
        
        // Set up canvas
        this.canvas.addEventListener('click', (e) => this.addPoint(e));
        
        // Initialize with some sample points
        this.addRandomPoints();
        this.draw();
    }
    
    addPoint(event) {
        const rect = this.canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        
        // Convert canvas coordinates to data coordinates
        const dataX = (x / this.canvas.width) * 10;
        const dataY = ((this.canvas.height - y) / this.canvas.height) * 10;
        
        this.points.push({x: dataX, y: dataY});
        this.calculateRegression();
        this.draw();
        this.updateDisplay();
    }
    
    addRandomPoints() {
        // Add some sample points with a trend
        const baseSlope = 0.8;
        const baseIntercept = 2;
        
        for (let i = 0; i < 8; i++) {
            const x = Math.random() * 8 + 1;
            const y = baseSlope * x + baseIntercept + (Math.random() - 0.5) * 2;
            this.points.push({x: x, y: Math.max(0, Math.min(10, y))});
        }
        
        this.calculateRegression();
        this.draw();
        this.updateDisplay();
    }
    
    clearPoints() {
        this.points = [];
        this.slope = 0;
        this.intercept = 0;
        this.draw();
        this.updateDisplay();
    }
    
    calculateRegression() {
        if (this.points.length < 2) {
            this.slope = 0;
            this.intercept = 0;
            return;
        }
        
        const n = this.points.length;
        const sumX = this.points.reduce((sum, p) => sum + p.x, 0);
        const sumY = this.points.reduce((sum, p) => sum + p.y, 0);
        const sumXY = this.points.reduce((sum, p) => sum + p.x * p.y, 0);
        const sumXX = this.points.reduce((sum, p) => sum + p.x * p.x, 0);
        
        const meanX = sumX / n;
        const meanY = sumY / n;
        
        const numerator = sumXY - n * meanX * meanY;
        const denominator = sumXX - n * meanX * meanX;
        
        if (Math.abs(denominator) < 1e-10) {
            this.slope = 0;
            this.intercept = meanY;
        } else {
            this.slope = numerator / denominator;
            this.intercept = meanY - this.slope * meanX;
        }
    }
    
    calculateR2() {
        if (this.points.length < 2) return 0;
        
        const meanY = this.points.reduce((sum, p) => sum + p.y, 0) / this.points.length;
        let ssRes = 0;
        let ssTot = 0;
        
        for (const point of this.points) {
            const predicted = this.slope * point.x + this.intercept;
            ssRes += Math.pow(point.y - predicted, 2);
            ssTot += Math.pow(point.y - meanY, 2);
        }
        
        return ssTot === 0 ? 1 : 1 - (ssRes / ssTot);
    }
    
    calculateMSE() {
        if (this.points.length === 0) return 0;
        
        let mse = 0;
        for (const point of this.points) {
            const predicted = this.slope * point.x + this.intercept;
            mse += Math.pow(point.y - predicted, 2);
        }
        
        return mse / this.points.length;
    }
    
    draw() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw grid
        this.drawGrid();
        
        // Draw regression line
        if (this.points.length >= 2) {
            this.drawRegressionLine();
        }
        
        // Draw points and residuals
        this.drawPoints();
        
        // Draw axes labels
        this.drawLabels();
    }
    
    drawGrid() {
        this.ctx.strokeStyle = '#f0f0f0';
        this.ctx.lineWidth = 1;
        
        // Vertical lines
        for (let i = 0; i <= 10; i++) {
            const x = (i / 10) * this.canvas.width;
            this.ctx.beginPath();
            this.ctx.moveTo(x, 0);
            this.ctx.lineTo(x, this.canvas.height);
            this.ctx.stroke();
        }
        
        // Horizontal lines
        for (let i = 0; i <= 10; i++) {
            const y = (i / 10) * this.canvas.height;
            this.ctx.beginPath();
            this.ctx.moveTo(0, y);
            this.ctx.lineTo(this.canvas.width, y);
            this.ctx.stroke();
        }
    }
    
    drawRegressionLine() {
        this.ctx.strokeStyle = '#ff4757';
        this.ctx.lineWidth = 2;
        
        const x1 = 0;
        const y1 = this.intercept;
        const x2 = 10;
        const y2 = this.slope * x2 + this.intercept;
        
        const canvasX1 = (x1 / 10) * this.canvas.width;
        const canvasY1 = this.canvas.height - (y1 / 10) * this.canvas.height;
        const canvasX2 = (x2 / 10) * this.canvas.width;
        const canvasY2 = this.canvas.height - (y2 / 10) * this.canvas.height;
        
        this.ctx.beginPath();
        this.ctx.moveTo(canvasX1, canvasY1);
        this.ctx.lineTo(canvasX2, canvasY2);
        this.ctx.stroke();
    }
    
    drawPoints() {
        for (const point of this.points) {
            const canvasX = (point.x / 10) * this.canvas.width;
            const canvasY = this.canvas.height - (point.y / 10) * this.canvas.height;
            
            // Draw residual line (vertical distance to regression line)
            if (this.points.length >= 2) {
                const predictedY = this.slope * point.x + this.intercept;
                const predictedCanvasY = this.canvas.height - (predictedY / 10) * this.canvas.height;
                
                this.ctx.strokeStyle = '#ff6b6b';
                this.ctx.lineWidth = 1;
                this.ctx.setLineDash([2, 2]);
                this.ctx.beginPath();
                this.ctx.moveTo(canvasX, canvasY);
                this.ctx.lineTo(canvasX, predictedCanvasY);
                this.ctx.stroke();
                this.ctx.setLineDash([]);
            }
            
            // Draw point
            this.ctx.fillStyle = '#2f3542';
            this.ctx.beginPath();
            this.ctx.arc(canvasX, canvasY, 4, 0, 2 * Math.PI);
            this.ctx.fill();
        }
    }
    
    drawLabels() {
        this.ctx.fillStyle = '#666';
        this.ctx.font = '12px Arial';
        
        // X-axis labels
        for (let i = 0; i <= 10; i += 2) {
            const x = (i / 10) * this.canvas.width;
            this.ctx.fillText(i.toString(), x - 5, this.canvas.height - 5);
        }
        
        // Y-axis labels
        for (let i = 0; i <= 10; i += 2) {
            const y = this.canvas.height - (i / 10) * this.canvas.height;
            this.ctx.fillText(i.toString(), 5, y + 3);
        }
    }
    
    updateDisplay() {
        document.getElementById('slope-value').textContent = this.slope.toFixed(3);
        document.getElementById('intercept-value').textContent = this.intercept.toFixed(3);
        document.getElementById('equation').textContent = `y = ${this.slope.toFixed(3)}x + ${this.intercept.toFixed(3)}`;
        
        if (this.points.length >= 2) {
            document.getElementById('r2-value').textContent = this.calculateR2().toFixed(3);
            document.getElementById('mse-value').textContent = this.calculateMSE().toFixed(3);
        } else {
            document.getElementById('r2-value').textContent = 'N/A';
            document.getElementById('mse-value').textContent = 'N/A';
        }
    }
}

// Global functions for buttons
function clearPoints() {
    if (window.regressionDemo) {
        window.regressionDemo.clearPoints();
    }
}

function addRandomPoints() {
    if (window.regressionDemo) {
        window.regressionDemo.clearPoints();
        window.regressionDemo.addRandomPoints();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('regressionCanvas')) {
        window.regressionDemo = new LinearRegressionDemo();
    }
});

// Initialize immediately if DOM is already loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        if (document.getElementById('regressionCanvas')) {
            window.regressionDemo = new LinearRegressionDemo();
        }
    });
} else {
    if (document.getElementById('regressionCanvas')) {
        window.regressionDemo = new LinearRegressionDemo();
    }
}
</script>

**Problem:** Given $$n$$ data points $$(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$$, find the line $$y = mx + c$$ that minimizes the sum of squared vertical distances from the points to the line.

**Objective Function:** We want to minimize
>$$S(m,c) = \sum_{i=1}^{n} (y_i - mx_i - c)^2$$

**Solution:** To find the minimum, we take partial derivatives and set them equal to zero.

Taking the partial derivative with respect to $$c$$:
>$$\frac{\partial S}{\partial c} = \sum_{i=1}^{n} 2(y_i - mx_i - c)(-1) = -2\sum_{i=1}^{n} (y_i - mx_i - c) = 0$$

This gives us:
>$$\sum_{i=1}^{n} y_i = m\sum_{i=1}^{n} x_i + nc$$

Therefore:
>$$c = \frac{1}{n}\sum_{i=1}^{n} y_i - m\frac{1}{n}\sum_{i=1}^{n} x_i = \bar{y} - m\bar{x}$$

where $$\bar{x}$$ and $$\bar{y}$$ are the means of $$x$$ and $$y$$ values.

Taking the partial derivative with respect to $$m$$:
>$$\frac{\partial S}{\partial m} = \sum_{i=1}^{n} 2(y_i - mx_i - c)(-x_i) = -2\sum_{i=1}^{n} x_i(y_i - mx_i - c) = 0$$

Substituting $$c = \bar{y} - m\bar{x}$$:
>$$\sum_{i=1}^{n} x_i(y_i - mx_i - \bar{y} + m\bar{x}) = 0$$

Rearranging:
>$$\sum_{i=1}^{n} x_iy_i - m\sum_{i=1}^{n} x_i^2 - \bar{y}\sum_{i=1}^{n} x_i + m\bar{x}\sum_{i=1}^{n} x_i = 0$$

Since $$\sum_{i=1}^{n} x_i = n\bar{x}$$ and $$\sum_{i=1}^{n} x_iy_i - \bar{y}\sum_{i=1}^{n} x_i = \sum_{i=1}^{n} x_i(y_i - \bar{y})$$:

>$$\sum_{i=1}^{n} x_i(y_i - \bar{y}) = m\left(\sum_{i=1}^{n} x_i^2 - n\bar{x}^2\right)$$

Note that $$\sum_{i=1}^{n} x_i^2 - n\bar{x}^2 = \sum_{i=1}^{n} (x_i - \bar{x})^2$$

Therefore:
>$$m = \frac{\sum_{i=1}^{n} x_i(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$$

**Final Result:** The best-fit line has parameters:
>$$\boxed{m = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2} \quad \text{and} \quad c = \bar{y} - m\bar{x}}$$

This is the classical least-squares solution for linear regression, also known as the **Normal Equations**.



### Proof for the Optimal Solution of Linear Regression

**Problem Statement:**

In Linear Regression, we aim to find a vector of coefficients $\mathbf{w}$ that best fits a linear model to a given dataset. We have $n$ data points, each with $p$ features.
Let $X$ be the design matrix of size $n \times p$, where each row represents a data point and each column represents a feature.

Let $\mathbf{y}$ be the vector of target values of size $n \times 1$.

Our linear model predicts the target values $\hat{\mathbf{y}}$ as:
$$ \hat{\mathbf{y}} = X\mathbf{w} $$
where $\mathbf{w}$ is the vector of unknown coefficients of size $p \times 1$.

**Objective Function (Cost Function):**

The goal is to minimize the sum of squared errors (residuals) between the actual target values $\mathbf{y}$ and the predicted values $\hat{\mathbf{y}}$. This is known as the Ordinary Least Squares (OLS) objective function:
$$ J(\mathbf{w}) = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \| \mathbf{y} - X\mathbf{w} \|^2 $$

We can express this in matrix form by expanding the squared Euclidean norm:
$$ J(\mathbf{w}) = (\mathbf{y} - X\mathbf{w})^{\text{T}}(\mathbf{y} - X\mathbf{w}) $$

Expanding this expression:
$$ J(\mathbf{w}) = \mathbf{y}^{\text{T}}\mathbf{y} - \mathbf{y}^{\text{T}}X\mathbf{w} - (X\mathbf{w})^{\text{T}}\mathbf{y} + (X\mathbf{w})^{\text{T}}X\mathbf{w} $$
Using the property that $(AB)^{\text{T}} = B^{\text{T}}A^{\text{T}}$, we have $(X\mathbf{w})^{\text{T}} = \mathbf{w}^{\text{T}}X^{\text{T}}$.
Also, since $\mathbf{y}^{\text{T}}X\mathbf{w}$ is a scalar, its transpose is itself: $(\mathbf{y}^{\text{T}}X\mathbf{w})^{\text{T}} = \mathbf{w}^{\text{T}}X^{\text{T}}\mathbf{y}$.
Thus, the two middle terms are identical:
$$ J(\mathbf{w}) = \mathbf{y}^{\text{T}}\mathbf{y} - 2\mathbf{w}^{\text{T}}X^{\text{T}}\mathbf{y} + \mathbf{w}^{\text{T}}X^{\text{T}}X\mathbf{w} $$

**Minimization using Calculus:**
To find the optimal $\mathbf{w}$ that minimizes $J(\mathbf{w})$, we take the derivative of $J(\mathbf{w})$ with respect to $\mathbf{w}$ and set it to zero. We use the following matrix calculus rules:
1.  $\frac{\partial (\mathbf{a}^{\text{T}}\mathbf{x})}{\partial \mathbf{x}} = \mathbf{a}$
2.  $\frac{\partial (\mathbf{x}^{\text{T}}A\mathbf{x})}{\partial \mathbf{x}} = (A + A^{\text{T}})\mathbf{x}$ (If $A$ is symmetric, this simplifies to $2A\mathbf{x}$)

Applying these rules to $J(\mathbf{w})$:
$$ \frac{\partial J(\mathbf{w})}{\partial \mathbf{w}} = \frac{\partial (\mathbf{y}^{\text{T}}\mathbf{y})}{\partial \mathbf{w}} - \frac{\partial (2\mathbf{w}^{\text{T}}X^{\text{T}}\mathbf{y})}{\partial \mathbf{w}} + \frac{\partial (\mathbf{w}^{\text{T}}X^{\text{T}}X\mathbf{w})}{\partial \mathbf{w}} $$
Let's evaluate each term:
*   $\frac{\partial (\mathbf{y}^{\text{T}}\mathbf{y})}{\partial \mathbf{w}} = 0$ (since $\mathbf{y}^{\text{T}}\mathbf{y}$ is a scalar constant with respect to $\mathbf{w}$).
*   $\frac{\partial (2\mathbf{w}^{\text{T}}X^{\text{T}}\mathbf{y})}{\partial \mathbf{w}} = 2X^{\text{T}}\mathbf{y}$ (using rule 1, with $\mathbf{a} = X^{\text{T}}\mathbf{y}$).
*   For the third term, let $A = X^{\text{T}}X$. Note that $A$ is a symmetric matrix because $(X^{\text{T}}X)^{\text{T}} = X^{\text{T}}(X^{\text{T}})^{\text{T}} = X^{\text{T}}X$.
    So, $\frac{\partial (\mathbf{w}^{\text{T}}X^{\text{T}}X\mathbf{w})}{\partial \mathbf{w}} = 2X^{\text{T}}X\mathbf{w}$ (using rule 2 for a symmetric matrix $A$).

Combining these, the derivative is:
$$ \frac{\partial J(\mathbf{w})}{\partial \mathbf{w}} = 0 - 2X^{\text{T}}\mathbf{y} + 2X^{\text{T}}X\mathbf{w} $$

**Solving for $\mathbf{w}$:**
Set the derivative to zero to find the critical point:
$$ 2X^{\text{T}}X\mathbf{w} - 2X^{\text{T}}\mathbf{y} = 0 $$
Divide by 2 and rearrange:
$$ X^{\text{T}}X\mathbf{w} = X^{\text{T}}\mathbf{y} $$
These are known as the **Normal Equations**.

Assuming that the matrix $X^{\text{T}}X$ is invertible (which is true if the columns of $X$ are linearly independent, meaning there is no perfect multicollinearity among the features), we can multiply both sides by $(X^{\text{T}}X)^{-1}$ from the left:
$$ (X^{\text{T}}X)^{-1}(X^{\text{T}}X)\mathbf{w} = (X^{\text{T}}X)^{-1}X^{\text{T}}\mathbf{y} $$
$$ \mathbf{I}\mathbf{w} = (X^{\text{T}}X)^{-1}X^{\text{T}}\mathbf{y} $$
$$ \mathbf{w} = (X^{\text{T}}X)^{-1}X^{\text{T}}\mathbf{y} $$

This is the formula for the optimal weight vector $\mathbf{w}$ that minimizes the sum of squared errors in Linear Regression.

---
**Note:** The correct formula for the optimal weight vector in linear regression is $$(X^T X)^{-1} X^T y$$, where $$X^T X$$ must be invertible.

---
### Solving Least-Squares Problems

**Problem:** Given a system $Ax = b$ where $A \in \mathbb{R}^{m \times n}$ with $m > n$ (overdetermined system), find $x^*$ that minimizes $\|Ax - b\|_2^2$.

**Proof:**

We want to minimize the objective function:
$$f(x) = \|Ax - b\|_2^2 = (Ax - b)^T(Ax - b)$$

Expanding this:
$$f(x) = x^T A^T A x - 2x^T A^T b + b^T b$$

To find the minimum, we take the gradient and set it equal to zero:
$$\nabla f(x) = 2A^T A x - 2A^T b = 0$$

This gives us the **normal equations**:
$$(A^T A)x = A^T b$$

**Why this is a minimum:** The Hessian matrix is:
$$\nabla^2 f(x) = 2A^T A$$

Since $A^T A$ is **positive semi-definite** (for any vector $v$: $v^T A^T A v = \|Av\|_2^2 \geq 0$), the critical point is indeed a minimum.

**Solution:** If $A$ has full column rank, then $A^T A$ is invertible, and:
$$x^* = (A^T A)^{-1} A^T b$$

This $x^*$ is the least-squares solution that minimizes the error $\|Ax - b\|_2$.

**So:**

The solution comes from solving the normal equations:
$$(A^T A)x = A^T b$$

This gives the closed-form solution:
$$x = (A^T A)^{-1} A^T b$$

**Performance:**
- Time complexity: roughly $n^2k$ operations
- A standard computer solves problems with hundreds of variables and thousands of terms in seconds
- Sparse matrices (many zero entries) can be solved much faster

**Example:** A sparse matrix for image processing might have only 5 non-zero entries per row in a 10,000 × 10,000 matrix.
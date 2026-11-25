---
layout: post
title: '14-01-02 Does Newton''s Method Move Perpendicular to the Level Curves?'
chapter: '14'
order: 4
owner: AI Assistant
categories:
- chapter14
lang: en
---

Every calculus student learns that $$-\nabla f(x)$$ points strictly perpendicular to the level curve $$f(x) = c$$. So it is natural to assume that Newton's method—being an "upgraded" gradient descent—also crosses level curves at $$90^\circ$$. In fact, it almost **never** does! On elongated elliptical valleys, the perpendicular direction misses the minimum completely, whereas Newton's method deliberately tilts *away* from the normal so it can aim directly at the valley floor.

## Key ideas: Level-Curve Geometry of Newton vs. Gradient Descent

- **Pillar 1 — Steepest Descent Is Euclidean-Orthogonal:** In the standard Euclidean inner product, $$-\nabla f(x)$$ is orthogonal to the tangent space of the level set $$\{y : f(y) = f(x)\}$$.
- **Pillar 2 — Newton Is Steepest Descent in the Hessian Metric:** Defining the local inner product $$\langle u, v \rangle_H = u^T H v$$ (where $$H = \nabla^2 f(x)$$), the Newton step $$-H^{-1}\nabla f(x)$$ is orthogonal to the level curve *in the $$H$$-metric*, not the Euclidean metric.
- **Pillar 3 — When Does Newton Move Perpendicularly?:** The angle between $$-\nabla f(x)$$ and $$-H^{-1}\nabla f(x)$$ is $$0^\circ$$ if and only if $$\nabla f(x)$$ is an eigenvector of $$\nabla^2 f(x)$$ (which happens everywhere only for isotropic $$H = cI$$, or along principal axes of an ellipse).
- **Pillar 4 — Descent Guarantee Despite Large Angles:** Even when the Euclidean angle between $$\Delta x_{\text{nt}}$$ and $$-\nabla f(x)$$ approaches $$89^\circ$$ on extreme canyons, $$\nabla f(x)^T \Delta x_{\text{nt}} = -\nabla f(x)^T H^{-1}\nabla f(x) < 0$$ guarantees the angle is strictly acute ($$< 90^\circ$$).

### Worked example: Measuring the Exact Angle Between Newton and the Level-Curve Normal

Consider the elliptical bowl $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + 9x_2^2)$$ at $$x = (3, 1)^T$$.

1. **Compute the steepest-descent direction (perpendicular to the level curve):**
   $$d_{\text{GD}} = -\nabla f(3, 1) = -\begin{bmatrix} 3 \\ 9 \end{bmatrix} = \begin{bmatrix} -3 \\ -9 \end{bmatrix}, \qquad \|d_{\text{GD}}\|_2 = \sqrt{9 + 81} = \sqrt{90} \approx 9.487.$$
2. **Compute the Newton direction:** With $$H = \operatorname{diag}(1, 9)$$,
   $$d_{\text{NT}} = -H^{-1}\nabla f(3, 1) = -\begin{bmatrix} 1 & 0 \\ 0 & 1/9 \end{bmatrix}\begin{bmatrix} 3 \\ 9 \end{bmatrix} = \begin{bmatrix} -3 \\ -1 \end{bmatrix}, \qquad \|d_{\text{NT}}\|_2 = \sqrt{10} \approx 3.162.$$
   Notice $$x + d_{\text{NT}} = (0, 0)^T$$ hits the exact minimum!
3. **Compute the Euclidean angle $$\theta$$ between $$d_{\text{GD}}$$ and $$d_{\text{NT}}$$:**
   $$\cos\theta = \frac{d_{\text{GD}}^T d_{\text{NT}}}{\|d_{\text{GD}}\|_2 \|d_{\text{NT}}\|_2} = \frac{(-3)(-3) + (-9)(-1)}{\sqrt{90}\cdot\sqrt{10}} = \frac{9 + 9}{30} = \frac{18}{30} = 0.6.$$
   Therefore $$\theta = \arccos(0.6) \approx 53.13^\circ$$! Newton tilts $$53.13^\circ$$ away from the perpendicular normal so it can shoot straight to the origin.

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center",
    tex2jax: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
    }
});
</script>

<style>
.interactive-container {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
}

.controls {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 20px;
    align-items: center;
}

.control-group {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.control-group label {
    font-weight: bold;
    font-size: 0.9em;
    color: #495057;
}

.control-group input[type="range"] {
    width: 150px;
}

.control-group input[type="number"] {
    width: 80px;
    padding: 4px;
    border: 1px solid #ced4da;
    border-radius: 4px;
}

button {
    background: #007bff;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9em;
}

button:hover {
    background: #0056b3;
}

button:disabled {
    background: #6c757d;
    cursor: not-allowed;
}

#canvas {
    border: 1px solid #dee2e6;
    border-radius: 4px;
    display: block;
    margin: 0 auto;
}

.info-panel {
    background: #e9ecef;
    padding: 15px;
    border-radius: 4px;
    margin-top: 15px;
    font-family: monospace;
    font-size: 0.85em;
}

.legend {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 10px;
    font-size: 0.9em;
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 5px;
}

.legend-color {
    width: 20px;
    height: 3px;
    border-radius: 2px;
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

.comparison-table th,
.comparison-table td {
    border: 1px solid #dee2e6;
    padding: 12px;
    text-align: left;
}

.comparison-table th {
    background: #f8f9fa;
    font-weight: bold;
}

.math-explanation {
    background: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 4px;
    padding: 15px;
    margin: 15px 0;
}

.key-insight {
    background: #d1ecf1;
    border: 1px solid #bee5eb;
    border-radius: 4px;
    padding: 15px;
    margin: 15px 0;
}
</style>

In this lesson, we explore an important question in optimization: **Does Newton's method move perpendicular to the level curves?** This question helps us understand more deeply the difference between Newton's method and gradient descent.

## 1. Basic Intuition

<div class="key-insight">
<strong>Short answer:</strong> <strong>NO</strong>, Newton's method generally does NOT move perpendicular to the level curves, unlike gradient descent.
</div>

### Comparison with Gradient Descent

- **Gradient Descent**: Always moves in the direction $$-\nabla f$$, perpendicular to the level curves
- **Newton's Method**: Uses second-order information (the Hessian) to "adjust" the direction of movement, which is no longer perpendicular in the original space

## 2. Mathematical Explanation

### Gradient Descent
The direction of movement in gradient descent:
$$\mathbf{d}_{GD} = -\nabla f(\mathbf{x})$$

This direction is always perpendicular to the level curves because the gradient is the normal vector of the level curves.

### Newton's Method
The direction of movement in Newton's method:
$$\mathbf{d}_{Newton} = -[\nabla^2 f(\mathbf{x})]^{-1} \nabla f(\mathbf{x})$$

<div class="math-explanation">
<strong>Explanation:</strong> The Hessian $$\nabla^2 f$$ "transforms" the space, so that the direction of movement is no longer perpendicular to the level curves in the original coordinates. Newton optimizes along the "steepest direction" in the space transformed by the Hessian.
</div>

### When Is Newton Perpendicular?
When the Hessian is a multiple of the identity matrix, $$\nabla^2 f = cI$$ (with $$c$$ a constant), Newton coincides with GD (with step size $$1/c$$) and moves perpendicular to the level curves. More generally, Newton is perpendicular only at points where $$\nabla f$$ is an eigenvector of the Hessian (for example, along the coordinate axes when the Hessian is a diagonal matrix).

## 3. Interactive Illustration

<div class="interactive-container">
    <h4>Comparing the Newton and Gradient Descent Trajectories</h4>
    
    <div class="controls">
        <div class="control-group">
            <label for="a-param">Parameter a (curvature along x):</label>
            <input type="range" id="a-param" min="1" max="20" value="10" step="1">
            <input type="number" id="a-value" min="1" max="20" value="10" step="1">
        </div>
        
        <div class="control-group">
            <label for="b-param">Parameter b (curvature along y):</label>
            <input type="range" id="b-param" min="1" max="20" value="1" step="1">
            <input type="number" id="b-value" min="1" max="20" value="1" step="1">
        </div>
        
        <div class="control-group">
            <label for="start-x">Starting point x:</label>
            <input type="number" id="start-x" min="-3" max="3" value="2" step="0.1">
        </div>
        
        <div class="control-group">
            <label for="start-y">Starting point y:</label>
            <input type="number" id="start-y" min="-3" max="3" value="1.5" step="0.1">
        </div>
        
        <div class="control-group">
            <label for="learning-rate">Learning Rate (GD):</label>
            <input type="range" id="learning-rate" min="0.01" max="0.5" value="0.1" step="0.01">
            <input type="number" id="lr-value" min="0.01" max="0.5" value="0.1" step="0.01">
        </div>
        
        <button id="start-btn">Start</button>
        <button id="step-btn">Step</button>
        <button id="reset-btn">Reset</button>
        <button id="toggle-contour">Show/Hide level curves</button>
    </div>
    
    <canvas id="canvas" width="600" height="500"></canvas>
    
    <div class="legend">
        <div class="legend-item">
            <div class="legend-color" style="background: #ff4444;"></div>
            <span>Gradient Descent (perpendicular to the level curves)</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background: #4444ff;"></div>
            <span>Newton's Method (cuts across the level curves)</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background: #888888;"></div>
            <span>Level curves</span>
        </div>
    </div>
    
    <div id="info-panel" class="info-panel">
        Objective function: f(x,y) = (ax² + by²)/2<br>
        Press "Start" to compare the trajectories of the two methods
    </div>
</div>

## 4. Detailed Analysis

<table class="comparison-table">
    <thead>
        <tr>
            <th>Property</th>
            <th>Gradient Descent</th>
            <th>Newton's Method</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Direction of movement</strong></td>
            <td>$$-\nabla f$$ (perpendicular to the level curves)</td>
            <td>$$-H^{-1}\nabla f$$ (not perpendicular)</td>
        </tr>
        <tr>
            <td><strong>Information used</strong></td>
            <td>Gradient only (first order)</td>
            <td>Gradient + Hessian (second order)</td>
        </tr>
        <tr>
            <td><strong>Convergence rate</strong></td>
            <td>Linear</td>
            <td>Quadratic (near the optimum)</td>
        </tr>
        <tr>
            <td><strong>Handling ill-conditioning</strong></td>
            <td>Poor (zig-zag)</td>
            <td>Good (goes straight)</td>
        </tr>
        <tr>
            <td><strong>Computational cost</strong></td>
            <td>O(n) per step</td>
            <td>O(n³) per step</td>
        </tr>
    </tbody>
</table>

## 5. A Concrete Example

Consider the function $$f(x,y) = x^2 + 10y^2$$, whose level curves are flat ellipses.

**At the point (1,1):**
- **Gradient**: $$\nabla f = (2, 20)$$ - perpendicular to the ellipse
- **Hessian**: $$H = \begin{pmatrix} 2 & 0 \\ 0 & 20 \end{pmatrix}$$
- **Newton direction**: $$\mathbf{d} = -H^{-1}\nabla f = -\begin{pmatrix} 1/2 & 0 \\ 0 & 1/20 \end{pmatrix} \begin{pmatrix} 2 \\ 20 \end{pmatrix} = (-1, -1)$$

<div class="key-insight">
<strong>Observation:</strong> Gradient descent moves in the direction (-2, -20) (perpendicular), while Newton moves in the direction (-1, -1) (cutting diagonally across the ellipse).
</div>

## 6. Why Does This Matter?

### Advantages of Newton
1. **Handles ill-conditioning well**: when the function has different curvature in different directions
2. **Faster convergence**: especially near the optimum
3. **Affine invariance**: independent of the coordinate system

### Disadvantages
1. **High computational cost**: the Hessian must be computed and inverted
2. **Can be unstable**: if the Hessian is not positive definite
3. **Not suitable for large-scale data**: because of the O(n³) complexity

## 7. Applications in Machine Learning

In practice, variants of Newton's method are used:
- **L-BFGS**: approximates the Hessian, avoiding the full computation
- **Gauss-Newton**: for least-squares problems
- **Levenberg-Marquardt**: combines the advantages of GD and Newton

<div class="math-explanation">
<strong>Conclusion:</strong> Newton's method does not move perpendicular to the level curves because it optimizes in the space "transformed" by the Hessian. This allows it to converge faster, at a higher computational cost.
</div>

<script>
class OptimizationVisualizer {
    constructor() {
        this.canvas = document.getElementById('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        // Parameters
        this.a = 10;
        this.b = 1;
        this.startX = 2;
        this.startY = 1.5;
        this.learningRate = 0.1;
        
        // Visualization settings
        this.scale = 80;
        this.centerX = this.width / 2;
        this.centerY = this.height / 2;
        this.showContour = true;
        
        // Animation state
        this.isRunning = false;
        this.gdPath = [];
        this.newtonPath = [];
        this.currentStep = 0;
        this.maxSteps = 20;
        
        this.setupEventListeners();
        this.reset();
    }
    
    setupEventListeners() {
        // Parameter controls
        const aParam = document.getElementById('a-param');
        const aValue = document.getElementById('a-value');
        const bParam = document.getElementById('b-param');
        const bValue = document.getElementById('b-value');
        const lrParam = document.getElementById('learning-rate');
        const lrValue = document.getElementById('lr-value');
        
        // Sync sliders with number inputs
        aParam.addEventListener('input', (e) => {
            this.a = parseFloat(e.target.value);
            aValue.value = this.a;
            this.reset();
        });
        
        aValue.addEventListener('input', (e) => {
            this.a = parseFloat(e.target.value);
            aParam.value = this.a;
            this.reset();
        });
        
        bParam.addEventListener('input', (e) => {
            this.b = parseFloat(e.target.value);
            bValue.value = this.b;
            this.reset();
        });
        
        bValue.addEventListener('input', (e) => {
            this.b = parseFloat(e.target.value);
            bParam.value = this.b;
            this.reset();
        });
        
        lrParam.addEventListener('input', (e) => {
            this.learningRate = parseFloat(e.target.value);
            lrValue.value = this.learningRate;
        });
        
        lrValue.addEventListener('input', (e) => {
            this.learningRate = parseFloat(e.target.value);
            lrParam.value = this.learningRate;
        });
        
        // Start position controls
        document.getElementById('start-x').addEventListener('input', (e) => {
            this.startX = parseFloat(e.target.value);
            this.reset();
        });
        
        document.getElementById('start-y').addEventListener('input', (e) => {
            this.startY = parseFloat(e.target.value);
            this.reset();
        });
        
        // Buttons
        document.getElementById('start-btn').addEventListener('click', () => this.startAnimation());
        document.getElementById('step-btn').addEventListener('click', () => this.stepAnimation());
        document.getElementById('reset-btn').addEventListener('click', () => this.reset());
        document.getElementById('toggle-contour').addEventListener('click', () => this.toggleContour());
    }
    
    // Objective function: f(x,y) = (ax² + by²)/2
    f(x, y) {
        return (this.a * x * x + this.b * y * y) / 2;
    }
    
    // Gradient: ∇f = (ax, by)
    gradient(x, y) {
        return [this.a * x, this.b * y];
    }
    
    // Hessian: H = [[a, 0], [0, b]]
    hessian(x, y) {
        return [[this.a, 0], [0, this.b]];
    }
    
    // Matrix inverse for 2x2
    inverse2x2(matrix) {
        const [[a, b], [c, d]] = matrix;
        const det = a * d - b * c;
        if (Math.abs(det) < 1e-10) return null;
        return [[d/det, -b/det], [-c/det, a/det]];
    }
    
    // Matrix-vector multiplication
    matVecMul(matrix, vector) {
        const [x, y] = vector;
        return [
            matrix[0][0] * x + matrix[0][1] * y,
            matrix[1][0] * x + matrix[1][1] * y
        ];
    }
    
    // Gradient descent step
    gradientDescentStep(x, y) {
        const [gx, gy] = this.gradient(x, y);
        return [
            x - this.learningRate * gx,
            y - this.learningRate * gy
        ];
    }
    
    // Newton method step
    newtonStep(x, y) {
        const [gx, gy] = this.gradient(x, y);
        const H = this.hessian(x, y);
        const Hinv = this.inverse2x2(H);
        
        if (!Hinv) return [x, y]; // Fallback if Hessian is singular
        
        const [dx, dy] = this.matVecMul(Hinv, [gx, gy]);
        return [x - dx, y - dy];
    }
    
    // Convert world coordinates to canvas coordinates
    worldToCanvas(x, y) {
        return [
            this.centerX + x * this.scale,
            this.centerY - y * this.scale
        ];
    }
    
    // Convert canvas coordinates to world coordinates
    canvasToWorld(canvasX, canvasY) {
        return [
            (canvasX - this.centerX) / this.scale,
            -(canvasY - this.centerY) / this.scale
        ];
    }
    
    drawContourLines() {
        if (!this.showContour) return;
        
        this.ctx.strokeStyle = '#888888';
        this.ctx.lineWidth = 1;
        
        const levels = [0.5, 1, 2, 4, 8, 16];
        
        for (const level of levels) {
            this.ctx.beginPath();
            
            // Draw ellipse for level set f(x,y) = level
            // (ax² + by²)/2 = level => ax² + by² = 2*level
            // x²/(2*level/a) + y²/(2*level/b) = 1
            const radiusX = Math.sqrt(2 * level / this.a) * this.scale;
            const radiusY = Math.sqrt(2 * level / this.b) * this.scale;
            
            this.ctx.ellipse(this.centerX, this.centerY, radiusX, radiusY, 0, 0, 2 * Math.PI);
            this.ctx.stroke();
        }
    }
    
    drawPath(path, color, label) {
        if (path.length < 2) return;
        
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = 3;
        this.ctx.beginPath();
        
        const [startCanvasX, startCanvasY] = this.worldToCanvas(path[0][0], path[0][1]);
        this.ctx.moveTo(startCanvasX, startCanvasY);
        
        for (let i = 1; i < path.length; i++) {
            const [canvasX, canvasY] = this.worldToCanvas(path[i][0], path[i][1]);
            this.ctx.lineTo(canvasX, canvasY);
        }
        this.ctx.stroke();
        
        // Draw points
        this.ctx.fillStyle = color;
        for (let i = 0; i < path.length; i++) {
            const [canvasX, canvasY] = this.worldToCanvas(path[i][0], path[i][1]);
            this.ctx.beginPath();
            this.ctx.arc(canvasX, canvasY, i === 0 ? 6 : 4, 0, 2 * Math.PI);
            this.ctx.fill();
        }
        
        // Draw arrows for direction
        for (let i = 0; i < path.length - 1; i++) {
            const [x1, y1] = this.worldToCanvas(path[i][0], path[i][1]);
            const [x2, y2] = this.worldToCanvas(path[i+1][0], path[i+1][1]);
            this.drawArrow(x1, y1, x2, y2, color);
        }
    }
    
    drawArrow(x1, y1, x2, y2, color) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        const length = Math.sqrt(dx * dx + dy * dy);
        
        if (length < 5) return;
        
        const angle = Math.atan2(dy, dx);
        const arrowLength = 10;
        const arrowAngle = Math.PI / 6;
        
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        
        // Arrow head
        const headX = x2 - arrowLength * Math.cos(angle - arrowAngle);
        const headY = y2 - arrowLength * Math.sin(angle - arrowAngle);
        this.ctx.moveTo(x2, y2);
        this.ctx.lineTo(headX, headY);
        
        const headX2 = x2 - arrowLength * Math.cos(angle + arrowAngle);
        const headY2 = y2 - arrowLength * Math.sin(angle + arrowAngle);
        this.ctx.moveTo(x2, y2);
        this.ctx.lineTo(headX2, headY2);
        
        this.ctx.stroke();
    }
    
    drawAxes() {
        this.ctx.strokeStyle = '#cccccc';
        this.ctx.lineWidth = 1;
        
        // X axis
        this.ctx.beginPath();
        this.ctx.moveTo(0, this.centerY);
        this.ctx.lineTo(this.width, this.centerY);
        this.ctx.stroke();
        
        // Y axis
        this.ctx.beginPath();
        this.ctx.moveTo(this.centerX, 0);
        this.ctx.lineTo(this.centerX, this.height);
        this.ctx.stroke();
        
        // Origin
        this.ctx.fillStyle = '#666666';
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, 3, 0, 2 * Math.PI);
        this.ctx.fill();
    }
    
    draw() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        // Draw axes
        this.drawAxes();
        
        // Draw contour lines
        this.drawContourLines();
        
        // Draw paths
        this.drawPath(this.gdPath, '#ff4444', 'GD');
        this.drawPath(this.newtonPath, '#4444ff', 'Newton');
        
        // Update info panel
        this.updateInfoPanel();
    }
    
    updateInfoPanel() {
        const panel = document.getElementById('info-panel');
        const gdCurrent = this.gdPath.length > 0 ? this.gdPath[this.gdPath.length - 1] : [this.startX, this.startY];
        const newtonCurrent = this.newtonPath.length > 0 ? this.newtonPath[this.newtonPath.length - 1] : [this.startX, this.startY];
        
        const gdValue = this.f(gdCurrent[0], gdCurrent[1]);
        const newtonValue = this.f(newtonCurrent[0], newtonCurrent[1]);
        
        panel.innerHTML = `
            Objective function: f(x,y) = (${this.a}x² + ${this.b}y²)/2<br>
            Current step: ${this.currentStep}<br>
            GD - Position: (${gdCurrent[0].toFixed(3)}, ${gdCurrent[1].toFixed(3)}), f = ${gdValue.toFixed(4)}<br>
            Newton - Position: (${newtonCurrent[0].toFixed(3)}, ${newtonCurrent[1].toFixed(3)}), f = ${newtonValue.toFixed(4)}
        `;
    }
    
    reset() {
        this.isRunning = false;
        this.gdPath = [[this.startX, this.startY]];
        this.newtonPath = [[this.startX, this.startY]];
        this.currentStep = 0;
        
        document.getElementById('start-btn').disabled = false;
        document.getElementById('step-btn').disabled = false;
        
        this.draw();
    }
    
    stepAnimation() {
        if (this.currentStep >= this.maxSteps) return;
        
        // Gradient descent step
        const gdCurrent = this.gdPath[this.gdPath.length - 1];
        const gdNext = this.gradientDescentStep(gdCurrent[0], gdCurrent[1]);
        this.gdPath.push(gdNext);
        
        // Newton step
        const newtonCurrent = this.newtonPath[this.newtonPath.length - 1];
        const newtonNext = this.newtonStep(newtonCurrent[0], newtonCurrent[1]);
        this.newtonPath.push(newtonNext);
        
        this.currentStep++;
        this.draw();
        
        // Check convergence
        const gdConverged = Math.abs(gdNext[0]) < 0.01 && Math.abs(gdNext[1]) < 0.01;
        const newtonConverged = Math.abs(newtonNext[0]) < 0.01 && Math.abs(newtonNext[1]) < 0.01;
        
        if (gdConverged && newtonConverged || this.currentStep >= this.maxSteps) {
            this.isRunning = false;
            document.getElementById('start-btn').disabled = false;
            document.getElementById('step-btn').disabled = true;
        }
    }
    
    startAnimation() {
        if (this.isRunning) return;
        
        this.isRunning = true;
        document.getElementById('start-btn').disabled = true;
        document.getElementById('step-btn').disabled = true;
        
        const animate = () => {
            if (!this.isRunning) return;
            
            this.stepAnimation();
            
            if (this.isRunning && this.currentStep < this.maxSteps) {
                setTimeout(animate, 500);
            } else {
                this.isRunning = false;
                document.getElementById('start-btn').disabled = false;
                document.getElementById('step-btn').disabled = false;
            }
        };
        
        animate();
    }
    
    toggleContour() {
        this.showContour = !this.showContour;
        this.draw();
    }
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', () => {
    new OptimizationVisualizer();
});
</script>

## References

1. Boyd, S., & Vandenberghe, L. (2004). *Convex optimization*. Cambridge University Press.
2. Nocedal, J., & Wright, S. J. (2006). *Numerical optimization* (2nd ed.). Springer.
3. Nesterov, Y. (2003). *Introductory lectures on convex optimization: A basic course*. Springer.
4. Bertsekas, D. P. (1999). *Nonlinear programming* (2nd ed.). Athena Scientific.

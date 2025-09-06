---
layout: post
title: 06-01 Gradient Descent
chapter: '06'
order: 2
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
lesson_type: required
---

Gradient descent is the simplest algorithm for solving unconstrained convex and differentiable optimization problems.

> $$\min_x f(x),$$
> where $$f$$ is differentiable and $$dom(f) = \mathbb{R}^n$$.

The optimal value is $$f^* = \min_x f(x)$$, and the optimizer is $$x^*$$.

## Why Gradient Descent Matters in Data Science

**Gradient descent is the workhorse of machine learning!** It's the algorithm behind:

- **Training neural networks**: Backpropagation uses gradient descent to update weights
- **Linear regression**: Finding optimal coefficients to minimize MSE
- **Logistic regression**: Optimizing parameters for classification
- **Deep learning**: Training complex models with millions of parameters
- **Recommendation systems**: Learning user preferences and item features

**Key insight**: Every time you see "training" or "learning" in ML, gradient descent (or its variants) is likely involved!


## Gradient Descent for Single Variable Functions

For functions of a single variable $$f: \mathbb{R} \to \mathbb{R}$$, gradient descent simplifies significantly. The gradient becomes the derivative, and the update rule becomes:

> $$x^{(k)} = x^{(k-1)} - t_k f'(x^{(k-1)}), \quad k = 1, 2, 3, ...$$

where $$f'(x)$$ is the derivative of $$f$$ at point $$x$$.

### Geometric Interpretation

In the single variable case, the derivative $$f'(x)$$ represents the slope of the tangent line at point $$x$$:
- If $$f'(x) > 0$$, the function is increasing, so we move left (subtract a positive value)
- If $$f'(x) < 0$$, the function is decreasing, so we move right (subtract a negative value)
- If $$f'(x) = 0$$, we have reached a critical point (potential minimum)

### Example: Quadratic Function

Consider the quadratic function $$f(x) = \frac{1}{2}(x - 2)^2 + 1$$ with derivative $$f'(x) = x - 2$$.

The gradient descent update becomes:
> $$x^{(k)} = x^{(k-1)} - t(x^{(k-1)} - 2)$$

Starting from $$x^{(0)} = 0$$ with step size $$t = 0.1$$:
> $$x^{(1)} = 0 - 0.1(0 - 2) = 0.2 \\ $$ 
> $$x^{(2)} = 0.2 - 0.1(0.2 - 2) = 0.38$$
> $$x^{(3)} = 0.38 - 0.1(0.38 - 2) = 0.542$$
> ...

The sequence converges to $$x^* = 2$$, which is the global minimum.

### Step Size Selection

The choice of step size $$t$$ is crucial:
- **Too small**: Convergence is very slow
- **Too large**: The algorithm may overshoot and diverge
- **Optimal**: For quadratic functions $$f(x) = \frac{1}{2}ax^2 + bx + c$$ with $$a > 0$$, the optimal step size is $$t = \frac{1}{a}$$

### Interactive Visualization

<div id="single-var-gradient-descent" style="margin: 20px 0;">
    <div style="margin-bottom: 15px;">
        <label for="step-size-slider">Step Size (t): <span id="step-size-value">0.1</span></label><br>
        <input type="range" id="step-size-slider" min="0.01" max="0.5" step="0.01" value="0.1" style="width: 300px;">
    </div>
    
    <div style="margin-bottom: 15px;">
        <label for="start-point-slider">Starting Point: <span id="start-point-value">-3</span></label><br>
        <input type="range" id="start-point-slider" min="-5" max="5" step="0.1" value="-3" style="width: 300px;">
    </div>
    
    <div style="margin-bottom: 15px;">
        <button id="start-animation">Start Animation</button>
        <button id="reset-animation">Reset</button>
        <button id="step-once">Single Step</button>
    </div>
    
    <canvas id="gradient-canvas" width="600" height="400" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    
    <div id="iteration-info" style="text-align: center; margin-top: 10px; font-family: monospace;">
        Iteration: 0, x = -3.000, f(x) = 13.500, f'(x) = -5.000
    </div>
</div>

<script>
class SingleVarGradientDescent {
    constructor() {
        this.canvas = document.getElementById('gradient-canvas');
        this.ctx = this.canvas.getContext('2d');
        this.stepSizeSlider = document.getElementById('step-size-slider');
        this.startPointSlider = document.getElementById('start-point-slider');
        this.stepSizeValue = document.getElementById('step-size-value');
        this.startPointValue = document.getElementById('start-point-value');
        this.iterationInfo = document.getElementById('iteration-info');
        
        // Animation state
        this.isAnimating = false;
        this.currentX = -3;
        this.iteration = 0;
        this.history = [];
        this.animationId = null;
        
        // Function parameters: f(x) = 0.5 * (x - 2)^2 + 1
        this.a = 0.5;
        this.b = 2;
        this.c = 1;
        
        this.setupEventListeners();
        this.reset();
    }
    
    setupEventListeners() {
        this.stepSizeSlider.addEventListener('input', (e) => {
            this.stepSizeValue.textContent = e.target.value;
        });
        
        this.startPointSlider.addEventListener('input', (e) => {
            this.startPointValue.textContent = e.target.value;
            if (!this.isAnimating) {
                this.reset();
            }
        });
        
        document.getElementById('start-animation').addEventListener('click', () => {
            this.startAnimation();
        });
        
        document.getElementById('reset-animation').addEventListener('click', () => {
            this.reset();
        });
        
        document.getElementById('step-once').addEventListener('click', () => {
            this.singleStep();
        });
    }
    
    // Function: f(x) = 0.5 * (x - 2)^2 + 1
    f(x) {
        return this.a * Math.pow(x - this.b, 2) + this.c;
    }
    
    // Derivative: f'(x) = (x - 2)
    fprime(x) {
        return 2 * this.a * (x - this.b);
    }
    
    // Convert x coordinate to canvas coordinate
    xToCanvas(x) {
        const xMin = -5, xMax = 5;
        return (x - xMin) / (xMax - xMin) * this.canvas.width;
    }
    
    // Convert y coordinate to canvas coordinate
    yToCanvas(y) {
        const yMin = 0, yMax = 15;
        return this.canvas.height - (y - yMin) / (yMax - yMin) * this.canvas.height;
    }
    
    // Convert canvas x to actual x
    canvasToX(canvasX) {
        const xMin = -5, xMax = 5;
        return xMin + (canvasX / this.canvas.width) * (xMax - xMin);
    }
    
    drawFunction() {
        this.ctx.strokeStyle = '#2196F3';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        
        for (let canvasX = 0; canvasX <= this.canvas.width; canvasX += 2) {
            const x = this.canvasToX(canvasX);
            const y = this.f(x);
            const canvasY = this.yToCanvas(y);
            
            if (canvasX === 0) {
                this.ctx.moveTo(canvasX, canvasY);
            } else {
                this.ctx.lineTo(canvasX, canvasY);
            }
        }
        this.ctx.stroke();
    }
    
    drawAxes() {
        this.ctx.strokeStyle = '#666';
        this.ctx.lineWidth = 1;
        
        // X-axis
        const yZero = this.yToCanvas(0);
        this.ctx.beginPath();
        this.ctx.moveTo(0, yZero);
        this.ctx.lineTo(this.canvas.width, yZero);
        this.ctx.stroke();
        
        // Y-axis
        const xZero = this.xToCanvas(0);
        this.ctx.beginPath();
        this.ctx.moveTo(xZero, 0);
        this.ctx.lineTo(xZero, this.canvas.height);
        this.ctx.stroke();
        
        // Labels
        this.ctx.fillStyle = '#666';
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'center';
        
        // X-axis labels
        for (let x = -4; x <= 4; x += 2) {
            const canvasX = this.xToCanvas(x);
            this.ctx.fillText(x.toString(), canvasX, yZero + 15);
        }
        
        // Y-axis labels
        this.ctx.textAlign = 'right';
        for (let y = 2; y <= 14; y += 2) {
            const canvasY = this.yToCanvas(y);
            this.ctx.fillText(y.toString(), xZero - 5, canvasY + 4);
        }
    }
    
    drawCurrentPoint() {
        const canvasX = this.xToCanvas(this.currentX);
        const canvasY = this.yToCanvas(this.f(this.currentX));
        
        // Current point
        this.ctx.fillStyle = '#F44336';
        this.ctx.beginPath();
        this.ctx.arc(canvasX, canvasY, 6, 0, 2 * Math.PI);
        this.ctx.fill();
        
        // Tangent line
        const derivative = this.fprime(this.currentX);
        const tangentLength = 1;
        const x1 = this.currentX - tangentLength;
        const x2 = this.currentX + tangentLength;
        const y1 = this.f(this.currentX) + derivative * (x1 - this.currentX);
        const y2 = this.f(this.currentX) + derivative * (x2 - this.currentX);
        
        this.ctx.strokeStyle = '#FF9800';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.moveTo(this.xToCanvas(x1), this.yToCanvas(y1));
        this.ctx.lineTo(this.xToCanvas(x2), this.yToCanvas(y2));
        this.ctx.stroke();
    }
    
    drawHistory() {
        if (this.history.length < 2) return;
        
        this.ctx.strokeStyle = '#4CAF50';
        this.ctx.lineWidth = 2;
        this.ctx.setLineDash([5, 5]);
        this.ctx.beginPath();
        
        for (let i = 0; i < this.history.length; i++) {
            const x = this.history[i];
            const canvasX = this.xToCanvas(x);
            const canvasY = this.yToCanvas(this.f(x));
            
            if (i === 0) {
                this.ctx.moveTo(canvasX, canvasY);
            } else {
                this.ctx.lineTo(canvasX, canvasY);
            }
        }
        this.ctx.stroke();
        this.ctx.setLineDash([]);
        
        // Draw history points
        this.ctx.fillStyle = '#4CAF50';
        for (let i = 0; i < this.history.length - 1; i++) {
            const x = this.history[i];
            const canvasX = this.xToCanvas(x);
            const canvasY = this.yToCanvas(this.f(x));
            
            this.ctx.beginPath();
            this.ctx.arc(canvasX, canvasY, 3, 0, 2 * Math.PI);
            this.ctx.fill();
        }
    }
    
    draw() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw components
        this.drawAxes();
        this.drawFunction();
        this.drawHistory();
        this.drawCurrentPoint();
        
        // Update iteration info
        this.iterationInfo.textContent = 
            `Iteration: ${this.iteration}, x = ${this.currentX.toFixed(3)}, ` +
            `f(x) = ${this.f(this.currentX).toFixed(3)}, f'(x) = ${this.fprime(this.currentX).toFixed(3)}`;
    }
    
    singleStep() {
        if (Math.abs(this.fprime(this.currentX)) < 1e-6) {
            return; // Already at minimum
        }
        
        const stepSize = parseFloat(this.stepSizeSlider.value);
        const newX = this.currentX - stepSize * this.fprime(this.currentX);
        
        this.history.push(this.currentX);
        this.currentX = newX;
        this.iteration++;
        
        this.draw();
    }
    
    startAnimation() {
        if (this.isAnimating) {
            this.stopAnimation();
            return;
        }
        
        this.isAnimating = true;
        document.getElementById('start-animation').textContent = 'Stop Animation';
        
        const animate = () => {
            if (!this.isAnimating) return;
            
            if (Math.abs(this.fprime(this.currentX)) > 1e-6 && this.iteration < 100) {
                this.singleStep();
                this.animationId = setTimeout(animate, 500);
            } else {
                this.stopAnimation();
            }
        };
        
        animate();
    }
    
    stopAnimation() {
        this.isAnimating = false;
        document.getElementById('start-animation').textContent = 'Start Animation';
        if (this.animationId) {
            clearTimeout(this.animationId);
            this.animationId = null;
        }
    }
    
    reset() {
        this.stopAnimation();
        this.currentX = parseFloat(this.startPointSlider.value);
        this.iteration = 0;
        this.history = [];
        this.draw();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new SingleVarGradientDescent();
});
</script>


## Gradient Descent Method for Multivariables function

Gradient descent starts from an initial point $$x^{(0)} \in \mathbb{R}^n$$ and iteratively updates as follows until a stopping criterion is met:
> $$x^{(k)} = x^{(k-1)} - t_k \nabla f(x^{(k-1)}), \quad k = 1, 2, 3, ...$$, $$t_k > 0$$

Pseudocode:
> **Given a starting point** $$x \in dom(f)$$ <br>
> **Repeat**  <br>
> 1. Determine descent direction $$\Delta x = -\nabla f(x)$$. <br>
> 2. Line search: choose step size $$t > 0$$. <br>
> 3. Update $$x = x + t \Delta x$$. <br>
> **Until** stopping criterion is satisfied <br>

### Examples

The figure below shows gradient descent on a convex function. In this case, the local minimum is also the global minimum.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_01_gradientdescent1.png" alt="gradientdescent1" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig 1] Gradient descent in convex functions[3]</figcaption>
</p>
</figure>

The next figure shows gradient descent on a non-convex function. Here, the initial point determines which local minimum is reached.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_01_gradientdescent2.png" alt="gradientdescent2" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig 2] Gradient descent in non-convex functions[3]</figcaption>
</p>
</figure>

## Gradient Descent Interpretation
Gradient descent can be interpreted as choosing the next point by minimizing a quadratic approximation of the function.

For a function $$f$$, the second-order Taylor expansion around $$x$$ is:
>$$f(y) \approx f(x) + \nabla f(x)^T (y - x) +  \frac{1}{2} \nabla^2 f(x)  \|y - x\|_2^2$$

If we approximate the Hessian $$\nabla^2 f(x)$$ by $$\frac{1}{t}I$$, then:
>$$f(y) \approx f(x) + \nabla f(x)^T (y - x) +  \frac{1}{2t}  \|y - x\|_2^2$$
where $$t$$ is the step size.

Thus, in gradient descent, the function is approximated by a quadratic function whose Hessian matrix has eigenvalues equal to the reciprocal of the step size. The term $$f(x) + \nabla f(x)^T (y - x)$$ represents a linear approximation of $$f$$, and $$\frac{1}{2t}  \|y - x\|_2^2$$ serves as a proximity term indicating how close $$y$$ is to $$x$$.

The next position is chosen as the minimum of this approximated quadratic function. Setting the gradient of $$f(y)$$ to zero to find the next position $$y = x^+$$ leads to:

> $$x^+ = x - t \nabla f(x)$$

In the illustration below, the blue dot represents the current position $$x$$, and the red dot represents the next position $$y$$. The curve below is the actual function $$f$$, and the curve above is the quadratic approximation of $$f$$. Hence, the red dot indicates the minimum of the quadratic approximation.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_01_gradientdescent3.png" alt="gradientdescent3" width="80%" height="80%">
  <figcaption style="text-align: center;">$$ \text{[Fig 3] Gradient descent algorithm : red dot is } x^+ \text{ and blue dot } x \text{ [3]} $$</figcaption>
</p>
</figure>

The proximity of the next position $$y$$ to the current position $$x$$ is influenced by the weight of the proximity term $$\frac{1}{2t}$$. A smaller $$t$$ results in a larger weight for the proximity term, leading to smaller steps. This process can be expressed as:

> \begin{align}
x^+ = \underset{y}{\arg \min} \ f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \parallel y - x \parallel_2^2
\end{align}

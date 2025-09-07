---
layout: post
title: 06-06 Gradient descent with momentum
chapter: '06'
order: 15
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
lesson_type: required
---

<script src="https://d3js.org/d3.v7.min.js"></script>

## The Problem with Vanilla Gradient Descent

Imagine you're rolling a ball down a valley. Standard gradient descent is like a ball with no memory - at each step, it only considers the current slope and moves accordingly. This can lead to several problems:

1. **Slow convergence in ravines**: When the function has steep gradients in some directions and shallow gradients in others
2. **Oscillations**: The algorithm may zigzag back and forth across the valley instead of making steady progress
3. **Getting stuck in poor local minima**: Without momentum, the algorithm may settle in suboptimal solutions

**Question**: What if our ball could "remember" its previous direction and maintain some velocity?

## Momentum: Adding Memory to Gradient Descent

Gradient descent with momentum is inspired by physics - specifically, the motion of a ball rolling down a hill with friction. The key insight is to accumulate a velocity vector that combines the current gradient with the previous momentum.

### The Momentum Algorithm

**Update rules:**
$$ \begin{align}
v^{(k)} &= \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align} $$

where:
- $$v^{(k)}$$ is the momentum (velocity) at iteration $$k$$
- $$\beta \in [0,1)$$ is the momentum coefficient (typically 0.9 or 0.99)
- $$t > 0$$ is the learning rate
- $$v^{(0)} = 0$$ (initial velocity is zero)

### Alternative Formulation (Nesterov-style)

Some implementations use a slightly different form:
$$ \begin{align}
v^{(k)} &= \beta v^{(k-1)} + \nabla f(x^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align} $$

**Key insight**: The momentum term $$v^{(k)}$$ is an exponentially weighted moving average of past gradients.

## Understanding the Momentum Coefficient $$\beta$$

The momentum coefficient $$\beta$$ controls how much "memory" the algorithm has:

- **$$\beta = 0$$**: No momentum, reduces to standard gradient descent
- **$$\beta = 0.9$$**: Moderate momentum, commonly used in practice
- **$$\beta = 0.99$$**: High momentum, used in some deep learning applications
- **$$\beta \to 1$$**: Maximum momentum, but may cause instability

### Exponentially Weighted Moving Average

The momentum $$v^{(k)}$$ can be expanded as:
$$ v^{(k)} = (1-\beta) \sum_{i=0}^{k-1} \beta^i \nabla f(x^{(k-1-i)}) $$

This shows that momentum gives exponentially decreasing weights to older gradients.

## Interactive Visualization: Gradient Descent vs Momentum

<div id="momentum-comparison" style="margin: 20px 0;">
    <!-- Parameter Controls -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <div>
            <label for="momentum-lr">Learning Rate: </label>
            <input type="range" id="momentum-lr" min="0.01" max="0.3" step="0.01" value="0.1">
            <span id="momentum-lr-value">0.1</span>
        </div>
        <div>
            <label for="momentum-beta">Momentum (β): </label>
            <input type="range" id="momentum-beta" min="0" max="0.99" step="0.01" value="0.9">
            <span id="momentum-beta-value">0.9</span>
        </div>
        <div>
            <label for="momentum-speed">Animation Speed: </label>
            <input type="range" id="momentum-speed" min="1" max="10" step="1" value="5">
            <span id="momentum-speed-value">5</span>
        </div>
    </div>
    
    <!-- Control Buttons -->
    <div style="display: flex; gap: 10px; margin-bottom: 15px; flex-wrap: wrap;">
        <button id="start-vanilla-gd" style="background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Start Vanilla GD</button>
        <button id="start-momentum-gd" style="background-color: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Start Momentum GD</button>
        <button id="start-both" style="background-color: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Compare Both</button>
        <button id="reset-momentum" style="background-color: #f44336; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Reset</button>
    </div>
    
    <!-- Visualization Canvas -->
    <div id="momentum-canvas" style="border: 1px solid #ccc; border-radius: 5px; background-color: white; position: relative; overflow: hidden;">
        <svg width="800" height="500" id="momentum-svg"></svg>
    </div>
    
    <!-- Algorithm Status -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
        <div style="padding: 10px; border: 1px solid #4CAF50; border-radius: 5px; background-color: #f1f8e9;">
            <h4 style="margin: 0 0 5px 0; color: #4CAF50;">Vanilla Gradient Descent</h4>
            <p id="vanilla-gd-info" style="margin: 0; font-size: 14px;">Ready to start</p>
        </div>
        <div style="padding: 10px; border: 1px solid #FF9800; border-radius: 5px; background-color: #fff8e1;">
            <h4 style="margin: 0 0 5px 0; color: #FF9800;">Momentum Gradient Descent</h4>
            <p id="momentum-gd-info" style="margin: 0; font-size: 14px;">Ready to start</p>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Momentum visualization implementation
    const svg = d3.select("#momentum-svg");
    const width = 800, height = 500;
    const margin = {top: 20, right: 20, bottom: 40, left: 40};
    
    // Function to optimize: f(x,y) = 0.5*x^2 + 5*y^2 (elongated bowl)
    function f(x, y) {
        return 0.5 * x * x + 5 * y * y;
    }
    
    function gradient(x, y) {
        return [x, 10 * y];
    }
    
    // Scale setup
    const xScale = d3.scaleLinear()
        .domain([-6, 6])
        .range([margin.left, width - margin.right]);
    
    const yScale = d3.scaleLinear()
        .domain([-3, 3])
        .range([height - margin.bottom, margin.top]);
    
    // Create contour plot
    function createContours() {
        // Create a simple grid-based contour visualization
        const gridSize = 20;
        const contourLevels = [1, 4, 9, 16, 25, 36, 49];
        
        svg.selectAll(".contour").remove();
        
        // Draw contour ellipses for the function f(x,y) = 0.5*x^2 + 5*y^2
        contourLevels.forEach(level => {
            // For f(x,y) = 0.5*x^2 + 5*y^2 = level
            // This is an ellipse: x^2/(2*level) + y^2/(level/5) = 1
            const a = Math.sqrt(2 * level); // semi-major axis in x direction
            const b = Math.sqrt(level / 5); // semi-minor axis in y direction
            
            if (a <= 6 && b <= 3) { // Only draw if within our domain
                svg.append("ellipse")
                    .attr("class", "contour")
                    .attr("cx", xScale(0))
                    .attr("cy", yScale(0))
                    .attr("rx", xScale(a) - xScale(0))
                    .attr("ry", yScale(0) - yScale(b))
                    .attr("fill", "none")
                    .attr("stroke", "#ddd")
                    .attr("stroke-width", 1)
                    .attr("opacity", 0.6);
            }
        });
    }
    
    createContours();
    
    // Add global minimum marker
    svg.append("circle")
        .attr("cx", xScale(0))
        .attr("cy", yScale(0))
        .attr("r", 8)
        .attr("fill", "red")
        .attr("stroke", "white")
        .attr("stroke-width", 2)
        .attr("opacity", 0.8);
    
    svg.append("text")
        .attr("x", xScale(0))
        .attr("y", yScale(0) - 15)
        .attr("text-anchor", "middle")
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .attr("fill", "red")
        .text("Global Minimum");
    
    // Add axes
    svg.append("g")
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(xScale));
    
    svg.append("g")
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(yScale));
    
    // Add axis labels
    svg.append("text")
        .attr("x", width / 2)
        .attr("y", height - 5)
        .attr("text-anchor", "middle")
        .attr("font-size", "14px")
        .text("x");
    
    svg.append("text")
        .attr("x", 15)
        .attr("y", height / 2)
        .attr("text-anchor", "middle")
        .attr("font-size", "14px")
        .attr("transform", `rotate(-90, 15, ${height / 2})`)
        .text("y");
    
    // Add title
    svg.append("text")
        .attr("x", width / 2)
        .attr("y", 15)
        .attr("text-anchor", "middle")
        .attr("font-size", "16px")
        .attr("font-weight", "bold")
        .text("f(x,y) = 0.5x² + 5y² - Optimization Paths Comparison");
    
    // Variables for animation
    let vanillaPath = [], momentumPath = [];
    let vanillaRunning = false, momentumRunning = false;
    let vanillaInterval, momentumInterval;
    
    // Algorithm implementations
    function runVanillaGD() {
        const lr = parseFloat(document.getElementById('momentum-lr').value);
        let x = -4, y = 2; // Starting point
        let iteration = 0;
        const maxIterations = 500;
        vanillaPath = [{x: x, y: y}];
        vanillaRunning = true;
        
        vanillaInterval = setInterval(() => {
            const grad = gradient(x, y);
            x -= lr * grad[0];
            y -= lr * grad[1];
            vanillaPath.push({x: x, y: y});
            iteration++;
            
            updateVisualization();
            updateStatus();
            
            // Stop if converged or max iterations reached
            if ((Math.abs(grad[0]) < 0.01 && Math.abs(grad[1]) < 0.01) || iteration >= maxIterations) {
                clearInterval(vanillaInterval);
                vanillaRunning = false;
            }
        }, 1000 / parseFloat(document.getElementById('momentum-speed').value));
    }
    
    function runMomentumGD() {
        const lr = parseFloat(document.getElementById('momentum-lr').value);
        const beta = parseFloat(document.getElementById('momentum-beta').value);
        let x = -4, y = 2; // Starting point
        let vx = 0, vy = 0; // Initial velocity
        let iteration = 0;
        const maxIterations = 500;
        momentumPath = [{x: x, y: y}];
        momentumRunning = true;
        
        momentumInterval = setInterval(() => {
            const grad = gradient(x, y);
            vx = beta * vx + (1 - beta) * grad[0];
            vy = beta * vy + (1 - beta) * grad[1];
            x -= lr * vx;
            y -= lr * vy;
            momentumPath.push({x: x, y: y});
            iteration++;
            
            updateVisualization();
            updateStatus();
            
            // Stop if converged or max iterations reached
            if ((Math.abs(grad[0]) < 0.01 && Math.abs(grad[1]) < 0.01) || iteration >= maxIterations) {
                clearInterval(momentumInterval);
                momentumRunning = false;
            }
        }, 1000 / parseFloat(document.getElementById('momentum-speed').value));
    }
    
    function updateVisualization() {
        // Remove existing paths
        svg.selectAll(".vanilla-path").remove();
        svg.selectAll(".momentum-path").remove();
        svg.selectAll(".vanilla-point").remove();
        svg.selectAll(".momentum-point").remove();
        
        // Draw vanilla GD path
        if (vanillaPath.length > 1) {
            const line = d3.line()
                .x(d => xScale(d.x))
                .y(d => yScale(d.y));
            
            svg.append("path")
                .datum(vanillaPath)
                .attr("class", "vanilla-path")
                .attr("d", line)
                .attr("fill", "none")
                .attr("stroke", "#4CAF50")
                .attr("stroke-width", 2);
            
            // Current point
            const current = vanillaPath[vanillaPath.length - 1];
            svg.append("circle")
                .attr("class", "vanilla-point")
                .attr("cx", xScale(current.x))
                .attr("cy", yScale(current.y))
                .attr("r", 5)
                .attr("fill", "#4CAF50");
        }
        
        // Draw momentum GD path
        if (momentumPath.length > 1) {
            const line = d3.line()
                .x(d => xScale(d.x))
                .y(d => yScale(d.y));
            
            svg.append("path")
                .datum(momentumPath)
                .attr("class", "momentum-path")
                .attr("d", line)
                .attr("fill", "none")
                .attr("stroke", "#FF9800")
                .attr("stroke-width", 2);
            
            // Current point
            const current = momentumPath[momentumPath.length - 1];
            svg.append("circle")
                .attr("class", "momentum-point")
                .attr("cx", xScale(current.x))
                .attr("cy", yScale(current.y))
                .attr("r", 5)
                .attr("fill", "#FF9800");
        }
    }
    
    function updateStatus() {
        // Update vanilla GD status
        if (vanillaPath.length > 0) {
            const current = vanillaPath[vanillaPath.length - 1];
            const fValue = f(current.x, current.y);
            document.getElementById('vanilla-gd-info').innerHTML = 
                `Iteration: ${vanillaPath.length - 1}<br>Position: (${current.x.toFixed(3)}, ${current.y.toFixed(3)})<br>f(x,y): ${fValue.toFixed(4)}`;
        }
        
        // Update momentum GD status
        if (momentumPath.length > 0) {
            const current = momentumPath[momentumPath.length - 1];
            const fValue = f(current.x, current.y);
            document.getElementById('momentum-gd-info').innerHTML = 
                `Iteration: ${momentumPath.length - 1}<br>Position: (${current.x.toFixed(3)}, ${current.y.toFixed(3)})<br>f(x,y): ${fValue.toFixed(4)}`;
        }
    }
    
    // Event listeners
    document.getElementById('start-vanilla-gd').addEventListener('click', () => {
        if (!vanillaRunning) {
            vanillaRunning = true;
            runVanillaGD();
        }
    });
    
    document.getElementById('start-momentum-gd').addEventListener('click', () => {
        if (!momentumRunning) {
            momentumRunning = true;
            runMomentumGD();
        }
    });
    
    document.getElementById('start-both').addEventListener('click', () => {
        if (!vanillaRunning && !momentumRunning) {
            vanillaRunning = true;
            momentumRunning = true;
            runVanillaGD();
            runMomentumGD();
        }
    });
    
    document.getElementById('reset-momentum').addEventListener('click', () => {
        clearInterval(vanillaInterval);
        clearInterval(momentumInterval);
        vanillaRunning = false;
        momentumRunning = false;
        vanillaPath = [];
        momentumPath = [];
        updateVisualization();
        document.getElementById('vanilla-gd-info').innerHTML = 'Ready to start';
        document.getElementById('momentum-gd-info').innerHTML = 'Ready to start';
    });
    
    // Update display values
    document.getElementById('momentum-lr').addEventListener('input', function() {
        document.getElementById('momentum-lr-value').textContent = this.value;
    });
    
    document.getElementById('momentum-beta').addEventListener('input', function() {
        document.getElementById('momentum-beta-value').textContent = this.value;
    });
    
    document.getElementById('momentum-speed').addEventListener('input', function() {
        document.getElementById('momentum-speed-value').textContent = this.value;
    });
});
</script>

## Advantages of Momentum

### 1. **Faster Convergence**
Momentum helps the algorithm build up speed in consistent directions, leading to faster convergence especially in:
- Functions with valleys or ravines
- Ill-conditioned problems (high condition number)
- Functions with many local minima

### 2. **Reduced Oscillations**
In directions where the gradient changes sign frequently, momentum helps smooth out the oscillations by averaging past gradients.

### 3. **Escape from Local Minima**
The accumulated momentum can help the algorithm "roll through" small local minima and continue toward better solutions.

## Variants and Extensions

### 1. **Nesterov Accelerated Gradient (NAG)**
Instead of computing the gradient at the current position, NAG computes it at the "look-ahead" position:

$$ \begin{align}
v^{(k)} &= \beta v^{(k-1)} + \nabla f(x^{(k-1)} - \beta v^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align} $$

**Intuition**: "Look before you leap" - check the gradient at where momentum would take you.

#### The Problem with Regular Momentum

While momentum helps the ball overcome local minima, there's a limitation we can observe: when approaching the target, momentum still takes considerable time before stopping. The reason is precisely because of the accumulated velocity.

#### The Key Insight

The fundamental idea is to **predict the future direction** - essentially looking ahead one step! Specifically, if we use the momentum term $$\beta v^{(k-1)}$$ for updating, we can approximate the next position as $$x^{(k-1)} - \beta v^{(k-1)}$$ (we don't include the gradient term here as we'll use it in the final step).

Instead of using the gradient at the current position, NAG takes a step forward and uses the gradient at the anticipated next position.

#### Visual Comparison

**With regular momentum**: The update is the sum of two vectors:
- Momentum vector (from previous step)
- Gradient at the current position

**With Nesterov momentum**: The update is the sum of two vectors:
- Momentum vector (from previous step)  
- Gradient at the **look-ahead** position (where momentum would take us)

This "look-ahead" approach allows NAG to make more informed corrections and often leads to faster convergence.

### 2. **Adaptive Moment Estimation (Adam)**
Adam combines momentum with adaptive learning rates for each parameter:

$$ \begin{align}
m^{(k)} &= \beta_1 m^{(k-1)} + (1-\beta_1) \nabla f(x^{(k-1)}) \\
v^{(k)} &= \beta_2 v^{(k-1)} + (1-\beta_2) (\nabla f(x^{(k-1)}))^2 \\
x^{(k)} &= x^{(k-1)} - t \frac{m^{(k)}}{\sqrt{v^{(k)}} + \epsilon}
\end{align} $$

## Practical Implementation Tips

### 1. **Choosing the Momentum Coefficient**
- **Start with $$\beta = 0.9$$**: A good default for most problems
- **Increase to $$\beta = 0.99$$**: For very smooth optimization landscapes
- **Decrease to $$\beta = 0.5-0.7$$**: For noisy or non-smooth functions

### 2. **Learning Rate Adjustment**
When using momentum, you may need to reduce the learning rate compared to vanilla gradient descent, as momentum amplifies the effective step size.

### 3. **Warm-up Period**
Consider starting with lower momentum and gradually increasing it, as momentum needs time to build up effective velocity.

## Mathematical Analysis

### Convergence Properties

For strongly convex functions with Lipschitz gradients, momentum gradient descent achieves:
- **Linear convergence**: $$f(x^{(k)}) - f^* \leq C \rho^k$$ for some $$\rho < 1$$
- **Improved condition number**: Effective condition number can be improved from $$\kappa$$ to $$\sqrt{\kappa}$$

### Heavy Ball Method Connection

Momentum gradient descent is closely related to the heavy ball method from classical mechanics:
$$mx'' + \gamma x' + \nabla f(x) = 0$$

This differential equation, when discretized, leads to the momentum update rules.

## Comparison Summary

| Aspect | Vanilla GD | Momentum GD |
|--------|------------|-------------|
| **Memory** | No | Yes (exponential decay) |
| **Convergence** | Can be slow | Often faster |
| **Oscillations** | More prone | Reduced |
| **Local minima** | May get stuck | Better escape |
| **Hyperparameters** | Learning rate | Learning rate + momentum |
| **Computational cost** | Low | Slightly higher |

## Key Takeaways

1. **Momentum adds memory**: It remembers the direction of previous steps
2. **Faster convergence**: Especially effective for functions with valleys or ravines
3. **Reduced oscillations**: Smooths out zigzag behavior
4. **Widely used**: Foundation for many modern optimization algorithms
5. **Tunable**: The momentum coefficient $$\beta$$ allows fine-tuning for different problems

**Bottom line**: Momentum is a simple yet powerful enhancement to gradient descent that has stood the test of time and remains relevant in modern machine learning applications.

---
layout: post
title: 06-07 Regularization and Loss Functions
chapter: '06'
order: 16
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
lesson_type: required
---

<script src="../../../public/js/script.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>

## Introduction: The Overfitting Problem in Machine Learning

In machine learning, one of the biggest challenges is **overfitting** - when a model learns too much detail from training data, leading to poor performance on new data. **Regularization** is a crucial technique to address this problem.

### Why do we need Regularization?

Consider the basic linear regression problem:
$$\min_{\mathbf{w}} \frac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2$$

**Problem**: When the number of features is large or data is scarce, the model can find solutions with training error = 0 but poor generalization.

**Solution**: Add a **regularization term** to "penalize" large weights:
$$\min_{\mathbf{w}} \frac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda R(\mathbf{w})$$

where:
- $$\lambda > 0$$ is the **regularization parameter**
- $$R(\mathbf{w})$$ is the **regularization function**

## Ridge Regression (L2 Regularization)

### Mathematical Definition

Ridge regression uses the L2 norm as the regularization term:

$$\min_{\mathbf{w}} \frac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \frac{\lambda}{2} \|\mathbf{w}\|_2^2$$

**Component explanation:**
- **Loss term**: $$\frac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2$$ - measures deviation between predictions and actual values
- **Regularization term**: $$\frac{\lambda}{2} \|\mathbf{w}\|_2^2 = \frac{\lambda}{2} \sum_{j=1}^p w_j^2$$ - penalizes large weights
- **Regularization strength**: $$\lambda$$ controls the amount of regularization

### Analytical Solution

Ridge regression has a closed-form solution:
$$\mathbf{w}^* = (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$$

**Advantages of this solution:**
- The matrix $$(\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})$$ is always invertible when $$\lambda > 0$$
- Solves multicollinearity problems
- Computationally efficient

### Effects of Ridge Regularization

<div id="ridge-effect-demo" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <h4>Ridge Regularization Controls</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
            <div>
                <label for="ridge-lambda">Lambda (λ): </label>
                <input type="range" id="ridge-lambda" min="0" max="10" step="0.1" value="1">
                <span id="ridge-lambda-value">1.0</span>
            </div>
            <div>
                <label for="ridge-noise">Noise Level: </label>
                <input type="range" id="ridge-noise" min="0" max="0.5" step="0.05" value="0.1">
                <span id="ridge-noise-value">0.1</span>
            </div>
            <div>
                <label for="ridge-features">Number of Features: </label>
                <input type="range" id="ridge-features" min="5" max="20" step="1" value="10">
                <span id="ridge-features-value">10</span>
            </div>
        </div>
        <div style="margin-top: 10px;">
            <button id="ridge-regenerate" style="background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Generate New Data</button>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Coefficients Path</h4>
            <svg id="ridge-coefficients" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="ridge-coeff-info" style="margin: 0; font-size: 12px;">L2 Norm of coefficients: 0</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Training vs Validation Error</h4>
            <svg id="ridge-error" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="ridge-error-info" style="margin: 0; font-size: 12px;">Optimal λ: 0</p>
            </div>
        </div>
    </div>
</div>

## Lasso Regression (L1 Regularization)

### Mathematical Definition

Lasso (Least Absolute Shrinkage and Selection Operator) uses the L1 norm:

$$\min_{\mathbf{w}} \frac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \|\mathbf{w}\|_1$$

where $$\|\mathbf{w}\|_1 = \sum_{j=1}^p |w_j|$$

### Key Properties of Lasso

**1. Sparse Solutions:**
- Lasso can set some coefficients to **exactly zero**
- Automatically performs **feature selection**
- Creates simple, interpretable models

**2. No closed-form solution:**
- Requires optimization algorithms (coordinate descent, proximal gradient)
- More computationally complex than Ridge

### Ridge vs Lasso Comparison

<div id="ridge-lasso-comparison" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f0f8ff;">
        <h4>Ridge vs Lasso Regularization Comparison</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div>
                <label for="comparison-lambda">Lambda (λ): </label>
                <input type="range" id="comparison-lambda" min="0" max="5" step="0.1" value="1">
                <span id="comparison-lambda-value">1.0</span>
            </div>
            <div>
                <label for="comparison-correlation">Feature Correlation: </label>
                <input type="range" id="comparison-correlation" min="0" max="0.9" step="0.1" value="0.5">
                <span id="comparison-correlation-value">0.5</span>
            </div>
        </div>
        <div style="margin-top: 10px;">
            <button id="comparison-update" style="background-color: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Update Comparison</button>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Ridge Coefficients</h4>
            <svg id="ridge-comparison" width="300" height="250" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 5px; padding: 5px; background-color: #e8f5e8; border-radius: 4px;">
                <p style="margin: 0; font-size: 12px;">Shrinkage: Uniform, never zero</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Lasso Coefficients</h4>
            <svg id="lasso-comparison" width="300" height="250" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 5px; padding: 5px; background-color: #fff3e0; border-radius: 4px;">
                <p style="margin: 0; font-size: 12px;">Sparsity: Some exactly zero</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Regularization Geometry</h4>
            <svg id="regularization-geometry" width="300" height="250" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 5px; padding: 5px; background-color: #f3e5f5; border-radius: 4px;">
                <p style="margin: 0; font-size: 12px;">L1: Diamond, L2: Circle</p>
            </div>
        </div>
    </div>
</div>

### Geometry of Regularization

**Intuitive understanding of why Lasso creates sparse solutions:**

1. **L1 constraint**: $$\|\mathbf{w}\|_1 \leq t$$ creates a **diamond shape** in 2D
2. **L2 constraint**: $$\|\mathbf{w}\|_2 \leq t$$ creates a **circular shape** in 2D
3. **Intersection with loss contours**: 
   - L1: High probability of intersecting contours at corners (sparse solutions)
   - L2: Usually intersects at smooth points (non-sparse solutions)

## Elastic Net: Combining Ridge and Lasso

Elastic Net combines both L1 and L2 regularization:

$$\min_{\mathbf{w}} \frac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \left[ \alpha \|\mathbf{w}\|_1 + \frac{1-\alpha}{2} \|\mathbf{w}\|_2^2 \right]$$

**Parameters:**
- $$\alpha \in [0,1]$$: mixing parameter
- $$\alpha = 1$$: Pure Lasso
- $$\alpha = 0$$: Pure Ridge
- $$0 < \alpha < 1$$: Combination

**Advantages:**
- Combines Lasso's sparsity with Ridge's stability
- Handles grouped variables well
- Works well when $$p > n$$

## Loss Functions in Machine Learning

### 1. Regression Loss Functions

#### Mean Squared Error (MSE)
$$L_{MSE}(\mathbf{w}) = \frac{1}{n} \sum_{i=1}^n (y_i - \mathbf{w}^T \mathbf{x}_i)^2$$

**Properties:**
- Smooth, differentiable everywhere
- Sensitive to outliers
- Convex optimization problem

#### Mean Absolute Error (MAE)
$$L_{MAE}(\mathbf{w}) = \frac{1}{n} \sum_{i=1}^n |y_i - \mathbf{w}^T \mathbf{x}_i|$$

**Properties:**
- Robust to outliers
- Non-differentiable at zero
- Convex but requires subgradient methods

#### Huber Loss
$$L_{Huber}(\mathbf{w}) = \frac{1}{n} \sum_{i=1}^n \begin{cases}
\frac{1}{2}(y_i - \mathbf{w}^T \mathbf{x}_i)^2 & \text{if } |y_i - \mathbf{w}^T \mathbf{x}_i| \leq \delta \\
\delta |y_i - \mathbf{w}^T \mathbf{x}_i| - \frac{1}{2}\delta^2 & \text{otherwise}
\end{cases}$$

**Properties:**
- Combines MSE (small errors) and MAE (large errors)
- Smooth and robust
- Parameter $$\delta$$ controls transition point

### 2. Classification Loss Functions

#### Logistic Loss (Cross-entropy)
$$L_{logistic}(\mathbf{w}) = \frac{1}{n} \sum_{i=1}^n \log(1 + \exp(-y_i \mathbf{w}^T \mathbf{x}_i))$$

#### Hinge Loss (SVM)
$$L_{hinge}(\mathbf{w}) = \frac{1}{n} \sum_{i=1}^n \max(0, 1 - y_i \mathbf{w}^T \mathbf{x}_i)$$

### Interactive Loss Functions Comparison

<div id="loss-functions-demo" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <h4>Loss Functions Comparison</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
            <div>
                <label for="loss-delta">Huber Delta (δ): </label>
                <input type="range" id="loss-delta" min="0.5" max="3" step="0.1" value="1">
                <span id="loss-delta-value">1.0</span>
            </div>
            <div>
                <label for="loss-range">Error Range: </label>
                <input type="range" id="loss-range" min="2" max="8" step="0.5" value="4">
                <span id="loss-range-value">4.0</span>
            </div>
            <div>
                <label>
                    <input type="checkbox" id="show-derivatives"> Show Derivatives
                </label>
            </div>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Regression Loss Functions</h4>
            <svg id="regression-losses" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <div style="display: flex; gap: 15px; justify-content: center; font-size: 12px;">
                    <span style="color: #1f77b4;">■ MSE</span>
                    <span style="color: #ff7f0e;">■ MAE</span>
                    <span style="color: #2ca02c;">■ Huber</span>
                </div>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Classification Loss Functions</h4>
            <svg id="classification-losses" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <div style="display: flex; gap: 15px; justify-content: center; font-size: 12px;">
                    <span style="color: #d62728;">■ Logistic</span>
                    <span style="color: #9467bd;">■ Hinge</span>
                    <span style="color: #8c564b;">■ 0-1 Loss</span>
                </div>
            </div>
        </div>
    </div>
</div>

## Regularization Path and Model Selection

### Cross-Validation for Regularization

Choosing optimal $$\lambda$$ is typically done through cross-validation:

1. **Split data**: Training, validation, test sets
2. **Grid search**: Try multiple $$\lambda$$ values
3. **Evaluate**: Compute validation error for each $$\lambda$$
4. **Select**: Choose $$\lambda$$ with lowest validation error

### Regularization Path Visualization

<div id="regularization-path-demo" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f0f8ff;">
        <h4>Regularization Path Analysis</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
            <div>
                <label for="path-method">Method: </label>
                <select id="path-method">
                    <option value="ridge">Ridge</option>
                    <option value="lasso">Lasso</option>
                    <option value="elastic">Elastic Net</option>
                </select>
            </div>
            <div>
                <label for="path-alpha">Elastic Net α: </label>
                <input type="range" id="path-alpha" min="0" max="1" step="0.1" value="0.5">
                <span id="path-alpha-value">0.5</span>
            </div>
            <div>
                <button id="path-animate" style="background-color: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Animate Path</button>
            </div>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Coefficient Path</h4>
            <svg id="coefficient-path" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="path-info" style="margin: 0; font-size: 12px;">Current λ: 0, Active features: 0</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Cross-Validation Curve</h4>
            <svg id="cv-curve" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="cv-info" style="margin: 0; font-size: 12px;">Optimal λ: 0, CV Score: 0</p>
            </div>
        </div>
    </div>
</div>

## Practical Guidelines and Best Practices

### 1. When to use Ridge vs Lasso?

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
    <div style="border: 1px solid #4CAF50; padding: 15px; border-radius: 5px; background-color: #f1f8e9;">
        <h4 style="color: #4CAF50;">Use Ridge when:</h4>
        <ul>
            <li>All features are meaningful</li>
            <li>High multicollinearity</li>
            <li>Need stability in predictions</li>
            <li>Small dataset, many features</li>
            <li>Don't need automatic feature selection</li>
        </ul>
    </div>
    <div style="border: 1px solid #FF9800; padding: 15px; border-radius: 5px; background-color: #fff8e1;">
        <h4 style="color: #FF9800;">Use Lasso when:</h4>
        <ul>
            <li>Need automatic feature selection</li>
            <li>Many irrelevant features</li>
            <li>Want simple, interpretable models</li>
            <li>Sparse solutions are preferred</li>
            <li>High-dimensional data</li>
        </ul>
    </div>
</div>

### 2. Hyperparameter Tuning Strategy

```python
# Pseudo-code for regularization tuning
def tune_regularization(X_train, y_train, X_val, y_val):
    lambda_values = np.logspace(-4, 2, 50)  # Log-spaced values
    best_lambda = None
    best_score = float('inf')
    
    for lambda_val in lambda_values:
        model = fit_regularized_model(X_train, y_train, lambda_val)
        val_score = evaluate_model(model, X_val, y_val)
        
        if val_score < best_score:
            best_score = val_score
            best_lambda = lambda_val
    
    return best_lambda, best_score
```

### 3. Feature Scaling

**Important**: Regularization is sensitive to feature scales!

- **Ridge/Lasso**: Require feature scaling (standardization)
- **Reason**: Regularization penalty depends on coefficient magnitudes
- **Solution**: Standardize features before applying regularization

## Conclusion and Takeaways

### Key Points:

1. **Regularization** is a powerful tool to prevent overfitting
2. **Ridge (L2)** creates smooth shrinkage, good for stability
3. **Lasso (L1)** creates sparse solutions, good for feature selection
4. **Elastic Net** combines advantages of both
5. **Loss function choice** greatly affects model behavior
6. **Cross-validation** is key for hyperparameter tuning

### Practical Workflow:

1. **Data preprocessing**: Scale features appropriately
2. **Method selection**: Choose based on problem characteristics
3. **Hyperparameter tuning**: Use cross-validation
4. **Model evaluation**: Test on held-out data
5. **Interpretation**: Analyze coefficient patterns

**Remember**: Regularization is not a magic bullet - understanding your data and problem domain is still most important!

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Ridge Effect Demo
    initializeRidgeEffectDemo();
    
    // Ridge vs Lasso Comparison
    initializeRidgeLassoComparison();
    
    // Loss Functions Demo
    initializeLossFunctionsDemo();
    
    // Regularization Path Demo
    initializeRegularizationPathDemo();
    
    function initializeRidgeEffectDemo() {
        const lambdaSlider = document.getElementById('ridge-lambda');
        const noiseSlider = document.getElementById('ridge-noise');
        const featuresSlider = document.getElementById('ridge-features');
        const regenerateBtn = document.getElementById('ridge-regenerate');
        
        let currentData = generateRidgeData();
        
        function generateRidgeData() {
            const n = 50; // samples
            const p = parseInt(featuresSlider.value); // features
            const noise = parseFloat(noiseSlider.value);
            
            // Generate true coefficients (sparse)
            const trueCoeffs = Array(p).fill(0).map((_, i) => 
                i < 3 ? (Math.random() - 0.5) * 4 : 0
            );
            
            // Generate X matrix
            const X = Array(n).fill().map(() => 
                Array(p).fill().map(() => Math.random() * 2 - 1)
            );
            
            // Generate y with noise
            const y = X.map(row => 
                row.reduce((sum, x, i) => sum + x * trueCoeffs[i], 0) + 
                (Math.random() - 0.5) * noise * 2
            );
            
            return { X, y, trueCoeffs, n, p };
        }
        
        function updateRidgeDemo() {
            const lambda = parseFloat(lambdaSlider.value);
            document.getElementById('ridge-lambda-value').textContent = lambda.toFixed(1);
            
            // Compute Ridge coefficients for different lambda values
            const lambdaRange = Array(50).fill().map((_, i) => i * 0.2);
            const coeffPaths = computeRidgeCoefficients(currentData, lambdaRange);
            
            // Update visualizations
            updateRidgeCoefficientsPlot(coeffPaths, lambdaRange, lambda);
            updateRidgeErrorPlot(currentData, lambdaRange);
        }
        
        function computeRidgeCoefficients(data, lambdaRange) {
            const { X, y, p } = data;
            const paths = Array(p).fill().map(() => []);
            
            lambdaRange.forEach(lambda => {
                const coeffs = solveRidge(X, y, lambda);
                coeffs.forEach((coeff, i) => paths[i].push(coeff));
            });
            
            return paths;
        }
        
        function solveRidge(X, y, lambda) {
            // Simplified Ridge solution: w = (X'X + λI)^(-1) X'y
            const p = X[0].length;
            const n = X.length;
            
            // Compute X'X
            const XtX = Array(p).fill().map(() => Array(p).fill(0));
            for (let i = 0; i < p; i++) {
                for (let j = 0; j < p; j++) {
                    for (let k = 0; k < n; k++) {
                        XtX[i][j] += X[k][i] * X[k][j];
                    }
                }
            }
            
            // Add λI
            for (let i = 0; i < p; i++) {
                XtX[i][i] += lambda;
            }
            
            // Compute X'y
            const Xty = Array(p).fill(0);
            for (let i = 0; i < p; i++) {
                for (let k = 0; k < n; k++) {
                    Xty[i] += X[k][i] * y[k];
                }
            }
            
            // Solve linear system (simplified - using pseudo-inverse)
            return solveLinearSystem(XtX, Xty);
        }
        
        function solveLinearSystem(A, b) {
            // Simplified solution using Gaussian elimination
            const n = A.length;
            const coeffs = Array(n).fill(0);
            
            // For demo purposes, use a simplified approach
            for (let i = 0; i < n; i++) {
                coeffs[i] = b[i] / (A[i][i] + 1e-10);
            }
            
            return coeffs;
        }
        
        function updateRidgeCoefficientsPlot(coeffPaths, lambdaRange, currentLambda) {
            const svg = d3.select('#ridge-coefficients');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain(d3.extent(lambdaRange))
                .range([0, width]);
            
            const allCoeffs = coeffPaths.flat();
            const yScale = d3.scaleLinear()
                .domain(d3.extent(allCoeffs))
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Lambda (λ)');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Coefficient Value');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(lambdaRange[i]))
                .y(d => yScale(d));
            
            // Draw coefficient paths
            const colors = d3.schemeCategory10;
            coeffPaths.forEach((path, i) => {
                g.append('path')
                    .datum(path)
                    .attr('fill', 'none')
                    .attr('stroke', colors[i % colors.length])
                    .attr('stroke-width', 2)
                    .attr('d', line);
            });
            
            // Current lambda line
            g.append('line')
                .attr('x1', xScale(currentLambda))
                .attr('x2', xScale(currentLambda))
                .attr('y1', 0)
                .attr('y2', height)
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            // Update info
            const currentIndex = Math.round(currentLambda / 0.2);
            const currentCoeffs = coeffPaths.map(path => path[currentIndex] || 0);
            const l2Norm = Math.sqrt(currentCoeffs.reduce((sum, c) => sum + c*c, 0));
            document.getElementById('ridge-coeff-info').textContent = 
                `L2 Norm of coefficients: ${l2Norm.toFixed(3)}`;
        }
        
        function updateRidgeErrorPlot(data, lambdaRange) {
            // Simplified error computation for demo
            const svg = d3.select('#ridge-error');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Generate synthetic error curves
            const trainErrors = lambdaRange.map(lambda => 
                0.1 + 0.5 * lambda + Math.random() * 0.1
            );
            const valErrors = lambdaRange.map(lambda => 
                0.3 + 0.2 * Math.abs(lambda - 2) + Math.random() * 0.1
            );
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain(d3.extent(lambdaRange))
                .range([0, width]);
            
            const yScale = d3.scaleLinear()
                .domain([0, Math.max(...trainErrors, ...valErrors)])
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Lambda (λ)');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Error');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(lambdaRange[i]))
                .y(d => yScale(d));
            
            // Draw error curves
            g.append('path')
                .datum(trainErrors)
                .attr('fill', 'none')
                .attr('stroke', 'blue')
                .attr('stroke-width', 2)
                .attr('d', line);
            
            g.append('path')
                .datum(valErrors)
                .attr('fill', 'none')
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('d', line);
            
            // Legend
            const legend = g.append('g')
                .attr('transform', `translate(${width - 100}, 20)`);
            
            legend.append('line')
                .attr('x1', 0).attr('x2', 20)
                .attr('y1', 0).attr('y2', 0)
                .attr('stroke', 'blue').attr('stroke-width', 2);
            legend.append('text')
                .attr('x', 25).attr('y', 5)
                .text('Training');
            
            legend.append('line')
                .attr('x1', 0).attr('x2', 20)
                .attr('y1', 15).attr('y2', 15)
                .attr('stroke', 'red').attr('stroke-width', 2);
            legend.append('text')
                .attr('x', 25).attr('y', 20)
                .text('Validation');
            
            // Find optimal lambda
            const optimalIndex = valErrors.indexOf(Math.min(...valErrors));
            const optimalLambda = lambdaRange[optimalIndex];
            document.getElementById('ridge-error-info').textContent = 
                `Optimal λ: ${optimalLambda.toFixed(2)}`;
        }
        
        // Event listeners
        lambdaSlider.addEventListener('input', updateRidgeDemo);
        noiseSlider.addEventListener('input', function() {
            document.getElementById('ridge-noise-value').textContent = this.value;
        });
        featuresSlider.addEventListener('input', function() {
            document.getElementById('ridge-features-value').textContent = this.value;
        });
        
        regenerateBtn.addEventListener('click', function() {
            currentData = generateRidgeData();
            updateRidgeDemo();
        });
        
        // Initial update
        updateRidgeDemo();
    }
    
    function initializeRidgeLassoComparison() {
        const lambdaSlider = document.getElementById('comparison-lambda');
        const correlationSlider = document.getElementById('comparison-correlation');
        const updateBtn = document.getElementById('comparison-update');
        
        function updateComparison() {
            const lambda = parseFloat(lambdaSlider.value);
            const correlation = parseFloat(correlationSlider.value);
            
            document.getElementById('comparison-lambda-value').textContent = lambda.toFixed(1);
            document.getElementById('comparison-correlation-value').textContent = correlation.toFixed(1);
            
            // Generate synthetic data with controlled correlation
            const p = 8; // features
            const trueCoeffs = [2, -1.5, 1, 0.5, -0.8, 0, 0, 0];
            
            // Compute Ridge and Lasso coefficients
            const ridgeCoeffs = computeRidgeCoeffs(trueCoeffs, lambda, correlation);
            const lassoCoeffs = computeLassoCoeffs(trueCoeffs, lambda, correlation);
            
            // Update visualizations
            updateComparisonPlot('ridge-comparison', ridgeCoeffs, 'Ridge');
            updateComparisonPlot('lasso-comparison', lassoCoeffs, 'Lasso');
            updateGeometryPlot(lambda);
        }
        
        function computeRidgeCoeffs(trueCoeffs, lambda, correlation) {
            // Simplified Ridge shrinkage
            const shrinkageFactor = 1 / (1 + lambda);
            return trueCoeffs.map(coeff => coeff * shrinkageFactor);
        }
        
        function computeLassoCoeffs(trueCoeffs, lambda, correlation) {
            // Simplified Lasso soft thresholding
            return trueCoeffs.map(coeff => {
                const absCoeff = Math.abs(coeff);
                if (absCoeff <= lambda) return 0;
                return Math.sign(coeff) * (absCoeff - lambda);
            });
        }
        
        function updateComparisonPlot(svgId, coeffs, title) {
            const svg = d3.select(`#${svgId}`);
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 40};
            const width = 300 - margin.left - margin.right;
            const height = 250 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Scales
            const xScale = d3.scaleBand()
                .domain(coeffs.map((_, i) => `w${i+1}`))
                .range([0, width])
                .padding(0.1);
            
            const yScale = d3.scaleLinear()
                .domain(d3.extent(coeffs))
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Bars
            const color = title === 'Ridge' ? '#4CAF50' : '#FF9800';
            g.selectAll('.bar')
                .data(coeffs)
                .enter().append('rect')
                .attr('class', 'bar')
                .attr('x', (d, i) => xScale(`w${i+1}`))
                .attr('width', xScale.bandwidth())
                .attr('y', d => d >= 0 ? yScale(d) : yScale(0))
                .attr('height', d => Math.abs(yScale(d) - yScale(0)))
                .attr('fill', color);
            
            // Zero line
            g.append('line')
                .attr('x1', 0)
                .attr('x2', width)
                .attr('y1', yScale(0))
                .attr('y2', yScale(0))
                .attr('stroke', 'black')
                .attr('stroke-width', 1);
        }
        
        function updateGeometryPlot(lambda) {
            const svg = d3.select('#regularization-geometry');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 40};
            const width = 300 - margin.left - margin.right;
            const height = 250 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            const centerX = width / 2;
            const centerY = height / 2;
            const radius = Math.min(width, height) / 3;
            
            // L2 constraint (circle)
            g.append('circle')
                .attr('cx', centerX)
                .attr('cy', centerY)
                .attr('r', radius)
                .attr('fill', 'none')
                .attr('stroke', '#4CAF50')
                .attr('stroke-width', 3)
                .attr('opacity', 0.7);
            
            // L1 constraint (diamond)
            const diamondPoints = [
                [centerX, centerY - radius],
                [centerX + radius, centerY],
                [centerX, centerY + radius],
                [centerX - radius, centerY]
            ];
            
            const line = d3.line()
                .x(d => d[0])
                .y(d => d[1]);
            
            g.append('path')
                .datum([...diamondPoints, diamondPoints[0]])
                .attr('d', line)
                .attr('fill', 'none')
                .attr('stroke', '#FF9800')
                .attr('stroke-width', 3)
                .attr('opacity', 0.7);
            
            // Contour lines (ellipses)
            for (let i = 1; i <= 3; i++) {
                g.append('ellipse')
                    .attr('cx', centerX + 20)
                    .attr('cy', centerY - 10)
                    .attr('rx', i * 15)
                    .attr('ry', i * 25)
                    .attr('fill', 'none')
                    .attr('stroke', '#666')
                    .attr('stroke-width', 1)
                    .attr('stroke-dasharray', '3,3')
                    .attr('opacity', 0.5);
            }
            
            // Labels
            g.append('text')
                .attr('x', centerX + radius + 10)
                .attr('y', centerY + 5)
                .text('L2')
                .attr('fill', '#4CAF50')
                .attr('font-weight', 'bold');
            
            g.append('text')
                .attr('x', centerX + radius/Math.sqrt(2) + 5)
                .attr('y', centerY - radius/Math.sqrt(2) - 5)
                .text('L1')
                .attr('fill', '#FF9800')
                .attr('font-weight', 'bold');
        }
        
        // Event listeners
        lambdaSlider.addEventListener('input', updateComparison);
        correlationSlider.addEventListener('input', updateComparison);
        updateBtn.addEventListener('click', updateComparison);
        
        // Initial update
        updateComparison();
    }
    
    function initializeLossFunctionsDemo() {
        const deltaSlider = document.getElementById('loss-delta');
        const rangeSlider = document.getElementById('loss-range');
        const derivativesCheckbox = document.getElementById('show-derivatives');
        
        function updateLossFunctions() {
            const delta = parseFloat(deltaSlider.value);
            const range = parseFloat(rangeSlider.value);
            const showDerivatives = derivativesCheckbox.checked;
            
            document.getElementById('loss-delta-value').textContent = delta.toFixed(1);
            document.getElementById('loss-range-value').textContent = range.toFixed(1);
            
            updateRegressionLosses(delta, range, showDerivatives);
            updateClassificationLosses(range, showDerivatives);
        }
        
        function updateRegressionLosses(delta, range, showDerivatives) {
            const svg = d3.select('#regression-losses');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Generate error values
            const errors = d3.range(-range, range, 0.1);
            
            // Loss functions
            const mseLoss = errors.map(e => 0.5 * e * e);
            const maeLoss = errors.map(e => Math.abs(e));
            const huberLoss = errors.map(e => 
                Math.abs(e) <= delta ? 0.5 * e * e : delta * Math.abs(e) - 0.5 * delta * delta
            );
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain([-range, range])
                .range([0, width]);
            
            const maxLoss = Math.max(...mseLoss, ...maeLoss, ...huberLoss);
            const yScale = d3.scaleLinear()
                .domain([0, maxLoss])
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Prediction Error');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Loss');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(errors[i]))
                .y(d => yScale(d));
            
            // Draw loss functions
            const colors = ['#1f77b4', '#ff7f0e', '#2ca02c'];
            const losses = [mseLoss, maeLoss, huberLoss];
            const names = ['MSE', 'MAE', 'Huber'];
            
            losses.forEach((loss, i) => {
                g.append('path')
                    .datum(loss)
                    .attr('fill', 'none')
                    .attr('stroke', colors[i])
                    .attr('stroke-width', 3)
                    .attr('d', line);
            });
            
            // Legend
            const legend = g.append('g')
                .attr('transform', `translate(${width - 80}, 20)`);
            
            names.forEach((name, i) => {
                legend.append('line')
                    .attr('x1', 0).attr('x2', 20)
                    .attr('y1', i * 20).attr('y2', i * 20)
                    .attr('stroke', colors[i]).attr('stroke-width', 3);
                legend.append('text')
                    .attr('x', 25).attr('y', i * 20 + 5)
                    .text(name);
            });
        }
        
        function updateClassificationLosses(range, showDerivatives) {
            const svg = d3.select('#classification-losses');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Generate margin values (y * f(x))
            const margins = d3.range(-range, range, 0.1);
            
            // Loss functions
            const logisticLoss = margins.map(m => Math.log(1 + Math.exp(-m)));
            const hingeLoss = margins.map(m => Math.max(0, 1 - m));
            const zeroOneLoss = margins.map(m => m <= 0 ? 1 : 0);
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain([-range, range])
                .range([0, width]);
            
            const maxLoss = Math.max(...logisticLoss, ...hingeLoss, ...zeroOneLoss);
            const yScale = d3.scaleLinear()
                .domain([0, maxLoss])
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Margin (y × f(x))');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Loss');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(margins[i]))
                .y(d => yScale(d));
            
            // Draw loss functions
            const colors = ['#d62728', '#9467bd', '#8c564b'];
            const losses = [logisticLoss, hingeLoss, zeroOneLoss];
            const names = ['Logistic', 'Hinge', '0-1 Loss'];
            
            losses.forEach((loss, i) => {
                g.append('path')
                    .datum(loss)
                    .attr('fill', 'none')
                    .attr('stroke', colors[i])
                    .attr('stroke-width', 3)
                    .attr('d', line);
            });
            
            // Legend
            const legend = g.append('g')
                .attr('transform', `translate(${width - 80}, 20)`);
            
            names.forEach((name, i) => {
                legend.append('line')
                    .attr('x1', 0).attr('x2', 20)
                    .attr('y1', i * 20).attr('y2', i * 20)
                    .attr('stroke', colors[i]).attr('stroke-width', 3);
                legend.append('text')
                    .attr('x', 25).attr('y', i * 20 + 5)
                    .text(name);
            });
        }
        
        // Event listeners
        deltaSlider.addEventListener('input', updateLossFunctions);
        rangeSlider.addEventListener('input', updateLossFunctions);
        derivativesCheckbox.addEventListener('change', updateLossFunctions);
        
        // Initial update
        updateLossFunctions();
    }
    
    function initializeRegularizationPathDemo() {
        const methodSelect = document.getElementById('path-method');
        const alphaSlider = document.getElementById('path-alpha');
        const animateBtn = document.getElementById('path-animate');
        
        let isAnimating = false;
        let animationId = null;
        
        function updateRegularizationPath() {
            const method = methodSelect.value;
            const alpha = parseFloat(alphaSlider.value);
            
            document.getElementById('path-alpha-value').textContent = alpha.toFixed(1);
            
            // Generate regularization path
            const lambdaRange = d3.range(0, 5, 0.1);
            const coeffPaths = generateRegularizationPath(method, alpha, lambdaRange);
            
            updateCoefficientPathPlot(coeffPaths, lambdaRange, method);
            updateCVCurvePlot(lambdaRange, method);
        }
        
        function generateRegularizationPath(method, alpha, lambdaRange) {
            const p = 6; // features
            const trueCoeffs = [2, -1.5, 1, 0.5, -0.8, 0.3];
            
            const paths = Array(p).fill().map(() => []);
            
            lambdaRange.forEach(lambda => {
                let coeffs;
                if (method === 'ridge') {
                    coeffs = trueCoeffs.map(c => c / (1 + lambda));
                } else if (method === 'lasso') {
                    coeffs = trueCoeffs.map(c => {
                        const abs_c = Math.abs(c);
                        return abs_c > lambda ? Math.sign(c) * (abs_c - lambda) : 0;
                    });
                } else { // elastic net
                    coeffs = trueCoeffs.map(c => {
                        const abs_c = Math.abs(c);
                        const l1_part = abs_c > alpha * lambda ? Math.sign(c) * (abs_c - alpha * lambda) : 0;
                        return l1_part / (1 + (1 - alpha) * lambda);
                    });
                }
                
                coeffs.forEach((coeff, i) => paths[i].push(coeff));
            });
            
            return paths;
        }
        
        function updateCoefficientPathPlot(coeffPaths, lambdaRange, method) {
            const svg = d3.select('#coefficient-path');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain(d3.extent(lambdaRange))
                .range([0, width]);
            
            const allCoeffs = coeffPaths.flat();
            const yScale = d3.scaleLinear()
                .domain(d3.extent(allCoeffs))
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Lambda (λ)');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Coefficient Value');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(lambdaRange[i]))
                .y(d => yScale(d));
            
            // Draw coefficient paths
            const colors = d3.schemeCategory10;
            coeffPaths.forEach((path, i) => {
                g.append('path')
                    .datum(path)
                    .attr('fill', 'none')
                    .attr('stroke', colors[i % colors.length])
                    .attr('stroke-width', 2)
                    .attr('d', line);
                
                // Add feature label at the end
                const lastValue = path[path.length - 1];
                if (Math.abs(lastValue) > 0.01) {
                    g.append('text')
                        .attr('x', width + 5)
                        .attr('y', yScale(lastValue) + 3)
                        .attr('font-size', '10px')
                        .text(`f${i+1}`);
                }
            });
            
            // Update info
            const currentLambda = 1.0; // example
            const activeFeatures = coeffPaths.filter(path => Math.abs(path[Math.floor(currentLambda * 10)]) > 0.01).length;
            document.getElementById('path-info').textContent = 
                `Current λ: ${currentLambda.toFixed(1)}, Active features: ${activeFeatures}`;
        }
        
        function updateCVCurvePlot(lambdaRange, method) {
            const svg = d3.select('#cv-curve');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Generate synthetic CV scores
            const cvScores = lambdaRange.map(lambda => {
                const base = 0.2 + 0.1 * Math.abs(lambda - 1.5);
                return base + (Math.random() - 0.5) * 0.05;
            });
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain(d3.extent(lambdaRange))
                .range([0, width]);
            
            const yScale = d3.scaleLinear()
                .domain(d3.extent(cvScores))
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Lambda (λ)');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('CV Score');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(lambdaRange[i]))
                .y(d => yScale(d));
            
            // Draw CV curve
            g.append('path')
                .datum(cvScores)
                .attr('fill', 'none')
                .attr('stroke', '#2196F3')
                .attr('stroke-width', 3)
                .attr('d', line);
            
            // Find and mark optimal lambda
            const minIndex = cvScores.indexOf(Math.min(...cvScores));
            const optimalLambda = lambdaRange[minIndex];
            
            g.append('circle')
                .attr('cx', xScale(optimalLambda))
                .attr('cy', yScale(cvScores[minIndex]))
                .attr('r', 5)
                .attr('fill', 'red');
            
            // Update info
            document.getElementById('cv-info').textContent = 
                `Optimal λ: ${optimalLambda.toFixed(2)}, CV Score: ${cvScores[minIndex].toFixed(3)}`;
        }
        
        function animatePath() {
            if (isAnimating) {
                // Stop animation
                isAnimating = false;
                if (animationId) clearInterval(animationId);
                animateBtn.textContent = 'Animate Path';
                return;
            }
            
            // Start animation
            isAnimating = true;
            animateBtn.textContent = 'Stop Animation';
            
            const lambdaRange = d3.range(0, 5, 0.1);
            let currentIndex = 0;
            
            animationId = setInterval(() => {
                if (currentIndex >= lambdaRange.length) {
                    currentIndex = 0;
                }
                
                // Update visualization for current lambda
                const currentLambda = lambdaRange[currentIndex];
                // Add animation logic here
                
                currentIndex++;
            }, 100);
        }
        
        // Event listeners
        methodSelect.addEventListener('change', updateRegularizationPath);
        alphaSlider.addEventListener('input', updateRegularizationPath);
        animateBtn.addEventListener('click', animatePath);
        
        // Initial update
        updateRegularizationPath();
    }
});
</script>

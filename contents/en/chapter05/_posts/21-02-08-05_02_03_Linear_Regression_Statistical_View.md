---
layout: post
title: 05-02-03 Linear Regression from Statistical Perspective
chapter: '05'
order: 10
owner: AI Assistant
categories:
- chapter05
lang: en
---

## Linear Regression from Statistical Perspective

In this lesson, we explore linear regression from a probabilistic and statistical viewpoint, demonstrating why minimizing the sum of squared errors (MSE) is not only intuitive but also theoretically justified through maximum likelihood estimation.

### 1. Probabilistic Interpretation of Linear Regression

From a probabilistic perspective, we can prove that the estimates obtained from linear regression based on minimizing the sum of squared errors from the MSE function are completely natural and reasonable.

Indeed, we assume that the target variable and input variables are related through the equation:

$$y_i = \mathbf{w}^\top \mathbf{x}_i + \epsilon_i$$

where $\epsilon_i$ represents the random error that any equation has. These are factors that cannot be explained by the model. Since our estimate is unbiased, this random error is assumed to satisfy the properties according to the Gauss-Markov hypothesis:

#### Assumption 1: Zero Mean Error
The errors $\epsilon_i$ are random variables with zero expectation:

$$\mathbb{E}(\epsilon_i) = 0$$

#### Assumption 2: Uncorrelated Errors
The random errors have no correlation:

$$\mathbb{E}(\epsilon_i \epsilon_j) = 0, \quad \forall i \neq j$$

#### Assumption 3: Constant Variance (Homoscedasticity)
The variance of the random error is invariant:

$$\text{Var}(\epsilon_i) = \sigma^2$$

#### Assumption 4: Independence of Errors and Features
The random error $\epsilon_i$ and the input variables $\mathbf{x}_i$ have no correlation:

$$\text{Cov}(\mathbf{x}_i, \epsilon_i) = 0, \quad \forall i = 1, \dots, p$$

### 2. Gaussian Distribution of Errors

Under these assumptions, the random errors $\epsilon_i$ form a Gaussian (normal) distribution with mean 0 and variance $\sigma^2$, denoted as $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$. The probability density function at each point $\epsilon_i$ is:

$$p(\epsilon_i) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right)$$

Substituting $\epsilon_i = y_i - \mathbf{w}^\top \mathbf{x}_i$ into the probability density function, we get:

$$p(y_i \mid \mathbf{x}_i; \mathbf{w}) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{(y_i - \mathbf{w}^\top \mathbf{x}_i)^2}{2\sigma^2} \right)$$

The notation $p(y_i \mid \mathbf{x}_i; \mathbf{w})$ indicates the probability of $y_i$ corresponding to $\mathbf{x}_i$, parameterized by $\mathbf{w}$. Here, $\mathbf{w}$ is known and is not considered as a condition of $y_i$, hence we use ; instead of ,.

### 3. Maximum Likelihood Estimation

From a probabilistic perspective, $p(y_i \mid \mathbf{x}_i; \mathbf{w})$ is a function dependent on the input data $\mathbf{x}_i$ when the weight $\mathbf{w}$ is known. When viewing probability from the perspective of a function with respect to $\mathbf{w}$, we call it the likelihood function:

$$L(\mathbf{w}) = L(\mathbf{w}; \mathbf{X}, \mathbf{y}) = p(\mathbf{y} \mid \mathbf{X}; \mathbf{w})$$

According to condition 2 of the Gauss-Markov hypothesis, the errors are independent, so the joint probability of the data equals the product of the probability densities of each data point:

$$\begin{align}
L(\mathbf{w}) &= \prod_{i=1}^{n} p(y_i \mid \mathbf{x}_i; \mathbf{w}) \\
&= \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right)
\end{align}$$

The likelihood function reflects the probabilistic relationship between $\mathbf{y}$ and $\mathbf{X}$. To find $\mathbf{w}$ such that this relationship is most appropriate, according to Maximum Likelihood Estimation, we choose $\mathbf{w}$ such that $L(\mathbf{w})$ is maximized.

### 4. Log-Likelihood Optimization

Taking the logarithm of both sides to simplify the optimization problem:

$$\begin{align}
\hat{\mathbf{w}} &= \arg \max \log L(\mathbf{w}) \\
&= \arg \max \log \left[ \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right) \right] \\
&= \arg \max \sum_{i=1}^{n} \log \left[ \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right) \right] \\
&= \arg \max \sum_{i=1}^{n} \left[ -\frac{\epsilon_i^2}{2\sigma^2} - \log \sqrt{2\pi \sigma^2} \right] \\
&= \arg \max \left[ -\frac{1}{2\sigma^2} \sum_{i=1}^{n} \epsilon_i^2 - n \log \sqrt{2\pi \sigma^2} \right]
\end{align}$$

Since $\sigma^2$ and $2\pi$ are constants, optimizing the above function is equivalent to minimizing:

$$\sum_{i=1}^{n} \epsilon_i^2 = \sum_{i=1}^{n} (y_i - \mathbf{w}^\top \mathbf{x}_i)^2$$

This is equivalent to minimizing the MSE function:

$$\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

### 5. Theoretical Justification

Thus, from a probabilistic perspective, we have proven that linear regression based on minimizing the sum of squared errors is equivalent to optimizing the likelihood function. When the conditions of the Gauss-Markov hypothesis are satisfied, our estimate is the best linear unbiased estimator (BLUE). Assumptions about confidence intervals for predicted values and evaluation of the significance of weights through P-values can be made based on the normal distribution.

<div id="mle-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f9f9f9;">
    <h4 style="text-align: center; color: #333;">Maximum Likelihood Estimation Visualization</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <!-- Canvas for visualization -->
        <div style="flex: 1; min-width: 400px;">
            <canvas id="mleCanvas" width="400" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            <p style="font-size: 12px; color: #666; margin-top: 5px;">
                <strong>Visualization:</strong> Blue dots are data points, red line is the fitted line, and the curves show the Gaussian distributions of errors.
            </p>
        </div>
        
        <!-- Controls -->
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Parameters</h5>
                
                <div style="margin-bottom: 15px;">
                    <label for="noise-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">Noise Level (σ): <span id="noise-value">0.5</span></label>
                    <input type="range" id="noise-slider" min="0.1" max="2" step="0.1" value="0.5" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="slope-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">True Slope: <span id="true-slope-value">1.0</span></label>
                    <input type="range" id="slope-slider" min="-2" max="3" step="0.1" value="1.0" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="intercept-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">True Intercept: <span id="true-intercept-value">0.0</span></label>
                    <input type="range" id="intercept-slider" min="-2" max="2" step="0.1" value="0.0" style="width: 100%;">
                </div>
                
                <button id="generate-data" style="width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; margin-bottom: 10px;">Generate New Data</button>
                
                <div id="mle-results" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>MLE Estimates:</strong></div>
                    <div>Slope: <span id="mle-slope">0.000</span></div>
                    <div>Intercept: <span id="mle-intercept">0.000</span></div>
                    <div>Log-Likelihood: <span id="log-likelihood">0.000</span></div>
                </div>
            </div>
        </div>
    </div>
</div>

### 6. Training Linear Regression Models with sklearn

Sklearn is a comprehensive Python library for data science, supporting training of most machine learning models, building pipelines, data normalization, and performing cross-validation.

In this section, we will learn how to train linear regression models on sklearn. Returning to the previous problem, if we add information about distance to city center:

$$\mathbf{x}_2 = [20, 18, 17, 16, 15, 14, 12, 10, 8, 7, 5, 2, 1]$$

then the problem becomes multivariate regression. The process of building and training the model includes the steps:

1. Data collection
2. Data cleaning
3. Feature selection
4. Data normalization
5. Train/test split
6. Model training and evaluation

In this problem, we focus on step 6 to understand how to train the model.

<div id="sklearn-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f9f9f9;">
    <h4 style="text-align: center; color: #333;">Sklearn Linear Regression Example</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <!-- Code example -->
        <div style="flex: 1; min-width: 400px;">
            <pre style="background: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; font-size: 12px;"><code id="sklearn-code">import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Sample data: house prices
# Features: [area, distance_to_center]
X = np.array([
    [50, 20], [60, 18], [70, 17], [80, 16], [90, 15],
    [100, 14], [110, 12], [120, 10], [130, 8], [140, 7],
    [150, 5], [160, 2], [170, 1]
])

# Target: prices (in thousands)
y = np.array([150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.3f}")
</code></pre>
        </div>
        
        <!-- Interactive results -->
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Model Results</h5>
                
                <button id="run-sklearn" style="width: 100%; padding: 10px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; margin-bottom: 15px;">Run Sklearn Example</button>
                
                <div id="sklearn-results" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>Model Parameters:</strong></div>
                    <div>Area coeff: <span id="area-coeff">--</span></div>
                    <div>Distance coeff: <span id="distance-coeff">--</span></div>
                    <div>Intercept: <span id="sklearn-intercept">--</span></div>
                    <div><strong>Performance:</strong></div>
                    <div>MSE: <span id="sklearn-mse">--</span></div>
                    <div>R²: <span id="sklearn-r2">--</span></div>
                </div>
                
                <div style="margin-top: 15px;">
                    <h6 style="margin-bottom: 10px; color: #444;">Prediction Calculator</h6>
                    <div style="margin-bottom: 10px;">
                        <label style="display: block; margin-bottom: 5px;">Area (m²):</label>
                        <input type="number" id="pred-area" value="100" min="50" max="200" style="width: 100%; padding: 5px; border: 1px solid #ddd; border-radius: 3px;">
                    </div>
                    <div style="margin-bottom: 10px;">
                        <label style="display: block; margin-bottom: 5px;">Distance to center (km):</label>
                        <input type="number" id="pred-distance" value="10" min="1" max="20" style="width: 100%; padding: 5px; border: 1px solid #ddd; border-radius: 3px;">
                    </div>
                    <button id="make-prediction" style="width: 100%; padding: 8px; background: #17a2b8; color: white; border: none; border-radius: 3px; cursor: pointer;">Predict Price</button>
                    <div id="prediction-result" style="margin-top: 10px; padding: 10px; background: #e9ecef; border-radius: 3px; text-align: center; font-weight: bold;">
                        Predicted Price: --
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

### Key Insights

1. **Theoretical Foundation**: Maximum likelihood estimation provides a solid theoretical foundation for why we minimize squared errors in linear regression.

2. **Gaussian Assumptions**: The effectiveness of linear regression relies on the Gauss-Markov assumptions, particularly that errors are normally distributed.

3. **Best Linear Unbiased Estimator**: Under the right conditions, OLS provides the BLUE - the most efficient unbiased linear estimator.

4. **Practical Implementation**: Modern tools like sklearn make it easy to implement these theoretical concepts in practice.

5. **Model Evaluation**: Understanding the statistical foundation helps in proper model evaluation using metrics like R², confidence intervals, and p-values.

<script>
// MLE Visualization
class MLEVisualization {
    constructor() {
        this.canvas = document.getElementById('mleCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        // Parameters
        this.trueSlope = 1.0;
        this.trueIntercept = 0.0;
        this.noiseLevel = 0.5;
        this.dataPoints = [];
        
        this.setupControls();
        this.generateData();
        this.draw();
    }
    
    setupControls() {
        const noiseSlider = document.getElementById('noise-slider');
        const slopeSlider = document.getElementById('slope-slider');
        const interceptSlider = document.getElementById('intercept-slider');
        const generateBtn = document.getElementById('generate-data');
        
        noiseSlider.addEventListener('input', (e) => {
            this.noiseLevel = parseFloat(e.target.value);
            document.getElementById('noise-value').textContent = this.noiseLevel.toFixed(1);
            this.generateData();
            this.draw();
        });
        
        slopeSlider.addEventListener('input', (e) => {
            this.trueSlope = parseFloat(e.target.value);
            document.getElementById('true-slope-value').textContent = this.trueSlope.toFixed(1);
            this.generateData();
            this.draw();
        });
        
        interceptSlider.addEventListener('input', (e) => {
            this.trueIntercept = parseFloat(e.target.value);
            document.getElementById('true-intercept-value').textContent = this.trueIntercept.toFixed(1);
            this.generateData();
            this.draw();
        });
        
        generateBtn.addEventListener('click', () => {
            this.generateData();
            this.draw();
        });
    }
    
    generateData() {
        this.dataPoints = [];
        const n = 20;
        
        for (let i = 0; i < n; i++) {
            const x = (i / (n - 1)) * 4 - 2; // x from -2 to 2
            const trueY = this.trueSlope * x + this.trueIntercept;
            const noise = (Math.random() - 0.5) * 2 * this.noiseLevel;
            const y = trueY + noise;
            
            this.dataPoints.push({ x, y, trueY });
        }
    }
    
    calculateMLE() {
        const n = this.dataPoints.length;
        let sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
        
        for (const point of this.dataPoints) {
            sumX += point.x;
            sumY += point.y;
            sumXY += point.x * point.y;
            sumX2 += point.x * point.x;
        }
        
        const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
        const intercept = (sumY - slope * sumX) / n;
        
        // Calculate log-likelihood
        let logLikelihood = 0;
        for (const point of this.dataPoints) {
            const predicted = slope * point.x + intercept;
            const error = point.y - predicted;
            logLikelihood -= 0.5 * Math.log(2 * Math.PI * this.noiseLevel * this.noiseLevel);
            logLikelihood -= (error * error) / (2 * this.noiseLevel * this.noiseLevel);
        }
        
        return { slope, intercept, logLikelihood };
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        const mle = this.calculateMLE();
        
        // Update display
        document.getElementById('mle-slope').textContent = mle.slope.toFixed(3);
        document.getElementById('mle-intercept').textContent = mle.intercept.toFixed(3);
        document.getElementById('log-likelihood').textContent = mle.logLikelihood.toFixed(2);
        
        // Transform coordinates
        const transform = (x, y) => ({
            x: (x + 2.5) * this.width / 5,
            y: this.height - (y + 2.5) * this.height / 5
        });
        
        // Draw axes
        this.ctx.strokeStyle = '#ddd';
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.moveTo(0, this.height / 2);
        this.ctx.lineTo(this.width, this.height / 2);
        this.ctx.moveTo(this.width / 2, 0);
        this.ctx.lineTo(this.width / 2, this.height);
        this.ctx.stroke();
        
        // Draw fitted line
        this.ctx.strokeStyle = '#ff4444';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        const start = transform(-2, mle.slope * (-2) + mle.intercept);
        const end = transform(2, mle.slope * 2 + mle.intercept);
        this.ctx.moveTo(start.x, start.y);
        this.ctx.lineTo(end.x, end.y);
        this.ctx.stroke();
        
        // Draw data points and error distributions
        for (const point of this.dataPoints) {
            const pos = transform(point.x, point.y);
            
            // Draw Gaussian error distribution
            const predicted = mle.slope * point.x + mle.intercept;
            const errorCenter = transform(point.x, predicted);
            
            this.ctx.strokeStyle = '#cccccc';
            this.ctx.lineWidth = 1;
            this.ctx.beginPath();
            for (let i = 0; i <= 20; i++) {
                const t = i / 20;
                const gaussY = predicted + (t - 0.5) * 4 * this.noiseLevel;
                const gaussVal = Math.exp(-0.5 * Math.pow((gaussY - predicted) / this.noiseLevel, 2));
                const gaussPos = transform(point.x + gaussVal * 0.3, gaussY);
                
                if (i === 0) {
                    this.ctx.moveTo(gaussPos.x, gaussPos.y);
                } else {
                    this.ctx.lineTo(gaussPos.x, gaussPos.y);
                }
            }
            this.ctx.stroke();
            
            // Draw data point
            this.ctx.fillStyle = '#4444ff';
            this.ctx.beginPath();
            this.ctx.arc(pos.x, pos.y, 4, 0, 2 * Math.PI);
            this.ctx.fill();
            
            // Draw error line
            this.ctx.strokeStyle = '#888';
            this.ctx.lineWidth = 1;
            this.ctx.beginPath();
            this.ctx.moveTo(pos.x, pos.y);
            this.ctx.lineTo(errorCenter.x, errorCenter.y);
            this.ctx.stroke();
        }
    }
}

// Sklearn Demo
class SklearnDemo {
    constructor() {
        this.setupControls();
        this.model = null;
        this.data = this.generateSampleData();
    }
    
    generateSampleData() {
        return {
            X: [
                [50, 20], [60, 18], [70, 17], [80, 16], [90, 15],
                [100, 14], [110, 12], [120, 10], [130, 8], [140, 7],
                [150, 5], [160, 2], [170, 1]
            ],
            y: [150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510]
        };
    }
    
    setupControls() {
        const runBtn = document.getElementById('run-sklearn');
        const predBtn = document.getElementById('make-prediction');
        
        runBtn.addEventListener('click', () => this.runSklearnExample());
        predBtn.addEventListener('click', () => this.makePrediction());
    }
    
    runSklearnExample() {
        // Simulate sklearn linear regression
        const { X, y } = this.data;
        
        // Calculate means
        const meanX1 = X.reduce((sum, row) => sum + row[0], 0) / X.length;
        const meanX2 = X.reduce((sum, row) => sum + row[1], 0) / X.length;
        const meanY = y.reduce((sum, val) => sum + val, 0) / y.length;
        
        // Calculate coefficients using normal equation
        let sumX1X1 = 0, sumX2X2 = 0, sumX1X2 = 0;
        let sumX1Y = 0, sumX2Y = 0;
        
        for (let i = 0; i < X.length; i++) {
            const x1 = X[i][0] - meanX1;
            const x2 = X[i][1] - meanX2;
            const yVal = y[i] - meanY;
            
            sumX1X1 += x1 * x1;
            sumX2X2 += x2 * x2;
            sumX1X2 += x1 * x2;
            sumX1Y += x1 * yVal;
            sumX2Y += x2 * yVal;
        }
        
        // Solve 2x2 system
        const det = sumX1X1 * sumX2X2 - sumX1X2 * sumX1X2;
        const coeff1 = (sumX2X2 * sumX1Y - sumX1X2 * sumX2Y) / det;
        const coeff2 = (sumX1X1 * sumX2Y - sumX1X2 * sumX1Y) / det;
        const intercept = meanY - coeff1 * meanX1 - coeff2 * meanX2;
        
        // Calculate MSE and R²
        let mse = 0, tss = 0;
        for (let i = 0; i < X.length; i++) {
            const predicted = coeff1 * X[i][0] + coeff2 * X[i][1] + intercept;
            const error = y[i] - predicted;
            mse += error * error;
            tss += (y[i] - meanY) * (y[i] - meanY);
        }
        mse /= X.length;
        const r2 = 1 - (mse * X.length) / tss;
        
        this.model = { coeff1, coeff2, intercept };
        
        // Update display
        document.getElementById('area-coeff').textContent = coeff1.toFixed(3);
        document.getElementById('distance-coeff').textContent = coeff2.toFixed(3);
        document.getElementById('sklearn-intercept').textContent = intercept.toFixed(3);
        document.getElementById('sklearn-mse').textContent = mse.toFixed(2);
        document.getElementById('sklearn-r2').textContent = r2.toFixed(3);
    }
    
    makePrediction() {
        if (!this.model) {
            alert('Please run the sklearn example first!');
            return;
        }
        
        const area = parseFloat(document.getElementById('pred-area').value);
        const distance = parseFloat(document.getElementById('pred-distance').value);
        
        const prediction = this.model.coeff1 * area + this.model.coeff2 * distance + this.model.intercept;
        
        document.getElementById('prediction-result').innerHTML = 
            `Predicted Price: <strong>$${prediction.toFixed(0)}k</strong>`;
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new MLEVisualization();
    new SklearnDemo();
});
</script>

<style>
#mle-demo canvas {
    border-radius: 5px;
}

#sklearn-demo pre {
    max-height: 400px;
    overflow-y: auto;
}

.demo-container {
    margin: 20px 0;
}

input[type="range"] {
    -webkit-appearance: none;
    appearance: none;
    height: 5px;
    background: #ddd;
    outline: none;
    border-radius: 5px;
}

input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 15px;
    height: 15px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
}

input[type="range"]::-moz-range-thumb {
    width: 15px;
    height: 15px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    border: none;
}
</style>

---
layout: post
title: '00-04-03 Likelihood and Maximum Likelihood Estimation (MLE)'
chapter: '00'
order: 17
owner: AI Assistant
categories:
- chapter00
lang: en
lesson_type: required
---

## Likelihood and Maximum Likelihood Estimation

In probability and statistics, the **likelihood** is an important concept that expresses how plausible the observed data is under an assumed model or a given set of parameters. However, the likelihood is not an ordinary probability: it is a function that measures how well a model fits the data.

### Definition of Likelihood

The likelihood of a parameter $$\theta$$ (or of a model) is defined as the probability of the observed data, assuming the parameter $$\theta$$ is true. It is usually written $$L(\theta \mid x)$$, where $$x$$ is the observed data.

**Formula:**
$$L(\theta \mid x) = P(x \mid \theta)$$

Here, $$P(x \mid \theta)$$ is the probability of the data $$x$$ when the parameter $$\theta$$ is given.

### The Difference from Probability

- **Probability** describes how likely a future event is, with known parameters.
- **Likelihood**, conversely, measures how well different parameters fit data that has already been observed.

<div style="background: #fff3cd; padding: 15px; border-left: 4px solid #ffc107; margin: 20px 0;">
<strong>⚠️ Important note:</strong> The likelihood is not the probability of the parameter θ, because it is not normalized like a probability distribution (the integral of the likelihood does not have to equal 1).
</div>

### Illustrative Example: Flipping a Coin

Suppose you flip a coin and observe 3 "heads" (H) and 2 "tails" (T) in 5 flips. You want to know the probability $$p$$ of getting heads.

The likelihood of $$p$$ is the probability of observing the data (3 heads, 2 tails) when $$p$$ is given:

$$L(p \mid \text{data}) = P(\text{3 heads, 2 tails} \mid p) = \binom{5}{3} p^3 (1-p)^2$$

Where:
- $$\binom{5}{3}$$ is the binomial coefficient
- $$p^3$$ is the probability of 3 heads
- $$(1-p)^2$$ is the probability of 2 tails

**Trying different values:**

For $$p = 0.6$$:
$$L(0.6 \mid \text{data}) = \binom{5}{3} (0.6)^3 (0.4)^2 = 10 \times 0.216 \times 0.16 \approx 0.3456$$

For $$p = 0.5$$:
$$L(0.5 \mid \text{data}) = \binom{5}{3} (0.5)^3 (0.5)^2 = 10 \times 0.125 \times 0.25 \approx 0.3125$$

The higher likelihood at $$p = 0.6$$ shows that this value fits the observed data better than $$p = 0.5$$.

### Interactive Example: Flipping a Coin

<div id="coin-flip-example" style="border: 1px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 8px;">
    <h4>Coin Flip Experiment</h4>
    
    <div style="margin: 15px 0;">
        <label for="p-slider">Probability of heads (p): <span id="p-value">0.5</span></label><br>
        <input type="range" id="p-slider" min="0.01" max="0.99" step="0.01" value="0.5" style="width: 300px;">
    </div>
    
    <div style="margin: 15px 0;">
        <label for="heads-input">Number of heads: </label>
        <input type="number" id="heads-input" value="3" min="0" max="20" style="width: 60px;">
        
        <label for="tails-input" style="margin-left: 20px;">Number of tails: </label>
        <input type="number" id="tails-input" value="2" min="0" max="20" style="width: 60px;">
    </div>
    
    <div style="margin: 15px 0;">
        <canvas id="likelihood-plot" width="600" height="300" style="border: 1px solid #ccc;"></canvas>
    </div>
    
    <div id="likelihood-result" style="background: #f8f9fa; padding: 10px; border-radius: 4px; margin: 10px 0;">
        <strong>Current likelihood:</strong> <span id="current-likelihood">0.3125</span><br>
        <strong>Log-likelihood:</strong> <span id="current-log-likelihood">-1.16</span>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const pSlider = document.getElementById('p-slider');
    const pValue = document.getElementById('p-value');
    const headsInput = document.getElementById('heads-input');
    const tailsInput = document.getElementById('tails-input');
    const canvas = document.getElementById('likelihood-plot');
    const ctx = canvas.getContext('2d');
    const likelihoodResult = document.getElementById('current-likelihood');
    const logLikelihoodResult = document.getElementById('current-log-likelihood');
    
    function binomialCoeff(n, k) {
        if (k > n) return 0;
        if (k === 0 || k === n) return 1;
        
        let result = 1;
        for (let i = 0; i < k; i++) {
            result = result * (n - i) / (i + 1);
        }
        return result;
    }
    
    function likelihood(p, heads, tails) {
        const n = heads + tails;
        const coeff = binomialCoeff(n, heads);
        return coeff * Math.pow(p, heads) * Math.pow(1 - p, tails);
    }
    
    function logLikelihood(p, heads, tails) {
        const n = heads + tails;
        const logCoeff = Math.log(binomialCoeff(n, heads));
        return logCoeff + heads * Math.log(p) + tails * Math.log(1 - p);
    }
    
    function plotLikelihood() {
        const heads = parseInt(headsInput.value);
        const tails = parseInt(tailsInput.value);
        const currentP = parseFloat(pSlider.value);
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw axes
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(50, 250);
        ctx.lineTo(550, 250);
        ctx.moveTo(50, 250);
        ctx.lineTo(50, 50);
        ctx.stroke();
        
        // Axis labels
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('p (probability of heads)', 250, 280);
        ctx.save();
        ctx.translate(20, 150);
        ctx.rotate(-Math.PI/2);
        ctx.fillText('Likelihood', 0, 0);
        ctx.restore();
        
        // Draw the likelihood curve
        ctx.strokeStyle = '#2196F3';
        ctx.lineWidth = 2;
        ctx.beginPath();
        
        let maxLikelihood = 0;
        const points = [];
        
        for (let i = 0; i <= 500; i++) {
            const p = 0.01 + (i / 500) * 0.98;
            const l = likelihood(p, heads, tails);
            points.push({p: p, l: l});
            maxLikelihood = Math.max(maxLikelihood, l);
        }
        
        for (let i = 0; i < points.length; i++) {
            const x = 50 + (points[i].p - 0.01) / 0.98 * 500;
            const y = 250 - (points[i].l / maxLikelihood) * 200;
            
            if (i === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        ctx.stroke();
        
        // Draw the current point
        const currentLikelihood = likelihood(currentP, heads, tails);
        const currentX = 50 + (currentP - 0.01) / 0.98 * 500;
        const currentY = 250 - (currentLikelihood / maxLikelihood) * 200;
        
        ctx.fillStyle = '#f44336';
        ctx.beginPath();
        ctx.arc(currentX, currentY, 5, 0, 2 * Math.PI);
        ctx.fill();
        
        // Update results
        likelihoodResult.textContent = currentLikelihood.toFixed(6);
        logLikelihoodResult.textContent = logLikelihood(currentP, heads, tails).toFixed(4);
        
        // Draw tick marks
        ctx.fillStyle = '#666';
        ctx.font = '10px Arial';
        for (let i = 0; i <= 10; i++) {
            const p = i / 10;
            const x = 50 + (p - 0.01) / 0.98 * 500;
            ctx.fillText(p.toFixed(1), x - 10, 265);
        }
    }
    
    function updateDisplay() {
        pValue.textContent = pSlider.value;
        plotLikelihood();
    }
    
    pSlider.addEventListener('input', updateDisplay);
    headsInput.addEventListener('input', plotLikelihood);
    tailsInput.addEventListener('input', plotLikelihood);
    
    // Initialize
    updateDisplay();
});
</script>

### Maximum Likelihood Estimation (MLE)

**Maximum likelihood estimation** is the method of finding the value of the parameter $$\theta$$ for which the likelihood function $$L(\theta \mid x)$$ attains its largest value.

**MLE formula:**
$$\hat{\theta}_{MLE} = \arg\max_{\theta} L(\theta \mid x)$$

It is often easier to maximize the log-likelihood:
$$\hat{\theta}_{MLE} = \arg\max_{\theta} \log L(\theta \mid x)$$

### MLE Example: The Normal Distribution

Suppose we have $$n$$ independent observations $$x_1, x_2, \ldots, x_n$$ from a normal distribution $$N(\mu, \sigma^2)$$.

**Likelihood function:**
$$L(\mu, \sigma^2 \mid x_1, \ldots, x_n) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right)$$

**Log-likelihood:**
$$\ell(\mu, \sigma^2) = -\frac{n}{2}\log(2\pi) - \frac{n}{2}\log(\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i - \mu)^2$$

**MLE estimates:**

To find $$\hat{\mu}$$, differentiate with respect to $$\mu$$ and set the derivative to 0:
$$\frac{\partial \ell}{\partial \mu} = \frac{1}{\sigma^2}\sum_{i=1}^{n}(x_i - \mu) = 0$$

Solving gives: $$\hat{\mu}_{MLE} = \frac{1}{n}\sum_{i=1}^{n} x_i = \bar{x}$$

Similarly for $$\sigma^2$$:
$$\hat{\sigma^2}_{MLE} = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

### Interactive Example: MLE for the Normal Distribution

<div id="normal-mle-example" style="border: 1px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 8px;">
    <h4>MLE for the Normal Distribution</h4>
    
    <div style="margin: 15px 0;">
        <button id="generate-data" style="background: #4CAF50; color: white; padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer;">Generate New Data</button>
        <span style="margin-left: 20px;">Sample size: </span>
        <input type="number" id="sample-size" value="50" min="10" max="200" style="width: 60px;">
    </div>
    
    <div style="margin: 15px 0;">
        <label for="mu-guess">Estimate of μ: <span id="mu-guess-value">0</span></label><br>
        <input type="range" id="mu-guess" min="-3" max="3" step="0.1" value="0" style="width: 300px;">
    </div>
    
    <div style="margin: 15px 0;">
        <label for="sigma-guess">Estimate of σ: <span id="sigma-guess-value">1</span></label><br>
        <input type="range" id="sigma-guess" min="0.1" max="3" step="0.1" value="1" style="width: 300px;">
    </div>
    
    <div style="margin: 15px 0;">
        <canvas id="normal-plot" width="600" height="300" style="border: 1px solid #ccc;"></canvas>
    </div>
    
    <div id="mle-results" style="background: #f8f9fa; padding: 10px; border-radius: 4px; margin: 10px 0;">
        <div><strong>True data:</strong> μ = <span id="true-mu">1.0</span>, σ = <span id="true-sigma">1.5</span></div>
        <div><strong>MLE estimate:</strong> μ̂ = <span id="mle-mu">0.95</span>, σ̂ = <span id="mle-sigma">1.48</span></div>
        <div><strong>Current estimate:</strong> μ = <span id="current-mu">0</span>, σ = <span id="current-sigma">1</span></div>
        <div><strong>Current log-likelihood:</strong> <span id="current-ll">-75.2</span></div>
        <div><strong>Maximum log-likelihood:</strong> <span id="max-ll">-72.1</span></div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-data');
    const sampleSizeInput = document.getElementById('sample-size');
    const muGuess = document.getElementById('mu-guess');
    const sigmaGuess = document.getElementById('sigma-guess');
    const muGuessValue = document.getElementById('mu-guess-value');
    const sigmaGuessValue = document.getElementById('sigma-guess-value');
    const canvas = document.getElementById('normal-plot');
    const ctx = canvas.getContext('2d');
    
    let data = [];
    let trueMu = 1.0;
    let trueSigma = 1.5;
    
    function normalRandom(mu, sigma) {
        let u = 0, v = 0;
        while(u === 0) u = Math.random();
        while(v === 0) v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v) * sigma + mu;
    }
    
    function generateData() {
        const n = parseInt(sampleSizeInput.value);
        trueMu = (Math.random() - 0.5) * 4; // -2 to 2
        trueSigma = 0.5 + Math.random() * 2; // 0.5 to 2.5
        
        data = [];
        for (let i = 0; i < n; i++) {
            data.push(normalRandom(trueMu, trueSigma));
        }
        
        // Compute the MLE
        const mleMu = data.reduce((sum, x) => sum + x, 0) / data.length;
        const mleSigma = Math.sqrt(data.reduce((sum, x) => sum + (x - mleMu) ** 2, 0) / data.length);
        
        document.getElementById('true-mu').textContent = trueMu.toFixed(2);
        document.getElementById('true-sigma').textContent = trueSigma.toFixed(2);
        document.getElementById('mle-mu').textContent = mleMu.toFixed(2);
        document.getElementById('mle-sigma').textContent = mleSigma.toFixed(2);
        
        plotData();
    }
    
    function logLikelihood(mu, sigma, data) {
        const n = data.length;
        const sumSquares = data.reduce((sum, x) => sum + (x - mu) ** 2, 0);
        return -n/2 * Math.log(2 * Math.PI) - n * Math.log(sigma) - sumSquares / (2 * sigma ** 2);
    }
    
    function normalPDF(x, mu, sigma) {
        return (1 / (sigma * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * ((x - mu) / sigma) ** 2);
    }
    
    function plotData() {
        if (data.length === 0) return;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const currentMu = parseFloat(muGuess.value);
        const currentSigma = parseFloat(sigmaGuess.value);
        
        // Find the data range
        const minX = Math.min(...data) - 1;
        const maxX = Math.max(...data) + 1;
        const range = maxX - minX;
        
        // Draw the histogram
        const bins = 20;
        const binWidth = range / bins;
        const binCounts = new Array(bins).fill(0);
        
        data.forEach(x => {
            const binIndex = Math.floor((x - minX) / binWidth);
            if (binIndex >= 0 && binIndex < bins) {
                binCounts[binIndex]++;
            }
        });
        
        const maxCount = Math.max(...binCounts);
        
        ctx.fillStyle = 'rgba(33, 150, 243, 0.3)';
        for (let i = 0; i < bins; i++) {
            const x = 50 + (i * binWidth / range) * 500;
            const height = (binCounts[i] / maxCount) * 200;
            const width = (binWidth / range) * 500;
            ctx.fillRect(x, 250 - height, width, height);
        }
        
        // Draw the true distribution curve
        ctx.strokeStyle = '#4CAF50';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let i = 0; i <= 500; i++) {
            const x = minX + (i / 500) * range;
            const y = normalPDF(x, trueMu, trueSigma);
            const plotX = 50 + (i / 500) * 500;
            const plotY = 250 - (y / (1 / (trueSigma * Math.sqrt(2 * Math.PI)))) * 200;
            
            if (i === 0) ctx.moveTo(plotX, plotY);
            else ctx.lineTo(plotX, plotY);
        }
        ctx.stroke();
        
        // Draw the current estimate curve
        ctx.strokeStyle = '#f44336';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        for (let i = 0; i <= 500; i++) {
            const x = minX + (i / 500) * range;
            const y = normalPDF(x, currentMu, currentSigma);
            const plotX = 50 + (i / 500) * 500;
            const plotY = 250 - (y / (1 / (currentSigma * Math.sqrt(2 * Math.PI)))) * 200;
            
            if (i === 0) ctx.moveTo(plotX, plotY);
            else ctx.lineTo(plotX, plotY);
        }
        ctx.stroke();
        ctx.setLineDash([]);
        
        // Draw axes
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(50, 250);
        ctx.lineTo(550, 250);
        ctx.stroke();
        
        // Update results
        const currentLL = logLikelihood(currentMu, currentSigma, data);
        const mleMu = data.reduce((sum, x) => sum + x, 0) / data.length;
        const mleSigma = Math.sqrt(data.reduce((sum, x) => sum + (x - mleMu) ** 2, 0) / data.length);
        const maxLL = logLikelihood(mleMu, mleSigma, data);
        
        document.getElementById('current-mu').textContent = currentMu.toFixed(2);
        document.getElementById('current-sigma').textContent = currentSigma.toFixed(2);
        document.getElementById('current-ll').textContent = currentLL.toFixed(2);
        document.getElementById('max-ll').textContent = maxLL.toFixed(2);
        
        // Add the legend
        ctx.fillStyle = '#4CAF50';
        ctx.fillRect(450, 60, 15, 3);
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('True distribution', 470, 65);
        
        ctx.strokeStyle = '#f44336';
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(450, 80);
        ctx.lineTo(465, 80);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillText('Current estimate', 470, 85);
    }
    
    function updateDisplay() {
        muGuessValue.textContent = muGuess.value;
        sigmaGuessValue.textContent = sigmaGuess.value;
        plotData();
    }
    
    generateBtn.addEventListener('click', generateData);
    muGuess.addEventListener('input', updateDisplay);
    sigmaGuess.addEventListener('input', updateDisplay);
    sampleSizeInput.addEventListener('change', generateData);
    
    // Initialize
    generateData();
});
</script>

### Properties of the MLE

1. **Consistency**: As the sample size grows, the MLE converges to the true value of the parameter.

2. **Asymptotic Normality**: For large samples, the distribution of the MLE is approximately normal.

3. **Asymptotic Efficiency**: The MLE attains the Cramér-Rao bound, meaning it has the smallest variance among unbiased estimators.

4. **Invariance**: If $$\hat{\theta}$$ is the MLE of $$\theta$$, then $$g(\hat{\theta})$$ is the MLE of $$g(\theta)$$ for an invertible function $$g$$ (the property extends to any function $$g$$ through the induced likelihood).

### Applications of the MLE

#### 1. Parameter Estimation

The MLE is widely used to estimate parameters in statistical models:
- Normal distribution: estimating the mean and variance
- Poisson distribution: estimating the parameter λ
- Linear regression: estimating the regression coefficients

#### 2. Model Comparison

The likelihood is used to compare different statistical models:
- **Likelihood Ratio Test**: compares two nested models
- **AIC/BIC**: model selection criteria based on the likelihood

#### 3. Bayesian Statistics

In Bayesian statistics, the likelihood is combined with a prior distribution to compute the posterior distribution:

$$P(\theta \mid x) \propto L(\theta \mid x) \cdot P(\theta)$$

### Connection with Optimization

The MLE gives rise to an optimization problem:

$$\max_{\theta} L(\theta \mid x) \quad \text{or} \quad \max_{\theta} \log L(\theta \mid x)$$

This often leads to:
- **Unconstrained optimization**: when there are no constraints on the parameters
- **Constrained optimization**: when the parameters must satisfy certain conditions
- **Convex problems**: for many models the log-likelihood is concave (equivalently, the negative log-likelihood is convex), so maximizing it is a convex problem and guarantees a global optimum

<div style="background: #e8f4fd; padding: 15px; border-left: 4px solid #2196F3; margin: 20px 0;">
<strong>💡 Connection with Convex Optimization:</strong> Many MLE problems lead to convex optimization, especially for exponential families of distributions. This guarantees that the solution found is globally optimal and that optimization algorithms will converge to the true solution.
</div>

### A Real-World Example: Logistic Regression

In logistic regression, we model the probability of a binary variable:

$$P(y = 1 \mid x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x)}}$$

**Log-likelihood** (with $$p_i = P(y_i = 1 \mid x_i)$$):
$$\ell(\beta_0, \beta_1) = \sum_{i=1}^{n} \left[ y_i \log(p_i) + (1-y_i) \log(1-p_i) \right]$$

This is a concave maximization problem (equivalently, a convex minimization of the negative log-likelihood), which can be solved by gradient descent or Newton's method.

### Summary

- The **likelihood** measures how well a parameter fits the observed data
- The **MLE** finds the parameter that maximizes the likelihood
- The MLE has many good statistical properties: consistency, efficiency, asymptotic normality
- The MLE gives rise to optimization problems, many of which are convex
- Widely used in statistics, machine learning and data science

<div style="background: #d4edda; padding: 15px; border-left: 4px solid #28a745; margin: 20px 0;">
<strong>🎯 Key Point:</strong> The MLE is an important bridge between statistics and optimization. Understanding the MLE helps you grasp how statistical models are estimated through optimization methods, especially convex optimization.
</div>




---
layout: post
title: 00-04 Probability and Statistics
chapter: '00'
order: 14
owner: AI Assistant
categories:
- chapter00
lang: en
---

Real-world optimization rarely operates on noiseless, deterministic formulas: demand forecasts fluctuate, sensor readings carry Gaussian noise, and machine learning datasets are random samples from an unknown population. Probability and statistics supply the mathematical bridge from noisy observations to clean optimization objectives—turning parameter estimation, risk management, and stochastic approximation into convex problems we can solve with provable guarantees.

## Background Knowledge Map: Why Probability Sits Inside Modern Optimization

- **Random Variables & Expectation:** Expected loss $$\mathbb{E}[\ell(w; Z)]$$ is the true target of stochastic optimization; linearity of expectation lets us differentiate and average unbiased gradient estimates.
- **Loss Functions as Distributional Assumptions:** Minimizing squared error corresponds to Gaussian noise, minimizing $$\ell_1$$ error corresponds to Laplace noise, and cross-entropy corresponds to categorical log-likelihood.
- **Empirical Risk Minimization (ERM):** Replaces an unknown expectation with a finite sample average $$\frac{1}{n}\sum_{i=1}^n \ell(w; z_i)$$, yielding a concrete finite-sum optimization problem.
- **Concentration & Variance Control:** Variance bounds explain why mini-batching, variance reduction, and regularization stabilize noisy optimization trajectories.

### Step-by-Step Worked Example (Read Slowly): Sample Mean vs. Sample Median as Optimization Solutions

Given a small noisy dataset $$\{2, 4, 9\}$$, compare two 1D empirical risk minimization objectives for a location estimate $$\theta \in \mathbb{R}$$:

1. **Squared loss ($$\ell_2$$ ERM):**
   $$L_2(\theta) = \frac{1}{3}\left[(2 - \theta)^2 + (4 - \theta)^2 + (9 - \theta)^2\right].$$
   Differentiate and set to zero:
   $$L_2'(\theta) = \frac{2}{3}\left[(\theta - 2) + (\theta - 4) + (\theta - 9)\right] = \frac{2}{3}(3\theta - 15) = 0 \implies \hat{\theta}_2 = 5 \text{ (the sample mean)}.$$
2. **Absolute loss ($$\ell_1$$ ERM):**
   $$L_1(\theta) = |2 - \theta| + |4 - \theta| + |9 - \theta|.$$
   For $$\theta < 4$$ the slope is $$-1$$ (or $$-3$$ below $$2$$); for $$\theta > 4$$ the slope is $$+1$$ (or $$+3$$ above $$9$$). The slope flips sign at $$\hat{\theta}_1 = 4$$ (the sample median), where $$L_1(4) = 2 + 0 + 5 = 7$$ (compared to $$L_1(5) = 3 + 1 + 4 = 8$$).
3. **Takeaway:** Changing the noise model from Gaussian ($$\ell_2$$) to heavy-tailed Laplace ($$\ell_1$$) shifts the optimizer from $$5$$ to $$4$$, making the estimate resistant to the outlier $$9$$.

## Probability and Statistics for Convex Optimization

Probability and statistics form a crucial foundation for understanding many optimization problems, especially in machine learning and data science. This section introduces the essential probabilistic concepts that frequently appear in convex optimization, from maximum likelihood estimation to Bayesian optimization.

### Why Probability Matters in Optimization

Many optimization problems arise from statistical modeling:

- **Maximum Likelihood Estimation (MLE)**: Finding parameters that maximize the likelihood of observed data
- **Bayesian Optimization**: Using probabilistic models to guide the search for optimal solutions
- **Stochastic Optimization**: Dealing with uncertainty and randomness in objective functions
- **Regularization**: Adding probabilistic priors to prevent overfitting
- **Risk Minimization**: Optimizing expected loss over probability distributions

### Key Topics Covered

1. **Basic Probability Theory**: Sample spaces, events, and probability axioms
2. **Common Probability Distributions**: Normal, exponential, and other distributions crucial for optimization
3. **Expectation and Variance**: Computing and optimizing expected values
4. **Bayes' Theorem**: Foundation for Bayesian optimization and inference
5. **Statistical Estimation**: Connecting probability theory to optimization problems

### Connection to Convex Optimization

Understanding probability helps you:

- **Formulate Problems**: Convert real-world uncertainty into mathematical optimization problems
- **Choose Objective Functions**: Select appropriate loss functions based on probabilistic assumptions
- **Interpret Results**: Understand confidence intervals and statistical significance of solutions
- **Handle Noise**: Deal with measurement errors and stochastic processes
- **Design Algorithms**: Develop robust optimization methods that work under uncertainty

This foundation will be essential as we explore how probabilistic models lead to convex optimization problems in machine learning, statistics, and engineering applications.

<div style="background: #e8f4fd; padding: 15px; border-left: 4px solid #2196F3; margin: 20px 0;">
<strong>💡 Learning Path:</strong> Start with basic probability concepts, then explore how they connect to optimization through maximum likelihood estimation and Bayesian methods. Each lesson builds toward understanding how uncertainty and randomness create optimization problems.
</div>

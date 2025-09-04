---
layout: post
title: 03-05 Log-concave and log-convex functions
chapter: '03'
order: 13
owner: Minjoo Lee
categories:
- chapter03
lang: en
---

This section introduces log-concave and log-convex functions, which are important in probability, statistics, and optimization.

## Definition

The definitions of log-concave and log-convex functions are as follows.

### $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ is Logarithmically concave or log-concave
If $$f(x) > 0$$ for all $$x \in \text{dom}f$$ and $$\log f$$ is concave, then $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ is called logarithmically concave or log-concave.
> $$f$$ is log-concave for $$f(x) > 0$$ for all $$x \in \text{dom}f$$ : <br>
>$$f(\theta x + (1 - \theta) y) \geq f(x)^\theta f(y)^{1-\theta}$$ for $$0 \leq \theta \leq 1$$.

### $$f : \mathbb{R}^n \mapsto \mathbb{R} $$ is Logarithmically convex or log-convex
If $$f(x) > 0$$ for all $$x \in \text{dom}f$$ and $$\log f$$ is convex, then $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ is called logarithmically convex or log-convex. Therefore, if $$f$$ is log-convex, then $$1/f$$ is log-concave.
> $$f$$ is log-convex for $$f(x) > 0$$ for all $$x \in \text{dom}f$$ $$\Longleftrightarrow \frac{1}{f}$$ is log-concave.

It is sometimes convenient to allow $$f$$ values to be 0, in which case $$\log f(x) = -\infty$$. In such cases, if the extended-value function $$\log f$$ is concave, then $$f$$ can be called log-concave.

**Log-convex functions and log-concave functions are quasiconvex and quasiconcave, respectively, because the logarithm is monotonically increasing.**

## Examples
### Affine function
If $$f$$ is defined as follows, then it is log-concave.
>$$f(x) = a^Tx + b$$ on $$\{x \mid a^Tx + b > 0\}$$

### Powers
$$f(x) = x^a$$ on $$\mathbb{R}_{++}$$ is log-convex when $$a \leq 0$$ and log-concave when $$a \geq 0$$.

### Exponentials
$$f(x) = e^{ax}$$ is both log-convex and log-concave.

### The cumulative distribution function of a Gaussian density
$$\Phi(x) = \frac{1}{ \sqrt{2 \pi } }  \int_ {-\infty} ^x e^{-u^2/2} du $$ is log-concave.

### Gamma function
$$\Gamma (x) = \int_0^\infty u^{x-1}e^{-u} du $$
is log-convex for $$x \geq 1$$.

### Determinant
$$\det X$$ is log-concave on $$S^n_{++}$$.

### Determinant over trace
$$\det X / \text{tr} X$$ is log-concave on $$S^n_{++}$$.

<br>
## Properties

### Twice differentiable log-convex / concave functions
If $$f$$ is twice differentiable and $$\text{dom} f$$ is convex, then the following equation holds:<br>
>$$\nabla ^2 \log f(x) = \frac{1}{f(x)} \nabla ^2f(x) - \frac{1}{f(x)^2}\nabla f(x) \nabla f(x)^T$$

$$f$$ is log-convex $$\Longleftrightarrow$$ $$f(x) \nabla ^2 f(x) \succeq \nabla f(x)\nabla f(x)^T$$ for all $$x \in \text{dom} f$$, and <br>
$$f$$ is log-concave $$\Longleftrightarrow$$ $$f(x) \nabla ^2 f(x) \preceq \nabla f(x)\nabla f(x)^T$$ for all $$x \in \text{dom} f$$.

<br>
### Multiplication
Log-convexity and log-concavity are closed under multiplication and positive scaling. 
If $$f$$ and $$g$$ are log-concave, then the pointwise product $$h(x) = f(x)g(x)$$ is also log-concave. 
This is because $$\log h(x) = \log f(x) + \log g(x)$$, and both $$\log f(x)$$ and $$\log g(x)$$ are concave functions.

### Addition and Integration
In general, the sum of log-concave functions is not log-concave. However, log-convexity is preserved under addition.
For example, let $$f$$ and $$g$$ be log-convex functions, i.e., $$F = \log f$$ and $$G = \log g$$ are convex.
By the composition rules for convex functions, the following holds:<br>

>$$\log(exp F + exp G) = \log(f + g)$$

This is convex. (The left side is convex because: 1. log-convex functions are convex, 2. applying the exponential function to convex functions preserves convexity, 3. the sum of convex functions is convex, and 4. the logarithm of convex functions is convex.
Therefore, the entire result is convex.) In conclusion, the sum of two log-convex functions is log-convex. 

Generalizing this, if $$f(x, y)$$ is log-convex for each $$y \in C$$, then $$g(x)$$ is log-convex.
>$$g(x) = \int_C^{} f(x,y) dy $$ 

### Integration of log-concave functions
In certain cases, log-concavity is also preserved under integration. If $$f : \mathbb{R}^n \times \mathbb{R}^m \mapsto \mathbb{R}$$ is log-concave, then $$g(x)$$ is a log-concave function for $$x \in \mathbb{R}^n$$.
>$$f : \mathbb{R}^n \mapsto \mathbb{R}$$ is log-concave $$\Longrightarrow$$ $$g(x) = \int_{}^{} f(x,y) dy$$ is log-concave , $$x \in \mathbb{R}^n$$ for each $$y \in C$$.

Based on this, we can confirm that the marginal distribution of a log-concave probability density is log-concave.<br>

Log-concavity is also closed under convolution operations. If $$f$$ and $$g$$ are log-concave on $$\mathbb{R}^n$$, then their convolution is also log-concave. 
>$$f$$, $$g$$ are log-concave on $$\mathbb{R}^n \Longrightarrow (f \ast g)(x) = \int_{}^{} f(x-y)g(y) dy$$ is log-concave.<br>

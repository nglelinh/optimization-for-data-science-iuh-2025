---
layout: post
title: 00.04 Taylor Series
chapter: "00"
order: 5
owner: "GitHub Copilot"
---

The Taylor series is a representation of a function as an infinite sum of terms calculated from the values of the function's derivatives at a single point. It is one of the most fundamental concepts in calculus and mathematical analysis, providing a way to approximate complex functions with simpler polynomial functions.

### 1. Definition

A Taylor series is a series expansion of a function $$f(x)$$ about a point $$a$$. If a function $$f(x)$$ is infinitely differentiable at a point $$a$$, its Taylor series is given by:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

Where:
*   $$f^{(n)}(a)$$ denotes the $$n$$-th derivative of $$f(x)$$ evaluated at the point $$a$$.
*   $$f^{(0)}(a)$$ is the function itself evaluated at $$a$$, i.e., $$f(a)$$.
*   $$n!$$ is the factorial of $$n$$.
*   $$(x-a)^n$$ is the $$n$$-th power of $$(x-a)$$.

This can also be written in expanded form as:

$$f(x) = f(a) + \frac{f'(a)}{1!}(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \dots$$

### 2. Maclaurin Series (Special Case)

A Maclaurin series is a special case of the Taylor series where the expansion point $$a$$ is $$0$$. It is given by:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n$$

In expanded form:

$$f(x) = f(0) + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots$$

### 3. Conditions for Existence and Convergence

For a function to have a Taylor series expansion about a point $$a$$, it must be infinitely differentiable at that point. However, the existence of a Taylor series does not guarantee that the series converges to the function $$f(x)$$.

*   **Convergence:** The Taylor series converges to $$f(x)$$ if and only if the remainder term (see below) approaches zero as $$n \to \infty$$.
*   **Radius of Convergence:** For a given Taylor series, there is often a radius of convergence $$R$$. The series converges for all $$x$$ such that $$\lvert x-a \rvert < R$$. Outside this interval, the series diverges. The radius of convergence can be found using tests like the ratio test:

    $$R = \lim_{n \to \infty} \left\lvert  \frac{a_n}{a_{n+1}} \right \rvert$$
    
    where $$a_n = \frac{f^{(n)}(a)}{n!}$$.

### 4. Taylor Polynomials and Remainder Term

A Taylor series is an infinite sum. In practice, we often use a finite number of terms to approximate the function. This finite sum is called a **Taylor polynomial** of degree $$N$$:

$$P_N(x) = \sum_{n=0}^{N} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

The difference between the actual function value and the Taylor polynomial approximation is called the **remainder term**, denoted $$R_N(x)$$:

$$f(x) = P_N(x) + R_N(x)$$

There are several forms for the remainder term, the most common being the **Lagrange form**:

$$R_N(x) = \frac{f^{(N+1)}(c)}{(N+1)!}(x-a)^{N+1}$$

where $$c$$ is some number between $$a$$ and $$x$$. This form is crucial for estimating the error of the approximation.

### 5. Common Maclaurin Series Expansions

Here are some frequently encountered Maclaurin series expansions:

*   **Exponential Function:**
    $$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots \quad \text{for all } x \in \mathbb{R}$$

*   **Sine Function:**
    $$\sin x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!}x^{2n+1} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots \quad \text{for all } x \in \mathbb{R}$$

*   **Cosine Function:**
    $$\cos x = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!}x^{2n} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots \quad \text{for all } x \in \mathbb{R}$$

*   **Geometric Series:**
    $$\frac{1}{1-x} = \sum_{n=0}^{\infty} x^n = 1 + x + x^2 + x^3 + \dots \quad \text{for } \lvert x \rvert<1$$

*   **Natural Logarithm:**
    $$\ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}x^n = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots \quad \text{for } -1 < x \le 1$$

*   **Binomial Series:**
    $$(1+x)^\alpha = \sum_{n=0}^{\infty} \binom{\alpha}{n} x^n = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^2 + \frac{\alpha(\alpha-1)(\alpha-2)}{3!}x^3 + \dots \quad \text{for } \lvert x \rvert<1 \text{ where } \binom{\alpha}{n} = \frac{\alpha(\alpha-1)\dots(\alpha-n+1)}{n!}.$$


###  Uniqueness

If a function $$f(x)$$ can be represented by a power series about a point $$a$$, then that power series must be its Taylor series. This means the Taylor series representation, if it exists and converges to the function, is unique.

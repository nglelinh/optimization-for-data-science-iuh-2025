---
layout: post
title: 00.04 Taylor Series
chapter: '00'
order: 5
owner: GitHub Copilot
lang: vi
categories:
- chapter00
---


Chuỗi Taylor là một cách biểu diễn hàm số dưới dạng tổng vô hạn các số hạng được tính từ các đạo hàm của hàm số tại một điểm duy nhất. Đây là một trong những khái niệm cơ bản nhất của giải tích và phân tích toán học, cung cấp phương pháp xấp xỉ các hàm phức tạp bằng các đa thức đơn giản hơn.

### 1. Định nghĩa

Chuỗi Taylor là khai triển chuỗi của một hàm số $$f(x)$$ quanh một điểm $$a$$. Nếu hàm số $$f(x)$$ khả vi vô hạn tại điểm $$a$$, chuỗi Taylor của nó được cho bởi:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

Trong đó:
*   $$f^{(n)}(a)$$ là đạo hàm bậc $$n$$ của $$f(x)$$ tại điểm $$a$$.
*   $$f^{(0)}(a)$$ là giá trị của hàm tại $$a$$, tức là $$f(a)$$.
*   $$n!$$ là giai thừa của $$n$$.
*   $$(x-a)^n$$ là lũy thừa bậc $$n$$ của $$(x-a)$$.

Công thức này cũng có thể viết dạng khai triển như sau:

$$f(x) = f(a) + \frac{f'(a)}{1!}(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \dots$$

### 2. Chuỗi Maclaurin (Trường hợp đặc biệt)

Chuỗi Maclaurin là trường hợp đặc biệt của chuỗi Taylor khi điểm khai triển $$a$$ là $$0$$. Công thức:

$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}x^n$$

Dạng khai triển:

$$f(x) = f(0) + \frac{f'(0)}{1!}x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots$$

### 3. Điều kiện tồn tại và hội tụ

Để một hàm số có khai triển chuỗi Taylor quanh điểm $$a$$, nó phải khả vi vô hạn tại điểm đó. Tuy nhiên, sự tồn tại của chuỗi Taylor không đảm bảo rằng chuỗi này hội tụ về đúng hàm số $$f(x)$$.

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

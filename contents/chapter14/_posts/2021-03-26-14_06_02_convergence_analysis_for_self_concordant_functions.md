---
layout: post
title: 14-06-02 Convergence analysis for self-concordant functions
chapter: "14"
order: 12
owner: "Minjoo Lee"
---
For self-concordant functions, the result of convergence analysis is as follows:

>Theorem (Nesterov and Nemirovskii): Newton's method with backtracking line search requires the following number of iterations to achieve $$f(x^{(k)})-f^{\star}\leq \epsilon$$:
>\begin{align}
>C(\alpha, \beta)\big( f(x^{(0)}-f^{\star} \big) + \log\log{(1/\epsilon)},
>\end{align}
>where $$C(\alpha, \beta)$$ is a constant depending on $$\alpha, \beta$$.

The proof above is similar to the convergence analysis for Newton's method, but uses the properties of self-concordant functions to organize the steps. (See [1], p.503)
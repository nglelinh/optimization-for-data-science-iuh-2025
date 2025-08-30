---
layout: post
title: 08-02-02 Convergence of Stochastic Methods
chapter: "08"
order: 13
owner: "Kyeongmin Woo"
---

Assume each function $$f_i, i = 1,...,m$$ is convex and Lipschitz continuous with constant G.

For the stochastic subgradient method, the following properties hold for fixed and diminishing step sizes:

- **Fixed step sizes** for $$t_k = t$$, $$k = 1, 2, 3, ...$$

>$$\text{For cyclic and randomized methods with fixed step sizes, the following holds:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) \le f^{*} + 5m^{2}G^{2}t/2
\end{align}
$$

Here, $$mG$$ is the Lipschitz constant of $$\sum_{i=1}^{m} f_i$$.

- **Diminishing step sizes**

>$$\text{For cyclic and randomized methods with diminishing step sizes, the following holds:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) = f^{*}
\end{align}
$$


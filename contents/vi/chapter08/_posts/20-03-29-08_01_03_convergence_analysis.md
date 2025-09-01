---
layout: post
title: '08-01-03 Convergence analysis'
chapter: '08'
order: 5
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

In gradient descent, it is assumed that $$\nabla f$$ is Lipschitz continuous, but in the subgradient method, we assume that $$f$$ itself is Lipschitz continuous. (See the convergence theorem for gradient descent [06-03-01]({% multilang_post_url contents/chapter06/21-03-20-06_03_01_convergence_analysis_and_proof %}) for reference.)

Assume $$f$$ is convex, dom $$f = \mathbb{R}^n$$, and $$f$$ satisfies the Lipschitz condition:

>\begin{align}
> | f(x) - f(y) | \le G \lVert x - y \rVert_2 \text{ for all } x, y
\end{align}

Given these assumptions, the convergence formulas for fixed and diminishing step sizes are as follows:

## Convergence theorem for fixed step sizes 

Fixed step sizes have the following convergence property:
>\begin{align}
> \lim_{k\to\infty} f(x^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}

## Convergence theorem for diminishing step sizes 

The diminishing step sizes method has the following convergence property:

>\begin{align}
\lim_{k\to\infty}f(x^{(k)}_{best}) = f^*
\end{align}

## Proofs

The proofs for fixed and diminishing step sizes are as follows.

## Proof of convergence theorem for fixed step sizes

The fixed step size method uses $$\sum_{i=1}^{k}t_{i} = kt$$ in its proof.  

>$$\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} = \frac{R^{2}+G^{2}k t^{2}}{2kt}  = \frac{R^{2}}{2tk} + \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^*) \le 0 + \frac{G^{2}t}{2} = \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}
$$


## Proof of convergence theorem for diminishing step sizes 

The proof for the diminishing step sizes uses the following properties (1) and (2):

>$$
\begin{align}
\text{(1)} \sum_{i=1}^{\infty} t_i = \infty, \quad \text{(2)}  \sum_{i=1}^{\infty} t_i^{2} = \beta < \infty
\end{align}
$$

>$$
\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^* ) \le \frac{R^{2}+G^{2}\beta}{2\infty} = 0 \\
& \lim_{k→\infty}(f^{(k)}_{best}) =  f^* \\
\end{align}
$$
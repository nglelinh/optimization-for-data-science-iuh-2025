---
layout: post
title: '08-01-03 Convergence analysis'
chapter: '08'
order: 5
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

In smooth optimization, Lipschitz continuity of the *gradient* $$\nabla f$$ caps how sharply the slope can bend, giving gradient descent a smooth quadratic upper bound to descend along. When $$f$$ has corners, $$\nabla f$$ does not even exist—so we step down one derivative and assume instead that $$f$$ itself is $$G$$-Lipschitz continuous. That single change of assumption explains the entire qualitative gap between smooth and nonsmooth convergence guarantees.

## Background Knowledge Map: From Lipschitz Functions to Convergence Theorems

- **Pillar 1 — $$G$$-Lipschitz Continuity Equals Bounded Subgradients:** For a convex function on $$\mathbb{R}^n$$, $$|f(x) - f(y)| \le G\|x - y\|_2$$ holds if and only if every subgradient satisfies $$\|g\|_2 \le G$$. This guarantees that the squared-norm penalty $$t_k^2 \|g^{(k)}\|_2^2$$ in the basic inequality is uniformly capped by $$G^2 t_k^2$$.
- **Pillar 2 — Constant Step Size Limit ($$G^2 t / 2$$ Floor):** Plugging $$t_i = t$$ into the basic inequality gives $$f_{\text{best}}^{(k)} - f^\star \le \frac{R^2}{2kt} + \frac{G^2 t}{2}$$. As $$k \to \infty$$, the initial-distance term vanishes at rate $$O(1/k)$$, leaving an irreducible bias floor of $$G^2 t / 2$$.
- **Pillar 3 — Asymptotic Convergence Under Diminishing Step Sizes:** When $$\sum_{i=1}^\infty t_i = \infty$$ and $$\sum_{i=1}^\infty t_i^2 = S < \infty$$, the numerator $$R^2 + G^2 S$$ stays bounded while the denominator $$2\sum_{i=1}^k t_i$$ diverges to $$\infty$$, forcing $$\lim_{k\to\infty} f_{\text{best}}^{(k)} = f^\star$$.
- **Pillar 4 — Bias–Variance Trade-off in Step Selection:** A larger fixed step $$t$$ crushes the transient term $$R^2/(2kt)$$ quickly but leaves a larger steady-state error $$G^2 t/2$$; a smaller $$t$$ shrinks the steady-state error at the cost of a longer transient phase.

### Step-by-Step Worked Example (Read Slowly): Computing the Exact Convergence Floor and Horizon

Suppose a $$G$$-Lipschitz convex function has $$G = 4$$, initial distance $$R = \|x^{(1)} - x^\star\|_2 = 10$$, and we run the subgradient method with a fixed step size $$t = 0.05$$.

1. **Compute the asymptotic error floor:**
   $$\frac{G^2 t}{2} = \frac{4^2 \cdot 0.05}{2} = \frac{16 \cdot 0.05}{2} = 0.40.$$
   No matter how many iterations we run with $$t = 0.05$$, the theorem only guarantees $$f_{\text{best}}^{(k)} - f^\star \le 0.40$$ in the limit.
2. **Evaluate the transient term at $$k = 250$$ iterations:**
   $$\frac{R^2}{2kt} = \frac{10^2}{2 \cdot 250 \cdot 0.05} = \frac{100}{25} = 4.00.$$
   Total guaranteed gap at $$k = 250$$: $$4.00 + 0.40 = 4.40$$.
3. **Balance both terms at $$k = 2500$$ iterations:**
   $$\frac{R^2}{2kt} = \frac{100}{2 \cdot 2500 \cdot 0.05} = \frac{100}{250} = 0.40.$$
   At $$k = 2500$$, the transient error equals the steady-state floor, giving $$f_{\text{best}}^{(2500)} - f^\star \le 0.40 + 0.40 = 0.80$$.
4. **Compare with diminishing step size $$t_i = 1/i$$ at $$k = 100$$:** Using $$\sum_{i=1}^{100} 1/i \approx 5.187$$ and $$\sum_{i=1}^{100} 1/i^2 < \pi^2/6 \approx 1.645$$, the bound is:
   $$f_{\text{best}}^{(100)} - f^\star \le \frac{100 + 16(1.645)}{2(5.187)} \approx \frac{126.32}{10.374} \approx 12.18,$$
   which eventually vanishes as $$k \to \infty$$, though very slowly because $$\sum 1/i \approx \ln k$$ grows only logarithmically!

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
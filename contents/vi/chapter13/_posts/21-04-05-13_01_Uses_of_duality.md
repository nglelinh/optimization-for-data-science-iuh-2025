---
layout: post
title: 13-01 Uses of duality
chapter: '13'
order: 2
owner: Wontak Ryu
categories:
- chapter13
lang: en
---

### Two key uses of duality
Let's revisit the two key characteristics of duality covered in Chapter 11.

• When $$x$$ is primal feasible and $$u,v$$ are dual feasible, the difference between the primal problem $$f(x)$$ and the dual problem $$g(u,v)$$ is called the **duality gap** between $$x$$ and $$u,v$$.
> $$f(x)-f^{\star}  \le f(x)-g(u, v)$$

When the duality gap is 0, this is called zero duality gap, which means that the solution to the dual problem is optimal.
Also, the upper bound $$g(u, v)$$ is always less than or equal to the optimal value $$f^{\star}$$. For detailed reasons, please refer to the content in [[Chapter 11]]({% multilang_post_url contents/chapter11/21-03-24-11_00_Duality_in_General_Programs %}).
Therefore, the following derivation is possible.

#### [Proof]
> $$\begin{align*}
> f^{\star} &\ge g(u, v) \\
> -f^{\star} &\le -g(u, v) \\
> f(x)-f^{\star} &\le \underbrace{f(x)-g(u, v)}_{\text{duality gap}}\\
> g^{\star}-g(x) &\le \underbrace{f(x)-g(u, v)}_{\text{duality gap}}\\
> \end{align*}$$


Moreover, the duality gap can be used as a stopping criterion for algorithms.
• When dual optimal $$u^{\star}, v^{\star}$$ are given, under the condition of strong duality, the primal solution minimizes the Lagrangian $$L (x, u^{\star}, v^{\star})$$ for all $$x$$ (i.e., satisfies the stationarity condition).

This can be used for computing the primal solution.

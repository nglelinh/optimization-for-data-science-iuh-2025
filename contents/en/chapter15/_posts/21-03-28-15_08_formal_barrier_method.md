---
layout: post
title: 15-08 Formal barrier method
chapter: "15"
categories:
- chapter16
order: 14
owner: "Minjoo Lee"
---

If a convex function $$\phi : D \to \mathbb{R}$$ defined on an open convex set $$D \subset \mathbb{R}^n$$ satisfies the following conditions, then the function is a **self-concordant barrier** with parameter $$\nu$$.

* $$\phi$$ is self-concordant
* For all $$x \in D$$, the Newton decrement is bounded by the constant $$\nu$$ as follows.

> $$\lambda(x)^2 = \nabla \phi(x) (\nabla^2 \phi(x))^{-1} \nabla \phi(x) \le \nu$$

Let's consider the following LP problem. (Here, $$\bar{D}$$ is the closure of the domain $$D$$.)
>
$$\begin{align}
&\min_{x} \           && c^Tx \\
&\text{subject to } \ && x \in \bar{D}  \\
\end{align}$$

This problem can be approximated as follows.
>
$$\begin{align}
&\min_{x} && tc^Tx + \phi(x) \\
\end{align}$$

Here, let $$\phi_t(x) := tc^Tx + \phi(x)$$ and let the corresponding Newton decrement be $$\lambda_t(x)$$.

Key observation: When $$t^+ > t$$
>
$$\begin{align}
\lambda_t^+(x) \le & \frac{t^+}{t}\lambda_t^+(x) + \left ( \frac{t^+}{t} -1 \right ) \sqrt{\nu}  \\\
\end{align}$$

## Theorem

>$$\begin{align}
& \text{if} \quad \lambda_t(x) \le \frac{1}{9} \quad \text{and} \quad \frac{t^+}{t} \le 1 + \frac{1}{8 \sqrt{\nu}} \quad \text{then} \quad \lambda_t^+(x^+) \le \frac{1}{9}  \\
& \qquad \qquad \text{for} \quad x^+ = x - (\nabla^2 (\phi_{t^+}(x))^{-1} \nabla (\phi_{t^+}(x)
\end{align}$$

In conclusion, if we start with $$x^{(0)}, t^{(0)}$$ such that $$\lambda_{t^{(0)}}(x^{(0)}) \lt \frac{1}{9}$$ and choose $$\mu := 1 + \frac{1}{8 \sqrt{\nu}}$$, then one Newton step per centering step is sufficient.

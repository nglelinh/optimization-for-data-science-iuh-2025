---
layout: post
title: 15-08 Formal barrier method
chapter: "15"
categories:
- chapter16
order: 14
owner: "Minjoo Lee"
lang: en
---

Earlier we saw the practical barrier method (v.1 and v.2) jump $$t$$ by a big factor $$\mu = 10$$ and take several Newton steps to re-center. Can we prove a mathematically airtight polynomial-time worst-case bound for *all* conic programs? Yes—by taking **short steps**! If $$\phi$$ is a $$\nu$$-self-concordant barrier and we nudge $$t$$ by the tiny factor $$\mu = 1 + \frac{1}{8\sqrt{\nu}}$$, then **one single Newton step** is guaranteed to restore $$\lambda_{t^+}(x^+) \le \frac{1}{9}$$ forever!

## Key ideas: Short-Step Path-Following & Polynomial Complexity

- **Pillar 1 — $$\nu$$-Self-Concordant Barrier Parameter:** A self-concordant function $$\phi$$ is a $$\nu$$-barrier if its own Newton decrement is uniformly bounded: $$\lambda_\phi(x)^2 = \nabla\phi(x)^T (\nabla^2\phi(x))^{-1}\nabla\phi(x) \le \nu$$ for all $$x \in D$$. For $$m$$ linear inequalities, $$\nu = m$$.
- **Pillar 2 — Quantifying the Jump in $$\lambda$$ When $$t \to t^+$$:** Increasing $$t$$ to $$t^+$$ perturbs the Newton decrement predictably by at most $$\lambda_{t^+}(x) \le \frac{t^+}{t}\lambda_t(x) + \left(\frac{t^+}{t} - 1\right)\sqrt{\nu}$$.
- **Pillar 3 — The One-Step Invariant ($$\lambda \le 1/9$$):** Choosing $$\frac{t^+}{t} = 1 + \frac{1}{8\sqrt{\nu}}$$ keeps $$\lambda_{t^+}(x) \le \frac{1}{4}$$, which sits strictly inside Newton's quadratic-contraction ball—so **one** pure Newton step snaps $$\lambda_{t^+}(x^+)$$ right back below $$\frac{1}{9}$$!
- **Pillar 4 — $$O(\sqrt{\nu}\log(1/\epsilon))$$ Worst-Case Complexity:** Since $$\log\left(1 + \frac{1}{8\sqrt{\nu}}\right) \approx \frac{1}{8\sqrt{\nu}}$$, reaching $$t = \nu/\epsilon$$ requires at most $$O\left(\sqrt{\nu}\log\left(\frac{\nu}{t^{(0)}\epsilon}\right)\right)$$ total Newton steps—proving polynomial time for LP, SOCP, and SDP!

### Worked example: Verifying the $$\nu$$-Barrier Parameter and Short-Step Growth Factor

Consider the standard orthant barrier $$\phi(x) = -\sum_{i=1}^m \log(x_i)$$ on $$D = \mathbb{R}^m_{++}$$.

1. **Compute the barrier parameter $$\nu$$ directly from $$\lambda_\phi(x)^2 = \nabla\phi(x)^T (\nabla^2\phi(x))^{-1}\nabla\phi(x)$$:**
   - From Section 15-01-03: $$\nabla \phi(x) = -X^{-1}\mathbf{1}$$ and $$\nabla^2 \phi(x) = X^{-2}$$, so $$(\nabla^2\phi(x))^{-1} = X^2$$.
   - Multiply out:
     $$\lambda_\phi(x)^2 = (-X^{-1}\mathbf{1})^T X^2 (-X^{-1}\mathbf{1}) = \mathbf{1}^T X^{-1} X^2 X^{-1} \mathbf{1} = \mathbf{1}^T \mathbf{1} = m.$$
   - Therefore $$\phi(x)$$ is a self-concordant barrier with exact parameter $$\nu = m$$!
2. **Apply the short-step update for $$m = 100$$ inequalities ($$\sqrt{\nu} = 10$$):**
   - Growth factor: $$\mu = 1 + \frac{1}{8\sqrt{100}} = 1 + \frac{1}{80} = 1.0125$$.
   - Check the perturbed decrement if $$\lambda_t(x) = \frac{1}{9} \approx 0.1111$$:
     $$\lambda_{t^+}(x) \le 1.0125(0.1111) + (0.0125)(10) = 0.1125 + 0.125 = 0.2375 < \frac{1}{4}.$$
   - One pure Newton step contracts $$\lambda_{t^+}(x^+) \le \frac{0.2375^2}{(1 - 0.2375)^2} \approx 0.097 \le \frac{1}{9}$$! The invariant holds inductively forever.

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

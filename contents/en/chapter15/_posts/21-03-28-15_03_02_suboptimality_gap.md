---
layout: post
title: 15-03-02 Suboptimality gap
chapter: '15'
order: '9'
owner: Minjoo Lee
categories:
- chapter15
lang: en
---

Most approximate optimization methods force you to guess whether your penalty weight $$t$$ is large enough. The log barrier is different: it hands you an exact, ironclad formula—$$f(x^*(t)) - f^\star \le \frac{m}{t}$$—requiring zero knowledge of the optimal value $$f^\star$$, the dimension $$n$$, or the condition number of $$f$$. Want an answer guaranteed within $$\epsilon = 10^{-6}$$ on a problem with $$m = 50$$ inequalities? Just drive $$t$$ past $$5 \times 10^7$$!

## Background Knowledge Map: Proving and Using the $$m/t$$ Suboptimality Bound

- **Pillar 1 — Dual Feasibility of $$(u(t), v(t))$$:** Because $$x^*(t)$$ minimizes the convex Lagrangian $$L(x, u(t), v(t))$$ over all $$x$$ (by stationarity), evaluating $$g(u(t), v(t))$$ is immediate—no extra optimization required!
- **Pillar 2 — Exact Evaluation of the Dual Function:** Plugging $$x^*(t)$$ into $$L$$ gives
  $$g(u(t), v(t)) = f(x^*(t)) + \sum_{i=1}^m \underbrace{u_i(t)h_i(x^*(t))}_{-1/t} + v(t)^T \underbrace{(Ax^*(t) - b)}_{0} = f(x^*(t)) - \frac{m}{t}.$$
- **Pillar 3 — Immediate Suboptimality Certificate:** By weak duality $$g(u(t), v(t)) \le f^\star$$, we get $$f(x^*(t)) - f^\star \le f(x^*(t)) - g(u(t), v(t)) = \frac{m}{t}$$.
- **Pillar 4 — Direct Algorithmic Stopping Rule:** The outer loop of the barrier method simply checks $$\frac{m}{t} \le \epsilon$$—stopping with a mathematically certified $$\epsilon$$-optimal primal-dual pair.

### Step-by-Step Worked Example (Read Slowly): Computing the Exact Dual Lower Bound and Gap

Using the problem from Section 15-03-01—$$\min \frac{1}{2}x^2$$ subject to $$h_1(x) = 2 - x \le 0$$ ($$m = 1$$, true $$f^\star = \frac{1}{2}(2)^2 = 2$$)—we found at $$t = 1$$ that $$x^*(1) = 1 + \sqrt{2} \approx 2.4142$$ and $$u_1(1) = 1 + \sqrt{2} \approx 2.4142$$.

1. **Compute the primal objective at $$x^*(1)$$:**
   $$f(x^*(1)) = \frac{1}{2}(1 + \sqrt{2})^2 = \frac{1}{2}(3 + 2\sqrt{2}) = 1.5 + \sqrt{2} \approx 2.9142.$$
2. **Compute the dual function $$g(u_1(1)) = L(x^*(1), u_1(1))$$:**
   $$g(u_1(1)) = f(x^*(1)) + u_1(1)h_1(x^*(1)) = (1.5 + \sqrt{2}) + (-1) = 0.5 + \sqrt{2} \approx 1.9142.$$
3. **Check the duality gap vs. true suboptimality:**
   - Certified duality gap: $$f(x^*(1)) - g(u_1(1)) = 2.9142 - 1.9142 = 1.0 = \frac{m}{t}$$.
   - True suboptimality: $$f(x^*(1)) - f^\star = 2.9142 - 2.0 = 0.9142 \le 1.0$$!
4. **How large must $$t$$ be to guarantee $$\epsilon = 10^{-4}$$?** Simply $$t \ge \frac{m}{\epsilon} = \frac{1}{10^{-4}} = 10{,}000$$.

What is the suboptimality gap between $$f(x^*(t))$$, the solution to the barrier problem obtained in the previous section, and $$f(x^*)$$, the solution to the original problem?

Therefore, we can derive the following equation.

>$$
>\begin{align}
>f(x^*) &\ge f(x^*(t)) + \nabla f(x^*(t))^T (x^* - x^*(t)) \\\\
>h_i(x^*) &\ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t)), \quad i = 1, \cdots, m
>\end{align}
>$$

If convexity is guaranteed, the function is always greater than its tangent, so $$f(x^*) \ge f(x^*(t)) + \nabla f(x^*(t))^T (x^* - x^*(t))$$ holds. (The tangent is the first-order Taylor approximation)

Similarly, since $$h_i(x^*) \ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t))$$ holds, we can derive the following equation:

$$
h_i(x^*(t)) - h_i(x^*) \le \nabla h_i(x^*(t))^T (x^*(t) - x^*), \quad i = 1, \cdots, m
$$

## Derivation of suboptimality gap

Let's use these two equations to derive the suboptimality gap. The right-hand side is derived from the two convexity conditions above.

$$
\begin{align}
f(x^*(t)) - f(x^*) + \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) &\le \left\langle \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)), \quad x^*(t) - x^* \right\rangle \\\\
&= \left\langle -tA^Tv, \quad x^*(t) - x^* \right\rangle \\\\
\end{align}
$$

If we look at the right-hand side of this equation as an inner product, since $$Ax^*(t) = b$$ and $$Ax^* = b$$, the entire term becomes zero.

Therefore, moving the third term of the first equation to the right and simplifying, we get the following result:

$$
\begin{align}
f(x^*(t)) - f(x^*) &\le - \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) \\\\
&= \frac{m}{t} + \sum_{i=1}^{m} u_i(t) h_i(x^*) \\\\
&\le \frac{m}{t}
\end{align}
$$

The first term in the second line becomes $$\frac{m}{t}$$ because it satisfies $$u_i(t) \cdot h_i(x^*(t)) = - \frac{1}{t}$$ from the KKT conditions.

The second term can be removed because $$\sum_{i=1}^{m} u_i(t) h_i(x^*) \le 0$$ from the KKT conditions.

As a result, we can obtain the following suboptimality gap, which becomes a useful stopping criterion for this problem. As a reference, the duality gap can also be derived in the next chapter.

>$$
>\begin{align}
>f(x^*(t)) - f(x^*) \le \frac{m}{t}
>\end{align}
>$$
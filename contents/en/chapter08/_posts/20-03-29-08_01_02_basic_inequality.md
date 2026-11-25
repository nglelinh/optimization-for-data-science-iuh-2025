---
layout: post
title: '08-01-02 Basic Inequality'
chapter: '08'
order: 4
owner: Kyeongmin Woo
categories:
- chapter08
lang: en
---

Every major theorem in Chapter 08—convergence under fixed step sizes, diminishing step sizes, optimal $$O(1/\varepsilon^2)$$ rates, and even Polyak's adaptive rule—flows from a single, five-line algebraic master key called the **basic inequality**. Rather than proving each step-size rule from scratch, Shor and Polyak discovered that expanding the squared Euclidean distance $$\|x^{(k+1)} - x^\star\|_2^2$$ and telescoping across iterations traps the entire trajectory in one clean ratio. Mastering this single inequality lets you derive every convergence bound in nonsmooth optimization on the back of an envelope.

## Background Knowledge Map: The Mechanics of the Basic Inequality

- **Pillar 1 — Squared-Distance Expansion:** Expanding $$\|x^{(k+1)} - x^\star\|_2^2 = \|x^{(k)} - \alpha_k g^{(k)} - x^\star\|_2^2$$ splits the update into three pieces: previous distance $$\|x^{(k)} - x^\star\|_2^2$$, a helpful cross-term $$-2\alpha_k g^{(k)\top}(x^{(k)} - x^\star)$$, and a quadratic overshoot penalty $$+\alpha_k^2 \|g^{(k)}\|_2^2$$.
- **Pillar 2 — The Subgradient Bridge:** Applying convexity $$g^{(k)\top}(x^{(k)} - x^\star) \ge f(x^{(k)}) - f^\star$$ converts the geometric inner product directly into an objective suboptimality gap, coupling Euclidean space to function values.
- **Pillar 3 — Telescoping Cancellation:** Summing the one-step recursion from $$i = 1$$ to $$k$$ causes all intermediate distances $$\|x^{(i)} - x^\star\|_2^2$$ to cancel in pairs, leaving only the initial squared radius $$R^2 \ge \|x^{(1)} - x^\star\|_2^2$$ minus the nonnegative final distance $$\|x^{(k+1)} - x^\star\|_2^2 \ge 0$$.
- **Pillar 4 — Weighted Average to Best-Iterate Bound:** Because $$\sum_{i=1}^k \alpha_i (f(x^{(i)}) - f^\star) \ge \left(\sum_{i=1}^k \alpha_i\right)(f_{\text{best}}^{(k)} - f^\star)$$, dividing by $$2\sum \alpha_i$$ immediately isolates $$f_{\text{best}}^{(k)} - f^\star$$ as a competition between initial distance $$R^2$$ and accumulated step variance $$G^2 \sum \alpha_i^2$$.

### Step-by-Step Worked Example (Read Slowly): Verifying the Basic Inequality Numerically

Take $$f(x) = |x|$$ ($$x^\star = 0, f^\star = 0, G = 1$$), starting at $$x^{(1)} = 1$$ (so $$R = |1 - 0| = 1$$), with $$k = 2$$ steps using $$\alpha_1 = 0.6$$ and $$\alpha_2 = 0.4$$.

1. **Run the two iterations explicitly:**
   - Step 1: $$g^{(1)} = 1$$, so $$x^{(2)} = 1 - 0.6(1) = 0.4$$. Objective values so far: $$f(x^{(1)}) = 1$$, $$f(x^{(2)}) = 0.4$$.
   - Step 2: $$g^{(2)} = 1$$, so $$x^{(3)} = 0.4 - 0.4(1) = 0.0$$.
   - The best value among $$\{x^{(1)}, x^{(2)}\}$$ (the iterates entering the sum $$i=1,2$$) is $$f_{\text{best}}^{(2)} = \min\{1, 0.4\} = 0.4$$, so $$f_{\text{best}}^{(2)} - f^\star = 0.4$$.
2. **Compute the telescoping sum directly:**
   - $$\|x^{(1)} - x^\star\|^2 - \|x^{(3)} - x^\star\|^2 = 1^2 - 0^2 = 1$$.
   - Weighted suboptimality sum: $$2\sum_{i=1}^2 \alpha_i (f(x^{(i)}) - f^\star) = 2[0.6(1) + 0.4(0.4)] = 2(0.76) = 1.52$$.
   - Accumulated squared-step term: $$\sum_{i=1}^2 \alpha_i^2 \|g^{(i)}\|^2 = 0.6^2(1) + 0.4^2(1) = 0.36 + 0.16 = 0.52$$.
   - Check the exact identity: $$1.52 = 1 + 0.52$$ (exact equality here because $$f(x) = |x|$$ is linear on $$x > 0$$!).
3. **Evaluate the Basic Inequality RHS:**
   $$\frac{R^2 + G^2(\alpha_1^2 + \alpha_2^2)}{2(\alpha_1 + \alpha_2)} = \frac{1 + 1(0.36 + 0.16)}{2(0.6 + 0.4)} = \frac{1.52}{2.0} = 0.76.$$
4. **Verify:** Indeed $$f_{\text{best}}^{(2)} - f^\star = 0.4 \le 0.76$$, and the slack $$0.76 - 0.4 = 0.36$$ comes purely from replacing the weighted average $$(0.6 \cdot 1 + 0.4 \cdot 0.4)/1.0 = 0.76$$ with the minimum $$0.4$$.

The convergence theorem and convergence rate of the subgradient method can be proved using the following basic inequality.

## Basic Inequality

>$$
\begin{align}
f_{best}^{k} - f^* \quad \le \quad \frac{R^{2}+G^{2}\sum_{i=1}^{k}\alpha_{i}^{2}}{2\sum_{i=1}^{k}\alpha_{i}} 
\end{align}
$$

## Proof
If $$x^*$$ is the optimal point of the function $$f$$, then the following equation holds:

>$$
\begin{alignat}{1}
 \Vert x^{(k+1)}-x^* \Vert _2^{2} & \quad = \quad  \Vert x^{(k)}-\alpha_k g^{(k)}-x^* \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert (x^{(k)}-x^*)-\alpha_k g^{(k)} \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert x^{(k)}-x^* \Vert _2^2 - 2 \alpha_k g^{(k)T}(x^{(k)}-x^*)+\alpha_k^2 \Vert g^{(k)} \Vert _2^2 \\
\end{alignat} $$

From the definition of subgradient, the following inequality holds:

>$$
\begin{alignat}{1}
f(x^*) \ge f(x^{(k)}) + g^{(k)T}(x^*-x^{(k)}) & \quad \Longleftrightarrow \quad f(x^*)-f(x^{(k)}) \ge  g^{(k)T}(x^*-x^{(k)}) \\
                     & \quad  \Longleftrightarrow \quad f(x^{(k)} - f(x^*)) \le  g^{(k)T}(x^{(k)}-x^*) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(f(x^{(k)}) - f(x^*)) \ge  -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \le -2\alpha_{k}(f(x^{(k)})-f(x^*)) \\
\end{alignat} $$

Using the above equations and inequalities, the following inequality can be derived:

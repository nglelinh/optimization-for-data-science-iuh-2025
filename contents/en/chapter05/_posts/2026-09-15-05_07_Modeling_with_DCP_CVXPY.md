---
layout: post
title: 05-07 Modeling with DCP and CVXPY
chapter: '05'
order: 13
owner: Nguyen Le Linh
categories:
- chapter05
lang: en
lesson_type: required
---

Writing a solver from scratch for every new convex model is like building a compiler every time you write a Python script. Disciplined Convex Programming (DCP), pioneered by Grant, Boyd, and Ye and implemented in CVXPY, flips the workflow: you declare your problem in near-textbook math using a small set of convexity-preserving composition rules, and CVXPY automatically *proves* your model is convex and compiles it into a canonical cone program for a solver.

## Key ideas: How DCP Verifies and Compiles Convex Models

1. **Atoms with Known Curvature and Sign**: Every built-in CVXPY atom (like `norm`, `quad_over_lin`, `log_sum_exp`, `sum_squares`) carries two tags: its *curvature* (affine, convex, concave, or constant) and its *monotonicity* in each argument.
2. **The DCP Composition Rule**: A composition $$h(g_1(x), \dots, g_k(x))$$ is certified **convex** if $$h$$ is convex and, for every argument $$i$$, one of three conditions holds:
   - $$g_i$$ is *affine*, OR
   - $$h$$ is *nondecreasing* in argument $$i$$ and $$g_i$$ is *convex*, OR
   - $$h$$ is *nonincreasing* in argument $$i$$ and $$g_i$$ is *concave*.
3. **Sufficient, Not Necessary**: DCP is a *sufficient* syntax check, not a complete theorem prover. A genuinely convex function like $$\sqrt{x^2 + 1}$$ written naively as `sqrt(square(x) + 1)` gets rejected because `sqrt` is concave while `square` is convex—rewriting it via the convex atom `norm2(vstack([x, 1]))` satisfies DCP immediately!
4. **Automatic Canonicalization to Cones**: Once an expression passes DCP, CVXPY replaces each atom with its epigraph cone representation (LP, QP, SOCP, SDP, or ExpCone), hands the canonical matrices to OSQP/Clarabel/SCS, and maps the numerical solution right back into your Python variable objects.

### Worked example: Fixing a DCP Violation by Hand

Suppose you want to minimize the convex function $$f(x) = \frac{1}{x} + \sqrt{x^2 + 4}$$ over $$x \ge 1$$ in CVXPY.

1. **Test the naive expression `1/x + sqrt(x**2 + 4)` against DCP rules**:
   - Term 1: `inv_pos(x)` is a built-in convex atom (for $$x > 0$$) — **DCP-valid**.
   - Term 2: `x**2 + 4` is **convex**, and `sqrt(u)` is **concave** and nondecreasing. Composing concave(convex) has *unknown* curvature under DCP — **CVXPY raises `DCPError`!**
2. **Verify mathematically that $$\sqrt{x^2 + 4}$$ is actually convex**:
   $$\sqrt{x^2 + 4} = \left\|\begin{bmatrix} x \\ 2 \end{bmatrix}\right\|_2.$$
   Since the Euclidean norm is convex and $$(x, 2)^T$$ is affine in $$x$$, the composition `cp.norm(cp.hstack([x, 2]), 2)` is **DCP-valid**!
3. **Trace what CVXPY canonicalizes under the hood**:
   - Introduce epigraph scalars $$t_1, t_2$$ and minimize $$t_1 + t_2$$ subject to $$x \ge 1$$,
   - $$1/x \le t_1 \iff \left\|\begin{bmatrix} 2 \\ x - t_1 \end{bmatrix}\right\|_2 \le x + t_1$$ (rotated SOCP),
   - $$\left\|\begin{bmatrix} x \\ 2 \end{bmatrix}\right\|_2 \le t_2$$ (SOCP).
4. **Evaluate at the boundary $$x = 1$$ vs. $$x = 2$$**: At $$x = 1$$, $$f(1) = 1 + \sqrt{5} \approx 3.236$$; at $$x = 2$$, $$f(2) = 0.5 + \sqrt{8} \approx 3.328$$. Checking derivative $$f'(x) = -x^{-2} + x/\sqrt{x^2 + 4}$$ at $$x = 1$$ gives $$-1 + 1/\sqrt{5} \approx -0.553 < 0$$, and at $$x \approx 1.46$$ it crosses zero—confirming an interior minimum around $$x^\star \approx 1.46$$ with $$f^\star \approx 3.16$$.

Disciplined convex programming (DCP) is the modeling contract used by [CVXPY](https://www.cvxpy.org/): you compose atoms that the library already knows are convex or concave, with rules that *preserve* convexity. If the rewriter accepts the model, a numerical solver (OSQP, SCS, Clarabel, ECOS, …) receives a canonical cone program — the same taxonomy as the rest of this chapter.

This is the Stanford EE364a practice habit: **model first, algorithm second**. For Lasso, SVM, and portfolio QPs you should not hand-code a projected gradient unless you are studying the algorithm.

## The DCP idea in one paragraph

A composition $$f(g(x))$$ is convex when, for example, $$f$$ is convex and increasing and $$g$$ is convex (Boyd & Vandenberghe, Ch. 3). CVXPY implements a finite catalog of such atoms (`norm`, `sum_squares`, `abs`, `quad_over_lin`, `logistic`, …) and rejects expressions it cannot certify. A rejection is not always “the problem is nonconvex” — sometimes you wrote a convex function in a form the rewriter does not see. The fix is to rewrite using known atoms, not to silence the error.

Install once:

```bash
pip install cvxpy numpy
```

## Mini-lab A — Lasso

Given a design matrix $$A\in\mathbb{R}^{m\times n}$$ and responses $$b$$, the Lasso

$$
\min_x \tfrac12\|Ax-b\|_2^2 + \lambda \|x\|_1
$$

is a convex QP in extended form (squared loss is a convex quadratic; $$\|\cdot\|_1$$ is a convex norm). In CVXPY it is three lines of atoms:

```python
import cvxpy as cp
import numpy as np

np.random.seed(0)
m, n = 80, 40
A = np.random.randn(m, n)
x_true = np.zeros(n)
x_true[:5] = np.array([1.2, -0.8, 0.4, 0.0, -1.1])
b = A @ x_true + 0.05 * np.random.randn(m)
lam = 0.2

x = cp.Variable(n)
objective = 0.5 * cp.sum_squares(A @ x - b) + lam * cp.norm1(x)
prob = cp.Problem(cp.Minimize(objective))
prob.solve(solver=cp.OSQP)  # or SCS / CLARABEL
print("status:", prob.status, "opt:", prob.value)
print("nnz ~", np.sum(np.abs(x.value) > 1e-4))
```

Compare the recovered support with `x_true`. Change $$\lambda$$ and watch the sparsity–fit trade-off — the same path proximal gradient will trace in Chapter 09.

## Mini-lab B — hard-margin SVM as a QP

For linearly separable labeled pairs $$(a_i,y_i)$$ with $$y_i\in\{-1,1\}$$, the hard-margin SVM is

$$
\begin{align}
\min_{w,b} \quad & \tfrac12 \|w\|_2^2 \\
\text{s.t.} \quad & y_i(w^\top a_i + b) \ge 1, \quad i=1,\ldots,m.
\end{align}
$$

```python
import cvxpy as cp
import numpy as np

np.random.seed(1)
m, d = 60, 2
a = np.random.randn(m, d)
y = np.sign(a[:, 0] - 0.2 * a[:, 1] + 0.1)
y[y == 0] = 1

w = cp.Variable(d)
b = cp.Variable()
prob = cp.Problem(
    cp.Minimize(0.5 * cp.sum_squares(w)),
    [cp.multiply(y, a @ w + b) >= 1],
)
prob.solve()
print("status:", prob.status, "||w|| =", np.linalg.norm(w.value))
```

If `status` is infeasible, the cloud is not linearly separable — switch to a soft-margin hinge (`cp.pos(1 - cp.multiply(y, a @ w + b))`), which is still DCP.

## What to remember

- DCP is a *sufficient* grammar for convexity, not a complete one.
- The solver, not your Python loop, chooses between simplex, interior-point, and first-order cone methods.
- When a model will not DCP-rewrite (deep nets, most nonconvex ERMs), you leave this chapter and enter [Chapter 26]({{ site.baseurl }}/contents/en/chapter26/) with autodiff ([Chapter 27]({{ site.baseurl }}/contents/en/chapter27/)).

**Exercise.** Replace the Lasso penalty by the elastic net $$\lambda(\alpha\|x\|_1 + \tfrac{1-\alpha}{2}\|x\|_2^2)$$ and confirm CVXPY still accepts the problem. Then try writing $$\|x\|_0$$ — the rewriter should refuse.

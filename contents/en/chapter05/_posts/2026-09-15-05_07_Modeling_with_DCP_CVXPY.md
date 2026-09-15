---
layout: post
title: 05-07 Modeling with DCP and CVXPY
chapter: '05'
order: 12
owner: Nguyen Le Linh
categories:
- chapter05
lang: en
lesson_type: required
---

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

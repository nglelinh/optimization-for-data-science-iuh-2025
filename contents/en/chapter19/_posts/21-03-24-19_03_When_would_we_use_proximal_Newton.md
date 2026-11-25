---
layout: post
title: "19-03 When would we use proximal Newton?"
chapter: '19'
order: 7
owner: Hooncheol Shin
categories:
- chapter19
lang: en
---

Knowing *how* proximal Newton works is only half the battle—a seasoned optimization engineer also knows *when not to use it*. If solving the scaled proximal subproblem costs 100 times more than a proximal gradient step, does $$O(\log\log(1/\epsilon))$$ outer convergence still win? The answer depends sharply on two structural levers: how expensive it is to evaluate $$\nabla g(x)$$ relative to the inner subproblem, and how severely ill-conditioned $$g$$ is.

## Key ideas: The Practical Decision Matrix for Proximal Newton

- **Expensive Smooth Oracle ($$\nabla g$$ Bottleneck):** In logistic Lasso with $$n \gg p$$ (e.g., $$10^5$$ rows, $$200$$ features) or graphical Lasso (where evaluating $$-\log\det\Theta$$ costs $$O(p^3)$$ Cholesky work), every outer gradient evaluation is costly—making proximal Newton's tiny outer iteration count a massive win.
- **Cheap Inner Quadratic Subproblem:** When $$h(x) = \lambda \|x\|_1$$ and active-set screening shrinks the working set to $$s \ll p$$ nonzero variables, coordinate descent solves the inner quadratic subproblem in microseconds—far cheaper than touching the full dataset again.
- **High-Accuracy vs. Low-Accuracy Regimes:** If you only need $$10^{-2}$$ relative accuracy (e.g., early-stopped deep learning), first-order FISTA wins; if you need $$10^{-8}$$ accuracy for statistical inference or dual certificates, proximal Newton's quadratic local convergence dominates.
- **Inexact Subproblem Solves (Warm-Started Inner Loops):** In practice you never solve the inner subproblem to machine precision at iteration 1; warm-starting coordinate descent from the previous outer step and tightening inner tolerance progressively preserves superlinear outer speed at minimal cost.

### Worked example: Break-Even FLOP Audit (PG vs. Proximal Newton)

Suppose you are fitting an $$\ell_1$$-penalized logistic regression with $$n = 100{,}000$$ samples, $$p = 200$$ features, condition number $$\kappa = 10^4$$, and target accuracy $$\epsilon = 10^{-8}$$.

1. **Cost of one Proximal Gradient (FISTA) iteration:**
   Computing $$X \beta$$ and $$X^T(p - y)$$ costs $$\approx 2np = 4 \times 10^7$$ FLOPs; soft-thresholding costs $$O(p) \approx 200$$ FLOPs (negligible).
   To reach $$\epsilon = 10^{-8}$$ with condition number $$\kappa = 10^4$$, accelerated proximal gradient needs roughly $$\sqrt{\kappa}\log(1/\epsilon) \approx 100 \times 18.4 \approx 1{,}840$$ iterations:
   $$\text{Total FISTA cost} \approx 1{,}840 \times (4 \times 10^7) \approx 7.4 \times 10^{10} \text{ FLOPs}.$$
2. **Cost of one Proximal Newton (`glmnet`) iteration:**
   - Computing $$\nabla g$$ and $$H = X^T W X$$ costs $$\approx np^2 = 4 \times 10^9$$ FLOPs? Wait—we don't even form $$H$$ densely for all $$p$$ if only $$s = 20$$ features are active, or even *if* we form the full $$200 \times 200$$ matrix $$X^T W X$$ via BLAS-3: $$np^2/2 \approx 2 \times 10^9$$ FLOPs.
   - Solving the $$200 \times 200$$ inner Lasso via 20 sweeps of coordinate descent costs $$20 \times p^2 = 8 \times 10^5$$ FLOPs (four orders of magnitude smaller!).
   - Reaching $$\epsilon = 10^{-8}$$ takes only $$\approx 6$$ outer Newton iterations:
   $$\text{Total Proximal Newton cost} \approx 6 \times (2 \times 10^9) \approx 1.2 \times 10^{10} \text{ FLOPs}.$$
3. **Verdict:**
   Even forming the full dense Hessian, Proximal Newton is **6× faster** in FLOPs (and often **20× faster** in wall-clock time due to cache-friendly BLAS-3 `X^T W X` and active-set screening). Flip the dimensions to $$n = 200, p = 100{,}000$$, however, and forming $$H \in \mathbb{R}^{p \times p}$$ becomes impossible—immediately tipping the choice back to FISTA or L-BFGS!

When is the proximal Newton method a good choice?

To understand when it is useful, let us compare the proximal Newton method with proximal gradient descent on the following problem.

**Problem**: $$\min_x g(x) + h(x)$$

## Proximal gradient descent vs. proximal Newton

| **Proximal gradient descent** |**Proximal Newton** | 
| -------- | -------- |
| Minimizes $$\frac{1}{2} \parallel b - x \parallel_2^2 + h(x)$$ at each step | Minimizes $$b^T x + x^T A x + h(x)$$ at each step | 
| The prox operator is usually available in closed form | The prox operator usually has no closed form |
| Cheap iterations | Very expensive iterations (more expensive than Newton's method) | 
| Convergence rate of gradient descent <br> $$O(1/\epsilon)$$ | Convergence rate of Newton's method <br> $$O(\log \log 1/\epsilon)$$ | 

The two methods look similar, but they actually do very different things.

Therefore, the proximal Newton method is worth using when we have a fast inner optimizer for the scaled prox problem (quadratic $$+\ h$$), so that very few outer iterations are needed. When $$h$$ is a separable function, the most commonly used inner optimizer is coordinate descent.

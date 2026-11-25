---
layout: post
title: 23 Coordinate Descent
chapter: '23'
order: '1'
owner: YoungJae Choung
categories:
- chapter23
lang: en
---

At first glance, Coordinate Descent looks almost embarrassingly naive: instead of moving along the full gradient in $$\mathbb{R}^p$$, freeze $$p - 1$$ variables, minimize along a single coordinate axis, and cycle to the next. Why would anyone trade a sophisticated full-gradient direction for axis-aligned baby steps? Yet in modern high-dimensional statistics—most famously in `glmnet` for Lasso and Elastic Net—Coordinate Descent routinely crushes gradient descent and even accelerated proximal gradient by an order of magnitude. The secret is that every single coordinate update uses the *freshest* information immediately (Gauss–Seidel style) and exploits closed-form 1D minimizers with zero line-search overhead.

## Background Knowledge Map: Why Coordinate-Wise Optimization Dominates High-Dimensional Regression

- **Gauss–Seidel vs. Jacobi Updates:** Full gradient descent updates all $$p$$ coordinates simultaneously from the same stale point (Jacobi). Coordinate descent updates coordinate $$i$$ immediately and feeds the new $$x_i^{(k)}$$ into coordinate $$i+1$$ (Gauss–Seidel), enabling larger effective coordinate-wise step sizes $$1/L_i$$ instead of the conservative global $$1/L$$.
- **Separability and Nonsmooth Convexity:** Tseng’s theorem guarantees global convergence of coordinate descent for composite functions $$f(x) = g(x) + \sum_{i=1}^p h_i(x_i)$$ whenever $$g$$ is smooth convex and the nonsmooth penalty separates across coordinates (like $$\lambda \|x\|_1$$). Without separability, coordinate descent can get stuck at non-optimal kinks!
- **Coordinate Selection Rules:** Cyclic sweeps are cache-friendly and deterministic; randomized coordinate descent (sampling coordinate $$i$$ proportionally to $$L_i$$) yields clean complexity bounds; greedy (Gauss–Southwell) selection picks the coordinate with the largest gradient magnitude.
- **Residual Maintenance for $$O(n)$$ Updates:** In linear models $$y - X\beta$$, updating a single coordinate $$\beta_j \to \beta_j^+$$ lets us refresh the residual vector $$r \leftarrow r - (\beta_j^+ - \beta_j) X_j$$ in $$O(n)$$ time, making one full sweep of $$p$$ coordinates cost $$O(np)$$—the exact same cost as a single full gradient!

### Step-by-Step Worked Example (Read Slowly): One Cyclic Coordinate Descent Sweep on a 2D Quadratic

Minimize $$f(x_1, x_2) = x_1^2 + 2 x_2^2 + 2 x_1 x_2 - 4 x_1 - 6 x_2$$ starting from $$x^{(0)} = (0, 0)^\top$$. (The exact minimizer satisfies $$2x_1 + 2x_2 = 4$$ and $$2x_1 + 4x_2 = 6$$, giving $$x^\star = (1, 1)^\top$$ with $$f(x^\star) = -5$$.)

1. **Update $$x_1$$ holding $$x_2 = 0$$ fixed:**
   Set $$\frac{\partial f}{\partial x_1} = 2 x_1 + 2 x_2 - 4 = 0 \implies x_1^{(1)} = 2 - x_2^{(0)} = 2$$.
   Objective drops from $$f(0, 0) = 0$$ to $$f(2, 0) = 4 - 8 = -4$$.
2. **Update $$x_2$$ using the NEW $$x_1^{(1)} = 2$$:**
   Set $$\frac{\partial f}{\partial x_2} = 4 x_2 + 2 x_1^{(1)} - 6 = 0 \implies x_2^{(1)} = \frac{6 - 2(2)}{4} = 0.5$$.
   Objective drops further to $$f(2, 0.5) = 4 + 0.5 + 2 - 8 - 3 = -4.5$$.
3. **Second sweep to verify rapid contraction:**
   - $$x_1^{(2)} = 2 - 0.5 = 1.5$$,
   - $$x_2^{(2)} = \frac{6 - 2(1.5)}{4} = 0.75$$, giving $$f(1.5, 0.75) = -4.875$$.
4. **Notice the geometric rate:** Error in $$x_2$$ shrinks by exactly a factor of $$1/2$$ each sweep: $$1 \to 0.5 \to 0.25$$, converging monotonically without ever tuning a step size $$\eta$$.

Coordinate descent is an optimization algorithm that iteratively moves along each coordinate axis to find the minimum of the objective function. At each iteration, according to a coordinate selection rule, it determines a coordinate axis (coordinate) or coordinate block, then minimizes the function along the direction of that axis while keeping the unselected coordinate axes or coordinate blocks fixed (exactly or inexactly).

Coordinate descent can be utilized not only with gradient-based methods but also with gradient-free methods. Additionally, depending on the case, line search can be used to determine appropriate step sizes for each axis [16].

Coordinate descent is very simple and easy to implement, and shows very good performance when carefully implemented for appropriate problems.

**Examples:** lasso regression, lasso GLMs (under proximal Newton), SVMs, group lasso, graphical lasso (applied to the dual), additive modeling, matrix completion, regression with nonconvex penalties

## References and Further readings

**Early coordinate descent in optimization:**
* D. Bertsekas and J. Tsitsiklis (1989), "Parallel and distributed computation: numerical methods"
* Z. Luo and P. Tseng (1992), "On the convergence of the coordinate descent method for convex differentiable minimization"
* J. Ortega and W. Rheinboldt (1970), "Iterative solution of nonlinear equations in several variables"
* P. Tseng (2001), "Convergence of a block coordinate descent method for nondifferentiable minimization"

**Early coordinate descent references in statistics and ML:**
* I. Daubechies and M. Defrise and C. De Mol (2004), "An iterative thresholding algorithm for linear inverse problems with a sparsity constraint"
* J. Friedman and T. Hastie and H. Hoefling and R. Tibshirani (2007), "Pathwise coordinate optimization"
* W. Fu (1998), "Penalized regressions: the bridge versus the lasso"
* T. Wu and K. Lange (2008), "Coordinate descent algorithms for lasso penalized regression"
* A. van der Kooij (2007), "Prediction accuracy and stability of regression with optimal scaling transformations"

**Coordinate descent applications:**
* O. Banerjee and L. Ghaoui and A. d'Aspremont (2007), "Model selection through sparse maximum likelihood estimation"
* J. Friedman and T. Hastie and R. Tibshirani (2007), "Sparse inverse covariance estimation with the graphical lasso"
* J. Friedman and T. Hastie and R. Tibshirani (2009), "Regularization paths for generalized linear models via coordinate descent"
* C.J. Hsieh and K.W. Chang and C.J. Lin and S. Keerthi and S. Sundararajan (2008), "A dual coordinate descent method for large-scale linear SVM"
* R. Mazumder and J. Friedman and T. Hastie (2011), "SparseNet: coordinate descent with non-convex penalties"
* J. Platt (1998), "Sequential minimal optimization: a fast algorithm for training support vector machines"

**Recent theory for coordinate descent:**
* A. Beck and L. Tetruashvili (2013), "On the convergence of block coordinate descent type methods"
* Y. Nesterov (2010), "Efficiency of coordinate descent methods on huge-scale optimization problems"
* J. Nutini, M. Schmidt, I. Laradji, M. Friedlander, H. Koepke (2015), "Coordinate descent converges faster with the Gauss-Southwell rule than random selection"
* A. Ramdas (2014), "Rows vs columns for linear systems of equations—randomized Kaczmarz or coordinate descent?"
* P. Richtarik and M. Takac (2011), "Iteration complexity of randomized block-coordinate descent methods for minimizing a composite function"
* A. Saha and A. Tewari (2013), "On the nonasymptotic convergence of cyclic coordinate descent methods"
* S. Wright (2015), "Coordinate descent algorithms"

**Screening rules and graphical lasso references:**
* L. El Ghaoui and V. Viallon and T. Rabbani (2010), "Safe feature elimination in sparse supervised learning"
* R. Tibshirani, J. Bien, J. Friedman, T. Hastie, N. Simon, J. Taylor, and R. J. Tibshirani (2011), "Strong rules for discarding predictors in lasso-type problems"
* R. Mazumder and T. Hastie (2011), "The graphical lasso: new insights and alternatives"
* R. Mazumder and T. Hastie (2011), "Exact covariance thresholding into connected components for large-scale graphical lasso"
* J. Wang, P. Wonka, and J. Ye (2015), "Lasso screening rules via dual polytope projection"
* D. Witten and J. Friedman and N. Simon (2011), "New insights and faster computations for the graphical lasso"

**Convergence analysis:**<br>
Here is a brief introduction to the research flow of coordinate descent convergence analysis.

* Convergence of coordinate-wise minimization for solving linear systems, the Gauss-Seidel method, is a classic topic. E.g., see Golub and van Loan (1996), or Ramdas (2014) for a modern treatment that looks at randomized coordinate descent
* Nesterov (2010) considers randomized coordinate descent for smooth functions and shows that it achieves a rate O(1/ε) under a Lipschitz gradient condition, and a rate O(log(1/ε)) under strong convexity
* Richtarik and Takac (2011) extend and simplify these results, considering smooth plus separable functions, where now each coordinate descent update applies a prox operation
* Saha and Tewari (2013) consider minimizing l1 regularized functions of the form g(β) + λ∥β∥1, for smooth g, and study both cyclic coordinate descent and cyclic coordinate-wise minimization. Under (very strange) conditions on g, they show both methods dominate proximal gradient descent in iteration progress
* Beck and Tetruashvili (2013) study cyclic coordinate descent for smooth functions in general. They show that it achieves a rate O(1/ε) under a Lipschitz gradient condition, and a rate O(log(1/ε)) under strong convexity. They also extend these results to a constrained setting with projections
* Nutini et al. (2015) analyze greedy coordinate descent (called Gauss-Southwell rule), and show it achieves a faster rate than randomized coordinate descent for certain problems
* Wright (2015) provides some unification and a great summary. Also covers parallel versions (even asynchronous ones)
* General theory is still not complete; still unanswered questions (e.g., are descent and minimization strategies the same?)

## 2026 applications (optional)

Pathwise CD is still how glmnet and `sklearn.linear_model.lasso_path` fit sparse GLMs. The 2023 JSS paper extends glmnet to *every* GLM family; skglm (NeurIPS 2022) adds working sets and nonconvex penalties at a million features; LIBLINEAR dual CD still trains linear SVMs. See [23-05 Modern applications of coordinate descent]({% multilang_post_url contents/chapter23/2026-09-16-23_05_modern_applications %}) after the Lasso / pathwise examples.
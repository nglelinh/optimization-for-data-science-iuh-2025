---
layout: post
title: '07-03-03 Example: Lasso Optimality Condition'
chapter: '07'
order: 9
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---

Why does Lasso regression—introduced by Robert Tibshirani in 1996—automatically zero out irrelevant features while Ridge regression keeps every feature nonzero? The secret isn't heuristic magic; it sits right inside the subgradient optimality condition $$0 \in \partial\bigl(\frac{1}{2}\|y - X\beta\|_2^2 + \lambda\|\beta\|_1\bigr)$$, which turns feature selection into a crisp correlation threshold between each predictor column $$X_j$$ and the residual $$y - X\beta$$!

## Background Knowledge Map: Subgradient Anatomy of the Lasso

1. **Decomposing the Lasso Objective**: $$F(\beta) = \frac{1}{2}\|y - X\beta\|_2^2 + \lambda\|\beta\|_1$$ sums a smooth quadratic data-fit term (gradient $$-X^T(y - X\beta)$$) and a nonsmooth separable $$\ell_1$$ penalty (subdifferential $$\lambda v$$ where $$v_j = \operatorname{sign}(\beta_j)$$ if $$\beta_j \neq 0$$, and $$v_j \in [-1, 1]$$ if $$\beta_j = 0$$).
2. **Coordinate-Wise Optimality (The Correlation Law)**: Setting $$0 \in -X^T(y - X\beta) + \lambda v$$ gives, for every feature $$j = 1, \dots, p$$:
   - If $$\beta_j^\star \neq 0$$: $$X_j^T(y - X\beta^\star) = \lambda \operatorname{sign}(\beta_j^\star)$$ (residual correlation hits *exactly* $$\pm \lambda$$).
   - If $$\beta_j^\star = 0$$: $$|X_j^T(y - X\beta^\star)| \le \lambda$$ (residual correlation is too weak to overcome the $$\lambda$$ threshold!).
3. **The Critical Regularization Threshold $$\lambda_{\max}$$**: Plugging $$\beta^\star = 0$$ into the condition shows that **all** coefficients are zero if and only if $$\lambda \ge \lambda_{\max} = \|X^T y\|_\infty = \max_j |X_j^T y|$$.
4. **Equicorrelation & Active Set**: Every selected (nonzero) feature has the exact same absolute inner product $$\lambda$$ with the final residual—the geometric foundation of LARS and coordinate-descent Lasso solvers (like `glmnet`).

### Step-by-Step Worked Example (Read Slowly): Checking Lasso Optimality and Finding $$\lambda_{\max}$$

Consider a 2-feature Lasso problem with orthogonal columns:
$$X = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \qquad y = \begin{bmatrix} 5 \\ 1 \end{bmatrix}, \qquad \lambda = 2.$$

1. **Compute $$\lambda_{\max} = \|X^T y\|_\infty$$**:
   $$X^T y = (5, 1)^T \implies \lambda_{\max} = \max(|5|, |1|) = 5.$$
   Since $$\lambda = 2 < 5$$, at least one feature will be nonzero.
2. **Test the candidate solution $$\beta^\star = (3, 0)^T$$**:
   - Residual: $$r = y - X\beta^\star = (5 - 3,\; 1 - 0)^T = (2,\; 1)^T$$.
   - Feature correlations $$X^T r = (2,\; 1)^T$$.
3. **Verify both coordinate optimality rules at $$\lambda = 2$$**:
   - Feature 1 ($$\beta_1^\star = 3 > 0$$): $$X_1^T r = 2 = \lambda \operatorname{sign}(3) = +2$$ — **satisfied!**
   - Feature 2 ($$\beta_2^\star = 0$$): $$|X_2^T r| = |1| = 1 \le \lambda = 2$$ — **satisfied!**
4. **Conclusion**: $$\beta^\star = (3, 0)^T$$ satisfies $$0 \in \partial F(\beta^\star)$$, so it is the exact global Lasso solution—Feature 2 is cleanly eliminated because its signal ($$1$$) falls below the threshold $$\lambda = 2$$.

For the lasso problem given below,
>
\begin{equation}
\min_{\beta} \frac{1}{2}  \| y-X\beta \|_2^2 + \lambda \| \beta \|_1
\end{equation}

where $$y \in \mathbb{R}^n$$, $$X \in \mathbb{R}^{n \times p}$$, $$\lambda \geq 0$$.

The subgradient optimality condition for this problem can be expressed as:
>
$$
\eqalign{
0 \in \partial\left(\frac{1}{2} \| y-X\beta \|_2^2 + \lambda \| \beta \|_1\right)
&\quad \Longleftrightarrow \quad 0 \in - X^T (y-X\beta) + \lambda \partial  \| \beta \|_1 \\
&\quad \Longleftrightarrow \quad X^T (y-X\beta)  = \lambda v \\
& \quad \text{for some } v \in \partial  \| \beta \|_1
}\\
$$

Here, for a point $$\beta=(\beta_1,\beta_2,\dots,\beta_p )$$, the subgradient $$v=(v_1,v_2,\dots,v_p)$$ is given by:

$$
v_i = 
\begin{cases}
 1   &\text{if } \beta_i > 0 \\
-1   &\text{if } \beta_i < 0 \\
[-1,1]   &\text{if } \beta_i = 0
\end{cases}
, i \in \{1,2,\dots,p \}
$$

Any $$\beta$$ satisfying the following is optimal:
>
\begin{equation}
X^T(y-X\beta) = \lambda v 
\end{equation}

That is, for the optimal $$\beta$$, the following conditions hold:
>
$$
\begin{cases}
X_i^T(y-X\beta) = \lambda \cdot \text{sign}(\beta_i) &\text{if } \beta_i \neq 0 \\
 |X_i^T(y-X\beta)|  \leq \lambda &\text{if } \beta_i = 0 
\end{cases}$$

Here, $$X_i, i \in \{1,2,\dots, p \}$$ denotes the $$i$$th column of the matrix $$X$$.

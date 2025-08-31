---
layout: post
title: "07-03-03 Example: Lasso Optimality Condition"
chapter: "07"
order: 9
owner: "Kyeongmin Woo"
---


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

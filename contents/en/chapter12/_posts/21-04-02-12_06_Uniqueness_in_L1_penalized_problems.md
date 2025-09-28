---
layout: post
title: 12-06 Uniqueness in L1 penalized problems
chapter: '12'
order: '7'
owner: Wontak Ryu
categories:
- chapter12
lang: en
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
displayAlign: "center"
});
</script>

The following $$L1$$ penalized linear regression problem is also well known as the lasso problem.

>$$
>\begin{align}
>&&&\hat{\beta} \in \text{argmin}_{\beta \in \mathbb{R}^p} \frac{1}{2} \| y - X\beta \|^2_2 + \lambda \|\beta\|_1, \qquad \\\\
>&& \text{ --- (1) } &\text{given } y \in \mathbb{R}^n, \\\\
>&&& \text{ a matrix } X \in \mathbb{R}^{n \text{ x } p} \ \text{ of predictor variables,} \\\\
>&&& \text{and a tuning parameter} \lambda \ge 0.
>\end{align}
>$$

The above Lasso problem has a unique solution when it is strictly convex, i.e., when $$rank(X) = p$$. On the other hand, when $$rank(X) < p$$ (when it is not strictly convex), it may have infinitely many solutions (Reference: [Underdetermined system](https://en.wikipedia.org/wiki/Underdetermined_system)).

- Note that if the number of variables (p) is greater than the number of observations (n), then $$rank(X)$$ is necessarily less than p.<br/>

Interestingly, in some special cases, the Lasso problem is guaranteed to have a unique solution regardless of the dimension of $$X$$ [13].

>**Theorem:** When the function $$f$$ is differentiable and strictly convex, $$\lambda > 0$$, and $$X \in \mathbb{R}^{n \times p}$$ follows some continuous probability distribution on $$\mathbb{R}^{np}$$, the following optimization problem always has a unique solution. Moreover, the solution consists of at most $$min\{n,p\}$$ nonzero components. There are no restrictions on the dimension of $$X$$. (That is, it is valid even when p >> n)

## Basic facts and the KKT conditions

> **Lemma 1.** For arbitrary $$y, X, \lambda \ge 0$$, the lasso problem (1) has the following properties.
> 
> 1. It has either a unique solution or infinitely many solutions.
> 2. All lasso solutions $$\hat{\beta}$$ have the same $$X\hat{\beta}$$ value.
> 3. When $$\lambda > 0$$, all lasso solutions $$\hat{\beta}$$ have the same $$l_1$$ norm ($$\|\hat{\beta}\|_1$$).

> **Proof.**<br/>
> 
> 1. If (1) has two solutions $$\hat{\beta}^{(1)}$$, $$\hat{\beta}^{(2)}$$, then for any $$0 < \alpha < 1$$, $$\alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)}$$ is also a solution, so infinitely many solutions exist.<br/>
> 
> 2. & 3. Suppose there are two solutions $$\hat{\beta}^{(1)}$$, $$\hat{\beta}^{(2)}$$. Let the optimal value be $$c^\star$$. Then for any solution $$\alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)}$$ ($$0 < \alpha < 1$$), the following equality must always hold.
> 
> >$$
> >\begin{align}
> >&\frac{1}{2} \| y - X(\alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)}) \|_2^2 + \lambda \| \alpha \hat{\beta}^{(1)} + (1 - \alpha) \hat{\beta}^{(2)} \|_1 \\
> >& = \alpha c^\star + (1-\alpha) c^\star = c^\star
> >\end{align}
> >$$
> 
> To satisfy this equality, $$X\hat{\beta}$$ must always have the same value for any solution $$\hat{\beta}$$, and when $$\lambda > 0$$, $$\|\hat{\beta}\|_1$$ must also always be the same.

Returning to the beginning, the KKT conditions for the lasso problem (1) are as follows.

>$$
>\begin{align}
>&&X^T (y - X\hat{\beta}) = \lambda \gamma, \qquad \text{ --- (2)} \\\\
>&&\gamma_i \in 
>\begin{cases}
>\{ sign(\hat{\beta_i}) \} & if \hat{\beta_i} \neq 0 \\\\
>[-1, 1] & if \hat{\beta_i} = 0,
>\end{cases} \\\\
>&&\text{for } i = 1, \dots, p. \text{ --- (3)} \\\\
>&&\text{Here } \gamma \in \mathbb{R}^p \text{ is called a subgradient of the function } \\
>&&f(x) = \| x \|_1 \text{ evaluated at } x = \hat{\beta}.
>\end{align}
>$$

That is, the solution $$\hat{\beta}$$ of (1) satisfies (2) and (3) for some $$\gamma$$. Let us try to use the KKT conditions obtained above to convert the condition for the lasso solution into a more explicit form. For the sake of simplicity in the subsequent derivation, we assume $$\lambda > 0$$.

First, we define the equicorrelation set $$\mathcal{E}$$ as follows. $$\mathcal{E}$$ is a set containing all indices $$i$$ where $$\hat{\beta}_i \neq 0$$ and all indices $$j$$ where $$\hat{\beta}_j = 0$$ and $$\vert\gamma_j\vert = 1$$.

$$
\mathcal{E} = \{ i \in \{1, \dots, p \} : \vert X_i^T (y - X\hat{\beta}) \vert = \lambda \}. \qquad \text{ --- (4)}
$$

Also, we define the equicorrelation sign $$s$$ as follows. Here, $$X_\mathcal{E}$$ means a matrix obtained by replacing all columns other than column $$i$$ where $$i \in \mathcal{E}$$ in matrix $$X$$ with zero vectors.

$$
s = sign(X^T_\mathcal{E} (y -X\hat{\beta})). \qquad \text{ --- (5)}
$$

Here, $$\mathcal{E}, s$$ can be expressed as follows with respect to $$\gamma$$: $$\mathcal{E} = \{i \in \{1, \dots, p \} : \vert \gamma_i \vert = 1 \}$$ and $$s = \gamma_{\mathcal{E}}$$. Also, by Lemma 1-2, since $$X\hat{\beta}$$ has a unique value, this implies that $$\mathcal{E}$$ and $$s$$ are unique.

By the definition of the subgradient $$\gamma$$ in (3), we can see that $$\hat{\beta}_{-\mathcal{E}} = 0$$ for all lasso solutions $$\hat{\beta}$$. Therefore, expressing (2) for the $$\mathcal{E}$$ block gives the following.

$$
X^T_\mathcal{E} ( y - X_\mathcal{E} \hat{\beta_\mathcal{E}} ) = \lambda \gamma_\mathcal{E}= \lambda s. \qquad \text{ --- (6)}
$$

Multiplying both sides of (6) by $$X^T_\mathcal{E} (X^T_\mathcal{E})^+$$ gives the following organization ($$(X^T_\mathcal{E})^+$$ is the pseudoinverse matrix of $$X^T_\mathcal{E}$$).

$$
\begin{align}
& X^T_\mathcal{E} X_\mathcal{E} \hat{\beta_\mathcal{E}} = X^T_\mathcal{E} ( y - (X^T_\mathcal{E})^+ \lambda s) \\\\
\Leftrightarrow & X_\mathcal{E} \hat{\beta_\mathcal{E}} = X^T_\mathcal{E} (X^T_\mathcal{E})^+ ( y - (X^T_\mathcal{E})^+ \lambda s).
\end{align}
$$

Since $$X\hat{\beta} = X_\mathcal{E} \hat{\beta_\mathcal{E}}$$, the above equation equals the following.

$$
X \hat{\beta} = X^T_\mathcal{E} (X^T_\mathcal{E})^+ ( y - (X^T_\mathcal{E})^+ \lambda s), \qquad \text{ --- (7)}
$$

And any lasso solution $$\hat{\beta}$$ is as follows.

$$
\begin{align}
& \hat{\beta_{-\mathcal{E}}} = 0 \text{ and } \hat{\beta_{\mathcal{E}}} = (X^T_\mathcal{E})^+ ( y - (X^T_\mathcal{E}) + b, \qquad \text{ --- (8)} \\\\
& \text{where } b \in null(X_\mathcal{E}).
\end{align}
$$

## Sufficient conditions for uniqueness

For the uniqueness of $$\hat{\beta_{\mathcal{E}}}$$ in (8) to be guaranteed, $$b=0$$ must be satisfied (because $$(X^T_\mathcal{E})^+ ( y - (X^T_\mathcal{E})$$ is unique). Noting that $$b=0$$ must be satisfied and transforming the equation in (8), we obtain the following conclusion.

>**Lemma 2.** For arbitrary $$y, X, \lambda > 0$$, if $$null(X_\mathcal{E}) = \{0\}$$, or $$rank(X_\mathcal{E}) = \vert\mathcal{E}\vert$$ ([reference](https://www.quora.com/When-the-null-space-of-a-matrix-is-the-zero-vector-the-matrix-is-invertible-Why/answer/Alexander-Farrugia)), then the lasso solution becomes unique, and this equals the following.
>
>$$
>\begin{align}
>&& \hat{\beta_{-\mathcal{E}}} = 0 \text{ and } \hat{\beta_{\mathcal{E}}} = (X^T_\mathcal{E}X^T_\mathcal{E})^{-1} ( X^T_\mathcal{E} y - \lambda s), \qquad \text{ --- (9)} \\\\
>&& \text{where } \mathcal{E} \text{ and } s \text{ are the equicorrelation set and signs as defined in (4) and (5)}.
>\end{align}
>$$

As a reference, this solution consists of at most $$min\{n, p\}$$ nonzero components.

So what more natural condition (for $$X$$) implies $$null(X_\mathcal{E}) = \{0\}$$? Let us first assume $$null(X_\mathcal{E}) \neq \{0\}$$ before exploring this. In this case, for some $$i \in \mathcal{E}$$, the following equation is satisfied.

$$
X_i = \sum_{j \in \mathcal{E} \backslash \{i\} } c_j X_j,\\\\
\text{where } c_j \in \mathbb{R}, j \in \mathcal{E}.
$$

Multiplying both sides of the above equation by $$s_i$$ and multiplying the right side by $$s_j s_j = 1$$.

$$
s_i X_i = \sum_{j \in \mathcal{E} \backslash \{i\} } (s_i s_j c_j) \cdot (s_j X_j). \qquad \text{ --- (10)}
$$

If we define $$r = y - X \hat{\beta}$$ as $$r$$ (lasso residual), then for any $$j \in \mathcal{E}$$, $$X_j^T r = s_j \lambda$$ is satisfied. Multiplying $$r$$ to both sides of (10) above gives an inequality for $$\lambda$$. (assuming $$\lambda > 0$$)

$$
\lambda = \sum_{j \in \mathcal{E} \backslash \{i\} } (s_i s_j c_j) \lambda \quad \text{ and } \quad \sum_{j \in \mathcal{E} \backslash \{i\} } (s_i s_j c_j) = 1.
$$

That is, if $$null(X_\mathcal{E}) \neq \{0\}$$, then for some $$i \in \mathcal{E}$$, the following equation holds.

$$
s_iX_i = \sum_{j \in \mathcal{E} \backslash \{i\} } a_j \cdot s_j X_j, \text{ with } \sum_{j \in \mathcal{E} \backslash \{i\} } a_j = 1.
$$

The above equation means that $$s_iX_i$$ exists on the affine span of $$s_j X_j, j \in \mathcal{E} \backslash \{i\}$$. Also, this means that any subset containing k+2 elements can represent only a maximum k-dimensional affine space.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter12/l1_uniqueness.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Fig 1] 4 elements on 2-dimensional affine space [3]</figcaption>
</p>
</figure>

What we want is for matrix $$X \in \mathbb{R}^{n \text{ x } p}$$ to satisfy $$null(X_\mathcal{E}) = \{0\}$$, which means that the columns of matrix $$X$$ are in [general position](https://en.wikipedia.org/wiki/General_position). In other words, no k-dimensional affine subspace contains more than k+1 elements in the set.

>**Lemma 3.** If the columns of matrix $$X$$ are in general position, then the lasso solution for arbitrary $$y$$ and $$\lambda > 0$$ is unique. Also, this solution satisfies (9).

So what matrix $$X$$ can always satisfy the above condition? The conclusion is as follows.

>**Lemma 4.** If all elements of matrix $$X \in \mathbb{R}^{n \text{ x } p}$$ follow a continuous probability distribution on $$\mathbb{R}^{np}$$, then the lasso solution for arbitrary $$y$$ and $$\lambda > 0$$ is unique and always satisfies (9).

Because when following a continuous probability distribution, all column vectors are linearly independent. ([reference](https://math.stackexchange.com/questions/432447/probability-that-n-vectors-drawn-randomly-from-mathbbrn-are-linearly-ind?rq=1))

## General convex loss functions

The same content can be applied to more general lasso problems [13].

$$
\hat{\beta} \in \text{argmin}_{\beta \in \mathbb{R}^p} f(X\beta) + \lambda \|\beta\|_1, \qquad \text{ --- (11) }
$$

>**Lemma 5.** If all elements of matrix $$X \in \mathbb{R}^{n \text{ x } p}$$ follow a continuous probability distribution on $$\mathbb{R}^{np}$$, then any differentiable and strictly convex function $$f$$ guarantees a unique solution for the problem in (11) for any $$\lambda > 0$$. This solution consists of at most $$min\{n,p\}$$ nonzero components.
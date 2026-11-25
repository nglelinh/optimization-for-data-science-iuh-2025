---
layout: post
title: 21-04 Example - Sparse subspace estimation and sparse plus low rank decomposition
chapter: '21'
order: 5
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

High-dimensional data matrices—from surveillance video streams to gene-expression tables—often hide two completely different structures superimposed on top of each other: a **low-rank background** $$L$$ plus a **sparse foreground** $$S$$ (Robust PCA), or a **low-rank covariance subspace** $$P$$ with **sparse loadings** (Fantope Sparse PCA). Interior-point SDP solvers choke once matrices exceed $$100 \times 100$$, because their Hessians scale as $$O(p^6)$$. **ADMM** handles $$1000 \times 1000$$ matrices effortlessly by splitting the spectral constraint (handled by SVD/eigendecomposition) from the entrywise sparsity constraint (handled by elementwise soft-thresholding)!

## Background Knowledge Map: Spectral + Sparse Matrix Splitting in ADMM

- **Convex Relaxation of Rank (Fantope & Nuclear Norm):** Replacing nonconvex $$\operatorname{rank}(P) = k$$ with the Fantope $$\mathcal{F}^k = \{P : 0 \preceq P \preceq I, \operatorname{tr}(P) = k\}$$ (for Sparse PCA) or replacing $$\operatorname{rank}(L)$$ with the nuclear norm $$\|L\|_\ast = \sum_i \sigma_i(L)$$ (for Robust PCA) yields tractable convex programs with near-optimal statistical recovery.
- **Singular Value Thresholding (SVT) Proximal Map:** The proximal operator of $$\tau\|L\|_\ast$$ is simply taking the SVD $$U \Sigma V^T$$ and soft-thresholding the singular values: $$\mathcal{D}_\tau(M) = U \operatorname{diag}\big((\sigma_i - \tau)_+\big) V^T$$.
- **Fantope Projection:** Projecting a symmetric matrix $$M = Q \Lambda Q^T$$ onto $$\mathcal{F}^k$$ keeps the eigenvectors $$Q$$ intact and projects the eigenvalues $$\lambda_i$$ onto the capped simplex $$\{0 \le \gamma_i \le 1, \sum_i \gamma_i = k\}$$ via a fast 1D bisection!
- **Decoupling Spectral vs. Entrywise Geometry:** In Robust PCA ($$\min \|L\|_\ast + \lambda\|S\|_1 \text{ s.t. } L + S = M$$), ADMM alternates one SVD (for $$L$$) and one elementwise soft-threshold (for $$S$$)—never mixing the two geometries inside a single subproblem!

### Step-by-Step Worked Example (Read Slowly): One ADMM Iteration of Robust PCA ($$L + S = M$$)

Consider a $$2 \times 2$$ data matrix $$M = \begin{bmatrix} 2 & 2 \\ 2 & 5 \end{bmatrix}$$ (a rank-1 matrix $$\begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix}$$ corrupted by a single sparse outlier $$+3$$ in the bottom-right corner!). Solve $$\min \|L\|_\ast + \lambda\|S\|_1$$ s.t. $$L + S = M$$ with $$\lambda = 0.5, \; \rho = 1$$ from $$S^0 = 0, \; W^0 = 0$$.

1. **$$L$$-update (Singular Value Thresholding $$\mathcal{D}_{1/\rho}(M - S^0 - W^0) = \mathcal{D}_1(M)$$):**
   Since $$M$$ is symmetric positive definite, its eigenvalues (and singular values) solve $$(2 - \sigma)(5 - \sigma) - 4 = \sigma^2 - 7\sigma + 6 = 0 \implies \sigma_1 = 6, \; \sigma_2 = 1$$!
   Unit eigenvectors: $$q_1 = \frac{1}{\sqrt{5}}\begin{bmatrix} 1 \\ 2 \end{bmatrix}$$ (for $$\sigma_1 = 6$$) and $$q_2 = \frac{1}{\sqrt{5}}\begin{bmatrix} 2 \\ -1 \end{bmatrix}$$ (for $$\sigma_2 = 1$$).
   Soft-threshold singular values by $$1/\rho = 1$$: $$\tilde{\sigma}_1 = 6 - 1 = 5$$, $$\tilde{\sigma}_2 = (1 - 1)_+ = 0$$!
   Thus $$L^1$$ is immediately **rank 1**:
   $$L^1 = 5 q_1 q_1^T = 5 \cdot \frac{1}{5}\begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}.$$
2. **$$S$$-update (Entrywise soft-thresholding $$S_{\lambda/\rho}(M - L^1 - W^0) = S_{0.5}(M - L^1)$$):**
   $$M - L^1 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \implies S^1 = S_{0.5}\!\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0.5 & 0 \\ 0 & 0.5 \end{bmatrix}.$$
3. **Dual update:**
   $$W^1 = W^0 + (L^1 + S^1 - M) = \begin{bmatrix} -0.5 & 0 \\ 0 & -0.5 \end{bmatrix}.$$
   In just *one* SVD + soft-thresholding pass, ADMM already extracted a clean rank-1 component $$L^1$$ and isolated sparse diagonal residuals!

# Example: Sparse Subspace Estimation and Sparse Plus Low Rank Decomposition

## Sparse Subspace Estimation

Given $$S=X^{T}X, X\in \mathbb{R}^{n\times p}$$, consider the problem of finding a projection that minimizes the Frobenius norm distance between the original $$X$$ and the projected $$X$$:

>$$
>\begin{align}
>&\min_{P} &&||X-XP||^{2}_{F}\\\\
>&\text{subject to} &&\text{rank(P)=k where P is a projection matrix}
>\end{align}
>$$

This problem is non-convex because the set of projection matrices is not a convex set. However, it is known to be equivalent to the following convex problem [[VCLR13]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]. This is also called the subspace estimation problem.

>$$
>\begin{align}
>&\max_{Y} &&tr(SY)\\\\
>&\text{subject to } &&Y\in F_{k} = \left\{Y\in \mathbb{S}^{p} : 0 \preceq Y \preceq I, tr(Y) = k \right\}
>\end{align}
>$$

[VCLR13] discusses solving the sparse version (with added L1 norm) of the subspace estimation problem. For detailed derivation, please refer to the corresponding paper.
>$$
>\begin{align}
>&\max_{Y} &&tr(SY)-\lambda ||Y||_{1}\\\\
>&\text{subject to } &&Y\in F_{k} 
>\end{align}
>$$

where $$F_{k}$$ is the Fantope of order k, as defined in the equation above.

When $$\lambda = 0$$, the above problem is equivalent to standard PCA.

This problem has an SDP form and can be solved using interior point methods. However, this approach is complex to implement and becomes very slow as the problem size increases.

## ADMM Formulation

To solve this problem with ADMM, we reformulate it as follows:
>$$
>\begin{align}
>&\min_{Y,Z} &&-tr(SY)+I_{F_{k}}(Y) + \lambda||Z||_{1}\\\\
>&\text{subject to } &&Y = Z.
>\end{align}
>$$

## ADMM Algorithm

Summarizing the problem, the ADMM steps are as follows: 
 >$$
 >\begin{align}
 >Y^{+} &=  \underset{Y}{\operatorname{argmin}} -tr(SY) + I_{F_{k}}(Y)+\frac{\rho}{2}||Y-Z+W||^{2}_{F}\\\\
 >&=\underset{Y\in F_{k}}{\operatorname{argmin}} \frac{1}{2}||Y-Z+W-\frac{S}{\rho}||^{2}_{F}\\\\
 >&=P_{F_{k}}(Z-W+\frac{S}{\rho})\\\\
 >Z^{+} & = \underset{Z}{\operatorname{argmin}}\lambda||Z||_{1}+\frac{\rho}{2}||Y^{+}-Z+W||^{2}_{F}\\\\
 >&=S_{\frac{\lambda}{\rho}}(Y^{+}+W)\\\\
 >W^{+} &=W+Y^{+}-Z^{+}.
 >\end{align}
 >$$
 
where $$P_{F_{k}}$$ is the fantope projection operator. This is defined by clipping the eigendecomposition $$A= U\Sigma U^{T}, \Sigma = diag(\sigma_{1},...\sigma_{p})$$ [[VCLR13]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]:
>$$
>\begin{align}
>P_{F_{k}}(A) = U\Sigma_{\theta}U^{T}, \: \Sigma_{\theta} = diag(\sigma_{1}(\theta),...\sigma_{p}(\theta))
>\end{align}
>$$

where each $$\sigma_{i}(\theta) = \min\left\{\max\left\{\sigma_{i}-\theta,0\right\},1\right\}$$ and $$\sum^{p}_{i=1}\sigma_{i}(\theta)=k$$.

## Sparse plus low rank decomposition
Given $$M\in \mathbb{R}^{n\times m}$$, the sparse plus low rank decomposition problem is as follows [[CLMW09]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %})]:
>$$
>\begin{align}
>&\min_{L,S} &&||L||_{tr}+\lambda||S||_{1}\\\\
>&\text{subject to } &&L+S=M
>\end{align}
>$$

## Problem Description

The goal of this problem is to decompose the observed matrix $$M$$ into a low rank matrix $$L$$ and a sparse matrix $$S$$. The first term of the objective function is the trace penalty of $$L$$, which minimizes the sum of singular values of $$L$$. The second term uses the $$l_{1}$$ norm on matrix $$S$$ to induce sparsity in $$S$$. $$\lambda$$ is a tuning parameter that balances these two terms. Both the trace norm and $$l_{1}$$ norm are non-smooth, and generally the trace norm is known to be difficult to optimize. Like the sparse subspace estimation problem, this problem has an SDP form and can be solved using interior point methods, but this is also complex and slow. For this problem, ADMM provides somewhat easier update steps.

>$$
>\begin{align}
>L^{+} &= S^{tr}_{\frac{1}{\rho}}(M-S+W)\\\\
>S^{+} &= S^{l_{1}}_{\frac{\lambda}{\rho}}(M-L^{+}+W)\\\\
>W^{+} &= W+M-L^{+}-S^{+}
>\end{align}
>$$

where $$S^{tr}_{\frac{1}{\rho}}$$ is matrix soft-thresholding and $$S^{l_{1}}_{\frac{\lambda}{\rho}}$$ is elementwise soft-thresholding.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/candes.png" alt="[Fig 1] Example of sparse plue low rank decomposition on surveliance camera[3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Example of sparse plue low rank decomposition on surveliance camera[3]</figcaption>
</p>
</figure>

## Application Example

[Fig 1] shows an example of applying sparse plus low rank decomposition to surveillance camera video analysis. From surveillance cameras that film a fixed area for a long time, we can easily separate the low rank part that shares most frames, and the sparse part extracts characteristic parts from specific frames. For example, in [Fig 1], the middle column represents the low rank part and the right column represents the sparse part. As can be confirmed, the low rank part contains background information that appears in almost all frames, and the sparse part contains only characteristic parts that appear only in specific frames.

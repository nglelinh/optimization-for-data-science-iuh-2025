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

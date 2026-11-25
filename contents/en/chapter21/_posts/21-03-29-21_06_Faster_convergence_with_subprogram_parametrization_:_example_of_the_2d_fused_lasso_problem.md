---
layout: post
title: 21-06 Faster convergence with subprogram parametrization - example of the 2d
  fused lasso problem
chapter: '21'
order: 7
owner: Hooncheol Shin
lesson_type: optional
categories:
- chapter21
lang: en
---

Here is an insider secret that separates textbook ADMM users from experts: **the exact same convex problem can have two different ADMM splittings where one converges 50× faster than the other!** Nowhere is this clearer than in **2D Fused Lasso (Total Variation denoising)**. A naive edge-by-edge split introduces a massive auxiliary vector for every pixel difference and crawls across the image; a clever **row-vs.-column splitting** decouples the 2D grid into independent 1D fused-lasso chains (each solvable in $$O(d)$$ linear time via dynamic programming!) that update in *orthogonal* directions and converge dramatically faster!

## Key ideas: Designing Fast ADMM Parametrizations

- **Why Splitting Choice Matters:** ADMM converges fastest when the coupled blocks act along *weakly correlated or orthogonal* subspaces (like horizontal rows vs. vertical columns), minimizing the "ping-pong" lag between $$x$$ and $$z$$.
- **Naive Graph-Difference Splitting ($$D x = z$$):** Setting $$z = D x$$ makes the $$z$$-update trivial soft-thresholding, but forces the $$x$$-update to solve a 2D discrete Poisson system $$(I + \rho D^T D) x = \text{rhs}$$ and decouples information only one pixel per iteration.
- **Orthogonal Row–Column Splitting ($$x = z$$ on 1D Chains):** Splitting the 2D TV penalty into $$\lambda\|D_{\text{row}} x\|_1 + \lambda\|D_{\text{col}} z\|_1$$ subject to $$x = z$$ turns the $$x$$-update into $$d$$ completely independent 1D fused-lasso problems (one per row) and the $$z$$-update into $$d$$ independent 1D problems (one per column)!
- **Linear-Time 1D Fused Lasso Oracles:** Using Condat's or Johnson's $$O(d)$$ dynamic-programming algorithm for 1D TV denoising makes each row/column pass cost only $$O(d^2)$$ total—the same per-iteration cost as soft-thresholding, while propagating information across the *entire* image in a single sweep!

### Worked example: Naive Edge Split vs. Row–Column Split on a $$2 \times 2$$ Image

Consider denoising a $$2 \times 2$$ image $$Y = \begin{bmatrix} 0 & 4 \\ 0 & 4 \end{bmatrix}$$ (a sharp vertical step edge between column 1 and column 2!) with 2D TV penalty $$\lambda = 1$$:
$$\min_{X \in \mathbb{R}^{2 \times 2}} \; \frac{1}{2}\|Y - X\|_F^2 + \underbrace{\sum_{\text{rows}} |X_{i,1} - X_{i,2}|}_{\text{horizontal diffs}} + \underbrace{\sum_{\text{cols}} |X_{1,j} - X_{2,j}|}_{\text{vertical diffs}}.$$

1. **Exact optimum (by symmetry of rows):**
   Both rows are identical (so vertical diffs are $$0$$!), and each row solves the 1D problem $$\min_{a,b} \frac{1}{2}a^2 + \frac{1}{2}(b - 4)^2 + |a - b|$$, giving $$a^\star = 1, \; b^\star = 3$$, so $$X^\star = \begin{bmatrix} 1 & 3 \\ 1 & 3 \end{bmatrix}$$.
2. **Trace 1 iteration of Row–Column ADMM ($$X = Z$$, $$\rho = 1$$, $$Z^0 = Y, W^0 = 0$$):**
   - **Row-wise $$X$$-update** (each row solves $$\min \frac{1}{2}\|Y_{i,:} - X_{i,:}\|^2 + \frac{1}{2}\|X_{i,:} - Z_{i,:}^0\|^2 + |X_{i,1} - X_{i,2}|$$):
     For row 1: $$\min (a - 0)^2 + (b - 4)^2 + |a - b| \implies 2a - 1 = 0 \implies a = 0.5$$ and $$2(b - 4) + 1 = 0 \implies b = 3.5$$.
     Thus $$X^1 = \begin{bmatrix} 0.5 & 3.5 \\ 0.5 & 3.5 \end{bmatrix}$$ (propagating information across the full row immediately!).
   - **Column-wise $$Z$$-update** (each column solves 1D TV on $$X_{:,j}^1$$):
     Since both entries of column 1 equal $$0.5$$ and both entries of column 2 equal $$3.5$$, vertical differences are *already* zero, so $$Z^1 = X^1 = \begin{bmatrix} 0.5 & 3.5 \\ 0.5 & 3.5 \end{bmatrix}$$!
3. **Why it wins:**
   In one sweep, horizontal and vertical structures decoupled orthogonally with zero cross-contamination—and on a $$512 \times 512$$ image, a single row-column sweep propagates boundary information across all 512 pixels at once instead of 1 pixel per iteration!

# Faster Convergence with Subprogram Parametrization

## Introduction

One very interesting property of ADMM is that when solving problems, if we parametrize the small subproblems in a special way, it can show much faster convergence performance than general methods. In the previous consensus ADMM example, the updates optimize over blocks of variables, which is similar to block coordinate descent. Therefore, ADMM can also achieve fast convergence by updating blocks of variables in nearly orthogonal directions.

## 2D Fused Lasso Example

In this section, we will demonstrate the above concepts through examples, designing auxiliary constraints so that the primal updates are in de-correlated directions.

For detailed information, see [RT16], [WSK14], [BS14].

Let's examine the 2D fused lasso or 2D total variation denoising problem, which was one of the examples we looked at in [Chapter 1]({% multilang_post_url contents/chapter01/21-01-07-01_01_optimization_problems %}). Given an image $$Y\in \mathbb{R}^{d\times d}$$, the problem is defined as follows:

>$$
>\begin{align}
>\min_{\Theta}\frac{1}{2}||Y-\Theta||^{2}_{F}+\lambda \sum_{i,j}(|\Theta_{i,j}-\Theta_{i+1,j}|+|\Theta_{i,j}-\Theta_{\Theta_{i,j+1}}|).
>\end{align}
>$$

In this problem, there is a parameter for each pixel of the image, and this parameter matrix is $$\Theta\in \mathbb{R}^{d\times d}$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/2dfussed.png" alt="[Fig 1] Interpretation of the penalty term in 2d fussed lasso[3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Interpretation of the penalty term in 2d fussed lasso[3]</figcaption>
</p>
</figure>

[Fig 1] visually shows the penalty term, which is the second term of the objective function. As can be seen from the defined problem, it aims to reduce the differences between a pixel and its adjacent horizontal and vertical pixels. That is, this penalty term makes the values of neighboring adjacent pixels similar. 

## Vector Form

Summarizing the penalty term as an operator, the problem becomes:
>$$
>\begin{align}
>\min_{\theta}\frac{1}{2}||y-\theta||^{2}_{F} + \lambda||D\theta||_{1}.
>\end{align}
>$$

where $$D\in \mathbb{R}^{m\times n}$$ is the 2D difference operator corresponding to the original equation.

## Forms of ADMM updates for the 2d fused lasso problem
## Forms of ADMM Updates for the 2D Fused Lasso Problem

Now we want to create ADMM steps in two ways by applying auxiliary constraints.

The first approach is to derive ADMM from the vector form created through the 2D difference operator.

>$$
>\begin{align}
>\min_{\theta, z}\frac{1}{2}||y-\theta||^{2}_{2}+\lambda||z||_{1} \qquad \text{subject to   }z = D\theta,
>\end{align}
>$$

The ADMM steps are then derived as follows:
>$$
>\begin{align}
>\theta^{(k)} &= (I+\rho D^{T}D)^{-1}(y+\rho D^{T}(z^{(k-1)}+w^{(k-1)}))\\\\
>z^{(k)} &= S_{\frac{\lambda}{\rho}}(D\theta^{(k)}-w^{(k-1)})\\\\
>w^{(k)} &= w^{(k-1)}+z^{(k-1)}-D\theta ^{(k)}.
>\end{align}
>$$

## Computational Complexity - Vector Form

Solving for $$\theta$$ is equivalent to solving the linear system $$(I+\rho D^{T}D)^{-1}$$. Here, $$D^{T}D$$ becomes the Laplacian matrix $$L=D^{T}D$$ of the 2D grid, which can be solved in $$O(n)$$ operations. The $$z$$ update also requires $$O(n)$$ operations since it involves applying the soft thresholding operator $$S_{t}$$. Therefore, solving ADMM in vector form takes $$O(n)$$ time.

## Matrix Form ADMM

The second approach is to derive ADMM in matrix form, identical to the original problem definition.
>$$
>\begin{align}
>&\min_{\Theta, Z} &&\frac{1}{2}||Y-\Theta||^{2}_{F}+\lambda\sum_{i,j}(|\Theta_{i,j}-\Theta_{i+1,j}+|Z_{i+1,j}-Z_{i,j+1}|)\\\\
>&\text{subject to } &&\Theta = Z
>\end{align}
>$$

The ADMM steps are as follows:
>$$
>\begin{align}
>\Theta_{\cdot \\ , j}^{(k)} &= FL^{1d}_{ \frac{\lambda}{(1+\rho)} } \bigg( \frac{ Y+\rho( Z^{(k-1)}_{\cdot \\ , j}-W_{\cdot \\ ,j}^{(k-1)} ) } {1+\rho} \bigg),\qquad j=1,...,d\\\\
>Z_{i, \cdot}^{(k)} &= FL^{1d}_{\frac{\lambda}{\rho}} \bigg(\Theta_{i, \cdot}^{(k)} + W_{i, \cdot}^{(k-1)} \bigg), \qquad j=1,...,d\\\\
>W^{(k)} &= W^{(k-1)} + \Theta^{(k)} - Z^{(k)} \\\\
>\end{align}
>$$
where $$FL_{\tau}^{1d}(a)$$ is the 1D fused lasso defined as $$FL_{\tau}^{1d}(a) = \underset{x}{\operatorname{argmin}}\frac{1}{2}||a-x||^{2}_{2}+\tau\sum_{i=1}^{d-1}|x_{i}-x_{i+1}|$$.

## Computational Complexity - Matrix Form

The matrix form ADMM can also be performed with $$O(n)$$ time complexity. Both $$\Theta$$ and $$Z$$ are in the form of 1D fused lasso, which has $$O(n)$$ time complexity.

[Fig 2] shows how the original penalty term is separated into 1D fused lasso problems.
 
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/2dfussedlasso.png" alt="[Fig 2]  Interpretation of the matrix form ADMM updates for 2d fused lasso[3]" width="70%">
  <figcaption style="text-align: center;">[Fig 2]  Interpretation of the matrix form ADMM updates for 2d fused lasso[3]</figcaption>
</p>
</figure>


## Image denoising experiments
## Image Denoising Experiments

Now let's revisit the image denoising problem we examined in Chapter 1.

[Fig 3] shows the data and denoised images. [Fig 4] shows a comparison of the two ADMM methods. The "specialized" ADMM in matrix form, which defines constraints by decomposing in vertical/horizontal directions, shows much faster convergence performance than the "standard ADMM" derived in vector form.

[Fig 5] shows the image quality according to ADMM iterations.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/ll1.png" alt="[Fig 3]  Data, exact solution image(300x200 image : n = 60,000).  
left : original image before denoising, right : the exact solution of denoised image[3]" width="70%">
  <figcaption style="text-align: center;">[Fig 3]  Data, exact solution image(300x200 image : n = 60,000).
left : original image before denoising, right : the exact solution of denoised image[3]</figcaption>
</p>
</figure>


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/ll2.png" alt="[Fig 4]  Convergence curves of two ADMM algorithms. black : standard(vector form), red : specialized(matrix form) [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 4]  Convergence curves of two ADMM algorithms. black : standard(vector form), red : specialized(matrix form) [3]</figcaption>
</p>
</figure>


<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/admm_iteration_visualized.png" alt="[Fig 5]  ADMM iterates visualized after k = 10, 30, 50, 100 iterations [3]" width="70%">
  <figcaption style="text-align: center;">[Fig 5]  ADMM iterates visualized after k = 10, 30, 50, 100 iterations [3]</figcaption>
</p>
</figure>

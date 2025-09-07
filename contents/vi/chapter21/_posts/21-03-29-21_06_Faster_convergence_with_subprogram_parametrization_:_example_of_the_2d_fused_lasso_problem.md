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

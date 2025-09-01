---
layout: post
title: 21-06 Faster convergence with subprogram parametrization - example of the 2d
  fused lasso problem
chapter: '21'
order: 7
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

ADMM의 성질 중 무척 흥미to,운 점은 problem solution결to, 있어서 작은 problem(subproblems)들을 특별한 형태to, parametrize하면, 일반적인 method보다 훨씬 빠른 convergence성능을 showing,준다는 것이다. 앞선 consensus ADMM의 예시at, update는 variable들의 block 모음about, optimization를 진행하는 형태를 보이는데, 이는 block coordinate descentand, 유사하다. therefore,, ADMM also, 각 variable들의 block 모음about, 거의 orthogonal한 direction들to, 업데이트하면서 빠른 convergence 속도를 보이게 할 수 있다.

이 절at,는 예시들을 through,, 보조적인 constraint를 가장 primal update가 de-correlate하는 directionwith, 설계함with,써 위의 내용들을 confirming,보고자 한다.

For detailed information, see [RT16], [WSK14], [BS14]를 reference한다.

[1장]({% multilang_post_url contents/chapter01/21-01-07-01_01_optimization_problems %})at, 살펴보았던 예시중 하나인 2d fussed lasso or, 2d total variation denoising problem를 살펴본다. 이미지 $$Y\in \mathbb{R}^{d\times d}$$가 주어졌을when,, problem는 아래and, 같이 정의된다.

>$$
>\begin{align}
>\min_{\Theta}\frac{1}{2}||Y-\Theta||^{2}_{F}+\lambda \sum_{i,j}(|\Theta_{i,j}-\Theta_{i+1,j}|+|\Theta_{i,j}-\Theta_{\Theta_{i,j+1}}|).
>\end{align}
>$$

이 problemat, 이미지의 각 pixelto, about, parameter가 있으며, 이 parameter matrix은 $$\Theta\in \mathbb{d\times d}$$이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/2dfussed.png" alt="[Fig 1] Interpretation of the penalty term in 2d fussed lasso[3]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Interpretation of the penalty term in 2d fussed lasso[3]</figcaption>
</p>
</figure>

[Fig 1]은 objective function의 두번째 항인 penalty 항을 시각적with, showing,준다. 정의된 problemat,도 알 수 있다시피, 한 픽셀about, 인접한 수평한 픽셀, 수직한 픽셀 간의 difference이를 줄이고자 한다. that is,, 이 penalty 항은 주변의 인접한 픽셀들간의 값을 유사한 값with, 만든다. 

Penalty 항의 sum을 operatorto, in summary, problem는 아래and, 같아진다.
>$$
>\begin{align}
>\min_{\theta}\frac{1}{2}||y-\theta||^{2}_{F} + \lambda||D\theta||_{1}.
>\end{align}
>$$

$$D\in \mathbb{m\times n}$$은 원 식to, correspondence되는 2d difference operator이다.

## Forms of ADMM updates for the 2d fused lasso problem
이제 보조적인 constraint를 applying, ADMM step을 두가지 methodwith, creating,보고자 한다.
첫번째to,는 2d difference operator를 through, 만들었던 vector formwith, from, ADMM을 유도하는 것이다.

>$$
>\begin{align}
>\min_{\theta, z}\frac{1}{2}||y-\theta||^{2}_{2}+\lambda||z||_{1} \qquad \text{subject to   }z = D\theta,
>\end{align}
>$$

이어서 ADMM step을 유도하면 as follows:.
>$$
>\begin{align}
>\theta^{(k)} &= (I+\rho D^{T}D)^{-1}(y+\rho D^{T}(z^{(k-1)}+w^{(k-1)}))\\\\
>z^{(k)} &= S_{\frac{\lambda}{\rho}}(D\theta^{(k)}-w^{(k-1)})\\\\
>w^{(k)} &= w^{(k-1)}+z^{(k-1)}-D\theta ^{(k)}.
>\end{align}
>$$

$$\theta$$는 $$ (I+\rho D^{T}D)^{-1}$$의 linear system을 푸는 것and, 같다. 여기서 $$D^{T}D$$는 $$L=D^{T}D$$to, 2d grid의 Laplacianmatrix이 되어 $$O(n)$$의 operationwith, solution결할 수 있다. $$z$$ also, soft thresholding operator $$S_{t}$$to, operation이 이루어지므to,, 동일하게 $$O(n)$$의 operation이 필요하다. therefore, vector 형태to, ADMM을 푸는 것은 $$O(n)$$의 시간이 걸린다.

두번째 methodwith,는 맨 처음의 problem 정의and, 동일하게 matrix 형태to, ADMM을 유도하는 것이다.
>$$
>\begin{align}
>&\min_{\Theta, Z} &&\frac{1}{2}||Y-\Theta||^{2}_{F}+\lambda\sum_{i,j}(|\Theta_{i,j}-\Theta_{i+1,j}+|Z_{i+1,j}-Z_{i,j+1}|)\\\\
>&\text{subject to } &&\Theta = Z
>\end{align}
>$$

ADMM steps는 아래and, 같다.
>$$
>\begin{align}
>\Theta_{\cdot \\ , j}^{(k)} &= FL^{1d}_{ \frac{\lambda}{(1+\rho)} } \bigg( \frac{ Y+\rho( Z^{(k-1)}_{\cdot \\ , j}-W_{\cdot \\ ,j}^{(k-1)} ) } {1+\rho} \bigg),\qquad j=1,...,d\\\\
>Z_{i, \cdot}^{(k)} &= FL^{1d}_{\frac{\lambda}{\rho}} \bigg(\Theta_{i, \cdot}^{(k)} + W_{i, \cdot}^{(k-1)} \bigg), \qquad j=1,...,d\\\\
>W^{(k)} &= W^{(k-1)} + \Theta^{(k)} - Z^{(k)} \\\\
>\end{align}
>$$
여기서 $$FL_{\tau}^{1d}(a)$$는 1d fused lasso이고,  $$FL_{\tau}^{1d}(a) = \underset{x}{\operatorname{argmin}}\frac{1}{2}||a-x||^{2}_{2}+\tau\sum_{i=1}^{d-1}|x_{i}-x_{i+1}|$$ 이다.
 matrix 형태의 ADMM also, $$O(n)$$의 시간복잡도to, operation을 수행할 수 있다. $$\Theta, Z$$ 둘 다 1d fused lasso의 형태이고, 이는 $$O(n)$$의 시간복잡도를 가진다. 
 [Fig 2]는 기존의 penalty 항을 1d fused lasso problemto, 어떻게 분리되는가를 showing,준다.
 
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter21/2dfussedlasso.png" alt="[Fig 2]  Interpretation of the matrix form ADMM updates for 2d fused lasso[3]" width="70%">
  <figcaption style="text-align: center;">[Fig 2]  Interpretation of the matrix form ADMM updates for 2d fused lasso[3]</figcaption>
</p>
</figure>


## Image denoising experiments
이제 1장at, 살펴보았던 image denoising problem를 다시 살펴본다.
[Fig 3]는 dataand, denoised된 image를 showing,준다. [Fig 4]는 두 ADMM methodto, about, 비교를 showing,준다. vertical/horizontal directionwith, decompose하여 constraint를 정의하는 matrix form인 "specialized" ADMM은 vector format, 유도한 "standard ADMM"보다 훨씬 빠른 convergence 성능을 showing,준다.
[Fig 5]는 ADMM의 iterationto, 따른 image quality를 showing,준다.

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

---
layout: post
title: 20-02-01 Dual Decomposition with Equality Constraint
chapter: '20'
order: 5
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

다음의 problem를 보자. 
>\begin{equation}
\min_x \sum_{i=1}^B f_i(x_i) \quad \text{ subject to } \quad Ax = b
\end{equation}

if,, variable $$x$$를 $$B$$개의 블록with, 분할하고, $$x = (x_1,\dots,x_B) \in \mathbb{R}^n, \text{ where } x_i \in \mathbb{R}^{n_i}$$, matrix $$A$$ 역시 $$B$$개의 sub-matrix 블록with, as follows: 분할하면, $$A = [A_1, \dots, A_B], \text{ where } A_i \in \mathbb{R}^{m \times n_i}$$, 위 minimization problem는 as follows: $$B$$개의 분리된 problemto, 분solution될 수 있다.  
> $$
> \begin{alignat}{1}
> & \quad x^+ \in \arg\min_x \sum_{i=1}^B f_i(x_i) + u^T Ax  \\
> \Longleftrightarrow & \quad x_i^+ \in \arg\min_{x_i} f_i(x_i) + u^T A_ix_i, \quad i=1,\dots, B
> \end{alignat}
> $$

### Dual decomposition algorithm: 

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right)
> \end{alignat}
> $$

위 두 step는 아래and, 같이 solution석할 수 있다. 
>* 첫번째 수식은 broadcast stepto,서, $$B$$개의 프to,세서의 각각to,게 $$u$$를 보낸다. and,, 프to,세서 각각은 병렬to, 자신의 최적 $$x_i$$를 찾는다.   
* 두번째 수식은 gather stepto,서, 각 프to,세서from, $$A_i x_i$$를 모은다. and, global dual variable $$u$$를 업데이트 한다. 

위 두 step는 $$k=1,2,3,\dots$$about, 계속 iteration한다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter20/decomposition.png" alt="[Fig 1] Broadcast and Gather" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Broadcast and Gather</figcaption>
</p>
</figure>

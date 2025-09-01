---
layout: post
title: 07-02-01 Connection to a Convexity Geometry
chapter: '07'
order: 4
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---



For a convex set $$C \subseteq \mathbb{R}^n$$, consider the indicator function $$I_C: \mathbb{R}^n \to \mathbb{R}$$ defined as:

>
$$
I_C(x) = I\{x \in C \} =
\begin{cases}
0               &\text{if } x \in C \\
\infty         &\text{if } x \notin C 
\end{cases}
$$

The subdifferential of this function has the following geometric meaning:

#### Lemma
For $$x \in C$$, the subdifferential $$\partial I_C(x)$$ coincides with the normal cone $$\mathcal{N}_C(x)$$ to the set $$C$$ at $$x$$:

>
\begin{equation}
\mathcal{N}_C(x) = \{g \in \mathbb{R}^n | g^Tx \geq g^Ty \text{  for all  } y \in C \}
\end{equation}

#### Proof

By definition, the subgradient must satisfy:
>
\begin{equation}
I_C(y) \geq I_C(x) + g^T(y-x) \text{ for all } y
\end{equation}

Here, $$x \in C$$ and $$I_C(x)=0$$, so:
>
\begin{equation}
I_C(y) \geq g^T(y-x) \text{ for all } y
\end{equation}

First, for all $$y \in C$$, we have:
>
\begin{equation}
I_C(y) = 0 \geq g^T(y-x)
\end{equation}

Thus, the subgradient $$g$$ must satisfy $$g^Tx \geq g^Ty$$.

Second, for all $$y \notin C$$, $$I_C(y) = \infty$$, so the inequality holds for any value of $$g$$:
>
$$I_C(y)=\infty \geq g^T(y-x)$$

which is always true.

위 두 조건에 대해, subgradient는 모두 만족시켜야 하므로, 위 함수에 대한 subgradient는 
>
$$\{g \in \mathbb{R}^n | g^Tx \geq g^Ty\}$$

가 된다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_02_subgrad-5.png" alt="connection_to_convexity_geometry" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Fig 1] Normal cone [1]</figcaption>
</figure>
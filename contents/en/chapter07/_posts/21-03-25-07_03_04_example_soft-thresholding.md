---
layout: post
title: '07-03-04 Example: Soft-Thresholding'
chapter: '07'
order: 10
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---


For the simpler lasso problem with $$X=I$$:
>
\begin{equation}
\min_{\beta} \frac{1}{2} \| y-\beta \|_2^2 + \lambda \| \beta \|_1
\end{equation}

From the previous example, the subgradient optimality condition is:
>
$$
\begin{cases}
y_i-\beta_i = \lambda \cdot \text{sign}(\beta_i) &\text{if } \beta_i \neq 0 \\
 |y_i-\beta_i| \leq \lambda &\text{if } \beta_i = 0
\end{cases}
$$

From this condition, the solution $$\beta = S_{\lambda}(y)$$ can be found, where
>
$$
[S_{\lambda}(y)]_{i} = 
\begin{cases}
y_i - \lambda &\text{if }y_i > \lambda \\
0             &\text{if }-\lambda \leq y_i \leq \lambda, \quad \quad i \in \{1,2,\dots,n \} \\
y_i + \lambda &\text{if } y_i < -\lambda
\end{cases}
$$

Here, $$S_{\lambda}$$ is called the soft-thresholding operator.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_03_subgrad-6.png" alt="connection_to_convexity_geometry" width="80%" height="80%">
</p>
 <figcaption style="text-align: center;">$$\text{[Fig 1] Soft-thresholding, y (x-axis), } \beta \text{ (y-axis), } \lambda=1/2 \text{ [3]}$$ </figcaption>
</figure>
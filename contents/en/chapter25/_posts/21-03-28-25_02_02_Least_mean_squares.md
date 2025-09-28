---
layout: post
title: 25-02-02 Least mean squares
chapter: '25'
order: 9
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

So far, we have solved regression problems by minimizing the $$l_2$$ norm or $$l_1$$ norm of residuals. Is there a more robust method than these methods?

When performing regression to minimize the median of residuals, we can achieve more robust regression. This is called **Least Median of Squares**, and it is robust enough that the estimator does not get corrupted even if about 50% of the data is corrupted. However, this problem is also an NP-Hard problem!

This section introduces how to solve the **Least Quantile of Squares** problem, which generalizes the Least Median of Squares problem, using Integer programming.
## Least mean squares
Let $$X = [x^{1} \quad \dotsc \quad x^{p}] \in \mathbb{R}^{n×p}$$ and $$y \in \mathbb{R}^{n}$$. And when $$\beta \in \mathbb{R}^{p}$$, let $$r : = y - X\beta$$.

### Observe
* Least squares (LS) : $$\beta_{LS} : = \underset{\beta}{\text{argmin}} \sum_{i} r^2_i$$
* Least absolute deviation (LAD) : $$\beta_{LAD} : = \underset{\beta}{\text{argmin}} \sum_{i} \lvert r_{i} \rvert$$
### Least Median of Squares (LMS)
>$$\beta_{LMS} : = \underset{\beta}{\text{argmin}} (\text{median} \lvert r_{i} \rvert )$$

## Least quantile regression
The Least Quantile of Squares problem, which generalizes the Least Median of Squares problem, can be defined as follows. Here $$r_{q}$$ is the $$q$$-th ordered absolute residual.
### Least Quantile of Squares (LQS)
>$$\beta_{LQS} : = \underset{\beta}{\text{argmin}} (\lvert r_{(q)} \rvert ), \quad 1 \le q \le n, \quad \lvert r_{1} \rvert \le \lvert r_{2} \rvert \le \cdots \le \lvert r_{n} \rvert$$

### Key step in the formulation
Now let's reformulate the Least Quantile of Squares problem as Integer Programming. Here, for each entry $$i$$ of $$r$$, we use the following binary variables.

>$$ \lvert r_{i} \rvert \le \lvert r_{(q)} \rvert$ or $\lvert r_{i} \rvert \ge \lvert r_{(q)} \rvert $$

### Integer programming formulation
$$\bar{\mu_{i}}$$ and $$\mu_{i}$$ are thresholds, with $$k$$ and $$n-k$$ of each respectively.

> $$
> \begin{align}
>   \min_{\beta, \mu, \bar{\mu}, z, \gamma} & \quad {\gamma} \\
>   \text{subject to} & \quad  \gamma \le \lvert r_{i} \rvert + \bar{\mu_{i}}, \quad i = 1, ..., n \\
>   & \quad  \gamma \le \lvert r_{i} \rvert -  \mu_{i}, \quad i = 1, ..., n \\
>   & \quad \bar{\mu_{i}} \le M \cdot z_{i}, \quad i = 1, ..., n \\
>   & \quad \mu_{i} \le M \cdot (1-z_{i}), \quad i = 1, ..., n \\
>   & \quad \sum^{p}_{i=1} z_{i} = q \\
>   & \quad \mu_{i}, \bar{\mu_{i}} \ge 0, \quad i = 1, ..., n \\
>   & \quad z_{i} \in \{0, 1\},  \quad i = 1, ..., n \\
> \end{align}
> $$

Looking at the first and second constraints of this problem, the absolute value of residuals $$\lvert r_{i} \rvert$$ is included, so it cannot be solved with convex relaxation. Therefore, the first and second constraints must be converted to convex functions.


## First-order algorithm
$$\lvert r_{i} \rvert$$ can be redefined as a convex function $$H_{q}(\beta)$$ in the following form.
>
$$ \lvert r_{q} \rvert = \lvert y_{(q)} - x^{T}_{(q)} \beta \rvert = H_{q}(\beta) - H_{q+1}(\beta)$$

Here, $$H_{q}(\beta)$$ is defined as follows.

> $$
> \begin{align}
> H_{q}(\beta) = \sum^{n}_{i=q} \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert  = &
> \max_{w} \sum^{n}_{i=1} w_i \lvert y_{(i)} - x^{T}_{(i)} \beta \rvert \\
> & \text{subject to} \sum^{n}_{i=1}  w_i  = n − q + 1 \\
> &0 \le w_i \le 1, i = 1, ..., n \\
> \end{align}
> $$

$$H_{q}(\beta)$$ is the sum of all residuals from the $$q$$-th position when the previously defined $$\lvert r_{i} \rvert$$ are arranged in ascending order. Therefore, we can see that subtracting the sum of residuals from the $$q+1$$-th position from the sum of residuals from the $$q$$-th position gives the $$q$$-th residual.

Using the subgradient algorithm, we can find the local minimum of $$H_{q}(\beta) - H_{q+1}(\beta)$$.

* For detailed information, see the paper [LEAST QUANTILE REGRESSION VIA MODERN OPTIMIZATION](https://arxiv.org/pdf/1310.8625.pdf)
## Computational results
The experimental results of the Least Quantile of Squares problem from the above paper can be seen in the following graphs.

### Mixed integer programming gap
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_06_LQS_results1.png" alt="[Fig1] Mixed integer programming gap [3]">
  <figcaption style="text-align: center;">[Fig1] Mixed integer programming gap [3]</figcaption>
</p>
</figure>
<br>

### Cold vs Warm Starts
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_07_LQS_results2.png" alt="[Fig2] Cold vs Warm Starts [3]">
  <figcaption style="text-align: center;">[Fig2] Cold vs Warm Starts [3]</figcaption>
</p>
</figure>
<br>

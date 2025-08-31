---
layout: post
title: 05-02 Quadratic Programming (QP)
chapter: "05"
order: 3
owner: "Hooncheol Shin"
---

A *Quadratic Program* (QP) is a convex optimization problem where the objective function is a convex quadratic and all constraint functions are affine. The general quadratic program is formulated as:

### Quadratic Program
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P \in \mathbb{S}_{+}^n, G \in \mathbb{R}^{m \times n}, \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

* The constant $$+ r$$ in the objective function does not affect the optimization process or result and can be omitted.
* If $$P \in \mathbb{S}_{+}^n$$ is not satisfied, the problem is not convex.
* Even if not explicitly stated, QP assumes $$P \in \mathbb{S}_{+}^n$$.
* The above problem seeks the minimizer $$x^*$$ of the convex quadratic function $$(1/2)x^T P x + q^T x + r$$ over a polyhedral feasible set.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_02_geometric_interpretation_of_QP.png" alt="[Fig 1] Geometric interpretation of QP [1]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Geometric interpretation of QP [1]</figcaption>
</p>
</figure>

## QP in Standard form
The standard form of a quadratic program is:

### Standard form QP
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{A x = b} \\\\
>    & &&{x \succeq 0}.
>\end{align}
>$$

Any general quadratic program can be converted to standard form using the following steps:

### Converting QPs to standard form
**Step 1.** Use slack variables $$s$$ to convert inequality constraints into equality constraints:
> $$
> \begin{align}
>     &\text{minimize}_{x, s} &&{(1/2)x^T P x + q^T x + r} \\\\
>     &\text{subject to } &&{Gx + s = h} \\\\
>     & &&{Ax = b},\\\\
>     & &&{s \succeq 0}.
> \end{align}
> $$

**Step 2.** Replace $$x$$ with two nonnegative variables:
$$x = x^{+}  - x^{-}$$, where $$x^{+} \text{ and } x^{-} \succeq 0.$$

> $$
> \begin{align}
>     &\text{minimize}_{x^{+}, x^{-}, s} &&{(1/2)(x^{+} - x^{-})^T P (x^{+} - x^{-}) + q^T x^{+} - q^T x^{-} + r}\\\\
>     &\text{subject to } &&{Gx^{+} - Gx^{-} + s = h} \\\\
>     & &&{Ax^{+} - Ax^{-} = b},\\\\
>     & &&{s \succeq 0}\\\\
>     & &&{x^{+} \succeq 0}, {x^{-} \succeq 0}.
> \end{align}
> $$

**Step 3.** Define 
$$\tilde{x} $$,
$$\tilde{q} $$, 
$$\tilde{b} $$,
$$\tilde{A} $$, 
$$\tilde{P} $$:

> $$
> \tilde{x} =
> \begin{bmatrix}
> x^{+} \\\\
> x^{-} \\\\
> s
> \end{bmatrix},
> \tilde{q} =
> \begin{bmatrix}
> q \\\\
> -q \\\\
> 0
> \end{bmatrix},
> \tilde{b} =
> \begin{bmatrix}
> h \\\\
> b
> \end{bmatrix},
> \tilde{A} =
> \begin{bmatrix}
> G & -G & I \\\\
> A & -A & O
> \end{bmatrix},
> \tilde{P} =
> \begin{bmatrix}
>  P & -P & O \\\\
> -P &  P & O \\\\
>  O &  O & O \\\\
> \end{bmatrix}
> $$

**Step 4.** Substitute the expressions from Step 2 into the formulations with 
$$\tilde{x}, \tilde{q}, \tilde{b}, \tilde{A}, \tilde{P}$$:

>$$
>\begin{align}
>    &\text{minimize}_{\tilde{x}} &&{(1/2)\tilde{x}^T \tilde{P} \tilde{x} + \tilde{q}^T \tilde{x} + r} \\\\
>    &\text{subject to } &&{\tilde{A} \tilde{x} = \tilde{b}} \\\\
>    & &&{\tilde{x} \succeq 0}.
>\end{align}
>$$

## LP and equivalent QP
If the quadratic term is removed from the objective function of a quadratic program, it takes the form of a linear program. Thus, LP is a special case of QP, denoted as LP $$ \subseteq $$ QP.

### Recall: General LP
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&G \in \mathbb{R}^{\text{m x n}} \text{ and } A \in \mathbb{R}^{\text{p x n}}.
>\end{align}\\
>$$

### Example 1) Portfolio optimization
This problem involves appropriately trading off performance and risk in creating a financial portfolio. 

>$$
>\begin{align}
>    &\text{maximize}_{x} &&{\mu^T x - \frac{\gamma}{2}x^T P x} \\\\
>    &\text{subject to } &&{1^Tx = 1} \\\\
>    & &&{x \succeq 0}.
>\end{align}
>$$

* $$\mu$$: expected assets' returns.
* $$P$$: covariance matrix of assets' returns.
* $$gamma$$: risk aversion (hyper-parameter).
* $$x$$: portfolio holdings (percentages).

$$\mu$$와 $$P$$는 과거의 데이터를 통해서 얻을 수 있으며, 각 종목에 $$x$$만큼 투자했을 때 그 평균을 $$\mu^T x$$, 분산을 $$x^T P x$$로 표현할 수 있다.

### Example 2)  Support vector machines
[Support vector machines(이하 SVM)](https://ratsgo.github.io/machine%20learning/2017/05/23/SVM/)은 quadratic program의 한 예에 해당한다. 아래는 SVM의 변형인 [C-SVM](https://ratsgo.github.io/machine%20learning/2017/05/29/SVM2/)이다. SVM에 대한 자세한 설명은 본 장의 주제에서 벗어나므로 여기서는 생략하도록 한다.

>$$
>\begin{align}
>    &\text{minimize}_{\beta, \beta_0, \xi} &&{\frac{1}{2} \| \beta \|_2^2 + C \sum_{i=1}^{n} \xi_i} \\
>    &\text{subject to } &&{\xi_i \geq 0, i = 1, \dotsc, n} \\
>    & &&{y_i (x_i^T \beta + \beta_0) \geq 1 - \xi_i, i = 1, \dotsc, n},\\
>    & \text{given} && \text{y} \in \left\{-1, 1\right\}^n, X \in \mathbb{R}^{\text{n x p}} \text{ having rows } x_1, \dotsc, x_n.
>\end{align}\\
>$$

### Example 3)  Least-squares in regression
다음과 같은 convex quadratic function을 최소화하는 문제는 (unconstrained) QP에 해당한다.
> $$\| Ax - b \|_2^2 = x^T A^TA x - 2b^TAx + b^Tb$$

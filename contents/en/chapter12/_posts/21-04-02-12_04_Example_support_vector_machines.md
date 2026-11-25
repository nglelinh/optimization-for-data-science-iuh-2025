---
layout: post
title: 12-04 Example support vector machines
chapter: '12'
order: 5
owner: Wontak Ryu
categories:
- chapter12
lang: en
lesson_type: required
---

Why are Support Vector Machines named after *support vectors*—and how can a classifier trained on 100,000 data points depend on just a tiny handful of critical boundary examples? The answer is pure KKT complementary slackness! Writing down the KKT system for the soft-margin SVM QP reveals in four lines why $$\beta^\star = \sum_{i=1}^n w_i^\star y_i x_i$$ is a sparse linear combination of training points, why points safely outside the margin have $$w_i^\star = 0$$, and how margin points pin down the intercept $$\beta_0^\star$$!

## Key ideas: Reading SVM Geometry Directly from KKT

- **Pillar 1 — Stationarity Produces the Representer Formula:** Differentiating the soft-margin SVM Lagrangian with respect to $$\beta, \beta_0, \xi_i$$ gives three gold-mine equations: $$\beta^\star = \sum_{i=1}^n w_i^\star y_i x_i$$, $$\sum_{i=1}^n w_i^\star y_i = 0$$, and $$w_i^\star + v_i^\star = C$$ (hence $$0 \le w_i^\star \le C$$).
- **Pillar 2 — Complementary Slackness Partitions All Data into 3 Regimes:**
  - *Strictly outside the margin* ($$y_i(x_i^\top \beta^\star + \beta_0^\star) > 1$$): forces $$w_i^\star = 0$$ and $$\xi_i^\star = 0$$ (ignored completely by the classifier!).
  - *On the margin boundary* ($$y_i(x_i^\top \beta^\star + \beta_0^\star) = 1,\; \xi_i^\star = 0$$): allows $$0 < w_i^\star < C$$ (**free support vectors**!).
  - *Inside/violating the margin* ($$\xi_i^\star > 0$$): forces $$v_i^\star = 0 \implies w_i^\star = C$$ (**bounded support vectors**!).
- **Pillar 3 — Recovering the Intercept $$\beta_0^\star$$:** Any free support vector ($$0 < w_i^\star < C$$) has $$\xi_i^\star = 0$$ and tight margin $$y_i(x_i^\top \beta^\star + \beta_0^\star) = 1$$, immediately giving $$\beta_0^\star = y_i - x_i^\top \beta^\star$$.
- **Pillar 4 — Dual Sparsity & Computational Payoff:** Because non-support vectors drop out of $$\beta^\star$$ completely, removing them from the training set does *not* change the optimal hyperplane by a single millimeter!

### Worked example: Identifying Support Vectors & Multipliers on a 3-Point 1D Dataset

Consider 3 labeled 1D training points with $$C = 2$$:
$$(x_1, y_1) = (-2, -1), \quad (x_2, y_2) = (0, -1), \quad (x_3, y_3) = (2, +1).$$

1. **Find the maximum-margin linear separator by geometry:**
   The negative points sit at $$x \le 0$$ and the positive point sits at $$x = 2$$, so the midpoint is $$x = 1$$ with half-margin $$1$$: $$\beta^\star = 1,\; \beta_0^\star = -1$$ (decision function $$f(x) = x - 1$$).
2. **Check functional margins $$y_i(\beta^\star x_i + \beta_0^\star)$$ and slacks $$\xi_i^\star$$:**
   - Point 1 ($$x_1 = -2, y_1 = -1$$): $$(-1)(-2 - 1) = +3 > 1$$ (strictly outside margin $$\implies \xi_1^\star = 0,\; w_1^\star = 0$$!).
   - Point 2 ($$x_2 = 0, y_2 = -1$$): $$(-1)(0 - 1) = +1$$ (on the margin $$\implies \xi_2^\star = 0$$, free support vector!).
   - Point 3 ($$x_3 = 2, y_3 = +1$$): $$(+1)(2 - 1) = +1$$ (on the margin $$\implies \xi_3^\star = 0$$, free support vector!).
3. **Solve for the KKT multipliers $$w_2^\star, w_3^\star$$ via stationarity:**
   - $$\sum w_i^\star y_i = -w_2^\star + w_3^\star = 0 \implies w_2^\star = w_3^\star$$.
   - $$\beta^\star = \sum w_i^\star y_i x_i = w_2^\star(-1)(0) + w_3^\star(+1)(2) = 2w_3^\star = 1 \implies w_3^\star = 0.5,\; w_2^\star = 0.5$$.
   - Dual feasibility check: $$0 \le w_i^\star = 0.5 < C = 2$$ and $$v_i^\star = C - w_i^\star = 1.5 > 0$$!
4. **Takeaway:** Point 1 ($$w_1^\star = 0$$) is completely irrelevant, while Points 2 and 3 ($$w_2^\star = w_3^\star = 0.5$$) are the exact support vectors holding the hyperplane in place!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

The support vector machine problem for non-separable sets is as follows.

>$$
>\begin{align}
>    &\min_{\beta, \beta-0, \xi} &&{\frac{1}{2} \rVert\beta\rVert_2^2 + C\sum_{i=1}^n \xi_i} \\\\
>    &\text{subject to} &&{\xi_i \ge 0, \quad i = 1, \dots, n}\\\\
>    & && y_i (x_i^T \beta + \beta-0) \ge 1 - \xi_i, \quad i = 1, \dots, n,\\\\
>&&&\text{given } y \in \{-1, 1\}^n \text{ and } X \in \mathbb{R}^{n \times p}.
>\end{align}
>$$

When the Lagrange multipliers for the two inequality constraints of the given problem are $$v^\star, w^\star \geq 0$$ respectively, the Lagrangian function is as follows.
>$$L(\beta, \beta-0, \xi, v^\star, w^\star) = \frac{1}{2} \rVert\beta\rVert_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i^\star \xi_i + \sum_{i=1}^n w_i^\star (1 - \xi_i - y_i ( x_i^T \beta + \beta_0))$$

Using the above Lagrangian function, we can find the following conditions that make this problem satisfy the KKT stationarity condition. (Derive the conditions where the Lagrangian function becomes 0 when differentiated with respect to $$\beta, \beta_0, \xi$$ respectively)
>$$
>0 = \sum_{i=1}^n w_i^\star y_i, \quad \beta = \sum_{i=1}^n w_i^\star y_i x_i, \quad w^\star = C \cdot 1 - v^\star
>$$

Also, complementary slackness for the two inequality constraints is as follows.
> $$
> v_i^\star \xi_i = 0, \quad w_i^\star (1 - \xi_i - y_i (x_i^T \beta + \beta-0)) =0, \quad 1 = 1, \dots, n.
> $$

That is, at optimality, $$\beta^\star = \sum_{i=1}^n w_i^\star y_i x_i$$ is satisfied, and when $$y_i (x_i^T \beta^\star + \beta-0^\star) = 1 - \xi_i^\star$$, $$w_i^\star$$ becomes nonzero, and such point i is called **support points**.

* For a support point i where $$\xi_i^\star = 0$$, $$x_i$$ is located on the hyperplane and $$w_i^\star \in (0, C]$$.
* For a support point i where $$\xi_i^\star \neq 0$$, $$x_i$$ is located on the opposite side of the hyperplane and $$w_i^\star = C$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/svm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$ \text{[Fig1] Illustration of support points with }\ \xi^\star \neq 0 \text{ [3]}$$ </figcaption>
</p>
</figure>

Before optimizing the SVM problem, the above method can be used to filter out non-support points (filtering out non-support points can improve computational efficiency). In fact, KKT conditions do not play a direct role in deriving the solution to this problem, but we can gain intuition to better understand the SVM problem through them [3].

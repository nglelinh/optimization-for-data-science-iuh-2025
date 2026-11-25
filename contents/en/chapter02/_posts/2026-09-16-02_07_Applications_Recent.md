---
layout: post
title: 02-07 Applications and recent developments
chapter: '02'
order: 17
owner: Nguyen Le Linh
categories:
- chapter02
lang: en
lesson_type: optional
---

Convex sets are not abstract museum pieces—they sit right inside the output layer of every large language model (the probability simplex), inside distributionally robust optimization against data shift (Wasserstein balls), and inside ethical AI systems (fairness polytopes). Whenever a modern ML architecture averages distributions, enforces a robustness radius, or balances competing group metrics, it is exploiting the exact Chapter 02 geometry of convex sets.

## Background Knowledge Map: Modern ML Geometry Through Chapter 02

- **Probability Simplex & Softmax:** The softmax map $$\text{softmax}(z)_i = e^{z_i} / \sum_j e^{z_j}$$ maps unconstrained neural network logits $$z \in \mathbb{R}^K$$ smoothly into the relative interior of the probability simplex $$\Delta_K$$.
- **Wasserstein Ambiguity Balls:** Distributionally robust optimization (DRO) protects models against distribution shift by hedging over a convex ball of probability distributions centered at the empirical data.
- **Fairness & Resource Polytopes:** Group fairness constraints (demographic parity, equal opportunity) carve a convex polytope out of the space of randomized classifiers, allowing exact feasibility analysis via linear programming.
- **Geometry Drives Tractability:** Whenever an ML constraint forms a convex set with an efficient projection or separation oracle, we can enforce it provably during training.

### Step-by-Step Worked Example (Read Slowly): Mapping Logits onto the Probability Simplex via Softmax

Given a 3-class classifier's raw logit vector $$z = (2, 1, 0)^T$$:

1. **Exponentiate each logit:**
   $$e^2 \approx 7.389, \qquad e^1 \approx 2.718, \qquad e^0 = 1.000.$$
2. **Normalize to land inside the relative interior of $$\Delta_3$$:**
   $$Z = 7.389 + 2.718 + 1.000 = 11.107,$$
   $$p = \text{softmax}(z) = \left(\frac{7.389}{11.107},\; \frac{2.718}{11.107},\; \frac{1.000}{11.107}\right)^T \approx (0.665,\; 0.245,\; 0.090)^T.$$
   Check simplex membership: every entry is strictly positive and $$0.665 + 0.245 + 0.090 = 1.000$$.
3. **Verify shift invariance (numerical stability trick):** Subtracting $$\max_i z_i = 2$$ gives $$z' = (0, -1, -2)^T$$ with $$e^{z'} = (1, 0.368, 0.135)^T$$ and sum $$1.503$$, producing the identical simplex point $$(0.665, 0.245, 0.090)^T$$ without risk of floating-point overflow.

A convex set is a feasible region you can *average inside*. That geometric fact is why so many modern machine-learning constraints look like simplices, balls, or spectrahedra. This lesson names three families of convex sets that appear in 2022–2025 papers and libraries, each tied to a definition you already have: the probability simplex, a Wasserstein ball of distributions, and a polyhedron cut by fairness (or budget) inequalities.

## The probability simplex, softmax, and last-layer geometry

The standard simplex

$$
\Delta^{n-1} = \bigl\{ p\in\mathbb{R}^n : p\ge 0,\; \mathbf{1}^\top p = 1\bigr\}
$$

is convex (it is the intersection of a hyperplane with the nonnegative orthant). Softmax is a smooth map *onto* the relative interior of $$\Delta^{n-1}$$. Every attention head in a Transformer, and every multiclass logistic model, therefore spends its last nonlinearity projecting a vector of logits onto a convex set you can draw in $$\mathbb{R}^2$$ and $$\mathbb{R}^3$$.

A more surprising simplex appears at the *end* of training. Papyan, Han, and Donoho (*Prevalence of neural collapse*, [PNAS 2020](https://www.pnas.org/doi/10.1073/pnas.2015509117); [arXiv:2008.08186](https://arxiv.org/abs/2008.08186)) measured a *simplex equiangular tight frame* (ETF) among last-layer class means: the centered means form the most symmetric point configuration on a sphere. Zhu, Ding, Zhou, et al. (*A Geometric Analysis of Neural Collapse with Unconstrained Features*, [NeurIPS 2021](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)) later showed that, in a simplified unconstrained-feature model with cross-entropy and weight decay, those ETF configurations are the global minimizers and every other critical point is a strict saddle. The convex-set language is not decorative: the ETF is a concrete subset of a sphere, and the probability simplex is the set the classifier actually outputs.

When you check “is $$C$$ convex?” on a homework set, include $$\Delta^{n-1}$$ and a Euclidean ball. Those two sets are the geometry of classification and of many regularizers.

## Wasserstein balls as ambiguity sets

Distributionally robust optimization (DRO) replaces a single training distribution $$\hat{P}$$ by a *set* of distributions, and optimizes against the worst member of that set. The Wasserstein ball

$$
\mathcal{B}_\varepsilon(\hat{P}) = \bigl\{ Q : W_p(Q,\hat{P}) \le \varepsilon\bigr\}
$$

is a convex set in the space of probability measures (an optimal-transport ball). Decisions that survive the worst $$Q\in\mathcal{B}_\varepsilon(\hat{P})$$ often admit convex finite-dimensional reformulations.

Two references you can actually open: Gao and Kleywegt, “Distributionally Robust Stochastic Optimization with Wasserstein Distance,” [*Mathematics of Operations Research* 48(2):603–655, 2023](https://doi.org/10.1287/moor.2022.1275), prove a strong duality result for Wasserstein DRO and describe the structure of worst-case distributions. Kuhn, Mohajerin Esfahani, Nguyen, and Shafieezadeh-Abadeh’s tutorial *Wasserstein Distributionally Robust Optimization* ([INFORMS TutORials 2019](https://doi.org/10.1287/educ.2019.0198); [arXiv:1908.08729](https://arxiv.org/abs/1908.08729), revised November 2024) is the readable companion and explicitly connects the ball to classification, regression, and MLE. A broader 2025 survey in *Acta Numerica* ([Kuhn, Shafiee, et al.](https://www.cambridge.org/core/journals/acta-numerica/article/distributionally-robust-optimization/5B4E65E3A5A2AEF24E218A6B34E6EAA2)) places Wasserstein balls next to other ambiguity sets.

The modeling move is the same as “replace a point estimate by a convex uncertainty set” in robust linear programming, except the “points” are distributions. If you can certify that $$\mathcal{B}_\varepsilon(\hat{P})$$ is convex and that the inner worst-case map is convex in the decision, the outer DRO program is a convex optimization problem of the kind Chapter 04 will formalize.

## Fairness and resource polytopes

Linear inequalities in probabilities define polyhedra. Demographic-parity style constraints of the form

$$
\bigl| \mathbb{E}[h(X)\mid A=a] - \mathbb{E}[h(X)\mid A=a'] \bigr| \le \epsilon
$$

cut a polytope in the space of (randomized) classifiers. Agarwal, Beygelzimer, Dudík, Langford, and Wallach ([ICML 2018](https://proceedings.mlr.press/v80/agarwal18a.html)) treat those cuts as the feasible set of a reduction; [Fairlearn](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html) still exposes them as `Moment` objects in 2025–2026.

The same picture covers budget and allocation constraints: $$x\ge 0$$, $$\mathbf{1}^\top x = 1$$ (a portfolio on the simplex), or $$0\le x\le 1$$, $$Ax\le b$$ (a knapsack-type media-mix polytope). Separating hyperplanes from later in this chapter are exactly the certificates that a candidate $$x$$ is outside such a polytope — the same certificates a solver uses when it returns an infeasible status.

## A two-line picture to keep

Every modern constraint in this lesson is an intersection of convex pieces you can name:

$$
\mathcal{C} = \Delta^{n-1} \cap \{ x : Fx \le g \} \qquad\text{or}\qquad \mathcal{B}_\varepsilon(\hat{P}).
$$

If you can prove each piece is convex, the intersection is convex, and every local search that stays in $$\mathcal{C}$$ is searching a set without “holes.” That is the entire reason Chapter 02 exists, restated in the language of attention, DRO, and fairness.

## Sources

1. V. Papyan, X. Y. Han, and D. L. Donoho, “Prevalence of neural collapse during the terminal phase of deep learning training,” *PNAS* 117(40):24652–24663, 2020. [DOI](https://www.pnas.org/doi/10.1073/pnas.2015509117) · [arXiv:2008.08186](https://arxiv.org/abs/2008.08186)
2. Z. Zhu, T. Ding, J. Zhou, et al., “A Geometric Analysis of Neural Collapse with Unconstrained Features,” NeurIPS 2021. [abstract](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)
3. R. Gao and A. J. Kleywegt, “Distributionally Robust Stochastic Optimization with Wasserstein Distance,” *Math. Oper. Res.* 48(2):603–655, 2023. [DOI](https://doi.org/10.1287/moor.2022.1275)
4. D. Kuhn, P. Mohajerin Esfahani, V. A. Nguyen, and S. Shafieezadeh-Abadeh, “Wasserstein Distributionally Robust Optimization,” INFORMS TutORials 2019; arXiv:1908.08729 (rev. 2024). [arXiv](https://arxiv.org/abs/1908.08729)
5. A. Agarwal et al., “A Reductions Approach to Fair Classification,” ICML 2018. [PMLR](https://proceedings.mlr.press/v80/agarwal18a.html) · [Fairlearn](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html)
